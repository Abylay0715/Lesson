import telebot
from telebot import types
bot = telebot.TeleBot('6000421821:AAFEBRJzx7nAPmT58U6skw3YJjBBK3CHofY')


@bot.message_handler(commands=['start'])
def kno(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Monday = types.KeyboardButton(text='1')
    Tuesday = types.KeyboardButton(text='2')
    Wednesday = types.KeyboardButton(text='3')
    Thursday = types.KeyboardButton(text='4')
    Friday = types.KeyboardButton(text='5')


    markup.add(Monday, Tuesday, Wednesday, Thursday, Friday)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == '1':
        bot.send_message(message.chat.id, text = """
1)Global evolution 344, (10-11)
2)Phizika lecture 414, (12-13)
3)phizika practice 441, (15-16)
 """)
    elif message.text == '2':
        bot.send_message(message.chat.id, text="""
1)Calculus 2 lecture 428 (10-11)
2)Calculus 2 lecture 428 (10-11)
3)phizika Labaratory 327 (14-16)
             """)
    elif message.text == '3':
        bot.send_message(message.chat.id, text="""
1)Global evolution 344, (10-11)
2)Statistics lecture 428 (11-12)
3)Statistics lecture 428 (12-13)
             """)
    elif message.text == '4':
        bot.send_message(message.chat.id, text="""
1)PP2 lecture 428 (10-11)
2)PP2 lecture 428 (11-12)
3)Statistics practice 217 (12-13)
             """)
    elif message.text == '5':
        bot.send_message(message.chat.id, text="""
1)Global evolution 344, (10-11)
2)PP2 practice 380 (12-13)
3)PP2 practice 380 (13-14)
                 """)

if __name__ == '__main__':
    bot.polling(none_stop=True)