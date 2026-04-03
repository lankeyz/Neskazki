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


# Определение изображений локации
image cattrain = "images/cattrain.jpg" # Кот в поезде
image train = "images/train.jpg" # Поезд
image intrain = "images/intrain.jpg" # В купе поезда
image home_fire = "images/location/home_fire.jpg" # Дом в огне

image saray_dark = "images/location/saray_dark.jpg" # Сарай в темноте
image bridge = "images/location/bridge.jpg" # Мост
image bridge_lisa = "images/location/bridge_lisa.jpg" # Мост с лисой

image lihoe = "images/location/lihoe.jpg" # Лихое
image lihoe_fire = "images/location/lihoe_fire.jpg" # Лихое в огне
image lihoe_night = "images/location/lihoe_night.jpg"# Лихое ночью

image room_day = "images/location/room_day.jpg" # Номер кота


# Определение изображений персы

image kot_based = "images/person/kot/kot_based.png" # Кот нейтральный
image kot_thinks = "images/person/kot/kot_thinks.png" # Кот задумчивый
image kot_headache = "images/person/kot/kot_headache.png" # Кот с головной болью
image kot_blocknot = "images/person/kot/kot_blocknot.png" # Кот пишет в блокнот
image kot_scared = "images/person/kot/kot_scared.png" # Кот напуган


image lisa_based = "images/person/lisa_based.png"
image lisa_sly_umb = "images/person/lisa_sly_umb.png"
image lisa_based_umb = "images/person/lisa_based_umb.png"


image bull_based = "images/person/bull_based.png"

image goose_based = "images/person/goose_based.png"
image goose_back = "images/person/goose_back.png"


# Определение аудио
define audio.shum = "audio/shum_dozhdya.ogg"  # Шум дождя
define audio.rainandtrain = "audio/rainandtrain.mp3"  # Шум поезда
define audio.stoptrain = "audio/stoptrain.ogg"  # Поезд все
define audio.fire = "audio/fire.ogg"  # Пожар
define audio.fire2 = "audio/fire2.mp3"  # Пожар и голоса
define audio.footsteps = "audio/footsteps.mp3"  # Шаги в траве
define audio.grom = "audio/grom.ogg" # Гром

# Определение видео
image akt1 = Movie(channel="movie", play="video/akt1.webm")


# Трансформации
transform blur_in:
    blur 10
    linear 2.0 blur 0

transform blur_out:
    linear 2.0 blur 10

transform kot_appear: # Персонаж слева
    xalign 0.0 yalign 1.0
    xoffset -500
    linear 1.0 xoffset 0

transform lisa_appear: # Персонаж справа
    xalign 1.0 yalign 1.0
    xoffset 500
    linear 1.0 xoffset 0

transform heart_attack: # Эффект испуга
    linear 0.03 zoom 1.1
    linear 0.02 zoom 1.05 xoffset -5
    linear 0.02 zoom 1.05 xoffset 5
    linear 0.02 zoom 1.0 xoffset 0

transform heart_jump_purple:# Фиолетовая молния и спуг
    linear 0.05 zoom 2.08
    matrixcolor TintMatrix("#ba53ff")  # Фиолетовый оттенок
    linear 0.1 zoom 1.0
    matrixcolor TintMatrix("#ffffff")  # Возврат к норме

# Настройка фонарика

