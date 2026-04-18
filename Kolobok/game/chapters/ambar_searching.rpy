

label ambar_searching:
    window hide
    # Запускаем режим фонарика
    call screen ambar_flashlight_mode
    
    # Сюда попадем, когда кликнем по лампе (Return)
    if _return == "found_lamp":
        "Я отыскал спички, большая часть из них отсырела, но на пятый раз мне удалось поджечь фитиль и осмотреться."
        jump ambar_light

label ambar_light:
    scene bg_ambar_light
    show screen ambar_search_screen
    window hide

label .waiting_loop:
    window hide
    
    # Сначала проверяем, что все три точки осмотрены
    if ambar_box_checked and ambar_hay_checked and ambar_lamp_checked:
        "Я осмотрел здесь всё."
        
        # Проверяем условие через ваш словарь
        if player_choices["needs_pencil"]:
            jump pencil_secret
        else:
            jump ambar_end

    pause
    jump .waiting_loop

# Клик по ящику
label ambar_check_box:
    hide screen ambar_search_screen
    if ambar_box_checked:
        "Я уже осмотрел."
        
    else:
        $ ambar_box_checked = True
        "Остатки картошки на дне. Клубни сморщились и затвердели, ростки иссохшими нитями переплетались и цеплялись за щели."
    
    show screen ambar_search_screen
    jump ambar_light.waiting_loop

# Клик по сено
label ambar_check_hay:
    hide screen ambar_search_screen
    if ambar_hay_checked:
        "Ничего интересного."
        
    else:
        $ ambar_hay_checked = True
        "Просто куча сена. Однако по спине пробежал холодок. Много лет назад я прятался в этом самом сене, зарываясь поглубже, чтобы меня не нашли."
    
    show screen ambar_search_screen
    jump ambar_light.waiting_loop

# Клик по лампе
label ambar_check_lamp:
    hide screen ambar_search_screen
    if ambar_lamp_checked:
        "Надо перед уходом погасить."
        
    else:
        $ ambar_lamp_checked = True
        "Надеюсь, не погаснет раньше, чем я осмотрю всё тут."
    
    show screen ambar_search_screen
    jump ambar_light.waiting_loop



# КАРАНДАШ

label pencil_secret:
    hide screen ambar_search_screen
    window show

    "Я собрался уходить, когда вспомнил про карандаш."
    "Я начал шарить по полу, разгребая сено, и в конце концов наткнулся на него."
    
    kb "Значит, я всё-таки был здесь... Осталось понять, что я тут делал."

    "Голоса на удивление молчали."
    "Я потянул руку чуть дальше и нашарил что-то еще. Какая-то небольшая щель в досках."
    
    # Смена фона на секретный и показ нового экрана
    
    scene bg_ambar_light_secret with dissolve
    
    "Я смел сено и пыль в сторону и уставился на дверцу подпола."
    "Она плотно прилегала к доскам."
    window hide
    show screen ambar_secret_screen with dissolve
    # Ждем клика игрока по двери (через ambar_secret_screen)
label .wait_for_prying:
    window hide
    pause
    jump .wait_for_prying


# Клик по секретной двери (Попытка вскрытия)
label try_open_secret_door:
   
    hide screen ambar_secret_screen
    window show
    
    "Я попытался поддеть её найденным карандашом, но тот с хрустом переломился."
    
    kb "Черт... Слишком хлипкий."

    "Я поискал вокруг какие-нибудь инструменты, но ничего не нашел."
    "В сарае у Деда наверняка найдется всё необходимое, но пробираться туда тайком было бы глупо, а просьба вызвала бы лишние вопросы."
    
    "Я почти уверен, что в подполе нет ничего интересного — максимум забродившее варенье или банки с мутными соленьями."
    "И всё же..."
    "Я чувствовал странное волнение. Мне нужно было открыть этот подпол."
    
    "В редакции есть перочинный нож, но нужно что-то помощнее. Что-то, что не погнется и не сломается."
    
    "Быть может, у Быка найдется подходящий инструмент. И он точно не будет расспрашивать."
       
    scene black
    jump ambar_end
    
