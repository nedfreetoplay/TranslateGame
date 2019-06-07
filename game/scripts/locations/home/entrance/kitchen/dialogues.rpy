label kitchen_jenny_final_breakfast:
    scene expression player.location.background_closeup with None
    show jenny f_upset at flip
    show jenny at Position (xpos=150)
    show debbie f_sad_talk at Position (xpos=600)
    with fade
    deb "Oh, good grief {b}[jen_name]{/b}..."
    deb "I never wanted you to leave in the first place!"
    show debbie f_sad
    show jenny f_eyeroll
    jen "Well, I want to get a place of my own, it's just..."
    show jenny f_sad_talk
    jen "I'm not ready yet."
    show jenny f_sad
    show debbie f_normal_talk
    deb "That's perfectly fine, dear."
    deb "You're welcome to stay here forever, so far as I'm concerned."
    show debbie f_laugh
    deb "God knows, I could use the help!"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Yeah, that's exactly what I was thinking and with my work going so well, I could probably chip in a couple hundred more a month."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Oh, that would be wonderful, dear!"
    show debbie f_normal
    show player f_normal_talk at Position (xpos=450) with dissolve
    player_name "What's going on?"
    show player f_normal
    show debbie f_normal_talk
    deb "Good morning, sweetie!"
    deb "We were just talking about {b}[jen_name]{/b} moving out."
    show debbie f_normal
    show player f_shock
    player_name "WHAT?!"
    show player f_worried_talk
    player_name "Y-you're moving out?!"
    show player f_worried
    show jenny f_grin at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    show debbie f_laugh
    deb "Oh, no, no, no!"
    show debbie f_normal_talk
    deb "I meant to say, she's not moving out."
    show debbie f_normal
    show jenny f_normal_talk
    jen "Yeah, I've decided to stay here awhile longer."
    jen "Save up some money, you know?"
    show jenny f_normal
    show debbie f_normal_talk
    deb "Isn't that wonderful, {b}[firstname]{/b}?!"
    show debbie f_normal
    show player f_normal_talk
    player_name "Y-yeah, wonderful!"
    show player f_normal with None
    hide jenny
    show debbie b_robe_hug3 a_empty f_empty
    with dissolve
    deb "I'm just so proud of you, dear!"
    show debbie b_robe_hug4
    jen "T-thanks, {b}[deb_name]{/b}..."
    show debbie f_normal_talk b_robe a_robe_mug
    show jenny at flip
    show jenny b_dressed a_dressed_hips at Position (xpos=250)
    with dissolve
    deb "Why don't you two go have a seat at the table and I'll whip you up some eggs and bacon?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Alright."
    hide jenny with dissolve
    show player f_laugh
    player_name "Mmm, that sounds great!"
    hide player with dissolve
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 3
    show player b_magic_sit_stand_dressed f_magic_sit_stand_worried a_magic_sit_stand_resting zorder 1 at Position (align=(0,0))
    show jenny f_magic_sit_stand_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1 at Position (align=(0,0))
    pause
    show player f_magic_sit_stand_worried_talk
    player_name "So uhh..."
    player_name "About last night..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "Ugh, you're not going to start in with this lovey-dovey bullshit again, are you?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Why are you being so weird about it?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Umm, you're the one being weird!"
    show jenny f_breakfast_upset_talk a_magic_sit_stand_hip_spoon with dissolve
    jen "I'm not interested in dating you, {b}[firstname]{/b}..."
    jen "We're having phenomenal sex and making great money, why can't that be enough for you?!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "You really don't want more?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "What, like marriage and kids?!"
    jen "A little brick house with a white picket fence?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "... Sounds kinda nice."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_gross_talk
    jen "Eugh, don't make me barf!"
    show jenny f_breakfast_gross
    show player f_magic_sit_stand_worried
    player_name "..."
    show jenny f_breakfast_upset
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal_talk zorder 2 with dissolve
    show player f_diningroom_table_normal_high
    deb "Alright, who's hungry?!"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "Right here!"
    show jenny f_breakfast_upset
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal
    pause
    show debbie b_breakfast_potatoes f_breakfast_standing_normal_talk with dissolve
    show player f_diningroom_table_shy_down
    deb "What were you all talking about?"
    show debbie f_breakfast_standing_normal
    show jenny f_breakfast_upset_talk
    jen "Nothing important."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried
    player_name "..."
    show player f_diningroom_table_worried_talk_high
    player_name "Actually, I've just lost my appetite."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_worried_high
    show jenny f_breakfast_eyeroll
    jen "Ugh, so what, now you're all mad?"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried
    deb "..."
    show player f_diningroom_table_worried_talk
    player_name "Can I be excused?"
    show player f_diningroom_table_worried
    show debbie f_breakfast_standing_sad_talk
    deb "O-of course..."
    deb "Is everything alright, sweetie?"
    show debbie f_breakfast_standing_sad
    show player f_magic_sit_stand_tired_talk
    player_name "Yeah, I'm fine."
    hide player with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "What's going on with you two?"
    show debbie f_breakfast_standing_sad
    show jenny f_breakfast_upset_talk
    jen "It's nothing, {b}[deb_name]{/b}."
    jen "{b}[firstname]'s{/b} just being a big baby..."
    show jenny f_breakfast_upset
    $ player.go_to(L_home_entrance)
    scene expression player.location.background_closeup with None
    show player f_worried with dissolve
    player_name "( Well, that could have gone better... )"
    pause
    show player f_skeptical
    player_name "( She's just so damn stubborn! )"
    player_name "( Even if she did want more, she'd never admit it. )"
    show player f_tired
    player_name "( *Sigh* )"
    show player f_worried
    player_name "( I should just {b}give her some space{/b}... )"
    player_name "( ... Maybe she'll come around? )"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast_confront_her:
    show debbie f_normal_talk
    deb "Sweetie, are you coming?"
    show debbie f_normal
    show player 10 with dissolve
    player_name "Actually, I just remember something I need to do."
    show player 5
    show debbie f_sad_talk
    deb "Oh."
    show debbie f_sad
    show player 10
    player_name "Rain check?"
    show player 5
    show debbie f_normal_talk
    deb "Sure!"
    show debbie f_normal
    show player 14
    player_name "Thanks, {b}[deb_name]{/b}."
    show player 5
    hide debbie with dissolve
    player_name "( {b}[jen_name]{/b} said she was heading upstairs to take a shower. )"
    player_name "( I should hurry if I wanna catch her! )"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast_let_it_go:
    show player 4 with dissolve
    player_name "( Hmm, whatever. )"
    show player 5 with dissolve
    player_name "( {b}*Sigh*{/b} I probably shouldn't worry about it too much. )"
    player_name "( I mean, at least she's giving money to {b}[deb_name]{/b} again... )"
    player_name "( That's the important thing. )"
    deb "Sweetie, are you coming?"
    show player 14
    player_name "Yup!"
    show player 13
    player_name "( I should head to the dinning room and join {b}[deb_name]{/b} for breakfast. )"
    hide player with dissolve
    return

label kitchen_jenny_helping_with_breakfast:
    scene expression player.location.background_closeup with None
    show debbie f_normal_talk
    show jenny at flip
    show jenny at Position (xpos=150)
    with dissolve
    deb "Well, of course I'm happy that you're gonna start contributing, dear."
    deb "I'm just curious about this new job you've got?"
    show debbie f_normal
    show jenny f_eyeroll
    jen "Ugh, it's nothing special {b}[deb_name]{/b}..."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Transcribing, you said?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Yeah."
    show jenny f_normal
    show debbie f_normal_talk
    deb "What are you transcribing?"
    show debbie f_normal
    show jenny f_normal_talk
    jen "I dunno, {b}[deb_name]{/b}..."
    show jenny f_normal
    pause
    show jenny f_normal_talk
    jen "Customer Service calls and stuff."
    show jenny f_normal
    show debbie f_laugh
    deb "Oh, that's neat!"
    show debbie f_normal
    show jenny f_normal_talk
    jen "Nah, it's really boring."
    jen "It pays though."
    show jenny f_normal
    show player 13 at left
    show debbie f_normal_talk
    deb "Well, I'm proud of you, dear."
    show debbie f_normal
    show jenny f_eyeroll
    jen "Uh huh."
    show jenny f_normal
    show player 14
    player_name "What's going on?"
    show player 13
    show debbie f_normal_talk
    deb "{b}[jen_name]{/b} was just telling me about her new job."
    show debbie f_normal
    show player 12
    player_name "Oh, really?"
    show player 91 with None
    show jenny f_angry a_dressed_crossed at unflip
    show jenny at Position (xpos=-250)
    with dissolve
    show debbie f_normal_talk
    deb "She's transcribing things over the internet."
    show debbie f_normal
    show player 92
    player_name "You don't say..."
    show player 91
    show debbie f_normal_talk
    deb "It sounds really interesting."
    show debbie f_normal with None
    show jenny f_normal_talk at flip
    show jenny at Position (xpos=150)
    with dissolve
    jen "It's not."
    show jenny f_normal
    show debbie f_normal_talk
    deb "Why don't you come have breakfast with {b}[firstname]{/b} and I."
    deb "You can tell us all about it."
    show debbie f_normal
    show jenny f_upset_talk
    jen "Ehh, no thanks."
    jen "I need a shower."
    hide jenny with dissolve
    pause
    show debbie f_sorry_talk
    deb "Oh, okay, dear."
    show debbie f_normal_talk
    deb "You'll join me, won't you {b}[firstname]{/b}."
    show debbie f_normal
    show player 14
    player_name "Yeah, sure!"
    hide player
    show debbie f_empty a_empty b_robe_hug1
    with dissolve
    deb "Aww, you're such a good boy!"
    show debbie b_robe_hug2 with dissolve
    player_name "Heh, thanks {b}[deb_name]{/b}."
    player_name "You go on ahead, I'll be right there."
    show debbie b_robe_hug1 with dissolve
    deb "Okay, sweetie."
    show player 13
    hide debbie
    with dissolve
    pause
    show player 5f with dissolve
    pause
    player_name "( Transcribing, huh? )"
    show player 90f
    player_name "( She's so full of crap... )"
    player_name "( ... And she's lying to {b}[deb_name]{/b} about it. )"
    return

