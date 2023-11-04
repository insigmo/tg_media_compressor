import asyncio
from pathlib import Path
from tempfile import TemporaryDirectory

from aiogram import Bot, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from source.file_handler import FileCompressor
from source.models.file_params import FileParams
from source.models.mime_type import FileFormats
from source.vars import Vars

dp = Dispatcher()
bot = Bot(token=Vars().bot_token)


@dp.message(Command('start'))
async def starting(message: Message):
    await message.answer(f'Hi, {message.from_user.first_name}')


@dp.message()
async def file_handler(message: Message):
    with TemporaryDirectory() as temp_folder:
        file_path = Path(temp_folder) / message.document.file_name
        await message.bot.download(message.document, file_path)

        file_params = FileParams(
            file_id=message.document.file_id,
            file_path=file_path,
            file_size=message.document.file_size,
            file_unique_id=message.document.file_unique_id,
            mime_type=FileFormats(message.document.mime_type),
        )

        result = FileCompressor.run(file_params)
        await message.bot.send_document(message.from_user.id, FSInputFile(path=result.file_path))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
