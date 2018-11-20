label sis_bedroom_sis_not_in_room:
    scene jennybedroom
    show player 34 at left with dissolve
    player_name "( Хммм... )"
    show player 35 at left
    player_name "( Она не у себя в комнате... )"
    show player 18 at left
    player_name "( Может, я могу пока тут осмотреться! )"
    hide player 18 at left with dissolve
    return

label sis_bedroom_sis_sleeping:
    scene jennybedroom_clear
    player_name "( {b}[jen_name]{/b} спит. )"
    player_name "( Я должен вести себя очень тихо, или она меня заметит... )"
    player_name "( ...Если она проснется - я труп! )"
    return

label sis_bedroom_sis_hallway_2_started:
    scene jennybedroom_closeup
    show jenny 22 at right
    show player 11 at left with dissolve
    jen "Да отстань от меня уже! Почему ты не попросишь трусики у {b}[deb_name]{/b}, извращенец!"
    jen "У неё в {b}ящичке{/b} их огромное количество, а иногда она просто разбрасывает одежду {b}в её комнате{/b}!!"
    return

label sis_bedroom_sis_caught_stealing_panties:
    scene jennybedroom
    show player 22 at left
    show jenny 7b at right
    with dissolve
    jen "Какого {b}хуя{/b} ты тут забыл?!!" with hpunch
    show jenny 8b at right
    show player 23 at left
    player_name "Это не то, что ты-"
    show player 22
    show jenny 7b
    jen "Ты рылся в моих вещах?!"
    show jenny 8b
    show player 23
    player_name "Да подожди же!"
    show jenny 7b
    show player 22
    jen "Или даже пытался что-то {b}украсть{/b}??"
    show player 23
    show jenny 8b
    player_name "Дай мне всё объяснить!!"
    show player 22
    show jenny 9c at Position(xpos=937)
    jen "Ох, лучше бы тебе имет {b}действительно{/b} хорошее, блять, объяснение!"
    jen "Если ты не хочешь, чтобы {b}[deb_name]{/b} узнала о том, что ты воруешь мои вещи."
    show player 23
    show jenny 6b
    player_name "Да нет же!"
    show player 10
    show jenny 10b
    player_name "То есть... Всё не совсем так..."
    player_name "Ладно, слушай, мне очень нужно оказать кое-кому одну услугу."
    player_name "И эта услуга... короче, я должен принести ему {b}трусики{/b}..."
    show player 5
    show jenny 9c
    jen "Что за хуйня?!"
    show jenny 10b
    show player 21
    player_name "Я понимаю, это звучит немного странно..."
    show jenny 7b at right
    show player 11
    with hpunch
    jen "{b}НЕМНОГО{/b}?!"
    jen "С какими же извращенцами ты общаешься!"
    show jenny 9c at Position(xpos=937)
    jen "Только не говори мне, что этот урод - {b}Эрик{/b}."
    show player 12
    show jenny 10b
    player_name "Конечно нет!"
    show player 10
    player_name "Слушай, {b}[jen_name]{/b}! Они мне очень нужны!"
    show jenny 11b
    player_name "Я дам тебе всё, что ты хочешь!"
    show player 5
    jen "Хмм..."
    show jenny 12b
    show player 11
    jen "Ладно! Если они так сильно тебе нужны - ты можешь {b}купить их{/b} у меня."
    show jenny 11b
    show player 10
    player_name "Что?"
    show jenny 12b
    show player 11
    jen "Ага."
    jen "Я знаю, что ты подрабатываешь в последнее время."
    show jenny 11b
    show player 10
    player_name "{b}Диана{/b} сказала тебе?"
    show player 11
    show jenny 9c
    jen "Какая разница..."
    show jenny 12b
    jen "У тебя должно быть при себе {b}немного{/b} денег!"
    show jenny 11b
    show player 10
    player_name "Но-"
    show jenny 9c
    show player 11
    jen "{b}ПОСЛУШАЙ МЕНЯ{/b}! Я {b}не{/b} собираюсь просто так швырять тебе свое белье, понятно?!"
    jen "Мне нужно покупать что-то новое, так что твой {b}единственный{/b} вариант..."
    show jenny 12b
    show player 5
    jen "... это {b}деньги{/b}."
    show jenny 18b at right
    show player 10
    player_name "Как много ты хочешь?"
    show jenny 19b
    show player 11
    jen "{b}$100{/b} покроют всё это."
    show jenny 18b
    show player 29
    player_name "Это большая сумма..."
    show jenny 9c at Position(xpos=937)
    show player 11 at left
    jen "Ну? Берешь их или нет?!"
    show jenny 6b
    return

label sis_bedroom_sis_caught_stealing_panties_buy_panties:
    show player 12 at left
    show jenny 18b at right
    player_name "Окей! Я беру!"
    play audio coins2
    show player 41 at Position (xpos=38) with fastdissolve
    pause
    show jenny 80b at Position(xpos=945)
    show player 1 at left
    jen "Вот и отлично, забирай..." with fastdissolve
    show jenny 81b
    show player 11
    jen "А теперь вали из моей комнаты, извращенец!"
    show jenny 14b
    show unlock17 at truecenter
    pause
    hide unlock17 with dissolve
    return

label sis_bedroom_sis_caught_stealing_panties_do_not_buy_panties:
    show jenny 10b at Position(xpos=937)
    show player 35 at left
    player_name "Вообще-то, сейчас они мне не нужны..."
    show jenny 9c
    show player 39 at Position (xpos=38)
    jen "Тогда давай их сюда и вали из моей комнаты, извращенец!"
    return

label sis_bedroom_sis_caught_stealing_panties_cant_buy_panties:
    show player 24 at left
    show jenny 10b at Position(xpos=937)
    player_name "У меня сейчас столько нет..."
    show jenny 9c
    show player 5
    jen "Тебе же хуже. А теперь пошел вон отсюда, извращенец!"
    return

label sis_bedroom_sis_diary_locked:
    scene jennybedroom_closeup
    show jenny 20 at right
    show player 24 at left with dissolve
    jen "Ну и ну."
    jen "И что же нужно этому маленькому извращенцу в этот раз?"
    jen "Может быть, ещё трусики?"
    return

label sis_bedroom_sis_diary_locked_more_panties:
    show jenny 21
    show player 111f
    player_name "Да, вообще-то, мне нужны ещё трусики."
    show player 106
    show jenny 22
    jen "Зайдешь попозже..."
    show jenny 23
    show player 108f
    player_name "Но-"
    show jenny 22
    show player 109f
    jen "Я сейчас немного занята, не видишь??"
    show jenny 23
    show player 108f
    player_name "Ладно..."
    show jenny 22
    show player 109f
    jen "И дверь закрой!"
    show jenny 20
    show player 106
    jen "Не хочу, чтобы какой-то извращенец подглядывал за мной."
    show jenny 21
    show player 109f
    player_name "..."
    show player 108f
    player_name "Ладно..."
    return

