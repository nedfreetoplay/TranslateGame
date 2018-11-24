label erik_basement:
    $ player.go_to(L_erikhouse_basement)
    if M_dewitt.get_state() == S_dewitt_eve_karaoke and game.timer.is_dark():
        call expression game.dialog_select("eriks_basement_dewitt_eve_karaoke")
        if game.cheat_mode:
            menu:
                "Play Minigame":
                    call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
                "Skip Minigame (Cheat)":
                    jump guitar_hero_minigame_karaoke_pass
        else:
            call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        jump erik_vr

    elif not M_erik.get('seen basement'):
        $ poker_table_seen = False
        call expression game.dialog_select("eriks_basement_first_time")
        $ M_erik.set('seen basement', True)
    $ game.main()

label eriks_basement_dewitt_eve_karaoke:
    scene erik_basement
    show player 13 at left
    show eve 2 at Position (xpos=600)
    show erik 1 at right
    with dissolve
    eve "Hey, it's about time! I was starting to think you flaked on me!"
    show eve 5
    show player 29 with dissolve
    player_name "Sorry, I got held up! Hey {b}Erik{/b}!"
    show player 13 with dissolve
    show erik 4
    eri "Hey, {b}[firstname]{/b}! I was just telling {b}Eve{/b} about my guild on World of Orcette."
    show erik 1
    show eve 6b
    eve "Yeah, it was riveting."
    show eve 5
    show player 14
    player_name "Heh, I see."
    player_name "Thanks for letting us come over tonight, {b}Erik{/b}."
    show player 13
    show erik 4
    eri "Yeah, no problem, dude! You're lucky my guild cancelled the raid tonight."
    show erik 1
    show player 10
    player_name "Raid?"
    show player 13
    show eve 2b
    eve "No, don't ask!"
    show eve 1
    show player 11
    show erik 51
    eri "..."
    show eve 2
    eve "Is that booze over there?"
    show eve 5
    show player 13
    show erik 53
    eri "Y-yeah, why?"
    show erik 52
    show eve 6
    eve "Cause I have a feeling I'm gonna need some tonight!"
    show eve 5
    show player 14
    player_name "That's not a bad idea. It'll loosen us up for the karaoke."
    show player 13
    show erik 54
    eri "Oh yeah, I guess that makes sense."
    show erik 52 with dissolve
    show eve 6
    eve "Hey, you've got bourbon, very classy!"
    eve "Why don't you go and grab us some glasses while {b}[firstname]{/b} and I get comfortable on the couch."
    show eve 5
    show erik 54
    eri "... Sure, okay!"
    hide erik with dissolve
    pause
    show eve 24 with dissolve
    eve "Can you believe {b}Erik's{/b} basement is sooo cool?"
    eve "C'mon {b}[firstname]{/b}, let's look at the other room!"
    hide player
    show eve 25f
    with dissolve

    pause

    scene erik_basement_back_b_01
    show player 13 at left
    show eve 2b at Position (xpos=500)
    eve "Wow... This is so awesome..."
    show eve 5
    show player 14
    player_name "I know right? This is the perfect party house."
    show player 13
    show eve 2b
    eve "So have you ever had bourbon before?"
    show eve 5
    show player 10
    player_name "I don't think so..."
    show player 5
    show eve 6
    eve "Get ready to have your mind blown!"
    show eve 5
    show player 13

    show erik 15f at right with dissolve
    eri "I was wondering where you guys went."
    eri "Will these work?"
    show erik 15bf

    show eve 9 with dissolve
    pause
    show eve 10
    eve "Sure."
    show erik 16f with dissolve
    pause
    show erik 17f with dissolve
    show player 185
    show eve 19
    with dissolve
    eve "Bottoms up!"
    show player 189
    show erik 19f
    show eve 18
    with dissolve
    pause
    show player 190
    show eve 21
    show erik 18f
    with dissolve
    eri "*Cough* *Cough* It went down the wrong throat! *Cough*"
    show erik 17f
    show eve 19
    eve "Mmmhmm, that's some good shit right there!"
    show eve 20
    show player 191
    player_name "Wow!!! That's really strong!"
    show player 190
    show eve 19
    eve "Don't puss out on me yet, boys!"
    show eve 20
    show erik 18f
    eri "Sure..."
    show eve 9
    show player 13
    with dissolve
    show erik 16f with dissolve
    pause
    show erik 17f with dissolve
    show player 188
    show eve 19
    with dissolve
    eve "Drink!"
    show player 189
    show eve 18
    show erik 19f
    with dissolve
    pause
    show erik 17f with dissolve
    show eve 21 with dissolve
    eve "Whooooo!"
    show eve 20
    show player 191 with dissolve
    player_name "Damn!"
    show player 190
    player_name "..."
    show player 187
    player_name "Alright, we should probably get this karaoke machine started up."

    scene erik_basement_back_b_03
    show eve 20 at Position (xpos=500)
    show erik 18f at right
    with dissolve
    eri "It's hot in here, is anybody else hot?"
    show erik 17f
    show eve 19f with dissolve
    eve "Heh, it's the booze, it's warms up your insides..."
    show eve 20f
    player_name "{b}Erik{/b}, how the heck do you work this thing?"
    show eve 18f with dissolve
    show erik 18f
    eri "I'll do it, move."

    scene erik_basement_back_b_02
    show eve 18f at Position (xpos=500)
    show player 14 at left
    with dissolve
    player_name "You ready to stretch those pipes of yours?"
    show player 13
    show eve 19 with dissolve
    eve "Yeah, I'm gonna need a lot more booze before I'm ready to sing."
    eve "Why don't you guys get started without me?"
    show eve 20
    show player 14
    player_name "... Oh, ehh. Alright."
    show player 13
    eri "It's ready!"
    show player 14
    player_name "Let's get this party started!"
    hide player
    hide eve
    with dissolve
    return

