label bedroom_mc_start_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    player_name "Ух... Ненавижу рано просыпаться."
    show player 9
    player_name "( {b}Эрик{/b} ничего не написал. Может он ещё спит. )"
    player_name "( Зайду к нему по пути в школу. )"
    hide player 9 with dissolve
    return

label bedroom_mc_weekday_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Нужно собираться в школу... )"
    hide player with dissolve
    return

label bedroom_mc_weekend_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Чего бы поделать на выходных... )"
    hide player with dissolve
    return

label bedroom_erik_bullying:
    scene black with fade
    deb "Милый?"
    pause
    deb "Просыпайся."
    scene expression game.timer.image("bedroom{}") with fade
    show debbie 14f at left
    show player 101bf at right
    with dissolve
    player_name "Ха? {b}[deb_name]{/b}? Сколько уже времени?"
    show player 100bf
    show debbie 13f
    deb "{b}Миссис Джонсон{/b} внизу, она хочет тебя увидеть."
    show debbie 14f
    show player 101bf
    player_name "{b}Миссис Джонсон{/b}? Увидеть меня?"
    show player 100bf
    show debbie 13f
    deb "Она ничего не мне объяснила, только сказал, что хочет поговорить с тобой до того, как ты куда-нибудь направишься."
    show debbie 14f
    show player 101bf
    player_name "Оу, Ок. Только дайте мне одеться."
    show player 100bf
    show debbie 13f
    deb "Конечно..."
    show debbie 14f
    pause
    show debbie 13f
    deb "Есть что-то, о чем я должна знать, {b}[firstname]{/b}?"
    show debbie 14f
    player_name "..."
    show player 101bf
    player_name "Я, как и ты, не знаю, почему она здесь, {b}[deb_name]{/b}."
    show player 100bf
    deb "..."
    show debbie 13f
    deb "Окей, милый."
    hide debbie
    hide player
    with dissolve
    return

label bedroom_mia_tattoo_help:
    scene expression game.timer.image("bedroom{}")
    show player 35 with dissolve
    player_name "( Нужна сделать хоть что-то для это её тату идеи. )"
    show player 34
    player_name "Хмм..."
    show player 35
    player_name "( Может, я смогу воспользоваться {b}мольбертом в классе искусств{/b}! )"
    show player 33
    player_name "( Там я и смогу придумать какой-нибудь интересный дизайн. )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 101 with dissolve
    player_name "Надо поспать."
    hide player with dissolve
    show unlock53 at truecenter with dissolve
    pause
    hide unlock53 with dissolve
    return

label bedroom_mia_strip_aftermath_grounded:
    scene expression game.timer.image("bedroom{}")
    show player 24 with dissolve
    player_name "( Не могу поверить, что мы с{b}Мией{/b} больше не сможем видеться. )"
    show player 25
    player_name "( Её родители мне не доверяют. )"
    show player 35
    player_name "( Может я смогу как-нибудь примириться с ними... )"
    hide player with dissolve
    return

label bedroom_mia_concerning_visit:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    pause
    show player 30 at Position (xoffset=-6) with dissolve
    player_name "( Интересно, как у {b}Мии{/b} дела. )"
    show player 12 at Position (xoffset=-6)
    player_name "( Я уже несколько дней ничего от неё не слышал... )"
    player_name "( ...Нужно зайти к ней и узнать, как она себя чувствует... )"
    hide player with dissolve
    return

label bedroom_mia_urgent_message:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Хах?"
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 14 with dissolve
    player_name "( Неужели сообщение... )"
    hide player with dissolve
    return

label bedroom_mia_angelicas_impatience:
    scene expression game.timer.image("bedroom{}")
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Зевает*"
    show player 56f with dissolve
    player_name "( Я должен быть готов к- )"
    show player 11f
    "*Тук-тук-тук*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Ха?"
    deb "Тут кто-то пришел к тебе."
    show debbie 1f
    show player 30f
    player_name "{b}Эрик{/b}?"
    show player 11f
    show debbie 2f
    deb "Нет, милый. Это дама!"
    deb "Она сказала, что предупредила тебя..."
    show debbie 1f
    show player 10f
    player_name "Что?"
    player_name "Но кто-"
    show player 5f
    show debbie 2f
    deb "Она ждет тебя. Так почему бы тебе не {b}одеться и спуститься{/b} наконец."
    hide debbie with dissolve
    show player 12f player_name "Дама?!"
    show player 4f at Position (xoffset=-6) with dissolve
    player_name "Ха..."
    hide player with dissolve
    return

label bedroom_mia_angelicas_home_visit:
    scene expression game.timer.image("bedroom{}")
    show player 13f at right
    show debbie 2f at left
    deb "Милый?"
    show debbie 1f
    show player 17f
    player_name "Доброе утро, {b}[deb_name]{/b}."
    show player 13f
    show debbie 2f
    deb "Доброе."
    deb "Та милая дама снова внизу."
    show debbie 1f
    show player 11f
    player_name "..."
    show player 12f
    player_name "Кто?"
    show player 5f
    show debbie 3f
    deb "Просыпайся уже. Та монахиня снова тут."
    show debbie 1f
    show player 22f
    player_name "!!!"
    deb "Если поторопишься, может успеешь с ней встретиться."
    hide debbie with dissolve
    show player 10f
    player_name "Да что ей надо от меня?"
    hide player with dissolve
    return

label bedroom_mia_angelicas_final_home_visit:
    scene expression game.timer.image("bedroom{}") with fade
    show player 55f at Position (xoffset=-12) with dissolve
    player_name "*Зевает*"
    show player 56f with dissolve
    player_name "Я должен быть готов к-"
    show player 11f
    "*Тук-тук-тук*"
    show debbie 2f at left
    show player 13f
    with dissolve
    deb "Ха?"
    deb "Эта монахиня снова тут..."
    show debbie 1f
    show player 30f
    player_name "Снова?"
    show player 24f
    pause
    show debbie 13f
    deb "Я бы хотела узнать..."
    deb "Что же именно ты сделал для церкви?"
    show debbie 14f
    show player 11f
    player_name "..."
    show debbie 13f
    deb "То есть, просто так странно, что она так часто приходит..."
    show debbie 14bf
    show player 29f at Position (xoffset=-35) with dissolve
    player_name "Да, эм... все в полном... порядке."
    player_name "Она просто... дает мне некоторые поручения."
    player_name "( Ага, хе... хе... )"
    show player 3f at Position (xoffset=-35)
    show debbie 14f
    deb "..."
    show debbie 13f
    deb "Ну, по крайней мере, ты делаешь что-то хорошее для общества..."
    show player 5f with dissolve
    show debbie 2f
    deb "Думаю, что мне не нужно волноваться."
    show debbie 3f
    deb "Что плохого может произойти, если ты будешь проводить время в церкви?"
    hide debbie with dissolve
    show player 11f
    player_name "..."
    show player 37f at Position (xoffset=-41) with dissolve
    player_name "( Ты даже не представляешь... )"
    hide player with dissolve
    return

