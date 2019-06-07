label basketball_court_dexter_start:
    scene basketball_b
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "What are you doing here?"
    show dexter 1
    show player 12
    player_name "Why do you care? Maybe I'm just here to practice."
    show player 11
    show dexter 3
    dex "Hah!"
    dex "That's a good one!"
    show dexter 1
    show player 25
    player_name "{b}*Sigh*{/b}"
    show player 12
    player_name "What do you want, {b}Dexter{/b}?"
    show player 5
    show dexter 6 with dissolve
    dex "Just stay away from my court, understood?"
    hide dexter with dissolve
    show player 24
    player_name "..."
    hide player with dissolve
    return

label basketball_court_roxxy_dexter_argument:
    scene basketball_b
    show roxxy 3f at left
    show dexter 2 at right
    with dissolve
    rox "How can you be so stupid?!"
    show roxxy 3bf
    show dexter 6 with dissolve
    dex "Don't call me stupid!"
    show dexter 2
    show roxxy 3f
    rox "You had one job to do."
    rox "I said, \"Get me his homework.\""
    rox "Isn't that what I said?"
    show roxxy 3df
    show dexter 8
    dex "Yeah, but..."
    show dexter 2
    show roxxy 3f
    rox "Shut up, stupid! I'm talking!"
    rox "So you find him."
    rox "You beat the crap out of him."
    rox "... And then you leave without getting the homework!"
    show roxxy 3df
    show dexter 4 with dissolve
    dex "Well, I punched him and his glasses broke."
    show dexter 3 with dissolve
    dex "It was funny..."
    dex "So I was laughing and he was crying and I guess... I just sorta forgot."
    show dexter 1
    show roxxy 3f
    rox "Well, what am I supposed to do?!"
    rox "I don't have anything to turn for the {b}French Bitch's class{/b}!"
    show roxxy 3bf
    show dexter 3
    dex "That's not my problem!"
    dex "Why don't you steal the homework yourself?!"
    show dexter 1
    show roxxy 30f
    rox "Grr, I told you, I can't do it myself!"
    rox "You never listen!"
    show roxxy 3f
    show dexter 2
    rox "You're so STUPID!"
    show roxxy 3bf
    show dexter 8
    dex "Stop calling me stupid, {b}Roxxy{/b}!"
    show dexter 2
    show roxxy 31f
    rox "... YOU'RE STUPID!"
    show roxxy 3bf
    show dexter 4
    dex "THAT'S IT!!!" with hpunch
    dex "I'm done with this!"
    show dexter 6 with dissolve
    dex "It's always, \"{b}Dexter{/b} do this.\" or \"{b}Dexter{/b} do that.\""
    dex "... And what do I get?"
    dex "Called stupid."
    dex "Well, screw you {b}Roxxy{/b}!"
    dex "No more favors!"
    dex "No more car rides!"
    dex "No more beer!"
    show dexter 8 with dissolve
    dex "... And no more favors!"
    show dexter 2
    show roxxy 3cf
    rox "You said that one already..."
    show roxxy 3f
    rox "... Stupid."
    show roxxy 3bf
    show dexter 6 with dissolve
    dex "Rrraahhh, FUCK YOU!"
    dex "I'm leaving!"
    hide dexter with dissolve
    show roxxy 3f
    rox "... Yeah, well see if I care!"
    hide roxxy with dissolve
    pause 1
    show player 13 at left
    show eve 6 at right
    with dissolve

    eve "Wow!"
    eve "That was a good show!"
    show eve 5
    show player 10
    player_name "Heh, yeah."
    show player 5
    player_name "..."
    show eve 2b
    eve "What's the matter?"
    show eve 1
    show player 10
    player_name "I can't believe I'm about to say this but..."
    player_name "I kinda feel sorry for {b}Dexter{/b}."
    show player 5
    show eve 2b
    eve "Eww..."
    eve "Don't say that."
    eve "He's an asshole!"
    show eve 1
    show player 10
    player_name "Yeah, I know."
    show player 5
    show eve 2
    eve "Did you miss the part where he broke some poor kids glasses for no reason other than he thought it was funny?"
    show eve 1
    show player 14
    player_name "... You're right."
    player_name "He deserves a bit of misery, doesn't he?"
    show player 13
    show eve 2
    eve "Yeah he does."
    eve "C'mon, we should get to class."
    hide player
    hide eve
    with dissolve
    return

