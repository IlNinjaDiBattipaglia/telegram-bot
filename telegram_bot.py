from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "5726874288:AAGfl7MKfmFhEQ8x4LkrVmIoQKuRpnH0XE8"

def start(update, context):
    update.message.reply_text("Bellaaaaaaaaaaa, parole chiave sono vaffanculo, dove sei e che ore sono")

def rispondi(update, context):
    testo = update.message.text.lower()
    if "vaffanculo" in testo:
        update.message.reply_text("Ma vacci tu a fare in culo assieme a tua madre")
    elif "dove sei" in testo:
        update.message.reply_text("Fatti un poco i cazzi tuoi")
    elif "che ore sono" in testo:
        update.message.reply_text("L'ora che ti compri un orologio")
updater = Updater(TOKEN)
updater.dispatcher.add_handler (CommandHandler('start', start))
updater.dispatcher.add_handler (MessageHandler(Filters.text, rispondi))
print("Bot in ascolto....")
updater.start_polling()
