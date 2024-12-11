#Импортируем сущность бота, диспетчера, «executor», типы
from  aiogram import Bot, Dispatcher, executor, types

#Из блока работы с памятью (находится в aiogram.contrib) нужен "fsm_storage".
# Нужно импортировать оттуда «MemoryStorage»
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio

api = ''
bot = Bot(token= api)
dp = Dispatcher(bot, storage= MemoryStorage())


@dp.message_handler(commands= ['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)

