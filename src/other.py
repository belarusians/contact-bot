from telegram import Update
from telegram.ext import CallbackContext

TO_BTN = "Другое"
STATE = "other"


def handler(update: Update, context: CallbackContext) -> str:
    return STATE


handlers = [
    # MessageHandler(Filters.regex(HELP_WITH_ADVOCATE_BTN), helpWithAdvocate),
    # MessageHandler(Filters.regex(HELP_WITH_FINANCE_BTN), handler),
    # MessageHandler(Filters.regex(HELP_WITH_STUFF_BTN), handler),
]
