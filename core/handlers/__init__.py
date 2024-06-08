import pathlib

from config import FILEPATH
from utility.converter import downsample
from utility.progress_bar import ProgressBar
from aiogram import Bot
from bot_whisper import Whisper
from aiogram.types import Message


async def download(file, message: Message, bot: Bot):
    pb = ProgressBar(total=100, current=0)

    process_msg = await message.reply(text=f"<b>{pb.render(14)}</b>\n"
                                           f"\n"
                                           f"<i>Downloading...</i>",
                                      parse_mode='HTML')

    extension = '.mp3'

    if file is message.video_note:
        extension = '.mp4'

    filename = f"{file.file_id}{extension}"

    await bot.download(file=file,
                       destination=FILEPATH + filename)

    pb.advance(20)
    return filename, process_msg, pb


async def resample(msg: Message, bot: Bot, filename: str, pb: ProgressBar):
    await pb.render_msg(bot, msg, "Downsampling...")
    downsample(filename)
    pb.advance(20)


async def voice2text(msg: Message, bot: Bot, filename: str, pb: ProgressBar):
    await pb.render_msg(bot, msg, "Loading model...")
    model = Whisper()
    pb.advance(10)
    await pb.render_msg(bot, msg, "Converting...")
    text = model.create_text(FILEPATH + filename)
    pathlib.Path(FILEPATH + filename).unlink()
    pb.advance(30)
    await pb.render_msg(bot, msg, "Editing...")
    await bot.edit_message_text(chat_id=msg.chat.id,
                                message_id=msg.message_id,
                                text=f'🗣️ <i>{text}</i>',
                                parse_mode='HTML')
