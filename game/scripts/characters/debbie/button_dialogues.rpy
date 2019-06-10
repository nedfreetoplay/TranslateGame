label debbie_dialogue_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show player f_normal
    show debbie f_normal_talk
    deb "So, what did she say?"
    show debbie f_normal
    show player f_worried
    player_name "Hmm?"
    show player f_worried_talk
    player_name "Oh, I haven't asked her yet..."
    show player f_normal
    show debbie f_normal_talk
    deb "Heh, what are you waiting for silly?"
    show debbie f_normal
    show player f_normal_talk
    player_name "I'll go right now."
    show player f_normal
    show debbie f_normal_talk
    deb "Thanks, sweetie."
    show debbie f_normal
    show player f_normal_talk
    player_name "No problem."
    hide debbie
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, I think {b}[jen_name]{/b} is {b}lounging out by the pool...{/b} )"
    hide player with dissolve
    return

label debbie_dialogue_mom_relaxing:
    scene expression player.location.background_closeup
    show player 1 at left with dissolve
	show debbie 2 at right with dissolve
    deb "Привет, милый! Разве ты не должен идти?"
    show player 2 at left
    show debbie 1 at right
    player_name "Я как раз собирался уходить."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    scene expression player.location.background_closeup with None
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Милый, что ты там делаешь?"
    show debbie 50j
    player_name "Ммм, ничегооо..."
    show debbie 50k
    deb "Милый!"
    deb "Что если {b}[jen_name]{/b} войдет?"
    deb "Она офигеет!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    player_name "... и к тому же..."
    player_name "... Это займет всего минутку."
    show debbie 50k
    deb "Ты такой плохой мальч-"
    deb "Ааа!"
    deb "... Хорошо! Только побыстрее!"
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 48c with dissolve
    deb "Ладно, ладно! Мы должны остановиться!!"
    show debbie 50k
    deb "Ещё немного и мне придется переодеть мои трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я ещё могу тебе помочь?"
    show debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Ты нашел мой {b}лосьон{/b} в моем {b}комоде в спальне{/b}?"
    show debbie 1
    show player 10
    player_name "Нет ещё."
    show player 5
    show debbie 2
    deb "Ну, так чего же ты ждешь?"
    return

label debbie_dialogue_mom_car_condition:
    show player 10 at left
    show debbie 61 at right
    with dissolve
    player_name "Я выяснил, почему машина не заводится..."
    show player 5
    show debbie 63
    deb "Да?! Ты уже все исправил?"
    show debbie 61
    pause
    show player 25
    player_name "Там все плохо, {b}[deb_name]{/b}... я не думаю, что смогу исправить поломку."
    show player 5
    show debbie 39
    deb "Ох."
    show debbie 38
    show player 10
    player_name "На самом деле, я думаю, нам придется заменить весь двигатель. Это действительно плохо!"
    player_name "Это очень дорого..."
    show player 5
    pause
    show debbie 60
    deb "А что насчет страховки? Мы должны пойти и посмотреть, что {b}в автосалоне{/b} могут сделать для нас."
    deb "Надеюсь, она покроет ремонт, в противном случае..."
    show debbie 39
    deb "... Мы останемся без машины на некоторое время."
    show debbie 38
    pause
    show player 10
    player_name "Я уверен, что все будет хорошо, {b}[deb_name]{/b}. Я пойду и поговорю в {b}автосалоне{/b}."
    show player 5
    pause
    show player 14
    player_name "Я приведу её в порядок."
    player_name "Тем или иным способом."
    show debbie 61
    show player 13
    pause
    show debbie 62
    deb "Я так рада, что ты рядом, милый!"
    deb "Спасибо!"
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    scene expression player.location.background_blur
    show debbieobj 2 at Position(xpos=590,ypos=768)
	return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    scene expression player.location.background_closeup with None
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 48 at Position(xpos=660,ypos=768) with dissolve
    deb "( !!! )"
    show debbie 48c
    deb "Милый?"
    deb "Что ты там делаешь?"
    show debbie 50j
    player_name "Ммм, ничегооо..."
    show debbie 50k
    deb "Ааа..."
    deb "Что если {b}[jen_name]{/b} войдет?"
    deb "Она офигеет!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show debbie 50j with dissolve
    player_name "Тебе приятно?"
    show debbie 50k
    deb "Конечно приятно..."
    deb "Ммм, ты делаешь меня такой мокрой!"
    deb "Ааа!"
    show debbie 50j
    player_name "Что, если я сниму эти трусики и трахну тебя прямо здесь?"
    show debbie 50k
    deb "Оо боже..."
    deb "Ладно, давай! Возьмите меня прямо здесь! Только побыстрее, милый!"
    show debbie 50j
    player_name "Ммм, тебе лучше держаться за этот шкаф покрепче!"
    show debbie 50c with dissolve
    pause
    show debbie 50d with dissolve
    pause
    hide debbie
    show debbie 50e at right
    with dissolve
    pause
    show debbie 50g with dissolve
    deb "Ооо, да!."
    hide debbie
    show debbies 164 at right
    with dissolve
    deb "Аааааа!"
    player_name "Ничего себе, с тебя капает..."
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies at right with dissolve
    deb "Ооо, трахни меня!"
    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
           if not animated:
            show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies
            $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [164,165,166,167,168]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
        $ animcounter += 1
    call screen mom_kitchen_fuck_options

