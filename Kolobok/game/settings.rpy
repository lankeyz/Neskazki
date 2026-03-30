# логика фонарика
init python:
    # Функция для получения позиции мыши
    def get_mouse_pos():
        return renpy.get_mouse_pos()

init python:
    # Переменная, чтобы звук и реплика сработали только ОДИН раз
    event_triggered = False    
    
# Основной шрифт
define gui.text_font = "fonts/georgia.ttf"
define gui.interface_text_font = "fonts/georgia.ttf" # Для кнопок и меню
define gui.name_text_font = "fonts/georgia.ttf"      # Для имен персонажей


# Определение персонажей
define kb = Character("Кот Владимир", color="#85a39a")
define ll = Character("Лиса Лиза", color="#c4b394")
define ga = Character("Гусь Аркадий", color="#ffa600")
define sf = Character("Свинья Фрося", color="#6a19ac")


# Определение изображений
image saray_dark = "images/location/saray_dark.jpg"
image room_day = "images/location/room_day.jpg"
image cattrain = "images/cattrain.jpg"
image train = "images/train.jpg"
image lihoe = "images/location/lihoe.jpg"
image intrain = "images/intrain.jpg"

image kot_based = "images/person/kot_based.png"
image kot_thinks = "images/person/kot_thinks.png"
image kot_headache = "images/person/kot_headache.png"


image lisa_based = "images/person/lisa_based.png"
image lisa_sly_umb = "images/person/lisa_sly_umb.png"
image lisa_based_umb = "images/person/lisa_based_umb.png"


image bull_based = "images/person/bull_based.png"

# Определение аудио
define audio.shum = "audio/shum_dozhdya.ogg"  # Шум дождя
define audio.rainandtrain = "audio/rainandtrain.mp3"  # Шум поезда
define audio.stoptrain = "audio/stoptrain.ogg"  # Поезд все
define sound.fire = "audio/fire.ogg"  # Пожар
define sound.likhoe = "audio/likhoe.ogg" # Эмбиент

# Определение видео
image akt1 = Movie(channel="movie", play="video/akt1.webm")


# Трансформации
transform blur_in:
    blur 10
    linear 2.0 blur 0

transform blur_out:
    linear 2.0 blur 10

transform kot_appear:
    xalign 0.0 yalign 1.0
    xoffset -500
    linear 1.0 xoffset 0

transform lisa_appear:
    xalign 1.0 yalign 1.0
    xoffset 500
    linear 1.0 xoffset 0

# Настройка фонарика

