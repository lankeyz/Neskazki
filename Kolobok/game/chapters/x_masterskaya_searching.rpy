
# МАСТЕРСКАЯ

label masterskaya_searching:

    scene bg_masterskaya_main
    window hide

       
    "Ну и свалка же здесь"

    show screen workshop_search_screen
    window hide
    
label .waiting_loop:
        window hide
        pause

# ЛОГИКА ВЕДРА
label check_bucket:
    hide screen workshop_search_screen

    if bucket_checked:
        "Больше не хочу туда заглядывать."
    else:
        $ bucket_checked = True
        "Остатки теста присохли к стенкам."
    show screen workshop_search_screen
    jump masterskaya_searching.waiting_loop

# ЛОГИКА СТОЛА
label witch_table:
    hide screen workshop_search_screen
    
    if witch_table_checked:
        kb "Там больше нет ничего интересного."
        # ИСПРАВЛЕНИЕ: Возвращаем игрока в цикл ожидания, 
        # чтобы он не провалился в jump shadow_of_alenushka ниже
        show screen workshop_search_screen
        jump masterskaya_searching.waiting_loop
    else:
        scene bg_book_plants with fade
        $ witch_table_checked = True
        kb "Это похоже на книгу рецептов."
        ll "Меня больше беспокоит, что кто-то решил добавить в пирожки багульник... Пожалуй, самое время отказаться от мучного."
        kb "Как превратить человека в животное... Что за?.."
        ll "Тебе лучше не читать остальное, поверь."

    # Этот переход сработает ТОЛЬКО если witch_table_checked был False
    jump babka


label babka:
    
    # Здесь мы уже знаем, что дверь будет открыта
    scene bg_masterskaya_main with fade

    "Тут что-то громыхнуло за нашими спинами, раздался вскрик. Мы резко обернулись."
    
    $ can_open_secret_door = True
    scene bg_masterskaya_open with dissolve
    
    "Неприметная дверь распахивается, и оттуда появляются Бабка и Сима Ильинична."
    "Завидев нас, Бабка начала плакать, а Сима — утешать ее."

    bya "Я думала, он мастерит что-то. Я не думала, что он решит… Я убрала сердцевину, теперь он не может петь."

    "Бабка подошла к столу и забрала книгу, прижав ее к груди."

    bya "Что же он никак не поймет, что уже всё, что нельзя так продолжать…"

    ll "Он не остановился десять лет назад, не остановится сейчас."

    kb "Я один не понимаю, что тут происходит?"

    ll "Как же надо было так мозги твои вывихнуть, что ты до сих пор ни черта не помнишь!"

    bya "Прости его... нас."

    "*еще немного говорят*"

    "Сима дернула Бабку за рукав, и мы посмотрели на нее. Совсем про нее забыли."

    bya "Сима увидела, что я иду сюда, догадалась... Она тоже искала Алёнушку. "

    ll "Мы найдем ее, не волнуйтесь."

    "Бабка и Сима выходят из мастерской."

    kb "Будьте осторожны, опять черноптицы налетели."

    bya "Они меня не тронут, да и не нужны они больше."
       
    show screen workshop_search_screen
    jump masterskaya_searching.waiting_loop

# ЛОГИКА ДВЕРИ
label masterskaya_kolobki:
    hide screen workshop_search_screen
    $ event_triggered = False
    scene bg_masterskaya_dark
    window hide

    kb "Ни черта не видно."
    ll "На твоё счастье у меня есть фонарик."
    kb "Рукопись, теперь ещё и фонарик... что еще у тебя припрятано?"
    ll "Ты можешь проверить это позже, если захочешь."

    label flashlight_loop:
        call screen flashlight_mode
        $ res = _return

        if res == "play_wheeze":
            play sound "audio/wheeze.wav"
            $ event_triggered = True
            kb "Ты слышала?"
            ll "Кажется, это в том углу, рядом с печкой..."
            jump flashlight_loop 

        if res == "found_kolobok":
            jump kolobok_found
    

label kolobok_found:
    scene black with fade
    ll "О боже, это же наш Колобок! Он ранен..."

    "Сердцевина вырезана, но сам Колобок жив."
    "Снаружи раздаются крики и ругань: старик прибежал к мастерской, заподозрив, что кто-то прознал про сжигание неудачных вариантов колобков."
    "Сима возвращается за ними и помогает выйти из мастерской, ведет на ту сторону реки в разрушенный дом стариков, показывает тайный ход."

    jump chapter_12
   