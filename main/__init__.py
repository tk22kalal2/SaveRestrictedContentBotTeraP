#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24058425
API_HASH = "694b063e55c24287a3d30aed90191373"
BOT_TOKEN = "6802436912:AAG8YFXKZZMduxzHAOFTqS0b87qAwrjpoO0"
SESSION = "BQCMLuIAfJeqvmuz0GCwQ1C63gOzl20eoeCvHLbhUDPxdV5-IA3s6bQvItA8RkbAbS-FOKS9R3hruobuGAfnZ_bbDVzfj2_s5L2t8CNdpPKhBgfBcZJWWVHFvFdd9WqR2L0jH_wY-rbctgxewO7xgwgdnJL5n1zkQF57TSiM2T_MxzAxMz4tLP_Q8o-qYbqyVwTWcyxv-nCUPRhIG4HCMjujxBXcIEN89yf18Jg8WtQSBTIT9pQM7ZXaE6u92qFALQe4irvjZ6cCms9LKGb3fsOcyy53Cov9TZ-Bs8qWdRCdNl2mdLznJImoIHt3-0imVg1NbE24g36DKeZMaJeEeCHERl7hxwAAAAF65MqvAA"
FORCESUB = "forcesubpavo3"
AUTH = 6356781743
DB_CHANNEL = -1002039233060
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
