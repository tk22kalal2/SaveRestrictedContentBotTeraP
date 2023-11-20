#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28698132
API_HASH = "1a2837cd39f87e9b224710af8acd13de"
BOT_TOKEN = "6838710773:AAFeCymPSrz3TqUGQG2y1uEgglpsFGbN0BA"
SESSION = "BQA6lfzC4oyhoFepMOjAzK8WaV03mmwq6EgVrY6iKweNh-WmIwn7nYUPejJEdCig0cD1D85f0H0iKJlgDqnb8Ig8Nom7SZdBTnMbyJi9blfnnrMY9ddZj6oran9V9_z0KtLXKNSE1EvmEw1kxgtULdtDYEMyO-r4aOR8MXnaY0Cx0k1_nG1zF6QdG3jBAXSd6oTGZhdp7XIA8KfPNiobSnQDi_QYnLzEKrbTgeKmaN3fI5ZFLtOlT94KsqIsmAqJwCZi9kMW1D81geGevZGx-U9ntFCukiAqcM5oqevBLBBD0Y2u2nt2e7FFu7CNhg5L70KgqlrTHcdbDGFe02msPYsoAAAAAZ-F-NAA"
FORCESUB = "forcesubpavo"
AUTH = 6971324624

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
