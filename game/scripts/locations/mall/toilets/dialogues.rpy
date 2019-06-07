label mall_toilets_rump_n_cunt:
    scene mall_toilets_event_b
    player_name "( A body guard? )"
    player_name "( What is he doing in here... ) "
    return

label mall_toilets_stall:
    scene mall_toilets_stall
    show player 1 at left with dissolve
    player_name "( Nothing in here... just some crusty stains on the walls. )"
    hide player with dissolve
    $ game.main()

label rump_toilets_stall:
    call expression game.dialog_select("rump_toilets_stall_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Rump"]["unlocked"] = True
    $ persistent.cookie_jar["Rump"]["gallery"]["01_unlocked"] = True
    $ A_rump_n_pump.unlock()
    call screen button(Image = "boxes/auto_option_generic_02", Label = "rump_toilets_stall_block")

label rump_toilets_stall_dialogue:
    scene mall_toilets_stall
    show rump_overlay zorder 3
    show rump_n_cunt 01_02_03_04 zorder 2 at left
    with fade
    $ renpy.pause(1, hard=True)
    rump "YES!"
    $ renpy.pause(1, hard=True)
    rump "YOU NASTY WOMAN!!!"
    $ renpy.pause(1, hard=True)
    return

label rump_toilets_stall_block:
    call expression game.dialog_select("rump_toilets_stall_block_dialogue")
    $ game.timer.tick()
    $ game.rump_n_cunt = False
    $ player.go_to(L_mall)
    $ game.main()

label rump_toilets_stall_block_dialogue:
    scene mall_toilets_b with fade
    show player 37 at left with dissolve
    player_name "( ... )"
    show player 38
    player_name "( Was that mayor Rump?! )"
    show player 22
    show rump_guard 1 at right
    with hpunch
    player_name "!!!"
    show rump_guard 2
    guard "Hey!"
    guard "No one is allowed in here!"
    guard "I need you to leave right NOW!!!"
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
