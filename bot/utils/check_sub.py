from aiogram import types, Bot
from bot.const import channels


async def check_sub(message: types.Message | types.CallbackQuery, bot: Bot) -> bool:
    c = []
    for channel in channels:
        user_channel_status = await bot.get_chat_member(chat_id=channel.id, user_id=message.from_user.id)
        if user_channel_status.status == 'left':
            c.append(channel.prefix)
        if len(c) > 0:
            return False
        return True
