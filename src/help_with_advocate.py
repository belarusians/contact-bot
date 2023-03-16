import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from constants import Button, State
from decorators import save_message


logger = logging.getLogger(__name__)

MSG = "Па якой прычыне вам патрэбна дапамога з адвакатам?"


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.ADVOCATE_STATE] = True
    reply_keyboard = [[Button.ADVOCATE_HUMANITARIAN_REASONS_BTN, Button.ADVOCATE_POLITICAL_REASONS_BTN, Button.ADVOCATE_OTHER_REASONS_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.ADVOCATE_STATE

@save_message
def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(Button.ADVOCATE_HUMANITARIAN_REASONS_BTN), contacts.handler),
    MessageHandler(Filters.regex(Button.ADVOCATE_POLITICAL_REASONS_BTN), contacts.handler),
    MessageHandler(Filters.regex(Button.ADVOCATE_OTHER_REASONS_BTN), contacts.handler),
    MessageHandler(Filters.all, handler_fallback)
]
