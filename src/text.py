from enum import Enum

class Text(str, Enum):

    START_MESSAGE = ("Здравствуйте!\n"
                     "Рады приветствовать вас в нашем телеграм боте!\n")
    
    HELP_BTN = ("Помощь")

    HELP = ("Вы запросили помощь")
    
    ANALYSIS_BTN = ("Анализ")
    
    ANALYSIS = ("Вы открыли меню анализа")

    SET_COMPANIES_BTN = ("Указать компании")

    SET_COMPANIES = ("Добавьте компанию")

    BACK_TO_MAIN_MENU_BTN = ("Назад")

    BACK_TO_MAIN_MENU = ("Вы вернулись в главное меню")

    UNKNOWN_COMMAND = ("Неизвестная команда")

    GET_COMPANES = ("Обновленный список компаний:")

    CONTACTS_BTN = ("Контакты")

    CONTACTS = ("Контакты разработчиков:\n"
                "Григорий - @CucumberMayoo\n"
                "Андрей - @NightsForever")

    USAGE_BTN = ("Правило использования")

    USAGE = ("Делайте то, се, пятое, десятое, но лучший выход всегда в окно")