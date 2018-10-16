label button_crystal_preamble:
    show player 5 at left
    show crystal 3 at right
    with dissolve
    crys "Это снова дружочек моей маленькой девочки."
    show crystal 1 with dissolve
    show player 10
    player_name "Я же вам говорил, мы не-"
    show player 5
    show crystal 2
    crys "Не обращай внимания, мальчишка."
    show crystal 4 with dissolve
    crys "*глоток*"
    show crystal 2 with dissolve
    crys "Итак, что тебе нужно?"
    return

label button_crystal_roxxys_dad:
    show player 10
    player_name "А где {b}папа Рокси{/b}?"
    show player 11
    show crystal 2
    crys "Хах! У нее нет отца!"
    crys "Я вырастила ее самостоятельно."
    show crystal 1
    show player 10
    player_name "Понятно."
    show player 11
    show crystal 2
    crys "Сказать по правде, я не помню, кто ее отец..."
    show crystal 4 with dissolve
    crys "*глоток*"
    show crystal 2 with dissolve
    crys "...Так что ее отцом может быть кто угодно, из тех кого я знаю."
    show crystal 1
    show player 22
    player_name "!!!"
    show crystal 2
    crys "Хочешь еще о чем-нибудь поговорить?"
    show player 5
    show crystal 1
    return

label button_crystal_roxxy:
    show player 10
    player_name "Где я могу найти {b}Рокси{/b}?"
    show player 5
    show crystal 3 with dissolve
    crys "Ха! Думаешь, я нянчусь со своей дочерью?"
    show crystal 1 with dissolve
    show player 10
    player_name "Хмм..."
    show player 5
    show crystal 2
    crys "Она постоянно что-то где-то делает..."
    crys "...Но, чаще всего она в {b}школе{/b} или на {b}пляже{/b}."
    show crystal 1
    show player 14
    player_name "О. Понятно. Спасибо!"
    show player 13
    show crystal 2
    crys "Что-нибудь ещё?"
    show crystal 1
    return

label button_crystal_nothing:
    show player 10
    player_name "О, ничего."
    player_name "Я просто проходил мимо..."
    show player 11
    show crystal 2
    crys "Ну, у меня скоро будет посетитель, так что почему бы тебе не свалить."
    show crystal 1
    show player 10
    player_name "Простите. Я ухожу."
    player_name "Пока!"
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_go_to_picnic:
    scene expression "backgrounds/location_trailer_closeup_night.jpg"
    show player 5 at left
    show player_wet at left
    show crystal 3 at right
    with dissolve
    crys "Знаешь, я могу помочь тебе снять мокрую одежду, если хочешь."
    show crystal 1 with dissolve
    show player 10
    player_name "Ааа... Я..."
    show player 5
    player_name "..."
    show crystal 2
    crys "Не стесняйся."
    crys "Красивый мужчина, как ты. Заслуживает особого внимания, не так ли?"
    show crystal 1
    show player 3 with dissolve
    player_name "..."
    rox "{b}Мама{/b}, оставь {b}[firstname]{/b} в покое!"
    show crystal 2
    crys "Хехехе, я просто немного дразню мальчика."
    show crystal 1
    rox "Ну, хватит!"
    show crystal 4 with dissolve
    rox "{b}[firstname]{/b}, иди сюда!"
    show crystal 1
    player_name "..."
    hide crystal
    hide player
    hide player_wet
    with dissolve
    return

label button_crystal_rox8_11_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 5 at left
    show crystal 6 at right
    with dissolve
    crys "Ты заблудился, красавчик?"
    show crystal 5
    show player 10
    player_name "Ааа?!"
    show player 5
    show crystal 6
    crys "О, ты новый мужчина {b}Roxxy{/b}."
    show crystal 5
    show player 12
    player_name "Н-нет, Я-"
    show player 5
    show crystal 6
    crys "Она в комнате."
    show crystal 5
    return

label button_crystal_rox8_11_day:
    scene trailer_interior_c
    show player 5 at left
    show crystal 2 at right
    with dissolve
    crys "Ты заблудился, красавчик?"
    show crystal 1
    show player 10
    player_name "Ааа?!"
    show player 5
    show crystal 2
    crys "О, ты новый мужчина {b}Roxxy{/b}."
    show crystal 1
    show player 10
    player_name "Н-нет, Я-"
    show player 5
    show crystal 2
    crys "Ее здесь нет."
    show crystal 4 with dissolve
    return

