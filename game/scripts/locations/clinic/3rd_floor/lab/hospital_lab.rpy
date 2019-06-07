label hospital_lab_dialogue:
    $ player.go_to(L_hospital_lab)
    if M_priya.is_state(S_priya_look_in_lab):
        call expression game.dialog_select("hospital_lab_priya_look_in_lab")
    $ game.main()

label hospital_laboratory_take_pills_dialogue:
    scene expression "backgrounds/location_hospital_lab_blur.jpg"
    show player 706 at left with dissolve
    player_name "( Hmm, so it comes in pill form? )"
    player_name "( Weird. )"
    player_name "( I was expecting some kind of cream... )"
    player_name "( ... Or maybe something in a syringe. )"
    player_name "( This is much simpler! )"
    priya "Who the hell are you?!"
    show player 23
    player_name "!!!" with hpunch
    show priya f_stern a_dressed_crossed with dissolve
    player_name "I uhh..."
    show player 22
    show priya f_angry
    priya "How did you get in-"
    show priya a_dressed_point with dissolve
    priya "{b}*Gasp*{/b} Are you stealing my drugs!"
    show priya f_stern a_dressed_crossed with dissolve
    show player 23
    player_name "N-no, I wasn't-"
    show player 22
    show priya f_angry a_dressed_point with dissolve
    priya "I'm calling security!"
    show priya f_stern a_dressed_sides at flip
    show priya at Position (xoffset=650)
    show player 40 with dissolve
    player_name "W-wait, please!"
    pause
    hide priya
    show priya f_stern a_dressed_crossed
    with dissolve
    show player 10 with dissolve
    player_name "I wasn't going to steal them, I was just looking!"
    show player 5
    show priya f_angry
    priya "Yeah, right!"
    show priya f_stern
    show player 10
    player_name "I'm serious!"
    player_name "Look, here."
    show player 239_240 with dissolve
    pause
    show player 705f with dissolve
    player_name "See, no harm done."
    show player 704f
    show priya f_angry a_dressed_point with dissolve
    priya "This is a restricted area!"
    priya "How did you even get up here?!"
    show priya f_stern a_dressed_crossed with dissolve
    show player 24 with dissolve
    player_name "{b}*Sigh*{/b} It's a long story. Please don't make me think about it again."
    show player 10
    player_name "Maybe you can help me?"
    player_name "I'm looking for a guy named, {b}Doctor Signh{/b}?"
    show player 5
    pause
    show priya f_rolleyes
    priya "Well, you found \"him\"."
    show priya f_stern
    show player 12
    player_name "Huh?"
    show player 10
    player_name "... You mean-"
    show player 37 with dissolve
    show priya f_angry
    priya "I'm {b}Doctor Singh{/b}."
    show priya f_stern
    show player 30
    player_name "B-but you're a woman... Right?"
    show player 5
    show priya f_angry
    priya "No shit, Sherlock."
    show priya f_stern
    show player 10
    player_name "Sorry, I didn't-"
    show player 401
    player_name "I was under the impression you were a man."
    show player 403
    priya "..."
    show priya f_angry
    priya "Would you hurry up and tell me what this is all about?!"
    show priya f_stern
    show player 10
    player_name "R-right, sorry!"
    show player 4 with dissolve
    player_name "Umm."
    show player 10 with dissolve
    player_name "I heard something about this {b}Pregnax{/b} drug you're developing..."
    show player 5
    show priya f_angry
    priya "Oh, and who exactly did you hear it from?!"
    show priya f_stern
    show player 10
    player_name "I... I promised I wouldn't say..."
    show player 18
    show priya f_angry
    priya "It was that air headed nurse on the second floor, wasn't it?!"
    priya "That woman can't keep her mouth closed for two seconds."
    show priya f_stern
    show player 11
    player_name "..."
    show priya f_rolleyes
    priya "Go on."
    show priya f_stern
    show player 10
    player_name "You see, my fri-"
    player_name "{b}*Ahem*{/b} M-my girlfriend is trying to get pregnant and her odds aren't very good."
    player_name "I want to do everything I can to help increase her odds."
    show player 5
    show priya f_angry
    priya "So, that's why you broke into my lab?"
    show priya f_stern
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 26 with dissolve
    player_name "Which again, was not to steal anything!"
    show player 38 with dissolve
    player_name "I just wanted to speak with you about the {b}Pregnax{/b} drug trial."
    show player 5 with dissolve
    show priya f_angry
    priya "The trial is at capacity."
    show priya f_stern
    show player 24
    player_name "Y-yeah, I heard about that too."
    pause
    player_name "Is there nothing you can do?"
    show priya f_facepalm a_dressed_facepalm with dissolve
    priya "..."
    show priya f_facepalm_talk
    priya "Well, I'll admit. I'm impressed with your determination."
    priya "It couldn't have been easy getting up here."
    show priya a_dressed_sides f_normal_talk with dissolve
    priya "... And I'm not unsympathetic to your girlfriend's plight."
    show priya f_normal
    show player 11
    pause
    show priya f_normal_talk
    priya "What's your name?"
    show priya f_normal
    show player 10
    player_name "{b}[firstname]{/b}."
    show player 5
    show priya f_normal_talk
    priya "How old are you, {b}[firstname]{/b}?"
    show priya f_normal
    show player 10
    player_name "I'm eighteen."
    show player 5
    show priya f_normal_talk
    priya "That's very young."
    priya "Our other test subjects are all ten to thirty years older than you."
    show priya f_normal
    show player 30
    player_name "Is that a good or bad thing?"
    show player 5
    show priya f_thinking a_dressed_thinking with dissolve
    pause
    show priya f_suspicious_talk
    priya "It's... Intriguing."
    show priya f_normal_talk
    priya "... And your girlfriend, how old is she?"
    show priya f_normal
    show player 35
    player_name "Uhh, I'm not sure exactly..."
    show player 34
    show priya f_suspicious_talk
    priya "You're trying for a baby with this woman and you don't even know her age?"
    show priya f_normal
    show player 35
    player_name "N-no, I uhh..."
    player_name "I mean, she's in her late thirties, I think."
    show player 34
    show priya f_normal_talk
    priya "Oh, now that is interesting..."
    priya "Is she your only sexual partner?"
    show priya f_normal
    show player 17
    player_name "... No."
    show player 18
    show priya f_rolleyes a_dressed_crossed with dissolve
    priya "Tsk."
    show priya f_thinking a_dressed_thinking with dissolve
    pause
    show priya f_normal_talk a_dressed_crossed with dissolve
    priya "Would you be willing to subject yourself to a few tests?"
    show priya f_normal
    show player 10
    player_name "Uhh, sure."
    show player 5
    show priya f_normal_talk
    priya "This would all be strictly off the books, mind you."
    show priya f_normal
    show player 10
    player_name "I'm fine with that."
    show player 5
    show priya f_normal_talk
    priya "I am not a charitable person by nature, {b}[firstname]{/b}."
    show priya a_dressed_point with dissolve
    priya "However, your unique circumstances would certainly prove useful to my research."
    show priya f_thinking a_dressed_thinking with dissolve
    priya "..."
    show priya f_normal_talk a_dressed_point with dissolve
    priya "I'll give you one bottle, for now."
    priya "Perhaps more, in the future."
    show priya f_normal a_dressed_crossed with dissolve
    show player 14
    player_name "That would be wonderful!"
    show player 13
    show priya f_normal_talk
    priya "... But only if you agree to return here for testing."
    show priya f_normal
    show player 14
    player_name "Not a problem!"
    show player 13
    show priya f_normal_talk a_dressed_point with dissolve
    priya "... And I want a full accounting of each and everytime you use the pill."
    priya "Every detail."
    show priya f_normal a_dressed_crossed with dissolve
    show player 10
    player_name "Every detail?"
    show player 5
    show priya f_normal_talk
    priya "If at any point I'm unsatisfied with your quality of information or test results, the deal ends."
    show priya f_normal
    show player 14
    player_name "O-okay."
    show player 13
    show priya f_normal_talk
    priya "There is something else you must understand, {b}[firstname]{/b}."
    priya "We're still very early in testing with {b}Pregnax{/b}."
    priya "{b}You must be cautious about using it{/b}."
    priya "{b}There may very well be side effects{/b} we aren't aware of yet."
    priya "Although, in theory it should be relatively safe."
    show priya f_normal
    show player 37 with dissolve
    player_name "{b}Gulp{/b} I... I understand."
    pause
    show player 13 with dissolve
    show priya f_normal
    priya "Hmmph."
    show priya f_normal_talk
    priya "Return to me if you run out of pills."
    priya "I'll be in touch with you about those... tests."
    show priya f_normal
    show player 14
    player_name "I will and look forward to hearing from you."
    player_name "Thank you, {b}Doctor Singh{/b}!"
    show player 13
    show priya f_normal_talk
    priya "It's {b}Priya{/b}."
    show priya f_normal
    show player 30
    player_name "Hmm?"
    show player 5
    show priya f_normal_talk
    priya "My name is {b}Priya{/b}."
    priya "{b}Priya Singh{/b}."
    show priya f_normal
    show player 30
    player_name "{b}Priya{/b}."
    show player 33
    player_name "That's a very pretty name!"
    show player 18
    show priya f_rolleyes
    priya "Yes, yes..."
    show priya f_normal_talk
    priya "Go on, Casanova."
    show priya a_dressed_point with dissolve
    priya "Get out of my lab."
    show priya f_normal
    hide player with dissolve
    pause
    show priya f_facepalm_talk a_dressed_facepalm
    priya "Grr, what are you thinking {b}Priya{/b}?!"
    priya "You've completely lost your mind!"
    show priya f_facepalm
    pause
    show priya f_normal a_dressed_sides with dissolve
    priya "..."
    show priya f_facepalm_talk
    priya "Oh, please, let him bring me good news..."
    hide priya with dissolve

    scene expression "backgrounds/location_hospital_third_blur.jpg"
    show player 705 with dissolve
    player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
    player_name "( {b}Effects will last for 24 hours.{/b} )"
    player_name "( {b}There's also a warning label, \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\"{/b} )"
    hide player with dissolve
    $ player.get_item("fertility_pills")
    $ player.get_item("birth_control_pills")
    $ M_priya.trigger(T_priya_start_testing)
    $ player.go_to(L_hospital_floor3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
