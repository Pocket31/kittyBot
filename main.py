import asyncio
from aiogram import Dispatcher, Bot, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F

from TOKEN import TELEGRAM_TOKEN

import sqlite3


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    cursor.execute(f"SELECT * FROM users WHERE user_id={user_id}")
    user = cursor.fetchone()

    if user:
        pass
    else:
        # Генерируем уникальный идентификатор для сессии
        # session_id = str(uuid.uuid4())

        # Добавляем запись о пользователе в базу данных
        cursor.execute(
            f"INSERT INTO users (user_id, registered_date) VALUES ({user_id}, '{message.date}')")
        conn.commit()

    builder = ReplyKeyboardBuilder()
    # builder.add(types.KeyboardButton(text="Товары"))
    builder.row(
        types.KeyboardButton(text="Товары"),
        types.KeyboardButton(text="Баланс"),
        types.KeyboardButton(text="FAQ"),
    )
    builder.row(
        types.KeyboardButton(text="Кабинет"),
        types.KeyboardButton(text="Поддержка"),
    )
    # kb = [[
    #     types.KeyboardButton(text="Кабинет"),
    #     types.KeyboardButton(text="Поддержка"),
    # ]]
    # keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer("Добро пожаловать! \nЗдесь ты можешь приобрести почты HIGH репутации.", reply_markup=builder.as_markup(), resize_keyboard=True)


# @dp.message(CommandStart())
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

builder = InlineKeyboardBuilder()
email_highButton = InlineKeyboardButton(
    text='Почты HIGH репутация', callback_data='lol')
builder.add(email_highButton)


@dp.message(F.text == 'Товары')
async def category_items(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=builder.as_markup())


@dp.message(F.text == 'FAQ')
async def category_items(message: types.Message):
    await message.answer("✉️ Руководство и правила сервиса \n \nЗдесь будут правила\n \n Удачных покупок и приятного использования!")


@dp.message(F.text == 'Поддержка')
async def category_items(message: types.Message):
    await message.answer("Обращаться сюда: @ceftik")


@dp.message(F.text == 'Кабинет')
async def category_items(message: types.Message):
    cursor.execute(
        f"SELECT * FROM users WHERE user_id={message.from_user.id}")
    user_info = cursor.fetchone()
    await message.answer(f"Логин: @{message.from_user.username}\n \nДата Регистрации: {user_info[2][:11]}\n \nБаланс:")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
