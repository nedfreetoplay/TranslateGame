label left_hallway_judith_changing:
    scene lefthall_c
    show player 2 at left with dissolve
    show judith 6 at right with dissolve
    player_name "Привет, {b}Джудит{/b}..."
    show player 11 at left
    player_name "..."
    show player 10 at left
    player_name "Все в порядке?"
    show player 5 at left
    show judith 3 at right
    jud "Оу, привет, {b}[firstname]{/b}..."
    jud "Мне не очень хорошо; Наверное, нужно пойти домой."
    show player 10 at left
    show judith 1 at right
    player_name "Не пойдешь на физ-ру?"
    show player 5 at left
    show judith 2 at right
    jud "Ну..."
    jud "...Просто..."
    show judith 3 at right
    jud "... Я не могу пойти в мужскую раздевалку."
    show player 10 at left
    show judith 1 at right
    player_name "... Мужскую раздевалку?"
    player_name "Почему ты должна туда идти?"
    show player 5 at left
    show judith 3 at right
    jud "Тебе не сказали?"
    show judith 1 at right
    show player 10 at left
    player_name "... Нет?"
    show player 5 at left
    show judith 3 at right
    jud "Трубу прорвало, и женскую раздевалку закрыли на ремонт..."
    show judith 2 at right
    jud "И теперь мы в одной раздевалке с мальчиками."
    show judith 1 at right
    show player 10 at left
    player_name "Серьезно?!"
    show player 5 at left
    show judith 3 at right
    jud "Мне не очень комфортно, не так как остальным девочкам."
    show judith 6 at right
    show player 35 at left
    player_name "Ну..."
    show player 10 at left
    show judith 1 at right
    player_name "Урок же уже скоро начнется, так что в раздевалке, наверное, осталось не так много людей?"
    show player 1 at left
    show judith 5 at right
    jud "Да, наверное ты прав..."
    show player 2 at left
    show judith 4 at right
    player_name "Я пойду с тобой, чтобы убедиться, что всё в порядке..."
    show player 33 at left
    player_name "...И я не буду смотреть!"
    show player 13 at left
    show judith 5 at right
    jud "Окей... тогда я буду прямо за тобой."
    hide player 13 at left with dissolve
    hide judith 5 at left with dissolve
    return

label left_hallway_latinos_bashing:
    scene lefthall_c
    show judith 10 at left
    show martinez at Position (xpos=350)
    show lopez f_normal_talk
    with dissolve
    lopez "Ты только глянь на эти отвисшие сиськи!"
    show lopez f_normal_talk
    show judith 7 at left
    jud "..."
    show judith 8 at left
    show martinez f_normal_talk
    martinez "Она, видно, настолько бедная, что не может позволить себе даже лифчик..."
    show martinez f_normal
    show judith 7 at left
    jud "Всё не так!!"
    show judith 10 at left
    show lopez f_normal_talk
    lopez "Думаешь, что если вот так светить сиськами - ты сможешь получить мужское внимание?"
    show lopez f_normal
    show judith 7 at left
    jud "У меня очень чувствительная грудь!! Мне больно, когда я ношу лифчик..."
    jud "Без него мне намного комфортнее!!"
    show judith 10 at left
    show lopez f_laugh
    lopez "Хаха!"
    show lopez f_normal
    show judith 9 at left
    show martinez f_angry_talk
    martinez "Йоу, лучше тебе больше тут не появляться..."
    show martinez a_dressed_sign with dissolve
    martinez "ПУТА! Ты меня услышала? Это наша точка, вали отсюда!"
    show martinez f_angry a_dressed_crossed with dissolve
    show player 12 at Position( xpos = 290, ypos = 768)
    hide judith 9
    show judith 9 at left
    with dissolve
    player_name "Что здесь происходит?!"
    show player 114
    jud "{b}*Рыдает*{/b}"
    show player 90 at Position( xpos = 290, ypos = 768)
    show judith 9 at left
    show lopez f_angry
	show martinez f_angry_talk
    martinez "Ты защищаешь эту уродливую сучку??"
    show martinez f_angry
    show lopez f_angry_talk
    lopez "Иди мимо, снежок!"
    show lopez f_angry
    show player 113
    player_name "Ты в порядке {b}Джудит{/b}?"
    hide judith
    show player 90 at left
    with dissolve
    show martinez f_angry_talk
    martinez "Что такое, белоснежка, не побежишь за своей сучкой?"
    show martinez f_angry
    show player 12 at left
    player_name "Тебе не нужно было этого делать..."
    show martinez f_angry_talk a_dressed_sign with dissolve
    martinez "Мы делаем всё, что нам, блять, захочется!"
    show martinez f_angry a_dressed_crossed with dissolve
    show lopez f_laugh
    lopez "Хаха! Увидимся!"
    hide player
    hide lopez
    hide martinez
    with dissolve
    return

label left_hallway_judith_missing:
    scene expression game.timer.image("lefthall{}")
    show player 11 with dissolve
    player_name "..."
    show player 10
    player_name "...Где {b}Джудит{/b}?"
    player_name "( Она же обычно в коридоре. )"
    show player 34
    player_name "Хмм..."
    show player 35
    player_name "( Я {b}что-то{/b} слышу... )"
    show player 10
    player_name "( Кто-то плачет... ? )"
    show player 12
    player_name "( Это же из {b}женской раздевалки{/b}... )"
    hide player 12 with dissolve
    return

