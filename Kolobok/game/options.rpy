## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("Kolobok")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "1.0"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
""")


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "Kolobok"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

# define config.main_menu_music = "main-menu-theme.ogg"


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = None


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 0


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>.
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = "Kolobok-1773478072"


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.
    
    # Исключит любые файлы в этой папке, имя которых начинается на "chapter_"
    build.classify('game/chapters/chapter_01.rpy', None)
    build.classify('game/chapters/chapter_01.rpyc', None)
    build.classify('game/chapters/chapter_02.rpy', None)
    build.classify('game/chapters/chapter_02.rpyc', None)
    build.classify('game/chapters/chapter_03.rpy', None)
    build.classify('game/chapters/chapter_03.rpyc', None)
    build.classify('game/chapters/chapter_04_ambar.rpy', None)
    build.classify('game/chapters/chapter_04_ambar.rpyc', None)
    build.classify('game/chapters/chapter_04_editorial_office.rpy', None)
    build.classify('game/chapters/chapter_04_editorial_office.rpyc', None)
    build.classify('game/chapters/chapter_05.rpy', None)
    build.classify('game/chapters/chapter_05.rpyc', None)
    build.classify('game/chapters/chapter_06_ambar.rpy', None)
    build.classify('game/chapters/chapter_06_editorial_office.rpyc', None)
    build.classify('game/chapters/chapter_07.rpy', None)
    build.classify('game/chapters/chapter_07.rpyc', None)
    build.classify('game/chapters/chapter_08.rpy', None)
    build.classify('game/chapters/chapter_08.rpyc', None)
    build.classify('game/chapters/chapter_09.rpy', None)
    build.classify('game/chapters/chapter_09.rpyc', None)
    build.classify('game/chapters/chapter_10.rpy', None)
    build.classify('game/chapters/chapter_10.rpyc', None)
    build.classify('game/chapters/chapter_11.rpy', None)
    build.classify('game/chapters/chapter_11.rpyc', None)
    build.classify('game/chapters/chapter_12.rpy', None)
    build.classify('game/chapters/chapter_12.rpyc', None)
    build.classify('game/chapters/chapter_13.rpy', None)
    build.classify('game/chapters/chapter_13.rpyc', None)
    build.classify('game/chapters/chapter_14.rpy', None)
    build.classify('game/chapters/chapter_14.rpyc', None)
    build.classify('game/chapters/chapter_15_THE END.rpy', None)
    build.classify('game/chapters/chapter_15_THE END.rpyc', None)

    build.classify('game/chapters/x_ambar_searching.rpy', None)
    build.classify('game/chapters/x_ambar_searching.rpyc', None)
    build.classify('game/chapters/x_editorial_office_searching.rpy', None)
    build.classify('game/chapters/x_editorial_office_searching.rpyc', None)
    build.classify('game/chapters/x_masterskaya_searching.rpy', None)
    build.classify('game/chapters/x_masterskaya_searching.rpyc', None)
  


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')


## Для совершения покупок в приложении требуется лицензионный ключ Google Play.
## Его можно найти в консоли разработчика Google Play в разделе "Монетизация" >
## "Настройка монетизации" > "Лицензирование".

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

define build.itch_project = "lunamaxima/Neskazki"


# Настройка фонарика

define config.layers = [ 'master', 'flashlight_layer', 'transient', 'screens', 'overlay' ]
