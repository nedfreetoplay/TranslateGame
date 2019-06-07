label art_classroom_ross_start:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    player_name "Hey, {b}Miss Ross{/b}."
    show player 1f
    show ross 2
    ross "Well hello there, {b}[firstname]{/b}!"
    show ross 25 with dissolve
    ross "I heard about your Father passing..."
    ross "You poor thing, I've been praying for you."
    show ross 24
    show player 2f
    player_name "Uhh, Thanks!"
    show player 1f
    show ross 25
    ross "Oh, it's no problem, Honey."
    ross "You let me know if there's ever anything I can do for you."
    show player 2f
    show ross 24
    player_name "Well, actually, there might be something you can do."
    player_name "I need a way to {b}improve my art grade{/b}."
    show player 1f
    show ross 25
    ross "Oh yes, it dropped quite a bit during your absence."
    ross "It's really too bad. You were top of the class before you left..."
    show player 10f
    show ross 24
    player_name "I was?!"
    show player 11f
    show ross 11
    ross "Aww, don't be modest, {b}[firstname]{/b}! You have such a talent for art!"
    show player 2f
    show ross 10
    player_name "Heh, Yeah, I guess..."
    show player 1f
    show ross 11
    ross "I'm certain we can come up with some way to improve your grade."
    show ross 2 with dissolve
    ross "Hmm, why don't we talk about it after class today?"
    show player 2f
    show ross 1
    player_name "That sounds great! Thanks so much, {b}Miss Ross{/b}!"
    show player 1f
    show ross 2
    ross "Well go {b}grab a slab of clay{/b} and take a seat so we can start the pre-class meditation."
    show player 10f
    show ross 1
    player_name "Meditation?"
    show player 11f
    show ross 2
    ross "Of course! We have to relax our minds and align our chakras if we want our creativity to flow correctly!"
    show player 10f
    show ross 1
    player_name "Ugh. Yes, Ma'am."
    return

label art_classroom_mia_find_easel:
    scene art_classroom_b
    show player 4 with dissolve
    player_name "Hmm..."
    show player 12 with dissolve
    player_name "Let's see if I can find an {b}easel{/b} I could use to draw some tattoo ideas..."
    hide player with dissolve
    return

label easel_dialogue_mia_show_tattoo:
    show player 14 with dissolve
    player_name "( I should show the drawing I made to {b}Mia{/b} first, before I make another one. )"
    hide player with dissolve
    return

label easel_dialogue_mia_draw_tattoo_intro:
    scene school_art_tattoos
    player_name "Hmm..."
    player_name "( What should I draw for {b}Mia{/b}... )"
    return

label easel_dialogue_mia_draw_tattoo_drawn:
    hide player with dissolve
    scene school_art_cs01
    with fade
    show text "I've drawn so many pictures before...\n...But, doing something like this for {b}Mia{/b} made me super nervous!\nI hope it's what she wants..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve
    scene art_classroom_b
    show player 381 with dissolve
    player_name "Not bad!"
    show player 386
    player_name "( I should go and show {b}Mia{/b} what I made. )"
    player_name "( Hopefully, she'll like it... )"
    hide player with dissolve
    return

