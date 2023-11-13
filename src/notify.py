import telegram
from telegram import Update
from telegram.ext import CallbackContext

from logger import logger
from decorators import TEXT
from args import args


template = """
<b>Новы запыт!</b>

--------------------
<i>{text}</i>
--------------------

"""

chat_id = args.chat
logger.info("Chat ID: %s", chat_id)


def set_chat_id(c_id):
    global chat_id
    chat_id = c_id
    logger.info("Chat ID is updated to: %s", chat_id)


def notify(update: Update, context: CallbackContext) -> None:
    text = template.format(text=context.user_data[TEXT])
    if 'contact' not in context.user_data or not context.user_data['contact']:
        text += "Карыстальнік не пакінуў кантактных дадзеных"
        send_contact = False
    else:
        send_contact = True

    context.bot.send_message(chat_id=chat_id, parse_mode=telegram.ParseMode.HTML, text=text)

    if send_contact:
        context.bot.send_contact(chat_id=chat_id, contact=context.user_data['contact'])
