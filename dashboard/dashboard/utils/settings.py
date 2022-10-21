from decouple import config

APP_HOST = config('HOST')
APP_PORT = int(config('PORT'))
APP_DEBUG = bool(config('DEBUG'))
DEV_TOOLS_PROPS_CHECK = bool(config('DEV_TOOLS_PROPS_CHECK'))
API_KEY = config('API_KEY', None)