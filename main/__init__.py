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
BOT_TOKEN = "6783282067:AAG4PP79fn4JVeyQ1j3iXjN7BoMF6bwpais"
SESSION = "BQCMLuIAF0Rda7B4qb-gI_rpLNFa9wnXdQRfoK00Q5yEg_v8rPo2CkFTX64U7Z_fmO0aAwlsOQ0LASEWAmclknW-U_CuSovHPOdfAjJUJrfWwC0gf-Y1cOqqa49KZfgG9lvqIgvJ-3FAoLn7H7OuBAqw4NXtQTyrtuOnduDs9qOs0hhRDc_QooWk8UQMwWX225EVZYW7shPi1l8Nv53Vsh772Bj51ezqKkr0yfJ1E3LjsCQDda9y2bq1X5GDyfyN5pBB1gijWxSJKe33VH9AngPz0D3n-fe1iTUwWNdsiDXG9mDKGrlQ1ckl7-tXXt1YIm9SY4tmqmMDTy1p6DEMHpidx6fVRAAAAAGX-jAhAA"
FORCESUB = "forcesubpavo4"
AUTH = 6356781743
DB_CHANNEL = -1002010535930
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