label bedroom_mom_overheard:
    scene expression game.timer.image("bedroom{}")
    show player 34 with dissolve
    player_name "...{b}*приглушенный голос*{/b}..."
    show player 35
    player_name "( {b}[deb_name]{/b} говорит по телефону? )"
    show player 12
    player_name "( ...Да она просто в бешенстве... )"
    show player 10
    player_name "( Нужно проверить, все ли в порядке. )"
    hide player with dissolve
    return

label bedroom_mom_doorbell:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Кто-то звонит в дверь. )"
    player_name "( Наверное {b}Эрик{/b}... )"
    hide player with dissolve
    return

label bedroom_mom_movie_afterthoughts:
    scene expression game.timer.image("bedroom{}")
    show player 5
    player_name "Ладно, это было очень неловко!"
    player_name "Она явно заметила..."
    player_name "Она, конечно, ничего не сказала."
    player_name "... но мне было крайне некомфортно."
    show player 11
    player_name "Надеюсь, {b}[deb_name]{/b} не расстроилась из-за этого..."
    player_name "..."
    show player 24
    player_name "Ах, ладно, переживать буду завтра. А сейчас нужно немного поспать."
    hide player with dissolve
    return

label bedroom_mom_afterthoughts_two:
    scene location_home_bedroom_night_blur
    show player 13
    player_name "( Это было прекрасно! )"
    player_name "( Соски {b}[deb_name]{/b} такие вкусные... )"
    player_name "( ... К тому же она такая влажная! )"
    show player 5
    player_name "( ... )"
    player_name "( Хотя в конце она вела себя странно. )"
    player_name "( Может нужно ещё раз извиниться? )"
    player_name "( ... )"
    show player 13
    player_name "( Нет смысла сейчас об этом переживать. Я должен поспать. )"
    hide player with dissolve
    return

label bedroom_mom_note:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 101 with dissolve
    player_name "Я должен поспать."
    hide player with dissolve
    return

label bedroom_mom_note_just_wokeup:
    scene expression game.timer.image("bedroom{}")
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Кто-то оставил {b}заметку{/b} на экране моего монитора?"
    hide player with dissolve
    return

label bedroom_mom_chores:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    if randomizer() < 50:
        player_name "Интересно, нужна ли {b}[deb_name]{/b} помощь по дому."
        player_name "Нужно спросить у нее..."
    else:
        player_name "А может, {b}[deb_name]{/b} нужна моя помощь с чем нибудь ещё..."
    hide player with dissolve
    return

label bedroom_mom_search_panties:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( Не могу перестать думать о том моменте в подвале... )"
    player_name "( {b}[deb_name]{/b} вроде как и правда наслаждалась этим массажем. )"
    player_name "( Её ноги такие мягкие и стройные... )"
    show player 11
    player_name "( Так, лосьон же был у неё в ящичке. )"
    player_name "( Я срочно должен на него взглянуть! )"
    show player 13
    player_name "( А сейчас, наверное, cамое подходящее время. )"
    hide player with dissolve
    return

label bedroom_mom_kissing_practice:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "Мне продолжают сниться эти пошлые сны о {b}[deb_name]{/b}."
    player_name "Это сводит меня с ума!"
    show player 5
    player_name "..."
    player_name "Я, наверное, должен {b}поговорить с ней{/b} об этом..."
    hide player with dissolve
    return

label bedroom_bissette_french_food_assignment:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "Я должен закончить мое задание по французскому."
    show player 14
    player_name "Ведь теперь у меня есть всё для это."
    hide player with dissolve
    return

label bedroom_sis_couch_1:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Я слышал кого-то в коридоре... Это дверь {b}[jen_name]{/b}? )"
    show player 4
    player_name "( Интересно, что она там делает. )"
    hide player with dissolve
    return

label bedroom_sis_couch_3:
    scene expression game.timer.image("bedroom{}")
    show player 4 with dissolve
    player_name "( Интересно, будет ли {b}новая порнуха{/b} сегодня по телевизору. )"
    show player 26
    player_name "( Нужно будет проверить, пока все будут спать... )"
    hide player with dissolve
    return

label bedroom_study01:
    if M_bissette.is_state(S_bissette_french_food_assignment):
        call expression game.dialog_select("bedroom_bissette_french_food_assignment_after")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()

    elif M_bissette.is_state(S_bissette_do_poem_assignment):
        call expression game.dialog_select("bedroom_bissette_do_poem_assignment")
        $ M_bissette.trigger(T_bissette_do_assignment)
        $ game.timer.tick()
    else:

        scene expression game.timer.image("bedroom{}")
        if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_martinez_books, S_bissette_got_martinez_eriks_books]):
            call expression game.dialog_select("bedroom_bissette_find_books")
        else:

            call expression game.dialog_select("bedroom_no_school_work")
    $ game.main()

label bedroom_bissette_french_food_assignment_after:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "В это книге есть все, что только можно знать о сыре.\nВсё от создания, готовки и поедания всех сортов сыра...\n...Но я прошелся только по нескольким главам, надеюсь, этого хватит, чтобы удовлетворить {b}Мисс Биссетт{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_bissette_do_poem_assignment:
    if not game.timer.is_dark():
        scene studybedroom01
    else:
        scene studybedroom02
    with fade
    show text "Оказывается, что писать стихи - это сложно.\n...А у меня, судя по всему, ещё и проблемы с сосрдоточенностью.\nНо после нескольких часов работы с парой... Перерывов. Я всё таки смог написать хоть что-то!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide studybedroom01
    hide studybedroom02
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 511 with dissolve
    player_name "Наконец-то!"
    player_name "Надеюсь этого хватит, чтобы впечатлить {b}Мисс Биссетт{/b}..."
    player_name "Нужно просто {b}Распечатать{/b} это в {b}компьютерном классе{/b} и дело с концом."
    hide player with dissolve
    return

label bedroom_bissette_find_books:
    show player 73 with dissolve
    player_name "( Мне надо найти нужный {b}учебник{/b}, прежде чем я смогу закончить {b}домашку{/b}... )"
    player_name "( Скорее всего, я смогу найти его в местной {b}библиотеке{/b}. )"
    hide player with dissolve
    return