label kitchen_jenny_sluttygram_pics:
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phone f_breakfast_upset_down zorder 1
    show player b_dinner_sitting a_dinner_sitting_bowl f_diningroom_table_shy_down zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating with dissolve
    pause 
    show jenny f_breakfast_upset_down_talk
    show player f_diningroom_table_surprised_left_food a_dinner_sitting_resting with dissolve
    jen "Oh, what the hell!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_surprised_talk_food
    player_name "What are you doing?"
    show player f_diningroom_table_surprised_left_food
    jen "..."
    show jenny f_breakfast_upset_down_talk
    jen "I can't believe how fucking stupid these people are!"
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Uhh, Hello?!"
    show player f_diningroom_table_grumpy_food_left
    show jenny f_breakfast_angry_talk
    jen "What?!"
    show jenny f_breakfast_angry
    show player f_diningroom_table_surprised_talk_food
    player_name "I asked what you are doing?"
    show player f_diningroom_table_surprised_left_food
    show jenny f_breakfast_eyeroll
    jen "Nothing."
    show jenny f_breakfast_upset_talk
    jen "Just, shut up and go away..."
    jen "... Twerp."
    show jenny f_breakfast_upset_down
    show player f_diningroom_table_grumpy_food_left_talk
    player_name "Ugh, fine."
    hide player
    show player 323c at Position(xpos=610,ypos=770)
    with dissolve
    player_name "I dunno why you have to be such a bitch, all the tim-"
    show player 323d
    show jenny f_breakfast_upset_down_talk
    jen "Wait a second!"
    show jenny f_breakfast_upset_down
    player_name "..."
    show jenny f_breakfast_upset_down_talk
    jen "What do you know about social media?"
    show jenny f_breakfast_upset_down
    show player 323e
    player_name "Huh?"
    player_name "Why?"
    show player 323b
    show jenny f_breakfast_upset_down_talk
    jen "Sit down."
    show jenny f_breakfast_upset_down
    show player 323c
    player_name "... Okay."
    hide player
    show player b_dinner_sitting a_dinner_sitting_bowl f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    with dissolve
    show jenny f_breakfast_upset_down_talk
    jen "I made an account on this website where loser guys pay hot girls to post pictures of themselves."
    show jenny f_breakfast_grin_talk a_breakfast_dressed_phoneshow with dissolve
    jen "I'm sure you've heard of it, you're a loser afterall..."
    scene expression "backgrounds/location_home_diningroom_sluttygram.jpg" with dissolve
    player_name "{b}Sluttygram{/b}, seriously?!"
    player_name "This is your bright money making idea?"
    pause
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_breakfast_dressed_phoneshow f_breakfast_upset_talk zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_magic_sit_stand_worried zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    jen "Yeah, so?!"
    show jenny a_breakfast_dressed_phone with dissolve
    jen "C'mon, I'm hot!"
    show jenny f_breakfast_eyeroll
    jen "Way hotter than all of these little bitches!"
    show jenny f_breakfast_upset_talk
    jen "I should be making a killing on this site!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Well, you're awfully full of yourself, aren't you?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_grin_talk
    jen "Pfft, says the guy who won't stop perving on me!"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "Hmm, fair enough."
    player_name "So what's the problem?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "The problem is, I've had this account active for a couple weeks now and I've barely gotten any followers at all!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Well these things take time... You don't just get a million followers overnight."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_normal_talk
    jen "That's bullshit!"
    jen "I don't have time to wait around, I need money now!"
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "I don't know what to tell you..."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_down_talk
    jen "I mean, look at all the followers this skank has!"
    show jenny f_breakfast_upset_down
    pause
    show jenny f_breakfast_upset_down_talk
    jen "And this one!"
    show jenny f_breakfast_upset a_breakfast_dressed_phoneshow with dissolve
    show player f_diningroom_table_surprised_left_low
    pause
    show jenny f_breakfast_upset_down_talk a_breakfast_dressed_phone with dissolve
    show player f_magic_sit_stand_worried
    jen "... And oh my god, look at that one!"
    show jenny f_breakfast_upset a_breakfast_dressed_phoneshow with dissolve
    show player f_magic_sit_stand_normal_talk
    player_name "Oh, I'm looking."
    show player f_diningroom_table_surprised_left_low
    show jenny f_breakfast_upset_talk
    jen "She looks like she fell out of the ugly tree and hit every branch on the way down..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Mmm, I dunno... She looks pretty good to me!"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_upset_talk a_breakfast_dressed_phone with dissolve
    jen "Tch, the only reason you're saying that is because her tits are hanging out..."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "No!"
    show player f_magic_sit_stand_normal
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "... That's not the only reason."
    player_name "Though now that you mention it, all of these girls are posting pictures that are way more provocative than the ones you are putting out there."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_sad_talk
    jen "Provocative?"
    show jenny f_breakfast_grin
    pause
    show jenny f_breakfast_grin_talk
    jen "You mean slutty!"
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_normal_talk
    player_name "Sure, okay."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_sad
    pause
    show jenny f_breakfast_sad_talk
    jen "You think I should post some sluttier pictures?!"
    show jenny f_breakfast_sad
    show player f_magic_sit_stand_worried_talk
    player_name "No, I think you should get a job like a normal person."
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry
    pause
    show jenny f_breakfast_angry_talk
    jen "No way, screw that!"
    jen "Come with me."
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset with dissolve
    show player f_magic_sit_stand_worried_talk
    player_name "Huh?"
    hide player
    show jenny b_breakfast_pulling f_empty with dissolve
    player_name "Where are we-"
    hide jenny with dissolve
    jen "Shut up and come on."
    scene black with dissolve
    $ player.go_to(L_home_sisbedroom)
    label jenny_taking_pictures_replay:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
    scene expression player.location.background_closeup with None
    show player 12 at left
    show jenny
    with dissolve
    player_name "What the heck are we doing?!"
    show player 90
    show jenny f_upset_talk a_dressed_camera_give with dissolve
    jen "We're taking some slutty pictures for my dumb {b}Sluttygram{/b} account so I can get more horny losers to subscribe to my feed!"
    show player 728b
    show jenny f_upset a_dressed_hips
    with dissolve
    player_name "When did you get a digital camera?!"
    show player 728
    show jenny f_upset_talk
    jen "None of your business, twerp."
    show jenny f_upset
    show player 728b
    player_name "Is that what you spent my money on?!"
    hide jenny with dissolve
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_dressed a_bed_dressed_tie f_bed_normal_low with dissolve
    jen "..."
    show jenny b_bed_tied a_bed_tied_knot with dissolve
    player_name "{b}[jen_name]{/b}, this is stupid!"
    player_name "Why don't you just go back up to {b}Consum-R{/b} and ask if you can have your old job back?!"
    show jenny a_bed_tied_down with dissolve
    player_name "I'm sure they'll-"
    pause
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_normal_low with dissolve
    player_name "They'll-"
    show jenny a_bed_back_pull f_bed_lay_back_normal_talk with dissolve
    jen "There. How's that?"
    show jenny f_bed_lay_back_normal
    player_name "..."
    player_name "You know, on second thought."
    player_name "I think the {b}Sluttygram{/b} idea is marvelous and I'm fully on board with this plan now."
    show jenny f_bed_lay_back_grin_talk
    jen "Heh, just shut up and take the pictures, loser!"
    call screen jenny_photo1

label kitchen_jenny_sluttygram_pics_post_photo1:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_normal_talk
    with fade
    jen "How did that look?"
    show jenny f_bed_lay_back_grin_talk
    jen "It's hot, right?"
    show jenny f_bed_lay_back_grin
    player_name "Y-yeah!"
    show jenny f_bed_lay_back_grin_talk
    jen "You should probably get a nice shot of my ass too."
    jen "I bet those losers will loooove that."
    show jenny f_bed_lay_back_grin
    call screen jenny_photo2

label kitchen_jenny_sluttygram_pics_post_photo2:
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show jenny b_bed_back_tied a_bed_back_down f_bed_lay_back_grin_talk
    with fade
    jen "Alright, time for the finale."
    jen "Make sure you get a good shot."
    show jenny f_bed_lay_back_grin
    player_name "This is awesome!"
    show jenny f_bed_lay_back_grin_talk
    jen "Yeah, yeah. Hurry it up."
    call screen jenny_photo3

label kitchen_jenny_sluttygram_pics_post_photo3:
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["02_unlocked"] = True
    $ player.go_to(L_home_sisbedroom)
    scene expression player.location.background_closeup with None
    show jenny b_tied f_normal_talk a_tied_hips
    show player 727 at left
    with dissolve
    jen "Alright, lemme see!"
    show player 13
    show jenny f_normal_low a_tied_camera_look
    with dissolve
    jen "..."
    show jenny f_normal_talk
    jen "Oh yeah, if this doesn't bring in the followers, nothing will."
    show jenny f_grin_talk
    jen "Those other skanks are about to learn just how hot they AREN'T!"
    show jenny f_grin_down
    pause
    show player 14
    player_name "I think you ruined your shirt..."
    show player 13
    show jenny f_normal_talk
    jen "Huh?"
    show jenny f_normal_low
    pause
    show jenny f_grin_talk
    jen "Yeah, whatever. I've got more shirts."
    show jenny f_upset_talk
    jen "Why are you still here?!"
    show jenny f_upset
    show player 12
    player_name "What do you mean?"
    show player 5
    show jenny f_upset_talk
    jen "I mean, get out, I'm done with you."
    show jenny f_upset
    show player 12
    player_name "What the hell, I just-"
    show player 90
    show jenny f_angry_talk
    jen "Goodbye, perv!"
    show jenny f_angry
    player_name "..."
    show player 24
    player_name "{b}*Sigh*{/b}"
    hide player with dissolve
    show jenny f_grin_down
    pause
    show jenny f_laugh
    jen "Damn, I'm sexy!"
    scene black with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( I can't believe that just happened. )"
    player_name "( She was actually being kind of cool for a few minutes there. )"
    show player 17
    player_name "( And then she practically stripped for me! )"
    pause
    show player 5
    player_name "( Too bad she went back into bitch mode after I took the pictures... )"
    show player 13
    player_name "( Oh well. )"
    pause
    show player 4 with dissolve
    player_name "( I wonder if I can get a copy of those photos somehow? )"
    hide player with dissolve
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_took_pictures)
    $ game.main()