label debbie_kitchen_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            deb "О!!!{p=1}{nw}"
        else:
            deb "АХХХХ!!!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            deb "Ты кончил, да?{p=2}{nw}"
            player_name "Нет пока...{p=2}{nw}"
            deb "Поторопись, милый... Я не думаю... Я могу взять... Гораздо больше!{p=3}{nw}"
    return

label mom_kitchen_fuck_cum:
    call expression game.dialog_select("mom_kitchen_fuck_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["09_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label mom_kitchen_fuck_cum_dialogue:
    player_name "( !!! )"
    player_name "Ох, {b}[deb_name]{/b}!"
    player_name "Я-"
    deb "Шшшшш!"
    show debbies 169 with flash
    player_name "УХХХ!!!"
    hide debbies
    show debbie 50h at right
    with dissolve
    pause
    deb "О, мне нравится, когда ты берешь на себя ответственность!"
    player_name "Ты кончила?"
    deb "О, да!"
    show debbie 50i at right
    show player 434 at left
    with dissolve
    deb "{b}*фуф*{/b}, мои ноги всё ещё дрожат..."
    deb "... Ничего себе как много вышло!"
    pause
    show debbie 61 with dissolve
    show player 10
    player_name "Прости."
    show player 13
    show debbie 62
    deb "Нет, мне это нравится! Внутри меня так хорошо."
    show debbie 61
    show player 14
    player_name "Мне нравится, когда ты так говоришь."
    show player 13
    show debbie 62
    deb "Хе-хе, ну это правда..."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene expression player.location.background_closeup with None
    hide debbieobj
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 50k at Position(xpos=660,ypos=768) with dissolve
    deb "Ну привет тебе, милый..."
    show debbie 50j
    player_name "Привет, {b}[deb_name]{/b}..."
    show debbie 50k
    deb "Будь осторожен..."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 50k with dissolve
    deb "Ладно, ладно! Мы должны остановиться!"
    deb "Ещё немного и мне придется переодеть трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я ещё могу помочь тебе?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene expression player.location.background_closeup with None
    hide debbieobj
    show debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Привет {b}[deb_name]{/b}, есть минутка?"
    show debbie 2
    show player 1
    deb "Что случилось, {b}[firstname]{/b}?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        deb "Вот мой большой мальчуган..."
    elif randomizer() <= 20:
        deb "Привет, милый."
        deb "Что я могу сделать для тебя?"
    elif randomizer() <= 30:
        deb "Авввв..."
        deb "Не здороваешься?"
    elif randomizer() <= 70:
        deb "Надеюсь, ты меня искал."
    elif randomizer() <= 80:
        deb "Что-нибудь нужно, милый?"
        deb "Или я могу сделать что-нибудь для тебя?"
    elif L_home_shower.is_here(M_jenny):
        deb "{b}[jen_name]{/b} в душе."
        deb "На случай, если понадоблюсь на секунду."
    else:
        deb "Я надеялась увидеть тебя сегодня."
    show debbie 1
    show player 14
    if randomizer() <= 50:
        player_name "Привет, {b}[deb_name]{/b}."
    else:
        player_name "Ты сегодня хорошо выглядишь."
    show player 13
    return

label debbie_dialogue_mom_not_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Привет, милый!"
    deb "В школе все хорошо?"
    show player 14 at left
    show debbie 1 at right
    player_name "Да..."
    show player 13 at left
    show debbie 13 at right
    deb "Надеюсь, ты не слишком отстал, из-зи того что произошло?"
    show debbie 14 at right
    show player 14 at left
    player_name "Нет, я наверстаю упущенное."
    show player 13 at left
    show debbie 13 at right
    deb "Просто дай мне знать, если нужна будет моя помощь?"
    show player 21 at left
    show debbie 14 at right
    player_name "Хорошо, {b}[deb_name]{/b}..."
    player_name "Я должен идти."
    show player 13 at left
    show debbie 3 at right
    deb "Не задерживайся допоздна!"
    show debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show debbie 1 at right
    player_name "{b}[deb_name]{/b}, ты знаешь, что случилось с моим {b}отцом{/b}?"
    show player 11
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Ох... Милый, я..."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Пожалуйста, я хочу знать правду!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Прости, милый. У меня нет ничего для тебя."
    deb "Полицейское расследование ничего не дало..."
    deb "На самом деле, насколько я понимаю, дело отложено из-за отсутствия доказательств."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Да, но они ведь что-нибудь найдут, верно? Я имею в виду, что это их работа!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Мы можем только надеяться на это."
    show debbie 59 at Position (xoffset=-28)
    pause
    show debbie 60 at Position (xoffset=-28)
    deb "Милый..."
    deb "... Но твой {b}Отец{/b} не хотел бы, чтобы мы были одержимы этим."
    deb "Я тоже хочу покончить со всем этим..."
    show debbie 63 at Position (xoffset=-28)
    deb "Ты молодой человек и тебе нужно сосредоточиться на своей жизни."
    deb "Сделай это для своего {b}отца{/b}."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Да. Я постараюсь."
    show player 14
    show debbie 61 at Position (xoffset=-28)
    player_name "Спасибо, {b}[deb_name]{/b}."
    show player 1
    show debbie 2 with dissolve
    deb "Тебе ещё что-нибудь нужно?"
    show debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show debbie 1
    show player 10
    player_name "{b}[deb_name]{/b}, расскажи о том разговоре по телефону..."
    show debbie 13
    show player 11
    deb "Я говорила тебе не беспокоиться об этом."
    deb "Все будет в порядке!"
    show debbie 14
    show player 14
    player_name "Хорошо, но что если я захочу тебе помочь?"
    player_name "Что если у меня будет настоящая работа?"
    show player 10
    player_name "Я чувствую некоторую ответственность за весь этот стресс..."
    show debbie 52 at Position (xoffset=1)
    show player 11
    deb "Ты можешь помочь мне, оставаясь в школе!"
    deb "Твой {b}отец{/b} перевернется в могиле, если я позволю тебе работать весь день..."
    deb "Он хотел, чтобы ты получил образование."
    show debbie 51 at Position (xoffset=1)
    show player 10
    player_name "... Но я могу работать после школы и по выходным?"
    show debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    deb "{b}*вздыхая*{/b} Ты такой же упрямый, как твой {b}отец{/b}..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    deb "Хмм..."
    show debbie 63 at Position (xoffset=-28)
    deb "Почему бы тебе не проверить {b}почтовый ящик{/b}?"
    deb "Кажется, я видела там объявления о работе."
    deb "Возможно, одно из них заинтересует тебя?"
    show debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Хорошо, я посмотрю."
    show debbie 62 at Position (xoffset=-28)
    show player 1
    deb "О чем ещё ты хотел поговорить, милый?"
    show debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, я хотел поговорить о том, что сказал тот парень в костюме..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Был ли мой {b}отец{/b} связан с ними?"
    show player 11
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*вздыхая*{/b} Полагаю, я не могу держать тебя в неведении вечно..."
    deb "Твой {b}отец{/b} был хорошим человеком, {b}[firstname]{/b}."
    deb "... но у него была слабость к азартным играм."
    deb "Он всегда говорил мне, что мне не о чем беспокоиться и что у него все под контролем."
    deb "... Но теперь его нет, и, похоже, он о многом мне не расказывал."
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Твой {b}отец{/b} задолжал этим людям много денег, и они всё ещё пытаются их вернуть."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Мы должны рассказать об этом полиции!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "НЕТ! Я боюсь того, что может случиться, если я втяну в это власти!"
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Ты просто заплатишь этим подонкам?!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Я сделал все возможное, но боюсь, что у меня просто нет денег, чтобы покрыть все это, милый."
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*вздыхая*{/b} Может нам с тобой просто исчезнуть и начать всё с начала."
    show player 1
    show debbie 63 at Position (xoffset=-28) with dissolve
    deb "Хех, вот это было бы приключение, не так ли?"
    show debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Я полагаю, да."
    show debbie 2 with dissolve
    show player 1
    deb "Ты еще о чем-нибудь хотел поговорить?"
    show debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Разве в гараже не осталось немного краски?"
    show player 5
    show debbie 13
    deb "Краска? Зачем тебе старая краска?"
    show debbie 1
    show player 10
    player_name "Я хочу сделать... кое-что."
    show player 5
    show debbie 2
    deb "Ох, ну, {b}Диана{/b} сказала что избавится от неё для меня."
    show debbie 1
    show player 12
    player_name "Правда?"
    player_name "Ну, я лучше пойду посмотрю, смогу ли я их забрать у неё, пока она их не выбросила!"
    player_name "Спасибо, {b}[deb_name]{/b}! Пока, {b}[deb_name]{/b}!"
    hide player with dissolve
    show debbie 2
    deb "Пока!"
    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Тебе нужна помощь?"
    show player 5
    show debbie 2
    deb "Ты закончил косить траву?"
    show debbie 1
    show player 10
    player_name "О, точно!"
    player_name "Я займусь этим."
    show player 13
    show debbie 2
    deb "Я была бы очень признательна, милый."
    show debbie 1
    show player 14
    player_name "Без проблем!"
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "( Надо как-то починить {b}раковину в ванной{/b}... )"
    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "С чем ещё тебе помочь?"
    show player 13
    show debbie 2
    return

label debbie_dialogue_help_chores_later:
    deb "Нет. Ничего не надо, милый."
    deb "Может быть позже, если у тебя будет время."
    return

label debbie_dialogue_help_chores_tomorrow:
    deb "Нет. Не сегодня, милый."
    deb "Может быть завтра, если у тебя будет время."
    return

label debbie_dialogue_help_chores_after:
    show debbie 3
    deb "Спасибо что спросил!"
    show debbie 1
    show player 14
    player_name "Не за что, {b}[deb_name]{/b}."
    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "( Я должен проверить {b}машину{/b} раз {b}[deb_name]{/b} попросила меня. )"
    return

label debbie_dialogue_help_fix_car:
    show player 4
    player_name "( Я должен посетить {b}автосалон{/b}. Может они смогут отремонтировать машину {b}[deb_name]{/b}... )"
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Привет, {b}[deb_name]{/b}, я могу чем-нибудь помочь тебе по дому?"
    show player 1
    deb "Хмм..."
    show debbie 2
    deb "Нет, ничего не приходит на ум."
    show debbie 1
    show player 2
    player_name "Дайте мне знать, если что-то будет нужно."
    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Мне нужно втереть ещё немного лосьона в... твои ноги?"
    show player 13
    show debbie 2
    deb "Звучит замечательно, милый."
    deb "Мне бы очень пригодились твои нежные прикосновения."
    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Мне нужно втереть ещё немного лосьона в... твои ноги?"
    show player 5
    show debbie 13
    deb "О... опять? Ну, Я..."
    show debbie 14
    show player 10
    player_name "Тебе не нравиться как я это делаю?"
    show player 5
    show debbie 13
    deb "Ох, нет, милый. Это было... действительно хорошо."
    show debbie 14
    pause
    show debbie 13
    deb "Конечно, думаю, мне не помешал бы перерыв."
    show debbie 1
    show player 14
    player_name "Отлично!"
    show player 13
    show debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    deb "Иди и возьми {b}лосьон из комода в моей спальне{/b}."
    show debbie 1
    show player 14
    player_name "Хорошо!"
    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show debbie 1 at right
    player_name "Помнишь, ты просила меня пойти с тобой по магазинам?"
    show player 1
    show debbie 2
    deb "Да."
    show player 2
    show debbie 1
    player_name "Что ж, я свободен. Ты все ещё хочешь поехать?"
    show player 1
    show debbie 3
    deb "Правда?! Отлично!"
    show debbie 2
    deb "Просто дай мне собраться и встретимся в машине, хорошо?!"
    show debbie 1
    show player 2
    player_name "Хорошо."
    return

label debbie_dialogue_shower_basement:
    show player 2
    show debbie 1
    player_name "Ну эээ.."
    player_name "Я подумал, что мы могли бы... Принять душ вместе, а?"
    show player 13
    show debbie 2
    deb "Сейчас?"
    show debbie 1
    deb "Хмм..."
    show debbie 3
    deb "Думаю, я могу пойти принять душ."
    show debbie 2
    deb "Давай я закончу складывать белье и встретимся в ванной."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Надеюсь, ты ещё не закончил..."
    deb "Я надеюсь, что мы сможем провести здесь немного времени."
    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show debbie 1
    player_name "Привет, {b}[deb_name]{/b}!"
    player_name "Мне было интересно..."
    show player 21
    player_name "Не хочешь принять со мной душ?"
    show player 14
    show debbie 2
    deb "В доме становится довольно жарко..."
    show debbie 3
    deb "Конечно! Душ сейчас, звучит прекрасно."
    show debbie 2
    deb "Дай мне одну минуту. Я присоединюсь к тебе, когда закончу здесь."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Прости, что заставила ждать, милый..."
    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Хочешь присоединиться ко мне в своей комнате?"
    show player 13
    show debbie 3
    deb "Прямо сейчас?"
    show debbie 1
    show player 10
    player_name "Однозначно!"
    show player 5
    show debbie 2
    deb "Хех, хорошо..."
    show player 13
    deb "... только убедись, что {b}[jen_name]{/b} не увидит нас."
    show debbie 1
    show player 14
    player_name "Хорошо."
    show player 13
    show debbie 2
    deb "Хехехе..."
    deb "Ты собираешься меня измотать!"
    show debbie 1
    show player 14
    player_name "Я просто хочу убедиться, что ты хорошо тренируешься!"
    show player 13
    show debbie 3
    deb "Ха Ха Ха."
    show debbie 2
    deb "Тащи свою задницу наверх и раздевайся!"
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_1:
        show debbie 86 at left
        show player 434f at right
        with dissolve
        deb "Простыни очень хорошие и мягкие... Почему бы тебе не полежать со мной..."
        show debbie 84
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show debbie 85
        show player 263 with dissolve
        deb "Непослушный мальчик."
        show debbie 84
        show player 262
        player_name "Что?"
        show player 263
        show debbie 85
        deb "Ты действительно ненасытен."
        show debbie 84
        show player 262
        player_name "Ты можешь просто лежать на спине, а я сделаю все остальное."
        show player 263
        show debbie 86
        deb "Ну и что в этом веселого?"
        show debbie 84
        show player 262
        player_name "Хех, не беспокойся. Я буду делать это весело!"
        show player 263
        show debbie 84
        deb "Ммм, у меня нет никаких сомнений на этот счёт!"
        show debbie 89 with dissolve
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_kitchen:
    show player 14
    player_name "Хочешь присоединиться ко мне в своей комнате?"
    show player 13
    show debbie 2
    deb "Прямо сейчас?"
    deb "Однозначно!"
    deb "Убедись, что {b}[jen_name]{/b} не увидит нас."
    show debbie 1
    show player 14
    player_name "Ага."
    show player 13
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_2:
        show player 434f at right
        show debbie 86 at left
        with dissolve
        deb "Я надеялась, что ты приведешь меня сюда для этого сегодня!"
        show debbie 84
        show player 435f
        player_name "Ты действительно думала об этом?"
        show player 434f
        show debbie 86
        deb "Тебя это удивляет?"
        deb "Я всегда думаю о твоем большом члене..."
        show debbie 84
        show player 435f
        player_name "Хех, я тоже много об этом думаю... Особенно, когда ты носишь свой халат."
        show player 434f
        show debbie 89 with dissolve
        deb "Ты имеешь в виду эту старую штуку?"
        show debbie 90
        show player 435f
        player_name "... О, да."
        show player 434f
        show debbie 89
        deb "Хехе, почему бы тебе не снять эту одежду и не пойти поиграть со мной?"
        show debbie 90
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show player 263
        show debbie 102
        with dissolve
        deb "Мммм..."
        show debbie 103
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_after:
    deb "Иди и возьми меня, большой мальчик!"
    hide player
    show debbie 104 at left
    with dissolve
    pause
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_sex_in_my_room:
    show player 2
    player_name "Хочешь переночевать в моей комнате?"
    show player 1
    show debbie 2
    deb "Ммм, с удовольствием, милый."
    show player 2
    show debbie 1
    player_name "Отлично! Тогда я буду ждать тебя наверху."
    show player 1
    show debbie 2
    deb "Не могу дождаться!"
    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, не могла бы ты пройти со мной на секунду?"
    show player 13
    show debbie 2
    deb "Хмм?"
    show debbie 1
    show player 14
    player_name "Просто иди за мной."
    show player 13
    show debbie 2
    deb "Хе-хе, что ты задумал?"
    show debbie 2
    deb "..."
    show debbie 3
    deb "Ты что-то задумал?!"
    show debbie 2
    deb "Хехе!"
    deb "Это сюрприз?"
    deb "... Я люблю сюрпризы!"
    show debbie 1
    show player 14
    player_name "Хех, Я знаю что ты любишь."
    player_name "Хотя я бы не назвал это сюрпризом..."
    show player 13
    show debbie 3
    deb "Хехе!"
    show debbie 2
    deb "Тогда, как бы ты это назвал?"
    show debbie 1
    deb "..."
    show debbie 2
    deb "Это что-то неприличное?"
    deb "..."
    show debbie 1
    show player 14
    player_name "Мооооожет быть."
    show debbie 2
    deb "Хехе, Хорошо. Давай быстрее пока {b}[jen_name]{/b} наверху."
    hide player
    hide debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "Я подумал, Может, нам стоит посмотреть фильм сегодня вечером. Интересно?"
    show player 1
    show debbie 2
    deb "Ммм, вечерний сеанс, хух?"
    deb "Звучит как отличная идея, Милый!"
    show player 2
    show debbie 1
    player_name "Потрясающе!"
    player_name "Тогда увидимся {b}вечером{/b} в {b}гостиной{/b}?"
    show player 1
    show debbie 2
    deb "Не могу дождаться..."
    return

label debbie_dialogue_laundry_sex_basement:
    scene home_basement
    show debbie 122 at right
    show player 14 at left
    player_name "Ты почти закончила со стиркой?"
    show player 13
    show debbie 123
    deb "Почти. Я просто должна загрузить эти вещи в сушилку."
    deb "Почему? Что случилось?"
    show player 14
    show debbie 122
    player_name "Я просто подумал, что ты захочешь прокатиться?"
    show player 13
    show debbie 123
    deb "Ох, мы почувствуем себя немного озорными?"
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show debbie 123
    deb "Хехе, Будем считать что, да!"
    show player 263f with dissolve
    deb "..."
    show debbie 121
    show player 432
    player_name "Абсолютно!"
    show player 431
    pause
    show debbie 123
    deb "Снимай эту одежду и положи её в стиралку!"
    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show debbie 108
    deb "Моя очередь..."
    deb "Мммм, Я всё утро этого ждала!"
    show debbie 109
    pause
    show debbie 110
    pause
    show debbie 111
    pause
    show debbie 112
    pause
    show debbie 113
    pause
    show debbie 114
    pause
    player_name "Ты выглядишь прекрасно, {b}[deb_name]{/b}."
    show debbie 115
    deb "Просто сядь и расслабься, милый."
    deb "Я обо всем позабочусь..."
    deb "... Просто убедись, что ты держишься за меня."
    hide player
    hide debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655)
    pause
    show debbies 126f with dissolve
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
    return

