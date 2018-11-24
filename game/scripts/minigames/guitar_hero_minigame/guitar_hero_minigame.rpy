label guitar_hero_minigame_karaoke_fail:
    scene erik_basement
    show erik 3f at Position (xpos=400)
    show player 5 at left
    show eve 23 at right with dissolve
    eve "Boo! You guys suck!"
    show eve 22
    show player 10
    player_name "I didn't know the words to that song!"
    show player 12
    player_name "{b}Erik{/b}, pick another!"
    show player 5
    show erik 3bf
    eri "Alright..."
    show erik 3f
    show player 14
    player_name "Here we go!"
    hide player
    hide erik
    with dissolve
    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        menu:
            "Play Minigame":
                call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
            "Skip Minigame (Cheat)":
                jump guitar_hero_minigame_karaoke_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

label guitar_hero_minigame_karaoke_pass:
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["01_unlocked"] = True
    scene erik_basement
    show erik 1f at Position (xpos=400)
    show player 13 at left
    show eve 19 at right
    with dissolve
    eve "I'll show you amateurs how it's done!"
    eve "Out of my way, boys!"
    show eve 15 with dissolve
    show erik 5f
    show player 11
    pause
    hide eve with dissolve

    scene erik_basement_cs2
    with fade
    show text "I guess the booze did it's job because {b}Eve{/b} rocked that mic with some serious confidence!\nShe was amazing! I was completely blown away by how beautiful her voice was!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Perhaps I should have stopped her at three glasses though...\n... As it ended up being quite the show!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene erik_basement
    show erik 57f at Position (xpos=400)
    show player 83c at left
    show eve 17c at right
    with dissolve
    eve "WHOOOOO!!!"
    show eve 16 with dissolve
    show player 83b
    player_name "Damn girl, you rock!"
    show player 83c
    show eve 17
    eve "Thanks! I guess- *hic* I guess it isn't that bad singing in front of others."
    show eve 16
    show player 83b
    player_name "Does that mean you'll sing in the talent show?!"
    show player 83c
    eve "..."
    show eve 17
    eve "Sure, why not!"
    show eve 16
    show player 83b
    player_name "You're awesome!"
    player_name "Maybe keep your clothes on for the talent show though."
    show player 83c
    show eve 17b with dissolve
    eve "Hmm?"
    show eve 17d with dissolve
    eve "Oh! Pfft!"
    show eve 17c with dissolve
    eve "Hahahahaha!"
    show eve 17 with dissolve
    eve "Whoopsie. Guess I- *hic* Guess I got carried away..."
    show eve 15 with dissolve
    show erik 58f
    eri "Heh, it's okay. We didn't mind."
    show erik 57f
    show eve 2b
    eve "Oh right, *hic* {b}Erik's{/b} here..."
    show eve 4 with dissolve
    eve "I completely forgot, hehehe."
    show eve 3
    eri "..."
    show player 79 with dissolve
    player_name "I should probably help you get home."
    show player 83c
    show eve 2
    with dissolve
    eve "Aww, such a- *hic* such a gentleman!"
    eve "I'll just text my sis- *hic* She'll pick me up."
    show eve 5
    show erik 58f
    eri "I'll see you guys later."
    show erik 57f
    show player 83b
    player_name "Thanks for the party {b}Erik{/b}."
    show player 83c
    show eve 15 with dissolve
    eve "Yeah, party! Whooooo!"
    show eve 5 with dissolve
    show player 83b
    player_name "Heh, c'mon drunkie. Let's go home!"
    show player 83c
    show eve 2
    eve "I was really good wasn't- *hic* wasn't I, {b}[firstname]{/b}?"
    show eve 5
    show player 83b
    player_name "You sure were."
    show player 83c
    show eve 4 with dissolve
    eve "Hehehe."
    hide eve
    hide player
    hide erik
    with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    if M_dewitt.is_set("talent ask kevin"):
        $ M_dewitt.trigger(T_dewitt_find_last_talent)
    else:
        $ M_dewitt.trigger(T_dewitt_karaoke_jam)
    $ game.main()

