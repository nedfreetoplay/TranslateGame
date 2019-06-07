label treasure_open_no_key:
    player_name "( Even if I had the combination I still need to find the {b}key{/b}! )"
    return

label beach_island_aqua_treasure_search:
    scene location_beach_island_blur
    show player 11 at left with dissolve
    pause
    show player 10
    player_name "That's one {b}strange looking statue.{/b}"
    show player 2
    player_name "..."
    player_name "But according to the map, the {b}treasure{/b} should be right here."
    hide player with dissolve
    return

label beach_statue_no_shovel:
    scene location_beach_island_blur
    show player 2 at left
    player_name "( I can't dig for {b}buried treasure{/b} without a {b}shovel.{/b} )"
    show player 4
    player_name "( ...I think we have one at {b}home{/b} somewhere. )"
    hide player with dissolve
    return

label beach_statue_aqua_treasure_search:
    scene location_beach_digging01 with fade
    show text "I continued to dig for what must have been hours..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...before long I started to tire, my arms aching." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Exhaustion was about to overtake me and I considered giving up." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Was I in the wrong spot?" at Position (xpos= 512, ypos= 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    scene location_beach_digging02 with fade
    show text "... Then, bang! My shovel hit something hard!" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    show text "My strength returned in an instant as I hurried to uncover what Ben Dover had buried." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    show text "...It was a large heavy chest; This was it! I had found the treasure!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label treasure_lock_intro:
    scene location_beach_lock with fade
    player_name "oh man.."
    player_name "( It looks like I need a {b}key{/b}...And a {b}combination{/b} to open this. )"
    return

label treasure_unlocked:
    scene location_beach_treasure
    if M_aqua.is_state(S_aqua_treasure_unlock):
        call expression game.dialog_select("treasure_aqua_treasure_unlock")
        $ player.get_item("golden_compass")
        $ M_aqua.trigger(T_aqua_treasure_unlocked)
    else:

        with fade
        pause
    $ game.main()

label treasure_aqua_treasure_unlock:
    show expression "objects/object_compass_01.png" at Position(xpos = 537, ypos = 473)
    with fade
    hide expression "objects/object_compass_01.png"
    call screen treasure_chest
    show closeup_compass_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
    player_name "Whoa!!"
    player_name "( I can't believe it! I found the treasure! )"
    player_name "( This has to be the compass Terry was talking about. )"
    show popup_item_compass1 at truecenter with dissolve
    pause
    hide popup_item_compass1 with dissolve
    hide closeup_compass_01 with dissolve
    return

label beach_roxxy_spin_bottle_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 13f at right with dissolve
    player_name "( Wow, this is the perfect day for the beach! )"
    player_name "( I wonder if the girls are here already? )"
    hide player
    show roxxy bikini 17f at right
    with dissolve
    rox "{b}[firstname]{/b}!!"
    player_name "!!!"
    pause
    hide roxxy
    show roxxy bikini 1f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "H-hey, {b}Roxxy{/b}..."
    show player 13f
    show roxxy bikini 2f
    rox "I'm glad you made it!"
    show becca bikini 11 at Position(xpos=315)
    show missy bikini 1 at left
    with dissolve
    show roxxy bikini 1f
    becca "Eugh, you two are hugging now?"
    show becca bikini 12
    show missy bikini 2
    missy "Hi, {b}[firstname]{/b}!!!"
    show missy bikini 1
    show player 14f
    player_name "Hey, {b}Missy{/b}! {b}Becca{/b}..."
    player_name "You all look beautiful in your swimsuits!"
    show player 13f
    show missy bikini 2b
    missy "Hehehe, I do?!"
    show missy bikini 1b
    becca "..."
    show becca bikini 11
    becca "Just try not to stare, Perv."
    show becca bikini 12
    show missy bikini 2b
    missy "Does this top make my boobs look bigger?"
    show missy bikini 1b
    show becca bikini 14
    becca "Silicone is the only thing that's gonna make those tiny tits look bigger..."
    show becca bikini 12
    show missy bikini 11
    show player 5f
    player_name "..."
    show roxxy bikini 19 at Position (xpos=600) with dissolve
    rox "Are you gonna be a bitch all day, {b}Becca{/b}?"
    show roxxy bikini 20
    show becca bikini 11
    becca "... Maybe."
    becca "Is HE gonna be here all day?"
    show becca bikini 12
    show roxxy bikini 19
    rox "{b}*Sigh*{/b}"
    show roxxy bikini 20
    show player 10f
    player_name "... {b}Becca{/b}, I umm..."
    show missy bikini 1
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "... I brought you something!"
    show player 239_240f with dissolve
    show becca bikini 11
    becca "Why would I want anything from-"
    show player 654bf with dissolve
    show becca bikini 6
    becca "!!!"
    becca "Oh my god!"
    becca "Is that {b}GoldSchwagger{/b}!!!?"
    show player 654f
    player_name "... Umm, yes?"
    show player 654bf
    show becca bikini 17
    becca "OhmygodohmygodOHMYGOD!!!"
    show becca bikini 8
    show player 13f
    with dissolve
    show roxxy bikini 1 at Position (xpos=600) with dissolve
    becca "This. stuff. is. THE BEST!"
    show becca bikini 7 with dissolve
    becca "Thanks for-"
    show becca bikini 7c
    becca "..."
    show becca bikini 7
    becca "I mean..."
    show becca bikini 7b
    show roxxy bikini 2
    rox "See {b}Becca{/b}."
    rox "{b}[firstname]{/b} is a good guy!"
    show roxxy bikini 1
    show missy bikini 2b
    missy "And cute!"
    show missy bikini 1b
    show becca bikini 7
    becca "... Yeah, well..."
    becca "I guess he's not SO bad."
    becca "For a nerd."
    show becca bikini 7b
    show missy bikini 2b
    missy "A cute nerd!"
    show missy bikini 1b
    show roxxy bikini 2
    rox "Okay, {b}Missy{/b}! We get it!"
    show roxxy bikini 2f at Position (xpos=500) with dissolve
    rox "C'mon, let's get this party started."
    rox "I've gotta get some sun!"
    hide roxxy
    show becca bikini 8
    with dissolve
    becca "I can't believe he brought me {b}GoldSchwagger{/b}!"
    hide becca with dissolve
    becca "{b}Dexter{/b} always forgets!"
    show player 17f
    player_name "..."
    show missy bikini 2b
    missy "C'mon {b}[firstname]{/b}, you can sit next to me!"
    show missy bikini 1b
    show player 14f
    player_name "Heh, sounds good."
    hide player
    hide missy
    with dissolve
    scene expression "backgrounds/location_beach_cutscene02.jpg"
    with fade
    show text "Beautiful weather. Beautiful beach. Beautiful girls...\n... What more could a guy ask for?!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Becca{/b} and {b}Missy{/b} may not have been the greatest conversationalists in the world...\nBut they made up for those shortcomings in other ways!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... And {b}Roxxy{/b} turned out to be surprisingly good company!\nIt almost felt like we were close to becoming friends..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause

    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 3 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "... And then the entire pyramid collapsed!!"
    show roxxy sitting 2
    show missy sitting 5
    missy "Hahahaha!"
    show missy sitting 2
    show player_sitting 4
    player_name "The whole thing?!"
    show player_sitting 3
    show becca sitting 3
    becca "Yeah... And this skinny bitch landed cunt first, right on my face!"
    show becca sitting 2
    show missy sitting 5
    missy "Aaahahahaha!"
    show player_sitting 4
    player_name "... Really?!"
    show player_sitting 3
    show roxxy sitting 3
    rox "It was pretty hilarious!"
    show roxxy sitting 2
    missy "{b}*Snort*{/b} Hahahaaaaah!"
    show becca sitting 7
    becca "... For you maybe!"
    becca "She's heavier than she looks!"
    show becca sitting 8
    show missy sitting 3
    missy "At least..."
    show missy sitting 5
    missy "{b}*Snort*{/b} ... At least I was wearing panties that day."
    show becca sitting 7
    becca "No, that little pink thong doesn't count!"
    show becca sitting 2
    show missy sitting 6
    show player_sitting 4
    player_name "You remember the color?"
    show player_sitting 3
    show becca sitting 3
    becca "Are you kidding? The image of that tiny pink thong coming at me, one hundred miles per hour, is like... Burned into my brain!"
    show becca sitting 5
    becca "It haunts my nightmares!"
    show player_sitting 5
    show missy sitting 5
    show roxxy sitting 5
    rox "Pfft, Hahaha!"
    missy "Hahaha!"
    becca "Hahaha!"
    show roxxy sitting 1
    show becca sitting 1
    show player_sitting 3
    player_name "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "It's getting late... We should really get a fire going if we're gonna hang around."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "That's a good idea-"
    becca "Whew, my head is spinning..."
    show becca sitting 2
    show missy sitting 5
    missy "Hahahaha! {b}*Snort*{/b}"
    show player_sitting 3b
    show roxxy sitting 3
    rox "Sheesh, you two really can't hold your liquor."
    show missy sitting 2
    show roxxy sitting 2
    show player_sitting 4
    player_name "I'll do it."
    player_name "You girls just chill."
    hide player_sitting with dissolve
    show becca sitting 3
    becca "Wow, such a gentleman..."
    show becca sitting 2
    rox "..."
    show roxxy sitting 3
    rox "... You finally warming up to him?"
    show roxxy sitting 2
    show becca sitting 3
    becca "... Maybe."
    becca "A little bit."
    show becca sitting 2
    show roxxy sitting 3
    rox "It's about time!"
    show roxxy sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "For real."
    show becca sitting 1
    missy "Hey, {b}[firstname]{/b}?"
    show missy sitting 2
    player_name "Hmm?"
    show missy sitting 3
    missy "Is it true nerds have huge dicks?!"
    show becca sitting 8
    show roxxy sitting 8
    becca "!!!" with hpunch
    rox "!!!"
    show missy sitting 2
    show becca sitting 7b
    show roxxy sitting 7
    becca "What the hell, {b}Missy{/b}?!"
    show becca sitting 6b
    show roxxy sitting 3
    rox "Oookay!"
    show becca sitting 6
    rox "No, more beer for her..."
    show roxxy sitting 2
    show missy sitting 3
    missy "Oh c'mon, you can't tell me you guys aren't curious?!"
    show missy sitting 2
    show becca sitting 3
    becca "Hahaha, You're such a dumb slut, {b}Missy{/b}..."
    show becca sitting 2
    show roxxy sitting 5
    rox "Hahaha!"
    show roxxy sitting 2
    show missy sitting 3
    missy "... So?"
    missy "I'm having fun!"
    show missy sitting 6
    missy "..."
    show missy sitting 3
    show becca sitting 8
    missy "Oh my gosh! I just had the best idea!"
    show becca sitting 2
    show missy sitting 2
    show roxxy sitting 3
    rox "Uh oh."
    show roxxy sitting 2
    show becca sitting 3
    becca "This should be good."
    show becca sitting 2
    show missy sitting 7
    missy "No seriously, shut up!"
    show missy sitting 3
    show becca sitting 8
    missy "We should play {b}Spin the Bottle{/b}!"
    show becca sitting 1
    show missy sitting 2
    show roxxy sitting 3
    rox "What?!"
    show roxxy sitting 2
    show missy sitting 3
    missy "Yeah, c'mon! It'll be so much fun!"
    show missy sitting 2
    show roxxy sitting 6
    rox "You just wanna kiss {b}[firstname]{/b}..."
    show roxxy sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "Hell yeah!"
    missy "Don't you?!"
    show becca sitting 1
    show missy sitting 2
    show roxxy sitting 7
    rox "..."
    show roxxy sitting 6
    rox "Uhh, no... Not really."
    rox "... And I doubt {b}Becca{/b} wan-"
    show roxxy sitting 2
    show becca sitting 3
    becca "I'll play!"
    show becca sitting 2
    show roxxy sitting 7
    rox "!!!" with hpunch
    show roxxy sitting 8
    rox "Really?!"
    show roxxy sitting 7
    show becca sitting 3
    becca "Meh, why not?"
    becca "I'm pretty wasted so I probably won't remember anyways..."
    show roxxy sitting 1
    show becca sitting 2
    show missy sitting 5
    missy "That's the spirit!"
    show missy sitting 2
    show roxxy sitting 2
    rox "..."
    show roxxy sitting 6
    rox "Well, I guess if you guys really want to... I'll play."
    show player_sitting 1 zorder 0 at Position (xpos=650) with dissolve
    show roxxy sitting 3
    rox "You okay with playing spin the bottle {b}[firstname]{/b}?"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "Uhh... I dunno."
    player_name "How does it work?"
    show player_sitting 3b
    show roxxy sitting 6
    rox "You seriously don't know?"
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Of course he doesn't, he's a nerd..."
    becca "We'll show you."
    show becca sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "Oh, I'm so going first!"
    show becca sitting 2
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "{b}*Sigh*{/b} Fine."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 5
    missy "Yay!!"
    show missy sitting 3
    show becca sitting 8
    missy "Okay, so all you have to do is {b}Spin this bottle{/b} and then {b}Kiss whomever it's pointing at{/b} when it comes to a stop."
    show becca sitting 2
    show missy sitting 2
    show player_sitting 5
    player_name "!!!" with hpunch
    show player_sitting 4
    player_name "Kiss?!"
    player_name "Like on the lips?"
    show player_sitting 5
    show missy sitting 3
    missy "That's right!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "We really don't have to play if you don't want to..."
    show roxxy sitting 2
    show player_sitting 4
    player_name "N-no! I'll play!"
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 6 zorder 1 at right
    show becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Hehe, I bet you will..."
    show becca sitting 2
    rox "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Alright."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 4 with dissolve
    missy "Okay, so I spin first!"
    call screen spin_bottle("becca", True)
    show missy sitting 6
    missy "..."
    show missy sitting 3
    missy "... And then {b}[firstname]{/b} kisses me!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "Wait a second!"
    rox "... It landed on {b}Becca{/b}. Not {b}[firstname]{/b}!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    show becca sitting 8
    missy "Oh, did it?"
    missy "{b}*Sigh*{/b} Fine."
    hide becca
    hide missy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show missy front sitting 1 at Position (xoffset=8)
    show becca front sitting 1f at Position (xoffset=-8)
    with dissolve
    pause
    show missy front sitting 3 at Position (xoffset=8)
    show becca front sitting 3f at Position (xoffset=-8)
    show missy_arm front sitting 1 at Position (xoffset=8)
    with dissolve
    pause
    hide becca
    hide missy
    hide missy_arm
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 1 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show player_sitting 3
    show missy sitting 7
    missy "There."
    show missy sitting 2
    show becca sitting 7b
    becca "What the hell was that?!"
    show becca sitting 6b
    show missy sitting 7
    missy "Huh?"
    show missy sitting 8
    show becca sitting 7b
    becca "You call that a kiss?"
    show becca sitting 6b
    show missy sitting 1
    missy "..."
    show roxxy sitting 2
    rox "..."
    show missy sitting 7
    missy "What, did you want me to slip you the tongue or something?!"
    show missy sitting 8
    show becca sitting 7b
    becca "Huh?! NO!"
    becca "I'm just..."
    becca "You're a pretty sucky kisser... Is all I'm saying."
    show becca sitting 6b
    show missy sitting 7
    missy "Shut up!"
    missy "That's not fair, I wasn't trying!"
    missy "{b}[firstname]{/b}, I wasn't trying!"
    show missy sitting 8
    show becca sitting 1
    show player_sitting 5
    player_name "..."
    show player_sitting 4
    player_name "I'm not... I mean-"
    show player_sitting 5
    show missy sitting 7
    missy "Seriously, I wasn'-"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 6
    rox "MOVING ON!"
    show roxxy sitting 3
    show missy sitting 6
    rox "{b}[firstname]{/b} It's your turn."
    show roxxy sitting 2
    show missy sitting 2
    show player_sitting 4b
    player_name "O-okay..."
    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("becca", True)
    show player_sitting 3
    show missy sitting 7
    missy "{b}Becca{/b} again!"
    missy "This is rigged!"
    show missy sitting 8
    hide player_sitting
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 2
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    becca "It's a beer bottle... How would we rig-"
    show player front sitting 7b
    show player_arms front sitting 3
    show becca front sitting 3
    show player_shadow front sitting 1 zorder 0
    becca "!!!" with hpunch
    show becca front sitting 3b
    show player front sitting 7
    pause
    show becca front sitting 3
    show player front sitting 7b
    pause
    hide becca
    hide player_shadow
    hide player
    hide player_arms
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 2 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "..."
    rox "..."
    show missy sitting 7
    missy "... How was it?!"
    show missy sitting 8
    show becca sitting 3
    becca "... Wow."
    show becca sitting 1
    show player_sitting 5
    show missy sitting 3
    missy "Was it good?!"
    show missy sitting 2
    show becca sitting 2
    becca "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "It looked pretty good!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "{b}Becca{/b}!!!"
    show missy sitting 8
    show becca sitting 6b
    becca "Hmm?"
    show missy sitting 7
    missy "How was it?!"
    show missy sitting 8
    pause
    show becca sitting 3
    becca "Pretty good..."
    show becca sitting 2
    show player_sitting 4
    player_name "It was?"
    show player_sitting 3
    show missy sitting 2
    show becca sitting 3
    becca "{b}*Ahem*{/b} I mean... Yeah, I guess."
    becca "... For a nerd. You know?"
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 4 with dissolve
    rox "Alright, my turn!"
    call screen spin_bottle("missy", True)
    show player_sitting 3b
    show roxxy sitting 3
    rox "Hmm, {b}Missy{/b}..."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Be warned. She sucks."
    show becca sitting 2
    show missy sitting 7
    missy "I do not!"
    missy "Watch this!"
    hide missy
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=2)
    show missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    show missy_arm front sitting 1f at Position (xoffset=-2)
    show roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    pause
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide missy
    hide missy_arm
    hide roxxy_arm
    hide roxxy
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show roxxy sitting 6
    rox "... Sheesh, did you use enough tongue?!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Wow... {b}Roxxy{/b}, you taste like cherries!"
    show missy sitting 2
    show roxxy sitting 6
    rox "Uhh... Right, okay."
    show roxxy sitting 3
    rox "{b}Becca{/b} it's your turn."
    show roxxy sitting 2
    show becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show becca sitting 2 with dissolve
    show missy sitting 7
    missy "{b}[firstname]{/b} again?!"
    missy "This is so unfair!"
    show missy sitting 8
    becca "..."
    rox "..."
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player front sitting 7b
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3
    show becca front sitting 3
    with dissolve
    becca "Mmm..."
    show player front sitting 7
    show becca front sitting 3b
    missy "Oh, man..."
    show player front sitting 7b
    show becca front sitting 3
    rox "..."
    show player front sitting 7
    show becca front sitting 3b
    rox "... You should play with her tits a little, {b}[firstname]{/b}."
    hide player
    hide player_arms
    hide player_shadow
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 7 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "What?!"
    missy "Tits aren't part of the game!"
    show missy sitting 8
    show roxxy sitting 6
    rox "Why not?"
    show roxxy sitting 3
    rox "I'm just saying, they're right there."
    show roxxy sitting 2
    show becca sitting 3
    becca "... Okay. I lied."
    becca "He's really good at that!"
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "Hah, now who's falling in love with him?"
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Shut up!"
    show becca sitting 2
    show missy sitting 4 with dissolve
    missy "Both of you shut up, it's my turn!"
    show missy sitting 2 with dissolve
    call screen spin_bottle("becca", True)
    show missy sitting 7
    missy "Oh c'mon, {b}Becca{/b} again?!"
    missy "What the hell!"
    show missy sitting 8
    show roxxy sitting 3
    rox "Just shut up and kiss her!"
    rox "Properly this time!"
    show roxxy sitting 2
    show missy sitting 7
    missy "{b}*Sigh*{/b} Fine."
    hide missy
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1f at Position (xoffset=-4)
    show missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    show missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "Now that's much better."
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    player_name "..."
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "I bet you're glad you came to hang out with us tonight. Huh, {b}[firstname]{/b}?"
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    player_name "... Definitely!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "Hah!"
    hide missy
    hide becca
    hide missy_arm
    with dissolve
    pause
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 3 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "See, I told you I'm a good kisser!"
    show missy sitting 2
    show becca sitting 7b
    becca "I dunno who told you that but they were lying!"
    becca "You're all tongue!"
    show missy sitting 8
    show becca sitting 2
    show roxxy sitting 5
    rox "Haha!"
    show roxxy sitting 2
    show missy sitting 7
    missy "Grr, screw you both!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "Okay, {b}[firstname]'s{/b} turn!"
    show roxxy sitting 2
    show missy sitting 2
    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("roxxy", True)
    show player_sitting 3b
    show missy sitting 8
    show roxxy sitting 3
    rox "Oh, it looks like it's your lucky night."
    show roxxy sitting 2
    show missy sitting 7
    missy "This sucks..."
    show missy sitting 8
    hide player_sitting
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    show roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    rox "Mmm..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    becca "He's good, right!"
    show player front sitting 7 at Position (xoffset=-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    missy "... So unfair."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide roxxy
    hide roxxy_arm
    hide player_arms
    hide player_shadow
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 8 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3b zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Holy shit, {b}[firstname]{/b}..."
    show roxxy sitting 6
    rox "Why are you so good at that?!"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "... I dunno."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Just... Wow!"
    show roxxy sitting 2
    show missy sitting 3
    show player_sitting 7
    missy "C'mon, let's keep it going!"
    show missy sitting 8
    rox "..."
    show missy sitting 7
    missy "{b}Roxxy{/b}!!!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "Hmm?"
    show roxxy sitting 2
    show missy sitting 7
    missy "It's your turn!"
    show missy sitting 8
    show roxxy sitting 3
    rox "Oh, sorry..."
    show roxxy sitting 4 with dissolve
    call screen spin_bottle("becca", True)
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "{b}Becca{/b} again."
    show missy sitting 8
    rox "..."
    show missy sitting 7
    missy "Why is it always {b}Becca{/b}?!"
    show missy sitting 8
    hide roxxy
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=5)
    show becca front sitting 1f
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    becca "!!!" with hpunch
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    missy "Whoa!"
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    missy "She actually went for her tits!"
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    player_name "..."
    hide roxxy
    hide roxxy_arm
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 7 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "What the hell, {b}Roxxy{/b}?!"
    show becca sitting 6
    show roxxy sitting 6
    rox "Oh, don't pretend like you didn't like it."
    show roxxy sitting 3
    rox "Your nipples are as hard as a rock."
    show roxxy sitting 2
    show becca 8b
    becca "!!!"
    show player_sitting 3b
    show roxxy sitting 6
    rox "Besides, this is boring if it's just kissing."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 1
    becca "..."
    show missy sitting 3
    missy "I agree!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "I bet {b}[firstname]{/b} liked it!"
    show roxxy sitting 2
    show player_sitting 4
    player_name "Y-yeah!"
    player_name "That was awesome!"
    show player_sitting 3
    show roxxy sitting 5
    show missy sitting 5
    show becca sitting 5
    rox "Hahaha!"
    missy "Hahaha!"
    becca "Hahaha!"
    show roxxy sitting 3
    show missy sitting 2
    show becca sitting 2
    show player_sitting 3b
    rox "See {b}Becca{/b}, I know what I'm doing."
    rox "Spin it, bitch!"
    show roxxy sitting 2
    show player_sitting 3
    becca "..."
    show becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show becca sitting 2 with dissolve
    show roxxy sitting 3
    rox "{b}[firstname]{/b}."
    show roxxy sitting 2
    show missy sitting 6
    missy "!!!"
    show missy sitting 7
    missy "This is such bullshit!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 6
    rox "Shut up, {b}Missy{/b}!"
    show roxxy sitting 3
    rox "Some of us are trying to enjoy the show!"
    rox "Get in there {b}[firstname]{/b} and play with her tits this time!"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "... Really?"
    show player_sitting 3b
    show roxxy sitting 3
    rox "Hell yeah!"
    rox "{b}Becca's{/b} got a nice rack."
    show roxxy sitting 6
    rox "... Not as nice as mine but..."
    show roxxy sitting 2
    show becca sitting 7
    becca "Screw you, {b}Roxxy{/b}."
    show becca sitting 6
    show roxxy sitting 3
    rox "You know you want it, bitch..."
    show roxxy sitting 2
    show missy sitting 3
    missy "I want it!"
    show missy sitting 5
    missy "Ahahaah!"
    show becca sitting 6b
    becca "..."
    show roxxy sitting 3
    rox "See, she's totally turned on!"
    show becca sitting 9
    rox "Do it, {b}[firstname]{/b}!"
    show roxxy sitting 2
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    with dissolve
    becca "Mmmm..."
    show player front sitting 7b
    show player_arms front sitting 4d
    show becca front sitting 3
    missy "I'm so jelly right now..."
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    rox "..."
    show player front sitting 7b
    show player_arms front sitting 4d
    show becca front sitting 3
    becca "Nnngh!"
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    missy "Damn!"
    hide player
    hide player_shadow
    hide player_arms
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Ahh..."
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "You should have kept going!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "What?! No way, it's my turn!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "... Oh, shut up, {b}Missy{/b}."
    show roxxy sitting 6
    rox "Look at her."
    rox "A couple of hours ago she didn't want anything to do with him."
    show roxxy sitting 3
    rox "Now she's totally ready to jump his bone."
    show roxxy sitting 2
    show player_sitting 5
    show becca sitting 7
    becca "I am not!"
    show becca sitting 6
    show player_sitting 3b
    show roxxy sitting 5
    rox "Hah. Yeah right!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "Can I spin now, please?"
    show missy sitting 8
    show roxxy sitting 6
    rox "I bet your pussy is sopping wet right now!"
    show roxxy sitting 2
    show becca sitting 8b
    show player_sitting 5
    becca "..."
    show missy sitting 7
    missy "Screw it, I'm spinning!"
    show player_sitting 3
    show missy sitting 8
    show roxxy sitting 3
    rox "Admit it!"
    show roxxy sitting 2
    show becca sitting 10b
    becca "... Shut up!"
    show roxxy sitting 5
    show becca sitting 10
    rox "Ahaha, I knew it!"
    show missy sitting 4 with dissolve
    player_name "..."
    call screen spin_bottle("mc", True)
    show missy sitting 5
    show becca sitting 9
    missy "YES!"
    missy "Finally!"
    show missy sitting 2
    becca "..."
    show missy sitting 3
    missy "Okay, feel free to grope whatever you want, {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 5
    rox "Hahahaah!"
    show roxxy sitting 3
    rox "You are such a dirty slut, {b}Missy{/b}!"
    show roxxy sitting 2
    show becca sitting 2
    show missy sitting 7
    missy "Shhh, don't ruin this for me!"
    show missy sitting 9
    show player_sitting 3b
    show roxxy sitting 3
    rox "Go ahead, {b}[firstname]{/b}."
    rox "Give it to her."
    show roxxy sitting 2
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    show missy_arm front sitting 1 zorder 3
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    hide missy
    hide missy_arm
    hide player
    hide player_arms
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_cutscene03.jpg" with fade
    show text "This turned out to be a wonderful night!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I can't believe I'm actually making out with {b}Roxxy{/b} and {b}her friends{/b}!\nNobody is going to believe me!\n... And {b}Roxxy{/b} is even pushing her friends to take things further!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Why would she do that, I wonder?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause
    scene expression "backgrounds/location_beach_water_evening_blur.jpg"
    show roxxy bikini 1f at Position (xpos=500)
    show becca bikini 9 at Position(xpos=315)
    show missy bikini 1b at left
    show player 14f at right
    with dissolve
    player_name "I should... Really get home."
    player_name "It's getting super late."
    show player 13f
    show missy bikini 2
    missy "Aww, but..."
    show missy bikini 1
    show roxxy bikini 2 at Position (xpos=600) with dissolve
    rox "{b}[firstname]'s{/b} right."
    rox "We gotta get the lush over here home before she passes out."
    show roxxy bikini 1
    show becca bikini 10
    becca "Hmm?"
    becca "No, I'm... {b}*Yawn*{/b}..."
    becca "... I'm fine!"
    show becca bikini 9
    show roxxy bikini 2
    rox "Yeah, right."
    rox "I'm not carrying her this time!"
    show roxxy bikini 1
    show missy bikini 8
    missy "Hey, I had to carry her last time!"
    show missy bikini 1
    show roxxy bikini 2
    rox "Well, you'd better hope she makes it home then."
    rox "'Cause I'm not doing it!"
    show roxxy bikini 1
    show missy bikini 8
    missy "Ahh, man..."
    show missy bikini 1
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    show player 14f
    player_name "Thanks for the great night ladies!"
    show player 13f
    show becca bikini 10
    becca "Thank you for the {b}GoldSchwagger, [firstname]{/b}!"
    show becca bikini 9
    show player 14f
    player_name "Heh, my pleasure!"
    hide becca with dissolve
    pause
    hide player
    show roxxy bikini 17f at right
    with dissolve
    rox "I'll see you at school, {b}[firstname]{/b}."
    show roxxy bikini 18f
    player_name "Thanks for inviting me, {b}Roxxy{/b}!"
    hide roxxy
    show roxxy bikini 2f at Position (xpos=500)
    show player 13f at right
    with dissolve
    rox "Yeah, it was fun!"
    rox "... Maybe we'll do it again {b}next weekend{/b}!"
    hide roxxy with dissolve
    show missy bikini 1b
    missy "..."
    player_name "..."
    show missy bikini 2b
    missy "So... Uhh..."
    missy "Call me... Sometime?"
    show player 11f
    missy "K, bye!"
    hide missy with dissolve
    show player 10f
    player_name "Wait!"
    show player 5f
    player_name "..."
    show player 12f
    player_name "You never gave me your number..."
    show player 5f
    player_name "..."
    show player 10f
    player_name "Oh, well."
    show player 17f
    player_name "( Man, what a night! )"
    player_name "( I'd better get home before {b}[deb_name]{/b} starts worrying. )"
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_no_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 5 with dissolve
    player_name "( {b}Roxxy{/b} and her friends are over there but I can't go in empty handed! )"
    player_name "I should speak with {b}Captain Terry{/b} about getting a bottle of {b}GoldSchwagger{/b} for {b}Becca{/b} first... )"
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_wrong_time:
    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 19f at Position (xpos=500)
    show becca bikini 1b at Position(xpos=315)
    show missy bikini 12 at left
    show player 13f at right
    with dissolve
    rox "Psh, well look who finally decided to showed up!"
    show roxxy bikini 20f
    show player 5f
    show becca bikini 17
    becca "Nerd!"
    show missy bikini 8
    missy "You missed the entire party, {b}[firstname]{/b}!"
    show missy bikini 12
    becca "Hahaha, nerdy neeeeerd!"
    show becca bikini 1b
    show player 12f
    player_name "Is {b}Becca{/b} hammered?"
    show becca bikini 17
    show missy bikini 1
    show player 5f
    show roxxy bikini 19bf
    rox "Yeah, we were just about to take her home..."
    show roxxy bikini 20f
    show player 10f
    player_name "Oh, alright."
    show becca bikini 1b
    player_name "Do you need help or something?"
    show player 5f
    show roxxy bikini 19f
    rox "No, we've got it."
    rox "I'd think that when the most popular girl in school invites you to a party, you'd show up for it on time..."
    show roxxy bikini 20f
    show player 10f
    player_name "I'm sorry, {b}Roxxy{/b}. I must have gotten confused..."
    show player 5f
    show roxxy bikini 19f
    rox "Yeah or you weren't listening!"
    rox "Whatever, I've gotta tend to {b}Becca's{/b} drunk ass..."
    hide roxxy
    hide becca
    with dissolve
    becca "NEEEEEEERD!!!"
    becca "Hahaha!"
    show player 37f with dissolve
    player_name "I really screwed up..."
    show player 5f with dissolve
    show missy bikini 2
    missy "It's okay, {b}[firstname]{/b}"
    missy "{b}Just show up in the afternoon next weekend{/b}."
    missy "{b}Roxxy{/b} will be over it by then."
    show missy bikini 1
    show player 10f
    player_name "Yeah, alright."
    player_name "Thanks, {b}Missy{/b}."
    show player 5f
    show missy bikini 2b
    missy "See ya!"
    hide player
    hide missy
    with dissolve
    return

