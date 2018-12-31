label mrsj_button_dialogue:
    if player.location == L_erikhouse_entrance:
        scene expression game.timer.image("erik_entrance{}_c")
    elif player.location == L_erikhouse_mrsjroom:
        if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
            call expression game.dialog_select("button_mrsj_sex_ed_intro")
            jump mrsj_button_dialogue_repeat

        elif game.timer.is_dark() and erik.over(erik_gf):
            call expression game.dialog_select("button_mrsj_private_yoga_intro")
            jump mrsj_button_dialogue_repeat
        scene erik_house_upstairs_night_c01
    call expression game.dialog_select("button_mrsj_greetings")
    menu mrsj_button_dialogue_repeat:
        "Об {b}Эрике{/b}." if erik.started(erik_path_split):
            call screen route_warning
            call expression game.dialog_select("button_mrsj_about_erik")
            menu mrsj_route_split:
                "Половое воспитание.":
                    call expression game.dialog_select("button_mrsj_route_sex_ed")
                    $ erik_path_split.finish()
                    $ erik.add_event(erik_sex_ed)
                    $ M_mrsj.place(place = L_erikhouse_mrsjroom)
                    $ M_mrsj.force()
                    $ M_erik.place(place = L_erikhouse_erikroom)
                    $ M_erik.force()
                    jump mrsj_button_dialogue_repeat
                "Достань ему девушку.":

                    call expression game.dialog_select("button_mrsj_route_gf")
                    $ erik_path_split.finish()
                    $ June.add_event(june_intro)
                    jump mrsj_button_dialogue_repeat

        "Половое воспитание." if mrsj.started(mrsj_sex_ed):
            call expression game.dialog_select("button_mrsj_sex_ed_prep")

        "Половое воспитание." if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
            jump mrsj_3some

        "Частная йога." if game.timer.is_dark() and erik.over(erik_gf):
            jump mrsj_private_yoga

        "Подруга." if erik.started(erik_gf):
            call expression game.dialog_select("button_mrsj_erik_got_gf")
            $ erik_gf.finish()
            call expression game.dialog_select("erik_house_dialogue")

        "Подруга." if erik.in_progress(erik_gf_stolen):
            call expression game.dialog_select("button_mrsj_erik_stole_gf")
            call expression game.dialog_select("erik_house_dialogue")

        "Подруга." if June.started(june_intro_2):
            call expression game.dialog_select("button_mrsj_erik_introduce_june")
            $ june_intro_2.finish()
            jump mrsj_button_dialogue_repeat

        "Грудное вскармливание." if erik.over(erik_breastfeeding_2) and (not erik.known(erik_sex_ed) and not mrsj.known(mrsj_sex_ed) and not June.known(june_intro)):
            call expression game.dialog_select("button_mrsj_breastfeeding")

        "Что мне нужно сделать?" if mrsj.started(mrsj_yoga_help):
            call expression game.dialog_select("button_mrsj_yoga_help_repeat")

        "Где {b}Эрик{/b}?" if not game.timer.is_dark():
            show player 14
            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "Знаете ли вы, где я мог бы найти {b}Эрика{/b}?"
                show player 1
                show mrsj 17
                mrsjo "Ну, он должен быть в {b}школе{/b} прямо сейчас."
            else:

                show mrsj 14
                player_name "Знаете ли вы, где я мог бы найти {b}Эрика{/b}?"
                show player 1
                show mrsj 17
                mrsjo "Ну, я думаю, что я видела как он пошёл в {b}подвал{/b}."
                mrsjo "Если он не там, он может быть в своей комнате."
                show mrsj 14
                show player 17
                player_name "Спасибо, {b}Миссис Джонсон{/b}!"
            show mrsj 14
            jump mrsj_button_dialogue_repeat

        "Вы так натренированны!" if not game.timer.is_dark():
            call expression game.dialog_select("button_mrsj_youre_so_fit")
            jump mrsj_button_dialogue_repeat

        "Пригласить в покер." if mrsj.known(mrsj_poker_night) and not game.timer.is_night():
            show player 14 at left
            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39 at right
            elif game.timer.is_dark() and erik.over(erik_gf):
                show mrsj 53
            else:
                show mrsj 14 at right

            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "Мне стало интересно, вы можете научить нас, как играть в покер?"
                show player 11
                show mrsj 19
                mrsjo "Разве ты не должен быть в школе прямо сейчас??"
                mrsjo "{b}Эрик{/b} уже ушел!"
                show player 29
                show mrsj 14
                player_name "Вот, чёрт! Вы правы..."
                player_name "Может быть, позже!"

            elif player.stats.chr() >= 5 and poker_bot02 == "" and not game.timer.is_morning():
                if mrsj.completed(mrsj_poker_night_2):
                    show player 14 at left
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14 at right
                    player_name "Хотите сыграть с нами в покер?"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "Все еще ищете друзей, чтобы сыграть?."
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Ну, это просто, что-"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "Всё хорошо!!"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "Я буду играть с вами, парни..."
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Серьёзно?"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40b
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 20
                    mrsjo "Ну ... в прошлый раз было немного..."
                    show player 13
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "Но почему бы и нет?"
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Хорошо."
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "Когда мы играем?"
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "После ужина сегодня вечером."
                    player_name "{b}Эрик{/b} и я будем настраивать игру."
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40b
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "Хаха, хорошо."
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "Увидимся тогда!"
                else:

                    call expression game.dialog_select("button_mrsj_invite_poker")
                $ poker_bot02 = "mrsj"
                $ poker_sayer02 = mrsjo
                $ M_mrsj.place(place = L_erikhouse_basement)
                $ M_mrsj.force(tod = [2,3])
                $ M_erik.place(place = L_erikhouse_basement)
                $ M_erik.force(tod = [2,3])
            else:

                if player.stats.chr() < 5 and not game.timer.is_morning():
                    $ stat_warn = chr_warn
                else:
                    $ stat_warn = ""
                player_name "[stat_warn]Мне было интересно, если бы вы могли научить нас играть в покер?"
                show mrsj 17
                show player 1
                mrsjo "[stat_warn]Карточная игра?"
                show mrsj 14
                show player 14
                player_name "[stat_warn]Да, {b}Эрик{/b} и я просто ищем третьего игрока."
                show mrsj 17
                show player 14
                mrsjo "[stat_warn]О, я бы с удовольствием."
                show player 19
                mrsjo "[stat_warn]Но сейчас у меня просто нет времени, извините..."
                show mrsj 14
                show player 14
                player_name "[stat_warn]Это нормально, может быть, в другой раз."
        "Мне нужно идти!":

            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39
                show player 14 at left
                player_name "Я должен идти, но я вернусь, хотя!"
            else:
                if game.timer.is_dark() and erik.over(erik_gf):
                    show mrsj 53
                else:
                    show mrsj 14 at right
                show player 14 at left
                player_name "Я должен найти {b}Эрика{/b}!"
            if game.timer.is_dark() and (mrsj.over(mrsj_sex_ed) or erik.over(erik_gf)):
                if mrsj.over(mrsj_sex_ed):
                    show mrsj 40
                elif erik.over(erik_gf):
                    show mrsj 54
                show player 1 at left
                mrsjo "Серьёзно?"
                mrsjo "Ну не забудь вернуться в ближайшее время!"
            else:
                show mrsj 18 at right
                show player 1 at left
                mrsjo "Хорошо, тогда!"
            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39
            elif game.timer.is_dark() and erik.over(erik_gf):
                show mrsj 53
            else:
                show mrsj 14 at right
            show player 17 at left
            player_name "Пока, {b}Миссис Джонсон{/b}!"
    hide player
    hide erik
    hide mrsj
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
