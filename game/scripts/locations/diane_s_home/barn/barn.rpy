label barn_garden_dialogue:
    $ player.go_to(L_diane_barn_garden)
    $ game.main()

label barn_dialogue:
    $ player.go_to(L_diane_barn_interior)
    if M_diane.is_state(S_diane_check_barn_out):
        call expression game.dialog_select("barn_diane_check_barn_out")
        $ player.get_item("mysterious_statue_1")
        $ M_diane.trigger(T_diane_checked_out_barn)

    if M_diane.is_state(S_diane_return_production_book):
        call expression game.dialog_select("barn_diane_return_production_book")
        $ player.remove_item("milkjug")
        $ M_diane.trigger(T_diane_gave_production_book)

    if M_diane.is_state(S_diane_barn_checkup):
        call expression game.dialog_select("barn_diane_barn_checkup")
        $ M_diane.trigger(T_diane_go_to_hospital)
        $ player.go_to(L_map)
        $ game.main()

    if M_diane.is_state(S_diane_outfit_package):
        call expression game.dialog_select("barn_diane_outfit_package")
        $ M_diane.trigger(T_diane_get_outfit_package)

    if M_diane.is_state(S_diane_return_outfit_package):
        call expression game.dialog_select("barn_diane_return_outfit_package")
        $ player.remove_item("package")
        jump expression game.dialog_select("diane_sex_breed_start")

    if M_diane.pregnancy.stage == 1 and not M_diane.pregnancy.announced_pregnancy and M_diane.pregnancy.text_announcement_seen:
        call expression game.dialog_select("barn_diane_pregnancy_anouncement")
        $ M_diane.pregnancy.announced_pregnancy = True
    $ game.main()

label barn_front_dialogue:
    $ player.go_to(L_diane_barn)
    $ game.main()

label barn_build_front_dialogue:
    $ player.go_to(L_diane_barn_building)
    if M_diane.is_state(S_diane_inform_carpenter):
        call expression game.dialog_select("barn_building_inform_carpenter")
        $ M_diane.trigger(T_diane_carpenter_agreed)
        $ game.timer.tick(2)
        $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
