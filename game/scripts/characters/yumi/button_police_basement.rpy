label police_yumi_dialogue:
    call expression game.dialog_select("yumi_police_basement_dialogue_pre")
    menu:
        "Donuts." if M_mia.is_state(S_mia_impress_harold):
            $ harold_topping = M_harold.get("topping")
            call expression game.dialog_select("yumi_police_basement_dialogue_donuts")
            $ del harold_topping

        "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
            call expression game.dialog_select("yumi_police_basement_dialogue_harold")
            $ M_mia.set("questioned yumi", True)
            jump expression game.dialog_select("police_basement_dialogue")
        "Just visiting.":

            call expression game.dialog_select("yumi_police_basement_dialogue_leave")

    hide player
    hide yumi
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
