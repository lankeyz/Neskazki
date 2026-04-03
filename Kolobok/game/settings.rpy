# логика фонарика
init python:
    # Функция для получения позиции мыши
    def get_mouse_pos():
        return renpy.get_mouse_pos()

init python:
    # Переменная, чтобы звук и реплика сработали только ОДИН раз
    event_triggered = False
    
init python:
    # Канал для погоды (дождь, ветер). Всегда зациклен (loop=True)
    renpy.music.register_channel("weather", mixer="sfx", loop=True, stop_on_mute=True)
    
    # Канал для окружения (пожар, поезд, шум толпы). Тоже зациклен.
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True)
    
    # Канал для разовых звуков (шаги, хрип, гром). НЕ зациклен (loop=False)
    renpy.music.register_channel("fx", mixer="sfx", loop=False)

    # Канал 'music' (стандартный) оставляем только для музыки (OST)
    renpy.music.register_channel("ost", mixer="music", loop=True, stop_on_mute=True)       
    
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
# --- ПОГОДА (weather) ---
define audio.w_rain = "audio/shum_dozhdya.ogg" #дождь
define audio.w.raintrain = "audio/rainandtrain.mp3" # шум поезда, дождь

# --- ОКРУЖЕНИЕ (ambience) ---
define audio.a_fire_voices = "audio/fire2.mp3"  # Пожар с голосами
define audio.a_fire_main = "audio/fire.ogg"    # Просто пожар

# --- ЭФФЕКТЫ (fx) ---
define audio.s_grom = "audio/grom.ogg" # гром
define audio.s_steps = "audio/footsteps.mp3" #шаги в траве
define audio.s_wheeze = "audio/wheeze.ogg" # хрип
define audio.s_train_stop = "audio/stoptrain.ogg"# поезд останавливается

# --- МУЗЫКА (OST)
define audio.o_likhoe = "audio/likhoe.mp3"
define audio.o_lost_home = "audio/lost_home.mp3"


# Определение видео
image akt1 = Movie(channel="movie", play="video/akt1.webm")

# медленное затемнение
define slow_fade = Fade(2.0, 1.0, 2.0)

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

#transform heart_jump_purple:# Фиолетовая молния и спуг
    linear 0.05 zoom 2.08
    matrixcolor TintMatrix("#ba53ff")  # Фиолетовый оттенок
    linear 0.1 zoom 1.0
    matrixcolor TintMatrix("#ffffff")  # Возврат к норме

# Определение резкой ослепляющей вспышки
transform thunder_flash_fx:
    # 1. МГНОВЕННАЯ ВСПЫШКА
    # Устанавливаем яркость сразу (без linear), чтобы бахнуло мгновенно
    matrixcolor BrightnessMatrix(0.9) 
    
    # 2. ЗАДЕРЖКА ОСЛЕПЛЕНИЯ
    # Вот эта строка держит экран белым. 
    # 0.5 — это полсекунды. Можно поставить 1.0 для очень долгой вспышки.
    pause 0.5 
    
    # 3. ПЛАВНЫЙ ВЫХОД
    # Теперь яркость возвращается к 0.0
    # Сделаем чуть дольше (например, 0.5), чтобы глаза "отходили" от света
    linear 0.5 matrixcolor BrightnessMatrix(0.0)
