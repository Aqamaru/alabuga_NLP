import keyboards as Keyboards
from text import Text
from telebot import TeleBot, types
from telebot.types import Message


BOT : TeleBot = TeleBot("7099811190:AAEwZY5cHq4aiuI7YvBt__uTwBTevQB_QCs")
COMPANY  = ["ВК", "Сбербанк", "Тбанк", "Ютуб", "Тикток"]

COMPANIES : list[str] = []


@BOT.message_handler(commands = ['start'])
def on_start(msg: Message) -> None: 

    BOT.send_message(msg.chat.id, text = Text.START_MESSAGE,
                     reply_markup = Keyboards.START) 
    
    BOT.reply_to(Message, "Здравствуй! Тебя приветствует бот команды Ин су лин, прежде чем пользоваться мной, советую ознакомиться с правилами (/help), чтобы не запутаться")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn = types.KeyboardButton("Добавить компанию")
    markup.add(btn)

    for i in COMPANY:
        btn = types.KeyboardButton(i)
        markup.add(btn)

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

        case Text.SET_COMPANIES_BTN:
            return
        
        case Text.BACK_TO_MAIN_MENU_BTN:
            BOT.send_message(msg.chat.id, text = Text.BACK_TO_MAIN_MENU,
                             reply_markup = Keyboards.START)
            return

        case Text.HELP_BTN:
            BOT.send_message(msg.chat.id, text = Text.HELP,
                             reply_markup = Keyboards.START)
            return

        case _:
            BOT.send_message(msg.chat.id, text = Text.UNKNOWN_COMMAND,
                             reply_markup = Keyboards.START)
            return

BOT.infinity_polling()
    
