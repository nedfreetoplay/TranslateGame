label dianes_dialogue_breastfeed:
    if store._in_replay:
        scene expression L_diane_barn_interior.background_blur
    show player 14 at left
    show diane b_naked a_naked_sides f_smirk
    player_name "Могу я попробовать еще вашего молока?"
    show player 13
    show diane f_laugh
    dia "Хочешь еще одну дозу прямо из крана?"
    show diane f_smirk
    show player 17
    player_name "Да, пожалуйста!"
    show player 13
    show diane f_smirk_talk
    dia "Хмм, хорошо."
    dia "Просто помни, не пить слишком много, хорошо?"
    show diane f_smirk
    show player 14
    player_name "Ага, я помню!"
    hide player
    hide diane
    with dissolve
    if M_diane.is_set("first boobjob"):
        jump diane_first_breastfeed
    jump diane_repeatable_breastfeed

label diane_repeatable_breastfeed:
    if L_diane_shed.is_here(M_diane):
        scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    else:
        scene expression "backgrounds/location_barn_hay_stack.jpg"
    if store._in_replay is not None:
        scene expression "backgrounds/location_barn_hay_stack.jpg"
    if M_diane.outfit == "shirtless":
        $ M_diane.is_naked = 0
    show diane b_hay_feeding a_hay_feeding_arm f_hay_feeding_explain
    with dissolve
    dia "Ммм, этот теплый рот чувствует себя так хорошо после дня накачки."
    show diane f_hay_feeding_lip_bite
    pause
    show diane f_hay_feeding_explain
    dia "Как сегодня на вкус, жеребец?"
    show diane f_hay_feeding_smirk_down
    player_name "Ммммм!"
    show diane f_hay_feeding_laugh
    dia "Хехехе!"
    show diane f_hay_feeding_smirk_down
    pause
    show diane f_hay_feeding_explain
    dia "Мы не должны делать это, но по какой-то причине ..."
    dia "... Это просто заставляет меня хотеть сделать это еще больше!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane b_hay_feeding1 a_empty with dissolve
    dia "Нггхх!"
    show diane f_hay_feeding_shamed_talk_look
    dia "Хорошо, нам лучше остановиться, прежде чем ты выпьешь меня насухо, жеребец."
    show diane f_hay_feeding_smirk_down
    player_name "Ауу."
    show diane f_hay_feeding_explain
    dia "Я знаю..."
    show diane f_hay_feeding_shamed_talk_look
    dia "Мы сделаем это снова в другой день, хорошо?"
    show diane f_hay_feeding_smirk_down
    player_name "Да, хорошо."
    show playersex 1 at right
    if M_diane.outfit == "shirtless":
        show diane f_hay_feeding_smirk_front b_hay_undress1
    else:
        show diane f_hay_feeding_smirk_front b_hay_sit
    with dissolve
    pause
    if M_diane.is_set("first cucumber"):
        $ M_diane.set("first cucumber", False)
        if M_diane.outfit == "shirtless":
            $ M_diane.is_naked = 1

        show diane f_hay_feeding_smirk_front_talk
        dia "У тебя все еще стояк?"
        if M_diane.outfit == "shirtless":
            show diane b_hay_dressed f_hay_feeding_smirk_front with dissolve
        else:
            show diane f_hay_feeding_smirk_front
        player_name "Ух."
        show diane f_hay_feeding_smirk_front_talk
        dia "Почему бы тебе не достать этот большой член для меня?"
        show diane f_hay_feeding_smirk_front
        player_name "Хорошо."
        show playersex 2 with dissolve
        show diane f_hay_feeding_down_front
        pause
        show playersex 4 with dissolve
        pause 1
        show playersex 3 with dissolve
        pause
        show diane f_hay_feeding_smirk_front_talk
        dia "Прекрасно!"
        if M_diane.outfit == "shirtless":
            dia "Мой черед."
            show diane f_hay_feeding_smirk_down b_hay_undress1 with dissolve
            pause
            show diane b_hay_undress2 with dissolve
            pause
            show diane b_hay_naked with dissolve
        dia "Теперь позволь мне просто-"
        hide playersex
        show diane b_hay_rub f_hay_feeding_lip_bite a_empty
        player_name "!!!" with hpunch
        player_name "О, боже!"
        pause
        pause
        show diane b_hay_sit f_hay_feeding_smirk_front
        show playersex 3
        with dissolve
        player_name "Как думаешь, мы могли бы сделать это снова?"
        player_name "Ты знаешь, твои сиськи и мой... Ух..."
        show diane f_hay_feeding_smirk_front_talk
        dia "Хочешь еще трах сиськами?"
        show diane f_hay_feeding_smirk_front
        player_name "Да, трах сиськами!"
        show diane f_hay_feeding_laugh
        dia "Хехе."
        show diane f_hay_feeding_smirk_front_talk
        dia "Ну, мы могли..."
        show diane f_hay_feeding_smirk_front
        pause
        show diane f_hay_feeding_smirk_front_talk
        dia "... Или, может быть, вы могли бы позаботиться о моих потребностях сегодня?"
        show diane f_hay_feeding_smirk_front
        player_name "Хух?"
        player_name "Хорошо, конечно."
        show diane f_hay_feeding_smirk_front_talk
        dia "Хороший мальчик!"
        show diane f_hay_feeding_smirk_front
        player_name "Что ты хочешь, чтобы я сделал?"
        show diane f_hay_feeding_smirk_front_talk
        dia "Ну, посмотрим..."
        show diane f_hay_feeding_thinking
        pause
        show diane f_hay_feeding_smirk_front_talk
        dia "О, я знаю!"
        show diane f_hay_feeding_smirk_front b_hay_cucumber1 with dissolve
        player_name "Ах, огурец?"
        show diane f_hay_feeding_smirk_front_talk
        dia " Да ладно, не прикидывайся дурачком."
        dia "Я знаю, что ты видел меня на кухне в тот день."
        show diane f_hay_feeding_smirk_front
        player_name "Да, но ты хочешь, чтобы я ... -"
        show diane f_hay_feeding_laugh
        dia "Мммммм!"
        show diane f_hay_feeding_smirk_front
        pause
        player_name "Хорошо."
        show diane b_hay_cucumber2 with dissolve
        pause
        show diane hay_behind_talk
        show playersex 18
        with dissolve
        dia "Будь нежным, хорошо?"
        show diane hay_behind
        player_name "Хорошо."
        show diane hay_behind_pre with dissolve
        pause
        hide playersex
        show diane hay_insert1
        with dissolve
        player_name "Так?"
        dia "Ммм, вот так!"
        hide diane
        jump diane_cucumber_start
    else:

        if M_diane.outfit == "shirtless":
            show diane b_hay_dressed with dissolve

        menu:
            "Трах сиськами.":
                show playersex 1 at right
                show diane f_hay_feeding_smirk_front
                with dissolve
                player_name "Как ты думаете, мы могли бы сделать трах сиськами еще раз?"
                show diane f_hay_feeding_smirk_front_talk
                dia "Конечно, мы можем."
                dia "Снимай штаны и садись сюда."
                show playersex 2
                if M_diane.outfit == "shirtless":
                    show diane f_hay_feeding_smirk_down b_hay_undress1
                else:
                    show diane f_hay_feeding_down_front
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit == "shirtless":
                    show diane b_hay_undress2 f_hay_feeding_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                hide diane
                hide playersex

                scene expression "backgrounds/location_barn_floor_boobjob.jpg"
                if M_diane.outfit == "shirtless":
                    $ M_diane.is_naked = 1
                show diane_sex_boobjob 2
                show diane_sex_boobjob_look talk
                with dissolve
                dia "Тебе правда это нравится, да?"
                hide diane_sex_boobjob_look

                jump diane_boobjob_start
            "Огурец.":

                show playersex 1 at right
                show diane f_hay_feeding_smirk_front
                with dissolve
                player_name "Хочешь снова использовать огурец?"
                show diane f_hay_feeding_smirk_front_talk
                dia "О, определенно!"
                show playersex 2
                if M_diane.outfit == "shirtless":
                    show diane f_hay_feeding_smirk_down b_hay_undress1
                else:
                    show diane f_hay_feeding_down_front
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit == "shirtless":
                    show diane b_hay_undress2 f_hay_feeding_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                    $ M_diane.is_naked = 1
                show diane f_hay_feeding_smirk_front_talk b_hay_cucumber1 with dissolve
                dia "Просто будь нежнее, хорошо?"
                show playersex 18
                show diane hay_behind
                with dissolve
                player_name "Хорошо."
                show diane hay_behind_pre with dissolve
                player_name "Вот и он..."
                hide playersex
                show diane hay_insert1
                with dissolve
                pause
                hide diane
                jump diane_cucumber_start
            "Мне лучше вернуться к работе.":

                if store._in_replay is None:
                    scene expression player.location.background_blur with None
                else:
                    scene expression L_diane_shed.background_blur with None
                if M_diane.outfit == "shirtless":
                    $ M_diane.is_naked = 1
                    show diane b_topless a_naked_sides f_smirk_talk
                else:
                    show diane b_naked a_naked_sides f_smirk_talk
                show player 13 at left
                with dissolve
                dia "А теперь верни свою милую задницу к работе!"
                show diane f_smirk
                show player 14
                player_name "Да, мэм!"
                hide player
                hide diane
                with dissolve
    $ game.main()

