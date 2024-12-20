import confige
import telebot
import sqlite3 

bot = telebot.TeleBot(confige.token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
                Привет, это бот-техподдержка онлайн магазина!\
                Мы вам поможем ответив на ваши вопросы или же свяжем вас с спициалистами\
""")
    
@bot.message_handler(commands=['help', 'comands'])
def send_welcome(message):
    bot.reply_to(message, """\
                Команды бота: "", ""\
""")
    
def info_project(message):
    info = manager.get_question_answer()
    if not info:
        info = 'Обрабатываем ваш запрос'
