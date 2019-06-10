label button_ross_office_dialogue:
    if not M_ross.is_state(S_ross_end):
        call expression game.dialog_select("button_ross_office_generic_pre_hscene")
    else:
        call expression game.dialog_select("button_ross_office_generic_post_hscene")
    menu:
        "Частный урок." if M_ross.is_state((S_ross_paint_with_body, S_ross_end)):
            call expression game.dialog_select("ross_dialogue_office_private_lessons")
            jump expression game.dialog_select("ross_hscene_start")
        "Прямо сейчас, ничего.":

            call expression game.dialog_select("ross_dialogue_office_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
