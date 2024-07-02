from text import Text
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

START = ReplyKeyboardMarkup(resize_keyboard = True)\
        .add(*(KeyboardButton(i) for i in (
            Text.ANALYSIS_BTN,
            Text.HELP_BTN,
<<<<<<< HEAD
            Text.SET_COMPANIES_BTN,
        )))
=======
        ))) 
>>>>>>> 23257666319246fa8066ba0093e8df61915e7231

ANALYSIS = ReplyKeyboardMarkup(resize_keyboard = True)\
        .add(*(KeyboardButton(i) for i in (
            Text.SET_COMPANIES_ANALYSIS,
            Text.BACK_TO_MAIN_MENU_BTN,
         )))

HELPS = ReplyKeyboardMarkup()\
        .add(*(KeyboardButton(i) for i in (
            Text.CONTACTS_BTN,
            Text.USAGE_BTN,
         )))
