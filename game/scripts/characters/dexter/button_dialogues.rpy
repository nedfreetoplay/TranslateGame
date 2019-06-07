label button_dexter_talent_show:
    show dexter 1
    show player 10
    player_name "Hey {b}Dexter{/b}, you play any instruments?"
    show player 5
    show dexter 2
    dex "Huh?"
    show player 12
    player_name "I-N-S-T-R-U-M-E-N-T-S. You know, like for music... Do you play any?"
    show player 5
    show dexter 8
    dex "Do I look like some kinda band geek to you?!"
    show dexter 2
    show player 12
    player_name "Ehh, no? I just thought maybe you had a hidden talent for banging the drums or something?"
    show player 5
    show dexter 6 with dissolve
    dex "I'd like to bang on your stupid face with my fists..."
    dex "You think that would make some music?"
    show dexter 5
    show player 29 with dissolve
    player_name "Heh, I was just leaving..."
    show player 3
    show dexter 4 with dissolve
    dex "Yeah, you better!"
    return

label button_dexter_challenge:
    show player 12
    player_name "I'm here to challenge you, {b}Dexter{/b}."
    show player 5
    show dexter 3
    dex "Ha ha!"
    dex "To what?!"
    show dexter 1
    show player 10
    player_name "To uh..."
    show player 5
    show dexter 3
    dex "You know I'd beat you at anything."
    show dexter 4 with dissolve
    dex "Now fuck off before I decide to beat the shit out of you."
    return

label button_dexter_library_book:
    show player 10
    player_name "Hey, umm, {b}Dexter{/b}..."
    show player 5
    show dexter 3
    dex "What do you want Twerp?"
    show dexter 1
    show player 10
    player_name "Did you remember where you left the library book you checked out..."
    show player 5
    show dexter 8
    dex "Library book?"
    show dexter 4 with dissolve
    dex "Didn't I tell you to get outta here, {b}[firstname]{/b}?"
    dex "Or do you want a knuckle sandwich!"
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
    return

label button_dexter_nothing:
    show player 10
    player_name "I... uhh... didn't mean to bother you."
    player_name "I need to get to class."
    show player 5
    show dexter 3
    dex "Run along, loser."
    return

label dexter_button_pushups:
    show player 16 at left
    show dexter 12 at right
    with dissolve
    dex "Oh, you want a rematch huh?"
    dex "No problem, nerd!"
    dex "I'll show you how it's done!"
    show dexter 11
    scene gym
    show player 16 at left
    show dexter 11 at right
    with dissolve
    bri "Alright, boys. You know the drill!"
    bri "Last man standing wins!"
    show dexter 12
    dex "Hahaha, watch and learn... NERD!"
    hide player
    hide dexter
    with dissolve
    bri "GO!"
    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show dexter 15 at right
    with dissolve
    dex "How about a rematch, nerd?!"
    show dexter 14
    show player 12
    player_name "What?! C'mon, man... You lost."
    player_name "Just move on."
    show player 5
    show dexter 12 with dissolve
    dex "Psh, you scared you're gonna lose?"
    show dexter 11
    show player 12
    player_name "No."
    show player 90
    show dexter 28 with dissolve
    dex "{b}[firstname]'s{/b} a chicken, everybody!"
    show dexter 11 with dissolve
    show player 12
    player_name "... Tch, fine."
    player_name "Let's do it!"
    hide player
    hide dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "What are you looking at, loser?!"
    show dexter 1
    show player 10
    player_name "Nothing."
    show player 5
    show dexter 3
    dex "Yeah, that's right!"
    dex "Keep on walkin' bitch!"
    dex "Hahahaha!"
    hide dexter with dissolve
    show player 12
    player_name "Ugh, he's such an asshole..."
    hide player with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "I thought I smelled a little bitch!"
    show dexter 2
    show player 12
    player_name "Screw you, {b}Dexter{/b}..."
    show player 90
    show dexter 6 with dissolve
    dex "WHAT DID YOU SAY?!"
    show dexter 4 with dissolve
    show player 11
    dex "You want me to knock your ass out, right here?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Yeah, that's what I thought."
    show dexter 6 with dissolve
    dex "You better be staying away from my girl!"
    show dexter 2 with dissolve
    show player 5
    player_name "..."
    show dexter 4 with dissolve
    dex "You hear me, bitch?!"
    show dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show dexter 2 at right
    with dissolve
    dex "..."
    show player 12
    player_name "I'm sorry, did you say something, {b}Dexter{/b}?"
    show player 91
    show dexter 8
    dex "No!"
    show dexter 2
    show player 12
    player_name "Yeah, that's what I thought."
    show player 91

    dex "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Still playing basketball?"
    show player 91
    dex "..."
    show player 12
    player_name "Have you guys managed to win a game yet?"
    show player 91
    show dexter 8
    dex "I don't wanna talk about it!"
    show dexter 2
    show player 12
    player_name "I'm just trying to-"
    show player 11
    show dexter 8
    dex "Leave me alone, {b}[firstname]{/b}!"
    hide dexter with dissolve
    pause
    show player 10
    player_name "Sheesh, alright."
    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Still playing basketball?"
    show player 90
    show dexter 3
    dex "Of course, I was born to play!"
    show dexter 1
    show player 12
    player_name "Have you even won a game yet?"
    show player 90
    show dexter 3
    dex "Psh, Yeah. Like a hundred million..."
    show dexter 1
    show player 12
    player_name "Yeah right! You guys are awful..."
    show player 90
    show dexter 4 with dissolve
    dex "HEY! You want a knuckle sandwich, loser?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "What does a little bitch like you know about basketball anyways?!"
    dex "It's a man's sport!"
    show dexter 1
    show player 17
    player_name "Oh, well then, it's no wonder why you ladies can't win a game."
    show player 13
    show dexter 3
    dex "Huh? I don't-"
    dex "Oh, you think that's funny?!"
    show dexter 8
    dex "How about I knock some of your teeth out?!"
    show player 5
    dex "That would be pretty funny, wouldn't it?!"
    show dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Tch, Yeah. Whatever, man..."
    hide player with dissolve
    pause
    show dexter 8
    dex "Hey, I'm not kidding {b}[firstname]{/b}!"
    dex "Stay away from, {b}Roxxy{/b}!"
    dex "She's mine!"
    hide dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "I trust you're behaving yourself."
    show player 90
    show dexter 8
    dex "... Yes."
    show dexter 2
    show player 12
    player_name "You do remember what happens, if I catch you messing with my friends again, right?"
    show player 92
    player_name "Do you need a reminder?!"
    show player 91
    show dexter 8
    dex "NO!"
    dex "I remember..."
    show dexter 2
    show player 92
    player_name "Good."
    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Run along now, {b}Dexter{/b}."
    show player 91
    dex "..."
    show dexter 8
    dex "GRRRR!!!"
    hide dexter with dissolve
    pause
    show player 17
    player_name "Hahaha!"
    player_name "I like the new {b}Dexter{/b}!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
