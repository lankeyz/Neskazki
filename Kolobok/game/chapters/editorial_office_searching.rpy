
label editorial_office_searching:

    scene editorial_office # Ставим фон
    show office
    window hide # Прячем окно диалога, чтобы оно не мешало кликать
    
    # Показываем экран
    show screen office_hover_screen 
    
    kb "Она была где-то здесь."

    # Скрываем окно диалога сразу после этой фразы
    window hide
    
label .waiting_loop:
    # Важно: принудительно скрываем окно в начале цикла, 
    # чтобы оно не возвращалось после закрытия реплик
    window hide 
    
    # Пауза без текста, чтобы игрок видел только фон и кнопки
    pause 
    
label go_inside_table:    
    
    hide screen office_hover_screen
    
    if table_checked:
        # Если уже заходили
        kb "Я тут уже всё осмотрел. Карандаши и мусор, больше ничего интересного."
    else:
        # Если зашли первый раз
        scene inside_table with fade
        "здесь валяются огрызки карандашей, но некоторыми еще можно пользоваться. главное заточить, как раз тут еще лежит перочинный нож."

        # Ставим отметку, что осмотрено
        $ table_checked = True 
    
    scene editorial_office 
    show screen office_hover_screen
    jump editorial_office_searching.waiting_loop

label go_inside_closet:
    hide screen office_hover_screen

    if closet_checked:
        kb "Я тут уже всё осмотрел. Пыль на полках."
        jump editorial_office_searching.waiting_loop
    else:
        $ closet_checked = True
        scene inside_closet with fade
        "Раньше здесь было много моих черновиков, но я их забрал домой. Боялся, что тут они пропадут."
        "Ну, хоть Сливушка осталась..."

    if chosen_chapter_ambar_first:
            # Если игрок сначала был в амбаре (т.е. сейчас 5 глава), 
            # то сразу вызываем Митю, пропуская бутылку и мусорку
            jump meet_Mitya
    else:
            # Если это 4 глава (первая локация), идем к бутылке как обычно
            jump bottle_empty  

     
label bottle_empty:
    hide inside_closet
    show black
    
    "Грога было ровно на глоток."
    "Да что же такое! Я купил ее в день приезда и специально оставил ее здесь нетронутой!"
    "Кто вообще о ней знал? Пробраться сюда и втихаря выжрать почти всю бутылку…"
    "Что за животное так поступает?"
    "Тьфу."
    "Я подхватил бутылку, намереваясь забросить ее в мусорную корзину, но взгляд зацепился на белеющие на дне скомканные листы бумаги."
    "А что, если…" 
        
    # ВКЛЮЧАЕМ МУСОРКУ
    $ can_check_trash = True
   
    scene editorial_office # Возвращаем кабинет
    show screen office_hover_screen  # Включаем интерактив
    
    jump editorial_office_searching.waiting_loop

label go_to_trash:

    hide screen office_hover_screen

    show secret_novel

    jump on_the_table