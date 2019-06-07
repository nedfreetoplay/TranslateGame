label entrance_jenny_pregnancy_first_baby_coming_home:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny b_casual a_dressed_baby f_happy at flip
    show jenny at Position (xpos=150)
    show debbie
    show player f_normal_talk at Position (xpos=450) with dissolve
    player_name "Hey, you're home!"
    show player f_normal
    show jenny f_eyeroll
    jen "Yeah, finally..."
    show jenny f_upset_talk
    jen "I hate hospitals, so much!"
    show jenny f_upset
    show debbie f_normal_talk
    deb "I'm making you a big welcome home steak for dinner, dear."
    show debbie f_normal
    show jenny f_happy_talk
    jen "Oh, that sounds amazing!"
    pause
    if M_jenny.pregnancy.baby_gender == "twins":
        jen "Would you mind watching them for a little bit?"
    elif M_jenny.pregnancy.baby_gender == "boy":
        jen "Would you mind watching him for a little bit?"
    else:
        jen "Would you mind watching her for a little bit?"
    jen "I would literally kill for a bath right now."
    show jenny f_happy
    show debbie f_normal_talk
    if M_jenny.pregnancy.baby_gender == "twins":
        deb "Of course, I'll watch them!"
        deb "Come see your godmother, little ones!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Aww, they're so cute!"
    elif M_jenny.pregnancy.baby_gender == "boy":
        deb "Of course, I'll watch him!"
        deb "Come see your godmother, little guy!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Aww, such a cutie pie!"
    else:
        deb "Of course, I'll watch her!"
        deb "Come see your godmother, little girl!"
        show debbie f_normal_talk_down a_robe_baby
        show jenny a_dressed_side
        with dissolve
        deb "Aww, such a cutie pie!"
    show debbie f_normal_down
    show jenny f_happy_talk
    jen "Thanks, {b}[deb_name]{/b}."
    show jenny f_happy
    show player f_normal_talk
    player_name "Welcome home, {b}[jen_name]{/b}!"
    show player f_normal
    show jenny f_happy_talk
    jen "Yeah, thanks {b}[firstname]{/b}."
    show jenny f_upset_talk
    jen "Out of my way, I have a date with the bath tub!"
    jen "And don't bother me!"
    show jenny f_upset
    show player f_worried_talk
    player_name "I wasn't going to..."
    show player f_worried
    show jenny f_upset_talk
    jen "Uh huh."
    hide jenny with dissolve
    pause
    show player f_normal_talk
    player_name "The tyrant returns, huh?"
    show player f_grin
    show debbie f_normal
    deb "Hmm?"
    show player f_tired_talk
    player_name "... Nevermind."
    hide player with dissolve
    return

label entrance_jenny_first_baby_stage_2_end:
    pause
    show jenny f_upset_talk
    jen "So, now what?!"
    show jenny f_upset
    show debbie f_curious
    pause
    show player f_worried_talk
    player_name "{b}[deb_name]{/b}?"
    player_name "Are you alright?!"
    show player f_worried
    show debbie f_laugh
    deb "I'm just happy..."
    show debbie f_curious
    show jenny f_upset_talk
    jen "Happy?!"
    show jenny f_upset
    show debbie f_normal_talk
    deb "I can't believe I'm going to be a godmother!"
    show debbie f_curious
    show jenny f_angry_pouting_top
    jen "..."
    show debbie f_normal_talk
    deb "Isn't it wonderful, {b}[firstname]{/b}?!"
    show debbie f_normal
    show player f_worried_talk
    player_name "Ehh, yes?"
    show player f_worried
    show debbie f_laugh
    deb "Hehe!"
    show jenny b_empty a_empty f_surprised zorder 2 at Position (xpos=376)
    show debbie b_robe_hug_jenny_bump a_empty f_normal_talk
    with dissolve
    deb "{b}*Sniff*{/b} Your child is going to be the luckiest kid in the whole world!"
    show debbie f_normal
    show jenny f_sad_talk
    jen "{b}[deb_name]{/b}..."
    show jenny at flip
    show jenny b_dressed_pregnant_bump f_sad a_dressed_side zorder 1 at Position (xpos=100)
    show debbie b_robe a_robe_mug f_normal_talk
    with dissolve
    deb "You've gotta help out too, {b}[firstname]{/b}!"
    show debbie f_sad_talk
    deb "Being a single mother is hard, believe me."
    deb "{b}[jen_name]'s{/b} gonna need all the support she can get."
    show debbie f_normal
    show player f_normal_talk
    player_name "Y-yeah, of course!"
    show player f_normal
    show debbie f_normal_talk
    deb "Why don't you two go into the dinning room and sit down?"
    show debbie f_laugh
    deb "I'll make us a nice big breakfast to celebrate!"
    show debbie f_normal
    show player f_laugh
    player_name "Yeah, okay."
    show player f_normal_talk
    player_name "C'mon, {b}[jen_name]{/b}!"
    hide player with dissolve
    show jenny f_sad_talk
    jen "Thanks, {b}[deb_name]{/b}..."
    show jenny f_sad
    show debbie f_normal_talk
    deb "You're welcome, dear."
    show debbie f_normal
    scene black with fade
    return

label entrance_jenny_first_baby_stage_2_no_diane:
    pause
    show debbie f_sad_talk
    deb "Just tell me, {b}[jen_name]{/b}."
    show debbie f_sad
    pause
    show jenny f_upset_talk
    jen "I think, I got pregnant from a toilet seat at the mall..."
    show jenny f_upset
    show debbie f_surprised_worried
    deb "{b}*Gasp*{/b}"
    show debbie f_sad
    show player f_surprised
    player_name "!!!"
    show player f_worried
    show debbie f_sad_talk
    deb "That's not-"
    show debbie f_sad
    pause
    show debbie f_surprised_worried
    deb "Can that even happen?"
    show debbie f_sad
    pause
    show jenny f_eyeroll
    jen "I dunno, probably..."
    show jenny f_upset
    pause
    show debbie f_sad_talk
    deb "Look, you don't have to tell me if you don't want to..."
    deb "It's your decision."
    deb "The important thing is that the baby is healthy and you get the care you need."
    show debbie f_sad
    show jenny f_upset_talk
    jen "R-really?"
    show jenny f_upset
    show debbie f_sad_talk
    deb "Of course, dear."
    deb "I just wish you had told me sooner, I could have been more help!"
    show debbie f_sad
    return

label entrance_jenny_first_baby_stage_2_diane:
    show diane f_laugh
    dia "Probably because she's sleeping with half the town..."
    show diane f_smirk
    show jenny f_angry_talk
    jen "Fuck you!"
    show jenny f_angry
    show diane f_annoyed
    show debbie f_angry_talk
    deb "Hey, stop it! Both of you!"
    show debbie f_angry
    show jenny f_angry_pouting_top
    jen "Hmmph!"
    pause
    show debbie f_sad_talk
    deb "Just tell me, {b}[jen_name]{/b}."
    show debbie f_sad
    pause
    show jenny f_upset_talk
    jen "I think, I got pregnant from a toilet seat at the mall..."
    show jenny f_upset
    show diane f_laugh
    show debbie f_surprised_worried
    deb "{b}*Gasp*{/b}"
    show debbie f_sad
    show player f_surprised
    player_name "!!!"
    show player f_worried
    dia "Hahahaah, that's the most ridiculous thing I've ever heard!"
    show diane f_smirk
    show jenny f_angry_talk
    jen "Shut up, {b}Diane{/b}!!!"
    show jenny f_upset
    show debbie f_sad_talk
    deb "That's not-"
    show debbie f_sad
    pause
    show debbie f_surprised_worried
    deb "Can that even happen?"
    show debbie f_sad
    show diane f_smirk_talk
    dia "No."
    show diane f_smirk
    show jenny f_upset_talk
    jen "Yes, it can!!"
    show jenny f_angry_pouting_top
    show diane f_lookup
    dia "It really can't."
    show diane f_smirk
    show debbie f_sad_talk
    deb "{b}*Sigh*{/b} Stop."
    deb "Look, she doesn't have to tell me if she doesn't want to..."
    show debbie f_sad
    show diane f_lookup
    dia "The hell she doesn't!"
    show diane f_shamed_talk_smile_back
    dia "You deserve better than-"
    show diane f_shamed
    show debbie f_sad_talk
    deb "It's alright, {b}Diane{/b}..."
    deb "It's her decision."
    deb "The important thing is that the baby is healthy and {b}[jen_name]{/b} gets the care she needs."
    show debbie f_sad
    show diane f_shamed_talk_smile_back
    dia "Good lord, {b}[deb_name]{/b}..."
    dia "You coddle her way too much!"
    show diane f_shamed
    show debbie f_sad_talk
    deb "Just let it go, please."
    show debbie f_sad
    dia "..."
    show diane f_normal_talk
    dia "Fine."
    dia "I've gotta get going anyways..."
    show debbie b_empty a_empty f_normal
    show diane b_hug_deb_robe a_empty f_normal_talk at flip
    show diane at Position (xpos=914)
    with dissolve
    dia "I'll see you tonight, love."
    show diane f_normal
    deb "..."
    hide diane
    show debbie b_robe a_robe_mug at Position (xpos=600)
    with dissolve
    return