label diane_cucumber_start:
    if store._in_replay is not None:
        scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
        $ M_diane.is_naked = True
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .4)
    show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
    dia "Ааааа!!"
    player_name "Вау, ты и правда мокрая, {b}Диана{/b}!"
    jump diane_cucumber_loop

label diane_cucumber_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_hay_insert {}".format(pose_list[pose_counter]) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
        $ animcounter += 1
    call screen diane_cucumber_options

label diane_cucumber_cum:
    dia "Я почти..!"
    if randomizer() < 50:
        dia "Не останавливайся!"
    else:
        dia "Трахни меня!"
    pause
    dia "НГГХХХХ!!!" with flash
    hide diane_hay_insert
    show diane hay_insert1
    with dissolve
    dia "Аааа... Аааа..."
    show playersex 18
    show diane hay_behind_pre
    with dissolve
    pause
    show diane hay_behind_talk with dissolve
    dia "О, это было прекрасно {b}[firstname]{/b}!"
    show diane hay_behind
    if randomizer() < 50:
        player_name "Хе-хе, ты кончила очень тяжело!"
        show diane hay_behind_talk
        dia "Верно, хехе!"
    else:
        player_name "Хе-хе, да, это было весело!"
        player_name "Ты дрожала как сумасшедшая в конце."
        show diane hay_behind_talk
        dia "Хехе!"
    dia "Это потому, что ты так заботишься обо мне."
    show diane hay_behind
    pause
    show diane hay_behind_talk
    dia "Кстати, спасибо тебе за это."
    show diane hay_behind
    player_name "Без проблем."
    show diane hay_behind_talk
    dia "Хаах... Мне нужно немного отдохнуть."
    dia "Ты не против вернуться к работе?"
    show diane hay_behind
    player_name "Конечно."
    show diane hay_behind_talk
    dia "Хороший мальчик."
    show diane hay_behind
    hide playersex with dissolve
    pause
    show diane hay_behind_pre with dissolve
    dia "Уф!"
    dia "Это было круто!"
    hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_cucumber_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        dia "О, боже!{p=1}{nw}"
    if animcounter == 0 and randomizer() < 25:
        dia "Ааа!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        dia "Да!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        dia "Ммм, вот так {b}[firstname]{/b}!{p=1}{nw}"
        dia "Трахни меня этим огурцом!{p=2}{nw}"
    if animcounter == 2 and randomizer() < 25:
        dia "Глубже, {b}[firstname]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 25:
        dia "Ты непослушный мальчишка!{p=1}{nw}"
        player_name "Хех.{p=1}{nw}"
    if animcounter == 3 and randomizer() > 75:
        dia "Аааа!!{p=1}{nw}"
        dia "Я почти...{p=2}{nw}"
    if animcounter == 3 and randomizer() > 75:
        dia "Быстрее!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.21:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.1)
        dia "Ааа!!{p=1}{nw}"
    return

