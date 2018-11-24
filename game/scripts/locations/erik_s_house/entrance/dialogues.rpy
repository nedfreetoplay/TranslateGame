label erikentrance_erik_gf_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14 at left
    show june 2 at Position (xpos=700)
    show erik 1 at right
    with dissolve
    player_name "Oh, hey guys!"
    show player 1
    show erik 4
    eri "Hey, {b}[firstname]{/b}!"
    show june 3
    show erik 1
    june "Hi!"
    show player 14
    show june 2
    player_name "I didn't know you two were already hanging out!"
    show player 1
    show erik 4
    eri "Yeah, we've been playing Ork Bork a lot..."
    show erik 1
    show june 6
    june "Ha ha. Yeah, we're totally addicted!"
    show june 2
    show player 14
    player_name "So, you two have been getting along fine, huh?"
    show player 1
    show erik 4
    eri "Yeah, actually we have to do something... in my err... room."
    show erik 1
    show player 11
    show june 3
    june "Yeah we have to, uhm... look over something?"
    show player 14
    show june 2
    player_name "Oh... I see!"
    show player 17
    player_name "It's alright, I'll come over another time then."
    show player 14
    player_name "I'll see you guys later!"
    show player 1
    show erik 4
    eri "Later, man."
    hide player
    hide june
    hide erik
    with dissolve
    return

label erikentrance_erik_sex_ed_block:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14
    with dissolve
    player_name "I should go see if {b}Erik{/b} is in his room..."
    hide player with dissolve
    return