label entrance_jenny_first_baby_stage_2_intro:
    scene expression L_home_entrance.background_closeup
    deb "Why won't you tell me who the father is?!"
    show player f_shock
    player_name "!!!" with hpunch
    jen "Would you please chill out, {b}[deb_name]{/b}?!"
    show player f_surprised_teeth
    player_name "( Uh oh, it sounds like {b}[jen_name]'s{/b} secret is out... )"
    player_name "( I'd better get down there! )"
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup
    show jenny at flip
    show jenny b_dressed_pregnant_bump f_upset a_dressed_crossed zorder 1 at Position (xpos=100)
    show debbie f_sad_talk zorder 1 at Position (xpos=600)
    if M_diane.finished_state(S_diane_check_barn_out):
        show diane b_casual a_casual_sides f_smirk zorder 0 at Position (xpos=400)
    show player f_worried zorder 2 at Position (xpos=400) with dissolve
    deb "Why won't you tell me who the father is?"
    show debbie f_sad
    show jenny f_upset_talk
    jen "I don't know who the father is, okay {b}[deb_name]{/b}?!"
    jen "Stop asking!"
    show jenny f_upset
    show debbie f_sad_talk
    deb "How can you not know?!"
    show debbie f_sad
    return

label entrance_jenny_want_some_breakfast:
    scene expression player.location.background_closeup with None
    show player
    show debbie f_normal_talk
    with dissolve
    deb "Sweetie, could you come in here for a second?"
    show debbie f_normal
    show player f_normal_talk
    player_name "Sure."
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show player f_normal_talk
    show debbie
    with dissolve
    player_name "What's up, {b}[deb_name]{/b}?"
    show player f_normal
    show debbie f_normal_talk
    deb "Would you mind {b}poking your head outside{/b} and asking {b}[jen_name]{/b} if she wants some of this breakfast?"
    show debbie f_normal
    show player f_worried_talk
    player_name "Ehh, I don't mind."
    player_name "She's just gonna say no..."
    show player f_worried
    show debbie f_laugh
    deb "Hehe, probably."
    hide player
    show debbie b_robe_hug1 a_empty f_empty
    with dissolve
    deb "Thanks, sweetie."
    show debbie b_robe_hug2
    player_name "No problem."
    hide debbie
    show player f_thinking a_dressed_thinking with dissolve
    player_name "( Hmm, I think {b}[jen_name]{/b} is {b}lounging out by the pool...{/b} )"
    hide player with dissolve
    return

label entrance_jenny_catch_her_jilling:
    $ player.location = L_home_entrance
    if store._in_replay is not None:
        $ game.timer._tod = 3
    scene expression player.location.background_closeup with None
    show player f_thinking a_dressed_thinking at flip
    with dissolve
    player_name "( Hmm? )"
    player_name "( Why is the TV on? )"
    pause
    player_name "( Did someone forget to turn it off? )"
    player_name "( I should check it out. )"
    hide player with dissolve
    scene expression "backgrounds/location_home_livingroom_couch_night_closeup.jpg"
    player_name "( Is that {b}[jen_name]{/b}?! )"
    player_name "( What's she- )"
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 300 at Position(xpos=566,ypos=331)
    show jenny b_couch_clit a_empty f_empty zorder 2
    player_name "( !!! )"
    hide player
    show player 299d zorder 1 at Position (yoffset=-291,xoffset=16)
    with dissolve
    pause
    show player 301 at Position(xpos=602,ypos=386) with fastdissolve
    player_name "( She's masturbating in the living room! )"
    player_name "( This is awesome! )"
    pause
    player_name "( What is she watching?! )"
    scene home_livingroom_tv
    show home_tv_channel_10 at Position(xpos=522, ypos=521)
    with dissolve
    player_name "( It's a woman jerking some guy off with her feet! )"
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show player 301 at Position(xpos=602,ypos=386)
    show jenny b_couch_clit a_empty f_empty
    player_name "Feet?!"
    show jenny b_couch_cought
    jen "!!!" with hpunch
    jen "What the fuck, {b}[firstname]{/b}?!"
    hide player
    show player b_couch_sit a_couch_boner_covered f_couch_sit_right_talk zorder 1
    show jenny b_couch_sit f_couch_sit_angry a_couch_rest zorder 2
    with dissolve
    player_name "I'm sorry, I-"
    show player f_couch_sit_right
    show jenny f_couch_sit_angry_talk
    jen "Are you just stalking me all over the house now?!"
    show jenny f_couch_sit_angry
    show player f_couch_sit_right_talk
    player_name "Shh, you're gonna wake {b}[deb_name]{/b}!"
    show player f_couch_sit_right
    show jenny f_couch_sit_upset_talk
    jen "Seriously, what do I have to do to get some alone time?!"
    jen "It's really beginning to-"
    show jenny f_couch_sit_surprised
    jen "Are you hard right now?"
    show player f_couch_sit_down_talk
    player_name "Uhh, yeah..."
    show player f_couch_sit_right_talk
    player_name "You were masturbating and it was really hot and..."
    show player f_couch_sit_right
    jen "Jesus."
    show jenny f_couch_sit_sexy_down
    pause
    show jenny f_couch_sit_sexy_talk_down
    jen "Let me see it."
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_right_talk
    player_name "Huh?"
    show player f_couch_sit_right
    show jenny f_couch_sit_sexy_talk_down
    jen "Show me!"
    show jenny f_couch_sit_sexy_down
    show player f_couch_sit_right_talk
    player_name "O-okay..."
    show player f_couch_sit_down a_couch_boner_pull1 with dissolve
    pause
    show player f_couch_sit_down a_couch_boner_pull2 with dissolve
    show player f_couch_sit_down a_couch_boner with dissolve
    show jenny f_couch_sit_sexy_talk_down
    jen "I've always wanted to try this..."
    show jenny f_couch_sit_sexy_down a_couch_up with dissolve
    show player f_couch_sit_down_surprised
    player_name "!!!"
    show player f_couch_sit_down_talk a_couch_sides
    $ M_jenny.set('sex speed', .3)
    show jenny a_empty
    show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub zorder 3 at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    player_name "What are you-"
    show player f_couch_sit_down
    show jenny f_couch_sit_sexy_talk_down
    jen "Shhh!"
    jen "Now you're the one who's going to wake up {b}[deb_name]{/b}!"
    show jenny f_couch_sit_sexy_down
    player_name "..."
    pause
    if store._in_replay is not None:
        jump jenny_couch_fj_loop
    return

label entrance_jenny_catch_her_leaving_has_money_dom:
    show player 10
    player_name "Here."
    show player 41 with dissolve
    pause
    show player 5
    show jenny f_upset_talk a_money
    with dissolve
    jen "It's about freaking time..."
    show jenny f_grin_down a_dressed_money_counting
    pause
    show player 10
    player_name "Can I go with you?"
    show player 5
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "What?! NO!"
    show jenny f_upset
    show player 12
    player_name "C'mon!"
    show player 90
    show jenny f_upset_talk
    jen "Absolutely not!"
    jen "I'm not going out in public with a loser like you..."
    show jenny f_gross
    show player 10
    player_name "... But I've given you so much money and-"
    show player 5
    pause
    show jenny f_upset_talk
    jen "You are such a pain in my ass..."
    show jenny f_upset
    show player 40 with dissolve
    player_name "P-please?!"
    pause
    show jenny f_eyeroll
    jen "{b}*Sigh*{/b} Fine, just quit whining."
    show jenny f_upset
    show player 17 with dissolve
    player_name "Sweet!"
    show player 13
    show jenny f_upset_talk
    jen "... And don't walk too close! I don't want people thinking we're together."
    show jenny f_upset
    show player 10
    player_name "O-okay."
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_no_money_dom:
label entrance_jenny_catch_her_leaving_no_money_sub:
label entrance_jenny_catch_her_leaving_no_money_dom_first:
    show player 29 with dissolve
    player_name "Actually, I don't have two-hundred right now..."
    show player 5 with dissolve
    show jenny f_upset_talk
    jen "Ugh, are you kidding me?"
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "Well, go and get it!"
    show jenny f_upset
    show player 12
    player_name "Yeah, yeah..."
    show player 90
    show jenny f_angry_talk
    jen "I'm serious!"
    show jenny f_angry
    show player 12
    player_name "I'll get it, just chill out."
    show jenny f_angry_talk
    jen "Hurry up!"
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving_repeat:
    scene expression player.location.background_blur with None
    show player 5 at left
    show jenny b_casual f_upset_talk
    with dissolve
    jen "You get the money yet?"
    show jenny f_upset
    return

