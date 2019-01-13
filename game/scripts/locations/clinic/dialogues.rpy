label hospital_jizz_checkup:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 13f at right
    show diane b_casual a_casual_sides f_normal_talk at Position (xpos=400)
    with dissolve
    dia "Здрасьте."
    show diane f_normal
    show roz 2
    roz "Да?"
    show roz 1
    show diane f_normal_talk
    dia "У меня назначена проверка."
    show diane f_normal
    show roz 11b at Position (xoffset=-40) with dissolve
    roz "Хмм."
    pause
    show roz 2 with dissolve
    roz "{b}Диана{/b}?"
    show roz 1
    show diane f_normal_talk
    dia "Верно."
    show diane f_normal
    show roz 2
    roz "Поднимитесь в смотровую на втором этаже и переоденьтесь в халат."
    roz "Медсестра сейчас придет к вам."
    show roz 1
    show diane f_normal_talk
    dia "Хорошо."
    show diane at flip
    show diane at Position (xpos=850)
    with dissolve
    dia "Пойдем, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve
    return

label hospital_diane_seen_in_labor:
    scene expression "backgrounds/location_hospital_bed.jpg"
    show diane a_gown_bed_baby b_gown_bed f_gurney_normal_talk at Position (xpos=578,ypos=850)
    show player 5 at left
    with dissolve
    dia "Вот он где!"
    show diane f_gurney_normal
    pause
    show diane f_gurney_teasing_look
    dia "А вот и твой папочка!"
    show diane f_gurney_down_front
    show player 3 with dissolve
    player_name "{b}*глоток*{/b}"
    show diane f_gurney_normal_talk
    dia "Давай же, красавчик."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Я хочу познакомить тебя с {b}твоим новым сыном{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}М-моим сыном{/b}?"
    else:
        dia "Я хочу познакомить тебя с {b}твоей новой дочерью{/b}."
        show diane f_gurney_down_front
        show player 10 with dissolve
        player_name "{b}М-моей дочерью{/b}?"
    show player 13
    dia "Ммммм."
    show player 426 at center with dissolve
    pause
    show player 14
    player_name "Вау..."
    if M_diane.pregnancy.baby_gender == "boy":
        player_name "... Он такой милый!"
    else:
        player_name "... Она такая красивая!"
    show player 426
    show diane f_gurney_laugh
    dia "Хехе, ага."
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Прямо как его папочка."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "Я не могу поверить, что у меня есть сын!"
    else:
        dia "Прямо как ее мамочка."
        show diane f_gurney_cheese
        if M_diane.pregnancy.number_of_babies == 1:
            show player 17
            player_name "Я не могу поверить, что у меня есть дочь!"
    if M_diane.pregnancy.number_of_babies == 1:
        show player 18
        show diane f_gurney_teasing_look
        dia "Я знаю, я тоже."
        show player 426
        dia "Я никогда не думала, что у меня будет ребенок..."
    show diane f_gurney_down_front
    pause
    show player 14
    player_name "Так когда вы двое возвращаетесь домой?"
    show player 13
    show diane f_gurney_normal_talk
    dia "Они хотят оставить нас здесь еще на пару дней."
    dia "Но мы скоро вернемся домой."
    show diane f_gurney_normal
    pause
    show diane f_gurney_normal_talk
    dia "Убедитесь, что мой сад не завянет!"
    show diane f_gurney_normal
    show player 14
    player_name "Не волнуйся, я обо всем позабочусь."
    show player 13
    show diane f_gurney_normal_talk
    dia "Спасибо, {b}[firstname]{/b}."
    show diane f_gurney_laugh
    dia "Попрощайся с папочкой!"
    show diane f_gurney_cheese
    pause
    show player 429
    show diane f_gurney_normal
    player_name "Скоро увидимся, малыш."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
