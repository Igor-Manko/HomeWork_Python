from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command_list import *


app = ApplicationBuilder().token("5625416216:AAEvM_Tkh5tMt8-3pB03jbloLy0eRNWcOfY").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')
app.run_polling()

if __name__ == '__main__':
    main()