label entrance_jenny_catch_her_leaving_has_money_sub:
    show player 10
    player_name "Here."
    show player 41 with dissolve
    pause
    show player 5
    show jenny f_upset_talk a_money
    with dissolve
    jen "It's about freaking time..."
    show jenny f_grin_down a_dressed_money_counting
    pause
    show player 10
    player_name "Can I go with you?"
    show player 5
    show jenny f_upset_talk a_dressed_hips with dissolve
    jen "What?! NO!"
    show jenny f_upset
    show player 12
    player_name "C'mon!"
    show player 90
    show jenny f_upset_talk
    jen "Absolutely not!"
    jen "I'm not going out in public with a loser like you..."
    show jenny f_gross
    show player 10
    player_name "... But I've given you so much money and-"
    show player 5
    pause
    show jenny f_upset_talk
    jen "You are such a pain in my ass..."
    show jenny f_upset
    show player 40 with dissolve
    player_name "P-please?!"
    pause
    show jenny f_eyeroll
    jen "{b}*Sigh*{/b} Fine, just quit whining."
    show jenny f_upset
    show player 17 with dissolve
    player_name "Sweet!"
    show player 13
    show jenny f_upset_talk
    jen "... And don't walk too close! I don't want people thinking we're together."
    show jenny f_upset
    show player 10
    player_name "O-okay."
    hide player
    hide jenny
    with dissolve
    return

label entrance_jenny_catch_her_leaving:
    show expression player.location.background_blur with None
    show player 5 at left
    show jenny b_casual a_phone f_grin_down at flip
    show jenny at Position (xpos=500)
    with dissolve
    pause
    show player 10
    player_name "Where are you going?"
    show player 5
    show jenny f_gross_down_talk
    jen "Out."
    show jenny f_grin_down
    show player 10
    player_name "Uhh, okay?"
    show player 5
    pause
    show player 12
    player_name "Care to elaborate?"
    show player 5
    show jenny f_gross_down_talk
    jen "Tch, I need to pick up some things from the mall..."
    show jenny f_grin_down
    pause
    show player 10
    player_name "What kind of things?"
    show player 5
    show jenny f_eyeroll
    jen "None of your business, loser!"
    jen "I don't know why you've always gotta have your nose in MY BUSINESS?!"
    show jenny f_gross_down
    pause
    show player 24
    show jenny f_angry_pouting_top
    pause
    hide jenny
    show jenny b_casual f_upset_talk
    with dissolve
    jen "How much money do you have?."
    show jenny f_upset
    show player 10
    player_name "Huh?"
    show player 5
    show jenny f_upset_talk
    jen "Give me two-hundred dollars."
    show jenny f_upset
    show player 12
    player_name "No way, I've given you tons of money already!"
    show player 5
    show jenny f_eyeroll
    jen "Psh! Yeah and you got stuff in return!"
    show jenny f_upset_talk
    jen "Don't act like I haven't been more than fair with you..."
    show jenny f_upset
    return

label entrance_jenny_catch_her_leaving_dom_first:
    show player 10
    player_name "Alright, so what do I get this time?"
    show player 5
    show jenny f_upset_talk
    jen "Tsk, you ain't getting shit."
    show jenny f_upset
    show player 12
    player_name "Fine."
    show player 12f with dissolve
    player_name "Have fun shopping."
    show player 90f
    show jenny f_upset_talk
    jen "W-wait!"
    show jenny f_upset
    show player 17 with dissolve
    pause
    show jenny f_angry_talk
    jen "Grr, damnit!"
    show jenny f_angry_pouting
    pause
    show jenny f_angry_talk
    jen "Why won't you just do what I fucking ask?!"
    show jenny f_angry
    show player 12
    player_name "Why don't you ever ask me nicely?"
    show player 5
    show jenny f_upset_talk
    jen "C'mon, {b}[firstname]{/b}! You owe me for that screw up with the toy the other day."
    show jenny f_upset
    show player 4 with dissolve
    player_name "( Man, screw her. She's lucky I bought her that toy at all... )"
    player_name "( ... Then again, this might be a good opportunity to learn more about what she's doing for that money. )"
    show jenny f_upset_talk
    jen "So are you gonna give me the money or not?"
    show jenny f_upset
    show player 12 with dissolve
    player_name "Yeah, I guess... If you say please."
    show player 5
    show jenny f_eyeroll
    jen "Ugh..."
    jen "Please?"
    show jenny f_angry_pouting_top
    return

label entrance_jenny_catch_her_leaving_sub_first:
    show player 26
    player_name "Y-yeah, okay but-"
    show player 11
    show jenny f_upset_talk
    jen "Quit being such a little bitch, {b}[firstname]{/b}!"
    jen "You make plenty of money."
    jen "Besides, you owe me for that little screw up with the toy the other day."
    show jenny f_upset
    show player 4 with dissolve
    player_name "( Ugh, I guess she's right about that... )"
    player_name "( ... And this might be a good opportunity to learn more about what she's doing for that money. )"
    show jenny f_upset_talk
    jen "Umm, hello?!"
    jen "Earth to loser!"
    show jenny f_upset
    show player 10 with dissolve
    player_name "{b}*Sigh*{/b} Fine."
    player_name "You said two-hundred?"
    show player 5
    show jenny f_grin_talk
    jen "Yup."
    show jenny f_grin
    return

label entrance_jenny_debbie_altercation:
    scene expression player.location.background_closeup with None
    show jenny f_upset_talk a_dressed_crossed
    show debbie 10bf zorder 1 at left
    jen "Why not?!"
    show jenny f_upset
    show debbie 11bf
    deb "Because I can't afford it!"
    deb "You're not a kid anymore {b}[jen_name]{/b}..."
    deb "If you want new clothes then you need to get yourself a job and buy them with your own money."
    show debbie 10bf
    show player 5 zorder 0 at Position (xpos=400)
    show jenny f_upset_talk
    jen "Ugh, how am I supposed to get a job when I have nothing nice to wear to the interview?!"
    show jenny f_upset
    show debbie 9bf with dissolve
    pause
    show debbie 11bf with dissolve
    deb "{b}[jen_name]{/b}, you have plenty of nice clothes..."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Not nice enough, not for the job I want..."
    show jenny f_upset
    show player 12
    player_name "What the heck kind of job are you trying to get?"
    show player 5
    show jenny f_eyeroll
    jen "I don't know, something with an office maybe?"
    show jenny f_upset
    show player 12
    player_name "Hah, Yeah right."
    player_name "I don't think many companies are looking for a college drop out with no qualifications and zero experience..."
    show player 90
    show jenny f_upset_talk
    jen "Shut up, turd!"
    jen "Who asked for your opinion?!"
    show jenny f_upset
    show player 11
    show debbie 11bf
    deb "Would you two cut it out?!"
    show jenny f_angry_pouting
    deb "I'm so sick of you fighting all time."
    show debbie 10bf
    show player 24
    player_name "Sorry, {b}[deb_name]{/b}."
    show player 5
    show debbie 11bf
    deb "{b}*Sigh*{/b} Just borrow something out of my closet, {b}[jen_name]{/b}."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Fine."
    show jenny f_upset
    pause
    show debbie 11bf
    deb "You should have never quit your job at {b}Consum-R{/b}..."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Psh, that job was lame!"
    show jenny f_upset
    show player 9 at Position (xoffset=41) with dissolve
    show debbie 11bf
    deb "Oh, grow up, {b}[jen_name]{/b}."
    deb "Do you think everyone enjoys what they do for a living?!"
    show debbie 10bf
    show jenny f_upset_talk
    jen "... No."
    show jenny f_upset
    show debbie 11bf
    deb "People do what they have to in order to put food on the table!"
    deb "I can't support you forever, you know?!"
    show debbie 10bf
    show player 5 with dissolve
    show jenny f_upset_talk
    jen "Oh, that's real nice {b}[deb_name]{/b}..."
    show jenny f_eyeroll
    jen "Sorry I'm such a HUGE burden on you guys!"
    show jenny f_upset
    show debbie 11bf
    deb "I never said that."
    show debbie 10bf
    show jenny f_upset_talk
    jen "You might has well have!"
    jen "Don't worry, you won't have to suffer me much longer."
    jen "The second I get a little money, I'm gone."
    show jenny f_angry_pouting_top
    show debbie 11bf
    deb "... Good grief."
    deb "Why do you always have to turn everything into a big drama?!"
    show debbie 10bf
    show jenny f_angry_pouting
    jen "..."
    show debbie 11bf
    deb "{b}*Sigh*{/b} You know I love you {b}[jen_name]{/b} and you're not a burden..."
    deb "I'm just saying you need to do something with your life."
    deb "You can't sit around on your ass forever, waiting the perfect opportunity to present itself."
    deb "You have to go out and make it happen."
    show debbie 10bf
    show jenny f_upset_talk
    jen "Yeah, yeah..."
    hide jenny with dissolve
    jen "God, I can't wait to leave this stupid town!"
    pause
    show debbie at center
    show player at left
    with dissolve
    deb "..."
    show debbie 11bf
    deb "Maybe I'm being too hard on her?"
    show debbie 10bf
    show player 10
    player_name "Eh, not really."
    player_name "I mean, I'm helping out around here and she's older than I am..."
    show player 5
    show debbie 11bf
    deb "I know."
    hide player
    show debbie 4b at left
    with dissolve
    deb "I really appreciate it, sweetie."
    deb "You're such a good boy."
    show debbie 4
    pause
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "Want me to fix you something to eat?"
    show debbie 1
    show player 14
    player_name "N-no, that's okay {b}[deb_name]{/b}..."
    player_name "I'm not really hungry."
    show player 13
    show debbie 2
    deb "Oh, alright."
    deb "Maybe I'll bake a pie..."
    deb "... Something to get my mind off all this drama."
    show debbie 1
    show player 17
    player_name "Heh, okay."
    show player 13
    hide debbie with dissolve
    pause
    show player 5
    player_name "( Poor {b}[deb_name]{/b}. )"
    player_name "( {b}[jen_name]{/b} doesn't realize how lucky she is... )"
    hide player with dissolve
    return