label eriks_basement_dewitt_get_beer:
    scene erik_basement
    show player 571 with dissolve
    player_name "Yeah, this should be plenty."
    hide player with dissolve
    show popup_item_beer1 at truecenter with dissolve
    pause
    $ player.get_item("beer")
    hide popup_item_beer1 with dissolve
    $ game.main()

label eriks_basement_dewitt_replace_guitar:
    scene erik_basement
    show player 575 at right with dissolve
    player_name "( Hmm. )"
    show player 574
    player_name "( It's not that noticeable. )"
    show player 575
    player_name "( ... Yeah, I think this might actually work! )"
    show player 577 with dissolve
    pause
    show mrsj 50f at left with dissolve
    player_name "( Now I just need to get the real guitar out of here without {b}Mrs. Johnson{/b} seeing me. )"
    show player 576
    show mrsj 52f
    mrsjo "What the hell is that?"
    show mrsj 38f
    show player 577df with hpunch
    player_name "!!!"
    show player 577cf
    player_name "H-hey, {b}Mrs. Johnson{/b}..."
    player_name "I didn't hear you come down."
    show player 577bf
    show mrsj 52f
    mrsjo "Did you make that thing, {b}[firstname]{/b}?"
    show mrsj 38f
    show player 577cf
    player_name "Y-yeah. Do you like it?"
    show player 577bf
    show mrsj 49f
    mrsjo "Hehehe, is this so I won't notice you walking off with my ex-husband's guitar?"
    show mrsj 50f
    show player 577cf
    player_name "... I just need to borrow it for the school talent show and {b}Erik{/b} thought you might get upset."
    show player 577bf
    show mrsj 18f
    mrsjo "Did he?"
    show mrsj 49f
    mrsjo "Aww, he's such a sweet young man to care about my feelings so much."
    show mrsj 50f
    show player 577cf
    player_name "So would you mind if I borrowed this guitar for a little while?"
    show player 577bf
    show mrsj 18f
    mrsjo "Pfft, not at all, honey."
    show mrsj 49f
    mrsjo "I never understood why that good for nothing ex of mine loved them so much. He wasn't even very good at playing them."
    mrsjo "You can keep the thing for all I care!"
    mrsjo "It's just sitting down here gathering dust after all."
    show mrsj 50f
    show player 577f
    player_name "Really?"
    show player 576f
    show mrsj 49f
    mrsjo "Well sure! You've been such a good friend to {b}Erik{/b}!"
    mrsjo "It's the least I can do!"
    show mrsj 50f
    show player 577f
    player_name "Thank you so much, {b}Mrs. Johnson{/b}!"
    show player 576f
    show mrsj 49f
    mrsjo "No problem, honey!"
    mrsjo "Just come back real soon and tell me all about this talent show of yours!"
    show mrsj 50f
    show player 577f
    player_name "Yeah, okay! See you soon {b}Mrs. Johnson{/b}!"
    hide player
    hide mrsj
    with dissolve
    $ player.remove_item("fake_guitar")
    $ player.get_item("guitar")
    $ M_dewitt.trigger(T_dewitt_get_fender_guitar)
    $ game.main()

