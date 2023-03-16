from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from constants import Button, State
from decorators import save_message


MSG = "Калі ласка апішыце вашы ідэі і прапановы. Калі будзеце гатовы - націсніце кнопку \"Гатова\""


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.IDEAS_STATE] = True
    reply_keyboard = [[Button.IDEAS_READY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.IDEAS_STATE


@save_message
def idea_handler(update: Update, context: CallbackContext) -> str:
    return State.IDEAS_STATE


handlers = [
    MessageHandler(Filters.regex(Button.IDEAS_READY_BTN), contacts.handler),
    MessageHandler(Filters.text, idea_handler),
]