label kitchen_jenny_have_breakfast:
    scene expression player.location.background_closeup with None
    show player 14 at left
    show debbie
    with dissolve
    player_name "Morning {b}[deb_name]{/b}."
    hide player
    show debbie b_robe_hug1 a_empty f_empty
    with dissolve
    deb "Good morning, sweetie."
    pause
    show player 14 at left
    hide debbie
    show debbie
    with dissolve
    player_name "Mmm, breakfast smells wonderful!"
    show player 13
    show debbie f_laugh
    deb "Hehe, it's almost done."
    show debbie f_normal_talk
    deb "{b}Why don't you go sit down at the table{/b} and I'll bring it to you."
    show debbie f_normal
    show player 14
    player_name "Awesome, thanks {b}[deb_name]{/b}!"
    show player 14f with dissolve
    player_name "( {b}[deb_name]{/b} makes the best breakfast! )"
    hide player
    hide debbie
    with dissolve
    $ player.go_to(L_home_diningroom)
    scene expression game.timer.image("dining_room{}") with None
    show jenny b_breakfast_dressed a_breakfast_dressed_spoon f_breakfast_normal_low zorder 1
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal zorder 0 at Position(align=(0,0))
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    pause
    show player f_magic_sit_stand_normal_talk
    player_name "Morning."
    show player f_magic_sit_stand_normal
    jen "Mmhmm."
    show player f_magic_sit_stand_tired_talk
    player_name "Why are you eating cereal?"
    player_name "Didn't you see {b}[deb_name]{/b} cooking breakfast?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_eyeroll
    jen "Yes but I was recently told I need to grow up and support myself, remember?"
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_surprised_left
    player_name "..."
    show player f_magic_sit_stand_normal_talk
    player_name "Are you really still pouting about that?"
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_low_talk
    jen "I'm not pouting."
    show jenny f_breakfast_normal_low
    show player f_magic_sit_stand_normal_talk
    player_name "Yes, you are."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_normal_low_talk
    jen "Tsk, shut up."
    show jenny f_breakfast_normal_low
    pause
    pause
    show jenny f_breakfast_normal_talk
    jen "Hey, lend me sixty dollars."
    show jenny f_breakfast_normal
    show player f_magic_sit_stand_worried_talk
    player_name "Huh?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "I said, lend me sixty dollars."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "What for?!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_eyeroll
    jen "Ugh, that's none of your business!"
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_worried_talk
    player_name "Umm, it's my money... So yes, it kinda is my business!"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_upset_talk
    jen "{b}*Sigh*{/b} Look, I know a way I can make some money but I need to buy something first."
    jen "I'll pay you back."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "Yeah, right."
    player_name "How are you gonna pay me back?!"
    player_name "You don't even have a job."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_angry_talk
    jen "Don't be a dick, {b}[firstname]{/b}!"
    show jenny f_breakfast_upset_talk
    jen "I know {b}Diane{/b} is overpaying you for whatever the hell you're doing at her house."
    show jenny f_breakfast_upset
    show player f_magic_sit_stand_normal_talk
    player_name "I'm tending her garden."
    show player f_magic_sit_stand_normal
    show jenny f_breakfast_grin_talk
    jen "Heh, whatever."
    jen "Don't care."
    jen "The point is, you can spare sixty measly dollars."
    show jenny f_breakfast_grin
    show player f_magic_sit_stand_worried_talk
    player_name "No way!"
    player_name "I need every cent I can get."
    player_name "I have to make tuition next year, remember?"
    show player f_magic_sit_stand_worried
    show jenny f_breakfast_angry_talk
    jen "Grr, fine!"
    jen "I'm gonna remember this!"
    show jenny f_breakfast_angry
    show debbie b_breakfast_potatoes a_empty f_breakfast_standing_normal with dissolve
    pause
    show jenny f_breakfast_normal_low
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "Here you go, sweetie."
    show debbie b_breakfast_potatoes3 f_empty with dissolve
    show player f_diningroom_table_normal_talk
    player_name "Thanks, {b}[deb_name]{/b}."
    show debbie b_breakfast_potatoes f_breakfast_standing_normal_talk
    show player a_dinner_sitting_bowl f_diningroom_table_shy_down
    with dissolve
    deb "You want me to fix you a plate, {b}[jen_name]{/b}?"
    show debbie f_breakfast_standing_normal
    show jenny b_breakfast_gettingup a_empty f_breakfast_getup_upset_talk with dissolve
    jen "No, I do not."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_looking_down_eating a_dinner_sitting_eating
    hide jenny
    with dissolve
    pause
    show player f_diningroom_table_looking_down_food a_magic_sit_stand_resting with dissolve
    show debbie f_breakfast_standing_sad_talk
    deb "What's the matter with her?"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "She's still upset about the other night."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "{b}*Sigh*{/b} I should go and apologize to her."
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "No you shouldn't, {b}[deb_name]{/b}."
    player_name "She's the one being a bitch."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_sad_talk
    deb "{b}[firstname]{/b}!"
    deb "Don't say that about {b}[jen_name]{/b}!"
    show debbie f_breakfast_standing_sad
    show player f_diningroom_table_surprised_talk_high_food
    player_name "Sorry, {b}[deb_name]{/b}."
    player_name "... She totally is though."
    show player f_diningroom_table_surprised_high_food
    show debbie f_breakfast_standing_normal_talk
    deb "Tsk, just eat your breakfast."
    show debbie f_breakfast_standing_normal
    show player f_diningroom_table_normal_talk_high
    player_name "Thanks again for this, it's delicious!"
    show player f_diningroom_table_normal_high
    show debbie f_breakfast_standing_normal_talk
    deb "You're welcome, sweetie."
    scene black with dissolve
    hide player
    hide debbie
    hide expression "characters/jenny/layeredimage/jenny_breakfast_table.png"
    return

label kitchen_diane_3way_aftermath:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_dressed_juice f_gross zorder 2 at flip
    show jenny at Position (xpos=200)
    show debbie 11b zorder 1 at right
    with dissolve
    deb "Oh, would you let it go already, {b}[jen_name]{/b}!"
    show debbie 10b
    show jenny f_upset_talk
    jen "No, I don't understand this!"
    jen "You're really gonna let {b}Diane{/b} stay?!"
    jen "She was fucking {b}[firstname]{/b}!"
    jen "Right there in our living room!!"
    show jenny f_gross
    show debbie 11b
    deb "I told you, I dealt with it."
    show debbie 10b
    show jenny f_upset_talk
    jen "You dealt with it?!"
    jen "What does that even-"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "Morning!"
    show player 13
    show jenny f_gross at unflip
    show jenny at Position (xpos=-200)
    show debbie 2
    deb "Good morning, sweetie!"
    show debbie 1
    show player 14
    player_name "It smells wonderful in here!"
    show player 13
    show debbie 3
    deb "Hehe, I'm making your favorite!"
    show debbie 1
    show player 14
    player_name "Smiley face pancakes?!"
    show player 13
    show debbie 2
    deb "And three strips of bacon!"
    show debbie 1
    show player 17
    player_name "Yum!!"
    show player 18
    show debbie 3
    deb "Hehe!"
    hide player
    show debbie 4
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    pause
    show jenny f_eyeroll
    jen "Ugh!"
    show jenny f_upset_talk
    jen "You guys are getting weirder and weirder everyday!"
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Whatever."
    jen "I don't even care anymore!"
    hide jenny with dissolve
    jen "Buncha weirdos!"
    show debbie 1
    show player 5f at left
    with dissolve
    pause
    deb "Oh, don't mind her {b}[firstname]{/b}."
    show player 5 with dissolve
    show debbie 2
    deb "She's just being dramatic."
    deb "You know how she is..."
    show debbie 1
    show player 10
    player_name "Y-yeah."
    show player 13
    pause
    show player 14
    player_name "Did {b}Diane{/b} already leave this morning?"
    show player 13
    deb "Hmm?"
    show debbie 2
    deb "Oh, yeah... She was gone before the sun was up."
    deb "Said she wanted to get a head start on the day."
    deb "Sounds like she'll have lots of work waiting for you."
    show debbie 1
    show player 29 with dissolve
    player_name "Heh, y-yeah... Work."
    show player 13 with dissolve
    show debbie 2
    deb "C'mon, we'd better get some food into you."
    deb "You're gonna need lots of energy to keep up with {b}Diane{/b}!"
    show debbie 1
    show player 14
    player_name "O-okay, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_diane_breeding_candidate:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show player 14 at left
    show jenny a_dressed_juice zorder 2 at flip
    show jenny at Position (xpos=200)
    show debbie 1 zorder 1 at right
    with dissolve
    player_name "Good morning."
    show player 13
    show jenny f_eyeroll
    show debbie 2
    deb "Morning, sweetie!"
    show debbie 1
    show jenny f_upset
    show player 10
    player_name "Where's {b}Diane{/b}?"
    show player 13 with None
    show jenny at unflip
    show jenny zorder 0 at Position (xpos=-200)
    with dissolve
    deb "Hmm?"
    show debbie 2
    deb "Oh, she took off early this morning, all excited about something."
    show debbie 1
    show player 14
    player_name "Excited?"
    show player 13
    show debbie 2
    deb "Yeah, she was even more amped up than the morning her barn was finished."
    show debbie 1
    show player 14
    player_name "Really?"
    show player 13
    show jenny f_upset_talk
    jen "She's so weird..."
    show jenny f_upset
    show debbie 13
    deb "Oh, hush."
    show debbie 14
    show jenny f_eyeroll
    jen "Well she is!"
    show jenny f_upset
    show debbie 13
    deb "{b}[jen_name]{/b}!"
    show debbie 14b
    pause
    show debbie 2
    deb "Did {b}Diane{/b} tell you what's going on?"
    show debbie 1
    show player 29 with dissolve
    player_name "Oh, uhh..."
    player_name "N-nope, heh."
    show player 14 with dissolve
    player_name "I should probably get over there and see what she's up to..."
    show player 13
    show debbie 2
    deb "Well, hold on now."
    deb "You need your breakfast!"
    show debbie 1
    show player 14
    player_name "No, that's okay."
    player_name "I'm not really hungry."
    show player 13
    show debbie 2
    deb "Tsk, it's not good to skip breakfast, {b}[firstname]{/b}."
    show debbie 1
    show player 14
    player_name "Really {b}[deb_name]{/b}, I'm fine."
    player_name "Thanks though!"
    show player 13
    deb "..."
    show debbie 2
    deb "Okay."
    show debbie 1
    show player 14
    player_name "I'll see you both later tonight."
    show player 13
    show debbie 2
    deb "Be careful, sweetie."
    show debbie 1
    hide player with dissolve
    pause
    show jenny f_gross
    jen "..."
    show jenny f_upset_talk
    jen "Something strange is going on with those two."
    show jenny f_upset
    show debbie 2
    deb "What do you mean?"
    show debbie 1 with None
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    jen "..."
    show debbie 2
    deb "They're just excited about the new business."
    show debbie 1
    show jenny f_upset_talk
    jen "Yeah, right."
    show jenny f_upset
    show debbie 14
    deb "Hmm?"
    show jenny f_upset_talk
    jen "Ugh, nothing. Nevermind."
    jen "I'll be in my room."
    hide jenny with dissolve
    show debbie 13
    deb "Alright, dear."
    hide debbie with dissolve
    return

