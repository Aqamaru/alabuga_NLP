from text import Text
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

START = ReplyKeyboardMarkup()\
        .add(*(KeyboardButton(i) for i in (
            Text.ANALYSIS_BTN,
            Text.HELP_BTN,
            Text.SET_COMPANIES_BTN,
        )))

ANALYSIS = ReplyKeyboardMarkup()\
        .add(*(KeyboardButton(i) for i in (
            Text.SET_COMPANIES_ANALYSIS,
            Text.BACK_TO_MAIN_MENU_BTN,
         )))

HELPS = ReplyKeyboardMarkup()\
        .add(*(KeyboardButton(i) for i in (
            Text.CONTACTS_BTN,
            Text.USAGE_BTN,
         )))


