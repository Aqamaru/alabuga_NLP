from text import Text
from keyboards import Keyboards
from telebot import TeleBot
from telebot.types import Message


BOT : TeleBot = TeleBot("7099811190:AAEwZY5cHq4aiuI7YvBt__uTwBTevQB_QCs")


@BOT.message_handler(commands=['start'])
def on_start(msg: Message) -> None: 

    BOT.send_message(msg.chat.id, text = Text.START_MESSAGE,
                     reply_markup = Keyboards.START) 

@BOT.message_handler(content_types=['text'])
def on_message(msg: Message) -> None:

    match msg.text:

        case Text.ANALYSIS_BTN:
            BOT.send_message(msg.chat.id, text = Text.ANALYSIS,
                             reply_markup = Keyboards.ANALYSIS)
            return

        case Text.SET_COMPANIES_BTN:
            return
        
        case Text.BACK_TO_MAIN_MENU_BTN:
            BOT.send_message(msg.chat.id, text = Text.BACK_TO_MAIN_MENU,
                             reply_markup = Keyboards.START)
            return
            
        case Text.HELP_BTN:
            return

        case _:
            return


def start_bot() -> None:
    BOT.infinity_polling()
    
