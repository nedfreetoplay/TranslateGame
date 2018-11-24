label beach_house_front_dialogue:
    $ player.go_to(L_beachhouse_front)
    $ game.main()

label beach_house_entrance_dialogue:
    $ player.go_to(L_beachhouse_entrance)
    if L_beachhouse_entrance.first_visit:
        call expression game.dialog_select("beach_house_first_time")
        $ L_beachhouse_entrance.first_visit = False
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