label basketball_court_bissette_get_books:
    scene basketball_b
    show dexter 2 at right
    show player 10 at left
    with dissolve
    player_name "Hey, umm, {b}Dexter{/b}..."
    show player 5
    show dexter 3
    dex "What do you want Twerp?"
    show dexter 1
    show player 10
    player_name "I was hoping you still had the library book you checked out..."
    show player 5
    show dexter 8
    dex "Library book?"
    show dexter 6 with dissolve
    show player 11
    dex "Do I look like the kinda guy who would be reading library books?"
    dex "...What do you think I'm some kinda nerd like you and your douchebag ginger friend?"
    show dexter 2 with dissolve
    show player 10
    player_name "What? No, I didn't..."
    show player 11
    show dexter 4 with dissolve
    dex "You better get outta here, {b}[firstname]{/b}, before I feed you a knuckle sandwich!"
    show dexter 2 with dissolve
    show player 12
    player_name "Alright, alright, I'm going!"
    hide dexter with dissolve
    show player 10f at center with dissolve
    player_name "I wonder if the librarian made a mistake?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "He could be lying. {b}I should check his locker{/b}!"
    player_name "Hopefully it's in there, otherwise I dunno what I'm gonna do..."
    hide player with dissolve
    return

label basket_ball_court_take_magazines:
    if player.location.is_here(M_dexter):
        if not M_ross.get("take porno fail"):
            call expression game.dialog_select("basketball_court_ross_magazines_intro")
        else:

            call expression game.dialog_select("basketball_court_ross_magazines_retry")

        if player.has_required_dex(3):
            call expression game.dialog_select("basketball_court_ross_magazines_dex_pass")
            call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
            $ M_ross.set("magazine dexter", True)
        else:

            call expression game.dialog_select("basketball_court_ross_magazines_dex_fail")
            $ M_ross.set("take porno fail", True)
    $ game.main()

label basketball_court_ross_magazines_intro:
    scene basketball_b
    show player 579
    with dissolve

    player_name "Looks like somebody left a few magazines sitting here..."
    show player 579c
    player_name "( Whoa!!! )"
    player_name "( These are naughty magazines!) "
    becca "What are you doin-"
    hide player
    show player 578 at left
    show becca 2bf zorder 1 at right
    with dissolve
    becca "EEEEWWWWW!!!"
    show becca 2f
    becca "Are you just walking around with those, you perv?!"
    show player 579
    show becca 1f
    player_name "What?! No! I just found these..."
    show player 578
    show becca 2bf
    becca "Whatever. You're disgusting!"
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    dex "What's going on over here!?"
    show dexter 24
    dex "This Twerp bothering you, Becca?"
    show dexter 23
    show becca 2bf
    becca "He's walking around with {b}porno mags{/b} like a total Sleezeball!"
    show dexter 21
    show becca 1f
    show player 579
    player_name "No! Seriously, they were just laying here."
    show player 578
    show dexter 22
    dex "You're grossing out {b}Roxxy's friend{/b} little man."
    hide player
    hide dexter
    show becca 2bf
    show dexter 25_26
    with dissolve
    dex "I think I'd better take those away before you make her sick!"
    return

label basketball_court_ross_magazines_retry:
    scene basketball_b
    show player 578 at left
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show becca 1f zorder 1 at right
    with dissolve
    dex "Back for more, huh?!"
    show dexter 23
    show becca 2bf
    becca "So gross..."
    show dexter 22
    show becca 1f
    dex "I guess you need another lesson."

    hide player
    hide dexter
    show becca 2bf
    show dexter 25_26
    with dissolve
    dex "Hand them over Twerp!"
    return

label basketball_court_ross_magazines_dex_pass:
    show dexter 26b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "Get off me you freakin' meathead!"
    hide dexter
    show player 38 at left
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dex "Hey! Get over here and let me punch you!"
    show player 15
    show dexter 21
    player_name "You gotta catch me first! You giant... DOUCHE-NOZZLE!"

    hide player with dissolve
    show becca 4f
    show dexter 23
    becca "Pffft, hahahaha!"
    show dexter 22
    dex "You think you're smart cause you know big words?!"
    show dexter 22 at Position(xpos=0.45, ypos=1.0) with dissolve
    show becca 1f
    dex "Get back here!"
    hide dexter with dissolve
    show becca 4f
    becca "... Douche-nozzle! Hahahah!"
    hide becca
    return

