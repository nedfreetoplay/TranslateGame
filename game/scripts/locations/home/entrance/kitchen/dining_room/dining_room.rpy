label dining_room_dialogue:
    $ player.go_to(L_home_diningroom)
    if M_mom.is_state(S_mom_fetch_towel) and player.has_item("towel"):
        jump expression game.dialog_select("mom_pool_dialogue")

    if M_jenny.is_state(S_jenny_have_breakfast_3):
        call expression game.dialog_select("dining_room_jenny_have_breakfast_3")
        $ M_jenny.trigger(T_jenny_wait_a_day)
        $ player.go_to(L_home_entrance)
        $ game.main()
    elif M_jenny.is_state(S_jenny_cedric_upset) and game.timer.is_morning():
        call expression game.dialog_select("dining_room_jenny_cedric_upset")
        $ M_jenny.trigger(T_jenny_talk_to_cedric)
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.is_state(S_jenny_pissed_at_handjob) and game.timer.is_morning():
        call expression game.dialog_select("dining_room_jenny_pissed_at_handjob")
        $ M_jenny.trigger(T_jenny_reconciliation_handjob)
        $ game.timer.tick()
    elif M_jenny.is_state(S_jenny_pissed_at_blowjob) and game.timer.is_morning():
        call expression game.dialog_select("dining_room_jenny_pissed_at_blowjob")
        $ M_jenny.trigger(T_jenny_reconciliation_blowjob)
        $ game.timer.tick()
    elif M_jenny.is_state(S_jenny_have_breakfast_4) and game.timer.is_morning():
        call expression game.dialog_select("dining_room_jenny_have_breakfast_4")
        $ M_jenny.trigger(T_jenny_get_cheerleader_outfit)
        $ game.timer.tick()
    $ game.main()

label dining_room_table_dialogue:
    scene expression game.timer.image("dining_room{}")
    show player 323e zorder 0 at Position(xpos=750,ypos=770)
    show expression "characters/xtra/overlay_o_dinner_table.png" with None
    with dissolve
    player_name "( Nobody's here. The table isn't set either. )"
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
