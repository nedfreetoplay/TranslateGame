label daisy_button_dialogue:
    scene expression player.location.background_blur
    if game.timer.is_dark():
        call expression game.dialog_select("daisy_button_sleeping")
        $ game.main()
    if M_daisy.pregnancy.gave_birth:
        call expression game.dialog_select("daisy_button_gave_birth_intro")
        menu daisy_baby_default_dialogue_options:
            "How's he doing?" if M_daisy.pregnancy.baby_gender == "boy":
                call expression game.dialog_select("daisy_button_hows_baby_doing_boy")
                jump daisy_baby_default_dialogue_options

            "How's she doing?" if M_daisy.pregnancy.baby_gender == "girl":
                call expression game.dialog_select("daisy_button_hows_baby_doing_girl")
                jump daisy_baby_default_dialogue_options
            "Can I get you anything?":

                call expression game.dialog_select("daisy_button_get_anything_baby")
                jump daisy_baby_default_dialogue_options
            "I'll leave you guys be.":

                call expression game.dialog_select("daisy_button_baby_leave")
        $ game.main()

    if not M_daisy.finished_state(S_daisy_picking_flowers):
        call expression game.dialog_select("daisy_button_intro_scared")
        $ game.main()
    elif M_daisy.is_state(S_daisy_get_pizza):
        if player.has_item("veggie_pizza"):
            call expression game.dialog_select("daisy_button_get_pizza_has_pizza")
            $ player.remove_item("veggie_pizza")
            $ M_daisy.trigger(T_daisy_eaten_pizza)
            $ game.timer.tick(2)
            $ player.go_to(L_diane_barn_garden)
            $ game.main()
        else:
            call expression game.dialog_select("daisy_button_get_pizza_has_not_pizza")
            $ game.main()
    elif M_daisy.is_state(S_daisy_get_new_flowers):
        if player.has_item("flower_7"):
            call expression game.dialog_select("daisy_button_get_new_flowers_has_flowers")
            $ M_daisy.trigger(T_daisy_gave_new_flowers)
            $ player.remove_item("flower_7")
            $ game.main()
        else:
            call expression game.dialog_select("daisy_button_get_new_flowers_no_flowers")
            $ game.main()
    elif M_daisy.is_state(S_daisy_need_milking):
        call expression game.dialog_select("daisy_button_daisy_need_milking")
        call screen milking_minigame("daisy")

    elif M_daisy.is_state(S_daisy_diane_breeding) and M_diane.finished_state(S_diane_milk_production_increase) and not M_diane.pregnancy:
        call expression game.dialog_select("daisy_button_diane_breeding")
        $ M_daisy.trigger(T_daisy_caught_breeding)
        $ game.timer.tick()
        $ player.go_to(L_diane_barn)
        $ game.main()

    elif M_daisy.between_states(S_daisy_get_pizza, S_daisy_need_milking):
        call expression game.dialog_select("daisy_button_finished_pizza_intro")
    elif M_daisy.is_state(S_daisy_end):
        call expression game.dialog_select("daisy_button_intro_end")
    elif M_daisy.finished_state(S_daisy_need_milking):
        call expression game.dialog_select("daisy_button_finished_milking_intro")
    else:
        call expression game.dialog_select("daisy_button_intro")

    menu daisy_menu_button:
        "Still nervous?" if not M_daisy.finished_state(S_daisy_get_pizza):
            call expression game.dialog_select("daisy_button_still_nervous")
            jump daisy_menu_button

        "How are your flowers?" if not M_daisy.finished_state(S_daisy_get_pizza):
            call expression game.dialog_select("daisy_button_how_are_your_flowers_1")
            jump daisy_menu_button

        "Tell me about yourself." if not M_daisy.finished_state(S_daisy_get_pizza):
            call expression game.dialog_select("daisy_button_about_yourself")
            jump daisy_menu_button

        "{b}Jebadiah Delmont{/b}" if not M_daisy.finished_state(S_daisy_get_pizza):
            call expression game.dialog_select("daisy_button_jebadiah_delmont")
            jump daisy_menu_button

        "How are your flowers?" if M_daisy.between_states(S_daisy_get_pizza, S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_how_are_your_flowers_2")
            jump daisy_menu_button

        "Milking business." if M_daisy.between_states(S_daisy_get_pizza, S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_milking_business")
            jump daisy_menu_button

        "More about {b}Jebadiah Delmont{/b}" if M_daisy.between_states(S_daisy_get_pizza, S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_more_jebadiah_delmont")
            jump daisy_menu_button

        "You seem really happy today." if M_daisy.finished_state(S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_you_seem_happy")
            jump daisy_menu_button

        "How are your flowers?" if M_daisy.finished_state(S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_how_are_your_flowers_3")
            jump daisy_menu_button

        "More about {b}Jebadiah Delmont{/b}" if M_daisy.finished_state(S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_more_jebadiah_delmont_2")
            jump daisy_menu_button

        "Have sex." if M_daisy.finished_state(S_daisy_caught_breeding) and not M_daisy.pregnancy:
            if M_daisy.get("daisy_breed_first_time"):
                call expression game.dialog_select("daisy_button_have_sex_first")
                jump first_time_dialogue_daisy_sex
            else:
                call expression game.dialog_select("daisy_button_have_sex_repeat")
                jump daisy_sex_breed_start

        "How's the baby?" if 0 < M_daisy.pregnancy.stage < 5:
            call expression game.dialog_select("daisy_button_hows_the_baby_{}".format(M_daisy.pregnancy.apparent_stage))
            jump daisy_menu_button

        "Pizza." if M_daisy.finished_state(S_daisy_get_pizza):
            if player.has_item("veggie_pizza"):
                call expression game.dialog_select("daisy_button_has_veggie_pizza")
                $ player.remove_item("veggie_pizza")
            else:
                call expression game.dialog_select("daisy_button_no_veggie_pizza")
            $ game.main()

        "You want me to milk you?" if M_daisy.finished_state(S_daisy_need_milking):
            call expression game.dialog_select("daisy_button_want_me_to_milk_you")
            call screen milking_minigame("daisy")
        "I should go.":

            call expression game.dialog_select("daisy_button_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