label button_crystal_final_evening:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Ммм, а вот и приятный умелый человек!"
    show crystal 5
    show player 14
    player_name "А, привет {b}Кристи{/b}..."
    show player 13
    show crystal 6
    crys "Почему бы тебе не выпить пивка и посидеть со мной?"
    crys "Ты можешь отключить свое красноречие на..."
    show crystal 5
    show player 14
    player_name "О, Я не знаю... {b}Рокси{/b} не будет-"
    show player 5
    show crystal 6
    crys "Ты пришел навестить {b}Рокси{/b}?"
    show crystal 5
    return

label button_crystal_final_day:
    scene trailer_interior_c
    show player 13 at left
    show crystal 2 at right
    with dissolve
    crys "Ммм, а вот и приятный умелый человек!"
    show crystal 1
    show player 14
    player_name "А, привет {b}Кристи{/b}..."
    show player 13
    show crystal 2
    crys "Почему бы тебе не выпить пивка и посидеть со мной?"
    crys "Ты можешь отключить свое красноречие на..."
    show crystal 1
    show player 14
    player_name "О, Я не знаю... {b}Рокси{/b} не будет-"
    show player 5
    show crystal 2
    crys "{b}Рокси{/b} здесь нет."
    show crystal 1
    return

label button_crystal_sorry_to_bother:
    show player 10
    player_name "Извините за беспокойство."
    show player 5
    show crystal 6
    crys "Пфф, болтовня не беспокоит меня..."
    crys "На самом деле, почему бы тебе не сбегать в магазин и не купить мне ещё упаковку пива?"
    crys "Сделаешь это, и мы будем болтать, пока у тебя уши не отвалятся."
    show crystal 5
    show player 17
    player_name "Хех, неа, все в порядке."
    player_name "Я должен зайти внутрь и повидаться с {b}Рокси{/b}."
    show player 13
    show crystal 6
    crys "Делай что хочешь."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_roxxy_rox8_rox11:
    show crystal 1 with dissolve
    show player 10
    player_name "Вы знаете, где она?"
    show player 5
    show crystal 2
    crys "Пфф, понятия не имею..."
    crys "Я никогда не смогу уследить за этой девчонкой."
    show crystal 1
    show player 10
    player_name "Правда?"
    show player 5
    show crystal 2
    crys "Неблагодарное отродье, ничего мне не говорит."
    crys "Ей нужно всегда кричать! Что ей нужно ..."
    show crystal 1
    player_name "..."
    return

label button_crystal_roxxy_final:
    show crystal 4 with dissolve
    show player 12
    player_name "Где она находится?"
    show player 5
    show crystal 2 with dissolve
    crys "Черт, если бы я знала."
    crys "Если она не в {b}школе{/b}, то я думаю, что она, вероятно {b}на пляже.{/b}"
    crys "Клянусь, эта девушка наполовину русалка!"
    show crystal 1
    show player 17
    player_name "Хе, да наверное..."
    show player 13
    return

label button_crystal_roxxys_mom:
    show crystal 1 with dissolve
    show player 10
    player_name "Вы {b}мама Рокси{/b}?"
    show player 5
    show crystal 2
    crys "Точно."
    crys "Разве ты не видишь сходство?"
    show crystal 1
    menu:
        "Да, возможно.":
            show player 12
            player_name "Теперь, когда вы упомянули об этом, вы очень похожи."
            show player 5
            show crystal 2
            crys "Да, ей действительно повезло, что она похожа на меня."
            crys "Ее отец был уродлив, как грех!"
            show crystal 1
            player_name "..."
            show crystal 2b
            crys "Хахаха!"
            show crystal 1
            jump roxmom_dialogue_repeat
        "Вы выглядите такой молодой!":
            show player 12
            player_name "Я вижу сходство, но ты выглядишь слишком молодой, чтобы быть мамой {b}Roxxy{/b}."
            show player 10
            player_name "Вы уверены что вы не сестра?"
            show player 5
            show crystal 2
            crys "Ну что ж, если у тебя нет 'серебряного языка'!"
            crys "Думаю, как именно так ты привлек внимание моей дочери, а?"
            show crystal 1
            show player 10
            player_name "Ну, Я-"
            show player 5
            show crystal 2
            crys "Не хочу тебя расстраивать, слизняк... Но чтобы удержать ее, нужно больше, чем просто болтовня."
            crys "Я правильно ее воспитала, понимаешь?"
            crys "Покажи ей, что ценность мужчины в его действиях, а не в его словах!"
            show crystal 1
            player_name "..."
            show crystal 2
            crys "Если ты не можешь должным образом заботиться о моей девочке, тогда тебе лучше отвалить, детка."
            show crystal 1
            jump roxmom_dialogue_repeat
    return

