label dianes_kitchen_diane_look_in_kitchen:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    player_name "( !!! )" with hpunch
    pause
    dia "Ngghhh..."
    player_name "( {b}Diane{/b} is... )"
    player_name "( She's... )"
    player_name "( ... Is that a cucumber? )"
    pause
    dia "Mmm, that's it!"
    $ M_diane.set("sex speed",0.3)
    show diane_masturbate 1_2
    player_name "( This is... )"
    dia "Fuck me harder, stud!"
    player_name "( I wonder who she's imagining? )"
    pause
    player_name "( I should get out of here before she sees me. )"
    pause
    hide diane_masturbate with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["01_unlocked"] = True
    $ renpy.end_replay()
    return

label dianes_kitchen_diane_clean_garden_report:
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 5f with dissolve
    player_name "..."
    show player 10f
    player_name "... Hello?!"
    show player 22f
    dia "EEEEKKK!!!" with hpunch
    player_name "!!!"
    show player 23f
    player_name "Diane?!"
    show player 22f
    dia "{b}[firstname]{/b}! Help!!!"
    show player 23f
    player_name "Where are you?!"
    show player 22f
    dia "AAHHHH!!!" with hpunch
    show player 23f
    player_name "It sounds like she's upstairs!"
    hide player with dissolve
    scene black with dissolve
    scene expression "backgrounds/location_diane_bedroom_closeup.jpg"
    show diane b_pole a_empty f_pole_scream
    show player 11 at left
    with dissolve
    dia "HELP!!!"
    show player 10
    player_name "{b}Diane{/b}?!"
    player_name "What's the mat-"
    show player 11
    dia "M-MM-MM-MOUSE!"
    show player 12
    player_name "Huh, mouse?"
    show player 14
    player_name "Is that what's got you so scared?"
    show player 13
    dia "..."
    show player 14
    player_name "Where is it?"
    show player 13
    show diane b_pole_point f_pole_scared_talk_back with dissolve
    dia "C-closet!"
    show diane f_pole_scared
    show player 10
    player_name "You saw a mouse in your closet?"
    show diane b_pole with dissolve
    show player 14
    player_name "I'll check it out."
    show diane f_pole_scared_talk_back
    show player 108f at right with dissolve
    player_name "I don't-"
    show player 670 with dissolve
    player_name "..."
    "{b}*Thud*{/b}"
    show player 22 at left
    player_name "!!!" with hpunch
    show diane f_pole_scream
    dia "EEEEKKK!!!"
    hide player
    show diane pickup
    player_name "HRRGGG!!!" with hpunch
    player_name "..."
    show diane pickup_scared
    dia "Was that the mouse?!"
    show diane pickup
    player_name "I... I don't know..."
    show diane pickup_talk
    dia "I hate mice!"
    show diane pickup_laugh
    player_name "Hehe, you deal with dirt and bugs all the time but mice freak you out?"
    show diane pickup_talk
    dia "YES!!!"
    show diane pickup_scared
    dia "Do you see it?!"
    show diane pickup
    player_name "Err... No?"
    show diane pickup_talk
    dia "I see it!"
    show diane pickup
    player_name "... Where?"
    show diane pickup_scared
    dia "RIGHT THERE!!"
    dia "See it's tail?!"
    show diane pickup
    player_name "..."
    player_name "I think that's a shoe lace..."
    show diane pickup_talk
    dia "What?! NO!!!"
    show diane pickup_scared
    dia "That's a mouse!"
    player_name "..."
    show diane pickup
    player_name "It's kinda hard to see with you squeezing my head..."
    show diane pickup_talk
    dia "Hmm?"
    dia "Oh, I'm sorry, {b}[firstname]{/b}!"
    show diane b_pole a_empty f_pole_scared
    show player 17 at left
    with dissolve
    player_name "Heh, it's alright."
    show player 14
    player_name "Now, let me take care of that shoe lace for you..."
    hide player with dissolve
    show diane f_pole_scared_talk_back
    dia "I'm telling you, it's a mouse!"
    show diane f_pole_scream
    dia "Ugh, be careful, {b}[firstname]{/b}!!!"
    player_name "..."
    show diane f_pole_scared
    show player 682 at left with dissolve
    player_name "..."
    show player 683
    player_name "{b}*Ahem*{/b}"
    show player 682
    show diane f_pole_scared
    dia "..."
    show diane f_pole_scared_talk
    dia "It's a shoe lace."
    show diane f_pole_scared
    show player 683
    player_name "Heh, I told you!"
    show player 682
    show diane b_lingerie a_lingerie_sides f_scared_talk
    with dissolve
    dia "Are you sure there isn't a mouse in there?"
    show diane f_scared
    show player 683
    player_name "Pretty sure."
    show player 13 at left with dissolve
    show diane f_laugh
    dia "Phew!"
    show diane f_scared_talk
    dia "I almost had a heart attack..."
    show diane f_normal
    show player 14
    player_name "Yeah, I've never seen you so worked up before."
    player_name "You alright, now?"
    show player 13
    show diane f_normal_talk
    dia "Yeah, I think so."
    show diane f_normal
    dia "..."
    show player 17
    player_name "... I can't believe you were screaming at a shoe lace!"
    player_name "Hahaha!"
    show diane f_laugh
    dia "Oh, shut up!"
    show diane f_normal
    show player 13
    show diane f_surprised_front
    pause
    show diane f_surprised_front_talk a_lingerie_cover with dissolve
    dia "... I'm... naked..."
    show diane f_shamed
    show player 10
    player_name "Well, not really naked..."
    show player 5
    show diane f_shamed_talk
    dia "I might as well be."
    dia "I'm sorry, {b}[firstname]{/b}."
    dia "I'm embarrassed."
    show diane f_shamed
    show player 10
    player_name "Hmm?"
    player_name "There's no need to be embarrassed..."
    show player 14
    player_name "You look fantastic!"
    show player 13
    show diane a_lingerie_shock f_laugh at Position (yoffset=13) with dissolve
    dia "{b}[firstname]{/b}!!!"
    show diane f_smirk at Position (yoffset=13)
    show player 17
    player_name "What? You do."
    show player 13
    show diane f_smirk_talk a_lingerie_sides with dissolve
    dia "{b}Debbie{/b} would throw a fit if she knew you saw me like this."
    show diane f_smirk
    show player 14
    player_name "Well, I'm not going to tell her..."
    show player 13
    dia "..."
    show diane f_normal_talk
    dia "You really think I look good?"
    show diane f_normal
    show player 14
    player_name "Of course!"
    player_name "You're beautiful!"
    show player 13
    dia "..."
    hide player
    show diane lingerie_kiss
    with dissolve
    dia "You're so sweet!"
    show player 13 at left
    show diane b_lingerie a_lingerie_sides f_smirk_talk
    with dissolve
    dia "Thank you, handsome!"
    show diane f_smirk
    player_name "..."
    show diane f_smirk_talk
    dia "I should finish getting dressed."
    dia "You wanna go with me to pick up the {b}pesticide{/b}?"
    show diane f_smirk
    player_name "Y-yeah, okay."
    show diane f_laugh
    dia "Great!"
    show diane f_smirk_talk
    dia "You should wait downstairs."
    dia "I'll just be a minute or two."
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 13f at right
    with dissolve
    player_name "( Wow, I can't believe I got to see {b}Diane{/b} like that! )"
    player_name "( She has such a great body! )"
    show diane b_casual a_casual_sides f_smirk_talk at flip with dissolve
    dia "Ready to go, stud?"
    show diane f_smirk
    show player 11f
    player_name "!!!"
    show player 14f
    player_name "Y-yeah..."
    player_name "Nice outfit!"
    show player 13f
    show diane f_laugh
    dia "Heh, thanks!"
    show diane f_normal_talk
    dia "We should be able to find the {b}pesticide{/b} we need at {b}Consum-R{/b}."
    show diane f_normal
    show player 14f
    player_name "Alright, let's go."
    hide player
    hide diane
    with dissolve
    return

label dianes_kitchen_diane_mouse_attack_started:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "Weird. She's not in here either."
    player_name "( I thought for sure... )"
    show player 11
    dia "EEEEEEKKKKKKK!"
    show player 23f
    player_name "What the..."
    player_name "( Is that {b}Diane{/b} screaming?! )"
    hide player with dissolve
    return

label dianes_kitchen_diane_drunken_splur_not_known:
    scene dianekitchen1
    player_name "( There's no one here. )"
    player_name "( {b}Diane{/b} is outside by the garden. )"
    return

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( I can't just leave, {b}Diane{/b} might be in trouble. )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