label basketball_court_ross_magazines_dex_fail:
    show becca 1f
    player_name "[dex_warn]Hey, lemme go you big lummox!"
    dex "[dex_warn]Hand over the magazines, Twerp!"
    hide dexter
    show dexter 27 with dissolve
    player_name "[dex_warn]Fine! Take em!"

    show player 16 at left
    show dexter 22 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dex "[dex_warn]That's what I thought!"
    dex "[dex_warn]Now beat it before I beat you!"

    show player 15
    show dexter 21
    player_name "[dex_warn]Grr, you're such an asshole!"
    hide player
    show dexter 28
    show becca 4f
    with dissolve
    dex "[dex_warn]Yeah, that's right, Sissyboy! Run away!"
    return

label basketball_court_roxxy_dexter_alcohol_fight:
    scene basketball_b
    show dexter 2 at right
    show becca 1 at Position(xpos=315)
    show missy 2b at left
    show roxxy 30f at Position (xpos=500)
    with dissolve
    rox "You seriously won't get us booze?!"
    show roxxy 29f
    show dexter 8
    dex "... Not unless you apologize!"
    show dexter 2
    show roxxy 30f
    rox "Forget it!"
    show roxxy 29f
    show becca 2
    becca "C'mon {b}Roxxy{/b}, just apologize..."
    becca "The party is gonna suck without alcohol!"
    show becca 1
    show roxxy 30f
    rox "No way!"
    rox "He's acting like a big baby..."
    show roxxy 29f
    show dexter 8
    dex "Oh, first I'm stupid and now I'm a baby..."
    dex "Which is it?"
    show dexter 2
    show roxxy 3bf
    rox "..."
    show roxxy 30f
    rox "You're both!"
    rox "Just a overgrown stupid baby!"
    show roxxy 29f
    show missy 6
    missy "Pfft, hahaha!"
    show missy 3
    show dexter 8
    dex "Hey!! Don't laugh at me, {b}Missy{/b}!"
    show dexter 2
    show missy 2b
    missy "..."
    show missy 2
    missy "My bad..."
    show missy 2b
    show dexter 3 with dissolve
    dex "If you want alcohol so bad, why don't you go ask that worthless drunk you call {b}a Mom{/b}?"
    show dexter 1
    show roxxy 2bf
    rox "!!!"
    show roxxy 30f
    rox "... Fuck you!"
    rox "You know what?!"
    rox "That's it, I'm done with you!"
    show roxxy 29f
    show dexter 8
    dex "Yeah well, that's fine by me!"
    show dexter 2
    show roxxy 3c with dissolve
    rox "C'mon, girls."
    rox "Let's ditch this STUPID asshole!"
    hide roxxy with dissolve
    show becca 2b
    becca "Ugh..."
    show becca 2f at Position(xpos=315) with dissolve
    becca "{b}Roxxy{/b}, what are we gonna do for drinks?!"
    hide becca
    hide missy
    show missy 3f at Position(xpos=250)
    with dissolve
    missy "..."
    show missy 3 with dissolve
    missy "..."
    show dexter 6 with dissolve
    dex "What are you looking at, skinny bitch?!"
    show dexter 2
    show missy 4c
    with dissolve
    missy "!!!"
    hide missy with dissolve
    dex "..."
    show dexter 4 with dissolve
    dex "Grr, I need to punch something!"
    hide dexter with dissolve
    pause
    show player 13 at left
    show eve 2 at right
    with dissolve
    eve "Damn!"
    eve "{b}Dexter{/b} got served!"
    show eve 5
    show player 14
    player_name "Yeah, I feel bad for whoever crosses his path right now."
    show player 13
    show eve 5
    eve "For real!"
    eve "C'mon, we should get back to {b}Miss Bissette's class{/b}."
    hide eve
    hide player
    show player 4
    with dissolve
    player_name "( ... )"
    player_name "( Yeah, it looked like {b}Roxxy{/b} was headed that way too. )"
    player_name "( ... Maybe I should {b}talk to her{/b} about this? )"
    scene black with fade
    return

label basketball_court_roxxy_basketball_challenge:
    scene basketball_b
    show player 90 at left
    show dexter 32 at right
    with dissolve
    dex "You ready for the rematch, loser?!"
    show dexter 31
    show player 12
    player_name "You're going down this time, {b}Dexter{/b}."
    show player 90
    show dexter 3
    dex "Hahaha!"
    dex "Yeah, right."
    show player 647
    show dexter 33
    with dissolve
    dex "Your ball, bitch!"
    show dexter 11 at Position (xoffset=2) with dissolve
    show player 648 with dissolve
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