label poker_table:
    scene erik_basement
    if not poker_table_seen:
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "You have a freaking {b}poker table{/b} down here?"
        show player 1
        show erik 4
        eri "Yeah. You wanna play?"
        $ poker_table_seen = True
        menu:
            "Play poker with {b}Erik{/b}?"
            "Yes":
                player_name "I would, but I've never played poker before..."
                show player 14
                eri "That's fine, I'll explain the rules."
                show player 1
                show erik 4
                player_name "In that case, let's play!"
                show player 14
                show erik 1

                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                $ game.main()
            "No":

                player_name "Maybe some other time, man. I'm not in the mood right now."
                show player 14
                show erik 1
                eri "That's cool. No problem."
                show player 1
                show erik 4
                hide player
                hide erik
    else:

        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Let's play a game of poker!"
        show player 1
        show erik 5
        eri "Yeah I guess we could try it..."
        eri "But don't we need more players?"
        show erik 1
        show player 4
        player_name "Hmm..."
        player_name "Yeah. You're right."
        player_name "We should {b}find someone{/b} who'd want to play with us."
        hide erik
        hide player
        with dissolve
    $ game.main()

label mrsj_poker:
    if poker_bot02 == "mrsj" and not poker_drunk:
        scene erik_basement_c
        show mrsj 19 at right with fastdissolve
        show erik 1f at Position(xpos=300,ypos=768) with fastdissolve
        show player 1 at left with dissolve
        mrsjo "You boys aren't planning on playing like this, are you?"
        show player 11
        show mrsj 14
        player_name "..."
        show player 10
        player_name "What do you mean?"
        show player 11
        show mrsj 18
        mrsjo "You can't play poker without a nice drink!"
        show mrsj 14
        show player 1
        show erik 4f
        eri "A drink?"
        show erik 1f
        show mrsj 18
        mrsjo "Let's see what's left in the {b}alcohol cabinet{/b}, shall we?"
        hide player
        hide mrsj
        hide erik
        with dissolve

    elif poker_bot02 == "mrsj" and poker_drunk:
        scene poker_table
        show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
        show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
        show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
        with fade

        mrsjo "So..."
        mrsjo "Are we playing {b}Omaha{/b}, or {b}Texas Hold'em{/b}?"
        show mrsjpoker 1
        player_name "..."
        player_name "We only know {b}Strip poker{/b}..."
        show mrsjpoker 2
        mrsjo "Ha ha! Are you kidding me?"
        show mrsjpoker 10 at Position(xpos=856,ypos=627)
        player_name "It's the only kind people play at school..."
        show erikpoker 2
        eri "You don't have to... {b}Mrs. Johnson{/b}."
        show erikpoker 11
        show mrsjpoker 9 at Position(xpos=856,ypos=627)
        mrsjo "I'll play!"
        show mrsjpoker 4 at Position(xpos=857,ypos=626)
        mrsjo "I'm not a prude. I can have fun, too!"
        show mrsjpoker 2
        mrsjo "I used to play Strip poker back in the day..."
        show mrsjpoker 5
        mrsjo "...And I was the {b}best{/b} at it!"
        show erikpoker 12
        show mrsjpoker 1
        eri "So, what do we do now?"
        show erikpoker 1
        menu mrsj_poker_repeat:
            "Play.":
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
                show erikpoker 1
                player_name "Let's play!!"
                jump start_poker
            "How to play.":

                player_name "Remind me again, how do I play poker?"
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                jump mrsj_poker_repeat

            "Skip Mini-Game (Cheat)" if game.cheat_mode:
                menu:
                    "{b}Mrs. Johnson{/b} Loses":
                        jump mrsj_lost
                    "{b}Erik{/b} Loses":
                        jump erik_lost
                    "{b}[firstname]{/b} Loses":
                        jump player_lost
    $ game.main()

