from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from _datetime import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.now().strftime("%d-%m-%Y; %H:%M: ")}{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()
