label barn_garden_statue_dialogue:
    $ M_daisy.trigger(T_daisy_view_statue)
    if player.has_item("milk_sample"):
        call expression game.dialog_select("barn_statue_has_milk")
        $ M_daisy.trigger(T_daisy_awaken_statue)
    else:
        call expression game.dialog_select("barn_statue_has_not_milk")
    $ game.main()

label barn_statue_has_milk:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 712 at left with dissolve
    player_name "( So, a {b}milk pail{/b}, huh? )"
    pause
    show diane b_shirtless a_shirtless_sides f_shamed_talk_smile at Position (xpos=600) with dissolve
    dia "What are you doing with that {b}milk{/b}, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 713
    player_name "I have an idea."
    show player 184 with dissolve
    show diane f_shamed_talk_look
    dia "You have an idea?"
    hide player with dissolve
    dia "You're not gonna-"
    scene expression "backgrounds/location_diane_garden_cutscene09.jpg"
    show expression FilteredText("I had to pour milk into that pail.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("It was like some urge that I couldn't fight.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("I'm not sure what I was expecting to happen...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene expression "backgrounds/location_diane_garden_cutscene10.jpg"
    show expression FilteredText("... But I never could have anticipated what did.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("The statue started to crack and a strange glow began to emit from it.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("Before long, it was so bright, {b}Diane{/b} and I had to shield our eyes!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression player.location.background_blur with None
    show player 428 at left
    show diane b_shirtless a_shirtless_sides f_surprised_front at Position (xpos=600)
    with dissolve
    player_name "!!!"
    show diane f_surprised_front_talk
    dia "What in the world-"
    show diane f_surprised_front
    show player 10b
    player_name "It's glowing..."
    show player 428
    pause
    show diane f_surprised_front_talk
    dia "It's so bright!"
    show player 718
    show diane f_scream a_shirtless_cover
    with dissolve
    dia "Ack!"
    player_name "!!!"
    show daisy b_appear_flash a_empty f_empty at Position (xpos=300) with flash
    pause
    show daisy b_appear with dissolve
    pause
    show player 23 with None
    show daisy f_sad_talk_closed b_naked a_naked_up
    show diane f_scared a_shirtless_sides
    with dissolve
    cow "No, master!!!"
    show player 428
    cow "Please, I'll be a good girl!"
    cow "I will, I'll-"
    show player 22
    pause
    show player 5b
    show daisy f_sad_talk
    pause
    show daisy f_scared b_naked a_naked_cover
    cow "AHHHHHHH!!!" with hpunch
    show daisy f_sad_talk_closed
    cow "D-don't look at me!"
    cow "I didn't mean to!!"
    show player 10b
    player_name "What in the hell?"
    show player 5b
    cow "You can't see me!"
    cow "Please, he'll hurt me if he finds out!"
    show player 11
    show diane f_scared_talk
    dia "Who's gonna hurt you, sweetie?"
    show diane f_scared with None
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "Master."
    show player 4 with dissolve
    show diane f_scared_talk
    dia "Who?"
    show diane f_scared
    show daisy f_sad_talk
    cow "{b}*Waaaah*{/b}"
    show daisy f_sad
    show player 10
    player_name "I think she's talking about {b}Jebadiah Delmont{/b}."
    show player 5
    show diane f_scared_talk
    dia "Who in the heck is {b}Jebadiah Delmont{/b}?"
    show diane f_scared
    show player 12
    player_name "Uhh, it's a long story..."
    show player 5
    pause
    show player 12
    player_name "Let's just say he's the guy who made the statue."
    show player 5
    pause
    show diane f_sad_talk
    dia "Is that who you're talking about, sweetie?"
    show diane f_sad
    show daisy f_sad_talk_closed
    cow "{b}*Sniff*{/b} Uh huh."
    show daisy f_sad
    show diane f_sad_talk
    dia "Aww, you poor thing."
    dia "Don't you worry, he's not gonna hurt you ever again."
    show diane f_sad
    show daisy f_sad_talk
    cow "{b}*Sniff*{/b} He will..."
    show daisy f_sad
    show diane f_sad_talk
    dia "No, I won't let him."
    show diane f_sad
    show daisy f_sad_talk a_naked_wiping_tears with dissolve
    cow "Y-you promise?"
    show daisy f_shy_sad b_naked_shy a_naked_shy_cover at Position (yoffset=10) with dissolve
    show diane f_shamed_talk_smile
    dia "I promise."
    hide daisy
    hide diane
    show daisy b_naked_diane_comfort_shirtless a_empty f_empty
    show diane a_empty b_empty f_shamed_talk_look_closed
    with dissolve
    pause
    show diane f_shamed_talk_look
    dia "Aww, there there..."
    dia "Everything is gonna be okay."
    dia "Let's get you into the barn and get you covered up, okay?"
    show daisy b_naked_diane_comfort2_shirtless
    show diane f_shamed_talk_look_closed
    cow "{b}*Sniff*{/b} O-okay."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 34
    player_name "( What in the hell just happened?! )"
    player_name "( Was {b}Clyde's{/b} kooky grandfather really a wizard?! )"
    pause
    show player 37 with dissolve
    player_name "( {b}I should follow them into the barn and learn more.{/b} )"
    hide player with dissolve
    return

label barn_statue_has_not_milk:
    scene expression player.location.background_blur with None
    show player 426 with dissolve
    player_name "( Wow, the statue does look really good in Diane's garden! )"
    pause
    player_name "( There is something off about it though. )"
    player_name "( She almost looks like she's afraid... )"
    pause
    show player 4 with dissolve
    player_name "( ... And why does she have a {b}milk pail{/b}, I wonder? )"
    pause
    show player 426 with dissolve
    player_name "( Hmm, strange... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