label sis_bedroom_sis_mom_needs_you:
    call expression game.dialog_select("sis_bedroom_sis_mom_needs_you_pre")
    menu:
        "Ей нужна помощь.":
            call expression game.dialog_select("sis_bedroom_sis_mom_needs_you_help")
    return

label sis_bedroom_sis_mom_needs_you_pre:
    scene location_home_jennybedroom_closeup with fade
    show jenny 21 zorder 0 at right
    show player 108f zorder 1 at left
    with dissolve
    player_name "Эм, Вообще-то {b}[deb_name]{/b} нужно..."
    show player 111f
    player_name "...С тобой кое о чем поговорить!"
    show jenny 22
    show player 106
    jen "О чем же?"
    return

label sis_bedroom_sis_mom_needs_you_help:
    show jenny 23
    show player 111f
    player_name "Ей нужна твоя помощь..."
    show player 110f
    jen "..."
    show jenny 22
    show player 106
    jen "И с чем же ей нужна помощь?"
    show player 108f
    show jenny 23
    player_name "Я не уверен."
    player_name "Она просто... Попросила сказать тебе об этом!"
    show jenny 22
    show player 109f
    jen "Угх!"
    show jenny 24
    jen "Ладно, сейчас спущусь..."
    show jennybed zorder 1 at right
    show player 5 zorder 2
    show jenny 9 zorder 2
    jen "Только не трогай тут ничего, и вообще прочь из комнаты..."
    hide jenny 9 with fade
    show player 106
    player_name "..."
    show player 113
    player_name "Окей..."
    hide player
    hide jennybed
    return

label sis_bedroom_sis_final_started:
    scene jenny_webcam2
    show jenny 151 at Position(xpos=407,ypos=748)
    with fade
    jen "Хей, парни!"
    show jenny 155
    jen "Я так рада, что вы наслаждаетесь моим шоу."
    show jenny 151
    jen "Новые игрушки так популярны, я получила кучу новых подписчиков!"
    show jenny 150
    jen "..."
    show jenny 152
    jen "Что?! Думаете, я могу ещё лучше? Но как?!"
    jen "Ролевые игры?"
    show jenny 154
    jen "Вы имеете ввиду всякие костюмы?"
    show jenny 152
    jen "Но тогда какая тема?"
    jen "Чирлидерши и связывание?!"
    show jenny 154
    jen "Это немного, специфично... Но, видно это сейчас популярно."
    show jenny 153
    jen "Хмм..."
    show jenny 151
    jen "А что ещё заставит вас донатить?"
    show jenny 152
    jen "Больше хардкора? В сексе?"
    jen "Без презерватива?!"
    show jenny 154
    jen "Ну, наверное, это будет выглядет более натурально..."
    show jenny 152
    jen "Ну, вам парни не повезло. У меня сейчас нет парня."
    show jenny 151
    jen "К сожалению, всё что у меня есть - это мои игрушки! Хаха!"
    show jenny 150
    jen "..."
    show jenny 152
    jen "Думаете, что с этим я смогу удвоить свой доход?"
    show jenny 153
    jen "Хмм..."
    show jenny 155
    jen "Ладно! Спасибо за ваши предложения, парни!!"
    show jenny 159 at left
    show jenny 159 at Position(ypos=748)
    jen "Посмотрю, что можно сделать..."
    show jenny 160 at Position(ypos=771) with fastdissolve

    jen "Черт... Они хотят увидеть настоящий секс."
    jen "Не думаю, что кто-то из моих бывших согласится. Да и они такие мудаки."
    jen "Хотя, всегда есть {b}[firstname]{/b}."
    jen "Угх... Не знаю, хорошая ли это идея."
    jen "Немого стремно думать о таком, но у него вроде неплохой член."
    jen "Он, наверное, даже сделает это бесплатно. Мелкий извращенец."
    jen "А если я ему что-нибудь пообещаю, он ещё и достанет мне костюмы!"
    jen "Боже, как же заманчиво! За это зрелище они готовы отвалить кучу денег."
    jen "Я должна это обдумать..."
    scene hallway
    show player 11
    with fade
    player_name "..."
    show player 35
    player_name "( Неужели она зайдет так далеко, чтобы удовлетворить своих подписчиков... )"
    show player 4 at Position(xpos=518)
    player_name "( Наверное, ей нравится получать столько внимания... И денег. )"
    hide player with dissolve
    return