label kitchen_diane_barn_news:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_dressed_juice f_gross
    show diane nightgown_dip
    with dissolve
    deb "Hahaha!"
    show jenny f_normal_talk
    jen "You guys are so weird... I'm outta here."
    show jenny f_normal zorder 1 at Position (xpos=100)
    show diane b_nightgown a_nightgown_sides f_smirk_talk at Position (xpos=400)
    show debbie 1 zorder 2 at right
    with dissolve
    dia "Aww, what's the matter princess?"
    show jenny at flip
    show jenny at Position (xpos=600)
    with dissolve
    dia "You jealous?"
    show diane f_smirk
    show jenny f_eyeroll
    jen "Psh."
    show jenny f_normal at unflip
    show jenny at Position (xpos=100)
    with dissolve
    show diane f_smirk_talk
    dia "Don't be grumpy, I'll take you for a spin too."
    show diane f_smirk a_nightgown_slap
    show jenny f_surprised_back
    jen "!!!" with hpunch
    show diane f_laugh a_nightgown_sides
    show jenny f_upset_talk at flip
    show jenny at Position (xpos=640)
    with dissolve
    jen "N-no way!"
    show jenny f_upset
    dia "Hahaha, look at those rosie cheeks!"
    show debbie 3
    deb "Haha!"
    show jenny f_eyeroll
    jen "Ugh, shuddup!"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "What's going on?"
    show player 13
    show debbie 1
    show diane f_normal_talk
    dia "{b}[firstname]{/b}!!!"
    show diane f_normal
    show debbie 2
    deb "Good morning, sweetie."
    show debbie 1
    show diane f_laugh
    dia "It's done, it's done, it's doooooooone!!!"
    show diane f_cheese
    show player 13
    player_name "Hmm?"
    show player 17
    player_name "Wait, you mean the barn is done?!"
    show player 13
    show diane f_normal_talk
    dia "Bingo!"
    dia "{b}Richard{/b} just called to let me know that everything is ready."
    show diane f_normal
    show jenny f_eyeroll
    jen "I don't get it."
    show jenny f_normal_talk
    jen "I'd much rather have a house than a stupid barn."
    show jenny f_normal
    show diane f_smirk_talk
    dia "Yeah well, I'd rather have a fun roomate, than a sour puss."
    show diane f_smirk
    show debbie 13
    deb "{b}*Sigh*{/b} You two..."
    show debbie 14
    show player 14
    player_name "Well, I'm excited!"
    show player 13
    show diane f_normal_talk
    dia "See!!"
    dia "{b}[firstname]{/b} knows how to react to good news!"
    hide player
    show diane nightgown_hug2
    show jenny f_gross at unflip
    show jenny at Position (xpos=350)
    with dissolve
    dia "Thank you, {b}[firstname]{/b}!"
    show diane nightgown_hug3
    player_name "Y-yeah."
    show diane nightgown_hug4
    show jenny f_upset_talk
    jen "Ugh, whatever."
    jen "I'll be in my room."
    hide jenny with dissolve
    pause
    show diane b_nightgown a_nightgown_sides at Position (xpos=250)
    show player 14 at left
    with dissolve
    player_name "So are we heading over there?"
    show player 13
    show diane f_normal_talk
    dia "You bet we are!"
    show diane f_normal
    show debbie 2
    deb "Ah ah ah!"
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "After breakfast!"
    show debbie 1
    show diane f_laugh
    dia "Aww, but Mooooom!"
    show diane f_normal
    show debbie 2
    deb "{b}Diane{/b}, it's the most important meal of the day."
    show debbie 1
    show diane f_normal_talk
    dia "I've been waiting almost thirty years for this, I'm going!"
    dia "We'll just have to eat an extra big dinner tonight!"
    show diane at unflip
    show diane f_smirk_talk at Position (xpos=250)
    with dissolve
    dia "Right, {b}[firstname]{/b}?!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "I uhh..."
    show player 3
    show debbie 3
    deb "Hahaha, alright fine."
    show debbie 2
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "Go have your fun."
    show player 13
    hide debbie
    show diane f_normal_talk b_nightgown_hug1 a_empty at flip
    show diane at Position (xpos=904)
    with dissolve
    dia "Thanks!"
    show debbie 1 at right
    show diane b_nightgown a_nightgown_sides f_normal_talk at unflip
    show diane at Position (xpos=250)
    with dissolve
    dia "C'mon, {b}[firstname]{/b}!"
    dia "{b}Let's go check out the new barn!{/b}"
    hide diane with dissolve
    show debbie 2
    deb "Just make sure you get dressed first!"
    show debbie 1
    show player 14
    player_name "Hehe, I've never seen her so excited..."
    show player 13
    show debbie 2
    deb "Yeah, you'd better go with her."
    hide player
    show debbie 4
    with dissolve
    pause
    show debbie 5
    player_name "Alright, I'll see you tonight {b}[deb_name]{/b}."
    show debbie 2 with dissolve
    deb "Be safe!"
    hide debbie with dissolve
    return

