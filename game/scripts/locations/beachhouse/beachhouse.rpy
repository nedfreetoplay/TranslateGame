label beach_house_front_dialogue:
    $ player.go_to(L_beachhouse_front)
    $ game.main()

label beach_house_entrance_dialogue:
    $ player.go_to(L_beachhouse_entrance)
    if L_beachhouse_entrance.first_visit:
        call expression game.dialog_select("beach_house_first_time")
        $ L_beachhouse_entrance.first_visit = False
    if L_beachhouse_entrance.is_here(M_consuela) and M_consuela.is_state(S_consuela_start):
        call expression game.dialog_select("beach_house_entrance_meet_consuela")
        $ M_consuela.trigger(T_consuela_intro)

    if L_beachhouse_entrance.is_here(M_consuela) and M_consuela.is_state(S_consuela_end) and player.has_item("mysterious_statue_1") and player.has_item("mysterious_statue_2") and not player.has_item("mysterious_statue_3"):
        call expression game.dialog_select("beach_house_entrance_mysterious_statue_3")
        $ player.get_item("mysterious_statue_3")
    $ game.main()

label beach_house_bedroom_dialogue:
    $ player.go_to(L_beachhouse_bedroom)
    $ game.main()

label beach_house_patio_dialogue:
    $ player.go_to(L_beachhouse_patio)
    $ game.main()

label beach_house_not_bought_dialogue:
    $ player.go_to(L_beachhouse_front)
    call expression game.dialog_select("beachhouse_not_bought")
    $ game.main()

label beach_house_sleeping:
    scene expression "backgrounds/location_beach_house_bedroom_sleep.jpg"
    pause
    $ Sleep()
    if M_player.is_set("just wokeup"):
        call expression game.dialog_select("player_just_wokeup")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
