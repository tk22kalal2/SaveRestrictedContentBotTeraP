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
BOT_TOKEN = "6703992527:AAGhh3nJssR-OFN5p1jnn3LhflP_lErMdj0"
SESSION = "BQAs5elmRJKYoKFqIfOUUpyCIDydkDVmPYBudI5Rc9G1gavJTfbqSSoUkO94UcG2QXjfU4aVsp3GTIl4TpTCCglH7P0fwngL9IbfCfji3AxyeQfLifEhhXAaf1Ql-sVPv5X-9iw2NQ_9uNg7szzYspcOZmqpdlJzdkNVx2_6oEOAiQWhYjr2S769JxJzYn11huhHodyBDaKxfv_a6Y_TF-mACAgw6G3lgAKzHQMpJHDnkJROSIktuVqeK4LqJV6fIlfm81WC3dFgGOnHbHnOO-5l2MwTCF_kS5SHPqNrAcMD9oj1HmVXTpoOm7o0XZdrTYeeG7K8E5glnS8A2ci0ZKsWAAAAAaAj3_oA"
FORCESUB = "forcesubpavo2"
AUTH = 6971324624
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
