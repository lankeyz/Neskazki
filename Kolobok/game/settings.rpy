# логика фонарика
init python:
    # Функция для получения позиции мыши
    def get_mouse_pos():
        return renpy.get_mouse_pos()

init python:
    config.mouse = {
        "default": [ ("images/searching/default_cursor.png", 0, 0) ],
        "point": [ ("images/searching/point_cursor.png", 16, 16) ],
    }
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
define gui.interface_text_font = "fonts/georgia.ttf"
define gui.name_text_font = "fonts/georgia.ttf"

# Добавьте этот блок ниже, чтобы Ren'Py подхватывал начертания:
init python:
    # Связываем основной файл с его курсивной версией
    # Параметры: (путь_к_шрифту, жирный, курсив)
    config.font_replacement_map["fonts/georgia.ttf", False, True] = ("fonts/georgiai.ttf", False, False)
    # Связываем основной файл с жирной версией
    config.font_replacement_map["fonts/georgia.ttf", True, False] = ("fonts/georgiab.ttf", False, False)
    # Связываем основной файл с жирным курсивом
    config.font_replacement_map["fonts/georgia.ttf", True, True] = ("fonts/georgiaz.ttf", False, False)

# Определение персонажей
define kb = Character("Владимир", color="#85a39a")
define ll = Character("Лиза", color="#c4b394")
define ga = Character("Аркадий", color="#ffa600")
define sf = Character("Ефросинья Федоровна", color="#6a19ac")
define zm = Character("Митя", color="#5a8abe")
define vs = Character("«Серый»", color="#d1d1d1")
define bb = Character("Борис", color="#ffcc99") 
define bya = Character("Бабушка", color="#e0e0e0")
define dk = Character("Дед Костя", color="#e0e0e0")
define mm = Character("Дядя Миша", color="#f5f5dc")
define ms = Character("Сима Ильинична", color="#e0e0e0")
define ev = Character("Егорушка", color="#e0e0e0")
define liho = Character("Лихо", color="#e0e0e0")

# Определение изображений локации
image cattrain = "images/cattrain.jpg" # Кот в поезде
image train = "images/train.jpg" # Поезд
image intrain = "images/intrain.jpg" # В купе поезда
image station = "images/location/station.png" # Вокзал
image station_light = "images/location/station_light.png" # Вокзал со светом
image station_lamp = "images/location/station_lamp.png" # Лампа вокзальная

image home_fire = "images/location/home_fire.jpg" # Дом в огне

image saray_dark = "images/location/saray_dark.jpg" # Сарай в темноте
image in_saray = "images/location/in_saray.jpg" # Сарай внутри
image bridge = "images/location/bridge.jpg" # Мост
image bridge_lisa = "images/location/bridge_lisa.jpg" # Мост с лисой

image lihoe = "images/location/lihoe.jpg" # Лихое
image lihoe_fire = "images/location/lihoe_fire.jpg" # Лихое в огне
image lihoe_night = "images/location/lihoe_night.jpg"# Лихое ночью

image room_day = "images/location/room_day.jpg" # Номер кота
image office = "images/location/office.jpg" # Редакция



# Определение изображений персы

image kot_based = "images/person/kot/kot_based.png" # Кот нейтральный
image kot_thinks = "images/person/kot/kot_thinks.png" # Кот задумчивый
image kot_headache = "images/person/kot/kot_headache.png" # Кот в смятении
image kot_blocknot = "images/person/kot/kot_blocknot.png" # Кот пишет в блокнот
image kot_scared = "images/person/kot/kot_scared.png" # Кот напуган
image kot_confusion = "images/person/kot/kot_confusion.png" # Кот в шоке
image kot_confusion0 = "images/person/kot/kot_confusion0.png" # Кот в шоке 2
image kot_back = "images/person/kot/kot_back.png" # Спина кота
image kot_dark = "images/person/kot/kot_dark.png" # В темноте
image k_choice = "images/person/kot/choice.png" # КОТ делай выбор
image k_choice_b = "images/person/kot/choice_gloomy.png" # КОТ выбор угрюмый
image k_choice_g = "images/person/kot/choice_pleased.png" # КОТ выбор довольный


image lisa_based = "images/person/lisa_based.png" # Лиса нейтральна
image lisa_sly_umb = "images/person/lisa_sly_umb.png" # Лиса хитрая с зонтом 
image lisa_based_umb = "images/person/lisa_based_umb.png" # Лиса нейтральна с зонтом 
image lisa_confusion_umb = "images/person/lisa_confusion_umb.png" # Лиса удивленная с зонтом 
image lisa_confusion_umb0 = "images/person/lisa_confusion_umb0.png" # Лиса удивленная с зонтом 2

