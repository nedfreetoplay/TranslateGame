label mias_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Привет!"
    mia "Я так рада, что ты смог прийти."
    show mia 7
    show player 17
    player_name "Все нормально. Просто мне показалось, что ты хочешь поговорить о чем-то важном."
    show player 14
    player_name "Ты хотела меня о чем-то спросить?"
    show player 13
    show mia 10
    mia "Ну, это не так уж и важно..."
    mia "...Я надеялась узнать твое мнение кое о чем, и, может, ты мне поможешь."
    show mia 7
    show player 10
    player_name "Ох... Думаю, да. В чем заключается дело?"
    show player 11
    show mia 10
    mia "Ты знаешь что-нибудь о татуировках?"
    show mia 7
    show player 10
    player_name "Татуировках?!"
    show player 12
    player_name "Почему? Ты хочешь сделать ее себе?"
    show player 11
    show mia 12
    mia "Я знаю, что это плохо..."
    mia "...Но, я устала от того, что мне говорят, что делать!"
    mia "Мне просто хочется сделать что-то ... спонтанное и веселое!"
    mia "Почувсвовать свободу..."
    show mia 8
    show player 10
    player_name "Твоя мама не будет возражать?"
    show player 5
    show mia 12
    mia "Мне пофиг."
    show mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Татуировка - это круто. Я просто не хочу, чтобы у тебя были неприятности."
    show player 13
    show mia 12
    mia "Ты собираешься мне помочь?"
    show mia 8
    show player 14
    player_name "Конечно, но как?"
    show player 13
    show mia 10
    mia "Я знаю, ты любишь рисовать, и я видела твои рисунки..."
    mia "...Я надеялась, ты нарисуешь что-нибудь для моей татуировки!"
    show mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29 at Position(xoffset=8)
    player_name "Ты уверена?"
    show player 13 with dissolve
    show mia 10
    mia "Да! У тебя хорошо получается."
    show mia 7
    show player 21
    player_name "Спасибо, но я даже не знаю, чего ты хочешь!"
    show player 13
    show mia 10
    mia "Хм... Я хочу что-нибудь... миленькое!"
    show mia 9
    mia "С красивыми цветами!"
    show mia 7
    show player 24
    player_name "Что делать, если не плучится... и в итоге тебе не понравится?"
    show player 13
    show mia 10
    mia "Я уверена, что все будет хорошо!"
    show mia 7
    show player 14
    player_name "Как скажешь..."
    show player 13
    show mia 10
    mia "Приходи ко мне, когда у тебя что-нибудь будет."
    show mia 7
    show player 14
    player_name "Хорошо."
    show player 13
    show mia 10
    mia "Мне нужно пойти поспать. Увидимся в школе!"
    show mia 7
    show player 36 with dissolve
    player_name "Спокойной ночи!"
    hide player
    hide mia
    with dissolve
    return

label mias_bedroom_mia_midnight_help:
    scene expression game.timer.image("mia_bedroom{}")
    player_name "{b}Мии{/b} здесь нет... И я не вижу ключа."
    return

label mia_study:
    $ game.timer.tick()
    call expression game.dialog_select("mia_study_intro")
    menu:
        mia "Тебе... Тоже нравится?"
        "Да.":
            call expression game.dialog_select("mia_study_like_mia")
            menu:
                "Закрой глаза.":
                    call expression game.dialog_select("mia_study_like_mia_kiss")
                    $ M_player.set("jerk mia", True)
                    $ M_mia.trigger(T_mia_kiss)
        "Нет.":

            call expression game.dialog_select("mia_study_dislike_mia")
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_study_intro:
    scene mia_bedroom_closeup
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Так... Я не знаю, как это сказать..."
    show mia 18
    show player 143
    mia "...И я такая застенчивая перед людьми, особенно перед мальчиками..."
    mia "...но я действительно не хочу учиться."
    show player 145
    show mia 19
    player_name "А?"
    show mia 18
    show player 143
    mia "Я не могла придумать лучшего оправдания, чтобы потусоваться..."
    mia "... И ты мне вроде как нравишься!"
    show player 145
    show mia 14
    player_name "Почему ты просто не сказала мне об этом раньше?"
    show mia 18
    show player 143
    mia "Ну, я хотела провести время вместе, но моя мама никогда не позволит этого..."
    show mia 13
    show player 145
    player_name "Все нормально. Я понимаю!"
    show player 142
    player_name "Очень мило с твоей стороны пригласить меня. Мне нравится это..."
    show mia 16
    show player 141
    mia "Как насчет тебя?"
    show mia 13
    show player 145
    player_name "А?"
    show mia 18
    show player 143
    return

