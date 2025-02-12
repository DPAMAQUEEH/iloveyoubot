import asyncio

from aiogram import types, Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.config import TOKENTGAPI

bot = Bot(token=TOKENTGAPI)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! \n\nЯ бот работающий на искусственном интелекте, и я помогу тебе узнать кое что интересное и полезное." + 
                         "\n\nВведи команду \n/ilv",
                         reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="/ilv")]],resize_keyboard=True))

@dp.message(Command("ilv"))
async def cmd_upload(message: Message):
    webAppInfo = types.WebAppInfo(url="https://dpamaqueeh.github.io/iloveyoubot/")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='Оpen', web_app=webAppInfo))
    await message.answer(text='Touch button', reply_markup=builder.as_markup())


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())