import html
import telebot
import telegram.tgConfig as tgConfig
from members import memberProcessing
import tgProcessing as tg
import numpy as np

bot = telebot.TeleBot(tgConfig.TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    obj = tg.dataProcessing("#2QLRR8U9U")
    table = obj.getTelegramMessageMemberDonations()
    bot.reply_to(message,table)
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()