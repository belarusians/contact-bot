from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, Filters, MessageHandler, ConversationHandler

from src.notify import notify

STATE = 'contact'
MSG = "Дзякуй! Зараз мы спытаем вашыя кантакты для зваротнай сувязі. Калі зваротная сувязь не патрэбна ці вы не хочаце даваць вашыя кантактныя данные - вы можаце адмовіцца"
CONTACT_MSG = "Яшчэ раз дзякуй! Калі спатэбіцца нешта яшчэ, выкарыстоўвайце каманду /start"
CONTACTS_BTN = "Даць кантакт"
CONTACTS_REJ_BTN = "Адмовіць"


def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = True
    reply_keyboard = [[KeyboardButton(CONTACTS_BTN, request_contact=True), KeyboardButton(CONTACTS_REJ_BTN)]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def handler_contact(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = update.message.contact
    update.message.reply_text(
        CONTACT_MSG,
        reply_markup=ReplyKeyboardRemove(),
    )

    notify(update, context)

    return ConversationHandler.END


def handler_reject_contact(update: Update, context: CallbackContext) -> str:
    context.user_data[STATE] = False
    update.message.reply_text(
        CONTACT_MSG,
        reply_markup=ReplyKeyboardRemove(),
    )

    notify(update, context)

    return ConversationHandler.END


def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(CONTACTS_REJ_BTN), handler_reject_contact),
    MessageHandler(Filters.text, handler),
    MessageHandler(Filters.contact, handler_contact),
    MessageHandler(Filters.all, handler_fallback),
]
