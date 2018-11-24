label park_count_night_0:
    scene park_night
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "( I can hear distant voices... )"
    show player 14
    player_name "( Maybe I should go check it out! )"
    hide player with dissolve
    return

label park_rap_battle:
    scene park_bench
    if M_dewitt.is_state(S_dewitt_eve_meet_up):
        call expression game.dialog_select("park_dewitt_eve_meet_up")
        $ M_dewitt.trigger(T_dewitt_gang_deal)

    elif M_eve.is_set("first park visit"):
        call expression game.dialog_select("park_rap_battle_first_visit")
        $ M_eve.set("first park visit", False)
        menu:
            "You look good!":
                call expression game.dialog_select("park_rap_battle_first_visit_look_good")
                jump expression game.dialog_select("park_rap_battle_options")
            "I should go home.":

                call expression game.dialog_select("park_rap_battle_first_visit_go_home")
    else:

        call expression game.dialog_select("park_rap_battle_pre")
        menu park_rap_battle_options:
            "Let's rap battle.":
                call expression game.dialog_select("park_rap_battle_start")
                menu:
                    "Chico":
                        $ rap_opponent = "Chico"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Chad" if player.stats.chr() < 4:
                        $ pass

                    "Chad" if player.stats.chr() >= 4:
                        $ rap_opponent = "Chad"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Tyrone" if player.stats.chr() < 7:
                        $ pass

                    "Tyrone" if player.stats.chr() >= 7:
                        $ rap_opponent = "Tyrone"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "Skip Mini-Game (Cheat)" if game.cheat_mode:
                        $ game.timer.tick()
                        $ player.stats.increase("chr")
                        show unlock23 at truecenter with dissolve
                        pause
                        hide unlock23 with dissolve
            "I have to go.":

                call expression game.dialog_select("park_rap_battle_leave")

    hide player
    hide eve
    with dissolve
    $ game.main()

label park_dewitt_eve_meet_up:
    show eve 1 zorder 1 at Position (xpos=450)
    show player 12 at left
    with dissolve
    player_name "Alright, I'm here. What's this idea you had?"
    show player 5
    show eve 2b
    eve "Well, we need help to clean the auditorium for the talent show, right?"
    show eve 1
    show player 10
    player_name "Yeah."
    show player 5
    show eve 2
    eve "Say hello to the help."
    show eve 1
    show tyrone 2 at Position (xpos=650)
    show chad 1 at right
    show chad 1 at Position (xoffset=-46)
    with dissolve
    tyrone "What up, crackajack?"
    show tyrone 1
    show player 12
    player_name "Whoa. You mean these guys are gonna help us clean?"
    show player 5
    show chad 4 with dissolve
    chad "That's right! What, you think just cause we gangsta we can't do a little charity work from time to time?"
    show chad 1 at Position (xoffset=-46) with dissolve
    show player 10
    player_name "Well no, I didn't mean-"
    show player 11
    show tyrone 2
    tyrone "Good, cause you'd be right! Hahaha!"
    show tyrone 1
    show player 12
    player_name "Okay, I'm officially confused."
    show player 5
    show eve 2
    eve "Heh, they're gonna help us."
    eve "... But you'll have to do something for them too."
    show eve 1
    show player 14
    player_name "Oh, I see."
    show player 12
    player_name "What do they want?"
    show player 5
    show chad 2 at Position (xoffset=-46)
    chad "You gotta {b}get us some forties{/b}, yo!"
    show chad 1 at Position (xoffset=-46)
    show player 10
    player_name "Eh, forties?"
    show player 5
    show eve 1bf with dissolve
    eve "No forties! I told you cans!"
    show eve 1cf
    show chad 2 at Position (xoffset=-46)
    chad "Pssh, fine! Whatever."
    show chad 1 at Position (xoffset=-46)
    show eve 2 with dissolve
    eve "They just want you to {b}get them some beer{/b}."
    show eve 1
    show player 10
    player_name "What?! I'm not old enough to buy beer!"
    show player 5
    show eve 6b
    eve "Well, yeah. I know that!"
    show eve 6
    eve "Doesn't your buddy have some?"
    show eve 1
    show player 12
    player_name "Huh?"
    show player 5
    show eve 6
    eve "That guy with the karaoke machine! {b}Evan{/b}?"
    show eve 1
    show player 12
    player_name "You mean {b}Erik{/b}?"
    show player 5
    show eve 2
    eve "Yeah, that guy!"
    show eve 6
    eve "{b}He had a bunch of beer there at his place{/b}!"
    show eve 1
    show player 37 with dissolve
    player_name "Ah, man."
    show player 38 with dissolve
    player_name "... They're gonna help us clean the entire thing, right?"
    show player 5 with dissolve
    show tyrone 2
    tyrone "That's the idea, dummy."
    show tyrone 1
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Fine, I'll see what I can do."
    player_name "I'll meet you guys in the {b}auditorium{/b} tomorrow for the clean up!"
    show player 5
    show eve 2
    eve "They'll be there!"
    hide eve
    hide chad
    hide tyrone
    with dissolve
    show player 10
    player_name "I should talk to {b}Erik{/b} about {b}taking some of Mr. Johnson's beer{/b}."
    return

