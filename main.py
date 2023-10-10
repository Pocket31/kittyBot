import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from TOKEN import TELEGRAM_TOKEN


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# urlkb = InlineKeyboardMarkup(row_width=1)
# urlButton = InlineKeyboardButton(
#     text='Перейти в блог Skillbox', url='https://skillbox.ru/media/code/')
# urlButton2 = InlineKeyboardButton(
#     text='Перейти к курсам Skillbox', url='https://skillbox.ru/code/')
# urlkb.add(urlButton, urlButton2)


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Полезные ссылки:', reply_markup=urlkb)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            KeyboardButton(text="Товары"),
            KeyboardButton(text="Баланс?"),
            KeyboardButton(text="FAQ"),
            KeyboardButton(text="Кабинет"),
            KeyboardButton(text="Поддержка"),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.reply("Привет!\nЯ Эхобот от Skillbox!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
