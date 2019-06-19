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
    player_name "{b}Диана{/b}?"
    show player 14
    player_name "Вы наконец-то дома?"
    show player 13
    show diane f_normal_talk
    dia "Да, мы вернулись домой."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Разве он не самая драгоценная вещь на свете?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Не знаю, он похож на картофелину..."
        show jenny f_normal
        show debbie 2f
        deb "Нет, это не так!"
        deb "Он такой красивый!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Кто у нас красивый мальчик, а?"
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
        deb "Разве она не самая драгоценная вещь на свете?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Не знаю, она похожа на картофелину..."
        show jenny f_normal
        show debbie 2f
        deb "Нет, это не так!"
        deb "Она прекрасна!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Кто у нас красивая девочка, а?"
    show debbie 1f
    show diane f_laugh
    dia "Хехе!"
    show diane f_normal
    show debbie 2f
    if M_diane.pregnancy.baby_gender == "twins":
        deb "I can't believe you finally have kids, {b}Diane{/b}."
    else:
        deb "I can't believe you finally have a child, {b}Diane{/b}."
	deb "Я так счастлива за тебя!"
    show debbie 1f
    show diane f_normal_talk
    dia "Я знаю, я не думала, что когда-нибудь стану мамой."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Он такой очаровательный..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Я могу просто слопать его!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Мне действительно нужно уложить его спать."
        dia "У него был напряженный день."
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
        deb "Она такая очаровательная..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Я могу просто слопать ее!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Мне действительно нужно уложить ее спать."
        dia "У нее был напряженный день."
    show diane f_down_front
    show debbie 2f
    deb "Ау, хорошо..."
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
    deb "О, я просто обожаю детей!"
    show debbie 1
    show jenny f_eyeroll
    jen "Уф, неважно."
    show jenny f_upset_talk
    if M_diane.pregnancy.baby_gender == "twins":
        jen "If those thing are up all night screaming, I will absolutely lose my shit!"
    else:
        jen "If that thing is up all night screaming, I will absolutely lose my shit!"
	show jenny f_upset
    show debbie 13
    deb "{b}*вздыхая*{/b}, {b}[jen_name]{/b}..."
    deb "Не будь такой, дорогая."
    show debbie 14b
    show jenny f_normal_talk
    jen "Я просто говорю, что мне нужны мои восемь часов для сна или я разозлюсь."
    show jenny f_normal
    show player 12
    player_name "Ты всегда капризничаешь..."
    show player 13 with None
    show jenny f_upset_talk at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    jen "Что ты сказал?!"
    show jenny f_gross
    show player 10
    player_name "Ничего."
    show player 5
    pause
    show jenny f_upset_talk
    jen "Угу."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "Лучше следи за своим языком."
    jen "Я знаю, где ты спишь."
    hide jenny with dissolve
    pause
    show player 12
    player_name "Она как солнечный лучик..."
    show player 13
    show debbie 3
    deb "Хехехе!"
    show debbie 2
    deb "Не обращайте на нее внимания."
    deb "Она тоже любит детей, просто не хочет этого признавать."
    show debbie 1
    show player 12
    player_name "Как скажешь."
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
    player_name "Хм, сегодня здесь тихо ..."
    show player 10
    player_name "Интересно, что {b}[deb_name]{/b} и {b}Даина{/b} делают."
    show player 14
    player_name "{b}Они обычно в гостиной{/b} смотрят телевизор и болтают."
    player_name "{b}Я должен проверить их.{/b}"
    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh zorder 1 at Position (xpos=625)
    with dissolve
    dia "Дорогая, мы вернулись домой!"
    dia "Хаха!"
    show player 17
    player_name "Хаха!"
    show diane f_normal
    show debbie 2f zorder 0 with dissolve
    deb "Что, черт возьми, происходит-"
    show debbie 3f
    show player 13
    deb "{b}*вздох*{/b} Ты здесь!"
    show debbie 2f
    show diane f_normal_talk
    dia "Я здесь!!"
    show diane f_normal_talk a_casual_bag_point with dissolve
    dia "Мы начинаем с пижамной вечеринки?"
    show diane f_normal a_casual_bag
    show debbie 222f
    with dissolve
    deb "Ааа?"
    pause
    show debbie 3f with dissolve
    deb "О, да ладно."
    show debbie 1f
    show diane f_normal_talk
    dia "Я серьезно, я принесла свою ночную рубашку и все такое!"
    show diane f_normal
    show debbie 2f
    deb "Ты голодная?"
    show debbie 1f
    show diane f_normal_talk
    dia "О, обслуживание номеров и все такое."
    show diane f_smirk_talk
    dia "Ты не говорила мне, что это будет так чудно..."
    show diane f_smirk
    show debbie 2f
    deb "Просто иди сюда, Я помогу тебе распаковать вещи."
    show debbie 1f
    show diane f_laugh
    dia "Да, мэм."
    show diane f_normal_talk
    dia "Ты хочешь присоединиться к нам, {b}[firstname]{/b}?"
    show debbie 1 with dissolve
    show diane f_normal
    show player 55 with dissolve
    player_name "{b}*зевая*{/b}"
    show player 26 with dissolve
    player_name "... Конечно!"
    show player 25
    show debbie 2
    deb "Милый, ты выглядишь уставшей!"
    deb "Почему бы тебе просто не пойти в кровать и позволить нам с {b}Дианой{/b} провести некоторое время вместе."
    show diane f_wink
    show debbie 1f with dissolve
    pause
    show diane f_smirk_talk
    dia "Ммм, время вместе, хух?"
    show diane f_smirk
    show debbie 3f
    deb "О, тише!"
    show diane f_laugh
    dia "Хаха."
    show diane f_normal
    show debbie 1 with dissolve
    show player 26
    player_name "Да, хорошо."
    player_name "Я довольно сильно устал."
    show player 25
    show diane f_smirk_talk
    dia "Думаю, тогда остались только ты и я, красавица."
    show diane f_smirk
    show debbie 3f with dissolve
    deb "Хе-хе, прекрати!"
    show debbie 1f
    show diane f_smirk_talk
    dia "Спокойной ночи, {b}[firstname]{/b}."
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
    deb "Подожди, {b}[firstname]{/b}."
    show debbie 220
    show player 14
    player_name "Привет, {b}[deb_name]{/b}."
    player_name "Что случилось?"
    show player 13
    show debbie 221
    deb "Ты сегодня работал у {b}Дианы{/b}?"
    show debbie 220
    show player 14
    player_name "Да, я уже был там."
    show player 13
    show debbie 221
    deb "С ней все в порядке?"
    show debbie 220
    show player 5
    player_name "Хмм?"
    show player 10
    player_name "Да, наверное..."
    show player 5
    show debbie 221
    deb "... Потому что я только что говорила с ней по телефону, и она кажется измученной."
    show debbie 220
    show player 10
    player_name "Ну, она очень усердно работает над своим новым бизнесом."
    player_name "Я сказал ей притормозить, но ты же знаешь, как она страстно к этому относится."
    show player 5
    show debbie 221
    deb "Да, у нее есть склонность бросаться на работу и игнорировать свои потребности."
    deb "Это меня беспокоит."
    deb "Мог бы ты вернуться туда?"
    show debbie 220
    show player 10
    player_name "Сегодня вечером?"
    show player 5
    show debbie 221
    deb "Да, я хочу, чтобы ты взял пирог, который я сегодня испекла, и убедился, что она его съест!"
    deb "Она, наверное, ничего не ела весь день."
    show debbie 220
    show player 14
    player_name "Да, я могу это сделать."
    show player 13
    show debbie 221
    deb "Я была бы очень признательна."
    show debbie 2
    show player 673
    with dissolve
    deb "Скажи ей, что ей тоже лучше поспать восемь часов, иначе я приду к ней в гости!"
    show debbie 1
    show player 674
    player_name "Хех, хорошо."
    hide debbie
    hide player
    with dissolve
    return

