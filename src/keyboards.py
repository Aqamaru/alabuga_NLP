from enum import Enum
from text import Text
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

class Keyboards(Enum, ReplyKeyboardMarkup):
    START_KBD = ReplyKeyboardMarkup(resize_keyboard)\
            .add(*(KeyboardButton(i) for i in (
                Text.ANALYSIS_BTN,
                Text.HELP_BTN,
            )))

    ANALYSIS_KBD = ReplyKeyboardMarkup(resize_keyboard=True)\
            .add(*(KeyboardButton(i) for i in (
                Text.SET_COMPANIES_BTN,
                Text.BACK_TO_MAIN_MENU_BTN,
            )))
