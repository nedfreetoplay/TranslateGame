label map_dialogue:
    $ player.go_to(L_map)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

        if June.started(june_mc_help):
            call expression game.dialog_select("map_june_mc_help_started")
            $ june_mc_help.finish()

        elif June.started(june_erik_help):
            call expression game.dialog_select("map_june_erik_help_started")
            $ june_erik_help.finish()

        elif erik.in_progress(erik_intro):
            call expression game.dialog_select("map_erik_intro_in_progress")
            $ L_diane_yard.unlock()
            $ L_mall.unlock()
            $ L_beach.unlock()
            $ L_treehouse.unlock()
            $ L_hill.unlock()
            $ L_warehouse.unlock()
            $ L_beachhouse_front.unlock()
            $ L_boat_bridge.unlock()
            $ L_rump_front.unlock()
            $ L_map.unlock(False, False)
            $ erik.complete_events(erik_intro)
            $ M_erik.place(place = L_erikhouse_basement)
            $ M_erik.force()

            $ game.sleep_lock = False
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
