from aiogram import Router, F, Bot

from core.handlers import download, resample, voice2text
from aiogram.types import Message

from utility.converter import convert_to_audio, downsample

router = Router()


@router.message(F.video_note)
async def video(message: Message, bot: Bot):
    filename, msg, pb = await download(message.video_note, message, bot)
    filename = await convert_to_audio(filename, f"{message.video_note.file_id}.mp3")
    await resample(msg, bot, filename, pb)
    await voice2text(msg, bot, filename, pb)
