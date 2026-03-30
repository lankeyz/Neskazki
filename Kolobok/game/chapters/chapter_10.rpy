
# ГЛАВА 10 КОЛОБОК

label chapter_10:
    
    show text "ГЛАВА 10\nКОЛОБОК" at truecenter with dissolve
    pause 2.0
    hide text with dissolve
    

label masterskaya:
    scene black with dissolve

    "Мы с Лисой были почти у самого сарая. Дым из трубы не шел, видимо там никого не было."
    "У Мастерсокй мы воровато оглянулись и тут же прыснули: горе-взломщики."
    "Дверь с протяжным скрипом отворилась, лязгнул затвор, мы зашли"

    jump masterskaya_searching

    
label continue:

    "Я уже потянулся, чтобы помочь ему, но замер..."


    if player_weapon == "dagger":
        
        "Из Колобка торчал кинжал. Тот, что я недавно видел у Лисы."

    elif player_weapon == "knife":
       
        "Из Колобка торчал мой перочинный нож."   

    jump chapter_TEST