label kitchen_diane_dinner:
    scene location_home_kitchen_day_blur
    show player 14 at left
    show debbie 1 at right
    with dissolve
    player_name "Hey, {b}[deb_name]{/b}. I have the {b}fish{/b} you wanted."
    show player 13
    show debbie 2
    deb "Thanks, sweetie! Now I can finish dinner."
    deb "I'll let you know when it's finished, okay?"
    show player 203

    scene black

    scene expression L_home_entrance.background
    show diane b_classy a_classy_sides f_normal_talk at Position (xpos=600)
    show debbie 91f
    with dissolve
    dia "Mmm, is that {b}Sea Trout{/b} I'm smelling?!"
    dia "You didn't?!"
    show diane f_normal
    show debbie 93f
    deb "Of course I did!"
    deb "I know how to treat my girl right!"
    show diane f_laugh
    show debbie 91f
    dia "Oh my gosh, I could totally kiss you right now!"
    show player 203 at left with dissolve
    show diane f_normal_talk
    dia "There he is..."
    dia "... The {b}man of the house{/b}!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 17
    player_name "That dress looks great on you!"
    show diane f_laugh
    show player 203
    dia "Oh stop it, you!"
    show player 13
    show diane f_normal
    show debbie 93f
    deb "He's quite the little charmer isn't he?"
    show diane f_normal_talk
    show debbie 91f
    dia "I don't know how you manage to keep your hands off him!"
    dia "Where's your other tenant? Is she going to join us tonight or did she have a Bitches of Summerville meeting to attend?"
    show player 10
    show diane f_normal
    player_name "No, she's gonna eat with us."
    show player 12
    player_name "... She's just upstairs getting ready."
    show player 203
    show diane f_laugh
    dia "Typical princess..."
    show diane f_normal_talk
    dia "Well, I'm not waiting for her! Not when {b}[deb_name]'s{/b} {b}Sea Trout{/b} is on the menu!"
    show debbie 92f
    show diane f_normal
    deb "Hey, be nice!"
    show debbie 93f
    deb "She's not as bad as you make her out to be..."
    show debbie 91f
    show diane f_laugh
    dia "Heh, if you say so."
    show debbie 93f
    show diane f_normal
    deb "I do. Now both of you get in there and sit down while I scrounge up a bottle of wine!"
    show debbie 92f
    deb "I've got this new brand I want you to try."
    hide debbie
    hide diane
    with dissolve
    show player 14
    player_name "I should join them in the {b}Dining Room{/b}."
    player_name "{b}[deb_name]'s{/b} cooking smells delicious!"
    hide player
    with dissolve

    $ player.go_to(L_home_diningroom)
    scene location_home_dining
    show player b_dinner_sitting a_dinner_sitting_resting f_diningroom_table_normal zorder 0 at Position(align=(0,0))
    show diane b_dinner a_dinner_normal f_dinner_normal
    show jenny b_dinner_casual_side f_empty a_dinner_casual_side1 at Position (align=(0,0))
    show jenny at Position (xpos=300)
    show debbie 65 at Position(xpos=887)
    show table 1 zorder 2 at Position(xpos=0.4976,ypos=0.7630)
    with fade
    deb "... the school really ordered that much?!"
    deb "It's a good thing you've got {b}[firstname]{/b} to help you, huh?"
    show jenny a_dinner_casual_side2 with dissolve
    deb "It seems like he's always over there nowadays."
    show debbie 64
    show jenny b_dinner_casual f_breakfast_surprised a_breakfast_dressed_spoon with dissolve
    show player f_magic_sit_stand_laugh
    show diane f_dinner_normal_talk
    dia "Well there's just so much work that needs doing between the garden and the milk business."
    dia "... And he's really shown an aptitude for it as well!"
    show diane f_dinner_normal
    show player f_diningroom_table_normal
    show debbie 65
    deb "Oh, really?"
    show jenny f_breakfast_gross
    show debbie 64
    show diane f_dinner_normal_talk a_dinner_hand with dissolve
    show player f_magic_sit_stand_normal
    dia "Oh, yeah."
    dia "You should really be proud of him, {b}[deb_name]{/b}!"
    dia "He's such a responsible young man."
    show jenny b_dinner_casual_side f_empty a_dinner_casual_side1 with dissolve
    show player f_diningroom_table_surprised_left a_dinner_sitting_touch1
    show diane f_dinner_normal a_dinner_hand2 b_dinner_open
    with dissolve
    player_name "( !!! )"
    show jenny a_dinner_casual_side2 with dissolve
    show diane f_dinner_normal_talk
    dia "... Really smart..."
    dia "... And strong..."
    show player f_diningroom_table_surprised_teeth_left a_dinner_sitting_touch2
    show diane a_dinner_hand3
    with dissolve
    dia "... And gentle."
    show jenny a_dinner_casual_side1 with dissolve
    show diane f_dinner_normal
    player_name "{b}*Gulp*{/b}"
    show debbie 65
    deb "Aww, of course I'm proud of him!"
    if M_mom.finished_state(S_mom_diane_visit) or store._in_replay is not None:
        show debbie 67 with dissolve
        deb "He's really been stepping up around here lately too."
        show debbie 68 with dissolve
        player_name "( !!! )"
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "Helping out with chores..."
        deb "... Doing maintenance around the house..."
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "... He's taking such good care of {b}[jen_name]{/b} and me."
        show debbie 69 with dissolve
        player_name "Hehehe, I-"
        show debbie 68 with dissolve
        player_name "... I mean, it's-"
    show player od_dinner_sitting_boner
    show jenny f_breakfast_gross_talk b_dinner_casual a_breakfast_dressed_spoon
    show debbie 64
    with dissolve
    jen "Ugh, all this lovey dovey shit is gonna make me barf..."
    show diane f_dinner_annoyed_left_talk
    dia "We don't need commentary from the peanut gallery, {b}[jen_name]{/b}..."
    dia "Just eat your dinner and hush."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    jen "Psh, whatever..."
    show jenny f_breakfast_gross
    pause
    show jenny f_breakfast_gross_talk
    jen "You guys are acting weird."
    show jenny f_breakfast_gross
    pause
    jen "Hmm..."
    show jenny f_breakfast_grin_down_talk a_dinner_casual_drop with dissolve
    jen "... Oops."
    show jenny b_dinner_casual_bending f_empty a_empty at Position (xpos=200)
    show diane f_dinner_annoyed_left
    with dissolve
    pause
    show expression "backgrounds/location_home_dining_under.jpg"
    hide table
    hide diane
    show diane dinner_under_hand
    jen "( !!! )" with hpunch
    pause
    scene location_home_dining
    show player b_dinner_sitting a_dinner_sitting_touch2 f_diningroom_table_surprised_teeth_left od_dinner_sitting_boner zorder 0 at Position(align=(0,0))
    show diane b_dinner_open a_dinner_hand3 f_dinner_annoyed_left
    show debbie 64 at Position(xpos=880)
    show table 1 zorder 2 at Position(xpos=0.4976,ypos=0.7630)
    if M_jenny.finished_state(S_jenny_catch_her_jilling) or store._in_replay is not None:
        show jenny f_breakfast_gross b_dinner_casual a_breakfast_dressed_spoon at Position (xpos=300)
        with dissolve
        jen "( ... )"
    else:
        show jenny b_dinner_casual f_breakfast_surprised a_breakfast_dressed_spoon at Position (xpos=300)
        with dissolve
        jen "( What the fuck... )"
    show debbie 65
    show diane f_dinner_normal
    deb "So have you had any luck finding a new workplace?"
    show debbie 64
    show jenny b_dinner_casual_bending f_empty a_empty at Position (xpos=200) with dissolve
    dia "Hmm?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch1
    with dissolve
    dia "Oh, uhh... No, unfortunately there just isn't anything available near town."
    show diane f_dinner_normal a_dinner_touch
    show debbie 64d
    show player f_diningroom_table_normal
    deb "Please tell me you aren't really gonna move away from us..."
    show jenny f_breakfast_gross b_dinner_casual a_breakfast_dressed_spoon at Position (xpos=300)
    show debbie 64c
    show diane f_dinner_normal_talk a_dinner_touch1
    show player f_magic_sit_stand_normal
    with dissolve
    dia "Well, not if I can help it!"
    show jenny f_breakfast_surprised
    dia "{b}[firstname]{/b} actually came up with a good idea the other day..."
    show diane f_dinner_normal
    show debbie 65
    show jenny f_breakfast_normal_closed a_dinner_casual_facepalm with dissolve
    deb "Oh yeah?"
    show debbie 64
    show diane f_dinner_normal_talk
    dia "Why buy a barn outside of town that doesn't even fit my business model?"
    dia "Wouldn't it be much better to build a custom one on the land I already own?"
    show diane f_dinner_normal
    show debbie 64b
    show player f_diningroom_table_normal
    deb "Hmm?"
    show debbie 65
    deb "You don't have enough land to build a barn, {b}Diane{/b}..."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Well no, not yet..."
    dia "... But once I demolish the house, I think-"
    show diane f_dinner_normal
    show debbie 67 with dissolve
    show player f_diningroom_table_normal
    deb "You're gonna demolish your house?!"
    show debbie 64c with dissolve
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Sure, why not?"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "I dunno."
    deb "It's such a nice house..."
    show debbie 64
    show diane f_dinner_laugh
    show player f_magic_sit_stand_normal
    dia "Psh, it's not that nice!"
    show diane f_dinner_normal_talk
    dia "It's way too big for me and besides, all it does is remind me of that asshole ex-husband of mine..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Okay, but where will you live?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Ehh, I'm not certain about that part yet..."
    dia "I mean, I'm sure I can find something but I don't really have time to drag my feet on this."
    dia "If I'm gonna do it, I'll have to start construction right away!"
    dia "Otherwise I risk losing my customer base..."
    show diane f_dinner_normal
    deb "..."
    show debbie 65
    show player f_diningroom_table_normal
    deb "Do you even know anyone that's capable of building something like that?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Of course!"
    dia "One of my best customers is married to a carpenter."
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Hmm?"
    player_name "Oh, you mean {b}Annie's{/b} dad?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Yeah, his name is {b}Richard{/b}, right?"
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Yeah."
    player_name "He doesn't seem like a very nice guy though..."
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch
    dia "Well that's alright."
    dia "I don't need him to be nice!"
    dia "I just need him to be competent..."
    dia "... And cheap!"
    show diane f_dinner_laugh a_dinner_touch1
    show debbie 66
    dia "Haha!"
    deb "Haha!"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Well, you can always stay here with us while you look for a new place, you know?"
    show debbie 64
    show jenny f_breakfast_surprised with dissolve
    jen "( !!! )"
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    show diane a_dinner_normal with dissolve
    jen "What?!"
    show jenny f_breakfast_gross
    show diane f_dinner_normal_talk
    dia "Oh, I don't want to be a bother..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "It's no bother!"
    deb "You're as good as family and more than welcome to stay as long as you need!"
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "{b}[deb_name]{/b}, I really don't think it's a good idea-"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Shh, nobody's talking to you..."
    show diane f_dinner_normal
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "I think it's a wonderful idea!"
    deb "It'll give you kids a chance to bond with {b}Diane{/b}."
    deb "Plus we could really use the extra help around here, even if it's just temporary..."
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "Where's she gonna sleep?!"
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "We'll figure something out."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "The couch would suit me just fine."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_surprised_left
    jen "Ugh, this is a stupid fucking idea!"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Hey, don't talk to {b}[deb_name]{/b} like that!"
    show diane f_dinner_annoyed_left zorder 1
    show jenny f_breakfast_gross
    jen "..."
    show jenny f_breakfast_gross_talk
    jen "Whatever."
    jen "I'll be in my room."
    show jenny b_dinner_walking f_empty a_empty zorder 0 at Position (xpos=500) with dissolve
    pause
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Sheesh, that girl needs to learn some respect..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Oh, {b}Diane{/b}... Leave it be."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "I'm serious!"
    dia "My parent's would have never have let me talk to them like that."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "It's just a phase."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "If you say so..."
    show diane f_dinner_normal
    show player f_diningroom_table_normal_talk
    player_name "So {b}Diane{/b} is really gonna move in with us?"
    show player f_diningroom_table_normal
    show debbie 65
    deb "Sure!"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Just give me a couple days to get the construction plans sorted out."
    show diane f_dinner_normal
    show debbie 66
    show player f_diningroom_table_normal
    deb "Oh, this is so exciting!"
    show debbie 65
    show player f_magic_sit_stand_normal
    deb "It'll be just like those sleepovers we used to have when we were girls!"
    show diane f_dinner_laugh
    show debbie 66
    dia "Hahaha!"
    deb "Hahaha!"
    scene black with fade
    hide diane
    hide player
    hide table
    hide debbie
    scene location_home_entrance_night_blur
    show diane b_classy a_classy_sides f_normal_talk
    show debbie 91f
    show player 203 at left
    with dissolve
    dia "Well, I guess I'll head home and start packing!"
    show diane f_normal
    show debbie 92f
    deb "I can't wait!"
    show debbie 91f
    show diane f_laugh
    dia "Hehe, me neither!"
    hide debbie
    show diane dinner_hug4
    with dissolve
    dia "I'll see you really soon."
    show diane dinner_hug3
    deb "Be careful going home!"
    show debbie 91f
    show diane b_classy a_classy_sides f_normal_talk
    with dissolve
    dia "I always am."
    show debbie 91 at Position (xoffset=100)
    hide player
    show diane dinner_hug2
    with dissolve
    dia "Come by the house soon, {b}[firstname]{/b}."
    dia "I'll definitely need your help with all this."
    show diane dinner_hug1
    player_name "Y-yeah, okay."
    show debbie 91f
    show player 13 at left
    show diane b_classy a_classy_sides f_shamed_talk_smile
    with dissolve
    dia "And tell the princess I said bye."
    show diane f_normal
    show debbie 93f
    deb "Hehe, will do."
    hide debbie
    hide diane
    hide player
    with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["03_unlocked"] = True
    $ renpy.end_replay()
    return

