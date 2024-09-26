import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from decouple import config


TOKEN = config('TELEGRAM_TOKEN')


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Напиши мне число или любое сообщение.")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo(message: types.Message):
    if message.text.isdigit():
        number = int(message.text)
        await message.reply(number ** 2)
    else:
        await message.reply(message.text)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def handle_docs(message: types.Message):
    file_id = message.document.file_id
    await bot.send_document(chat_id=message.chat.id, document=file_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
