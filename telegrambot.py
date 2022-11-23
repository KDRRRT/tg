# 1 перенести словарь в базу данных (телеграм ид, слово, перевод
# 2 пофиксить и написать бот, чтобы выдавал команды: русское слово - перевод на вепсский, такого слова нет
# 3 проверить бот на роботоспособность, понять, как делиться ботом

import telebot

from tg_def import get_word

bot = telebot.TeleBot("5703002222:AAFp-EydFC7G9-y0psUeAiCsGh-v8k65030")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте. Данный бот является электронным '
                                      'аналогом русско-вепсского словаря. Для того, чтобы перевести '
                                      'необходимое слово напишите его на русском языке')


@bot.message_handler(func=lambda message: True, content_types=['text'])
def search(message):
    word = get_word(message.text)
    if word is not None:
        bot.send_message(message.chat.id, word)
    else:
        bot.send_message(message.chat.id, 'К сожалению, в словаре нет такого слова :(')


bot.infinity_polling()
