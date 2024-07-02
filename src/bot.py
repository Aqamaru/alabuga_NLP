import keyboards as Keyboards 
from text import Text 
from telebot import TeleBot, types 
from telebot.types import Message 
 
 
BOT : TeleBot = TeleBot("7099811190:AAEwZY5cHq4aiuI7YvBt__uTwBTevQB_QCs") 
 
COMPANIES : list[str] = [] 
 
 
@BOT.message_handler(commands = ['start']) 
def on_start(msg: Message) -> None:  
 
    BOT.send_message(msg.chat.id, text = Text.START_MESSAGE, 
                     reply_markup = Keyboards.START) 
 
@BOT.message_handler(commands = ['help']) 
def on_help(msg: Message) -> None: 
    pass 
 
@BOT.message_handler(commands = ['companies']) 
def on_companies(msg: Message) -> None: 
    pass 
 
@BOT.message_handler(commands= ['analysis']) 
def on_analysis(msg: Message) -> None: 
 
    BOT.send_message(msg.chat.id, text = msg.text) 
 
@BOT.message_handler(content_types=['text']) 
def on_message(msg: Message) -> None: 
 
    match msg.text: 
 
        case Text.ANALYSIS_BTN: 
            BOT.send_message(msg.chat.id, text = Text.ANALYSIS, 
                             reply_markup = Keyboards.ANALYSIS) 
            return 
         
        case Text.BACK_TO_MAIN_MENU_BTN: 
            BOT.send_message(msg.chat.id, text = Text.BACK_TO_MAIN_MENU, 
                             reply_markup = Keyboards.START) 
            return 
 
        case Text.HELP_BTN: 
            BOT.send_message(msg.chat.id, text = Text.HELP, 
                             reply_markup = Keyboards.HELPS) 
            return 
         
        case Text.CONTACTS_BTN: 
            BOT.send_message(msg.chat.id, text = Text.CONTACTS, 
                             reply_markup = Keyboards.START) 
            return 
         
        case Text.USAGE_BTN: 
            BOT.send_message(msg.chat.id, text = Text.USAGE, 
                             reply_markup = Keyboards.START) 
            return 
         
        case Text.SET_COMPANIES_BTN: # Кнопка в главном меню, добавляет в базу новую компанию для выбора 
            message = BOT.send_message(msg.chat.id, text = Text.SET_COMPANIES) 
            BOT.register_next_step_handler(message = message, callback=get_companes) 
            return 
         
        case Text.SET_COMPANIES_ANALYSIS_BTN: # Тут в аналитике выбирается компания, следом необходимо будет ввести ссылку на статью 
            message = BOT.send_message(msg.chat.id, text = Text.SET_COMPANIES_ANALYSIS, 
                                        reply_markup = Keyboards.ANALYSIS) 
             
            # вывод кнопок с компаниями, после вывод просьбы вывести статью =>  
            # => BOT.send_message(message.chat.id, text = Text.SEND_AN_ARTICLE)  
 
            return 
         
 
        case _: 
            BOT.send_message(msg.chat.id, text = Text.UNKNOWN_COMMAND, 
                             reply_markup = Keyboards.START) 
            return 
         
def get_companes(message: Message) -> None: 
    global COMPANIES  
    COMPANIES +=  message.text.split() 
 
    BOT.send_message(message.chat.id, text = Text.GET_COMPANES + " " +  " ".join(COMPANIES)) 
 
 
BOT.infinity_polling()