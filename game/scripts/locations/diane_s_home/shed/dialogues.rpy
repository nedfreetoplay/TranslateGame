label dianes_shed_diane_delivery_2_fetch_goods:
    scene shed
    show player 14 with dissolve
    player_name "Whoa!!!"
    player_name "Look at all the milk jugs!"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Did {b}Diane{/b} really fill all of those by herself?!"
    player_name "It would take forever, especially if she's hauling them out to the cow one by one..."
    show player 4 with dissolve
    player_name "Hmm."
    show player 33 with dissolve
    player_name "Well, I guess it explains why she spends so much time in here."
    show player 13
    player_name "..."
    show player 14
    player_name "I should {b}get started with the delivery.{/b}"
    hide player with dissolve
    return
















































label dianes_shed_diane_fetch_pump:
    show player 35 at left with dissolve
    player_name "Woah..."
    show player 34
    player_name "...What a strange looking shed."
    player_name "What's up with all the containers... And those chains?!"
    show player 43
    player_name "Anyway, let's try and {b}find that pump{/b}..."
    hide player 43 with dissolve
    return

label dianes_shed_milking_help:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    $ M_diane.is_naked = 1
    show player 10 at left
    show diane b_topless_blank a_topless_pump1 f_surprised_front at lright
    with dissolve
    player_name "{b}Diane{/b}?!"
    player_name "What's going on in here?"
    player_name "Are you okay?"
    show player 5
    show diane f_sad_talk
    dia "Arrgh, no!"
    dia "I'm clogging up again and the piece of crap pump is stuck!"
    show diane f_sad
    show player 10
    player_name "Clogging up?"
    show player 5
    dia "..."
    show player 10
    player_name "So wait, that thing is stuck to your boob?"
    show player 5
    show diane f_surprised_down a_topless_pump_stuck with dissolve
    pause
    show diane f_scream
    dia "{b}*iiitthhh*{/b} Ah, this really hurts!"
    show diane a_topless_pump1 f_tired_down with dissolve
    show player 10
    player_name "Let me help!"
    show player 5
    show diane f_sad_talk
    dia "No."
    dia "I'll get it."
    show diane f_surprised_down a_topless_pump_stuck with dissolve
    pause
    show diane a_topless_pump1 f_scream with dissolve
    dia "Arrghh!"
    show diane f_tired_down
    show player 10
    player_name "C'mon, you're in pain. Just let me take a look."
    show player 5
    show diane f_sad_talk
    dia "Fine."
    show diane f_surprised_front
    show player 670b at Position (xoffset=100)
    with dissolve
    pause
    show diane f_surprised_down
    dia "Just be careful."
    show diane f_surprised_front
    player_name "I will, I promise."
    pause
    player_name "Hmm."
    show player 670c zorder 1 at Position (xoffset=46)
    show diane f_surprised_down a_topless_pump_stuck
    with dissolve
    pause
    player_name "Got it!"
    show player 13
    show diane a_topless_ouch f_surprised_front_talk
    with dissolve
    dia "Oh, thank goodness..."
    show diane f_surprised_front
    player_name "Are you alright?"
    show diane f_surprised_front_talk
    dia "Phew, I'm a lot better now that you got that stupid pump off me."
    show diane b_topless a_naked_sides f_smirk_talk with dissolve
    dia "Thank you, {b}[firstname]{/b}."
    show diane f_smirk
    show player 429
    player_name "You're welcome."
    show player 426
    pause
    show player 14
    player_name "... You mentioned something about a clog?"
    show player 13
    dia "Hmm?"
    show diane f_sad_talk
    dia "Oh, yeah."
    dia "It happens sometimes. Women can get a clogged duct in their milk glands."
    show diane f_sad
    show player 10
    player_name "Does it hurt?"
    show player 5
    show diane f_laugh
    dia "... Well, it certainly doesn't feel good!"
    show diane f_smirk
    show player 10
    player_name "Sorry..."
    player_name "How do we fix it?"
    show player 5
    show diane f_smirk_talk a_topless_ouch with dissolve
    dia "Oh, I usually just put on a hot compress on and massage it."
    show diane f_smirk a_naked_sides with dissolve
    show player 12
    player_name "So, massaging can unclog it?"
    show player 5
    show diane f_smirk_talk
    dia "Yeah, if you know what you're doing."
    show diane f_smirk
    show player 429
    player_name "Can I try?"
    show player 426
    show diane f_surprised
    dia "..."
    show diane f_shamed_talk_smile
    dia "I'm not sure that's a good idea."
    show diane f_shamed
    show player 10
    player_name "I don't like seeing you in pain, {b}Diane{/b}."
    player_name "Please, let me help."
    show player 5
    show diane f_smirk
    dia "..."
    show diane f_explain
    dia "Yeah, okay..."
    show diane a_topless_ouch f_smirk_talk
    show player 426
    with dissolve
    dia "Just press in here with your thumb and kneed downward towards my nipple."
    show diane f_smirk
    show player 17
    player_name "Alright!"
    hide player
    show diane b_topless_blank2 a_topless_waiting f_down_front
    with dissolve
    pause
    show diane b_topless_blank2 a_topless_squeeze1 with dissolve
    player_name "Like this?"
    show diane f_shamed_talk_look
    dia "Yes. Now squeeze and pull."
    show diane a_topless_squeeze f_explain_close with dissolve
    pause
    show diane f_explain
    dia "Yeeeah. Just like that..."
    show diane f_explain_close
    pause
    show diane f_explain
    dia "Mmm, that feels nice."
    dia "I can't remember a time my breasts weren't sore..."
    show diane f_explain_close
    player_name "That's not good, {b}Diane{/b}."
    show diane f_laugh
    dia "Heh, yeah I know."
    show diane f_explain
    dia "I need to get better equipment."
    show diane f_lip_bite
    pause
    player_name "Is this helping?"
    show diane f_explain
    dia "Ahh, definitely..."
    dia "Your hands feel amazing, {b}[firstname]{/b}!"
    show diane f_down_front
    pause
    show diane f_explain
    dia "You're very good at this!"
    show diane f_lip_bite
    pause
    player_name "How will I know when it's fixed?"
    show diane f_laugh a_topless_squeeze_milk
    dia "Haaah!" with hpunch
    show diane f_down_front
    pause
    show diane a_topless_squeeze1 with dissolve
    player_name "Hehe, oh."
    show diane a_topless_squeeze_milk with dissolve
    player_name "I guess that's how..."
    show diane f_laugh
    dia "Haaah... Haaah..."
    dia "Phew, thank you..."
    show player 83b at left
    show diane b_topless a_naked_sides f_smirk
    with dissolve
    player_name "Hehe, you're welcome."
    player_name "I'm just happy I could help for once."
    show player 83c
    show diane f_smirk_talk
    dia "You have like, the best hands I've ever-"
    show diane f_surprised_down
    dia "!!!"
    pause
    show player 83
    player_name "... You've ever?"
    show player 82
    show diane f_smirk
    dia "Hmm?"
    show player 83
    player_name "You were saying something about my hands."
    show player 82
    show diane f_teasing_look
    dia "Was I?"
    dia "I completely forgot what I was saying..."
    show diane f_smirk
    show player 83b
    player_name "Heh, sorry."
    show player 83c
    show diane f_smirk_talk
    dia "No, it's alright {b}[firstname]{/b}..."
    show diane f_teasing_look
    dia "... I just-"
    show player 78
    show diane b_jerk_pre a_empty f_jerk_down_front at Position (xoffset=-110)
    player_name "!!!" with hpunch
    hide player
    show diane b_jerk2 at Position (xpos=402)
    with dissolve
    player_name "{b}Diane{/b}?"
    player_name "I thought you didn't want to-"
    show diane f_jerk_teasing_look
    dia "I know."
    dia "Truthfully, I'm not sure what I want..."
    show diane b_jerk f_jerk_down_front
    player_name "That feels really good."
    pause
    show diane f_jerk_smirk_up_talk
    dia "You promise you won't tell {b}[deb_name]{/b}?"
    show diane f_jerk_smirk_up
    player_name "Oh, I promise!"
    pause
    show diane b_jerk2 f_jerk_smirk_up_talk
    dia "You wanna try my milk again?"
    show diane f_jerk_down_front
    player_name "Hmm?"
    player_name "Umm, yeah... Okay, sure."
    pause
    show diane b_topless a_naked_sides f_smirk at lright
    show player 10 at left
    with dissolve
    player_name "Should I get the pump?"
    show player 5
    show diane f_smirk_talk
    dia "No."
    dia "I thought, maybe you'd like to..."
    dia "... You know, try it directly from the tap?"
    show diane f_smirk
    pause
    show player 10
    player_name "You mean-"
    show player 29 with dissolve
    player_name "Y-yeah, definitely!"
    show player 3
    show diane f_smirk_talk a_topless_invite with dissolve
    dia "Come sit here."
    show diane f_smirk
    show player 29
    player_name "On your lap?"
    show player 3
    dia "Mmmhmm."
    show diane f_smirk_talk
    dia "Don't be shy."
    show player 29
    player_name "O-okay."
    hide player
    hide diane
    with dissolve
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "shirtless"
    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding1 a_empty f_hay_feeding_explain
    with dissolve
    dia "Go ahead, handsome."
    show diane b_hay_feeding f_hay_feeding_lip_bite
    dia "Mmm."
    pause
    show diane f_hay_feeding_explain
    dia "Oh my god, that feels so good!"
    show diane f_hay_feeding_explain_close
    pause
    show diane f_hay_feeding_explain
    dia "How's it taste?"
    show diane f_hay_feeding_lip_bite
    player_name "Delicious!"
    show diane f_hay_feeding_laugh
    dia "Hehe."
    show diane a_hay_feeding_arm f_hay_feeding_shamed_talk_look with dissolve
    dia "You've got such a nice dick, {b}[firstname]{/b}."
    dia "Have I mentioned that before?"
    show diane f_hay_feeding_smirk_down
    player_name "Heh, yeah. I think you mentioned it before."
    show diane f_hay_feeding_laugh
    dia "Haha!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane f_hay_feeding_explain
    dia "Mmm, oh yeah... Keep doing that with your tongue."
    dia "Your mouth feels amazing on my nipple!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane b_hay_feeding1 a_empty with dissolve
    dia "Nngghh!"
    show diane f_hay_feeding_shamed_talk_look
    dia "Alright, we'd better stop before you drink me dry, stud."
    show diane f_hay_feeding_smirk_down
    player_name "Aww."
    show diane f_hay_feeding_explain
    dia "I know..."
    hide diane with dissolve
    $ M_diane.is_naked = 1
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_topless a_naked_sides f_smirk_talk
    with dissolve
    dia "We'll do it again another day, alright?"
    show diane f_smirk
    show player 14
    player_name "Yeah, okay."
    show player 13
    show diane f_smirk_talk
    dia "You can't be greedy though."
    show diane f_laugh
    dia "I've got a business to run!"
    show diane f_smirk
    show player 17
    player_name "Heh, I know."
    show player 13
    show diane f_smirk_talk
    dia "Now get your cute butt back to work!"
    show diane f_smirk
    show player 14
    player_name "Yes, ma'am!"
    hide player
    hide diane
    with dissolve
    $ M_diane.outfit = "shirtless"
    return