label mia_study_like_mia:
    show mia 19
    show player 145
    player_name "Хорошо..."
    show mia 15
    show player 141
    mia "Правда??"
    show mia 16
    show player 143
    mia "Так... Что тебе во мне нравится?"
    show mia 19
    show player 145
    player_name "Я думаю, ты очень милая... ты знаешь..."
    player_name "... Ну когда ты говоришь со мной в школе и все такое!"
    show mia 18
    show player 141
    mia "Как мило!"
    show mia 19
    show player 142
    player_name "Я также думаю, что ты очень красивая!"
    show player 141
    mia "..."
    show mia 18
    mia "Правда?"
    return

label mia_study_like_mia_kiss:
    show player 142
    show mia 19
    player_name "Закрой глаза..."
    show mia 18
    show player 141
    mia "Зачем?"
    show mia 19
    show player 142
    player_name "...Просто закрой."
    show mia 17
    show player 147
    mia "Хмм..."
    show mia 18
    mia "..."
    show player 148
    show mia 20 at Position (xpos = 647, ypos = 574) with hpunch
    mia "{b}!!!{/b}"
    show mia 18 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 143
    mia "...Я не могу этого сделать... Пока!"
    show mia 14
    show player 146
    player_name "...Извени, я думал-"
    show mia 22
    show player 144
    mia "Нет! Все нормально! Извините. Я просто не могу, прямо сейчас..."
    mia "...Если моя мама увидит, мы - трупы."
    show mia 14
    show player 146
    player_name "О, прости..."
    show player 143
    show mia 18
    mia "Все в порядке..."
    mia "Мой отец, вероятно, не взбесится так сильно, как моя мама..."
    mia "На самом деле он классный, когда {b}мамы{/b} нет рядом."
    show mia 22
    mia "{b}Мама{/b} просто... очень религиозная. Меня бы, наверное, заперли и заставили изучать Библию."
    show mia 14
    show player 145
    player_name "Вау. Правда?"
    show player 141
    show mia 18
    mia "Она все о грехах и прочем."
    show mia 22
    mia "Она думает, что ты развращаешь меня и заставляешь делать плохие вещи..."
    show mia 14
    show player 143
    player_name "..."
    show player 145
    player_name "Я...Я бы не стал этого делать!"
    show player 143
    show mia 15
    mia "Ха-ха, я знаю - это глупость."
    show player 144
    show mia 16
    mia "В любом случае, уже поздно и {b}Мама{/b} будет меня проверять."
    mia "Так что мне пора ложиться спать."
    show mia 13
    show player 142
    player_name "Хорошо, {b}Mia{/b}."
    player_name "Увидимся в {b}школе{/b}!"
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}.jpg")
    show mia 7 at right
    show player 21 at left
    with dissolve
    player_name "Значит, увидимся позже?"
    show mia 10
    show player 13
    mia "Да..."
    mia "Спасибо что пришел."
    show mia 7
    show player 21
    player_name "Спокойной ночи!"
    return

label mia_study_dislike_mia:
    show mia 14
    show player 146
    player_name "Я вижу тебя больше как ... друга."
    show mia 22
    show player 144
    mia "О...понятно."
    show mia 14
    show player 145
    player_name "Но, это первый раз, когда мы тусовались!"
    player_name "Подожди некоторое время. Может, мы сможем узнать друг друга получше!"
    show mia 22
    show player 144
    mia "Да, хорошо..."
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}.jpg")
    show mia 8 at right
    show player 21 at left
    with dissolve
    player_name "Значит, увидимся позже?"
    show player 13
    show mia 12
    mia "Да..."
    mia "Спасибо что пришел."
    show mia 8
    show player 21
    player_name "Спокойной ночи!"
    return