label debbie_dialogue_laundry_sex_basement_random_true:
    deb "Ммммм..."
    deb "Я с трудом могу поместить тебя целиком."
    return

label debbie_dialogue_laundry_sex_basement_random_false:
    deb "Ахх..."
    player_name "( !!! )"
    player_name "Ты такая теплая..."
    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Привет, {b}[deb_name]{/b}... Ты хочешь потусоваться в подвале для некторых быстрых утех?"
    show player 13
    show debbie 2
    deb "Ох?"
    show debbie 1
    show player 14
    player_name "Я подумал, что мы можем включить сушилку и ты могла бы быть такой же громкой как ты и хотела..."
    show player 13
    show debbie 3
    deb "Ха ха."
    show debbie 2
    deb "Это довольно шаловливо, милый."
    show debbie 1
    pause
    show debbie 2
    deb "Хмм... ладно!"
    deb "У меня есть немного свободного времени и мне бы не помешала некоторая... внимательность."
    show debbie 1
    show player 14
    player_name "Правда?"
    show player 13
    show debbie 2
    deb "Конечно!"
    deb "Давай встретимся там в низу, через минуту..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show debbie 1 at right
    player_name "Приветик... эмм, {b}[deb_name]{/b}?"
    show player 5
    show debbie 2
    deb "Да, милый?"
    show player 10
    show debbie 1
    player_name "Можно тебя спросить кое о чём?"
    show player 5
    show debbie 3
    deb "Разумеется! Ты можешь спрашивать меня о чем угодно."
    show player 10
    show debbie 1
    player_name "Ну, это немного... смущает."
    show player 5
    show debbie 13
    deb "Ох? Что ж всё в порядке, {b}[firstname]{/b}."
    deb "Нет нужды смущаться."
    deb "Не со мной..."
    show debbie 14
    show player 10
    player_name "Хорошо."
    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show debbie 14 at right
    player_name "Я хотел спросить, если бы ты смогла..."
    player_name "Ну..."
    show player 5
    show debbie 13
    deb "Если бы я смогла что, дорогой?"
    show player 10
    show debbie 14
    player_name "Эээ... Помнишь тот день в торговом центре?"
    show player 5
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "... Д-да?"
    show player 10
    show debbie 14b
    player_name "Ну... Я надеялся, что ты сможешь научить меня большему, ты знаешь, о поцелуях?"
    show player 5
    show debbie 13
    deb "Что?!"
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "Это было ошибкой, сладкий. Я не должна была..."
    deb "В любом случае, чему, ты надеешься, я смогу тебя научить?"
    show player 10
    show debbie 14b
    player_name "Ты знаешь, типа, как это делать."
    player_name "Я подумал, может быть, ты могла бы показать мне, что нравятся женщинам?"
    show player 5
    show debbie 13
    deb "Хмм, что ж я бузусловно могла бы рассказать тебе, что женщинам нравятся."
    deb "... Но я не думаю, что показывать на тебе это хорошая идея. Это было бы немного неуместно..."
    show debbie 14b
    return

