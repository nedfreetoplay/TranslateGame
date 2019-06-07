label jenny_bedroom_cannot_snoop:
    if game.timer.is_evening():
        scene expression "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
    elif game.timer.is_dark():
        scene expression "backgrounds/location_home_jennybedroom_night_blur.jpg"
    else:
        scene expression "backgrounds/location_home_jennybedroom_jenny_day_blur.jpg"
    show player 5 with dissolve
    player_name "( I can't snoop around with {b}[jen_name]{/b} here! )"
    show player 4
    player_name "( I should come back when she is not around anymore. )"
    hide player
    return

label sis_bedroom_jenny_pregnancy_announcement_repeat:
    scene expression player.location.background_closeup
    show jenny f_upset a_dressed_crossed
    show player f_worried_talk with dissolve
    player_name "You wanted to see me?"
    show player f_worried
    show jenny f_upset_talk
    jen "Yeah."
    jen "Congratulations, dummy... I'm pregnant again."
    show jenny f_angry_pouting
    show player f_shock
    player_name "What, again?!"
    show player f_worried
    show jenny f_angry_talk
    jen "I told you not to cum inside me!"
    show jenny f_angry
    show player f_tired_talk
    player_name "{b}*Sigh*{/b}"
    show player f_worried_talk
    player_name "Does this mean you're gonna get all bitchy again?"
    show player f_worried
    show jenny f_angry_talk
    jen "EXCUSE ME?!"
    show jenny f_angry
    show player f_shock
    player_name "Wha-"
    show player f_worried_talk
    player_name "I didn't mean-"
    show player f_surprised_teeth
    pause
    show player f_shock
    player_name "Please, don't get the hair dryer..."
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Just get out!"
    show jenny f_angry
    show player f_worried_talk
    player_name "Well, hold on."
    player_name "I know this isn't an ideal situation but I'm here for you, you know?"
    show player f_worried
    show jenny f_eyeroll
    jen "Ugh, seriously get out!"
    show jenny f_angry
    show player f_worried_talk
    player_name "O-okay..."
    show player f_worried
    hide jenny with dissolve
    pause
    player_name "( Well, I tried... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_pregnancy_announcement_first:
    scene expression player.location.background_closeup
    show player f_worried_talk with dissolve
    player_name "Hey, I came as soon as I-"
    show jenny f_angry_talk a_dressed_hit2 with dissolve
    show player 6 at left
    jen "You fucking asshole!"
    show jenny a_dressed_hit with dissolve
    player_name "What the-"
    show jenny a_dressed_hit2 with dissolve
    jen "I knew this was going happen!"
    show jenny a_dressed_hit with dissolve
    player_name "Why are you-"
    show jenny a_dressed_hit2 with dissolve
    jen "YOU STUPID, IDIOT, MOTHER-"
    show jenny a_dressed_hit with dissolve
    player_name "Stop hitting me!"
    show jenny f_angry a_dressed_upset with dissolve
    jen "Grrr!!!"
    show player f_skeptical_talk with dissolve
    player_name "Sheesh, what's gotten into you?!"
    show player f_skeptical
    show jenny f_angry_talk
    jen "Your potato headed spawn, that's what!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Huh?"
    show player f_skeptical
    show jenny f_angry_talk a_dressed_crossed with dissolve
    jen "I'm pregnant, you moron!"
    show jenny f_angry
    show player f_shock
    player_name "!!!"
    player_name "Y-you're pregnant?!"
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Yes, dummy!"
    jen "You kept cumming inside me, what did you think was going to happen?!"
    show jenny f_angry
    show player f_skeptical_talk
    player_name "Hey, that's not fair!"
    player_name "This is just as much your fault as it is mine..."
    show player f_skeptical
    show jenny f_eyeroll
    jen "Pfft, whatever."
    show jenny f_angry_pouting_top
    pause
    show player f_worried_talk
    player_name "S-so, what are you going to tell {b}[deb_name]{/b}?"
    show player f_worried
    show jenny f_eyeroll
    jen "Ugh, I don't know..."
    show jenny f_angry_pouting_top
    show player f_worried_talk
    player_name "She's going to figure it out eventually."
    show player f_worried
    show jenny f_upset_talk
    jen "Yeah but not for a while, I'll think of something..."
    show jenny f_upset
    pause
    show player f_laugh
    player_name "I'm going to be a father..."
    show player f_grin
    show jenny f_eyeroll
    jen "Yeah, I feel sorry for the kid already."
    show jenny f_angry_pouting_top
    show player f_normal_talk
    player_name "... and {b}[jen_name]{/b}, you're going to be a mother!"
    show player f_normal
    pause
    show player f_worried_talk
    player_name "You're not even a little bit excited?"
    show player f_worried
    show jenny f_sad
    pause
    show jenny f_sad_talk
    jen "N-no, I-"
    show jenny f_angry
    pause
    show jenny f_angry_talk a_dressed_upset with dissolve
    jen "Grr, I can't believe you're excited about this!"
    show jenny f_angry
    player_name "..."
    show jenny f_angry_talk
    jen "You're always a pain in my ass, you know that?!"
    show jenny f_angry a_dressed_crossed with dissolve
    show player f_worried_talk
    player_name "I'm sorry?"
    show player f_worried
    show jenny f_eyeroll
    jen "Just, ugh... Forget it."
    show jenny f_upset_talk
    jen "Get out."
    show jenny f_upset
    show player f_worried_talk
    player_name "What?!"
    show player f_worried
    show jenny f_angry_talk
    jen "Get the fuck out of my room, {b}[firstname]{/b}!"
    hide jenny with dissolve
    show player f_worried_talk
    player_name "O-okay..."
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup
    show player f_worried
    with fade
    player_name "( I'm not sure she knows how to feel right now... )"
    player_name "( ... And what will {b}[deb_name]{/b} do when she finds out?! )"
    show player f_surprised_teeth
    pause
    player_name "( Oh man, things are about to get a lot more complicated around here... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_cheerleader_sex:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_closeup with None
    show player f_worried_talk
    show jenny f_upset
    with dissolve
    player_name "Alright, I got your uniform down from the attic."
    show player f_worried
    show jenny f_gross_down_talk
    jen "Is it all dusty?"
    show jenny f_gross
    show player f_worried_talk
    player_name "No, it looks fine to-"
    show player f_worried_talk
    show jenny f_upset_talk
    jen "Give it here!"
    show jenny f_upset_down a_dressed_hips_cheer with dissolve
    pause
    show jenny f_upset_down_talk
    jen "Hmm, it'll have to do."
    show jenny f_upset_down
    player_name "..."
    show jenny f_upset_talk
    jen "Why are you still wearing clothes?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Uhh..."
    show player f_worried
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show player f_surprised
    pause
    show jenny b_panties a_naked_hips f_upset with dissolve
    show jenny f_upset_talk
    jen "Hurry up, my fans are waiting..."
    show jenny b_naked f_grin_down a_naked_panties_remove with dissolve
    show player f_worried_talk
    player_name "R-right..."
    show player f_worried
    show jenny b_cheer_dress1 f_empty a_empty
    show player b_dressed_changing a_empty f_empty
    with dissolve
    pause
    show player b_dressed_changing2 a_empty f_empty with dissolve
    pause
    show player b_underwear a_naked_sides f_worried_talk with dissolve
    player_name "What are we doing today?"
    show player f_worried
    show jenny b_cheer_dress3 f_grin_talk with dissolve
    jen "Something special."
    show jenny b_cheer_dress2 f_empty with dissolve
    pause
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Well, what do you think?"
    show jenny f_sexy
    show player f_worried_talk
    player_name "It's a bit small..."
    show player f_worried
    show jenny f_laugh
    jen "Haha, more than a bit!"
    show jenny b_cheer_showoff a_empty f_sexy_talk with dissolve
    jen "It's sexy though, right?"
    show jenny b_cheer_side f_overshoulder_back_look_normal at Position (align=(0,0)) with dissolve
    show player f_laugh
    player_name "Y-yeah!"
    show player f_normal
    show jenny b_cheer a_cheer_hips f_sexy_talk with dissolve
    jen "Haha, good!"
    jen "Get on the bed."
    show jenny f_sexy
    hide player with dissolve
    pause
    show jenny f_sexy_talk
    jen "... And put your mask on!"
    show jenny f_sexy
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_down at Position (align=(0,0))
    with dissolve
    pause
    show jenny f_bed_facing_comp_laugh
    jen "Hehe, see!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "I told you guys I used to be head cheerleader."
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Oh, really?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "So you always wanted to fuck a cheerleader, huh?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "How about the rest of you boys?!"
    jen "You wanna see me get fucked?"
    show jenny f_bed_facing_comp_sexy_down
    show player f_jenny_bed_sit_surprised
    player_name "( !!! )"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "You can do better than that..."
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_laugh
    jen "Hehehe!"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Alright, let me get things ready..."
    show jenny b_bed_climbing a_empty f_empty o_cheer_bed_climbing
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label sis_bedroom_jenny_get_cheerleader_outfit:
    show player f_worried
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "What are you doing?!"
    show jenny f_upset
    show player f_worried_talk
    player_name "You told me to meet you here this afternoon."
    show player f_worried
    show jenny f_upset_talk
    jen "Yeah, {b}with my cheerleading uniform{/b}!"
    show jenny f_upset
    show player f_worried_talk
    player_name "Oh, right."
    show player f_worried
    show jenny f_upset_talk
    jen "Hurry up and go {b}get it from the attic{/b}!"
    hide jenny with dissolve
    jen "Idiot..."
    hide player with dissolve
    return

