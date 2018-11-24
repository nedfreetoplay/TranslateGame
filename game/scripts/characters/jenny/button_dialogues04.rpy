label sis_cheerleader_break_free_pass_animation:
    player_name "( Hey, these cuffs don't feel that sturdy... )"
    player_name "( Okay, here goes... )"
    return

label sis_cheerleader_break_free_pass_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    player_name "( Hey, these cuffs don't feel that sturdy... )"
    show jennysex 118
    player_name "( Okay, here goes... )"
    return

label sis_cheerleader_break_free_pass_after:
    $ animated = False
    show jennysex 119b at Position(xpos = 939, ypos = 674)
    jen "Hey, what are you-"
    show jennysex 122 at Position(xpos = 1022, ypos = 768)
    hide playersex
    jen "!!!" with hpunch
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "Ahh!!" with vpunch
    show jennysex 124
    jen "What are you... DOING?!"
    show jennysex 125
    pause
    show jennysex 126
    pause
    show jennysex 127
    pause
    show jennysex 123
    jen "You're... going too... fast!"
    show jennysex 124
    pause
    show jennysex 125
    pause
    show jennysex 126
    jen "This feels... AMAZING!!"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_unhappy:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_manual")
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_after")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_after_no_xray")
    call expression game.dialog_select("sis_cheerleader_fuck_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ sis_final_cum = "Inside"
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_inside_unhappy_animation:
    jen "( Oh my god, I can feel him tensing up... )"
    jen "( ... Is he about to cum {b}inside me{/b}?! )"
    pause
    jen "( Shit, I can't get him off me!!! )"
    return

label sis_cheerleader_fuck_cum_inside_unhappy_manual:
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "( Oh my god, I can feel him tensing up... )"
    show jennysex 124
    jen "( ... Is he about to cum {b}inside me{/b}?! )"
    show jennysex 125
    pause
    show jennysex 126
    jen "( Shit, I can't get him off me!!! )"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_unhappy_after:
    show jennysex 129
    jen "AAHHHH!!!!" with vpunch
    show white zorder 5
    show jennysex 129c
    hide white with dissolve
    pause
    show jennysex 128 with fastdissolve
    jen "Oh god..."
    show jennysex 129b_128
    pause 2.9
    show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
    show jennysex 131 zorder 2 at Position(xpos=985,ypos=674)
    with dissolve
    return

label sis_cheerleader_fuck_cum_inside_unhappy_after_no_xray:
    jen "What the... {b}FUCK{/b}?!"
    jen "I told you {b}NOT{/b} to cum inside me, you {b}IDIOT{/b}!!!" with hpunch
    return

label sis_cheerleader_fuck_cum_inside_happy:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_manual")
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_after")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_after_no_xray")
    call expression game.dialog_select("sis_cheerleader_fuck_after_repeat")
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_inside_happy_animation:
    jen "( Oh my god, I can feel him tensing up... )"
    jen "( ... Is he about to cum {b}inside me{/b}?! )"
    pause
    jen "( Shit, I can't get him off me!!! )"
    return

label sis_cheerleader_fuck_cum_inside_happy_manual:
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "( Oh my god, I can feel him tensing up... )"
    show jennysex 124
    jen "( ... Is he about to cum {b}inside me{/b}?! )"
    show jennysex 125
    pause
    show jennysex 126
    jen "( Shit, I can't get him off me!!! )"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_happy_after:
    show jennysex 129
    jen "AAHHHH!!!!" with vpunch
    show white zorder 5
    show jennysex 129c
    hide white with dissolve
    jen "YESS, DEEPER!!"
    show jennysex 128 with fastdissolve
    pause
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    jen "Keep cumming!"
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    jen "I want more..."
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    pause
    show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
    show jennysex 132 zorder 2 at Position(xpos=985,ypos=674)
    with dissolve
    return

label sis_cheerleader_fuck_cum_inside_happy_after_no_xray:
    jen "Look at all that cum dripping out of my pussy..."
    jen "...I might get {b}knocked up{/b}, at this rate..."
    return

label sis_cheerleader_fuck_after_repeat:
    scene jennybedroom
    show jenny 109 at right
    show player 13 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Well done!"
    show jenny 108
    show player 21
    player_name "We did okay?"
    show player 13
    show jenny 109
    jen "Yeah, they're loving our {b}little act{/b}."
    jen "I... have to give you credit."
    jen "I didn't expect you to be able to keep up so well."
    jen "You're pretty good."
    show jenny 108
    show player 14
    player_name "Really?"
    show jenny 109
    show player 13
    jen "I'm still gonna need you for more cam shows."
    show player 21
    show jenny 167
    player_name "Thanks, I really enjo-"
    show jenny 164
    show player 11
    jen "STOP it!!" with hpunch
    show jenny 165
    jen "..."
    show jenny 166
    jen "{b}*Sigh*{/b}"
    show jenny 109
    jen "Yeah, me too, I guess..."
    show player 13
    show jenny 108
    jen "..."
    show jenny 166
    show player 11
    jen "But, don't start getting ideas! I'm doing this because it's getting me loads of money..."
    jen "Oh, and do me a favor: try not to spend TOO much time with {b}[deb_name]{/b}..."
    jen "I know what you two are up to, I need you {b}fresh{/b} and {b}rested{/b}."
    jen "My subscribers now expect this kind of stream {b}regularly{/b}."
    show jenny 164
    jen "So NO jerking off, and NO sex!!"
    show jenny 165
    show player 12
    player_name "Okay! Okay! I get it..."
    show jenny 109
    show player 13
    jen "Good."
    show jenny 164
    show player 11
    jen "Good, now {b}GET OUT OF MY ROOM{/b}!!" with hpunch
    hide player
    hide jenny
    hide jenny_cheer2
    return