label kitchen_diane_debbie_dinner_outfit:
    pause
    deb "Oh!"
    deb "{b}[firstname]{/b}, before you go, do you have a second to look at something?"
    show player 14
    show debbie 61
    player_name "Of course, {b}[deb_name]{/b}. What do you need?"
    show player 1
    show debbie 62
    deb "I have a new outfit for dinner tonight and I wanted to get your opinion."
    deb "Let me go put it on real fast."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "I'm excited to see {b}[deb_name]{/b} all dressed up!"
    show player 11
    deb "Sweetie!"
    deb "I'm ready!"
    show player 2
    player_name "Coming!"
    hide player with dissolve
    return

label kitchen_diane_meet_debbie_kitchen:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "There you are!"
    show debbie 3
    deb "I need your help with something..."
    show debbie 2
    show player 11
    deb "{b}Diane{/b} is coming over for dinner tonight."
    deb "... And I need you to pick up some {b}Sea Trout{/b} down at the {b}Pier{/b}."
    deb "I want to cook her something special and {b}Sea Trout{/b} is her absolute favorite!"
    show debbie 1
    show player 2
    player_name "That's a nice surprise!"
    player_name "It'll be good for her to get out of her house for awhile."
    player_name "I worry about her sometimes... All alone over there."
    player_name "I can swing by the {b}Pier{/b} and grab some {b}Sea Trout{/b} on my way home."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "Thanks, sweetie."
    return

label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Hey, sweetie!"
    deb "Hungry for some breakfast?"
    show debbie 51 at Position(xpos=1025)
    show player 10
    player_name "I don't know If I have time, {b}[deb_name]{/b}."
    if game.timer.is_weekend():
        player_name "I have to meet {b}Erik{/b} at his house..."
    else:
        player_name "I'm running late for school."
    show player 11
    show debbie 52
    deb "Honey, you have to eat!"
    show player 11
    if game.timer.is_weekend():
        deb "I don't care if your friend {b}Erik{/b} has to wait all day..."
    else:
        deb "I don't care if your school calls me to complain about you being late..."
    show player 1
    deb "You can't just go out on an empty stomach!"
    show player 14
    show debbie 51
    player_name "I guess I could take a few minutes to eat something..."
    show player 1
    show debbie 2
    deb "I prepared some cereal for you in the {b}dining room{/b}."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression game.timer.image("homekitchen{}")
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Good morning, sweetie! I made you some breakfast!"
    deb "I thought you'd like something special for your first day back at school."
    show player 2
    show debbie 1
    player_name "Thanks, {b}[deb_name]{/b} but I'm not really hungry and I'm running late for school. So..."
    show player 1
    show debbie 2
    deb "You're sure? I made your favorite..."
    deb "Happy face pancakes with three strips of baaaacon!"
    show debbie 1
    show player 10
    player_name "Oh man..."
    show player 11
    player_name "..."
    show player 10
    player_name "No, I really shouldn't..."
    player_name "I think {b}Erik{/b} overslept again and I don't wanna be late on my first day back."
    show player 11
    show debbie 3
    deb "Hah, again huh?"
    show player 1
    show debbie 2
    deb "Well I guess you'd better get a move on then."
    show player 2
    show debbie 1
    player_name "Yeah, thanks anyways, {b}[deb_name]{/b}!"
    show player 1f with dissolve
    show debbie 2
    deb "My pleasure, Sweet- Oh! Wait!"
    show player 1 with dissolve
    player_name "Hmm?"
    show debbie 3
    deb "I nearly forgot!"
    show debbie 2
    deb "I spoke with my friend {b}Diane{/b} yesterday and she mentioned that she could use some {b}help with her garden{/b} over the summer!"
    show player 10
    show debbie 1
    player_name "Hmm, I don't really know much about gardening {b}[deb_name]{/b}..."
    show player 11
    show debbie 3
    deb "Oh c'mon, It's easy! {b}Diane{/b} can teach you and if you do a good job she'll pay you as well!"
    show debbie 2
    deb "It could be a good way to {b}earn some money for college{/b}, don't you think?"
    show player 10
    show debbie 1
    player_name "Yeah, I guess you're right."
    show player 2
    player_name "I should go visit her and see what she wants me to do."
    show debbie 2
    deb "Atta' boy!"
    hide player
    show debbie 4b
    with dissolve
    deb "I know these last few weeks have been hard..."
    deb "But your {b}father{/b} would want you to carry on, you know?"
    deb "You'll get through this. I promise things will get better."
    show debbie 5b
    player_name "Yeah, I-I know. Thanks {b}[deb_name]{/b}..."
    deb "Chin up, sweetie! I'm here for you."
    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "There you are!"
    show debbie 3
    deb "I need your help with something..."
    show debbie 2
    show player 11
    deb "My friend {b}Diane{/b} is coming over for dinner tonight."
    deb "... And I need you to pick up some {b}Sea Trout{/b} down at the {b}Pier{/b}."
    deb "I want to cook her something special and it's her absolute favorite!"
    show debbie 1
    show player 2
    player_name "Oh, {b}Diane{/b} is coming over? That's a nice surprise!"
    player_name "It'll be good for her to get out of her house for awhile..."
    player_name "I worry about her sometimes... All alone over there."
    player_name "I'll swing by the {b}Pier{/b} and grab some {b}Sea Trout{/b} on my way home."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "{b}[firstname]{/b}, before you go, do you have a second to look at something?"
    show player 14
    show debbie 61
    player_name "Of course, {b}[deb_name]{/b}. What do you need?"
    show player 1
    show debbie 62
    deb "I have a new outfit for dinner tonight and I wanted to get your opinion."
    deb "Let me go put it on real fast."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "I'm excited to see {b}[deb_name]{/b} all dressed up!"
    show player 11
    deb "Sweetie!"
    deb "I'm ready!"
    show player 2
    player_name "Coming!"
    hide player with dissolve
    return

