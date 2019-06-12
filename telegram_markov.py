import pickle
import pandas as pd
import markovify
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
df = pd.read_csv("wiki_movie_plots_deduped.csv")
def Model(msg):
        corpus = list(df.Plot)
        example = markovify.Text(corpus)
        plot = example.make_sentence()
        return plot

updater = Updater(token='851227046:AAH5_p3gvo2hoClaj6CSwSzIMdYleva8gHs')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Generate a crazy movie plot with Markov Chain')

def textMessage(bot, update):
    custom_keyboard = [['Press']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    plot = Model(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=plot, reply_markup=reply_markup)


start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()
