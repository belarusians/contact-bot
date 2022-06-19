from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import help_with_advocate
import help_with_finance
import help_with_stuff


TO_BTN = "Я бежанец"
MSG = "Якога кшталту дапамога вам патрэбна?"
STATE = 'refugee'


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[help_with_advocate.TO_BTN, help_with_finance.TO_BTN, help_with_stuff.TO_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


handlers = [
    MessageHandler(Filters.regex(help_with_advocate.TO_BTN), help_with_advocate.handler),
    MessageHandler(Filters.regex(help_with_finance.TO_BTN), help_with_finance.handler),
    MessageHandler(Filters.regex(help_with_stuff.TO_BTN), help_with_stuff.handler),
]