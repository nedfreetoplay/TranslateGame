label button_grace_mia_get_tattoo:
    scene tattoo_indoor_c
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace 2 at right
    show tattoo_desk at right
    with dissolve
    grace "Hey there!"
    grace "Are you here for an appointment?"
    return

label button_grace_generic:
    show player 13 at left
    show grace 2 at right
    show tattoo_desk at right
    with dissolve
    grace "Hey there!"
    grace "Are you here for an appointment?"
    return

label button_grace_tattoo:
    show mia 10f
    mia "I'd like to get a tattoo... Now."
    show mia 7f
    show grace 2
    grace "Now? I see..."
    show grace 3
    grace "Do you have a design in mind?"
    show grace 1
    show mia 30f at Position (xoffset=64) with dissolve
    mia "My friend here drew this for me, and I'd like it done today!"
    show mia 7f
    show grace 5
    with dissolve
    grace "Hmm..."
    show grace 6
    grace "Are you sure you want this done?"
    grace "Tattoos are permanent, so I have to make sure my clients know what they're getting into!"
    show grace 7
    show mia 10f
    mia "I've been thinking about it for a long time and... Yes, I do want it."
    show mia 7f
    show grace 6
    grace "Alright, sweetie. But, it aint cheap!"
    show grace 7
    show player 14
    player_name "How much is it?"
    show player 13
    show grace 5
    grace "For that size... with colors... Around {b}$400{/b}."
    show grace 7
    show player 22
    show mia 12f
    mia "!!!"
    mia "Damn... I think I only have {b}$200{/b}..."
    show mia 8f
    show player 11
    player_name "..."
    show player 10
    player_name "You don't have enough?"
    show player 5
    show mia 12 with dissolve
    mia "No, that's all I was able to save up."
    mia "What do you think I should do?"
    show mia 8
    return