label entrance_erik_bullying:
    scene expression L_home_entrance.background
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Все хорошо, {b}Миссис Джонсон{/b}?"
    show player 5
    show mrsj 19
    mrsjo "Извени что беспокою тебя утром."
    show mrsj 52
    mrsjo "Просто...это насчет {b}Эрика{/b}."
    mrsjo "У {b}Эрика{/b} были проблемы в последнее время в школе?"
    show mrsj 19c
    show player 12
    player_name "Эээ?"
    show player 35
    player_name "Насколько мне известно, нет."
    show player 10
    player_name "Он обычно хорошо учится в школе..."
    show player 5
    show mrsj 20
    mrsjo "Нет. Я не говорю об уроках."
    show mrsj 52
    mrsjo "Другие дети в школе доставляли {b}Эрикe{/b} много хлопот?"
    mrsjo "Он попросил остаться дома вместо того, чтобы идти на занятия."
    show mrsj 20
    mrsjo "Я... Я даже видела, как он пришел домой на прошлой неделе с синяками."
    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Эрик{/b} ведет себя в школе довольно тихо."
    player_name "Я никогда не видел, чтобы он участвовал в каких-то плохих делах."
    show player 5
    show mrsj 19
    mrsjo "Может быть, если бы близкий друг спросил его, он был бы готов поговорить..."
    show mrsj 19c
    show player 10
    player_name "Вы хотите, чтобы я спросил его?"
    show player 5
    show mrsj 19
    mrsjo "Я просто хочу, лучшего для него, а ты его единственный друг."
    show mrsj 19c
    show player 12
    player_name "Хорошо. Пойду спрошу у него."
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
    deb "Милый!! Ты в порядке?!"
    show debbie 14b
    show player 10
    player_name "Я в норме, {b}[deb_name]{/b}. Медсестра сказала, что у меня было небольшое сотрясение мозга."
    show player 11
    show debbie 13
    deb "Сотрясение!"
    show debbie 14b
    show player 10
    player_name "Все отлично. Я буду в порядке, {b}[deb_name]{/b}."
    show player 5
    show debbie 13
    deb "Твоя глупая школа даже не позвонила, чтобы сообщить, что ты в больнице!"
    deb "Я узнала об этом от {b}Тэмми{/b}!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, все в порядке. Я в порядке! Успокойся."
    show player 11
    show debbie 13
    deb "Извини ... Я так волновался за тебя!"
    deb "Твой {b}отец{/b} просил присматривать за тобой!"
    show debbie 14b
    show mrsj 19
    mrsjo "Я так рада, что ты в порядке, {b}[firstname]{/b}."
    mrsjo "Я пришел сюда, чтобы рассказать {b}[deb_name]{/b} вскоре как {b}Эрик{/b} позвонил мне."
    mrsjo "Ты сделал хорошее дело, защищая {b}Эрика{/b}."
    show mrsj 38
    show debbie 13
    deb "Да, это было очень храбро с твоей стороны заступиться за своего друга в школе."
    deb "Но, пожалуйста, будь осторожен!"
    show debbie 14b
    show player 24
    player_name "Я понял {b}[deb_name]{/b}..."
    show player 25
    player_name "Я обещаю, что постараюсь держаться подальше от неприятностей."
    show player 24
    show debbie 13
    deb "Иди сюда."
    hide player
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at right
    show debbie 4
    with dissolve
    deb "Я так рада, что ты в безопасности."
    deb "{b}Твой отец{/b} закатит бы истерику, если узнал, что я позволил этому случиться."
    player_name "Все хорошо, {b}[deb_name]{/b}."
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at Position (xpos=700)
    show debbie 1 at right
    show player 13 at left
    with dissolve
    show mrsj 17
    mrsjo "Спасибо еще раз, {b}[firstname]{/b}."
    mrsjo "Ты всегда можешь приходить к нам."
    show mrsj 14
    show player 14
    player_name " Все нормально. Просто помогаю другу."
    show player 13
    show mrsj 17
    mrsjo "Спасибо."
    show mrsj 14
    show player 36 with dissolve
    player_name "Спокойной ночи, {b}Миссис Джонсон{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Спокойной ночи."
    hide mrsj with dissolve
    show debbie 2
    deb "А теперь поспеши в постель и отдохни."
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
    deb "А вот и он!"
    show debbie 1
    show player 22
    player_name "!!!" with hpunch
    show debbie 2
    deb "Я так рад слышать, что {b}[firstname]{/b} недавно посетил нашу местную церковь..."
    deb "... И предложили волонтерскую работу с духовенством!"
    show debbie 1
    show player 24
    player_name "Ааа..."
    show debbie 2
    deb "Ну! Оставлю вас двоих, у меня есть дела на кухне!"
    show debbie 2f with dissolve
    deb "Было приятно познакомиться, {b}Сестра Анжелика{/b}!"
    hide debbie with dissolve
    show player 12
    player_name "Волонтерская работа?"
    player_name "И почему вы здесь?!"
    show player 11
    show ang 2
    ang "Я думала, мы договорились?"
    show ang 1
    show player 24
    player_name "..."
    show ang 2
    ang "Ты думаешь, что я просто позволю тебе ускользнуть от меня?!"
    show ang 1
    show player 10
    player_name "Нет, я только... Что вам нужно от меня?"
    show player 11
    show ang 2
    ang "Дверь церкви ночью останется незапертой."
    ang "Приходите ко мне в гости в мою палату, и я объясню, что мне нужно от тебя..."
    ang "...И не пытайся скрыть от меня, иначе-"
    show ang 1
    show player 12
    player_name "Хорошо, хорошо!"
    player_name "Только ничего не говори моей {b}хозяйке{/b}..."
    show player 11
    show ang 2
    ang "Это зависит от тебя..."
    hide ang with dissolve
    show player 12
    player_name "Теперь мне нужно увидеться с ней в церкви? Ночью?!"
    show player 10
    player_name "Это странно..."
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
    deb "Всегда приятно слышать, что {b}[firstname]{/b} активно сотрудничает с церковью."
    deb "Вы двое, должно быть, хорошо друг друга узнали."
    show debbie 1f
    show ang 2
    ang "Да, {b}[firstname]{/b} был очень полезен, вызывая угрюмых грешников."
    ang "{b}Бог{/b} непременно вспомнит о своих плодах любви к ближним."
    show ang 1
    show debbie 3f
    deb "Это же здорово!"
    deb "Я знаю, что мы все можем быть непослушными время от времени..."
    show debbie 2f
    deb "Что ж, мне лучше поторопиться. Стирка сама себя не постирает."
    hide debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "Что сейчас?"
    player_name "Я привел к вам {b}Хелен{/b}. Разве этого недостаточно?"
    show player 5
    show ang 4
    ang "О, нет, дорогой ребенок. {b}У Бога{/b} есть много вещей для вас."
    ang "{b}Хелен{/b} далеко не очищенна. Ее упрямство раздражает."
    show ang 3
    show player 26
    player_name "Расскажи мне об этом."
    show player 5
    show ang 2
    ang "Самые кающиеся христиане нуждаются в особой заботе."
    ang "Их нужно сбросить с пьедестала, чтобы мы могли его восстановить."
    ang "Думаю, для нее потребуется еще два ритуала..."
    ang "Вот почему я пришела повидаться с тобой."
    ang "Я нуждаюсь в инструменте, используемом на протяжении многих библейских времен."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "Что вам нужно?"
    show player 5
    show ang 2
    ang "Я намерена подорвать {b}Хелен{/b} с помощью бичевания."
    show ang 1
    show player 12
    player_name "Что?"
    show player 5
    show ang 4
    ang "Принеси мне {b}плетку{/b}."
    show ang 3
    show player 23
    player_name "{b}Плетку{/b}!?"
    show player 11
    show ang 4
    ang "Я бы предпочла плетку которой подвергся наш {b}Спаситель{/b}."
    ang "Но я боюсь, что ее будет трудно найти."
    ang "{b}Стандартной кожаной плетки{/b} хватит."
    show ang 2
    ang "Принеси ее мне в мои покои."
    show ang 1
    show player 10
    player_name "Это не кажется мне правильным-"
    show player 11
    show ang 2
    ang "Ты забыл, где твое место? Не заставляй меня напоминать тебе и всем остальным о твоих грехах!"
    show ang 1
    show player 15
    player_name "Но вы хотите выпороть {b}Хелен{/b}!"
    show player 16
    show ang 2
    ang "Ты заключил со мной сделку. Не сомневайтесь в моих... церковных методах."
    show ang 1
    show player 12
    player_name "Это просто не правильно."
    show player 5
    show ang 4
    ang "И кто ты такой, чтобы отличать хорошее от плохого?"
    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Хорошо. Где я вообще должен достать {b}плетку{/b}?"
    show player 17
    player_name "Есть ли список дистрибьюторов на задней странице Библии?"
    show player 5
    show ang 1
    ang "..."
    show ang 2
    ang "Я уверена, что кто-то из твоих друзей знает о грязных похотливых местах, которые продают такие вещи."
    ang "Не заставляй меня ждать."
    hide ang with dissolve
    show player 37 with dissolve
    player_name "Мне не следовало ходить в церковь."
    pause
    show player 38 with dissolve
    player_name "Куда пойти чтобы добыть {b}плетку{/b}?"
    player_name "Может в {b}магазине Pink в торговом центре{/b} торгуют чем-то похожим."
    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    ang "Самое время спуститься вниз."
    ang "Ты мне снова понадобился."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Я не уверен, что хочу продолжать помогать после того, что вы сделали с {b}Хелен{/b}, Я-"
    show player 5
    show ang 4
    ang "О, не будь таким наивным!"
    ang "Несмотря на ее нежелание, мы оба знаем, что ей понравилось."
    show ang 3
    show player 11
    player_name "..."
    show ang 2
    ang "Я пришла сюда не спорить с грешником."
    show ang 39 with dissolve
    ang "Если ты действительно хочешь помочь {b}Хелен{/b} ты поможешь мне получить это..."
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
    player_name "Что...ЭТО?"
    show player 461 at Position (xoffset=1)
    show ang 4
    ang "Это главный элемент для последнего этапа очистки {b}Хелен{/b} ..."
    ang "...И твое последнее задание."
    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "Но как это будет использоваться для очистки {b}Хелен{/b}?"
    show player 11 with dissolve
    show ang 2
    ang "Не задавай мне вопросов!"
    ang "Грешники должны просто принять слова, сказанные избраниками {b}Бога{/b}."
    ang "А теперь принеси мне предмет с фотографии и встретимся в моем кабинете."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Хорошо..."
    show player 5
    show ang 2
    ang "Хорошо. Поторопись."
    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Хелен{/b}  кажется, даже не понимает, что {b}Сестра Анжелика{/b} превращает её..."
    player_name "...в секс-рабыню!"
    show player 12
    player_name "Я должен поговорить с {b}Гарольд{/b} перед тем как помочь {b}Сестре Анжелике{/b}."
    player_name "Может, он поможет мне понять, что делать."
    show unlock55 at truecenter with dissolve
    $ player.get_item("strapon_drawing")
    pause
    hide unlock55 with dissolve
    hide player with dissolve
    return

