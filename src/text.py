from enum import Enum

class Text(Enum, str):

    START_MESSAGE = ("Здравствуйте!\n"
                     "Рады приветствовать вас в нашем телеграм боте!\n")
    
    HELP_BTN = ("Помощь")

    HELP = ("Вы запросили помощь")

    ANALYSIS_BTN = ("Анализ")

    SET_COMPANIES_BTN = ("Указать компании")

    BACK_TO_MAIN_MENU_BTN = ("Назад")
