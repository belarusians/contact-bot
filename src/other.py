from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from constants import Button, State
from decorators import save_message


MSG = "Я вас слухаю. Калі закончыце - націсніте кнопку \"{}\"".format(Button.OTHER_READY_BTN)


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.OTHER_STATE] = True
    reply_keyboard = [[Button.OTHER_READY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.OTHER_STATE


@save_message
def other_handler(update: Update, context: CallbackContext) -> str:
    return State.OTHER_STATE


handlers = [
    MessageHandler(Filters.regex(Button.OTHER_READY_BTN), contacts.handler),
    MessageHandler(Filters.text, other_handler),
]
