"""
Exemple des notions du chapitre 7.
"""


from chatbot import *
from twitch_bot import *


def build_say_hi_callback(bot, message):
	def callback(oauth:h6uxc1fszs0xyglz5lov1jgzb1zgln):
		bot.send_privmsg(message)
        return callback

def run_ch7_example():
	bot = TwitchBot("logs")
	# TODO: Construire le callback avec le bot et un message de votre choix.
	callback = ...
	# TODO: Enregister le callback sous la commande "say_hi".
	bot.register_command(...)
	# TODO: Mettre votre jeton (incluant le "oauth:") et le nom du compte Twitch associé.
	bot.connect_and_join("oauth:...", "...", "samsei109")
	bot.run()