label park_rap_battle_first_visit:
    show player 1 at left
    show eve 2 at right
    with dissolve
    eve "So you decided to show up, huh?"
    show eve 1
    show player 2
    player_name "Well, you said that I should..."
    show eve 6
    show player 11
    eve "Isn't it a bit late for you?"
    eve "Don't you have a curfew, or something?"
    show eve 1
    show player 5
    player_name "..."
    show eve 6
    show player 11
    eve "I'm just kidding!!"
    show eve 1
    show player 17
    player_name "Oh. Haha..."
    show player 1
    show eve 2
    eve "So, what's up?"
    show eve 1
    return

label park_rap_battle_first_visit_look_good:
    show player 21
    player_name "I don't know if I've ever told you, but I really like your hair!"
    show eve 4
    show player 13
    eve "Haha! That's random!"
    show player 29
    player_name "Just saying... The blue really looks good on you."
    show eve 3
    show player 13
    eve "..."
    show eve 4
    eve "Uhh... Thanks?"
    show eve 6
    show player 11
    eve "Hmm... Hey, you should stick around for a bit!"
    eve "The guys are gonna {b}rap battle{/b} soon."
    show eve 1
    show player 2
    player_name "Oh yeah? Like... dissing each other with a mic?"
    show eve 6
    show player 1
    eve "Yeah!"
    show eve 7
    show player 11
    eve "I think you should do it."
    show eve 5
    show player 23 with hpunch
    player_name "What?!"
    show eve 6
    show player 5
    eve "Oh come on. You can't be THAT shy?"
    eve "Just have fun with it!"
    show eve 5
    show player 21
    player_name "I guess I could try it..."
    show player 13
    show eve 6
    eve "So? You going to do it?"
    return

label park_rap_battle_first_visit_go_home:
    show player 10
    player_name "Oh crap! I have to go. There's something I have to do."
    show eve 2
    show player 13
    eve "I guess you really do have a curfew..."
    show eve 1
    show player 2
    player_name "Sorry. I'll come by another time to hang out!"
    show eve 7
    show player 13
    eve "Yeah, whatever."
    return

label park_rap_battle_pre:
    show player 1 at left
    show eve 6 at right
    with dissolve
    eve "Hey {b}[firstname]{/b}!"
    show eve 5
    show player 14
    player_name "Hey, {b}Eve{/b}!"
    show eve 6
    show player 1
    eve "I'm glad you showed up!"
    show eve 3
    show player 14
    player_name "It's nice seeing you again..."
    show eve 4
    show player 1
    eve "So what's up?"
    show eve 1
    return

label park_rap_battle_start:
    show player 33
    show eve 5
    player_name "I wanna rap battle again!"
    show eve 6
    show player 1
    eve "Oh yah??"
    show eve 5
    show player 26
    player_name "Yeah! I think I'm getting better."
    show eve 6
    show player 1
    eve "That's cool!"
    show eve 8
    eve "Okay. Here's your mic..."
    show eve 1
    show player 70
    player_name "Hmmm... Who should I battle?"
    show player 71
    return

label park_rap_battle_leave:
    show player 10
    player_name "Actually, I have to go. There's something I have to do."
    show player 13
    show eve 6
    eve "But, you just got here..."
    show eve 1
    show player 2
    player_name "Sorry. I'll come by another time to hangout!"
    show eve 7
    show player 13
    eve "Alright then..."
    return