label dianes_shed_diane_check_shed_light:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    show diane b_topless_blank a_topless_pump f_tired
    dia "..."
    show diane f_tired_talk
    dia "{b}*Yawn*{/b}"
    show diane f_tired_down
    pause
    player_name "{b}Diane{/b}??"
    show player 10 at left with dissolve
    player_name "Are you in here?"
    show player 14
    player_name "I brought you some-"
    show player 23
    player_name "{b}*Gasp*{/b}"
    show diane f_sad_talk
    dia "{b}[firstname]{/b}!!!" with hpunch
    show diane f_surprised
    show player 428
    player_name "!!!"
    show diane f_sad_talk
    dia "What are you-"
    show diane b_topless a_topless_covering f_surprised with dissolve
    show player 10
    player_name "... Is that..."
    player_name "You're..."
    show player 11
    show diane f_scared
    dia "..."
    show player 12
    player_name "Why are you using the cow's breast pump on yourself?"
    show player 5
    show diane f_sad_talk
    dia "I'm sorry, I never meant for you to... Wait, what?!"
    show diane f_sad
    dia "..."
    show diane f_sad_talk
    dia "{b}[firstname]{/b}, there is no cow."
    show diane f_sad
    show player 10
    player_name "... There is no cow?"
    player_name "But then, where is all that milk-"
    show player 11
    pause
    show player 37 with dissolve
    player_name "... Oh."
    show player 38 with dissolve
    player_name "OOOH!!!"
    player_name "You mean, all of this was-"
    show player 3 with dissolve
    show diane f_sad_talk
    dia "It's breast milk."
    dia "It's MY breast milk."
    show diane f_sad
    show player 11 with dissolve
    player_name "!!!"
    show player 17
    player_name "That's so awesome!"
    show player 18
    show diane f_shamed_talk_smile
    dia "... Awesome?"
    show diane f_shamed
    show player 14
    player_name "Yeah!!"
    player_name "I had no idea people could make this much!"
    show player 13
    show diane f_shamed_talk_look
    dia "Uhh..."
    show diane f_shamed
    show player 22
    player_name "{b}*Gasp*{/b}"
    show player 14
    player_name "I just realized!"
    player_name "... {b}Tony's{/b} making pizza with milk from your boobs!!"
    show player 17
    player_name "That's so cool!"
    show player 13
    show diane f_shamed_talk_smile
    dia "Hehe, I really didn't think you would take it this well..."
    dia "It doesn't bother you?"
    show diane f_shamed
    show player 12
    player_name "No, why would it?"
    show player 13
    dia "..."
    show player 14
    player_name "Can I try some?"
    show player 13
    show diane f_surprised_front_talk
    dia "You wanna try some?!"
    show diane f_shamed_talk_smile
    dia "Really?"
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "Umm, sure. I guess..."
    show diane f_shamed a_topless_milk_cover with dissolve
    pause
    show diane a_topless_covering
    show player 104
    with dissolve
    pause
    show player 105 with dissolve
    pause
    show player 34 with dissolve
    player_name "Hmm."
    show diane f_shamed_talk_smile
    dia "What do you think?"
    show diane f_shamed
    show player 33
    player_name "It's really creamy!"
    show player 34
    pause
    show player 33
    player_name "... And it's kinda got a... Sweetness to it."
    show player 34
    pause
    show player 14
    player_name "I like it!"
    show player 13
    show diane f_shamed_talk_smile
    dia "You do?"
    show diane f_shamed
    show player 14
    player_name "Yeah."
    player_name "I can't believe you've been making all this yourself!"
    show player 13
    show diane f_laugh
    dia "Heh, yeah. It hasn't been easy."
    show diane f_shamed_talk_smile
    dia "I've been milking myself around the clock for weeks now..."
    show diane f_shamed
    show player 14
    player_name "Oh, right!"
    player_name "{b}[deb_name]{/b} sent you this."
    show player 239_240 with dissolve
    pause
    show player 674 with dissolve
    player_name "She's worried you aren't eating enough."
    show player 673
    show diane f_shamed_talk_smile
    dia "Oh, is that apple?"
    show diane f_shamed
    player_name "Mmmhmm."
    show diane f_shamed_talk_smile
    dia "It looks delicious!"
    show diane f_tired_talk
    dia "And she's right, I haven't eaten all day."
    show diane f_tired
    show player 675
    player_name "That's not good, {b}Diane{/b}..."
    player_name "You've gotta take care of yourself!"
    show player 676
    show diane f_tired_talk
    dia "{b}*Sigh*{/b} I know, I'm pushing myself too hard."
    show diane f_tired
    show player 674
    player_name "How about the next time I come over, you take the day off?"
    show player 673
    show diane f_sad_talk
    dia "A whole day?"
    show diane f_tired_talk
    dia "I dunno..."
    show diane f_tired
    show player 674
    player_name "Oh, c'mon!"
    player_name "I'll take care of the garden and get you anything you need."
    player_name "You can just lay back and relax."
    player_name "Doesn't that sound nice?"
    show player 673
    dia "Hmm."
    show diane f_shamed_talk_smile
    dia "It does really nice..."
    show diane f_shamed
    show player 674
    player_name "It's a date then!"
    show player 673
    show diane f_surprised
    dia "!!!"
    show diane f_shamed_talk_smile
    dia "You're so sweet, {b}[firstname]{/b}."
    show diane f_shamed
    show player 674
    player_name "It's no problem at all."
    show player 673
    show diane f_shamed_talk_smile
    dia "You're not gonna tell anybody are you?"
    show diane f_shamed
    show player 676
    player_name "Hmm?"
    show diane f_shamed_talk_smile
    dia "You know, about the milk..."
    show diane f_shamed
    show player 674
    player_name "Oh, no. I won't tell anybody."
    show player 673
    show diane f_shamed_talk_smile
    dia "Thank you, handsome!"
    show diane f_shamed
    show player 674
    player_name "Now, lets get inside and eat {b}[deb_name]'s{/b} warm pie!"
    show diane f_lookup
    dia "Phew!"
    show diane f_shamed_talk_smile
    dia "I was so worried you'd think it was gross..."
    dia "... Or that I was a terrible person."
    show diane f_shamed
    show player 674
    player_name "Not at all!"
    show player 673
    show diane f_shamed_talk_smile
    dia "I was using cows originally but my breast milk has been such a hit..."
    show diane f_shamed
    show player 674
    player_name "Yeah, it tastes really good!"
    player_name "I'm not surprised they like it so much."
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_front_night_blur.jpg"
    show player 13
    player_name "( Wow, she was nodding off the entire time she ate. )"
    player_name "( I barely managed to get her in bed. )"
    player_name "( It's hard to believe all that milk came from {b}Diane{/b} )"
    show player 18
    player_name "( That's so cool! )"
    show player 13
    player_name "( She's working herself to the bone though! )"
    player_name "( ... Maybe, I can help her get a better routine going? )"
    player_name "( For now though, I'll just have to make sure her day off is really special and that she gets plenty of rest. )"
    hide player with dissolve
    return

















































































































