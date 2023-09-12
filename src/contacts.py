from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, Filters, MessageHandler, ConversationHandler

import notify
from decorators import save_message
from constants import Button, State


MSG = "Дзякуй! Зараз мы спытаем вашыя кантакты для зваротнай сувязі. Калі зваротная сувязь не патрэбна ці вы не хочаце даваць вашыя кантактныя данные - вы можаце адмовіцца. Увага: мы не зможам з вамі звязацца, калі вы не дадзіце нам ваш кантакт."
CONTACT_MSG = "Яшчэ раз дзякуй! Калі спатэбіцца нешта яшчэ, выкарыстоўвайце каманду /start"


@save_message
def handler(update: Update, context: CallbackContext) -> str:
    context.user_data[State.CONTACT_STATE] = True
    reply_keyboard = [[KeyboardButton(Button.CONTACTS_BTN, request_contact=True), KeyboardButton(Button.CONTACTS_REJ_BTN)]]
    update.message.reply_text(
        MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return State.CONTACT_STATE


@save_message
def handler_contact(update: Update, context: CallbackContext) -> str:
    context.user_data[State.CONTACT_STATE] = update.message.contact
    update.message.reply_text(
        CONTACT_MSG,
        reply_markup=ReplyKeyboardRemove(),
    )

    notify.notify(update, context)

    return ConversationHandler.END


@save_message
def handler_reject_contact(update: Update, context: CallbackContext) -> str:
    context.user_data[State.CONTACT_STATE] = False
    update.message.reply_text(
        CONTACT_MSG,
        reply_markup=ReplyKeyboardRemove(),
    )

    notify.notify(update, context)

    return ConversationHandler.END


@save_message
def handler_fallback(update: Update, context: CallbackContext) -> str:
    update.message.reply_text("Калі ласка, выкарыстоўвайце клавіятуру")

    return handler(update, context)


handlers = [
    MessageHandler(Filters.regex(Button.CONTACTS_REJ_BTN), handler_reject_contact),
    MessageHandler(Filters.text, handler),
    MessageHandler(Filters.contact, handler_contact),
    MessageHandler(Filters.all, handler_fallback),
]
