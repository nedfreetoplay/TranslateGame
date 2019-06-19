label MC_computer_night_locked:
    scene expression game.timer.image("bedroom{}")
    show player 24 at left
    player_name "( Я очень устал, я должен поспать... )"
    hide player 17 at left
    return

label egay_search_dialogue:
    if erik.started(erik_orcette):
        call expression game.dialog_select("egay_search_dialogue_erik_orcette_started")
    show screen MC_computer
    call screen egay("Search")

label egay_search_dialogue_erik_orcette_started:
    scene player_computer_bg
    show player_computer_egay_search
    player_name "( Хм... Думаю, я должен просто ввести название предмета, который хотел {b}Эрик{/b}. )"
    player_name "( Что это было снова? )"
    hide player_computer_egay_search
    hide player_computer_bg
    return

label egay_purchased_dialogue:
    scene player_computer_bg
    show player_computer_egay_purchased
    player_name "( Похоже, что я должен получить пакет в почтовом ящике во {b}Вторник{/b}. )"
    hide player_computer_egay_purchased
    hide player_computer_bg
    show screen MC_computer
    call screen egay("Purchased")

label egay_search:
    if erik.started(erik_orcette):
        if egay_search.lower() == "orcette":
            show screen MC_computer
            call screen egay("Found")
    show screen MC_computer
    call screen egay("Fail")

label webcam_dialogue:
    scene expression game.timer.image("MC_computer{}_b")
    call expression game.dialog_select("webcam_dialogue_not_connected")
    call screen MC_computer

label webcam_dialogue_not_connected:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( Странно. Здесь говорится, что я могу подключить свой компьютер к {b}веб-камере{/b}, но, кажется, я не могу сделать это отсюда. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label webcam_dialogue_nothing_showing:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( На данный момент ничего нет. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label sis_camshow_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if current_camshow == 1:
                    show expression AnimatedImage("jennysex", [23,24,25,22], M_jenny) as jennysex zorder 1 at Position(xpos = 543, ypos = 767)

                elif current_camshow == 2:
                    show expression AnimatedImage("jennysex", [28,29,30,31], M_jenny) as jennysex zorder 1 at Position(xpos = 512, ypos = 770)

                elif current_camshow == 3:
                    show expression AnimatedImage("jennysex", [36,37,38,35], M_jenny) as jennysex zorder 1 at Position(xpos = 540, ypos = 582)

                elif current_camshow == 4:
                    show expression AnimatedImage("jennysex", [42,43,44,41], M_jenny) as jennysex zorder 1 at Position(xpos = 427, ypos = 746)
                $ animated = True
            pause 8
        else:

            $ pose_counter = 0
            if current_camshow == 1:
                $ pose_list = [23,24,25,22]
                $ xpos_list = [543]
                $ ypos_list = [767]

            elif current_camshow == 2:
                $ pose_list = [28,29,30,31]
                $ xpos_list = [512]
                $ ypos_list = [770]

            elif current_camshow == 3:
                $ pose_list = [36,37,38,35]
                $ xpos_list = [540]
                $ ypos_list = [582]

            elif current_camshow == 4:
                $ pose_list = [42,43,44,41]
                $ xpos_list = [427]
                $ ypos_list = [746]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex zorder 1 at Position(xpos = xpos_list[0], ypos = ypos_list[0])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1

label sis_camshow_finish:
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    if current_camshow == 1:
        call expression game.dialog_select("sis_camshow_01_finish")
    elif current_camshow == 2:
        call expression game.dialog_select("sis_camshow_02_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_2"
    elif current_camshow == 3:
        call expression game.dialog_select("sis_camshow_03_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_3"
    elif current_camshow == 4:
        call expression game.dialog_select("sis_camshow_04_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_4"
    $ game.timer.tick()
    $ game.main()

label webcam_menu_2:
    label webcam_menu_3:
        label webcam_menu_4:
            scene blank
    menu:
        "Электро Клитор.":
            jump expression game.dialog_select("electroclit_replay")

        "Ультравибратор 2000." if store._in_replay in ["webcam_menu_2", "webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("ultravibrator_replay")

        "Двойной Вибратор." if store._in_replay in ["webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("dualsybian_replay")

        "Плохой Монстр." if store._in_replay == "webcam_menu_4":
            jump expression game.dialog_select("badmonster_replay")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
