import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Здравчтвуй новый пользователь это телеграм бот основаный на игре Поле чудес")



@bot.message_handler(content_types=["text"])
def handle_start(message):
    bot.send_message(message.chat.id, "не " + message.text)

bot.polling(none_stop=True)
