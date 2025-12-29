from aiogram import Bot, Dispatcher, Router
import asyncio, config
from handlers import photos_menu, start, letters, congratulations, videos_menu
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

router = Router()

bot = Bot(config.BOT_TOKEN,
          default=DefaultBotProperties(parse_mode=ParseMode.HTML)
          )
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(letters.router)
dp.include_router(congratulations.router)
dp.include_router(photos_menu.router)
dp.include_router(videos_menu.router)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())