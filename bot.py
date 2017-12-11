import telebot

token = "Token"

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start', 'help','anek','pic'])
def help(message):
    user = message.chat.id
    if message.text == "/start":
        bot.send_message(user, "Привет, спасибо что решил зайти ко мне! \nЯ могу прислать тебе смешной анекдот, если ты напечатаешь команду /anek, \nили же поделиться актуальным мемом, если ты напечатаешь команду /pic. ")
    if message.text == "/help":
        bot.send_message(user, "Я не помогаю глупым")
    if message.text == "/anek":
        bot.send_message(user, "Лови анекдот")
        bot.send_message(user, 'Купил мужик шляпу, а она ему как раз')
    if message.text == "/pic":
        bot.send_message(user, "Лови мемас")
        bot.send_photo (user, 'https://68.media.tumblr.com/de444125f77aa2361812c61137dd8519/tumblr_nmx7dqiC8s1se177do1_500.jpg')
# content_types=['text'] - сработает, если нам прислали текстовое сообщение
@bot.message_handler(content_types=['text'])
def echo(message):
    # message - входящее сообщение
    # message.text - это его текст
    # message.chat.id - это номер его автора
    text = message.text
    user = message.chat.id

    #отправляем картинку с попугаем
    bot.send_photo(user, "http://popygau.ru/wp-content/uploads/2016/03/maxresdefault.jpg")

    #отправляем сообщение тому же пользователю с тем же текстом
    bot.send_message(user, text)

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)
