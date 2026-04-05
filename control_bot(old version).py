# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import os
# import subprocess
# import pyautogui
# import psutil

# TOKEN = "8076710235:AAFt0LnGTsB41pw-YQmhLONLLo2lmmpKHjg"
# AUTHORIZED_USER = 1166325884

# def authorized(update):
#     return update.message.from_user.id == AUTHORIZED_USER

# def start(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Laptop control bot ready 😘😎✨✨")
    
# def shutdown(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Shutting Down...")
#     os.system("shutdown /s /t 1")
    
# def restart(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Restarting...")
#     os.system("shutdown /r /t 1")
    
# def openapp(update, context):
#     if not authorized(update): return
#     app = " ".join(context.args)
#     subprocess.Popen(app)
#     update.message.reply_text(f"Opening {app}")
    
# def type_text(update, context):
#     if not authorized(update): return
#     text = " ".join(context.args)
#     pyautogui.write(text)
#     update.message.reply_text("Typed!!!")
    
# def screenshot(update, context):
#     if not authorized(update): return
#     image = pyautogui.screenshot()
#     image.save("screen.png")
#     context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("screen.png", "rb"))
    
# def status(update, context):
#     if not authorized(update): return
#     battery = psutil.sensors_battery()
#     cpu = psutil.cpu_percent()
#     msg = f"CPU: {cpu}%\nBattery: {battery.percent}%"
#     update.message.reply_text(msg)
    

# def unknown(update, context):
#     update.message.reply_text("Unknown command")
    
# updater = Updater(TOKEN, use_context = True)
# dp = updater.dispatcher

# dp.add_handler(CommandHandler("start", start))
# dp.add_handler(CommandHandler("shutdown", shutdown))
# dp.add_handler(CommandHandler("restart", restart))
# dp.add_handler(CommandHandler("open", openapp))
# dp.add_handler(CommandHandler("type", type_text))
# dp.add_handler(CommandHandler("screenshot", screenshot))
# dp.add_handler(CommandHandler("status", status))
# dp.add_handler(MessageHandler(Filters.command, unknown))

# print("Bot Running...")
# updater.start_polling()
# updater.idle()

# (OR)

# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# import os
# import pyautogui
# import psutil

# TOKEN = "PASTE_NEW_TOKEN"
# AUTHORIZED_USER = 1166325884

# def authorized(update):
#     return update.message.from_user.id == AUTHORIZED_USER

# def start(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Laptop control ready 😘😎✨✨")

# def shutdown(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Shutting Down...")
#     os.system("shutdown /s /t 1")

# def restart(update, context):
#     if not authorized(update): return
#     update.message.reply_text("Restarting...")
#     os.system("shutdown /r /t 1")

# def openapp(update, context):
#     if not authorized(update): return
#     app = " ".join(context.args)
#     os.system(f"start {app}")
#     update.message.reply_text(f"Opening {app}")

# def type_text(update, context):
#     if not authorized(update): return
#     text = " ".join(context.args)
#     pyautogui.write(text)
#     update.message.reply_text("Typed!")

# def screenshot(update, context):
#     if not authorized(update): return
#     image = pyautogui.screenshot()
#     image.save("screen.png")
#     context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("screen.png", "rb"))

# def status(update, context):
#     if not authorized(update): return
#     cpu = psutil.cpu_percent()
#     battery = psutil.sensors_battery()

#     msg = f"CPU: {cpu}%"
#     if battery:
#         msg += f"\nBattery: {battery.percent}%"

#     update.message.reply_text(msg)

# def unknown(update, context):
#     update.message.reply_text("Unknown command")

# updater = Updater(TOKEN, use_context=True)
# dp = updater.dispatcher

# dp.add_handler(CommandHandler("start", start))
# dp.add_handler(CommandHandler("shutdown", shutdown))
# dp.add_handler(CommandHandler("restart", restart))
# dp.add_handler(CommandHandler("open", openapp))
# dp.add_handler(CommandHandler("type", type_text))
# dp.add_handler(CommandHandler("screenshot", screenshot))
# dp.add_handler(CommandHandler("status", status))
# dp.add_handler(MessageHandler(Filters.command, unknown))

# print("Bot Running...")
# updater.start_polling()
# updater.idle()