label debbie_dialogue_kiss_teach_stat_fail:
    show player 10 at left
    show debbie 14b at right
    player_name "[chr_warn]Ты уверена?"
    player_name "[chr_warn]Я бы очень хотел потренироваться с тобой."
    show player 5
    deb "..."
    show debbie 13
    deb "Это просто не очень хорошая идея, милый."
    show player 10
    show debbie 14b
    player_name "[chr_warn]Ох... Хорошо."
    show player 5
    show debbie 13
    deb "Прости, Милый."
    show player 10
    show debbie 14b
    player_name "[chr_warn]Все хорошо, {b}[deb_name]{/b}."
    return

label debbie_dialogue_kiss_leave:
    show player 10 at left
    show debbie 14 at right
    player_name "... На самом деле."
    player_name "Неважно."
    show debbie 13
    show player 5
    deb "Ты уверен?"
    deb "Ты всегда можешь поговорить со мной, {b}[firstname]{/b}."
    show player 10
    show debbie 14
    player_name "Да, это пустяки."
    player_name "Прости, что досадил тебе."
    show player 5
    show debbie 13
    deb "Ты никогда не досаждаешь мне, милый."
    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show debbie 1 at right
    player_name "Как ты думаешь, мы могли бы практиковать снова?"
    player_name "Ты знаешь... в поцелуях?"
    show player 1
    show debbie 13
    deb "Ещё раз?"
    show player 2
    show debbie 14b
    player_name "Д-да. Я думаю у меня уже получается лучше!"
    show player 1
    show debbie 13
    deb "... Ладно."
    deb "Но только немного!"
    show player 2
    show debbie 14
    player_name "Хорошо, конечно."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    deb "Ммм..."
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show debbie 77
    deb "Вау... я бы сказала что у тебя определенно стало получаться."
    deb "...Ты уже и так был хорош, чтобы начинать!"
    show player 232
    show debbie 76
    player_name "Спасибо {b}[deb_name]{/b}!"
    show player 231
    show debbie 74
    pause
    show player 230
    pause
    show player 232
    show debbie 76
    player_name "Извини за то... Ты знаешь."
    show player 231
    show debbie 75
    deb "Хехе, все в порядке, дорогой."
    deb "Это совершенно естественно."
    deb "У девочек в этом городе будут большие неприятности."
    show player 232
    show debbie 72
    player_name "Хах, ещё бы!"
    show player 231
    show debbie 73
    deb "Покажи им, милый!"
    show player 232
    show debbie 72
    player_name "Да, мэм!"
    return

label debbie_dialogue_leave:
    show player 2
    player_name "На самом деле, неважно, увидимся позже, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
