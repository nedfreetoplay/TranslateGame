label dianes_shed_diane_breeding_help_started:
    scene shed_night with None
    show diane 89 at right
    show player 11 at left
    dia "У меня есть {b}небольшая просьба{/b} к тебе."
    show diane 88
    player_name "..."
    show player 21
    player_name "Конечно! Что могу сделать для тебя?"
    show diane 87
    show player 13
    dia "Мне пришла... {b}Коробка{/b}, Можешь принести её мне."
    show diane 88
    show player 10
    player_name "О, хорошо."
    player_name "Где она?"
    show diane 89
    show player 13
    dia "Она находится в {b}торговом центре{/b}..."
    show diane 90
    show player 11
    dia "...В магазине, под названием {b}Pink{/b}."
    dia "Записан на моё имя!"
    show diane 88
    show player 29
    player_name "В магазине {b}Pink{/b}?!"
    show player 21
    player_name "..."
    player_name "Но, что это?"
    show diane 87
    show player 13
    dia "Это что-то для тебя... Но это {b}сюрприз{/b}!"
    show diane 88
    show player 11
    player_name "!!!"
    show player 21
    player_name "Правда?"
    show player 108f
    player_name "Торговый центр сейчас закрыт..."
    show player 21
    player_name "Схожу завтра."
    show diane 90
    show player 13
    dia "Вот молодчина..."
    show diane 89
    return

label dianes_shed_shed_dialouge_0:
    show player 35 at left with dissolve
    player_name "Воу..."
    show player 34
    player_name "...Какой странный сарай."
    player_name "Что случилось со всеми контейнерами... А эти цепи?!"
    show player 43
    player_name "В любом случае, {b}попробую найти насос{/b}..."
    hide player 43 with dissolve
    return

label dianes_shed_shed_dialouge_1_intro:
    scene shed_blur_night
    show diane 57 at right with dissolve
    window hide
    pause
    show diane 58 at right
    window hide
    pause
    show diane 57 at right
    window hide
    pause
    show diane 58 at right
    window hide
    pause
    show diane 57 at right
    show player 11 at left with dissolve
    player_name "..."
    show player 23 at left
    player_name "{b}Диана{/b}!??"
    show diane 59 at right with hpunch
    show player 22 at left
    dia "!!!"
    show diane 60 at right
    dia "Что ты здесь делаешь??!"
    show diane 64 at right
    show player 29 at left
    player_name "Я увидел что дверь открыта! И-"
    show player 3 at left
    player_name "..."
    show player 21 at left
    player_name "...Это {b}молокоотсос{/b}?"
    show diane 61 at right
    show player 5 at left
    dia "{b}*вздыхает*{/b}"
    show diane 62 at right
    show player 11 at left
    dia "Да, {b}[firstname]{/b}... Я... иногда люблю подоить себя..."
    show diane 64 at right
    show player 12 at left
    player_name "Подожди..."
    if M_player.get("drank milk"):
        player_name "Это молоко, которое ты заставила меня выпить на днях?!"
    else:
        player_name "Это молоко, которое ты дала мне выпить на днях?!"
    show diane 61 at right
    show player 11 at left
    dia "Я знаю... Я должна была сказать тебе..."
    show diane 60 at right
    show player 5 at left
    dia "Но оно натуральное, и мне больше не с кем было попробовать!!"
    show diane 61 at right
    dia "Надеюсь, ты сможешь простить меня?"
    return

label dianes_shed_shed_dialouge_1_okay:
    show diane 64 at right
    show player 21 at left
    player_name "Все в порядке, {b}Диана{/b}."
    player_name "Ты не должна извенятся..."
    show diane 63 at right
    show player 17 at left
    if M_player.get("drank milk"):
        player_name "...Мне вообще-то понравилось!"
    else:

        player_name "...Я рад, что ты мне предложила!"
    show diane 62 at right
    show player 13 at left
    dia "Это... очень мило с твоей стороны..."
    show diane 63 at right
    show player 29 at left
    player_name "Я... должен идти домой."
    show diane 62 at right
    show player 3 at left
    dia "Да, я пойду в дом..."
    dia "И пожалуйста-"
    show diane 64 at right
    show player 21 at left
    player_name "Я никому не расскажу. Не волнуйся."
    show diane 63 at right
    show player 13 at left
    dia "Спасибо."
    hide player 13 at left with dissolve
    hide diane 63 at right with dissolve
    return

