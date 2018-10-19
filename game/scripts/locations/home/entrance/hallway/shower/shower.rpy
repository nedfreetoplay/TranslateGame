label shower_dialogue:
    $ player.go_to(L_home_shower)
    if game.timer.is_dark():
        $ game.main()


    if M_mom.is_state(S_mom_sis_check):
        call expression game.dialog_select("shower_mom_sis_check")
        $ M_mom.trigger(T_mom_sis_order)
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_close_valve):
        call expression game.dialog_select("shower_mom_close_valve")
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_pipe_check):
        call expression game.dialog_select("shower_mom_pipe_check")
        $ M_mom.trigger(T_mom_get_wrench)
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_fix_pipe) and not player.has_item("wrench"):
        call expression game.dialog_select("shower_mom_fix_pipe_no_wrench")
        jump hallway_dialogue

    elif M_mom.is_state(S_mom_fix_pipe) and player.has_item("wrench"):
        call expression game.dialog_select("shower_mom_fix_pipe_wrench")
        $ player.remove_item("wrench")
        $ M_mom.trigger(T_mom_fixed_broken_pipe)
        jump hallway_dialogue

    elif player.location.is_here(M_jenny):
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        jump sis_shower

    elif player.location.is_here(M_mom):
        $ playSound("<loop 1>audio/ambience_shower_room.ogg")
        jump mom_shower
    else:

        scene shower1
        player_name "( Здесь никого нет. )"
    $ game.main()

label mom_shower:
    if M_mom.is_state(S_mom_shower_peek_after):
        call expression game.dialog_select("shower_mom_shower_peek_after")
        $ player.go_to(L_home_hallway)
        $ game.main()

    scene shower06a
    if M_mom.is_state(S_mom_shower_peek):
        call expression game.dialog_select("shower_mom_shower_peek")
        $ M_mom.trigger(T_mom_shower_admire)

    elif M_mom.is_state(S_mom_shower_walk_in):
        call expression game.dialog_select("shower_mom_walk_in")
        menu:
            "Войти внутрь.":
                call expression game.dialog_select("shower_mom_walk_in_yes")
                $ M_mom.trigger(T_mom_shower_admire)
                $ game.timer.tick()
                $ playSound()
            "Оставить.":

                call expression game.dialog_select("shower_mom_walk_in_no")

    elif M_mom.get("shower sex available"):
        label shower_mom_sex_replay:
            call expression game.dialog_select("shower_mom_sex")
        if not store._in_replay == None:
            $ M_mom.set("sex available", True)
            call expression game.dialog_select("shower_mom_sex_walk_in_pre")
            jump expression game.dialog_select("mom_shower_question")
        menu:
            "Зайти внутрь":
                $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
                call expression game.dialog_select("shower_mom_sex_walk_in_pre")
                label mom_shower_question:
                    $ M_mom.set("shower fingered", False)
                call expression game.dialog_select("shower_mom_sex_walk_in_after")
                menu:
                    "Мыть [deb_name].":
                        call expression game.dialog_select("shower_mom_sex_wash")
                        menu shower_mom_sex_wash_menu:
                            "Мастурбирует.":
                                call expression game.dialog_select("shower_mom_sex_wash_handjob")
                                jump expression game.dialog_select("mom_shower_end")

                            "Палец {b}[deb_name]{/b}." if M_mom.is_set("sex available") and not M_mom.is_set("shower fingered"):
                                call expression game.dialog_select("shower_mom_sex_finger")
                                $ M_mom.set("shower fingered", True)
                                jump expression game.dialog_select("shower_mom_sex_wash_menu")

                            "Отсос." if M_mom.is_set("sex available"):
                                call expression game.dialog_select("shower_mom_sex_blowjob")
                                menu shower_mom_sex_blowjob_menu:
                                    "Продолжай":
                                        call expression game.dialog_select("shower_mom_sex_blowjob_loop")
                                        jump expression game.dialog_select("shower_mom_sex_blowjob_menu")
                                    "Сперма в рот":

                                        call expression game.dialog_select("shower_mom_sex_blowjob_cum_in_mouth")
                                        jump expression game.dialog_select("mom_shower_end")
                                    "Сперма на лицо":

                                        call expression game.dialog_select("shower_mom_sex_blowjob_cum_on_face")
                                        jump expression game.dialog_select("mom_shower_end")

                            "Секс." if M_mom.is_set("sex available"):
                                if M_mom.is_set("shower fingered"):
                                    call expression game.dialog_select("shower_mom_sex_already_fingered")
                                    call expression game.dialog_select("shower_mom_sex_wash_handjob")
                                    jump expression game.dialog_select("mom_shower_end")
                                else:

                                    jump expression game.dialog_select("mom_shower_sex")
                            "Оставить":

                                jump expression game.dialog_select("mom_shower_end")

                    "Секс." if M_mom.is_set("sex available"):
                        label mom_shower_sex:
                            $ M_mom.set("sex speed", .4)
                            $ anim_toggle = False
                            $ xray = False
                            $ cum = False
                        call expression game.dialog_select("shower_mom_sex_fuck_pre")
                        jump expression game.dialog_select("mom_shower_sex_loop")
            "Оставить":

                call expression game.dialog_select("shower_mom_sex_leave")
    else:
        call expression game.dialog_select("shower_mom_shower_peek")
        $ player.go_to(L_home_hallway)
        $ game.main()
    hide debbie_shower
    hide debbie
    hide debbies
    hide player
    with dissolve
    $ player.go_to(L_home_hallway)
    $ game.main()

label sis_shower:
    call expression game.dialog_select("shower_sis_sex_pre")
    menu:
        "Выглядывать." if sister.known(sis_shower_cuddle01):
            if sister.over(sis_shower_cuddle01):
                call expression game.dialog_select("shower_sis_sex_peep_after_cuddle")
            else:

                call expression game.dialog_select("shower_sis_sex_peep_before_cuddle")
                $ sis_shower_cuddle01.finish()

        "Войти внутрь." if sister.known(sis_shower_cuddle02):
            $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
            call expression game.dialog_select("shower_sis_sex_go_inside")
            jump expression game.dialog_select("shower_sis_sex_intro")
        "Оставить.":

            call expression game.dialog_select("shower_sis_sex_leave")
    jump expression game.dialog_select("hallway_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
