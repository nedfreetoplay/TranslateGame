label second_floor_first_visit:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 2 at right
    with dissolve
    kev "Whoa, {b}[firstname]{/b}?!"
    kev "When did you get back?"
    show kevin 1
    show player 14
    player_name "Hey, {b}Kevin{/b}."
    player_name "Today's my first day."
    show player 13
    show kevin 2
    kev "Right on, bro."
    show kevin 2c with dissolve
    kev "Good to see you!"
    show player 19 with dissolve
    pause
    show player 3
    show kevin 2d
    with dissolve
    kev "Sorry about {b}your dad{/b} by the way..."
    show kevin 2e
    show player 10 with dissolve
    player_name "Yeah, thanks."
    show player 5
    pause
    show player 14
    player_name "What's with the apron?"
    show player 13
    show kevin 2 with dissolve
    kev "Ugh, {b}Mrs. Smith{/b} put me on cafeteria duty until I raise my grade in {b}Miss Okita's{/b} class..."
    show kevin 1
    show player 10
    player_name "You're failing science?"
    show player 13
    show kevin 2
    kev "Well, I'm not failing yet but it defintely isn't looking good, bro."
    show kevin 1
    show player 14
    player_name "That sucks man."
    show player 13
    show kevin 2
    kev "Tell me about it!"
    kev "I haven't had a good workout in weeks!"
    show kevin 1
    show player 14
    player_name "Oh, yeah?"
    player_name "Still hanging out down at that gym?"
    show player 13
    show kevin 2
    kev "You know it, bro!"
    show kevin 2b with dissolve
    kev "I can't let these guns go unpolished, can I?"
    show player 14
    player_name "Heh, no, I guess not..."
    show player 13
    show kevin 2 with dissolve
    kev "Oh, that reminds me!"
    kev "We got that new {b}Muay Thai{/b} trainer there."
    kev "His name is {b}Master Somrak{/b}."
    kev "He's like, a grandmaster or something with all his ancient teachings..."
    kev "It's pretty awesome!"
    show kevin 1
    show player 14
    player_name "{b}Muay Thai{/b}?"
    show player 13
    show kevin 2
    kev "Yeah, bro!"
    kev "You know, like, {b}kickboxing{/b} and stuff."
    show kevin 1
    show player 14
    player_name "Really?"
    show player 13
    show kevin 2
    kev "You should go in there and check it out!"
    show kevin 1
    show player 29 with dissolve
    player_name "Oh, I dunno..."
    show player 3
    show kevin 2
    kev "C'mon, bro!"
    kev "You gotta get that body in shape."
    kev "The people demand beefcake, not sweet cake!"
    show kevin 1
    show player 10 with dissolve
    player_name "Eh?"
    player_name "I guess, I could check it out..."
    show player 13
    show kevin 2
    kev "That's the spirit, bro!"
    kev "Who knows, you might even be able to whoop {b}Dexter's{/b} ass once you've got a few classes under your belt."
    show kevin 1
    show player 14
    player_name "Psh, yeah right."
    show player 13
    pause
    show player 14
    player_name "I should get going, man."
    player_name "{b}Mrs. Smith{/b} is waiting on me upstairs {b}in her office{/b}."
    show player 13
    show kevin 2
    kev "Oh shit, bro... I didn't know that!"
    kev "You better hurry on then before you end up in the cafeteria with me."
    show kevin 1
    show player 36 with dissolve
    player_name "See ya, {b}Kevin{/b}."
    show player 13 with dissolve
    show kevin 2
    kev "Come by {b}the cafeteria{/b} later and we can hang."
    show kevin 1
    show player 14
    player_name "Alright."
    hide player
    hide kevin
    with dissolve
    return

label second_floor_okita_dose_smith:
    scene expression game.timer.image("backgrounds/location_school_second{}_blur.jpg")
    show player 35
    player_name "Хмм, Я думаю {b}Директриса Смит{/b} пошла в {b}Учительскую{/b} чтобы {b}попить кофе{/b} в дневное время."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
