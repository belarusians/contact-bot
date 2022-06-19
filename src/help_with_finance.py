from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

from src import contacts

TO_BTN = "Фінансавая дапамога"
MSG = "На якія патрэбы?"
ANY_REASONS_BTN = "Хутка любыя патрэбы"
ADVOCATE_REASONS_BTN = "На адваката"

STATE = 'help-with-finance'


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[ANY_REASONS_BTN, ADVOCATE_REASONS_BTN]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def any_necessity_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["any-reasons"] = True
    return contacts.handler(update, context)


def advocate_necessity_handler(update: Update, context: CallbackContext) -> str:
    context.user_data["advocate-reasons"] = True
    return contacts.handler(update, context)


def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(ANY_REASONS_BTN), any_necessity_handler),
    MessageHandler(Filters.regex(ADVOCATE_REASONS_BTN), advocate_necessity_handler),
    MessageHandler(Filters.all, handler_fallback)
]