label button_crystal_roxxy_busy:
    show player 29 with dissolve
    player_name "{b}Рокси{/b} занята?"
    show player 3
    show crystal 6
    crys "Пфф, сомневаюсь..."
    crys "Наверное, она просто треплется по своему чертову телефону."
    show crystal 5
    show player 12 with dissolve
    player_name "Так я могу просто зайти и увидеть ее?"
    show player 5
    show crystal 11
    crys "... Ты ждешь, что я тебя остановлю или что?"
    show crystal 10
    show player 10
    player_name "Я не-"
    show player 11
    show crystal 6
    crys "Какое несчастье, малыш."
    crys "Выразите пару и заходите туда уже!"
    hide crystal
    hide player
    with dissolve
    return

label button_crystal_happy_home:
    show player 10
    player_name "Вы счастливы быть дома?"
    show player 5
    show crystal 2
    crys "Конечно!"
    crys "Это место может быть дерьмовой дырой, но оно чертовски лучше тюремной камеры, скажу я вам!"
    crys "Думаю, я должна поблагодарить тебя за то, что вытащил меня оттуда."
    show crystal 4 with dissolve
    show player 14
    player_name "О, не надо благодарить. Я просто рад помочь."
    show player 13
    show crystal 2 with dissolve
    crys "Хех, да... хорошо."
    crys "Как скажешь, ловкач."
    crys "Предложение в силе, если ты передумаешь..."
    crys "Я могу быть ОЧЕНЬ благодарной... Понимаешь, о чем я говорю?"
    show crystal 1
    show player 5
    player_name "... {b}*глоток*{/b}"
    show crystal 2
    crys "Хехехе."
    return

label button_crystal_should_go_evening:
    show player 14
    player_name "Наверное, мне стоит туда попасть..."
    show player 13
    show crystal 6
    crys "Да, думаю ты прав."
    crys "Позаботься о моей девочке, слышишь?"
    show crystal 5
    show player 14
    player_name "Да, мэм."
    hide player with dissolve
    pause
    show crystal 6
    crys "Хахаха, \"мэм...\""
    crys "Это убивает меня каждый раз!"
    hide crystal with dissolve
    return

label button_crystal_should_go_day:
    show player 14
    player_name "Наверное, мне стоит пойти и найти {b}Рокси{/b}."
    show player 13
    show crystal 2
    crys "Ну, тебе не обязательно сейчас убегать..."
    crys "Я с радостью составлю тебе компанию, пока она не вернется домой."
    show crystal 1
    show player 14
    player_name "Хех, нет, все в порядке. Не хотелось бы вас беспокоить."
    show player 13
    show crystal 2
    crys "Пфф, беспокоить."
    crys "Я знаю несколько способов скоротать время..."
    show crystal 1
    show player 3 with dissolve
    player_name "{b}*глоток*{/b}"
    show player 29
    player_name "Я эээто... Увидемся позже, {b}Кристи{/b}."
    show player 3
    show crystal 2
    crys "Делай как знаешь."
    hide player
    hide crystal
    with dissolve
    return

label button_crystal_she_here:
    show player 14
    player_name "Да, она здесь?"
    show player 13
    show crystal 6
    crys "Да, она там..."
    show crystal 11
    crys "Наверное, треплется по телефону, как обычно."
    crys "Если бы я не знала, я бы поклялся, что эта штука была приклеена к её голове всегда..."
    show crystal 5
    show player 17
    player_name "Хе, да."
    show player 13
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
