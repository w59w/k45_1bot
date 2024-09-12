import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: types.Message):
    await message.answer("Привет, я бот группы 45-1, Ибраимовой Кумушай")


@dp.message(Command('picture'))
async def picture_handler(message: types.Message):
    image = types.FSInputFile("images/pic1.jpg")
    await message.answer_photo(photo=image, caption=f"изображение")


@dp.message()
async def echo_handler(message: types.Message):
    if message.text.isdigit():
        await message.answer(f'{int(message.text)**2}')
    else:
        await message.answer(message.text)


async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
