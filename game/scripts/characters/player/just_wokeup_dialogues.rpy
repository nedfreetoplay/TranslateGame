label player_jenny_sleepover_mcbedroom:
    scene expression "backgrounds/location_home_bedroom_cutscene19.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene20.jpg" with dissolve
    player_name "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene21.jpg" with dissolve
    player_name "You're leaving?"
    if M_jenny.get("jenny_girlfriend_first_time"):
        $ M_jenny.set('jenny_girlfriend_first_time', False)
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Yeah, the sun is up which means your time is over."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Oh."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Besides, {b}[deb_name]{/b} will be awake soon and I don't want her finding me in here."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Did you sleep okay?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "I did, actually."
        jen "In spite of your crazy loud snoring."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "What?!"
        player_name "I don't snore!"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Heh, whatever."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Can we do this again?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Sure, as long as you're paying."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "But-"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Later, loser."
    else:
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Yeah, {b}[deb_name]{/b} will be up soon."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Oh, okay."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Remember to come by {b}my room{/b} this afternoon for our show."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Alright, I will."
        scene black with fade
        pause
    return

label player_jenny_sleepover_sisbedroom:
    scene expression player.location.background_blur
    show jenny b_panties a_naked_hips f_upset
    show player b_underwear a_naked_sides f_normal_talk
    player_name "Good morning!"
    show player f_normal
    show jenny f_eyeroll
    jen "Yeah, yeah..."
    show jenny f_upset_talk
    jen "Get lost, I need a shower."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Sheesh, that's it?"
    player_name "You're not a very fun person to wake up next to..."
    show player f_skeptical
    show jenny f_upset_talk
    jen "Well, what do you want me to do?!"
    jen "Fix you breakfast or something?"
    jen "Get real."
    show jenny f_upset
    show player f_worried_talk
    player_name "I would never ask you to do that, {b}[jen_name]{/b}..."
    show player f_laugh
    player_name "... I've tasted your cooking, it's awful."
    show player f_grin
    show jenny f_eyeroll a_naked_crossed with dissolve
    jen "Fuck you!"
    show jenny f_upset
    show player f_laugh
    player_name "Hahaah!"
    hide player with dissolve
    show jenny f_gross_talk
    jen "Asshole."
    show jenny f_gross
    return

label bedroom_sis_webcam_show:

    show player 4 with dissolve
    player_name "Hmm..."
    player_name "( I wonder what {b}[jen_name]{/b} is doing right now. )"
    show player 1
    player_name "( Maybe I could connect to her {b}webcam{/b} from my computer... )"
    hide player with dissolve
    return

label bedroom_bissette_roxxy_jenny_mentoring:
    show player 12 with dissolve
    player_name "{b}Roxxy{/b} is supposed to meet {b}[jen_name]{/b} for a cheer-leading session."
    show player 10
    player_name "{b}I should head home{/b} and make sure {b}[jen_name]{/b} doesn't flake on her."
    hide player with dissolve
    return

label bedroom_dewitt_make_replacement_guitar:
    if game.timer.is_dark():
        show player 14 with dissolve
        player_name "I think I have everything I need to make my fake guitar."
        show player 4
        player_name "I need to remember to assemble it in the garage tomorrow."
        hide player with dissolve
    else:
        show player 14 with dissolve
        player_name "I think I have everything I need to make my fake guitar."
        player_name "I should head back to my garage so I can start working on it."
        hide player with dissolve
    return

label bedroom_sis_telescope_1:

    show player 4 with dissolve
    player_name "( I wonder what {b}Erik{/b} is doing right now. )"
    player_name "( I should use my {b}telescope{/b} and see what he's up to... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_2:

    show player 4 with dissolve
    player_name "( I wonder what {b}Mia{/b} is doing right now. )"
    player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_3:

    show player 4 with dissolve
    player_name "( I wonder what {b}Mrs. Johnson{/b} is doing right now. )"
    player_name "( I should use my {b}telescope{/b} and see what she's up to... )"
    hide player with dissolve
    return

label bedroom_master_somrak_training:

    show player 4 with dissolve
    player_name "( I wonder if {b}Master Somrak{/b} is ready to train me again. )"
    hide player with dissolve
    return

label bedroom_roxxy_spin_bottle:
    show player 17 with dissolve
    player_name "{b}Roxxy{/b} and the girls wanted me to visit the beach this afternoon."
    player_name "I should head there now!"
    return

label bedroom_roxxy_spin_bottle_no_goldschwagger:
    show player 4 with dissolve
    player_name "( I also still need to talk to {b}Captain Terry{/b} about {b}GoldSchwagger{/b} for {b}Becca{/b}. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
