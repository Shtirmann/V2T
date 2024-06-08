from aiogram import Bot
from aiogram.types import Message


class ProgressBar:
    def __init__(self, total: int, current: int = None):
        if current is None:
            current = 0
        self.total = total
        self.current = current

    def advance(self, advance: int):
        self.current += advance

    def reset(self):
        self.total = 0

    def render(self, bars: int = None):
        if bars is None:
            bars = 10
        bar = round(self.total / bars)
        ready = 0
        if bar > 0:
            ready = round(self.current / bar)
        tb = ' '
        if bars == ready:
            tb = ''
        return f"[{'=' * ready}{' ·' * (bars - ready)}{tb}]"

    async def render_msg(self, bot: Bot, msg: Message, comment: str, bars: int = None):
        if bars is None:
            bars = 14
        await bot.edit_message_text(message_id=msg.message_id,
                                    chat_id=msg.chat.id,
                                    text=f"<b>{self.render(bars)}</b>\n"
                                         f"\n"
                                         f"<i>{comment}</i>",
                                    parse_mode='HTML')
