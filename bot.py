from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
import ephem
import datetime


PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}


date = datetime.datetime.now().strftime('%d.%m.%Y')


def greet_user(bot, update):
    text='Приветствую, '+ update['message']['chat']['username']+'!'
    print(text, update)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def get_planet (bot, update):
    planet_name = update.message.text.split()[1]
    planet = getattr(ephem, planet_name,'try another planet')
    constellation = ephem.constellation(planet(date))
    print (planet_name, date, constellation)
    update.message.reply_text(constellation)




def main():
    mybot=Updater('605962200:AAFpd_mhYS7RCP8D7_sA6u1wsCd1i6nqHTg', request_kwargs=PROXY)
    
    dp=mybot.dispatcher
    #когда пользователь нажимает команду "старт", его приветствуют
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()

main()

