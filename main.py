#!/usr/bin/python3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import psutil
import os

updater = Updater(token='TOKEN', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher


def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="OK!")
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()

#battery
def convertTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return "%d:%02d:%02d" % (hours, minutes, seconds)

battery = psutil.sensors_battery()
bat=(battery.percent)

def battery(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=bat)
battery_handler = CommandHandler('battery', battery)
dispatcher.add_handler(battery_handler)
updater.start_polling()

#shutdown
def shutdown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=os.system('sudo shutdown now'))
shutdown_handler = CommandHandler('shutdown', shutdown)
dispatcher.add_handler(shutdown_handler)
updater.start_polling()