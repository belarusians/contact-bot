from telegram import Update
from telegram.ext import CallbackContext


def notify(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=-1001107989091, text=str(context.user_data))
