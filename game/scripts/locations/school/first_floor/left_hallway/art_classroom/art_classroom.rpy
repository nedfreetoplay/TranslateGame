default art_classroom_first_visit = True

label art_classroom_dialogue:
    $ player.go_to(L_school_artclassroom)
    call pa_announcement
    if player.location.is_here(M_ross):
        if M_ross.is_state(S_ross_start):
            call expression game.dialog_select("art_classroom_ross_start")
            $ M_ross.trigger(T_ross_intro)

    if M_mia.is_state(S_mia_find_easel):
        call expression game.dialog_select("art_classroom_mia_find_easel")
        $ M_mia.trigger(T_mia_easel_found)
    $ game.main()

label easel_dialogue:
    scene art_classroom_b
    if M_mia.is_state(S_mia_show_tattoo):
        call expression game.dialog_select("easel_dialogue_mia_show_tattoo")
    else:

        show player 35 with dissolve
        player_name "( What should I draw today? )"
        menu:
            "Tattoo ideas.":
                call expression game.dialog_select("easel_dialogue_mia_draw_tattoo_intro")
                call screen tattoos
                call expression game.dialog_select("easel_dialogue_mia_draw_tattoo_drawn")
                $ M_mia.trigger(T_mia_visit)
                show expression [drawn_tattoo] at truecenter with dissolve
                $ player.get_item(drawn_tattoo)
                pause
                hide expression [drawn_tattoo] with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
