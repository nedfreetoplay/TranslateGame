label micoe_button_dialogue:
    scene expression player.location.background_blur
    call expression game.dialog_select("micoe_dialogue_intro")
    menu micoe_menu_options:
        "Увеличить шанс зачатия." if M_diane.finished_state(S_diane_checkup_results) and M_priya.is_state(S_priya_start):
            call expression game.dialog_select("micoe_dialogue_increase_chance_of_conception")
            $ M_priya.trigger(T_priya_start)
            $ game.main()

        "Отсос." if M_diane.finished_state(S_diane_checkup_results):
            call expression game.dialog_select("micoe_dialogue_blowjob")
            if game.timer.is_day():
                $ player.go_to(L_hospital_room)
            else:
                $ player.go_to(L_map)
            jump micoe_bj_loop

        "Таблетки Pregnax." if M_priya.finished_state(S_priya_talk_to_roz):
            call expression game.dialog_select("micoe_dialogue_pregnax")
            jump micoe_menu_options
        "Просто поздороваться.":

            call expression game.dialog_select("micoe_dialogue_goodbye")
            $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