label beach_roxxy_invite_to_bikini_contest:
    scene expression "backgrounds/location_beach_water_contest_day_blur02.jpg"
    show player 14f at right with dissolve
    player_name "Whoa, look at this place!"
    player_name "There are so many bikinis!"
    show player 31f with dissolve
    player_name "..."
    show player 32f
    player_name "Hey, is that {b}Captain Terry{/b} up there?!"
    player_name "I should go and see what he's doing here."
    hide player with dissolve
    return

label beach_cabin_roxxy_in_cabin:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 13f at right
    show player 10 at left
    with dissolve
    player_name "... {b}Roxxy{/b}?"
    player_name "You alright?"
    show player 5
    show roxxy bikini 15f
    rox "... No."
    rox "Ugh, that was so embarrassing!"
    show roxxy bikini 14f
    show player 10
    player_name "It's not so bad."
    player_name "I don't think anybody saw but {b}Becca{/b} and I..."
    show player 5
    show roxxy bikini 15f
    rox "... Really?"
    show roxxy bikini 14f
    show player 14
    player_name "Yeah."
    player_name "Besides, even if somebody did... Who cares?"
    show player 18
    player_name "You have amazing breasts!"
    player_name "Definitely nothing to be ashamed of..."
    show player 13
    rox "..."
    show roxxy bikini 15 with dissolve
    rox "Yeah, I guess you're right about that."
    show roxxy bikini 14
    rox "..."
    show roxxy bikini 13
    rox "... But what am I going to do?!"
    rox "I can't compete in the contest with a broken bikini top!"
    show roxxy bikini 14
    show player 10
    player_name "You don't have a back up?"
    show player 5
    show roxxy bikini 13
    rox "... No."
    show roxxy bikini 14
    show player 34
    player_name "..."
    show player 14
    player_name "Don't worry, {b}Roxxy{/b}."
    player_name "I'll just go and buy you a new one!"
    show player 13
    show roxxy bikini 15
    rox "We don't have time for that!"
    show player 5
    rox "The competition is starting soon, {b}[firstname]{/b}!"
    show roxxy bikini 13
    rox "... I'm completely screwed."
    show roxxy bikini 14
    show player 10
    player_name "Calm down."
    player_name "I'll find you something!"
    show player 5
    show roxxy bikini 15
    rox "Yeah, right!"
    rox "Where are you going to find one?"
    show roxxy bikini 14
    show player 10
    player_name "Well, this is a beach..."
    show player 14
    player_name "{b}There's gotta be an extra bathing suit here somewhere.{/b}"
    show player 13
    show roxxy bikini 15b
    rox "Go and tell {b}Becca{/b} to bring me hers!"
    show roxxy bikini 15c
    show player 12
    player_name "Huh?"
    player_name "You want to take {b}Becca's{/b} swimsuit?"
    show player 5
    show roxxy bikini 15b
    rox "Yeah, that bitch will give it to me if I tell her too."
    show roxxy bikini 15c
    show player 12
    player_name "... But then, what is she going to wear?"
    show player 5
    show roxxy bikini 15b
    rox "Umm, who cares?"
    rox "It's not like she's gonna win anyways!"
    show roxxy bikini 15c
    show player 10
    player_name "Don't do that, {b}I'll find you one!{/b}"
    show player 5
    show roxxy bikini 15b
    rox "Hmm, fine!"
    rox "I'll give you ten minutes but after that, I'm taking {b}Becca's{/b}..."
    show roxxy bikini 15c
    show player 10
    player_name "I'll be back."
    hide player with dissolve
    show roxxy bikini 15b
    rox "... Don't get me an ugly one either!"
    hide roxxy with dissolve
    return

