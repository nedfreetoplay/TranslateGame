label mom_dialogue_button_room:
    call expression game.dialog_select("debbie_dialogue_master_room_pre")
    jump expression game.dialog_select("debbie_dialogue_master_room_options")

    label debbie_dialogue_master_room_after_kiss:
        call expression game.dialog_select("debbie_dialogue_master_room_after_kiss_dialogue")
    menu debbie_dialogue_master_room_options:
        "Kiss.":
            call expression game.dialog_select("debbie_dialogue_master_room_kiss")
            jump expression game.dialog_select("debbie_dialogue_master_room_after_kiss")
        "Shower.":

            call expression game.dialog_select("debbie_dialogue_master_room_shower")
            jump expression game.dialog_select("mom_shower_question")
        "Have sex.":

            label sex_mom_bed_intro_3:
                if randomizer() <= 50:
                    call expression game.dialog_select("debbie_dialogue_master_room_sex_random_true")
                else:

                    call expression game.dialog_select("debbie_dialogue_master_room_sex_random_false")
                call expression game.dialog_select("debbie_dialogue_master_room_sex_after")
            jump expression game.dialog_select("mom_sex")

        "Laundry." if M_mom.is_set("basement sex"):
            call expression game.dialog_select("debbie_dialogue_master_room_laundry_sex")
            jump expression game.dialog_select("basement_mom_sex")

        "Watch a Movie." if not M_mom.is_set("movie night"):
            call expression game.dialog_select("debbie_dialogue_master_room_watch_movie")
            $ M_mom.set("movie night", True)
        "Nevermind.":

            call expression game.dialog_select("debbie_dialogue_master_room_leave")
    hide player
    hide debbie
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
