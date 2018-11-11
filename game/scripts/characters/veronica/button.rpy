label veronica_button_dialogue:
    call expression game.dialog_select("veronica_dialogue_pre")
    menu:
        "Овощной Бульон." if M_okita.is_state(S_okita_get_ingredients):
            call expression game.dialog_select("veronica_dialogue_vegatable_stock")
            $ M_okita.set("talked with veronica", True)

        "Спрей от жуков?" if quest10 in quest_list and not infestation_done:
            call expression game.dialog_select("veronica_dialogue_bug_spray")
            menu:
                "Большые крылья.":
                    call expression game.dialog_select("veronica_dialogue_bug_spray_large_wings")
                "Клещи на спине.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_pincers")
                "Белые пятна.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_white_spots")
        "Я в порядке.":

            call expression game.dialog_select("veronica_dialogue_leave")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
