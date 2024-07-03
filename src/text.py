from enum import Enum

class Text(str, Enum):

    START_MESSAGE = ("Здравствуйте!\n"
                     "Рады приветствовать вас в нашем телеграм боте!\n")
    
    HELP_BTN = ("Помощь")
    
    HELP_BASE = ("Выберите вид помощи")
    
    HELP_CMD_COMPANIES = ("Устанавливает список компаний для анализа")

    HELP_CMD_ANALYSIS = ("Запускает анализ при наличии списка компании")
    
    ANALYSIS_BTN = ("Анализ")
    
    ANALYSIS = ("Вы открыли меню анализа")

    ANALYSIS_START = ("Введите ссылку на статью")

    ANALYSIS_START_BTN = ("Начать анализ")

    SET_COMPANIES_BTN = ("Указать компании")

    SET_COMPANIES = ("Укажите список компаний для анализа")
    
    BACK_TO_MAIN_MENU_BTN = ("Назад")

    BACK_TO_MAIN_MENU = ("Вы вернулись в главное меню")

    UNKNOWN_COMMAND = ("Неизвестная команда")
    
    GET_COMPANES = ("Обновленный список компаний:")

    CONTACTS_BTN = ("Контакты")

    CONTACTS = ("Контакты разработчиков:\n"
                "Григорий - @CucumberMayoo\n"
                "Андрей - @NightsForever")

    USAGE_BTN = ("Как пользоваться?")

    USAGE = ("1) Откройте раздел Анализ\n"
             "2) Нажмите кнопку Указать компании\n"
             "3) Введите их список через пробел без использования запятых\n"
             "4) Нажмите кнопку начать анализ\n"
             "5) Введите ссылку на статью\n"
             "P.S. - более одной статьи обработано не будет")

    ERROR_NO_COMPANIES = ("В списке для анализа не обнаружено компаний")

def get_analysis_result(companies: list[str], ai_answer: str) -> str:
    answer = ""
    for i in companies:
        answer = answer + f"Оценка компании {i}: {ai_answer}\n"
        answer.replace("neutral", "Нейтральная")
        answer.replace("positive", "Положительная")
        answer.replace("negative", "Отрицательная")
    return answer