label sis_bedroom_jenny_start_camshow_blowjob:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        scene expression player.location.background_blur with None
    show player f_worried
    with dissolve
    jen "There he is!"
    show jenny b_naked a_naked_hips f_upset_talk with dissolve
    jen "Let's go!"
    show jenny f_upset
    show player f_worried_talk
    player_name "You're naked..."
    show player f_worried
    show jenny f_upset_talk
    jen "No shit?"
    jen "Everyone is waiting on you, dummy!"
    show jenny f_upset
    show player f_worried_talk
    player_name "I wasn't-"
    show player f_worried
    show jenny f_upset_talk
    jen "C'mon, get your clothes off!"
    show jenny f_upset
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg" with dissolve
    jen "Put your mask on!"
    player_name "I know."
    jen "Well, hurry up!"
    player_name "Stop pulling me!"
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show player b_bed_jenny_sit a_empty f_jenny_bed_sit_shy_down of_jenny_bed_sit_mask at Position (align=(0,0))
    show jenny o_under_body_laptop b_naked_bed_bellytype a_empty f_bed_facing_comp_sexy_talk_down at Position (align=(0,0))
    with dissolve
    jen "That's right, we're doing a special show today..."
    show jenny b_naked_bed_belly f_bed_facing_comp_sexy_down with dissolve
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "You'll just have to wait and find out, won't you?"
    show jenny f_bed_facing_comp_sexy_down
    pause
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Oh, you wanna see his big dick, huh?"
    jen "Well, I wanna see more tips!"
    show jenny f_bed_facing_comp_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_facing_comp_sexy_talk_down
    jen "Hehe, there we go!"
    jen "Give me a second to get everything set up..."
    show jenny o_laptop b_bed_climbing a_empty f_empty
    show player b_bed_jenny_laying_undies_arms f_empty a_empty of_bed_jenny_laying_undies_arms_mask od_bed_jenny_laying_dick1
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    player_name "W-what are you-"
    show jenny b_bed_back_sit a_bed_back_sit_handcuffs with dissolve
    jen "..."
    player_name "H-hey, I didn't agree to handcuffs!"
    show jenny a_bed_back_sit_tie
    show player oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jen "Shut up!"
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    if M_jenny.get("dominance") <= 0:
        jen "You're only here to do what I tell you, remember?!"
        player_name "Y-yeah..."
        jen "I think you mean, \"Yes, {b}Princess [jen_name]{/b}.\""
        player_name "Yes, {b}Princess [jen_name]{/b}..."
        show jenny a_bed_back_sit_hips with dissolve
        jen "Hahahaah!"
    else:
        player_name "This isn't funny, {b}[jen_name]{/b}!"
        player_name "Get these off me!"
        jen "Oh, just relax for a second."
        show jenny a_bed_back_sit_hips with dissolve
        jen "You're going to like this, I promise."
        player_name "..."
    show jenny b_bed_back_look a_bed_back_look_up f_bed_back_look_normal with dissolve
    pause
    show jenny a_bed_back_look_butt f_bed_back_look_normal_talk with dissolve
    jen "Now, let's give the big fella some air, shall we?"
    show jenny b_bed_front_sit a_bed_front_sit_sides f_bed_front_sit_sexy_down with dissolve
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_bed_front_sit_pull1
    with dissolve
    pause
    show jenny a_bed_front_sit_pull2 f_bed_front_sit_sexy_talk_down with dissolve
    jen "Hehe, looks like he's ready to give you guys a good show."
    show player od_bed_jenny_laying_dick6
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_bed_front_sit_sides f_bed_front_sit_sexy_down
    with dissolve
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_sit_sexy_talk_down
    jen "Today's not going to be about him though..."
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_sexy_down
    with dissolve
    pause
    show jenny f_bed_front_laying_sexy_talk_down
    jen "Hehe, that's right."
    jen "Today, my little boy toy is going to learn about eating pussy."
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    player_name "What?!"
    player_name "This wasn't-"
    show jenny b_bed_pussy1 f_bed_pussy1_sexy_down
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "!!!"
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_sexy_talk_down
    jen "What was that, boy toy?"
    jen "We can't hear you..."
    show jenny f_bed_pussy1_laugh
    jen "Hahahaah!"
    show player od_empty
    show jenny b_bed_pussy f_bed_pussy_sexy_talk_down
    with dissolve
    jen "C'mon, stop fighting and stick your tongue out!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "{b}*Gasp*{/b} Oh, yeah!"
    jen "There we go!"
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_nipple2
    jen "Mmm, fuuuuck..."
    show jenny f_bed_pussy_sexy_down
    pause
    show jenny f_bed_pussy_sexy_talk_down
    jen "He's pretty good at this you guys!"
    show jenny f_bed_pussy_nipple2
    jen "Ahh!"
    show jenny f_bed_pussy_nipple3
    pause
    show jenny f_bed_pussy_nipple2
    jen "Ngghhh, right there!"
    show jenny f_bed_pussy_nipple3
    jen "{b}*Whimper*{/b}"
    pause
    show jenny f_bed_pussy_nipple2
    jen "Oh, shit!"
    jen "OHHH, SHIT!"
    jen "I'm gonna-"
    show jenny f_bed_pussy_nipple3
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    pause
    show jenny b_bed_pussy1 f_bed_pussy1_nipple2
    jen "NGGHHH!!!" with flash
    pause
    hide expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying a_empty f_bed_front_laying_nipple2
    show player od_bed_jenny_laying_dick6
    with dissolve
    jen "Haah... Haaah..."
    player_name "{b}*Gasp*{/b}"
    player_name "{b}*Cough* *Sputter* *Cough*{/b}"
    player_name "I thought you were gonna drown me!"
    show jenny f_bed_front_laying_laugh
    jen "Hehehe!"
    show jenny f_bed_front_laying_sexy_talk_down
    jen "So boys, how was the show?"
    jen "Pretty good, huh?"
    show jenny f_bed_front_laying_sexy_down
    pause
    jen "Hmm?"
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Eww, fuck no!"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "No way! I don't do that!"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Umm, because it's gross?"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_laugh
    jen "Heh, yea right..."
    show jenny f_bed_front_laying_sexy_talk_down
    jen "You guys would have to tip me a ton of money before I'd ever consider-"
    show jenny f_bed_front_laying_sexy_down
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    show jenny f_bed_front_laying_surprised_down_talk
    "{b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b} {b}*PING*{/b}"
    jen "Aww, c'mon you guys..."
    show jenny f_bed_front_laying_gross_down
    player_name "What's going on?"
    show jenny f_bed_front_laying_gross_down_talk
    jen "{b}*Sigh*{/b} They want me to suck your dick..."
    show jenny f_bed_front_laying_gross_down
    player_name "!!!"
    show jenny f_bed_front_laying_gross_down_talk
    jen "Isn't there something else I can do?"
    show jenny f_bed_front_laying_gross_down
    pause
    show jenny f_bed_front_laying_gross_down_talk
    jen "Ugh, fine..."
    jen "... But don't expect this to become a regular thing!"
    show jenny f_bed_front_laying_gross_down
    player_name "{b}*Gulp*{/b} A-are you really going to-"
    show jenny b_bed_pussy1 f_bed_pussy1_upset
    show expression "characters/player/layeredimage/player_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    player_name "!!!"
    show jenny f_bed_pussy1_upset_talk
    jen "Shut up!"
    show jenny f_bed_pussy1_upset
    player_name "Mrphmmmll-"
    show jenny f_bed_pussy1_eyeroll
    jen "{b}*Sigh*{/b} I can't believe I'm doing this..."
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    player_name "Nnnrrrmmph-" with hpunch
    jen "{b}*Gluullggh*{/b}"
    jump jenny_bj_loop

