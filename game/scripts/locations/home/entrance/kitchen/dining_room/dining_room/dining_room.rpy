label dining_room_dialogue:
    $ player.go_to(L_home_diningroom)
    if M_jenny.is_state(S_jenny_breakfast):
        call expression game.dialog_select("dining_room_sis_breakfast_started")

    elif M_mom.is_state(S_mom_fetch_towel) and player.has_item("towel"):
        jump expression game.dialog_select("mom_pool_dialogue")
    $ game.main()

label dining_room_table_dialogue:
    scene expression game.timer.image("dining_room{}")
    show player 2 with dissolve
    player_name "( Здесь никого нет. Стол тоже не накрыт. )"
    $ game.main()

label dining_room_table_sis:
    scene dining_room with None
    show object_diningtable zorder 1 at Position(ypos=581)
    show jenny 44 at left
    show player 316 zorder 0 at Position(xpos=610)
    with dissolve
    if M_jenny.is_state(S_jenny_breakfast):
        call expression game.dialog_select("dining_room_sis_breakfast")
        $ M_jenny.trigger(T_jenny_breakfast_done)
    else:

        call expression game.dialog_select("dining_room_sis_breakfast_done")
    hide player
    hide jenny
    with dissolve
    jump expression game.dialog_select("dining_room_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
