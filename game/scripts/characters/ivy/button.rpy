label ivy_button_dialogue:
    if M_ivy.is_state(S_ivy_start):
        call expression game.dialog_select("button_ivy_start_intro")
        $ M_ivy.trigger(T_ivy_intro)
    else:
        call expression game.dialog_select("button_ivy_end_intro")
    menu:
        "Окей." if M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage_first")
            call screen pamphlet

        "Массаж." if not M_ivy.is_state(S_ivy_start):
            call expression game.dialog_select("button_ivy_massage")
            call screen pamphlet

        "Пакет." if quest13 in quest_list and quest13 not in completed_quests and not player.has_item("package"):
            call expression game.dialog_select("button_ivy_package")
            $ player.get_item("package")
        "Просто покупки.":

            call expression game.dialog_select("button_ivy_just_shopping")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
