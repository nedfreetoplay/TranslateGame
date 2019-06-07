label button_cedric_about_jenny:
    show player 10
    player_name "You know she's been trying to get ahold of you, right?"
    show player 5
    show cedric f_normal_talk
    ced "Yeah, believe me... I know."
    ced "I don't want anything to do with that crazy bitch!"
    show cedric f_normal
    show player 12
    player_name "That's a little harsh."
    show player 5
    show cedric f_normal_talk
    ced "You know she's gotten herself into doing porn or something?"
    show cedric f_normal
    show player 10
    player_name "Y-yeah, I know."
    show player 5
    show cedric f_normal_talk
    ced "Now she's trying to sweet talk me into doing it too!"
    show cedric f_normal
    show player 10
    player_name "Uh huh?"
    show player 5
    show cedric f_normal_talk
    ced "Do I look like the kinda guy who does porn?!"
    show cedric f_normal
    show player 29 with dissolve
    player_name "Err, I dunno... Kinda?"
    show player 3
    show cedric f_normal_talk
    ced "Yeah, well... I ain't!"
    ced "She just needs to find someone else to sink her talons into."
    ced "I'm done with her."
    show cedric f_normal
    show player 5 with dissolve
    player_name "..."
    show player 10
    player_name "Will you at least call and tell her that?"
    show player 5
    show cedric f_normal_talk
    ced "Why, so she can yell and call me names?"
    ced "No thanks."
    ced "You tell her."
    hide cedric with dissolve
    pause
    show player 37 with dissolve
    player_name "{b}*Sigh*{/b} Crap."
    player_name "( {b}[jen_name]{/b} isn't going to like this... )"
    player_name "( I'd better go and let her know. )"
    hide player with dissolve
    return

label button_cedric_see_ya:
    show player 14
    player_name "I should get going."
    show player 13
    show cedric f_normal_talk
    ced "Yeah, alright."
    ced "See you around, little buddy."
    show cedric f_normal
    hide player with dissolve
    pause
    show cedric f_normal_talk
    ced "Don't go skipping leg day now, Heh!"
    hide cedric with dissolve
    return

label button_cedric_can_you_spot_me:
    show player 10
    player_name "Can you spot me?"
    show player 13
    show cedric f_normal_talk a_dressed_reject with dissolve
    ced "No can do, little buddy."
    show player 5
    ced "You're not ready to work out with the big boys yet."
    show cedric f_normal a_dressed_hips with dissolve
    player_name "..."
    show cedric f_normal_talk a_dressed_point with dissolve
    ced "I don't wanna see you drop a nut or blow out your o-ring."
    show cedric f_normal a_dressed_hips with dissolve
    show player 10
    player_name "Uh huh, thanks for nothing."
    show player 5
    show cedric f_normal_talk
    ced "Aww, no need to get sore about it."
    ced "You'll get there soon enough."
    ced "Check this out!"
    show cedric f_normal a_dressed_flex with dissolve
    show player 13
    pause
    show cedric f_normal_talk
    ced "I'm getting pretty ripped, huh?"
    show cedric f_normal
    show player 14
    player_name "Sure, {b}Cedric{/b}..."
    show player 13
    show cedric f_normal_talk a_dressed_hips with dissolve
    ced "Heh, oh yeah!"
    show cedric f_normal
    return

label button_cedric_what_have_you_been_up_to:
    show player 14
    player_name "What have you been up to?"
    show player 13
    show cedric f_normal_talk
    ced "Oh, things have been great!"
    ced "Since I finally got that harpy roommate of yours off my back, I can finally focus on my workouts."
    show cedric f_normal
    show player 4
    player_name "Huh."
    show player 14 with dissolve
    player_name "Well, that's good... I guess."
    show player 13
    show cedric f_normal_talk
    ced "It's real good, little buddy!"
    show cedric a_dressed_point_himself with dissolve
    ced "You wanna come watch me do some dead lifts?"
    ced "I'm up to four-hundred and five pounds!"
    show cedric f_normal a_dressed_hips with dissolve
    show player 29 with dissolve
    player_name "Ehh, maybe some other time..."
    show player 13 with dissolve
    show cedric f_normal_talk
    ced "Suit yourself."
    show cedric f_normal
    return

label button_cedric_intro_repeat:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show cedric f_normal_talk
    ced "What's up, little buddy?"
    show cedric f_normal
    show player 14
    player_name "Oh, hey {b}Cedric{/b}."
    show player 13
    show cedric f_normal_talk
    ced "You here to bulk up?"
    show cedric f_normal
    return

label button_cedric_intro_first:
    scene expression player.location.background_closeup with None
    show cedric f_normal_talk
    show player 13 at left
    ced "Whoa, {b}[firstname]{/b}?"
    show cedric f_normal
    show player 14
    player_name "Oh, hey {b}Cedric{/b}."
    show player 13
    show cedric f_normal_talk
    ced "I haven't seen you for awhile, little buddy."
    show cedric f_normal
    show player 14
    player_name "Uh huh."
    show player 13
    show cedric f_normal_talk a_dressed_point with dissolve
    ced "You finally decide to hit the gym and bulk up?"
    show cedric f_normal a_dressed_hips with dissolve
    show player 29 with dissolve
    player_name "Y-yeah, something like that..."
    show player 13 with dissolve
    show cedric f_normal_talk
    ced "How's {b}[jen_name]{/b}?"
    show cedric f_normal
    show player 12
    player_name "Umm, I dunno... Bitchy?"
    show player 13
    show cedric f_normal_talk
    ced "Hahaha, good one!"
    show cedric f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