label entrance_mom_overheard:
    scene expression game.timer.image("home_entrance{}")
    show player 34 with dissolve
    player_name "...{b}*отдаленный голос*{/b}..."
    show player 35
    player_name "( Это {b}[deb_name]{/b} по телефону? )"
    show player 12
    player_name "( ...Похоже, она сумасшедшая. Она кричит?)"
    show player 10
    player_name "( Пойду посмотрю, все ли с ней в порядке. )"
    hide player with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        deb "Доброе утро, милый."
    else:
        deb "Привет, милый."
    show debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Доброе утро, {b}[deb_name]{/b}."
    else:
        player_name "Привет, {b}[deb_name]{/b}."
    show player 1
    show debbie 2
    if game.timer.is_morning():
        deb "Готов к школе?"
    else:
        deb "Счастлив вернуться в школу?"
    show debbie 1
    show player 10
    player_name "Да, наверное. У меня столько домашней работы, чтобы догнать."
    show player 1
    show debbie 3
    deb "О, я уверена, что все будет хорошо."
    show debbie 2
    deb "Хорошо вернуться в обычную рутину."
    show debbie 1
    show player 14
    player_name "Наверное."
    player_name "Что ты сегодня делаешь?"
    show player 13
    show debbie 13
    deb "Я?"
    deb "По дому в основном. Это заставляет меня быть очень занятой."
    deb "Нелегко заботиться об этом большом месте в одиночку."
    show debbie 14b
    show player 5
    pause
    show player 2
    player_name "Я могу помочь, понимаешь?"
    show player 1
    show debbie 13
    deb "Хочешь помочь по хозяйству?"
    show debbie 1
    show player 29 with dissolve
    player_name "Конечно! Я имею в виду, я чувствую, что я должен внести свой вклад..."
    show player 1 with dissolve
    show debbie 2
    deb "Это отлично, {b}[firstname]{/b}!"
    show debbie 1
    deb "Хмм..."
    show debbie 2
    deb "Ну, газон не косили уже несколько недель..."
    deb "Можешь покосить его!"
    deb "{b}Косилка{/b} должна быть в {b}гараже{/b}."
    show debbie 1
    show player 14
    player_name "Хорошо. Пойду посмотрю."
    show player 13
    show debbie 2
    deb "Спасибо, {b}[firstname]{/b}."
    deb "Будь осторожен!"
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
    jen "Ого, что это за запах?!"
    show player 14
    show jenny f_gross
    player_name "... Я кажется. Я был снаружи, косил газон-"
    show player 11
    show jenny f_gross_talk
    jen "Это отвратительно! Ты везде в траве, неряха!"
    show player 12
    show jenny f_gross
    player_name "Извини. Я просто пыталась помочь {b}[deb_name]{/b}."
    show player 11
    show jenny f_upset_talk
    jen "Итак, что ты собираешься делать здесь?"
	show jenny f_grin_talk a_dressed_crossed with dissolve
    jen "Тебе нравится {b}[deb_name]{/b} или что-то еще?"
    show player 10
    show jenny f_grin
    player_name "Нет! Я только-"
    show player 11
    show jenny f_eyeroll
    jen "Пфф, не прикидывайся идиотом! Я вижу, что ты задумал!"
    hide jenny with dissolve
    pause
    show player 12
    player_name "Что у нее за проблема?"
    show player 10
    player_name "Ну что ж, я должен отнести эту одежду {b}вниз, в стирку{/b}."
    hide player with dissolve
    return

