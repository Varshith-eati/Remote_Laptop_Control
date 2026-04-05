import os
import psutil
import pyautogui
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8076710235:AAFt0LnGTsB41pw-YQmhLONLLo2lmmpKHjg"
AUTHORIZED_USER = 1166325884


def authorized(update: Update):
    return update.effective_user.id == AUTHORIZED_USER


# ---------------- COMMANDS ---------------- #

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("Laptop control bot ready 😎")


async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("Shutting down...")
    os.system("shutdown /s /t 1")


async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("Restarting...")
    os.system("shutdown /r /t 1")


async def open_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    app = " ".join(context.args)
    os.system(f"start {app}")
    await update.message.reply_text(f"Opening {app}")


async def type_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    text = " ".join(context.args)
    pyautogui.write(text)
    await update.message.reply_text("Typed!")


async def screenshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    img = pyautogui.screenshot()
    img.save("screen.png")
    await update.message.reply_photo(photo=open("screen.png", "rb"))


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update):
        return

    cpu = psutil.cpu_percent(interval=1)
    cores = psutil.cpu_count()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()

    msg = f"🖥 CPU Usage: {cpu}%"
    msg += f"\n🧠 CPU Cores: {cores}"
    msg += f"\n💾 RAM Usage: {ram.percent}%"
    msg += f"\n📂 Disk Used: {disk.percent}%"

    if battery:
        msg += f"\n🔋 Battery: {battery.percent}%"

        if battery.power_plugged:
            msg += "\n🔌 Power: Charging"
        else:
            msg += "\n❌ Power: Not Charging"

        if battery.secsleft not in (psutil.POWER_TIME_UNKNOWN, psutil.POWER_TIME_UNLIMITED):
            mins = battery.secsleft // 60
            hrs = mins // 60
            mins = mins % 60
            msg += f"\n⏳ Time Left: {hrs}h {mins}m"
    else:
        msg += "\n🔋 Battery: Not detected"

    await update.message.reply_text(msg)


async def stopbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not authorized(update): return
    await update.message.reply_text("Stopping bot...")
    os._exit(0)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Unknown command")


# ---------------- MAIN ---------------- #

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shutdown", shutdown))
    app.add_handler(CommandHandler("restart", restart))
    app.add_handler(CommandHandler("open", open_app))
    app.add_handler(CommandHandler("type", type_text))
    app.add_handler(CommandHandler("screenshot", screenshot))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("stopbot", stopbot))

    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