label entrance_diane_gave_birth_dialogue_seen:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 10 at left
    show debbie 1f at Position (xpos=600)
    show diane a_casual_baby b_casual at Position (xpos=625)
    show jenny f_grin at flip
    show jenny at Position (xpos=150)
    with dissolve
    player_name "{b}Diane{/b}?"
    show player 14
    player_name "You guys are finally home?"
    show player 13
    show diane f_normal_talk
    dia "Yup, we're home."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Isn't he just the most precious thing ever?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "I dunno, he kinda looks like a potato..."
        show jenny f_normal
        show debbie 2f
        deb "No he doesn't!"
        deb "He's so handsome!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Who's a handsome boy, huh?"
    elif M_diane.pregnancy.baby_gender == "twins":
        deb "Aren't they just the most precious things ever?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "I dunno, they kinda look like potatoes..."
        show jenny f_normal
        show debbie 2f
        deb "No they don't!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Who's beautiful, huh?"
    else:
        deb "Isn't she just the most precious thing ever?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "I dunno, she kinda looks like a potato..."
        show jenny f_normal
        show debbie 2f
        deb "No she doesn't!"
        deb "She's beautiful!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Who's a pretty girl, huh?"
    show debbie 1f
    show diane f_laugh
    dia "Hehe!"
    show diane f_normal
    show debbie 2f
    if M_diane.pregnancy.baby_gender == "twins":
        deb "I can't believe you finally have kids, {b}Diane{/b}."
    else:
        deb "I can't believe you finally have a child, {b}Diane{/b}."
    deb "I'm so happy for you!"
    show debbie 1f
    show diane f_normal_talk
    dia "I know, I didn't think I'd ever get to be a mommy."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "He's so adorable..."
        show jenny f_eyeroll
        show debbie 3f
        deb "I could just gobble him up!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "I should really get him down for the night."
        dia "He's had a busy day."
    elif M_diane.pregnancy.baby_gender == "twins":
        deb "They're so adorable..."
        show jenny f_eyeroll
        show debbie 3f
        deb "I could just gobble them up!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "I should really get them down for the night."
        dia "They've had a busy day."
    else:
        deb "She's so adorable..."
        show jenny f_eyeroll
        show debbie 3f
        deb "I could just gobble her up!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "I should really get her down for the night."
        dia "She's had a busy day."
    show diane f_down_front
    show debbie 2f
    deb "Aww, okay..."
    if M_diane.pregnancy.baby_gender == "twins":
        deb "Bye bye, little ones."
    else:
        deb "Bye bye, little one."
    show debbie 1f
    pause
    show debbie 1 at right
    show jenny at Position (xpos=200)
    hide diane
    with dissolve
    pause
    show debbie 3
    deb "Oh, I just love babies!"
    show debbie 1
    show jenny f_eyeroll
    jen "Ugh, whatever."
    show jenny f_upset_talk
    if M_diane.pregnancy.baby_gender == "twins":
        jen "If those thing are up all night screaming, I will absolutely lose my shit!"
    else:
        jen "If that thing is up all night screaming, I will absolutely lose my shit!"
    show jenny f_upset
    show debbie 13
    deb "{b}*Sigh*{/b}, {b}[jen_name]{/b}..."
    deb "Don't be like that, dear."
    show debbie 14b
    show jenny f_normal_talk
    jen "I'm just saying, I need my eight hours or I get cranky."
    show jenny f_normal
    show player 12
    player_name "You're always cranky..."
    show player 13 with None
    show jenny f_upset_talk at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    jen "What did you say?!"
    show jenny f_gross
    show player 10
    player_name "N-nothing."
    show player 5
    pause
    show jenny f_upset_talk
    jen "Uh huh."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "You better watch your mouth."
    jen "I know where you sleep."
    hide jenny with dissolve
    pause
    show player 12
    player_name "She's such a ray of sunshine..."
    show player 13
    show debbie 3
    deb "Hehehe!"
    show debbie 2
    deb "Oh, don't mind her."
    deb "She likes babies too, she just doesn't want to admit it."
    show debbie 1
    show player 12
    player_name "If you say so."
    hide player
    hide debbie
    hide diane
    with dissolve
    return

label entrance_diane_peeking:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 34 with dissolve
    pause
    show player 35
    player_name "Hmm, it sure is quiet in here tonight..."
    show player 10
    player_name "I wonder what {b}[deb_name]{/b} and {b}Diane{/b} are doing."
    show player 14
    player_name "{b}They're usually in the living room{/b} watching tv and having girl talk."
    player_name "{b}I should check on them.{/b}"
    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh zorder 1 at Position (xpos=625)
    with dissolve
    dia "Honey, we're home!"
    dia "Haha!"
    show player 17
    player_name "Haha!"
    show diane f_normal
    show debbie 2f zorder 0 with dissolve
    deb "What in the heck is going-"
    show debbie 3f
    show player 13
    deb "{b}*Gasp*{/b} You're here!"
    show debbie 2f
    show diane f_normal_talk
    dia "I'm here!"
    show diane f_normal_talk a_casual_bag_point with dissolve
    dia "Are we starting with a pajama party?"
    show diane f_normal a_casual_bag
    show debbie 222f
    with dissolve
    deb "Huh?"
    pause
    show debbie 3f with dissolve
    deb "Oh, shuddup."
    show debbie 1f
    show diane f_normal_talk
    dia "I'm serious, I brought my nightgown and everything!"
    show diane f_normal
    show debbie 2f
    deb "Are you hungry?"
    show debbie 1f
    show diane f_normal_talk
    dia "Oh, room service and everything."
    show diane f_smirk_talk
    dia "You didn't tell me it was gonna be so fancy..."
    show diane f_smirk
    show debbie 2f
    deb "Just get in here and I'll help you unpack."
    show debbie 1f
    show diane f_laugh
    dia "Yes, ma'am."
    show diane f_normal_talk
    dia "You wanna join us, {b}[firstname]{/b}?"
    show debbie 1 with dissolve
    show diane f_normal
    show player 55 with dissolve
    player_name "{b}*Yawn*{/b}"
    show player 26 with dissolve
    player_name "... Sure!"
    show player 25
    show debbie 2
    deb "Oh sweetie, you look exhausted!"
    deb "Why don't you just head on to bed and let {b}Diane{/b} and I spend some time together."
    show diane f_wink
    show debbie 1f with dissolve
    pause
    show diane f_smirk_talk
    dia "Mmm, time together, huh?"
    show diane f_smirk
    show debbie 3f
    deb "Oh, hush!"
    show diane f_laugh
    dia "Haha."
    show diane f_normal
    show debbie 1 with dissolve
    show player 26
    player_name "Yeah, okay."
    player_name "I am pretty tired."
    show player 25
    show diane f_smirk_talk
    dia "I guess it's just you and me then, beautiful."
    show diane f_smirk
    show debbie 3f with dissolve
    deb "Hehe, stop it!"
    show debbie 1f
    show diane f_smirk_talk
    dia "Good night, {b}[firstname]{/b}."
    show player 55
    hide debbie
    hide diane
    with dissolve
    pause
    hide player with dissolve
    return

