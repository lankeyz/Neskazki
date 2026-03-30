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

    

# Текст романа

define novel = Character(None, 
    callback=novel_callback, 
    what_font="fonts/Truetypewriter PolyglOTT.ttf", 
    what_size=36,
    what_color="#1a1a1a",
    what_slow_cps=30,
    what_first_indent=60, 

    # ОКНО
    window_background=Image("images/Paper Overlay 15.png"), 
    window_xsize=1920,
    window_ysize=1080,
    window_xalign=0.5,
    window_yalign=0.5,
    
    # ОТСТУПЫ
    window_left_padding=480,   # Отступ слева до начала бумаги
    window_right_padding=480,  # ТЕПЕРЬ ЭТО СРАБОТАЕТ: отступ справа до края бумаги
    window_top_padding=300,    # Поднял текст повыше (было 400)
    window_bottom_padding=200,

    # ГЛАВНОЕ: Ограничиваем ширину текстового блока напрямую
    # 1920 - 480 (лево) - 480 (право) = 960 пикселей для текста
    what_xsize=960, 
    what_xalign=0.0,
    what_text_align=0.0
)

image secret_novel = "images/Paper Overlay 15_secret.png"


define sound.typewriter = "audio/typewriter.ogg"  # Печатная машинка

# Заливка Текст романа
# Создаем черную заливку на весь экран (1920x1080)
# "000000" — черный цвет
# "b3" — прозрачность примерно 70% (можно менять: "cc" — 80%, "ff" — 100%)
image black_overlay = Solid("#000000b3")        