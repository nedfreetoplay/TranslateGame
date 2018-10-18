label girl_lockerroom_dialogue:
    $ player.go_to(L_school_girlsroom)
    call pa_announcement
    if M_roxxy.is_state(S_roxxy_lockerroom_event):
        call expression game.dialog_select("girls_lockerroom_roxxy_lockerroom_event")
        $ M_roxxy.trigger(T_roxxy_argument)

        $ player.go_to(L_school_lefthallway)
        $ game.main()
    elif M_judith.is_state(S_judith_in_girls_bathroom):
        call expression game.dialog_select("girls_lockerroom_judith_in_girls_bathroom")
    $ game.main()

label judith_toilet:
    if M_judith.get("in bathroom"):
        if M_judith.get("sex sequence locked"):
            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_intro")
            menu:
                "Ты не уродина!":
                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_not_ugly")
                    menu:
                        "Ладно.":
                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ok")
                            menu:
                                "Конечно.":
                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_sure")
                                    menu:
                                        "Да.":
                                            $ M_judith.trigger(T_judith_comfort_her)
                                            $ M_judith.set("sex sequence locked", False)
                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_yes")
                                            $ M_judith.set("in bathroom", False)
                                            $ M_judith.unforce()
                                        "Мы должны остановиться.":

                                            call expression game.dialog_select("girls_lockerroom_judith_toilet_first_should_stop")
                                "Я не могу.":

                                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_cant")
                        "Мы должны уйти.":

                            call expression game.dialog_select("girls_lockerroom_judith_toilet_should_leave")
                "Я знаю...":

                    call expression game.dialog_select("girls_lockerroom_judith_toilet_first_ugly")
            hide player
            hide judith
            with dissolve
            jump expression game.dialog_select("left_hall_dialogue")
        else:

            call expression game.dialog_select("judith_toilet_replay")
    else:
        call expression game.dialog_select("girls_lockerroom_judith_toilet_not_here")
    jump expression game.dialog_select("girl_lockerroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
