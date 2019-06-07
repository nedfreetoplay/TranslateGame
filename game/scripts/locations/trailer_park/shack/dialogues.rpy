label trailer_shack_cant_go_in:
    scene expression L_trailer_shack.background_blur
    player_name "I can't go there now."
    return

label shack_doghouse_roxxy_get_uniform_on_doggo:
    scene expression "backgrounds/location_trailer_shack_day_closeup.jpg"
    show player 109f at left
    show roxxy 3d at right
    with dissolve
    pig "{b}*Oink Oink*{/b}"
    show player 111f
    player_name "There you are!"
    show player 110f
    pig "{b}*Snort*{/b}"
    show roxxy 3c
    rox "Ugh, disgusting thing!"
    show roxxy 3d
    show player 111f
    player_name "Naw, you're cute... Aren't you?"
    show player 110f
    pig "{b}*Oink*{/b}"
    show player 184 with dissolve
    pause
    show player 630 with dissolve
    player_name "Sorry, girl."
    player_name "You've gotta give this uniform back to {b}Roxxy{/b}..."
    show player 631 with dissolve
    pause
    show player 632 with dissolve
    pig "{b}*Squeeeee*{/b}"
    show player 633 with dissolve
    player_name "Heh, don't worry."
    player_name "I'm sure {b}Clyde{/b} will find you something else to wear."
    show player 184 with dissolve
    pause
    show player 634 with dissolve
    pig "{b}*Snort*{/b}"
    show roxxy 2
    rox "Yeah, probably from my wardrobe."
    show player 5
    show roxxy 61
    with dissolve
    player_name "..."
    show roxxy 60
    rox "What a mess!"
    show roxxy 62
    rox "C'mon, let's get back to my place."
    rox "I'll have to wash the pig stink off this!"
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
