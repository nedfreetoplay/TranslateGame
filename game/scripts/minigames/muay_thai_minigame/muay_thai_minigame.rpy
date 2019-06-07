label bag_minigame_attack:
    if cheat_pass:
        $ cheat_pass = False

    if player.stats.dex() < 4:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a with hpunch
    elif player.stats.dex() < 7:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a2 with hpunch
    elif player.stats.dex() < 9:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a3 with hpunch
    else:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a4 with hpunch

    $ player.stats.increase("dex")
    player_name "Huah!!"

    scene expression player.location.background_closeup with None
    if M_somrak.finished_state(S_somrak_sated_a):
        call expression game.dialog_select("button_somrak_panties_next_times")
    else:
        call expression game.dialog_select("button_somrak_panties_first_time")
    call expression game.dialog_select("button_somrak_panties_repeatable_continue")

    $ M_somrak.trigger(T_somrak_trained)
    $ game.timer.tick()
    $ game.main()


label training_failed_dialogue:
    scene expression game.timer.image("training{}_b")
    show masterplayer 27 at left
    show somrak f_angry a_cane_up
    mas "NO, NO, NO!" with vpunch
    mas "You're attacking like an undisciplined dog!"
    show somrak f_normal
    player_name "I'm sorry, {b}Master{/b}... I-"
    show somrak a_poke f_angry
    show masterplayer 40
    player_name "!!!" with hpunch
    show masterplayer 27
    show somrak f_angry a_point with dissolve
    mas "Do not be sorry, be better!"
    mas "Come back tomorrow!"
    show somrak a_cane f_normal with dissolve
    player_name "Y-yes, {b}Master Somrak{/b}..."
    hide masterplayer
    hide somrak
    with dissolve
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
