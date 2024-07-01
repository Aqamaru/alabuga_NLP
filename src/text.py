from enum import Enum

class Text(str, Enum):

    START_MESSAGE = ("Здравствуйте!\n"
                     "Рады приветствовать вас в нашем телеграм боте!\n")
    
    HELP_BTN = ("Помощь")

    HELP = ("Вы запросили помощь")
    
    ANALYSIS_BTN = ("Анализ")
    
    ANALYSIS = ("Вы открыли меню анализа")

    SET_COMPANIES_BTN = ("Указать компании")

    BACK_TO_MAIN_MENU_BTN = ("Назад")

    BACK_TO_MAIN_MENU = ("Вы вернулись в главное меню")

    UNKNOWN_COMMAND = ("Неизвестная команда")