label bedroom_no_school_work:
    show player 1 with dissolve
    player_name "( Сейчас у меня нет никаких заданий. )"
    hide player with dissolve
    return

label mia_midnight_text:
    call expression game.dialog_select("mia_midnight_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_midnight_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 442 with dissolve
    player_name "{b}Мия{/b}!? Просит...помощи?"
    player_name "Это что ещё за хрень?"
    player_name "Она попала в беду?"
    show player 443
    player_name "..."
    show player 442
    player_name "Может стоит пойти {b}сейчас её проверить{/b}... Чтобы убедиться, что всё в порядке."
    hide player with dissolve
    return

label mia_urgent_text:
    call expression game.dialog_select("mia_urgent_text_dialogue")
    $ M_mia.trigger(T_mia_message)
    $ game.main()

label mia_urgent_text_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Она не может найти отца?"
    player_name "Лучше пойти к ней и разобраться, в чем дело..."
    hide player with dissolve
    return

label bed_locked:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Я должен сделать кое-что ещё перед сном... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_check_on_mom:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Нужно проверить, как там {b}[deb_name]{/b}... )"
    hide player 10 with dissolve
    $ game.main()

label bedroom_sleeping_jerk_off_roxxy:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496c_496d_496e_496d_496c zorder 0 at Position(xpos=0.3375, ypos=0.875)
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show roxxy dream 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show roxxy dream 2 with dissolve
    rox "Mмм, привет {b}[firstname]{/b}..."
    rox "Я так рада, что ты пришел!"
    show roxxy dream 1 with dissolve
    player_name "..."
    show roxxy dream 2 with dissolve
    rox "Я не могла думать ни о ком другом в последнее время..."
    rox "Ты так сильно мне помог, я думаю, ты заслужил свою награду!"
    rox "Да, как насчет чего-нибудь особенного, чего-то только для тебя?"
    rox "Ты ведь хочешь этого, {b}[firstname]{/b}?"
    show roxxy dream 1 with dissolve
    $ M_player.set("sex speed", .3)
    show player 496c_496d_496e_496d_496c
    player_name "Ты ведь знаешь, что хочу!"
    show roxxy dream 2 with dissolve
    rox "Хехе, тогда просто расслабься и наслаждайся шоу!"
    rox "Только не забывай поглаживать этот большой член, ради меня, {b}[firstname]{/b}!"
    show roxxy dream 3 with dissolve
    $ M_player.set("sex speed", .2)
    show player 496c_496d_496e_496d_496c
    rox "Дай мне Спе!"
    "Спе!"
    rox "Дай мне Р!"
    "Р!"
    rox "Дай мне Мы!"
    "Мы!"
    show player 496f
    rox "Ну и что это?!"
    show player 496g
    player_name "HNNGGG!!!" with flash
    rox "Вау!!!"
    show player 496h
    hide jerkbubble
    hide roxxy dream
    player_name "Ха... Хааа..."
    player_name "Ооо боже, мне так хорошо..."
    pause
    player_name "{b}Рокси{/b} так горяча!"
    return


label bedroom_sleeping_jerk_off_debbie:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "... {b}[deb_name]{/b} так прекрасна."
    player_name "Не могу перестать думать об этом."
    player_name "... думать о ней."
    player_name "Mмм, Боже, я так сильно её хочу!"
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show debbied 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
    pause
    show debbied 2
    deb "Ну привет..."
    show debbied 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    show debbied 2
    deb "Ух ты... Это мне?"
    deb "... Какой же он большой!"
    show debbied 1
    pause
    show debbied 2
    deb "... и толстый."
    show debbied 3 with dissolve
    deb "Mмм, прошу дай мне его..."
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    deb "Дай мне его всего, {b}[firstname]{/b}!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1)
    show debbied 4_5
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show player 496f
    player_name "OХ!"
    show player 496g with flash
    player_name "ХХХХХХГГГГГГГ, ХХХХХуууууУУУГГГГГГ!!"
    show player 496h
    hide jerkbubble
    hide debbied
    player_name "Хаааа... Хаааа..."
    player_name "О боже, как же хорошо..."
    return

label bedroom_sleeping_jerk_off_mia:
    $ M_player.set("sex speed", .4)
    scene expression game.timer.image("backgrounds/location_home_bedroom_jerk{}.jpg")
    show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
    pause
    show player 496b
    player_name "{b}Мия{/b} такая милай!"
    player_name "Как же я хочу снова её увидеть..."
    pause
    player_name "... Её прекрасное тело."
    player_name "Mмм..."
    show player 496c
    show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
    pause
    show miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
    pause
    show miad 2
    mia "Эй, {b}[firstname]{/b}!"
    show miad 1
    pause
    show miad 2
    mia "Воу, никогда ничего такого не видела!"
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    mia "Они все такие большие?!"
    show miad 1
    pause
    show miad 2
    mia "Я надеюсь, что ты станешь моим, {b}[firstname]{/b}."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "Ты думаешь это влезет?"
    mia "... В мою..."
    show miad 1
    $ M_player.set("sex speed", M_player.get("sex speed") / 2)
    show player 496c_496d_496e_496d_496c
    pause
    show miad 2
    mia "...В мою киску?"
    show player 496f
    player_name "OХ!"
    show player 496g with flash
    player_name "ХХХХХНННГГГГ, ХХХХуууууууХХХХ!!"
    show player 496h
    hide jerkbubble
    hide miad
    player_name "Хааах... Хааах..."
    player_name "Ооо боже, как же хорошо..."
    return

label bedroom_sleeping_debbie_movie_night:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Я вроде бы слышал, что {b}[deb_name]{/b} делает что-то внизу."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_sleepover:
    scene expression game.timer.image("bedroom{}")
    show player 101b with dissolve
    player_name "Может в следующий раз я буду спать  вместе с {b}[deb_name]{/b}..."
    player_name "Она ведь сказала, что я могу прийти ночью, если захочу..."
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_pre:
    scene location_home_bedroom_cutscene01 with fade
    pause
    "{b}*Тук*{/b}"
    scene bedroom_cs03 with dissolve
    "{b}*Тук Тук*{/b}"
    player_name "..."
    scene bedroom_cs04 with dissolve
    player_name "Что это за звук?"
    scene bedroom_night with fade
    show player 101bf
    player_name "( Он явно исходит снаружи. )"
    player_name "( ... Может со двора {b}Эрика{/b}? )"
    show player 100bf
    return