label mia_strip_show:
    call expression game.dialog_select("mia_strip_show_dialogue")
    $ game.timer.tick()
    $ M_mia.trigger(T_mia_strip_tease)
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_strip_show_dialogue:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Ты здесь!!"
    show mia 7
    show player 14
    player_name "Привет {b}Мия{/b}. Я опоздал?"
    show player 13
    show mia 10
    mia "Нет."
    show mia 12
    mia "Но ты уверен, что никто не видел, как ты сюда пришел?"
    show mia 8
    show player 10
    player_name "Эхх... Я практически уверен в этом?"
    show player 12
    player_name "Есть что-то, о чем мне стоит беспокоиться?"
    show player 11
    show mia 10
    mia "Нет, конечно же, нет. Просто убедится, что никто не будет мешать нам!"
    show mia 7
    show player 14
    player_name "Хорошо."
    player_name "Так что ты хотела сделать?"
    show player 13
    show mia 9
    mia "У меня есть...сюрприз для тебя."
    show mia 7
    show player 18
    player_name "..."
    show player 13
    show mia 10
    mia "Я хотела наконец показать тебе свою татуировку..."
    mia "...Но я хочу сделать это особенным способом."
    show mia 7
    player_name "..."
    show mia 10
    mia "Сядь на мою кровать..."
    scene black
    with fade
    hide player
    hide mia

    scene mia_bedroom_strip01
    show mia_strip 1 at Position (xpos=457,ypos=670)
    show player mia_strip 18 at right
    with fade
    pause
    show mia_strip 2
    mia "Это благодарность тебе за то, что так добр ко мне..."
    show mia_strip 3 at Position (xoffset=39) with dissolve
    pause
    show mia_strip 4 at Position (xoffset=15) with dissolve
    pause
    show mia_strip 5 with dissolve
    player_name "..."
    show mia_strip 6
    mia "Как думаешь...Я хорошо выгляжу?"
    show mia_strip 5
    player_name "Я-Конечно! Я имею в виду, конечно!"
    show mia_strip 7
    mia "Ха ха, Ты милый..."
    show mia_strip 8 with dissolve
    pause
    show mia_strip 9 with dissolve
    pause
    show mia_strip 10 with dissolve
    pause
    show mia_strip 11 with dissolve
    pause
    show mia_strip 12 with dissolve
    pause
    player_name "!!!"
    show mia_strip 13 with dissolve
    pause
    show player mia_strip 19 with dissolve
    player_name "( ВАУ!!! )"
    show mia_strip 14 with dissolve
    pause
    show mia_strip 15
    mia "И? Тебе нравится?"
    show mia_strip 14
    player_name "Мне-Мне нравится, что? Прости?"
    show mia_strip 16
    show player mia_strip 20 with dissolve
    mia "Моя татуировка, глупенький! Тебе нравится-"
    show mia_strip 17
    mia "!!!"
    mia "О, боже... Что у тебя в штанах?!"
    scene mia_bedroom_strip02
    pause
    scene mia_bedroom_strip03
    pause
    scene mia_bedroom_strip04
    helen "..."
    scene black
    with fade
    hide player
    hide helen
    hide mia

    scene location_mia_bedroom_closeup
    show helen 6f at Position (xpos=431)
    show player 22f at right
    show mia 37 at Position (xpos=674)
    with dissolve
    pause
    show mia 39
    mia "{b}МАМА{/b}!!!"
    show mia 37
    show helen 5f
    helen "Что это у тебя на ноге?!"
    show helen 7f at Position (xpos=441) with dissolve
    helen "!!!"
    helen "Что этот МАЛЬЧИК ЗДЕСЬ делает?!!"
    show helen 8f
    show mia 36
    mia "Я могу все объяснить, {b}Мама{/b}!"
    show mia 35
    show helen 7f
    helen "Не могу поверить, что ты так со мной поступаешь..."
    helen "...После воспитания ты будешь хорошей дочерью..."
    helen "...ты выбрала стать прелюбодеем, грешником, НЕГОДЯЕМ!!"
    show helen 8f
    show player 16f
    show mia 38
    mia "..."
    show player 12f
    player_name "Это была моя идея! {b}Mia{/b} не-"
    show player 22f
    show helen 7f
    helen "Кто разрешил тебе говорить?! ИЛИ БЫТЬ ЗДЕСЬ ВООБЩЕ! {b}В МОЕМ ДОМЕ{/b}!!!"
    show helen 8f
    show mia 37
    show player 23f
    player_name "!!!" with hpunch
    show player 22f
    show helen 9f at left with fastdissolve
    helen "Убирайтесь отсюда, {b}СЕЙЧАС{/b}!!"
    show mia 39
    mia "{b}Мама{/b}!!!"
    scene black
    with fade
    hide player
    hide mia
    hide helen

    scene miahouse_night
    show player 24 with dissolve
    player_name "Вау!"
    show player 37 at Position (xoffset=41) with dissolve
    player_name "{b}Helen{/b} действительно разозлилась."
    show player 25 with dissolve
    player_name "Я просто надеюсь, что у {b}Mia{/b} не будет много проблем..."
    hide player with dissolve
    return

