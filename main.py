import asyncio
from aiogram import Dispatcher

from config import bot
from user_interface import router as user_router

async def main():
    dp = Dispatcher()
    dp.include_router(router=user_router)

    await bot.delete_webhook(True)
    await dp.start_polling(bot, skip_updates=True, sleep=False)
    

if __name__ == '__main__':
    asyncio.run(main())
