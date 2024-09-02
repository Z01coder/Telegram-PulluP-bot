import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('ваш токен')
user_attempts = {}
@bot.message_handler(commands=['start']) #
def start_message(message):

        reminder_thread = threading.Thread(target=set_reminders, args=(message.chat.id,))
        reminder_thread.start()
        bot.send_message(message.chat.id,
    "Привет! Готов подтянуться? Тогда скорее прыгай на турник, "
        "а после этого, вне зависимости от результата, возвращайся и напиши 'Я турникмен!'")

@bot.message_handler(func= lambda message: message.text == "Я турникмен!")
def answer_yes(message):
    user_id = message.chat.id
    if user_id in user_attempts:
        user_attempts[user_id] += 1
    else:
        user_attempts[user_id] = 1
    bot.send_message(user_id, f"Количество успешных подходов уже: {user_attempts[user_id]}!")
    bot.reply_to(message, "Ты молодец! " + random.choice(facts))
facts = [
    "Подтягивания укрепляют мышцы спины, рук и плеч, "
    "помогая формировать сильное и подтянутое тело 💪.",
    "Регулярные подтягивания улучшают осанку и поддерживают "
    "здоровье позвоночника 🧍‍♂️.",
    "Подтягивания развивают силу хвата и выносливость, "
    "что полезно не только в спорте, но и в повседневной жизни 🏋️‍♂️."
]
def set_reminders(chat_id):
    st1_rem = "09:00"
    nd2_rem = "11:00"
    rd3_rem = "15:00"
    th4_rem = "20:12"
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == st1_rem or now == nd2_rem or now == rd3_rem or now == th4_rem:
            bot.send_message(chat_id, "Время подтянуться! Не забудь после "
                                      "подхода написать 'Я турникмен!'")
            time.sleep(60)
        time.sleep(1)

bot.polling(none_stop=True)