label bedroom_sleeping_erik_thief_use_telescope:
    show player 101bf
    player_name "( Я, наверное, должен посмотреть. )"
    show player 100f
    player_name "Хмм..."
    show player 101bf
    player_name "( Быстренько гляну в телескоп. )"
    hide player

    scene windowbackyardnight02a
    player_name "!?!"
    player_name "Что за..."
    scene windowbackyardnight02b
    player_name "( Кто-то лазает по двору {b}Эрика{/b}?! )"
    player_name "( Наверное, это тот {b}Взломшик{/b}, о котором говорили в новостях! )"
    scene windowbackyardnight02c
    player_name "..."
    player_name "( Он хочет пробраться в дом {b}Эрика{/b}?! )"

    scene bedroom_night with fade
    show player 101bf with dissolve
    player_name "( Это плохо! )"
    player_name "( А что, если {b}Эрик{/b} и {b}Миссис Джонсон{/b} в опасности? )"
    player_name "( Нужно выйти и посмотреть что он делает во дворе {b}Эрика{/b}. )"
    hide player with dissolve
    return

label bedroom_sleeping_erik_thief_sleep:
    show player 101f
    player_name "( Это, скорее всего, просто какое-то животное. )"
    player_name "( Мне нужно просто заснуть... )"
    hide player
    return

label bedroom_sleeping_erik_bullying_3_started:
    scene expression game.timer.image("bedroom{}")
    show player 12 with dissolve
    player_name "( Боже... Что за день. )"
    show player 17
    player_name "( Я думаю, что тренировки в зале начали приносить свои плоды! )"
    pause
    show player 12
    player_name "( Но {b}Декстер{/b} ни за что не уступит. )"
    player_name "(... Так что я должен выложиться на полную! )"
    show player 8 with dissolve
    pause
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 101 with dissolve
    player_name "( Нужно поспать. )"
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_eve_karaoke:
    scene expression game.timer.image("bedroom{}")
    show player 14 with dissolve
    player_name "Я должен встретиться с {b}Ив{/b} у {b}Эрика{/b} дома сегодня ночью!"
    show player 30
    player_name "Сон может и подождать."
    hide player with dissolve
    return

label bedroom_sleeping_dewitt_school_sneak_mission:
    scene expression game.timer.image("bedroom{}")
    show player 10 with dissolve
    player_name "Сегодня я собирался пробраться в школу вместе с {b}Эриком{/b}."
    player_name "Поэтому по что не могу лечь спать."
    hide player with dissolve
    return

label bedroom_sleeping_mia_midnight_call:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Хрр..."
    "{b}Бззт{/b}!"
    player_name "..."
    "{b}Бззззззззт{/b}!"
    scene bedroom_cs04 with dissolve
    player_name "Ха?"
    player_name "Это мой телефон?"
    scene black with fade
    pause
    scene bedroom_night
    show player 7 with dissolve
    pause
    show player 101
    player_name "Кто-то мне пишет?"
    player_name "Нужно посмотреть, кто именно..."
    hide player with dissolve
    return

label bedroom_sleeping_debbie_solo_dream:
    scene dream_debbie_04 with fade:
        ypos -707
        linear 4.0 ypos 0
    deb "Mмм..."
    deb "Ох, это просто прекрасно, милый."
    player_name "..."
    player_name "О, {b}[deb_name]{/b}..."
    deb "Я хочу тебя {b}[firstname]{/b}!"
    deb "Я так хочу ощутить тебя внутри!"
    player_name "{b}*Глоть*{/b}"
    player_name "Правда?"
    deb "Ты даже не представляешь, насколько! Дай мне уже этот большой твердый член, {b}[firstname]{/b}!"
    deb "Прошу тебя, он нужен мне!"
    player_name "..."
    deb "Давай же! Быстрее! Я не могу больше ждать!"
    scene dream_debbie_05 with dissolve:
        ypos 0
    pause
    player_name "Хнннгггг!!" with flash
    pause
    scene dream_debbie_05 with flash:
        ypos 0
        linear 4.0 ypos -475
    player_name "... Oooooх..."
    pause

    scene location_home_bedroom_cutscene06 with fade
    pause
    scene location_home_bedroom_cutscene07
    player_name "..."
    scene location_home_bedroom_cutscene08
    player_name "О боже..."
    pause
    scene location_home_bedroom_cutscene09
    pause
    player_name "Теперь стирать придется..."
    player_name ".. Но, черт, это было впечатляюще..."
    player_name "И ощущалось так реально!"
    player_name "Aрх, это уже через чур!"
    player_name "Я не могу перестать думать о ней!"
    player_name "Я так хочу прижать к себе и поцеловать..."
    player_name "Может я должен {b}поговорить с {b}[deb_name]{/b} о поцелуях{/b}?"
    player_name "Ей вроде было неплохо, когда мы поцеловались в торговом центре..."
    player_name "Хмм, это конечно рисковано, но попробовать стоит!"
    player_name "Я сойду с ума, если не сделаю что-нибудь..."
    player_name "... Но сейчас нужно почистить это и ещё немного поспать."
    return

