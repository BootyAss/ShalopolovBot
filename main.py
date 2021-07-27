from math import floor
from random import random
from telebot import types, TeleBot
from descs import data, startValues

bot = TeleBot(token='1924703853:AAHglk4Jw8ilRx4MYsLpr3FC1POnYRuj00w')


@bot.message_handler(commands=['start'])
def welcome(msg):
    chat = msg.chat

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('го')

    with open(f'{chat.id}.txt', 'w') as file:
        for i in startValues:
            file.write(str(i)+'\n')

    markup.add(item)

    bot.send_message(
        chat.id,
        f'Привет, {chat.first_name}\nЯ тестовая хуета по случаю др Андрея\nТут пока что все, что смог откопать')

    bot.send_message(
        chat.id,
        f'Напиши "го" и получи рандомную фотку с Андреем',
        reply_markup=markup)


@bot.message_handler(content_types=['text'])
def parse(msg):
    chat = msg.chat
    text = msg.text.lower()

    if text == 'го':
        with open(f'{chat.id}.txt', 'r') as file:
            values = [int(x[:-1]) for x in file.readlines()]

        if len(values) == 0:
            startValues = [i+1 for i in range(62)]
            with open(f'{chat.id}.txt', 'w') as file:
                for i in startValues:
                    file.write(str(i)+'\n')
            bot.send_message(chat.id,
                             text='Все фотки просмотрены, пустил все по новой')
            return

        index = floor(random()*len(values))
        photo_id = values[index]

        del values[index]
        with open(f'{chat.id}.txt', 'w') as file:
            for i in values:
                file.write(str(i)+'\n')
        desc = ''
        for item in data:
            if int(item['id']) == photo_id:
                desc = item['desc']
                break

        bot.send_photo(chat.id,
                       photo=open(f'./data/photo' +
                                  '{:03d}'.format(photo_id) + '.jpeg', 'rb')
                       )
        if desc:
            bot.send_message(chat.id,
                             text=f'{desc}')


bot.polling()