label left_hallway_martinez_book_search:
    scene lefthall_c
    show martinez a_dressed_backpack at Position (xpos=350)
    show lopez 18 at right
    show player 10 at left
    with dissolve
    player_name "Хей, {b}Мартинез{/b}?"
    show player 5
    show martinez f_normal_talk
    martinez "...Чего ты хочешь, задница?"
    show martinez f_normal
    show lopez 19
    lopez "Да! Чего тебе надо?"
    show lopez 18
    show player 10
    player_name "Ухх, я слышал, что ты не вернул книгу в библиотеке."
    show player 5
    show martinez f_angry_talk
    martinez "Ты что, следишь за мной, белый парень?"
    show martinez f_angry
    show player 10
    player_name "Ха? нет, меня послала библиотекарша!"
    show player 5
    show lopez 19
    lopez "Так ты, значит, сучка библиотекарши?"
    show lopez 18
    show martinez f_laugh
    martinez "Хаха!"
    show martinez f_normal
    show player 12
    player_name "Что? Нет, она просто заказала для меня книгу, но взамен попросила меня поговорить с вами."
    show player 5
    show martinez f_angry_talk
    martinez "Да пофиг! У нас нет на это времени..."
    show martinez f_normal_talk
    martinez "Давай, {b}Лопес{/b}. Мы уже должны быть в спортзале."
    show martinez f_normal
    show lopez 19
    lopez "И правда, {b}Мартинез{/b}. Ещё увидимся, задница!"
    show lopez f_laugh
	lopez "Хахаха!"
    hide lopez
    show martinez b_back f_empty a_empty
    with dissolve
    show player 428
    pause
    show martinez at Position (xpos=500) with dissolve
    show player 11
    player_name "!!!"
    hide martinez with dissolve
    show player 12
    player_name "Я уверен, что она в его портфеле!"
    show player 30
    player_name "Нужно попытаться стащить её, {b}пока они будут в душе{/b}. Они, наверное, даже не заметят."
    show player 33
    player_name "Нужно просто быть аккуратнее..."
    hide player with dissolve
    return

label left_hallway_cult_discovery:
    scene cult_event 5
    with dissolve
    window hide
    $ renpy.pause()
    scene cult_event 6
    with Dissolve(0.3)
    $ renpy.pause()
    scene expression "backgrounds/location_school_lefthall_night.jpg"
    with Dissolve(0.3)
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 1 at right with dissolve
    player_name "..."
    show player 12
    player_name "Они пошли в кладовку?"
    show player 90
    show erik 5
    eri "Зачем им туда?"
    show player 35
    show erik 1
    player_name "Но более важный вопрос: как они там помещаются?"
    player_name "Наверное, там есть проход куда-то ещё..."
    show player 34
    show erik 5
    eri "Может мы уже уйдем?"
    show player 12
    show erik 1
    player_name "Давай просто придерживаться плана. И не забывай оглядываться по сторонам."
    show player 1
    show erik 3
    eri "Окей..."
    hide player 1 with dissolve
    hide erik 3 with dissolve
    return

label left_hallway_school_sneak_mission:
    scene cult_event 5
    with dissolve
    window hide
    pause
    scene cult_event 6
    with Dissolve(0.3)
    pause
    scene expression game.timer.image("lefthall{}")
    show player 11 at left with dissolve
    show erik 51 at right with dissolve
    player_name "..."
    show player 12
    player_name "Они залезли в кладовку?"
    show player 90
    show erik 53
    eri "Зачем им туда?"
    show erik 52
    show player 35
    player_name "Это бессмысленно."
    player_name "Они не могут влезть туда все вместе!"
    show player 34
    show erik 53
    eri "Думаешь, там секретный тоннель или типа того?"
    show erik 52
    show player 10
    player_name "Хмм, не знаю. Может и да..."
    show player 5
    show erik 53
    eri "Это меня правда пугает."
    eri "Можем мы уже уйти?"
    show erik 52
    show player 12
    player_name "Подожди. Мы всё ещё должны выполнить нашу миссию."
    show player 5
    show erik 50
    eri "..."
    show player 12
    player_name "Давай, пойдем в офис {b}Директриса Смит{/b} на {b}третьем этаже{/b}."
    hide player
    hide erik
    with dissolve
    return

label door14_locked_dialogue:
    scene expression game.timer.image("lefthall{}")
    show player 35 at left
    player_name "( Подсобка заперта. )"
    $ game.main()

label left_hallway_roxxy_lockerroom_event:
    scene expression game.timer.image("lefthall{}")
    show player 34 with dissolve
    player_name "Хмм?"
    player_name "( Из {b}женской раздевалки{/b} доносятся голоса! )"
    player_name "( Но она же закрыта... )"
    show player 4 at Position (xoffset=6) with dissolve
    player_name "( ... Интересно, что там происходит? )"
    hide player with dissolve
    return

label left_hallway_roxxy_shower_event:
    scene expression game.timer.image("lefthall{}")
    show erik 62 at right
    show jersey 10 at left
    with dissolve
    player_name "{b}Эрик{/b}?"
    show erik 61
    player_name "Где твоя одежда?"
    show jersey 5
    show erik 63
    eri "Привет, {b}[firstname]{/b}..."
    eri "Я переодевался в {b}раздевалке{/b}, когда {b}Рокси{/b} зашла со своими подружками..."
    show erik 62
    eri "... Они выпнули меня."
    show erik 61
    show jersey 10
    player_name "А твоя одежда осталась там?"
    show jersey 5
    show erik 62
    eri "... Ага."
    show erik 61
    show jersey 12
    player_name "Да ладно тебе, эх, я пойду с тобой."
    player_name "Мы возьмем твою одежду, а мне нужно в душ."
    show jersey 5
    show erik 62
    eri "О-окей..."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
