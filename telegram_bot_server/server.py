import telebot;
import threading
import time
import psycopg2


bot = telebot.TeleBot('6001720319:AAFMmaYqNGUc6oGNis3XzpG8Czxuusw1opc')
conn = psycopg2.connect(dbname='SIPI', user='postgres',
                        password='postgres', host='127.0.0.1', port='5432')

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"""Чел... Ты теперь подписан на рассылку предсказаний акций раз день. 
  Но для того чтобы она заработала нужно на сайте ввести свой телеграмм id\n
  Еблуша, твой id кстати - """ + str(message.chat.id))


def start_send_timer():
  while True:
    send_mailing()
    time.sleep(60*60)
def send_mailing():
  global bot
  cursor = conn.cursor()
  cursor.execute('SELECT id, telegramid FROM users WHERE sendmailing is true and telegramid is not null')
  records = cursor.fetchall()
  for el in records:
    cursor.execute("""SELECT t2.stocksymbol FROM target_stocks as t1 LEFT JOIN stocks as t2 
    on t1.fkstock = t2.id WHERE t1.fkuser = %s""", (el[0], ));
    ts = cursor.fetchall()
    messageText = 'Прогноз акций на сегодня:\n'
    for elTs in ts:
      messageText += elTs[0] + ' - 100p\n'
    print(el[1])
    print(messageText)
    bot.send_message(int(el[1]), messageText)
  #print(records)
  cursor.close()

def start_bot():
  bot.polling(none_stop=True, interval=0)

if __name__ == '__main__':
  t1 = threading.Thread(target=start_bot, daemon=True)
  t2 = threading.Thread(target=start_send_timer, daemon=True)
  t2.start()
  t1.start()
  t2.join()
  t1.join()

