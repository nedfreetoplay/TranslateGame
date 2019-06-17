label park_dialogue:
    $ player.go_to(L_park)
    if game.timer.is_dark():
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_dark() and L_park.first_visit:
        call expression game.dialog_select("park_count_night_0")
        $ L_park.visited()
    $ game.main()

label park_fountain_dialogue:
    $ player.go_to(L_park_fountain)
    scene expression game.timer.image("park_fountain{}")
    if not player.has_item("weird_coin"):
        if game.timer.is_dark():
            show expression "objects/object_coin_01_night.png" at Position(xalign = 0.44, yalign = 0.81)
        else:

            show expression "objects/object_coin_01.png" at Position(xalign = 0.44, yalign = 0.81)
    player_name "( Я вижу тут много монет. )"
    $ player.location.call_screen(False, False)

label park_rap_battle:
    scene park_bench
    if M_dewitt.is_state(S_dewitt_eve_meet_up):
        call expression game.dialog_select("park_dewitt_eve_meet_up")
        $ M_dewitt.trigger(T_dewitt_gang_deal)

    elif M_eve.is_set("first park visit"):
        call expression game.dialog_select("park_rap_battle_first_visit")
        $ M_eve.set("first park visit", False)
        menu:
            "Клево выглядишь!":
                call expression game.dialog_select("park_rap_battle_first_visit_look_good")
                jump expression game.dialog_select("park_rap_battle_options")
            "Я должен идти домой.":

                call expression game.dialog_select("park_rap_battle_first_visit_go_home")
    else:

        call expression game.dialog_select("park_rap_battle_pre")
        menu park_rap_battle_options:
            "Давайте рэп-битву.":
                call expression game.dialog_select("park_rap_battle_start")
                menu:
                    "Чико":
                        $ rap_opponent = "Chico"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Чад" if player.stats.chr() < 4:
                        $ pass

                    "Чад" if player.stats.chr() >= 4:
                        $ rap_opponent = "Chad"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Тайрон" if player.stats.chr() < 7:
                        $ pass

                    "Тайрон" if player.stats.chr() >= 7:
                        $ rap_opponent = "Tyrone"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "Пропустить Мини-Игру (Cheat)" if game.cheat_mode:
                        $ game.timer.tick()
                        $ player.stats.increase("chr")
                        show unlock23 at truecenter with dissolve
                        pause
                        hide unlock23 with dissolve
            "Я должен идти.":

                call expression game.dialog_select("park_rap_battle_leave")

    hide player
    hide eve
    with dissolve
    $ game.main()

label park_night_closed:
    scene park_night
    show player 10 with dissolve
    player_name "( Уже поздно. Мне пора домой. )"
    hide player
    hide park_night
    $ game.main()

label park_pilly_button:
    call expression game.dialog_select("park_pilly_button_dialogue")
    $ player.go_to(L_map)
    $ M_roxxy.trigger(T_roxxy_drug_deal_over)
    $ game.timer.tick()
    $ game.sleep_lock = False
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