label entrance_diane_debbie_drop_off_request:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show debbie 221 at right
    with dissolve
    deb "Hold on, {b}[firstname]{/b}."
    show debbie 220
    show player 14
    player_name "Hey, {b}[deb_name]{/b}."
    player_name "What's up?"
    show player 13
    show debbie 221
    deb "Did you do any work for {b}Diane{/b} today?"
    show debbie 220
    show player 14
    player_name "Yeah, I was over there earlier."
    show player 13
    show debbie 221
    deb "Is she doing alright?"
    show debbie 220
    show player 5
    player_name "Hmm?"
    show player 10
    player_name "Yeah, I guess..."
    show player 5
    show debbie 221
    deb "... Cause I just got off the phone with her and she sounds exhausted."
    show debbie 220
    show player 10
    player_name "Well, she is working herself really hard with that new business of hers."
    player_name "I told her to slow down but you know how passionate she is about it."
    show player 5
    show debbie 221
    deb "Yeah, she has a tendency to throw herself into her work and disregard her needs."
    deb "It worries me."
    deb "Would you mind heading back over there?"
    show debbie 220
    show player 10
    player_name "Tonight?"
    show player 5
    show debbie 221
    deb "Yeah, I want you to take her this pie I made today and make sure she eats it!"
    deb "She probably hasn't eaten a thing all day."
    show debbie 220
    show player 14
    player_name "Yeah, I can do that."
    show player 13
    show debbie 221
    deb "I would really appreciate it."
    show debbie 2
    show player 673
    with dissolve
    deb "Tell her she had better get a solid eight hours sleep too or it'll be me visiting her next!"
    show debbie 1
    show player 674
    player_name "Heh, alright."
    hide debbie
    hide player
    with dissolve
    return

label entrance_erik_bullying:
    scene expression L_home_entrance.background
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Is everything ok, {b}Mrs. Johnson{/b}?"
    show player 5
    show mrsj 19
    mrsjo "Sorry to disturb you this morning."
    show mrsj 52
    mrsjo "It's just... it's about {b}Erik{/b}."
    mrsjo "Has {b}Erik{/b} been having trouble lately at school?"
    show mrsj 19c
    show player 12
    player_name "Huh?"
    show player 35
    player_name "Not that I know of?"
    show player 10
    player_name "He usually does well at school..."
    show player 5
    show mrsj 20
    mrsjo "No. I'm not talking about grades."
    show mrsj 52
    mrsjo "Have the other kids in school been giving {b}Erik{/b} a hard time?"
    mrsjo "He's been asking to stay home instead of going to class."
    show mrsj 20
    mrsjo "I... I even saw him come home last week with bruises."
    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Erik{/b} is pretty quiet at school."
    player_name "I've never seen him get involved in any kind of bad stuff."
    show player 5
    show mrsj 19
    mrsjo "Maybe, if a close friend stopped over to him see him, he'd be more willing to talk..."
    show mrsj 19c
    show player 10
    player_name "You want me to ask him?"
    show player 5
    show mrsj 19
    mrsjo "I just want what's best for him, and you're his only friend."
    show mrsj 19c
    show player 12
    player_name "Okay. I'll go see him."
    hide mrsj
    hide player
    with dissolve
    return

label entrance_erik_bullying_3:
    scene expression L_home_entrance.background
    show mrsj 19c at Position (xpos=700)
    show debbie 13 at right
    with dissolve
    show player 5 at left with dissolve
    deb "Sweetie!! Are you okay?!"
    show debbie 14b
    show player 10
    player_name "I'm fine, {b}[deb_name]{/b}. The nurse said I just had a small concussion."
    show player 11
    show debbie 13
    deb "You had a concussion!"
    show debbie 14b
    show player 10
    player_name "Everything is fine. I'll be okay, {b}[deb_name]{/b}."
    show player 5
    show debbie 13
    deb "Your stupid school didn't even call to let me know you were in the hospital!"
    deb "I had to hear about it from {b}Tammy{/b}!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, it's alright. I'm really fine! Calm down."
    show player 11
    show debbie 13
    deb "I'm sorry... I was just so worried about you!"
    deb "Your {b}Father{/b} is counting on me to watch over you!"
    show debbie 14b
    show mrsj 19
    mrsjo "I'm so happy to see you're okay, {b}[firstname]{/b}."
    mrsjo "I came over here to fill {b}[deb_name]{/b} in the second {b}Erik{/b} called me."
    mrsjo "You did a good thing standing up for {b}Erik{/b}."
    show mrsj 38
    show debbie 13
    deb "Yes, it was really brave of you to stand up for your friend at school."
    deb "But, be please be careful!"
    show debbie 14b
    show player 24
    player_name "I know {b}[deb_name]{/b}..."
    show player 25
    player_name "I promise I'll try and stay out of trouble."
    show player 24
    show debbie 13
    deb "Come here."
    hide player
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at right
    show debbie 4
    with dissolve
    deb "I'm so glad you're safe."
    deb "{b}Your father{/b} would just throw a fit if he knew I let this happen."
    player_name "It's alright, {b}[deb_name]{/b}."
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at Position (xpos=700)
    show debbie 1 at right
    show player 13 at left
    with dissolve
    show mrsj 17
    mrsjo "Thanks again, {b}[firstname]{/b}."
    mrsjo "You're always welcome to stop over and visit."
    show mrsj 14
    show player 14
    player_name "It's fine. Just helping a friend."
    show player 13
    show mrsj 17
    mrsjo "Thank you."
    show mrsj 14
    show player 36 with dissolve
    player_name "Good night {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Good night."
    hide mrsj with dissolve
    show debbie 2
    deb "Now hurry up to bed and get some rest."
    hide player
    hide debbie
    with dissolve
    return

label entrance_mia_angelicas_impatience:
    scene expression L_home_entrance.background
    show debbie 1f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3
    with dissolve
    deb "There he is!"
    show debbie 1
    show player 22
    player_name "!!!" with hpunch
    show debbie 2
    deb "I'm so happy to hear {b}[firstname]{/b} visited our local church lately..."
    deb "... And offered volunteer work with the clergy!"
    show debbie 1
    show player 24
    player_name "Uhh..."
    show debbie 2
    deb "Well! I will leave you two to it, I have things cooking in the kitchen!"
    show debbie 2f with dissolve
    deb "It was great meeting you {b}Sister Angelica{/b}!"
    hide debbie with dissolve
    show player 12
    player_name "Volunteer work?"
    player_name "And why are you here?!"
    show player 11
    show ang 2
    ang "I thought we had an agreement?"
    show ang 1
    show player 24
    player_name "..."
    show ang 2
    ang "Did you think I would just let you slip away from me?!"
    show ang 1
    show player 10
    player_name "No, I just... What do you want from me?"
    show player 11
    show ang 2
    ang "The door of the church will be left unlocked at night."
    ang "Come visit me in my chamber and I will explain what I need from you..."
    ang "...And don't try to hide from me again, or else-"
    show ang 1
    show player 12
    player_name "Okay, okay!"
    player_name "Just don't say anything to my {b}landlady{/b}..."
    show player 11
    show ang 2
    ang "That will be up to you..."
    hide ang with dissolve
    show player 12
    player_name "Now I have to go see her at church? In the middle of the night?!"
    show player 10
    player_name "This is strange..."
    hide player with dissolve
    return