label park_rap_battle_opponent:
    if rap_opponent == "Chico":
        player_name "I'll go against {b}[rap_opponent]{/b} first."
        hide eve with dissolve
        call expression game.dialog_select("park_rap_battle_opponent_chico")
    else:

        player_name "I'll go against {b}[rap_opponent]{/b}."
        hide eve with dissolve
        if rap_opponent == "Chad":
            call expression game.dialog_select("park_rap_battle_opponent_chad")
        else:

            call expression game.dialog_select("park_rap_battle_opponent_tyrone")

    hide player
    hide chico
    hide chad
    hide tyrone
    hide douche
    with dissolve
    return

label park_rap_battle_opponent_chico:
    if chico_battle_count == 0:
        call expression game.dialog_select("park_rap_battle_opponent_chico_first")
        $ chico_battle_count = 1
    else:

        call expression game.dialog_select("park_rap_battle_opponent_chico_repeat")
    return

label park_rap_battle_opponent_chico_first:
    show player 77
    show douche 1 at right
    with dissolve
    player_name "Hey guys!"
    show douche 2
    show player 74
    show chico 3 with dissolve
    chi "Who the fuck're you?!"
    show chico 1
    show player 71
    player_name "Oh, hi! I'm {b}[firstname]{/b}!"
    player_name "And I'm guessing you're... {b}Chico{/b}?"
    show chico 2
    show player 74
    chi "You don't know me, foo!"
    show chico 1
    show player 71
    player_name "Well, {b}Eve{/b} just told me your name so-"
    show chico 3 with hpunch
    show player 74
    chi "{b}YO{/b}! Shut the {b}fuck{/b}, {b}UP{/b}!"
    show player 75
    show chico 1
    player_name "..."
    show chico 4
    show player 74
    chi "I'm going first, now {b}step up{/b}!"
    return

label park_rap_battle_opponent_chico_repeat:
    show player 77
    show douche 1 at right
    with dissolve
    player_name "Hey guys!"
    show douche 2
    show player 74
    show chico 3 with dissolve
    chi "You back for some more? You lil'punk!"
    show chico 1
    show player 71
    player_name "Hey {b}Chico{/b}!"
    player_name "Yah, let's do it!"
    show chico 4
    show player 74
    chi "I'm going first. Now {b}step up{/b}!"
    return

label park_rap_battle_opponent_chad:
    show player 1
    show chad 2 at right with dissolve
    chad "So you’re the the kid who beat Chico."
    chad "Don’t know why you’re stepping up to me though unless you think you can beat me somehow."
    show chad 1
    show player 2
    player_name "That's exactly what I'm thinking."
    show chad 4
    show player 1
    chad "Check this out! Punk has balls!"
    chad "I’ll play your game, just know you aren’t leaving here the same way you came in."
    return

label park_rap_battle_opponent_tyrone:
    show player 1
    show tyrone 2 at right with dissolve
    tyrone "Ay who is this fool?"
    show tyrone 1
    show player 2
    player_name "Hey I’m-"
    show player 3
    show tyrone 3
    tyrone "Was I asking you!"
    show player 12
    show tyrone 1
    player_name "No, but I thought-"
    show tyrone 2
    tyrone "You thought wrong!"
    tyrone "Now you tryin’ to get your ass beat, or you here to waste my damn time?"
    show tyrone 4
    show player 12
    player_name "Neither?"
    show player 1
    show tyrone 3
    tyrone "Boi, I only gave you two options, and you’re doing the latter, right now!"
    show tyrone 2
    tyrone "Let me just roast you, and get this over with!"
    return

label park_take_picture_judith:
    call expression game.dialog_select("park_take_picture_judith_pre")
    if player.has_picked_up_item("masterkey"):
        call expression game.dialog_select("park_take_picture_judith_have_master_key")
    else:

        call expression game.dialog_select("park_take_picture_judith_do_not_have_master_key")

    $ M_okita.trigger(T_okita_picture_taken)
    $ game.main()
    return