label mia_bedroom_sex:
    call expression game.dialog_select("mia_bedroom_sex_intro")
    if not store._in_replay == None:
        call expression game.dialog_select("mia_bedroom_sex_study")
        call expression game.dialog_select("mia_bedroom_sex_sure")
        jump expression game.dialog_select("mia_strip_repeat")
    menu:
        "Учится":
            call expression game.dialog_select("mia_bedroom_sex_study")
            menu:
                "Может потом.":
                    call expression game.dialog_select("mia_bedroom_sex_maybe_later")
                "Конечно!":

                    call expression game.dialog_select("mia_bedroom_sex_sure")
                    label mia_strip_repeat:
                        call expression game.dialog_select("mia_bedroom_sex_strip_repeat")

                    if M_mia.get("cum 1st choice") == "":
                        call expression game.dialog_select("mia_bedroom_sex_first_intro")
                    else:

                        call expression game.dialog_select("mia_bedroom_sex_repeat_intro")
                    menu:
                        "В попу.":
                            $ M_mia.set("anal sex", True)
                            call expression game.dialog_select("mia_bedroom_sex_butt_intro")

                            label mia_butt_start:
                                call expression game.dialog_select("mia_bedroom_sex_butt_start")

                            $ anim_toggle = True
                            jump expression game.dialog_select("mia_bedroom_sex_loop")

                        "Мне нравится другой способ." if store._in_replay == None and player.stats.chr() < 7:
                            $ M_mia.set("anal sex", True)
                            call expression game.dialog_select("mia_bedroom_sex_vaginal_stat_fail")
                            jump expression game.dialog_select("mia_butt_start")

                        "Только кончик!" if not store._in_replay == None or player.stats.chr() >= 7:
                            $ M_mia.set("anal sex", False)
                            if not M_mia.is_set("vaginal sex"):
                                $ M_mia.set("vaginal sex", True)
                                call expression game.dialog_select("mia_bedroom_sex_vaginal_first_intro")
                            else:

                                call expression game.dialog_select("mia_bedroom_sex_vaginal_repeat_intro")

                            call expression game.dialog_select("mia_bedroom_sex_vaginal_intro")
                            $ M_mia.set("sex speed", .125)
                            jump expression game.dialog_select("mia_bedroom_sex_loop")
    $ game.main()

label mia_bedroom_sex_intro:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Я так рада, что ты пришел."
    show mia 7
    show player 14
    player_name "Привет, {b}Мия{/b}."
    player_name "Твои родители снова смотрят телевизор вместе, да?"
    show player 13
    show mia 10
    mia "Да. Приятно, что все снова стало нормальным."
    mia "Ну что потусуемся?"
    mia "Или ты здесь, чтобы попробовать мою новую методику обучения?"
    show mia 7
    return

label mia_bedroom_sex_study:
    show player 14
    player_name "Думаю, нам надо заниматься."
    show player 13
    show mia 10
    mia "Конечно!"
    mia "Тогда давайте сделаем это!"
    mia "Давай я соберу все учебники и лягу на кровать?"
    show mia 7
    show player 14
    player_name "Ух... Хорошо."
    hide player
    hide mia
    with dissolve

    scene mia_bedroom_closeup with fade
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Теперь, по крайней мере, похоже, что мы учимся!"
    show mia 13
    player_name "..."
    show mia 16
    mia "Извините... Наверное, я просто взволнована, чтобы тусить, как мы привыкли ..."
    show mia 13
    show player 142
    player_name "Не беспокойся об этом. Я просто рад, что ты снова счастлива."
    show player 141
    show mia 16
    mia "Спасибо, {b}[firstname]{/b}."
    show mia 15
    mia "Ты все еще думаешь о том времени, когда я показала тебе свою татуировку?"
    show mia 13
    show player 145
    player_name "Конечно!"
    player_name "Ты выглядела такой красивой."
    show player 144
    show mia 15
    mia "Не заставляй меня краснеть."
    show mia 17
    show player 141
    player_name "..."
    show player mia_bed_kiss 53
    show mia 52
    with dissolve
    mia "!!!"
    hide player
    show mia 54
    with dissolve
    pause
    mia "Мммм..."
    show player 144 zorder 0 at Position (xpos = 250, ypos = 578)
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    with dissolve
    mia "Ты очень хорошо целуешься...."
    show mia 13
    show player 145
    player_name "...Спасибо."
    show player 144
    mia "..."
    show mia 16
    mia "Хочешь знать о том трюке с исследованием, о котором я читала?"
    show mia 13
    show player 142
    player_name "Конечно!"
    show player 141
    mia "..."
    show mia 16
    mia "Я надеялся попробовать в ту ночь, когда мама застукала нас."
    show mia 13
    show player 142
    player_name "Ох?"
    show player 141
    show mia 16
    mia "Я...Я всегда хотела попробовать учиться голой..."
    show mia 13
    show player 143
    player_name "!!!"
    show mia 16
    mia "Ты хочешь учиться со мной...голым?"
    show mia 13
    return

label mia_bedroom_sex_maybe_later:
    show player 146
    player_name "Я имею в виду... Я бы очень хотел, но мне нужно вернуться домой."
    show player 141
    show mia 18
    mia "О? Неужели [deb_name] выпорет тебя если ты придешь домой поздно?"
    show mia 13
    show player 145
    player_name "Хе... Хе... Нет..."
    show player 141
    show mia 18
    mia "Я просто прикалываюсь. Уже довольно-таки поздно...и я тоже начинаю уставать."
    hide mia
    hide player
    with dissolve

    scene location_mia_bedroom_closeup
    show mia 7 at right
    show player 14 at left
    with dissolve
    player_name "Спокойной ночи, {b}Мия{/b}."
    player_name "Увидемся завтра."
    show player 13
    show mia 10
    mia "Спокойной ночи, {b}[firstname]{/b}."
    hide player
    show mia 49 at left
    with dissolve
    pause
    show player 13 at left
    show mia 10 at Position (xpos=300)
    with dissolve
    mia "Я буду... думаю о тебе сегодня вечером..."
    hide player
    hide mia
    with dissolve
    return

