label mall_jenny_get_a_mask:
    scene expression "backgrounds/location_mall_day_crowd_blur.jpg" with None
    show player 11 at left with dissolve
    player_name "( What the- )"
    player_name "( There's a crowd of people outside {b}Cosmic Cumics{/b}! )"
    show player 31 with dissolve
    player_name "( Is that {b}Erik{/b}? )"
    hide player with dissolve
    return

label mall_jenny_go_shopping:
    scene expression player.location.background_blur with None
    show player 10 at left
    show jenny b_casual f_upset at flip
    show jenny at Position (xpos=500)
    with dissolve
    player_name "Would you slow down?!"
    show player 5
    pause
    show player 12
    player_name "{b}[jen_name]{/b}!"
    show player 90
    show jenny f_upset_talk
    jen "Don't talk to me."
    show jenny f_upset
    show player 12
    player_name "Ugh, why do you always have a stick up your butt?"
    player_name "Can't you just be chill for for a little while?"
    show player 90
    show jenny f_upset_talk
    jen "No, I can't be chill. Not when I have a loser shadowing my every move."
    show jenny f_upset
    show player 10
    player_name "Nobody is even looking at us, {b}[jen_name]{/b}!"
    show player 5
    show jenny f_eyeroll
    jen "Whatever."
    show jenny f_upset
    pause
    show player 10
    player_name "Where are we going anyways?"
    show player 5
    pause
    show player 12
    player_name "I'm just gonna keep asking, you know?"
    show player 90
    pause
    show player 15
    player_name "{b}[jen_name]{/b}, where are we-"
    show player 11
    hide jenny
    show jenny b_casual f_angry_talk
    with dissolve
    jen "Grr, we're going to {b}Pink{/b} on the second floor, okay?!"
    show jenny f_angry
    show player 10
    player_name "More sex toys?"
    show player 5
    show jenny f_upset_talk
    jen "I swear to god, if you don't shut up, the only place you're going is the hospital."
    jen "To get my foot surgically removed from your ass."
    show jenny f_upset
    show player 401
    player_name "Heh, good one."
    show player 403 with None
    show jenny at flip
    show jenny at Position (xpos=1000)
    with dissolve
    pause
    show player 10
    player_name "I don't know what you're so bent out of shape for anyways..."
    player_name "Like I said, nobody here cares if we're tog-"
    show player 11
    grace "{b}[jen_name]{/b}?!"
    show jenny f_surprised
    pause
    show player 11f at Position (xpos=400)
    hide jenny
    show jenny b_casual f_sad_talk
    show grace at flip
    with dissolve
    jen "{b}Grace{/b}?"
    show jenny f_sad
    show player 13f
    show grace f_normal_talk
    grace "Oh my god, it is you!"
    grace "I haven't seen you since highschool!"
    show grace f_normal
    show jenny f_eyeroll
    jen "Ehh, yeah..."
    show jenny f_upset
    show grace f_normal_talk
    grace "How have you been?"
    show grace f_normal
    show jenny f_upset_talk
    jen "I'm fine."
    show jenny f_upset
    show grace f_normal_talk
    grace "Well, that's good!"
    grace "I'm doing great too."
    grace "I opened up my own tattoo parlor, over on the north side of town."
    grace "{b}Sugartats{/b}."
    grace "You heard of it?"
    show grace f_normal
    show jenny f_upset_talk
    jen "No..."
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, you have to come check it out!"
    grace "We get pretty busy in the evenings but if you came before that we'd have time to chat and catch up."
    show grace f_normal
    show jenny f_upset_talk
    jen "Yeah, no thanks {b}Grace{/b}..."
    show jenny f_upset
    show grace f_normal_talk
    grace "Ah, you're probably busy, huh?"
    grace "What are you doing for work nowadays?"
    show grace f_normal
    if M_jenny.get("dominance") <=0:
        show jenny f_surprised
        jen "I uhh..."
        show player 10f
        player_name "H-hi, I'm {b}[firstname]{/b}."
        show player 5f
        show jenny f_normal
    else:
        show player 17f
        player_name "Heh, yeah {b}[jen_name]{/b}... What are you doing for work?"
        show player 18f
        show jenny f_sad_talk
        jen "I uhh..."
        show jenny f_sad
    show grace f_normal_talk
    grace "Oh, I'm sorry. I didn't know you two were together."
    grace "I'm {b}Grace{/b}."
    show grace f_normal
    show player 14f
    player_name "Nice to meet you."
    show player 13f
    show grace f_laugh
    grace "Wow, {b}[jen_name]{/b}! You're boyfriend is cuuuute!"
    show grace f_normal
    show jenny f_angry
    show player 10f
    player_name "Oh, I'm not-"
    show player 11f
    show jenny f_upset_talk
    jen "Ugh, he is NOT my boyfriend!"
    show jenny f_upset
    show player 10f
    player_name "I'm her roommate."
    show player 5f
    show grace f_normal_talk
    grace "Oh, I see."
    grace "You're still living at home then?"
    show grace f_normal
    show jenny f_eyeroll
    jen "N-not because I have to or anything..."
    show jenny f_upset_talk
    jen "They're just... Having money problems and I'm helping them out, you know?"
    show jenny f_upset
    player_name "..."
    show grace f_normal_talk
    grace "Oh, I can totally relate."
    grace "I took {b}my sister{/b} in a couple years ago after my parents went ballistic on her."
    grace "She's been living with me ever since."
    grace "Family comes first, right?"
    show grace f_normal
    show jenny f_upset_talk
    jen "I didn't know you have a sister?"
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, yeah... She's younger than us."
    show grace f_normal
    show player 14f
    player_name "She's in my class."
    show player 13f
    show jenny f_eyeroll
    jen "Yeah, that's great..."
    show jenny f_upset
    show player 5f
    pause
    show grace f_normal_talk
    grace "Oh, I ran into {b}Cedric{/b} the other day."
    grace "He mentioned you guys had broken up a few months ago."
    show grace f_normal
    show jenny f_upset_talk
    jen "Yeah, I need someone more motivated than boring old {b}Cedric{/b}."
    show jenny f_upset
    show grace f_normal_talk
    grace "Aww, I always thought he was kinda sweet..."
    show jenny f_angry
    grace "... But I imagine you're looking for bigger fish, eh?"
    grace "You always were popular with the guys."
    show grace f_normal
    show jenny f_upset_talk
    jen "You know, {b}Grace{/b}... This has been fun and all but I'm really busy so, if you don't mind?"
    show jenny f_upset
    show grace f_normal_talk
    grace "Oh, right... Sorry."
    grace "I could jabber on all day, hehe."
    show grace f_normal
    pause
    show grace f_normal_talk
    grace "Why don't I give you my card, in case you change your mind-"
    show grace f_normal
    show jenny f_upset_talk
    jen "NO, no... That's okay."
    jen "I won't."
    show grace f_suspicious
    jen "Come on, loser."
    hide jenny with dissolve
    pause
    show player 5 with dissolve
    pause
    show player 10f with dissolve
    player_name "S-sorry about that."
    show player 5f
    show grace f_normal_talk
    grace "It's alright. I wasn't expecting anything different."
    grace "She hasn't changed one bit since high school."
    show grace f_normal
    show player 10f
    player_name "Yeah."
    player_name "I should probably catch up with her."
    show player 5f
    show grace f_laugh
    grace "Hehe, good luck."
    show grace f_normal
    show player 10f
    player_name "Thanks."
    show player 5f
    hide grace with dissolve
    pause
    show player 31 with dissolve
    player_name "( Hmm, now where did {b}[jen_name]{/b} go? )"
    player_name "( She said she was headed towards, {b}Pink{/b}... {b}I should check there{/b}. )"
    hide player with dissolve
    return

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
    player_name "{b}[deb_name]{/b} would hang out with you."
    show player 13
    show diane f_shamed_talk_smile
    dia "Heh, {b}[deb_name]{/b} has her own stuff going on..."
    dia "... I don't wanna bother her."
    show diane f_shamed
    show player 14
    player_name "Oh, please! {b}[deb_name]{/b} has tons of free time."
    show player 10
    player_name "Especially now, with {b}my Dad{/b} gone..."
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
