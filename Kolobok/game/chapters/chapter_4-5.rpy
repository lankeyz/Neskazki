
# ГЛАВА 4-5

label chapter_choice: # Исправлено: добавлена 'l' в label

    # Показываем Главу 4 (название уже записано в меню)
    $ chapter_number += 1
    "Глава [chapter_number]: [chapter_name]."

    "На рассвете я вышел из дома и побрёл по деревне."

    novel "«Дымка от пепелища сизым саваном укутывала деревню... Запах смерти»."

    # Прыгаем в первую выбранную локацию
    if first_destination == "saray":
        jump chapter_saray
    else:
        jump chapter_editorial_office

# --- ЛОКАЦИЯ: САРАЙ ---
label chapter_saray:
    "Я осмотрел Сарай."
    "Здесь пахнет сырым сеном и гниющими досками."

    # Проверяем: если мы здесь были ПЕРВЫМ делом, значит пора идти в Редакцию
    if first_destination == "saray":
        "Теперь нужно было идти в редакцию."
        
        # Готовим Главу 5
        $ chapter_number += 1
        $ chapter_name = "Редакция"
        "Глава [chapter_number]: [chapter_name]."
        jump chapter_editorial_office
    
    # Если мы пришли сюда ВТОРЫМ делом, значит всё осмотрено — идем в Главу 6
    else:
        jump chapter_06

# --- ЛОКАЦИЯ: РЕДАКЦИЯ ---

label chapter_editorial_office:
    "Я в редакции, разобрал свои заметки."
    "Всё давно покрылось пылью. В мусорном веде скомканные листы."

    # Проверяем: если Редакция была ПЕРВОЙ, значит идем в Сарай
    if first_destination == "editorial_office":
        "Закончив здесь, я решил заглянуть в сарай."
        
        # Готовим Главу 5
        $ chapter_number += 1
        $ chapter_name = "Сарай"
        "Глава [chapter_number]: [chapter_name]."
        jump chapter_saray
    
    # Если Редакция была ВТОРОЙ — идем в Главу 6
    else:
        jump chapter_06

# --- ФИНАЛ ---

    jump chapter_06