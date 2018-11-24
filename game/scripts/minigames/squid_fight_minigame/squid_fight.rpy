label squid_attack:
    $ M_aqua.trigger(T_aqua_squid_defeated)
    scene location_lair_ocean_afterfight
    $ renpy.pause(1.0, hard = True)
    scene location_lair_ocean
    player_name "( Ah hah! She must be in that cave. )"
    player_name "( I'll need to find her quickly. )"
    player_name "( ...before I run out of air! )"
    player_name "( ...before I run out of air! )"
    call screen lair_entrance

label squid_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ game.timer.tick()
    scene location_lair_fail_squid
    with fade
    show text "The fight just wasn't going my way..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "The beast was too strong and the water was stifling." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I waited for my opening and made a mad dash to the surface" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_pier_minigame06b with fade
    show player 478 at Position (xpos=0.644,ypos=1.0) with dissolve
    player_name "*cough*"
    player_name "I couldn't do it."
    show player 479 at Position (xpos=0.663,ypos=1.0) with dissolve
    player_name "..."
    player_name "I need to make sure I'm better prepared next time."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
