label helens_bedroom_mia_midnight_help:
    scene mia_house_helen_night_b
    player_name "( Ключ должен быть где-то здесь... )"
    return

label helens_bedroom_mia_helen_talk:
    scene expression game.timer.image("mia_house_helen_c{}")
    show helen 1f at right
    show player 10 at left
    with dissolve
    player_name "Эмм... Здрасьте?"
    show player 5
    show helen 4
    helen "!!!"
    show helen 5
    helen "Снова ты?!"
    show helen 6
    show player 10
    player_name "{b}Мия{/b} попросила меня поговорить с вами."
    show player 5
    show helen 2
    helen "Тебя попросила {b}Мия{/b}?"
    show helen 1
    show player 12
    player_name "Я не до конца понимаю, что происходит, да это и не моё дело..."
    show player 10
    player_name "...но я думаю, что {b}Мия{/b} не хочет, чтобы её родители расходились вот так."
    show player 11
    show helen 5
    helen "Ты прав. Это не твое дело!"
    show helen 4
    helen "Кроме того... Мы ничего здесь не можем изменить..."
    show helen 3
    helen "...ибо всё в руках {b}Божьих{/b}!"
    show helen 1
    show player 12
    player_name "Чего?"
    show player 5
    show helen 4
    helen "Тебе лучше уйти..."
    hide player
    hide helen
    with dissolve
    return

label helens_bedroom_mia_unexpected_visit:
    label helen_baton_replay_1:
        scene mia_house_helen_sneak
    show helens 1_2 at Position (xpos=465,ypos=565) with dissolve
    player_name "!!!"
    player_name "( ...{b}Хелен{/b}?! )"
    player_name "( Это... полицейская дубинка?! )"
    helen "Ооооох! Ооооо даааа..."
    helen "{b}Гарольд{/b}..."
    helen "Ооооох..."
    helen "Я ждала... так долго..."
    show helens 3 with dissolve
    player_name "!!!" with hpunch
    player_name "( Меня заметили!! )"
    scene black
    scene mia_house_helen_c
    show helen 33 at right
    show player 10 at left
    with dissolve
    player_name "Извините, {b}Хелен{/b}!!!"
    player_name "Я услышал какие-то звуки и подумал, что {b}Мия{/b} здесь..."
    player_name "...Я не ожидал увидеть..."
    show player 5
    show helen 34
    helen "П... Прости, что увидел меня такой..."
    show helen 29
    show player 24
    player_name "Я почти ничего не видел... Я просто..."
    player_name "Я пожалуй пойду, простите за то, что потревожил."
    show player 11
    show helen 30
    helen "Постой!"
    helen "Мне нужно тебе кое-что сказать."
    show helen 29
    show player 3 with dissolve
    player_name "..."
    show helen 34
    helen "Как ты думаешь, я всё ещё... привлекательна?"
    show helen 33
    show player 22 with dissolve
    player_name "!!!" with hpunch
    show player 10
    player_name "Эмм... Я не знаю, могу ли-"
    show player 11
    show helen 30
    helen "Просто ответь!"
    show helen 29
    show player 37 with dissolve
    player_name "...Да."
    show player 24
    show helen 41 at Position (xoffset=1)
    with dissolve
    helen "{b}*Вздох*{/b}"
    show helen 42 at Position (xoffset=1)
    show player 11
    helen "После того, как я начала посещать эти занятия с {b}сестрой Анжеликой{/b}..."
    helen "...меня обуревают желания, которых я раньше не замечала!"
    helen "Моему телу необходимо внимание..."
    helen "...но что, если мой муж не захочет вернуться?"
    show helen 33 with dissolve
    show player 12
    player_name "Я думаю {b}Гарольд{/b} очень вас любит, {b}Хелен{/b}."
    show player 5
    show helen 34
    helen "Я не уверена, что он ещё считает меня привлекательной..."
    helen "...я понимаю, что я должна быть более... сексуальной для моего супруга."
    helen "Я хочу измениться."
    show helen 29
    show player 12
    player_name "Измениться?"
    show player 5
    show helen 30
    helen "Мне нужно обновить гардероб, {b}[firstname]{/b}."
    show helen 29
    show player 10
    player_name "Оу..."
    show player 5
    show helen 30
    helen "Я хочу, чтобы он снова возжелал меня. Найти что-то... возбуждающее!"
    show helen 29
    show player 11
    player_name "..."
    show helen 34
    helen "Ты бы не мог... помочь мне?"
    show helen 33
    show player 12
    player_name "Помочь?"
    show player 5
    show helen 30
    helen "Мне нужно сексуальное бельё или что-то в этом роде..."
    show helen 29
    show player 23
    player_name "!!!"
    show player 30
    player_name "Не уверен, что смогу помочь с этим, {b}Хелен{/b}. Я просто-"
    show player 11
    show helen 30
    helen "Просто купи что-нибудь сексуальное..."
    helen "...я дам тебе немного денег!!"
    show helen 29
    show player 12
    player_name "Почему бы вам самой не купить это? Уверен, вы лучше меня знаете, чего хотите."
    show player 5
    show helen 30
    helen "Я же не могу ходить по всяким {b}секс-шопам{/b}."
    helen "Ты должен помочь мне... Ну пожалуйста!"
    show helen 29
    show player 10
    player_name "Охх... Ладно, что вам нужно?"
    show player 5
    show helen 34
    helen "Я всегда хотела носить корсет... и ещё, {b}Гарольду{/b} нравится красный цвет."
    show helen 29
    show player 12
    player_name "Короче говоря, {b}красный корсет{/b}?"
    show player 5
    show helen 30
    helen "Если сможешь его найти, купи его для меня."
    show helen 29
    show player 10
    player_name "Я постараюсь..."
    show player 5
    show helen 34
    helen "Спасибо, {b}[firstname]{/b}."
    hide player
    hide helen
    with dissolve
    if not store._in_replay == None:
        scene black with dissolve
        pause 0.5
        scene mia_house_helen_c with dissolve
        jump helen_baton_replay_2
    return

