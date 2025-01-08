import telebot
from googletrans import Translator

API_TOKEN = '7402774915:AAE7h-yNvMxxHKE8UfCf16slajYpQ48YYfw'

bot = telebot.TeleBot(API_TOKEN)

translate = Translator()


@bot.message_handler(commands=['start'])
def start_Bot(message):
    bot.reply_to(message , 'Hi\nhow can i help you?')

@bot.message_handler(commands=['help'])
def help_Bot(message):
    bot.reply_to(message , 'Hi\nhow can i help you?')


@bot.message_handler(func=lambda message:True)
def wellcome_mesage(message):
    translated_text = translate.translate(message.text , src='en' , dest='fa')
    bot.reply_to(message , translated_text.text)

bot.infinity_polling()