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
    deb "О, {b}[jen_name]{/b}, может, уже забудешь?"
    show debbie 10b
    show jenny f_upset_talk
    jen "Нет, я не понимаю!"
    jen "Ты правда позволишь {b}Диане{/b} остаться?!"
    jen "Она трахалась с {b}[firstname]{/b}!"
    jen "Прямо здесь, в нашей гостиной!!"
    show jenny f_gross
    show debbie 11b
    deb "Я же сказала, я справилась."
    show debbie 10b
    show jenny f_upset_talk
    jen "Ты справилась с этим?!"
    jen "Что это вообще-"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "Доброе утро!"
    show player 13
    show jenny f_gross at unflip
    show jenny at Position (xpos=-200)
    show debbie 2
    deb "Доброе утро, милый!"
    show debbie 1
    show player 14
    player_name "Здесь чудесно пахнет!"
    show player 13
    show debbie 3
    deb "Хе-хе, я делаю твое любимое!"
    show debbie 1
    show player 14
    player_name "Блинчики со смайликами?!"
    show player 13
    show debbie 2
    deb "И три полоски бекона!"
    show debbie 1
    show player 17
    player_name "Ням!!"
    show player 18
    show debbie 3
    deb "Хехе!"
    hide player
    show debbie 4
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    pause
    show jenny f_eyeroll
    jen "Фу!"
    show jenny f_upset_talk
    jen "Вы, ребята, становитесь все страннее и страннее с каждым днем!"
    show jenny f_gross
    pause
    show jenny f_upset_talk
    jen "Неважно."
    jen "Мне уже все равно!"
    hide jenny with dissolve
    jen "Кучка чудаков!"
    show debbie 1
    show player 5f at left
    with dissolve
    pause
    deb "О, не обращай на нее внимания, {b}[firstname]{/b}."
    show player 5 with dissolve
    show debbie 2
    deb "Она просто драматизирует."
    deb "Ты же знаешь, какая она..."
    show debbie 1
    show player 10
    player_name "Да."
    show player 13
    pause
    show player 14
    player_name "{b}Диана{/b} уже уехала?"
    show player 13
    deb "Хмм?"
    show debbie 2
    deb "О, да... Она ушла еще до восхода солнца."
    deb "Сказала, что хочет начать день с чистого листа."
    deb "Похоже, у нее будет много работы для тебя."
    show debbie 1
    show player 29 with dissolve
    player_name "Хех, М-да... Работа."
    show player 13 with dissolve
    show debbie 2
    deb "Давай, нам лучше положить тебе немного еды."
    deb "Тебе понадобится много энергии, чтобы не отставать от {b}Дианы{/b}!"
    show debbie 1
    show player 14
    player_name "Хорошо, {b}[deb_name]{/b}."
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
    player_name "Доброе утро."
    show player 13
    show jenny f_eyeroll
    show debbie 2
    deb "Доброе утро, милый!"
    show debbie 1
    show jenny f_upset
    show player 10
    player_name "Где {b}Диана{/b}?"
    show player 13 with None
    show jenny at unflip
    show jenny zorder 0 at Position (xpos=-200)
    with dissolve
    deb "Хмм?"
    show debbie 2
    deb "О, она ушла рано утром, взволнованная чем-то."
    show debbie 1
    show player 14
    player_name "Взволнованная?"
    show player 13
    show debbie 2
    deb "Да, она была еще более возбуждена, чем в то утро, когда ее сарай был закончен."
    show debbie 1
    show player 14
    player_name "Правда?"
    show player 13
    show jenny f_upset_talk
    jen "Она такая странная..."
    show jenny f_upset
    show debbie 13
    deb "О, тише."
    show debbie 14
    show jenny f_eyeroll
    jen "Так и есть!"
    show jenny f_upset
    show debbie 13
    deb "{b}[jen_name]{/b}!"
    show debbie 14b
    pause
    show debbie 2
    deb "{b}Диана{/b} сказала тебе, что происходит?"
    show debbie 1
    show player 29 with dissolve
    player_name "О, эээ..."
    player_name "Нет."
    show player 14 with dissolve
    player_name "Наверное, мне стоит пойти туда и посмотреть, что она задумала..."
    show player 13
    show debbie 2
    deb "Ну, погоди-ка."
    deb "Тебе нужно позавтракать!"
    show debbie 1
    show player 14
    player_name "Нет, спасибо."
    player_name "Я не голоден."
    show player 13
    show debbie 2
    deb "Цц, нехорошо пропускать завтрак, {b}[firstname]{/b}."
    show debbie 1
    show player 14
    player_name "Правда {b}[deb_name]{/b}, я в порядке."
    player_name "Спасибо!"
    show player 13
    deb "..."
    show debbie 2
    deb "Хорошо."
    show debbie 1
    show player 14
    player_name "Увидимся вечером."
    show player 13
    show debbie 2
    deb "Будь осторожен, милый."
    show debbie 1
    hide player with dissolve
    pause
    show jenny f_gross
    jen "..."
    show jenny f_upset_talk
    jen "Что-то странное происходит с этими двумя."
    show jenny f_upset
    show debbie 2
    deb "Что ты имеешь в виду?"
    show debbie 1 with None
    show jenny at flip
    show jenny at Position (xpos=0)
    with dissolve
    jen "..."
    show debbie 2
    deb "Они просто в восторге от нового бизнеса."
    show debbie 1
    show jenny f_upset_talk
    jen "Да, ага, точно."
    show jenny f_upset
    show debbie 14
    deb "Хмм?"
    show jenny f_upset_talk
    jen "Тьфу, ничего. Неважно."
    jen "Я буду в своей комнате."
    hide jenny with dissolve
    show debbie 13
    deb "Хорошо, дорогая."
    hide debbie with dissolve
    return