label beach_cabin_roxxy_get_new_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 5 at left
    show roxxy bikini 15 at right
    with dissolve
    rox "Did you find one?!"
    show roxxy bikini 14
    show player 10
    player_name "Stop worrying, {b}I'll find you a swimsuit!{/b}"
    show player 5
    show roxxy bikini 15b
    rox "Hmph!"
    rox "Well, it had better be a good one, otherwise I'm taking {b}Becca's{/b}..."
    hide roxxy with dissolve
    show player 10
    player_name "Hmm, {b}I should look around here for a bikini that nobody's using{/b}."
    hide player with dissolve
    return

label beach_cabin_roxxy_has_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 14 at right
    show player 14 at left
    with dissolve
    player_name "{b}Roxxy{/b}, I think I've found one!"
    show roxxy bikini 15
    rox "Really?!"
    rox "Lemme see, lemme see!"
    show roxxy bikini 14
    show player 239_240 with dissolve
    pause
    show player 656b with dissolve
    show roxxy bikini 15
    rox "*Gasp*"
    show roxxy bikini 15d
    show player 13
    with dissolve
    rox "It's pretty!"
    show roxxy bikini 15e
    show player 14
    player_name "Yeah, it's umm... Patriotic."
    show player 13
    show roxxy bikini 15d
    rox "Hehehe!"
    show roxxy bikini 9 with dissolve
    show player 433
    pause
    show roxxy bikini usa 5
    show player 296
    with dissolve
    pause
    show roxxy 22 with dissolve
    pause
    show roxxy 23b with dissolve
    rox "What are you doing?"
    show roxxy 23
    pause
    player_name "Hmm?"
    show roxxy 24
    rox "You've already seen me naked, remember?"
    show roxxy 23
    player_name "Yeah, I know... I'm just..."
    show roxxy 23b
    rox "Psh, stop acting so nerdy!"
    show player 433 with dissolve
    show roxxy 22 with dissolve
    pause
    show player 434
    show roxxy bikini usa 6 with dissolve
    pause
    show roxxy bikini usa 14 with dissolve
    show player 435
    player_name "... Wow!"
    show roxxy bikini usa 11 with dissolve
    show player 434
    rox "I know, right!"
    show roxxy bikini usa 6b with dissolve
    rox "Hmm, it's a bit tight..."
    show roxxy bikini usa 6c with dissolve
    pause
    show roxxy bikini usa 6b with dissolve
    rox "It's not too small is it?"
    pause
    show roxxy bikini usa 6c with dissolve
    player_name "..."
    show roxxy bikini usa 6b
    rox "... What do you think?"
    show roxxy bikini usa 9 with dissolve
    player_name "..."
    show roxxy bikini usa 12 with dissolve
    rox "{b}[firstname]{/b}!!!"
    show roxxy bikini usa 13
    show player 435
    player_name "Hmm?"
    show player 434
    show roxxy bikini usa 8 with dissolve
    rox "How does it look?"
    show player 435
    player_name "... Really, REALLY good!"
    player_name "... That's like, my favorite bikini ever!"
    show player 434
    show roxxy bikini usa 10 with dissolve
    rox "Hehehe!"
    rox "You still think I'll win?"
    show roxxy bikini usa 9
    show player 17
    player_name "Without a doubt!"
    show player 13
    show roxxy bikini usa 10
    rox "Good!"
    rox "Now I just need you to oil me up and it's a sure thing!"
    show roxxy bikini usa 9
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Did you say, you want ME to..."
    show player 22
    player_name "{b}*Gulp*{/b}"
    show roxxy bikini usa 12 with dissolve
    rox "Hah, you getting shy on me, {b}[firstname]{/b}?"
    rox "I can have {b}Becca{/b} do it if you don't want to..."
    rox "I just thought, since you found me the replacement bikini and all..."
    show roxxy bikini usa 13
    show player 36 with dissolve
    player_name "N-no! I'll do it!"
    show player 14 with dissolve
    player_name "I'll definitely do it!"
    show player 13
    show roxxy bikini usa 12
    rox "Haha, I thought so!"
    rox "{b}They usually keep some in the life guard's tower.{/b}"
    rox "Why don't you go grab the bottle and I'll wait for you here."
    show roxxy bikini usa 13
    show player 14
    player_name "Totally! I'll be right back!"
    show player 12
    player_name "Don't move!"
    hide player with fastdissolve
    pause
    show roxxy bikini usa 6b with dissolve
    rox "Haha, hurry back, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    return