label dianes_shed_shed_dialouge_1_wrong:
    show diane 64 at right
    show player 12 at left
    player_name "Я не знаю, {b}Диана{/b}."
    if M_player.get("drank milk"):
        player_name "Это ужасно, что ты обманом заставила меня пить твое грудное молоко..."
    else:

        player_name "Это было довольно неправильно предложить мне это..."
    show diane 61 at right
    show player 90 at left
    dia "Я знаю..."
    dia "Мне очень жаль!"
    show diane 64 at right
    show player 12 at left
    player_name "Я иду {b}домой{/b}..."
    show diane 60 at right
    show player 13 at left
    dia "Но-"
    show diane 64 at right
    show player 24 at left
    player_name "Пока..."
    hide diane 64 at right with dissolve
    hide player 24 at left with dissolve
    return

label dianes_shed_seen_shed_locked:
    show player 34 with dissolve
    player_name "Хмм..."
    show player 35
    player_name "Дверь закрыта."
    hide player 35 with dissolve
    return

label dianes_shed_not_seen_shed_locked:
    show player 35 at left with dissolve
    player_name "Хм.. Сарай заперт на ключ. Интересно, что там?"
    show diane 8 at right with dissolve
    show player 22 at left
    dia "Что ты тут лазиешь?"
    show diane 9 at right
    show player 10 at left
    player_name "Ох, прости. Я просто искал инструменты..."
    show diane 10 at right
    show player 11 at left
    dia "Все нормально. Возможно, однажды я устрою тебе небольшую экскурсию..."
    show player 21 at left
    show diane 9 at right
    player_name "Конечно, {b}Диана{/b}..."
    hide player 21 at left with dissolve
    hide diane 9 at right with dissolve
    return

label dianes_shed_dianes_dialogue:
    scene location_diane_shed01_night_closeup
    show player 1 at left with dissolve
    show diane 89 at right with dissolve
    dia "Привет, Красавчик."
    dia "Готовы научиться доить?"
    show diane 88
    show player 17
    player_name "Конечно! Я с удовольствием помогу!"
    show diane 89
    show player 1
    dia "Вот хороший мальчик..."
    return

label dianes_shed_dianes_dialogue_not_package:
    show diane 88
    show player 10
    player_name "Я забыл, где забрать {b}коробку{/b}."
    show player 29
    player_name "Как я могу найти его?"
    show diane 89
    show player 13
    dia "Тебе нужно забрать его в {b}торговом центре{/b}."
    show diane 87
    dia "Магазин называется {b}Pink{/b}."
    show diane 89
    dia "Она будет записана на мое имя!"
    show diane 88
    show player 21
    player_name "О. Хорошо. Понял!"
    show diane 89
    show player 13
    dia "Хочешь ещё о чем-нибудь поговорить?"
    return

