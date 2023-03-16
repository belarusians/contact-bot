import telegram
from telegram import Update
from telegram.ext import CallbackContext

template = """
<b>Новы запыт!</b>

<b>Секцыя:</b> {state}

<b>Тэкст запыту:</b>
====================
<i>{text}</i>
====================

"""


def notify(update: Update, context: CallbackContext) -> None:
    text = template.format(text=context.user_data['ideas'], state="Ідэі і прапановы")
    if 'contact' not in context.user_data or not context.user_data['contact']:
        text += "Карыстальнік не пакінуў кантактных дадзеных"
        send_contact = False
    else:
        send_contact = True

    context.bot.send_message(chat_id=-1001743348246, parse_mode=telegram.ParseMode.HTML, text=text)

    if send_contact:
        context.bot.send_contact(chat_id=-1001743348246, contact=context.user_data['contact'])
