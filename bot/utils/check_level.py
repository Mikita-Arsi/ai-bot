from aiogram import types, Bot
from bot.const import pre_study_forum_id, pre_study_channel, admins
from bot.models import UserLevel, LEVEL0, LEVEL1, LEVEL2


async def check_user_level(message: types.Message | types.CallbackQuery, bot: Bot) -> UserLevel:
    if message.from_user.id in [admin.id for admin in admins]:
        return LEVEL2
    user_channel_status = await bot.get_chat_member(chat_id=pre_study_channel.id, user_id=message.from_user.id)
    if user_channel_status.status in ['kicked', 'left']:
        user_forum_status = await bot.get_chat_member(chat_id=pre_study_forum_id, user_id=message.from_user.id)
        if user_forum_status.status in ['kicked', 'left']:
            return LEVEL0
    return LEVEL1
