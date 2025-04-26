import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7896165148:AAFKmmxHT01cbgqPcuHpbigHnGETVO4vSk4')
    API_ID = int(os.environ.get("API_ID", '28748671'))
    API_HASH = os.environ.get("API_HASH", 'f53ec7c41ce34e6d585674ed9ce6167c')
    AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
