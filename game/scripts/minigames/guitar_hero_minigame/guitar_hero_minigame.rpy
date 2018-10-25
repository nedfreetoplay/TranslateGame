label guitar_hero_minigame_karaoke_fail:
    scene erik_basement
    show erik 3f at Position (xpos=400)
    show player 5 at left
    show eve 23 at right with dissolve
    eve "Вы, ребята, отстой!"
    show eve 22
    show player 10
    player_name "Я не знал, что это за песня такая!"
    show player 12
    player_name "{b}Эрик{/b}, выбери другую!"
    show player 5
    show erik 3bf
    eri "Хорошо..."
    show erik 3f
    show player 14
    player_name "Вот так-то!"
    hide player
    hide erik
    with dissolve
    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        menu:
            "Играть в мини-игру":
                call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
            "Пропустить мини-игру (чит)":
                jump guitar_hero_minigame_karaoke_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

label guitar_hero_minigame_karaoke_pass:
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["01_unlocked"] = True
    scene erik_basement
    show erik 1f at Position (xpos=400)
    show player 13 at left
    show eve 19 at right
    with dissolve
    eve "Я покажу вам, как это делается!"
    eve "Прочь с дороги, мальчики!"
    show eve 15 with dissolve
    show erik 5f
    show player 11
    pause
    hide eve with dissolve

    scene erik_basement_cs2
    with fade
    show text "Думаю, выпивка сделала свое дело, потому что {b}Ева{/b} потрясла этот микрофон с некоторой серьезной уверенностью\nОна была великолепна! Я был полностью поражен тем, как прекрасен её голос!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Возможно, мне стоило остановить её на трех стаканах...\n... Но я не хотел пропустить это шоу." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene erik_basement
    show erik 57f at Position (xpos=400)
    show player 83c at left
    show eve 17c at right
    with dissolve
    eve "ЕЕЕЕЕ!!!"
    show eve 16 with dissolve
    show player 83b
    player_name "Черт девченка, ты жжешь!"
    show player 83c
    show eve 17
    eve "Спасибо! Я думаю - *ик* я думаю, что это не так уж плохо петь перед другими."
    show eve 16
    show player 83b
    player_name "Это значит, что ты будешь петь в шоу талантов?!"
    show player 83c
    eve "..."
    show eve 17
    eve "Конечно, почему бы и нет!"
    show eve 16
    show player 83b
    player_name "Ты великолепна!"
    player_name "Хотя, может, не стоит раздеваться перед шоу талантов."
    show player 83c
    show eve 17b with dissolve
    eve "Хмм?"
    show eve 17d with dissolve
    eve "О! Пфффф!"
    show eve 17c with dissolve
    eve "Ахахаха!"
    show eve 17 with dissolve
    eve "Упс. Наверное, я - *ик* думаю, я увлеклась..."
    show eve 15 with dissolve
    show erik 58f
    eri "Хех, все в порядке. Мы не против."
    show erik 57f
    show eve 2b
    eve "Ох, конечно *ик* {b}Эрик{/b} конечно..."
    show eve 4 with dissolve
    eve "Я совершенно забыла, хехехе."
    show eve 3
    eri "..."
    show player 79 with dissolve
    player_name "Наверное, мне стоит помочь тебе добраться домой."
    show player 83c
    show eve 2
    with dissolve
    eve "О, такой ... *ик* настоящий джентльмен!"
    eve "Я просто напишу своей сестре *ик* она меня заберет."
    show eve 5
    show erik 58f
    eri "Увидимся позже."
    show erik 57f
    show player 83b
    player_name "Спасибо за вечеринку {b}Эрик{/b}."
    show player 83c
    show eve 15 with dissolve
    eve "Да, вечеринка! Уу-хуууу!"
    show eve 5 with dissolve
    show player 83b
    player_name "Хех, ну ты и пьяница. Пойдем домой!"
    show player 83c
    show eve 2
    eve "Я был действительно хороша - *ик* не так ли, {b}[firstname]{/b}?"
    show eve 5
    show player 83b
    player_name "Конечно."
    show player 83c
    show eve 4 with dissolve
    eve "Хехехе."
    hide eve
    hide player
    hide erik
    with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    if M_dewitt.is_set("talent ask kevin"):
        $ M_dewitt.trigger(T_dewitt_find_last_talent)
    else:
        $ M_dewitt.trigger(T_dewitt_karaoke_jam)
    $ game.main()

