import asyncio
from aiogram import Dispatcher, Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F

from walet.CreateWallet import create_wallet_usdt_trc_20
from walet.Balance import check_balance_usdt_trc_20
from walet.SendTransaction import send_transaction
from walet.CheckTranzStatus import check_tranzaktion
from googledrive.GD import check_product
from TOKEN import TELEGRAM_TOKEN

import sqlite3


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

user_id = None


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    cursor.execute(f"SELECT * FROM users WHERE user_id={user_id}")
    user = cursor.fetchone()

    if user:
        pass
    else:
        # Добавляем запись о пользователе в базу данных
        cursor.execute(
            f"INSERT INTO users (user_id, registered_date) VALUES ({user_id}, '{message.date}')")
        conn.commit()

    builder = ReplyKeyboardBuilder()

    builder.row(
        types.KeyboardButton(text="Товары"),
        types.KeyboardButton(text="Баланс"),
        types.KeyboardButton(text="FAQ"),
    )
    builder.row(
        types.KeyboardButton(text="Кабинет"),
        types.KeyboardButton(text="Поддержка"),
    )

    await message.answer("Добро пожаловать! \nЗдесь ты можешь приобрести почты HIGH репутации.", reply_markup=builder.as_markup(), resize_keyboard=True)


builder = InlineKeyboardBuilder()
email_highButton = InlineKeyboardButton(
    text='Почты HIGH репутация', callback_data='email_high')
builder.add(email_highButton)

builder_trc_20 = InlineKeyboardBuilder()
trc_20_button = InlineKeyboardButton(
    text='USDT TRC-20', callback_data='usdt_trc_20')
builder_trc_20.add(trc_20_button)

builder_check_balance = InlineKeyboardBuilder()
check_balance_button = InlineKeyboardButton(
    text='Обновить баланс', callback_data='usdt_trc_20')
builder_check_balance.add(check_balance_button)

builder_buy = InlineKeyboardBuilder()
buy_button = InlineKeyboardButton(
    text='Купить', callback_data='buy')
builder_buy.add(buy_button)

builder_confirm = InlineKeyboardBuilder()
confirm_button = InlineKeyboardButton(
    text='Подтвердить', callback_data='confirm')
cancel_button = InlineKeyboardButton(
    text='Отменить', callback_data='email_high')
builder_confirm.add(confirm_button, cancel_button)


@dp.message(F.text == 'Товары')
async def category_items(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=builder.as_markup())


@dp.message(F.text == 'FAQ')
async def category_items(message: types.Message):
    await message.answer("✉️ Руководство и правила сервиса \n \nЗдесь будут правила\n \n Удачных покупок и приятного использования!")


@dp.message(F.text == 'Поддержка')
async def category_items(message: types.Message):
    await message.answer("Обращаться сюда: @ceftik")


@dp.message(F.text == 'Баланс')
async def balance(message: types.Message):
    await message.answer("Выберите сеть в которой хотите пополнить баланс:", reply_markup=builder_trc_20.as_markup())


@dp.message(F.text == 'Кабинет')
async def category_items(message: types.Message):
    cursor.execute(
        f"SELECT * FROM users WHERE user_id={message.from_user.id}")
    user_info = cursor.fetchone()
    await message.answer(f"Логин: @{message.from_user.username}\n \nДата Регистрации: {user_info[2][:11]}\n \nБаланс:")


@dp.callback_query(F.data == 'usdt_trc_20')
async def send_balance_usdt_trc_20(callback: types.CallbackQuery):
    cursor.execute(
        f"SELECT * FROM users WHERE user_id={callback.from_user.id}")
    user_info = cursor.fetchone()

    if user_info[3] == None:
        wallet = create_wallet_usdt_trc_20()
        cursor.execute(
            'UPDATE users SET trc_20_wallet_address = ?, trc_20_wallet_private_key = ? WHERE user_id = ?',
            (wallet['address'], wallet['key'], callback.from_user.id))
        wallet_address = wallet['address']
    else:
        wallet_address = user_info[3]

    conn.commit()

    balance = check_balance_usdt_trc_20(wallet_address)
    await callback.message.answer(f"Валюта получения: USDT TRC-20\nВаш баланс: {balance} USDT\nДля Вас сгенерирован кошелек:\n{wallet_address}\n \nДля пополнения своего баланса в боте, переведите нужную сумму на данный кошелек, и нажмите кнопку проверки платежа под этим сообщением.", reply_markup=builder_check_balance.as_markup())


@dp.callback_query(F.data == 'email_high')
async def email_high(callback: types.CallbackQuery):
    product_quantity = check_product()
    await callback.message.answer(f"Описание:\nЦена:\nКоличество: {product_quantity}", reply_markup=builder_buy.as_markup())


@dp.callback_query(F.data == 'buy')
async def buy(callback: types.CallbackQuery):
    if check_product() == 0:
        await callback.answer(text='На данный момент товар отсутсвует!', show_alert=True)
    else:
        await callback.message.answer(f'Для подтверждения покупки нажмите "Подтвердить"', reply_markup=builder_confirm.as_markup())


@dp.callback_query(F.data == 'confirm')
async def confirm_buy(callback: types.CallbackQuery):
    # product_quantity = check_product()
    cursor.execute(
        f"SELECT * FROM users WHERE user_id={callback.from_user.id}")
    user_info = cursor.fetchone()
    transaction = send_transaction(private_key=user_info[4], wallet_address_from=user_info[3],
                                   wallett_address_to='TChGkQpWkfKvADqfMKfJBf2cLsgiMDBFhk', amount=2000000)
    await callback.message.answer(f"Выполняется транзакция.\n id транзакции {transaction}.\n По окончанию выполнения транзакции Вам будет отправлен товар")
    await check_tranzaktion(tranzaction_id=transaction)
    await callback.message.answer("Товар")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