label mia_bedroom_sex_sure:
    show player 142
    player_name "Я с удовольствием помогу тебе!"
    show player 141
    show mia 16
    mia "Великолепно!"
    mia "Умм..."
    show mia 16
    mia "Как насчет того, чтобы сесть на кровать, пока я снова разденусь."
    mia "Мои родители сказали, что больше не будут нас прерывать."
    mia "Так что просто расслабься..."
    mia "...и наслождайся шоу."
    hide player
    hide mia
    with dissolve
    return

label mia_bedroom_sex_strip_repeat:
    scene mia_bedroom_strip01 with fade
    show player mia_strip 18 at right
    show mia_strip 1 at Position (xpos=457,ypos=670)
    pause
    show mia_strip 3 at Position (xoffset=39) with dissolve
    pause
    show mia_strip 4 at Position (xoffset=15) with dissolve
    pause
    show mia_strip 5 with dissolve
    pause
    show mia_strip 6
    mia "Думаешь... Я хорошо выгляжу?"
    show mia_strip 5
    player_name "Я-Конечно! Я имею в виду, конечно!"
    show mia_strip 7
    mia "Ха Ха, ты милый."
    show mia_strip 8 with dissolve
    pause
    show mia_strip 9 with dissolve
    pause
    show mia_strip 10 with dissolve
    pause
    show mia_strip 11 with dissolve
    pause
    show mia_strip 12 with dissolve
    pause
    player_name "!!!"
    hide player
    show player mia_strip 18 at right
    show mia_strip 13
    with dissolve
    pause
    show player mia_strip 19 with dissolve
    player_name "( ВАУ!!! )"
    hide mia_strip
    show mia_strip 14 at Position (xpos=457,ypos=670)
    with dissolve
    pause
    show mia_strip 17
    mia "!!!"
    show mia_strip 16
    mia "Я думаю, ты действительно думаешь, что я выгляжу красиво."
    show mia_strip 15
    mia "Моя татуировка все еще хорошо выглядит?"
    show mia_strip 14
    player_name "Она выглядит очень мило на тебе."
    show mia_strip 15
    mia "Правда?"
    mia "...Что насчет моей попы?"
    show mia_strip 14
    player_name "{b}*глоток*{/b}"
    player_name "Ухх... Да... Я думаю... конечно!"
    player_name "Ты вся - сексуальная девушка!"
    show mia_strip 16
    mia "Ха ха ха."
    show mia_strip 15
    mia "Не говори мне, что ты... нервничаешь, {b}[firstname]{/b}."
    player_name "Может быть чуть чуть..."
    show mia_strip 22 with dissolve
    mia "Я тоже..."
    show mia_strip 21
    show player mia_strip 20 with dissolve
    pause
    show mia_strip 22
    mia "Позволь мне сделать домашнюю работу."
    show mia_strip 23 with dissolve
    pause
    show mia_strip 26 with dissolve
    mia "Вот она!"
    show mia_strip 25
    mia "Ты готов?"
    show mia_strip 24
    player_name "Да!"
    show mia_strip 25
    mia "Вау..."
    mia "Я понятия не имела, что они такие большие..."
    show mia_strip 24
    player_name "О... Да..."
    show mia_strip 25
    mia "Умм... Ладно, давай я лягу на кровать..."
    mia "...И ты присоединишься ко мне..."
    show mia_strip 27 with dissolve
    pause
    scene black with fade
    hide player
    hide mia
    pause
    scene mia_bed_sex with fade
    return

label mia_bedroom_sex_first_intro:
    show mias 2 with dissolve
    mia "Глупый мальчишка. Как ты собираешься там учиться?"
    show mias 1
    player_name "О... Я могу видеть все отсюда."
    player_name "Все норм."
    show mias 2
    mia "Бьюсь об заклад."
    mia "..."
    show mias 5
    mia "Ум..."
    mia "{b}[firstname]{/b}?"
    show mias 1
    player_name "Да, {b}Мия{/b}?"
    show mias 5
    mia "..."
    mia "Ты хочешь заняться сексом?"
    show mias 1
    player_name "!!!"
    show mias 2
    mia "Каждый раз, когда я думала об учебе голышом..."
    mia "...Я вроде как фантазировала и у меня получился... секс."
    show mias 5
    mia "Это моя маленькая тайная фантазия..."
    show mias 2
    mia "Хочешь попробовать?"
    show mias 1
    player_name "Да!"
    show mias 2
    mia "Я так и думала..."
    show mias 5
    mia "Но... умм..."
    mia "У меня есть одна просьба."
    mia "Можешь это сделать..."
    mia "В попу?"
    show mias 2
    mia "Мои родители говорят, что я должна подождать, пока выйду замуж."
    mia "Но я думаю, что это не повредит если сделать в попу."
    mia "Ты не против?"
    show mias 5
    mia "Если тебе это кажется отвратительным... Я пойму..."
    show mias 1
    return

