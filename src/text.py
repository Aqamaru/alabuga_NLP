from enum import Enum 
 
class Text(str, Enum): 
 
    START_MESSAGE = ("Здравствуйте!\n" 
                     "Рады приветствовать вас в нашем телеграм боте!\n") 
     
    HELP_BTN = ("Помощь") 
     
    HELP_BASE = ("Выберите вид помощи") 
 
    ANALYSIS_BTN = ("Анализ") 
     
    ANALYSIS = ("Вы открыли меню анализа") 
 
    SET_COMPANIES_BTN = ("Добавить компании") 
 
    SET_COMPANIES_ANALYSIS_BTN = ("Выбрать компанию") 
 
    SET_COMPANIES_ANALYSIS = ("Выбрать компанию для поиска их эмоциональной составляющей в статьях  ") 
 
    SET_COMPANIES = ("Впишите название компании") 
     
    BACK_TO_MAIN_MENU_BTN = ("Назад") 
 
    BACK_TO_MAIN_MENU = ("Вы вернулись в главное меню") 
 
    UNKNOWN_COMMAND = ("Неизвестная команда") 
     
    GET_COMPANES = ("Спасибо, мы получили Ваши компании, теперь поиск будет производиться по данным компаниям:") 
 
    CONTACTS_BTN = ("Контакты") 
 
    CONTACTS = ("Если у Вас возникли вопросы или предложения, напишите пожалуйста сюда:\n" 
                "Григорий - @CucumberMayoo\n" 
                "Андрей - @NightsForever") 
 
    USAGE_BTN = ("Правило использования") 
 
    USAGE = ("Мы подготовили для Вас краткий чек-лист, в котором подробно написано как пользоваться этим ботом:\n" 
             "\nДля добавления новой компании нажми в главном меню кнопку ___ (дополнить этот моментик)\n\n" 
             "Для получения характера упоминания компании в статье, в главном меню нажми кнопку анализ, затем" 
             " выбери нужную компанию, а после отправь ссылку на статью") 
     
     
    SEND_AN_ARTICLE = ("Отправьте статью, анализ которой, будет проводиться") 
 
    BOT_RESPONSE = ("Статья получена! Компания упоминается ")