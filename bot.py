from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot token va admin ID
TOKEN = "7938346036:AAHtkDx0mZQz3uRrjGKZ1f07Dy_gTRRTims"
ADMIN_ID = 7098943602
SITE_URL = "https://resonant-squirrel-f2fb6a.netlify.app"

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.username or f"id{user.id}"
    name = user.first_name

    # Salomlashish xabari va tugma
    msg = f"Salom, {name}!\nSiz UC ishlashingiz mumkin."
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Boshlash", url=f"{SITE_URL}/?user={username}")]
    ])
    await update.message.reply_text(msg, reply_markup=keyboard)

# Botni ishga tushirish
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
