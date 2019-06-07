label button_eve_intro:
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 13 at left
    show eve 1 at right
    with dissolve
    return

label button_eve_talent_show_help:
    show player 10
    player_name "Do you play any instruments?"
    show player 5
    show eve 2
    eve "No, I don't play any instruments. I've always wanted to learn but I just haven't had the time, you know?"
    show eve 1
    show player 10
    player_name "Okay, well how about singing?"
    show player 5
    show eve 6
    eve "Oh, umm..."
    show eve 2b
    eve "Yeah, I like to sing I guess. I dunno if I'm any good though."
    show eve 1
    show player 14
    player_name "I bet you are! You should sign up for the talent show with me!"
    player_name "We're really hurting for more volunteers."
    show player 13
    show eve 2b
    eve "... Yeah, I dunno."
    eve "You want me to sing in front of the entire school? That sounds pretty embarassing."
    eve "... And I haven't sang in awhile. Not since my karaoke machine broke."
    eve "I'm quite out of practice."
    show eve 1
    show player 4 with dissolve
    player_name "Hmm..."
    show player 14 with dissolve
    player_name "You know, I think my friend {b}Erik{/b} has a {b}karaoke machine{/b} in his basement."
    show player 13
    show eve 2
    eve "Oh, yeah?"
    show eve 1
    show player 17
    player_name "Totally! You should come over sometime and practice!"
    show player 13
    show eve 6
    eve "Heh, you want me to sing for you and your friend?"
    show eve 5
    show player 14
    player_name "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    show player 13
    show eve 1
    eve "..."
    show eve 6b
    eve "Alright, I guess I can stop by for a little while."
    show eve 5
    show player 14
    player_name "Awesome! {b}I'll meet you at Erik's house{/b} tonight."
    return

label button_eve_ross_find_art_pad:
    show player 2
    player_name "I need to ask you for a favor."
    show player 1
    show eve 2
    eve "Oh?"
    show player 2
    show eve 1
    player_name "You see, I'm kinda helping {b}Miss Ross{/b} with something and we need your art pad."
    show player 1
    show eve 2
    eve "Well that's no problem."
    eve "You just have to {b}help me find my backpack{/b} first."
    show player 10
    show eve 1
    player_name "You lost your backpack?"
    show player 11
    show eve 2
    eve "Yeah..."
    eve "My art pad should be inside it."
    show player 10
    show eve 1
    player_name "Where was the last place you remember having it?"
    show player 11
    show eve 2
    eve "Hmm, well I think {b}I had it when I went to hang out with the guys in the park last night{/b}."
    show player 2
    show eve 1
    player_name "Alright, I'm on it!"
    return

label button_eve_ross_find_eve_backpack_have_backpack:
    show player 610
    player_name "Look what I found!"
    show player 609
    show eve 2
    eve "Niiiice!"
    show player 1 with dissolve
    eve "Thanks, {b}[firstname]{/b}!"
    show player 2
    show eve 1
    player_name "No worries. I couldn't find your {b}Art Pad{/b} though."
    show player 1
    show eve 2
    eve "It wasn't in my bag?"
    show player 2
    show eve 1
    player_name "Nope."
    show player 1
    show eve 2
    eve "Weird."
    show eve 6b
    eve "I wonder if {b}Chad{/b} snatched it again?"
    show player 10
    show eve 1
    player_name "Chad?"
    show player 11
    show eve 2
    eve "Yeah, he digs my art."
    show player 10
    show eve 1
    player_name "Interesting..."
    show player 2
    player_name "I'll go ask him."
    show player 1
    show eve 2
    eve "Cool. See ya, {b}[firstname]{/b}."
    show player 2
    show eve 1
    player_name "See ya, {b}Eve{/b}."
    return

label button_eve_ross_find_eve_backpack_no_backpack:
    show player 2
    player_name "Where did you leave your backpack, again?"
    show player 1
    show eve 2
    eve "I'm not entirely sure. I remember having it with me {b}at the park{/b} lastnight."
    show player 2
    show eve 1
    player_name "Okay, I'll check there!"
    return

label button_eve_ross_get_eve_drawing:
    show player 10
    player_name "Where did you say that {b}Art Pad{/b} was again?"
    show player 11
    show eve 6b
    eve "Oh, {b}Chad probably has it{/b}."
    show eve 2
    eve "He digs my art."
    show player 2
    show eve 1
    player_name "Gotcha, thanks!"
    return

label button_eve_ask_model:
    show player 2
    show eve 1
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show eve 2
    eve "Modeling? That could be fun."
    show player 2
    show eve 1
    player_name "Really!? Awesome! I was hoping you would say that!"
    show player 1
    show eve 2
    eve "Yeah, I don't mind. It's a good thing I wore this cute outfit today."
    show player 10
    show eve 1
    player_name "... Oh, umm. It would be nude modeling."
    show player 11
    show eve 2b
    eve "Nude?!"
    show eve 6
    eve "Oh, hell no!"
    show player 10
    show eve 5
    player_name "So you won't do it? I thought you were into artsy stuff?"
    show player 11
    show eve 6
    eve "Yeah, but that doesn't mean I'm into public nudity!"
    show player 10
    show eve 5
    player_name "Good point. Sorry."
    show player 11
    show eve 2
    eve "It's alright. Just not interested."
    show player 2
    show eve 1
    player_name "Well, thanks anyways..."
    return

label button_eve_ross_get_paint:
    show player 2
    show eve 1
    player_name "I need some paint. Any idea where I could find some?"
    show player 1
    show eve 6b
    eve "I dunno, maybe try a store?"
    show player 2
    show eve 1
    player_name "Well yeah, I know... Duh, right?"
    player_name "... But the paint is for {b}Miss Ross{/b} and she can't afford to buy it."
    show player 1
    show eve 6
    eve "Oh, hehe."
    show eve 4 with dissolve
    eve "Hmm, free paint. That's a toughie."
    show eve 3
    show player 2
    player_name "Tell me about it..."
    show player 1
    show eve 2 with dissolve
    eve "We could try asking {b}My Sister{/b}."
    show player 2
    show eve 5
    player_name "She's a {b}Tattoo Artist{/b}, right?"
    show player 1
    show eve 6
    eve "She's the best {b}Tattoo Artist{/b}!"
    eve "You should come check out her work, it's amazing!"
    show player 2
    show eve 5
    player_name "You think she would let me have some paint?"
    show player 1
    show eve 2
    eve "We can go ask her."
    show eve 5
    show player 10
    player_name "Isn't her parlor called {b}Sugar Tats{/b}?"
    show player 11
    show eve 6
    eve "Yuuuup. It's on the {b}North{/b} side of town."
    show player 2
    show eve 5
    player_name "Alright, I'll meet you there!"
    return

label button_eve_ross_get_paint_grace:
    show player 10
    show eve 5
    player_name "What's the name of your Sister's parlor again?"
    show player 11
    show eve 2
    eve "{b}Sugar Tats{/b}. It's on the {b}North{/b} side of town."
    show player 2
    show eve 5
    player_name "Okay, {b}I'll meet you there{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
