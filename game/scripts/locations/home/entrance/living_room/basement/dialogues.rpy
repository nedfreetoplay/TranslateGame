label basement_mom_wash_clothes:
    scene home_basement_sideview
    show player 324 at Position(xpos=860)
    show debbie 136 at Position(xpos=550,ypos=805)
    deb "... Отлично, ты принес эту грязную одежду."
    show debbie 137
    deb "{b}*хихикая*{/b}"
    show player 325
    show debbie 135
    player_name "Что смешного?"
    show player 326
    show debbie 136
    deb "Твоя одежда! Она в полном беспорядке!"
    show player 324
    show debbie 137
    deb "Ты действительно много работал, да?"
    show player 325
    show debbie 135
    player_name "Да, я, наверное, должен был переодеться во что-то еще, прежде чем начать..."
    show player 324
    show debbie 136
    deb "Все в порядке, милый! Мы приведем тебя в порядок."
    deb "Просто отдай свою одежду и я добавлю ее в стирку."
    show player 325
    show debbie 135
    player_name "Хорошо, {b}[deb_name]{/b}. Так и сделаю."
    show player 324
    show debbie 136
    deb "Нет проблем. Я как раз собиралась загрузить машинку."
    show debbie 135
    show player 327 at Position(xoffset=-27) with fastdissolve
    pause
    show expression Cutscene("home_basement_cutscene", "Было немного неловко раздеваться перед {b}[deb_name]{/b}. \nНо она, похоже, не заметила. Она просто поспешно засунула мою одежду в машину. \nЯ не мог не заметить этого взгляда, когда она рассказывала о своей работе.\nИзлишне говорить, что я довольно быстро забыл о своем смущении...") as cutscene with fade
    pause
    hide cutscene
    scene home_basement_sideview
    show player 330 at Position(xpos=860)
    show debbie 142 at Position(xpos=550,ypos=805)
    with fade
    deb "( Он, вероятно, будет носить эти вонючие боксеры весь день. )"
    deb "( Я тоже должна их добавить. В противном случае они могут оказаться на его полу на следующей неделе... )"
    show debbie 136
    deb "Боксеры тоже, {b}[firstname]{/b}."
    show player 332
    deb "Возможно, теперь все будет постирано."
    show debbie 135
    player_name "( !!! )"
    show player 331
    player_name "Правда? Нет, все в порядке. Я просто брошу их в корзину с грязной одеждой наверху..."
    show debbie 136
    show player 330
    deb "Не говори глупостей, ты сейчас здесь. Давай просто бросим их, и ты сможешь принять душ!"
    show debbie 135
    show player 333
    player_name "... Да, но-"
    show debbie 136
    show player 330
    deb "Не нужно стесняться. Ничего такого, чего бы я не видела раньше миллион раз."
    deb "И давай поторопимся и покончим с этим."
    show debbie 138
    show player 334 with fastdissolve
    pause
    show player 335 with fastdissolve
    pause
    show player 336 with fastdissolve
    pause 0.1
    show debbie 139
    show player 337 at Position(xpos=855) with vpunch
    pause
    show debbie 140
    show player 338 at Position(xpos=853)
    deb "Ой блин..."
    deb "..."
    deb "Вау! Это... Ого..."
    deb "Давай я принесу тебе что-нибудь, чтобы прикрыться."
    show debbie 141 with fastdissolve
    pause
    show player 339 at Position(xpos=845)
    show debbie 142
    with fastdissolve
    pause
    show player 341
    player_name "Прости, {b}[deb_name]{/b}."
    show player 340
    show debbie 143
    deb "Хех, нет проблем, милый."
    deb "Такое случается."
    show debbie 140
    deb "Это совершенно естественно."
    show debbie 142
    deb "Хех."
    show debbie 143
    deb "Что-то полотенце для рук маловато?"
    deb "Извините, у меня здесь нет ничего больше этого..."
    deb "Тебе лучше пойти сейчас и принять душ."
    show debbie 142
    show player 341
    player_name "Да, Мэм."
    hide player with dissolve

    show debbie 139
    deb "( Бог мой... )"
    deb "( ... Я понятия не имела, что он такой... Одаренный. )"
    scene black with fade
    return

label basement_mom_close_valve:
    scene home_basement
    show player 34 with dissolve
    player_name "( Водяной кран должен находиться рядом с водонагревателем. )"
    player_name "( Я лучше выключу его, пока наверху не затопило. )"
    hide player with dissolve
    return