label kitchen_mom_debt_call:
    scene expression game.timer.image("homekitchen{}")
    show debbie 6 at right with dissolve
    deb "I've told you already! I don't {b}KNOW{/b} where the money is..."
    deb "I had no idea he was involved in any of this!"
    show debbie 7 at right
    deb "But-"
    show debbie 6 at right
    deb "I don't have it!!"
    show debbie 7 at right
    deb "..."
    show debbie 6 at right
    deb "Was that a {b}threat{/b}?!"
    deb "I'm hanging up now. Don't call back here again."
    show debbie 8 at right with hpunch
    deb "Just leave us {b}ALONE!!!{/b}"
    show debbie 9 at right
    show player 10 at left with dissolve
    player_name "..."
    player_name "...{b}[deb_name]{/b}?"
    player_name "...Are you okay?"
    show player 5 at left
    show debbie 11 at right
    deb "I'm alright, sweetie."
    show debbie 10 at right
    show player 10 at left
    player_name "Are you sure? It sounded pretty bad..."
    show player 5 at left
    show debbie 11 at right
    deb "It's nothing for you to worry about..."
    show debbie 10 at right
    show player 5 at left
    player_name "..."
    show player 10 at left
    player_name "I could try and find another job. Maybe I can come up with some money for you."
    show player 5 at left
    show debbie 11 at right
    deb "No."
    deb "Your {b}Father{/b} wouldn't want that, Sweetheart."
    deb "You need to keep your focus on school and {b}Save your money for tuition{/b}."
    show debbie 10 at right
    show player 10 at left
    player_name "Yeah, but {b}[deb_name]{/b}, I can help..."
    hide player 10 at left
    show debbie 12 at right
    with dissolve
    deb "Oh, sweetie..."
    deb "Just let me handle it and everything will be fine, okay? I promise."
    hide debbie with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane b_kitchen a_empty f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "... I don't see the problem. Isn't it a good thing that he's helping you around the house?"
    show diane f_normal
    show debbie 60f
    deb "I know, it's just..."
    deb "He's been so... affectionate towards me lately..."
    show diane f_laugh
    show debbie 59f
    dia "That's not surprising, he just lost the only family he ever had..."
    show diane f_normal_talk
    dia "He probably just needs someone he can feel close with..."
    dia "Especially with all this other stuff that's been happening to you guys."
    show diane f_normal
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "It's not that. There's more to it! It's the way he looks at me, you know?"
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane f_surprised
    dia "..."
    show diane f_normal_talk
    dia "What do you mean?"
    show diane f_normal
    show debbie 60f
    deb "Well, a little while ago I.. I started noticing things..."
    show diane f_normal_talk
    show debbie 59f
    dia "...Like?"
    show diane f_normal
    show debbie 60f
    deb "Like how he's always getting hard around me..."
    deb "... And touching me... in certain ways."
    show diane f_surprised
    show debbie 59f
    dia "..."
    show debbie 60f
    deb "... And the other day, I found him playing with himself; In my bed!"
    deb "... With my underwear!"
    show diane f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "What did you do?!"
    show diane f_normal
    show debbie 60f
    deb "We discussed it!"
    deb "I told him not to do that kind of stuff in my room, but..."
    show diane f_normal_talk
    show debbie 59f
    dia "But, what?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "I caught him again! He apologized and started talking about urges that he couldn't control..."
    show diane f_normal_talk
    show debbie 59f
    dia "Okay, so what did you say to that?"
    show diane f_surprised
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "... I kinda... Let him finish."
    show diane f_normal_talk
    show debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    dia "You watched him masturbate?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "I didn't know what to do!"
    deb "I thought maybe if he just got it out of his system..."
    deb "... You know?"
    show diane f_normal_talk
    show debbie 59f
    dia "That's so naughty..."
    show diane f_normal
    show debbie 60f
    deb "There's more..."
    show diane f_normal_talk
    show debbie 59f
    dia "More?!"
    dia "You're serious?!"
    dia "Tell me!"
    show diane f_surprised
    show debbie 60f
    deb "Diane..."
    show diane f_normal_talk
    show debbie 59f
    dia "{b}[deb_name]{/b}, tell me!"
    show diane f_surprised
    show debbie 60f
    deb "... We've been taking showers together."
    show diane f_normal_talk
    show debbie 59f
    dia "Wow..."
    show diane f_teasing
    dia "... How is he?"
    show diane f_surprised
    show debbie 60f
    deb "Diane!!"
    show diane f_laugh
    show debbie 59f
    dia "What?!"
    show diane f_thinking
    dia "Don't act like a prude! We both know you're dying to tell me!"
    show diane f_surprised
    show debbie 60f
    deb "... {b}*Sigh*{/b}"
    show diane f_teasing
    show debbie 59f
    dia "Did you... touch him?"
    show diane f_smirk
    show debbie 60f
    deb "... Yes."
    deb "I kinda, jerked him off..."
    show diane f_teasing
    show debbie 59f
    dia "All the way?"
    show diane f_smirk
    show debbie 60f
    deb "... Until he came, yeah."
    show debbie 59f
    if not M_diane.finished_state(S_diane_drunken_garden_work):
        show diane f_teasing
        dia "So how is it?"
        show diane f_smirk
        show debbie 60f
        deb "... How is what?"
        show diane f_teasing
        show debbie 59f
        dia "His {b}dick{/b}, {b}[deb_name]{/b}! Is it big?"
        show diane f_smirk
        show debbie 60f
        deb "( !!! )"
        show debbie 59f
        deb "..."
        show diane f_explain
        dia "Don't get shy on me now, girl. Spit it out!"
        show debbie 60f
        show diane f_smirk
        deb "{b}Diane{/b}, he's got the biggest... {b}Dick{/b} I've ever seen!"
        show diane f_teasing
        show debbie 59f
        dia "... You don't say?!"
    show diane f_laugh
    dia "I'm surprised you stopped at the handjob..."
    show diane f_smirk
    show debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    deb "{b}Diane{/b}, he's just a kid!"
    show diane f_teasing
    show debbie 15f
    dia "Pfft, he's in college!"
    show diane f_smirk
    show debbie 16f
    deb "Yeah, but I'm old enough to be his {b}Mother{/b}!"
    show diane f_laugh
    show debbie 15f
    dia "... But {b}you aren't{/b} his {b}Mother{/b}, {b}[deb_name]{/b}!"
    show diane f_normal
    show debbie 16f
    deb "Oh, I dunno, {b}Diane{/b}..."
    show diane f_surprised
    show debbie 15f
    dia "He obviously wants to."
    show diane f_normal
    show debbie 16f
    deb "Please, tell me I'm not doing something terribly wrong here..."
    show diane f_normal_talk
    show debbie 15f
    dia "It's your decision, but..."
    dia "I think you should relax and enjoy it a little. Who care's about the age difference?"
    show diane f_normal
    show debbie 16f
    deb "Really? You don't think it's wrong?"
    show diane f_normal_talk
    show debbie 15f
    dia "Nope. I don't see the harm in it!"
    show diane f_normal
    show debbie 16f
    deb "I suppose we aren't hurting anybody... And we're both consenting adults."
    show diane f_laugh
    show debbie 15f
    dia "Plus this is all really {b}HOT{/b}!"
    show diane f_normal
    show debbie 16f
    deb "You are such a bad influence! I don't know why I listen to you!"
    show diane f_normal_talk
    show debbie 15f
    dia "... Because you know I'm right! Just give it a chance. Who know's maybe it was meant to be?"
    show diane f_normal
    show debbie 62f at Position(xpos=0.3318,ypos=1.000)
    deb "Yeah, I suppose anything is possible..."
    show diane f_normal_talk
    show debbie 61f
    dia "Alright, well I'd better head home. It's getting late."
    show diane f_teasing
    dia "We'll continue this another time. I want all the juicy details for my spank bank!"
    show diane f_normal
    show debbie 62f
    deb "{b}Diane{/b}! You're terrible!"
    deb "Why don't you come by for dinner sometime? I'd love to see you more often!"
    show debbie 61f
    show diane f_normal_talk
    dia "I'm always down for dinner, {b}[deb_name]{/b}. Just as long as I'm not the one doing the cooking!"
    dia "Good luck, Honey."
    scene expression L_home_entrance.background
    show player 5
    player_name "( That... was a lot to take in. )"
    player_name "( {b}[deb_name]{/b} seemed really conflicted about all of this... )"
    show player 203
    player_name "( She said she's enjoying it, though. )"
    player_name "( Either way, I'm glad {b}Diane{/b} thinks it's okay for us to be doing these things! )"
    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show debbie 14b at right
    player_name "Aww, c'mon {b}[deb_name]{/b}!"
    player_name "You're the one who said I need to get out and start dating."
    player_name "It would definitely help if I knew how to kiss a girl properly, wouldn't it?"
    show player 1
    deb "..."
    show debbie 13
    deb "... Well."
    deb "Y-yeah, I suppose I could give you a few pointers."
    show debbie 14
    show player 2
    player_name "I would really appreciate it, {b}[deb_name]{/b}."
    show player 1
    show debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    deb "O-okay, umm... Come in close to me."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show debbie 72
    player_name "Alright."
    show player 227
    show debbie 73
    deb "Good. Now, lean in, that's it."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Okay."
    show player 227
    show debbie 73
    deb "... Close your eyes and gently press your lips against mine..."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    deb "Mmm."
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "How was that?"
    show player 227
    show debbie 77
    deb "... Wow."
    show player 227c
    show debbie 76
    player_name "Bad?"
    show player 227
    show debbie 73
    deb "N-no. That was quite good!"
    show player 227c
    show debbie 72
    player_name "Really?!"
    show player 227
    show debbie 73
    deb "Yeah. Are you sure this is your first time?"
    show player 227c
    show debbie 72
    player_name "Heh, yeah. Do you have any pointers?"
    show player 227
    deb "..."
    show debbie 73
    deb "Well, let's see..."
    deb "Oh, I know!"
    deb "Kiss me again and I'll show you a little trick!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80c
    player_name "( !!! )" with hpunch
    show debbie 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Whoa!"
    player_name "That thing you did with your tongue, that was so cool!"
    show player 227
    show debbie 75
    deb "Hehe, yeah."
    show debbie 73
    deb "It's just a little something I picked up awhile back..."
    show player 227c
    show debbie 72
    player_name "Hmm, can I try it?"
    show player 227
    show debbie 73
    deb "Oh... uh."
    show player 227c
    show debbie 72
    player_name "Please?"
    show player 227c
    show debbie 73
    deb "Y-yeah... Sure!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80b
    deb "( !!! )" with hpunch
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "How was that?!"
    show player 227
    deb "Mmm..."
    show player 227c
    player_name "{b}[deb_name]{/b}?"
    show player 227
    show debbie 77
    deb "Oh, sorry!"
    show debbie 75
    deb "That was REALLY good, sweetie!"
    deb "I mean, wow! You're gonna be quite the little heart breaker once you get out into the dating world!"
    show player 227c
    show debbie 76
    player_name "Really? Thanks {b}[deb_name]{/b}!"
    show player 227
    deb "Mmmhmm."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause 
    show debbie 77
    pause
    show debbie 74
    deb "Oh!"
    deb "Oh my..."
    show player 230
    player_name "..."
    show player 232
    player_name "Sorry, {b}[deb_name]{/b}."
    player_name "I didn't mean to..."
    show player 231
    show debbie 75
    deb "Hehe, it's okay, sweetie. It's perfectly understandable."
    show debbie 73
    deb "We'd better take a break though."
    show player 232
    show debbie 72
    player_name "... Yeah. O-okay."
    player_name "Do you think, maybe, we could do this again sometime?"
    show player 231
    deb "..."
    show player 232
    player_name "You know... Just for practice?"
    show player 231
    show debbie 73
    deb "I suppose that would be okay."
    deb "Just to practice though!"
    show player 232
    show debbie 72
    player_name "Yeah, of course!"
    show player 231
    show debbie 73
    deb "Alright. Feel free to ask me anytime."
    show player 232
    show debbie 72
    player_name "Thanks {b}[deb_name]{/b}!"
    show player 231
    show debbie 73
    deb "No problem, {b}[firstname]{/b}."
    show player 232
    show debbie 72
    player_name "See ya!"
    hide debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "That was awesome!"
    return

label kitchen_mom_dishes:
    scene expression player.location.background_closeup with None
    show debbie 116 at right
    with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    show player 1 at left with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 119 at Position(xpos=1014)
    deb "Oh, hey, sweetie!"
    show debbie 120
    show player 14
    player_name "Hey, {b}[deb_name]{/b}!"
    show debbie 119
    show player 1
    deb "You need something?"
    deb "I'm just finishing up the dishes..."
    show debbie 120
    return