label guitar_hero_minigame_talent_show_fail:
    scene assembly_hall_cs03
    with fade
    show text "It was not a good start and the crowd was growing restless...\n{b}Eve{/b} and {b}Kevin{/b} looked worried but I knew we could still save it!\nI gave them both a reassuring nod and started it over from the top.\nWe'll win them over this time for sure!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve
    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        menu:
            "Play Minigame":
                call screen guitar_hero(0, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")
            "Skip Minigame (Cheat)":
                jump guitar_hero_minigame_talent_show_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")

label guitar_hero_minigame_talent_show_pass:
    if M_dewitt.get("failcount") == 0:
        $ A_smooth_mcgroove.unlock()
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Dewitt"]["gallery"]["02_unlocked"] = True
    scene assembly_hall_cs02
    with fade
    show text "The crowd was transfixed as we played our hearts out!\n{b}Kevin{/b} shredded on his guitar and {b}Eve's{/b} angelic voice lulled them into submission!\n... I finished it all off with a whimsical flute solo that left the crowd reeling!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_paint02_c
    show kevin 17f at Position (xpos=600)
    show player 554 at left
    show eve 12 at right
    with dissolve
    eve "Awesome job guys!"
    show eve 11
    show player 555
    player_name "Yeah, that was really amazing!"
    show player 554
    show kevin 18f
    kev "Where the heck is {b}Miss Dewitt{/b}?!"
    show kevin 17f
    show player 553
    player_name "... Huh?"
    show player 552
    show kevin 18f
    kev "Bro, she's gone!"
    show kevin 17f
    show eve 12
    eve "He's right! She was right here a second ago..."
    show eve 11
    show player 553
    player_name "She's supposed to close out the show with a speech."
    show player 552
    player_name "..."
    show kevin 18f
    kev "Well somebody has to go up and say something!"
    show kevin 17f
    show eve 12
    eve "{b}[firstname]{/b} should do it!"
    show eve 11
    show player 553
    player_name "... Why do I always have to do everything?!"
    show player 552
    show kevin 18f
    kev "You got this, Bro!"
    show kevin 17f
    show player 553
    player_name "{b}*Sigh*{/b} Fine."
    show player 551c with dissolve
    player_name "( Think I'll put my hair back down. )"
    show player 551b at Position (xoffset=6) with dissolve
    show eve 12
    eve "Aww... I liked your hair like that though!"
    show eve 11
    show player 551d with dissolve
    pause
    show player 14 at Position (xoffset=52) with dissolve
    player_name "Sorry! Maybe you can fix my hair another time."
    show player 13 at Position (xoffset=52)
    show eve 12
    eve "Alright! Now get out there!"
    hide player
    hide kevin
    hide eve
    with dissolve

    scene assembly_hall_cs04
    with fade
    show text "The crowd was waiting with bated breath as I made my way to the podium.\nI had no idea what to say to these people!\nWhere the heck had {b}Miss Dewitt{/b} gotten off to?" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_podium_c
    show player podium 3 at Position (xoffset=-120)
    show xtra 44
    with dissolve
    player_name "H-hey, so uh..."
    player_name "That was really something, huh?"
    show player podium 4 at Position (xoffset=-120)
    player_name "We just want to say we appreci-"
    show player podium 2 zorder 1 with dissolve
    player_name "!!!"
    player_name "What the-"

    scene under_podium
    show dewitt under 1
    with dissolve
    dewitt "Well hello there, sugar."
    show dewitt under 2
    player_name "What are you doi-"
    show dewitt under 3 with dissolve
    dewitt "Shhhh...."
    show dewitt under 1 with dissolve
    dewitt "I know what you did."
    dewitt "How you risked expulsion to make sure this {b}Talent Show{/b} went off without a hitch."
    show dewitt under 2
    player_name "It's no big deal, Ma'am."
    player_name "You should really come up here and close out the show!"
    show dewitt under 1
    dewitt "Nu uh! Not until I've had a chance to properly thank you, sugar!"
    show dewitt under 4 with dissolve
    player_name "What are you-"
    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 1 at left
    with dissolve
    player_name "!!!"
    show dewitt bj 2
    pause
    show dewitt bj 3
    dewitt "Keep talking, {b}[firstname]{/b}!"
    dewitt "Your adoring crowd is waiting!"

    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "{b}*Ahem*{/b} Sorry... Where was I?"
    player_name "..."
    player_name "Oh, right!"

    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 4
    with dissolve
    player_name "We just wanted to say that we appre-"
    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    player_name "Holy shit!"
    show screen dewitt_bj_options
    player_name "... Oh, Wow!"
    player_name "W-we really appreciate..."
    player_name "... You all coming out to..."
    player_name "Oh man!!"
    player_name "... coming out to support us!"
    player_name "Let's hear it one more time for-"
    player_name "Mmmm!"
    player_name "{b}Kevin{/b} on guitar!"

    player_name "{b}Eve{/b} on vocals!"
    player_name "... And I'm-"
    player_name "Oh, jesus!"
    player_name "Haaaah!"
    player_name "I'm {b}[firstname]{/b}!"
    dewitt "Mmm."
    player_name "..."
    player_name "Also a special thanks to-"
    player_name "Fuuuuuu..."
    player_name "... MC Tyrone!"
    player_name "... And of course, {b}Miss Dewitt{/b}!"
    player_name "Who-"
    player_name "Haaah!"
    player_name "Oh, god!"
    player_name "{b}Miss Dewitt{/b}, who never fails..."
    player_name "... To suck every..."
    player_name "... Last... Drop..."
    dewitt "{b}*Slurp*{/b}"
    player_name "... Of talent..."
    player_name "... Out of her students!"
    player_name "I'm gonna..."
    player_name "I'M GONNA!!!"
    hide screen dewitt_bj_options

    scene assembly_hall_podium_c
    show player podium 1
    show xtra 44
    with dissolve
    player_name "HNNGGG!!!"
    player_name "Ooohhh, take it all!"
    player_name "Yeeaaaahhh..."

    $ M_dewitt.set("sex speed", 0.075)
    scene dewitt_podium_bj
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    pause
    pause
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    pause
    show dewitt bj 6
    pause
    show dewitt bj 7
    pause
    dewitt "Mmm, delicious!"
    dewitt "Thanks again, sugar!"
    dewitt "Muah!"

    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "{b}*Phew*{/b}"
    show player podium 3 zorder 0 at Position (xoffset=-120) with dissolve
    player_name "Sorry, I meant to say."
    player_name "I'm gonna call it all to the close now."
    show player podium 4 at Position (xoffset=-120)
    player_name "Thanks again for coming out!"
    player_name "... And be sure to sign up for next year's show!"
    player_name "We love you Summerville!"
    player_name "Goodnight!"
    show player podium 5 at Position (xoffset=-56) with dissolve
    pause


    scene assembly_hall_cs07
    with fade
    show text "As I finished my speech. I spotted a very pecular pair entering the Auditorium.\nIt seems {b}Principal Smith{/b} and {b}Annie{/b} had managed to get themselves free after all.\nJudging by the state of them, it hadn't been easy!\nThey didn't stay long... Turning to leave the instant they realized they'd been beaten." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene assembly_hall_paint02_c
    show kevin 17f at Position (xpos=600)
    show player 13 at left
    show eve 12 at Position (xpos=450)
    with dissolve
    eve "Hahahaha!! Did you see that cushion stuck to {b}Annie{/b}?!"
    eve "That might be the funniest thing I've ever seen in my life!"
    show eve 11
    show kevin 18f
    kev "Yeah, and {b}Principal Smith's clothes{/b} were in tatters!"
    kev "They really wanted to stop this show, huh?"
    show kevin 17f
    show player 14
    player_name "Heh, yeah. I can't believe they managed to get loose on their own!"
    show player 13
    show dewitt 9bf at right
    show dewitt 9bf at Position (xoffset=-73)
    with dissolve
    $ renpy.end_replay()
    dewitt "Oh my goodness, you guys were so great!"
    show eve 11f
    show kevin 17 at Position (xpos=700)
    with dissolve
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "I've never been more proud!"
    show dewitt 1bf at Position (xoffset=-73)
    show eve 12f
    eve "Thanks, Ma'am!"
    show eve 11f
    show kevin 18
    kev "... Where did you get off to?"
    show kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "Oh, I was just tending to a little something."
    show dewitt 1bf at Position (xoffset=-73)
    show kevin 18
    kev "A little something?"
    show kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "... Hmm, well. A big something actually!"
    show dewitt 1bf at Position (xoffset=-73)
    player_name "..."
    show dewitt 19f with dissolve
    dewitt "Great speech by the way, {b}[firstname]{/b}."
    dewitt "You have quite a talent..."
    dewitt "... For public speaking."
    show dewitt 18f
    show eve 12f
    eve "Hey, you guys wanna celebrate?! ... Grab a bite to eat or something?"
    show eve 11f
    show kevin 18
    kev "I'm down!"
    show kevin 17
    show dewitt 19f
    dewitt "Oh, no thanks, sweetie. I'm afraid I'm full..."
    show dewitt 18f
    show eve 12 with dissolve
    eve "{b}[firstname]{/b}?"
    show eve 11
    show player 14
    player_name "I'm going to have to pass too. I'm pretty tired."
    show player 13
    show eve 12
    eve "Awww! Come on!"
    show eve 11
    show dewitt 19f
    dewitt "Actually would you mind giving {b}[firstname]{/b} and I a moment alone real quick?"
    show dewitt 18f
    show eve 11f with dissolve
    show kevin 18
    kev "Hey, if you change your mind, shoot us a text."
    show kevin 17
    show player 14
    player_name "Alright. Later!"
    show player 13
    hide kevin
    hide eve
    with dissolve
    show dewitt 9bf at Position (xoffset=-73) with dissolve
    dewitt "I just wanted to thank you one more time for everything, {b}[firstname]{/b}."
    show dewitt 9df at Position (xoffset=-73)
    dewitt "This {b}Talent Show{/b} never would have happened without your help."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "It was my pleasure, {b}Miss Dewitt{/b}."
    show player 13
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "I've decided to give you an A+ in my class."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "Really?!"
    show player 13
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "That's right, sugar."
    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "Oh, thank you!"
    show player 13
    show dewitt 19f with dissolve
    dewitt "... And I have one more surprise for you."
    show dewitt 18f
    show player 10
    player_name "Hmm?"
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "You'll have to come to my office {b}tomorrow{/b} after school if you want it..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-okay..."
    player_name "I'll be there."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Mmm, I can't wait!"
    dewitt "See you then, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    hide player with dissolve
    $ renpy.end_replay()

    $ game.timer.tick()
    $ M_dewitt.trigger(T_dewitt_talent_show_success)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
