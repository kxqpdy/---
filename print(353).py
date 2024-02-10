import telebot

bot = telebot.TeleBot("6366348527:AAFcFWXB57aK06gZFdRn-Bdc0YNVcijb0C0")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет")
    else:
        bot.send_message(message.from_user.id, "Мой разраб ещё работает над этой функцией")

bot.polling(none_stop=True, interval=10)