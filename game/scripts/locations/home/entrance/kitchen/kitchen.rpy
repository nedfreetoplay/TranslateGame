label home_kitchen_dialogue:
    $ player.go_to(L_home_kitchen)
    if not game.timer.is_dark():
        if M_mom.is_state(S_mom_start):
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
        if M_diane.is_state(S_diane_dinner):
            $ S_diane_dinner.add_delay(1)
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

    elif M_diane.is_state(S_diane_barn_news) and game.timer.is_day():
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

    if M_jenny.is_state(S_jenny_have_breakfast) and game.timer.is_morning():
        call expression game.dialog_select("kitchen_jenny_have_breakfast")
        $ M_jenny.trigger(T_jenny_had_breakfast)
        $ game.timer.tick()
    elif M_jenny.is_state(S_jenny_sluttygram_pics) and game.timer.is_day():
        call expression game.dialog_select("kitchen_jenny_sluttygram_pics")
    elif M_jenny.is_state(S_jenny_helping_with_breakfast) and game.timer.is_morning():
        call expression game.dialog_select("kitchen_jenny_helping_with_breakfast")
        menu:
            "Let it go. {color=7ff7}[[Submissive]{/color}":
                call expression game.dialog_select("kitchen_jenny_helping_with_breakfast_let_it_go")
                $ M_jenny.decrement("dominance")
                $ M_jenny.trigger(T_jenny_have_breakfast)
                $ game.main()
            "Confront her. {color=f77b}[[Dominant]{/color}":
                call expression game.dialog_select("kitchen_jenny_helping_with_breakfast_confront_her")
                $ M_jenny.increment("dominance")
                $ M_jenny.trigger(T_jenny_catch_her_in_shower)
                $ player.go_to(L_home_entrance)
                $ game.main()
    elif M_jenny.is_state(S_jenny_final_breakfast) and game.timer.is_morning():
        call expression game.dialog_select("kitchen_jenny_final_breakfast")
        $ player.go_to(L_home_entrance)
        $ M_jenny.trigger(T_jenny_end)
        $ game.main()

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
