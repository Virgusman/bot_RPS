import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import TOKEN
from handlers.other_handlers import register_other_handler
from handlers.user_handlers import register_user_handlers

#функция для регистрации хэндлеров
def register_all_handlers(dp: Dispatcher):
    register_user_handlers(dp)
    register_other_handler(dp)
    

#Конфигурирование и запуск бота
async def main():
    bot: Bot = Bot(token = TOKEN)
    dp: Dispatcher = Dispatcher(bot)
    register_all_handlers(dp)

    # Запускаем polling
    try:
        await dp.start_polling()
    finally:
        await bot.close()

try:
    #Запускаем main
    asyncio.run(main())
except (KeyboardInterrupt, SystemExit):
    # Выводим в консоль сообщение об ошибке,
    # если получены исключения KeyboardInterrupt или SystemExit
    print('Bot stopped!')
