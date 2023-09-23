import database
import telebot
import time
import log
from telebot import types


token = '6599088530:AAG95c9zmMlD9A0YOGdhko05utXCPk5RIs4'

bot = telebot.TeleBot(token)
dataset = {}
pool = ["0", "0", "0"]


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Сообщить статус")
    btn2 = types.KeyboardButton("❓ Узнать статус")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я сообщаю информацию о наличии задания на основе крайней полученной "
                          "информации от других пользователей.".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Сообщить статус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Задание есть")
        btn4 = types.KeyboardButton("Задания нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4, back)
        bot.send_message(message.chat.id, text=f"Укажите ответ", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Сообщить статус")
        button2 = types.KeyboardButton("❓ Узнать статус")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif message.text == "Задание есть":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back1 = types.KeyboardButton("Вернуться в главное меню")

        pool.append(message.chat.id)
        pool.append(message.text)
        now_time = time.strftime("%H:%M:%S %d.%m.%Y")
        pool.append(now_time)
        database.add_data(pool)

        markup.add(back1)
        bot.send_message(message.chat.id, text="Спасибо, {0.first_name}! Информация добавлена в "
                                               "базу данных.".format(message.from_user), reply_markup=markup)

    elif message.text == "Задания нет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back2 = types.KeyboardButton("Вернуться в главное меню")

        pool.append(message.chat.id)
        pool.append(message.text)
        now_time = time.strftime("%H:%M:%S %d.%m.%Y")
        pool.append(now_time)
        database.add_data(pool)

        markup.add(back2)
        bot.send_message(message.chat.id, text="Спасибо, {0.first_name}! Информация добавлена в "
                                               "базу данных.".format(message.from_user), reply_markup=markup)

    elif message.text == "❓ Узнать статус":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back6 = types.KeyboardButton("Вернуться в главное меню")
        btn_stat = types.KeyboardButton("Статистика")
        markup.add(btn_stat, back6)
        bot.send_message(message.chat.id,
                         text=f"По последней информации от пользователя с ID: {database.view_users()[0][0]}"
                              f" на дату *{database.view_time()[0][0]}* ===>"
                              f" *{database.view_answear()[0][0]}*", parse_mode="Markdown", reply_markup=markup)

    elif message.text == "Статистика":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back5 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back5)
        bot.send_message(message.chat.id, text=f"{database.get_all()}", reply_markup=markup)

        print(database.get_all())

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Сообщить статус")
        btn2 = types.KeyboardButton("❓ Узнать статус")
        markup.add(btn1, btn2)
        now_time = time.strftime("%H:%M:%S %d.%m.%Y")
        log.write_log(message.text, message.from_user.first_name, now_time)
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован..", reply_markup=markup)


bot.polling(none_stop=True)