label erikentrance_mrsj_poker_night_over:
    scene expression game.timer.image("erik_inside{}_b")
    show mrsj 17 at right
    show player 1 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!"
    show player 11
    mrsjo "Can I have a quick word with you before you go see {b}Erik{/b}?"
    show mrsj 14
    show player 14
    player_name "Sure, {b}Mrs. Johnson{/b}."
    show mrsj 20
    show player 11
    mrsjo "I... I don't remember much of last night."
    show mrsj 19
    mrsjo "Whatever happened, I want to apologize."
    show player 13
    mrsjo "I drank too much, and I shouldn't have done those things with you boys."
    show mrsj 19c
    show player 10
    player_name "Oh, it's fine, {b}Mrs. Johnson{/b}..."
    show mrsj 19
    show player 13
    mrsjo "You don't resent me, right?"
    show mrsj 19c
    show player 14
    player_name "Of course not."
    player_name "I think it was fun!"
    show mrsj 19
    show player 1
    mrsjo "What about {b}Erik{/b}?"
    mrsjo "Did he have fun too?"
    show player 14
    show mrsj 14
    player_name "I... I think so?"
    show mrsj 17
    show player 1
    mrsjo "Well... as long as you boys didn't find it too strange..."
    show mrsj 19c
    show player 14
    player_name "Did you talk to him about it?"
    show mrsj 19
    show player 11
    mrsjo "No! God no."
    show mrsj 20
    mrsjo "I don't want to make this more awkward than it already is."
    show mrsj 19
    mrsjo "But... Could you do me a favour and talk to him about it?"
    mrsjo "I just want to make sure he's not mad at me about it."
    show mrsj 14
    show player 14
    player_name "Sure, {b}Mrs. Johnson{/b}. I'll talk to him."
    show mrsj 18
    show player 1
    mrsjo "Thanks, you're so sweet."
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_sex_ed:
    scene erik_house_upstairs_night_c01
    show erik 5f at Position (xpos=300)
    show player 13 at left
    show mrsj 14 at right
    with dissolve
    eri "Hi, {b}Mrs. Johnson{/b}!"
    eri "You...needed something from us?"
    show erik 1f
    show mrsj 19
    mrsjo "Listen, boys."
    mrsjo "I know you two have been talking about this, so..."
    mrsjo "I've thought this over, and since you two are okay with this..."
    show mrsj 49
    mrsjo "I'll agree to give you two private...sex education lessons."
    show mrsj 50
    show player 23
    player_name "!!!"
    show erik 5f
    eri "M...{b}Mrs. Johnson{/b}, are you sure?"
    show erik 1f
    show mrsj 49
    show player 18
    mrsjo "Of course, pumpkin!"
    mrsjo "I don't have a problem with it, as long as this stays between us!!"
    show mrsj 50
    show player 14
    player_name "I...I don't have a problem with that, {b}Mrs. Johnson{/b}..."
    show player 11
    show mrsj 52
    mrsjo "But!!" with hpunch
    mrsjo "Before we start with these lessons... I'll need something from you two."
    show player 5
    show mrsj 14
    show erik 4f
    eri "What do you need, {b}Mrs. Johnson{/b}?"
    show erik 1f
    show mrsj 19
    show player 13
    mrsjo "...I've actually never had sex with two guys before."
    show mrsj 49
    mrsjo "I'd like a book that shows sexual positions for more than two partners."
    mrsjo "I've heard a book called {b}Karma Sutra{/b} describes ancient eastern positions."
    mrsjo "See if you can find me that book."
    show mrsj 52
    mrsjo "And there's one more thing..."
    show mrsj 14
    show erik 5f
    eri "Oh, yeah?"
    show erik 1f
    show mrsj 49
    mrsjo "Well, if we're going to have sex, I have to make sure I don't get pregnant!"
    show mrsj 50
    player_name "..."
    show mrsj 49
    mrsjo "I'll have to take {b}birth control pills{/b}..."
    show mrsj 50
    show erik 5f
    eri "Can't we use condoms?"
    show erik 1f
    show mrsj 52
    mrsjo "Even with condoms, there's always a risk!!"
    show mrsj 49
    mrsjo "And if I use the pill, we can do it raw..."
    show mrsj 50
    show player 83
    show erik 58f
    player_name "!!!"
    show player 82
    show mrsj 20
    pause
    mrsjo "..."
    show mrsj 18
    mrsjo "Ha ha!"
    show player 81
    player_name "!!!" with hpunch
    show player 78
    show mrsj 49
    mrsjo "I can see you two are very excited about starting those sex lessons with me..."
    show mrsj 50
    show erik 56f
    eri "Sorry, {b}Mrs. Johnson{/b}."
    show erik 57f
    show mrsj 49
    mrsjo "It's fine, pumpkin."
    show player 80
    mrsjo "The sooner you two help me get what I need, the sooner we can start!"
    show mrsj 50
    show erik 58f
    eri "Okay, {b}Mrs. Johnson{/b}!"
    show erik 57f
    show player 83
    player_name "We will find you what you need, {b}Mrs. Johnson{/b}!"
    hide player
    hide mrsj
    hide erik
    with dissolve
    scene black with fade
    pause
    scene expression game.timer.image("erik_entrance{}_c")
    show erik 4 at right
    show player 13 at left
    with dissolve
    eri "I can't believe {b}Mrs. Johnson{/b} is okay with having sex with us..."
    show erik 1
    show player 17
    player_name "I think we're lucky..."
    show player 13
    show erik 3
    eri "I've never had sex before..."
    show erik 3c
    show player 14
    player_name "Well, {b}Mrs. Johnson{/b} plans on teaching us how. And it's going to be awesome!"
    show player 13
    show erik 5
    eri "But how are we going to get that stuff she asked for?"
    show erik 1
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "I think I got an idea."
    show player 13
    show erik 5
    eri "Oh, yeah?"
    show erik 1
    show player 14
    player_name "I'm sure the {b}hospital has the pills Mrs. Johnson{/b} talked about..."
    show player 33
    player_name "And we can always find the {b}Kama Sutra book at the library{/b}!"
    show player 13
    show erik 5
    eri "I hope you're right."
    show erik 1
    show player 14
    player_name "I'll come back when I find something..."
    hide player
    hide erik
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ erik.complete_events(erik_sex_ed)
    $ mrsj.add_event(mrsj_sex_ed)
    $ M_erik.place(place = L_erikhouse_erikroom)

    $ game.main()

