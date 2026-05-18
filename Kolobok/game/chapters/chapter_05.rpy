
label chapter_05:

    show text "ГЛАВА 5\nСима" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    show street

    "На мосту я увидел фигуру.  В последнее время всех так и тянуло туда. Но кого я меньше всего ожидал встретить здесь - Егора."

    if chosen_chapter_ambar_04:
        # Если в 4-й БЫЛ амбар, значит сейчас (в 6-й) нужна редакция
        jump chapter_06_editorial_office
    else:
        # Если в 4-й НЕ БЫЛО амбара, значит сейчас идем туда
        jump chapter_06_ambar