label guitar_hero_minigame_talent_show_fail:
    scene assembly_hall_cs03
    with fade
    show text "Это не было хорошим началом, и толпа становилась беспокойной...\n{b}Ева{/b} и {b}Кевин{/b} выглядели обеспокоенными, но я знал, что мы всё ещё можем спасти его!\nЯ дал им обоим обнадеживающий кивок и начал сверху.\nМы обязательно победим их за это время!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve
    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        menu:
            "Играть в мини-игру":
                call screen guitar_hero(0, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")
            "Пропустить мини-игру (чит)":
                jump guitar_hero_minigame_talent_show_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")

label guitar_hero_minigame_talent_show_pass:
    if M_dewitt.get("failcount") == 0:
        $ A_smooth_mcgroove.unlock()
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Dewitt"]["gallery"]["02_unlocked"] = True
    scene assembly_hall_cs02
    with fade
    show text "Зрители были потрясены, когда мы играли нашими сердцами!\n{b}Кевин{/b} разорвал на своей гитаре и у {b}Евы{/b} ангельский голосок убаюкал их подчинил их себе!\n... Я закончил все это с причудливым соло флейты, которое заставила толпу содрогнуться!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_paint02_c
    show kevin 17f at Position (xpos=600)
    show player 554 at left
    show eve 12 at right
    with dissolve
    eve "Отличная работа, ребята!"
    show eve 11
    show player 555
    player_name "Да, это было действительно потрясающе!"
    show player 554
    show kevin 18f
    kev "Где, черт возьми, {b}Мисс Девитт{/b}?!"
    show kevin 17f
    show player 553
    player_name "... А?"
    show player 552
    show kevin 18f
    kev "Братан, она пропала!"
    show kevin 17f
    show eve 12
    eve "Он прав! Она была здесь секунду назад..."
    show eve 11
    show player 553
    player_name "Она должна была закончить шоу речью.."
    show player 552
    player_name "..."
    show kevin 18f
    kev "Чтож кто-то должен подняться и что-то сказать!"
    show kevin 17f
    show eve 12
    eve "{b}[firstname]{/b} должен сделать это!"
    show eve 11
    show player 553
    player_name "... Почему я всегда должен все делать?!"
    show player 552
    show kevin 18f
    kev "У тебя получится, братан!"
    show kevin 17f
    show player 553
    player_name "{b}*Вздох*{/b} Хорошо."
    show player 551c with dissolve
    player_name "( Думаю, я положу свои волосы набок. )"
    show player 551b at Position (xoffset=6) with dissolve
    show eve 12
    eve "Ох... Мне нравятся твои волосы!"
    show eve 11
    show player 551d with dissolve
    pause
    show player 14 at Position (xoffset=52) with dissolve
    player_name "Извини! Может быть, ты сможешь поправить мне прическу в следующий раз?"
    show player 13 at Position (xoffset=52)
    show eve 12
    eve "Все в порядке! А теперь убирайcя отсюда!"
    hide player
    hide kevin
    hide eve
    with dissolve

    scene assembly_hall_cs04
    with fade
    show text "Толпа затаив дыхание ждала, когда я направлюсь на подиум.\nЯ понятия не имел, что сказать этим людям!\nКуда черт возьми подевалась {b}Мисс Девитт{/b}?" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_podium_c
    show player podium 3 at Position (xoffset=-120)
    show xtra 44
    with dissolve
    player_name "Здравствуйте, итак эм..."
    player_name "Это было нечто, мм?"
    show player podium 4 at Position (xoffset=-120)
    player_name "Мы просто хотим сказать, что мы ценим..."
    show player podium 2 zorder 1 with dissolve
    player_name "!!!"
    player_name "Какого..."

    scene under_podium
    show dewitt under 1
    with dissolve
    dewitt "Ну Здравствуй, сладкий мой."
    show dewitt under 2
    player_name "Что ты делаешь?"
    show dewitt under 3 with dissolve
    dewitt "Тссс...."
    show dewitt under 1 with dissolve
    dewitt "Я знаю, что ты сделал."
    dewitt "Ты так рисковал отчислением, чтобы этот {b}Шоу талантов{/b} прошел без сучка и задоринки."
    show dewitt under 2
    player_name "В этом нет ничего особенного, мэм."
    player_name "Ты действительно должны были прийти сюда и закончить шоу!"
    show dewitt under 1
    dewitt "Ну эх! Нет, пока у меня не будет шанса отблагодарить тебя, мой сладкий!"
    show dewitt under 4 with dissolve
    player_name "Что ты де..."
    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 1 at left
    with dissolve
    player_name "!!!"
    show dewitt bj 2
    pause
    show dewitt bj 3
    dewitt "Продолжай говорить, {b}[firstname]{/b}!"
    dewitt "Твоя обожающая толпа ждет!"

    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "{b}*Кхм*{/b} Извините... Где я остановился?"
    player_name "..."
    player_name "А, точно!"

    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 4
    with dissolve
    player_name "Мы просто хотели сказать, что мы ценим..."
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    player_name "Вот дерьмо!"
    show screen dewitt_bj_options
    player_name "... О, Вау!"
    player_name "Мы-мы очень благодарны..."
    player_name "... Вы все пришли..."
    player_name "Ох чувак!!!"
    player_name "... Вы пришли поддержать нас!"
    player_name "Давайте послушаем ещё раз..."
    player_name "Мммм!"
    player_name "{b}Кевин{/b} на гитаре!"

    player_name "{b}Ева{/b} по вокалу!"
    player_name "... И меня"
    player_name "Ох Иисусе...!"
    player_name "Ахх!"
    player_name "Я {b}[firstname]{/b}!"
    dewitt "Ммм."
    player_name "..."
    player_name "Также особая благодарность-"
    player_name "Бляяяя..."
    player_name "... Мс Тирону!"
    player_name "... И конечно, же {b}Мисс Девитт{/b}!"
    player_name "Которая-"
    player_name "Ахх!"
    player_name "О боже!"
    player_name "{b}Мисс Девитт{/b}, никогда не подводит..."
    player_name "... Выкачивает каждый..."
    player_name "... Последний..."
    dewitt "{b}*Хлюп*{/b}"
    player_name "... Талант..."
    player_name "... Из её учеников!"
    player_name "Я хочу..."
    player_name "Я СОБИРАЮСЬ!!!"
    hide screen dewitt_bj_options

    scene assembly_hall_podium_c
    show player podium 1
    show xtra 44
    with dissolve
    player_name "КОНЧИТЬ!!!"
    player_name "Ох, возьми все это!"
    player_name "Даааа..."

    $ M_dewitt.set("sex speed", 0.075)
    scene dewitt_podium_bj
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    pause
    pause
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    pause
    show dewitt bj 6
    pause
    show dewitt bj 7
    pause
    dewitt "МММ, вкусно!"
    dewitt "Ещё раз спасибо, сладкий!"
    dewitt "!!!"

    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "{b}*Фух*{/b}"
    show player podium 3 zorder 0 at Position (xoffset=-120) with dissolve
    player_name "Извините, я хотел сказать ..."
    player_name "Я собираюсь объявить, что сейчас все подошло к концу."
    show player podium 4 at Position (xoffset=-120)
    player_name "Еще раз спасибо, что пришли!"
    player_name "... И обязательно запишитесь на шоу в следующем году!"
    player_name "Мы любим тебя, Саммервилл!"
    player_name "Спокойной ночи!"
    show player podium 5 at Position (xoffset=-56) with dissolve
    pause


    scene assembly_hall_cs07
    with fade
    show text "Когда я закончил свою речь. Я заметил очень странную пару, входящую в зал.\nСудя по всему это {b}Директриса Смит{/b} и {b}Энни{/b} которые сумели освободиться все-таки.\nСудя по их состоянию, это было нелегко!\nОни не задержались на долго... Повернувшись, чтобы уйти в тот момент, когда они поняли, что их избили." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_paint02_c
    show kevin 17f at Position (xpos=600)
    show player 13 at left
    show eve 12 at Position (xpos=450)
    with dissolve
    eve "Хахахаха!! Ты видел, что подушка прилипла к {b}Энни{/b}?!"
    eve "Это было самое смешное, что я когда-либо видела в жизни!"
    show eve 11
    show kevin 18f
    kev "Да, и {b}Одежда директора Смит{/b} разорвана в клочья"
    kev "Они действительно хотели остановить это шоу, да?"
    show kevin 17f
    show player 14
    player_name "Хех, да. Не могу поверить, что им удалось освободиться самостоятельно!"
    show player 13
    show dewitt 9bf at right
    show dewitt 9bf at Position (xoffset=-73)
    with dissolve
    $ renpy.end_replay()
    dewitt "Боже мой, вы были просто великолепны!"
    show eve 11f
    show kevin 17 at Position (xpos=700)
    with dissolve
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "Я никогда не была так горда!"
    show dewitt 1bf at Position (xoffset=-73)
    show eve 12f
    eve "Спасибо мэм"
    show eve 11f
    show kevin 18
    kev "...Откуда вы вышли?!"
    show kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "О, мне просто надо было сделать кое-что маленькое."
    show dewitt 1bf at Position (xoffset=-73)
    show kevin 18
    kev "Что-нибудь маленькое?"
    show kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "... Хм, ну, хорошо. Что-то большое на самом деле!"
    show dewitt 1bf at Position (xoffset=-73)
    player_name "..."
    show dewitt 19f with dissolve
    dewitt "Кстати, отличная речь, {b}[firstname]{/b}."
    dewitt "У тебя большой талант...."
    dewitt "... Для публичных выступлений."
    show dewitt 18f
    show eve 12f
    eve "Эй, ребята, хотите отпраздновать?! ... Перекусить или ещё что-нибудь?"
    show eve 11f
    show kevin 18
    kev "Я вниз!"
    show kevin 17
    show dewitt 19f
    dewitt "О, Нет, спасибо, дорогая. Боюсь, у меня нет свободного места..."
    show dewitt 18f
    show eve 12 with dissolve
    eve "{b}[firstname]{/b}?"
    show eve 11
    show player 14
    player_name "Мне тоже придется отказаться. Я довольно сильно устал."
    show player 13
    show eve 12
    eve "Ой! Ну же!"
    show eve 11
    show dewitt 19f
    dewitt "На самом деле вы не могли бы дать {b}[firstname]{/b} и я ненадолго остаюсь один?"
    show dewitt 18f
    show eve 11f with dissolve
    show kevin 18
    kev "Эй, если передумаешь, напиши нам смс."
    show kevin 17
    show player 14
    player_name "Хорошо. Позже!"
    show player 13
    hide kevin
    hide eve
    with dissolve
    show dewitt 9bf at Position (xoffset=-73) with dissolve
    dewitt "Я просто хотел поблагодарить тебя ещё раз за все, {b}[firstname]{/b}."
    show dewitt 9df at Position (xoffset=-73)
    dewitt "если бы не этот {b}Шоу Талантов{/b} ничего бы не случилось без твоей помощи."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "С удовольствием, {b}Мисс Девитт{/b}."
    show player 13
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "Я решила поставить тебе пятерку в классе."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "Правда?!"
    show player 13
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "Все правильно, сладкий моя."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "О, спасибо!"
    show player 13
    show dewitt 19f with dissolve
    dewitt "... И у меня есть еще один сюрприз для тебя."
    show dewitt 18f
    show player 10
    player_name "Хм?"
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Вам придется прийти ко мне в офис {b}завтра{/b} после школы, если хочешь..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "Окей..."
    player_name "Я буду там."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "МММ, не могу дождаться!"
    dewitt "Увидимся, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    hide player with dissolve
    $ renpy.end_replay()

    $ game.timer.tick()
    $ M_dewitt.trigger(T_dewitt_talent_show_success)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