label sis_bedroom_jenny_get_a_mask_quest:
    scene expression player.location.background_closeup with None
    show jenny f_angry_talk
    show player 5 at left
    with dissolve
    jen "It's about time!"
    show jenny f_angry
    show player 10
    player_name "Huh?"
    show player 5
    show jenny f_angry_talk
    jen "I've been waiting forever!"
    show jenny f_angry
    show player 10
    player_name "I came right-"
    show player 11
    show jenny f_angry_talk
    jen "Shut up!"
    show jenny f_angry
    show player 5
    player_name "..."
    show jenny f_upset_talk
    jen "Ugh, this is such a bad idea..."
    show jenny f_upset
    if M_jenny.get("dominance") <= 0:
        show player 12
        player_name "Are you going to tell me-"
        show player 5
        show jenny f_upset_talk
        jen "Didn't I tell you to shut up?!"
        show jenny f_upset
        show player 10
        player_name "Yes?"
        show player 5
        show jenny f_upset_talk
        jen "So why are you still talking?!!"
        show jenny f_upset
        show player 10
        player_name "I'm sorry, I-"
        show player 11
        show jenny f_upset_talk
        jen "Don't be sorry, be quiet!"
        show jenny f_upset
        show player 5
        player_name "..."
        jen "..."
        show jenny f_eyeroll
        jen "Finally!"
        show jenny f_upset_talk
        jen "{b}*Sigh*{/b} Alright, here's the deal."
        jen "As I'm sure you've figured it out by now, I've been doing camshows for money recently..."
        jen "I know it's not the most glamorous profession but it's bringing in buttloads of money."
        show jenny f_upset
        show player 10
        player_name "You realize {b}[deb_name]{/b} is going to kill you, right?"
        show player 5
        show jenny f_upset_talk
        jen "{b}[deb_name]{/b} isn't going to find out!"
        show jenny f_upset
        player_name "..."
        show jenny f_angry_talk
        jen "I swear to god, I'll kill you if you say one peep to her!"
        show jenny f_angry
        show player 10
        player_name "{b}*Gulp*{/b} I wouldn't-"
        player_name "I mean, I'm not going to tell her!"
        show player 5
        show jenny f_angry_talk
        jen "Damn right you're not!"
        show jenny f_upset
        pause
        show jenny f_upset_talk
        jen "In fact, you're going to help me."
        show jenny f_upset
        show player 11
        player_name "Hmm?"
        show jenny f_upset_talk
        jen "You see, my fans are tired of watching me with just toys."
        jen "They wanna see me with a real guy and since I can't find one of those..."
        show jenny f_eyeroll a_dressed_crossed with dissolve
        jen "You'll have to do."
        show jenny f_upset
        show player 12c with dissolve
        player_name "M-me?!"
        show player 5 with dissolve
        show jenny f_upset_talk
        jen "Yes, you."
        show jenny f_upset
        show player 10
        player_name "Are you talking, like... S-sex?"
        show player 5
        show jenny f_gross
        jen "Sex?! Eww, no!"
        show jenny f_angry_talk
        jen "What the hell is your problem?!"
        show jenny f_gross
        show player 10
        player_name "B-but-"
        show player 5
        show jenny f_angry_talk
        jen "As if I would ever have sex with you, gross!"
        show jenny f_gross
        show player 12
        player_name "Okay, I'm confused."
        show player 5
        show jenny f_eyeroll
        jen "You're an idiot."
        show jenny f_gross
        show player 10
        player_name "What do you want me to do?"
        show player 5
        show jenny f_upset_talk
        jen "I want you to sit on the bed and keep your mouth shut."
        jen "Do you think you can manage that?!"
        show jenny f_upset
        show player 10
        player_name "Y-yes."
        show player 5 at Position (xoffset=50) with dissolve
        show jenny f_upset_talk
        jen "Not right now, moron!"
        show jenny f_upset
        show player 10 with dissolve
        player_name "B-but you just said-"
        show player 5
        show jenny f_upset_talk
        jen "We're not going to stream right this second!"
        jen "Besides, we need a couple things first."
        show jenny f_upset
        show player 10
        player_name "Like what?"
        show player 5
        show jenny f_upset_talk
        jen "You need a mask or something."
        show jenny f_upset
        show player 10
        player_name "A mask?"
        show player 5
        show jenny f_upset_talk
        jen "Yeah, to cover your face."
        show jenny f_upset
        show player 10
        player_name "W-why?"
        show player 5
        show jenny f_angry_talk
        jen "Umm, because I don't want anyone to know it's you, dummy!"
        show jenny f_upset_talk
        jen "Do you have any idea what people would say if they saw me doing stuff with you?!"
        show jenny f_eyeroll
        jen "Ugh, I don't even wanna think about it."
        show jenny f_gross
        show player 10
        player_name "Oh."
        show player 5
        show jenny f_upset_talk a_dressed_hips with dissolve
        jen "So just run over to {b}the mall{/b} and pick up a ski-mask or something..."
        show jenny f_upset
        show player 10
        player_name "What if they don't have any ski-masks?"
        show player 5
        show jenny f_upset_talk
        jen "Then figure something out, loser!"
        show jenny f_upset
        show player 24
        player_name "{b}*Sigh*{/b} Fine."
        show player 10
        player_name "Anything else?"
        show player 5
        show jenny f_upset_talk
        jen "No, I'll get the other stuff."
        jen "Just {b}don't come back here without a mask{/b}, got it?!"
        show jenny f_upset
        show player 10
        player_name "Yeah, I got it."
        show player 5
        show jenny f_upset_talk
        jen "Good."
        jen "Now scram!"
        hide jenny with dissolve
        pause
        show player 24
        player_name "{b}*Sigh*{/b}"
        show player 37 with dissolve
        player_name "( Alright, I should head to {b}the mall{/b} and look for {b}a mask{/b}. )"
        hide player with dissolve
    else:
        show player 12
        player_name "Would you tell me what's going on already?!"
        show player 5
        show jenny f_upset_talk
        jen "Don't you raise your voice with me!"
        jen "You're lucky I'm even consider-"
        show jenny f_upset
        show player 12
        player_name "Okay, I'm outta here."
        show player 5f with dissolve
        show jenny f_upset_talk
        jen "No, wait!!"
        show player 5 with dissolve
        jen "God damnit..."
        show jenny f_eyeroll
        jen "{b}*Sigh*{/b} I need your help, okay?"
        show jenny f_gross
        show player 12
        player_name "If you're gonna act like a bitch, then you can forget my help."
        show player 5
        show jenny f_upset_talk
        jen "Grr, fine!"
        show jenny f_eyeroll
        jen "I'll... Ugh, I'll be nice."
        show jenny f_gross
        show player 10
        player_name "Yeah, right."
        show player 5
        show jenny f_upset_talk
        jen "Would you-"
        show jenny f_angry_pouting_top
        pause
        show jenny f_upset_talk
        jen "Can I at least explain the situation?"
        show jenny f_upset
        show player 10
        player_name "Okay, let's hear it."
        show player 5
        show jenny f_eyeroll
        jen "{b}*Sigh*{/b} As I'm sure you have figured it out by now, I've been doing camshows for money recently."
        show jenny f_upset
        show player 14
        player_name "Heh, yeah... It wasn't exactly hard to piece together, {b}[jen_name]{/b}."
        show player 13
        show jenny f_angry_talk
        jen "Don't laugh, it's good money!"
        show jenny f_angry
        show player 17
        player_name "Heh, okay but you realize {b}[deb_name]{/b} is going to kill you, right?"
        show player 13
        show jenny f_angry_talk
        jen "You didn't tell her, did you?"
        show jenny f_angry
        show player 14
        player_name "No, I didn't tell her."
        show player 13
        pause
        show jenny f_eyeroll
        jen "Phew, that's good!"
        show jenny f_upset_talk
        jen "What {b}[deb_name]{/b} doesn't know, won't hurt her."
        show jenny f_upset
        show player 14
        player_name "So what do you want my help with?"
        show player 13
        show jenny f_sad_talk
        jen "Well, it's..."
        jen "Y-you see..."
        show jenny f_sad
        show player 11
        player_name "..."
        show player 14
        player_name "Just spit it out."
        show player 13
        show jenny f_sad_talk
        jen "My fans are... Well, they're tired of watching me with toys and..."
        show jenny f_sad
        pause
        show player 14
        player_name "And?"
        show player 13
        show jenny f_sad_talk
        jen "... And they're offering to pay me a boatload of money, if I can find a man to stream with."
        show jenny f_sad
        show player 22
        player_name "!!!"
        show player 10
        player_name "You can't be serious..."
        show player 5
        show jenny f_upset_talk a_dressed_crossed with dissolve
        jen "Why not?"
        jen "Stupid {b}Cedric{/b} won't do it, plus you and I have already... Done stuff."
        show jenny f_upset
        show player 10
        player_name "Not on camera we haven't!"
        show player 5
        show jenny f_upset_talk
        jen "Don't be a pussy."
        show jenny f_upset
        show player 10
        player_name "What if they figure out who we are?!"
        show player 5
        show jenny f_upset_talk
        jen "They won't."
        show jenny f_grin_talk
        jen "You're gonna wear a mask."
        show jenny f_grin
        show player 12
        player_name "Huh?"
        show player 5
        show jenny f_upset_talk
        jen "Yeah, we just need to get you a ski mask or something."
        show jenny f_upset
        show player 10
        player_name "It's the middle of summer..."
        player_name "Where are we gonna find a ski mask?!"
        show player 5
        show jenny f_upset_talk
        jen "It doesn't have to be a ski mask, just-"
        show jenny a_dressed_facepalm with dissolve
        jen "{b}*Sigh*{/b} Just {b}go to the mall{/b} and find {b}a mask{/b}!"
        jen "Any {b}mask{/b} will do."
        show jenny f_upset a_dressed_hips with dissolve
        show player 12
        player_name "Am I going to get paid for this?"
        show player 5
        jen "..."
        show jenny f_upset_talk
        jen "You get to touch me, that's payment enough."
        show jenny f_upset
        show player 12
        player_name "No, I want a cut."
        show player 5
        show jenny f_angry
        jen "..."
        show player 12
        player_name "You won't get that money without me..."
        show player 5
        show jenny f_angry_talk
        jen "Oh my god, FINE!"
        jen "Fucking pain in my ass..."
        show jenny f_angry
        show player 14
        player_name "Good."
        show player 13
        show jenny f_angry_talk
        jen "Just get out!"
        hide jenny with dissolve
        jen "And don't come back without {b}a mask{/b}!"
        show player 4 with dissolve
        player_name "( Hmm, I wonder what she's planning to do for the stream? )"
        pause
        player_name "( I'll have to {b}get a mask{/b} if I wanna find out... )"
        player_name "( I should {b}head to the mall and look around for one{/b}. )"
        hide player with dissolve
    return