label park_take_picture_judith_pre:
    scene location_park_closeup
    show player 1 at left
    show judith 5 at right
    with dissolve
    jud "You really came!"
    show player 2
    show judith 4
    player_name "I told you I would."
    show player 1
    show judith 5
    jud "This is wonderful! I can't tell you how much this means to me."
    show player 2
    show judith 4
    player_name "It's no problem, {b}Judith{/b}."
    player_name "What do you need me to do?"
    show player 1
    show judith 5
    jud "... Just, come sit next to me."
    show player 2
    show judith 4
    player_name "Alright."

    scene location_park_bench_closeup2
    show playerf 2 zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 4 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show judithfa 3 zorder 1 at Position(xpos=0.6645, ypos=0.635)
    player_name "Like this?"
    show playerf 2b
    show judithf 5
    jud "No, silly."

    scene location_park_bench_closeup3
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 8 zorder 0 at Position(xpos=0.665, ypos=1.0)
    show judithfa 4 zorder 1 at Position(xpos=0.725, ypos=0.4375)
    show juditho 1 zorder 4 at Position(xpos=0.5065, ypos=0.639)
    with dissolve
    jud "Like this!"
    jud "Smile!"

    scene location_park_bench_cutscene
    with fade
    show text "I'm not sure how this picture was supposed to help {b}Judith{/b}?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... But it seemed like a small price to pay for the lenses {b}Okita{/b} wanted, though." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Plus it made {b}Judith{/b} really happy!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_park_bench_closeup2
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 6 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show judithfa 2 zorder 1 at Position(xpos=0.67, ypos=0.7275)
    with dissolve
    jud "This is perfect!"
    show judithf 5
    jud "Thank you so much, {b}[firstname]{/b}!"
    show playerf 2
    show judithf 4
    player_name "No problem."
    show playerf 2c
    player_name "So about that spare set of glasses..."
    show judithf 2
    show judithfa 1 at Position(xpos=0.67, ypos=0.76) with dissolve
    show playerf 2b
    jud "Ohh, of course!"
    jud "I keep them in my locker at school."
    show judithf 3
    jud "I can write down the combination for you, just one second."
    show playerf 2c
    show judithf 1
    player_name "That's alright, I don't need the combination."
    return

label park_take_picture_judith_have_master_key:
    show playerf 2b
    show judithf 2
    jud "You don't?"
    show playerf 2c
    show judithf 1
    player_name "I have a masterkey to all the lockers."
    show playerf 2b
    show judithf 5
    jud "Really?! How did you manage to get that?"
    show playerf 2c
    show judithf 4
    player_name "Heh, I have my ways."
    show playerf 2b
    show judithf 5
    jud "That's so awesome!"
    jud "I had no idea you were such a bad boy!"
    show playerf 2c
    show judithf 4
    player_name "Uhh, Yeah. Heh, I guess..."
    player_name "Thanks for the help, {b}Judith{/b}. I'll see you around."
    show playerf 2b
    show judithf 5
    jud "Thank you, {b}[firstname]{/b}! See you soon!"
    return

label park_take_picture_judith_do_not_have_master_key:
    show playerf 2b
    show judithf 2
    jud "You don't?"
    show playerf 2c
    show judithf 1
    player_name "I know where {b}Principal Smith keeps her Masterkey{/b}..."
    show playerf 2b
    show judithf 5
    jud "Really?! You're going to steal the Principal's key?"
    show playerf 2c
    show judithf 4
    player_name "Steal?! I dunno about that... I just wanna borrow it till they get me a new lock."
    show playerf 2b
    show judithf 5
    jud "That's so awesome!"
    jud "I had no idea you were such a bad boy!"
    show playerf 2c
    show judithf 4
    player_name "Uhh, Yeah. Heh, I guess..."
    player_name "Thanks for the help, {b}Judith{/b}. I'll see you around."
    show playerf 2b
    show judithf 5
    jud "Thank you, {b}[firstname]{/b}! See you soon!"
    return

label fountain_dialogue:
    $ player.go_to(L_park_fountain)
    scene expression game.timer.image("park_fountain{}")
    if not player.has_item("weird_coin"):
        if game.timer.is_dark():
            show expression "objects/object_coin_01_night.png" at Position(xalign = 0.44, yalign = 0.81)
        else:

            show expression "objects/object_coin_01.png" at Position(xalign = 0.44, yalign = 0.81)
    player_name "( I can see a lot of coins in there. )"
    $ player.location.call_screen(False, False)