label button_grace_tattoo_help:
    show player 14
    player_name "I'll cover the rest."
    show player 13
    show mia 12
    mia "Really?!"
    show mia 7
    show player 14
    player_name "Why not."
    player_name "I've been working lately so I have some money to spend..."
    show player 17
    player_name "...And it's for a good cause!"
    show player 13
    show mia 10
    mia "That's really sweet of you..."
    mia "...And I'll make sure to pay you back!"
    show mia 7
    show player 17
    player_name "It's alright, ha ha."
    show player 13
    show grace 6
    grace "So?"
    show mia 7f with dissolve
    grace "Ready to start?"
    show grace 7
    show mia 10f
    mia "I'm ready!"
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve

    scene tattoo_cs01
    show text "It took a while for {b}Grace{/b} to finish the work.\nI was really nervous for {b}Mia{/b}...\n...But, she seemed to be fine the whole time!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide tattoo_cs01
    with dissolve

    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace 2 at right
    with dissolve
    grace "All done!"
    grace "I hope you guys like it."
    show grace 1
    show mia 10f
    mia "It's great! And it didn't hurt as much as I thought..."
    show mia 7f
    show grace 2
    grace "Make sure you leave the bandage on it for at least a few days."
    show grace 1
    show mia 10f
    mia "Okay, thank you!"
    show mia 7f
    show grace 2
    grace "Bye, guys."
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 7 right
    with dissolve
    show player 14
    player_name "How does it feel?"
    show player 13
    show mia 12
    mia "The tattoo?"
    show mia 7
    show player 14
    player_name "Yeah."
    show player 13
    show mia 12
    mia "It's fine... It just has this tingling sensation."
    show mia 10
    mia "And I'm glad I did it... I can finally say I did something that I wanted."
    show mia 7
    show player 10
    player_name "Are you scared your mom might find out?"
    show player 5
    show mia 9
    mia "Hopefully not, but it's in a well hidden spot, ha ha."
    show mia 7
    show player 17
    player_name "I think it's cool you did it."
    show player 18
    show mia 10
    mia "Thanks, {b}[firstname]{/b}. I'm happy you came with me."
    show player 13
    mia "I should get going, though. Before my mom starts getting suspicious..."
    show mia 7
    show player 14
    player_name "Okay, see you at school!"
    show player 13
    show mia 10
    mia "Bye."
    hide player
    hide mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    show player 10
    player_name "Maybe we should come back later?"
    show player 5
    mia "..."
    show mia 12
    mia "I suppose we should."
    show mia 8
    show player 10
    player_name "It's okay. We can always come back another time."
    show player 5
    show mia 12
    mia "You're right."
    show mia 8
    show player 10
    player_name "Sorry you couldn't get your tattoo today..."
    show player 5
    show mia 12
    mia "It's fine. I should get home now."
    show mia 8
    show player 10
    player_name "Alright, see you later."
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene location_tattoo_indoor_closeup
    show player 10 zorder 3 at left
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace 1 zorder 0 at right
    player_name "May I ask you something?"
    show player 11
    show grace 2
    grace "Sure!"
    show player 10
    show grace 1
    player_name "Well, you see..."
    show player 11
    pause
    show player 10
    player_name "The thing is..."
    show player 11
    grace "..."
    show player 10
    player_name "... Here's the thing..."
    show player 11
    show eve 2f zorder 2 at Position(xpos=0.35, ypos=1.0) with dissolve
    eve "Geez, spit it out already, {b}[firstname]{/b}!"
    show eve 1bf with dissolve
    eve "What up, Raggedy Ann?"
    show eve 5f with dissolve
    show grace 4
    grace "Heh, not much."
    show grace 2
    grace "You staying outta trouble, Punk?"
    show eve 6bf
    show grace 1
    eve "Of course not."
    show player 1
    show eve 5f
    show grace 4
    grace "Hehe."
    show eve 2f
    show grace 1
    eve "Look, {b}[firstname]{/b} here needs some ink."
    show eve 5f
    show grace 2
    grace "Oh, you thinking of getting a tattoo there, Stud?"
    show player 11
    show grace 1
    player_name "..."
    show eve 1bf with dissolve
    eve "No, no, no. He needs actual ink! Like in bottles, ya Dummy!"
    show eve 6bf
    eve "Sorry, she can be a little slow."
    show eve 5f
    show grace 3
    grace "Hey! I heard that!"
    show eve 6f
    show grace 1
    eve "Yeah, I said it loud..."
    show eve 5f
    show grace 4
    grace "Haha, smart ass."
    show eve 6f
    show grace 1
    eve "Looove ya, Sis!"
    show eve 5f
    show grace 2
    grace "Yeah, yeah. You're lucky you're cute."
    show player 1
    show grace 1
    show eve 1bf with dissolve
    eve "I am, aren't I?"
    show grace 2
    show eve 5f with dissolve
    grace "So, how much ink do you need, {b}[firstname]{/b}?"
    show player 2
    show grace 1
    player_name "Umm, I'm not sure."
    player_name "Just enough to do one painting."
    show player 1
    show grace 2
    grace "Ahhh, an artist, huh?"
    show grace 4
    grace "Figures, the first guy {b}Eve{/b} brings home is an artist."
    show player 11
    show grace 1
    show eve 6bf
    eve "Tch, better than that biker freak you had hanging around here in high school."
    show eve 1f
    show grace 4
    grace "Heh, you'll get no arguements there..."
    show grace 2
    grace "Would one bottle of each primary color be enough?"
    show grace 3
    grace "I assume you know how to mix?"
    show player 10
    show grace 1
    player_name "Mix?"
    show player 11
    show eve 2f
    eve "Yeah, you know? Blue and red make purple."
    eve "Yellow and blue make green."
    show player 2
    show eve 1f
    player_name "Oh yeah, like color wheel stuff, right?"
    show player 1
    show grace 2
    grace "Yeah, exactly."
    show grace 3
    grace "I guess the only question now, is what are you gonna do for me?"
    show grace 1
    show player 10
    player_name "Oh, uhh. I dunno? What do you want me to do?"
    show grace 3
    show player 11
    grace "Hmm, did you happen to notice the graffiti on the side of the building when you came in?"
    show player 10
    show grace 1
    player_name "... Yeah, it's pretty hard to miss."
    show player 11
    show grace 2
    grace "I'll give you the paints if you can wash it off for me."
    show grace 1
    show eve 2f
    eve "For real?"
    show player 2
    show eve 1f
    player_name "I can do that!"
    show player 1
    show eve 6bf
    grace "Pfft, what a waste of time!"
    show eve 1f
    show player 11
    player_name "..."
    show eve 1bf with dissolve
    eve "It's just gonna get tagged again..."
    show eve 1f
    show grace 8
    with dissolve
    grace "Well, it's your stupid fucking friends that keep doing it!"
    grace "You need to tell those little bitches, I'll whoop their fucking asses if it happens again!"
    show grace 9
    show player 10
    player_name "Daaang, I didn't know your {b}Sister{/b} was such a bad ass!"
    show eve 6f
    show player 11
    eve "Heh, you have no idea."
    show eve 5f
    show grace 8
    grace "I dunno why you hang out with those douchebags anyways..."
    show eve 2f
    show grace 9
    eve "... If you're going to blackmail {b}[firstname]{/b} into doing chores. You could at least have him do something useful."
    eve "Like maybe moving all that heavy shit you ordered into the back room?"
    show eve 6bf
    show grace 1 with dissolve
    eve "I don't wanna bust my vagina carrying that shit!"
    show eve 5f
    show grace 3
    grace "Hmm, I suppose that's not a bad idea."
    show grace 4
    grace "... Especially if it gets you to shut up about your vagina! Ugh!"
    show grace 1
    show eve 6bf
    eve "... Bitch."
    show eve 5f
    show grace 4
    grace "Hahaha, don't pretend like you don't love the abuse."
    show grace 1
    show eve 6bf
    eve "Yeah, yeah..."
    show eve 2f
    eve "If you'll excuse me, {b}[firstname]{/b}."
    show player 1
    eve "I'd better go warn the guys that {b}Grace{/b} is on the war path again."
    show eve 1f
    show grace 4
    grace "Damn right!"
    show grace 1
    show eve 6f
    eve "See ya, Sis!"
    hide eve
    with dissolve
    show grace 2
    grace "The {b}boxes are right in front of the counter{/b}. Just {b}move them{/b} into the back for me and the paint is yours."
    show grace 1
    show player 2
    player_name "Sounds good!"
    return

