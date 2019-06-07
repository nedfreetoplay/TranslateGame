label ivy_button_dialogue:
    if M_ivy.is_state(S_ivy_start):
        call expression game.dialog_select("button_ivy_start_intro")
        $ M_ivy.trigger(T_ivy_intro)
    else:
        call expression game.dialog_select("button_ivy_end_intro")
    menu:
        "Okay." if M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage_first")
            call screen pamphlet

        "Massage." if not M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage")
            call screen pamphlet

        "Package." if M_diane.is_state(S_diane_outfit_package):
            call expression game.dialog_select("button_ivy_diane_outfit_package")
            $ player.get_item("package")
            $ M_diane.trigger(T_diane_get_outfit_package)
        "Just shopping.":

            call expression game.dialog_select("button_ivy_just_shopping")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
