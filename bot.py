from telegram.ext import Updater, CommandHandler
import requests

def grabStars(bot, update):
	print(bot, update)
	stars = 0
	r = requests.get('https://api.github.com/orgs/JBossOutreach/repos').json()

	for repo in r:
		stars += repo['stargazers_count']

	update.message.reply_text(
        'JBossOutreach has {} stars!'.format(stars))

	return stars

updater = Updater('Your Token Here!')
updater.dispatcher.add_handler(CommandHandler('stars', grabStars))

updater.start_polling()
updater.idle()