import logging
from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("Bot actif. Je publie les nouveaux animes automatiquement !")

def main():
    from os import getenv

    token = getenv("BOT_TOKEN")
    if not token:
        print("Erreur : token introuvable.")
        return

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot actif. Surveillance des nouveaux épisodes...")
    app.run_polling()

if __name__ == "__main__":
    main()