label mrsj_sex_ed_2:
    scene erik_house_upstairs_night_c01
    show erik 4f at Position (xpos=300)
    show player 13 at left
    show mrsj 14 at right
    with dissolve
    eri "Hey, {b}Mrs. Johnson{/b}."
    show erik 1f
    show mrsj 17
    mrsjo "Hi, boys!"
    mrsjo "How are you two doing?"
    show mrsj 14
    show erik 4f
    eri "We found some things that may help you...with our lessons."
    show erik 1f
    show player 239_240 with dissolve
    pause
    show player 425 with dissolve
    player_name "Here's what I found, {b}Mrs. Johnson{/b}!"
    show player 13
    show mrsj 63
    with dissolve
    mrsjo "Oh, wonderful!"
    mrsjo "I'll have to prepare for our little lessons together..."
    mrsjo "Maybe you two should visit me at night in my room...Or, should I call it, our classroom!"
    mrsjo "Ha ha."
    hide player
    hide mrsj
    hide erik
    with dissolve
    scene black with fade
    pause
    scene expression game.timer.image("erik_entrance{}_c")
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "When should we visit {b}Mrs. Johnson{/b}?"
    show erik 1
    show player 14
    player_name "I'll try and stop back over as soon as I can..."
    player_name "But you should do it with her whenever you want!"
    show player 13
    show erik 4
    eri "I guess you're right..."
    eri "Thanks for helping me with this, {b}[firstname]{/b}."
    hide player
    hide erik
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ player.remove_item("kamasutra")
    $ player.remove_item("birth_control_pills")
    $ mrsj_sex_ed.finish()
    $ M_mrsj.unforce()
    $ M_erik.unforce()
    $ M_erik.set_default_locations([[L_school_scienceclassroom, L_school_cafeteria, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom],
                                    [L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom]])
    $ game.main()

label erik_breastfeeding:
    scene erik_house_cs01_01b with fade
    show text "This was the first time I had ever been in {b}Mrs. Johnson{/b}'s room.\nI knew her and {b}Erik{/b} had an unusual relationship...\nI didn't expect to see him... breastfeeding..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene erik_house_cs02 with fade
    show text "The look on their faces said everything...\n...I was not supposed to be there. Everything would've been fine...\n...If only I had knocked first.\nInstinctively, I closed the door and decided I should leave." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene expression game.timer.image("erik_entrance{}_c")
    show player 22 at left with dissolve
    show erik 2 at Position (xpos=750)
    show mrsj 52 at right
    with dissolve
    mrsjo "{b}[firstname]{/b}?!"
    mrsjo "I... What are doing here?"
    show mrsj 38
    show player 37 with dissolve
    player_name "{b}Erik{/b}?!"
    show erik 3b with dissolve
    player_name "I... um... was just trying to find you."
    show player 24 with dissolve
    show erik 3
    eri "{b}[firstname]{/b}..."
    show erik 2 with dissolve
    show player 25
    player_name "I heard voices and I thought..."
    show player 11
    show erik 3b
    eri "I...I just want to be in my room right now."
    show erik 2
    show mrsj 19b
    mrsjo "It's fine I-"
    hide erik with dissolve
    show mrsj 19c
    show player 22
    mrsjo "..."
    show mrsj 20
    mrsjo "Listen, what you saw just now is something... normal!"
    show player 5
    show mrsj 19
    mrsjo "I'm just trying to get him out of his shell, {b}[firstname]{/b}."
    show mrsj 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}."
    player_name "I didn't mean to walk in on you guys like that..."
    show player 5
    pause
    show player 10
    player_name "Can you just tell {b}Erik{/b} that I'm sorry?"
    show player 5
    show mrsj 19
    mrsjo "Don't worry about him. He'll be fine..."
    mrsjo "It's just... {b}Erik{/b} doesn't seem to see or talk about many girls, so I try and..."
    show player 11
    mrsjo "...I give him a little womanly attention!"
    mrsjo "I thought I could get him off his computer if he could just... have a little taste!"
    show mrsj 19c
    show player 5
    player_name "..."
    show mrsj 19
    mrsjo "Can you just... you know. Keep this between us?"
    mrsjo "I don't think he would want the other kids at school to find out."
    show mrsj 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}. I won't tell anyone."
    hide player
    hide mrsj
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ erik.complete_events(erik_breastfeeding)
    $ erik.add_event(erik_breastfeeding_2)
    $ erik_breastfeeding_2.finish()
    $ M_erik.unforce()

    $ game.main()

label mrsj_room_locked_dialogue:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Oops! {b}Mrs. Johnson{/b} must be keeping her door locked..."
    hide player with dissolve
    $ game.main()

label mrsj_filled_block:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10
    with dissolve
    player_name "I should let {b}Mrs. Johnson{/b} rest."
    player_name "Besides, I don't think I can handle two of those lessons in one day..."
    hide player with dissolve
    $ game.main()

