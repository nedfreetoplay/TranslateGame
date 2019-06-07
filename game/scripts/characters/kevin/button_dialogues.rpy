label button_kevin_shift_cover_has_favor:
    show kevin 2
    kev "You {b}talk with Erik about covering for me{/b} yet?"
    show kevin 1
    show player 17
    player_name "I did."
    player_name "He's gonna do it."
    show player 13
    show kevin 2b with dissolve
    kev "HELL!"
    kev "YEAH!"
    kev "BRO!"
    show kevin 2c with dissolve
    kev "You are the freaking man!"
    show kevin 6 with dissolve
    kev "Finally I can get back to my two-a-days!"
    show kevin 5
    show player 14
    player_name "Heh, so I guess I'll see you at the gym in the {b}Morning{/b}?"
    show player 13
    show kevin 9b with dissolve
    kev "You know it, bro!"
    hide kevin
    hide player
    with dissolve
    return

label button_kevin_shift_cover_no_favor:
    show kevin 2
    kev "You {b}talk with Erik about covering for me{/b} yet?"
    show kevin 1
    show player 29 with dissolve
    player_name "No, not yet."
    show player 3
    show kevin 2
    kev "Ugh, you gotta hurry, bro!"
    show kevin 2b with dissolve
    kev "My muscles are wasting away in here!"
    show kevin 1 with dissolve
    show player 14 with dissolve
    player_name "Heh, just relax."
    player_name "I'll talk with him."
    show player 13
    return

label button_kevin_cafeteria_duty_repeat:
    show player 14
    player_name "You any closer to getting out of here?"
    show player 13
    show kevin 2
    kev "Hell no."
    kev "I'm gonna be stuck in here all semester, I just know it!"
    show kevin 1
    return

label button_kevin_cafeteria_duty_first:
    show player 14
    player_name "How much longer are you stuck doing this?"
    show player 13
    show kevin 2d with dissolve
    kev "{b}*Sigh*{/b} Until I get my science grade up, bro..."
    kev "Honestly, it could take all semester."
    show kevin 2e
    show player 14
    player_name "Seriously?"
    show player 13
    show kevin 2d
    kev "Yeah."
    show kevin 2e
    show player 14
    player_name "That does suck man."
    player_name "I need you at the gym to spot me."
    show player 13
    show kevin 2 with dissolve
    kev "Ah, don't get me all depressed..."
    kev "You know I wanna be in there helping my bro get ripped!"
    show kevin 1
    pause
    show kevin 4
    kev "Tsk, you know what..."
    show kevin 2
    kev "I wonder if I could sneak outta here?"
    show kevin 1
    show player 5
    player_name "Hmm?"
    show kevin 2
    kev "I mean, if we could {b}find someone to cover for me{/b}..."
    kev "... Like in the mornings."
    kev "It could totally work, bro!"
    show kevin 1
    show player 10
    player_name "What do you mean?"
    show player 5
    show kevin 2
    kev "Well, {b}Mrs. Smith{/b} never comes in here in the morning."
    kev "So as long as the work got done, it wouldn't really matter who was doing it."
    show kevin 1
    show player 14
    player_name "So we just need to {b}find someone to cover for you{/b}?"
    show player 13
    show kevin 2
    kev "Yeah, you got any ideas?"
    show kevin 1
    show player 4
    pause
    show player 14
    player_name "Hmm, I might be able to convice {b}Erik{/b} to do it."
    show player 13
    show kevin 2
    kev "Oh, that would be awesome, bro!"
    show kevin 1
    show player 14
    player_name "I'll {b}ask him{/b} about it."
    show player 13
    show kevin 2
    kev "Hell yeah!"
    show kevin 1
    return