label dianes_shed_seen_shed_locked:
    scene garden
    show player 34 with dissolve
    player_name "Hmm..."
    show player 35
    player_name "The door's locked."
    hide player 35 with dissolve
    return

label dianes_shed_not_seen_shed_locked:
    scene garden
    show player 35 at left with dissolve
    player_name "Hmm.. The shed is locked. I wonder what's in there?"
    show diane f_smirk_talk b_naked a_naked_sides with dissolve
    show player 22 at left
    dia "Are you snooping around?"
    show diane f_smirk
    show player 10 at left
    player_name "Uhh, sorry. I was just looking for tools..."
    show diane f_normal_talk
    show player 11 at left
    dia "It's okay. Perhaps one day I'll give you a little tour..."
    show player 21 at left
    show diane f_normal
    player_name "Sure, {b}Diane{/b}..."
    hide player
    hide diane
    with dissolve
    return

label dianes_shed_dewitt_paint:
    scene location_diane_shed01_night_closeup
    show player 588
    with dissolve
    player_name "Finally found the paint!"
    player_name "If I bring this and some {b}lumber{/b} to the {b}work bench{/b} in the {b}garage{/b}, I can make a fake guitar, no problem."
    hide player with dissolve
    $ M_dewitt.trigger(T_dewitt_shed_find_paint)
    if not player.has_item("paint"):
        $ player.get_item("paint")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