label kitchen_mom_dishes_yes:
    show debbie 118
    show player 14
    player_name "Why don't you take a break for awhile?."
    player_name "I'll dry the rest."
    show debbie 119
    show player 1
    deb "That's very sweet but you don't have to do that."
    show debbie 118
    show player 14
    player_name "Nah, it's fine. I'm bored anyways."
    show debbie 119
    show player 1
    deb "Heh, well alright. If you're bored anyways..."
    show player 272
    show debbie 62
    deb "Just dry and store them away in the cupboard."
    show player 273
    show debbie 61
    player_name "Will do."
    show debbie 63
    show player 272
    deb "Thanks for helping out around here, {b}[firstname]{/b}."
    show player 274
    show debbie 61
    player_name "My pleasure, {b}[deb_name]{/b}."
    scene expression "backgrounds/location_home_cutscene01.jpg"
    show expression FilteredText("I don't think {b}[deb_name]{/b} had ever had help with dishes before... \nShe told me her late husband never did any work around the house and my {b}Dad{/b} only really helped with yard work or broken appliances. \nShe stayed with me in the kitchen until I was finished and we had a nice long chat. \nIt was nice getting to know {b}[deb_name]{/b} better...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show debbie 120 at Position(xpos=1014)
    player_name "Okay. I'll come back later, then."
    return

label kitchen_diane_debbie_evening_visit:
    scene expression "backgrounds/location_home_kitchen_secret.jpg"
    show diane b_kitchen a_empty
    show debbie 165bf at Position(xpos=0.3318,ypos=1.000)
    with dissolve
    deb "And you're getting plenty of rest?"
    show debbie 169bf
    show diane f_lookup
    dia "... Yes, Mom."
    show diane f_smirk
    show debbie 165f
    deb "Oh, hush!"
    show debbie 164f
    show diane f_laugh
    dia "Haha!"
    show diane f_normal
    show debbie 165f
    deb "I just worry about you is all."
    show debbie 164f
    show diane f_normal_talk
    dia "I know, {b}[deb_name]{/b} and I really do appreciate it..."
    dia "... But I've got everything under control, I promise!"
    dia "I've settled into a nice work schedule and {b}[firstname]{/b} has been making sure I stick to it."
    show diane f_normal
    show debbie 165bf
    deb "He doesn't know... About the... You know..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Mmm, yeah..."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Diane{/b}..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "I didn't mean for him to find out!"
    dia "He caught me that night you sent him over with the pie..."
    show diane f_shamed
    show debbie 169bf
    deb "..."
    show diane f_smirk_talk
    dia "Thanks for that, by the way."
    show diane f_smirk
    show debbie 164bf at Position (xoffset=10) with dissolve
    deb "..."
    show diane f_laugh
    dia "I mean, the pie was delicious!"
    show diane f_smirk
    show debbie 165bf with dissolve
    deb "You know, if you'd told me what you were up to from the start, I never would have sent him over to work in your garden this summer..."
    show debbie 169bf
    show diane f_laugh
    dia "Haha, well I guess it's a good thing I didn't tell you then, huh?"
    show diane f_smirk
    deb "..."
    show diane f_normal_talk
    dia "And besides, my garden has never looked better."
    dia "You should see the size of the crops {b}[firstname]{/b} is producing!"
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "You don't have him in there with you while you're doing it, do you?"
    show debbie 169bf
    show diane f_surprised_down
    dia "What?"
    show diane f_shamed_talk_smile
    dia "... Uhh, no. Not usually."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Diane{/b}!!!"
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "What?!"
    show diane f_shamed_talk
    dia "You know how he is!"
    dia "So determined he has to help out with every little thing..."
    show diane f_shamed_talk_smile
    dia "He keeps popping his head in and asking to lend a hand!"
    show diane f_shamed_talk_look
    dia "Then you go and get him all worked up about my health, so now it's practically impossible to keep him out!"
    show diane f_shamed
    show debbie 165bf
    deb "Hmm, it might be best if he stops working for you..."
    show debbie 169bf
    show diane f_shamed_talk
    dia "Oh, now you're just being ridiculous!"
    show diane f_shamed
    show debbie 165bf
    deb "You shouldn't be exposing him to-"
    show debbie 169bf
    show diane f_shamed_talk
    dia "He's not a kid anymore, {b}[deb_name]{/b}!"
    show diane f_normal_talk
    dia "I think he can handle seeing a pair of tits..."
    show diane f_normal
    deb "..."
    if M_mom.finished_state(S_mom_diane_visit):
        show diane f_smirk_talk
        dia "Besides, the stuff happening in my shed is far tamer than you're little shower sessions with him!"
        show diane f_smirk
        show debbie 164bf at Position (xoffset=10)
        deb "!!!" with hpunch
        show debbie 166df with dissolve
        deb "That's not- !!"
        show debbie 166cf
        deb "{b}*Sigh*{/b} I should never have told you about that..."
        show debbie 166ef
        show diane f_laugh
        dia "Haha, please!"
        show diane f_smirk_talk
        dia "Who else do you have to discuss these things with?!"
        dia "Besides, I think it's super hot!"
        show diane f_smirk
        show debbie 165bf
        deb "Yeah, I'm aware."
        show debbie 169bf
    else:
        show diane f_normal_talk
        dia "You're really making too big a deal of this, {b}[deb_name]{/b}!"
        dia "{b}[firstname]{/b} is really mature for his age."
        show diane f_normal
        deb "..."
        show diane f_explain
        dia "He's been a perfect gentleman about the whole thing."
        show diane f_normal_talk
        dia "You should spend more time with him and you'd see what I mean."
        show diane f_normal
        show debbie 165bf
        deb "You really think he can handle it?"
        show debbie 169bf
        show diane f_laugh
        dia "I'm positive!"
        show diane f_normal
        show debbie 166bf
        deb "( Hmm, maybe I should spend more time with him... )"
        show debbie 169bf
    show diane f_normal_talk
    dia "Look, I just can't afford to lose {b}[firstname]{/b} right now, {b}[deb_name]{/b}."
    dia "Not when my business is just taking off."
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "Things are really going that well, huh?"
    show debbie 169bf
    show diane f_laugh
    dia "Better than I ever imagined!"
    show diane f_normal_talk
    dia "I'm already looking into ways to expand."
    show diane f_normal
    show debbie 165bf
    deb "What do you mean expand?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Well, getting a proper work space for one thing."
    show diane f_normal
    show debbie 165bf
    deb "Workspace?"
    show debbie 169bf
    show diane f_laugh
    dia "Yeah!"
    show diane f_thinking
    dia "I was looking at the most adorable little barn the other day, about two hours drive outside of town."
    show diane f_normal_talk
    dia "I'll have to send you the pictures."
    show diane f_normal
    show debbie 168f
    deb "Barn?!"
    deb "You can't be serious!"
    show debbie 164f
    show diane f_explain
    dia "Heh I'm dead serious!"
    show diane f_normal_talk
    dia "You know I've always wanted one!"
    show diane f_normal
    show debbie 165f
    deb "Yeah but you have to admit, this isn't the kind of livestock you envisioned filling it with..."
    show debbie 164f
    show diane f_normal_talk
    dia "True."
    show diane f_smirk_talk
    dia "... This is way better than what I had planned!"
    show diane f_smirk
    show debbie 168f
    deb "Oh my gosh, you're such a wierdo..."
    show debbie 165f
    show diane f_laugh
    dia "Hahaha!"
    deb "Hahaha!"
    show diane f_normal
    deb "So where is this all going anyway?"
    deb "Are you eventually gonna start looking for more women to join your little milk business?"
    show debbie 164f
    show diane f_normal_talk
    dia "Yeah, maybe..."
    dia "I mean, I'm not there yet, but it's definitely something I've thought about..."
    show diane f_smirk_talk
    dia "... Is that your way of volunteering?"
    show diane f_smirk
    show debbie 168f
    deb "Pfft, yeah right!"
    show debbie 164f
    show diane f_laugh
    dia "Haha, c'mon!"
    show diane f_smirk
    show debbie 165f
    deb "No way!"
    deb "I'm not getting mixed up with all your silly dreams."
    show debbie 164f
    show diane f_smirk_talk
    dia "You are such a wet blanket sometimes..."
    dia "... But see, that's why I need {b}[firstname]{/b} to keep helping me!"
    dia "Nobody else will work as hard as he does..."
    show diane f_thinking
    dia "... At least nobody that I can afford to pay."
    show diane f_normal
    show debbie 169bf
    deb "..."
    show debbie 165bf
    deb "Ugh, fine."
    deb "... But I want you to promise me there won't be any funny business going on!"
    show debbie 169bf
    show diane f_normal_talk
    dia "Oh my gosh, stop worrying!"
    dia "I'll be on my best behaviour, I promise."
    show diane f_normal
    show debbie 169bf
    deb "Hmmph."
    show debbie 169bf
    dia "..."
    show debbie 165bf
    deb "Two hours?!"
    deb "Are all the barns you're looking at so far away?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Pretty much."
    dia "{b}Mayor Rump{/b} owns all the farm land just outside town and he's refusing to sell for some reason."
    dia "So I've been forced to look a bit further out."
    show diane f_normal
    show debbie 165bf
    deb "Gosh, what am I gonna do if you move away?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Oh, don't get all boo-hooey yet."
    dia "There's still time and who knows, I might find something closer."
    show diane f_normal
    deb "..."
    show diane f_laugh
    dia "If you keep making that face, it's gonna freeze that way..."
    show diane f_normal
    show debbie 168f
    deb "Heh, shut up!"
    show debbie 164f
    show diane f_laugh
    dia "Hahaha!"
    show diane f_surprised_down
    dia "Oh my gosh, look at the time..."
    show diane f_normal_talk
    dia "I've gotta get home and pump one more batch before bed."
    show diane f_normal
    show debbie 165f
    deb "Aww but you just got here!"
    show debbie 164f
    show diane f_shamed_talk_smile
    dia "I know, I'm sorry."
    show diane f_normal_talk
    dia "I'll call you tomorrow, okay?"
    show diane f_normal
    show debbie 165f
    deb "Yeah, okay."
    show debbie b_empty a_empty f_normal_talk at flip
    show debbie at Position (xpos=597)
    show diane b_hug_deb a_empty f_normal at Position (xpos=285)
    with dissolve
    deb "Be careful going home."
    show diane f_normal_talk
    show debbie f_normal
    dia "I will."
    show debbie at unflip
    show debbie 164f at Position(xpos=0.3318,ypos=1.000)
    show diane f_laugh b_casual a_casual_sides at lright
    with dissolve
    dia "Don't forget to try that milk I brought you!"
    show diane f_normal
    show debbie 165f
    deb "Ehh, we'll see..."
    show debbie 164f
    show diane f_normal_talk
    dia "I'm serious, {b}[deb_name]{/b}!"
    dia "Put a splash in your morning coffee or something."
    dia "You'll be hooked, I'm telling ya!"
    show diane f_normal
    show debbie 165f
    deb "Goodbye, {b}Diane{/b}..."
    show debbie 164f
    show diane f_laugh
    dia "Hahaha! See ya, {b}[deb_name]{/b}."
    scene black
    with fade
    hide diane
    hide debbie
    pause
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 5 at left with dissolve
    show diane b_casual a_casual_sides f_smirk_talk
    with dissolve
    dia "Oh, hey there {b}[firstname]{/b}!"
    dia "Are your ears burning?"
    show diane f_smirk
    show player 10
    player_name "Hmm?"
    show player 5
    show diane f_smirk_talk
    dia "We were just talking about you..."
    show diane f_smirk
    show player 29 with dissolve
    player_name "O-oh, yeah?"
    show player 3
    show diane f_smirk_talk
    dia "You coming by tomorrow?"
    show diane f_smirk
    show player 29
    player_name "I dunno, maybe..."
    show player 3
    show diane f_smirk_talk
    dia "Well, I hope you do."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 21 at left
    show diane f_smirk_talk b_casual a_casual_sides
    with dissolve
    dia "I'm gonna need those magic hands of yours for a big job real soon..."
    show diane f_smirk
    show player 28
    player_name "{b}*Gulp*{/b} O-okay."
    show player 21
    show diane f_laugh
    dia "Hehe."
    dia "See ya, stud!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Bye, {b}Diane{/b}."
    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
