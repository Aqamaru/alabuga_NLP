from enum import Enum

class Text(str, Enum):

    START_MESSAGE = ("Здравствуйте!\n"
                     "Рады приветствовать вас в нашем телеграм боте!\n")
    
    HELP_BTN = ("Помощь")

    HELP_BASE = ("Выберите вид помощи")
    
    HELP_CMD = ("")
    
    HELP_CMD_COMPANIES = ("")

    HELP_CMD_ANALYSIS = ("")

    ANALYSIS_BTN = ("Анализ")
    
    ANALYSIS = ("Вы открыли меню анализа")

    SET_COMPANIES_BTN = ("Указать компании")

    SET_COMPANIES = ("Список компании обновлен\n"
                     "Компании:\n")

    BACK_TO_MAIN_MENU_BTN = ("Назад")

    BACK_TO_MAIN_MENU = ("Вы вернулись в главное меню")

    UNKNOWN_COMMAND = ("Неизвестная команда")