label entrance_mom_debt_collectors:
    scene henchman_cs1 2 with fade
    show text "Я ожидал увидеть {b}Эрика{/b}, но вместо него там стоял странный мужчина...\nОн был весь в черном, с таким взглядом, что даже тренер Бриджит не могла бы с ним соперничать." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene henchman_cs1 1
    show player 2 at left
    show henchman2 1 at right
    with dissolve
    player_name "Привет?"
    show henchman2 2
    show player 1
    henchman2 "Где владелец дома?"
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "А кто спрашивает?"
    show player 11
    show henchman2 3
    henchman2 "Это не твое дело, парень."
    show henchman2 1
    show player 12
    player_name "Ну, она сейчас немного занята, почему бы вам не зайти в другой раз?"
    show henchman2 2
    show player 11
    henchman2 "Не нужно, просто передай ей это сообщения."
    show henchman2 3
    henchman2 "У неё осталось мало времени, лучше бы поскорее заплатить или..."
    henchman2 "Мой босс не любит ждать."
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Или что?"
    show player 11
    show henchman2 3
    henchman2 "Просто передай ей это, парень."
    henchman2 "Мы скоро вернемся..."
    show henchman2 1
    player_name "..."
    $ playMusic()
    hide henchman2
    with dissolve
    scene expression L_home_entrance.background
    show player 10 at left
    with fade
    player_name "( Что {b}это{/b} было вообще... )"
    show player 5
    show debbie 62 at right with dissolve
    deb "Кто-то приходил, милый?"
    show player 10
    show debbie 61
    player_name "Да, какой-то странный мужик в черном костюме..."
    show player 5
    show debbie 59
    deb "!!!"
    show player 11
    show debbie 60
    deb "... Чего он хотел?"
    show debbie 59
    show player 10
    player_name "Он сказал, что тебе нужно заплатить, и что он скоро вернется, но нормально ничего не объяснил."
    show player 11
    show debbie 60
    deb "Это должно быть..."
    deb "Но я ведь уже всё-"
    show debbie 59
    deb "..."
    show player 10
    player_name "Что такое?"
    show player 11
    show debbie 60
    deb "Ничего, милый."
    show player 1
    show debbie 62
    deb "Наверное, он просто ошиблись домом."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background
    show player 11 at left
    show debbie 13 at right
    with dissolve
    deb "Милый! Как хорошо, что ты тут!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} и мне нужна твоя помощь."
    show debbie 14b
    show player 12
    player_name "Ха?"
    show player 5
    show debbie 13
    deb "Наверху прорвало труду, и вода сейчас просто повсюду!"
    deb "Твоя сестра сейчас пытается с этим разобраться."
    deb "Не мог бы ты помочь ей?"
    show debbie 14b
    show player 10
    player_name "Я? Эмм..."
    show player 5
    show debbie 13
    deb "Я не могу сейчас вызвать ремонтников. После того, что произошло..."
    show debbie 14b
    show player 10
    player_name "Ох, верно..."
    show player 14
    player_name "Я тогда схожу посмотрю."
    show player 13
    show debbie 2
    deb "Спасибо, милый! Скажешь, если тебе что-то понадобится."
    show debbie 1
    show player 14
    player_name "Конечно."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene location_home_entrance_night_blur
    show player 1 at left
    show debbie 62 at right
    deb "О, привет, милый!"
    deb "Уже собираешься спать?"
    show player 2
    show debbie 61
    player_name "Не, просто думаю, чем бы заняться..."
    show player 14
    player_name "А ты чего делаешь?"
    show player 1
    show debbie 62
    deb "Думала глянуть какой-нибудь фильм."
    show player 2
    show debbie 61
    player_name "Отлично."
    show player 1
    deb "..."
    show debbie 63
    deb "Может присоединишься?"
    show player 10
    show debbie 61
    player_name "Серьезно?"
    show player 11
    show debbie 62
    deb "А почему нет? Сейчас ещё не поздно, да и я люблю смотреть что-нибудь в компании!"
    show player 2
    show debbie 61
    player_name "Д-да, окей. Звучит неплохо, {b}[deb_name]{/b}."
    show player 1
    show debbie 62
    deb "Отлично!"
    deb "Тогда я пойду всё приготовлю, а ты приходи, как будешь готов, окей?"
    show player 2
    show debbie 61
    player_name "Окей!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene location_home_entrance_day_blur
    show player 1 at left with dissolve
    show debbie 165 at right with dissolve
    deb "Привет, мой милый!"
    show player 2
    show debbie 164
    player_name "Привет, {b}[deb_name]{/b}!"
    player_name "Отлично выглядишь! Ты куда-то собираешься?"
    show player 1
    show debbie 165
    deb "Ох, мне нужно сходить в {b}Торговый центр{/b} и купить несколько вещей."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Может хочешь со мной?"
    show player 11
    show debbie 164
    player_name "Хмм?"
    show player 10
    player_name "Оу, я не знаю, я собирался-"
    show player 11
    show debbie 165
    deb "Оу, да ладно! Тебе нужно хотя бы чуть-чуть подышать свежим воздухом."
    show debbie 164
    player_name "..."
    show debbie 165
    deb "... К тому же, я не хочу идти одна..."
    deb "Составишь мне компанию?"
    show debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Хех, ладно, {b}[deb_name]{/b}! Я пойду с тобой."
    show player 1
    show debbie 166
    deb "Прекрасно"
    show debbie 165
    deb "Жду тебя в машине, милый!"
    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Прости {b}[deb_name]{/b}, у меня были планы на сегодня..."
    show player 11
    show debbie 168
    deb "Оу."
    show debbie 169
    deb "..."
    show debbie 168
    deb "Ладно, милый... Только будь аккуратен и вернись к ужину."
    show player 2
    show debbie 169
    player_name "Конечно."
    return