label kitchen_diane_barn_news:
    scene expression "backgrounds/location_home_kitchen_day_closeup.jpg"
    show jenny a_dressed_juice f_gross
    show diane nightgown_dip
    with dissolve
    deb "Хахаха!"
    show jenny f_normal_talk
    jen "Вы, ребята, такие странные... Я ухожу отсюда."
    show jenny f_normal zorder 1 at Position (xpos=100)
    show diane b_nightgown a_nightgown_sides f_smirk_talk at Position (xpos=400)
    show debbie 1 zorder 2 at right
    with dissolve
    dia "В чем дело, принцесса?"
    show jenny at flip
    show jenny at Position (xpos=600)
    with dissolve
    dia "Ты ревнуешь?"
    show diane f_smirk
    show jenny f_eyeroll
    jen "Пф."
    show jenny f_normal at unflip
    show jenny at Position (xpos=100)
    with dissolve
    show diane f_smirk_talk
    dia "Не сердись, я тебя тоже покатаю."
    show diane f_smirk a_nightgown_slap
    show jenny f_surprised_back
    jen "!!!" with hpunch
    show diane f_laugh a_nightgown_sides
    show jenny f_upset_talk at flip
    show jenny at Position (xpos=640)
    with dissolve
    jen "Н-ни за что!"
    show jenny f_upset
    dia "Ха-ха-ха, посмотри на эти розовые щечки!"
    show debbie 3
    deb "Хаха!"
    show jenny f_eyeroll
    jen "Тьфу, шаддап!"
    show jenny f_upset
    show player 14 at left with dissolve
    player_name "Что происходит?"
    show player 13
    show debbie 1
    show diane f_normal_talk
    dia "{b}[firstname]{/b}!!!"
    show diane f_normal
    show debbie 2
    deb "Доброе утро, милый."
    show debbie 1
    show diane f_laugh
    dia "Готово, готово, гооотооовооо!!!"
    show diane f_cheese
    show player 13
    player_name "Хмм?"
    show player 17
    player_name "Подожди, ты хочешь сказать, что амбар готов?!"
    show player 13
    show diane f_normal_talk
    dia "Бинго!"
    dia "{b}Ричард{/b} только что позвонил и сказал что все готово."
    show diane f_normal
    show jenny f_eyeroll
    jen "Я не понимаю."
    show jenny f_normal_talk
    jen "Лучше иметь дом, чем дурацкий сарай."
    show jenny f_normal
    show diane f_smirk_talk
    dia "Да, я бы предпочла веселого соседа, чем кислую кошечку."
    show diane f_smirk
    show debbie 13
    deb "{b}*вздыхая*{/b} Вы двое..."
    show debbie 14
    show player 14
    player_name "Ну, я в восторге!"
    show player 13
    show diane f_normal_talk
    dia "Видишь!!"
    dia "{b}[firstname]{/b} знает, как реагировать на хорошие новости!"
    hide player
    show diane nightgown_hug2
    show jenny f_gross at unflip
    show jenny at Position (xpos=350)
    with dissolve
    dia "Спасибо, {b}[firstname]{/b}!"
    show diane nightgown_hug3
    player_name "Да."
    show diane nightgown_hug4
    show jenny f_upset_talk
    jen "Фу, неважно."
    jen "Я буду в своей комнате."
    hide jenny with dissolve
    pause
    show diane b_nightgown a_nightgown_sides at Position (xpos=250)
    show player 14 at left
    with dissolve
    player_name "Так мы направляемся туда?"
    show player 13
    show diane f_normal_talk
    dia "Конечно!"
    show diane f_normal
    show debbie 2
    deb "Э Э Э!"
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "После завтрака!"
    show debbie 1
    show diane f_laugh
    dia "Но, маааамммма!"
    show diane f_normal
    show debbie 2
    deb "{b}Диана{/b}, это самая важная еда за день."
    show debbie 1
    show diane f_normal_talk
    dia "Я ждала этого почти тридцать лет, я ухожу!"
    dia "Мы просто должны съесть большой ужин!"
    show diane at unflip
    show diane f_smirk_talk at Position (xpos=250)
    with dissolve
    dia "Верно, {b}[firstname]{/b}?!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Я эээ..."
    show player 3
    show debbie 3
    deb "Хахаха, хорошо."
    show debbie 2
    show diane at flip
    show diane at Position (xpos=750)
    with dissolve
    deb "Иди развлекайся."
    show player 13
    hide debbie
    show diane f_normal_talk b_nightgown_hug1 a_empty at flip
    show diane at Position (xpos=904)
    with dissolve
    dia "Спасибо!"
    show debbie 1 at right
    show diane b_nightgown a_nightgown_sides f_normal_talk at unflip
    show diane at Position (xpos=250)
    with dissolve
    dia "Пошли, {b}[firstname]{/b}!"
    dia "{b}Пойдем посмотрим новый сарай!{/b}"
    hide diane with dissolve
    show debbie 2
    deb "Только оденься сначала!"
    show debbie 1
    show player 14
    player_name "Хе-хе, я никогда не видел ее такой взволнованной..."
    show player 13
    show debbie 2
    deb "Да, тебе лучше пойти с ней."
    hide player
    show debbie 4
    with dissolve
    pause
    show debbie 5
    player_name "Хорошо, увидимся вечером {b}[deb_name]{/b}."
    show debbie 2 with dissolve
    deb "Береги себя!"
    hide debbie with dissolve
    return

