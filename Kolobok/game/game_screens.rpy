# Интерактивный экран поиска в Редакции
# По умолчанию игрок еще ничего не видел
default table_checked = False
default closet_checked = False
default trash_checked = False
default can_check_trash = False # По умолчанию мусорка недоступна

image editorial_office = "images/location/editorial_office.jpg"
image inside_table = "images/location/inside_table.jpg"
image inside_closet = "images/location/inside_closet.jpg"      

screen office_hover_screen():
    zorder 100 # Выводит на самый верхний слой

    # стол (без изменений)
    imagebutton:
        xpos 0 ypos 0 
        idle Transform("location/table_glow.png", alpha=0.0) 
        hover Transform("location/table_glow.png", alpha=1.0) 
        focus_mask "location/table_glow.png"
        action Jump("go_inside_table")

    # шкаф (без изменений)
    imagebutton:
        xpos 0 ypos 0 
        idle Transform("location/closet_glow.png", alpha=0.0) 
        hover Transform("location/closet_glow.png", alpha=1.0) 
        focus_mask "location/closet_glow.png"    
        action Jump("go_inside_closet")

    # МУСОРКА — теперь под условием
    if can_check_trash:
        imagebutton:
            xpos 0 ypos 0 
            idle Transform("location/trash_glow.png", alpha=0.0) 
            hover Transform("location/trash_glow.png", alpha=1.0) 
            focus_mask "location/trash_glow.png"    
            action Jump("go_to_trash")


# Интерактивный экран поиска в мастерской

# Флаги состояния
default witch_table_checked = False
default bucket_checked = False
default can_open_secret_door = False # По умолчанию дверь закрыта

# Изображения локаций
image bg_masterskaya_main = "images/masterskaya/bg_masterskaya_main_close.jpg"
image bg_masterskaya_open = "images/masterskaya/bg_masterskaya_main_open.jpg"
image bg_book_plants = "images/masterskaya/book_plants.jpg"

screen workshop_search_screen():
    zorder 100

    # Ведро
    imagebutton:
        xpos 0 ypos 0 
        idle Transform("masterskaya/bucket_glow.png", alpha=0.0) 
        hover Transform("masterskaya/bucket_glow.png", alpha=1.0) 
        focus_mask "masterskaya/bucket_glow.png"
        action Jump("check_bucket")

    # Ведьмин стол
    imagebutton:
        xpos 0 ypos 0 
        idle Transform("masterskaya/witch_table_glow.png", alpha=0.0) 
        hover Transform("masterskaya/witch_table_glow.png", alpha=1.0) 
        focus_mask "masterskaya/witch_table_glow.png"
        action Jump("witch_table")

    # Секретная дверь (активна только после события со столом)
    if can_open_secret_door:
        imagebutton:
            xpos 0 ypos 0 
            idle Transform("masterskaya/secret_door_glow.png", alpha=0.0) 
            hover Transform("masterskaya/secret_door_glow.png", alpha=1.0) 
            focus_mask "masterskaya/secret_door_glow.png"
            action Jump("masterskaya_kolobki")

# ФОНАРИК

# 1. ОПРЕДЕЛЯЕМ ИЗОБРАЖЕНИЯ НАПРЯМУЮ
# Я переименовал переменную в 'kolobok_sprite', чтобы не было конфликта с именем файла
image bg_masterskaya_light = "images/masterskaya/bg_masterskaya_light.jpg"
image bg_masterskaya_dark = "images/masterskaya/bg_masterskaya_dark.jpg"
image flashlight_spot = "images/masterskaya/flashlight.png"
image kolobok_sprite = "images/masterskaya/kolobok_is_injured.png"

# Создаем композицию
image bg_lit_full = Fixed(
    "bg_masterskaya_light", 
    # Ставим его ровно по центру для теста (0.5, 0.5)
    Transform("kolobok_sprite", align=(0.5, 0.5)), 
    fit_first=True
)

# 2. ЭКРАН ФОНАРИКА
screen flashlight_mode():
    $ mouse_x, mouse_y = renpy.get_mouse_pos()
    
    add "bg_masterskaya_dark"
    add AlphaMask("bg_lit_full", Transform("flashlight_spot", pos=(mouse_x, mouse_y), anchor=(0.5, 0.5)))

    if not event_triggered:
        timer 5.0 action Return("play_wheeze")

    # Невидимая кнопка
    imagebutton:
        idle Solid("#00000000") 
        # Кнопка тоже должна быть в центре, как и спрайт
        align (0.5, 0.5) 
        
        # Указываем ПРЯМОЙ путь к файлу для маски клика
        focus_mask "images/masterskaya/kolobok_is_injured.png" 
        
        action Return("found_kolobok") 

    timer 0.02 repeat True action renpy.restart_interaction

# МЕНЮ ВЫБОРА ГЛАВы

screen chapter_selection():
    tag menu
    add "#1a1a1a" 

    vbox:
        align (0.5, 0.4)
        spacing 40

        text "ВЫБОР ГЛАВЫ" xalign 0.5 size 60 color "#fff" 

        # Основной контейнер для двух колонок
        hbox:
            align (0.5, 0.5)
            spacing 50 # Расстояние между левым и правым столбиком

            # ЛЕВАЯ КОЛОНКА
            vbox:
                spacing 20 # Расстояние между кнопками по вертикали
                textbutton "Пролог" action Jump("chapter_prolog") style "ch_button"
                textbutton "Глава 1: ВСТРЕЧА" action Jump("chapter_01") style "ch_button"
                textbutton "Глава 2: ПОЖАР" action Jump("chapter_02") style "ch_button"
                textbutton "Глава 3: ФРОСЯ" action Jump("chapter_03") style "ch_button"
                textbutton "Глава 4-5" action Jump("chapter_04_05_choice") style "ch_button"
                textbutton "Глава 6" action Jump("chapter_06") style "ch_button"

            # ПРАВАЯ КОЛОНКА
            vbox:
                spacing 20
                textbutton "Глава 7" action Jump("chapter_07") style "ch_button"
                textbutton "Глава 9" action Jump("chapter_09") style "ch_button"
                textbutton "Глава 10" action Jump("chapter_10") style "ch_button"
                textbutton "Глава Ambar 1" action Jump("chapter_ambar_first") style "ch_button"
                textbutton "Глава Ambar 2" action Jump("chapter_ambar_second") style "ch_button"
                textbutton "Редакция" action Jump("chapter_editorial_office") style "ch_button"

# Стили оставляем те же, они отлично работают
style ch_button:
    xsize 600           
    ysize 80            
    background Solid("#333") 
    hover_background Solid("#555") 
    padding (10, 10)
    align (0.5, 0.5)

style ch_button_text:
    idle_color "#ccc"   
    hover_color "#fff"  
    size 30             
    xalign 0.5          
    yalign 0.5