label mia_bedroom_sex_repeat_intro:
    show mias 2
    mia "Я думала, ты хочешь позаниматься голышом на этот раз?"
    show mias 1
    player_name "Я заниматься...ты."
    show mias 2
    mia "Будет трудно учиться, если ты не расслабишься."
    mia "Ха ха!"
    mia "Хочешь сделать это в попу?"
    show mias 1
    return

label mia_bedroom_sex_butt_intro:
    player_name "Я не думаю, что это отвратительно."
    player_name "Довольно редко можно услышать, что девушка хочет сделать это туда."
    show mias 2
    mia "Ха ха."
    mia "Я редкая девочка."
    return

label mia_bedroom_sex_butt_start:
    show mias 4
    mia "Только...вставляй медленно, чтобы не было больно."
    mia "Я не думала, что у тебя такой...большой."
    show mias 3
    pause
    show mias 5
    player_name "Хорошо, спасибо за подсказку..."
    show mias 6b
    mia "Ой!"
    player_name "Извени!"
    mia "Не двигайся... Пожалуйста..."
    player_name "Хорошо. Скажи когда я могу продолжать."
    mia "..."
    mia "Хорошо... Давай потихоньку."
    show mias 7b
    pause
    show mias 8b
    pause
    show mias 9b
    mia "..."
    player_name "Я полностью внутри."
    player_name "Расслабся."
    mia "Очень большой!"
    player_name "Да ... довольно плотно."
    mia "Хорошо. Только помедленнее."
    show mias 10b
    pause
    show mias 11b
    mia "Это не... плохо..."
    player_name "Готова?"
    mia "Ух Ухух."
    return

label mia_bedroom_sex_vaginal_stat_fail:
    show mias 1
    player_name "[chr_warn]Но другой путь намного лучше {b}Мии{/b}."
    player_name "[chr_warn]...Не думая, что кто-то узнает что мы делали это."
    show mias 4
    mia "[chr_warn]Я буду знать, хотя."
    show mias 3
    player_name "[chr_warn]Ну... это буду чувствовать себя намного лучше-"
    show mias 5
    mia "[chr_warn]Нет, если ты хочешь сделать это со мной, используй мою попу."
    player_name "[chr_warn]...Хорошо."
    return

label mia_bedroom_sex_vaginal_first_intro:
    player_name "Я обещаю, что не войду весь."
    show mias 2
    mia "Только кончик? ...Ты уверен?"
    show mias 1
    player_name "Это даже не считается, если просто кончик..."
    show mias 2
    mia "Ха ха!"
    mia "Тогда все может быть в порядке..."
    mia "Но просто двигайся медленно... Это мой первый раз..."
    show mias 6
    mia "О!"
    mia "Даже кончик у тебя такой большой!"
    show mias 7
    mia "Как...чувствуешь себя?"
    player_name "Очень хорошо."
    mia "..."
    mia "...Давай немного глубже..."
    player_name "Что?"
    mia "Можешь немного глубже?"
    player_name "...Хорошо."
    show mias 8
    pause
    show mias 7
    pause
    show mias 8
    player_name "Теперь входить и выходить легче."
    show mias 7_8
    pause
    mia "Охх...."
    pause
    mia "Охххх...."
    mia "Глубже {b}[firstname]{/b}."
    return

label mia_bedroom_sex_vaginal_repeat_intro:
    show mias 2
    mia "Твой кончик зашел глубоко."
    show mias 1
    player_name "...Да..."
    player_name "Извени."
    show mias 2
    mia "Не переживай.Мне понравилось."
    mia "И я хочу еще."
    show mias 6
    mia "Охх!"
    show mias 7_8
    pause
    mia "Как...чувствуешь себя?"
    player_name "Очень хорошо."
    mia "...Входи на полную..."
    return

label mia_bedroom_sex_vaginal_intro:
    show mias 9
    mia "Оххх!!!"
    show expression AnimatedImage("mias", [7,8,9,10,11], M_mia) as mias
    pause
    mia "Аххх!!!"
    mia "Потрясающее ощущение!"
    pause
    mia "Быстрее, {b}[firstname]{/b}!"
    return

