default first_revealing = True

label home_kitchen_dialogue:
    $ player.go_to(L_home_kitchen)
    if not game.timer.is_dark():
        if game.timer.is_morning() and M_jenny.is_state(S_jenny_debbie_breakfast) and L_home_diningroom.is_here(M_jenny):
            call expression game.dialog_select("kitchen_sis_telescope_1")
            $ M_jenny.trigger(T_jenny_debbie_mention_breakfast)
            $ game.main()

        elif M_mom.is_state(S_mom_start):
            call expression game.dialog_select("kitchen_mom_start")
            call screen deb_name_input
            if deb_char_name.strip() == "":
                $ deb_char_name = "Debbie"
            $ config.replay_scope["deb_char_name"] = deb_char_name
            $ persistent.deb_char_name = deb_char_name
            $ deb = Character("[deb_char_name]", color="#ff6df0")
            $ M_mom.trigger(T_mom_breakfast)
            $ game.unlock_ui()
            $ L_map.unlock()
            $ game.main()

    if M_mom.is_state(S_mom_debt_call):
        call expression game.dialog_select("kitchen_mom_debt_call")
        $ M_mom.trigger(T_mom_debt_help)
        $ game.main()

    elif M_diane.is_state(S_diane_meet_debbie_kitchen):
        call expression game.dialog_select("kitchen_diane_meet_debbie_kitchen")
        if M_mom.finished_state(S_mom_diane_visit):
            call expression game.dialog_select("kitchen_diane_debbie_dinner_outfit")
            $ M_diane.trigger(T_diane_debbie_check_outfit)
            $ player.go_to(L_home_livingroom)
        else:
            $ M_diane.trigger(T_diane_debbie_ask_fish)

    elif M_mom.is_state(S_mom_diane_visit) and game.timer.is_evening():
        call expression game.dialog_select("kitchen_mom_diane_visit")
        $ M_mom.trigger(T_mom_diane_chat)
        $ game.timer.tick()
        jump home_entrance

    if M_diane.is_state(S_diane_debbie_evening_visit) and game.timer.is_evening():
        call expression game.dialog_select("kitchen_diane_debbie_evening_visit")
        $ M_diane.trigger(T_diane_debbie_overhear_conversation)
        $ player.go_to(L_home_entrance)
        $ game.timer.tick()

    elif M_diane.is_state(S_diane_dinner):
        call expression game.dialog_select("kitchen_diane_dinner")
        $ M_diane.trigger(T_diane_dinner_finished)
        $ player.go_to(L_home_entrance)
        $ player.remove_item("seatrout")
        $ game.timer.tick(3)

    elif M_diane.is_state(S_diane_barn_news):
        call expression game.dialog_select("kitchen_diane_barn_news")
        $ M_diane.trigger(T_diane_barn_built)
        $ player.go_to(L_home_entrance)

    elif M_diane.is_state(S_diane_breeding_candidate):
        call expression game.dialog_select("kitchen_diane_breeding_candidate")
        $ M_diane.trigger(T_diane_breeding_partner)
        $ player.go_to(L_home_entrance)

    elif M_diane.is_state(S_diane_3way_aftermath) and game.timer.is_morning():
        call expression game.dialog_select("kitchen_diane_3way_aftermath")
        $ M_diane.trigger(T_diane_3way_finished)
        $ player.go_to(L_home_entrance)
        $ game.timer.tick()
    $ game.main()

label mom_kissing_practice:
    call expression game.dialog_select("kitchen_mom_kissing_practice")
    $ M_mom.trigger(T_mom_kiss)
    $ game.timer.tick()
    $ game.main()

label dishes_dialogue:
    call expression game.dialog_select("kitchen_mom_dishes")
    menu:
        "Let me help.":
            call expression game.dialog_select("kitchen_mom_dishes_yes")
            $ game.timer.tick()
            $ M_mom.trigger(T_mom_washed_dishes)
        "Nevermind.":

            call expression game.dialog_select("kitchen_mom_dishes_no")
    $ M_mom.set("chores", False)
    $ game.main()

label sis_breakfast_force:
    call expression game.dialog_select("kitchen_sis_breakfast_force")
    $ game.main()

label sis_breakfast_force_mom:
    call expression game.dialog_select("kitchen_sis_breakfast_force_mom")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
