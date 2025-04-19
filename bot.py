import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

TOKEN = "8147042739:AAHM3epqqx7bUbWo1hUNgmGJqadoVX4JEL8"
CHANNEL_LINK = "https://t.me/onlyrate18"

# Указываем parse_mode через default
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f"Приветик! Ты попал к боту который переправит тебя к нам, вот держи ссылку, мы ждем тебя:)\n{CHANNEL_LINK}")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Вот ссылка на канал, как и просил:\n{CHANNEL_LINK}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