label mia_bedroom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if M_mia.is_set("anal sex"):
                show expression AnimatedImage("mias", ["7b","8b","9b","10b","11b"], M_mia) as mias
            else:
                show expression AnimatedImage("mias", [7,8,9,10,11], M_mia) as mias
            pause 6
            if animcounter in [2]:
                call expression game.dialog_select("mia_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                if M_mia.is_set("anal sex"):
                    show expression "mias {}b".format(pose_list[pose_counter]) as mias
                else:
                    show expression "mias {}".format(pose_list[pose_counter]) as mias
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [2]:
                call expression game.dialog_select("mia_hscene_dialog")
        $ animcounter += 1

    player_name "{b}Мия{/b}, куда хочешь чтобы я кончил?"
    mia "...куда угодно."
    call screen mia_bedroom_sex_options

label mia_hscene_dialog:
    mia "Ахххх!!!{p=1}{nw}"
    return

label mia_bedroom_sex_cum_outside:
    call expression game.dialog_select("mia_bedroom_sex_cum_outside_intro")
    if M_mia.get("cum 1st choice") == "":
        $ M_mia.set("cum 1st choice", "Outside")
        call expression game.dialog_select("mia_bedroom_sex_cum_outside_first")
    else:

        call expression game.dialog_select("mia_bedroom_sex_cum_outside_repeat")
        if M_mia.is_set("cum 1st choice") == "Inside":
            call expression game.dialog_select("mia_bedroom_sex_cum_outside_first_inside")

    call expression game.dialog_select("mia_bedroom_sex_cum_outside_after")
    jump expression game.dialog_select("mia_bedroom_sex_end")

label mia_bedroom_sex_cum_outside_intro:
    show mias 14 with flash
    player_name "УХХХ!!!"
    mia "О!!!"
    pause
    return

label mia_bedroom_sex_cum_outside_first:
    show mias 16
    mia "Так много спермы получилось."
    show mias 15
    player_name "Да."
    show mias 16
    mia "Я чувствую, как он бежит по моей спине."
    show mias 15
    player_name "Извени."
    show mias 16
    mia "Можешь принести мне салфетки?"
    mia "Я не хочу, чтобы она протекла на простыни..."
    return

label mia_bedroom_sex_cum_outside_repeat:
    show mias 16
    mia "Это было здорово!"
    mia "Ты кончил довольно быстро!"
    show mias 15
    player_name "Извени..."
    show mias 16
    mia "Я пошутила."
    return

label mia_bedroom_sex_cum_outside_first_inside:
    mia "Легче убирать, когда ты просто кончаешь внутрь меня."
    return

label mia_bedroom_sex_cum_outside_after:
    mia "Мне лучше привести себя в порядок."
    mia "Мама может увидеть пятна на простынях..."
    show mias 15
    player_name "Извени..."
    show mias 16
    mia "Не беспокойся."
    mia "Это было здорово, {b}[firstname]{/b}."
    show mias 15
    player_name "Да, точно."
    return

label mia_bedroom_sex_cum_inside:
    if M_mia.get("cum 1st choice") == "":
        $ M_mia.set("cum 1st choice", "Inside")

    if M_mia.is_set("anal sex"):
        call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_intro")
        if M_mia.get("sex 1st choice") == "":
            $ M_mia.set("sex 1st choice", "Anal")
            call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_first")
        call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_after")
    else:

        call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_intro")
        if M_mia.get("sex 1st choice") == "":
            $ M_mia.set("sex 1st choice", "Vaginal")
            call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_first")
        else:

            call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_repeat")
    jump expression game.dialog_select("mia_bedroom_sex_end")

label mia_bedroom_sex_cum_inside_anal_intro:
    show mias 12b_13b with flash
    player_name "Уххх!!!"
    mia "Оххх!!!"
    show mias 18b with dissolve
    mia "Вау!"
    return

label mia_bedroom_sex_cum_inside_anal_first:
    mia "Так вот что такое Анальный секс..."
    show mias 17b
    player_name "Больно?"
    show mias 18b
    mia "Все было не так уж и плохо."
    return

label mia_bedroom_sex_cum_inside_anal_after:
    mia "Тебе понравилось?"
    show mias 17b
    player_name "Да!"
    player_name "На самом деле...плотно."
    show mias 18b
    mia "Спасибо, что не торопишься."
    show mias 17b
    player_name "Незачто, {b}Mia{/b}."
    show mias 18b
    mia "Мне лучше привести себя в порядок."
    mia "Мама может увидеть пятна на простынях..."
    show mias 17b
    player_name "Извени..."
    show mias 18b
    mia "Не беспокойся."
    mia "Это было здорово, {b}[firstname]{/b}."
    show mias 17b
    player_name "Да, точно."
    return

label mia_bedroom_sex_cum_inside_vaginal_intro:
    show mias 12_13 with flash
    player_name "УХХ!!!"
    mia "ОХХ!!!"
    return

label mia_bedroom_sex_cum_inside_vaginal_first:
    show mias 18 with dissolve
    mia "Это было потрясающе!"
    mia "Я никогда не чувствовал ничего подобного."
    show mias 17
    player_name "!!!"
    player_name "Ты имеешь в виду, никогда....не кончала?"
    show mias 18
    mia "Нет, у меня был оргазм раньше..."
    mia "...Я имела в виду... Чувствовать, как ты кончаешь в меня и все такое."
    show mias 17
    player_name "Ох..."
    show mias 18
    mia "Не расстраивайся. Я тоже этого хотела."
    return

label mia_bedroom_sex_cum_inside_vaginal_repeat:
    show mias 18
    mia "Это было фантастично!"
    mia "Я до сих пор не могу поверить, что оргазм ощущается именно так."
    mia "От одной мысли об этом у меня мурашки по коже."
    show mias 17
    player_name "Правда? Мне... тоже очень понравилось."
    show mias 18
    mia "Мне лучше привести себя в порядок."
    mia "Мама может увидеть пятна на простынях..."
    show mias 17
    player_name "Извени..."
    show mias 18
    mia "Не беспокойся."
    mia "Это было здорово, {b}[firstname]{/b}."
    show mias 17
    player_name "Да, точно."
    return

label mia_bedroom_sex_end:
    if M_mia.is_set("anal sex") and M_mia.get("butt speed") < 2:
        $ M_mia.set("butt speed", M_mia.get("butt speed") + 1)
    call expression game.dialog_select("mia_bedroom_sex_end_dialogue")
    $ persistent.cookie_jar["Mia"]["unlocked"] = True
    $ persistent.cookie_jar["Mia"]["gallery"]["03_unlocked"] = True
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_miahouse)
    $ M_mia.trigger(T_mia_sex)
    $ game.main()

