import asyncio
from core.handlers import voice, video
from core import dp, bot


async def main():
    dp.include_routers(voice.router, video.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
