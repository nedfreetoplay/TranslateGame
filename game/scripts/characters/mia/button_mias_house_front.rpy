label mia_dialogue_mias_house_front:
    call expression game.dialog_select("mia_dialogue_mias_house_front_intro")
    menu:
        "About that homework.":
            call expression game.dialog_select("mia_dialogue_mias_house_front_homework")
        "I forgot...":

            call expression game.dialog_select("mia_dialogue_mias_house_front_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
