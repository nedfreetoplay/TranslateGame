label locker_room_dialogue:
    $ player.go_to(L_school_boysroom)
    call pa_announcement
    if not game.timer.is_dark():
        if M_roxxy.is_state(S_roxxy_shower_event) and not M_roxxy.get("shower event intro done"):
            call expression game.dialog_select("boys_lockerroom_roxxy_shower_event")
            $ M_roxxy.set("shower event intro done", True)

        elif not L_school_boysroom.is_visited:
            call expression game.dialog_select("boys_lockerroom_judith_changing")
            $ persistent.cookie_jar["Judith"]["unlocked"] = True
            $ persistent.cookie_jar["Judith"]["gallery"]["01_unlocked"] = True
            $ Machine.trigger(T_mc_lockerroom_change)
            $ L_school_boysroom.visited()

        if M_bissette.is_set("martinez book search"):
            call expression game.dialog_select("boys_lockerroom_martinez_book_search")
    else:

        if False:
            call expression game.dialog_select("boys_lockerroom_webcam_quest")
    $ game.main()

label roxxy_shower_dialogue:
    label roxxy_shower_replay:
        call expression game.dialog_select("roxxy_shower_dialogue_intro")
    if not store._in_replay == None:
        jump roxxy_shower_replay_continue
    menu:
        "Please!":
            if player.has_required_chr(5):
                label roxxy_shower_replay_continue:
                call expression game.dialog_select("roxxy_shower_dialogue_please_pass")
                $ renpy.end_replay()
                $ M_roxxy.trigger(T_roxxy_get_homework)
                $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
                $ persistent.cookie_jar["Roxxy"]["gallery"]["01_unlocked"] = True
                $ player.go_to(L_school_lefthallway)
            else:

                call expression game.dialog_select("roxxy_shower_dialogue_please_fail")
        "Nevermind.":

            call expression game.dialog_select("roxxy_shower_dialogue_leave")
    hide missy
    hide becca
    hide jersey
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
