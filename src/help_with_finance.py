from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from constants import Button, State
from decorators import save_message


MSG = "На якія патрэбы?"


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.FINANCE_STATE] = True
    reply_keyboard = [[Button.FINANCE_ANY_REASONS_BTN, Button.FINANCE_ADVOCATE_REASONS_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.FINANCE_STATE


@save_message
def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(Button.FINANCE_ANY_REASONS_BTN), contacts.handler),
    MessageHandler(Filters.regex(Button.FINANCE_ADVOCATE_REASONS_BTN), contacts.handler),
    MessageHandler(Filters.all, handler_fallback)
]