label entrance_mom_spy:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Ха?"
    player_name "Что это за шум?"
    show player 11
    pause
    show player 10
    player_name "Может быть это просто телевизор."
    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background
    show player 4 with dissolve
    player_name "Интересно, {b}[deb_name]{/b} даст мне снова её поцеловать, если я попрошу?"
    player_name "Нужно {b}поговорить с ней{/b} об этом..."
    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression L_home_entrance.background
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Доброе утро, милый."
    show debbie 1
    show player 14
    player_name "Утра, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Ты хорошо спал сегодня?"
    show debbie 1
    show player 10
    player_name "... Даа... типа."
    player_name "Мне снилось много странных вещей."
    show player 11
    show debbie 2
    deb "Да? И что же это за странные вещи?"
    show debbie 1
    show player 10
    player_name "Ох, Эмм..."
    player_name "Ну, это немного смущает."
    show player 11
    show debbie 2
    deb "... Пошлые сны?"
    show debbie 1
    show player 10
    player_name "Эх... Да."
    show player 11
    show debbie 2
    deb "Ну тут нечего смущаться, милый!"
    show debbie 3
    deb "Ты ведь как раз в том возрасте."
    show debbie 1
    pause
    show debbie 2
    deb "Ну и кому так повезло?"
    show player 10
    show debbie 1
    player_name "Повезло?"
    player_name "Эмм, я не очень хочу об этом говорить..."
    show player 11
    show debbie 3
    deb "Хехе, оу? Я просто думала, может я её знаю?"
    show player 11
    player_name "..."
    show debbie 3
    deb "Ну ладно. У всех свои секрет!"
    show debbie 2
    deb "Ну пока ты тут, мне нужна твоя помощь. Есть минутка?"
    show debbie 14
    show player 10
    player_name "Ух... Ага. Что нужно сделать?"
    show player 1
    show debbie 13
    deb "Можешь посмотреть, почему машина не заводится?"
    show debbie 1
    show player 10
    player_name "Может она заведется в следующий раз?"
    show player 1
    show debbie 13
    deb "Может быть, но сейчас-то она не заводится!"
    show debbie 1
    show player 2
    player_name "Ты ведь не забыла снова выключить фары и не посадила аккумулятор?"
    show debbie 2
    show player 1
    deb "Ха, нет... То есть, ну... Я не думаю, что я сделала это. Ну так ты проверишь?"
    show debbie 1
    show player 14
    player_name "Нет!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background
    show player 1
    player_name "( Не могу поверить, что {b}[deb_name]{/b} терлась об мой член! )"
    player_name "( ... ещё пара секунд и я кончу. )"
    player_name "( Ахх, я так сильно её хочу. Это просто пытка! )"
    show player 11
    player_name "( .... )"
    player_name "( Хмм, я обещал не дрочить в её комнате... )"
    show player 13
    player_name "( Просто в тот раз было так приятно! )"
    player_name "( ... )"
    player_name "( А может, если я сделаю все быстро и тихо, то смогу незаметно взять её трусики и кончить... )"
    player_name "( Вроде она {b}сейчас знаята{/b}, а значит я успею подрочить в её кровати. )"
    player_name "( Я думаю, оно того стоит... Мне нужна разрядка... Чтобы очистить свой разум! )"
    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background
    show player 34 with dissolve
    player_name "...{b}*приглушенный голос*{/b}..."
    show player 35
    player_name "( Хмм, вроде {b}[deb_name]{/b} сейчас говорит с кем-то на кухне... )"
    show player 12
    player_name "( Интересно с кем? )"
    show player 10
    player_name "( Нужно пойти проверить... )"
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
    deb "Ох!!!"
    deb "Ты меня напугал..."
    show debbie 98
    show player 17
    player_name "Прости меня, {b}[deb_name]{/b}."
    show player 14
    player_name "Я не хотел!"
    show debbie 97
    show player 1
    deb "Прости за этот шум."
    deb "Просто я хотела пропылесосить."
    deb "... Ох, это просто уничтожает мою спину!"
    show debbie 98
    return

