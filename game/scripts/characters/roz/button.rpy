label roz_dialogue:
    call expression game.dialog_select("roz_dialogue_intro")
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_options:
        "First floor?":
            call expression game.dialog_select("roz_dialogue_1st_floor")
            jump expression game.dialog_select("roz_dialogue_options")
        "Second floor?":

            call expression game.dialog_select("roz_dialogue_2nd_floor")
            jump expression game.dialog_select("roz_dialogue_options")

        "Third floor?" if L_hospital_floor3.locked:
            if M_priya.is_state(S_priya_talk_to_roz):
                call expression game.dialog_select("roz_dialogue_3rd_floor_priya")
                $ M_priya.trigger(T_priya_talked_to_roz)
                $ game.main()
            else:
                call expression game.dialog_select("roz_dialogue_3rd_floor")
                jump roz_dialogue_options
            $ game.main()
        "Schedule.":

            call expression game.dialog_select("roz_dialogue_schedule")
            jump expression game.dialog_select("roz_dialogue_options")

        "Ancestry." if M_aqua.is_state(S_aqua_boatsmith_search) and M_roz.is_state(S_roz_start):
            call expression game.dialog_select("roz_dialogue_ancestory")
            $ M_roz.trigger(T_roz_favour)
            $ M_roz.set("fun time", True)

        "Go on break." if M_roz.is_state(S_roz_end) and not M_roz.is_set("fun time"):
            call expression game.dialog_select("roz_dialogue_go_on_break")
            $ M_roz.set("fun time", True)
        "Nothing.":

            call expression game.dialog_select("roz_dialogue_nothing")

    hide player
    hide roz
    hide roz_desk
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
