#!/usr/bin/env python

import logging
import sys

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

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

START = "start"
GREETINGS_MSG = "Вітаем! Мы - беларуская дыяспара ў Нідэрландах. Наконт чаго вы хацелі бы звязацца з намі?"


def start(update: Update, context: CallbackContext) -> str:
    context.user_data.clear()
    reply_keyboard = [[refugee.TO_BTN, ideas.TO_BTN, other.TO_BTN]]

    update.message.reply_text(
        GREETINGS_MSG,
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return START


def cancel(update: Update, context: CallbackContext) -> int:
    logger.info("User canceled the conversation")
    update.message.reply_text('Дзякуй, да пабачэння', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


# def debug_handler(update: Update, context: CallbackContext) -> str:
#     return ConversationHandler.END


def main() -> None:
    updater = Updater(sys.argv[1])

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[
            # MessageHandler(Filters.all, debug_handler),
            CommandHandler('start', start)
        ],
        states={
            START: [
                MessageHandler(Filters.regex(refugee.TO_BTN), refugee.handler),
                MessageHandler(Filters.regex(other.TO_BTN), other.handler),
                MessageHandler(Filters.regex(ideas.TO_BTN), ideas.handler)
            ],
            refugee.STATE: refugee.handlers,
            help_with_finance.STATE: help_with_finance.handlers,
            help_with_stuff.STATE: help_with_stuff.handlers,
            help_with_advocate.STATE: help_with_advocate.handlers,
            ideas.STATE: ideas.handlers,
            contacts.STATE: contacts.handlers,
            other.STATE: other.handlers,
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
