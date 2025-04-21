import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


# Get this value from my.telegram.org/apps
API_ID = "21968859"
API_HASH = "21a59d21687f01d448530ee88a26b1eb"

## Get it from @Botfather in Telegram.
BOT_TOKEN = ("7002687044:AAEytlXRdQWms-lfXCX_ZEMkf9RVPeNSXZ0")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "Telgrammusicbot")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = ("mongodb+srv://anandcollage245:ZehHlJTPgnFr8AjH@cluster0.t7w7l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", 5)
)  # Remember to give value in Seconds

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", 300)
)  # Remember to give value in Minutes


EXTRA_PLUGINS = getenv(
    "EXTRA_PLUGINS",
    True,
)

# Fill True if you want to load extra plugins
# Fill here the external plugins repo where plugins that you want to load
EXTRA_PLUGINS_REPO = getenv(
    "EXTRA_PLUGINS_REPO",
    "https://github.com/Rishuz/ChampExtra",
)

# Your folder name in your extra plugins repo where all plugins stored
EXTRA_PLUGINS_FOLDER = getenv("EXTRA_PLUGINS_FOLDER", "plugins")

LOGGERS = "\x52\x69\x73\x68\x75\x43\x6F\x64\x65\x72\x62\x6F\x74"  # connect errors api key "Dont change it"
# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", 1000)
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOGGER_ID = ("-1002346695101")

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", 7774827065).split())
)  # Input type must be interger

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Itachiuchiha786786/Nexio",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/aethonixsupport"
)  
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/igrischatsupport"
) 

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", False)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", 1800)
)  # Remember to give value in Seconds

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorize command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", False)


# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", 3))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", 5))


# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/Rishubot")


# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "27abb49d299c4a9abbd5aba126ad3c69")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "d7b2393eb88e4acfba14358e8d1eff7d")


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", 999))


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 500))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))  # Remember to give value in bytes
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496)) # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# If you want your bot to setup the commands automatically in the bot's menu set it to true.
# Refer to https://i.postimg.cc/Bbg3LQTG/image.png
SET_CMDS = getenv("SET_CMDS", False)


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @ChampuStringBot
STRING1 = ("BQFbXrIAEUTp0U8tt172mmvp_ISrC5C72Ovlft9xUPyUs2izcu8nO5gKdBDEk4V4jWDwodygpQmjxQ6Jl9gG9PavLfMW6aiWLmgThrmdhh6b0_MqYKiASuQwHQKzplLY3jRWzlqQPe0nP2VtWBG7daJXmfaPGiVgP03-u_TbZwZX_JFfTtervw8_tz9vQpXSY_mzXeqJLxxN1CcVM5VZLDjT3KNwpKobFSQ5rSDW-IVqYiTbXeRpcJn2OfiB7Wb_o3JaDd1CzHMc7jskMy8kqtr55HsbzUsoGdwcNP3lUUTHwDg9o-aK6M63Hp4t-8Uo_j9_nwGCnc3hIuWThm8RQ8mCRRTvQAAAAAHm-3v4AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
  



### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "musiclogs.txt"
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images

START_IMG_URL = getenv(
    "START_IMG_URL",
    "https://i.ibb.co/WN7PXzp6/photo-2025-04-21-03-16-06-7495600001838481432.jpg",
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://i.ibb.co/wNsRMCfg/photo-2025-04-21-03-07-23-7495597742685683728.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://i.ibb.co/Zp98KZjf/photo-2025-04-21-03-12-20-7495599662536065036.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://i.ibb.co/WN7PXzp6/photo-2025-04-21-03-16-06-7495600001838481432.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://telegra.ph/file/a9d91437d795b0ae55af8.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://i.ibb.co/MyPRGJ45/photo-2025-04-21-03-12-17-7495599525097111572.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://i.ibb.co/zTtfQmBn/photo-2025-04-21-03-12-13-7495599434902798356.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://i.ibb.co/qM29nC5h/photo-2025-04-21-03-12-09-7495599344708485136.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://i.ibb.co/jkCh42c0/photo-2025-04-21-03-12-03-7495599160024891416.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://i.ibb.co/Rkb8Q3SB/photo-2025-04-21-03-12-07-7495599258809139204.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://i.ibb.co/hJxpybYr/photo-2025-04-21-03-12-01-7495599039765807112.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://i.ibb.co/hJxpybYr/photo-2025-04-21-03-12-01-7495599039765807112.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://i.ibb.co/hJxpybYr/photo-2025-04-21-03-12-01-7495599039765807112.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )


if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )


if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )


if PING_IMG_URL:
    if PING_IMG_URL != "https://i.ibb.co/hJxpybYr/photo-2025-04-21-03-12-01-7495599039765807112.jpg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://i.ibb.co/Zp98KZjf/photo-2025-04-21-03-12-20-7495599662536065036.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://i.ibb.co/hJxpybYr/photo-2025-04-21-03-12-01-7495599039765807112.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://i.ibb.co/3YLPzsGR/photo-2025-04-21-03-12-24-7495599808564953104.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://i.ibb.co/MyPRGJ45/photo-2025-04-21-03-12-17-7495599525097111572.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://i.ibb.co/qM29nC5h/photo-2025-04-21-03-12-09-7495599344708485136.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://i.ibb.co/jkCh42c0/photo-2025-04-21-03-12-03-7495599160024891416.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://i.ibb.co/Rkb8Q3SB/photo-2025-04-21-03-12-07-7495599258809139204.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://i.ibb.co/zTtfQmBn/photo-2025-04-21-03-12-13-7495599434902798356.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
