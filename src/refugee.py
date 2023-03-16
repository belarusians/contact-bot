from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import help_with_advocate
import help_with_finance
import help_with_stuff
from constants import Button, State
from decorators import save_message


MSG = "Якога кшталту дапамога вам патрэбна?"


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.REFUGEE_STATE] = True
    reply_keyboard = [[Button.ADVOCATE_TO_BTN, Button.FINANCE_TO_BTN, Button.STUFF_TO_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.REFUGEE_STATE


handlers = [
    MessageHandler(Filters.regex(Button.ADVOCATE_TO_BTN), help_with_advocate.handler),
    MessageHandler(Filters.regex(Button.FINANCE_TO_BTN), help_with_finance.handler),
    MessageHandler(Filters.regex(Button.STUFF_TO_BTN), help_with_stuff.handler),
]