import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts

logger = logging.getLogger(__name__)

MSG = "Па якой прычыне вам патрэбна дапамога з адвакатам?"
TO_BTN = "Дапамога з адвакатам"
HUMANITARIAN_REASONS_BTN = "Гуманітарныя прычыны"
POLITICAL_REASONS_BTN = "Палітычныя прычыны"
OTHER_REASONS_BTN = "Іншыя прычыны"

STATE = 'help-with-advocate'


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[HUMANITARIAN_REASONS_BTN, POLITICAL_REASONS_BTN, OTHER_REASONS_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def humanitarian_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["humanitarian-reasons"] = True
    return contacts.handler(update, context)


def political_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["political-reasons"] = True
    return contacts.handler(update, context)


def other_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["other-reasons"] = True
    return contacts.handler(update, context)


def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(HUMANITARIAN_REASONS_BTN), humanitarian_handler),
    MessageHandler(Filters.regex(POLITICAL_REASONS_BTN), political_handler),
    MessageHandler(Filters.regex(OTHER_REASONS_BTN), other_handler),
    MessageHandler(Filters.all, handler_fallback)
]
