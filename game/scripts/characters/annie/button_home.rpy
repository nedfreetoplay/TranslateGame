label annie_button_home_dialogues:
    scene expression player.location.background_blur with None
    call expression game.dialog_select("annie_button_home_intro")
    menu annie_button_menu_dialogues:
        "Хорошо, блин.":
            call expression game.dialog_select("annie_button_home_menu_alright_sheesh")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
