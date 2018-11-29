label anna_button_dialogue:
    scene location_park_closeup
    if M_anna.is_state(S_anna_dog_hunt):
        call expression game.dialog_select("anna_dialogue_anna_dog_hunt")
        menu:
            "Yes":
                call expression game.dialog_select("anna_dialogue_anna_dog_hunt_yes")
                $ M_anna.trigger(T_anna_find_awesomo)
            "No":

                call expression game.dialog_select("anna_dialogue_anna_dog_hunt_no")

    elif M_anna.is_state(S_anna_find_dog):
        if player.has_item("dog"):
            call expression game.dialog_select("anna_dialogue_anna_find_dog_have_dog")
            $ player.remove_item("dog")
            $ M_anna.trigger(T_anna_found_dog)
        else:

            call expression game.dialog_select("anna_dialogue_anna_find_dog_do_not_have_dog")
    hide player
    hide anna
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
