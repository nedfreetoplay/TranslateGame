label mall_first_visit:
    scene mall
    show player 14 with dissolve
    player_name "( I love the mall! )"
    show player 17
    player_name "( You can go shopping for all sorts of stuff, there's even a movie theater! )"
    hide player 17 with dissolve
    return

label mall_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_day_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Mmm, it's nice to get out of the house for awhile."
    show diane f_normal
    show player 14
    player_name "Yeah, how come you don't go out more?"
    show player 13
    show diane f_normal_talk
    dia "Oh, I don't know."
    dia "There's not much to do in this town by yourself..."
    show diane f_normal
    show player 14
    player_name "{b}Debbie{/b} would hang out with you."
    show player 13
    show diane f_shamed_talk_smile
    dia "Heh, {b}Debbie{/b} has her own stuff going on..."
    dia "... I don't wanna bother her."
    show diane f_shamed
    show player 14
    player_name "Oh, please! {b}Debbie{/b} has tons of free time."
    show player 10
    player_name "Especially now, with {b}my dad{/b} gone..."
    show player 5
    dia "..."
    show diane f_shamed_talk_smile
    dia "You're right, I should make more of an effort."
    dia "We used to be so close when we were younger."
    show diane f_shamed
    show player 10
    player_name "... And if she's busy..."
    show player 17
    player_name "You can always ask me!"
    show player 13
    show diane f_laugh
    dia "Hah, you don't wanna hang out with an old lady like me!"
    show diane f_normal
    show player 14
    player_name "You aren't old {b}Diane{/b}!"
    player_name "Besides, you're one of the most fun people I know!"
    show player 13
    show diane f_normal_talk
    dia "I am?"
    show diane f_normal
    show player 17
    player_name "Yeah!"
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}..."
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "{b}*Ahem*{/b} Well, we should head towards {b}Consum-R{/b} and get that {b}pesticide{/b}."
    show diane f_normal
    show player 14
    player_name "Right behind you."
    hide player
    hide diane
    with dissolve
    return

label mall_mom_mall_outing:
    scene mall
    show player 13 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Thanks again for coming with me, sweetie!"
    show player 14
    show debbie 164
    player_name "No problem, {b}[deb_name]{/b}. I'm having fun!"
    show player 13
    show debbie 166
    deb "Me too!"
    show debbie 164
    deb "..."
    show debbie 165
    deb "Are there any stores you'd like to visit while we're here?"
    show player 14
    show debbie 164
    player_name "Hmm, No, not really."
    show player 13
    show debbie 165
    deb "Alright, well {b}Tammy{/b} was telling me all about this {b}new store{/b} that opened up recently."
    deb "I think she said it was called, {b}Cupid{/b}."
    deb "We should go check it out! What do you say?"
    show player 14
    show debbie 164
    player_name "Sure, {b}[deb_name]{/b}. Okay."
    show player 13
    show debbie 165
    deb "... It should be up on the {b}second floor{/b}."
    show debbie 167 at right with dissolve
    deb "Lead the way, sweetie."
    hide player
    hide debbie
    with dissolve
    return

label mall_roxxy_fake_id_ask_terry:
    scene mall
    show player 13 at left
    show roxxy 2 at right
    with dissolve
    rox "So you have a job, huh?"
    show roxxy 1
    show player 14
    player_name "Yeah."
    show player 13
    show roxxy 1b
    rox "... And you make good money?"
    show roxxy 1
    show player 29 with dissolve
    player_name "I dunno."
    player_name "Good enough, I guess..."
    show player 13 with dissolve
    show roxxy 1l with dissolve
    rox "Hmm..."
    show roxxy 1d
    rox "So if you had a girlfriend... You could like... Buy her clothes and stuff, huh?"
    show roxxy 1e
    show player 12
    player_name "Uhh, yeah. I suppose."
    show player 5
    show roxxy 1h with dissolve
    rox "Interesting..."
    show roxxy 1b
    rox "C'mon, {b}the photo booth{/b} should be on {b}the second floor{/b}!"
    hide roxxy with dissolve
    show player 10
    player_name "O-okay."
    hide player with dissolve
    return

label mom_mall_outing_block:
    scene expression player.location.background_blur
    show player 1
    player_name "Hmm, I'm supposed to be looking for a store called, {b}Cupid.{/b}"
    show player 4
    player_name "{b}[deb_name]{/b} said it should be on the {b}second floor{/b}."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