label mia_bedroom_sex_end_dialogue:
    hide mias
    scene black
    with fade
    pause
    scene location_mia_bedroom_closeup with fade
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Спасибо, что помогаешь мне учиться и проводишь со мной время."
    show mia 9
    mia "Было немного трудно сосредоточиться на учебе."
    show player 17
    player_name "Ха ха ха!"
    show mia 7
    show player 14
    player_name "Да, мне тоже нравилось заниматься с тобой."
    show player 17
    player_name "Это тот вид обучения, в котором я определенно могу отстать."
    show player 18
    show mia 9
    mia "Ха ха!"
    show mia 7
    pause
    show player 10
    player_name "...Тебе было больно?"
    show player 5
    show mia 10
    mia "Немного... Хех Хех."
    mia "Но мне очень понравилось."
    show mia 7
    show player 14
    player_name "Мне тоже."
    player_name "Мне пора уходить. Уже поздно."
    hide player
    show mia 49 at left
    with dissolve
    pause
    show player 13 at left
    show mia 10 at Position (xpos=300)
    with dissolve
    mia "Спокойной ночи, {b}[firstname]{/b}."
    mia "Возвращайся и навещай меня снова...если хочешь заниматься."
    show mia 7
    show player 14
    player_name "Хорошо!"
    player_name "Спокойной ночи, {b}Mia{/b}."
    hide player
    hide mia
    with dissolve
    $ renpy.end_replay()
    return

label mia_bedroom_teddy:
    if M_mia.is_set("telescope teddy seen"):
        call expression game.dialog_select("mia_bedroom_teddy_masturbation_seen")
    else:

        call expression game.dialog_select("mia_bedroom_teddy_masturbation_havent_seen")
    $ game.main()

label mia_bedroom_teddy_masturbation_seen:
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}_blur.jpg")
    show player 439 with dissolve
    player_name "Это плюшевый медведь {b}Mia{/b} с которым она играла ранее."
    player_name "Кажется, у него немного странный запах..."
    show player 441
    player_name "Пахнет как..."
    show player 440 with dissolve
    player_name "*нюхать*"
    pause
    show player 441 with dissolve
    player_name "Рыба..."
    player_name "Мистер Тедди, вы видели ужасные вещи, не так ли?"
    player_name "Интересно, почему он ей так нравится?"
    show player 438
    pause
    show player 439
    player_name "Похоже, сзади есть дырка...."
    player_name "Хух. У него есть маленькая сумочка."
    player_name "Похоже, там можно что-то спрятать."
    hide player with dissolve
    return

label mia_bedroom_teddy_masturbation_havent_seen:
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}_blur.jpg")
    show player 438 with dissolve
    pause
    show player 439
    player_name "Этот Мишка был в ее комнате, с тех пор когда мы были детьми."
    player_name "Интересно, почему он до сих пор у нее..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