label cabinet:
    scene erik_basement_cabinet
    if poker_bot02 == "":
        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "That's a lot of alcohol..."
        show player 1
        show erik 4
        eri "Yeah, {b}Mr. Johnson{/b} always kept it well stocked."
        show erik 1
        show player 14
        player_name "Should we try some?"
        show player 1
        show erik 4
        eri "I was thinking maybe we should keep it for a special occasion?"
        show erik 1
        show player 4
        player_name "I guess you're right."
        player_name "We should {b}find someone{/b} who'd want drink with us."
        hide erik
        hide player
        with dissolve

    elif poker_bot02 == "mrsj":
        if mrsj.completed(mrsj_poker_night_2):
            show erik 4f at Position(xpos=300)
            show player 1 at left
            show mrsj 14 at right
            with dissolve
            eri "I'll fetch the whiskey!"
            show erik 1f
            show mrsj 19
            show player 11
            mrsjo "Oh, are you two sure about that?"
            show mrsj 19c
            show player 10
            player_name "About what?"
            show mrsj 19
            show player 11
            mrsjo "The alcohol, you remember what happened last time, right?"
            show mrsj 19c
            show erik 5f
            eri "But, we all had fun, didn't we?"
            show erik 1f
            pause
            show mrsj 14 with fastdissolve
            pause
            show mrsj 17
            show player 1
            mrsjo "I suppose you're right..."
            show mrsj 18
            mrsjo "Oh, what the heck, let's do it!"
        else:

            show erik 5f at Position(xpos=300,ypos=768)
            show player 1 at left
            show mrsj 14 at right
            with dissolve
            eri "Whiskey..."
            eri "Whiskey... whiskey..."
            eri "Whiskey... whiskey... whiskey..."
            eri "There's nothing but whiskey in here..."
            show erik 1f
            show mrsj 17
            mrsjo "My husband only drank whiskey."
            show mrsj 14
            show player 14
            player_name "That's fine!"
            player_name "We'll take whatever's in there, ha ha!"
            show erik 15
            show player 1
            eri "Should we try it before we take it to the table?"
            show erik 16
            show mrsj 22
            mrsjo "Let's see how this tastes..."
            show erik 20
            show mrsj 21
            show player 185
            with fastdissolve
            eri "Here we go..."
            show player 186
            show erik 17
            player_name "Cheers!"
            show player 189
            show erik 19
            show mrsj 25
            with fastdissolve

            pause
            show mrsj 26
            show erik 17
            show player 190
            with fastdissolve
            pause
            show player 191
            player_name "Ugh!!"
            show player 188
            show mrsj 24
            show erik 17
            mrsjo "Woaa.."
            show erik 20
            show mrsj 14
            eri "Hmm... Not bad!"
            show erik 17
            player_name "..."
            show player 187
            player_name "You liked that?!"
            show player 188
            show erik 20
            eri "Yeah, it's kind of sweet."
            show player 185
            show erik 17
            show mrsj 18
            mrsjo "Alright, boys! Let's take this back and start the game!"
        hide mrsj
        hide erik
        hide player
        with dissolve
        $ poker_drunk = True
    $ game.main()

label mrsj_afterpoker_fun_block:
    scene erik_basement
    show player 11 at left
    show erik 4 at right
    with dissolve
    eri "I thought we were *Hic* going to the backroom..."
    eri "{b}Mrs. Johnson{/b} is waiting for us, remember?"
    show player 14
    show erik 1
    player_name "Oh, riiiight!"
    player_name "Let's go back there and see what she wants."
    show player 1
    show erik 4
    eri "I *Hic* agree."
    hide erik
    hide player
    with dissolve
    $ game.main()

