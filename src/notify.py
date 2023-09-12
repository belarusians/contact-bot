import telegram
import sys
from telegram import Update
from telegram.ext import CallbackContext

from decorators import TEXT


template = """
<b>Новы запыт!</b>

--------------------
<i>{text}</i>
--------------------

"""

chat_id = sys.argv[2] if len(sys.argv) > 2 else None
print("Chat ID: ", chat_id)


def set_chat_id(c_id):
    global chat_id
    chat_id = c_id
    print("Chat ID is updated to: ", chat_id)


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
