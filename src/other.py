from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from states import State

TO_BTN = "Іншае"
READY_BTN = "Гатова"
MSG = "Я вас слухаю. Калі закончыце - націсніте кнопку \"{}\"".format(READY_BTN)
STATE = State.other


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[READY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def other_handler(update: Update, context: CallbackContext) -> str:
    if type(context.user_data[STATE]) == str:
        context.user_data[STATE] += "\n {}".format(update.message.text)
    else:
        context.user_data[STATE] = update.message.text

    return STATE


handlers = [
    MessageHandler(Filters.regex(READY_BTN), contacts.handler),
    MessageHandler(Filters.text, other_handler),
]
