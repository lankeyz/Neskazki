
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

    # Этот переход сработает ТОЛЬКО если witch_table_checked был False
    jump shadow_of_alenushka

# СОБЫТИЕ С АЛЕНУШКОЙ
label shadow_of_alenushka:
    
    # Здесь мы уже знаем, что дверь будет открыта
    scene bg_masterskaya_main with fade

    "Тут что-то громыхнуло за нашими спинами, раздался вскрик. Мы резко обернулись."
    
    $ can_open_secret_door = True
    scene bg_masterskaya_open with dissolve
    
    "Кто-то вылетел из неприметной двери и выбежал наружу."
    "Я не успел понять, кто это был, но заметил светлые длинные волосы."
       
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
    kb "Карта, теперь ещё и фонарик... что еще у тебя припрятано?"
    ll "Ты можешь проверить это позже, если захочешь." # вариант если романтик

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

    jump continue    
   