import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "xender_xd")
ALIVE_NAME = getenv("ALIVE_NAME", "xender")
BOT_USERNAME = getenv("BOT_USERNAME", "Eula_musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Eula_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "come_and_feel_music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "the_acr_network")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b7118a97fe3f607b9d9ed.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/b7118a97fe3f607b9d9ed.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b7118a97fe3f607b9d9ed.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b7118a97fe3f607b9d9ed.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b7118a97fe3f607b9d9ed.jpg")