label diane_first_breastfeed:

    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding a_hay_feeding_arm f_hay_feeding_explain
    with dissolve
    dia "Ммм, этот теплый рот чувствует себя так хорошо после дня накачки."
    show diane f_hay_feeding_lip_bite
    pause
    show diane f_hay_feeding_explain
    dia "Как сегодня на вкус, жеребец?"
    show diane f_hay_feeding_smirk_down
    player_name "Ммммм!"
    show diane f_hay_feeding_laugh
    dia "Хехехе!"
    show diane f_hay_feeding_smirk_down
    pause
    show diane f_hay_feeding_explain
    dia "Мы не должны этого делать, но по какой-то причине..."
    dia "... Это просто заставляет меня хотеть сделать это еще больше!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane b_hay_feeding1 a_empty with dissolve
    dia "Нггхх!"
    show diane f_hay_feeding_shamed_talk_look
    dia "Ладно, нам лучше остановиться, пока ты не выпил меня досуха, жеребец."
    show diane f_hay_feeding_smirk_down
    player_name "Ауу."
    show diane f_hay_feeding_explain
    dia "Я знаю..."
    show diane f_hay_feeding_shamed_talk_look
    dia "Мы повторим это в другой раз, хорошо?"
    show playersex 1 at right
    if M_diane.outfit == "shirtless":
        show diane f_hay_feeding_smirk_down b_hay_undress1
    else:
        show diane f_hay_feeding_smirk_front b_hay_sit
    with dissolve
    player_name "Есть ли что-нибудь еще, что мы можем сделать?"
    if M_diane.outfit == "shirtless":
        show diane b_hay_dressed f_hay_feeding_smirk_front_talk with dissolve
    else:
        show diane f_hay_feeding_smirk_front_talk
    dia "Например?"
    show diane f_hay_feeding_smirk_front
    player_name "Я не знаю..."
    player_name "... Я просто такой возбужденный!"
    show diane f_hay_feeding_laugh
    dia "Хе-хе, я знаю, красавчик, я тоже ..."
    show diane f_hay_feeding_smirk_front
    pause
    show diane f_hay_feeding_smirk_front_talk
    dia "Хорошо, почему бы тебе не вытащить его для меня?"
    dia "Дай мне хорошенько на него взглянуть."
    show diane f_hay_feeding_smirk_front
    pause
    player_name "Хорошо."
    show playersex 2 with dissolve
    show diane f_hay_feeding_down_front
    pause
    show playersex 4 with dissolve
    pause 1
    show playersex 3 with dissolve
    pause
    show diane f_hay_feeding_surprised_front_talk
    dia "Ммм, Боже милостивый..."
    dia "Это что-то особенное!"
    show diane f_hay_feeding_surprised_front
    player_name "Да?"
    show diane f_hay_feeding_smirk_front
    dia "Мммммм."
    pause
    if M_diane.outfit == "shirtless":
        $ M_diane.is_naked = 1
        show diane f_hay_feeding_smirk_front_talk
        dia "Полагаю, теперь моя очередь, да?"
        show diane f_hay_feeding_smirk_down b_hay_undress1 with dissolve
        pause
        show diane b_hay_undress2 with dissolve
        player_name "Вау!"
        show diane b_hay_naked f_hay_feeding_laugh with dissolve
        dia "Хехехе, тебе нравится?"
        show diane f_hay_feeding_smirk_front
    player_name "Ты такая красивая, {b}Диана{/b}!"
    show diane f_hay_feeding_smirk_front_talk
    dia "О, я не настолько красива..."
    show diane f_hay_feeding_smirk_front
    player_name "Да, это так!"
    show diane f_hay_feeding_smirk_front_talk
    dia "Ччч, такая очаровашка..."
    show diane f_hay_feeding_smirk_front
    player_name "Итак, что же мы будем делать-"
    hide playersex
    show diane b_hay_rub f_hay_feeding_lip_bite a_empty
    player_name "!!!" with hpunch
    player_name "О, боже!"
    pause
    pause
    if M_diane.outfit == "shirtless":
        player_name "Могу я положить его внутрь, {b}Диана{/b}?"
        show playersex 3 at right
        show diane b_hay_naked f_hay_feeding_shamed_front_talk
        with dissolve
        dia "Нгг, нет..."
        show diane f_hay_feeding_shamed_front
        player_name "Почему?"
        show diane f_hay_feeding_shamed_front_talk
        dia "{b}[firstname]{/b}, ты знаешь почему..."
        dia "Мы не можем..."
        show diane f_hay_feeding_shamed_front
        player_name "{b}*вздыхая*{/b} Но я так сильно этого хочу!"
        show diane f_hay_feeding_shamed_front_talk
        dia "Я знаю, милый..."
        show diane f_hay_feeding_shamed_front
        pause
        show diane f_hay_feeding_smirk_front_talk
    else:
        show playersex 3 at right
        show diane b_hay_sit f_hay_feeding_smirk_front_talk
        with dissolve
    dia "Садись сюда."
    show diane f_hay_feeding_smirk_front
    player_name "Хмм?"
    show diane f_hay_feeding_smirk_front_talk
    dia "Давай."
    dia "Я позабочусь об этом для тебя."
    show diane f_hay_feeding_smirk_front
    player_name "Хорошо..."
    hide diane
    hide playersex
    scene expression "backgrounds/location_barn_floor_boobjob.jpg"
    if M_diane.outfit == "shirtless":
        $ M_diane.is_naked = 1
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    dia "Тебе нравится моя грудь не так ли?"
    show diane_sex_boobjob_look
    player_name "Конечно!"
    show diane_sex_boobjob_look talk
    dia "Я покажу тебе кое-что особенное..."
    show diane_sex_boobjob_look
    player_name "Что ты-"
    hide diane_sex_boobjob_look
    jump diane_boobjob_start

