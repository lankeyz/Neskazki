
# ГЛАВА 10 КОЛОБОК

label chapter_09:
    
    show text "ГЛАВА 9\nПРИЗНАНИЕ" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    
    menu:
        "Простить Лису за содеянное?":
            $ lisa_points += 1
            "Вы решили, что прошлое должно остаться в прошлом."
        "Не прощать":
            "Такое невозможно забыть. Ваше сердце осталось холодным."
    
    jump chapter_10