label kitchen_diane_dinner:
    scene location_home_kitchen_day_blur
    show player 14 at left
    show debbie 1 at right
    with dissolve
    player_name "Привет, {b}[deb_name]{/b}. Я добыл {b}рыбу{/b} которая тебе нужна."
    show player 13
    show debbie 2
    deb "Спасибо, милый! Теперь я могу закончить ужин."
    deb "Я дам тебе знать, когда все закончится, хорошо?"
    show player 203

    scene black

    scene expression L_home_entrance.background
    show diane b_classy a_classy_sides f_normal_talk at Position (xpos=600)
    show debbie 91f
    with dissolve
    dia "Ммм, это {b}морской форелью{/b} пахнет?!"
    dia "Чувствуешь?!"
    show diane f_normal
    show debbie 93f
    deb "Конечно, я чувствую!"
    deb "Я знаю, как правильно обращаться с моей девочкой!"
    show diane f_laugh
    show debbie 91f
    dia "Боже мой, я бы могла расцеловать тебя прямо сейчас!"
    show player 203 at left with dissolve
    show diane f_normal_talk
    dia "Это все он..."
    dia "... {b}мужчина дома{/b}!"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 17
    player_name "Это платье отлично на тебе смотрится!"
    show diane f_laugh
    show player 203
    dia "Ой, ну хватит!"
    show player 13
    show diane f_normal
    show debbie 93f
    deb "Он такой обаятельный, правда?"
    show diane f_normal_talk
    show debbie 91f
    dia "Я не знаю, как тебе удается держать свои руки подальше от него!"
    dia "Где твой другой жилец? Она присоединится к нам сегодня вечером или у нее встреча с сучками из Саммервилля?"
    show player 10
    show diane f_normal
    player_name "Нет, она будет есть с нами."
    show player 12
    player_name "... Она наверху, готовится."
    show player 203
    show diane f_laugh
    dia "Типичная принцесса..."
    show diane f_normal_talk
    dia "Ну, я ее не жду! Не тогда, когда в меню {b}морская форель{/b}, приготовленная {b}[deb_name]{/b}!"
    show debbie 92f
    show diane f_normal
    deb "Эй, веди себя хорошо!"
    show debbie 93f
    deb "Она не так плоха, как ты думаешь..."
    show debbie 91f
    show diane f_laugh
    dia "Хех, если ты так считаешь."
    show debbie 93f
    show diane f_normal
    deb "Да. А теперь вы оба идите туда и сядьте, пока я достану бутылку вина!"
    show debbie 92f
    deb "У меня есть этот новый бренд, я хочу, чтобы ты попробовала."
    hide debbie
    hide diane
    with dissolve
    show player 14
    player_name "Я должен присоединиться к ним в {b}столовой{/b}."
    player_name "Еда {b}[deb_name]{/b} пахнет вкусно!"
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
    deb "... школа действительно столько заказала?!"
    deb "Хорошо, что у тебя есть {b}[firstname]{/b}, чтобы помочь тебе, да?"
    show jenny 45 with dissolve
    deb "Кажется, он теперь всегда там."
    show debbie 64
    show jenny b_dinner_casual f_breakfast_surprised a_breakfast_dressed_spoon with dissolve
    show player f_magic_sit_stand_laugh
    show diane f_dinner_normal_talk
    dia "Ну, есть так много работы, которую нужно сделать между садом и молочным бизнесом."
    dia "... И он действительно показал склонность к этому!"
    show diane f_dinner_normal
    show player f_diningroom_table_normal
    show debbie 65
    deb "О, правда?"
    show jenny f_breakfast_gross
    show debbie 64
    show diane f_dinner_normal_talk a_dinner_hand with dissolve
    show player f_magic_sit_stand_normal
    dia "О, да."
    dia "Ты должна гордиться им, {b}[deb_name]{/b}!"
    dia "Он такой ответственный молодой человек."
    show jenny b_dinner_casual_side f_empty a_dinner_casual_side1 with dissolve
    show player f_diningroom_table_surprised_left a_dinner_sitting_touch1
    show diane f_dinner_normal a_dinner_hand2 b_dinner_open
    with dissolve
    player_name "( !!! )"
    show jenny a_dinner_casual_side2 with dissolve
    show diane f_dinner_normal_talk
    dia "... Очень умный..."
    dia "... И сильный..."
    show player f_diningroom_table_surprised_teeth_left a_dinner_sitting_touch2
    show diane a_dinner_hand3
    with dissolve
    dia "... И нежный."
    show jenny a_dinner_casual_side1 with dissolve
    show diane f_dinner_normal
    player_name "{b}*глоток*{/b}"
    show debbie 65
    deb "Конечно, я горжусь им!"
    if M_mom.finished_state(S_mom_diane_visit) or store._in_replay is not None:
        show debbie 67 with dissolve
        deb "В последнее время он тоже стал здесь лучше."
        show debbie 68 with dissolve
        player_name "( !!! )"
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "Помогает по хозяйству..."
        deb "... Делает ремонт по дому..."
        show debbie 69 with dissolve
        pause
        show debbie 71 with dissolve
        deb "... Он хорошо заботится о {b}[jen_name]{/b} и мне."
        show debbie 69 with dissolve
        player_name "Хехехе, Я-"
        show debbie 68 with dissolve
        player_name "...т.е., это-"
    show player od_dinner_sitting_boner
    show jenny f_breakfast_gross_talk b_dinner_casual a_breakfast_dressed_spoon
    show player_dick 222
    with dissolve
    jen "Ух, вся эта хрень с голубками меня вырвет..."
    show diane f_dinner_annoyed_left_talk
    dia "Нам не нужны комментарии с галерки, {b}[jen_name]{/b}..."
    dia "Просто ешь свой ужин и молчи."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    jen "Пф, неважно..."
    show jenny f_breakfast_gross
    pause
    show jenny f_breakfast_gross_talk
    jen "Вы ведете себя странно."
    show jenny f_breakfast_gross
    pause
    jen "Хмм..."
    show jenny f_breakfast_grin_down_talk a_dinner_casual_drop with dissolve
    jen "... Упс."
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
        jen "( Какого хрена... )"
    show debbie 65
    show diane f_dinner_normal
    deb "Вам удалось найти новое рабочее место?"
    show debbie 64
    show jenny b_dinner_casual_bending f_empty a_empty at Position (xpos=200) with dissolve
    dia "Хмм?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch1
    with dissolve
    dia "Ох, ох... Нет, к сожалению, рядом с городом ничего нет."
    show diane f_dinner_normal a_dinner_touch
    show debbie 64d
    show player f_diningroom_table_normal
    deb "Пожалуйста, скажи мне, что ты на самом деле не собираешься уходить от нас..."
    show jenny f_breakfast_gross b_dinner_casual a_breakfast_dressed_spoon at Position (xpos=300)
    show debbie 64c
    show diane f_dinner_normal_talk a_dinner_touch1
    show player f_magic_sit_stand_normal
    with dissolve
    dia "Нет, если я могу помочь!"
    show jenny f_breakfast_surprised
    dia "{b}[firstname]{/b} на днях мне пришла в голову хорошая идея..."
    show diane f_dinner_normal
    show debbie 65
    show jenny f_breakfast_normal_closed a_dinner_casual_facepalm with dissolve
    deb "Да?"
    show debbie 64
    show diane f_dinner_normal_talk
    dia "Зачем покупать сарай за городом, который даже не соответствует моей бизнес-модели?"
    dia "Не лучше ли было бы построить новый на земле, которой я уже владею?"
    show diane f_dinner_normal
    show debbie 64b
    show player f_diningroom_table_normal
    deb "Хмм?"
    show debbie 65
    deb "У тебя нет достаточно земли, чтобы построить сарай, {b}Диана{/b}..."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Нет, пока нет..."
    dia "... Но как только я снесу дом, я думаю-"
    show diane f_dinner_normal
    show debbie 67 with dissolve
    show player f_diningroom_table_normal
    deb "Ты собираешься снести свой дом?!"
    show debbie 64c with dissolve
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Конечно, почему бы и нет?"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Не знаю."
    deb "Это такой хороший дом..."
    show debbie 64
    show diane f_dinner_laugh
    show player f_magic_sit_stand_normal
    dia "Пф, не такой он уж хороший!"
    show diane f_dinner_normal_talk
    dia "Он слишком велик для меня и, кроме того, все, что он делает, это напоминает мне о моем бывшем муже..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Хорошо, но где ты будешь жить?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Я пока не уверена насчет этого..."
    dia "Я имею в виду, я уверена, что смогу что-то найти, но у меня нет времени, чтобы затягивать это."
    dia "Если я собираюсь это сделать, я должна начать строительство прямо сейчас!"
    dia "В противном случае я рискую потерять свою клиентскую базу..."
    show diane f_dinner_normal
    deb "..."
    show debbie 65
    show player f_diningroom_table_normal
    deb "Ты вообще знаешь кого-нибудь, кто способен построить что-то подобное?"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Конечно!"
    dia "Один из моих лучших клиентов замужем за плотником."
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Хмм?"
    player_name "О, ты имеешь в виду отца {b}Энни{/b}?"
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Да, его зовут {b}Ричард{/b}, верно?"
    show diane f_dinner_normal
    show player f_magic_sit_stand_normal_talk
    player_name "Да."
    player_name "Хотя он не кажется очень хорошим парнем..."
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk a_dinner_touch
    dia "Что ж, все в порядке."
    dia "Мне не нужно, чтобы он был милым!"
    dia "Мне просто нужно, чтобы он был компетентным..."
    dia "... И дешев!"
    show diane f_dinner_laugh a_dinner_touch1
    show debbie 66
    dia "Хаха!"
    deb "Хаха!"
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Ну, ты всегда можешь остаться здесь с нами, пока ищешь новое место, понимаешь?"
    show debbie 64
    show jenny f_breakfast_surprised with dissolve
    jen "( !!! )"
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    show diane a_dinner_normal with dissolve
    jen "Что?!"
    show jenny f_breakfast_gross
    show diane f_dinner_normal_talk
    dia "О, я не хочу быть обузой..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Не беспокойся!"
    deb "Ты как член семьи и более чем, добро пожаловать, можешь остаться так долго, как тебе нужно!"
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "{b}[deb_name]{/b}, Я действительно не думаю, что это хорошая идея-"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Шшш, никто с тобой не разговаривает..."
    show diane f_dinner_normal
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "Я думаю, это замечательная идея!"
    deb "Это даст вам шанс сблизиться с {b}Дианой{/b}."
    deb "К тому же нам бы не помешала дополнительная помощь, пусть даже временная..."
    show debbie 64
    show jenny f_breakfast_gross_talk
    show player f_diningroom_table_surprised_left
    jen "Где она будет спать?!"
    show jenny f_breakfast_gross
    show debbie 65
    show player f_diningroom_table_normal
    deb "Мы что-нибудь придумаем."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Диван меня вполне устроит."
    show diane f_dinner_normal
    show jenny f_breakfast_eyeroll
    show player f_diningroom_table_surprised_left
    jen "Это, блядь, глупая идея!"
    show jenny f_breakfast_gross
    show diane f_dinner_annoyed_left_talk
    dia "Эй, не говори так с {b}[deb_name]{/b}!"
    show diane f_dinner_annoyed_left zorder 1
    show jenny f_breakfast_gross
    jen "..."
    show jenny f_breakfast_gross_talk
    jen "Неважно."
    jen "Я буду в своей комнате."
    show jenny b_dinner_walking f_empty a_empty zorder 0 at Position (xpos=500) with dissolve
    pause
    hide jenny with dissolve
    pause
    show player f_magic_sit_stand_normal
    show diane f_dinner_normal_talk
    dia "Блин, этой девочке нужно научиться уважению..."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "О, {b}Диана{/b}... Оставь ее."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Я серьезно!"
    dia "Родители никогда бы не позволили мне так с ними разговаривать."
    show diane f_dinner_normal
    show debbie 65
    show player f_diningroom_table_normal
    deb "Это просто переходной период."
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Как скажешь..."
    show diane f_dinner_normal
    show player f_diningroom_table_normal_talk
    player_name "{b}Диана{/b} действительно переедет к нам?"
    show player f_diningroom_table_normal
    show debbie 65
    deb "Да!"
    show debbie 64
    show diane f_dinner_normal_talk
    show player f_magic_sit_stand_normal
    dia "Просто дай мне пару дней, чтобы разобраться с планами строительства."
    show diane f_dinner_normal
    show debbie 66
    show player f_diningroom_table_normal
    deb "О, это так волнующе!"
    show debbie 65
    show player f_magic_sit_stand_normal
    deb "Это будет как те ночевки, которые мы устраивали, когда были девочками!"
    show diane f_dinner_laugh
    show debbie 66
    dia "Хахаха!"
    deb "Хахаха!"
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
    dia "Что ж, я пойду домой и начну собираться!"
    show diane f_normal
    show debbie 92f
    deb "Не могу ждать!"
    show debbie 91f
    show diane f_laugh
    dia "Хе-хе, я тоже!"
    hide debbie
    show diane dinner_hug4
    with dissolve
    dia "Скоро увидимся."
    show diane dinner_hug3
    deb "Будь осторожна!"
    show debbie 91f
    show diane b_classy a_classy_sides f_normal_talk
    with dissolve
    dia "Я всегда осторожна."
    show debbie 91 at Position (xoffset=100)
    hide player
    show diane dinner_hug2
    with dissolve
    dia "Приходи домой поскорее, {b}[firstname]{/b}."
    dia "Мне определенно понадобится твоя помощь со всем этим."
    show diane dinner_hug1
    player_name "Да, хорошо."
    show debbie 91f
    show player 13 at left
    show diane b_classy a_classy_sides f_shamed_talk_smile
    with dissolve
    dia "И передай принцессе, что я попрощалась."
    show diane f_normal
    show debbie 93f
    deb "Хехе, хорошо."
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
    deb "О!"
    deb "{b}[firstname]{/b}, перед уходом, у тебя есть минутка на кое-что посмотреть?"
    show player 14
    show debbie 61
    player_name "Конечно, {b}[deb_name]{/b}. Что тебе нужно?"
    show player 1
    show debbie 62
    deb "У меня сегодня на ужин новый наряд, и я хотела узнать твое мнение."
    deb "Позволь мне надеть его, я очень быстро."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "Я взволнован, чтобы увидеть наряд {b}[deb_name]{/b}!"
    show player 11
    deb "Милый!"
    deb "Я готова!"
    show player 2
    player_name "Вхожу!"
    hide player with dissolve
    return

