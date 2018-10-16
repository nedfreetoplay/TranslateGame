label kitchen_dialogue:
    $ player.go_to(L_diane_kitchen)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if aunt.started(aunt_breeding_bull) and quest12 in completed_quests:
        call expression game.dialog_select("dianes_kitchen_diane_breeding_bull_started")
        $ aunt_breeding_bull.finish()

    elif aunt.started(aunt_mouse_attack):
        call expression game.dialog_select("dianes_kitchen_diane_mouse_attack_started")

    elif aunt_drink_active:
        $ game.main()
    else:

        if not aunt.known(aunt_drunken_splur) and aunt_count < 8 or aunt.over(aunt_drunken_splur) and aunt_count < 8:
            call expression game.dialog_select("dianes_kitchen_diane_drunken_splur_not_known")
    $ game.main()

label kitchen_drink:
    call expression game.dialog_select("dianes_kitchen_diane_kitchen_drink_intro")
    $ aunt_drink_made = True
    menu:
        "Нет.":
            call expression game.dialog_select("dianes_kitchen_diane_kitchen_drink_no")
        "Да.":

            call expression game.dialog_select("dianes_kitchen_diane_kitchen_drink_yes")
            $ aunt_extra_shot = True
    $ in_garden = True

    call expression game.dialog_select("garden_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