label eriks_house_intro:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 1 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Hello, {b}[firstname]{/b}!"
    show mrsj 14
    show player 36 with dissolve
    player_name "Hi, {b}Mrs. Johnson{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "It's been a while since your last visit!"
    show mrsj 14
    show player 10
    player_name "Yeah, I've been a bit busy lately."
    player_name "Catching up in school and saving money for tuition."
    show player 13
    show mrsj 17
    mrsjo "It's nice to hear of a young man, such as yourself, acting so responsibly."
    show mrsj 49
    mrsjo "Just make sure you save yourself some time to chase after girls, Honey."
    show mrsj 50
    show player 21
    player_name "Yeah, okay..."
    show player 13
    pause
    show mrsj 17
    mrsjo "Well, It's good to see you again!"
    show mrsj 18
    mrsjo "You're probably here to see {b}Erik{/b}, not little ol' me."
    show mrsj 17
    mrsjo "It's been so quiet around here..."
    show mrsj 14
    show player 10
    player_name "What do you mean?"
    show player 5
    show mrsj 19
    mrsjo "Well, {b}Erik{/b} doesn't get many visitors and you seem to be his only friend."
    show mrsj 17
    show player 13
    mrsjo "I want you to know that you're always welcome in this house. Day or night."
    show mrsj 49
    mrsjo "You and {b}Erik{/b} are good kids."
    show mrsj 50
    show player 2
    player_name "Thanks, {b}Mrs. Johnson{/b}."
    show player 13
    pause
    show player 12
    player_name "Where is {b}Erik{/b} anyways?"
    show player 5
    show mrsj 17
    mrsjo "I think I saw him just a bit ago. He was making a rare appearance outside his room!"
    mrsjo "He's in the basement right now."
    return

label erikentrance_erik_thief_2_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14 at left
    show erik 1 zorder 1 at right
    with dissolve
    player_name "Hey, {b}Erik{/b}."
    show erik 4
    show player 1
    eri "Hey, did you find anyone?"
    show erik 1
    show player 10
    player_name "Not much so far, everyone is either busy or just doesn't want to come over."
    show erik 5
    show player 11
    eri "Even {b}Mia{/b}?"
    show erik 1
    show player 10
    player_name "I think she's busy with homework."
    show erik 3
    show player 5
    eri "Aww man, who else is gonna play cards with us?"
    show player 1
    show erik 1b at Position(xpos=870)
    show mrsj 17b zorder 2 at right
    with dissolve
    mrsjo "Is something wrong, pumpkin?"
    show erik 4b
    show mrsj 14b
    eri "Oh, it's nothing, {b}Mrs. Johnson{/b}."
    show erik 1b
    show mrsj 18
    mrsjo "Oh, come on! I heard you guys talking about inviting friends over."
    show erik 5b
    show mrsj 14b
    eri "Well, we can't find anyone to play Poker with us."
    show erik 1b
    show mrsj 17
    mrsjo "Ooh, that sounds fun!"
    show erik 5b
    show mrsj 14b
    eri "It would be more fun if we had other players..."
    show erik 1b
    show player 11
    show mrsj 17
    mrsjo "What about me?"
    show player 13
    show mrsj 18
    mrsjo "I'd like to play..."
    show player 1
    show erik 4b
    show mrsj 14b
    eri "Really?"
    show erik 1b
    show mrsj 17
    mrsjo "Yeah! It's not fair that a couple of good boys like you can't find someone to play with..."
    mrsjo "Tell you what, if you need another player, let me know, I'm always up for a nice poker night!"
    show erik 1
    show player 14
    show mrsj 14
    player_name "That sounds awesome!"
    show player 17
    player_name "Thanks, {b}Mrs. Johnson{/b}."
    show player 1
    show erik 1 at right
    hide mrsj
    with dissolve
    pause
    show player 14
    player_name "Dude!! I can't believe {b}Mrs. Johnson{/b} is going to play with us."
    show erik 4
    show player 1
    eri "Well, I guess we found someone..."
    hide player
    hide erik
    with dissolve
    return

