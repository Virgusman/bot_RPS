from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU

#Хэндлер для текстовых сообщений, не попавших в другие хендлеры
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])

#Функция для регистрации хэндлера
def register_other_handler(dp:Dispatcher):
    dp.register_message_handler(send_answer)