label erikmom_bedroom:
    if M_jenny.is_state(S_jenny_perv_on_tammy) and game.timer.is_morning():
        call expression game.dialog_select("telescope_jenny_perv_on_tammy")
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_tammy)
        hide screen telescope
        jump bedroom_jenny_give_cunni
    else:
        call expression game.dialog_select(game.telescope.mrsj)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_jenny_perv_on_tammy:
    if mrsj.over(mrsj_private_yoga):
        label mrsj_private_yoga_perv_jenny_replay:
        scene windowmrsjday 3a with dissolve
        player_name "( There she is... )"
        player_name "( Whoa, she's completely naked! )"
        pause
        scene windowmrsjday 3b with dissolve
        player_name "( What is she- )"
        scene windowmrsjday 3c-d
        player_name "( !!! )" with hpunch
        player_name "( Holy crap! )"
        pause
        player_name "( Does she know I'm watching?! )"
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
        player_name "Whoaaaa!"
        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_peeking a_empty f_empty
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk zorder 1 at Position (align=(0,0)) with dissolve
        jen "Spying on the neighbor girl again?"
        show jenny f_telescope_standing_grin
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (align=(0,0)) with hpunch
        player_name "N-no, I'm not-"
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Yeah, right."
        jen "Don't lie."
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "What's she doing now?"
        player_name "..."
        jen "Holy shit!"
        scene windowmrsjday 3c-d with dissolve
        jen "Isn't that your friend, what's his name's {b}landlady{/b}?"
        player_name "{b}Erik{/b}."
        jen "Yeah, {b}Erik{/b}."
        pause
        jen "Hah, what's she doing with that excers!"
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_worried_talk at Position (align=(0,0))
        show jenny b_telescope_look f_empty a_empty
        with fade
        player_name "I don't-"
        show player f_telescope_lay_worried
        show jenny f_telescope_surprised b_telescope a_telescope_down with dissolve
        jen "Wait a minute..."
        show jenny f_telescope_normal_talk
        jen "Does she know you're watching her?!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_laugh
        jen "No fucking way!"
        show jenny f_telescope_normal
        player_name "..."
        show jenny f_telescope_normal_talk
        jen "You're fucking {b}Mrs. Johnson{/b}, {b}[firstname]{/b}?!"
        show jenny f_telescope_normal
        show player f_telescope_lay_worried_talk
        player_name "Maybe... Just a little..."
        show player f_telescope_lay_worried
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "Hahahahaah!"
        pause
        jen "I have to give it to you, {b}[firstname]{/b}."
        jen "She's really good looking for her age."
        show player f_telescope_lay_worried_talk
        player_name "Y-yeah."
        show player f_telescope_lay_worried
        jen "I mean, she's no where near as hot as me but still-"
        player_name "..."
        show jenny b_telescope_rub a_telescope_rub with dissolve
        show player f_telescope_lay_surprised
        player_name "( !!! )"
        jen "Damn, look at her go..."
        jen "You think she's imagining your dick inside her, right now?"
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ renpy.end_replay()
    else:
        label mrsj_erik_cunni_perv_jenny_replay:
        scene windowmrsjday 4a with dissolve
        pause
        player_name "( Hmm, she's just talking to {b}Erik{/b}. )"
        player_name "( I guess, there's not going to be a show today... )"
        pause
        scene windowmrsjday 4b with dissolve
        player_name "( Wait a minute, is she- )"
        scene windowmrsjday 4c
        player_name "( !!! )" with hpunch
        player_name "( He's going down on her! )"
        pause
        player_name "( Way to go {b}Erik{/b}! )"
        scene expression "backgrounds/location_home_bedroom_caught_01.jpg" with dissolve
        player_name "Whoaaaa!"
        scene expression "backgrounds/location_home_bedroom_caught_02.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_03.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_caught_04.jpg" with dissolve
        pause
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_peeking a_empty f_empty
        show jenny b_telescope_standing a_empty f_telescope_standing_grin_talk zorder 1 at Position (align=(0,0)) with dissolve
        jen "Spying on the neighbor girl again?"
        show jenny f_telescope_standing_grin
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_surprised zorder 0 at Position (align=(0,0)) with hpunch
        player_name "!!!"
        show player f_telescope_lay_worried_talk
        player_name "N-no, I'm not-"
        show player f_telescope_lay_worried
        show jenny f_telescope_standing_grin_talk
        jen "Yeah, right."
        jen "Don't lie."
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "What's she doing now?"
        player_name "..."
        jen "Holy shit!"
        scene windowmrsjday 4c with dissolve
        jen "Isn't that your friend, what's his name?"
        player_name "{b}Erik{/b}."
        jen "Yeah, {b}Erik{/b}."
        pause
        jen "Hah, his landlady must be desperate if she's turning to that fat ass for some release!"
        scene expression "backgrounds/location_home_bedroom_telescope_window.jpg" with None
        show player b_telescope_laying_back a_telescope_side f_telescope_lay_worried_talk at Position (align=(0,0))
        show jenny b_telescope_look f_empty a_empty
        with fade
        player_name "Hey, be nice!"
        player_name "{b}Erik{/b} is a good guy."
        show player f_telescope_lay_worried
        show jenny f_telescope_laugh b_telescope a_telescope_down with dissolve
        jen "Pfft, yeah whatever."
        show jenny f_telescope_normal_talk
        jen "Nobody cares!"
        show jenny b_telescope_look f_empty a_empty with dissolve
        jen "Well, she seems to be enjoying herself..."
        show jenny b_telescope_rub a_telescope_rub with dissolve
        player_name "( !!! )"
        jen "I guess, tubbo really knows what he's doing."
        pause
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["03_unlocked"] = True
        $ renpy.end_replay()
    return

label telescope_mrsj_morning_1:
    scene windowmrsjmorning01
    player_name "( ...is that {b}Erik's landlady{/b}?! )"
    scene windowmrsjmorning01b
    player_name "( Oh wow! She's getting dressed... )"
    scene windowmrsjmorning01c
    player_name "( No! Just a little bit longer! )"
    scene windowmrsjmorning01d
    player_name "( Damn! Show's over... )"
    return

label telescope_mrsj_morning_2:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_afternoon_1:
    scene windowmrsjday01
    player_name "( She's not home. )"
    return

label telescope_mrsj_afternoon_2:
    show windowmrsjday 3a
    player_name "( Woah... She's completely naked!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Is that a bouncing ball... with a dildo on it?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Why didn't she close the blinds? )"
    show windowmrsjday 3c-d
    player_name "( It's like she wants to be seen... )"
    player_name "( I think she knows... )"
    player_name "( She's staring right at me. )"
    return

label telescope_mrsj_afternoon_3:
    scene windowmrsjday02
    player_name "( Her blinds are closed. She's probably not home. )"
    return

label telescope_mrsj_night_1:
    scene windowmrsjnight03
    player_name "( ...Is she practicing yoga? )"
    player_name "( ...On her bed? )"
    scene windowmrsjnight04
    player_name "..."
    player_name "( {b}Erik's landlady{/b} is so fit... )"
    player_name "( ...she really does have a great body... )"
    return

label telescope_mrsj_night_2:
    scene windowmrsjnight01
    player_name "( She's not in her room... )"
    return

label telescope_mrsj_night_3:
    scene windowmrsjnight02
    player_name "( She must be sleeping. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
