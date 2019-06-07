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
        player_name "( There's no one in here. )"
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
            "Go inside.":
                call expression game.dialog_select("shower_mom_walk_in_yes")
                $ M_mom.trigger(T_mom_shower_admire)
                $ game.timer.tick()
                $ playSound()
            "Leave.":

                call expression game.dialog_select("shower_mom_walk_in_no")

    elif M_mom.get("shower sex available"):
        label shower_mom_sex_replay:
            call expression game.dialog_select("shower_mom_sex")
        if not store._in_replay == None:
            $ M_mom.set("sex available", True)
            call expression game.dialog_select("shower_mom_sex_walk_in_pre")
            jump expression game.dialog_select("mom_shower_question")
        menu:
            "Walk inside":
                $ playSound("<loop 0.5>audio/ambience_shower_interior.ogg")
                call expression game.dialog_select("shower_mom_sex_walk_in_pre")
                label mom_shower_question:
                    $ M_mom.set("shower fingered", False)
                call expression game.dialog_select("shower_mom_sex_walk_in_after")
                menu:
                    "Wash [deb_name].":
                        call expression game.dialog_select("shower_mom_sex_wash")
                        menu shower_mom_sex_wash_menu:
                            "Handjob.":
                                call expression game.dialog_select("shower_mom_sex_wash_handjob")
                                jump expression game.dialog_select("mom_shower_end")

                            "Finger {b}[deb_name]{/b}." if M_mom.is_set("sex available") and not M_mom.is_set("shower fingered"):
                                call expression game.dialog_select("shower_mom_sex_finger")
                                $ M_mom.set("shower fingered", True)
                                jump expression game.dialog_select("shower_mom_sex_wash_menu")

                            "Blowjob." if M_mom.is_set("sex available"):
                                call expression game.dialog_select("shower_mom_sex_blowjob")
                                jump expression game.dialog_select("mom_shower_end")

                            "Sex." if M_mom.is_set("sex available"):
                                if M_mom.is_set("shower fingered"):
                                    call expression game.dialog_select("shower_mom_sex_already_fingered")
                                    call expression game.dialog_select("shower_mom_sex_wash_handjob")
                                    jump expression game.dialog_select("mom_shower_end")
                                else:

                                    jump expression game.dialog_select("mom_shower_sex")
                            "Leave":

                                jump expression game.dialog_select("mom_shower_end")

                    "Sex." if M_mom.is_set("sex available"):
                        label mom_shower_sex:
                            $ M_mom.set("sex speed", .4)
                            $ anim_toggle = True
                            $ animated = False
                            $ xray = False
                            $ cum = False
                        call expression game.dialog_select("shower_mom_sex_fuck_pre")
                        jump expression game.dialog_select("mom_shower_sex_loop")
            "Leave":

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
    $ player.go_to(L_home_shower)
    if M_jenny.pregnancy:
        call expression game.dialog_select("shower_jenny_pregnant")
    elif M_jenny.is_state(S_jenny_shower_spy):
        call expression game.dialog_select("shower_jenny_shower_spy")
        $ M_jenny.trigger(T_jenny_spied_shower)
    else:
        call expression game.dialog_select("shower_jenny_shower_spy_repeat")
        if M_jenny.is_state(S_jenny_snoop_around):
            $ player.go_to(L_home_hallway)
            call expression game.dialog_select("shower_jenny_snoop_around")
            $ game.main()
        elif M_jenny.is_state(S_jenny_snoop_around_for_laptop):
            $ player.go_to(L_home_hallway)
            call expression game.dialog_select("shower_jenny_snoop_around_for_laptop")
            $ game.main()
        elif not M_jenny.pregnancy:
            if M_jenny.finished_state(S_jenny_perv_on_tammy) and M_jenny.get("first_shower_time"):
                call expression game.dialog_select("shower_jenny_blowjob_intro_first")
            elif M_jenny.finished_state(S_jenny_perv_on_tammy):
                call expression game.dialog_select("shower_jenny_blowjob_intro_repeat")
            elif M_jenny.finished_state(S_jenny_pissed_at_handjob):
                call expression game.dialog_select("shower_jenny_pissed_at_handjob")
            else:
                call expression game.dialog_select("shower_jenny_peep")
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_shower_peep_end:
    pause
    $ player.go_to(L_home_hallway)
    $ game.main()

label scene_shower_with_vfx:
    scene shower_running
    show shower_steam zorder 100
    return

label scene_shower_with_vfx_peep:
    call scene_shower_with_vfx
    show bathroom_door_left zorder 200 at left
    show bathroom_door_right zorder 200 at right
    return

label scene_shower_with_vfx_zoom:
    scene shower_running at shower_zoom
    show shower_steam zorder 100 at shower_zoom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