label erik_vr:
    scene location_erik_basement01_closeup
    show erik 15f at right
    show player 13 at left
    with dissolve
    eri "Hey, {b}[firstname]{/b}."
    show erik 15bf
    show player 14
    player_name "Hey!"
    show player 11
    player_name "..."
    show player 12
    player_name "Are you... Drinking?"
    show player 11
    show erik 15f
    eri "Oh, {b}Mrs. Johnson{/b} wanted me to clean up the basement."
    eri "I was just getting ready to toss all this old booze."
    show erik 15bf
    pause
    show player 38 with dissolve
    player_name "!!!" with hpunch
    show player 23 with dissolve
    player_name "Wait!"
    player_name "Can't you see?"
    show player 18
    show erik 15f
    eri "Huh?"
    show erik 15bf
    show player 14
    player_name "We can use all these things!!"
    show player 13
    show erik 5 with dissolve
    eri "What for?"
    show erik 3b
    show player 17
    player_name "Well, I have an idea."
    show player 14
    player_name "What if we put this liquor to good use!"
    show player 17
    player_name "I mean, it'd be a shame to waste it all..."
    show player 13
    show erik 5
    eri "Hmmm.... Yeah, I guess."
    show erik 3b
    show player 14
    player_name "What if we had some friends from school come over and... Have fun!"
    show player 33
    player_name "This place is the perfect party room!"
    show player 14
    player_name "Just think, we could invite girls over, play poker, and get drunk!"
    show player 13
    show erik 5
    eri "I'm not so sure."
    eri "{b}Mrs. Johnson{/b} might flip out if things got out of hand..."
    show erik 3b
    show player 12
    player_name "Come on, {b}Erik{/b}... This place is perfect!"
    show player 14
    player_name "Just think of the cool stuff we could do!"
    show player 33
    player_name "We could even get girls to play some strip poker..."
    show player 18
    show erik 4 with hpunch
    eri "!!!"
    eri "I don't know, {b}[firstname]{/b}..."
    show erik 1
    show player 30
    player_name "Hmm..."
    pause
    show player 12
    player_name "What if I bought you something you always wanted?"
    player_name "Would you help me invite friends over?"
    show player 14
    player_name "I've been making some money! I can definitely help you get what you want..."
    show player 13
    eri "..."
    show erik 4
    eri "Well, there is something I've always wanted... But it costs a LOT!"
    show erik 1
    show player 14
    player_name "Yeah? What is it?"
    show player 13
    show erik 4
    eri "Down at {b}Cosmic Cumics{/b}, I saw they were selling the VR headset {b}Virtual Saga X{/b}."
    show erik 1
    show player 17
    player_name "Done!"
    show player 13
    show erik 5
    eri "Really?!"
    eri "But, wait! I... I also want a game with it, too."
    show erik 4
    eri "It's called... {b}World of Orcette{/b}."
    show erik 1
    show player 11
    player_name "..."
    show player 12
    player_name "Is that one of those lewd games about-"
    show player 5
    show erik 5b
    eri "Uhh!!"
    show erik 5
    eri "Anyway!"
    show erik 4
    eri "Those would do it, I think!"
    eri "You can find them at {b}Cosmic Cumics{/b}, in the mall."
    show erik 1
    show player 14
    player_name "Alright."
    player_name "It's a deal!"
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_vr)
    $ M_erik.unforce()
    $ game.main()

label erik_card_hunt:
    scene location_erik_basement01_closeup
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Hi, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Hey, {b}Erik{/b}."
    show player 2
    player_name "Thought I'd stop by and see what you're up to."
    show player 1
    show erik 5
    eri "Oh, just looking for my {b}Magic the Fappening{/b} cards."
    eri "I have to get ready for the next tournament, but I can't seem to find them..."
    show erik 1
    show player 14
    player_name "Oh yeah?"
    show player 13
    show erik 5
    eri "I usually leave them down in the basement, but they aren't here."
    show erik 1
    show player 12
    player_name "Hmm..."
    player_name "I can help you look for them. They shouldn't have gone too far."
    show player 13
    show erik 5
    eri "Yeah, they've gotta be here somewhere."
    eri "I wonder if {b}Mrs. Johnson{/b} moved them?"
    show erik 1
    show player 14
    player_name "Oh yeah, I was supposed to tell you."
    show player 17
    player_name "She mentioned she was going to make dinner for you."
    show player 5
    show erik 5
    eri "You mean she's gone already? Shoot!"
    eri "Maybe I left them upstairs."
    eri "Could you look down here?"
    show erik 1
    show player 14
    player_name "Yeah."
    show player 5

    hide erik with dissolve
    show player 4
    player_name "( I wonder where he left the cards. )"
    show player 12
    player_name "( They have to be down here somewhere... )"
    hide player with dissolve
    return

