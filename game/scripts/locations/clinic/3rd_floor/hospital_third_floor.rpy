label hospital_third_floor_dialogue:
    $ player.go_to(L_hospital_floor3)
    $ game.main()

label hospital_floor3_locked:
    scene expression "backgrounds/location_hospital_elevator_interior.jpg" with None
    show player 427g with dissolve
    player_name "( I have no reason to go to the third floor. )"
    player_name "( Besides, the floor description just says it's some sort of lab anyway. )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
