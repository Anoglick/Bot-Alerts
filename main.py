import asyncio
from datetime import datetime, timedelta
from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from other.config import bot
from other.checking_updates import checking
from user_interface.user_interface import router as user_router


async def main():
    dp = Dispatcher()
    dp.include_routers(
        user_router,
    
    )
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(
        checking, 
        trigger='interval', 
        hours=24, 
        kwargs={'bot': bot}
    )
    scheduler.start()


    await bot.delete_webhook(True)
    await dp.start_polling(bot, skip_updates=True, sleep=False)
    

if __name__ == '__main__':
    asyncio.run(main())