label entrance_mom_vacuum_yes:
    show debbie 98 at right
    show player 14 at left
    player_name "Эй, {b}[deb_name]{/b}, давай я помогу."
    show player 1
    show debbie 96
    deb "..."
    show debbie 97
    deb "Ты хочешь пропылесосить?"
    show debbie 96
    show player 14
    player_name "Да, я закончу тут за тебя."
    player_name "А ты дай своей спине отдохнуть..."
    show player 10
    player_name "Не нужно так убиваться, если я тут и могу помочь."
    show debbie 97
    show player 11
    deb "Нет, всё в порядке, ты не должен-"
    show debbie 98
    show player 10
    player_name "Я знаю, что я не обязан помогать, {b}[deb_name]{/b}."
    player_name "Но я хочу."
    show debbie 97
    show player 1
    deb "Ну, если ты настаиваешь..."
    show player 257
    show debbie 100
    with dissolve
    deb "Это было бы очень мило с твоей стороны."
    show player 259
    show debbie 99
    player_name "Без проблем!"
    hide player
    hide debbie
    with dissolve
    scene expression "backgrounds/location_home_cutscene02.jpg"
    show expression FilteredText("Я чувствовал себя плохо, {b}[deb_name]{/b} испытывала затруднения при болях в спине.\nСамое малое, что я мог сделать, это помочь ей, даже если я сделаю это в последний раз.\nЛестница была худшей частью! Неудивительно, что её спина причиняет ей боль...\nПо крайней мере, {b}[deb_name]{/b} была со мной, пока я работал.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label entrance_mom_vacuum_no:
    show debbie 96 at right
    show player 10 at left
    player_name "Может закончишь уборку в другой раз?"
    player_name "Я тут пытаюсь заниматься, а этот шум отвлекает."
    show debbie 97
    show player 11
    deb "Прости меня, милый!"
    deb "Я не знала, что ты сейчас занимаешься."
    show debbie 96
    show player 14
    player_name "Все хорошо, {b}[deb_name]{/b}."
    show debbie 97
    show player 1
    deb "Как раз дам своей спине отдохнуть..."
    show debbie 96
    show player 17
    player_name "Спасибо!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( Что это за звук? )"
    player_name "( Как будто телевизор работает. )"
    show player 4 at Position(xpos=518)
    player_name "( Но кто может смотреть его так поздно? )"
    hide player with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background
    show player 26 with dissolve
    player_name "( Это порно, что смотрит {b}[jen_name]{/b}, такое горячее! Я бы даже хотел к ней присоединиться... )"
    show player 33
    player_name "Хмм... Может {b}в следующий раз{/b}."
    hide player with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( Что это за звук? )"
    hide player with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Милый, кто-то звонит в дверь! Можешь открыть?"
    show debbie 1
    show player 14
    player_name "Конечно, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Привет, {b}Рокси{/b}! Ты пришла к {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Пф. А что, ты думаешь, что я пришла тебя увидеть или что-то вроде того?!"
    show roxxy 1
    show player 21
    player_name "... Нет."
    show player 5
    show roxxy 2
    rox "Отлично, потому что это-"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Кхм*"
    jen "Это та девушка, которой я должна помочь?"
    show jenny f_laugh
    jen "Ну знаешь, та, которую ты пытаешься завалить?"
    show jenny f_sad
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 3
    rox "ИЗВИНИ, ЧТО!?"
    show roxxy 14
    show player 113
    player_name "н-НЕТ!!"
    show player 10
    player_name "{b}Рокси{/b}, Я клянусь, я никогда-"
    show player 11
    show roxxy 2
    rox "Как будто у тебя есть шанс... Разве что в своих мечтах!"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_laugh
    jen "Оу, бедный маленький извращенец."
    jen "Я полагаю, что твоя рука застряла в банке с лосьоном."
    show jenny f_grin
    show roxxy 4
    rox "Ха! Да, и мне даже жаль этот лосьон..."
    show roxxy 1
    show jenny f_laugh
    jen "Хахаха! А ты мне нравишься! {b}Рокси{/b}, не так ли?"
    show jenny f_sad
    show roxxy 1b
    rox "Ага, а ты, значит, {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny f_laugh
    jen "Это так."
    jen "Давай, {b}Рокси{/b}. Мы можем укрыться от этого задрота в моей комнате."
    show jenny f_sad
    show roxxy 1b
    rox "Прекрасно."
    show roxxy 2
    rox "Ещё увидимся, задрот!"
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "У меня плохое предчувствие."
    hide player
    hide debbie
    with dissolve

    scene location_home_entrance_cutscene04
    with fade
    show text "Эти двое так быстро спелись...\nЯ полагаю, что у {b}[jen_name]{/b} и {b}Рокси{/b} много общего." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Они обе были капитанами чирлидерш, они популярны, красивы,\nа так же они обе постоянно совершенствуют это искусство быть сукой..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Я надеюсь, что не пожалею об этом..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Кто это был?"
    show debbie 14
    show player 10
    player_name "Просто девочка из моей школы. {b}[jen_name]{/b} согласилась помочь ей с чирлидерскими штуками."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} кому-то помогает?"
    show debbie 3
    deb "Это что-то новенькое."
    show debbie 1
    show player 12
    player_name "Да, это потому что я заплатил ей..."
    show player 90
    show debbie 13
    deb "Оу."
    deb "Милый, ты не должен позволять {b}[jen_name]{/b} так себя пользовать..."
    show debbie 14
    show player 12
    player_name "Да, я знаю."
    show player 90
    player_name "..."
    show debbie 13
    deb "О чем ты думаешь?"
    show debbie 14
    show player 12
    player_name "Я просто никогда не видел, чтобы {b}[jen_name]{/b} так легко находила с кем-то общий язык..."
    show player 10
    player_name "Это меня даже пугает, если честно."
    show player 5
    show debbie 2
    deb "Ну, я думаю, что это неплохо, если она нашла новую подругу."
    deb "Я немного переживаю из-за того, что она сидит у себя там каждый день..."
    show debbie 13
    deb "Я думаю, что ей очень одиноко."
    show debbie 14
    show player 10
    player_name "Я бы поспорил с этим."
    show player 5
    player_name "..."
    show player 11
    jen "Хахаха!!"
    show player 10
    player_name "...{b}Может стоит их там проверить{/b}?"
    show player 5
    show debbie 2
    deb "Может."
    show debbie 13
    deb "...Только будь осторожен, милый."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Милый, кто-то звонит в дверь! Можешь открыть??"
    show debbie 1
    show player 14
    player_name "Конечно, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Привет, {b}Рокси{/b}! Ты пришла к {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Да, предложение ведь ещё в силе?"
    show roxxy 1
    show player 21
    player_name "Конечно."
    show player 5
    show roxxy 2
    rox "Прекрасно, я так взволнована-"
    show roxxy 1 with None
    show jenny f_grin a_dressed_crossed at flip
    show jenny at Position (xpos=-120)
    with dissolve
    jen "*Кхм*"
    jen "Это та девушка, которой я должна помочь?"
    show jenny f_laugh
    jen "Ну знаешь, та, которую ты пытаешься завалить?"
    show jenny f_sad
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 4
    rox "... Хахаха!"
    show roxxy 14
    show player 113
    player_name "Я не-"
    show player 10
    player_name "{b}Рокси{/b}, Клянусь, я никогда-"
    show player 11
    show roxxy 1h
    rox "И что именно ты рассказал, {b}[firstname]{/b}?"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny f_laugh
    jen "Секунду..."
    jen "Имеешь ввиду, что ты... И он?!"
    show jenny f_sad
    show roxxy 4
    rox "Эм даа?!"
    rox "До тех пор, пока он хорошо обо мне заботится..."
	show jenny f_grin
    rox "... И пока он не растолстеет или не облысеет!"
    show roxxy 1
    show jenny f_laugh
    jen "Хахаха! А ты мне нравишься! {b}Рокси{/b}, не так ли?"
    show jenny f_sad
    show roxxy 1b
    rox "Ага, а ты, значит, {b}[jen_name]{/b}??"
    show roxxy 1
    show jenny f_laugh
    jen "Верно."
    jen "Давай, {b}Рокси{/b}. Сделаем это у меня в комнате."
    show jenny f_sad
    show roxxy 1b
    rox "Окей."
    show roxxy 2
    rox "Ещё раз спасибо, {b}[firstname]{/b}."
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "У меня плохое предчувствие."
    hide player
    hide debbie
    with dissolve
    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Так вы с ней встречаетесь?"
    show debbie 14
    show player 10
    player_name "Хех, да. {b}[jen_name]{/b} согласилась помочь ей с чирлидерскими штуками."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} помогает кому-то?"
    show debbie 3
    deb "Это что-то новенькое..."
    show debbie 1
    show player 12
    player_name "Да, просто я заплатил ей..."
    show player 90
    show debbie 13
    deb "Ох."
    deb "Милый, ты не должен позволять {b}[jen_name]{/b} так себя пользовать..."
    show debbie 14
    show player 12
    player_name "Да, я знаю."
    show player 90
    player_name "..."
    show debbie 13
    deb "О чем ты думаешь?"
    show debbie 14
    show player 12
    player_name "Я просто никогда не видел, чтобы {b}[jen_name]{/b} так легко находила с кем-то общий язык..."
    show player 10
    player_name "Это меня даже немного пугает."
    show player 5
    show debbie 2
    deb "Ну, я думаю, что это неплохо, если она нашла новую подругу."
    deb "Я немного переживаю из-за того, что она сидит у себя там каждый день..."
    show debbie 13
    deb "Я думаю, что ей очень одиноко."
    show debbie 14
    show player 10
    player_name "Я бы поспорил"
    show player 5
    player_name "..."
    show player 11
    jen "Хахаха!!"
    show player 10
    player_name "...{b}Может стоит их там проверить{/b}?"
    show player 5
    show debbie 2
    deb "Может"
    show debbie 13
    deb "...Только будь аккуратен, милый."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Я должен пойти проверить как там {b}Рокси{/b} и {b}[jen_name]{/b}..."
    hide player with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 34 with dissolve
    player_name "( Хмм? )"
    player_name "( Это {b}Диана{/b}? )"
    player_name "( {b}[deb_name]{/b} должно быть, пригласила ее. )"
    player_name "( {b}Интересно, о чем они говорят?{/b} )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
