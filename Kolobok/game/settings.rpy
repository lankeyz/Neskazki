init python:
    def novel_callback(event, interact=True, **kwargs):
        if not interact:
            return

        # 1. ПОЯВЛЕНИЕ: включаем затемнение и печатную машинку
        if event == "show" or event == "begin":
            # zorder=100 гарантирует, что заливка накроет всех персонажей (Кота, Лизу и т.д.)
            renpy.show("black_overlay", what=Solid("#000000b3"), zorder=100)
            renpy.transition(dissolve)
            # Используем вашу переменную sound.typewriter
            renpy.sound.play(sound.typewriter, loop=True)
            
        # 2. ПАУЗА: текст напечатан до конца
        elif event == "slow_done":
            renpy.sound.stop()

        # 3. ФИНАЛЬНЫЙ ЭТАП: когда игрок кликает, чтобы перейти дальше
        elif event == "end":
            renpy.hide("black_overlay")
            # Можно добавить транзишн, чтобы исчезало плавно
            renpy.with_statement(dissolve)

# Основной шрифт
define gui.text_font = "fonts/georgia.ttf"
define gui.interface_text_font = "fonts/georgia.ttf" # Для кнопок и меню
define gui.name_text_font = "fonts/georgia.ttf"      # Для имен персонажей


# Определение персонажей
define kb = Character("Кот Владимир", color="#85a39a")
define ll = Character("Лиса Лиза", color="#c4b394")
define ga = Character("Гусь Аркадий", color="#ffa600")
define sf = Character("Свинья Фрося", color="#6a19ac")
define narrator = Character(None) # Авторская речь


# Текст романа
define novel = Character(None, 
    callback=novel_callback, 
    what_font="fonts/Truetypewriter PolyglOTT.ttf", 
    what_slow_cps=30, 
    what_size=36,
    what_color="#1a1a1a",    # Черный цвет текста
    what_first_indent=60,   # Красная строка
    what_xalign=0.5,        # Центрирование текстового блока
    what_width=1000,        # Ограничение ширины текста

    window_hide=True,       # Позволяет окну закрыться сразу и вызвать звук hide
    
    window_background=Frame("images/Paper Overlay 15.jpg", 10, 10),
    window_xsize=1200,      
    window_ysize=810,       
    window_xalign=0.5,      
    window_yalign=1.0,      
    window_top_padding=160,    
    window_yminimum=810,
    window_xfill=False
)

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
define sound.typewriter = "audio/typewriter.ogg"  # Печатная машинка
define sound.likhoe = "audio/likhoe.ogg" # Эмбиент

# Заливка Текст романа

# Создаем черную заливку на весь экран (1920x1080)
# "000000" — черный цвет
# "b3" — прозрачность примерно 70% (можно менять: "cc" — 80%, "ff" — 100%)
image black_overlay = Solid("#000000b3")

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

# Выборы игрока
default first_destination = "none" # Сюда запишем, куда Кот пойдет сначала
default visited_saray = False
default visited_editorial_office = False

# Нумерация глав
default chapter_number = 1

# Название глав
default chapter_name = ""
