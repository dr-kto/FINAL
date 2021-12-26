import eel
import telebot

TOKEN = "1990527566:AAEOHVU71WKFHttlWCWNo9uisa_A8cchrUQ"

bot = telebot.TeleBot(TOKEN)

@eel.expose
def send_message(chat_id, message):
    bot.send_message(chat_id, message)
    return "Cooбщение отправлено!"

@eel.expose
def send_video(chat_id, file):
    bot.send_video(chat_id, file)
    return "Видео отправлено!"

@eel.expose
def send_photo(chat_id, path):
    bot.send_photo(chat_id, path)
    return "Фото отправлено"

eel.init("web")
eel.start("index.html", size = (400, 600), mode="edge")
