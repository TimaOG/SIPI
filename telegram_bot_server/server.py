import telebot;
import threading
import time
import psycopg2


bot = telebot.TeleBot('6001720319:AAFMmaYqNGUc6oGNis3XzpG8Czxuusw1opc')
conn = psycopg2.connect(dbname='stocks', user='postgres',
                        password='postgres', host='127.0.0.1', port='5432')

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Чел... Ты теперь подписан на рассылку предсказаний акций раз день. Но для того чтобы она заработала нужно на сайте ввести свой телеграмм id")


def start_bot():
  bot.polling(none_stop=True, interval=0)

def start_send_timer():
  while True:
    send_mailing()
    time.sleep(60*60)
def send_mailing():
  cursor = conn.cursor()
  cursor.execute('SELECT id, telegramid FROM users WHERE sendmailing = true and telegramid != null')
  records = cursor.fetchall()
  cursor.close()

if __name__ == '__main__':
  t1 = threading.Thread(target=start_bot, daemon=True)
  t2 = threading.Thread(target=start_send_timer, daemon=True)
  t1.start()
  t2.start()
  t1.join()
  t2.join()