label diane_boobjob_start:
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .25)
    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
    player_name "Аааа!" with hpunch
    dia "Тебе это нравится?"
    player_name "Да!!"
    label diane_boobjob_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    $ animated = True
                pause 5
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                $ pose_list = [1,2,3,2]
                $ poses_done = []
                while poses_done != pose_list:
                    show expression "diane_sex_boobjob {}".format(pose_list[pose_counter]) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
            $ animcounter += 1
        call screen diane_boobjob_options

label diane_boobjob_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        player_name "Боже мой, это потрясающе!{p=2}{nw}"
        dia "Хехехе!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 90:
        player_name "Где ты этому научилась?{p=2}{nw}"
        dia "Хмм?{p=1}{nw}"
        dia "О, ммм... На самом деле, это была {b}[deb_name]{/b} кто показала мне как это делать...{p=2}{nw}"
        dia "Back when we were young and wild.{p=2}{nw}"
        player_name "Что?!{p=1}{nw}"
        player_name "{b}[deb_name]{/b} научила тебя этому?!{p=2}{nw}"
        dia "Хехе, что?{p=1}{nw}"
        dia "Вы не думали, что {b}[deb_name]{/b} была девственницей?{p=2}{nw}"
        player_name "Ну, нет.{p=1}{nw}"
        player_name "Я только не...{p=1}{nw}"
        player_name "Ааа!!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 75:
        player_name "Ммм, это так круто!{p=2}{nw}"
    if animcounter == 2 and randomizer() > 90:
        dia "Тебе правда нравится трахать мои сиськи, правда, красавчик?{p=2}{nw}"
        player_name "Да!{p=1}{nw}"
        dia "Хехе!{p=1}{nw}"
    else:
        dia "Тебе нравится, как мои сиськи обвиваются вокруг твоего члена?{p=2}{nw}"
        player_name "Да!{p=1}{nw}"
    if animcounter == 2 and randomizer() < 10:
        dia "Мне нравится чувствовать твой большой твердый член между моих сисек...{p=2}{nw}"
        player_name "Мне тоже!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 75:
        player_name "Я уже близко...{p=2}{nw}"
    return