label coin_dialogue:
    call expression game.dialog_select("coin_dialogue_pre")
    $ player.get_item("weird_coin")
    call expression game.dialog_select("coin_dialogue_after")
    $ player.location.call_screen(False, False)

label coin_dialogue_pre:
    hide expression "objects/object_coin_01.png"
    show expression "objects/closeup_coin_01.png" at Position(xalign = 0.5, yalign = 1.0)
    with dissolve
    player_name "Huh?"
    player_name "That looks like a really old coin."
    player_name "Just look at these odd {b}symbols{/b}!"
    player_name "I should keep it. Maybe it's worth something?"
    show popup_item_coin1 at truecenter with dissolve
    return

label coin_dialogue_after:
    pause
    hide popup_item_coin1 with dissolve
    hide expression "objects/closeup_coin_01.png" with dissolve
    return

label park_night_closed:
    scene park_night
    show player 10 with dissolve
    player_name "( It's getting late. I should go home. )"
    hide player
    hide park_night
    $ game.main()

label park_pilly_button:
    call expression game.dialog_select("park_pilly_button_dialogue")
    $ player.go_to(L_map)
    $ M_roxxy.trigger(T_roxxy_drug_deal_over)
    $ game.timer.tick()
    $ game.sleep_lock = False
    $ game.main()

