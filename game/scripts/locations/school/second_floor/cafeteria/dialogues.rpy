label cafeteria_diane_delivery_3_drop_off_goods:
    scene cafeteria_b
    show player 164 at left with dissolve
    show annie 1 at right with dissolve
    player_name "All done!"
    show annie 9
    show player 163
    ann "..."
    show annie 3
    ann "{b}Principal Smith{/b} took the {b}invoice{/b}?"
    show annie 1
    show player 164
    player_name "Yeah, she was... kind of... busy. But she said I should give it to you."
    show annie 5
    show player 163
    ann "I see..."
    show annie 15
    show player 1
    ann "I'll take these from you, then."
    show annie 14
    show player 17
    player_name "Thanks, {b}Annie{/b}!"
    hide player
    hide annie
    with dissolve
    return

label cafeteria_erik_favor_not_known:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Привет, {b}Кэвин{/b}!"
    show player 1 at left
    show kevin 2 at right
    kev "Привет, чувак..."
    show kevin 1 at right
    show player 10 at left
    player_name "ты правда работаешь в кафитерии..."
    show kevin 2 at right
    show player 13 at left
    kev "Ага! Мне осталось еще 2 месяца этого дерьма."
    show kevin 1 at right
    show player 17 at left
    player_name "Это хреново."
    show kevin 2 at right
    show player 1 at left
    kev "Да но что я могу сделать?"
    kev "Кстати, {b}Декстер{/b} доставляет вам неприятности в коридоре?"
    show kevin 1 at right
    show player 24 at left
    player_name "Да, он и {b}Рокси{/b} всегда по нашу душу..."
    show player 26 at left
    player_name "Но это ничто. Мне все равно что они там говорят."
    show kevin 3 at right
    show player 11 at left
    kev "Чувак. Ты должен уметь постоять за себя."
    show kevin 1 at right
    show player 10 at left
    player_name "Я бы лучше избежал этого с ним, ты понимаешь?"
    player_name "Нет смысла начинать драку с парнем который в двое больше меня."
    show kevin 3 at right
    show player 11 at left
    kev "Ты не можешь позволять ему все время не считаться с тобой. Как ты собираешься выживать в колледже вот так?"
    show kevin 1 at right
    show player 24 at left
    player_name "Что ж,Я слишком слаб что бы что то с этим поделать."
    show kevin 4 at right
    show player 11 at left
    kev "Хмм... Возможно мы погли бы что нибудь придумать."
    show kevin 1 at right
    show player 10 at left
    player_name "Что ты имеешь в виду?"
    show kevin 4 at right
    show player 1 at left
    kev "Ну, я бы мог помочь тебе с тренеровками в {b}Спортзале{/b}..."
    kev "Посмотреть на тебя что ты можешь и когда ты более не менее освоишься показать тебе несколько трюков."
    show kevin 2 at right
    show player 34 at left
    kev "Но тебе придется {b}Найти кого-нибудь на мое место{/b} в кафитерии."
    kev "Я не могу больше это выносить."
    show player 34 at left
    show kevin 1 at right
    player_name "Хорошо! Я могу попробовать найти кого-нибудь кто сможет поменяться с тобой."
    show kevin 2 at right
    show player 1 at left
    kev "Отлично, чувак. Мне нужно возвращаться к работе. Увидимся позже!"
    show kevin 1 at right
    show player 36 at left
    player_name "Пока, {b}Кэвин{/b}!"
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_known_intro:
    scene cafeteria_b
    show player 2 at left with dissolve
    show kevin 1 at right with dissolve
    player_name "Привет, {b}Кэвин{/b}!"
    show kevin 2 at right
    show player 1 at left
    kev "Привет, чувак..."
    kev "Удалось ли тебе найти кого-нибудь кто смог бы взять на себя мои кафитерные обязательства?"
    return

label cafeteria_erik_favor_known_found_replacement:
    show player 14 at left
    show kevin 1 at right
    player_name "Я думаю что нашел замену!"
    show kevin 2 at right
    show player 1 at left
    kev "Не может быть, мужик! Это круто!"
    kev "Кто займет мое место?"
    show kevin 1 at right
    show player 17 at left
    player_name "Это {b}Эрик{/b}... и мне пришлось подкупить его..."
    show kevin 2 at right
    show player 1 at left
    kev "Хаха! Что ж, спасибо,чувак!"
    kev "Теперь я смогу проводить больше времени в {b}Спортзале{/b}!"
    show kevin 6 at right
    show player 11 at left
    kev "...И мне больше не понадобиться заниматься в столовой!"
    show kevin 5 at right
    show player 12 at left
    player_name "Это мерзко..."
    show kevin 12 at right
    show player 1 at left
    kev "Хэй! Если ты найдешь спортзал бро, ты знаешь где меня найти!"
    show kevin 5 at right
    show player 14 at left
    player_name "Хорошо! Я зайду!"
    return

label cafeteria_erik_favor_known_not_yet:
    show kevin 1 at right
    show player 26 at left
    player_name "Пока нет, Я продолжу поиски!"
    show kevin 3 at right
    show player 1 at left
    kev "Хорошо..."
    return

label cafeteria_erik_favor_known:
    call expression game.dialog_select("cafeteria_erik_favor_known_intro")
    menu:
        "Думаю, что да!" if erik.known(erik_favor_2):
            call expression game.dialog_select("cafeteria_erik_favor_known_found_replacement")
            $ erik_favor_2.finish()
            $ M_kevin.set_default_locations([[L_gym, L_school_cafeteria, L_gym, L_NULL],
                                            [L_gym, L_gym, L_gym, L_NULL]])
        "Пока нет.":

            call expression game.dialog_select("cafeteria_erik_favor_known_not_yet")
    hide player
    hide kevin
    with dissolve
    return

label cafeteria_erik_favor_2_completed:
    scene cafeteria_b
    show player 36 at left with dissolve
    show erik 11 at right with dissolve
    player_name "Привет, {b}Эрик{/b}!"
    show erik 12 at right
    show player 1 at left
    eri "Привет, {b}[firstname]{/b}!"
    show erik 11 at right
    show player 21 at left
    player_name "И так... Как твои обязаности в кафетерии?"
    show erik 12 at right
    show player 13 at left
    eri "Могло быть и хуже, Я думаю."
    eri "В общем я обычно не занимался ничем в течении обеда в школе..."
    show erik 11 at right
    show player 17 at left
    player_name "Я очень рад что ты согласился на это."
    show erik 12 at right
    show player 1 at left
    eri "Я хочу скорее вернуться домой, чтобы поиграть в {b}Sea Dogs SAGA{/b}!"
    show erik 11 at right
    show player 14 at left
    player_name "Круто! Что ж, я позволю вернуться тебе к своим обязанностям..."
    show erik 11 at right
    show player 1 at left
    eri "Увидимся позже!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