label entrance_mia_angelicas_home_visit:
    scene expression L_home_entrance.background with fade
    show debbie 2f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3f
    with dissolve
    deb "It's always a pleasure to hear that {b}[firstname]{/b} is actively involved with the church."
    deb "You two must be getting to know each other quite well."
    show debbie 1f
    show ang 2
    ang "Yes, {b}[firstname]{/b} has been very helpful bringing in remorsefully wretched sinners."
    ang "{b}God{/b} will surely remember his fruits of love to his neighbors."
    show ang 1
    show debbie 3f
    deb "That's great!"
    deb "I know we all can be naughty at times..."
    show debbie 2f
    deb "Well then, I'd better get going. The laundry isn't going to fold itself."
    hide debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "What now?"
    player_name "I brought you {b}Helen{/b}. Isn't that enough?"
    show player 5
    show ang 4
    ang "Oh no my dear child. {b}God{/b} has many things in store for you."
    ang "{b}Helen{/b} is far from being purified. Her stubbornness is most annoying."
    show ang 3
    show player 26
    player_name "Tell me about it."
    show player 5
    show ang 2
    ang "The most penitent Christians require extra care."
    ang "They need to be broken down from their pedestal so that we may build them back up."
    ang "I believe it will take two more rituals for her..."
    ang "That is why I have come to see you."
    ang "I am in need of an essential tool used throughout biblical times."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "What do you need?"
    show player 5
    show ang 2
    ang "I intend to subvert {b}Helen{/b} through the means of flagellation."
    show ang 1
    show player 12
    player_name "What?"
    show player 5
    show ang 4
    ang "Get me {b}a whip{/b}."
    show ang 3
    show player 23
    player_name "{b}A whip{/b}!?"
    show player 11
    show ang 4
    ang "I'd prefer a cat o' nine tails of which our {b}Savior{/b} was subjected to."
    ang "But I fear that might be more difficult to come by."
    ang "{b}A standard leather whip{/b} will do."
    show ang 2
    ang "Bring it to me in my chambers."
    show ang 1
    show player 10
    player_name "This doesn't seem right at-"
    show player 11
    show ang 2
    ang "Do you forget your place? Don't make me remind you and everyone else of your depraved sins!"
    show ang 1
    show player 15
    player_name "But you want to whip {b}Helen{/b}!"
    show player 16
    show ang 2
    ang "You made a deal with me. Don't question my...the church's methods."
    show ang 1
    show player 12
    player_name "It's just not right."
    show player 5
    show ang 4
    ang "And who are you to judge right from wrong?"
    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Fine. Where am I even supposed to get {b}a whip{/b} though?"
    show player 17
    player_name "Is there a listing of distributors in the back of the bible?"
    show player 5
    show ang 1
    ang "..."
    show ang 2
    ang "I'm sure someone of your age knows of dirty lustful places that sell such things."
    ang "Don't keep me waiting."
    hide ang with dissolve
    show player 37 with dissolve
    player_name "I should never have gone to church."
    pause
    show player 38 with dissolve
    player_name "Where am I going to get {b}a whip{/b}?"
    player_name "Maybe the {b}Pink store at the mall{/b} carries something like that."
    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    ang "It's about time you came downstairs."
    ang "I have need of you again."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "I'm not sure I want to continue helping after what you did to {b}Helen{/b}, I-"
    show player 5
    show ang 4
    ang "Oh, don't be so naive!"
    ang "Despite her reluctance, we both know she enjoyed it."
    show ang 3
    show player 11
    player_name "..."
    show ang 2
    ang "I didn't come here to argue with a sinner."
    show ang 39 with dissolve
    ang "If you truly intend to help {b}Helen{/b} you will help me obtain this..."
    show ang 38
    pause
    show ang 3
    show player 459 at Position (xoffset=1)
    with dissolve
    player_name "..."
    hide player
    hide ang
    show note_01_c
    with dissolve
    pause
    hide note_01_c
    show player 1 at left
    show ang 3 at right
    show player 460 at Position (xoffset=1)
    with dissolve
    player_name "What...is it?"
    show player 461 at Position (xoffset=1)
    show ang 4
    ang "It is a crucial element to the final ritual of {b}Helen's{/b} purification..."
    ang "...And your last task."
    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "But how is this going to be used to purify {b}Helen{/b}?"
    show player 11 with dissolve
    show ang 2
    ang "Don't question me!"
    ang "Sinners should just accept the words spoken by {b}God's{/b} chosen."
    ang "Now get me the item in the photograph and meet me in my chambers."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Alright..."
    show player 5
    show ang 2
    ang "Good. And be quick about it."
    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Helen{/b} doesn't even seem to realize {b}Sister Angelica{/b} is transforming her into..."
    player_name "...A sex freak!"
    show player 12
    player_name "I should talk with {b}Harold{/b} before I help out {b}Sister Angelica{/b}."
    player_name "Maybe he can help me figure out what to do."
    show unlock55 at truecenter with dissolve
    $ player.get_item("strapon_drawing")
    pause
    hide unlock55 with dissolve
    hide player with dissolve
    return

label entrance_mom_overheard:
    scene expression game.timer.image("home_entrance{}")
    show player 34 with dissolve
    player_name "...{b}*distant voice*{/b}..."
    show player 35
    player_name "( Is that {b}[deb_name]{/b} on the phone? )"
    show player 12
    player_name "( ...She sounds like she's mad. Is she yelling? )"
    show player 10
    player_name "( I should go see if she's okay. )"
    hide player with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        deb "Good morning, sweetie."
    else:
        deb "Hello, sweetie."
    show debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Morning, {b}[deb_name]{/b}."
    else:
        player_name "Hello, {b}[deb_name]{/b}."
    show player 1
    show debbie 2
    if game.timer.is_morning():
        deb "Ready for school?"
    else:
        deb "Happy to be back at school?"
    show debbie 1
    show player 10
    player_name "Yeah, I guess. I have so much homework to catch up on."
    show player 1
    show debbie 3
    deb "Oh, I'm sure you'll do fine."
    show debbie 2
    deb "It's good to get back into a normal routine."
    show debbie 1
    show player 14
    player_name "I guess."
    player_name "What are you doing today?"
    show player 13
    show debbie 13
    deb "Oh, me?"
    deb "Housework mostly. It keeps me pretty busy."
    deb "It's not easy taking care of this big place by myself you know?"
    show debbie 14b
    show player 5
    pause
    show player 2
    player_name "I could help, you know?"
    show player 1
    show debbie 13
    deb "You want to help with the house work?"
    show debbie 1
    show player 29 with dissolve
    player_name "Sure! I mean, I feel like I should pull my own weight around here..."
    show player 1 with dissolve
    show debbie 2
    deb "That's a great attitude to have, {b}[firstname]{/b}!"
    show debbie 1
    deb "Hmm..."
    show debbie 2
    deb "Well, the lawn hasn't been mowed in weeks."
    deb "You can start there if you want!"
    deb "The {b}lawn mower{/b} should be in the {b}garage{/b}."
    show debbie 1
    show player 14
    player_name "All right. I'll go take a look."
    show player 13
    show debbie 2
    deb "Thanks, {b}[firstname]{/b}."
    deb "Be careful!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_clothes_dirty:
    scene expression L_home_entrance.background
    show player 11 zorder 1 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show jenny f_gross_talk
    with dissolve
    jen "Eugh, what's that smell?!"
    show player 14
    show jenny f_gross
    player_name "... Me I think. I was outside mowing the law-"
    show player 11
    show jenny f_gross_talk
    jen "That's disgusting! You're getting grass everywhere, you slob!"
    show player 12
    show jenny f_gross
    player_name "I'm sorry. I was just trying to help {b}[deb_name]{/b}."
    show player 11
    show jenny f_upset_talk
    jen "So what, you're going to start doing chores around here now?"
    show jenny f_grin_talk a_dressed_crossed with dissolve
    jen "You got a thing for {b}[deb_name]{/b} or something?"
    show player 10
    show jenny f_grin
    player_name "No! I'm just-"
    show player 11
    show jenny f_eyeroll
    jen "Pfft, don't play dumb! I see what you're up to!"
    hide jenny with dissolve
    pause
    show player 12
    player_name "What's her problem?"
    show player 10
    player_name "Oh well, I should get these clothes {b}downstairs to the wash{/b}."
    hide player with dissolve
    return

