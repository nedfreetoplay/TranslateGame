label veronica_button_dialogue:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg" with None
    if M_diane.between_states(S_diane_start, S_diane_garden_restored):
        call expression game.dialog_select("veronica_dialogue_pre_d05")

    elif M_diane.between_states(S_diane_garden_restored, S_diane_drunken_shenanigans_apology):
        call expression game.dialog_select("veronica_dialogue_pre_d11")

    elif M_diane.between_states(S_diane_drunken_shenanigans_apology, S_diane_end):
        call expression game.dialog_select("veronica_dialogue_pre_d20")
    menu veronica_button_menu:
        "Овощной склад." if M_okita.is_state(S_okita_get_ingredients):
            call expression game.dialog_select("veronica_dialogue_vegatable_stock")
            $ M_okita.set("talked with veronica", True)
            $ game.main()

        "Что вы здесь продаете?" if M_diane.between_states(S_diane_start, S_diane_garden_restored):
            call expression game.dialog_select("veronica_dialogue_what_do_you_sell")
            jump veronica_button_menu

        "Ты сегодня хорошо выглядишь." if M_diane.finished_state(S_diane_garden_restored):
            call expression game.dialog_select("veronica_dialogue_you_look_nice")
            jump veronica_button_menu

        "Разговаривала с {b}Дианой{/b} в последнее время?" if M_diane.finished_state(S_diane_garden_restored):
            call expression game.dialog_select("veronica_dialogue_spoken_with_diane_lately")
            jump veronica_button_menu
        "Просто смотрю.":

            call expression game.dialog_select("veronica_dialogue_leave")
            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
