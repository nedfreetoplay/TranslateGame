label cellphone_exit:
    if game.read_message:
        $ game.read_message = False
        $ player.location.hide_screen()
        $ game.unlock_sleep()
        if M_mia.is_state(S_mia_urgent_message):
            jump expression game.dialog_select("mia_urgent_text")

        elif M_mia.is_state(S_mia_midnight_call):
            jump expression game.dialog_select("mia_midnight_text")
        else:

            call check_pregnancies
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