label bedroom_sleeping_debbie_night_visit:
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Зззз..."
    scene location_home_bedroom_cutscene02 with dissolve
    deb "( ... )"
    deb "( Я не могу заснуть. )"
    deb "( С того момента, когда я увидела, как он мастурбирует... )"
    deb "( Я не могу перестать думать о его- )"
    deb "( Я просто... )"
    deb "( ... )"
    define fadehold = Fade(0.5, 1.0, 0.5)

    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Не могу поверить, что думаю о чем-то подобном... )"
    deb "( Это ведь нормально для него, иметь такие сны. Он ведь молодой парень. )"
    deb "( ... А я уже достаточно взрослая, я должна быть адекватна! )"
    show debbies 2
    deb "( Он не хочет меня на самом деле! Это просто бред! )"
    deb "( В таком возрасте я уже должна быть просто его {b}мамой{/b}! )"
    deb "( ... Но это так соблазнительно. )"
    show debbies 3
    deb "( То, как он смотрит на меня этими голодными глазами... )"
    show debbies 4
    deb "( ... Ммм, я должна его увидеть... )"
    show debbies 5
    deb "( Одним глазком. )"
    show debbies 6
    deb "( ... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( Он такой большой... )"
    show debbies 7_8
    deb "( ... Но становится ещё больше. )"
    deb "( Mмм... )"
    show debbies 9
    pause
    show debbies 10
    deb "( Я должна его увидеть! )"
    deb "( Ох, какой же он толстый... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "{b}*Глоть*{/b}!"
    deb "( Это невероятно! )"
    deb "( {b}*Эх*{/b} И что мне делать? )"
    deb "( Я не могу выбросить этот член из головы! )"
    deb "( ... )"
    deb "( Я уже так давно не чувствовала мужского тепла... )"
    deb "( ... И я так по этому скучаю. )"
    deb "( Ведь, если я потрогаю, ничего ужасного не произойдет... Совсем чуть-чуть. Верно? )"
    deb "( Конечно, ему же самому некомфортно. Только гляньте, какой он твердый! )"
    show debbies 13
    pause
    show debbies 14
    pause
    deb "( ... Такой твердый... )"
    deb "( ... И толстый. )"
    show debbies 13
    deb "..."
    show debbies 13_14
    pause
    deb "( О боже, что же я делаю?! )"
    deb "..."
    deb "( Я дрочу его член! )"
    deb "( Его... Большой, сочный- )"
    deb "( Он будто подготовил его к моему приходу. )"
    pause
    deb "( Он же сказал, что хочет меня... Хочет так сильно, что мастурбировал, думая обо мне! )"
    deb "( Mмм... )"
    deb "( Он хочет трахнуть меня этим- )"
    show debbies 12
    deb "( ... )"
    show debbies 20
    deb "( Да что со мной не так!? ) "
    show debbies 21
    deb "( Боже мой! )"
    deb "( Я должна уйти отсюда! )"
    deb "( ... Уходи же, {b}[deb_name]{/b}! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Хмм?"
    show debbies 23
    player_name "Что-?"
    player_name "( Это было? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( Хмм, да пофиг. )"
    return

label bedroom_sleeping_debbie_night_visit_two:
    label mom_night_suck:
        scene location_home_bedroom_cutscene01 with dissolve
    player_name "Zzz..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Что я опять тут делаю?! )"
    deb "( Я не могу перестать думать о его члене! )"
    deb "( Постоянно представляю его внутри себя! )"
    show debbies 2
    deb "( ... )"
    deb "( ... Может Diane права; Может я должна просто расслабиться и будь, что будет. )"
    deb "( Этот его голодный взгляд... )"
    deb "( Mмм, да я намокаю просто думая об этом... )"
    show debbies 3
    deb "( Я должна снова его увидеть! )"
    show debbies 4
    deb "( ... )"
    show debbies 5
    deb "( Oх, это так неправильно... Что же ты делаешь, {b}[deb_name]{/b}? )"
    show debbies 6
    deb "( Он даже больше, чем мне казалось... )"
    show debbies 7_8
    pause 4
    show debbies 6
    deb "( Ммм, и он опять увеличивается... )"
    show debbies 7_8
    deb "( ... Такой {b}твердый{/b}. )"
    deb "( ... )"
    deb "( ... Может я могу хотя бы немного... )"
    show debbies 9
    pause
    show debbies 10
    deb "( ... То есть, ему же, наверное, некофортно. )"
    deb "( А я просто помогаю ему расслабиться... Только и всего. )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Oх, господь помоги мне! )"
    deb "( Mмм... )"
    show debbies 13
    deb "( Я не могу перестать его трогать! )"
    deb "( Это так приятно... )"
    show debbies 13_14
    deb "( Он такой толстый... )"
    deb "( ... и сочный. )"
    deb "( ... )"
    deb "( Я так давно... )"
    deb "( хотела... )"
    deb "( Хотела его попробовать! )"
    show debbies 15
    deb "( Я {b}ДОЛЖНА{/b} его попробовать на вкус! )"
    deb "( Всего одна секунда! Ему ведь не будет больно? )"
    show debbies 16_17
    deb "( Да!! )"
    deb "( О боже, я так по этому скучала! )"
    deb "( Я так возбуждена! )"
    show debbies 18
    player_name "{b}*Стон*{/b}"
    show debbies 19
    deb "( !!! )" with hpunch
    deb "( О черт! Он просыпается... )"
    deb "( ... )"
    show debbies 20
    deb "( Что же я делаю?! )"
    deb "( Он не должен меня увидеть! )"
    show debbies 21
    deb "( Нужно срочно уходить! )"
    show debbies 22 at Position(xpos = 544, ypos = 768)
    player_name "Хмм?"
    show debbies 23
    player_name "Что-"
    player_name "( Это было? )"
    show debbies 24 at Position(xpos = 512, ypos = 768)
    player_name "( ... )"
    player_name "( Да пофиг... )"
    $ renpy.end_replay()
    return

label bedroom_sleeping_debbie_midnight_noises:
    scene bedroom_cs01 with fade
    "Ха ха ха..."
    "{b}*Всплеск*{/b}"
    scene bedroom_cs03 with dissolve
    player_name "..."
    scene bedroom_cs04
    player_name "Да что это за шум?"
    scene bedroom_cs03
    player_name "..."
    player_name "......"
    scene bedroom_cs01 with dissolve
    pause
    "{b}*Всплеск*{/b}"
    scene bedroom_cs04 with dissolve
    player_name "Что происходит?"

    scene bedroom_night
    show player 101b
    with dissolve
    player_name "Может стоит проверить?"
    player_name "Кто бы там ни был, он вроде пока не собирается останавливаться."
    show player 8 with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three:
    $ M_mom.set("sex speed", .175 / .75)
    scene location_home_bedroom_cutscene01 with dissolve
    player_name "Ззз..."
    scene location_home_bedroom_cutscene02 with dissolve
    pause
    scene location_home_bedroom_sex01
    show debbies 1
    with dissolve
    deb "( Ох... )"
    deb "( Я снова тут... )"
    show debbies 3
    deb "( Что я делаю! )"
    show debbies 4
    deb "( ДА ЧТО Я ДЕЛАЮ!!! )"
    show debbies 5
    deb "( Mмм! )"
    deb "( Вот он! )"
    show debbies 6
    deb "( Ох, я так его хочу... )"
    show debbies 7_8
    deb "( Стань твердым ради меня, милый... )"
    deb "( Пожалуйста... )"
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    deb "..."
    deb "( Оу, мне так жарко... Он мне просто необходим!!! )"
    show debbies 15
    deb "( Ммм. )"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .75)
    show debbies 16_17
    deb "( Oх! Как же хорошо! )"
    deb "( Я так скучала по этому вкусу! )"
    player_name "( Ммм. )"
    deb "{b}*Лизь*{/b}"
    show debbies 19
    player_name "Хмм?"
    show debbies 20b
    player_name "Что-"
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    show debbies 20d
    deb "Все хорошо, {b}[firstname]{/b}, это я."
    show debbies 20c
    player_name "... Ладно."
    player_name "Но что про-"
    show debbies 20d
    deb "Шшш..."
    show debbies 20c
    player_name "{b}[deb_name]{/b}? Что ты де-"
    show debbies 20e with dissolve
    deb "Тихо, милый, просто расслабься..."
    player_name "..."


    deb "Ох, я так его хочу, {b}[firstname]{/b}!"
    deb "Мне нужен этот большой член!!!"
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "{b}*Глоть*{/b}"
    deb "Я пыталась..."
    deb "Пыталась устоять."
    deb "... Но я не могу!"
    show debbies 20g with dissolve
    deb "Прошу, не думай обо мне плохо..."
    pause
    show debbies 20h with hpunch

    player_name "... OоОх!!"
    deb "Хаааах!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.75)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "О господи!!"
    pause
    deb "Ох, это даже лучше, чем я себе представляла!"
    player_name "Ох, {b}[deb_name]{/b} это так хорошо!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 2)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Хаа! {b}[firstname]{/b}! Ох, {b}[firstname]{/b}!"
    deb "Я сейчас кончу!"
    show debbies 20h with flash
    deb "AAХХХ!!"

    player_name "... Тебя просто трясе! Ты в порядке, {b}[deb_name]{/b}?!"
    deb "Хаах... Хааах..."
    deb "... Не переживай, милый."
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "Продолжай! Трахни меня хорошенько!"
    player_name "..."
    deb "Дай мне его!!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.5)
    show debbies 20h_20i_20j_20k_20l_20m_20n_20o
    deb "ООО ДА!!!"
    deb "Вот оно!!!"
    deb "Дай мне этот толстый член!"
    return

