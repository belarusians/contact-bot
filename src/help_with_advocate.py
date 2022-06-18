import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

logger = logging.getLogger(__name__)

MSG = "Па якой прычыне вам патрэбна дапамога з адвакатам?"
TO_BTN = "Дапамога з адвакатам"

STATE = 'help-with-advocate'


def handler(update: Update, context: CallbackContext) -> str:
    reply_keyboard = [["тамушто"]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


handlers = [
    # MessageHandler(Filters.regex(HELP_WITH_ADVOCATE_BTN), helpWithAdvocate),
    # MessageHandler(Filters.regex(HELP_WITH_FINANCE_BTN), handler),
    # MessageHandler(Filters.regex(HELP_WITH_STUFF_BTN), handler),
]