label button_grace_you_look_familiar:
    show player 10
    player_name "You know... I think..."
    show player 12
    player_name "Uhh."
    show player 34
    show grace 3
    grace "Is everything okay?"
    show grace 1
    show player 30
    player_name "Sorry, but you look... familiar."
    show player 5
    show grace 3
    grace "Huh?"
    show grace 2
    grace "Hmm... Maybe you're thinking of my sister?"
    show grace 1
    show player 12
    player_name "Sister?"
    show player 11
    show grace 3
    grace "My little sister? {b}Eve{/b}?"
    show grace 1
    show player 38 with dissolve
    player_name "Oh! Of course!"
    show player 14 with dissolve
    player_name "I can see the connection, now."
    show player 13
    show grace 4
    grace "Ha ha."
    show grace 2
    grace "Anyway, is there anything I can do for you?"
    return

label button_grace_nothing:
    show player 14
    player_name "I'm just looking around."
    show player 13
    show grace 2
    grace "Cool! Have a look."
    grace "I do all styles and designs showcased in my shop!"
    grace "Just let me know if you ever think about getting something, and we can make an appointment!"
    show grace 1
    show player 14
    player_name "Okay, thanks!"
    show player 13
    show grace 2
    grace "See ya."
    hide grace
    hide mia
    hide player
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
