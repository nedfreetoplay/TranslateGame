label prom_poster:
    show expression game.timer.image("prom_poster_day{}")
    pause
    player_name "( The prom is coming up soon. )"
    player_name "( Seems like it'd be a good time... if I had a date. )"
    player_name "( I'd better hurry and find someone. )"
    player_name "( I wonder who I could ask. )"
    $ game.main()

label school_righthallway_roxxy_go_in_auditorium:
    scene expression player.location.background_blur
    show player 642 at left
    show erik 4 at right
    with dissolve
    eri "Hey!"
    eri "What's up, dude?!"
    show erik 1
    show player 641
    player_name "Oh, hey, {b}Erik{/b}."
    player_name "I'm just taking these records to the {b}auditorium{/b} for {b}Miss Dewitt{/b}..."
    show player 642
    show erik 4
    eri "Ah, right on..."
    eri "It looks heavy!"
    show erik 1
    show player 641
    player_name "A bit, yeah."
    player_name "What are you doing here?"
    show player 642
    show erik 4
    eri "I was just heading to the auditorium too."
    eri "I've got a small break before my next class and its usually quiet and dark in the {b}auditorium{/b}."
    eri "Which is perfect for playing games on my handheld!"
    show erik 1
    show player 641
    player_name "Hmm, why do you need it dark and quiet?"
    show player 642
    show erik 5
    eri "I err... I dunno."
    show erik 4
    eri "It's just more peaceful I guess!"
    show erik 5
    eri "You want me to help you carry that?"
    show erik 1
    show player 641
    player_name "Nah, I've got it."
    player_name "What game are you playing-"
    show player 642
    show erik 1b
    dex "Aww, C'mon {b}Becca{/b} just lemme get a peek..."
    player_name "..."
    show erik 3b
    eri "Wait a second. Was that {b}Dexter{/b}?"
    show erik 52
    show player 641
    player_name "Yeah, it sounds like him..."
    show player 642
    show erik 3b
    eri "What the heck is he doing in the auditorium?"
    show erik 52
    show player 641
    player_name "No idea..."
    player_name "We should check it out!"
    show player 642
    show erik 3b
    eri "... Ehh, really?"
    show erik 52
    show player 641
    player_name "Yeah, man. C'mon!"
    hide player
    hide erik
    with dissolve
    scene expression "backgrounds/location_school_assembly_hall_cutscene08.jpg"
    with fade
    show text "What was going on in the assembly hall?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause
    scene assembly_hall_paint02_c
    show dexter 34
    show becca 2 at left
    with dissolve
    becca "{b}Dexter{/b} stop it!"
    becca "Ugh, is this what you called me in here for?!"
    show becca 1
    show dexter 35
    dex "Huh?!"
    dex "What's the problem?"
    dex "{b}Roxxy{/b} and I are on a break and you're always wearing those low cut tops with your tits hanging out anyways..."
    dex "Just let me see em for a second."
    show dexter 34
    show becca 2
    becca "No way!"
    becca "We're at school!"
    becca "... And even if we weren't. I don't like you that way."
    show becca 1
    show dexter 35
    dex "Psh, stop pretending you don't want it..."
    show dexter 34
    show becca 2
    becca "I'm not pretending anything!"
    show becca 1
    show dexter 36
    dex "Hey, what's that on you're jeans?!"
    show becca 14 at Position (xoffset=86) with dissolve
    becca "Hmm?"
    show dexter 37 at left
    hide becca
    with dissolve
    becca "Ouch! What the fuck, {b}Dexter{/b}!"
    show becca 14 at left
    show becca 14 at Position (xoffset=86)
    hide dexter
    show dexter 35
    with dissolve
    dex "Hahaha, I've always thought you had a great butt..."
    show dexter 34
    hide becca
    show dexter 38 at left
    with dissolve
    becca "God damnit. I'm leaving!"
    show dexter 40 with dissolve
    dex "Hey!"
    dex "You aren't going anywhere 'till I see those tits!"
    show dexter 39
    becca "What the hell is with you today?!"
    becca "I said no!"
    show dexter 40
    dex "Nobody tells me no!"
    scene black with fade
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 12f at right
    show erik 51f
    with dissolve
    player_name "We have to do something!"
    show player 90f
    show erik 3bf
    eri "B-but... {b}Dexter{/b} will kill us!"
    show erik 51f
    show player 12f
    player_name "We can't just stand here! C'mon!"
    hide player
    hide erik
    with dissolve
    scene assembly_hall_paint02_c
    show erik 51 at Position (xpos=950)
    show player 12f at Position (xpos=775)
    show dexter 34 at Position (xpos=400)
    show becca 16 zorder 1 at left
    with dissolve
    player_name "Back off her!"
    show player 90f
    show dexter 24 at Position (xoffset=47)
    dex "Hmm?!"
    show dexter 23 at Position (xoffset=47)
    show becca 17 with dissolve
    becca "Screw you, {b}Dexter{/b}!"
    hide dexter
    show becca 18
    dex "Ghhurt!" with hpunch
    show dexter 41 at Position (xoffset=-80)
    show becca 2b
    with dissolve
    becca "Asshole!"
    show becca 19
    hide dexter with dissolve
    dex "*Cough*"
    hide player
    show becca 21f at Position (xpos=421)
    with dissolve
    player_name "!!!"
    show erik 3b
    eri "Holy crap!"
    show erik 52
    show becca 19 at Position (xpos=400)
    show player 10f at Position (xpos=775)
    with dissolve
    player_name "{b}Becca{/b}, are you okay?"
    show player 11f
    show becca 20
    becca "{b}[firstname]{/b}!!!"
    becca "I was just... I mean, {b}Dexter{/b} was..."
    show becca 19
    show player 12f
    player_name "I know. We saw it..."
    show player 5f
    becca "..."
    show erik 4
    eri "You just kicked his nuts to the moon!"
    eri "That was awesome!"
    show erik 1
    show becca 20
    becca "... It was?"
    show becca 19
    show player 14f
    player_name "Haha, totally."
    show player 13f
    dex "Ugh... {b}*Cough* *Sputter*{/b}"
    show player 12f
    player_name "... Are you sure you're okay though?"
    show player 5f
    show becca 20
    becca "{b}*Sniff*{/b} Yeah, I think so..."
    becca "I've never seen him act that way before!"
    show becca 19
    show player 12f
    player_name "Well don't worry. I don't think he'll try something like that again..."
    show player 14f
    show dexter 41 zorder 0 at Position (xpos=400) with dissolve
    player_name "... Man, you really got him good!"
    show player 13f
    dex "{b}*Cough*{/b} Uhh... My... Nads..."
    show roxxy 3cf at Position (xpos=75) with dissolve
    rox "What the hell is going on-"
    show roxxy 2cf
    rox "What's the matter with {b}Becca{/b}?"
    show roxxy 27f at Position (xoffset=34) with dissolve
    rox "..."
    show roxxy 28f at Position (xoffset=34)
    rox "... And why are you holding your balls, {b}Dexter{/b}?"
    show roxxy 27f at Position (xoffset=34)
    menu:
        "Tell {b}Roxxy{/b}.":
            show player 12f
            player_name "{b}Dexter{/b} was trying to force {b}Becca{/b} to flash him."
            show player 90f
            show becca 19f
            show roxxy 3cf
            with dissolve
            rox "... Seriously?"
            show roxxy 3bf
            show erik 3b
            eri "Yeah, we saw it."
            show erik 52
            show roxxy 3f
            rox "You idiot!"
            rox "What the hell's the matter with you?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Gasp* *Wheeze*{/b} ... Help."
            show dexter 41 at Position (xoffset=0)
            show becca 20f
            becca "{b}*Sniff*{/b} {b}[firstname]{/b} ran in and tried to stop him."
            show becca 19f
            show roxxy 2cf
            rox "You stood up to {b}Dexter{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Err, kinda..."
            show player 5f
            show roxxy 3cf
            rox "Are you nuts?"
            rox "You realize he would kill you, right?"
            show roxxy 3df
            show player 12f
            player_name "... No?"
            show player 90f
            show roxxy 2f
            rox "Uhh, yeah. He would absolutely destroy you."
            rox "Don't be stupid."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Uhh... You're so dead, {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Oh, shut up!"
            rox "You're not gonna do a damn thing!"
            show player 13f
            rox "If this gets out you'll be expelled for sure!"
            rox "... And that will be the least of your problems!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3f
            rox "Uh huh. That's what I thought."
            show roxxy 3cf
            rox "C'mon, {b}Becca{/b}. I'll walk you to the locker room."
            show roxxy 3df
            becca "..."
            show roxxy 3d with dissolve
            show becca 20f
            becca "Wait!"
            show becca 5 with dissolve
            pause
            show becca 22f at Position (xpos=457)
            hide player
            with dissolve
            show roxxy 3df
            player_name "!!!" with hpunch
            show becca 8 at Position (xpos=400)
            show player 13f at Position (xpos=775)
            with dissolve
            show roxxy 2bf
            becca "Thank you."
            show becca 7
            show roxxy 1f f
            show player 14f
            player_name "Heh, I didn't really do anything."
            show player 13f
            show becca 8
            becca "Yes, you did!"
            becca "I..."
            becca "... Just thanks!"
            hide becca
            hide roxxy
            with dissolve
        "Remain Silent.":

            show player 10f
            player_name "I uhh..."
            show player 5f
            player_name "..."
            show becca 20f with dissolve
            becca "{b}Dexter{/b} was forcing me to flash him!"
            show becca 19f
            show roxxy 3cf with dissolve
            rox "... Seriously?"
            show roxxy 3bf
            show erik 3b
            eri "Yeah, we saw it."
            show erik 52
            show roxxy 3f
            rox "You idiot!"
            rox "What the hell's the matter with you?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Gasp* *Wheeze*{/b} ... Help."
            show dexter 41 at Position (xoffset=0)
            show becca 20 with dissolve
            becca "{b}*Sniff*{/b} {b}[firstname]{/b} ran in and tried to stop him."
            show becca 19f with dissolve
            show roxxy 2cf
            rox "You stood up to {b}Dexter{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Err, kinda..."
            show player 5f
            show roxxy 3cf
            rox "Are you nuts?"
            rox "You realize he would kill you, right?"
            show roxxy 3df
            show player 10f
            player_name "... No?"
            show player 5f
            show roxxy 2f
            rox "Uhh, yeah. He would absolutely destroy you."
            rox "Don't be stupid."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Uhh... You're so dead, {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Oh, shut up!"
            rox "You're not gonna do a damn thing!"
            rox "If this gets out you'll be expelled for sure!"
            show player 5f
            rox "... And that will be the least of your problems."
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3cf
            rox "Uh huh. That's what I thought."
            rox "C'mon, {b}Becca{/b}. I'll walk you to the locker room."
            hide becca
            hide roxxy
            with dissolve
    show player 13f
    player_name "..."
    show erik 3b
    eri "... So, you're really friends with them now, huh?"
    show erik 52
    show player 14 at Position (xpos=700) with dissolve
    player_name "Yeah, kind of."
    show player 13
    show erik 4
    eri "That's so awesome, dude!"
    show erik 1
    show dexter 41 at Position (xoffset=2)
    dex "{b}*Whimper*{/b}"
    show dexter 41 at Position (xoffset=0)
    show player 11
    show erik 3b
    eri "... Uhh, we should probably get out of here."
    show erik 52
    show player 12
    player_name "Yeah, let's go."
    hide player
    hide erik
    with dissolve
    scene school
    show player 13 at left
    show erik 4
    with dissolve
    eri "... So what happened after the fake ID?"
    show erik 1
    show player 14
    player_name "I don't think I can say..."
    player_name "... But I've been helping {b}Roxxy{/b} out with some personal stuff."
    show player 13
    eri "..."
    show erik 4
    eri "Oooh, I get it. Ten four, dude."
    eri "I hear what your saying."
    show erik 1
    show player 14
    player_name "Heh, what? I don't think you do..."
    show player 13
    show roxxy 3c at right with dissolve
    rox "Well, that was a mess..."
    show roxxy 3d
    show erik 1f with dissolve
    show player 10
    player_name "Is {b}Becca{/b} doing okay?"
    show player 5
    show roxxy 33 with dissolve
    rox "Yeah, she's fine."
    rox "She was just a bit shocked is all."
    show roxxy 30 with dissolve
    rox "I can't believe {b}Dexter{/b} did that!"
    rox "I mean, he's done a lot of stupid shit in the past..."
    show roxxy 3c
    rox "... But never anything creepy!"
    show roxxy 3d
    show player 10
    player_name "Well, I'm just glad {b}Erik{/b} and I were there..."
    show player 5
    show roxxy 2
    rox "... Who's {b}Erik{/b}?"
    show roxxy 1
    show erik 2f with dissolve
    eri "..."
    show player 12
    player_name "Umm, my friend {b}Erik{/b}..."
    show player 90
    show roxxy 1b
    rox "Oh, right!"
    rox "Sorry, I forgot you were there."
    show roxxy 1
    show erik 3bf with dissolve
    eri "... That's okay."
    show erik 1f
    show roxxy 1b
    rox "So uhh, I was gonna tell you..."
    rox "The girls and I are doing a bikini contest this weekend and you should totally come!"
    show roxxy 1
    show erik 51f
    show player 10
    player_name "Really?"
    show player 14
    player_name "That sounds awesome!"
    show player 13
    show roxxy 2
    rox "I know right?!"
    show roxxy 1b
    rox "Just come to the beach on {b}Saturday afternoon{/b}!"
    show roxxy 1
    show erik 1f
    show player 14
    player_name "Alright, I'll be there."
    show player 13
    show roxxy 1b
    rox "Heh, cool."
    rox "See ya, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    pause
    show erik 4 with dissolve
    eri "Whoa, dude!"
    eri "A bikini contest?!"
    eri "That's so awesome!"
    show erik 1
    show player 14
    player_name "You wanna come with me?"
    show player 13
    show erik 3b
    eri "Aww, I can't."
    eri "I wish I could but I've got a raid with my guild {b}Saturday afternoon{/b}..."
    show erik 52
    show player 12
    player_name "Skip it!"
    show player 14
    player_name "C'mon man, think about all those bikinis!"
    show player 13
    show erik 3b
    eri "Are you nuts?! I can't skip a raid!"
    eri "That's a 50 DKP MINUS!"
    show erik 52
    show player 10
    player_name "... Huh?"
    show player 5
    show erik 3b
    eri "It's a big deal, dude!"
    show erik 52
    show player 14
    player_name "Heh, alright. Fine."
    player_name "I guess, I'll go by myself then..."
    show player 13
    show erik 3b
    eri "Shoot, I've gotta get to computer lab."
    show erik 3
    eri "I'll catch you later, dude."
    show erik 4
    show player 14
    player_name "See you around, {b}Erik{/b}."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
