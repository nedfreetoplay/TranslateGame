label latinas_dialogue_shower:
    scene location_school_lockershowers_closeup
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    show player 57 zorder 0 at left
    with dissolve
    lopez "Hey! What are you doing in here?"
    show lopez f_angry
    show player 58
    player_name "Umm... Just trying to take a shower?"
    show lopez f_angry_talk
    show player 59
    lopez "Listen, boy. This is our turf, so go take a walk elsewhere!"
    show lopez f_angry
    show martinez f_normal_talk
    martinez "Wait, {b}Lopez{/b}!"
    martinez "Yo, I think this guy's the one people have been talking about!"
    show lopez f_angry_left_talk
    show martinez f_normal
    lopez "What?! No way..."
    lopez "You telling me this guy's packing a {b}huge dick{/b}?"
    show lopez f_angry
    show martinez f_angry_talk
    martinez "Alright boy! Show us what you got down there, and you can get in!"
    show martinez f_angry
    show player 60
    player_name "Uhh... I think I'll pass. I'll just shower at home then-"
    show martinez b_towelgrab f_empty a_empty
    pause
    show player 61
    show lopez f_surprised_down
    show martinez b_towel a_towel_hold_towel f_smirk_down
    with hpunch
    pause
    player_name "..."
    show player 62
    show martinez f_normal_talk_right
    martinez "There you go!"
    show martinez f_smirk_down
    show lopez f_normal_down_talk
    lopez "...That's what you call {b}big{/b}?"
    show lopez f_normal_down
    show martinez f_surprised_right
    martinez "Wha-"
    show player 63
    show martinez f_suspicious
    martinez "You soft?!..."
    martinez "...He needs a little excitement..."
    show martinez f_eyeroll
    martinez "...Hmm..."
    show martinez f_normal_talk_right
    martinez "...This should do the trick!"
    show lopez f_normal with None
    show martinez f_normal_talk_right b_towel a_empty
    show martinez_body_parts a_towel_hold_towel_pull1 zorder 3
    with dissolve
    pause
    show player 64
    show lopez f_surprised_down_down b_toweldown a_towel_surprised
    show martinez f_smirk_down
    show martinez_body_parts a_towel_hold_towel_pull2
    with hpunch
    pause
    show lopez f_angry_left_talk a_toweldown_cover1
    show martinez a_towel_crossed
    hide martinez_body_parts
    with dissolve
    lopez "Oh my god, puta!"
    show lopez f_angry
    show martinez f_normal_talk_right
    martinez "Chill, everyone's seen 'em at school already!"
    show martinez f_laugh
    martinez "Haha!"
    show martinez f_smirk_down
    show lopez f_surprised_down
    lopez "Yo, it's not doing anything!"
    show lopez f_normal_down
    show martinez f_eyeroll
    martinez "Maybe he's into guys?"
    show martinez f_angry
    show lopez f_normal_down_talk a_toweldown_pull1 with dissolve
    lopez "Here, I know what will work!"
    show martinez b_empty
    show martinez_body_parts b_towelup zorder 0
    show lopez f_normal_down a_toweldown_pull2
    with dissolve
    pause
    show martinez f_smirk_down2
    show lopez f_surprised_down
    with hpunch
    pause
    show player 65
    show martinez f_smirk_down
    player_name "...Oh... No..."
    pause
    show player 66 with hpunch
    show martinez f_surprised_down
    pause
    hide martinez_body_parts
    show martinez b_towel
    show lopez f_surprised_right a_toweldown_cover2
    with dissolve
    show player 67
    lopez "Oh, shit!"
    lopez "{b}Annie's{/b} coming!!"
    show lopez f_sorry
    show martinez f_sad_down a_towel_cover b_towel with dissolve
    show player 68
    show annie 1 zorder 3 at Position (xpos=400)
    ann "..."
    show annie 3
    ann "What's going on here??"
    show player 69
    show annie 1
    player_name "I was just trying to-"
    show player 68
    show annie 3
    ann "Expose yourself inappropriately?"
    show annie 4
    ann "{b}AGAIN{/b}!?"
    show player 69
    show annie 6
    player_name "No, that's not-"
    show player 68
    show annie 5
    ann "I don't want to hear your pathetic excuses!"
    ann "My orders are to bring in repeated offenders to the {b}Office{/b}!"
    show annie 7
    ann "Come with me, {b}NOW{/b}!!!"
    show annie 8f
    ann "...and you two, get out of here before I send you both to detention!!!"
    hide lopez
    hide martinez
    hide player
    hide annie
    with dissolve
    $ renpy.end_replay()
    return

label latinas_dialogue_leave:
    show player 57 at left
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    with dissolve
    lopez "Hey! You here to get us in trouble again?"
    show player 58 at left
    show lopez f_angry
    player_name "Umm... Just trying to take a shower?"
    show player 59 at left
    show martinez f_angry_talk
    martinez "Get out of here, yo!"
    show martinez f_angry
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