label erikentrance_erik_thief_over:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 19 at right
    show player 13 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!"
    mrsjo "I just wanted to say thank you so much for, you know, protecting us."
    show mrsj 20
    mrsjo "It's pretty embarrassing you had to see my ex husband like that..."
    show mrsj 19c
    show player 33
    player_name "I just wanted to make sure you didn't get your house broken into."
    show player 13
    show mrsj 17
    mrsjo "I'm lucky to have such a wonderful neighbor..."
    show mrsj 14
    show player 17
    player_name "Oh, thanks!"
    show player 13
    show mrsj 49
    mrsjo "I should... reward you with something special, for what you've done for us..."
    show mrsj 50
    show player 4 with dissolve
    player_name "..."
    show player 29 with dissolve
    player_name "Uhh, you don't have to, {b}Mrs. Johnson{/b}!"
    show player 13 with dissolve
    show mrsj 49
    mrsjo "Oh, no. I insist!"
    mrsjo "I'll think of something and I'm sure you're going to like it..."
    show mrsj 50
    show player 17
    player_name "Ha ha, alright."
    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_mrsj_yoga_2_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "( It's quiet, is anyone home? )"
    player_name "( Maybe {b}Erik{/b} is in his room. )"
    show player 17
    player_name "( I hope he's not sleeping... or doing something else. )"
    hide player with dissolve
    return

label erikentrance_mrsj_yoga_2_started:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 17 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!!"
    mrsjo "How did your first time instructing a yoga class go?"
    show mrsj 14
    show player 14
    player_name "I think I did ok?"
    show player 13
    show mrsj 17
    mrsjo "Was {b}Anna{/b} able to help you?"
    show mrsj 14
    show player 14
    player_name "Yeah, she was there."
    player_name "She is really good at yoga..."
    show player 17
    player_name "...and flexible!"
    show player 13
    show mrsj 18
    mrsjo "Ha ha ha!"
    show mrsj 49
    mrsjo "{b}Anna{/b} can get into any position I put her in."
    mrsjo "I've had her twisted up like a pretzel, once."
    show mrsj 50
    show player 12
    player_name "Really?"
    show player 11
    show mrsj 49
    mrsjo "Oh yeah. She's very good in tight... situations."
    mrsjo "And a little baby oil doesn't hurt either..."
    show mrsj 50
    show player 13
    player_name "..."
    show mrsj 19
    mrsjo "Umm... Anyway, so you think you'd do it again?"
    show mrsj 14
    show player 14
    player_name "Well, she invited me to do more yoga with her at the gym at night."
    show player 13
    show mrsj 18
    mrsjo "You should go!"
    show mrsj 49
    mrsjo "{b}Anna{/b} can teach you a lot of things..."
    show mrsj 50
    show player 17
    player_name "I'm sure, ha ha."
    show player 13
    show mrsj 19
    mrsjo "Thank you for helping me. Again."
    show mrsj 17
    mrsjo "And don't think I've forgot how much you've done for {b}Erik{/b} and me."
    show mrsj 49
    mrsjo "I owe you... a lot."
    show mrsj 50
    show player 33
    player_name "Don't worry about it. It's no problem."
    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_erik_vr_over:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 13 at left
    with dissolve
    mrsjo "Oh, good!"
    show mrsj 19
    mrsjo "{b}[firstname]{/b}, I hate to bother you, but are you available tonight?"
    show mrsj 19c
    show player 10
    player_name "Huh?"
    show player 11
    show mrsj 19
    mrsjo "I need someone to go and teach my yoga class for me tonight. I have another appointment I need to attend."
    show mrsj 14
    show player 12
    player_name "Me?!"
    show player 5
    show mrsj 49
    mrsjo "Do you think you could help your... favorite neighbor??"
    show mrsj 50
    show player 38 with dissolve
    player_name "Uhh... I... guess I could try?"
    show player 29 with dissolve
    player_name "But I don't know much about yoga..."
    show player 11 at left with dissolve
    show mrsj 17
    mrsjo "It's a beginners class!"
    mrsjo "You'll do fine!"
    show mrsj 57 with dissolve
    mrsjo "Here is a list of the yoga moves to do in front of the class."
    show mrsj 58
    pause
    show mrsj 14
    show player 386
    with dissolve
    player_name "Thanks."
    show player 380
    pause
    show player 384
    player_name "Umm... These moves look pretty complicated..."
    show player 385
    show mrsj 17
    mrsjo "My friend {b}Anna{/b} will be there to assist you during the class."
    show mrsj 18
    mrsjo "She's my little eager beaver. Always willing to help and to please."
    show mrsj 14
    show player 386
    player_name "Oh. Okay... I'll try my best."
    show player 385
    show mrsj 49
    mrsjo "You're so sweet. I'll make sure to pay you back one day!"
    show mrsj 17
    mrsjo "I gotta go, so study those moves!"
    mrsjo "Bye!"
    show mrsj 14
    show player 386
    player_name "Bye, {b}Mrs. Johnson{/b}."
    show player 385
    hide mrsj with dissolve
    return