label helens_bedroom_mia_helen_outfit_request:
    label helen_baton_replay_2:
        scene mia_house_helen_c
    show helen 23 at right
    show player 14 at left
    with dissolve
    player_name "Здрасьте, {b}Хелен{/b}!"
    show player 13
    show helen 24
    helen "Наконец-то."
    helen "Как продвигаются поиски?"
    show helen 23
    show player 33
    player_name "Думаю, я нашёл что-то похожее..."
    show player 239_240 with dissolve
    pause
    show player 449 with dissolve
    pause
    show player 451
    player_name "Вот он!"
    player_name "Это сексуальный красный корсет, прям как вы и просили."
    show player 450
    show helen 24
    helen "Вау."
    show player 13
    show helen 18
    with dissolve
    helen "Он... несколько экстравагантный..."
    show helen 17
    show player 10
    player_name "Вам не нравится?"
    show player 5
    show helen 18
    helen "Нет, он просто такой... Я раньше не надевала ничего подобного."
    show helen 17
    show player 36 with dissolve
    player_name "Ну, думаю, мне пора."
    show player 11 with dissolve
    show helen 20
    helen "Постой!"
    helen "Ты не хочешь остаться и оценить меня?"
    show helen 19
    show player 12
    player_name "Что?"
    show player 5
    show helen 20
    helen "Давай я его надену и ты скажешь, как я в нём выгляжу!"
    show helen 21 with dissolve
    pause
    show helen 22 at Position (xoffset=-14) with dissolve
    pause
    show helen 35 with dissolve
    pause
    show helen 36 with dissolve
    pause
    show helen 38 with dissolve
    show player 433
    player_name "!!!"
    show helen 45 with dissolve
    pause
    show helen 46 with dissolve
    pause
    show player 11
    show helen 48 at Position (xpos=970) with dissolve
    helen "Он немного жмёт... Но он подчёркивает грудь, что очень хорошо..."
    show helen 49 at Position (xoffset=18) with dissolve
    helen "А что это за вырез внизу?!"
    show player 433
    pause
    show player 435
    player_name "А, это, я эээ... не заметил его при покупке!"
    show player 79 with dissolve
    player_name "Хаха..."
    show player 82
    show helen 48
    with dissolve
    helen "Чем ты вообще ДУМАЛ?"
    show helen 47
    show player 83
    player_name "Оу, Я... всё выглядит просто чудесно!"
    player_name "Я подумал, что он будет хорошо смотреться на вас..."
    show player 82
    show helen 48
    helen "Всё хорошо... Думаю, {b}Гарольду{/b} понравится нечто подобное."
    helen "Спасибо, {b}[firstname]{/b}."
    show helen 47
    show player 79 with dissolve
    player_name "Не за что, {b}Хелен{/b}... Но мне правда нужно идти."
    player_name "До свидания!"
    hide player
    hide helen
    with dissolve
    $ renpy.end_replay()
    return

