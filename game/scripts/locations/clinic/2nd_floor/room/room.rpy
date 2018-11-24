label hospital_second_floor_room_dialogue:
    $ player.go_to(L_hospital_room)
    if M_diane.is_state(S_diane_jizz_checkup) and L_hospital_room.is_here(M_diane):
        call expression game.dialog_select("hospital_second_floor_room_jizz_checkup")
        $ M_diane.trigger(T_diane_bathroom_sampling)
        $ game.main()
    $ game.main()

label hospital_2nd_floor_room_bathroom_dialogue:
    $ player.go_to(L_hospital_room_bathroom)
    if M_diane.is_state(S_diane_jizz_checkup_extra_hand) and L_hospital_room.is_here(M_diane):
        jump micoe_bj_scene
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