label jenny_bedroom_jenny_deliver_bad_monster:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    show jenny b_bed_reading a_bed_phone1 f_bed_lay_way_back_laugh at Position (yoffset=62) with dissolve
    jen "Can you believe that?!"
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Yeah, I told him how much money it was bringing in but he's being a little bitch about it!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "No, he won't do it."
    show jenny f_bed_lay_way_back_laugh at Position (yoffset=62)
    jen "Haha! Yeah, I know!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "I dunno, I'll find someone eventually..."
    show player 13 at left with dissolve
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    jen "!!!"
    show jenny f_bed_lay_way_back_upset_talk a_bed_phone2 at Position (yoffset=62) with dissolve
    jen "I'm on the phone!"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    show player 14
    player_name "I got you something."
    show player 13
    show jenny f_bed_lay_way_back_surprised at Position (yoffset=62)
    jen "Huh?"
    show jenny f_bed_lay_way_back_angry at Position (yoffset=62)
    show player 14
    player_name "A present."
    show player 13
    show jenny f_bed_lay_way_back_upset_talk at Position (yoffset=62)
    jen "You bought me something?"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    show player 14
    player_name "Yes."
    show player 13
    show jenny f_bed_lay_way_back_upset_talk at Position (yoffset=62)
    jen "Was it expensive?"
    show jenny f_bed_lay_way_back_upset at Position (yoffset=62)
    player_name "..."
    show player 14
    player_name "Yes."
    show player 13
    show jenny f_bed_lay_way_back_happy_talk a_bed_phone1 at Position (yoffset=62) with dissolve
    jen "{b}Jane{/b}, I'm gonna have to call you back."
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "Haha, yeah... I'm sure they would love that."
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_happy_talk at Position (yoffset=62)
    jen "I'll keep that in mind..."
    jen "You're such a slut!"
    show jenny f_bed_lay_way_back_happy at Position (yoffset=62)
    pause
    show jenny f_bed_lay_way_back_laugh at Position (yoffset=62)
    jen "Haha, bye!"
    show jenny f_bed_upset b_bed_dressed a_bed_dressed_down with dissolve
    pause
    show jenny f_bed_upset_talk
    jen "Okay, this had better be good."
    show jenny f_bed_upset
    show player 239_240 with dissolve
    pause
    show player 286g
    show jenny f_bed_surprised
    jen "!!!" with hpunch
    jen "I-is that a {b}Bad Monster{/b}?!"
    show player 286
    player_name "Yup."
    show player 286g
    jen "How did you-"
    show jenny f_bed_upset_talk
    jen "Why did you buy this for me?!"
    show jenny f_bed_upset
    show player 286
    player_name "Well, you-"
    show player 286e
    show jenny f_bed_angry_talk
    jen "Did you read my diary?!"
    show jenny f_bed_angry
    show player 286d
    player_name "W-what?"
    player_name "No!"
    player_name "You just had me buying sex toys for you and I heard this was the best one and..."
    show player 286e
    pause
    show player 286d
    player_name "I didn't read your diary! Sheesh!"
    show player 286e
    show jenny f_bed_angry_talk
    jen "You better not have!"
    jen "Give me that!"
    show jenny f_bed_grin_down a_bed_dressed_hips_toy4b
    show player 5
    with dissolve
    pause
    show jenny f_bed_grin_down_talk
    jen "It's awesome..."
    show player 13
    jen "They're gonna go nuts for this!"
    show jenny f_bed_grin_down
    show player 14
    player_name "Who's gonna-"
    show player 13
    show jenny f_bed_upset
    jen "Hmm?"
    show jenny f_bed_upset_talk
    jen "Oh, uhh... Nobody!"
    jen "Just, shut up and get out!"
    show jenny f_bed_upset
    show player 10
    player_name "You're not even gonna say thank you?"
    show player 90
    if M_jenny.get("dominance") <= 0:
        show jenny f_bed_eyeroll
        jen "Uhh, no?"
        show jenny f_bed_upset_talk
        jen "I know there's probably some creepy motive behind this..."
        show jenny f_bed_upset
        show player 29 with dissolve
        player_name "No there's not!"
        player_name "Can't I just do something nice for you?"
        show player 3
        show jenny f_bed_upset_talk
        jen "Yeah right, whatever."
    else:
        show jenny f_bed_eyeroll
        jen "Ugh, thank you."
        show jenny f_bed_upset
        show player 29
        player_name "You're welcome."
        show player 3
    show jenny f_bed_angry_talk
    jen "Now get out!"
    show jenny f_bed_angry
    show player 24 with dissolve
    player_name "{b}*Sigh*{/b} Fine."
    hide player with dissolve
    pause
    show jenny f_bed_grin_down_talk
    jen "Hehehehehe!"
    scene black with fade
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 90 with dissolve
    player_name "( Typical bitchy result... )"
    pause
    show player 403
    player_name "( Oh well, maybe she'll make another video for her {b}CAMslut profile{/b}! )"
    player_name "( I'll just have to wait and {b}check it in the morning.{/b} )"
    hide player with dissolve
    return