label helens_bedroom_helen_master_servant_fun:
    scene mia_house_helen_window0 with fade
    show expression "objects/character_helen_02.png" at Position (xpos = 211, ypos = 732)
    player_name "Вау..."
    player_name "Здесь темновато."
    return

label helens_mary_statue:
    scene mia_house_statue
    show key3 at Position (xpos=450,ypos=450):
        rotate -45
    player_name "На этих чётках есть ключ... Может он может открыть дверь?"
    player_name "Нужно попробовать..."
    show unlock52 at truecenter with dissolve
    $ player.get_item("key03")
    pause
    hide unlock52 with dissolve
    $ M_mia.trigger(T_mia_key_found)
    $ game.main()

label helen_bedroom_sex:
    call expression game.dialog_select("helen_bedroom_sex_intro")
    if not store._in_replay == None:
        call expression game.dialog_select("helen_bedroom_sex_yes")
        jump expression game.dialog_select("helen_bedroom_sex_start")
    menu:
        "В другой раз.":
            call expression game.dialog_select("helen_bedroom_sex_leave")
        "Давай.":

            call expression game.dialog_select("helen_bedroom_sex_yes")

            label helen_bedroom_sex_start:
                menu:
                    "Оставь корсет.":
                        $ M_helen.set("corset lingerie", True)
                    "Раздевайся.":

                        $ M_helen.set("corset lingerie", False)

            call expression game.dialog_select("helen_bedroom_sex_start_after")
            $ anim_toggle = True
            jump expression game.dialog_select("helen_bedroom_sex_loop")
    hide player
    hide helen
    with dissolve
    $ game.main()

label helen_bedroom_sex_intro:
    scene mia_house_helen_closed_c with fade
    show player 5 at left
    show helen 63 at right
    with dissolve
    helen "Здравствуйте, {b}[firstname]{/b}."
    helen "Я очень рада видеть вас."
    helen "Теперь я наконец могу обслужить вас, {b}Господин{/b}."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Ты заперла дверь?"
    show helen 62
    show player 12
    player_name "Нет."
    show player 11
    show helen 63
    helen "Меня не волнует, что кто-то может придти и увидеть нас с вами...вместе."
    show helen 62
    show player 10
    player_name "Эмм... А как же... {b}Мия{/b}?"
    player_name "Она не... расстроится?"
    show player 5
    show helen 63
    helen "Ней волнуйтесь о том, чтобы быть замечеными ею."
    helen "Это куда лучше поможет мне искупить свои грехи."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Вам нравится мой наряд? Он вас возбуждает?"
    show helen 62
    show player 10
    player_name "Я... я считаю тебя милой, и мне без разницы, в нём ты или нет."
    show player 5
    show helen 49 with dissolve
    helen "Оу? Так вы предпочтёте, чтобы я разделась?"
    pause
    show helen 62 with dissolve
    show player 23
    player_name "!!!"
    show player 37 with dissolve
    player_name "Нет, {b}Хелен{/b}! В смысле...да, но..."
    show player 29 with dissolve
    player_name "Без одежды ты тоже прекрасно выглядишь."
    show player 3
    show helen 63
    helen "Хехе... Я буду всегда надевать этот наряд для вас."
    helen "Вы знаете... Я здесь, чтобы обслужить вас, {b}Господин{/b}."
    show helen 62
    show player 29
    player_name "Хе...Хе... Не нужно, {b}Хелен{/b}."
    show player 5 with dissolve
    show helen 63
    helen "Нужно!"
    helen "{b}Сестра Анжелика{/b} сказала, что ваше семя - единственный путь к моей чистоте."
    helen "Мое тело нужно очищение вашим божественным семенем."
    helen "Поэтому я отдаю вам свое тело, используйте его, чтобы удовлетворить свои желания."
    show helen 62
    show player 11
    player_name "..."
    return

