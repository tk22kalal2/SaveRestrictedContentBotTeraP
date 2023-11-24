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
SESSION = "BQCMLuIAOjpNgP4rXUYxZUYwblGv63lfh7epfQFrAS-ip3e0Wid5-rF86t85noSWjPcvKqjrbU7ypBuTUvkrUdDmV4Sxi_rJLDovKHKhhRPzbUeJoG_QegiTQwWeKvcDx6YQwBd7SsyCXD9mPdwHxWEgV3lD-lY-WtwIdlGyH5tpEd4Vyncg_4Wq-PN8OVtp4tGbsuA-_EJrR0as51Y2ax1Mconxj_BZ2R_zAfyxgU1CES-Dh2U43_OrdSHlk1QgSJrTrRUGRE5Z_4p0aKAk9xu1JwV80DdgrMFssqUiVFptpMKWe4qdFiIULYt_nhpL3AS0eX_K-IBIb0ygUObux5tphPfkigAAAAF65MqvAA"
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
