import os
from dotenv import load_dotenv

# Downloading of environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

ACRCLOUD_ACCESS_KEY = os.getenv('ACRCLOUD_ACCESS_KEY')
ACRCLOUD_ACCESS_SECRET = os.getenv('ACRCLOUD_ACCESS_SECRET')
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')

ACRCLOUD_HOST = ' identify-eu-west-1.acrcloud.com'
AUDIO_PATH = 'music_file.mp3'

YANDEX_ASR_HOST = 'asr.yandex.net'
YANDEX_ASR_PATH = '/asr_xml'
CHUNK_SIZE = 1024 ** 2

CHROME_DRIVER_PATH = '/Users/vlasenckov/Desktop/chromedriver'

MUSIC_RECOGNITION = True
SPEECH_RECOGNITION = True

SUCCESS_MSG = 'success'
FAIL_MSG = 'fail'

START_MSG = 'Hey! I аm ready to go!'
HELP_MSG = 'If you need help, the best way at the moment is to contact one of the creators.'
DEFAULT_MODE_MSG = 'The default mode is set. Recognized ' \
                   'music first, ' \
                       'in case the track is not found, ' \
                   'voice recognition starts'
MUSIC_MODE_MSG = 'Music-only recognition mode is set.\n' \
                 'But I can still recognize audio files'
MUSIC_FAIL_MSG = 'Apparently the file is too short, ' \
                 'or no similar audio was found in my database!'
MUSIC_SUCCESS_MSG = ['Song ', '%s', ' performer ', '%s',
                     '\n', 'Link to Yandex.Music ', '%s']
SPEECH_FIND_SUCCESS_MSG = 'Hooray! I found these words in song / songs. Here is:\n'
SPEECH_FIND_FAIL_MSG = 'I didn’t find such words in my database. Try again ' \
                       'or contact my creator '
SPEECH_TOO_MANY_FAIL = 'Too many tracks found! Try to be more precise or ' \
                       'contact my creators '
SPEECH_MODE_MSG = 'The voice recognition mode is set.'
SPEECH_RECOGNITION_START_MSG = 'Moving on to voice recognition!'
SPEECH_SUCCESS_MSG = ['You told me:\n', '"', '%s', '"', '\n',
                      'Now I will look for it in my database!']
SPEECH_FAIL_MSG = 'I was unable to recognize this message.'

YANDEX_MUSIC_MAIN_PAGE = 'https://music.yandex.ru'
YANDEX_MUSIC_FIND_PAGE = "https://music.yandex.ru/search?text="

LOG_PARSE_VOICE_ERROR = 'PARSE VOICE ERROR'
LOG_PARSE_FILE_ERROR = 'PARSE FILE ERROR'
LOG_SPEECH_ERROR = 'SPEECH ERROR'
LOG_START = 'START'
LOG_HELP = 'HELP'
LOG_SPEECH_MODE = 'SPEECH MODE'
LOG_MUSIC_MODE = 'MUSIC MODE'
LOG_DEFAULT_MODE = 'DEFAULT MODE'
LOG_PARSE_FILE = 'PARSE FILE'
LOG_PARSE_SPEECH = 'PARSE SPEECH'
LOG_PARSE_MUSIC = 'PARSE MUSIC'