label art_classroom_ross_molding_clay_cutscene:
    scene location_school_art_cutscene03
    with fade
    show text "It was nice to be back in art class again." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I always had a bit of a knack for it." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_art_cutscene04
    with fade
    show text "Sadly, the same couldn't be said for my friends..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 547f at right
    show ross 27 zorder 1 at left
    with dissolve
    ross "Goodness, what a cute little giraffe, {b}[firstname]{/b}!"
    show player 548f
    show ross 26
    player_name "You think so?"
    show player 547f
    show ross 27
    ross "Simply Adorable!"
    show ross 13 with dissolve
    ross "It's certainly very -- Gifted. Isn't it?"
    show player 10f with dissolve
    show ross 12
    player_name "Huh?"
    show player 11f
    show ross 13
    ross "I just mean it's so long and thick..."
    show player 2f
    show ross 12
    player_name "... Oh, you mean the neck!"
    show player 1f
    show ross 11
    ross "Hehe, yeah that too. It's very well done!"
    show ross 10
    player_name "..."
    show ross 11
    ross "So what are we going to do about these low grades of yours?"
    show ross 13
    ross "I can think of more than a few uses for those talented hands..."
    show player 11f
    show ross 12
    player_name "..."
    show ross 13
    ross "Maybe we should start with a little after scho-"
    show ross 12
    smi "{b}Ross{/b}!!!" with hpunch
    show ross 24
    show player 22f
    smi "Where are you, you Quack!?"
    show player 11 zorder 0 at Position(xpos=0.45, ypos=1.0)
    show principal 2 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    smi "You'd better not be doing naked meditation agai-"
    show principal 3b at Position(xpos=0.8, ypos=1.0) with dissolve
    pause
    show principal 27 at Position(xpos=0.75, ypos=1.0) with dissolve

    smi "Oh, there you are!"
    show ross 23
    show principal 26
    ross "Excuse me, I'm with a student right now..."
    show ross 22
    show principal 27
    smi "Pfft. He's just gonna have to wait."
    smi "I need to talk to you about all this stuff you ordered."
    show ross 25
    show principal 26
    ross "You mean the art supplies?"
    show ross 24
    show principal 27
    smi "I don't know! Whatever this stuff is it's not happening!"
    show ross 25b
    show principal 26
    ross "B-but..."
    show ross 24
    show principal 27
    smi "Look, it's just not in the budget {b}Barbara{/b}."
    smi "You're going to have to make do without this stuff."
    show ross 25
    show principal 26
    ross "{b}Principal Smith{/b}, we need those supplies! Our equipment is in shambles!"
    show ross 24
    show principal 27
    smi "I can't give you what I don't have, now can I?"
    show principal 26
    ross "..."
    show principal 28 at Position(xpos=0.7, ypos=1.0) with dissolve
    smi "Just be thankful you still have any {b}budget{/b} at all."
    smi "Do you have any idea how hard it is to sell this, hippie crap you teach to the school board?"
    show ross 25b
    show principal 26 at Position(xpos=0.75, ypos=1.0) with dissolve
    ross "... But Art is important to an individuals growth!"
    show ross 24
    show principal 27
    smi "Yeah, sure it is..."
    smi "The answer is NO, {b}Barbara{/b}!"
    smi "You're just gonna have to tough it out."
    hide principal
    with dissolve
    pause
    hide player
    show player 11f zorder 1 at right
    show ross 23
    with dissolve

    ross "Arrghh!"
    ross "Every year it gets worse and worse!"
    show ross 22
    pause
    show mia 12b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve

    mia "You alright, {b}Miss Ross{/b}?"
    show ross 11
    show mia 8b
    ross "Oh, hello, {b}Mia{/b} dear."
    show ross 10
    show mia 12b
    mia "I heard {b}Principal Smith{/b} yelling at you..."
    show mia 8b
    show player 10f
    player_name "Yeah, it definitely didn't sound good."
    show player 11f
    show ross 25
    ross "There's just so little budget for art."
    show ross 25b
    ross "It gets smaller and smaller each year."
    show ross 25
    ross "I'm afraid I might not have a job soon..."
    show ross 24
    show mia 12b
    mia "Seriously?"
    mia "They can't just cut art class can they?"
    show ross 25
    show mia 8b
    ross "I wouldn't put it past {b}Principal Smith{/b}. She has no respect for the things I teach."
    show ross 25b
    ross "If only I could find a way to increase the funding a little..."
    show ross 24
    show player 10f
    player_name "Hmm, how much money would you need?"
    show ross 25
    show player 11f
    ross "I'm not sure."
    show ross 24
    pause
    show mia 12b
    mia "Would a thousand dollars help?"
    show mia 8b
    show ross 25
    ross "Huh? Yeah, that would be plenty to order new equipment, restock the art shelves, and maybe even hire some real models for you kids to paint."
    ross "... But where would we get that kind of money?"
    show ross 24
    show mia 62 at Position(xpos=0.585, ypos=1.0) with dissolve

    mia "You could enter {b}the Mayor's art contest{/b}!"
    show mia 63
    show ross 11
    ross "{b}The Mayor{/b} is hosting an art contest?"
    show mia 62
    show ross 10
    mia "Yeah, take a look."
    show flyer 1 zorder 3 with dissolve
    show mia 63
    pause
    hide flyer with dissolve

    show player 10f
    player_name "First place is a thousand dollars, huh?"
    show player 2f
    player_name "{b}Miss Ross{/b}, you should enter!"
    show player 1f
    show ross 27 with dissolve
    ross "Oh heavens, no! I wouldn't have a chance of winning something like that..."
    show ross 26
    show mia 7 at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "..."
    show ross 27
    ross "... But {b}[firstname]{/b} might."
    show ross 26
    show player 10f
    player_name "What?!"
    player_name "No way! I'm not talented enough for something like that."
    show ross 11 with dissolve
    show player 11f
    ross "Nonsense! You're the most talented student I've had in a long time!"
    ross "With me guiding you, it's practically a sure thing!"
    show ross 10
    show mia 9
    mia "Hehe, this is so exciting!"
    show mia 10b
    mia "You can do it, {b}[firstname]{/b}!"
    show mia 7
    show ross 11
    ross "See, {b}Mia{/b} here believes in you! Let's give it a shot!"
    show player 10f
    show ross 10
    player_name "I dunno..."
    show player 11f
    show ross 27 with dissolve
    ross "What if I promised to raise your grades?"
    show player 10f
    show ross 26
    player_name "You'd raise my grades?"
    show player 11f
    show ross 27
    ross "All you have to do is stay late to practice your techniques with me for a few weeks and enter something into the contest."
    ross "You do that and I'll give you an A+!"
    show player 10f
    show ross 26
    player_name "An A+?!"
    player_name "Just for entering?"
    show player 11f
    show ross 27
    ross "That's right. Do we have a deal?!"
    show ross 26
    pause
    show player 2f
    player_name "Yeah, Okay. I'll do it!"
    show player 1f
    show mia 9
    mia "Yay!"
    show mia 7

    hide player
    show ross 21 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Oh, I knew you wouldn't let me down, {b}[firstname]{/b}!"
    ross "Come back here {b}tomorrow after class{/b} and we'll get started!"
    show ross 11 at left
    show player 11f at right
    with dissolve
    ross "Alright, {b}[firstname]{/b}?"
    show ross 10
    show player 10f
    player_name "Okay, {b}Miss Ross{/b}. I'll see you tomorrow then."

    $ game.timer.tick()
    $ M_ross.trigger(T_ross_molded_clay)
    $ game.main()

label leave_art_classroom:
    if not M_ross.is_state(S_ross_grab_clay):
        jump left_hall_dialogue
    else:

        scene location_school_art_closeup
        show player 2 with dissolve
        player_name "{b}Miss Ross{/b} wants me to grab a slab of clay and take my seat."
        $ game.main()

label player_ross_magazines_3_left:
    show player 14 with dissolve
    player_name "I found one stack of magazines!"
    player_name "If I can find two more stacks this size, I should have enough to make that art collage."
    hide player with dissolve
    $ player.get_item("magazines1")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_2_left:
    show player 14 with dissolve
    player_name "Now I just need to find one more stack of magazines for {b}Miss Ross{/b}."
    hide player with dissolve
    $ player.remove_item("magazines1")
    $ player.get_item("magazines2")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_1_left:
    show player 14 with dissolve
    player_name "Thats it! I should have plenty of magazines to start working on the art collage for {b}Miss Ross{/b}!"
    hide player with dissolve
    $ player.remove_item("magazines2")
    $ player.get_item("magazines")
    $ M_ross.trigger(T_ross_found_magazines)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