label kitchen_diane_meet_debbie_kitchen:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "Вот ты где!"
    show debbie 3
    deb "Мне нужна твоя помощь..."
    show debbie 2
    show player 11
    deb "{b}Диана{/b} придет сегодня на ужин."
    deb "... И мне нужно, чтобы ты купил немного {b}морской форели{/b} на {b}пирсе{/b}."
    deb "Я хочу приготовить ей что-то особенное,а {b}морская форель{/b} - ее любимое блюдо!"
    show debbie 1
    show player 2
    player_name "Какой приятный сюрприз!"
    player_name "Ей будет полезно на некоторое время выбраться из дома."
    player_name "Иногда я беспокоюсь о ней... Совсем одна там."
    player_name "Я могу заскочить на {b}пирс{/b} и прихватить немного {b}морской форели{/b} по дороге домой."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "Спасибо, милый."
    return

label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Привет, милый!"
    deb "Хочешь позавтракать?"
    show debbie 51 at Position(xpos=1025)
    show player 10
    player_name "Не думаю, что у меня есть время, {b}[deb_name]{/b}."
    if game.timer.is_weekend():
        player_name "Я должен встретиться с {b}Эриком{/b}..."
    else:
        player_name "Желательно ещё и в школу не опоздать."
    show player 11
    show debbie 52
    deb "Милый, ты должен поесть!"
    show player 11
    if game.timer.is_weekend():
        deb "Мне не важно, что {b}Эрик{/b} будет ждать тебя..."
    else:
        deb "Мне не важно, будут ли звонить из школы, жалуясь на то, что ты опоздал..."
    show player 1
    deb "Но ты не можешь уйти с пустым животом!"
    show player 14
    show debbie 51
    player_name "Ладно, я думаю, что у меня есть пара минут, чтобы перекусить..."
    show player 1
    show debbie 2
    deb "В {b}столовой{/b} тебя ждет несколько тостов."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression game.timer.image("homekitchen{}")
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Доброе утро, любимый! Я приготовила тебе завтрак!"
    deb "Для первого дня в школе я приготовила тебе что-то особенное."
    show player 2
    show debbie 1
    player_name "Спасибо, {b}[deb_name]{/b}, но я не очень голоден да и в школу опаздываю. Так что..."
    show player 1
    show debbie 2
    deb "Ты уверен? Я сделала твои любимые..."
    deb "Улыбающиеся блинчики с тремя кусочками бекона!"
    show debbie 1
    show player 10
    player_name "О боже..."
    show player 11
    player_name "..."
    show player 10
    player_name "Нет, я правда..."
    player_name "Я думаю, что {b}Эрик{/b} опять проспал, а я не хочу опаздывать в первый же день."
    show player 11
    show debbie 3
    deb "Ха, опять?"
    show player 1
    show debbie 2
    deb "Ну тогда тебе следует поспешить."
    show player 2
    show debbie 1
    player_name "Да, всё равно спасибо, {b}[deb_name]{/b}!"
    show player 1f with dissolve
    show debbie 2
    deb "Ничего страшного, Милый- Ой! Подожди!"
    show player 1 with dissolve
    player_name "Хмм?"
    show debbie 3
    deb "Я почти забыла!"
    show debbie 2
    deb "Я вчера говорила с моей подругой, {b}Дианой{/b}, и она сказала, что летом ей может понадобиться {b}помощь с садом{/b}!"
    show player 10
    show debbie 1
    player_name "Хмм, я знаю не так много о садоводстве, {b}[deb_name]{/b}..."
    show player 11
    show debbie 3
    deb "Да ладно, это же просто! {b}Диана{/b} всему тебя научит, а может ещё и заплатит, если будешь стараться!"
    show debbie 2
    deb "Это может стать неплохим способом {b}заработать денег на коледж{/b}, что думаешь?"
    show player 10
    show debbie 1
    player_name "Да, думаю, ты права."
    show player 2
    player_name "Я зайду к ней и спрошу, чем могу помочь."
    show debbie 2
    deb "Это мой мальчик!"
    hide player
    show debbie 4b
    with dissolve
    deb "Я понимаю, что последние недели были непростыми..."
    deb "Но твой {b}отец{/b} хотел бы, чтобы ты был сильным."
    deb "Ты справишься с этим. Я обещаю, скоро всё наладится."
    show debbie 5b
    player_name "Да, я знаю. Спасибо {b}[deb_name]{/b}..."
    deb "Выше нос, милый! Я буду рядом."
    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "А вот и ты!"
    show debbie 3
    deb "Мне нужна твоя помощь..."
    show debbie 2
    show player 11
    deb "Моя подруга {b}Диана{/b} прийдет сегодня на ужин."
    deb "... Тебе нужно пойти на {b}пристань{/b} и купить {b}морскую форель{/b}."
    deb "Я хочу приготовить ей что-нибудь особенное, а морскую форель она как раз очень любит!"
    show debbie 1
    show player 2
    player_name "Ох, {b}Диана{/b} сегодня придет? Это приятный сюрприз!"
    player_name "Ей будет полезно хоть не на долго выйти из дома..."
    player_name "Я переживавю за неё... Она там совсем одна."
    player_name "Я зайду на {b}пристань{/b} на обратном пути и возьму {b}форель{/b}."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "{b}[firstname]{/b}, пока ты тут, можешь посмотреть на кое-что?"
    show player 14
    show debbie 61
    player_name "Конечно, {b}[deb_name]{/b}. Что тебе нужно?"
    show player 1
    show debbie 62
    deb "Я купила немного одежды для сегодняшнего вечера, мне хотелось бы узнать твое мнение."
    deb "Я сейчас быстро всё надену."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "Я хочу увидеть {b}[deb_name]{/b} при параде!"
    show player 11
    deb "Милый!"
    deb "Я готова!"
    show player 2
    player_name "Уже иду!"
    hide player with dissolve
    return