label park_pilly_button_dialogue:
    scene park_bench
    show player 90 at Position (xpos=400)
    show player_outfit bb 638e at Position (xpos=400)
    show clyde 2 at left
    with dissolve
    clyde "Ah, 'dere he is!"
    clyde "You just let me do the talkin' now!"
    show clyde 1
    show pilly 2f at right with dissolve
    buyer "... {b}Clyde{/b}?"
    show pilly 1f
    show clyde 4 with dissolve
    clyde "Oh, uhh... How's it goin' dere, {b}Pilly{/b}..."
    show clyde 3
    show player 10
    player_name "{b}Pilly{/b}?"
    player_name "What kind of name is that?"
    show player 5
    show pilly 2f
    pilly "Excuse me?!"
    show pilly 1f
    show clyde 22 with dissolve
    clyde "Shhhh, don't say nothin' bout his name..."
    clyde "He's sensative."
    show clyde 2
    clyde "Uhh, don't mind him, {b}Pilly{/b}. How 'bout a smoke afore we get down to business?"
    show clyde 1
    pilly "..."
    show pilly 2f
    pilly "I quit."
    show pilly 1f
    show clyde 22
    clyde "For real?!"
    clyde "... You know, nobody likes a quitter, {b}Pilly{/b}."
    show clyde 21
    show pilly 2f
    pilly "Yeah, well... I got an offer I couldn't refuse."
    pilly "Where's {b}Crystal{/b}?"
    show pilly 1f
    show clyde 22
    clyde "I'm afraid mah {b}Auntie{/b} is otherwise occupied."
    show clyde 21
    pilly "..."
    show pilly 2f
    pilly "Well that's a shame, {b}your Auntie{/b} usually offers to sweeten the deal."
    pilly "Who is this gentleman?"
    show pilly 1f
    show player 11
    player_name "..."
    show clyde 2
    clyde "Ah, well... This 'ere's my newest associate."
    clyde "You can call him... Err..."
    clyde "... {b}Mr. White{/b}!"
    show clyde 1
    show player 18
    pilly "..."
    show pilly 2f
    pilly "Somethin' fishy is going on here and I don't like it, {b}Clyde{/b}."
    show pilly 1f
    show clyde 2
    clyde "Now, now... Ain't no funny business!"
    show player 90
    show clyde 28 with dissolve
    clyde "I brought the merchandise just like we agreed..."
    clyde "Have a look fer yerself!"
    show clyde 1
    show pilly 4f
    with dissolve
    pilly "Hmm, this is a lot more than we discussed over the phone."
    show pilly 6f with dissolve
    show clyde 2
    clyde "Well ya see, I'm having a little goin' outta business sale."
    clyde "I'll give ya the entire lot for $100,000!"
    show clyde 1
    pilly "..."
    show pilly 5f
    pilly "Heh, how exactly did you arrive at that number?"
    show pilly 6f
    show clyde 26
    clyde "That's 5 pounds of mah finest stuff right 'dere!"
    clyde "It's worth every penny!"
    show clyde 25
    pilly "..."
    show pilly 5f
    pilly "I think not."
    pilly "I'll give you $60,000."
    show pilly 6f
    show clyde 26
    clyde "Pfft, are you outta yer damn mind?!"
    clyde "You ain't takin' advantage of me!"
    show clyde 25
    show pilly 5f
    pilly "Suit yerself."
    show clyde 27
    show pilly 2f
    with dissolve
    pilly "Good luck!"
    show pilly 1f
    show clyde 28
    clyde "Well, hold on now!"
    show clyde 22
    show pilly 6f
    with dissolve
    clyde "Don't do nuthin' drastic, we just hagglin' here!"
    show clyde 26
    clyde "$75,000!"
    show clyde 25
    show player 12
    player_name "We'll take the $60,000."
    show player 90
    show clyde 22
    clyde "{b}WHAT?!{/b}" with hpunch
    show clyde 26
    clyde "Now you listen here!"
    show clyde 25
    show player 12
    player_name "Shut up, {b}Clyde{/b}!"
    show clyde 21
    player_name "Don't forget why we're here!"
    show player 90
    clyde "..."
    show clyde 22
    clyde "Fine."
    show clyde 21
    show pilly 5f
    pilly "Heh, nice to see your \"associate\" is a reasonable man."
    show pilly 3f with dissolve
    pilly "Pleasure doing business with you, {b}Mr. White{/b}."
    show player 638b
    show player_outfit 638d
    show pilly 1f
    with dissolve
    pause
    show player 638
    show player_outfit 638c
    with dissolve
    player_name "Y-yeah... Thanks."
    show player 638b
    show player_outfit 638d
    hide pilly
    with dissolve
    show clyde 22
    clyde "... Man, he just bent us over the barrel with dat deal!"
    show clyde 21
    show player 12f at Position (xpos=700)
    show player_outfit 638ef at Position (xpos=700)
    with dissolve
    player_name "C'mon, let's get out of here!"
    show player 90f
    show clyde 22
    clyde "Well, hold on now!"
    clyde "What about mah cut?"
    show clyde 21
    show player 10f
    player_name "Huh?"
    show player 5f
    show clyde 2
    clyde "We gonna split that money fifty-fifty ain't we?!"
    show clyde 1
    show player 12f
    player_name "No!"
    player_name "This is to get {b}Your Aunt{/b} outta jail!"
    player_name "... Remember?!"
    show player 90f
    show clyde 2
    clyde "Well, ya but..."
    clyde "Can't we just take a lil' bit to the strip club or somethin'?"
    clyde "You could buy a whole lot of lap dances with that kind of money..."
    show clyde 1
    show player 12f
    player_name "... Get your ass home and start writing that letter!"
    show player 90f
    show clyde 26
    clyde "Alright, alright."
    clyde "Sheesh, you're a real party pooper, you know dat?"
    show clyde 31 with dissolve
    clyde "Besides, I dun wrote yer stupid letter!"
    hide clyde
    hide player
    hide player_outfit
    show expression "objects/closeup_clyde_note_01.png"
    with dissolve
    pause
    hide expression "objects/closeup_clyde_note_01.png"
    show player 13f at Position (xpos=700)
    show player_outfit bb 638ef at Position (xpos=700)
    show clyde 1 at left
    with dissolve
    player_name "..."
    show player 14f
    player_name "Yeah, that should work."
    show player 13f
    show clyde 2
    clyde "Good."
    clyde "I'm glad dis mess is all over with!"
    show clyde 1
    show player 10f
    player_name "You'd better disappear quickly if you don't wanna end up in prison."
    player_name "{b}Roxxy{/b} and I will {b}turn this into the police tomorrow{/b}."
    show player 5f
    show clyde 4 with dissolve
    clyde "Oh, dun you worry none."
    clyde "I'll be long gone by then, buddy!"
    clyde "You just take real good care mah cousin now!"
    show clyde 3
    player_name "..."
    hide clyde with dissolve
    pause
    show player 14f
    player_name "I should take the letter to {b}Roxxy tomorrow at school{/b}."
    hide player
    hide player_outfit
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