label button_kevin_intro_pre_favor:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 2 at right
    with dissolve
    kev "Sup, bro?!"
    show kevin 1
    show player 14
    player_name "Hey, {b}Kevin{/b}."
    show player 13
    show kevin 2
    kev "You here to scrub some pots?"
    show kevin 1
    show player 17
    player_name "Heh, no way man!"
    show player 13
    show kevin 2
    kev "Ugh, this cafeteria duty sucks dick, bro!"
    show kevin 1
    pause
    show kevin 2
    kev "... And not the cool kind, either."
    show kevin 1
    show player 29 with dissolve
    player_name "Eh, right..."
    show player 5 with dissolve
    return

label button_kevin_used_panties_repeat:
    show player 10
    player_name "I can't believe this guy has me stealing {b}used panties{/b}..."
    show player 5
    show kevin magic 2
    kev "It's not that big a deal, bro!"
    kev "Just swipe a pair from home."
    show kevin magic 1
    show player 37 with dissolve
    player_name "Yeah, yeah."
    player_name "I'll {b}check around my house{/b} and see if I can find a pair of {b}[deb_name]'s{/b} or {b}[jen_name]'s{/b}."
    show player 13 with dissolve
    return

label button_kevin_used_panties_first:
    show player 10 at left
    show kevin magic 1 at right
    player_name "So I met that new {b}Muay Thai{/b} trainer you were going on about."
    show player 5
    show kevin magic 2
    kev "Right on, bro!"
    kev "He's pretty awesome, right?!"
    show kevin magic 1
    show player 12
    player_name "He's a total crackpot!"
    show player 5
    show kevin magic 2
    kev "Huh?"
    show kevin magic 1
    show player 12
    player_name "Yeah, he said he won't teach me unless I bring him {b}used panties{/b}!"
    show player 5
    show kevin magic 2
    kev "Oh, that..."
    show kevin magic 3 with dissolve
    kev "Umm."
    show kevin magic 4
    show player 10
    player_name "Wait a second..."
    show player 14
    player_name "You brought him a pair, didn't you?!"
    show player 13
    show kevin magic 3
    kev "Eh, yeeeeah."
    show kevin magic 4
    show player 14
    player_name "Dude, seriously?"
    show player 13
    show kevin magic 2 with dissolve
    kev "Well, I heard all this awesome stuff about him and I was curious..."
    kev "Once you get past the panties thing, he's like totally legit!"
    show kevin magic 1
    show player 11
    player_name "..."
    show kevin magic 2
    kev "I'm serious!"
    kev "He really knows his shit, bro."
    show kevin magic 1
    show player 14
    player_name "Where did you get a pair of {b}used panties{/b}?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Oh, eh... I kinda... Snatched a pair of {b}my mom's{/b}, outta the dirty clothes basket."
    show kevin magic 4
    show player 12
    player_name "Dude..."
    show player 5
    show kevin magic 2 with dissolve
    kev "What?!"
    kev "It's not THAT weird."
    kev "I just took one pair and it's not like I was taking them for me."
    kev "I gave them to {b}Master Somrak{/b}."
    show kevin magic 1
    show player 14
    player_name "It's pretty weird {b}Kevin{/b}."
    show player 13
    show kevin magic 2
    kev "Nah, bro."
    kev "You're getting hung up on trivial stuff..."
    kev "You've got a couple girls at your house don't you?"
    show kevin magic 1
    show player 10
    player_name "Yeah but-"
    show player 11
    show kevin magic 2
    kev "Well, there ya go! Just snag one pair and you're in!"
    kev "It's really not a big deal, bro."
    show kevin magic 1
    show player 35
    player_name "Hmm, I dunno..."
    show player 34
    show kevin magic 2
    kev "Just do it, {b}[firstname]{/b}."
    kev "{b}Master Somrak's{/b} teachings will change your life, I'm telling ya!"
    show kevin magic 1
    show player 33
    player_name "I guess I could take one pair..."
    show player 13
    show kevin magic 2
    kev "See, there ya go!"
    show kevin magic 1
    show player 14
    player_name "I'll {b}check around my house{/b} and see if I can find a pair of {b}[deb_name]'s{/b} or {b}[jen_name]'s{/b} panties."
    show player 13
    return