label dianes_shed_dianes_dialogue_package:
    show player 239_240
    pause
    show diane 88
    show player 170
    player_name "У меня {b}коробка{/b} которую ты спрашивала!"
    show diane 90
    show player 169
    dia "Прекрассно!"
    label aunt_shed_replay_1:
        show diane 119
        show player 11
        dia "Так, стой здесь..."
        dia "...я вернусь через минутку с сюрпризом для тебя."
        scene black with dissolve
        pause 0.5

        scene shed_night
        show diane 113 at right
        show player 23 at left
        with dissolve
        player_name "!!!" with hpunch
        show diane 114
        show player 22
        dia "Ну?"
        show diane 115
        dia "...Нравится?"
        show diane 113
        show player 29
        player_name "Это... реально сексуально, {b}Диана{/b}."
        show diane 114
        show player 13
        dia "Я всегда хотела надеть это... У меня просто никогда не было никого, для кого надевать его..."
        show diane 113
        show player 11
        player_name "..."
        show diane 116
        show player 23
        dia "Мне нравится, как моя грудь может висеть, естественно, как..."
        show player 22
        player_name "..."
        show diane 114
        dia "Я подумала, что это поможет тебе настроиться... {b}на дойку{/b}..."
        show diane 113
        show player 29
        player_name "Ну, это сработало! Хаха..."
        show diane 114
        show player 13
        dia "Ну... Эмм..."
        dia "Чем хочешь занятся?"
    return

label dianes_shed_dianes_dialogue_not_lets_milk:
    show diane 88
    show player 21
    player_name "Я готов начать если хочешь."
    show diane 87
    show player 11
    dia "Не сейчас!"
    show diane 89
    show player 13
    dia "Тебе нужно {b}позаботиться о нескольких вещах{/b}, о которых я тебя спрашивал, прежде чем мы начнем..."
    show diane 88
    show player 21
    player_name "А, точно!"
    show player 17
    player_name "Моя вина, я позабочусь об этом первым..."
    show diane 90
    show player 13
    dia "Не волнуйся. Скоро мы будем веселиться..."
    return

label dianes_shed_dianes_dialogue_lets_milk_no_sex:
    show diane 113
    show player 17
    player_name "Давайте сделаем немного молока!"
    show diane 114
    show player 2
    dia "Я надеялася, что ты это скажешь..."
    show diane 112
    dia "Но прежде чем мы начнем, я должна подготовиться к извлечению молока!"
    show diane 113
    show player 12
    player_name "Каким образом ты это делаешь?"
    show diane 117
    show player 11
    dia "С помощью этого!"
    dia "Я должна присоединить эти всасывающие насосы..."
    player_name "!!!"
    show diane 113
    show player 21
    player_name "А не... больно?"
    show diane 115
    show player 13
    dia "Хаха. Вроде нет..."
    show diane 114
    dia "Это немного странно, когда он качает, но мне это нравится!"
    show diane 113
    show player 21
    player_name "Классно!"
    show diane 114
    show player 11
    dia "Знаешь, говорят, что коровы больше дают молока, когда они... {b}оплодотворенны{/b}..."
    show diane 113
    player_name "..."
    show player 29
    player_name "Я... Я не понимаю-"
    show diane 112
    show player 13
    dia "Я просто хочу сказать... Беременные коровы дают намного больше молока!"
    show player 11
    show diane 114
    dia "... И {b}эта корова еще не беременна{/b}. Её {b}бык{/b} готов {b}размножаться{/b} с ней?"
    show diane 113
    show player 23
    player_name "!!!"
    show diane 114
    show player 22
    dia "Трахни меня, {b}[firstname]{/b}! Сделай мою матку своей!"
    show diane 113
    show player 29
    player_name "... Да, Я... Я с удовольствием..."
    show diane 114
    show player 13
    dia "Это мой малыш!"
    show player 11
    return

label dianes_shed_dianes_dialogue_lets_milk_had_sex:
    show diane 113
    show player 17
    player_name "Давай сделаем немного молока!"
    show diane 114
    show player 2
    dia "Я надеялася, что ты это скажешь..."
    dia "Я не могла дождаться, когда ты вернешься!"
    show diane 112
    show player 11
    dia "Но прежде чем мы начнем, позвольте мне войти в образ!"
    show player 11
    show diane 116
    dia "Как я выгляжу?"
    show player 21
    player_name "Ты прекрасна, {b}Диана{/b}!"
    show player 13
    show diane 112
    dia "Теперь, когда ты посадишь меня на стул..."
    dia "Сделай так чтобы твоя сперма была {b}глубоко{/b} внутри меня...."
    show player 11
    show diane 113
    player_name "!!!"
    show player 23
    show diane 114
    dia "Мне нужно чтобы мой бычёк.... {b}оплодотворил{/b} меня как можно лучше..."
    show diane 112
    show player 22
    dia "...Ты справишься с этим?"
    show diane 113
    show player 29
    player_name "...Да, Я... Я сделаю это для тебя..."
    show diane 115
    show player 13
    dia "Это мой хороший мальчик!"
    show player 11
    show diane 114
    return

