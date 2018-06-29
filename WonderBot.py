from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegit
import teleweather
import telenews
import telecom
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


logger = logging.getLogger(__name__)


start_message = """ Hi! My name is Wonder Bot. I will help you find some basic stuff.Send /done to stop talking to me.Use these commands to control me:
These are some of the stuff i am able to perform at the moment.
/hello - greetings from me! :)
/github <username> - To know about your github Repos and Starred repos
/news - get some live news feed
/weather - get the weather forecast of your area
/cubicom - get the upcoming cubing events in your area
/help - show the list of commands
\n
"""


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def facts_to_str(user_data):

    facts = list()
    for key,data in enumerate(user_data, 1):
        facts.append('{} - {}'.format(key, data))

    return "\n".join(facts).join(['\n', '\n'])


def button(bot, update):
    query = update.callback_query

    bot.editMessageText(text= " %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)


def start(bot, update):
    update.message.reply_text(start_message)


def done(bot, update):
    user = update.message.from_user
    update.message.reply_text("Bye! Hope to see you soon. Have a nice day {} .".format(user.first_name))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def github(bot, update, args):
        """ It returns information about the github user repos and starred repositories"""
        args = "".join(args)
        keyboard = [[InlineKeyboardButton("github repos", callback_data='repos')],[InlineKeyboardButton("github stars", callback_data='stars')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Wait, I am getting your :', reply_markup=reply_markup)
        url = "https://api.github.com/users/{}/repos".format(args )
        profile = telegit.get_repos(url)
        update.message.reply_text(profile)
        url = "https://api.github.com/users/{}/starred".format(args)
        profile = telegit.get_starred(url)
        update.message.reply_text(profile)


def news(bot, update):
    """To get the top stories"""
    feed = telenews.get_news()
    update.message.reply_text(facts_to_str(feed))


def weather(bot, update):
    """Get weather forecast of your area"""
    temp, humidity, pressure, wspeed, wdegree, longitude, latitude, desc, city = teleweather.get_weather()
    update.message.reply_text("\nCity : {}\nLatitude : {} degrees\nLongitude : {} degrees\nTemperature : {} degree celcius\nHumidity : {} g/m^3\nPressure : {} mBar\nWind Speed : {} mph\nWind degree : {} degrees\nDescription : {}".format(city, latitude, longitude, temp, humidity, pressure, wspeed, wdegree, desc))


def cubicom(bot, update):
    """ get the upcoming cubing competitions around your area"""
    comps = telecom.get_comps()
    update.message.reply_text(facts_to_str(comps))


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("595350816:AAGI_0cnuHgnBFqEZ7owyjHXSA_PyO_Cbsc")
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('github', github, pass_args = True))
    updater.dispatcher.add_handler(CommandHandler('news', news))
    updater.dispatcher.add_handler(CommandHandler('weather', weather))
    updater.dispatcher.add_handler(CommandHandler('cubicom', cubicom))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