label beach_tower_roxxy_get_oil:
    scene expression "backgrounds/location_beach_cutscene01.jpg"
    with fade
    show text "I practically flew up the ladder to the life guard's tower!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Roxxy{/b} was actually going to let me oil her body up for the competition!\nI couldn't believe it!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "I'd best locate that bottle quickly so I can get as much time with her as possible!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_beach_tower_day_blur.jpg"
    show player 14 with fastdissolve
    player_name "( Hmm, {b}Roxxy{/b} said there should be a {b}bottle of oil{/b} in here somewhere! )"
    hide player with fastdissolve
    return

label beach_cabin_roxxy_get_oil:
    scene expression "backgrounds/location_beach_water_contest_day_blur.jpg"
    show player 29 with fastdissolve
    player_name "Holy crap! What am I doing?!"
    show player 29f with fastdissolve
    player_name "I've gotta {b}get that bottle of oil{/b} from the {b}life guard's tower{/b} before {b}Roxxy{/b} changes her mind!"
    hide player with fastdissolve
    return

label beach_cabin_roxxy_has_oil:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 9 at right with None
    show player 184b at left
    with fastdissolve
    player_name "{b}*Huff*{/b} I made..."
    player_name "I made it..."
    player_name "{b}*Puff*{/b}"
    show player 658 with dissolve
    player_name "Phew! Here's your oil..."
    show roxxy bikini usa 10
    rox "Sheesh, did you run the entire way or something?!"
    show roxxy bikini usa 9
    show player 184b with dissolve
    player_name "..."
    show roxxy bikini usa 10
    rox "Hahahahaah!"
    show roxxy bikini usa 10
    rox "Well, thanks I guess..."
    show roxxy bikini usa 9
    player_name "..."
    show roxxy bikini usa 10
    rox "Okay, well..."
    rox "Let's start oiling then, shall we?!"
    show roxxy bikini usa 9
    show player 658 with dissolve
    player_name "Y-yeah, okay!"
    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show roxxy massage 2 with dissolve
    rox "Just make sure you get everything, okay!"
    show roxxy massage 3 with dissolve
    rox "Start with my shoulders..."
    show roxxy massage 1 with dissolve
    player_name "Alright!"
    show roxxy massage 4_5 with dissolve
    rox "Mmm..."
    player_name "..."
    pause
    show roxxy massage 1 with dissolve
    player_name "Am I doing it right?"
    show roxxy massage 2
    rox "... What, have you never rubbed a girls shoulders before?"
    show roxxy massage 1
    player_name "Wha- No!"
    player_name "I mean... Of course, I've rubbed plenty of girls shoulders!"
    show roxxy massage 2
    rox "Uh huh..."
    rox "Well, don't ask stupid questions then!"
    show roxxy massage 1
    player_name "..."
    pause
    label roxxy_massage_45:
        show roxxy massage 4_5 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_45")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8_9 with dissolve
    rox "Mmm... That's good."
    rox "Make sure you don't miss any spots!"
    player_name "Yeah, I know."
    player_name "I'll make sure to coat everything!"
    pause
    rox "Ooh, that's really good."
    player_name "..."
    label roxxy_massage_89:
        show roxxy massage 8_9 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_89")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 5 with dissolve
    pause
    show roxxy massage 6_7 with dissolve
    rox "Ahhh... That feels REALLY good, {b}[firstname]{/b}..."
    player_name "... Y-yeah?"
    rox "Mmmhmm, don't stop..."
    player_name "O-okay."
    pause
    label roxxy_massage_67:
        show roxxy massage 6_7 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_67")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8 with dissolve
    pause
    show roxxy massage 9_10 with dissolve
    rox "Ngghh!!"
    rox "..."
    rox "Oh, wow!"
    player_name "..."
    rox "That feels amazing!"
    pause
    show roxxy massage 3 with dissolve
    rox "Ahh, keep going!"
    show roxxy massage 9_10 with dissolve
    rox "Don't stop!"
    rox "Don't-"
    becca "{b}Roxxy{/b} it's time to start heading-"
    scene expression "backgrounds/location_beach_cutscene04.jpg"
    with fade
    show text "Just my luck...\n{b}Missy{/b} and {b}Becca{/b} were at the entrance of the tent..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 1 at right
    rox "!!!" with hpunch
    show becca bikini 18 at Position(xpos=315)
    show missy bikini 12 at left
    with dissolve
    becca "... Holy shit!"
    show becca bikini 1b
    hide roxxy
    show roxxy bikini usa 15 zorder 1 at Position (xpos=650)
    show player 81f zorder 0 at right
    with dissolve
    show missy bikini 14
    pause
    show missy bikini 15 with dissolve
    missy "I fucking knew it!"
    missy "See, {b}Becca{/b}?"
    missy "I told you nerds have huge dicks!"
    show becca bikini 15
    show missy bikini 14
    becca "..."
    show player 78f
    show becca bikini 18
    becca "Sorry, we didn't realize-"
    show becca bikini 15
    becca "..."
    show becca bikini 18
    becca "Seriously though... Holy shit {b}[firstname]{/b}!"
    show becca bikini 15
    show player 82f
    show roxxy bikini usa 18 with dissolve
    rox "We weren't doing anything..."
    show becca bikini 1b
    rox "He was just putting oil on me for the competition!!!"
    show roxxy bikini usa 17
    becca "..."
    show becca bikini 2b
    becca "Well, it certainly didn't look like nothing {b}Roxxy{/b}..."
    show becca bikini 1b
    show missy bikini 13
    missy "For real!"
    missy "Can I go next?"
    show missy bikini 14
    show becca bikini 14
    becca "Shut up, {b}Missy{/b}!"
    show becca bikini 16
    show missy bikini 2
    missy "... What?!"
    show missy bikini 13
    missy "I want some oil too!"
    missy "You'll rub oil on me, won't you {b}[firstname]{/b}?"
    show becca bikini 1b
    show missy bikini 14
    show player 83f
    player_name "... I uhh."
    show player 82f
    show roxxy bikini usa 18
    rox "You guys, seriously!"
    rox "You can't tell anybody about this!"
    show roxxy bikini usa 17
    show becca bikini 2b
    becca "Yeah, {b}Dexter{/b} would kill you both if he heard about this."
    show becca bikini 1b
    player_name "..."
    rox "..."
    show becca bikini 2
    becca "We won't tell anybody."
    show becca bikini 14
    becca "Right, {b}Missy{/b}?!"
    show becca bikini 16
    show missy bikini 2b
    missy "Hmm?!"
    missy "Tell anybody what?"
    show missy bikini 14
    show becca bikini 14
    becca "... Exactly."
    show becca bikini 2
    becca "C'mon, they are calling everyone to the stage."
    show becca bikini 16
    missy "..."
    show becca bikini 14
    becca "Quit staring at his dick and lets go!"
    show becca bikini 16
    show missy bikini 13
    missy "... Aww."
    hide missy with dissolve
    show becca bikini 15
    pause
    show becca bikini 18
    becca "... Holy shit."
    hide becca with dissolve
    pause
    show roxxy bikini usa 19
    rox "..."
    show player 83f
    player_name "... You okay?"
    show player 82f
    show roxxy bikini usa 18f at Position (xpos=550) with dissolve
    rox "Y-yeah."
    rox "Just nervous about the competition is all."
    show roxxy bikini usa 17f
    show player 83f
    player_name "Right."
    player_name "Don't worry, you're gonna do great!"
    show player 82f
    rox "..."
    show player 83f
    player_name "C'mon, we better hurry!"
    hide player with dissolve
    rox "..."
    show roxxy bikini usa 13f
    pause
    hide roxxy with dissolve
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    show tstand 19b zorder 0 at Position (xpos=729)
    Terry "Oh ho ho! You're gonna be the death of me one day, Love..."
    show tstand 20b
    sara "Hehe, well at least you'll die happy!"
    show tstand 19b
    Terry "Amen to that!"
    show player 11 zorder 2 at left with dissolve
    show tstand 19
    Terry "Well then, if it isn't the skipper, once more."
    Terry "How's it going, lad?"
    show tstand 19d
    show player 14
    player_name "It's going awesome, {b}Captain{/b}!"
    player_name "I was just escorting my friend here to the stage."
    show player 13
    show roxxy bikini usa 9f zorder 1 at Position (xpos=400) with dissolve
    pause
    show tstand 19
    Terry "Phew, what a beauty!"
    show tstand 19d
    show roxxy bikini usa 10f
    rox "... T-thanks!"
    show roxxy bikini usa 9f
    show tstand 20c with dissolve
    sara "{b}*Gasp*{/b}"
    sara "Is that my bikini?"
    show tstand 19d
    show roxxy bikini usa 16f
    with dissolve
    rox "!!!"
    show player 21
    player_name "Y-yeah."
    show roxxy bikini usa 17f
    player_name "{b}Roxxy's{/b} top broke at the last second and it was the only replacement I could find."
    player_name "I hope that's okay, {b}Miss Sara{/b}?"
    player_name "... I would have asked but..."
    show player 11
    show tstand 20
    sara "Hehehe, say no more."
    sara "It's no problem at all, dear."
    show roxxy bikini usa 13f
    show player 13
    sara "I just wish it was a little bigger is all..."
    show tstand 19d
    show roxxy bikini usa 11f with dissolve
    rox "Does it look bad?"
    show roxxy bikini usa 9f
    show tstand 19
    Terry "Not at all!"
    Terry "It's a bit tight but there's nothing wrong with that..."
    Terry "In fact it's making me want to salute all the more!"
    Terry "Oh ho ho!"
    show tstand 20
    sara "Haha, {b}Terry{/b} you're terrible!"
    sara "You look gorgeous, sweetie!"
    sara "Go ahead and keep it!"
    show tstand 20d at right with dissolve
    sara "But first you gotta get up there and win this thing!"
    hide tstand
    show tstand 19d at Position (xpos=729)
    with dissolve
    show roxxy bikini usa 10f
    rox "Right!"
    show roxxy bikini usa 10 zorder 1 at Position (xpos=450) with dissolve
    rox "Wish me luck, {b}[firstname]{/b}!"
    show roxxy bikini usa 9
    show player 14
    player_name "Heh, you don't need it but good luck!"
    show roxxy bikini usa 10
    rox "Aww, thanks {b}[firstname]{/b}!"
    hide player
    show roxxy bikini usa 7 at left
    with dissolve
    pause
    hide roxxy
    show player 13 at left
    with dissolve
    show tstand 19
    Terry "I'll take it things are progressing well with that one?"
    show tstand 19d
    show player 10
    player_name "Huh?"
    show player 5
    show tstand 19c
    Terry "Oh ho ho!"
    Terry "Nevermind Skipper."
    show tstand 19
    Terry "Why don't you take my {b}Sara{/b} here and go find a couple of seats?"
    Terry "I've got a show to host!"
    show player 13
    show tstand 20b
    sara "Go get em, love."
    show tstand 20e with dissolve
    pause
    show tstand 20 with dissolve
    sara "C'mon, {b}[firstname]{/b}! Let's go find some seats!"
    hide tstand with dissolve
    show player 14
    player_name "Yes, ma'am."
    hide player with dissolve
    scene expression "backgrounds/location_beach_cutscene05.jpg"
    with fade
    show text "The competition was so much fun to watch!\nAll those beautiful women in skimpy bikinis...\n... And {b}Miss Sara{/b} sitting beside me the entire event.\nIt was such a good day!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Roxxy{/b} and her friends all made it to the finals too!\n... But there was never a doubt as to who was going to win." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "None of those other girls could compare to {b}Roxxy{/b}!!!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    show player 13 at Position (xpos=500)
    show missy bikini 13 at left
    show becca bikini 17 at Position (xpos=315)
    show roxxy bikini usa 4 at right
    with dissolve
    rox "Woooo!!!"
    missy "Hehehe!"
    show roxxy bikini usa 2
    becca "Way to go, girl!"
    show missy bikini 1
    show becca bikini 1
    show player 14
    player_name "Congratulations, {b}Roxxy{/b}!"
    show player 14f at Position (xpos=550) with dissolve
    player_name "To all of you, really!"
    show player 13f
    show missy bikini 2
    missy "I made it to the finals!"
    show missy bikini 13
    missy "Did you see me, {b}[firstname]{/b}?!"
    show missy bikini 1
    show becca bikini 14
    becca "... Of course he saw you, dummy..."
    becca "He was in the crowd watching the entire time."
    show becca bikini 16
    show missy bikini 2b
    missy "Oh, were you checking to see if he was watching?!"
    show missy bikini 1b
    show becca bikini 14
    becca "What?!"
    becca "N-no!"
    becca "Shut up!"
    show becca bikini 1
    show roxxy bikini usa 4
    rox "Hahaha!"
    show roxxy bikini usa 3
    rox "You guys never stop!"
    show player 13 at Position (xpos=500) with dissolve
    show roxxy bikini usa 4
    rox "I can't believe I won!"
    show player 18
    rox "{b}[firstname]{/b}, I won!!!"
    show roxxy bikini usa 2
    show player 14
    player_name "I know! You were really awesome!"
    show player 13
    show roxxy bikini usa 4
    rox "Hehehe!"
    show roxxy bikini usa 3
    rox "Thank you so much for all your help today!"
    show roxxy bikini usa 2
    show becca bikini 2b
    becca "Heh, yeah... He was a \"big help\" wasn't he, {b}Roxxy{/b}?!"
    show becca bikini 1b
    rox "..."
    show missy bikini 8
    missy "... Huh?"
    show missy bikini 2
    missy "Oh, wait! I get it!"
    show missy bikini 13
    show becca bikini 16
    missy "You're talking about his huge dick, right?!"
    show becca bikini 17
    show roxxy bikini usa 4
    show player 37 at Position (xoffset=41) with dissolve
    becca "Hahaha!"
    missy "Hahaha!"
    rox "... Hahaha!"
    show becca bikini 1
    show missy bikini 1
    show roxxy bikini usa 3
    rox "Just ignore them, {b}[firstname]{/b}."
    rox "Seriously, thank you for today!"
    show roxxy bikini usa 2
    show player 14 with dissolve
    player_name "My pleasure."
    player_name "You need help carrying it home?"
    show player 13
    show roxxy bikini usa 3
    rox "Nah, I'll make these two bitches carry it."
    show roxxy bikini usa 2
    becca "..."
    show missy bikini 2
    missy "Oh, I'll carry it!"
    show missy bikini 1
    show roxxy bikini usa 3
    rox "I'll see you at school?"
    show roxxy bikini usa 2
    show player 14
    player_name "Sure. I'll see you all tomorrow."
    show player 13
    show becca bikini 2b
    becca "See ya, {b}[firstname]{/b}."
    show becca bikini 1b
    show missy bikini 13
    missy "Byeee, {b}[firstname]{/b}!!!"
    hide becca
    hide missy
    hide roxxy
    hide player
    with dissolve
    return

