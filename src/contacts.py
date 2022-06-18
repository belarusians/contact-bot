from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, Filters, MessageHandler, ConversationHandler

STATE = 'contact'
MSG = "Дзякуй! Зараз мы спытаем вашыя кантакты для зваротнай сувязі. Калі зваротная сувязь не патрэбна ці вы не хочаце даваць вашыя кантактныя данные - вы можаце адмовіцца"
CONTACTS_BTN = "Даць доступ да кантактных дадзеных"


def handler(update: Update, context: CallbackContext) -> str:
    reply_keyboard = [[KeyboardButton(CONTACTS_BTN, request_contact=True)]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return STATE


def handler_contact(update: Update, context: CallbackContext) -> str:
    print(update.message)

    return ConversationHandler.END


handlers = [
    MessageHandler(Filters.text, handler),
    MessageHandler(Filters.contact, handler_contact),
]
