label somrak_button_dialogue:
    scene expression player.location.background_closeup with None
    if M_somrak.is_state(S_somrak_start):
        call expression game.dialog_select("button_somrak_start")
        $ M_somrak.trigger(T_somrak_hungry)
        $ game.main()
    elif game.timer.is_morning() or game.timer.is_dark():
        call expression game.dialog_select("button_somrak_morning_dialogue")
        $ game.main()

    elif M_somrak.is_state(S_somrak_waiting_a, S_somrak_waiting_b, S_somrak_waiting_c, S_somrak_waiting_d):
        python hide:
            pants = {'debbie_panties': 'Debbie', 'jenny_panties': 'Jenny',
                     'mia_panties': 'Mia', 'roxxy_panties': 'Roxxy'}
            try:
                item = next(item for item in player.inventory.items if item in pants)
                M_somrak.set('delivered_panties', pants[item])
                M_somrak.set("just_delivered_panties", True)
                player.remove_item(item)
            except StopIteration:
                M_somrak.set("just_delivered_panties", False)
        if M_somrak.get('just_delivered_panties'):
            call expression game.dialog_select("button_somrak_panties_story")
            if M_somrak.is_state(S_somrak_waiting_a):
                call expression game.dialog_select("button_somrak_has_panties")
            else:
                call expression game.dialog_select("button_somrak_panties_repeatable")
            $ M_somrak.trigger(T_somrak_fed)
            call screen muay_thai
        elif M_somrak.is_state(S_somrak_waiting_a):
            call expression game.dialog_select("button_somrak_waiting_for_panties")
            $ game.main()

    call expression game.dialog_select("button_somrak_afternoon_dialogue")

    menu somrak_menu_dialogue:
        "More training?":
            call expression game.dialog_select("button_somrak_more_training_not_trained_1")
            if M_somrak.is_state(S_somrak_sated_a, S_somrak_sated_b, S_somrak_sated_c, S_somrak_sated_d):
                call expression game.dialog_select("button_somrak_more_training_not_trained_2")
                call screen muay_thai
            else:
                call expression game.dialog_select("button_somrak_more_training_not_trained_3")
                jump somrak_menu_dialogue
        "The monkey thing.":
            call expression game.dialog_select("button_somrak_monkey_thing")
            jump somrak_menu_dialogue
        "Panties obsession.":
            call expression game.dialog_select("button_somrak_panties_obsession")
            jump somrak_menu_dialogue
        "Nevermind.":
            call expression game.dialog_select("button_somrak_nevermind")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