label dianes_shed_dianes_dialogue_lets_milk:
    dia "Давайте устроимся на {b}стул для размножения{/b}..."
    scene shed_closeup 1
    show dianesex 36
    with dissolve
    dia "Сейчас вставляй мягко и медленно..."
    dia "...и не доставай пока не кончишь {b}глубоко{/b} внутри..."
    show dianesex 38
    dia "Вот так..."
    show dianesex 40
    dia "{b}*стонет*{/b}"
    return

label shed_sex_loop:
    if shed_sex_action == 0:
        if shed_sex_angle == 0:
            if not renpy.showing("shed_closeup 1"):
                scene shed_closeup 1
                show expression AnimatedImage("dianesex", [38,40], M_aunt) as dianesex
        else:
            if not renpy.showing("shed_closeup 2"):
                scene shed_closeup 2
                show expression AnimatedImage("dianesex", [50,52], M_aunt) as dianesex at right

    elif shed_sex_action == 1:
        if not renpy.showing("shed_closeup 3"):
            scene shed_closeup 3
            show dianesex 54
            player_name "Ты вся мокрая, {b}Диана{/b}."
            dia "Мне просто нравится ощущение моего клитора на твоем жестком члене, милый."
            dia "Продолжай..."

    elif shed_sex_action == 2:
        if previous_shed_sex_action != shed_sex_action:
            show dianesex 56
            dia "Я хочу, чтобы он был внутри меня..."
    show screen sex_xray_anim_buttons
    pause
    hide screen sex_xray_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if shed_sex_action == 0:
                if shed_sex_angle == 0:
                    show expression AnimatedImage("dianesex", [38,40], M_aunt) as dianesex
                else:
                    show expression AnimatedImage("dianesex", [50,52], M_aunt) as dianesex at right

            elif shed_sex_action == 1:
                show expression AnimatedImage("dianesex", [54,55], M_aunt) as dianesex

            elif shed_sex_action == 2:
                show expression AnimatedImage("dianesex", [58,59,58,57], M_aunt) as dianesex

            elif shed_sex_action == 3:
                show expression AnimatedImage("dianesex", [61,60], M_aunt) as dianesex
            pause 8
        else:

            $ pose_counter = 0
            if shed_sex_action == 0:
                if shed_sex_angle == 0:
                    $ pose_list = [38,40]
                else:
                    $ pose_list = [50,52]

            elif shed_sex_action == 1:
                $ pose_list = [54,55]
            elif shed_sex_action == 2:
                $ pose_list = [58,59,58,57]

            elif shed_sex_action == 3:
                $ pose_list = [61,60]
            $ poses_done = []
            while poses_done != pose_list:
                if shed_sex_action == 0 and shed_sex_angle == 1:
                    show expression "dianesex {}".format(pose_list[pose_counter]) as dianesex at right
                else:

                    show expression "dianesex {}".format(pose_list[pose_counter]) as dianesex
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1

    if shed_sex_action == 3:
        $ persistent.cookie_jar["Diane"]["unlocked"] = True
        $ persistent.cookie_jar["Diane"]["gallery"]["06_unlocked"] = True
        pause .3
        show dianesex 62
        player_name "Вау..."
        player_name "Она так сильно брызнула!"
        dia "{b}*задыхаясь*{/b}"
        dia "Ты подоил меня..."
        if not store._in_replay == None:
            jump expression game.dialog_select("after_milk_replay")
    $ previous_shed_sex_action = shed_sex_action
    call screen shed_sex_options