label helen_bedroom_sex_leave:
    show player 10
    player_name "Спасибо, {b}Хелен{/b}..."
    player_name "Как нибудь в другой раз."
    show player 12
    show helen 47
    player_name "У меня...есть неотложные дела."
    show player 5
    show helen 48
    helen "Оу..."
    helen "Я так надеялась обслужить вас..."
    helen "Приходите почаще."
    show helen 47
    show player 12
    player_name "Обязательно... Я дам тебе знать, {b}Хелен{/b}."
    return

label helen_bedroom_sex_yes:
    show player 14
    player_name "Хорошо... Давай начнём..."
    show player 13
    show helen 63
    helen "Прекрасно!"
    helen "Пока мы не начали, разденьтесь и раздвиньте шторы."
    show helen 62
    show player 10
    player_name "Что? Раздвинуть шторы?"
    show player 5
    show helen 63
    helen "Не волнуйтесь, {b}[firstname]{/b}."
    helen "Просто разденьтесь и сядьте на край кровати."
    helen "Это не займёт много времени."
    show helen 62
    show player 10
    player_name "Хорошо..."
    hide helen
    hide player
    with dissolve

    scene mia_house_helen_window1
    show player helen_sex 52
    with fade
    helen "Я так долго скрывала свои грешные помыслы."
    helen "Больше я не буду ничего скрывать."
    scene mia_house_helen_window2
    show player helen_sex 52
    helen "Я хочу, чтобы {b}Господь{/b} и соседи видели меня такой, какая я есть."
    scene mia_house_helen_window3
    show player helen_sex 52
    show helen 54 with dissolve
    helen "Грешную женщину, пытающуюся следовать учениям церкви."
    show helen 53
    player_name "!!!"
    player_name "Ты уверена, что хочешь так сделать?"
    show helen 54
    helen "Вы слишком волнуетесь, {b}[firstname]{/b}."
    helen "Нет ничего постыдного в наших телах..."
    helen "...лягте на спину, и я пролью на себя благодать {b}Божью{/b}."
    show helen 53
    player_name "Хорошо."
    show player helen_sex 59 with dissolve
    show helen 54
    return

label helen_bedroom_sex_start_intro:
    helen "Вы хотите, чтобы я разделась, перед тем как мы приступим к таинству?"
    show helen 53
    return

label helen_bedroom_sex_start_after:
    show helen 54
    helen "Как прикажете, {b}Господин{/b}."
    if M_helen.is_set("corset lingerie"):
        show helen 54
    else:

        show helen 55 with dissolve
        pause
        show helen 56 with dissolve
        pause
        show helen 58 with dissolve

    helen "Позвольте мне вставить ваш священный жезл."
    helen "Не сдерживайтесь."
    helen "Я хочу почувствовать всё ваше благословенное семя внутри себя."
    hide player
    if M_helen.is_set("corset lingerie"):
        show helen 61
    else:

        show helen 60
    with dissolve

    if not M_helen.is_state(S_helen_master_servant_fun):
        helen "Боже..."
        helen "Ваш...член..."
        helen "В прошлый раз я не успела рассмотреть его."
        helen "Воистину, {b}Господь{/b} благословил вас"
    else:

        pause

    scene mia_house_helen_bed1 with fade
    hide helen
    show helens 22
    if M_helen.is_set("corset lingerie"):
        show h_corset 22b
    with dissolve

    if M_helen.is_state(S_helen_master_servant_fun):
        helen "Не перестаю поражаться размеру вашего члена."
        helen "{b}Господь{/b} воистину благословил вас."

    helen "Будьте нежны со мной...поначалу."
    pause
    show helens 23
    if M_helen.is_set("corset lingerie"):
        show h_corset 23b
    with dissolve

    helen "Ооох!!! {b}[firstname]{/b}!"
    helen "Не так глубоко!"
    helen "Я не ожидала, что ваш член настолько большой."
    helen "Но мне так нравится..."
    return