label kevin_dialogue_ross_find_magazines:
    show player 2 at left
    show kevin 29b at right
    with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 1
    show kevin 30
    kev "What's up, {b}[firstname]{/b}?"
    show player 2
    show kevin 29b
    player_name "Not much. What are you reading?"
    show player 1
    show kevin 30b
    kev "Oh, just some work out magazines I got from the gym."
    show player 2
    show kevin 29b
    player_name "Cool, you trying a new work out or something?"
    show player 1
    show kevin 30
    kev "No, why?"
    show player 11
    show kevin 29
    player_name "..."
    show kevin 31 with dissolve
    kev "Come check out this beefcake, {b}[firstname]{/b}!"
    show player 10
    show kevin 31b
    player_name "... beefcake?"
    show player 11
    player_name "..."
    show player 10
    player_name "Uh, right... You think, I could take some of these magazines?"
    show player 11
    show kevin 30 with dissolve
    kev "Heh, I didn't know you were a fellow connoisseur of the masculine form..."
    show player 10
    show kevin 29
    player_name "Actually, I'm making a collage."
    show player 11
    show kevin 30b
    kev "Oh, right. Collage."
    show kevin 31 with dissolve
    kev "I gotcha, Bro! Say no more!"
    kev "Take all you need! This one will keep me busy for awhile."
    show player 2
    show kevin 31b
    player_name "Awesome! Thanks, uhh, Bro..."
    show player 1
    show kevin 31c
    kev "Daaaamn, he's glistening..."
    show player 10
    player_name "..."
    return

label kevin_dialogue_ross_ask_model:
    show player 2 at left
    show kevin 1 at right
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show kevin 2
    show player 1
    kev "Modeling. Like I just have to stand there?"
    show player 2
    show kevin 1
    player_name "Yeah, you just have to stand there."
    show player 10
    player_name "Naked."
    show kevin 3
    show player 11
    kev "Naked!?"
    kev "Oh, man. I dunno, Bro."
    kev "Is it just gonna be you there drawing?"
    show player 10
    show kevin 1
    player_name "Well, {b}Mia{/b} and I will both be drawing."
    player_name "{b}Miss Ross{/b} will be there too."
    show player 11
    show kevin 4
    kev "Ugh, pass..."
    show kevin 3
    kev "I don't want girls to see me naked, Bro. That's kinda gross."
    show kevin 1
    player_name "..."
    show player 10
    player_name "O-okay."
    return

label kevin_dialogue_intro:
    show kevin 23 at right
    show player 14 at left
    with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 13
    show kevin 9b
    kev "Hello, {b}[firstname]{/b}."
    show kevin 23
    show player 14
    player_name "What's up?"
    show player 13
    show kevin 9b
    kev "Not much. Yesterday was glutes day for me."
    kev "My ass is sore!"
    kev "Feel how tight it is though!"
    show kevin 23
    show player 10
    player_name "Uhhh... No thanks dude."
    show player 13
    show kevin 9b
    kev "Your loss!"
    return

label kevin_dialogue_erik_favor_2_completed:
    kev "I'd better see you at the gym later today!"
    show kevin 23
    show player 14
    player_name "Maybe..."
    show player 13
    show kevin 9b
    return

label kevin_dialogue_dewitt_kevin_give_guitar:
    show player 14
    player_name "I found a guitar for you!"
    show player 13
    show kevin 24
    kev "Really?"
    show kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "What do you think?"
    show player 13 with dissolve
    show kevin 16f with dissolve
    kev "Holy crap! Where did you get this thing?"
    kev "This thing is really high end!"
    show kevin 14f
    show player 10
    player_name "It is?"
    show player 5
    show kevin 15f
    kev "Uhh, yeah Bro!"
    kev "I hope you didn't steal it or something."
    show kevin 14f
    show player 14
    player_name "Borrowed it actually, from a friend of mine. So be careful with it, yeah?"
    hide player
    show kevin 27 at left
    with dissolve
    kev "No problems there!"
    kev "I'll treat this beauty with the respect it deserves!"
    show kevin 28
    player_name "Cool, so you're down to play it for the talent show."
    show kevin 27
    kev "I'm down!"
    show kevin 28
    player_name "Awesome! I'll see you in {b}Ms. Dewitt's{/b} class soon for practice then!"
    show kevin 27
    kev "Sounds good, Bro!"
    show player 13 at left
    show kevin 16 at right
    with dissolve
    kev "I'm gonna call you... Devin"
    kev "Would you like that beautiful?"
    show player 11
    hide kevin with dissolve
    player_name "..."
    return

