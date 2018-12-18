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