label helen_bedroom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("helens", [23,24,25,26,27], M_helen) as helens
            if M_helen.is_set("corset lingerie"):
                show expression AnimatedImage("h_corset", ["23b","24b","25b","26b","27b"], M_helen) as h_corset
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("helen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [23,24,25,26,27]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                if M_helen.is_set("corset lingerie"):
                    show expression "h_corset {}b".format(pose_list[pose_counter]) as h_corset
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("helen_hscene_dialog")
        $ animcounter += 1

    helen "Я...уже..."
    call screen helen_bedroom_sex_options

label helen_hscene_dialog:
    if animcounter == 1:
        helen "Ааааах!!!{p=1}{nw}"

    elif animcounter == 3:
        helen "{b}[firstname]{/b}!!!{p=1}{nw}"
        player_name "Оооох...{p=1}{nw}"
    return

label helen_bedroom_sex_cum:
    call expression game.dialog_select("helen_bedroom_sex_cum_intro")
    if not M_helen.is_state(S_helen_master_servant_fun):
        $ game.timer.tick()
        call expression game.dialog_select("helen_bedroom_sex_cum_repeat")
    else:

        $ player.go_to(L_miahouse_upstairs)

        show player 13

    call expression game.dialog_select("helen_bedroom_sex_cum_after")
    $ persistent.cookie_jar["Helen"]["unlocked"] = True
    $ persistent.cookie_jar["Helen"]["gallery"]["02_unlocked"] = True
    $ M_helen.trigger(T_helen_master_servant_sex)
    pause
    jump expression game.dialog_select("mias_upstairs")

label helen_bedroom_sex_cum_intro:
    helen "Кончайте, {b}[firstname]{/b}! Пронзайте меня глубже своим членом!"
    show helens 28
    if M_helen.is_set("corset lingerie"):
        show h_corset 28b
    with flash
    player_name "ААААХ!!!"
    helen "ООООХ!!!"
    show helens 29
    if M_helen.is_set("corset lingerie"):
        show h_corset 29b
    with dissolve
    pause
    helen "Я чувствую ваше божественное семя, заполняющее меня..."
    show helens 30
    if M_helen.is_set("corset lingerie"):
        show h_corset 30b
    with dissolve
    pause
    show helens 31
    if M_helen.is_set("corset lingerie"):
        show h_corset 31b
    with dissolve
    pause
    show helens 32
    if M_helen.is_set("corset lingerie"):
        show h_corset 32b
    with dissolve
    pause
    helen "Благодарю вас, {b}Господин{/b}."
    scene black with fade
    hide helens
    hide h_corset
    pause

    scene mia_house_helen_c with fade
    show player 13 at left
    if M_helen.is_set("corset lingerie"):
        show helen 63 at right
    else:

        show helen 65 at right
    with dissolve
    helen "Мне нужно исповедоваться, {b}Господин{/b}."
    helen "Я ждала вас весь день."
    helen "Я рада, что вы решили очистить меня..."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 26
    player_name "Да... Мне очень понравилось заниматься...этим...с тобой."
    show player 13
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Вы вернётесь завтра?"
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 10
    player_name "Может быть..."
    show player 35
    player_name "Если в школе не дадут много домашки..."
    return

label helen_bedroom_sex_cum_repeat:
    show player 29 with dissolve
    player_name "...но сделай одолжение, не рассказывай никому, чем мы здесь занимались"
    player_name "Я не хочу, чтобы {b}Мия{/b} знала об этом."
    show player 13 with dissolve
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Не волнуйся за мою дочь. Она всё поймёт."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 11
    player_name "..."
    return

label helen_bedroom_sex_cum_after:
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Не заставляйте меня ждать слишком долго."
    helen "Моё тело будет с нетерпением ждать вас."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 10
    player_name "Хорошо."
    show player 36 with dissolve
    player_name "Ну, мне пора."
    show player 13 with dissolve
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "До свидания, {b}Господин{/b}."
    helen "Спасибо за то, что одарили меня своим священным семенем."
    scene black
    hide player
    hide helen
    with fade
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
