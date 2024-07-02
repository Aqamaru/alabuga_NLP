from text import Text
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

START = ReplyKeyboardMarkup(resize_keyboard = True)\
        .add(*(KeyboardButton(i) for i in (
            Text.ANALYSIS_BTN,
            Text.HELP_BTN,
        ))) 

ANALYSIS = ReplyKeyboardMarkup(resize_keyboard = True)\
        .add(*(KeyboardButton(i) for i in (
            Text.SET_COMPANIES_BTN,
            Text.BACK_TO_MAIN_MENU_BTN,
         )))

HELPS = ReplyKeyboardMarkup()\
        .add(*(KeyboardButton(i) for i in (
            Text.CONTACTS_BTN,
            Text.USAGE_BTN,
         )))