label erikentrance_erik_orcette_completed:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 375 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Hello, {b}[firstname]{/b}!"
    mrsjo "Are you looking for {b}Erik{/b}?"
    show mrsj 14
    show player 377
    player_name "!!!"
    show player 376
    player_name "H... Hi, {b}Mrs. Johnson{/b}."
    show player 378
    mrsjo "..."
    show mrsj 17
    mrsjo "So, what're you two up to..."
    show mrsj 14
    show player 376
    player_name "Oh, nothing!"
    show player 377
    show mrsj 49
    mrsjo "What is it that you're holding anyway?"
    mrsjo "Something new you and {b}Erik{/b} are going to play with, huh?"
    show mrsj 50
    player_name "!!!"
    show player 379
    player_name "Uh.... Yeah something like that."
    show player 377
    show mrsj 17
    mrsjo "I just love surprises! What is it? It has to be some new game."
    mrsjo "That's all {b}Erik{/b} does these days..."
    show mrsj 14
    show player 379
    player_name "Yeah... Um... It's not... Well..."
    show player 377
    show mrsj 17
    mrsjo "Let me see!"
    show player 23 with dissolve
    show mrsj 43 with dissolve
    player_name "Wait!"
    show player 22
    mrsjo "!!!"
    show mrsj 44
    mrsjo "What... is it?"
    show mrsj 46
    show player 10
    player_name "It's..."
    show player 11
    show mrsj 43
    mrsjo "Is this one of those fake sex things they advertise online?"
    show mrsj 46
    show player 10
    player_name "Uh..."
    show player 24
    show mrsj 44
    mrsjo "Did {b}Erik{/b} put you up to this?"
    mrsjo "I've seen it flash across his computer screen when I entered his room one time."
    show mrsj 46
    show player 25
    player_name "No. No. It's... Um... Mine."
    show player 24
    player_name "I... Uh... Was going to... Just show him?"
    show mrsj 45
    mrsjo "Ha ha."
    mrsjo "Boys and their toys!"
    show mrsj 46
    player_name "..."
    show player 25
    show mrsj 44
    mrsjo "Oh Honey... It's alright!"
    mrsjo "Young men exploring their sexuality is a good thing!"
    mrsjo "Maybe seeing your new toy will motivate him to... get out of his room?"
    mrsjo "The real thing is... even better, young man."
    show mrsj 46
    show player 22
    player_name "{b}*Gulp*{/b}"
    show mrsj 44
    mrsjo "{b}Erik{/b} is upstairs, Honey."
    mrsjo "Oh, and make sure to use lube with that thing."
    mrsjo "You don't want to get friction burns on your... parts."
    hide mrsj with dissolve
    show player 377 with dissolve
    pause
    show player 376
    player_name "( Wow... I thought she was going to be disgusted at me for this... )"
    player_name "( But she seemed pretty cool about it? )"
    player_name "( {b}Erik{/b} sure is lucky he ended up here... )"
    return

label erikentrance_mrsj_intro_started_day:
    mrsjo "Anyway, I should probably get going."
    show player 13
    mrsjo "I have to teach yoga lessons in the afternoon down at the gym."
    mrsjo "I've got some new students and I'd better hurry up so I'm not late!"
    show mrsj 14
    show player 14
    player_name "Okay, have fun!"
    show player 13
    show mrsj 17
    mrsjo "You too! Tell {b}Erik{/b} I'll be back with dinner and not to eat too many sweets."
    show mrsj 49
    mrsjo "I want him nice and hungry for me tonight!"
    return

label erikentrance_mrsj_intro_started_night:
    show mrsj 18
    mrsjo "Well, it's getting a bit late for me."
    show mrsj 17
    show player 13
    mrsjo "I'm off to bed, so you have fun. But remember to keep the volume to a respectable level if you play some video games."
    show mrsj 14
    show player 14
    player_name "Will do. Have a good night {b}Mrs. Johnson{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
