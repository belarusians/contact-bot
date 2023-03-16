from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts
from constants import Button, State
from decorators import save_message


MSG = "Якое адзенне вам патрэбна?"


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.STUFF_STATE] = True
    reply_keyboard = [[Button.STUFF_CLOTHES_YS_BTN, Button.STUFF_CLOTHES_CHILD_BTN, Button.STUFF_CLOTHES_FAMILY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.STUFF_STATE


@save_message
def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(Button.STUFF_CLOTHES_YS_BTN), contacts.handler),
    MessageHandler(Filters.regex(Button.STUFF_CLOTHES_CHILD_BTN), contacts.handler),
    MessageHandler(Filters.regex(Button.STUFF_CLOTHES_FAMILY_BTN), contacts.handler),
    MessageHandler(Filters.all, handler_fallback)
]