label bedroom_sleeping_debbie_night_visit_three_loop:
    menu:
        "Продолжать." if keep_going < 2:
            $ keep_going += 1
            if M_mom.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")

        "Сменить позу." if keep_going < 2:
            $ keep_going += 1
            if not M_mom.get("change angle"):
                $ M_mom.set("sex speed", .15)
                $ M_mom.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                with fade
            else:

                $ M_mom.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_mom.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                with fade
            pause
            jump expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_loop")
        "Кончить.":

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_pre")


            if M_player.is_set("pet cat"):
                scene location_home_bedroom_sleeping4 with fade
            else:
                scene location_home_bedroom_sleeping2 with fade

            if store._in_replay == None:
                show unlock11 at truecenter with dissolve
                $ renpy.pause()
                hide unlock11

            call expression game.dialog_select("bedroom_sleeping_debbie_night_visit_three_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["10_unlocked"] = True
    $ M_mom.trigger(T_mom_midnight_fun)
    $ Sleep()
    $ game.main()

label bedroom_sleeping_debbie_night_visit_three_cum_pre:
    player_name "Ох, {b}[deb_name]{/b}... Я сейчас..."
    player_name "... Я сейчас!!"
    deb "Не останавливайся! Не-"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "ХХННГГГГ!!!!!"

    deb "AAAAAAAAХХХ!!!"
    pause
    show debbies 20h

    player_name "{b}*Задыхается*{/b}"

    deb "Ммм..."
    show debbies 20r with dissolve
    deb "..."
    show debbies 20s with dissolve
    deb "O боже..."
    show debbies 20t
    player_name "Это было великолепно!"
    show debbies 20s
    deb "Хехе, это и правда было..."
    deb "..."
    deb "Прости меня, любимый!"
    deb "Я не должна была..."
    show debbies 20t
    player_name "Что?! Не говори так!"
    deb "..."
    player_name "Я тоже этого хотел!"
    show debbies 20s
    deb "... Правда?"
    show debbies 20t
    player_name "Ты даже не представляешь насколько! Я практически ни о чем другом думать не мог!"
    show debbies 20s
    deb "... Серьёзно?"
    show debbies 20t
    player_name "Да!"
    player_name "Я люблю тебя, {b}[deb_name]{/b}!"
    show debbies 20s
    deb "Я...  Я тоже тебя люблю, {b}[firstname]{/b}!"
    deb "..."
    deb "Никто ещё никогда не доводил меня до такого оргазма!"
    show debbies 20t
    player_name "Никогда?"
    show debbies 20s
    deb "Никогда. Это был самый отпадный оргазм!"
    show debbies 20t
    player_name "Прости, что не продержался чуть дольше..."
    show debbies 20s
    deb "Нет, всё было прекрасно, милый! Особенно для нашего первого раза!"
    show debbies 20t
    player_name "... Первый раз?"
    deb "..."
    player_name "Мы можем сделать это снова, {b}[deb_name]{/b}?"
    show debbies 20s
    deb "Ох, милый, ты правда хочешь этого?"
    show debbies 20t
    player_name "Конечно!!!"
    player_name "{b}[deb_name]{/b}, я ничего так сильно не хотел!"
    show debbies 20s
    deb "О боже..."
    deb "Мне неприятно это признавать, но я хочу того же!"
    deb "..."
    deb "Ладно, милый.."
    deb "... Но мы можем так себя вести, только когда рядом никого нет!"
    deb "И ты не скажешь об этом {b}НИКОМУ{/b}! ОСОБЕННО {b}[jen_name]{/b}!"
    deb "Ты понял?!"
    show debbies 20t
    player_name "Да."
    show debbies 20s
    deb "{b}[firstname]{/b}, Я серьезно! Вообще никому не говорить!"
    show debbies 20t
    player_name "Я не скажу, {b}[deb_name]{/b}. Обещаю."
    show debbies 20s
    deb "Хороший мальчик."
    deb "{b}*Зевает*{/b}"
    deb "Ох, я так вымоталась."
    show debbies 20t
    player_name "Да, я тоже."
    show debbies 20s
    deb "Ммм, да я прямо тут и усну."
    show debbies 20t
    player_name "Я не против, {b}[deb_name]{/b}."
    show debbies 20s
    deb "Я думаю, что проблем не будет. Нужно просто уйти до того, как{b}[jen_name]{/b} проснется."



    scene location_home_bedroom_cutscene_sleep
    with fade
    show text "{b}[deb_name]{/b} и я наконец-то переспали." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Это было прекрасно! Все наши переживайния просто испарились!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Всё стало хорошо, как только она заснула в моих объятьях." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... А когда мы проснулись, каждый из нас чувствовал себе так, как никогда раньше." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label bedroom_sleeping_debbie_night_visit_three_cum_after:

    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "{b}[deb_name]{/b}?"
    show debbies 20u
    player_name "..."
    show debbies 20v
    player_name "{b}[deb_name]{/b}, просыпайся."
    show debbies 20u
    deb "Хмм?"
    show debbies 20x
    deb "{b}*Зевает*{/b} Уже утро?"
    show debbies 20w
    player_name "Боюсь, что да."
    show debbies 20x
    deb "Ох, я спала как убитая..."
    show debbies 20w
    player_name "Хех, да, я тоже."
    show debbies 20x
    deb "Ммм, ладно. Нужно уйти раньше, чем {b}[jen_name]{/b} проснется."
    show debbies 20w
    player_name "Уверена, что не хочешь ещё немного тут побыть?"
    show debbies 20x
    deb "Хехе, не соблазняй меня, милый. Твоему члену очень трудно сказать нет."
    show debbies 20w
    player_name "Как же приятно это слышать!"
    show debbies 20x
    deb "Просто найди меня чуть позже, окей?"
    scene black with fade
    return

label bedroom_sleeping_debbie_smith_dream:
    scene dream_debbie 1 at Position(ypos=1475) with fade
    deb "Доброе утро, милый."
    deb "Это я, {b}[deb_name]{/b}."
    player_name "{b}[deb_name]{/b}?"
    player_name "Где мы?"
    deb "Все хорошо. Всё будет в порядке..."
    deb "Дай мне позаботиться о тебе."
    scene dream_debbie 1_2:
        linear 5.0 ypos -707
    player_name "{b}[deb_name]{/b}..."
    player_name "Что ты делаешь..."
    deb "- Все окей... Просто хочу сделать тебе приятно..."
    player_name "{b}[deb_name]{/b}... Это просто охрененно!"
    scene dream_debbie 3
    player_name "( !!! )" with hpunch
    smi "{b}[firstname]{/b}!!!"
    scene dream_debbie 3:
        ypos -707
        linear 1.0 ypos 0
    smi "Что ты тут делаешь???"
    smi "Ты что... СПИШЬ?!"

    smi "А ну БЫСТРО в клас или твоей заднице придется задержаться здесь {b}после занятий{/b}!"
    scene black with fade
    pause .2
    scene expression game.timer.image("bedroom{}")
    show player 264
    with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 265 with dissolve
    player_name "( !!! )"
    show player 266
    player_name "( Это был очень странный сон! )"
    player_name "( Мы с {b}[deb_name]{/b} делали всякие вещи, и она было голая! )"
    player_name "( А потом {b}Директриса Смит{/b}... )"
    show player 267 with hpunch
    player_name "( !!! )"
    show player 268
    player_name "( Это вообще нормально?! )"
    player_name "( Мне раньше не снились такие сны про {b}[deb_name]{/b}... )"
    hide player with dissolve
    return

label bedroom_debbie_sleepover_pre:
    $ M_mom.set("sex speed", .175)
    scene location_home_bedroom_sex01 with fade
    show debbies 1
    player_name "( ... )"
    deb "Милый?"
    deb "Оуу, ты что, заснул, пока меня спал?"
    player_name "( ... )"
    show debbies 3
    pause
    show debbies 4
    pause
    show debbies 5
    pause
    show debbies 6
    deb "... Просыпайся, милый."
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .75)
    show debbies 7_8
    deb "Ммм..."
    show debbies 6
    pause
    show debbies 9
    pause
    show debbies 10
    deb "( ... )"
    show debbies 11
    deb "( !!! )"
    show debbies 12
    pause
    show debbies 20b
    deb "{b}[firstname]{/b}?"
    player_name "... Хмм?"
    show debbies 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... {b}[deb_name]{/b}?"
    player_name "Черт, я заснул?"
    show debbies 20d
    deb "Хехе, всё в порядке, милый."
    show debbies 20c
    player_name "Ты до сих пор хочешь- ?"
    show debbies 20e with dissolve
    deb "Шшш, мы же не хотим разбудить {b}[jen_name]{/b}?!"
    player_name "Ох! ... Точно, прости."
    show debbies 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    deb "Хехе..."
    deb "Все в порядке, ты просто возбужден. Я тоже уже не могу терпеть!"
    deb "Я уже не могу ждать, пока {b}[jen_name]{/b} ляжет спать."
    show debbies 20g with dissolve
    player_name "Вау, {b}[deb_name]{/b}, а ты очень влажная!"
    deb "Я же сказал, что уже не могу терпеть."
    show debbies 20h with dissolve
    deb "Ммм..."
    deb "А теперь, хватит трать время зря... Иди ко мне, милый!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / 3)
    show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
    return

