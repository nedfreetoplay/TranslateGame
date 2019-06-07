label bissette_office_dialogue:
    scene expression game.timer.image("french_office_c{}")
    if M_bissette.between_states(S_bissette_roxxy_exam_convince, S_bissette_roxxy_jenny_spying):
        call expression game.dialog_select("bissette_dialogue_office_bissette_roxxy_exam_convince")

    elif M_bissette.is_state(S_bissette_roxxy_convinced):
        call expression game.dialog_select("bissette_dialogue_office_bissette_roxxy_convinced")
        $ M_bissette.trigger(T_bissette_quiz_warning)

    elif M_bissette.is_state(S_bissette_wine_sampling) and M_bissette.is_set("night visit") and game.timer.is_dark():
        call expression game.dialog_select("bissettes_office_night_visit")
        jump expression game.dialog_select("bissettes_office_sex_loop")

    elif M_bissette.is_set("night visit"):
        label bissettes_office_night_visit_replay:
        call expression game.dialog_select("bissettes_office_night_visit_repeat")
        jump expression game.dialog_select("bissettes_office_sex_loop")
    else:

        call expression game.dialog_select("bissette_dialogue_office_intro")
        menu:
            "Wine Sampling." if M_bissette.is_state(S_bissette_wine_sampling):
                call expression game.dialog_select("bissette_dialogue_office_bissette_wine_sampling")
                $ M_bissette.set("night visit", True)
                jump expression game.dialog_select("mrs_bissettes_office_dialogue")
            "Nothing.":

                call expression game.dialog_select("bissette_dialogue_office_leave")
    hide player
    hide teacher
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
