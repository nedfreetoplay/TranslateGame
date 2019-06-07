label police_basement_roxxy_ask_earl_release:
    scene police_lobby_b
    show player 12 with dissolve
    player_name "We need to find an officer to ask about {b}Roxxy's{/b} Mom."
    hide player with dissolve
    return

label police_basement_first_visit:
    scene police_basement_b
    pause .4
    scene police_c_3
    show player 1
    with dissolve
    player_name "( This must be the \"drunk tank\" people talk about... )"
    hide player with dissolve
    return

label police_basement_mia_clues_summary:
    scene police_basement_b
    show player 35 with dissolve
    player_name "( Okay, so he's taking time off and took off for a drive this morning... )"
    player_name "( ...And he's drunk. )"
    show player 12
    player_name "Hmm..."
    player_name "( I need more {b}clues{/b}. )"
    player_name "( Maybe I should check his {b}desk{/b}... )"
    hide player with dissolve
    return

label police_basement_mia_inmate_status:
    scene police_basement_empty_b
    show player 4 at Position (xoffset=6) with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "( I don't see {b}Yumi{/b} anywhere, maybe I should- )"
    "*Shouting*" with hpunch
    show player 11
    player_name "..."
    show player 10
    player_name "( Is that coming from one of the cells?! )"
    hide player with dissolve
    return

label police_basement_mia_harold_backup:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( I have to find {b}Harold{/b} Quickly! )"
    hide player with dissolve
    return

label inmate_transfer_block:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( People are shouting! )"
    player_name "( I should check what's happening in those cells! )"
    hide player with dissolve
    $ game.main()

label police_cell_mia_inmate_status:
    scene police_cell_inside_fight1
    yum "Hey, stop!!!!"
    scene police_cell_inside_fight2
    crys "Arhh!!"
    scene police_cell_inside_fight1
    yum "...Help!! Get some backup!!"
    player_name "!!!"
    scene police_cell_inside_fight2
    player_name "I'll get {b}Harold{/b}!"
    scene police_cell_inside_fight1
    yum "Go! Quickly!"
    return

label police_cell_mia_harold_backup:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( I have to find {b}Harold{/b} quickly! )"
    hide player with dissolve
    return

label police_cell_mia_harold_to_the_rescue:
    scene police_cell_inside_cs1
    with fade
    show text "{b}Harold{/b} and I rushed to the basement.\nWhen {b}Harold{/b} walked into the cell, he froze for a moment...\n...But realized he had to find the courage to step in and help {b}Yumi{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause

    scene police_cell_inside_cs2
    with fade
    show text "Inside the cell was {b}Crystal{/b}...\n...{b}Roxxy's{/b} mom, notorious for causing trouble when drunk.\nIt turns out, she is quite a fighter after a few drinks..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause

    scene police_cell_inside_cs3
    with fade
    show text "{b}Harold{/b} had quite a bit of trouble at first...\n...But he soon found his old form.\nI could tell that despite the trouble, he enjoyed getting some action." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide police_cell_inside_cs1
    hide police_cell_inside_cs2
    hide police_cell_inside_cs3

    scene police_cell_c_02 with fade
    show harold 39 at Position (xpos=158)
    show yumi 5 at Position (xpos=855)
    harold "Now, STAY there!!"
    show harold 38
    show yumi 7
    yum "..."
    show harold 37
    harold "Are you okay?"
    show harold 36
    show yumi 6
    yum "Yeah, I just... I've never seen you like this before."
    show yumi 5
    show harold 37
    harold "Oh, it's just, you know... These type of people get on your nerves..."
    show harold 36
    show yumi 6
    yum "No, I meant like... Taking action like this."
    yum "It was really nice! It's a side of you I haven't seen before."
    show yumi 5
    show harold 37
    harold "You know what, I kind of missed that. The action."
    show harold 36
    show yumi 6
    yum "Thanks for having my back..."
    show yumi 5
    show harold 37
    harold "Oh, come on. I would do anything for my partner!"
    show harold 36
    show yumi 6
    yum "Ugh! I should have been more careful..."
    yum "...It was stupid of me and everyone at work will find out, I'm sure..."
    show yumi 5
    show harold 37
    harold "Well, {b}Yumi{/b}..."
    harold "I wouldn't worry to much about it..."
    show harold 42 at Position (xoffset=32) with dissolve
    pause
    show harold 43 at Position (xpos=195) with dissolve
    pause
    scene police_cell_inside_zoom
    pause
    scene police_cell_inside_splash with flash
    pause
    scene police_cell_c_02
    show harold 41 at Position (xpos=158)
    show yumi 7 at Position (xpos=855)
    with fade
    harold "...Because I'll take care of it."
    harold "Now, let's get out of here!"
    hide harold
    hide yumi
    with dissolve
    scene black with fade
    pause
    scene police_basement_empty_b
    show player 10f at right
    show harold 40 at left
    show yumi 5f at Position (xpos=550)
    with dissolve
    player_name "...{b}Harold{/b}?"
    show player 11f
    show harold 41
    harold "Hey, kid."
    show harold 40
    show player 10f
    player_name "Are you okay? Your shirt is ripped."
    show player 11f
    show harold 41
    harold "It's fine, just a scratch."
    show harold 40
    show player 12f
    player_name "Looks like your partner had a rough time as well..."
    show player 11f
    show yumi 6f
    yum "Oh, yeah... MY hair's a mess."
    show yumi 5 with dissolve
    show harold 41
    harold "Actually, I kind of like your hair this way. Keep it."
    show player 13f
    show harold 40
    show yumi 7
    yum "..."
    show harold 41
    harold "How about we go for a drive?"
    show harold 40
    show yumi 8
    yum "You mean, now?!"
    show yumi 9
    show harold 41
    harold "Yeah, it's nice out... and I'm thirsty."
    show harold 40
    show yumi 8
    yum "Ha ha. Fine. If you insist."
    show yumi 9
    show harold 41
    harold "Hop in the car, I'll meet you outside."
    show harold 40
    hide yumi with dissolve
    show player 14f
    player_name "I should let you go then."
    show player 13f
    show harold 41
    harold "Wait..."
    show harold 40
    show player 11f
    player_name "..."
    show harold 41
    harold "Thanks for all your...help."
    show harold 40
    show player 14f
    player_name "Oh, I... It's nothing, sir."
    show player 13f
    show harold 41
    harold "See ya, kiddo!"
    hide harold
    hide player
    with dissolve
    return

label police_cell_empty:
    scene police_cell
    show xtra 13 zorder 1 at left
    show player 10f zorder 2
    with dissolve
    player_name "( I wouldn't want to end up in there. Sheesh! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
