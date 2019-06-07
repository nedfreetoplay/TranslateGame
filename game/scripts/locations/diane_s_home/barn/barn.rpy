label barn_garden_dialogue:
    $ player.go_to(L_diane_barn_garden)
    $ game.main()

label barn_dialogue:
    if M_daisy.is_state(S_daisy_caught_breeding):
        call expression game.dialog_select("barn_dialogue_daisy_caught_breeding")
        $ game.main()

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

    if M_daisy.pregnancy.stage == 1 and not M_daisy.pregnancy.announced_pregnancy and M_daisy.pregnancy.text_announcement_seen:
        if M_daisy.pregnancy.number_of_babies == 0:
            call expression game.dialog_select("barn_daisy_pregnancy_anouncement_first")
        else:
            call expression game.dialog_select("barn_daisy_pregnancy_anouncement_repeat")
        $ M_daisy.pregnancy.announced_pregnancy = True
        $ player.go_to(L_diane_barn)
        $ game.main()

    if M_daisy.pregnancy.stage == 5 and not M_daisy.pregnancy.seen_in_labor:
        call expression game.dialog_select("barn_daisy_pregnancy_seen_in_labor")
        $ M_daisy.pregnancy.seen_in_labor = True
        $ M_daisy.pregnancy.gave_birth = True

    if player.has_item("mysterious_statue_1") and player.has_item("mysterious_statue_2") and player.has_item("mysterious_statue_3"):
        call expression game.dialog_select("barn_player_completed_mysterious_statue")
        $ M_daisy.trigger(T_daisy_intro)
        $ player.remove_item("mysterious_statue_1", "mysterious_statue_2", "mysterious_statue_3")
        $ player.go_to(L_diane_barn_garden)
        $ game.main()

    if M_daisy.is_state(S_daisy_awakened_statue):
        call expression game.dialog_select("barn_daisy_awakened_statue")
        $ M_daisy.trigger(T_daisy_checked_on_cow)
        $ player.go_to(L_diane_barn_garden)
        $ game.main()

    if M_daisy.is_state(S_daisy_dead_flowers):
        call expression game.dialog_select("barn_daisy_dead_flowers")
        $ M_daisy.trigger(T_daisy_flower_bad_news)
        $ player.go_to(L_map)
        $ game.main()

    if M_daisy.is_state(S_daisy_caught_breeding_aftermath):
        call expression game.dialog_select("barn_daisy_caught_breeding_aftermath")
        $ M_daisy.trigger(T_daisy_end)
        menu:
            "Yes.":
                call expression game.dialog_select("barn_daisy_caught_breeding_aftermath_yes")
                jump first_time_dialogue_daisy_sex
            "No.":

                call expression game.dialog_select("barn_daisy_caught_breeding_aftermath_no")
                $ game.main()
    $ game.main()

label barn_front_dialogue:
    $ player.go_to(L_diane_barn)
    if M_daisy.is_state(S_daisy_picking_flowers) and game.timer.is_morning():
        call expression game.dialog_select("barn_front_daisy_picking_flowers")
        $ M_daisy.trigger(T_daisy_named_herself)
        $ game.timer.tick()
        $ M_daisy.outfit.is_naked = True
        $ player.go_to(L_diane_barn_garden)
        $ game.main()
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
