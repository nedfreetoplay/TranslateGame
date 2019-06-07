label trailer_lock_check(destination_screen):
    scene expression player.location.background_blur
    $ destination = destination_screen.lower()
    $ destination_label = destination + "_dialogue"
    if M_roxxy.is_state(S_roxxy_studying_at_roxxys) and not game.timer.is_dark() and destination == "trailer":
        show player 34 with dissolve
        player_name "( I'm supposed to meet {b}Roxxy{/b} there this {b}evening{/b}. I should wait till then. )"
        hide player with dissolve

    elif M_roxxy.is_state(S_roxxy_studying_at_mcs) and destination not in ["trailer", "trailer_park"]:
        if destination == "trailer_interior" and not M_roxxy.get("heard clyde in trailer"):
            $ M_roxxy.set("heard clyde in trailer", True)
            scene trailer_interior_c
            show crystal 12 at right
            show clyde 17 at left
            with dissolve
            clyde "Jesus, {b}Auntie{/b}! Slow down a bit!"
            show clyde 16
            show crystal 13
            crys "Don't you worry 'bout me!"
            crys "I been doin' this since before you was born."
            show crystal 12
            show clyde 17
            clyde "I'm just sayin', yer gonna screw up the count!"
            show clyde 16
            show crystal 13
            crys "Just sit your butt over there lookin' perty and let your {b}Auntie{/b} do her thing!"
            show crystal 12
            player_name "( Hmm, are they... Wow! That's a big stack of money! )"
            player_name "( Where the heck did they get that I wonder? )"
            player_name "( I'd better get out of here before they see me! )"
            scene black with fade
        else:
            scene expression player.location.background_blur
            show player 34 with dissolve
            player_name "( Hmm, no... )"
            player_name "( I need to catch up with {b}Roxxy{/b}! )"
            hide player with dissolve
        $ game.main()
    elif M_roxxy.is_state(S_roxxy_get_uniform_on_doggo):
        if not player.has_item("roxxy_uniform") and destination not in ["trailer_park", "trailer_shack", "shack_doghouse"]:
            if destination == "trailer_shack_interior":
                scene expression player.location.background_blur
                player_name "( Hmm, that {b}pig{/b} should be around here somewhere... )"
                jump expression destination_label
            else:
                show player 12 with dissolve
                player_name "I'm supposed to look for {b}Clyde's Pig{/b}."
                show player 10
                player_name "I should probably check around his {b}Shack{/b}."
                hide player with dissolve
        elif destination not in ["trailer_park", "trailer"] and player.has_item("roxxy_uniform"):
            show player 10 with dissolve
            player_name "I'm supposed to follow {b}Roxxy{/b} back to {b}her trailer{/b}."
            hide player with dissolve
        else:
            if destination in ["trailer_interior", "trailer_bedroom", "trailer_shack_interior"]:
                $ playSound()
                play audio sfxDoor()
            jump expression destination_label
    elif M_roxxy.is_state(S_roxxy_beat_clyde) and destination not in ["trailer_park", "trailer_tractor"]:
        show player 10 with dissolve
        player_name "Hmm, I should follow {b}Roxxy{/b}..."
        player_name "She said something about a {b}Tractor{/b}?"
        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_wait_in_her_room) and destination not in ["trailer", "trailer_interior", "trailer_bedroom"]:
        if destination == "roxxy_trailer_button":
            show player 5 at left
            show roxxy 1 at right
            with dissolve
            player_name "..."
            show roxxy 3c
            rox "Seriously, quit staring at me and go wait in my room!"
            show roxxy 1b
            rox "I'll be there in a minute."
            show roxxy 1
            show player 10
            player_name "Yeah, okay."
            hide roxxy
            hide player
            with dissolve
        else:
            show player 14 with dissolve
            player_name "I'm supposed to wait for {b}Roxxy{/b} in her room."
            hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_confront_clyde) and destination not in ("trailer_park", "trailer_tractor", "trailer_shack"):
        show player 10 with dissolve
        player_name "( {b}Roxxy{/b} took off after {b}Clyde{/b}! )"
        player_name "( I should find them before {b}Roxxy{/b} murders him! )"
        hide player with dissolve
    elif M_roxxy.is_state(S_roxxy_picnic_done) and destination != "trailer_bedroom":
        show player 13 at left
        show player_wet at left
        with dissolve
        player_name "( I should go dry off with {b}Roxxy{/b} inside her room! )"
        hide player
        hide player_wet
        with dissolve
    else:
        if destination in ["trailer_interior", "trailer_bedroom", "trailer_shack_interior"]:
            $ playSound()
            play audio sfxDoor()
        jump expression destination_label
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
