label squid_attack:
    $ M_aqua.trigger(T_aqua_squid_defeated)
    scene location_lair_ocean_afterfight
    $ renpy.pause(1.0, hard = True)
    scene location_lair_ocean
    player_name "( А, ха! Она должно быть в той пещере. )"
    player_name "( Мне нужно найти ее быстро. )"
    player_name "( ...пока у меня не кончился воздух! )"
    player_name "( ...пока у меня не кончился воздух! )"
    call screen lair_entrance

label squid_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ game.timer.tick()
    scene location_lair_fail_squid
    with fade
    show text "Драка шла не по-моему..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Зверь был слишком силен, и вода душила." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я дождался своего открытия и сделал безумный рывок на поверхность." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_pier_minigame06b with fade
    show player 478 at Position (xpos=0.644,ypos=1.0) with dissolve
    player_name "*кхм*"
    player_name "Я не смог этого сделать."
    show player 479 at Position (xpos=0.663,ypos=1.0) with dissolve
    player_name "..."
    player_name "В следующий раз я должен быть лучше подготовлен."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