label basement_mom_give_laundry:
    scene home_basement_c
    show debbie 125 at right
    show player 277 at left
    with dissolve
    player_name "О, вот ты где!"
    show player 276
    player_name "Я принес твое белье, как ты просила."
    show player 13
    show debbie 121
    with dissolve
    pause
    show debbie 123
    deb "Спасибо, милый."
    deb "Это был лишь предлог, чтобы затащить тебя сюда..."
    show debbie 124
    show player 10
    player_name "Да? Что ты собираешься делать?"
    show player 5
    show debbie 123
    deb "Хехе..."
    show debbie 63 with dissolve
    deb "Я оставила тебе эту записку утром, потому что хотела увидеть тебя перед твоим уходом."
    show debbie 61
    show player 11
    player_name "Хух?"
    show debbie 39
    deb "Я хочу тебя, {b}[firstname]{/b}!"
    show debbie 62
    show player 1
    deb "Я хочу прокатиться на твоем большом члене!"
    show debbie 61
    show player 2
    player_name "ККК-Конечно!"
    show player 13
    show debbie 62
    deb "Раздевайся!"
    show player 11
    show debbie 125
    player_name "( !!! )"
    show player 297
    player_name "Д-Да, Мэм!"
    show player 13
    show debbie 62
    deb "{b}[jen_name]{/b} не найдет нас здесь."
    show player 21
    show debbie 125
    player_name "Ну... хорошо."
    return

label basement_mom_sex:
    $ M_mom.set("sex speed", .175)
    $ player.go_to(L_home_basement)
    $ cum = False
    $ anim_toggle = False
    $ xray = False
    if not M_mom.is_state(S_mom_give_laundry) and randomizer() <= 50:
        $ mom_basement_rand = True
    else:
        $ mom_basement_rand = False
    call expression game.dialog_select("basement_mom_sex_pre")
    jump expression game.dialog_select("basement_mom_sex_loop")

label basement_mom_sex_pre:
    if mom_basement_rand:
        scene home_basement_c
        show debbie 62 at right
        show player 13 at left
        with dissolve
        deb "Sit up on the washer for me."
    scene home_basement_sex_01
    show player 270 zorder 1 at Position(xpos=466,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with fade
    pause
    show player 271 at Position(xpos=655,ypos=768)
    pause
    if mom_basement_rand:
        player_name "Хорошо?"
        show debbie 108
        deb "Прекрасно."
        deb "Твой член просто идеален."
    else:

        show debbie 108
        deb "Мой черед..."
    show debbie 109 at Position(xpos=205)
    pause
    show debbie 110
    pause
    show debbie 111 at Position(xpos=207)
    pause
    show debbie 112 at Position(xpos=196)
    pause
    show debbie 113 at Position(xpos=203)
    pause
    show debbie 114
    pause
    show debbie 115
    if mom_basement_rand:
        deb "Теперь сядь и позволь мне помочь тебе с твоим грязным липким грузом."
    else:

        deb "Нравится то, что видишь?"
        show debbie 114
        player_name "Ты прекрасна, {b}[deb_name]{/b}."
        show debbie 115
        deb "Просто сядь и расслабся, милый."
        deb "Начнем медленно и аккуратно..."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655) with dissolve
    pause
    show debbies 126f at Position(xpos=660) with dissolve
    deb "Ох!"
    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    if mom_basement_rand:
        deb "Мммм..."
        deb "Он едва помещается в меня."
    else:

        deb "Аххх..."
        player_name "( !!! )"
        player_name "Ты вся мокрая..."
    return