label erik_orcette:
    scene location_erik_basement01_closeup
    show erik 1 at right
    show player 14 at left
    with dissolve
    player_name "Down in the basement, again?"
    player_name "What are you up to?"
    show player 13
    show erik 5
    eri "Hey, {b}[firstname]{/b}!"
    eri "... I was just thinking about selling this poker table."
    show erik 1
    show player 23
    player_name "What?!"
    show player 30
    player_name "Why!"
    show player 12
    player_name "That poker table is so cool!"
    show player 5
    show erik 3b
    eri "..."
    show player 10
    player_name "I mean that thing is made out of solid oak!"
    show player 11
    show erik 5
    eri "Yeah... But nobody ever uses it."
    eri "And I could use some money."
    show erik 3b
    show player 12
    player_name "Would {b}Mrs. Johnson{/b} even be okay with you selling her ex-husbands stuff?"
    show player 11
    show erik 5
    eri "I think so. She's always saying she'll do anything to make me happy and I really need the cash..."
    show erik 3b
    show player 12
    player_name "Come on, {b}Erik{/b}. These things might have sentimental value to her."
    player_name "What's so important that you need to sell off her stuff?"
    show player 5
    show erik 3
    eri "Well..."
    show erik 5
    eri "It's sort of personal?"
    show erik 3b
    show player 26
    player_name "Oh, come on."
    pause
    show player 14
    player_name "Listen, I'll buy you whatever you want if you promise not to sell the table."
    show player 30
    player_name "Deal?"
    show player 5
    eri "..."
    show erik 4
    eri "Why would you do that?"
    show erik 1
    show player 43
    player_name "Because I have some plans for this basement!"
    show player 14
    player_name "I think we could use it to hang out... And maybe invite... people over!"
    show player 13
    show erik 4
    eri "Alright..."
    show erik 5
    eri "But promise you won't make fun of me?"
    show erik 3b
    show player 12
    player_name "Ehh... Sure?"
    show player 5
    eri "..."
    show erik 5
    eri "You can only buy this thing online..."
    eri "So if your computer is still broken, you're gonna need to fix it."
    show erik 1
    show player 12
    player_name "What is it you want me to buy, {b}Erik{/b}?"
    show player 5
    eri "..."
    show erik 4
    eri "Well, have you ever heard of the {b}Orcette{/b}?"
    show erik 1
    pause
    show player 10
    player_name "The what?"
    show player 11
    show erik 5
    eri "It's like... a rubber... tube?"
    show erik 1
    show player 12
    player_name "What?"
    show player 11
    show erik 5
    eri "And it's green!"
    show erik 1
    show player 14
    player_name "Wait... Is it a, sex toy?!"
    show player 13
    show erik 5
    eri "Hey! You promised!"
    show erik 3
    show player 17
    player_name "Alright. Alright."
    show player 26
    player_name "I've got no problem buying it for you."
    show player 13
    show erik 5
    eri "That would be awesome, {b}[firstname]{/b}!"
    show erik 3
    show player 14
    player_name "Just remember. You're not going to sell any of {b}Mrs. Johnson{/b}'s things, okay?!"
    show player 13
    show erik 5
    eri "Yeah, I promise."
    eri "Just bring it over as soon as you can!"
    show erik 1
    show player 12
    player_name "I will."
    show player 10
    player_name "Just chill though, cause it will probably take awhile for delivery."
    show player 11
    show erik 5
    eri "See if they have one of those package trackers!"
    show erik 1
    show player 12
    player_name "What?"
    show player 11
    show erik 5
    eri "You know, the delivery companies nowadays track their shipments."
    show erik 4
    eri "They can tell you exactly when it will arrive."
    show erik 1
    show player 12
    player_name "Alright. I'll see what I can do."
    show player 5
    show erik 4
    eri "Thanks, {b}[firstname]{/b}. You're the best!"
    show erik 1
    show player 14
    player_name "Yeah. Yeah."

    hide erik with dissolve
    show player 12
    player_name "( I guess I should get on my computer and look up this {b}Orcette{/b}... )"
    hide player with dissolve
    $ erik.add_event(erik_orcette)
    $ M_erik.unforce()
    $ game.main()

label eriks_basement_first_time:
    scene erik_basement
    show player 14 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Duuuuuude! This place looks freaking awesome!"
    player_name "Why have you not shown me this before?"
    show player 1
    show erik 4
    eri "I dunno. I guess I never thought about it..."
    eri "Plus, {b}Mr. Johnson{/b} was pretty protective of his man cave back when he was living here."
    show erik 14
    eri "He liked his privacy."
    show erik 4
    eri "But I don't have to worry about that anymore!"
    show erik 1
    show player 14
    player_name "Can I take a look around the place?"
    show erik 1
    show player 1
    eri "Sure thing, Dude!"
    show erik 1
    show player 14
    player_name "Sweet!"
    show player 1
    show erik 5
    eri "Just try not to break anything."
    eri "{b}Mrs. Johnson{/b} might get pissed!"
    show erik 1
    show player 14
    player_name "I'll be careful."
    hide player with dissolve
    hide erik with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
