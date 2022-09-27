import telebot
from telebot import types # для указание типов
import config
import time
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters

bot = telebot.TeleBot(token = "5586426259:AAFU0u5rWjCK1KI_zsPVZmmQjKxZ3fUZ_FU")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать❤")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, я хочу тебе кое-что передать!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Узнать❤"):
        bot.send_message(message.chat.id, text="Дело в том-что...")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEF7yxjMdHsGFvTiRj3RKwTsxfh3zsYWAAC_QEAAnLWYjcmhqmr42OhIykE")
        time.sleep(1)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEF7zJjMdJdiYTMRtDjR6ierjvD1mWfSwAC_gEAAnLWYjfulj_5_copsikE")
        time.sleep(1)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEF7zpjMdL-3FanafuoLw9XCS14oLAZhgACBQIAAnLWYjecSst7ZNKKUSkE")
        time.sleep(1)
        chatId = message.chat.id
        bot.send_audio(chatId, open("file.mp3", 'rb'))
    


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()





bot.polling(none_stop=True)