label sneak_in_sis_bed:
    $ game.timer.tick()
    label sis_bed_replay_1:
    label sis_bed_replay_2:
    label sis_bed_replay_3:
    label sis_bed_replay_4:
    label sis_bed_replay_5:
    label sis_bed_replay_final:
    call expression game.dialog_select("sneak_in_sis_bed_pre")

    if store._in_replay == "sis_bed_replay_1":
        jump expression game.dialog_select("sis_bed_replay_fail")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont")
    menu:
        "Уйти.":
            call expression game.dialog_select("sneak_in_sis_bed_pre_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Прижаться." if sister.known(sis_shower_cuddle01) and not sister.known(sis_shower_cuddle02):
            $ sis_shower_cuddle01.finish()
            label sis_bed_replay_fail:
                call expression game.dialog_select("sneak_in_sis_bed_cuddle_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            jump expression game.dialog_select("hallway_dialogue")

        "Прижаться" if sister.known(sis_shower_cuddle02):
            $ sis_shower_cuddle02.finish()
            label sis_bed_replay_cont:
                call expression game.dialog_select("sneak_in_sis_bed_cuddle_pass")

            if store._in_replay == "sis_bed_replay_2":
                jump expression game.dialog_select("sis_bed_replay_fail_2")

            elif not store._in_replay == None:
                jump expression game.dialog_select("sis_bed_replay_cont_2")
    menu:
        "Уйти.":
            call expression game.dialog_select("sneak_in_sis_bed_cuddle_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Сжать груди." if not sister.known(sis_shower_cuddle03):
            label sis_bed_replay_fail_2:
                call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_2"
            jump expression game.dialog_select("hallway_dialogue")

        "Сжать груди." if sister.known(sis_shower_cuddle03):
            $ sis_shower_cuddle03.finish()
            if not sister.known(sis_couch03):
                $ sister.add_event(sis_couch03)
            label sis_bed_replay_cont_2:
                call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_pass")

    if store._in_replay == "sis_bed_replay_3":
        jump expression game.dialog_select("sis_bed_replay_fail_3")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont_3")
    menu:
        "Уйти.":
            call expression game.dialog_select("sneak_in_sis_bed_squeeze_boobs_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Потереть киску." if not sister.known(sis_shower_cuddle04):
            label sis_bed_replay_fail_3:
                call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_3"
            jump expression game.dialog_select("hallway_dialogue")

        "Потереть киску." if sister.known(sis_shower_cuddle04):
            if not sister.known(sis_final):
                $ sister.add_event(sis_final)
            $ sis_shower_cuddle04.finish()
            label sis_bed_replay_cont_3:
                call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_pass")

    if store._in_replay == "sis_bed_replay_4":
        jump expression game.dialog_select("sis_bed_replay_fail_4")

    elif not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_cont_4")
    menu:
        "Уйти.":
            call expression game.dialog_select("sneak_in_sis_bed_rub_pussy_leave")
            jump expression game.dialog_select("hallway_dialogue")

        "Вставить внутрь." if not sister.known(sis_shower_cuddle05) or player.stats.dex() < 7:
            label sis_bed_replay_fail_4:
                if player.stats.dex() < 7:
                    $ stat_warn = dex_warn
                else:
                    $ stat_warn = ""
                if not store._in_replay == None:
                    $ stat_warn = dex_warn
                call expression game.dialog_select("sneak_in_sis_bed_sex_stat_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_4"
            jump expression game.dialog_select("hallway_dialogue")

        "Вставить внутрь." if sister.known(sis_shower_cuddle05) and player.stats.dex() >= 7:
            $ sis_shower_cuddle05.finish()
            label sis_bed_replay_cont_4:
                call expression game.dialog_select("sneak_in_sis_bed_sex_stat_pass")

    if not store._in_replay == None:
        jump expression game.dialog_select("sis_bed_replay_fuck")
    menu:
        "Быстрый секс.":
            label sis_bed_replay_fuck:
                call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck")

    menu sisbedroom_sex_loop:
        "Продолжать.":
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_keep_going")
            jump expression game.dialog_select("sisbedroom_sex_loop")

        "Кончить внуть." if store._in_replay == "sis_bed_replay_5" or store._in_replay == None and player.stats.str() < 7:
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_fail")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_5"

        "Кончить внутрь." if store._in_replay == "sis_bed_replay_final" or store._in_replay == None and player.stats.str() >= 7:
            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_pass")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_final"
        "Вытащить и кончить.":

            call expression game.dialog_select("sneak_in_sis_bed_rabbit_fuck_cum_outside")
            $ renpy.end_replay()
            $ persistent.cookie_jar["Jenny"]["unlocked"] = True
            $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
            if not persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] == "sis_bed_replay_final":
                $ persistent.cookie_jar["Jenny"]["gallery_labels"]["07_label"] = "sis_bed_replay_5"
    jump expression game.dialog_select("hallway_dialogue")

label sneak_in_sis_bed_pre:
    scene jennybedroom_bed with None
    show jennysex 46 at right
    with dissolve
    player_name "( Может если я буду очень аккуратен... )"
    player_name "( ...Она не заметит... )"
    show jennysex 47 with dissolve
    player_name "( Нужно просто медленно залезть к ней под одеяло... )"
    hide jennysex
    show jennysex 48 zorder 1 at Position(xpos=644)
    show jenny_bedcover zorder 2 at right
    with dissolve
    player_name "( Ладно, это страшнее, чем я думал... )"
    player_name "( Но я так хочу её потрогать... )"
    player_name "( ... может она не заметит легкого прикосновения? )"
    return

label sneak_in_sis_bed_pre_leave:
    player_name "( С другой стороны, может лучше в другой раз. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_cuddle_fail:
    show jennysex 49 at Position(xpos=682) with fastdissolve
    pause
    show jennysex 50 with fastdissolve
    pause
    show jennysex 52
    jen "{b}[firstname]{/b}?"
    show jennysex 53
    jen "Какого {b}ХУЯ{/b} ты тут делаешь??!!" with hpunch
    show jennysex 91
    player_name "Не кричи так! Ты разбудишь {b}[deb_name]{/b}..."
    show jennysex 53
    jen "Думаешь, мне {b}есть до этого дело{/b}??! Да что с тобой не так?!"
    show jennysex 91
    player_name "Прости..."
    player_name "Прости меня!!"
    show jennysex 53
    jen "Заткнись и {b}ПРОВАЛИВАЙ{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_cuddle_pass:
    show jennysex 49 at Position(xpos=682) with fastdissolve
    player_name "( Воу... Её кожа такая мягкая... )"
    player_name "( ...И она, вроде как, не заметила, что я трогаю её ногу. )"
    player_name "( Я поглажу её немного... )"
    show jennysex 84
    pause .4
    show jennysex 49_84 at Position(xpos = 682)
    pause 8
    show jennysex 84
    player_name "( Если она не заметит, можно будет продвигаться дальше... )"
    return

label sneak_in_sis_bed_cuddle_leave:
    player_name "( Я хочу большего... )"
    player_name "( Но нужно уйти до того, как она меня заметит. )"
    player_name "( Попробую ещё раз в следующий раз... )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_squeeze_boobs_fail:
    show jennysex 54 with fastdissolve
    pause
    show jennysex 55
    pause
    show jennysex 50 with fastdissolve
    pause
    show jennysex 52
    jen "{b}[firstname]{/b}?"
    show jennysex 53
    jen "Какого {b}ХУЯ{/b} ты тут делаешь??!!" with hpunch
    show jennysex 91
    player_name "Не кричи так! Ты разбудишь {b}[deb_name]{/b}..."
    show jennysex 53
    jen "Думаешь, мне {b}есть до этого дело{/b}??! Да что с тобой не так?!"
    show jennysex 91
    player_name "Прости..."
    player_name "Прости меня!!"
    show jennysex 53
    jen "Заткнись и {b}ПРОВАЛИВАЙ{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_squeeze_boobs_pass:
    show jennysex 54 with fastdissolve
    pause
    show jennysex 55
    pause
    player_name "( Вау, а они большие... )"
    player_name "( Почти что не помещаются в руку... )"
    show jennysex 54_55
    pause 8
    show jennysex 56 with fastdissolve
    player_name "!!!"
    player_name "( Черт! Неужели она просыпается?! )"
    show jennysex 57 with fastdissolve
    pause
    show jennysex 58 with fastdissolve
    player_name "( Она... )"
    player_name "( Она подняла футболку... )"
    player_name "( Что она пытается мне сказать? )"
    player_name "( Хочет, чтобы я снова их потрогал...? )"
    show jennysex 59 with fastdissolve
    pause
    show jennysex 60_59
    pause 8
    show jennysex 60
    player_name "( Они такие {b}теплые{/b}... )"
    show jennysex 59
    player_name "( ...такие {b}мягкие{/b}... )"
    show jennysex 60
    player_name "( Это охрененно... )"
    show jennysex 61 with fastdissolve
    player_name "!!!"
    player_name "( Ох, черт! )"
    show jennysex 62 with fastdissolve
    player_name "( У меня встает... )"
    player_name "( Дерьмо! Он давит прямо ей на киску... )"
    player_name "( Стоп... )"
    player_name "( Она никак не реагирут? )"
    player_name "( Может я смогу потерться об неё... )"
    return

label sneak_in_sis_bed_squeeze_boobs_leave:
    player_name "( Нет... Слишком рисковано. )"
    player_name "( Попробую в следующий раз. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rub_pussy_fail:
    show jennysex 63 at Position(xpos=684) with fastdissolve
    pause
    show jennysex 62 at Position(xpos=682)
    pause
    show jennysex 63 at Position(xpos=684)
    pause
    show jennysex 64 at Position(xpos=682) with fastdissolve
    pause
    show jennysex 65
    pause
    show jennysex 66
    jen "{b}[firstname]{/b}?"
    show jennysex 67
    jen "Какого {b}ХУЯ{/b} ты тут делаешь??!!" with hpunch
    show jennysex 91
    player_name "Не кричи так! Ты разбудишь {b}[deb_name]{/b}..."
    show jennysex 53
    jen "Думаешь, мне {b}есть до этого дело{/b}??! Да что с тобой не так?!"
    show jennysex 91
    player_name "Прости..."
    player_name "Прости меня!!"
    show jennysex 53
    jen "Заткнись и {b}ПРОВАЛИВАЙ{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rub_pussy_pass:
    show jennysex 63 at Position(xpos=684) with fastdissolve
    pause
    show jennysex 62_64 at Position(xpos=682)
    pause 8
    show jennysex 62 at Position(xpos=682)
    player_name "( Её дыхание учащается... )"
    player_name "( Это ощущение... Она и правда намокла... )"
    show jennysex 63 at Position(xpos=684)
    player_name "( Как же {b}хорошо{/b}! Я хочу большего... )"
    show jennysex 68 at Position(xpos=682) with fastdissolve
    player_name "( Посмотрим, смогу ли я приспустить... )"
    show jennysex 69 with fastdissolve
    pause
    show jennysex 70 at Position(xpos=652) with fastdissolve
    pause
    show jennysex 71 at Position(xpos=682) with fastdissolve
    player_name "( Боже... )"
    show jennysex 72 with fastdissolve
    player_name "( Не могу поверить, что я собираюсь это сделать... )"
    return

label sneak_in_sis_bed_rub_pussy_leave:
    player_name "( Нет... не сейчас. )"
    player_name "( Нужно уйти, пока она не перевернулась. )"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_sex_stat_fail:
    show jennysex 76 at Position(xpos=674) with fastdissolve
    pause
    show jennysex 75 at Position(xpos=682)
    jen "[stat_warn]Ты и {b}правда{/b} думал, что я позволю тебе зайти так далеко?!" with hpunch
    show jennysex 74
    jen "[stat_warn]Радуйся, что я не остановила тебя раньше, ебучий извращенец!!"
    show jennysex 73b
    player_name "Ты... Ты знала, что я здесь?"
    show jennysex 74
    jen "[stat_warn]Кончено же, идиот! Просто я хотела посмотреть, насколько ты {b}отчаянный{/b}."
    show jennysex 75
    jen "[stat_warn]А сейчас подтяни штаны, и закончи в {b}своей{/b} комнате то, что ты начал!!"
    show jennysex 73b
    player_name "Я..."
    player_name "Я прошу прощения!"
    show jennysex 75
    jen "Ага, конечно, {b}ВАЛИ УЖЕ ОТСЮДА{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_sex_stat_pass:
    show jennysex 76 at Position(xpos=674) with fastdissolve
    pause
    show jennysex 75 at Position(xpos=682)
    jen "Ты и {b}правда{/b} думал, что я позволю тебе зайти так далеко?!" with hpunch
    show jennysex 74
    jen "Радуйся, что я не остановила тебя раньше, ебучий извращенец!!"
    show jennysex 73b
    player_name "Ты... Ты знала, что я здесь?"
    show jennysex 74
    jen "Кончено же, идиот! Ты слишком тупой, чтобы тебя не заметить..."
    show jennysex 73
    return

label sneak_in_sis_bed_rabbit_fuck:
    show jennysex 77 at Position(xpos=713)
    jen "Ахх!!!" with vpunch
    show jennysex 79b at Position(xpos=720) with fastdissolve
    jen "ЧТО ТЫ ТВОРИШЬ?!!"
    show jennysex 78 at Position(xpos=713) with fastdissolve
    player_name "Я хочу тебя, {b}[jen_name]{/b}!!!"
    $ anim_toggle = False
    $ xray = False
    show screen sex_xray_anim_buttons
    pause
    if anim_toggle:
        hide jennysex 78
        hide screen sex_xray_anim_buttons
        show jennysex 79_78 at Position(xpos = 720)
        pause 8
        hide jennysex 79_78
    else:

        hide screen sex_xray_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            show jennysex 79 at Position(xpos = 720)
            pause
            show jennysex 78 at Position(xpos = 713)
            pause
            $ animcounter += 1
    show jennysex 79b at Position(xpos=720)
    jen "БЛЯТЬ!!!"
    show jennysex 77 at Position(xpos=713)
    jen "Не так БЫСТРО!!"
    show jennysex 79b at Position(xpos=720)
    jen "О Боже..."
    show jennysex 77 at Position(xpos=713)
    jen "Это..."
    show jennysex 79 at Position(xpos=720)
    jen "... Это {b}ПРОСТО АХУЕННО{/b}!!" with vpunch
    if anim_toggle:
        hide jennysex 79
        show jennysex 78_79 at Position(xpos = 713)
        pause 4
        hide jennysex 78_79
    else:

        $ animcounter = 0
        while animcounter < 2:
            show jennysex 78 at Position(xpos = 713)
            pause
            show jennysex 79 at Position(xpos = 720)
            pause
            $ animcounter += 1
    show jennysex 77 at Position(xpos=713)
    jen "Не {b}СМЕЙ{/b} кончать в меня..."
    show jennysex 79b at Position(xpos=720)
    jen "... Я клянусь, Я {b}ТЕБЯ ПРИКОНЧУ{/b}!!"
    return

label sneak_in_sis_bed_rabbit_fuck_keep_going:
    show jennysex 79b at Position(xpos = 720)
    show screen sex_xray_anim_buttons
    pause
    if anim_toggle:
        hide jennysex 79b
        hide screen sex_xray_anim_buttons
        show jennysex 78_79 at Position(xpos = 713)
        pause 8
        hide jennysex 78_79
        show jennysex 79b at Position(xpos = 720)
    else:

        hide screen sex_xray_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            show jennysex 78 at Position(xpos = 713)
            pause
            show jennysex 79 at Position(xpos = 720)
            pause
            $ animcounter += 1
    return

label sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_fail:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    pause
    show jennysex 89b at Position(xpos=674) with hpunch
    pause
    show white zorder 3
    show jennysex 89c
    hide white with dissolve
    pause
    show jennysex 88 at Position(xpos=674)
    jen "[str_warn]Какого {b}ХЕРА{/b}??" with vpunch
    jen "[str_warn]Ты хотел КОНЧИТЬ В МЕНЯ??"
    show jennysex 89
    player_name "Не кричи! Ты разбудишь {b}[deb_name]{/b}..."
    show jennysex 87
    jen "[str_warn]Да что с тобой не так?!"
    show jennysex 88
    jen "[str_warn]Я ведь могу {b}ЗАБЕРЕМЕНИТЬ{/b}, знаешь??! ИДИОТ!!"
    show jennysex 89
    player_name "Я..."
    player_name "Я прошу прощения!!"
    show jennysex 88
    jen "Ага, конечно! {b}ПОШЕЛ ВОН{/b}!!"
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rabbit_fuck_cum_inside_stat_pass:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    jen "Боже..."
    show jennysex 78 at Position(xpos=713)
    jen "... Я больше не могу..."
    show jennysex 80a at Position(xpos=738)
    jen "{b}Aххх!!!!{/b}" with vpunch
    show white zorder 3
    show jennysex 80b
    hide white with dissolve
    pause
    show white zorder 3
    show jennysex 80c
    hide white with dissolve
    pause
    $ xray = False
    show jennysex 81b at Position(xpos=674) with fastdissolve
    jen "{b}*Жадно дышит*{/b}"
    show jennysex 81 at Position(xpos=674)
    jen "Ты что, кончил в меня??"
    show jennysex 90
    player_name "Я... Я не уверен..."
    show jennysex 82
    jen "Не смей врать! Я чувствую, он продолжает пульсировать во мне!"
    show jennysex 90
    player_name "Это просто рефлекс!"
    player_name "Я... Я не мог остановиться..."
    show jennysex 82
    jen "Да что с тобой не так?!" with hpunch
    jen "Я ведь могу {b}ЗАБЕРЕМЕНИТЬ{/b}, знаешь??! ИДИОТ!!"
    show jennysex 90
    player_name "Я..."
    player_name "Я проше прощения!!"
    show jennysex 82
    jen "Просто..."
    jen "Просто {b}ВАЛИ ОТСЮДА{/b}!!" with hpunch
    hide jennysex
    hide jenny_bedcover
    return

label sneak_in_sis_bed_rabbit_fuck_cum_outside:
    show jennysex 78 at Position(xpos=713)
    pause
    show jennysex 79 at Position(xpos=720)
    pause
    show jennysex 85b at Position(xpos=674)
    pause
    show white zorder 3
    show jennysex 85 at Position(xpos=674)
    hide white with dissolve
    pause
    show jennysex 86 with fastdissolve
    player_name "Ахх..."
    show jennysex 88
    jen "Ну что, удовлетворен?! Мелкий ублюдок..." with hpunch
    show jennysex 87
    jen "Тебе повезло, что я была возбуждена..."
    jen "... и, что у тебя отличный... член."
    show jennysex 89
    player_name "Мне он тоже нравится-"
    show jennysex 87
    jen "Мне нет до этого дела!!"
    show jennysex 88
    jen "{b}ВАЛИ УЖЕ ОТСЮДА{/b}!!"
    hide jennysex
    hide jenny_bedcover
    return

label diary_dialogue:
    scene jennybedroom
    $ counter = 1
    while counter <= 4:
        call expression game.dialog_select("diary0" + str(counter))
        $ counter += 1
    call expression game.dialog_select("diary_after")
    $ game.main()

label diary01:
    show jenny_diary 01 at truecenter with dissolve
    player_name "( А это... Её {b}дневник{/b}... )"
    player_name "( Интересно... )"
    player_name "( Может, чуток почитать... )"
    window hide
    call screen diary_next
    return

label diary02:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 02 at truecenter with Dissolve(0.2)
    player_name "( Ей нужно придумать хоть какое-то занятие... )"
    player_name "( Она слишком долго просто сидит тут ничего не делая... )"
    window hide
    call screen diary_next
    return

label diary03:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 03 at truecenter with Dissolve(0.2)
    player_name "Вау..."
    player_name "( Никогда бы не подумал, что {b}[jen_name]{/b} была настолько {b}возбуждена{/b}... )"
    window hide
    call screen diary_next
    return

label diary04:
    show jenny_diary next at Position (xpos = 512, ypos = 394) with Dissolve(0.2)
    show jenny_diary 04 at truecenter with Dissolve(0.2)
    player_name "!!!"
    window hide
    call screen diary_next
    return

label diary_after:
    hide jenny_diary
    show player 108f
    with dissolve
    player_name "( ...Не могу поверить, что она написала все эти вещи... )"
    show player 21
    player_name "( Неужели она и правда... Поможет мне потерять девственность?? )"
    show player 108f
    player_name "( Или... Она просто шутила? )"
    show player 12
    player_name "( ...И о чем это вэбкам шоу {b}Live Crush{/b} вообще?? )"
    show player 109f
    player_name "..."
    show player 108f
    player_name "( Я так много не знал о {b}[jen_name]{/b}... )"
    show player 113
    player_name "( Нужне быстрее свалить отсюда, а то будет хуже. )"
    hide player
    return

label bedtable_night:
    call expression game.dialog_select("bedtable_night_dialogue")
    $ in_sis_room = True
    jump expression game.dialog_select("sis_bedroom_dialogue")

label bedtable_night_dialogue:
    scene jennybedroom_night
    player_name "( Я ещё вернусь, когда она не сможет меня спалить. )"
    return

label desk02_locked_dialogue:
    scene expression game.timer.image("sisbedroom{}")
    show player 35 at left
    player_name "( У меня нет {b}пароля{/b} от её компьютера... )"
    $ game.main()

label bedside01_dialogue:
    call expression game.dialog_select("bedside01_dialogue{}".format(random.randint(1,2)))
    $ look_for_panties = True
    $ sis_bedroom_count = 1

    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    show screen bedside01
    call screen ui

label bedside01_dialogue1:
    scene bedside01
    player_name "ЧТО ЗА-"
    player_name "..."
    player_name "( Это... {b}Секс игрушки{/b}?! )"
    player_name "..."
    player_name "( ...и её {b}трусики{/b}! )"
    player_name "( Может если... я возьму одни... )"
    player_name "( ...она не заметит. )"
    return

label bedside01_dialogue2:
    scene bedside01
    player_name "( Боже... )"
    player_name "..."
    player_name "( Это место просто наполнено этими мезкими вещами! )"
    player_name "( Лучше сначала спросить у неё... )"
    return

label siscomp_day:
    call expression game.dialog_select("siscomp_day_pre")
    if L_home_shower.is_here(M_jenny):
        call expression game.dialog_select("siscomp_day_showering")
    else:
        call expression game.dialog_select("siscomp_day_not_showering")
    $ player.go_to(L_home_hallway)
    $ game._in_shower = None
    $ game.main()

label siscomp_day_pre:
    scene jennybedroom
    show player 98 at left with dissolve
    player_name "( Хмм... Посмотрим, включен ли компьютер. )"
    player_name "( Интересно, что же я там найду... )"
    return

label siscomp_day_showering:
    show jenny 8b at right with dissolve
    jen "..."
    show jenny 7b at right with hpunch
    jen "{b}ЧЕМ{/b} я могу тебе помочь??!"
    show jenny 8b at right
    show player 23 at left
    player_name "!!!"
    show player 29 at left
    show jenny 10b at right
    player_name "Прости... Я просто хотел проверить, работает ли у тебя инет!!"
    player_name "А то у меня что-то не подключается..."
    show player 3 at left
    show jenny 9c at right
    jen "Не смей, блять, {b}трогать{/b} мой компьютер!!"
    show player 24 at left
    jen "Просто спроси меня в следующий раз."
    show player 10 at left
    show jenny 6b at right
    player_name "Обязательно!"
    show player 22 at left
    show jenny 7b at right
    jen "А теперь пошел прочь из {b}МОЕЙ КОМНАТЫ{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label siscomp_day_not_showering:
    show jenny 8 at right with dissolve
    jen "..."
    show jenny 7 at right with hpunch
    jen "{b}ЧЕМ{/b} я могу тебе помочь??!"
    show jenny 8 at right
    show player 23 at left
    player_name "!!!"
    show player 29 at left
    show jenny 10 at right
    player_name "Прости... Я просто хотел проверить, работает ли у тебя инет!!"
    player_name "А то у меня что-то не подключается..."
    show player 3 at left
    show jenny 9 at right
    jen "Не смей, блять, {b}трогать{/b} мой компьютер!!"
    show player 24 at left
    jen "Просто спроси меня в следующий раз."
    show player 10 at left
    show jenny 6 at right
    player_name "Обязательно!"
    show player 22 at left
    show jenny 7 at right
    jen "А теперь пошел прочь из {b}МОЕЙ КОМНАТЫ{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal:
    scene jennybedroom
    show jenny 11 at right
    show player 10 at left
    with dissolve
    player_name "Хей, {b}[jen_name]{/b}."
    show player 5
    show jenny 9
    jen "Чего тебе?"
    show jenny 9b
    show player 10
    player_name "Мне нужна твоя помощь с кое-чем..."
    show player 5
    show jenny 12
    jen "Как много ты мне заплатишь"
    show jenny 11
    show player 12
    player_name "Я ведь ещё даже не сказал, что я хочу!"
    show player 5
    show jenny 9
    jen "Хмм, и правда... Прежде чем устанавливать цену, я должна узнать все детали!"
    show jenny 11
    show player 37 with dissolve
    player_name "*Эх*"
    show player 10 with dissolve
    player_name "Одной девочке из моей школы нужно потренировать её навыки чирлидерши"
    show player 5
    show jenny 9
    jen "Ты пытаешься завалить её в постель?"
    show jenny 11
    show player 12
    player_name "Что? Нет!"
    show player 5
    show jenny 12
    jen "Почему нет? Она уродина?"
    show jenny 11
    show player 12
    player_name "Нет, она великолепна, но полнейшая сука!"
    show player 5
    show jenny 12
    jen "Хмм, она мне уже нравится."
    show jenny 11
    player_name "..."
    show player 12
    player_name "Ну так что, ты ей поможешь?"
    show player 5
    show jenny 12
    jen "$500."
    show jenny 11
    show player 10
    player_name "Что?! Ты с ума сошла?"
    show player 5
    show jenny 9
    jen "Такова цена."
    jen "Плати или вали."
    show jenny 9b
    show player 12
    player_name "Почему ты не можешь просто помочь мне?"
    show player 5
    show jenny 12
    jen "Хахаха, неплохая попытка, {b}[firstname]{/b}!"
    show jenny 13 with dissolve
    jen "$500."
    show jenny 18 with dissolve
    show player 12
    player_name "*Пфф* Ладно!"
    player_name "Вернусь, когда будут деньги..."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_jenny_spying:
    $ persistent.cookie_jar["Roxxy"]["gallery"]["02_unlocked"] = True
    $ suffix = ""
    if M_roxxy.get("roxxy trailer sex"):
        $ suffix = "_sex"
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_pre{}".format(suffix))
    if M_jenny.is_set("seen MCs penis"):
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis{}".format(suffix))
    else:
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis{}".format(suffix))
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_after")
    $ del suffix
    $ renpy.end_replay()
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre:
    scene jennybedroom_peek_c
    show jenny 168 at Position (xpos=638,ypos=762)
    show roxxy 36 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Ещё раз спасибо за то, что одолжила мне униформу."
    show roxxy 35
    show jenny 169
    jen "Без проблем!"
    jen "Она всё равно мне уже мала."
    jen "Черт, да всё эта школьная униформа вообще очень плохо сидит  на теле..."
    show jenny 168
    show roxxy 37
    rox "Хаха, точно."
    show roxxy 36
    rox "Такое ощущение, что твои сиськи в любой момент могут выскочить..."
    show roxxy 35
    show jenny 170
    jen "Хехе!"
    show jenny 169
    jen "... Об этом я и говорю! Судьи точно дают дополнительные очки за сексуальность."
    jen "Поэтому я никогда не носила лифчик на соревнованиях."
    show jenny 168
    show roxxy 36
    rox "Д-да, я об этом и не задумывалась."
    rox "Да ты просто гений!"
    show roxxy 35
    show jenny 169
    jen "Скажи мне что-то, чего я не знаю..."
    jen "Эти девочки подарили мне три победы подряд на чемпионате штата!"
    show jenny 168
    show roxxy 36
    rox "... Они и правда хороши..."
    show roxxy 38
    show jenny 169
    jen "Спасибо!"
    jen "Твои тоже."
    show jenny 168
    show roxxy 36
    rox "Да, но они не такие большие, как у тебя..."
    show roxxy 38
    show jenny 169
    jen "Ммм, может быть, но я уверена, что твои более упругие."
    show jenny 168
    show roxxy 37
    rox "Хехе, возможно..."
    show roxxy 35
    show jenny 169
    jen "Дай-ка мне на них посмотреть."
    hide roxxy
    hide roxxy_outfit
    show jenny 171 at center
    with dissolve
    rox "Воу! Что ты-{p=1}{nw}"
    show jenny 171b with dissolve
    pause .1
    show jenny 171c with dissolve
    pause .1
    show roxxy 34b at Position (xpos=317,ypos=768)
    show jenny 169 at Position (xpos=638,ypos=762)
    with dissolve
    jen "Спокойно!"
    jen "Тут ведь только мы."
    show jenny 168
    rox "..."
    show roxxy 34
    rox "Я-я не знаю..."
    show roxxy 34b
    show jenny 169
    jen "Смотри."
    show jenny 172 with dissolve
    pause
    show jenny 173 with dissolve
    jen "Видишь, нечего смущаться!"
    show jenny 179
    show roxxy 40 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Ну да, наверное..."
    hide roxxy
    hide roxxy_outfit
    show jenny 175 at center
    rox "!!!" with hpunch
    show jenny 174
    jen "Я была права, они и правда упругие..."
    jen "Я даже немного завидую!"
    show jenny 176
    rox "... Спасибо."
    show jenny 174
    jen "У тебя очень милые соски!"
    show jenny 175
    rox "..."
    show jenny 174
    jen "Оуу, она смущена!"
    show jenny 176
    rox "Я не-"
    show jenny 174
    jen "Восхитительно!"
    jen "Хочешь потрогать мои?"
    show jenny 176
    rox "Хочешь, чтобы я-"
    show jenny 177
    rox "!!!" with hpunch
    jen "Видишь, ничего ужасного..."
    show jenny 178
    rox "У тебя такая мягкая кожа..."
    show jenny 177
    jen "Приятно, правда?"
    jen "Это благодаря особому лосьону. Я дам тебе попробывать!"
    show jenny 178
    rox "Спасибо, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=352,ypos=768)
    show jenny 181 at Position (xpos=638,ypos=762)
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Черт возми, милая! У тебя прекрасное тело!"
    show jenny 179
    show roxxy 40
    rox "Думаешь, судьи заметят?"
    show roxxy 39
    show jenny 180
    jen "Обязательно!"
    jen "Я понимаю, почему этот задрот так тебя хочет."
    show jenny 179
    show roxxy 40
    rox "Не могу поверить, что вы живете вместе!"
    rox "Ты просто замечательная, а он такой придурок!"
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis:
    show jenny 180
    jen "Он не такой уж и плохой..."
    jen "Иногда он довольно полезен."
    show jenny 179
    show roxxy 40
    rox "... Да, он и правда помог мне недавно."
    show roxxy 39
    show jenny 180
    jen "Кстати, только между нами..."
    jen "У него как у коня!"
    show jenny 179
    show roxxy 40
    rox "Серьезно? Ты видела его член?"
    show roxxy 39
    show jenny 180
    jen "Ох, да, было пару раз."
    jen "Мы всё же живем вместе."
    show jenny 179
    show roxxy 40
    rox "И правда..."
    rox "Так он, большой, да?"
    show roxxy 39
    show jenny 181
    jen "Огромный!"
    show jenny 179
    show roxxy 42
    rox "Интересно."
    show roxxy 39
    show jenny 180
    jen "А у твоего парня большой?"
    show jenny 179
    show roxxy 40
    rox "У {b}Дектера{/b}?"
    show roxxy 42
    rox "Пфф."
    show roxxy 43 with dissolve
    show jenny 181
    jen "Хахаха!"
    show jenny 180
    show roxxy 39 with dissolve
    jen "Маленький, да? Это плохо."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Ну, да ладно... Хочешь выучить несколько движений?"
    show jenny 179
    show roxxy 37
    rox "Ещё как!"
    show roxxy 39
    show jenny 180
    jen "Отлично, сделаем это!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis:
    show jenny 180
    jen "Странно, правда?!"
    jen "Я говорю всем, что он просто прислуга..."
    show jenny 179
    show roxxy 37
    rox "Хаха!"
    show roxxy 40
    rox "Да, мой парень всё время надерает ему зад."
    show roxxy 39
    show jenny 180
    jen "У тебя есть парень?"
    show jenny 179
    show roxxy 40
    rox "Ну, типа того..."
    rox "Скажем так, он думает, что он мой парень."
    show roxxy 39
    show jenny 180
    jen "Мне нравится твой стиль, {b}Рокси{/b}!"
    show jenny 179
    show roxxy 40
    rox "Хехе, спасибо!"
    show roxxy 39
    show jenny 180
    jen "У него большой?"
    show jenny 179
    show roxxy 40
    rox "Что ты имеешь ввиду?"
    show roxxy 39
    show jenny 180
    jen "Ну знаешь, там на юге..."
    jen "Он большой?"
    show jenny 179
    show roxxy 42
    rox "Пффф..."
    show roxxy 43 with dissolve
    show jenny 180
    jen "Маленький!?"
    show jenny 179
    show roxxy 40 with dissolve
    rox "Просто крохотный."
    show roxxy 39
    show jenny 181
    jen "Хахаха!"
    show jenny 179
    show roxxy 40
    rox "Да, он у меня не для секса."
    show roxxy 39
    show jenny 180
    jen "Да я и не подумала бы..."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Ну, да лдно... Хочешь выучить несколько движений?"
    show jenny 179
    show roxxy 37
    rox "А то!"
    show roxxy 39
    show jenny 180
    jen "Отлично, тогда сделаем это!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre_sex:
    scene jennybedroom_peek_c
    show jenny 168 at Position (xpos=638,ypos=762)
    show roxxy 36 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Ещё раз спасибо за то, что одолжила мне униформу."
    show roxxy 35
    show jenny 169
    jen "Без проблем!"
    jen "Она всё равно мне уже мала."
    jen "Черт, да всё эта школьная униформа вообще очень плохо сидит  на теле..."
    show jenny 168
    show roxxy 37
    rox "Хаха, точно"
    show roxxy 36
    rox "Такое ощущение, что твои сиськи в любой момент могут выскочить..."
    show roxxy 35
    show jenny 170
    jen "Хехе!"
    show jenny 169
    jen "... Об этом я и говорю! Судьи точно дают дополнительные очки за сексуальность."
    jen "Поэтому я никогда не носила лифчик на соревнованиях."
    show jenny 168
    show roxxy 36
    rox "Д-да, я об этом и не задумывалась."
    rox "Да ты просто гений!"
    show roxxy 35
    show jenny 169
    jen "Скажи мне что-то, что я не знаю..."
    jen "Эти девочки подарили мне три победы подряд на чемпионате штата!"
    show jenny 168
    show roxxy 36
    jen "Скажи мне что-то, чего я не знаю..."
    jen "Эти девочки подарили мне три победы подряд на чемпионате штата!"
    show jenny 168
    show roxxy 36
    rox "... Они и правда хороши..."
    show roxxy 38
    show jenny 169
    jen "Спасибо!"
    jen "Твои тоже."
    show jenny 168
    show roxxy 36
    rox "Да, но они не такие большие, как у тебя..."
    show roxxy 38
    show jenny 169
    jen "Ммм, может и так, но твои явно более упругие."
    show jenny 168
    show roxxy 37
    rox "Хехе, может..."
    show roxxy 35
    show jenny 169
    jen "Дай-ка мне на них взгялнуть."
    hide roxxy
    hide roxxy_outfit
    show jenny 171 at center
    with dissolve
    rox "Воу, что ты-{p=1}{nw}"
    show jenny 171b with dissolve
    pause .1
    show jenny 171c with dissolve
    pause .1
    show roxxy 34b at Position (xpos=317,ypos=768)
    show jenny 169 at Position (xpos=638,ypos=762)
    with dissolve
    jen "Спокойно!"
    jen "Здесь только мы вдвоем."
    show jenny 168
    rox "..."
    show roxxy 34
    rox "Я-я не знаю..."
    show roxxy 34b
    show jenny 169
    jen "Смотри."
    show jenny 172 with dissolve
    pause
    show jenny 173 with dissolve
    jen "Видишь, вообще нечего стесняться!"
    show jenny 179
    show roxxy 40 at Position (xpos=352,ypos=768)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Да, наверное..."
    hide roxxy
    hide roxxy_outfit
    show jenny 175 at center
    rox "!!!" with hpunch
    show jenny 174
    jen "Я была права, они более упругие..."
    jen "Я даже немного завидую!"
    show jenny 176
    rox "... Спасибо."
    show jenny 174
    jen "У тебя очень милые соски!"
    show jenny 175
    rox "..."
    show jenny 174
    jen "Оуу, она смущена!"
    show jenny 176
    rox "Я не-"
    show jenny 174
    jen "Просто восхитительно!"
    jen "Хочешь потрогать мои?"
    show jenny 176
    rox "Хочешь, чтобы я-"
    show jenny 177
    rox "!!!" with hpunch
    jen "Видишь, ничего ужасного..."
    show jenny 178
    rox "У тебя такая мягкая кожа..."
    show jenny 177
    jen "Приятно, правда?"
    jen "Это благодаря особому лосьону. Я дам тебе попробывать!"
    show jenny 178
    rox "Спасибо, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=352,ypos=768)
    show jenny 181 at Position (xpos=638,ypos=762)
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Боже, милая! У тебя потрясное тело!"
    show jenny 179
    show roxxy 40
    rox "Думаешь, судьи заметят?"
    show roxxy 39
    show jenny 180
    jen "Обязательно!"
    jen "Не могу поверить, что {b}[firstname]{/b} смог сделать это с такой как ты!"
    show jenny 179
    show roxxy 40
    rox "Хехе, ну я заставила его попотеть ради этого."
    rox "Он очень упорный парень..."
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis_sex:
    show jenny 180
    jen "Да, иногда он и правда очень упрямый..."
    jen "Он достаточно находчивый, отдаю ему должное."
    show jenny 179
    show roxxy 40
    rox "К тому же у него огромный член!"
    show roxxy 39
    show jenny 180
    jen "Невероятно просто, да?!"
    jen "Да он просто конь!"
    show jenny 179
    show roxxy 40
    rox "Воу, подожди... Хочешь сказать, что ты его видела?"
    show roxxy 39
    show jenny 180
    jen "Ох, да, было пару раз."
    jen "Это почти неизбежно. Мы ведь живем вместе."
    show jenny 179
    show roxxy 40
    rox "Да, я понимаю."
    rox "Наверное сложно жить вместе с парнем..."
    show roxxy 39
    show jenny 181
    jen "Хехе, не знаю. У всего есть свои плюсы."
    show jenny 179
    rox "..."
    show jenny 180
    jen "У твоего бывшего был большой?"
    show jenny 179
    show roxxy 40
    rox "У {b}Декстера{/b}?"
    show roxxy 42
    rox "Пфф."
    show roxxy 43 with dissolve
    show jenny 181
    jen "Хахаха!"
    show jenny 180
    show roxxy 39 with dissolve
    jen "Маленький, да? Это плохо."
    show roxxy 35e
    show jenny 179
    rox "Да уж, к тому же он просто придурок."
    show jenny 180
    show roxxy 39
    jen "Ну, да ладно... Хочешь выучить пару движений?"
    show jenny 179
    show roxxy 37
    rox "А то!"
    show roxxy 39
    show jenny 180
    jen "Отлично, тогда начнем!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis_sex:
    show jenny 180
    jen "Вряд ли ему хватит этого упорства, {b}Рокси{/b}!"
    jen "Ему бы пришлось целовать мои ноги и ползать как собачке, прежде чем я пущу его в ко мне в трусики..."
    show jenny 179
    show roxxy 37
    rox "Хахаха! А ты та ещё сучка, {b}[jen_name]{/b}!"
    show roxxy 40
    rox "Ему повезло, что тебе это не интересно, верно ведь?"
    rox "Хотя, он вроде как пытается..."
    show roxxy 39
    show jenny 180
    jen "... Да, повезло ему..."
    jen "... Ну, он хотя бы хорош?"
    show jenny 179
    show roxxy 40
    rox "Что ты имеешь ввиду? Типа, в постели?"
    jen "Ага."
    rox "Он просто великолепен!"
    show roxxy 39
    show jenny 180
    jen "Великолепен? Ты шутишь!."
    show jenny 179
    show roxxy 40
    rox "Нет, я абсолютно серьезно!"
    rox "Он как будто савант или типа того..."
    rox "... И этот его массивный член!"
    show roxxy 39
    show jenny 180
    jen "Ха? В каком смысле массивный?"
    show jenny 179 with None
    show roxxy 43b
    hide roxxy_outfit
    with dissolve
    rox "..."
    show roxxy 39
    show roxxy_outfit cheer 41d
    with dissolve
    show jenny 180
    jen "Ты шутишь!"
    show jenny 179
    show roxxy 42
    rox "Даже не чуть-чуть."
    show roxxy 43 with dissolve
    show jenny 180
    jen "Боже мой..."
    show jenny 179
    show roxxy 40 with dissolve
    rox "Это просто потрясно!"
    show roxxy 39
    show jenny 181
    jen "Хахаха!"
    show jenny 179
    show roxxy 40
    rox "Клянусь тебе, он будто машина для оргазмов!"
    show roxxy 39
    show jenny 180
    jen "Интересно..."
    show jenny 179
    rox "..."
    show jenny 180
    jen "Ну, да ладно... Хочешь выучить пару движений?"
    show jenny 179
    show roxxy 37
    rox "А то!"
    show roxxy 39
    show jenny 180
    jen "Отлично, сделаем это!"
    return


label jennys_bedroom_bissette_roxxy_jenny_spying_after:
    scene black with fade
    scene hallway
    show player 33 with dissolve
    player_name "( Вау!!! )"
    show player 17
    player_name "( Может это была не такая уж и плохая идея! )"
    hide player with dissolve
    return

label jennybedroom_talk_after_cuddle:
    show player 2
    player_name "Просто хотел узнать, как у тебя дела."
    show player 13
    show jenny 10 at Position(xpos = 937)
    jen "..."
    show jenny 9
    jen "Обычно ты не спрашиваешь у меня что-то подобное..."
    jen "Почему тебя внезапно это начало волновать?"
    show player 2
    show jenny 9b
    player_name "Просто, мне кажется, что мы должны быть немного ближе."
    show player 11
    show jenny 7 at right
    jen "Послушай меня, идиот."
    jen "Со мной всё в порядке, и мы НЕ друзья."
    show jenny 8
    show player 5
    player_name "..."
    show jenny 9 at Position(xpos = 937)
    jen "Хочешь со мной о чем-то ещё поговорить, или я могу просто выпнуть тебя из моей комнаты?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