label basement_mom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("debbies", ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"], M_mom) as debbies at Position(xpos = 660)
            pause 4
            call expression game.dialog_select("debbie_basement_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = ["126","126b","126c","126d","126e","126f","126g","126h","126i","126j"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 660)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_basement_hscene_dialog")
        $ animcounter += 1
    call screen basement_mom_sex_options

label debbie_basement_hscene_dialog:
    if animcounter == 1:
        if mom_basement_rand:
            deb "О, малыш!{p=1}{nw}"
            deb "Да!{p=1}{nw}"
        else:

            deb "Ахххх!!!{p=1}{nw}"

    elif animcounter == 2:
        deb "Ахх!!!{p=1}{nw}"

    elif animcounter == 3:
        if mom_basement_rand:
            deb "О!{p=1}{nw}"
        else:

            deb "О, милый!!!{p=1}{nw}"
            player_name "Уххх...{p=1}{nw}"
    return

label basement_mom_sex_cum:
    player_name "{b}[deb_name]{/b}!"
    show white
    show debbies 129 at Position(xpos=609) with vpunch
    hide white with dissolve
    if mom_basement_rand:
        deb "О, милый!"
        deb "Я тоже кончаю!"
        show debbies 129 with flash
        deb "АХХ!!!"
    else:

        deb "Ахх!!!"
    jump expression game.dialog_select("basement_mom_sex_after")

label basement_mom_sex_after:
    if M_mom.is_state(S_mom_give_laundry):
        call expression game.dialog_select("basement_mom_sex_after_pre_give_laundry")

    elif mom_basement_rand:
        call expression game.dialog_select("basement_mom_sex_after_pre_random")
    else:

        call expression game.dialog_select("basement_mom_sex_after_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["12_unlocked"] = True
    $ game.timer.tick()
    if M_mom.is_state(S_mom_give_laundry):
        jump expression game.dialog_select("basement_confession_kiss")
    $ game.main()

label basement_confession_kiss:
    call expression game.dialog_select("basement_confession_kiss_pre")
    if randomizer() <= M_mom.get("mom concerned"):
        if M_mom.get("mom concerned") > 0:
            $ M_mom.set("mom concerned", M_mom.get("mom concerned") - 20)

        if M_mom.get("mom concerned") < 0:
            $ M_mom.set("mom concerned", 0)

        call expression game.dialog_select("basement_confession_kiss_concerned_random")
    call expression game.dialog_select("basement_confession_kiss_after")
    $ M_mom.trigger(T_mom_basement_fun)

    $ game.main()

label basement_mom_sex_after_pre_give_laundry:
    show debbies 132 at Position(xpos=650) with fade
    deb "Спасибо, что принес мне белье..."
    show debbies 131
    player_name "В любое время, {b}[deb_name]{/b}."
    show debbies 132
    deb "Дай мне знать, если захочешь сделать это снова."
    show debbies 131
    player_name "Определенно."
    return

label basement_mom_sex_after_pre_random:
    show debbies 130 at Position(xpos=650) with fade
    deb "Это было замечательно, милый!"
    show debbies 131
    player_name "Это точно!"
    player_name "Мне нравится делать это с тобой в подвале!"
    player_name "Мы можем шуметь здесь так громко, как захотим."
    show debbies 132
    deb "Хе-Хе, Да. Это определенно преимущество!"
    return

label basement_mom_sex_after_pre:
    show debbies 132 at Position(xpos=650) with fade
    deb "Это было хорошо, милый."
    deb "Спасибо за приглашение!"
    show debbies 131
    player_name "В любое время!"
    return

label basement_confession_kiss_pre:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show debbie 73 at Position(xpos=650)
    with fade
    deb "Милый..."
    return

label basement_confession_kiss_concerned_random:
    deb "Я хочу, чтобы ты сказал мне, если ты больше не хочешь этого делать, хорошо?"
    show player 228
    show debbie 76
    player_name "Нет, все хорошо, {b}[deb_name]{/b}..."
    player_name "Мне всегда хочется делать это с тобой."
    show player 227
    show debbie 77
    deb "Правда?"
    show player 228
    player_name "Да, это все, о чем я думаю, когда вижу тебя..."
    show player 227
    show debbie 75
    deb "Ты всегда такой милый..."
    return

label basement_confession_kiss_after:
    deb "Поцелуй меня."
    hide player
    show debbie 80 at Position(xpos=500)
    with dissolve
    pause
    show debbie 79 with dissolve
    pause
    show debbie 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show debbie 78 at Position(xpos=650)
    with dissolve
    player_name "Я люблю тебя, {b}[deb_name]{/b}!"
    show player 227
    show debbie 75
    deb "Я люблю тебя тоже, милый..."
    scene home_basement
    hide debbie
    hide player
    with fade
    return

label broken_pipe:
    call expression game.dialog_select("broken_pipe_dialogue")
    $ M_mom.trigger(T_mom_closed_valve)
    $ game.main()

label broken_pipe_dialogue:
    scene home_basement
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed with dissolve
    scene home_basement_c
    show player 2
    with dissolve
    player_name "Хорошо, кран закрыт."
    player_name "Я должен вернуться в {b}ванную{/b} чтобы посмотреть смогу ли я подчинить {b}раковину{/b}."
    hide player
    with dissolve
    return

label laundry_dialogue:
    call expression game.dialog_select("laundry_dialogue_pre")
    menu:
        "Позволь помочь.":
            call expression game.dialog_select("laundry_dialogue_help")
            $ M_mom.trigger(T_mom_cleaned_laundry)
        "Ты занята.":


            call expression game.dialog_select("laundry_dialogue_busy")
    $ M_mom.set("chores", False)
    $ game.main()

label laundry_dialogue_pre:
    scene home_basement_c
    show debbie 123 at right
    show player 1 at left
    with dissolve
    deb "О! Привет, милый!"
    deb "Тебе что-нибудь нужно?"
    show debbie 124
    return

label laundry_dialogue_help:
    show debbie 124
    show player 14
    player_name "Я могу постирать, {b}[deb_name]{/b}. Почему бы тебе не сделать перерыв."
    show debbie 123
    show player 5
    deb "Все нормально. Я справлюсь."
    show debbie 122
    show player 10
    player_name "Ты заслуживаешь отдыха. Ты так много работаешь по дому."
    player_name "Кроме того, мне нравится помогать тебе."
    show debbie 123
    show player 11
    deb "О, {b}[firstname]{/b}. В последнее время ты мне очень помогаешь!"
    show player 1
    deb "Что я сделала, чтобы заслужить такого замечательного жильца?"
    show player 275
    show debbie 62
    deb "Ты знаешь, как все работает?"
    show debbie 125
    show player 276
    player_name "Да, я не в первый раз стираю."
    show debbie 63
    show player 275
    deb "Большое спасибо за это, {b}[firstname]{/b}."
    deb "Я действительно ценю это."
    deb "Твой {b}Отец{/b} гордился бы тобой!"
    show debbie 125
    show player 277
    player_name "Хех, спасибо!"
    show expression Cutscene("help_debbie_basement_cutscene", "Было очень весело помогать {b}[deb_name]{/b} по дому. \nДумаю, ей тоже это нравится. Всегда так хочется завести разговор и узнать больше о своей жизни. \nВ последнее время мы все ближе и ближе, и я не могу не восхищаться ее красотой и очарованием. \nКажется, ей тоже становится более комфортно со мной. Она смотрит на меня, ее невинные прикосновения...") as cutscene with fade
    pause
    hide cutscene with dissolve
    scene home_basement_c with fade
    show debbie 2 at right
    show player 13 at left
    with dissolve
    deb "Хех, еще раз спасибо за это, {b}[firstname]{/b}."
    deb "Мне очень понравились наши беседы."
    show debbie 1
    show player 14
    player_name "Да, мне тоже!"
    show player 13
    show debbie 13
    deb "В последнее время ты мне очень помогаешь..."
    deb "Не мог бы ты подняться наверх и взять {b}лосьон{/b} из моего ящика?"
    deb "Мои ноги немного суховаты."
    show debbie 1
    show player 12
    player_name "Где он находится, наверху?"
    show player 5
    show debbie 13
    deb "Посмотри в {b}ящике в спальне{/b}."
    deb "Он должен быть там."
    show debbie 1
    show player 14
    player_name "Хорошо, Я сейчас вернусь!"
    hide player
    hide debbie
    with dissolve
    show popup_debbiebedroom at truecenter with dissolve
    pause
    hide popup_debbiebedroom with dissolve
    return

label laundry_dialogue_busy:
    show player 14
    player_name "Похоже, что ты занята."
    player_name "Я вернусь позже."
    return

label mom_lotion_fun:
    if M_mom.is_set("lotion fun"):
        if player.location == L_home_basement:
            scene home_basement_c

        elif player.location == L_home_kitchen:
            scene homekitchen_closeup
            if M_mom.is_set("sex available"):
                call expression game.dialog_select("mom_lotion_fun_kitchen_sex_available")
                $ player.remove_item("lotion")
                $ M_mom.set("fetch lotion", False)
                $ M_mom.set("retrieved lotion", False)

                pause
                $ M_mom.set("sex speed", .225)
                $ M_mom.set("sex flip", False)
                $ M_mom.set("robe on", True)
                $ first_pass = True
                jump expression game.dialog_select("mom_finger_loop")

        call expression game.dialog_select("mom_lotion_fun_pre")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue")
        call expression game.dialog_select("mom_lotion_fun_location_dialogue_after")

        if player.location == L_home_basement:
            $ player.go_to(L_home_livingroom)
            scene home_livingroom_b with fade

        elif player.location == L_home_kitchen:
            $ player.go_to(L_home_entrance)
            scene expression L_home_entrance.background with fade

        call expression game.dialog_select("mom_lotion_fun_after")
    else:

        call expression game.dialog_select("mom_lotion_fun_first_pre")
        menu:
            "Помочь ей.":
                call expression game.dialog_select("mom_lotion_fun_first_help_her")
                $ player.go_to(L_home_livingroom)
                $ M_mom.set("lotion fun", True)
            "Уйти.":

                call expression game.dialog_select("mom_lotion_fun_first_leave")

        $ M_mom.trigger(T_mom_lotion_applied)
    hide player
    hide debbie
    with dissolve
    $ player.remove_item("lotion")
    $ M_mom.set("fetch lotion", False)
    $ M_mom.set("retrieved lotion", False)

    $ game.timer.tick()
    $ game.main()

label mom_lotion_fun_kitchen_sex_available:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Вот он, {b}[deb_name]{/b}!"
    show player 484
    show debbie 2
    deb "Спасибо, милый."
    deb "Позволь мне сесть на стол, чтобы тебе не пришлось наклоняться."
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184f zorder 2
    with dissolve
    pause
    show debbie 185
    show debbie_robe 185j
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    pause
    show player_arms 488c_488d with dissolve
    show player 487g
    show debbie 185b
    deb "О, щекотно!"
    show debbie 185g
    deb "Тебе нравится заботиться обо мне, не так ли?"
    show debbie 185f
    show player 487f
    player_name "Всегда!"
    show player 487g
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185b
    deb "Я бы сказала, ты такой хороший мальчик..."
    deb "...Но я знаю, почему тебе нравится это делать."
    show debbie 185f
    show player 487
    player_name "..."
    show debbie 185g
    deb "Тебе просто нравится мое маленькое шоу..."
    show debbie 185f
    show player 487g
    player_name "!!!"
    show debbie 185g
    deb "Твой маленький массаж меня возбуждает."
    show debbie 185b
    show player 487d
    deb "Продолжай массировать и, возможно, ты сможешь помочь мне кое с чем еще..."
    show debbie 185f
    show player 487f
    player_name "Да, мэм!"
    show player 487g
    show debbie_robe 185k
    show player_arms 488e_488f
    with dissolve
    pause
    show debbie 185b
    deb "Это действительно здорово. Я как масло в твоих руках."
    hide player_arms
    show player 13 at Position (xoffset=-118)
    hide debbie_robe
    show debbie 189
    with dissolve
    deb "Кажется, даже моя одежда хочет соскользнуть."
    show debbie 188
    show player 26 at Position (xoffset=-118)
    player_name "И когда ты снял свои трусики?"
    show player 13 at Position (xoffset=-118)
    show debbie 189
    deb "{b}*хихикает*{/b}"
    show debbie 187
    deb "Интересно, заметил ли ты."
    show debbie 189
    deb "Итак, ты хочешь попробовать что-то еще?"
    show debbie 188
    show player 14 at Position (xoffset=-118)
    player_name "Конечно!"
    show player 110f at Position (xoffset=-118)
    show debbie 191
    show debbie_robe 191b zorder 2
    with dissolve
    deb "Тогда будь хорошим мальчиком и используй свои пальцы, чтобы заставить меня кончить..."
    show debbie 190
    show player 26 at Position (xoffset=-119)
    player_name "Да, {b}[deb_name]{/b}."
    show player finger 193b zorder 3
    show debbie 192
    show debbie_robe 194b at right
    with dissolve
    return

label mom_lotion_fun_pre:
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "Понял!"
    show player 484
    show debbie 2
    deb "Отлично! Одну секундочку."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184b zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    deb "Готов!"
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    show debbie 185d
    deb "О! Как холодно."
    show player 487d
    deb "Втирай немного лосьона в руки, прежде чем применять его."
    show player 487c
    show debbie 185
    show player_arms 488c_488d with dissolve
    show debbie 185b
    deb "Так хорошо."
    show debbie 185
    show player 487f
    show player_arms 488b with dissolve
    player_name "Прекрасно!"
    show player 487g
    show player_arms 488c_488d with dissolve
    pause
    show player 487f
    show player_arms 488 with dissolve
    player_name "Где-нибудь еще?"
    show player 487g
    show debbie 185c
    deb "Хмм?"
    show player 487e
    player_name "Ты хочешь, чтобы я положил лосьон куда-нибудь еще?"
    show player 487d
    show debbie 185d
    deb "О..."
    show debbie 185g
    deb "Умм... Если ты не возражаешь, потри немного выше на моей ноге..."
    show debbie 185f
    show player 487e
    player_name "Хо... Хорошо..."
    show player_arms 488b with dissolve
    show player 487c
    pause
    show player_arms 488c_488d_488e with dissolve
    show debbie 185d
    deb "Ммм... Немного глубже."
    show player_arms 488e with dissolve
    deb "Чувствуешь этот узел?"
    deb "Попробуй натереть..."
    show debbie 185c
    show player 487b
    player_name "Хо... Хорошо..."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "Ммм... Так хорошо."
    show debbie 185
    show player 487f
    player_name "!!!"
    show player 487g
    player_name "( Она сейчас очень расслаблена! )"
    player_name "( Интересно, понимает ли она, что я вижу сквозь ее трусики! )"
    show debbie 185d
    deb "О, твои пальцы, так хорошо."
    deb "Ты практиковался?"
    show debbie 185g
    deb "Некоторым маленьким леди понравится, насколько ты услужлив и внимателен."
    show debbie 185d
    deb "О! Вот здесь..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "!!!"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "...Умм... Спасибо, милый..."
    show debbie 186
    show player 29
    player_name "...пожалуйста..."
    show player 3
    show debbie 187
    deb "Послушай, я должна... ум..."
    return

label mom_lotion_fun_location_dialogue:
    if player.location == L_home_basement:
        deb "Наверное, мне надо закончить... стирку..."
        deb "Иди наверх и... ум..."

    elif player.location == L_home_kitchen:
        deb "Мне, наверное, надо закончить готовить..."
    return

label mom_lotion_fun_location_dialogue_after:
    show debbie 186
    show player 29
    player_name "Да... Я как раз собиралась заканчивать."
    show player 3
    show debbie 187
    deb "Спасибо... опять, милый."
    show debbie 186
    show player 29
    player_name "Пожалуйста."
    return

label mom_lotion_fun_after:
    show player 24 with dissolve
    player_name "Блин..."
    player_name "Думаю, она заметила, что я смотрю..."
    show player 34
    pause
    show player 35
    player_name "Она вся мокрая?"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "Я лучше найду себе другое занятие."
    return

label mom_lotion_fun_first_pre:
    scene home_basement_c
    show debbie 1 at right
    show player 485 at left
    with dissolve
    player_name "У меня есть твой {b}лосьон{/b}, {b}[deb_name]{/b}."
    show player 484
    show debbie 2
    deb "О, спасибо большое!"
    show debbie 8b
    deb "Ай!"
    show player 486
    pause
    show debbie 11b
    deb "Эта боль в спине не отступает!"
    deb "Совсем не весело стареть, {b}[firstname]{/b}. Я не рекомендую!"
    show debbie 10b
    return

label mom_lotion_fun_first_help_her:
    show player 485
    player_name "Хочешь, чтобы я тебе помог тебе?"
    show player 484
    show debbie 13
    deb "Хмм?"
    deb "Ты имеешь ввиду... с моим лосьоном?"
    show debbie 10b
    show player 485
    player_name "Ну, конечно... Если хочешь."
    show player 484
    show debbie 11b
    deb "Ты не будешь возражать?"
    show debbie 10b
    show player 485
    player_name "Конечно, нет! Я был бы очень рад!."
    player_name "Я могу нанести лосьон и сделать массаж везде!"
    player_name "Как тебе такое предложение?!"
    show player 484
    show debbie 14
    deb "..."
    show debbie 2
    deb "Звучит замечательно, милый!"
    deb "Как девушка может отказаться от бесплатного массажа?"
    deb "Одну секундочку..."
    deb "... Позволь мне устроиться поудобнее."
    show player 486
    show debbie 183 with dissolve
    pause
    show debbie 184 zorder 2
    show debbie_robe 184e zorder 2
    with dissolve
    show player 485
    player_name "Ты сказала, что у тебя сухие ноги?"
    show player 484
    show debbie 184b
    deb "Да, они всегда кажутся сухими в это время года!"
    show debbie 184
    show player 485
    player_name "Хорошо."
    show player 484
    show debbie 185
    show debbie_robe 185h
    with dissolve
    pause
    hide player
    show player 487c zorder 1
    show player_arms 488 zorder 3
    with dissolve
    pause
    show player_arms 488b
    with dissolve
    player_name "( !!! )"
    show debbie 185c
    show player 487b
    player_name "Упс, я не ожидал, что это выйдет так много!"
    show player 487d
    show debbie 185b
    deb "Хех."
    show debbie 185d
    deb "Все в порядке, милый. Там много поверхности, чтобы пропитать!"
    show debbie 185
    show player 487b
    player_name "Хорошо."
    show player 487c
    show player_arms 488c_488d with dissolve
    show player 487
    show debbie 185d
    deb "Ммм, как приятно..."
    show debbie 185
    show player 487c
    show player_arms 488b with dissolve
    player_name "..."
    show player_arms 488c_488d with dissolve
    pause
    show player_arms 488 with dissolve
    show player 487e
    player_name "Позаботились о нижней половине."
    player_name "Ты хочешь, чтобы я намазал тебе бедра?"
    show player 487d
    show debbie 185b
    deb "... Да, я полагаю. Если не возражаешь."
    show debbie 185
    show player 487b
    player_name "Да, нет."
    show player 487c
    show player_arms 488b with dissolve
    pause
    show player_arms 488c_488d_488e with dissolve
    pause
    show debbie 185d
    deb "Ммм, у тебя хорошо получается, {b}[firstname]{/b}..."
    show player_arms 488e with dissolve
    deb "Можешь тереть сильнее, если хочешь."
    deb "У меня определенно есть напряжение в мышцах бедер..."
    show debbie 185c
    show player 487b
    player_name "Да, Я чувствую."
    show player 487c
    show player_arms 488e_488f with dissolve
    pause
    show debbie 185b
    deb "О, это рай..."
    show debbie 185
    show player 487f
    player_name "( !!! )"
    show player 487g
    player_name "( Она сейчас действительно расслаблена! )"
    player_name "( Интересно, понимает ли она, что я вижу сквозь ее трусики? )"
    show debbie 185d
    deb "У тебя прекрасные руки, {b}[firstname]{/b}!"
    deb "Ты должен стать массажистом..."
    show debbie 185g
    deb "Держу пари, ты бы сколотил состояние!"
    show debbie 185d
    deb "О! Прямо там..."
    show debbie 185f
    pause
    show debbie_robe 185i with dissolve
    pause
    show debbie 185e
    deb "( !!! )"
    hide player_arms
    show player 3 at Position (xpos=420)
    show xtra 21 zorder 2 at Position (xpos=289)
    hide debbie_robe
    show debbie 187
    with dissolve
    deb "... Хе-хе, этого, наверное, достаточно. Я могу закончить отсюда."
    show debbie 186
    show player 29
    player_name "Ты уверена?"
    show player 3
    show debbie 187
    deb "Почему бы тебе не подняться наверх?"
    deb "Я должен присматривать за стиркой..."
    deb "... и включить сушилку."
    show debbie 186
    show player 29
    player_name "Да, хорошо."
    show player 3
    show debbie 187
    deb "Спасибо опять, милый."
    show debbie 186
    show player 29
    player_name "Пожалуйста."
    scene home_livingroom_b with fade
    show player 24 with dissolve
    player_name "Черт..."
    player_name "Она, должно быть, заметила, что я подглядываю."
    show player 34
    pause
    show player 35
    player_name "Она была взволнована или я просто вообразил это?"
    show player 43
    pause
    show player 81 with dissolve
    pause
    show player 83
    player_name "... Наверное, мне стоит отвлечься!"
    return

label mom_lotion_fun_first_leave:
    show player 485
    player_name "Что-нибудь еще, {b}[deb_name]{/b}?"
    show player 484
    show debbie 11b
    deb "Нет, этого достаточно."
    deb "Еще раз спасибо за помощь, милый."
    show debbie 10b
    show player 485
    player_name "Пожалуйста, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
