from dotenv import load_dotenv
import os

load_dotenv()

import telebot
bot = telebot.TeleBot(os.getenv('TOKEN'))

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'hi':
        bot.send_message(message.from_user.id, 'hi, can i help you?')
    else:
        bot.send_message(message.from_user.id, 'anything else?')

bot.polling(none_stop=True, interval=0)