label jenny_dialogue_cam_show_no_items:
    show player 1
    show jenny 12 at Position(xpos=937)
    jen "So?"
    jen "Do you have all the stuff I asked you for?"
    show player 2
    show jenny 11
    player_name "Not yet..."
    show player 22
    show jenny 7 at right
    jen "Then go find them and {b}GET OUT{/b}!!"
    return

label jenny_dialogue_cam_show_have_items:
    scene jennybedroom
    show player 1 at left
    show jenny 12 at right
    show jenny 12 at Position(xpos=937)
    jen "So..."
    jen "Do you have all the stuff I asked you for?"
    show jenny 82
    show player 21
    player_name "Yeah, yeah..."
    show player 239_240
    pause
    show player 285 with fastdissolve
    player_name "Here it is."
    show player 1
    show jenny 158 at right
    with fastdissolve
    jen "Excellent."
    show jenny 12 at Position(xpos=937)
    show player 11
    jen "Maybe you're not as stupid as I thought after all."
    show jenny 10
    show player 12
    player_name "Can I go now?"
    show jenny 7 at right
    show player 11
    jen "Wait!!"
    show jenny 9 at Position(xpos=937)
    jen "We're not done yet."
    show jenny 12
    jen "Don't you want to know what my end of the deal is?"
    show jenny 10
    show player 12
    player_name "Right... let me guess: Another insult or something..."
    show jenny 9
    show player 16
    jen "{b}*Sigh*{/b}."
    show player 11
    jen "I was hoping to find someone else to do this with... but you'll have to do."
    show jenny 9b
    player_name "..."
    show jenny 19 at right
    jen "I need you to fuck me."
    show jenny 18
    player_name "!!!" with vpunch
    show player 10
    player_name "What? I don-"
    show jenny 7
    show player 11
    jen "DON'T GET ANY IDEAS!"
    show jenny 9 at Position(xpos=937)
    jen "I'm only doing this because I need to boost my channel!"
    show jenny 10
    show player 10
    player_name "I don't think I want-"
    show jenny 7 at right
    show player 11
    jen "You're COMPLAINING?!!" with hpunch
    show jenny 8
    player_name "!!!"
    show player 10
    player_name "No! It's just that, sometimes, I feel like you're just using me for money..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Oh, please! Stop pretending."
    jen "I know you've been enjoying this little game of ours..."
    jen "And now, you finally get to do what you wanted to for so long..."
    show jenny 12
    jen "You get to fuck me."
    jen "Don't lie to me! I know you've been fantasizing about this moment for a long while now."
    jen "So this is your chance, pervert."
    show jenny 82
    show player 4
    player_name "..."
    show player 14
    player_name "Okay! I'm in!"
    player_name "But, what do I have to do for your cam show?"
    show jenny 12
    show player 1
    jen "Let me get dressed in this outfit, first."
    jen "Then I'll explain what we're going to do..."
    show jenny 9
    show player 11
    jen "...and you better do EXACTLY as I say! Got it?!"
    show jenny 82
    show player 21
    player_name "Yes, {b}[jen_name]{/b}..."
    scene black with fade
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 11 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "You really couldn't find me a more fitting outfit?!"
    show jenny 167
    show player 10
    player_name "Well, it's yours from high school... I figured it would still fit you."
    show jenny 164
    show player 11
    jen "Yeah, it fit five years ago, you moron!"
    jen "Can't you see that my tits got BIGGER?!"
    show jenny 167
    show player 10
    player_name "I'm sorry..."
    show jenny 166
    show player 11
    jen "Oh, forget it! Just sit on my bed and don't say anything while I set up for the cam show..."
    jen "Just sit back, keep that cock of yours nice and hard, and let me know when you're about to cum."
    jen "Got it, idiot?"
    show jenny 108
    show player 21
    player_name "Okay..."
    scene jenny_webcam2
    show jenny 151 zorder 2 at Position(xpos=407,ypos=748)
    show jenny_cheer1 zorder 3 at Position(xpos=439,ypos=724)
    show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
    show xtra 20 zorder 4 at left
    with fade
    jen "Alright, we're live!"
    show jenny 155
    jen "Heyyy guys!"
    show jenny 151
    jen "Sorry about the wait! I know you've all been waiting patiently to see me..."
    jen "... but I have something special on the menu for you today!"
    jen "I'm a diiirty little high school slut, wearing only my cheerleader outfit, with no panties..."
    jen "I also have my horny boyfriend, waiting to fuck me with his huuuge cock..."

    jen "Let's get started, shall we?"
    hide jenny
    hide jenny_cheer1
    show jennysex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
    show playersex 116b
    with fastdissolve
    jen "Just gotta do a few things..."
    hide jennysex
    show jennysex 104 zorder 1 at Position(xpos=122,ypos=540)
    show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
    with fastdissolve
    jen "Let me remove this skirt, first..."
    show jennysex 105 at Position(xpos=144,ypos=544) with fastdissolve
    pause
    show jennysex 106 at Position(xpos=170,ypos=542) with fastdissolve
    jen "Now, let's use these to make sure he doesn't go anywhere, while I fuck his brains out..."
    show jennysex 106b
    show playersex 120
    player_name "You're not really going to-"
    show jennysex 107 zorder 2 at Position(xpos=300,ypos=542)
    show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
    with fastdissolve
    pause
    show playersex 125
    show jennysex 109 at Position(xpos=357,ypos=620)
    with fastdissolve
    jen "What do you say, guys? Should we find out what's hiding under his shorts?"
    show jennysex 108
    player_name "..."
    show jennysex 111 at Position(xpos=375,ypos=634) with fastdissolve
    jen "Oh, wow..."
    show jennysex 112 at Position(xpos=374,ypos=674)
    show playersex 127
    jen "Will you look at that nice, thick, long cock..." with vpunch
    show jennysex 113 with fastdissolve
    jen "Let's make it nice and hard."
    show jennysex 115b with fastdissolve
    pause
    show jennysex 114b_115b
    pause 8
    show jennysex 114
    jen "I wonder if it'll fit inside me..."
    show jennysex 115b
    player_name "!!!"
    show playersex 126
    player_name "We're having sex right now?"
    player_name "Shouldn't we, you know, use a cond-"
    show jennysex 110b at Position(xpos=423,ypos=674)
    show playersex 127b
    jen "Shhh!!!" with hpunch
    jen "My fans want to see raw sex, okay??!"
    jen "So I'll just make sure you cum outside, got it!?"
    show jennysex 114 at Position(xpos=374,ypos=674)
    show playersex 127
    with fastdissolve
    jen "Sorry about that, guys!"
    show jennysex 115
    jen "My boyfriend is just... shy."
    show jennysex 114
    jen "Now, let's give you what you've all been waiting for..."
    show jennysex 116 at right with dissolve
    pause
    show jennysex 119b at Position(xpos = 939, ypos = 674) with fastdissolve
    jen "Oh, YESS!!"
    show jennysex 117b with fastdissolve
    jen "It's so... {b}deep{/b}!!"
    $ M_jenny.set("sex speed", .3)
    show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
    pause 8
    show jennysex 117b
    jen "I love riding my boyfriend's cock!"
    show jennysex 118b
    jen "It barely fits in my tight pussy...."
    show jennysex 119
    pause
    show jennysex 120
    pause
    show jennysex 121
    pause
    return

