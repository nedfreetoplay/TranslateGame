label grace_dialogue:
    scene tattoo_indoor_c
    if M_mia.is_state(S_mia_buy_tattoo) and player.location.is_here(M_mia):
        call expression game.dialog_select("button_grace_mia_get_tattoo")
    else:
        call expression game.dialog_select("button_grace_generic")
    show grace 1
    menu grace_menu_dialogue:
        "Тату." if M_mia.is_state(S_mia_buy_tattoo) and player.location.is_here(M_mia):
            call expression game.dialog_select("button_grace_tattoo")
            menu:
                "Я помогу тебе." if player.has_money(200):
                    call expression game.dialog_select("button_grace_tattoo_help")
                    $ player.spend_money(200)
                    $ game.timer.tick()
                    $ M_mia.trigger(T_mia_tattoo_done)
                "Вернись позже.":

                    call expression game.dialog_select("button_grace_tattoo_come_back")

        "Краска" if M_ross.is_state(S_ross_get_paint_grace):
            call expression game.dialog_select("button_grace_paint")
            $ M_ross.set("talked to grace", True)

        "Ты кажешься мне знакомой." if M_grace.is_state(S_grace_start) and not player.location.is_here(M_mia):
            call expression game.dialog_select("button_grace_you_look_familiar")
            $ M_grace.trigger(T_grace_intro)
            jump expression game.dialog_select("grace_menu_dialogue")
        "Ничего.":

            call expression game.dialog_select("button_grace_nothing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