label entrance_mom_debt_collectors:
    scene henchman_cs1 2 with fade
    show text "I was expecting to see {b}Erik{/b}, instead I saw a strange man...\nHe was wearing an all black suit coupled with a stern look that would put coach Bridget's to shame." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene henchman_cs1 1
    show player 2 at left
    show henchman2 1 at right
    with dissolve
    player_name "Hi?"
    show henchman2 2
    show player 1
    henchman2 "Where's the owner of this residence?"
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Who's asking?"
    show player 11
    show henchman2 3
    henchman2 "It's personal matters, Kid."
    show henchman2 1
    show player 12
    player_name "Well, she's kind of busy at the moment, so why don't you come another time."
    show henchman2 2
    show player 11
    henchman2 "No need. Just give her this message."
    show henchman2 3
    henchman2 "She's running out of time. She better pay up or else!"
    henchman2 "My boss ain't the patient type."
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Or else, what?"
    show player 11
    show henchman2 3
    henchman2 "Just give her the message, Kid."
    henchman2 "We'll be back soon..."
    show henchman2 1
    player_name "..."
    $ playMusic()
    hide henchman2
    with dissolve
    scene expression L_home_entrance.background
    show player 10 at left
    with fade
    player_name "( What was {b}that{/b} all about... )"
    show player 5
    show debbie 62 at right with dissolve
    deb "Was someone at the door, sweetie?"
    show player 10
    show debbie 61
    player_name "Yeah, some strange guy in a black suit came by..."
    show player 5
    show debbie 59
    deb "!!!"
    show player 11
    show debbie 60
    deb "...What did he want?"
    show debbie 59
    show player 10
    player_name "He said you need to pay up and that he'll be back soon, but refused to say why."
    show player 11
    show debbie 60
    deb "It must be about..."
    deb "But I already paid off all the-"
    show debbie 59
    deb "..."
    show player 10
    player_name "What is it?"
    show player 11
    show debbie 60
    deb "It's nothing, sweetie."
    show player 1
    show debbie 62
    deb "They must've gotten the wrong address, that's all."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background
    show player 11 at left
    show debbie 13 at right
    with dissolve
    deb "Sweetie! Thank God you're here!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} and I need your help."
    show debbie 14b
    show player 12
    player_name "Huh?"
    show player 5
    show debbie 13
    deb "There's a broken pipe upstairs and water everywhere!"
    deb "She's up there messing with it now."
    deb "Could you go and help her?"
    show debbie 14b
    show player 10
    player_name "Me? I err..."
    show player 5
    show debbie 13
    deb "I can't afford to call a repairman right now. Not with everything that's happened recently..."
    show debbie 14b
    show player 10
    player_name "Oh, right..."
    show player 14
    player_name "I'll go take a look."
    show player 13
    show debbie 2
    deb "Thanks, sweetie! Let me know if there's anything I can do to help."
    show debbie 1
    show player 14
    player_name "Alright."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene location_home_entrance_night_blur
    show player 1 at left
    show debbie 62 at right
    deb "Oh, hey, sweetie!"
    deb "Heading to bed?"
    show player 2
    show debbie 61
    player_name "Nah, just looking around for something to do..."
    show player 14
    player_name "Why, what are you up to?"
    show player 1
    show debbie 62
    deb "I was just thinking about starting a movie."
    show player 2
    show debbie 61
    player_name "Cool."
    show player 1
    deb "..."
    show debbie 63
    deb "Why don't you come join me?"
    show player 10
    show debbie 61
    player_name "Really?"
    show player 11
    show debbie 62
    deb "Sure, why not? It's still early and I would love the company!"
    show player 2
    show debbie 61
    player_name "Y-yeah, okay. That sounds nice, {b}[deb_name]{/b}."
    show player 1
    show debbie 62
    deb "Great!"
    deb "I'll go get situated and you just come join me when you're ready, alright?"
    show player 2
    show debbie 61
    player_name "Sounds good!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene location_home_entrance_day_blur
    show player 1 at left with dissolve
    show debbie 165 at right with dissolve
    deb "Hey there, Sweetheart!"
    show player 2
    show debbie 164
    player_name "Hey {b}[deb_name]{/b}!"
    player_name "You look nice! Going somewhere?"
    show player 1
    show debbie 165
    deb "Oh, I just need to run to the {b}Mall{/b} and pick up a few things."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Would you like to join me?"
    show player 11
    show debbie 164
    player_name "Hmm?"
    show player 10
    player_name "Oh I dunno, I was gonna-"
    show player 11
    show debbie 165
    deb "Aww, c'mon! It'll do you good to get some fresh air."
    show debbie 164
    player_name "..."
    show debbie 165
    deb "... And besides, I don't want to go all by myself..."
    deb "Won't you come and keep me company?"
    show debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Heh, sheesh {b}[deb_name]{/b}! Alright, I'll go."
    show player 1
    show debbie 166
    deb "Great!"
    show debbie 165
    deb "I'll meet you in the car then, sweetie!"
    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Sorry {b}[deb_name]{/b}, I have something else planned for today..."
    show player 11
    show debbie 168
    deb "Oh."
    show debbie 169
    deb "..."
    show debbie 168
    deb "Okay, sweetie, well... Just stay safe and be home for dinner."
    show player 2
    show debbie 169
    player_name "Sure thing."
    return

label entrance_mom_spy:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Huh?"
    player_name "What was that noise?"
    show player 11
    pause
    show player 10
    player_name "Maybe the TV is on in the living room."
    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background
    show player 4 with dissolve
    player_name "I wonder if {b}[deb_name]{/b} would let me kiss her again if I asked?"
    player_name "I should {b}talk to her{/b} about it..."
    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression L_home_entrance.background
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Good morning, sweetie."
    show debbie 1
    show player 14
    player_name "Morning, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Did you sleep well last night?"
    show debbie 1
    show player 10
    player_name "...Yeah... sorta."
    player_name "I've been having a lot of weird dreams lately."
    show player 11
    show debbie 2
    deb "Is that so? What kind of weird dreams?"
    show debbie 1
    show player 10
    player_name "Oh, umm..."
    player_name "Well, it's kinda embarrassing."
    show player 11
    show debbie 2
    deb "... Naughty dreams?"
    show debbie 1
    show player 10
    player_name "Err... Yeah."
    show player 11
    show debbie 2
    deb "Well that's nothing to be embarrassed about, Sweetheart!"
    show debbie 3
    deb "You're at that age after all."
    show debbie 1
    pause
    show debbie 2
    deb "So who's the lucky girl?"
    show player 10
    show debbie 1
    player_name "The girl?"
    player_name "Umm, I don't really wanna talk about it..."
    show player 11
    show debbie 3
    deb "Hehe, Oh? I wonder if it's somebody I would know?"
    show player 11
    player_name "..."
    show debbie 3
    deb "Oh, fine. Keep your secrets!"
    show debbie 2
    deb "While you're here, I need your help with something. Got a minute?"
    show debbie 14
    show player 10
    player_name "Uh... Yeah. What is it?"
    show player 1
    show debbie 13
    deb "Can you look at the car and see why it's not starting?"
    show debbie 1
    show player 10
    player_name "Didn't we just take it out the other day?"
    show player 1
    show debbie 13
    deb "Yeah but for some reason I can't get it started now!"
    show debbie 1
    show player 2
    player_name "You didn't leave the lights on and kill the battery again, did you?"
    show debbie 2
    show player 1
    deb "Hah, no... I mean, well... I don't think I did. Would you mind checking?"
    show debbie 1
    show player 14
    player_name "Not at all!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background
    show player 1
    player_name "( I can't believe {b}[deb_name]{/b} actually rubbed my Cock! )"
    player_name "( ... a couple more seconds and I would have popped. )"
    player_name "( Arrgh, I want her so bad! This is torture! )"
    show player 11
    player_name "( .... )"
    player_name "( Hmm, I know I promised not to jerk off in her room but... )"
    show player 13
    player_name "( It just felt so good last time! )"
    player_name "( ... )"
    player_name "( Maybe if I do it quickly and quietly, I can snag a pair of her panties and bust a nut without her noticing. )"
    player_name "( She seems to be {b}busy in the [temp]{/b} which should allow me to sneak into her room and rub one out in her bed. )"
    player_name "( I think it's worth a shot... I need the release... To clear my head! )"
    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background
    show player 34 with dissolve
    player_name "...{b}*distant voice*{/b}..."
    show player 35
    player_name "( Hmm, sounds like {b}[deb_name]{/b} is talking to someone in the kitchen... )"
    show player 12
    player_name "( I wonder who's here? )"
    show player 10
    player_name "( I should go take a look... )"
    hide player with dissolve
    return

label entrance_mom_vacuum:
    scene location_home_entrance_fight
    show debbie 94 at right with dissolve
    pause
    show debbie 95
    pause
    show debbie 94
    pause
    show debbie 95
    pause
    show debbie 94
    show player 1 at left with dissolve
    pause
    show debbie 95
    pause
    show debbie 97 with dissolve
    deb "Oh!!"
    deb "You startled me..."
    show debbie 98
    show player 17
    player_name "Sorry, {b}[deb_name]{/b}."
    show player 14
    player_name "I didn't mean to!"
    show debbie 97
    show player 1
    deb "Sorry about the noise."
    deb "I should be done with the vacuum soon."
    deb "... Ugh, this is killing my back!"
    show debbie 98
    return

