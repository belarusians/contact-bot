from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts


TO_BTN = "Ідэі і прапановы"
READY_BTN = "Гатова"
MSG = "Калі ласка апішыце вашы ідэі і прапановы. Калі будзеце гатовы - націсніце кнопку \"Гатова\""
STATE = "ideas"


def handler(update: Update, context: CallbackContext) -> str:
    reply_keyboard = [[READY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


handlers = [
    MessageHandler(Filters.regex(READY_BTN), contacts.handler),
]
