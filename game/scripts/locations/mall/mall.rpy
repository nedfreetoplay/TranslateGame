label mall_dialogue:
    $ player.go_to(L_mall)
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)

    if L_mall.first_visit:
        call expression game.dialog_select("mall_first_visit")
        $ L_mall.visited()

    if M_mom.is_state(S_mom_mall_outing):
        call expression game.dialog_select("mall_mom_mall_outing")
        $ M_mom.trigger(T_mom_mall_arrival)

    if M_roxxy.is_state(S_roxxy_fake_id_ask_terry) and M_roxxy.get("take roxxy mall"):
        call expression game.dialog_select("mall_roxxy_fake_id_ask_terry")

    if M_diane.is_state(S_diane_go_to_mall):
        call expression game.dialog_select("mall_diane_get_bug_spray")
        $ M_diane.trigger(T_diane_arrived_at_mall)

    if M_jenny.is_state(S_jenny_go_shopping):
        call expression game.dialog_select("mall_jenny_go_shopping")
        $ M_jenny.trigger(T_jenny_go_at_pinks)
    elif M_jenny.is_state(S_jenny_get_a_mask):
        call expression game.dialog_select("mall_jenny_get_a_mask")

    $ game.main()

label cupid_store_waiting_line:
    scene expression "backgrounds/location_mall_closeup_comic.jpg" with None
    show player 10 at left
    show erik at flip
    show erik at Position (xpos=100)
    show karl at flip
    show karl at Position (xpos=350)
    show justin at flip
    show justin at Position (xpos=600)
    with dissolve
    player_name "{b}Erik{/b}?"
    show player 5
    eri "Hmm?"
    show erik f_normal_talk at unflip
    show erik at Position (xpos=-300)
    show karl at unflip
    show karl at Position (xpos=-150)
    with dissolve
    eri "{b}[firstname]{/b}?"
    show erik f_normal with None
    show justin at unflip
    show justin at Position (xpos=50)
    with dissolve
    show player 14
    player_name "What's going on?"
    show player 13
    show erik f_normal_talk
    eri "I didn't know you were a wrestling fan."
    show erik f_normal
    show player 10
    player_name "Wrestling?"
    show player 13
    show erik f_normal_talk
    eri "Yeah, aren't you here to pick up the new game?"
    show erik f_normal
    show player 10
    player_name "New game?"
    show player 5
    show karl f_curious_talk
    karl "You don't know about {b}WPWF{/b}?"
    show karl f_curious
    show player 10
    player_name "Excuse me?"
    show player 5
    show karl f_curious_talk
    karl "Uhh, {b}Womens Professional Wrestling Federation{/b}?"
    show karl f_angry_talk
    karl "Psh, who is this joker?"
    show karl f_angry with None
    show erik f_normal_talk at flip
    show erik at Position (xpos=100)
    with dissolve
    eri "Whoa, calm down {b}Brutalitops{/b}!"
    eri "{b}[firstname]{/b} is a friend."
    show erik f_normal
    show justin f_normal_talk
    justin "Does he want to join our merry band?"
    show justin f_normal
    show karl f_angry_talk
    karl "C'mon, we don't need this guy."
    show karl f_angry
    show erik f_normal_talk
    eri "Eh, {b}[firstname]{/b} doesn't really play {b}WoO{/b}."
    show erik f_normal
    show karl f_eyeroll
    karl "Laaaaame."
    show karl f_angry
    show justin f_normal_talk
    justin "That's too bad, our guild could really use some new members."
    show justin f_normal
    show karl f_embarassed_talk
    karl "I bet he doesn't even have a class."
    show karl f_embarassed
    show erik f_normal_talk
    eri "We could give him one."
    show erik f_normal
    show justin f_normal_talk
    justin "Hmm, I bet he'd make an excellent bard."
    show justin f_normal
    show karl f_embarassed_talk
    karl "Yeah right, he'd probably fit better as one of those fancy pants druids..."
    show karl f_embarassed
    show player 10
    player_name "{b}Erik{/b}, who are these guys?"
    show player 5 with None
    show karl f_normal with None
    show erik f_normal_talk at unflip
    show erik at Position (xpos=-300)
    with dissolve
    eri "Heh, these are my guild mates from {b}World of Orcette{/b}."
    show erik f_normal
    show player 10
    player_name "Oh."
    show player 5 with None
    show erik f_normal_talk at flip
    show erik at Position (xpos=100)
    with dissolve
    eri "This here is {b}Karl{/b}."
    show erik f_normal
    show karl f_angry_talk a_dressed_fist with dissolve
    karl "Only my friends know me as {b}Karl{/b}."
    show karl f_crazy_laugh
    karl "You can call me {b}Brutalitops{/b}. Master of the Seven Sided Strike and defender of goblin maidens!"
    show karl f_normal a_dressed_sides with dissolve
    show player 30
    player_name "Goblin maidens?"
    show player 5 with None
    show erik f_normal_talk at unflip
    show erik at Position (xpos=-300)
    with dissolve
    eri "He's our Fury Monk."
    show erik at Position (xpos=-350) with dissolve
    eri "Hence the anger issues."
    show erik f_normal at Position (xpos=-300) with dissolve
    show player 10
    player_name "O-okay..."
    show player 5 with None
    show erik f_normal_talk at flip
    show erik at Position (xpos=100)
    with dissolve
    eri "And this is {b}Justin the Wise{/b}, our guild leader and the most talented magician in all the lands."
    show erik f_normal
    show justin f_normal_talk
    justin "Oh, please... He's exaggerating."
    show justin f_normal
    show karl f_normal_talk
    karl "No way, man!"
    karl "The way you charmed that demoness the other day..."
    show karl f_normal
    show erik f_normal_talk
    eri "Yeah, it was incredible!"
    show erik f_normal
    show justin f_boasting_talk a_dressed_boasting with dissolve
    justin "That was nothing."
    justin "The real magic didn't happen until we retired to my bed chambers for the night."
    show justin f_normal_talk
    justin "If you catch my drift?"
    show justin f_normal a_dressed_sides with dissolve
    show player 10
    player_name "Ehh..."
    show player 5
    show justin f_normal_talk
    justin "Pleasure to meet you, {b}[firstname]{/b}."
    justin "Any friend of {b}Erik the Mighty{/b} is a friend to me as well."
    show justin f_normal with None
    show erik at unflip
    show erik at Position (xpos=-300)
    with dissolve
    show player 14
    player_name "Y-yeah, thanks."
    player_name "So all these people are here to buy a wrestling game?"
    show player 13
    show erik f_normal_talk
    eri "Pretty much."
    show erik f_normal
    show justin f_normal_talk
    justin "Not me, I'm here to meet the {b}Pink Cyclone{/b} in the flesh!"
    justin "She's always been my favorite."
    show justin f_normal
    show player 14
    player_name "Who?"
    show player 13
    show karl f_normal_talk
    karl "{b}Pink Cyclone{/b}, man!"
    karl "You've seriously never heard of her?!"
    show karl f_normal
    show player 14
    player_name "Nope, sorry."
    show player 13
    show karl f_curious_talk
    karl "Sheesh, you need to get out more."
    show karl f_curious
    show erik f_normal_talk
    eri "She's the undefeated champion of the {b}WPWF{/b}!"
    show erik f_normal
    show player 14
    player_name "Oh, really?"
    show player 13
    show justin f_normal_talk
    justin "More like the undefeated champion of my heart."
    show justin f_normal
    show karl f_eyeroll
    karl "Well, she's not exactly undefeated..."
    show karl f_normal with None
    show erik f_normal_talk at flip
    show erik at Position (xpos=100)
    with dissolve
    eri "C'mon man, {b}Nikita{/b} totally cheated!"
    eri "The Commissioner even declared the match no contest."
    show erik f_normal
    show karl f_curious_talk
    karl "Doesn't matter, the {b}Pink Cyclone{/b} lost the belt."
    show karl f_curious
    show erik f_normal_talk
    eri "Only because {b}Nikita{/b} shattered her knee with a chair!"
    show erik f_normal
    show karl f_curious_talk
    karl "Yeah, leaving her incapable of defending the title."
    show karl f_curious
    show erik f_normal_talk
    eri "She's still 34-0"
    show erik f_normal
    show karl f_embarassed_talk
    karl "You mean, 34-0-1"
    show karl f_embarassed
    show erik f_normal_talk
    eri "It was a no contest!"
    show erik f_normal
    show karl f_embarassed_talk
    karl "She hasn't wrestled since, man and that was three years ago..."
    show karl f_embarassed
    show player 14
    player_name "So this {b}Pink Cyclone{/b} lady is here today?"
    show player 13
    show karl f_normal with None
    show erik f_normal_talk at unflip
    show erik at Position (xpos=-300)
    with dissolve
    eri "Yeah, she's inside signing autographs to promote the game."
    eri "You wanna come with us to meet her?"
    show erik f_normal
    show player 29 with dissolve
    player_name "Eh, sure... I guess."
    show player 13 with dissolve
    show justin f_boasting_talk
    justin "I'm totally gonna declare my love to her."
    show justin f_boasting with None
    show erik at flip
    show erik at Position (xpos=100)
    show karl f_normal_talk at flip
    show karl at Position (xpos=350)
    with dissolve
    karl "Don't you have enough women, {b}Justin{/b}?!"
    show justin f_normal
    karl "With the new Demoness and those elven twins, you've basically got a harem!"
    show karl f_normal
    show player 17
    show justin f_normal_talk
    justin "There's no such thing as enough women, {b}Karl{/b}..."
    show justin f_normal
    show player 13
    show karl f_normal_talk
    karl "I dunno, I'm happy with what I've got."
    show karl f_normal
    show justin f_normal_talk
    justin "Hah, you and your goblin maidens..."
    justin "I just don't get the appeal."
    show justin f_normal
    show erik f_normal_talk
    eri "I think he's got a midget fetish!"
    show erik f_normal
    show player 11
    show karl f_crazy_laugh
    karl "What?!"
    show karl f_angry_talk
    karl "That's not it at all, you guys!"
    show karl f_angry
    player_name "..."
    scene black with fade
    pause
    scene expression "backgrounds/location_mall_closeup_comic.jpg" with None
    show player 9 at left
    show erik at flip
    show erik at Position (xpos=100)
    show karl f_normal_talk at flip
    show karl at Position (xpos=350)
    show justin at flip
    show justin at Position (xpos=600)
    with dissolve
    karl "Alright, we're next!"
    show karl f_normal
    show justin f_boasting_talk
    justin "Wish me luck, fellas."
    hide karl
    hide justin
    with dissolve
    show erik f_normal_talk
    eri "That crazy bastard..."
    show erik f_normal
    show player 14 with dissolve
    player_name "You definitely have some colorful friends, {b}Erik{/b}."
    show player 13
    show erik f_normal_talk
    eri "Yeah, we get along pretty well."
    show erik at unflip
    show erik at Position (xpos=-300)
    with dissolve
    eri "You really can join our guild, you know?"
    show erik f_normal
    show player 14
    player_name "Eh, I'm not sure I would fit in with those guys."
    show player 13
    show erik f_normal_talk
    eri "Dude, what are you talking about?!"
    eri "You're awesome!"
    eri "We'd all be ecstatic if you joined."
    show erik f_normal
    show player 14
    player_name "Heh, thanks for saying that {b}Erik{/b}."
    player_name "I'll think about it."
    show player 13
    show erik f_normal_talk
    eri "Okay."
    show erik f_normal
    karl "HAHAHAAH!"
    show justin a_dressed_neck f_wincing at Position (xpos=400)
    show karl f_embarassed_talk a_dressed_game at Position (xpos=600)
    show erik at flip
    show erik at Position (xpos=100)
    with dissolve
    karl "Dude, that was hilarious!"
    show karl f_embarassed
    show justin f_wincing_talk
    justin "Shut up, {b}Karl{/b}! It wasn't funny!"
    show justin f_wincing
    show karl f_embarassed_talk
    karl "Pfft, hahahaha!!"
    show karl f_embarassed
    show erik f_normal_talk
    eri "What happened?"
    show erik f_normal
    show karl f_embarassed_talk
    karl "Romeo over here confessed his undying love to the {b}Pink Cyclone{/b} and then tried to hug her."
    show karl f_embarassed
    show player 14
    player_name "So, what's funny about that?"
    show player 13
    show karl f_embarassed_talk
    karl "Before he got within two steps she lashed out and put him in a headlock!"
    show karl f_embarassed
    show player 11
    show erik f_surprised
    eri "Really?!"
    show karl f_embarassed_talk
    karl "Haha, yeah and she wouldn't let him go until he apologized!"
    show karl f_embarassed
    show erik f_normal_talk
    eri "You okay, {b}Justin{/b}?"
    show erik f_normal
    show justin f_boasting_talk a_dressed_boasting with dissolve
    justin "Are you kidding?"
    show justin f_wincing_talk a_dressed_neck with dissolve
    justin "I've never been better!"
    show justin f_wincing
    show player 10
    player_name "Huh?"
    show player 5
    show justin f_boasting_talk
    justin "She smelled so good, man!"
    show player 37 with dissolve
    justin "I would have stayed in that headlock all day if they had let me."
    show justin f_boasting
    show player 13
    show karl f_embarassed_talk
    karl "Dude, you almost passed out..."
    show karl f_embarassed
    show justin f_normal_talk
    justin "All part of the act, my friend."
    show justin f_normal
    show karl f_embarassed_talk
    karl "Yeah, right!"
    show karl f_embarassed
    show justin f_normal_talk
    justin "She was crazy strong though!"
    show justin f_normal
    show karl f_normal_talk a_dressed_game_up with dissolve
    karl "Welp, I got my game and my autograph."
    karl "I can't wait to crack this sucker open and PWN some noobs!"
    karl "C'mon, let's go {b}Justin{/b}."
    show karl f_normal a_dressed_game with dissolve
    show justin f_normal_talk
    justin "Yeah okay, I might need to pay my chiropractor a visit..."
    show justin f_normal
    show karl f_normal_talk
    karl "Later, {b}Erik{/b}."
    hide karl
    hide justin
    with dissolve
    show erik f_normal_talk
    eri "Cya online, guys!"
    show erik f_normal
    show player 14
    player_name "I guess we're next, huh?"
    show player 13
    show erik f_normal_talk
    eri "This is going to be awesome!"
    show erik f_normal
    scene black with fade
    pause
    $ player.go_to(L_comicstore)
    scene expression player.location.background_closeup with None
    show player 13 at left
    show erik f_surprised at flip
    show erik at Position (xpos=100)
    show lily f_normal_talk zorder 1 at Position (xpos=600)
    show bridget b_lucha o_mask a_lucha_sides zorder 0 at flip
    show bridget at Position (xpos=400)
    with dissolve
    lily "Are you sure you don't want me to call the cops?"
    show lily f_normal
    show bridget f_normal_talk
    pink "Oh, there's no reason to get the cops involved."
    pink "I took care of it."
    show bridget f_normal
    show lily f_normal_talk
    lily "O-okay."
    show lily f_normal
    show bridget f_normal_talk
    pink "Besides, he's long gone by now."
    pink "How many more copies are left?"
    show bridget f_normal
    show lily f_normal_talk
    lily "Just the one."
    show lily f_normal
    show bridget f_normal_talk
    pink "Good, my time is almost up here."
    show bridget f_normal
    show player 29 with dissolve
    player_name "H-hello?"
    show player 13
    show bridget f_normal_talk a_lucha_hips zorder 2 at unflip
    show bridget at Position (xpos=-100)
    with dissolve
    pink "Nice to mee-"
    show bridget f_surprised
    pause
    show bridget f_angry_talk
    pink "W-what are you two doing here?!"
    show bridget f_angry
    show player 5
    player_name "Hmm?"
    show bridget f_angry_talk
    pink "Did somebody put you up to this? Cause I'm not laughing!"
    show bridget f_angry
    show player 10
    show erik f_faint
    player_name "N-nobody pu-"
    show erik at Position (xpos=-100)
    hide player
    show bridget f_angry_talk a_lucha_hold_mc1
    with dissolve
    pink "You better start talking, right now!"
    show bridget f_angry
    show erik a_dressed_faint with dissolve
    pause
    show erik b_dressed_falling a_empty f_empty with dissolve
    show erik b_dressed_ground with dissolve
    hide erik with dissolve
    show bridget f_surprised
    pink "!!!"
    show bridget a_lucha_hold_mc2
    player_name "W-we just wanted an autograph!"
    show bridget a_lucha_hold_mc1
    pause
    show bridget f_normal_talk a_lucha_sides
    show player 22 at left
    with dissolve
    pink "Oh."
    pink "Sorry about that, I guess, I mistook you for someone else..."
    show bridget f_normal
    show player 10
    player_name "{b}*Gulp*{/b} S-sure, no problem."
    show player 5
    show bridget f_normal_talk
    pink "Is he alright?"
    show bridget f_normal
    show player 10
    player_name "{b}Erik{/b}?"
    show player 184 with dissolve
    pause
    hide player
    show erik b_dressed_pickup a_empty f_empty at flip
    with dissolve
    pause
    show player 5 at left
    show erik b_dressed a_dressed_sides f_woozy_talk at unflip
    show erik at Position (xpos=-300)
    with dissolve
    eri "W-what happened?!"
    show erik f_woozy
    show player 10
    player_name "You fainted, dude."
    show player 5
    show erik f_woozy_talk
    eri "I did?"
    show erik f_woozy a_dressed_faint at flip
    show erik at Position (xpos=100)
    with dissolve
    show lily f_laugh
    lily "Hehe, that's so adorable!"
    show lily f_normal
    show player 13
    show bridget f_normal_talk a_lucha_hips with dissolve
    pink "You boys are big fans, huh?"
    show bridget f_normal
    show erik f_normal_talk a_dressed_sides with dissolve
    eri "Oh, totally!"
    eri "That time you knocked out {b}Lioness{/b} in the royal rumble!"
    eri "Or when you tapped out {b}Rebecca Savage{/b} in that cage match!"
    eri "Oh and your moonsault off the top rope onto-"
    show erik f_normal
    show bridget f_normal_talk
    pink "Okay, okay, I get it..."
    show bridget f_laugh
    pink "Hah, you two really ARE big fans."
    show bridget f_normal
    show erik f_normal_talk
    eri "The BIGGEST!"
    show erik f_normal
    show bridget f_normal_talk
    pink "Well, I've got something special for you two then."
    show bridget f_normal
    show erik f_normal_talk
    eri "R-really?!"
    show erik f_normal
    show bridget f_empty a_empty o_empty b_lucha_bend with dissolve
    pink "Mmhmm."
    show bridget f_normal_talk o_mask a_lucha_poster b_lucha with dissolve
    pink "Here you go."
    show bridget f_normal a_lucha_poster_show with dissolve
    show erik f_surprised
    eri "WHOA!!!"
    show player 735
    show bridget a_lucha_hips
    show erik f_normal_talk a_dressed_poster
    with dissolve
    eri "{b}Justin{/b} is going to be so jealous..."
    eri "This is like, the coolest thing ever!"
    show erik f_normal
    show player 14 with dissolve
    player_name "Thank you, miss... Uhh, {b}Pink Cyclone{/b}."
    show player 13
    show bridget f_normal_talk
    pink "You're very welcome, boys."
    show bridget f_normal_talk zorder 0 at flip
    show bridget at Position (xpos=400)
    pink "Now, unless there's anything else?"
    pink "I should really head out."
    show bridget f_normal
    show lily f_normal_talk
    lily "Nope, you've already done so much."
    show lily a_casual_mask_point with dissolve
    lily "These replica masks are going to be a huge hit with our cosplay community!"
    show player 11
    lily "I might even grab one for myself."
    show lily f_normal a_casual_sides with dissolve
    show bridget f_normal_talk
    pink "Oh, you'll have to e-mail me a picture of that."
    show bridget f_normal
    show lily f_laugh
    lily "Will do!"
    show lily f_normal
    show player 29 with dissolve
    player_name "E-excuse me?"
    show bridget at unflip
    show bridget at Position (xpos=-90)
    player_name "A-are you selling those?"
    show player 3
    show lily f_normal_talk
    lily "Yup, starting today, {b}you can pick one of these up{/b} from our {b}Cosplay Section{/b}."
    show lily f_normal
    show player 4 with dissolve
    player_name "( Hmm, I bet that would work for {b}[jen_name]'s camshows{/b}... )"
    show bridget b_empty a_empty f_lily_lucha_hug_normal o_lily_lucha_hug_mask zorder 2 at Position (xpos=87,yoffset=1)
    show lily b_hug a_empty f_bridget_hug_normal_talk at Position (yoffset=18)
    with dissolve
    show player 13
    lily "Thanks again for coming out."
    show lily f_bridget_hug_normal at Position (yoffset=18)
    show bridget f_lily_lucha_hug_normal_talk at Position (yoffset=1)
    pink "My pleasure, sweetie."
    hide bridget
    show bridget f_normal_talk b_lucha a_lucha_hips o_mask
    hide lily
    with dissolve
    pink "I'll see you two at schoo-"
    show bridget f_surprised
    show player 10
    player_name "Huh?"
    show player 5
    show bridget f_normal_talk a_lucha_rubbing_hands with dissolve
    pink "I err, meant to say..."
    pink "Stay in school!"
    show bridget f_laugh
    pink "Heh, you know... Don't be a fool, stay in school!"
    show bridget f_normal_talk
    pink "That's what... I was..."
    pink "I'll just... Goodbye boys."
    hide bridget with dissolve
    show erik f_normal_talk
    eri "Bye, {b}Pink Cyclone{/b}!"
    show erik f_normal at unflip
    show erik at Position (xpos=-100)
    with dissolve
    show player 10
    player_name "That was weird."
    show player 13
    show erik f_normal_talk
    eri "That was awesome!"
    eri "Check out this poster, dude!"
    eri "She's so hot!"
    show erik f_normal
    show player 14
    player_name "Heh, yeah."
    show player 13
    show erik f_normal_talk
    eri "Alright, time to snag that last copy of the game."
    show erik f_normal
    show player 14
    player_name "Heh, you'd better hurry."
    hide erik with dissolve
    show player 4 with dissolve
    player_name "( Hmm. )"
    player_name "( I should see about {b}buying{/b} one of those {b}replica masks{/b} for {b}[jen_name]'s camshows{/b}. )"
    hide player with dissolve
    $ player.go_to(L_comicstore)
    $ M_jenny.trigger(T_jenny_buy_mask)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