label sis_cheerleader_fuck_after_initial:
    scene jennybedroom
    show jenny 109 at right
    show player 13 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Well done!"
    show jenny 108
    show player 21
    player_name "We did okay?"
    show player 13
    show jenny 109
    jen "I think so: my subscribers seem to love the new content."
    jen "I have to say though..."
    jen "I didn't expect a little pervert like you to be able to perform like that."
    jen "You did pretty well, I guess."
    show jenny 108
    show player 14
    player_name "Really?"
    show jenny 109
    show player 13
    jen "Maybe I can use you again for more cam shows..."
    show player 21
    show jenny 167
    player_name "Thanks, I enjoyed-"
    show jenny 164
    show player 11
    jen "No, STOP that!!" with hpunch
    show jenny 166
    jen "This was {b}strictly business{/b}, nothing else!"
    jen "Don't start getting ideas. I'm doing this to earn good money..."
    jen "Oh, and do me a favor, try not to spend TOO much time with {b}[deb_name]{/b}..."
    jen "I know what you two are up to, but I need you {b}fresh{/b} and {b}rested{/b}."
    jen "My subscribers are expecting more cam shows this week."
    show jenny 164
    jen "So NO jerking off, and NO sex!!"
    show jenny 165
    show player 12
    player_name "Okay! Okay! I got it..."
    show jenny 109
    show player 13
    jen "Good!"
    show jenny 164
    show player 11
    jen "Now, {b}GET OUT OF MY ROOM{/b}!!" with hpunch
    hide player
    hide jenny
    hide jenny_cheer2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