label kevin_dialogue_talent_show_help:
    show player 10
    player_name "I'm helping {b}Ms. Dewitt{/b} find volunteers for the talent show."
    player_name "Didn't you used to play the guitar?"
    show player 5
    show kevin magic 2
    kev "Yeah, I used to."
    show kevin magic 1
    show player 10
    player_name "What happened?"
    show player 5
    show kevin magic 2
    kev "Ah, my ex kinda smashed it after I broke up with him."
    show kevin magic 1
    show player 12
    player_name "Him?"
    show player 11
    show kevin magic 3 with dissolve
    kev "Did I say him? Sorry, I meant her."
    kev "... Yeah, SHE smashed it to pieces."
    show kevin magic 1 with dissolve
    show player 14
    player_name "Huh, you got a thing for the crazy girls, huh?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Heh, you know it! Crazy girls, I'm waaaaay into them! Totally..."
    show kevin magic 1 with dissolve
    show player 14
    player_name "So if you had a guitar, would you play in the talent show?"
    show player 13
    show kevin magic 2
    kev "Yeah, I wouldn't mind."
    kev "Where am I gonna get a guitar though? They are super expensive!"
    show kevin magic 1
    show player 35
    player_name "Hmm, maybe I can find you one..."
    show player 34
    player_name "( {b}Erik{/b} has a bunch in his basement. Maybe I can borrow one? )"
    show player 14
    player_name "I'll be back!"
    show player 13
    show kevin magic 2
    kev "Alright."
    return

label kevin_dialogue_talent_show_replace_guitar:
    show player 14
    player_name "So if you had a guitar, would you play in the talent show?"
    show player 13
    show kevin magic 2
    kev "Yeah, I wouldn't mind."
    kev "Where am I gonna get a guitar though? They are super expensive!"
    show kevin magic 1
    show player 34
    player_name "( I need to switch my custom-made guitar with one in {b}Erik's{/b} basement! )"
    show player 14
    player_name "I'll be back!"
    show player 13
    show kevin magic 2
    kev "Alright."
    return

label kevin_dialogue_talent_show:
    show player 14
    player_name "So if you had a guitar, would you play in the talent show?"
    show player 13
    show kevin magic 2
    kev "Yeah, I wouldn't mind."
    kev "Where am I gonna get a guitar though? They are super expensive!"
    show kevin magic 1
    show player 35
    player_name "Hmm, maybe I can find you one..."
    show player 34
    player_name "( {b}Erik{/b} has a bunch in his basement. Maybe I can borrow one? )"
    show player 14
    player_name "I'll be back!"
    show player 13
    show kevin magic 2
    kev "Alright."
    return

label kevin_dialogue_dewitt_science_adhesive:
    show player 10
    player_name "What do we need for that {b}adhesive{/b} again?"
    show player 13
    show kevin 2
    kev "Just meet me in the {b}science lab after class{/b}."
    kev "I'll take care of the rest."
    show kevin 1
    show player 14
    player_name "Awesome! Thanks, {b}Kevin{/b}!"
    return

label kevin_dialogue_leave:
    show player 14
    player_name "Anyways, I gotta go."
    player_name "Keep your spirits up, man."
    show player 13
    show kevin 2
    kev "Yeah, alright bro."
    kev "See ya around."
    hide kevin
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
