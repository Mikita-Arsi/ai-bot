from aiogram import Router
from aiogram.filters import Command, CommandStart
from bot.commands.custom_filters import (
    SubFilter,
    MessageFilter,
    NewCommentFilter,
    CheckCommentFilter,
    ResetFilter,
    AdminFilter,
    MenuFilter,
    GPTFilter,
    DalleFilter,
    DalleBlockedFilter
)
from bot.commands.finish_sub import sub_finish
from bot.commands.finish_comment import comment_finish
from bot.commands.gpt_state import gpt_answer
from bot.commands.reset import reset_dialog
from bot.commands.register_comment import register_comment
from bot.commands.for_admin import call_admin_consol
from bot.commands.start import hello
from bot.commands.back_to_menu import back_to_menu
from bot.commands.to_gpt import to_gpt
from bot.commands.to_dalle import to_dalle
from bot.commands.gpt_state import gpt_router
from bot.commands.dalle_blocked import block_dalle


__all__ = ['register_base_handlers']


def register_base_handlers(router: Router) -> None:

    router.message.register(register_comment, NewCommentFilter())

    router.message.register(hello, CommandStart())
    router.message.register(reset_dialog, Command(commands=['reset']))
    router.message.register(call_admin_consol, AdminFilter())

    router.callback_query.register(sub_finish, SubFilter())
    router.callback_query.register(reset_dialog, ResetFilter())
    router.callback_query.register(comment_finish, CheckCommentFilter())
    router.callback_query.register(back_to_menu, MenuFilter())
    router.callback_query.register(to_gpt, GPTFilter())
    router.callback_query.register(to_dalle, DalleFilter())
    router.callback_query.register(block_dalle, DalleBlockedFilter())

    router.include_router(gpt_router)

