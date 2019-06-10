label mia_dialogue_mias_house_front:
    call expression game.dialog_select("mia_dialogue_mias_house_front_intro")
    menu:
        "О домашнем задании.":
            call expression game.dialog_select("mia_dialogue_mias_house_front_homework")
        "Я забыл...":

            call expression game.dialog_select("mia_dialogue_mias_house_front_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