label entrance_mom_vacuum_yes:
    show debbie 98 at right
    show player 14 at left
    player_name "Here, {b}[deb_name]{/b}, pass me the vacuum."
    show player 1
    show debbie 96
    deb "..."
    show debbie 97
    deb "You want the vacuum?"
    show debbie 96
    show player 14
    player_name "Yeah, I'll take over from here."
    player_name "You should rest your back for a bit..."
    show player 10
    player_name "No sense in working yourself so hard when I'm here to help."
    show debbie 97
    show player 11
    deb "No, it's okay, sweetie. You don't have-"
    show debbie 98
    show player 10
    player_name "I know I don't have to help, {b}[deb_name]{/b}."
    player_name "I want to do it."
    show debbie 97
    show player 1
    deb "Well, if you insist..."
    show player 257
    show debbie 100
    with dissolve
    deb "This is very sweet of you."
    show player 259
    show debbie 99
    player_name "Not a problem!"
    hide player
    hide debbie
    with dissolve
    scene expression "backgrounds/location_home_cutscene02.jpg"
    show expression FilteredText("I felt bad {b}[deb_name]{/b} was having a hard time with her back pain. \nThe least I could do was help her out, even if it took me forever to finish. \nThe stairs were the worst part! No wonder her back is hurting her... \nAt least {b}[deb_name]{/b} kept me company while I worked.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label entrance_mom_vacuum_no:
    show debbie 96 at right
    show player 10 at left
    player_name "Can you please finish cleaning another time?"
    player_name "I'm trying to study upstairs and all this noise is distracting."
    show debbie 97
    show player 11
    deb "I'm sorry, sweetie!"
    deb "I had no idea you were upstairs studying."
    show debbie 96
    show player 14
    player_name "It's okay, {b}[deb_name]{/b}."
    show debbie 97
    show player 1
    deb "It'll be good to rest my back for a bit anyways..."
    show debbie 96
    show player 17
    player_name "Thanks!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( What's that sound? )"
    player_name "( It sounds like the TV is on. )"
    show player 4 at Position(xpos=518)
    player_name "( Who could be watching TV this late? )"
    hide player with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background
    show player 26 with dissolve
    player_name "( That porno {b}[jen_name]{/b} was watching was hot! I kind of feel like watching it, too... )"
    show player 33
    player_name "Hmm... Maybe {b}another night{/b}."
    hide player with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( What was that sound? )"
    hide player with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Sweetie, somebody is at the door! Can you get it?"
    show debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Duh. What do you think I'm here to see you or something?!"
    show roxxy 1
    show player 21
    player_name "... No."
    show player 5
    show roxxy 2
    rox "Good, cause there is no fucking way-"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Ahem*"
    show jenny f_grin_talk
    jen "Is this that girl you wanted me to help?"
    jen "You know, the one you're trying to bang?"
    show jenny f_grin
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 3
    rox "EXCUSE ME!?"
    show roxxy 14
    show player 113
    player_name "N-no!!"
    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"
    show player 11
    show roxxy 2
    rox "As if you even have a shot... Not even in your dreams, Twerp!"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_grin_talk
    jen "Aww, too bad little pervert."
    jen "I guess you're stuck with your hand and a bottle of lotion."
    show jenny f_grin
    show roxxy 4
    rox "Hah! Yeah, and I feel sorry for the lotion..."
    show roxxy 1
    show jenny f_laugh a_dressed_hips with dissolve
    jen "Hahaha! Oh, I like you! {b}Roxxy{/b} was it?"
    show jenny f_grin
    show roxxy 1b
    rox "Yeah, and you're {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny f_grin_talk
    jen "That's right."
    jen "C'mon, {b}Roxxy{/b}. We can ditch the dweeb and get started in my room."
    show jenny f_grin
    show roxxy 1b
    rox "Gladly."
    show roxxy 2
    rox "See ya, dweeb!"
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."
    hide player
    hide debbie
    with dissolve

    scene location_home_entrance_cutscene04
    with fade
    show text "Those two had formed a connection almost instantly...\nI guess {b}[jen_name]{/b} and {b}Roxxy{/b} did have a lot in common." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "They were both Captains of the cheer squad, popular, beautiful,\nand both of them had mastered the art of being a bitch..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "I really hope I don't end up regretting this..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Who was that?"
    show debbie 14
    show player 10
    player_name "Just a girl from my school. {b}[jen_name]{/b} agreed to help her with some cheer-leading stuff."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} is helping somebody?"
    show debbie 3
    deb "That's a new one."
    show debbie 1
    show player 12
    player_name "Yeah, because I paid her..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."
    show debbie 14
    show player 12
    player_name "Yeah, I know."
    show player 90
    player_name "..."
    show debbie 13
    deb "Something else on your mind?"
    show debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."
    show player 10
    player_name "Kinda freaks me out, to be honest."
    show player 5
    show debbie 2
    deb "Well, I think it's a good thing she's made a new friend."
    deb "I worry about her sitting upstairs by herself all day..."
    show debbie 13
    deb "I'm sure she gets lonely."
    show debbie 14
    show player 10
    player_name "I doubt it."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Maybe I should go check on them{/b}?"
    show player 5
    show debbie 2
    deb "Maybe."
    show debbie 13
    deb "...Just be careful, sweetie."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Sweetie, somebody is at the door! Can you get it?"
    show debbie 1
    show player 14
    player_name "Sure thing, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Hey {b}Roxxy{/b}! You here for your session with {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Yup. It's still on, right?"
    show roxxy 1
    show player 21
    player_name "Absolutely."
    show player 5
    show roxxy 2
    rox "Awesome! I'm so excited to-"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Ahem*"
    show jenny f_grin_talk
    jen "Is this that girl you wanted me to help?"
    jen "You know, the one you're trying to bang?"
    show jenny f_grin
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 4
    rox "... Hahaha!"
    show roxxy 14
    show player 113
    player_name "I didn't-"
    show player 10
    player_name "{b}Roxxy{/b}, I swear I never said-"
    show player 11
    show roxxy 1h
    rox "What exactly have you been telling them, {b}[firstname]{/b}?"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_surprised
    jen "Wait a second..."
    jen "You mean, you... A-and him?!"
    show jenny f_sad
    show roxxy 4
    rox "Uhh yeah?!"
    rox "So long as he keep taking good care of me..."
    show jenny f_grin
    rox "... And doesn't get fat or lose his hair, yuck!"
    show roxxy 1
    show jenny f_laugh
    jen "Hahaha! Oh, I like you! {b}Roxxy{/b} was it?"
    show jenny f_grin
    show roxxy 1b
    rox "Yeah, and you're {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny f_grin_talk
    jen "That's right."
    jen "C'mon, {b}Roxxy{/b}. We'll do this in my room."
    show jenny f_grin
    show roxxy 1b
    rox "Alright."
    show roxxy 2
    rox "Thanks again, {b}[firstname]{/b}."
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "I have a bad feeling about this."
    hide player
    hide debbie
    with dissolve
    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "So you two are dating now?"
    show debbie 14
    show player 10
    player_name "Heh, yeah. {b}[jen_name]{/b} agreed to help her with some cheer-leading stuff."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} is helping somebody?"
    show debbie 3
    deb "That's a new one."
    show debbie 1
    show player 12
    player_name "Yeah, because I paid her..."
    show player 90
    show debbie 13
    deb "Ah."
    deb "Sweetie, you really shouldn't let {b}[jen_name]{/b} take advantage of you like that..."
    show debbie 14
    show player 12
    player_name "Yeah, I know."
    show player 90
    player_name "..."
    show debbie 13
    deb "Something else on your mind?"
    show debbie 14
    show player 12
    player_name "I've just never seen {b}[jen_name]{/b} hit it off with someone like that..."
    show player 10
    player_name "Kinda freaks me out, to be honest."
    show player 5
    show debbie 2
    deb "Well, I think it's a good thing she's made a new friend."
    deb "I worry about her sitting upstairs by herself all day..."
    show debbie 13
    deb "I'm sure she gets lonely."
    show debbie 14
    show player 10
    player_name "I doubt it."
    show player 5
    player_name "..."
    show player 11
    jen "Hahahaha!!"
    show player 10
    player_name "...{b}Maybe I should go check on them{/b}?"
    show player 5
    show debbie 2
    deb "Maybe."
    show debbie 13
    deb "...Just be careful, sweetie."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "I should go check on {b}Roxxy{/b} and {b}[jen_name]{/b}..."
    hide player with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 34 with dissolve
    player_name "( Hmm? )"
    player_name "( Is that {b}Diane{/b}? )"
    player_name "( {b}[deb_name]{/b} must have invited her over. )"
    player_name "( {b}I wonder what they're talking about?{/b} )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
