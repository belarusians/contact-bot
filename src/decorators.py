from telegram import Update
from telegram.ext import CallbackContext

from constants import Button


TEXT = "text"
DELIMITER = "\n--------------------\n"

UNNEEDED_BUTTONS = {Button.IDEAS_READY_BTN, Button.OTHER_READY_BTN, Button.CONTACTS_BTN, Button.CONTACTS_REJ_BTN}


def save_message(function):
    def wrapper(update: Update, context: CallbackContext):
        if update.message.text is not None and update.message.text not in UNNEEDED_BUTTONS:
            user_message = update.message.text if update.message.text in Button else "<b>user message:</b> " + update.message.text
            context.user_data[TEXT] = user_message if TEXT not in context.user_data \
                else context.user_data[TEXT] + DELIMITER + user_message
        result = function(update, context)
        return result

    return wrapper