label bedroom_debbie_sleepover_random_33:
    deb "Aхх!!!"
    deb "Ох {b}[firstname]{/b}, это так глубоко!"
    deb "Тебе ведь нравится, когда я сжимаю его своим влагалищем?"
    player_name "О боже, да!"
    deb "{b}[firstname]{/b}!"
    return

label bedroom_debbie_sleepover_random_66:
    deb "О да!!!"
    deb "Вот так, милый! Еби мою киску!"
    deb "Ммм, тебе это нравится?"
    player_name "О да, {b}[deb_name]{/b}!"
    deb "Ещё быстрее!"
    return

label bedroom_debbie_sleepover_random_100:
    deb "Боже, как же мне хорошо!"
    deb "Кто мой пошлый мальчишка?"
    player_name "Ммм, Я..."
    deb "Верно, малыш! Еби меня сильнее!"
    player_name "Ухх!! А тебе очень нравится мой твердый член, {b}[deb_name]{/b}?"
    deb "Aaaхх!! Да! Дааа! ДААА!!"
    deb "Вставь его ещё глубже!"
    return

label bedroom_debbie_sleepover:
    call expression game.dialog_select("bedroom_debbie_sleepover_pre")
    if randomizer() < 33:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_33")

    elif randomizer() < 66:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_66")

    elif randomizer() < 100:
        call expression game.dialog_select("bedroom_debbie_sleepover_random_100")

    $ M_mom.set("sex speed", M_mom.get("sex speed") / 1.5)
    pause
    $ M_mom.set("change angle", False)

    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_loop:
    menu:
        "Продолжать.":
            if M_mom.get("change angle"):
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
            else:

                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
        "Сменить позу.":

            if not M_mom.get("change angle"):
                $ M_mom.set("sex speed", .15)
                $ M_mom.set("change angle", True)
                hide debbies
                scene bedroom_sex_05
                show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                with fade
            else:

                $ M_mom.set("sex speed", ((.175 / .75) / 3) / 1.5)
                $ M_mom.set("change angle", False)
                hide debbies
                scene location_home_bedroom_sex01
                show expression AnimatedImage("debbies", ["20h","20i","20j","20k","20l","20m","20n","20o"], M_mom) as debbies
                with fade
        "Кончить.":

            jump expression game.dialog_select("bedroom_debbie_sleepover_cum")
    pause
    jump expression game.dialog_select("bedroom_debbie_sleepover_loop")

