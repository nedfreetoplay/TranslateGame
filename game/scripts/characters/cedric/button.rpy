label cedric_button_dialogue:
    scene expression player.location.background_blur
    if not M_cedric.get("first talk"):
        call expression game.dialog_select("button_cedric_intro_first")
        $ M_cedric.set("first talk", True)
    else:
        call expression game.dialog_select("button_cedric_intro_repeat")

    menu cedric_menu:
        "Чем ты занимался?":
            call expression game.dialog_select("button_cedric_what_have_you_been_up_to")
            jump cedric_menu
        "Ты меня видишь?":

            call expression game.dialog_select("button_cedric_can_you_spot_me")
            jump cedric_menu

        "О {b}[jen_name]{/b}." if M_jenny.is_state(S_jenny_talk_to_cedric):
            call expression game.dialog_select("button_cedric_about_jenny")
            $ M_jenny.trigger(T_jenny_talked_to_cedric)
        "Пока!":

            call expression game.dialog_select("button_cedric_see_ya")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
