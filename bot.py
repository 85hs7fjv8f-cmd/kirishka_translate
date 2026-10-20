import os
import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
import threading

TOKEN = os.environ.get('TELEGRAM_TOKEN')
WEB_APP_URL = "https://indexhtml-sigma-dusky-70.vercel.app"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=WEB_APP_URL)
    markup.add(InlineKeyboardButton("Открыть переводчик", web_app=web_app))
    
    bot.send_message(
        message.chat.id, 
        "Привет! Нажми на кнопку ниже, чтобы открыть приложение.", 
        reply_markup=markup
    )

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    t = threading.Thread(target=run_flask)
    t.start()
    print("Бот запущен...")
    bot.infinity_polling()
