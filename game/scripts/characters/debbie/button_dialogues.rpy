label debbie_dialogue_mom_relaxing:
    scene location_home_kitchen_closeup
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Привет, милый! Разве ты не должен идти?"
    show player 2 at left
    show debbie 1 at right
    player_name "Да. Я был в пути."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    scene location_home_kitchen_closeup
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
    deb "Что мы будем делать, если {b}[jen_name]{/b} войдёт?"
    deb "Она будет неприятно удивлена!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    player_name "... И, кроме того..."
    player_name "... Это займет всего минуту."
    show debbie 50k
    deb "Ты такой плохой паре-"
    deb "Ахх!"
    deb "... Все в порядке! Только побыстрее!"
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 48c with dissolve
    deb "Ладно, ладно! Мы должны остановиться!"
    show debbie 50k
    deb "На этом всё, и мне придется сменить трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я еще могу тебе помочь?"
    show debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Ты нашёл мой {b}лосьон{/b} в {b}комоде спальни{/b}?"
    show debbie 1
    show player 10
    player_name "Нет, еще нет."
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
    deb "Да?! Ты уже все исправила?"
    show debbie 61
    pause
    show player 25
    player_name "Это довольно ужастно, {b}[deb_name]{/b}... Не думаю, что смогу это исправить."
    show player 5
    show debbie 39
    deb "Ох."
    show debbie 38
    show player 10
    player_name "На самом деле, я думаю, нам придется заменить весь двигатель. На этом можно действительно разориться!"
    player_name "Это будет дорого..."
    show player 5
    pause
    show debbie 60
    deb "А что насчет страховки? Мы должны пойти и посмотреть, что {b}автосалон{/b} может сделать для нас."
    deb "Надеюсь, они покроют ремонт, в противном случае..."
    show debbie 39
    deb "... Мы останемся без машины на некоторое время."
    show debbie 38
    pause
    show player 10
    player_name "Уверен, все будет хорошо., {b}[deb_name]{/b}. Я пойду и поговорю с {b}дилерами авто{/b}."
    show player 5
    pause
    show player 14
    player_name "Я все исправлю."
    player_name "Так или иначе."
    show debbie 61
    show player 13
    pause
    show debbie 62
    deb "Я так рада, что ты рядом, дорогой!"
    deb "Спасибо тебе!"
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    show debbieobj 2 at Position(xpos=590,ypos=768)
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    scene location_home_kitchen_closeup
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
    deb "Ахх..."
    deb "Что мы будем делать, если {b}[jen_name]{/b} войдёт?"
    deb "Она будет неприятно удивлена!"
    show debbie 50j
    player_name "Не волнуйся, она наверху, в своей комнате."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show debbie 50j with dissolve
    player_name "Ты хорошо себя чувствуешь?"
    show debbie 50k
    deb "Конечно..."
    deb "Ммм, ты делаешь меня такой мокрой.!"
    deb "Ахх!"
    show debbie 50j
    player_name "Что, если я стянул эти трусики и трахнул тебя прямо здесь?"
    show debbie 50k
    deb "Оо боже..."
    deb "Ладно, давай! Возьмите меня прямо здесь! Только побыстрее, дорогой!"
    show debbie 50j
    player_name "Ммм, держись крепче за этот шкаф!"
    show debbie 50c with dissolve
    pause
    show debbie 50d with dissolve
    pause
    hide debbie
    show debbie 50e at right
    with dissolve
    pause
    show debbie 50g with dissolve
    deb "Ох да!."
    hide debbie
    show debbies 164 at right
    with dissolve
    deb "Аххх!"
    player_name "Вау, с тебя капает..."
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies at right with dissolve
    deb "Ох, трахни меня!"
    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("debbies", [164,165,166,167,168], M_mom) as debbies
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
            deb "ОХ!!!{p=1}{nw}"
        else:
            deb "АХХХ!!!{p=1}{nw}"

    elif animcounter == 3:
        if randomizer() <= 50:
            deb "Ты кончил?{p=2}{nw}"
            player_name "Еще нет...{p=2}{nw}"
            deb "Поторопись, милый... Я не думаю, что... Я могу взять... Куда более!{p=3}{nw}"
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
    deb "Шшшш!"
    show debbies 169 with flash
    player_name "Ухх!!!"
    hide debbies
    show debbie 50h at right
    with dissolve
    pause
    deb "Обожаю, когда ты за главного!"
    player_name "Ты кончил?"
    deb "Ох, да!"
    show debbie 50i at right
    show player 434 at left
    with dissolve
    deb "{b}*Фуф*{/b}, мои ноги все еще дрожат..."
    deb "... Ничего себе, вы тебе много!"
    pause
    show debbie 61 with dissolve
    show player 10
    player_name "Прости."
    show player 13
    show debbie 62
    deb "Нет, мне это нравится! Внутри меня так хорошо."
    show debbie 61
    show player 14
    player_name "Мне нравится, когда ты так говоришь"
    show player 13
    show debbie 62
    deb "Хе-хе, ну это правда..."
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene location_home_kitchen_closeup
    hide debbieobj
    show debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show debbie 50k at Position(xpos=660,ypos=768) with dissolve
    deb "Ну привет тебе, дорогой...."
    show debbie 50j
    player_name "Хей, {b}[deb_name]{/b}..."
    show debbie 50k
    deb "Просто будь осторожен..."
    show debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show debbie 50k with dissolve
    deb "Ладно, ладно! Мы должны остановиться!"
    deb "На этом всё, и мне придется сменить трусики!"
    show player 1 at left
    show debbie 52 at right
    with dissolve
    deb "Чем я еще могу тебе помочь?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene location_home_kitchen_closeup
    hide debbieobj
    show debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Привет {b}[deb_name]{/b}, есть минутка?"
    show debbie 2
    show player 1
    deb "Что-то нужно, {b}[firstname]{/b}?"
    show debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        deb "Вот мой большой человек..."
    elif randomizer() <= 20:
        deb "Привет, дорогая."
        deb "Что я могу для тебя сделать?"
    elif randomizer() <= 30:
        deb "Эмм..."
        deb "Без приветствия?"
    elif randomizer() <= 70:
        deb "В поисках меня, надеюсь."
    elif randomizer() <= 80:
        deb "Тебе что-то нужно, милый?"
        deb "Или я могу сделать что-нибудь для тебя?"
    elif L_home_shower.is_here(M_jenny):
        deb "{b}[jen_name]{/b} находится в душе."
        deb "В случае, если ты нуждаешься во мне в течение секунды."
    else:
        deb "Я надеялась, что увижу тебя сегодня."
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
    deb "В школе все в порядке?"
    show player 14 at left
    show debbie 1 at right
    player_name "Да..."
    show player 13 at left
    show debbie 13 at right
    deb "Надеюсь, ты не зашел слишком далеко, со всем этим?"
    show debbie 14 at right
    show player 14 at left
    player_name "нет, я догоню."
    show player 13 at left
    show debbie 13 at right
    deb "Просто дайте мне знать, если есть что-нибудь я могу сделать, чтобы помочь?"
    show player 21 at left
    show debbie 14 at right
    player_name "Хорошо, {b}[deb_name]{/b}..."
    player_name "Я должен идти."
    show player 13 at left
    show debbie 3 at right
    deb "Не задерживайся до поздна!"
    show debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show debbie 1 at right
    player_name "{b}[deb_name]{/b}, Ты знаете, что случилось с моим {b}Отцом{/b}?"
    show player 11
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Ох... Милый, Я..."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Пожалуйста, я хочу знать правду!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Прости, милый. У меня нет ничего для тебя."
    deb "Полицейское расследование ничего не дало..."
    deb "На самом деле, я понимаю, что дело приостановлено из-за отсутствия доказательств."
    show debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Да, но они найдут что-нибудь, не так ли? Я имею в виду, что это их работа!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Мы можем только надеяться."
    show debbie 59 at Position (xoffset=-28)
    pause
    show debbie 60 at Position (xoffset=-28)
    deb "Милый..."
    deb "Я тоже хочу закрыть все это..."
    deb "... Но твой {b}Отец{/b} не хотел бы, чтобы мы были одержимы этим."
    show debbie 63 at Position (xoffset=-28)
    deb "Ты молод, и тебе необходимо сосредоточиться на том, чтобы жить своей жизнью"
    deb "Сделай это для своего {b}Отца{/b}."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Да. Я попробую."
    show player 14
    show debbie 61 at Position (xoffset=-28)
    player_name "Спасибо, {b}[deb_name]{/b}."
    show player 1
    show debbie 2 with dissolve
    deb "Ещё что-то нужно?"
    show debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show debbie 1
    show player 10
    player_name "{b}[deb_name]{/b}, о том, что ты сказала по телефону..."
    show debbie 13
    show player 11
    deb "Я сказала тебе не беспокоиться об этом."
    deb "Все будет хорошо!"
    show debbie 14
    show player 14
    player_name "Хорошо, но что, если я хочу помочь тебе?"
    player_name "Что если у меня будет настоящая работа?"
    show player 10
    player_name "Я чувствую себя несколько ответственным за весь этот стресс..."
    show debbie 52 at Position (xoffset=1)
    show player 11
    deb "Ты можешь помочь мне, оставаясь в школе!"
    deb "Твой {b}Отец{/b} перевернется в могиле, если я позволю тебе пойти на полный рабочий день..."
    deb "Он хотел, чтобы ты закончил свою учёбу."
    show debbie 51 at Position (xoffset=1)
    show player 10
    player_name "... Но я могу работать после школы и по выходным?"
    show debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    deb "{b}*Вздох*{/b} Ты такой упрямый, как твой {b}Отец{/b}..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    deb "Хмм..."
    show debbie 63 at Position (xoffset=-28)
    deb "Почему бы тебе не пойти проверить {b}почтовый ящик{/b}?"
    deb "Кажется, я видела там объявления о работе.."
    deb "Возможно, одно из объявлений заитересует тебя?"
    show debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Хорошо, я посмотрю."
    show debbie 62 at Position (xoffset=-28)
    show player 1
    deb "Это всё, о чем ты хотел поговорить со мной, дорогой?"
    show debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, Я хотел бы поговорить о тех парнях в костюме..."
    show debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Был ли мой {b}папа{/b} связан с ними?"
    show player 11
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*Вздох({/b} Наверное, я не смогу вечно держать это в секрете..."
    deb "Твой {b}Отец{/b} был хорошим человеком, {b}[firstname]{/b}."
    deb "... Но у него была слабость к азартным играм."
    deb "Он всегда говорил мне, что мне не о чем беспокоиться, и что у него все под рукой."
    deb "... Но теперь его нет, и, похоже, он многим со мной не поделился."
    show debbie 60 at Position (xoffset=-28) with dissolve
    deb "Твой {b}Отец{/b} задолжал этим людям много денег и они все еще пытаются вернуть."
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Мы должны просто рассказать об этом полиции!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Нет! Я боюсь того, что может случиться, если я втяну в это власти!"
    show player 10
    show debbie 59 at Position (xoffset=-28)
    player_name "Так что, ты просто заплатишь этим подонкам?!"
    show player 11
    show debbie 60 at Position (xoffset=-28)
    deb "Я сделал все возможное, но боюсь, что у меня просто нет денег, чтобы покрыть все это, милый."
    show debbie 53 at Position (xoffset=-18) with dissolve
    deb "{b}*Вздох({/b} Может нам с тобой просто исчезнуть и начать все с начала."
    show player 1
    show debbie 63 at Position (xoffset=-28) with dissolve
    deb "Хе, это будет приключение, не так ли?"
    show debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Да, я предполагаю."
    show debbie 2 with dissolve
    show player 1
    deb "Ты еще о чем-нибудь хотел поговорить?"
    show debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Разве в гараже не было краски?"
    show player 5
    show debbie 13
    deb "Краска? Зачем тебе старая краска?"
    show debbie 1
    show player 10
    player_name "Я собирался попробовать и сделать... нечто."
    show player 5
    show debbie 2
    deb "О, ну, {b}Дайан{/b} сказала, что она избавится от них для меня."
    show debbie 1
    show player 12
    player_name "Правда?"
    player_name "Ну, мне лучше посмотреть, смогу ли я забрать их, прежде чем она их выбросит!"
    player_name "Спасибо, {b}[deb_name]{/b}! Пока, {b}[deb_name]{/b}!"
    hide player with dissolve
    show debbie 2
    deb "Пока!"
    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Тебе нужна помощь с чем-нибудь?"
    show player 5
    show debbie 2
    deb "Ты закончил косить двор?"
    show debbie 1
    show player 10
    player_name "О, точно!"
    player_name "Я займусь этим."
    show player 13
    show debbie 2
    deb "Я была бы очень признательна, милый."
    show debbie 1
    show player 14
    player_name "Не проблема!"
    hide player
    hide debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "( Я должен как-то починить {b}умывальник{/b} в ванной... )"
    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "Тебе в чём-нибудь ещё помочь?"
    show player 13
    show debbie 2
    return

label debbie_dialogue_help_chores_later:
    deb "Нет. Давай позже, дорогой."
    deb "Может быть, позже, если ты будешь все еще свободен."
    return

label debbie_dialogue_help_chores_tomorrow:
    deb "Нет. Не сегодня, милый."
    deb "Может быть, завтра, если ты будешь все еще свободен."
    return

label debbie_dialogue_help_chores_after:
    show debbie 3
    deb "Спасибо что спросил!"
    show debbie 1
    show player 14
    player_name "Добро пожаловать, {b}[deb_name]{/b}."
    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "( Я должен пойти проверить {b}автомобиль{/b} для {b}[deb_name]{/b}. )"
    return

label debbie_dialogue_help_fix_car:
    show player 4
    player_name "( Я должен посетить {b}автосалон{/b}. Возможно, они могут исправить {b}[deb_name]{/b} автомобиль... )"
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Эй, {b}[deb_name]{/b}, что я могу сделать, чтобы помочь по дому?"
    show player 1
    deb "Хмм..."
    show debbie 2
    deb "Ничего из того, о чем я сейчас могу думать. Нет."
    show debbie 1
    show player 2
    player_name "Класс. Дай мне знать, если что-то случится."
    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Можно я протиру лосьоном... твои ноги?"
    show player 13
    show debbie 2
    deb "Звучит замечательно, милый."
    deb "Мне бы очень пригодились твои нежные прикосновения."
    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Можно я протиру лосьоном... твои ноги?"
    show player 5
    show debbie 13
    deb "Ох... снова? Ну, Я..."
    show debbie 14
    show player 10
    player_name "Я сделал что-то не так?"
    show player 5
    show debbie 13
    deb "О, Нет, дорогой. Это было... действительно хорошо."
    show debbie 14
    pause
    show debbie 13
    deb "Конечно, думаю, мне не помешал бы перерыв."
    show debbie 1
    show player 14
    player_name "Чудестно!"
    show player 13
    show debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    deb "Пойди и возьми лосьон {b}из моей спальни{/b}."
    show debbie 1
    show player 14
    player_name "Хорошо!"
    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show debbie 1 at right
    player_name "Помнишь, когда ты попросила меня пойти с тобой по магазинам?"
    show player 1
    show debbie 2
    deb "Да."
    show player 2
    show debbie 1
    player_name "Ну, теперь я свободен. Как насчёт сходить ещё раз?"
    show player 1
    show debbie 3
    deb "В самом деле?! Привосходная идея!"
    show debbie 2
    deb "Просто дай мне подготовиться, и я встречу тебя в машине, хорошо?!"
    show debbie 1
    show player 2
    player_name "Хорошо."
    return

label debbie_dialogue_shower_basement:
    show player 2
    show debbie 1
    player_name "Так что.."
    player_name "Я подумал, мы могли бы... Принять душ вместе?"
    show player 13
    show debbie 2
    deb "Прямо сейчас?"
    show debbie 1
    deb "Хмм..."
    show debbie 3
    deb "Думаю, я могу принять душ."
    show debbie 2
    deb "Давай я закончу складывать белье и встретимся наверху."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Я пологая, я могу принять душ..."
    deb "Я надеюсь, что мы сможем провести здесь немного времени."
    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show debbie 1
    player_name "Хэй, {b}[deb_name]{/b}!"
    player_name "Мне было интересно..."
    show player 21
    player_name "Хочешь ли ты принять душ со мной?"
    show player 14
    show debbie 2
    deb "В доме становится довольно жарко..."
    show debbie 3
    deb "Конечно! Душ сейчас, звучит прекрасно."
    show debbie 2
    deb "Дай мне минуту. Я присоединяюсь к тебе после того, как я закончю здесь."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Прости, что заставила ждать..."
    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Хочешь присоединиться ко мне в своей комнате?" #Возможно некоректый вопрос
    show player 13
    show debbie 3
    deb "Прямо сейчас?"
    show debbie 1
    show player 10
    player_name "Абсолютно!"
    show player 5
    show debbie 2
    deb "Хех, хорошо..."
    show player 13
    deb "... Только убедись, что {b}[jen_name]{/b} не видит нас."
    show debbie 1
    show player 14
    player_name "Я помню."
    show player 13
    show debbie 2
    deb "Хехехе..."
    deb "Ты собираешься меня измотать!"
    show debbie 1
    show player 14
    player_name "Я просто хочу убедиться, что ты хорошо тренируешься!"
    show player 13
    show debbie 3
    deb "Ха ха ха."
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
        deb "Ну и что в этом интересного?"
        show debbie 84
        show player 262
        player_name "Хех, не беспокойся. Я буду делать это весело!"
        show player 263
        show debbie 84
        deb "У меня нет никаких сомнений на этот счет!"
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
    deb "Абсолютно!"
    deb "Давай просто убедимся, что {b}[jen_name]{/b} не видит нас."
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
        deb "Тебя это правда удивляет?"
        deb "Я все время думаю о твоем большом члене..."
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
    deb "Приди и возьми меня, большой мальчик!"
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
    deb "Ммм, я бы с удовольствием, милый."
    show player 2
    show debbie 1
    player_name "Отлично! Я буду тебя ждать тогда."
    show player 1
    show debbie 2
    deb "Не могу дождаться!"
    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, не могли бы вы пройти со мной на секунду?"
    show player 13
    show debbie 2
    deb "Хмм?"
    show debbie 1
    show player 14
    player_name "Просто следуй за мной."
    show player 13
    show debbie 2
    deb "Хе-хе, что ты задумал?"
    show debbie 2
    deb "..."
    show debbie 3
    deb "Ты что-то планируешь!"
    show debbie 2
    deb "Хехе!"
    deb "Это сюрприз?"
    deb "... Я люблю сюрпризы!"
    show debbie 1
    show player 14
    player_name "Хех, я знаю, что ты делаешь."
    player_name "Я бы не назвал это сюрпризом, хотя..."
    show player 13
    show debbie 3
    deb "Хехе!"
    show debbie 2
    deb "Ну, как бы вы это назвали?"
    show debbie 1
    deb "..."
    show debbie 2
    deb "Это что-то неприличное?"
    deb "..."
    show debbie 1
    show player 14
    player_name "Моожет быть."
    show debbie 2
    deb "Хе-хе, ладно. Поехали быстро, а {b}[jen_name]{/b} наверху."
    hide player
    hide debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "Я подумал, Может, нам стоит посмотреть другой фильм Сегодня вечером. Интересно?"
    show player 1
    show debbie 2
    deb "Ммм, вечер кино, да?"
    deb "Звучит как отличная идея, дорогой!"
    show player 2
    show debbie 1
    player_name "Потрясающе!"
    player_name "Тогда увидимся {b}сегодня{/b} в {b}гостиной{/b}?"
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
    deb "Почти. Мне просто нужно переместить этот груз в сушилку."
    deb "Почему, что случилось, милый?"
    show player 14
    show debbie 122
    player_name "Я просто подумал, что ты захочешь прокатиться?"
    show player 13
    show debbie 123
    deb "О, чувствуешь себя немного непослушным?"
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show debbie 123
    deb "Хе-хе, я буду считать, что да!"
    show player 263f with dissolve
    deb "..."
    show debbie 121
    show player 432
    player_name "Абсолютно!"
    show player 431
    pause
    show debbie 123
    deb "Раздевайся и ложись на шайбу!"
    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show debbie 108
    deb "Моя очередь..."
    deb "Ммм, я все утро ждала этого момента!"
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
    deb "...Просто убедись, что держишься за меня."
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
    deb "Мммм..."
    deb "Я едва могу вместить его."
    return

label debbie_dialogue_laundry_sex_basement_random_false:
    deb "Ахх..."
    player_name "( !!! )"
    player_name "Ты такая теплая..."
    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Хэй, {b}[deb_name]{/b}... Ты хочешь пообщаться в подвале для быстрой игры?"
    show player 13
    show debbie 2
    deb "Ох?"
    show debbie 1
    show player 14
    player_name "Я подумал, что мы можем включить сушилку, и ты можешь быть такой громкой, какой бы тебе хотелось..."
    show player 13
    show debbie 3
    deb "Ха ха."
    show debbie 2
    deb "Это довольно непослушно, милый."
    show debbie 1
    pause
    show debbie 2
    deb "Хмм... Хорошо!"
    deb "У меня есть свободное время, и я могла бы использовать некоторое... внимание"
    show debbie 1
    show player 14
    player_name "Правда?"
    show player 13
    show debbie 2
    deb "Конечно!"
    deb "Встретимся там через минуту..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show debbie 1 at right
    player_name "Хэй... ммм, {b}[deb_name]{/b}?"
    show player 5
    show debbie 2
    deb "Да, милый?"
    show player 10
    show debbie 1
    player_name "Могу я спросить тебя кое о чем?"
    show player 5
    show debbie 3
    deb "Ну конечно! Ты можешь спросить меня о чем угодно."
    show player 10
    show debbie 1
    player_name "Ну, это любопытно... Смущающе."
    show player 5
    show debbie 13
    deb "Да? Ну это нормально, {b}[firstname]{/b}."
    deb "Нет нужды смущаться."
    deb "Не со мной..."
    show debbie 14
    show player 10
    player_name "Хорошо."
    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show debbie 14 at right
    player_name "Мне было интересно, сможешь ли ты..."
    player_name "Ну..."
    show player 5
    show debbie 13
    deb "Если бы я могла, Милый?"
    show player 10
    show debbie 14
    player_name "Эмм... Помнишь тот день в торговом центре?"
    show player 5
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "... Д-да?"
    show player 10
    show debbie 14b
    player_name "Ну... Я надеялся, что ты научишь меня большему, знаешь, о поцелуях?"
    show player 5
    show debbie 13
    deb "Что?!"
    show debbie 14b
    player_name "..."
    show debbie 13
    deb "Это была ошибка, милый. Я никогда не должна..."
    deb "На что ты надеешься, что я научу тебя в любом случае?"
    show player 10
    show debbie 14b
    player_name "Ты знаешь, как это сделать."
    player_name "Я подумала, Может, ты покажешь мне, что нравится женщинам?"
    show player 5
    show debbie 13
    deb "Ну, я могу сказать тебе, что нравится женщинам."
    deb "... Но я не думаю, что показывать тебе это хорошая идея. Было бы неуместно..."
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
    player_name "... Фактически."
    player_name "Неважно."
    show debbie 13
    show player 5
    deb "Ты уверен?"
    deb "Ты всегда можешь поговорить со мной, {b}[firstname]{/b}."
    show player 10
    show debbie 14
    player_name "Да, ничего страшного."
    player_name "Извините, что."
    show player 5
    show debbie 13
    deb "Ты никогда мне не надоедаешь, милый."
    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show debbie 1 at right
    player_name "Как ты думаешь, мы могли бы практиковать снова?"
    player_name "Ты знаешь... Целование?"
    show player 1
    show debbie 13
    deb "Снова?"
    show player 2
    show debbie 14b
    player_name "Д-да. Думаю, у меня определенно получится!"
    show player 1
    show debbie 13
    deb "... Хорошо."
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
    deb "Вау... Я бы сказала, у тебя определенно получается."
    deb "... и ты уже так хорош, для начала!"
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
    player_name "Жаль что... Ты знаешь."
    show player 231
    show debbie 75
    deb "Хе-хе, все в порядке, милый."
    deb "Совершенно естественный."
    deb "Девочки в этом городе находятся в беде."
    show player 232
    show debbie 72
    player_name "Ха, ты права!"
    show player 231
    show debbie 73
    deb "Вперед, дорогой!"
    show player 232
    show debbie 72
    player_name "Да, мэм!"
    return

label debbie_dialogue_leave:
    show player 2
    player_name "Вообще-то, забудь, увидимся позже, {b}[deb_name]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