label beach_cabin_roxxy_massage:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 2 at right
    show player 13 at left
    with dissolve
    rox "Sorry, it took me forever to slip away from them!"
    show roxxy bikini 1
    show player 14
    player_name "No problem."
    player_name "You ready for a massage?"
    show player 13
    show roxxy bikini 2
    rox "Hell yeah!"
    rox "You give the best massages!"
    show roxxy bikini 1
    show player 12
    player_name "Hey, isn't that {b}Miss Sara's{/b} bikini?"
    show player 13
    show roxxy bikini 2
    rox "Yeah, she told me to keep it remember?"
    rox "I thought you might want me to wear it for our massage sessions?"
    show roxxy bikini 1
    show player 14
    player_name "Y-yeah, definitely!"
    show player 13
    show roxxy bikini 2
    rox "Hehehe!"
    show roxxy bikini 5 with dissolve
    pause
    show roxxy bikini 6 with dissolve
    show player 434
    pause
    show roxxy bikini 7 with dissolve
    pause
    show roxxy bikini 8 with dissolve
    pause
    show roxxy bikini 9 with dissolve
    pause
    show roxxy bikini usa 5 with dissolve
    pause
    show roxxy 22 with dissolve
    pause
    show roxxy bikini usa 6 with dissolve
    pause
    show roxxy bikini usa 14 with dissolve
    pause
    show roxxy bikini usa 12 with dissolve
    rox "Well don't just stand there gawking at my tits, start rubbing!"
    hide roxxy
    hide player
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 4_5 with dissolve
    rox "Mmm..."
    player_name "..."
    pause
    show roxxy massage 1 with dissolve
    player_name "Does that feel good?"
    show roxxy massage 2
    rox "... Oh, yeah."
    rox "Rub a little harder."
    show roxxy massage 1
    player_name "You got it!"
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 4_5 with dissolve
    pause
    rox "Phew, that's good!"
    player_name "..."
    pause
    label roxxy_massage_45_repeat:
        show roxxy massage 4_5 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_45_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8_9 with dissolve
    rox "Mmm... That's so good."
    rox "Make sure you don't miss any spots!"
    player_name "Yeah, I know."
    player_name "I'll make sure to get everything!"
    pause
    rox "Ooh, that's it!"
    player_name "..."
    label roxxy_massage_89_repeat:
        show roxxy massage 8_9 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_89_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 5 with dissolve
    pause
    show roxxy massage 6_7 with dissolve
    pause
    rox "Ahhh... That feels REALLY good, {b}[firstname]{/b}..."
    player_name "... Y-yeah?"
    rox "Mmmhmm, don't stop..."
    player_name "O-okay."
    pause
    label roxxy_massage_67_repeat:
        show roxxy massage 6_7 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_67_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8 with dissolve
    pause
    show roxxy massage 9_10 with dissolve
    rox "Ngghh!!"
    rox "..."
    rox "Oh, wow!"
    player_name "..."
    rox "That feels amazing!"
    pause
    show roxxy massage 3 with dissolve
    rox "Ahh, keep going!"
    show roxxy massage 9_10 with dissolve
    rox "Don't stop!"
    rox "Don't-"
    missy "{b}Roxxy{/b}, are you guys in here?"
    scene expression "backgrounds/location_beach_cutscene04.jpg"
    with fade
    show text "Once again, {b}Missy{/b} and {b}Becca{/b} were at the entrance of the tent..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 1 at right
    show becca bikini 1b at Position(xpos=315)
    show missy bikini 1b at left
    with dissolve
    rox "!!!" with hpunch
    hide roxxy
    show roxxy bikini usa 15b zorder 1 at Position (xpos=650)
    show player 82f zorder 0 at right
    with dissolve
    rox "God damnit, you two!"
    rox "Are you spying on us again?!"
    show roxxy bikini usa 15
    show missy bikini 13
    missy "Yes."
    show missy bikini 1b
    show becca bikini 14
    becca "Huh?! No!"
    show roxxy bikini usa 17 with dissolve
    becca "Shut up, {b}Missy{/b}!"
    show becca bikini 16
    show missy bikini 8
    missy "What?"
    show missy bikini 15 with dissolve
    missy "We want a massage too..."
    show missy bikini 14 with dissolve
    show becca bikini 18
    becca "Oh. My. God."
    show becca bikini 1
    show roxxy bikini usa 15b with dissolve
    rox "{b}*Sigh*{/b}"
    show roxxy bikini usa 18 with dissolve
    rox "We were just finishing anyways..."
    show roxxy bikini usa 17
    show missy bikini 13
    missy "Cool, I'll go next!"
    show missy bikini 14
    show roxxy bikini usa 18
    rox "Yeah, I don't think so!"
    rox "Get your dumb asses back out to the water!"
    show roxxy bikini usa 17
    show missy bikini 10
    missy "Aww..."
    hide becca
    hide missy
    with dissolve
    show roxxy bikini usa 18f at Position (xpos=550) with dissolve
    rox "Sorry about them, {b}[firstname]{/b}..."
    show roxxy bikini usa 17f
    show player 83bf
    player_name "Heh, it's okay."
    player_name "It's actually really cute."
    show player 83cf
    show roxxy bikini usa 12f
    rox "Heh, yeah I know..."
    rox "... But I can't give them everything they want."
    rox "Buncha greedy bitches, those two!"
    show roxxy bikini usa 13f
    show player 83bf
    player_name "Hahaha!"
    show player 83cf
    show roxxy bikini usa 10f with dissolve
    rox "Well, thanks for the massage."
    show roxxy bikini usa 9f
    show player 83bf
    player_name "My pleasure."
    show player 83cf
    show roxxy bikini usa 11f
    rox "Who knows? Maybe next time we'll get to finish..."
    show roxxy bikini usa 9f
    show player 82f
    player_name "{b}*Gulp*{/b}"
    show roxxy bikini usa 10f
    rox "Hehehe."
    hide roxxy with dissolve
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_sex_intro:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 14f at right
    show missy bikini 1 zorder 2 at left
    with dissolve
    player_name "Hey, {b}Missy{/b}."
    show player 13f
    show missy bikini 16 with dissolve
    missy "{b}*Gasp*{/b}!"
    show missy bikini 13 with dissolve
    missy "He's here!"
    missy "{b}Roxxy{/b}, {b}Becca{/b}!! He's here, he's here, HE's HERE!!!"
    show missy bikini 1 with None
    show becca bikini 2 zorder 1 at Position (xpos=315)
    show roxxy bikini 1f zorder 0 at Position (xpos=500)
    with dissolve
    becca "Hi, {b}[firstname]{/b}."
    show becca bikini 1
    show player 14f
    player_name "Hey, {b}Becca{/b}."
    show player 13f
    show missy bikini 2
    missy "He's finally here!!"
    show missy bikini 1
    show roxxy bikini 19bf
    rox "Oh my god, shut up."
    rox "We heard you the first time."
    show roxxy bikini 1f
    show missy bikini 10
    missy "Tsk, you shut up!"
    show missy bikini 13
    show roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "I'm excited..."
    show missy bikini 1
    show becca bikini 19
    becca "..."
    show roxxy bikini 19
    rox "Do you want me to call the whole thing off?!"
    show roxxy bikini 20
    show becca bikini 6
    show missy bikini 8
    becca "What?!"
    missy "No, please!"
    show becca bikini 6b
    missy "I'm sorry! Look, I'm shutting up right now!"
    show missy bikini 16 with dissolve
    show roxxy bikini 2
    rox "Yeah, we'll see how long that lasts..."
    show roxxy bikini 1
    show player 17f
    player_name "Hahaha, you girls are too funny!"
    show player 14f
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "So, what's up?"
    player_name "{b}Roxxy{/b} said something about a surprise?"
    show player 13f
    show roxxy bikini 2f
    rox "Yeah, I've got-"
    show missy bikini 13 with dissolve
    missy "A great surprise!"
    show roxxy bikini 24f
    show becca bikini 13
    with dissolve
    pause
    show roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "You're going to love-"
    hide becca
    show missy bikini 18
    with dissolve
    becca "{b}Missy{/b} shut up!"
    show missy bikini 18b
    show roxxy bikini 19
    rox "Seriously?!"
    rox "You can't even be quiet for five seconds?!"
    show roxxy bikini 20
    show missy bikini 19
    becca "Don't worry, she's done."
    show missy bikini 19b
    show roxxy bikini 19b
    rox "{b}*Sigh*{/b}"
    show roxxy bikini 2f at Position (xpos=500) with dissolve
    rox "We're gonna play spin the bottle."
    show roxxy bikini 1f
    show player 14f
    player_name "Heh, spin the bottle again?"
    show player 13f
    show roxxy bikini 22f with dissolve
    rox "Yes, but with a slight rule change."
    show roxxy bikini 21f
    show player 12f
    player_name "Rule change?"
    show player 13f
    rox "Mmmhmm..."
    show roxxy bikini 22f
    rox "You see, at a certain point... I'm gonna call {b}final spin{/b}."
    rox "Then you will spin one final time."
    rox "... And whomever the bottle lands on, will join us in the changing room for a special reward."
    show roxxy bikini 21f
    show player 14f
    player_name "Oh?"
    player_name "What kind of special reward?"
    show player 13f
    show missy bikini 17 with dissolve
    missy "Mrffllmmmrf!"
    show roxxy bikini 19bf with dissolve
    rox "..."
    show missy bikini 18b with dissolve
    rox "She really can't keep her mouth shut!"
    show missy bikini 19b
    show roxxy bikini 2f
    rox "Anyways, it's a surprise."
    rox "You'll have to play to find out."
    show roxxy bikini 1f
    show player 14f
    player_name "Heh, alright."
    player_name "Let's do it!"
    show player 13f
    show missy bikini 17 with dissolve
    missy "Mrrfff!!"
    show player 14f
    player_name "Heh, she's so excited..."
    show player 13f
    show missy bikini 18b with dissolve
    show roxxy bikini 19f
    rox "{b}*Sigh*{/b}..."
    show roxxy bikini 1f
    show missy bikini 19
    becca "You have no idea..."
    hide roxxy
    hide missy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
