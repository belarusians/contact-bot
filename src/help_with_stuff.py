from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

import contacts

TO_BTN = "Матэрыяльная дапамога"
MSG = "Якое адзенне вам патрэбна?"
CLOTHES_YS_BTN = "Адзенне для сябе"
CLOTHES_CHILD_BTN = "Адзенне для дзяцей"
CLOTHES_FAMILY_BTN = "Адзенне для сям'і"
STATE = 'help-with-stuff'


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[CLOTHES_YS_BTN, CLOTHES_CHILD_BTN, CLOTHES_FAMILY_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def clothes_ys_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["clothes-for-yourself"] = True
    return contacts.handler(update, context)


def clothes_for_child_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["clothes-for-child"] = True
    return contacts.handler(update, context)


def clothes_for_family_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["clothes-for-family"] = True
    return contacts.handler(update, context)


def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(CLOTHES_YS_BTN), clothes_ys_handler),
    MessageHandler(Filters.regex(CLOTHES_CHILD_BTN), clothes_for_child_handler),
    MessageHandler(Filters.regex(CLOTHES_FAMILY_BTN), clothes_for_family_handler),
    MessageHandler(Filters.all, handler_fallback)
]