label kitchen_mom_debt_call:
    scene expression game.timer.image("homekitchen{}")
    show debbie 6 at right with dissolve
    deb "Я ведь уже вам сказала! Я не {b}ЗНАЮ{/b} где деньги..."
    deb "Я понятия не имела о том, куда он втянут!"
    show debbie 7 at right
    deb "Но-"
    show debbie 6 at right
    deb "У меня нет столько!!"
    show debbie 7 at right
    deb "..."
    show debbie 6 at right
    deb "Это была {b}угроза{/b}?!"
    deb "Я кладу трубку. Не звоните сюда больше."
    show debbie 8 at right with hpunch
    deb "Просто оставьте нас {b}В ПОКОЕ!!!{/b}"
    show debbie 9 at right
    show player 10 at left with dissolve
    player_name "..."
    player_name "...{b}[deb_name]{/b}?"
    player_name "...Ты в порядке?"
    show player 5 at left
    show debbie 11 at right
    deb "Со мной всё хорошо, милый."
    show debbie 10 at right
    show player 10 at left
    player_name "Ты уверена? Это звучало не очень хорошо..."
    show player 5 at left
    show debbie 11 at right
    deb "Тебе не о чем беспокоиться..."
    show debbie 10 at right
    show player 5 at left
    player_name "..."
    show player 10 at left
    player_name "Я могу попытаться найти хорошую работу. Может я смогу заработать немного денег."
    show player 5 at left
    show debbie 11 at right
    deb "Нет."
    deb "Твой {b}отец{/b} не хотел бы этого, милый."
    deb "Тебе нужно сфокусироваться на школе и {b}найти деньги на обучение{/b}."
    show debbie 10 at right
    show player 10 at left
    player_name "Да, но {b}[deb_name]{/b}, я ведь могу помочь..."
    hide player 10 at left
    show debbie 12 at right
    with dissolve
    deb "Ох, милый..."
    deb "Дай мне со всем разобраться и всё будет в порядке, окей? Я обещаю."
    hide debbie with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane b_kitchen a_empty f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "... Я не вижу проблемы. Разве это не хорошо, что он помогает тебе по дому?"
    show diane f_normal
    show debbie 60f
    deb "Я знаю, это просто..."
    deb "Он был таким... в последнее время он ко мне очень привязан..."
    show diane f_laugh
    show debbie 59f
    dia "Неудивительно, он только что потерял единственную семью, которая у него была..."
    show diane f_normal_talk
    dia "Возможно, ему просто нужен кто-то, с кем он мог бы чувствовать себя ближе..."
    dia "Особенно после всего того, что с вами происходит."
    show diane f_normal
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "Дело не в этом. Это еще не все! Он так на меня смотрит, понимаешь?"
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane f_surprised
    dia "..."
    show diane f_normal_talk
    dia "Что ты имеешь в виду?"
    show diane f_normal
    show debbie 60f
    deb "Ну, некоторое время назад.. Я начала кое-что замечать..."
    show diane f_normal_talk
    show debbie 59f
    dia "...Например?"
    show diane f_normal
    show debbie 60f
    deb "Например, как он всегда становится скованным со мной..."
    deb "... И прикасаться ко мне... в некоторых отношениях."
    show diane f_surprised
    show debbie 59f
    dia "..."
    show debbie 60f
    deb "... А на днях я застала его играющим с самим собой в моей постели!"
    deb "... С моим нижним бельем!"
    show diane f_normal_talk
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "Что ты сделала?!"
    show diane f_normal
    show debbie 60f
    deb "Мы это обсуждали!"
    deb "Я сказала ему не делать этого в моей комнате, но....."
    show diane f_normal_talk
    show debbie 59f
    dia "Но, что?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Я снова поймала его! Он извинился и начал говорить о желаниях, которые не мог контролировать..."
    show diane f_normal_talk
    show debbie 59f
    dia "Ладно, что ты на это сказала?"
    show diane f_surprised
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "... Я... Дала ему закончить."
    show diane f_normal_talk
    show debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    dia "Ты смотрела как он мастурбировал?"
    show diane f_normal
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Я не знала что делать!"
    deb "Я подумала, может, если он просто выкинет это из головы..."
    deb "... Знаешь?"
    show diane f_normal_talk
    show debbie 59f
    dia "Это так неприлично..."
    show diane f_normal
    show debbie 60f
    deb "Это еще не все..."
    show diane f_normal_talk
    show debbie 59f
    dia "Еще?!"
    dia "Ты серьезно?!"
    dia "Расскажи мне!"
    show diane f_surprised
    show debbie 60f
    deb "Диана..."
    show diane f_normal_talk
    show debbie 59f
    dia "{b}[deb_name]{/b}, расскажи мне!"
    show diane f_surprised
    show debbie 60f
    deb "... Мы вместе принимали душ."
    show diane f_normal_talk
    show debbie 59f
    dia "Вау..."
    show diane f_teasing
    dia "... Как он?"
    show diane f_surprised
    show debbie 60f
    deb "Диана!!"
    show diane f_laugh
    show debbie 59f
    dia "Что?!"
    show diane f_thinking
    dia "Не веди себя как ханжа! Мы оба знаем, что ты умираешь от желания рассказать мне!"
    show diane f_surprised
    show debbie 60f
    deb "... {b}*вздыхая*{/b}"
    show diane f_teasing
    show debbie 59f
    dia "Ты... трогала его?"
    show diane f_smirk
    show debbie 60f
    deb "... Да."
    deb "Я его вроде как дрочила..."
    show diane f_teasing
    show debbie 59f
    dia "До конца?"
    show diane f_smirk
    show debbie 60f
    deb "... Пока он не кончил."
    show debbie 59f
    if not M_diane.finished_state(S_diane_drunken_garden_work):
        show diane f_teasing
        dia "Ну и как?"
        show diane f_smirk
        show debbie 60f
        deb "... Как что?"
        show diane f_teasing
        show debbie 59f
        dia "Его {b}член{/b}, {b}[deb_name]{/b}! Он большой?"
        show diane f_smirk
        show debbie 60f
        deb "( !!! )"
        show debbie 59f
        deb "..."
        show diane f_explain
        dia "Не стесняйся меня, девочка. Выкладывай!"
        show debbie 60f
        show diane f_smirk
        deb "{b}Диана{/b}, у него самый большой... {b}Член{/b}из тех, что я видела в жизни!"
        show diane f_teasing
        show debbie 59f
        dia "... Что ты говоришь?!"
    show diane f_laugh
    dia "Я удивлена, что ты остановилась на мастурбации..."
    show diane f_smirk
    show debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    deb "{b}Диана{/b}, он всего лишь ребенок!"
    show diane f_teasing
    show debbie 15f
    dia "Пфф, он ходит в колледже!"
    show diane f_smirk
    show debbie 16f
    deb "Да, но я достаточно взрослая, чтобы быть его {b}матерью{/b}!"
    show diane f_laugh
    show debbie 15f
    dia "... Но {b}ты не{/b} его {b}мама{/b}, {b}[deb_name]{/b}!"
    show diane f_normal
    show debbie 16f
    deb "О, Я не знаю, {b}Диана{/b}..."
    show diane f_surprised
    show debbie 15f
    dia "Он явно этого хочет."
    show diane f_normal
    show debbie 16f
    deb "Пожалуйста, скажи мне, что я не делаю здесь ничего ужасного..."
    show diane f_normal_talk
    show debbie 15f
    dia "Это твое решение, но....."
    dia "Думаю, тебе стоит расслабиться и немного насладиться этим. Кого волнует разница в возрасте?"
    show diane f_normal
    show debbie 16f
    deb "Неужели? Ты не думаешь, что это неправильно?"
    show diane f_normal_talk
    show debbie 15f
    dia "Нет. Я не вижу в этом ничего плохого!"
    show diane f_normal
    show debbie 16f
    deb "Полагаю, мы никому не причиняем вреда... И мы обе взрослые."
    show diane f_laugh
    show debbie 15f
    dia "К тому же, это все очень {b}КРУТО{/b}!"
    show diane f_normal
    show debbie 16f
    deb "Ты так плохо на меня влияешь! Не знаю, почему я тебя слушаю!"
    show diane f_normal_talk
    show debbie 15f
    dia "... Потому что ты знаешь, что я права! Просто дай ему шанс. Кто знает, может, так и должно было быть?"
    show diane f_normal
    show debbie 62f at Position(xpos=0.3318,ypos=1.000)
    deb "Да, полагаю, все возможно..."
    show diane f_normal_talk
    show debbie 61f
    dia "Ладно, я лучше пойду домой. Уже поздно."
    show diane f_teasing
    dia "Продолжим в другой раз. Я хочу узнать все сочные детали!"
    show diane f_normal
    show debbie 62f
    deb "{b}Диана{/b}! Ты ужасна!"
    deb "Почему бы тебе не прийти на ужин? Я бы хотела видеть тебя почаще!"
    show debbie 61f
    show diane f_normal_talk
    dia "Я всегда спускаюсь к ужину, {b}[deb_name]{/b}. До тех пор, пока я не буду готовить!"
    dia "Удачи, дорогая."
    scene expression L_home_entrance.background
    show player 5
    player_name "( Это... было слишком. )"
    player_name "( {b}[deb_name]{/b} казалось, действительно сомневалась во всем этом... )"
    show player 203
    player_name "( Она сказала, что ей это нравится. )"
    player_name "( В любом случае, я рад, что {b}Диана{/b} думает, что это нормально для нас, делать такие вещи! )"
    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show debbie 14b at right
    player_name "Оу, да ладно тебе, {b}[deb_name]{/b}!"
    player_name "Ты ведь сама сказала, что мне нужно кого-нибудь найти."
    player_name "Это станет намного проще, если я буду знать, как правильно целовать девушку, разве нет?"
    show player 1
    deb "..."
    show debbie 13
    deb "... Ладно."
    deb "Я думаю, я смогу дать тебе пару советов."
    show debbie 14
    show player 2
    player_name "Это крайне важно для меня, {b}[deb_name]{/b}."
    show player 1
    show debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    deb "Окей, эмм... Подойди поближе."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show debbie 72
    player_name "Ладно."
    show player 227
    show debbie 73
    deb "Хорошо. Сейчас обопрись, вот так."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Окей."
    show player 227
    show debbie 73
    deb "... Закрой глаза и чуть-чуть надави своими губами на мои..."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    deb "Mмм."
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "И как?"
    show player 227
    show debbie 77
    deb "... Вау."
    show player 227c
    show debbie 76
    player_name "Плохо?"
    show player 227
    show debbie 73
    deb "Н-нет. Это было вполне неплохо!"
    show player 227c
    show debbie 72
    player_name "Правда?!"
    show player 227
    show debbie 73
    deb "Да. Ты уверен, что это твой первый раз?"
    show player 227c
    show debbie 72
    player_name "Ха, уверен. Так что там за советы?"
    show player 227
    deb "..."
    show debbie 73
    deb "Ну, давай посмотри..."
    deb "Ох, я знаю!"
    deb "Поцелуй меня ещё раз, и я покажу тебе небольшой трюк!"
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
    player_name "Вау!"
    player_name "То, что ты сделала своим языком, - это было так круто!"
    show player 227
    show debbie 75
    deb "Хехе, да."
    show debbie 73
    deb "Этому я научилась достаточно давно..."
    show player 227c
    show debbie 72
    player_name "Хмм, как мне это попробовать?"
    show player 227
    show debbie 73
    deb "Ох... ах."
    show player 227c
    show debbie 72
    player_name "Пожалуйста?"
    show player 227
    show debbie 73
    deb "Да... Конечно!"
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
    player_name "Как это было?!"
    show player 227
    deb "Mмм..."
    show player 227c
    player_name "{b}[deb_name]{/b}?"
    show player 227
    show debbie 77
    deb "Ох, прости!"
    show debbie 75
    deb "Это было ОЧЕНЬ неплохо, милый!"
    deb "То есть, вау! Ты будешь отличным обольстителем, как окунешься в мир свиданий!"
    show player 227c
    show debbie 76
    player_name "Правда? Спасибо {b}[deb_name]{/b}!"
    show player 227
    deb "Mммхмм."
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
    deb "Oх!"
    deb "Oх боже..."
    show player 230
    player_name "..."
    show player 232
    player_name "Прости, {b}[deb_name]{/b}."
    player_name "Я не хотел..."
    show player 231
    show debbie 75
    deb "Хехе, всё в порядке, милый. Я всё понимаю."
    show debbie 73
    deb "Нам лучше сделать перерыв."
    show player 232
    show debbie 72
    player_name "... Да. Конечно."
    player_name "Что думаешь, может, мы сделаем это снова?"
    show player 231
    deb "..."
    show player 232
    player_name "Ну знаешь, чтобы я попрактиковался?"
    show player 231
    show debbie 73
    deb "Я думаю, что это не проблема."
    deb "Но только ради практики!"
    show player 232
    show debbie 72
    player_name "Да, конечно!"
    show player 231
    show debbie 73
    deb "Отлично. Ты можешь попросить меня об этом в любое время."
    show player 232
    show debbie 72
    player_name "Спасибо {b}[deb_name]{/b}!"
    show player 231
    show debbie 73
    deb "Никаких проблем, {b}[firstname]{/b}."
    show player 232
    show debbie 72
    player_name "Увидимся!"
    hide debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "Это было прекрасно!"
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
    deb "Оу, эй, милый!"
    show debbie 120
    show player 14
    player_name "Хэй, {b}[deb_name]{/b}!"
    show debbie 119
    show player 1
    deb "Тебе нужно что-то?"
    deb "Я как раз домыла посуду..."
    show debbie 120
    return

