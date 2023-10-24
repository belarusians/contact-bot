#!/usr/bin/env python

import sys
import threading
import requests

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

import refugee
import help_with_stuff
import help_with_finance
import help_with_advocate
import other
import ideas
import contacts
import notify
from logger import logger
from constants import Button, State


START = "start"
GREETINGS_MSG = "Вітаем! Мы - беларуская дыяспара ў Нідэрландах. Наконт чаго вы хацелі бы звязацца з намі?"


def start(update: Update, context: CallbackContext) -> str:
    context.user_data.clear()
    reply_keyboard = [[Button.REFUGEE_TO_BTN, Button.IDEAS_TO_BTN, Button.OTHER_TO_BTN]]

    update.message.reply_text(
        GREETINGS_MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return START


def cancel(update: Update, context: CallbackContext) -> int:
    logger.info("User canceled the conversation")
    update.message.reply_text('Дзякуй, да пабачэння', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def handle_new_chat(update: Update, context: CallbackContext) -> None:
    matches = [x for x in update.message.new_chat_members if x.id == context.bot.id]
    if len(matches) > 0:
        chat_id = update.effective_chat.id
        notify.set_chat_id(chat_id)
        context.bot.send_message(chat_id=chat_id, text=chat_id)


def main() -> None:
    token = sys.argv[1]
    if not token:
        print("Token is not provided")
        exit(1)

    updater = Updater(token)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            MessageHandler(Filters.all, handle_new_chat),
        ],
        states={
            START: [
                MessageHandler(Filters.regex(Button.REFUGEE_TO_BTN), refugee.handler),
                MessageHandler(Filters.regex(Button.OTHER_TO_BTN), other.handler),
                MessageHandler(Filters.regex(Button.IDEAS_TO_BTN), ideas.handler)
            ],
            State.REFUGEE_STATE: refugee.handlers,
            State.FINANCE_STATE: help_with_finance.handlers,
            State.STUFF_STATE: help_with_stuff.handlers,
            State.ADVOCATE_STATE: help_with_advocate.handlers,
            State.IDEAS_STATE: ideas.handlers,
            State.CONTACT_STATE: contacts.handlers,
            State.OTHER_STATE: other.handlers,
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


# https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval
def set_interval(func, sec: int):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


def heartbeat():
    url = sys.argv[2]
    requests.head(url)


if __name__ == '__main__':
    set_interval(heartbeat, 60 * 5)
    main()