label upstairs_bedroom_jenny_figure_out_password:
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( Alright, I've gotta be quiet here... )"
    player_name "( I just need to {b}log into her laptop{/b} and find her {b}CAMslut{/b} stuff. )"
    show player 403
    player_name "( Easy peasy... )"
    hide player with dissolve
    return

label sis_bedroom_jenny_get_a_toy:
    scene expression player.location.background_blur with None
    show player 10 at left
    show jenny
    with dissolve
    player_name "Alright, I'm here."
    player_name "What do you want?"
    show player 5
    show jenny a_dressed_hips f_normal_talk with dissolve
    jen "I found another way to make money."
    jen "WAY better than that stupid {b}Sluttygram{/b} site."
    show jenny f_normal
    show player 10
    player_name "Okay."
    player_name "What is it?"
    show player 5
    show jenny f_normal_talk
    jen "None of your business, loser."
    show jenny f_normal
    player_name "..."
    return

label sis_bedroom_jenny_get_a_toy_submissive:
    show player 10
    player_name "{b}*Sigh*{/b} C'mon, {b}[jen_name]{/b}..."
    show player 5
    show jenny f_upset_talk
    jen "Would you just shut up and listen!"
    show jenny f_upset
    player_name "..."
    show jenny f_normal_talk
    jen "I need you to go to the mall and buy something for me."
    show jenny f_normal
    show player 12
    player_name "Why does it always come down to money with you?"
    show player 5
    show jenny f_normal_talk
    jen "Umm, because you have nothing else to offer me?"
    jen "It's not that big a deal, it's only one-hundred dollars..."
    show jenny f_normal
    show player 11
    pause
    show player 10
    player_name "Another one-hundred?!"
    player_name "I dunno, that's a lot of money!"
    show player 11
    show jenny f_upset_talk
    jen "If you buy me this, I'll take everything off for you."
    show jenny f_upset
    show player 12
    player_name "You'll get completely naked?"
    show player 11
    show jenny f_upset_talk
    jen "For two minutes..."
    show jenny f_angry_talk
    jen "But no touching!"
    show jenny f_upset
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Alright, fine."
    player_name "I guess that's worth one-hundred."
    show player 5
    show jenny f_eyeroll
    jen "It's worth a lot more than one-hundred!"
    show jenny f_upset_talk
    jen "You're lucky I'm feeling generous..."
    show jenny f_upset
    return

label sis_bedroom_jenny_get_a_toy_end:
    show player 10
    player_name "So what am I buying?"
    show player 5
    show jenny f_normal_talk
    jen "I need you to go to {b}the mall{/b} and look on {b}the second floor{/b} for a store called {b}Pink{/b}."
    show jenny f_normal
    show player 10
    player_name "{b}Pink{/b}, huh?"
    player_name "Okay..."
    show player 5
    show jenny f_normal_talk
    jen "The toy I want is called, {b}The Electro Clit.{/b}"
    show jenny f_normal
    show player 10
    player_name "Toy?"
    player_name "Aren't you a little old for toys?"
    show player 5
    show jenny f_upset_talk
    jen "It's a sex shop, dummy..."
    show jenny f_upset
    show player 23
    player_name "!!!" with hpunch
    show player 12c with dissolve
    player_name "You expect me to go into a sex shop?!"
    show player 12 with dissolve
    player_name "No freaking way!"
    show player 5
    show jenny f_grin_talk
    jen "Aww, is the little virgin afraid of a big scary sex shop?"
    show jenny f_grin
    show player 10
    player_name "W-what, no..."
    player_name "I just... Why can't you go?!"
    player_name "I'll give you the money and you can-"
    show player 5
    show jenny f_eyeroll
    jen "I have other stuff I need to do!"
    show jenny f_upset_talk
    jen "Just man up and go, doofus."
    show jenny f_upset
    show player 10
    player_name "F-fine."
    show player 5
    show jenny f_eyeroll
    pause
    hide jenny with dissolve
    pause
    player_name "( I can't believe she's making me do this... )"
    show player 37 with dissolve
    player_name "( Ugh, let's just get it over with. )"
    hide player with dissolve
    return

label sis_bedroom_jenny_get_a_toy_dominant:
    show player 10
    player_name "Okay, see ya."
    show player 5f with dissolve
    pause
    show jenny f_sad_talk a_dressed_upset with dissolve
    jen "No, wait!"
    show jenny f_sad
    show player 5 with dissolve
    show jenny f_angry_pouting a_dressed_crossed
    pause
    show jenny f_upset_talk
    jen "I don't want to say, it's embarrassing..."
    show jenny f_upset
    show player 12
    player_name "Really?"
    player_name "I don't think I've ever seen you embarrassed about anything before."
    show player 5
    show jenny f_upset_talk
    jen "Can you just help me, please?"
    show jenny f_upset
    show player 10
    player_name "{b}*Sigh*{/b} Fine."
    player_name "... But only because you asked me so nicely."
    show player 5
    show jenny f_eyeroll
    jen "Yeah, yeah, whatever."
    show jenny f_upset_talk
    jen "I need you to go to the mall and buy something for me."
    show jenny f_upset
    show player 12
    player_name "Why does it always come down to money with you?"
    show player 5
    show jenny f_upset_talk
    jen "Don't be an asshole, you know I need the money."
    jen "It's not that big a deal, it's only one-hundred dollars..."
    show jenny f_upset
    show player 23
    player_name "That's a lot of money, {b}[jen_name]{/b}!"
    show player 11
    show jenny f_eyeroll
    jen "Don't be stupid, one-hundred dollars is nothing."
    show jenny f_upset
    show player 12
    player_name "{b}*Sigh*{/b} What's in it for me?"
    show player 5
    show jenny f_upset_talk
    jen "I dunno, I guess... I'll take everything off for you?"
    show jenny f_upset
    show player 17
    player_name "You'll get completely naked in front of me but you won't tell me what your planning for money?"
    show player 13
    show jenny f_angry_talk
    jen "You wanna see me naked or not?"
    show jenny f_angry
    show player 4 with dissolve
    player_name "..."
    show player 14 with dissolve
    player_name "Alright, sure."
    show player 26
    player_name "... But I get to look as long as I want."
    show player 13
    show jenny f_eyeroll
    jen "Ugh, fine... Within reason."
    show jenny f_upset_talk
    jen "... And don't even think about touching because that's not happening, perv!"
    show jenny f_upset
    show player 14
    player_name "Yeah, yeah..."
    return

label jenny_bedroom_jenny_go_to_her_room_dominant:
    scene expression player.location.background_closeup with None
    show jenny f_upset at flip
    show jenny at Position (xpos=500)
    show player 10 at left
    with dissolve
    player_name "Listen, {b}[jen_name]{/b} I wasn't trying to-"
    hide jenny
    show jenny f_grin_down b_pull1 a_empty
    with dissolve
    pause
    show jenny b_pull2 f_empty
    show player 22
    player_name "!!!" with hpunch
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show jenny b_groping a_groping_hips f_upset with dissolve
    show player 23
    player_name "W-what are you doing?"
    show player 428
    show jenny f_upset_talk
    jen "Tell me these aren't the hottest pair of tits you've ever seen?!"
    show jenny f_upset
    show player 427
    player_name "Y-yeah..."
    player_name "{b}*Gulp*{/b} Those are really nice!"
    show player 427g
    show jenny f_upset_talk
    jen "That's what I thought."
    show jenny f_eyeroll
    jen "Fuck!"
    jen "... I should have made you pay for this."
    show jenny f_upset
    show player 429
    player_name "I'll pay you."
    show player 426
    show jenny f_surprised
    jen "Hmm?"
    show player 429
    player_name "If you let me touch them."
    show player 426
    show jenny f_eyeroll
    jen "Yeah, right!"
    show jenny f_upset_talk
    jen "In your dreams, loser!"
    show jenny f_upset
    player_name "..."
    show player 429
    player_name "Fine."
    show player 5f with dissolve
    pause
    show jenny f_sad
    hide player with dissolve
    pause
    show jenny f_sad_talk
    jen "Wait!"
    show jenny f_sad
    show player 426 at left with dissolve
    pause
    show jenny f_upset_talk
    jen "Two-hundred."
    show jenny f_upset
    show player 429
    player_name "What?"
    show player 426
    show jenny f_upset_talk
    jen "Two-hundred and you can touch them."
    show jenny f_upset
    show player 429
    player_name "Alright."
    show player 426
    show jenny f_eyeroll
    jen "... I cannot believe I'm doing this."
    show jenny f_upset_talk
    jen "You're lucky I need the money."
    show jenny f_upset
    return

label jenny_bedroom_jenny_go_to_her_room_dominant_has_money:
    show player 638 with dissolve
    player_name "Here."
    show player 640b

    show jenny f_eyeroll
    jen "I should have asked for three-hundred..."
    show jenny f_upset
    show player 640e
    player_name "Too late now."
    show player 426 with dissolve
    if M_jenny.finished_state(S_jenny_go_to_her_room):
        show jenny f_grin_down b_pull1 a_empty
        with dissolve
        pause
        show jenny b_pull2 f_empty
        pause
        show jenny b_pull3 with dissolve
        show jenny b_pull4 with dissolve
        pause
        show jenny b_groping a_groping_hips f_upset_talk with dissolve
    else:
        show jenny f_upset_talk
    jen "Just hurry up."
    hide player
    show jenny b_groping_touch_look f_upset
    with dissolve
    pause
    show jenny b_groping_touch_talk
    player_name "Wow!"
    player_name "They're so soft!"
    show jenny f_eyeroll b_groping_touch
    jen "Well yeah, dummy."
    show jenny f_upset
    pause
    show jenny a_groping_up f_sad_talk with dissolve
    jen "Mmm, be careful!"
    jen "My nipples are sensitive!"
    show jenny f_sad
    pause
    show jenny b_groping_suck a_groping_up_clench f_nipple2
    jen "!!!" with hpunch
    show jenny f_nipple1
    jen "I never said you could-"
    show jenny f_nipple2
    jen "Ahh!"
    pause
    jen "Fffffuu-"
    pause
    show jenny f_angry_talk b_cover a_empty
    show player 24 at left
    with dissolve
    jen "Stop!"
    jen "It's too much, I can't..."
    show jenny f_angry
    pause
    show jenny f_angry_talk
    jen "Ugh, you're such a pervert!"
    show jenny f_angry
    show player 14
    player_name "You liked it."
    show player 13
    show jenny f_angry_talk
    jen "Yeah, right!"
    show jenny f_angry
    show player 17
    player_name "Liar."
    show player 13
    show jenny f_angry_talk
    jen "Just get out."
    show jenny f_angry
    show player 14
    player_name "Fine."
    player_name "Pleasure doing business with you, {b}[jen_name]{/b}."
    hide player with dissolve
    show jenny f_angry_talk
    jen "Shut up!"
    show jenny f_angry

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Wow, she's got like, the best tits in the world. )"
    player_name "( I can't believe she's letting me touch them! )"
    player_name "( This is awesome! )"
    hide player with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_dominant_no_money:
    show player 10
    player_name "I don't have two-hundred."
    show player 5
    show jenny f_upset_talk
    jen "Ugh, seriously?!"
    jen "Well, you're definitely not touching them for free!"
    show jenny f_upset
    show player 10
    player_name "I'll give you what I've got."
    show player 5
    show jenny f_upset_talk
    jen "No way!"
    jen "If you think I'm letting you touch them for anything less than two-hundred, you're nuts!"
    show jenny f_upset
    player_name "..."
    show player 10
    player_name "{b}*Sigh*{/b} Fine."
    player_name "{b}I'll be back with the money{/b}."
    show player 5
    show jenny f_upset_talk
    jen "Hurry up, loser."
    jen "I need that money!"
    show jenny f_upset
    show player 10
    player_name "Yeah, yeah."
    hide player
    hide jenny
    with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive:
    scene expression player.location.background_closeup with None
    show jenny a_phone f_grin_down at flip
    show jenny at Position (xpos=500)
    show player 10 at left
    with dissolve
    player_name "Listen, {b}[jen_name]{/b} I wasn't trying to-"
    show player 5 with None
    hide jenny
    show jenny b_dressed a_dressed_hips f_upset_talk
    with dissolve
    jen "Just shut up..."
    jen "I've got a proposition for you."
    show jenny f_upset
    show player 10
    player_name "Okay, what?"
    show player 5
    show jenny f_grin_talk
    jen "You're a horny little loser, right?"
    show jenny f_grin
    show player 29 with dissolve
    player_name "What?! N-no..."
    show player 3
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "And I need money, so..."
    show jenny f_upset
    pause
    show jenny f_eyeroll
    jen "... How about you pay me two-hundred dollars and I let you look at my tits?"
    show jenny f_upset
    show player 12 with dissolve
    player_name "Two-hundred dollars?!"
    show player 10
    player_name "I dunno, that's a lot..."
    show player 5
    show jenny f_upset_talk
    jen "Yeah but we're talking like actual, real tits here."
    jen "Not anime tits like you're used to, loser."
    show jenny f_upset
    show player 4 with dissolve
    player_name "..."
    show player 92
    player_name "Fine."
    return

label jenny_bedroom_jenny_go_to_her_room_submissive_has_money:
    show player 640e with dissolve
    player_name "Here."
    show player 13

    show jenny f_grin_down a_dressed_money_counting
    with dissolve
    pause
    show jenny f_eyeroll a_dressed_hips with dissolve
    jen "I should have asked for three-hundred..."
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "{b}*Sigh*{/b}"
    label repeat_boobies:
    jen "I hope you can appreciate how lucky you are."
    show jenny f_grin_down b_pull1 a_empty with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4
    show player 428
    player_name "!!!" with hpunch
    show jenny b_groping a_groping_hips f_grin with dissolve
    show player 429
    player_name "Wow..."
    show jenny f_grin_talk
    jen "Tuck your tongue back into your mouth, nerd!"
    show jenny f_grin
    pause
    player_name "They're so-"
    show jenny f_grin_talk
    jen "Beautiful."
    show player 731 with dissolve
    jen "I know."
    show jenny f_grin
    pause
    hide player
    show jenny f_surprised b_groping_touch1 a_groping_up
    jen "!!!" with hpunch
    show player 732
    show jenny f_angry_talk b_cover a_empty
    with dissolve
    jen "Hey, no touching!"
    show jenny f_angry b_groping a_groping_up_clench
    show player 24 at left
    with dissolve
    player_name "Sorry, I didn't mean to-"
    show jenny f_upset_talk a_groping_hips with dissolve
    jen "Pathetic little losers don't get to touch!"
    show player 11
    show jenny b_pull1 a_empty with dissolve
    jen "I think that's enough..."
    show jenny b_dressed a_dressed_hips f_upset with dissolve
    show player 12
    player_name "Aww, c'mon!"
    show player 90
    show jenny f_upset_talk with dissolve
    jen "No, you've looked plenty."
    show jenny f_grin_talk
    jen "You want to look again, you know the price."
    show jenny f_grin
    show player 10
    player_name "Two-hundred?"
    show player 5
    show jenny f_grin_talk
    jen "That's right."
    show jenny f_upset_talk
    jen "Now get out."
    hide jenny with dissolve
    pause
    show player 29 with dissolve
    player_name "Aww, man..."
    hide player with dissolve
    pause

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show player 17 with dissolve
    player_name "( Wow, she's got like, the best tits in the world. )"
    show player 26
    player_name "( I wish, I could have touched them... )"
    player_name "( Maybe next time? )"
    hide player with dissolve
    return

label jenny_bedroom_jenny_go_to_her_room_submissive_no_money:
    show player 10
    player_name "I don't even have two-hundred!"
    show player 5
    show jenny f_upset_talk
    jen "Well, I'm not showing you my tits for anything less than two-hundred."
    jen "So you'd better go and get it if you want a look at these things..."
    show jenny f_upset
    show player 24
    player_name "{b}*Sigh*{/b} Fine."
    player_name "{b}I'll be back with the money{/b}."
    show jenny f_upset_talk
    jen "Hurry up, loser."
    jen "I need that money!"
    show jenny f_upset
    show player 10
    player_name "Yeah, yeah."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_jenny_caught_snooping:
    scene expression player.location.background_blur with None
    show player 11 at left
    show jenny f_angry_talk a_dressed_hips
    with dissolve
    jen "What the fuck, {b}[firstname]{/b}?!"
    show jenny f_angry
    show player 22
    player_name "!!!" with hpunch
    if M_jenny.finished_state(S_jenny_snoop_nightstand) and player.has_item('jenny_panties'):
        show jenny f_upset_talk
        jen "Oh.{w=1} My.{w=1} God."
        show jenny f_angry_talk
        jen "ARE THOSE MY PANTIES?!"
        show jenny f_angry
        show player 23
        player_name "N-no?"
        player_name "I didn't-"
        show player 22
        show jenny f_angry_talk
        jen "Save it, loser. Give them here!"
        $ player.remove_item("jenny_panties")
        $ player.inventory.remove_picked_up("jenny_panties")
        show jenny f_upset_talk
        jen "I suppose you just stumbled in here by accident, huh?"
    else:
        show jenny f_angry_talk
        jen "What are you doing in my room, you perverted little loser?!"
        show jenny f_angry
        show player 23
        player_name "N-nothing!"
        show player 22
        show jenny f_upset_talk
        jen "Oh, yeah right. You just stumbled in here by accident, huh?"
    show jenny f_upset
    show player 29 with dissolve
    player_name "Not exactly..."
    show player 24 with dissolve
    player_name "{b}*Sigh*{/b} I was looking for your {b}digital camera{/b}, okay?"
    show jenny f_upset_talk
    jen "Huh, why?!"
    show jenny f_upset
    show player 3 with dissolve
    pause
    show jenny f_grin_talk
    jen "Oh, I get it."
    jen "You're so pathetic, you know that?"
    jen "You'd rather sit in your room fapping to stolen pictures of me, than go out and find real a girlfriend."
    show jenny f_grin
    show player 10 with dissolve
    player_name "N-no."
    show player 5
    show jenny f_grin_talk
    jen "Haha, yeah right!"
    show jenny f_grin
    show player 24
    player_name "..."
    show jenny f_grin_talk a_dressed_camera_give with dissolve
    jen "Tell you what, I'll let you look at the pictures, okay?"
    show jenny f_grin
    show player 10
    player_name "Y-you will?"
    show player 5
    show jenny f_grin_talk
    jen "Sure."
    show player 20
    show jenny f_grin_talk a_dressed_camera_back with dissolve
    with dissolve
    jen "{b}Sixty bucks{/b}."
    show jenny f_grin
    show player 10 with dissolve
    player_name "What?!"
    show player 5
    show jenny f_grin_talk
    jen "{b}Sixty bucks{/b} and you can look at them for two minutes."
    show jenny f_grin
    show player 10
    player_name "Two minutes?!"
    show player 12
    player_name "You're out of your mind."
    show player 5
    show jenny f_upset_talk
    jen "Hey, you're the pathetic one who's hard up to get his rocks off..."
    jen "You want to see the sexy pics or not?"
    show jenny f_upset
    menu:
        "Fine. {color=7ff7}[[Submissive]{/color}":
            $ M_jenny.decrement("dominance")
            if player.has_money(60):
                show player 174b with dissolve
                player_name "Here."
                show player 727
                show jenny f_grin_talk a_money
                with dissolve
                jen "Hahaha! Oh my god, you're so pathetic!"
                jen "You've got two minutes..."
            else:
                show player 24
                player_name "I don't even have Sixty dollars..."
                show jenny f_eyeroll
                jen "{b}*Sigh*{/b} God, you're pathetic."
                show jenny f_upset
                pause
                show jenny f_upset_talk
                jen "Fine, just give me what you do have."
                show jenny f_upset
                if not player.has_money(1):
                    show player 40 with dissolve
                    player_name "I don't have anything... Please can I just look?"
                    show jenny f_upset_talk
                    jen "Pathetic..."
                    jen "You've got 30 seconds..."
                else:
                    show player 174b with dissolve
                    show jenny f_upset_talk
                    jen "You've got two minutes..."
            $ player.spend_money(60)
        "Screw you. {color=f77b}[[Dominant]{/color}":
            $ M_jenny.increment("dominance")
            show player 12
            player_name "I'm not paying you {b}sixty dollars{/b} for a couple stupid pictures..."
            show player 90
            show jenny f_angry_talk
            jen "Excuse me?!"
            show jenny f_angry
            show player 12
            player_name "You heard me!"
            show player 90
            show jenny f_angry_pouting a_dressed_crossed with dissolve
            jen "Hmph!"
            pause
            show jenny f_upset_talk
            jen "{b}Thirty bucks{/b}?!"
            show jenny f_upset
            show player 12
            player_name "NO!"
            show player 90
            show jenny f_gross_talk
            jen "Seriously?!"
            show jenny f_angry_talk
            jen "Grr, just get out!"
            show jenny f_angry
            show player 10
            player_name "What?"
            show player 90
            show jenny f_angry_talk a_dressed_upset with dissolve
            jen "Get out of my fucking room before I tell {b}[deb_name]{/b} you're perving on me!"
            show jenny f_angry
            show player 12
            player_name "Gladly."
            hide player with dissolve
            show jenny f_angry_pouting a_dressed_crossed with dissolve
            jen "( He's such a pain in my ass! )"

            $ player.go_to(L_home_hallway)
            scene expression player.location.background_closeup with None
            show player 90 with dissolve
            player_name "( Damn, I really wanted to see those pictures but not so much that I'll let her walk all over me. )"
            show player 13
            player_name "( At least I found out she's got a diary and just how sexually frustrated she is. )"
            show player 17
            player_name "( Haha! )"
            hide player with dissolve
            return
    show expression "backgrounds/location_home_jennybedroom_photo01.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo02.jpg" at Position (yoffset=110) with dissolve
    pause
    show expression "backgrounds/location_home_jennybedroom_photo03.jpg" at Position (yoffset=110) with dissolve
    pause
    scene expression player.location.background_closeup with None
    show player 11 at left
    show jenny f_upset_talk a_dressed_camera_look
    with dissolve
    jen "Times up, loser!"
    show jenny f_upset a_dressed_hips with dissolve
    show player 12
    if not player.has_money(1):
        player_name "That wasn't even 30 seconds!"
    else:
        player_name "That wasn't even two minutes!"
    show player 90
    show jenny f_grin_talk
    jen "Aww, poor little virigin..."
    show jenny f_upset_talk
    jen "Go whine to somebody who cares."
    hide jenny with dissolve
    jen "... And get the fuck outta my room, LOSER!"
    show player 15
    player_name "Fine!"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 90 with dissolve
    player_name "( She's such a bitch! )"
    show player 17
    player_name "( Those pics were worth it though... )"
    hide player with dissolve
    return

label jennys_bedroom_jenny_snoop_around:
    scene expression player.location.background_closeup with None
    show player 5 with dissolve
    player_name "( Okay, I just need to {b}find that camera and get out of here as quickly as possible{/b}. )"
    player_name "( She probably keeps it- )"
    show player 11
    player_name "( !!! )"
    player_name "( Is that a diary?! )"
    show player 17
    player_name "( Oh, I have to check that out! )"
    hide player with dissolve
    return

label sis_bedroom_sis_not_in_room:
    scene jennybedroom
    show player 34 at left with dissolve
    player_name "( Hmmm... )"
    show player 35 at left
    player_name "( She's not in her room... )"
    show player 18 at left
    player_name "( Maybe I can look around a bit! )"
    hide player 18 at left with dissolve
    return

label sis_bedroom_sis_sleeping:
    scene jennybedroom_clear
    player_name "( {b}[jen_name]'s{/b} sleeping. )"
    player_name "( I have to be real quiet or she might hear me... )"
    player_name "( ...Don't want to wake her up, or I'm dead! )"
    return

label bedtable_night:
    call expression game.dialog_select("jenny_bedroom_cannot_snoop")
    $ in_sis_room = True
    jump expression game.dialog_select("sis_bedroom_dialogue")

label desk02_locked_dialogue:
    scene expression game.timer.image("sisbedroom{}")
    show player 35 at left
    player_name "( I don't have the {b}password{/b} for her computer... )"
    $ game.main()

label sister_bedtable_panties:
    scene expression player.location.background_blur with None
    show player 5 with dissolve
    player_name "( Hmm, it's not in here... )"
    pause
    show player 30
    player_name "( Are those her panties? )"
    hide player with dissolve
    return

label siscomp_day:
    scene expression player.location.background_closeup
    show player 98 at Transform(align=(-.53, 1.)) with dissolve
    player_name "( Hmm... Let's see if she left her computer on. )"
    player_name "( I wonder what I could find on here... )"
    show jenny f_angry at right
    if L_home_shower.is_here(M_jenny):
        show jenny b_towelhead
    with dissolve
    jen "..."
    show jenny f_angry_talk with hpunch
    jen "Can I help you with {b}SOMETHING{/b}??!"
    show jenny f_angry
    hide player
    show player f_shock at left
    with Dissolve(.2)
    player_name "!!!"
    show player f_shy_talk a_dressed_behind_head at left
    show jenny a_dressed_crossed f_gross
    with dissolve
    player_name "Sorry!! I was just... trying to see if your internet is working!!"
    player_name "I can't seem to connect on my computer..."
    show player f_shy
    show jenny f_gross_talk
    jen "Don't fucking {b}touch{/b} my computer!!"
    show player f_looking_down a_dressed_pocket with dissolve
    jen "Just ask me next time."
    show player f_sad_talk_down
    show jenny f_gross
    player_name "Of course!"
    show player f_surprised_teeth
    show jenny f_angry_talk
    jen "Now, get out of {b}MY ROOM{/b}!!!"
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_cheerleader_deal:
    scene jennybedroom
    show jenny f_upset
    show player f_worried_talk
    with dissolve
    player_name "Hey, {b}[jen_name]{/b}."
    show player f_worried
    show jenny f_upset_talk
    jen "What do you want?"
    show jenny f_upset a_dressed_crossed with dissolve
    show player f_worried_talk
    player_name "I need your help with something..."
    show player f_worried
    show jenny f_grin_talk
    jen "How much are you paying me?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "I haven't even told you what it is yet!"
    show player f_worried
    show jenny f_grin_talk
    jen "Hmm, good point... I should hear all the details before I set the price!"
    show jenny f_grin
    show player f_tired_talk
    player_name "*Sigh*"
    show player f_worried_talk
    player_name "There's this girl at school who needs help with her cheer-leading routine."
    show player f_worried
    show jenny f_grin_talk
    jen "Is this some girl you're trying to bang?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Huh? NO!"
    show player f_worried
    show jenny f_grin_talk a_dressed_hips with dissolve
    jen "Why not? Is she ugly?"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "No, she's gorgeous, but a total bitch!"
    show player f_worried
    show jenny f_grin_talk
    jen "Hmm, I like her already."
    show jenny f_grin
    player_name "..."
    show player f_skeptical_talk
    player_name "So you'll help her with the routine?"
    show player f_worried
    show jenny f_grin_talk
    jen "$500."
    show jenny f_grin
    show player f_surprised
    player_name "What?! Are you nuts?"
    show player f_worried
    show jenny f_upset_talk
    jen "That's the price."
    jen "Pay up or get out."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Couldn't you just help me out?"
    show player f_worried
    show jenny f_laugh
    jen "Hahahaha, good one {b}[firstname]{/b}!"
    show jenny f_upset_talk a_dressed_hips_asking with dissolve
    jen "$500."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "*Sigh* Fine!"
    show jenny a_dressed_crossed with dissolve
    player_name "I'll come back when I've got the money..."
    hide player
    hide jenny
    with dissolve
    return

label jennys_bedroom_bissette_roxxy_jenny_spying:
    $ persistent.cookie_jar["Roxxy"]["gallery"]["02_unlocked"] = True
    $ suffix = ""
    if M_roxxy.get("roxxy trailer sex"):
        $ suffix = "_sex"
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_pre")
    if M_jenny.is_set("seen MCs penis"):
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis{}".format(suffix))
    else:
        call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis{}".format(suffix))
    call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying_after")
    $ del suffix
    $ renpy.end_replay()
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_pre:
    scene jennybedroom_peek_c
    show jenny b_bed_cheer a_bed_cheer_down f_bed_roxxy_normal at Position (align=(0,0))
    show roxxy 36 at Position (xpos=415,ypos=692)
    show roxxy_outfit cheer 41b
    show poms 41 zorder 665
    show xtra 41 zorder 666
    with dissolve
    rox "Thanks again for letting me borrow your old uniform."
    show roxxy 35
    show jenny f_bed_roxxy_normal_talk
    jen "Not a problem!"
    jen "It doesn't fit me anyways."
    jen "Shit, this college uniform barely fits..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Haha, yeah."
    show roxxy 36
    rox "It looks like your tits are gonna spill out, like any second..."
    show roxxy 35
    show jenny f_bed_roxxy_laugh
    jen "Hehe!"
    show jenny f_bed_roxxy_normal_talk
    jen "... That's what I'm saying though! The judges totally give extra points for sex appeal."
    jen "That's why I never wear a bra during competitions."
    show jenny f_bed_roxxy_normal
    show roxxy 36
    rox "Y-yeah, I never thought about it."
    rox "You're like, a total genius!"
    show roxxy 35
    show jenny f_bed_roxxy_normal_talk
    jen "Tell me something I don't know..."
    jen "These ladies won me three consecutive state championships!"
    show jenny f_bed_roxxy_normal
    show roxxy 36
    rox "... They are really nice..."
    show roxxy 38
    show jenny f_bed_roxxy_normal_talk
    jen "Thanks!"
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Yours are nice too."
    show jenny f_bed_roxxy_sexy_down
    show roxxy 36
    rox "Yeah but mine aren't as big as yours..."
    show roxxy 38
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Mmm, maybe not but I betcha they're perkier than mine."
    show jenny f_bed_roxxy_sexy_down
    show roxxy 37
    rox "Hehe, maybe..."
    show roxxy 35
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Lemme have a look at those puppies."
    hide roxxy
    hide roxxy_outfit
    show jenny b_bed_cheer_roxxy_lift1 a_empty f_bed_roxxy_sexy_down
    with dissolve
    rox "Whoa!! What are you-{p=1}{nw}"
    show jenny b_bed_cheer_roxxy_lift2 with dissolve
    pause .1
    show jenny b_bed_cheer_roxxy_lift3 with dissolve
    pause .1
    show roxxy 34b at Position (xpos=380,ypos=692)
    show jenny b_bed_cheer a_bed_cheer_down f_bed_roxxy_normal_talk
    with dissolve
    jen "Calm down!"
    jen "It's just us girls here."
    show jenny f_bed_roxxy_sexy_down
    rox "..."
    show roxxy 34
    rox "I-I dunno..."
    show roxxy 34b
    show jenny f_bed_roxxy_sexy_talk_down
    jen "Here."
    show jenny b_bed_cheerlift f_bed_roxxy_normal_low a_empty with dissolve
    pause
    show jenny b_bed_cheerup a_bed_cheerup_surprised f_bed_roxxy_happy_talk_down with dissolve
    jen "See, nothing to be embarrassed about!"
    show jenny f_bed_roxxy_sexy_down
    show roxxy 40 at Position (xpos=415,ypos=692)
    show roxxy_outfit cheer 41d
    with dissolve
    rox "... Y-yeah, I guess..."
    hide roxxy
    hide roxxy_outfit
    show jenny b_bed_cheer_roxxy_touch1 a_empty f_bed_roxxy_sexy_down
    rox "!!!" with hpunch
    show jenny f_bed_roxxy_sexy_talk_down
    jen "I was right, they are perkier than mine..."
    jen "I'm kinda jealous!"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_sexy_down
    rox "... Thanks."
    show jenny b_bed_cheer_roxxy_touch1 f_bed_roxxy_sexy_talk_down
    jen "You've got cute little nipples too!"
    show jenny f_bed_roxxy_sexy_down
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Aww, she's shy!"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_normal
    rox "I'm not-"
    show jenny b_bed_cheer_roxxy_touch1 f_bed_roxxy_normal_talk
    jen "So adorable!"
    jen "Don't you wanna feel mine?"
    show jenny b_bed_cheer_roxxy_touch2 f_bed_roxxy_normal
    rox "You want me to-"
    show jenny b_bed_cheer_roxxy_grab1 f_bed_roxxy_sexy_down
    rox "!!!" with hpunch
    jen "See, not so bad..."
    show jenny b_bed_cheer_roxxy_grab2
    rox "Your skin is so soft..."
    show jenny b_bed_cheer_roxxy_grab1 f_bed_roxxy_sexy_talk_down
    jen "I know, right?"
    jen "It's this special lotion I use. I'll hook you up!"
    show jenny b_bed_cheer_roxxy_grab2 f_bed_roxxy_sexy_down
    rox "Thanks, {b}[jen_name]{/b}!"
    show roxxy 39 at Position (xpos=415,ypos=692)
    show jenny b_bed_cheerup a_bed_cheerup_down f_bed_roxxy_laugh
    show roxxy_outfit cheer 41d
    with dissolve
    jen "Damn girl! You've got a bangin' body!"
    show jenny f_bed_roxxy_sexy_down
    show roxxy 40
    rox "You think the judges will notice?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Totally!"
    if M_roxxy.get("roxxy trailer sex"):
        jen "I can't believe {b}[firstname]{/b} is hitting that!"
        show jenny f_bed_roxxy_normal
        show roxxy 40
        rox "Hehe, well I really made him work for it."
        rox "He's a pretty tenacious guy..."
    else:
        jen "I can see why that dweeb downstairs wants to hit that."
        show jenny f_bed_roxxy_normal
        show roxxy 40
        rox "I can't believe you two live together!"
        rox "You're so awesome and he's such a dork!"
    show roxxy 39
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis:
    show jenny f_bed_roxxy_normal_talk
    jen "He's not so bad..."
    jen "He can be pretty useful to have around."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "... Yeah, I guess he has been pretty helpful recently."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Also, just between you and me..."
    jen "He's hung like a horse!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Really?! You mean you've seen his dick?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Oh, I've seen it plenty of times."
    jen "We do live together after all."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "I guess that's true..."
    rox "So it's big, huh?"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Huge!"
    show jenny f_bed_roxxy_normal
    show roxxy 42
    rox "Interesting."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Is your boyfriend packing?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39 with dissolve
    jen "Tiny, eh? That's too bad."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Well, anyways... You ready to learn some moves?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis:
    show jenny f_bed_roxxy_normal_talk
    jen "I know right!"
    jen "I tell everybody he's the maintenance boy..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hahaha!"
    show roxxy 40
    rox "Yeah, my boyfriend threatens to kick his ass all the time."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "You have a boyfriend?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Well, kinda..."
    rox "Let's just say, he thinks he's my boyfriend."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "I like your style, {b}Roxxy{/b}!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Hehe, thanks!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Is he packing?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "What do you mean?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "You know, down south..."
    jen "Is he big?"
    show jenny f_bed_roxxy_normal
    show roxxy 42
    rox "Pfft..."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "He's small!?"
    show jenny f_bed_roxxy_normal
    show roxxy 40 with dissolve
    rox "Real tiny."
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Yeah, I don't keep him around for the sex."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "I wouldn't think so..."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Well, anyways... You ready to learn some moves?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_seen_penis_sex:
    show jenny f_bed_roxxy_normal_talk
    jen "Yeah, he can be really stubborn..."
    jen "He's resourceful though, I'll give him that."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Plus, he's got that huge cock!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "I know right?!"
    jen "He's hung like a freaking horse!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Whoa, wait... You mean you've seen it?"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Oh, I've seen it plenty of times."
    jen "Kind of unavoidable really. Living in close proximity like this."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Yeah, I guess that makes sense."
    rox "It must be annoying living with some random dude..."
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hehe, I dunno. It has it's perks."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Was your last boyfriend packing?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "{b}Dexter{/b}?"
    show roxxy 42
    rox "Pfft."
    show roxxy 43 with dissolve
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39 with dissolve
    jen "Tiny, eh? That's too bad."
    show roxxy 35e at Position (xoffset=-120, yoffset=100)
    show jenny f_bed_roxxy_normal
    rox "Yeah, he turned out to be a huge douchebag too."
    show jenny f_bed_roxxy_normal_talk
    show roxxy 39
    jen "Well, anyways... You ready to learn some moves?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Cool, let's do it!"
    return

label jennys_bedroom_bissette_roxxy_jenny_spying_havent_seen_penis_sex:
    show jenny f_bed_roxxy_normal_talk
    jen "Not hard enough, {b}Roxxy{/b}!"
    jen "He'd have to kiss my feet and grovel like a dog before I let him in my panties..."
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hahaha! Sheesh, you're a hardcore bitch, {b}[jen_name]{/b}!"
    show roxxy 40
    rox "Lucky for him, you aren't interested, huh?"
    rox "Otherwise, I could totally see him trying..."
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "... Yeah. Lucky for him..."
    jen "... So is he any good?"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "What do you mean? Like, in bed?"
    jen "Yeah."
    rox "He's amazing!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Amazing? You're joking."
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "No, I'm completely serious!"
    rox "He's like an idiot savant or something..."
    rox "... And he's got that massive cock!"
    show roxxy 39
    show jenny f_bed_roxxy_sad_talk
    jen "Huh? What do you mean by massive?"
    show jenny f_bed_roxxy_sad with None
    show roxxy 43b
    hide roxxy_outfit
    with dissolve
    rox "..."
    show roxxy 39
    show roxxy_outfit cheer 41d
    with dissolve
    show jenny f_bed_roxxy_normal_talk
    jen "You're joking!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "Not even a little bit."
    show roxxy 39
    show jenny f_bed_roxxy_sad_talk
    jen "Holy shit..."
    show jenny f_bed_roxxy_sad
    show roxxy 40
    rox "It's super crazy!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Hahaha!"
    show jenny f_bed_roxxy_normal
    show roxxy 40
    rox "I swear, he's like an orgasm machine!"
    show roxxy 39
    show jenny f_bed_roxxy_normal_talk
    jen "Interesting..."
    show jenny f_bed_roxxy_normal
    rox "..."
    show jenny f_bed_roxxy_normal_talk
    jen "Well, anyways... You ready to learn some moves?"
    show jenny f_bed_roxxy_normal
    show roxxy 37
    rox "Hell yeah!"
    show roxxy 39
    show jenny f_bed_roxxy_laugh
    jen "Cool, let's do it!"
    return


label jennys_bedroom_bissette_roxxy_jenny_spying_after:
    scene black with fade
    scene hallway
    show player 33 with dissolve
    player_name "( Wow!!! )"
    show player 17
    player_name "( Maybe this wasn't such a bad idea after all! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
