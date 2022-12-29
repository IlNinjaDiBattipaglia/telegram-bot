from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "Enter your token"

def start(update, context):
    update.message.reply_text("Enter the message of the start")

def rispondi(update, context):
    testo = update.message.text.lower()
    if "word" in testo:
        update.message.reply_text("reply")
    elif "word" in testo:
        update.message.reply_text("reply")
    elif "word" in testo:
        update.message.reply_text("reply")
updater = Updater(TOKEN)
updater.dispatcher.add_handler (CommandHandler('start', start))
updater.dispatcher.add_handler (MessageHandler(Filters.text, rispondi))
print("Bot in ascolto....")
updater.start_polling()
