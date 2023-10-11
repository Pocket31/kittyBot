import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton


from TOKEN import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        KeyboardButton(text="Товары"),
        KeyboardButton(text="Баланс"),
        KeyboardButton(text="FAQ"),
    )
    keyboard.row(
        KeyboardButton(text="Кабинет"),
        KeyboardButton(text="Поддержка"),
    )
    await message.reply("Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

inline_kb = InlineKeyboardMarkup(row_width=2)
email_highButton = InlineKeyboardButton(
    text='Почты HIGH репутация', callback_data='lol')
inline_kb.add(email_highButton)


@dp.message_handler(text='Товары')
async def category_items(message: types.Message):

    await message.reply("Выберите категорию:", reply_markup=inline_kb)

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
