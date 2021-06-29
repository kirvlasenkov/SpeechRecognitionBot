
import json

with open("keys.json") as f:
  keys_dict = json.load(f)



AIRCLOUD_ACCESS_KEY = keys_dict["AIRCLOUD_ACCESS_KEY"]
AIRCLOUD_ACCESS_SECRET = keys_dict["AIRCLOUD_ACCESS_SECRET"]
TELEGRAM_API_TOKEN = keys_dict["TELEGRAM_API_TOKEN"]
YANDEX_API_KEY = keys_dict["YANDEX_API_KEY"]

AIRCLOUD_HOST = 'eu-west-1.api.acrcloud.com'

AUDIO_PATH = 'music_file.mp3'

YANDEX_ASR_HOST = 'asr.yandex.net'
YANDEX_ASR_PATH = '/asr_xml'
CHUNK_SIZE = 1024 ** 2

MUSIC_RECOGNITION = True
SPEECH_RECOGNITION = True

SUCCESS_MSG = 'success'
FAIL_MSG = 'fail'

START_MSG = 'Привет! Я готов к работе!'
HELP_MSG = 'helpppp'
DEFAULT_MODE_MSG = 'Установлен режим по умолчанию. Распознается ' \
                   'сначала музыка, ' \
                       'в случае, если трек не найдет, ' \
                   'запускается распознавание по голосу'
MUSIC_MODE_MSG = 'Установлен режим распознавания только музыки.\n' \
                 'Но я все равно могу распознавать аудиофайлы:)'
MUSIC_FAIL_MSG = 'Видимо, файл слишком короткий, ' \
                 'или в моей базе данных не нашлось похожей аудиозаписи!'
MUSIC_SUCCESS_MSG = ['Песня ', '%s', ' исполнителя ', '%s',
                     '\n', 'Ссылка на Яндекс.Музыку ', '%s']
SPEECH_FIND_SUCCESS_MSG = 'Ура! Я нашел эти слова в песне/песнях. Вот:\n'
SPEECH_FIND_FAIL_MSG = 'Я не нашел таких слов в своей базе:( Попробуй еще ' \
                       'или обратись к моему создателю ' \
                       'https://vk.com/k_artemkaa'
SPEECH_TOO_MANY_FAIL = 'Слишком много треков найдено! Попоробуй точнее или ' \
                       'обратись к моим создателям'
SPEECH_MODE_MSG = 'Установлен режим распознавания только по голосу.'
SPEECH_RECOGNITION_START_MSG = 'Перехожу к распознаванию голоса!'
SPEECH_SUCCESS_MSG = ['Ты наговорил мне:\n', '"', '%s', '"', '\n',
                      'Сейчас я поищу это у себя в базе!']
SPEECH_FAIL_MSG = 'Я не смог распознать это сообщение:('

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