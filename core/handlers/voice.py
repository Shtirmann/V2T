from aiogram import Router, F, Bot
from aiogram.types import Message
from core.handlers import download, resample, voice2text

router = Router()


@router.message(F.voice)
async def voice(message: Message, bot: Bot):
    duration = message.voice.duration
    minutes = duration // 60
    formated = f"{'{:02d}'.format(min(minutes, 59))}:{'{:02d}'.format(duration - minutes * 60)}"

    if duration > 120:
        await message.reply(text=f"<b>~ [{formated} &gt 02:00] ~</b>\n\n"
                                 f"<i> Voice message is too long.</i>",
                            parse_mode='HTML')
        return
    filename, msg, pb = await download(message.voice, message, bot)
    await resample(msg, bot, filename, pb)
    await voice2text(msg, bot, filename, pb)