label shed_sex_cum:
    call expression game.dialog_select("shed_sex_cum_dialouge")
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label shed_sex_cum_dialouge:
    dia "Не сдерживайся..."
    dia "Кончай глубоко внутрь меня..."
    dia "Оплодотвори меня!!!"
    if shed_sex_angle == 0:
        show dianesex 40
        if xray:
            show expression "characters/player/char_player_sex_44.png" as playersex_cum
    else:

        show dianesex 52 at right
        if xray:
            show expression "characters/player/char_player_sex_48.png" as playersex_cum at right
    dia "{b}ААаааааххххх!!{/b}"
    if shed_sex_angle == 0:
        show dianesex 36
        show expression "characters/player/char_player_sex_45.png" as playersex_cum
    else:

        show dianesex 48
        show expression "characters/player/char_player_sex_49.png" as playersex_cum at right
        pause
        show dianesex 46
        show expression "characters/player/char_player_sex_50.png" as playersex_cum
    dia "Это было... Так много спермы..."
    player_name "Я сделал все верно?"
    dia "Ты трахнул меня очень хорошо."
    dia "Спасибо..."
    hide playersex_cum
    label after_milk_replay:
        scene shed_night
    show player 1 at left
    show diane 89 at right
    with dissolve
    dia "Большое спасибо за помощь..."
    show diane 87
    dia "Скоро у меня будет самое вкусное молоко в городе!"
    show player 2
    show diane 88
    player_name "Я действительно наслаждался этим. Я надеюсь, что смогу помочь снова в ближайшее время!"
    show player 1
    show diane 89
    dia "Я планирую расширить свой молочный бизнес, так что..."
    show diane 90
    dia "Здесь много работы, которую нужно сделать!"
    show diane 89
    dia "Мне всегда пригодится помощь..."
    show player 17
    show diane 88
    player_name "Это было бы замечательно!"
    show player 1
    show diane 89
    dia "Уже поздно. Тебе, наверное, пора идти..."
    show diane 92
    dia "Ты же не хочешь чтобы {b}[deb_name]{/b} ждала!"
    show player 21
    show diane 91
    player_name "Да."
    show player 13
    show diane 87
    dia "Помни: мы должны сохранить это в секрете."
    show player 21
    show diane 88
    player_name "Не переживай, {b}Диана{/b}, я никому не скажу."
    show player 13
    show diane 90
    dia "Это мой красивый мальчик!"
    show diane 111 at left
    dia "Нам будет очень {b}весело{/b} вместе..."
    hide diane 111 at left
    $ renpy.end_replay()
    return

label dianes_shed_dianes_dialogue_leave:
    show diane 88 at right
    show player 10 at left
    player_name "Я бы хотел остаться здесь и подоить тебя..."
    show diane 91
    player_name "Но уже пождно и {b}[deb_name]{/b} наверно переживает."
    show diane 92
    show player 5
    dia "Это плохо."
    dia "Я с нетерпением ждала помощи с моим молоком..."
    show diane 91
    show player 10
    player_name "Прости... Может другой ночью?"
    show diane 87
    show player 13
    dia "Конечно... Ты знаешь где меня найти."
    show diane 88
    show player 21
    player_name "Хорошо!"
    hide diane 88 at right with dissolve
    hide player 21 at left with dissolve
    return

label dianes_shed_dewitt_paint:
    scene location_diane_shed01_night_closeup
    show player 588
    with dissolve
    player_name "Наконец-то нашел краску!"
    player_name "Если я возьму ее и немного {b}досок{/b} на {b}верстак{/b} в {b}гараже{/b}, Я смогу сделать копию гитары, без проблем."
    hide player with dissolve
    $ M_dewitt.trigger(T_dewitt_shed_find_paint)
    if not player.has_item("paint"):
        $ player.get_item("paint")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