label kitchen_mom_dishes_yes:
    show debbie 118
    show player 14
    player_name "Почему бы тебе не передохнуть?."
    player_name "Я протру остальное."
    show debbie 119
    show player 1
    deb "Это очень мило с твоей стороны, но ты не обязан."
    show debbie 118
    show player 14
    player_name "Всё в порядке. Я всё равно собирался сменить деятельность."
    show debbie 119
    show player 1
    deb "Ах, но ладно. Раз ты так говоришь..."
    show player 272
    show debbie 62
    deb "Просто вытри и поставь их в шкаф."
    show player 273
    show debbie 61
    player_name "Сделаю."
    show debbie 63
    show player 272
    deb "Спасибо за твою помощь, {b}[firstname]{/b}."
    show player 274
    show debbie 61
    player_name "Не за что, {b}[deb_name]{/b}."
    scene expression "backgrounds/location_home_cutscene01.jpg"
    show expression FilteredText("Не думаю, что {b}[deb_name]{/b} кто-нибудь помогал с посудой раньше... \nОна сказала,что её бывший муж вообще ничего не делал по дому, а мой {b}отец{/b} помогал только в саду, или изредка что-то чинил. \nОна стояла со мной на кухне до тех пор, пока я не разложил всю посуду по местам, а после этого мы мило поговорили. \nБыло приятно узнать {b}[deb_name]{/b} по-лучше...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show debbie 120 at Position(xpos=1014)
    player_name "Окей. Тогда я зайду позже."
    return

label kitchen_diane_debbie_evening_visit:
    scene expression "backgrounds/location_home_kitchen_secret.jpg"
    show diane b_kitchen a_empty
    show debbie 165bf at Position(xpos=0.3318,ypos=1.000)
    with dissolve
    deb "И ты много отдыхаешь?"
    show debbie 169bf
    show diane f_lookup
    dia "... Да, Мам."
    show diane f_smirk
    show debbie 165f
    deb "О, тише!"
    show debbie 164f
    show diane f_laugh
    dia "Хаха!"
    show diane f_normal
    show debbie 165f
    deb "Я просто беспокоюсь о тебе, вот и все."
    show debbie 164f
    show diane f_normal_talk
    dia "Я знаю, мы с {b}[deb_name]{/b} очень ценим это..."
    dia "... Но у меня все под контролем, обещаю!"
    dia "У меня хороший рабочий график, и {b}[firstname]{/b} следит, чтобы я его придерживалась."
    show diane f_normal
    show debbie 165bf
    deb "Он не знает... О своем... Ты знаешь..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Ммм, да..."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Диана{/b}..."
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Я не хотела, чтобы он узнал!"
    dia "Он поймал меня в ту ночь, когда ты послала его с пирогом..."
    show diane f_shamed
    show debbie 169bf
    deb "..."
    show diane f_smirk_talk
    dia "Кстати, спасибо за это."
    show diane f_smirk
    show debbie 164bf at Position (xoffset=10) with dissolve
    deb "..."
    show diane f_laugh
    dia "Я имею в виду, пирог был восхитительным!"
    show diane f_smirk
    show debbie 165bf with dissolve
    deb "Знаешь, если бы ты с самого начала рассказала мне, что ты задумала, я бы никогда не отправила его работать в твой сад этим летом..."
    show debbie 169bf
    show diane f_laugh
    dia "Ха-ха, хорошо, что я не сказала тебе тогда, а?"
    show diane f_smirk
    deb "..."
    show diane f_normal_talk
    dia "И кроме того, мой сад никогда не выглядел так хорошо."
    dia "Ты должна увидеть размер овощей, которые выращивает {b}[firstname]{/b}!"
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "Он ведь не будет с тобой, пока ты этим занимаешься?"
    show debbie 169bf
    show diane f_surprised_down
    dia "Что?"
    show diane f_shamed_talk_smile
    dia "... Ухх, нет. Обычно нет."
    show diane f_shamed
    show debbie 165bf
    deb "{b}Диана{/b}!!!"
    show debbie 169bf
    show diane f_shamed_talk_smile
    dia "Что?!"
    show diane f_shamed_talk
    dia "Ты же знаешь, какой он!"
    dia "Такой решительный, он должен помогать с каждой мелочью..."
    show diane f_shamed_talk_smile
    dia "Он все время заглядывает и просит помочь!"
    show diane f_shamed_talk_look
    dia "Тогда иди и заставь его волноваться о моем здоровье, так что теперь его практически невозможно удержать!"
    show diane f_shamed
    show debbie 165bf
    deb "Возможно, будет лучше, если он перестанет работать на тебя..."
    show debbie 169bf
    show diane f_shamed_talk
    dia "О, теперь ты просто смешная!"
    show diane f_shamed
    show debbie 165bf
    deb "Ты не должна подвергать его опасности-"
    show debbie 169bf
    show diane f_shamed_talk
    dia "Он больше не ребенок, {b}[deb_name]{/b}!"
    show diane f_normal_talk
    dia "Я думаю, он справится с парой сисек..."
    show diane f_normal
    deb "..."
    if M_mom.finished_state(S_mom_diane_visit):
        show diane f_smirk_talk
        dia "Кроме того, вещи, происходящие в моем сарае, намного более укрощены, чем ваши маленькие душевые с ним!"
        show diane f_smirk
        show debbie 164bf at Position (xoffset=10)
        deb "!!!" with hpunch
        show debbie 166df with dissolve
        deb "Это не- !!"
        show debbie 166cf
        deb "{b}*вздыхая*{/b} Мне не следовало говорить тебе об этом..."
        show debbie 166ef
        show diane f_laugh
        dia "Ха-ха, пожалуйста!"
        show diane f_smirk_talk
        dia "С кем еще ты можешь это обсуждать?!"
        dia "Кроме того, я думаю, что это супер горячо!"
        show diane f_smirk
        show debbie 165bf
        deb "Да, я знаю."
        show debbie 169bf
    else:
        show diane f_normal_talk
        dia "Ты действительно придаешь этому слишком большое значение, {b}[deb_name]{/b}!"
        dia "{b}[firstname]{/b} очень зрелый для своего возраста."
        show diane f_normal
        deb "..."
        show diane f_explain
        dia "Он вел себя как настоящий джентльмен."
        show diane f_normal_talk
        dia "Тебе стоит проводить с ним больше времени, и ты поймешь, что я имею в виду."
        show diane f_normal
        show debbie 165bf
        deb "Ты правда думаешь, что он справится?"
        show debbie 169bf
        show diane f_laugh
        dia "Я уверена!"
        show diane f_normal
        show debbie 166bf
        deb "( Хмм, может мне стоит проводить с ним больше времени... )"
        show debbie 169bf
    show diane f_normal_talk
    dia "Слушай, я просто не могу позволить себе потерять {b}[firstname]{/b} прямо сейчас, {b}[deb_name]{/b}."
    dia "Не тогда, когда мой бизнес только начинается."
    show diane f_normal
    deb "..."
    show debbie 165bf
    deb "Все действительно так хорошо, да?"
    show debbie 169bf
    show diane f_laugh
    dia "Лучше, чем я могла себе представить!"
    show diane f_normal_talk
    dia "Я уже ищу способы расширения."
    show diane f_normal
    show debbie 165bf
    deb "Что значит расширить?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Ну, во-первых, найти подходящее место для работы."
    show diane f_normal
    show debbie 165bf
    deb "Рабочее место?"
    show debbie 169bf
    show diane f_laugh
    dia "Да!"
    show diane f_thinking
    dia "На днях я смотрела на самый очаровательный маленький сарай, примерно в двух часах езды от города."
    show diane f_normal_talk
    dia "Я пришлю тебе фотографии."
    show diane f_normal
    show debbie 168f
    deb "Сарай?!"
    deb "Ты это не серьезно!"
    show debbie 164f
    show diane f_explain
    dia "Ха, я чертовски серьезна!"
    show diane f_normal_talk
    dia "Ты же знаешь, я всегда мечтала об этом!"
    show diane f_normal
    show debbie 165f
    deb "Да, но ты должна признать, что это не тот скот, которым ты представляла его наполнить..."
    show debbie 164f
    show diane f_normal_talk
    dia "Правда."
    show diane f_smirk_talk
    dia "... Это намного лучше, чем я планировала!"
    show diane f_smirk
    show debbie 168f
    deb "Боже мой, ты такая странная..."
    show debbie 165f
    show diane f_laugh
    dia "Хахаха!"
    deb "Хахаха!"
    show diane f_normal
    deb "Так к чему все это идет?"
    deb "Ты в конце концов начнешь искать больше женщин, чтобы присоединиться к твоему маленькому молочному бизнесу?"
    show debbie 164f
    show diane f_normal_talk
    dia "Да, возможно..."
    dia "Я имею в виду, я еще не там, но это определенно то, о чем я думала..."
    show diane f_smirk_talk
    dia "... Это твой способ волонтерства?"
    show diane f_smirk
    show debbie 168f
    deb "Пфф, да!"
    show debbie 164f
    show diane f_laugh
    dia "Ха-ха, давай!"
    show diane f_smirk
    show debbie 165f
    deb "Ни за что!"
    deb "Я не собираюсь вмешиваться во все твои глупые мечты."
    show debbie 164f
    show diane f_smirk_talk
    dia "Иногда ты становишься таким мокрым одеялом..."
    dia "...Но видишь, вот почему мне нужно чтобы {b}[firstname]{/b} продолжал помогать мне!"
    dia "Никто не будет работать так усердно, как он..."
    show diane f_thinking
    dia "... По крайней мере, никого, кому я могла бы заплатить."
    show diane f_normal
    show debbie 169bf
    deb "..."
    show debbie 165bf
    deb "Тьфу, хорошо."
    deb "... Но я хочу, чтобы ты пообещала мне, что не будет никакого смешного дела!"
    show debbie 169bf
    show diane f_normal_talk
    dia "О боже, перестань волноваться!"
    dia "Я буду хорошо себя вести, обещаю."
    show diane f_normal
    show debbie 169bf
    deb "Хммм."
    show debbie 169bf
    dia "..."
    show debbie 165bf
    deb "Два часа?!"
    deb "Все амбары, которые ты смотрала, так далеко?"
    show debbie 169bf
    show diane f_normal_talk
    dia "Большинство."
    dia "{b}Мэр Рамп{/b} владеет всеми сельскохозяйственными угодьями за пределами города, и он отказывается продавать их по какой-то причине."
    dia "Поэтому я была вынуждена смотреть немного дальше."
    show diane f_normal
    show debbie 165bf
    deb "Боже, что мне делать, если ты уедешь?"
    show debbie 169bf
    show diane f_normal_talk
    dia "О, не надо пока всяких глупостей."
    dia "Еще есть время, и кто знает, может, я найду что-нибудь поближе."
    show diane f_normal
    deb "..."
    show diane f_laugh
    dia "Если ты продолжишь делать такое лицо, оно замерзнет..."
    show diane f_normal
    show debbie 168f
    deb "Хех, заткнись!"
    show debbie 164f
    show diane f_laugh
    dia "Хахаха!"
    show diane f_surprised_down
    dia "Боже мой, посмотри на время..."
    show diane f_normal_talk
    dia "Мне нужно вернуться домой и накачать еще одну порцию перед сном."
    show diane f_normal
    show debbie 165f
    deb "Но ты же только что пришла!"
    show debbie 164f
    show diane f_shamed_talk_smile
    dia "Я знаю, мне жаль."
    show diane f_normal_talk
    dia "Я позвоню тебе завтра, хорошо?"
    show diane f_normal
    show debbie 165f
    deb "Да, хорошо."
    show debbie b_empty a_empty f_normal_talk at flip
    show debbie at Position (xpos=597)
    show diane b_hug_deb a_empty f_normal at Position (xpos=285)
    with dissolve
    deb "Будь осторожна."
    show diane f_normal_talk
    show debbie f_normal
    dia "Хорошо."
    show debbie at unflip
    show debbie 164f at Position(xpos=0.3318,ypos=1.000)
    show diane f_laugh b_casual a_casual_sides at lright
    with dissolve
    dia "Не забудь попробовать молоко, которое я тебе принесла!"
    show diane f_normal
    show debbie 165f
    deb "Посмотрим, посмотрим..."
    show debbie 164f
    show diane f_normal_talk
    dia "Я серьезно, {b}[deb_name]{/b}!"
    dia "Плесни себе в утренний кофе."
    dia "Тебе понравиться, говорю тебе!"
    show diane f_normal
    show debbie 165f
    deb "Пока, {b}Диана{/b}..."
    show debbie 164f
    show diane f_laugh
    dia "Хахаха! Пока, {b}[deb_name]{/b}."
    scene black
    with fade
    hide diane
    hide debbie
    pause
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 5 at left with dissolve
    show diane b_casual a_casual_sides f_smirk_talk
    with dissolve
    dia "О, привет {b}[firstname]{/b}!"
    dia "- У тебя уши горят?"
    show diane f_smirk
    show player 10
    player_name "Хмм?"
    show player 5
    show diane f_smirk_talk
    dia "Мы только что говорили о тебе..."
    show diane f_smirk
    show player 29 with dissolve
    player_name "О, правда?"
    show player 3
    show diane f_smirk_talk
    dia "Ты придешь завтра?"
    show diane f_smirk
    show player 29
    player_name "Не знаю, может быть..."
    show player 3
    show diane f_smirk_talk
    dia "Ну, я надеюсь, что ты придешь."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 21 at left
    show diane f_smirk_talk b_casual a_casual_sides
    with dissolve
    dia "Мне скоро понадобятся твои волшебные руки для большой работы..."
    show diane f_smirk
    show player 28
    player_name "{b}*глоток*{/b} Хорошо."
    show player 21
    show diane f_laugh
    dia "Хехе."
    dia "Пока, жеребец!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Пока, {b}Диана{/b}."
    hide player
    hide diane
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