label bedroom_debbie_sleepover_cum:
    call expression game.dialog_select("bedroom_debbie_sleepover_cum_dialogue")

    if M_player.is_set("pet cat"):
        scene location_home_bedroom_sleeping4 with fade
    else:
        scene location_home_bedroom_sleeping2 with fade

    show unlock11 at truecenter with dissolve
    pause
    $ Sleep()
    hide unlock11 with dissolve
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and not M_mom.is_state(S_mom_note):
        call expression game.dialog_select("bedroom_debbie_sleepover_after_random_70")
    else:

        call expression game.dialog_select("bedroom_debbie_sleepover_after_not_random")
        if not M_mom.is_set("basement sex"):
            call expression game.dialog_select("bedroom_debbie_sleepover_after_not_basement_sex")
            $ M_mom.trigger(T_mom_delay)
        hide player with dissolve
    $ game.main()

label bedroom_debbie_sleepover_cum_dialogue:
    player_name "... Ох!"
    player_name "{b}[deb_name]{/b}, Я сейчас..."
    deb "Давай, малыш! Кончи в меня!"
    $ M_mom.set("sex speed", M_mom.get("sex speed") / .075)
    scene location_home_bedroom_sex01
    show debbies 20p_20q
    with flash
    player_name "Ууухх!!!"
    deb "Хнг!!"
    deb "AAAAХХХХ!!!"
    player_name "Шшш! Ты разбудишь {b}[jen_name]{/b}!"
    player_name "..."
    show debbies 20h with dissolve
    deb "Хаа... Хааа..."
    show debbies 20r with dissolve
    pause
    show debbies 20s with dissolve
    deb "Ох {b}[firstname]{/b}... Это было..."
    show debbies 20t
    player_name "Крышесносно?"
    show debbies 20s
    deb "Фух... Да!"
    deb "Ммм, я ног не чувствую."
    pause
    deb "... Я люблю тебя, {b}[firstname].{/b}"
    show debbies 20t
    player_name "Я тоже тебя люблю, {b}[deb_name]{/b}. Ты лучшая!"
    show debbies 20s
    deb "Ха, спасибо, милый."
    return

label bedroom_debbie_sleepover_after_random_70:
    scene location_home_bedroom_sex04
    show debbies 20u
    pause
    show debbies 20v
    player_name "Просыпайся, {b}[deb_name]{/b}."
    show debbies 20u
    deb "Ммм..."
    show debbies 20w
    player_name "Солнце уже высоко."
    show debbies 20x
    deb "Доброе утро, милый."
    show debbies 20w
    player_name "Ты хорошо спала?"
    show debbies 20x
    deb "... Шутишь? После такой ебли я спала просто прекрасно!"
    show debbies 20w
    player_name "Ха, да, я тоже..."
    deb "..."
    show debbies 20x
    deb "Я, наверное, должна уйти до того, как {b}[jen_name]{/b} проснется."
    show debbies 20w
    player_name "Да..."
    show debbies 20x
    deb "Спасибо за прекрасную ночь, {b}[firstname]{/b}! Я люблю тебя!"
    show debbies 20w
    player_name "Я тоже тебя люблю, {b}[deb_name]{/b}!"
    scene black with fade
    return

label bedroom_debbie_sleepover_after_not_random:
    scene location_home_bedroom_day_blur
    show player 7
    pause
    show player 8
    pause
    show player 1
    player_name "..."
    show player 2
    player_name "Хмм, {b}[deb_name]{/b} видно ушла раньше, чем я проснулся..."
    player_name "Фух, сто за ночка! Я спал как младенец..."
    return

label bedroom_debbie_sleepover_after_not_basement_sex:
    show player 10
    player_name "Хмм, что это за записка на мониторе?"
    player_name "... Это {b}[deb_name]{/b} оставила?"
    return

label sleeping_locked:
    scene expression player.location.background_blur
    show player 35 at left
    if not erik.over(erik_intro):
        player_name "( Не могу сейчас спать. Мне нужно идти в школу. )"
    else:
        player_name "(Я ещё должен кое-что сегодня сделать...)"
    $ game.main()

label tired_bedroom_dialogue:
    scene expression game.timer.image("bedroom{}")
    show player 55 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 56
    player_name "( Я слишком устал для этого... )"
    hide player 56
    $ game.main()

label M6_note:
    call expression game.dialog_select("M6_note_dialogue")
    $ M_mom.trigger(T_mom_read_note)
    $ game.main()

label M6_note_dialogue:
    scene expression game.timer.image("bedroom{}")
    show debbienote at Position (ypos=650) with dissolve
    pause
    hide debbienote with dissolve
    show player 11 with dissolve
    player_name "( {b}[deb_name]{/b} нужна помощь в прачечной? )"
    player_name "( Нужно пойти и посмотреть, что к чему. )"
    hide player with dissolve
    return

label pet_cat:
    scene expression game.timer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Эй, [cat]!"
    show cat 12
    if randomizer() < 33:
        cat "Мяу"
    elif randomizer() < 66:
        cat "Пррр"
    else:
        cat "Врау"
    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Кто тут хороший котик?!"
    elif randomizer() < 30:
        player_name "Хочешь проспать весь день?"
    elif randomizer() < 45:
        player_name "Чем ты сегодня занималься, а?"
    elif randomizer() < 60:
        player_name "Ты милый маленький шерстяной шарик."
    elif randomizer() < 75:
        player_name "Aуу, немного ласк для котенка!"
    elif randomizer() < 85:
        player_name "Хей, только посмотри на эти коготки!"
    elif randomizer() < 93:
        player_name "Нужно купить тебе игрушку, да?"
    else:
        player_name "Я так люблю гладить свою киску..."
    show cat 16
    pause
    hide cat with dissolve
    $ game.main()

label cookies:
    scene expression game.timer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( Коробка моих любимых печенек! )"
    player_name "( Нужно положить их в портфель, на случай если я проголодаюсь. )"
    hide expression "objects/closeup_cookies.png" with dissolve
    show expression "boxes/popup_cookies.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_cookies.png" with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
