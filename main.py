import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    web_app_info = WebAppInfo(url="https://lively-dolphin-345c07.netlify.app")
    keyboard_button = KeyboardButton(text="Open", web_app=web_app_info)
    reply_markup = ReplyKeyboardMarkup(keyboard=[[keyboard_button]])
    await message.answer(text=f"Hello!", reply_markup=reply_markup)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:

        await message.answer("Nice try!")


async def main() -> None:

    bot = Bot(
        token="6297811466:AAGG4PBUzY_VTixLV3T22cvmu1xPjMWfaF0",
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
