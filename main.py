import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import load_config
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

# Инициализируем логгер
logger = logging.getLogger(__name__)


async def main() -> None:
    
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    logger.info('bot is running')

    BOT_TOKEN = load_config().tg_bot.token
    
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    await set_main_menu(bot)
   
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())