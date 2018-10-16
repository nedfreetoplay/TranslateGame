label mall_toilets_rump_n_cunt:
    scene mall_toilets_event_b
    player_name "( Телохранитель? )"
    player_name "( Что он здесь делает... ) "
    return

label mall_toilets_stall:
    scene mall_toilets_stall
    show player 1 at left with dissolve
    player_name "( Здесь ничего нет... разве что несколько старых подтёков на стенах. )"
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
    rump "ДА!"
    $ renpy.pause(1, hard=True)
    rump "ТЫ ГРЯЗНАЯ ЖЕНЩИНА!!!"
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
    player_name "( Это был мер Рамп?! )"
    show player 22
    show rump_guard 1 at right
    with hpunch
    player_name "!!!"
    show rump_guard 2
    guard "Эй!"
    guard "Здесь никому нельзя находиться!"
    guard "Ты должен уйти от сюда прямо СЕЙЧАС!!!"
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
