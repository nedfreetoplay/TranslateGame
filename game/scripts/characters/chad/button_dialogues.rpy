label button_chad_get_eve_drawing_first:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "Hey Man, I'm trying to find {b}Eve's Art Pad{/b}."
    player_name "She said you might have it."
    show player 1
    show chad 2
    chad "Yeah, that's right."
    show player 10
    show chad 1
    player_name "So, could I get it from you?"
    show player 11
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "Tch, Not for free, yo."
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "..."
    show player 10
    player_name "What do you want?"
    show player 11
    show chad 6
    chad "Man, {b}Eve's{/b} a pretty dope artist, you know what I'm sayin'?"
    show player 10
    show chad 5
    player_name "Yeah, so I hear."
    show player 11
    show chad 6
    chad "She's got this one drawin'..."
    chad "Shit is lit as fuck, man!"
    chad "I thought it would be in her {b}art pad{/b} but no dice."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "You gotta {b}get me that drawin'{/b}, Dawg!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "... And if I do, you'll give me the {b}Art Pad{/b}?"
    show player 11
    show chad 6
    chad "Haaah, that's the deal, yo."
    show chad 2
    chad "You down?"
    show player 10
    show chad 1
    player_name "Sure. What's the drawing look like?"
    show player 11
    show chad 6
    chad "Ah, it's this self portrait she did."
    chad "S'pose to be like an anime girl or somethin'"
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "All I know is... It's fuckin' sexy, yo!"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Any idea where it could be?"
    show player 11
    show chad 3
    chad "Mmm, man if I had to guess..."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "I betcha she's keepin' that shit {b}in her locker{/b}."
    show player 2
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Alright, I'll go take a look."
    show player 1
    show chad 2
    chad "Hurry back, Man."
    return

label button_chad_get_eve_drawing:
    scene location_school_right_hall_day_blur
    show player 10 at left
    show chad 1 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    player_name "What did you want for that {b}Art Pad{/b} again?"
    show player 11
    show chad 2
    chad "You forget or somethin'?"
    show player 10
    show chad 1
    player_name "Yeah, kinda."
    show player 11
    show chad 2
    chad "Tch, I want that self portrait {b}Eve{/b} did."
    show chad 4 at Position(xpos=0.75, ypos=1.0) with dissolve
    chad "She's probably got it under wraps {b}in her locker{/b}, know what I'm sayin'?"
    show player 10
    show chad 1 at Position(xpos=0.8, ypos=1.0) with dissolve
    player_name "Alright."
    return

label button_chad_get_eve_drawing_completed:
    scene location_school_right_hall_day_blur
    show player 1 at left
    show chad 6 at Position(xpos=0.8, ypos=1.0)
    with dissolve
    chad "Ey, Man. Did you get it?"
    show chad 1
    show player 612 with dissolve
    player_name "Yeah, you were right. It's pretty sexy..."
    show chad 6
    show player 611
    chad "Lemme see that shit!"

    $ player.remove_item("eve_drawing")
    show player 1 with dissolve
    show chad 7 at Position(xpos=0.765, ypos=1.0) with dissolve
    pause
    show chad 8
    chad "Doooope!"
    chad "Damn! Now that's a woman, yo!"
    show player 2
    show chad 7
    player_name "Can I have that {b}Art Pad{/b} now?"
    show player 1
    show chad 9
    chad "Ah, yeah. My bad! I'm all over here droolin' and shit!"
    show chad 10 at Position(xpos=0.725, ypos=1.0) with dissolve
    chad "Here ya go."
    show player 598
    show chad 7 at Position(xpos=0.765, ypos=1.0)
    with dissolve
    show expression "boxes/popup_item_artpad1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_artpad1.png"
    player_name "Thanks, Chad."
    show player 596
    show chad 8
    chad "Pleasure doin' business with ya."
    return

label button_chad_generic:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad 1 at right
    with dissolve
    player_name "Hey, what's up, man?"
    show player 1
    show chad 3
    chad "Damnit, {b}[firstname]{/b}! Can't you see I'm practicing my rhymes here, Dawg!"
    show player 10
    show chad 1
    player_name "Uhh, okay?"
    show player 11
    show chad 2
    chad "What do you want anyways?"
    return

label button_chad_nothing:
    show player 2
    show chad 1
    player_name "Just thought I'd say hello."
    show player 1
    show chad 3
    chad "Beat it, yo."
    show player 11
    chad "I'm struggling with some serious shit right now."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