label diane_boobjob_cum:
    player_name "Я уже близко, {b}Диана{/b}!"
    dia "Все в порядке, красавчик."
    dia "Выпусти её."
    pause
    show diane_sex_boobjob cum
    show diane_sex_boobjob_cum
    player_name "ХННГГГГ!!!" with flash
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    dia "Хороший мальчик!"
    show diane_sex_boobjob_look
    pause
    player_name "Ааааа... Ааааа..."
    pause
    show diane_sex_boobjob_look talk
    dia "Хехехе!"
    scene black with fade
    hide diane_sex_boobjob_look
    hide diane_sex_boobjob
    if store._in_replay is None:
        scene expression player.location.background_blur with None
    else:
        scene expression L_diane_barn_interior.background_blur with None
    if M_diane.is_set("first boobjob"):
        $ M_diane.set("first boobjob", False)
        show player 261bf at left
        show diane b_naked a_naked_sides f_down_front o_boob_cum
        with dissolve
        pause
        show player 14 with dissolve
        show diane f_smirk
        player_name "Это было потрясающе!"
        show player 13
        show diane f_smirk_talk
        dia "Теперь ты чувствуешь себя лучше?"
        show diane f_smirk
        show player 17
        player_name "Определенно!"
        show player 13
        show diane a_naked_touch_cum f_down_front with dissolve
        pause
        show diane a_naked_lick_cum f_lick_finger with dissolve
        show player 11
        player_name "!!!"
        show diane f_smirk a_naked_sides with dissolve
        show player 10
        player_name "Ты только-"
        show player 5
        show diane f_laugh
        dia "Хехехе!"
        show diane f_smirk_talk
        dia "Ты пил мое молоко, будет справедливо, если я попробую твое."
        show diane f_smirk
        show player 14
        player_name "... Ну?"
        show player 13
        show diane f_smirk_talk
        dia "Не плохо."
        show diane f_smirk
        pause
        show diane f_smirk_talk
        dia "Я не думаю, что мы получим какие-либо заказы на это..."
        show diane f_cheese
        show player 17
        player_name "Хаха!"
        show player 14
        player_name "Да, наверное, нет."
        show player 13
        show diane f_smirk_talk
        dia "Ладно, нам действительно пора возвращаться к работе."
        dia "... И мне нужно привести себя в порядок!"
        show diane f_smirk
        show player 14
        player_name "Да, хорошо {b}Диана{/b}."
        player_name "Я буду в саду, если понадоблюсь."
        show player 13
        show diane f_smirk_talk
        dia "Спасибо, {b}[firstname]{/b}."
        show diane f_smirk
        hide player with dissolve
        pause
        show diane a_naked_touch_cum f_down_front with dissolve
        pause
        show diane a_naked_lick_cum f_lick_finger with dissolve
        dia "Ммм!"
        hide diane with dissolve
    else:
        if M_diane.outfit == "shirtless":
            $ M_diane.is_naked = 1
        show player 261bf at left
        show diane b_naked a_naked_sides f_down_front o_boob_cum
        with dissolve
        pause
        show player 14
        show diane f_smirk
        player_name "Уф!"
        player_name "Спасибо, {b}Диана{/b}."
        player_name "Мне действительно это было нужно."
        show player 13
        show diane f_smirk_talk
        dia "С удовольствием, жеребец."
        dia "А теперь возвращайся к работе, ладно?"
        show diane f_smirk
        show player 14
        player_name "Да, хорошо."
        hide player with dissolve
        pause
        show diane a_naked_touch_cum f_down_front with dissolve
        pause
        show diane a_naked_lick_cum f_lick_finger with dissolve
        dia "Ммм, вкусно!"
        show diane a_naked_sides f_cheese with dissolve
        dia "Хехе!"
        hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["04_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_sex_breed_start:
    if store._in_replay:
        scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ diane_sex_position = "back"
    $ anim_toggle = True
    $ animated = True
    $ M_diane.outfit = "cow"
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    jump diane_sex_breed_loop

label diane_sex_breed_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression AnimatedImage("diane_sex_front", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression "diane_sex_front {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression "diane_sex_back {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
        $ animcounter += 1
    call screen diane_sex_breed_options

label diane_sex_breed_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        if randomizer() > 50:
            dia "О, да!{p=1}{nw}"
            dia "Так глубоко!{p=1}{nw}"
        else:
            if M_diane.pregnancy.number_of_babies>0:
                dia "О, я так хочу еще одного ребенка, {b}[firstname]{/b}.{p=2}{nw}"
            else:
                dia "О, я так сильно хочу твоего ребенка, {b}[firstname]{/b}.{p=2}{nw}"
            dia "Засунь его в меня, пожалуйста!{p=2}{nw}"
    if animcounter == 0 and randomizer() > 90:
        dia "Да, {b}[firstname]{/b}!{p=1}{nw}"
        dia "Трахни меня, как животное!{p=1}{nw}"
    if animcounter == 1 and randomizer() < 25:
        dia "Мой бык!{p=1}{nw}"
        dia "Мой большой сильный бык!{p=2}{nw}"
    if animcounter == 1 and randomizer() < 25:
        if randomizer() > 50:
            dia "О, это так замечательно!{p=1}{nw}"
        else:
            dia "У тебя такой большой, {b}[firstname]{/b}!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Пф, это потрясающе {b}Диана{/b}!{p=2}{nw}"
            dia "Мммммм!{p=1}{nw}"
        else:
            dia "Да!{p=1}{nw}"
            dia "О боже, да!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 90:
        player_name "Мычи для меня.{p=1}{nw}"
        dia "Что?{p=1}{nw}"
        pause 1
        player_name "Ты хочешь, чтобы тебя трахнули как животное, не так ли?{p=2}{nw}"
        dia "О боже, да!{p=1}{nw}"
        player_name "Тогда мычи для меня.{p=1}{nw}"
        pause 1
        dia "... Муу?{p=1}{nw}"
        player_name "Ты можешь лучше...{p=2}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        dia "Муууу!{p=1}{nw}"
        player_name "Громче, {b}Диана{/b}!{p=1}{nw}"
        dia "Муууу!!{p=1}{nw}"
        player_name "Громче!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        dia "О, черт!{p=1}{nw}"
        player_name "Мычи для меня!{p=1}{nw}"
        dia "МУУУУ!!!{p=1}{nw}"
        pause 1
        dia "МУУУУУУУУУУУ!!!{p=1}{nw}"
    if animcounter == 3 and randomizer() > 75:
        if randomizer() > 50:
            dia "Вот так!{p=1}{nw}"
            dia "Трахни меня, жеребец!{p=1}{nw}"
        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        if randomizer() > 50:
            dia "Ооо! Оооо!!{p=1}{nw}"
            pause 1
            dia "ООООО, БОЖЕ!!!{p=1}{nw}"
        else:
            dia "Ааааааа!!!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        if randomizer() < 50:
            dia "Так хорошо!{p=1}{nw}"
            pause 1
            dia "Ох, это так чертовски хорошо!{p=1}{nw}"
        else:
            dia "Наполни меня до краев, жеребец!{p=1}{nw}"
    if animcounter == 4 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Вау, {b}Диана{/b}, ты такая мокрая!{p=1}{nw}"
            pause 1
            dia "Я знаю!{p=1}{nw}"
            dia "Мое тело любит твой член!{p=1}{nw}"
        else:
            dia "Давай, {b}[firstname]{/b}!{p=1}{nw}"
            dia "Осемени меня!{p=1}{nw}"
    return

label diane_sex_breed_cum_pre:
    player_name "{b}Диана{/b} я кончаю!"
    dia "Ааа, яяяя  ттттоооожжжжееее!!!"
    pause
    if randomizer() < 50:
        dia "Кончи в меня, {b}[firstname]{/b}!"
        if M_diane.pregnancy.number_of_babies>0:
            dia "Я хочу еще одного ребенка внутри себя!"
        else:
            dia "Я хочу, чтобы твой ребенок был внутри меня!"
    else:
        dia "Кончи в меня, {b}[firstname]{/b}!"
        dia "Я хочу все!"
    player_name "Ох, боже!"
    pause
    if store._in_replay is None:
        $ M_diane.trigger(T_diane_brought_outfit_package)
    call screen diane_cum_breed_options 

label diane_sex_breed_cum_out:
    player_name "Я не..."
    $ M_diane.set('sex speed', 0.09)
    pause
    player_name "Я не могу..."
    pause
    dia "АААААААА!!!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed after
    show diane_sex_breed_mc cumshot 2
    player_name "ННГГГГ!!!" with flash
    show diane_sex_breed_mc cumshot 1
    show diane_sex_flying_cum 1
    with dissolve
    pause 1
    show diane_sex_flying_cum 2
    with dissolve
    pause
    player_name "Ааааа... Ааааа..."
    dia "Что-"
    pause
    hide diane_sex_flying_cum
    hide diane_sex_breed_mc
    hide diane_sex_breed
    with dissolve
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 368 at left
    show diane b_naked a_naked_sides f_sad_talk
    with dissolve
    if randomizer() < 50:
        dia "... Что случилось?"
        dia "{b}[firstname]{/b}, ты должен был кончить в меня..."
        show diane b_naked a_naked_sides f_sad
        show player 367
        player_name "Я знаю."
        show player 368
        pause
        show player 367
        player_name "Я знаю..."
        player_name "Прости."
        player_name "Настал момент, и я просто ..."
        show player 368
        pause
        show player 367
        player_name "Уф, я не знаю."
        player_name "Я кончу в тебя в следующий раз, ладно?"
        show player 368
        pause
        if M_diane.pregnancy.number_of_babies>0:
            show diane f_shamed_talk_smile
            dia "Хорошо..."
        else:
            show diane f_sad_talk
            dia "Ты должен помнить, есть причина, по которой мы это делаем..."
            show diane f_shamed
            show player 367
            player_name "Я знаю."
            show player 368
        show diane f_normal_talk
        dia "Это было невероятно, хотя!"
    else:
        dia "Ты вытащил!"
        show diane f_sad
        show player 367
        player_name "Я знаю."
        show player 368
        show diane f_sad_talk
        dia "Почему ты-"
        dia "{b}[firstname]{/b}, Я не могу забеременеть, если ты кончишь мне на спину!"
        show diane f_sad
        show player 367
        player_name "Прости."
        player_name "Я просто не мог на этот раз ..."
        show player 368
        pause
        show diane f_sad_talk
        dia "Все в порядке."
        dia "Я не сумасшедшая."
        if M_diane.pregnancy.number_of_babies>0:
            show diane f_sad
            show player 367
        else:
            dia "Ты просто должен помнить, почему мы делаем это."
            show diane f_sad
            pause
            show diane f_normal_talk
            dia "Не пойми меня неправильно, мне очень нравится трахать тебя, {b}[firstname]{/b}..."
            show diane f_sad_talk
            dia "... Но если я не забеременею, бизнес пострадает."
            show diane f_sad
            show player 367
            player_name "Я знаю."
        player_name "Прости."
        hide player
        show diane kiss_both_naked at Position (xoffset=-217)
        with dissolve
        player_name "!!!"
        pause
        show player 366 at left
        show diane b_naked a_naked_sides f_normal_talk
        with dissolve
        dia "Не извиняйся."
        show diane f_smirk_talk
        if M_diane.pregnancy.number_of_babies>0:
            dia "В следующий раз положи в меня еще одного ребенка!"
        else:
            dia "В следующий раз положи в меня ребенка!"
        dia "Хорошо?"
        show diane f_smirk
        show player 365
        player_name "Хорошо..."
        show player 366
        show diane f_smirk_talk
        dia "Теперь давай начнем дойку."
        show diane f_smirk
        show player 365
        player_name "Да, мэм."
        show player 366
        show diane f_smirk_talk
        dia "Просто будь нежным, {b}[firstname]{/b}."
        hide player
        hide diane
        with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    jump milking_game_pre_after_sex

label diane_sex_breed_cum_in:
    player_name "Ооо!"
    pause
    player_name "Here it comes!"
    dia "Наполни меня, {b}[firstname]{/b}!!"
    pause
    dia "ААААААААААА!!!"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_diane.set("sex speed",0.4)
    show diane_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (xpos=440,ypos=680)
    player_name "ХННГГГГГ!!!" with flash
    hide xray_diane_back
    show diane_sex_breed creampie_pullout
    with dissolve
    dia "НГГХХХХ!!!"
    show diane_sex_breed insert_and_pullout
    show diane_sex_dick_cum 2 zorder 3
    with dissolve
    pause
    show diane_sex_breed after
    show diane_sex_cum zorder 1
    show diane_sex_breed_mc zorder 2
    show diane_sex_dick_cum 1
    with dissolve
    pause
    show diane_sex_breed after_spread
    show diane_sex_cum spread
    with dissolve
    player_name "Ааааа... Аааааа..."
    pause
    dia "О, БОЖЕ!"
    pause
    dia "ТАк много..."
    pause
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["06_unlocked"] = True
    $ renpy.end_replay()
    call screen pregnancy_minigame(return_label="diane_sex_breed_cum_in_after_minigame", machine=M_diane)

label diane_sex_breed_cum_in_after_minigame:
    hide diane_sex_cum
    hide diane_sex_breed
    hide diane_sex_dick_cum
    hide diane_sex_breed_mc
    with dissolve

    if M_diane.is_state(S_diane_milk_production_increase):
        $ M_diane.trigger(T_diane_breeding)

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 366 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    if randomizer() < 50 or M_diane.is_set("breed first time"):
        dia "Так много спермы, {b}[firstname]{/b}!"
        show diane f_smirk
        show player 365
        player_name "Прости."
        show player 366
        show diane f_smirk_talk
        dia "Нет, это замечательно!"
    else:
        dia "Ммм, Я люблю твои огромные загрузки, {b}[firstname]{/b}."
        show diane f_smirk
        show player 365
        player_name "Да?"
        show player 366
        show diane f_laugh
        dia "Они замечательны!"
    show diane f_smirk
    show player 365
    player_name "Хех."
    show player 366
    pause
    show player 365
    if M_diane.pregnancy.number_of_babies>0:
        player_name "Как ты думаешь, ты ... ты знаешь ... снова беременна?"
    else:
        player_name "Как ты думаешь, ты ... ты знаешь ... беременна?"
    show player 366
    show diane f_laugh
    dia "Ха-ха, еще слишком рано чтобы знать."
    show diane f_smirk_talk
    dia "Надеюсь, что да."
    show diane f_smirk
    pause
    show player 365
    player_name "У тебя может быть мой ребенок внутри, прямо сейчас!"
    show player 366
    show diane f_smirk_talk
    dia "Хехе, я знаю!"
    dia "Это так захватывающе!"
    dia "Ох, жеребец ... Ты был так хорош!"
    jump milking_game_pre_after_sex

label diane_debbie_sex_start:
    if store._in_replay:
        scene expression "backgrounds/location_home_debbiebed_sex.jpg"
    $ anim_toggle = True
    if not M_diane.is_set("3way first time"):
        $ M_diane.set('sex speed', 0.09)
    if not animated:
        show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
        $ animated = True

label diane_debbie_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_debbie_sex_bed {}".format(pose_list[pose_counter]) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
        $ animcounter += 1
    call screen diane_debbie_sex_options

label diane_debbie_sex_hscene_dialog:
    if not M_diane.get("change partner"):
        if animcounter == 0 and randomizer() < 25:
            dia "О БОЖЕ!{p=1}{nw}"
            dia "Не останавливайся!!{p=1}{nw}"
        if animcounter == 1 and randomizer() < 25:
            dia "О, черт!{p=1}{nw}"
            dia "Ааааа!{p=1}{nw}"
        if animcounter == 2 and randomizer() < 10:
            deb "Хехе, Мне нравится этот вид!{p=2}{nw}"
            dia "Извините, если я протеку на тебя...{p=2}{nw}"
            deb "Все хорошо, я не против.{p=2}{nw}"
        elif randomizer() < 25:
            dia "Боже мой, так глубоко!{p=2}{nw}"
            deb "У моего мальчика лучший член, не так ли?!{p=2}{nw}"
            dia "Да!!{p=1}{nw}"
        if animcounter == 3 and randomizer() < 25:
            player_name "Я близко...!{p=1}{nw}"
            dia "Ааа, я тоже!{p=1}{nw}"
            deb "Это хорошо, милый, давай!{p=2}{nw}"
    else:
        if animcounter == 0 and randomizer() < 25:
            dia "Давай, {b}[firstname]{/b}!{p=1}{nw}"
            dia "Трахни ее сильнее!{p=1}{nw}"
            if M_diane.get("sex speed") > 0.31:
                $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
            deb "О, боже!{p=1}{nw}"
        elif randomizer() < 50:
            deb "ААААА!!{p=1}{nw}"
            dia "Вот так, жеребец!{p=1}{nw}"
        if animcounter == 1 and randomizer() < 25:
            deb "Ааа!{p=1}{nw}"
        if animcounter == 2 and randomizer() < 25:
            dia "Как это так просто для тебя?!{p=2}{nw}"
            deb "Хмм?{p=1}{nw}"
            dia "Ты берешь этот огромный член, как будто это ничего!{p=2}{nw}"
            deb "Ммм, я не знаю...{p=1}{nw}"
            deb "... Это просто замечательно!{p=1}{nw}"
        if animcounter == 3 and randomizer() < 25:
            player_name "Я близко...!{p=1}{nw}"
            deb "Ааа, я тоже!{p=1}{nw}"
            dia "Давай, красавчик.{p=1}{nw}"
            dia "Покажи {b}[deb_name]{/b} как сильно ты ее любишь.{p=2}{nw}"
    return

label diane_debbie_sex_cum:
    player_name "Вот оно!"
    pause
    if M_diane.get("cum inside"):
        show diane_debbie_sex_bed cumpie
        if not M_diane.get("change partner"):
            show xray_diane_debbie_sex at Position (xpos=360,ypos=680)
        else:
            show xray_diane_debbie_sex at Position (xpos=380,ypos=750)
    else:
        show diane_debbie_sex_bed base
        show diane_debbie_sex_bed_cumshot_mc
    player_name "ХННГГГГ!!!" with flash
    if not M_diane.get("change partner"):
        dia "НГГХХХХ!!!"
    else:
        deb "ОООООО!!!"
    hide xray_diane_debbie_sex with dissolve
    pause
    player_name "Ааааа... Ааааа..."
    hide diane_debbie_sex_bed_cumshot_mc

    if not M_diane.get("change partner"):
        show diane_debbie_sex_bed diane_after_talk
        with dissolve
        dia "О, вау..."
        if M_diane.get("cum inside"):
            dia "Он так сильно вошел в меня."
            show diane_debbie_sex_bed debbie_after_talk
            deb "Хехе, это мой мальчик!"
            show diane_debbie_sex_bed diane_after_talk
            dia "Ммм."
        else:
            show diane_debbie_sex_bed debbie_after_talk
            deb "Так много!"
            show diane_debbie_sex_bed diane_after_talk
            dia "Блин, я покрыта!"
            dia "Хаха!"
    else:
        show diane_debbie_sex_bed debbie_after_talk
        with dissolve
        deb "О, мой..."
        if M_diane.get("cum inside"):
            deb "I feel so full."
            show diane_debbie_sex_bed diane_after_talk
            dia "Хехе, это мой большой сексуальный жеребец!"
            show diane_debbie_sex_bed debbie_after_talk
            deb "Ммм."
        else:
            show diane_debbie_sex_bed diane_after_talk
            dia "Так много!"
            show diane_debbie_sex_bed debbie_after_talk
            deb "Хехе!"
            deb "О, я люблю чувствовать это на себе!"

    if M_diane.is_set("3way first time"):
        show diane_debbie_sex_bed diane_after_talk
        dia "Я так рада, что это случилось!"
        show diane_debbie_sex_bed debbie_after_talk
        deb "Это было замечательно, не так ли?"
        player_name "Это было так здорово!"
        show diane_debbie_sex_bed diane_after_talk
        dia "Хехехе!"
        show diane_debbie_sex_bed debbie_after_talk
        deb "Хехехе!"
        player_name "Мы можем сделать это снова?!"
        show diane_debbie_sex_bed diane_after_talk
        dia "Я упала!"
        show diane_debbie_sex_bed debbie_after_talk
        deb "Конечно, мы можем повторить когда захочешь, {b}[firstname]{/b}."
        pause
        show diane_debbie_sex_bed debbie_after_talk
        deb "Прямо сейчас, я просто хочу, чтобы ты пришел и полежал с нами."
        show diane_debbie_sex_bed debbie_lounge_after_talk with dissolve
        deb "Я измотана!"
        show diane_debbie_sex_bed diane_lounge_after_talk
        dia "Ха, да... Я тоже!"
        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "Хехе."
        show diane_debbie_sex_bed debbie_lounge_after_talk
        deb "Иди сюда, милый!"
        deb "Ложись между нами."
        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "Хорошо."
    else:

        show diane_debbie_sex_bed diane_after_talk
        dia "Пфф."
        dia "Я так устала..."
        show diane_debbie_sex_bed debbie_after_talk
        deb "Ух, я тоже."
        deb "Нас двое и мы все еще не можем угнаться за ним!"
        show diane_debbie_sex_bed diane_after_talk
        dia "Хаха!"
        player_name "Без разницы."
        show diane_debbie_sex_bed player_lounge_after_talk with dissolve
        player_name "Я устал тоже!"
        show diane_debbie_sex_bed debbie_lounge_after_talk
        deb "Все хорошо, милый."
        deb "Просто лежи и отдыхай."
        show diane_debbie_sex_bed diane_lounge_after_talk
        dia "Ауу, Я люблю вас, ребята!"
        show diane_debbie_sex_bed debbie_lounge_after_talk
        deb "Хехе, мы тебя тоже."

    scene black with fade
    hide diane_debbie_sex_bed

    if M_diane.get("previous outfit") == "naked":
        $ M_diane.is_naked = 1
    else:
        $ M_diane.outfit = "cow"
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["07_unlocked"] = True
    $ renpy.end_replay()
    $ M_diane.trigger(T_diane_debbie_3way)
    if M_diane.get("cum inside") and not M_diane.get("change partner"):
        call screen pregnancy_minigame("diane_debbie_sleeping", M_diane)
    jump diane_debbie_sleeping

label diane_debbie_sleeping:
    call expression game.dialog_select("diane_debbie_sleeping_pre")
    $ Sleep()
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_diane)
    $ game.main()

label diane_debbie_sleeping_pre:
    scene location_home_debbiebedroom_night_sleep_trio with fade
    show unlock11 at truecenter with dissolve
    pause
    hide unlock11 with dissolve
    scene black with fade
    hide location_home_debbiebedroom_night_sleep_trio with fade
    return

label diane_debbie_sleepover_wakeup_first:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg"
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 5 with dissolve
    player_name "Хмм?"
    show player 10
    player_name "Куда все подевались?"
    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 17 with dissolve
    player_name "{b}*нюхая*{/b} Что-то вкусно пахнет!"
    show player 14
    player_name "{b}[deb_name]{/b} возможно готовит {b}на кухне{/b}."
    player_name "Я должен проверить."
    hide player with dissolve
    return

label diane_debbie_sleepover_wakeup_repeat:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg"
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 14 with dissolve
    player_name "Похоже, {b}Диана{/b} и {b}[deb_name]{/b} уже встали."
    hide player with dissolve
    return

label diane_debbie_pre_sex_loop:
    if not animated:
        show diane_debbie_sex_bed prev_insert
    if not M_diane.get("change partner"):
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "Я думаю пришел черед {b}Дианы{/b}."
            if animated:
                show diane_debbie_sex_bed debbie_talk
            deb "Если это то, чего ты хочешь, милый."
            deb "Давай."
            if animated:
                show diane_debbie_sex_bed diane_talk
            dia "Мммммм, неси сюда этот большой член."
            show diane_debbie_sex_bed insert with dissolve
            deb "Хехе!"
            dia "Давай жеребец, покажи мне что у тебя есть!"
            show diane_debbie_sex_bed 7
            dia "!!!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "{b}Диана{/b}, ты следующая!"
            if animated:
                show diane_debbie_sex_bed diane_talk
            dia "Ммм, мне повезло!"
            show diane_debbie_sex_bed insert with dissolve
            dia "Давай жеребец, покажи мне что у тебя есть!"
            show diane_debbie_sex_bed 7
            dia "!!!" with hpunch
    else:
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "Готова, {b}[deb_name]{/b}?"
            if animated:
                show diane_debbie_sex_bed debbie_talk
            deb "Ммм!"
            show diane_debbie_sex_bed insert with dissolve
            deb "Вот так, милый!"
            deb "Позволь мне показать кое-что, {b}[firstname]{/b}!"
            player_name "Ух!"
            show diane_debbie_sex_bed 7
            dia "О!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "Черед {b}[deb_name]{/b}!"
            if animated:
                show diane_debbie_sex_bed diane_talk
            dia "Ааа, хорошая идея..."
            dia "Мне нужно отдохнуть!"
            if animated:
                show diane_debbie_sex_bed debbie_talk
            deb "Хехе!"
            show diane_debbie_sex_bed insert with dissolve
            player_name "Вот и он, {b}[deb_name]{/b}."
            deb "Я готова!"
            show diane_debbie_sex_bed 7
            deb "О! Вот так, милый!" with hpunch
    $ animated = False
    jump diane_debbie_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
