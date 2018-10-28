label dining_room_dialogue:
    $ player.go_to(L_home_diningroom)
    if sister.started(sis_breakfast):
        call expression game.dialog_select("dining_room_sis_breakfast_started")

    elif M_mom.is_state(S_mom_fetch_towel) and player.has_item("towel"):
        jump expression game.dialog_select("mom_pool_dialogue")
    $ game.main()

label dining_room_table_dialogue:
    scene expression game.timer.image("dining_room{}")
    if M_mom.is_state(S_mom_diane_dinner) and game.timer.is_evening():
        call expression game.dialog_select("dining_room_mom_diane_dinner")
        $ M_mom.trigger(T_mom_diane_dinner_chat)

        $ player.go_to(L_home_entrance)
        $ game.timer.tick()
    else:

        show player 2 with dissolve
        player_name "( Здесь никого нет. Стол тоже не накрыт. )"
    $ game.main()

label dining_room_table_sis:
    scene dining_room with None
    show object_diningtable zorder 1 at Position(ypos=581)
    show jenny 44 at left
    show player 316 zorder 0 at Position(xpos=610)
    with dissolve
    if not sister.completed(sis_breakfast):
        call expression game.dialog_select("dining_room_sis_breakfast")

        $ sis_breakfast.finish()
        $ M_jenny.unforce()
    else:

        call expression game.dialog_select("dining_room_sis_breakfast_done")
    hide player
    hide jenny
    with dissolve
    jump expression game.dialog_select("dining_room_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