image bull_based = "images/person/bull_based.png"

image goose_based = "images/person/goose_based.png"
image goose_back = "images/person/goose_back.png"


# Определение аудио

# --- ПОГОДА (weather) ---
define audio.w_rain = "audio/shum_dozhdya.ogg" #дождь
define audio.w.raintrain = "audio/rainandtrain.mp3" # шум поезда, дождь
define audio.w.train = "audio/train.ogg" # стук колес

# --- ОКРУЖЕНИЕ (ambience) ---
define audio.a_prolog_station = "audio/prolog station.mp3"  # на станции
define audio.a_prolog_station_2 = "audio/prolog station 2.mp3"  # на станции
define audio.a_fire_voices = "audio/fire2.mp3"  # Пожар с голосами
define audio.a_fire_main = "audio/fire.ogg"    # Просто пожар
define audio.a_magicpole = "audio/magicpole.mp3"    # Телек


# --- ЭФФЕКТЫ (fx) ---
define audio.s_prolog = "audio/prolog.mp3" # пролог
define audio.s_golosa = "audio/golosa.mp3" # голоса
define audio.s_grom = "audio/grom.ogg" # гром
define audio.s_steps = "audio/footsteps.mp3" # бег в мокрой траве
define audio.s_steps2 = "audio/footsteps2.mp3" # шаг в мокрой траве
define audio.s_wheeze = "audio/wheeze.ogg" # хрип
define audio.s_train_stop = "audio/stoptrain.ogg" # поезд останавливается
define audio.s_tresk = "audio/tresk.mp3" # треск дерева
define audio.s_heartbeat = "audio/heartbeat.ogg" # удар сердца
define audio.s_opendoor = "audio/opendoor.mp3" #открывается дверь


# --- МУЗЫКА (OST)
define audio.o_likhoe = "audio/likhoe.mp3"
define audio.o_lost_home = "audio/lost_home.mp3"

## Музыка в главном меню
define config.main_menu_music = "audio/menu_music.ogg"

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

transform center_char: # Персонаж центр
    xalign 0.5
    yalign 1.0

transform heart_attack: # Эффект испуга
    linear 0.03 zoom 1.1
    linear 0.02 zoom 1.05 xoffset -5
    linear 0.02 zoom 1.05 xoffset 5
    linear 0.02 zoom 1.0 xoffset 0

transform heartbeat: # Удар сердца
    linear 0.1 zoom 1.02
    linear 0.1 zoom 1.0
    linear 0.1 zoom 1.01
    linear 0.1 zoom 1.0

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

transform wake_effect:
    alpha 0.0
    blur 20
    linear 1.0 alpha 1.0
    linear 1.5 blur 0

transform walking_shake: # Ходьба
    anchor (0.5, 0.5)
    pos (0.5, 0.5)

    easeout 0.2 yoffset -8 zoom 1.1
    easein 0.2 yoffset 0 zoom 1.1

    easeout 0.2 yoffset -8 zoom 1.2
    easein 0.2 yoffset 0 zoom 1.2

    easeout 0.2 yoffset -7 zoom 1.3
    easein 0.2 yoffset 0 zoom 1.3

    easeout 0.2 yoffset -6 zoom 1.4
    easein 0.2 yoffset 0 zoom 1.4

define fast_push = PushMove(0.2, "pushleft")  # Резкая смена кадра

transform slow_zoom: # ЗУМ
    zoom 1.0
    ease 20.0 zoom 1.06
transform reset_zoom: # Обратный зум
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom 1.05
    ease 0.5 zoom 1.0

transform train_night: # Тряска поезда
    subpixel False
    anchor (0.5, 0.5)
    pos (0.5, 0.5)

    parallel:
        linear 0.14 yoffset -5
        linear 0.14 yoffset 0
        linear 0.14 yoffset -5
        linear 0.28 yoffset 0
        repeat

    parallel:
        ease 0.7 xoffset -1
        ease 0.7 xoffset 1
        repeat

    parallel:
        ease 0.8 zoom 1.015
        ease 0.8 zoom 1.0
        repeat


transform fade_in_overlay: # заемнение экрана
    alpha 0.0
    linear 0.3 alpha 0.8

screen dark_overlay():
    add Solid("#000") at fade_in_overlay

transform float_text:
    yoffset 0
    ease 1.5 yoffset -10
    ease 1.5 yoffset -0
    repeat