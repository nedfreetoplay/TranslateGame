label hospital_dialogue:
    $ player.go_to(L_hospital)
    if M_diane.is_state(S_diane_jizz_checkup) and L_hospital_room.is_here(M_diane):
        call expression game.dialog_select("hospital_jizz_checkup")
    if M_diane.pregnancy.stage == 5 and not M_diane.pregnancy.seen_in_labor:
        call expression game.dialog_select("hospital_diane_seen_in_labor")
        $ M_diane.pregnancy.seen_in_labor = True
        $ player.go_to(L_hospital_room)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
