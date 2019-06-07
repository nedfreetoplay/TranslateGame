label dexter_fight_pre:
    if game.cheat_mode:
        menu:
            "Skip minigame (Cheat)":
                $ renpy.call('dexter_fight_success', 0)
            "Play minigame":
                call screen dexter_fight
    call screen dexter_fight

label dexter_fight_minigame_prepare:
    scene school
    show becca 2 at Position (xpos=315)
    show roxxy 32 at Position (xpos=600)
    show missy 2b at left
    with dissolve
    becca "... And he wasn't there when you checked?"
    show becca 1
    show roxxy 33
    rox "Nope."
    show roxxy 32
    show becca 3
    show missy 2
    missy "Her {b}mom{/b} said he was there, {b}Becca{/b}."
    show missy 2b
    show becca 3b
    becca "Yeah, but... Was she drinking?"
    show becca 1
    show missy 3
    show roxxy 33
    rox "{b}*Sigh*{/b} It's my {b}mom{/b}. Of course she was drinking... She's always drinking!"
    show roxxy 33b
    show missy 4d
    with dissolve
    missy "..."
    show becca 2
    becca "Sorry, I didn't mean to..."
    show becca 1
    show missy 2b
    show roxxy 33
    with dissolve
    rox "No, it's okay."
    rox "I know what you're saying."
    rox "I'm just worried."
    rox "You know better than anyone that {b}Dexter{/b} has been getting more and more aggressive since we broke up."
    show roxxy 32
    becca "..."
    show roxxy 33
    rox "If {b}Dexter{/b} thinks that I'm dating {b}[firstname]{/b}... Who knows what he'll do?"
    show roxxy 32
    show missy 1b
    missy "... Are you dating, {b}[firstname]{/b}?"
    show missy 1
    show roxxy 28
    rox "I..."
    show roxxy 27
    pause
    show roxxy 1l
    rox "... I don't know, okay?"
    show roxxy 1k
    show becca 2
    becca "How can you not know?"
    show becca 1
    show roxxy 28
    rox "I mean..."
    show roxxy 27
    pause
    show roxxy 1l
    rox "{b}*Sigh*{/b} Look, I like him, right?!"
    rox "He's sweet and funny. He takes care of me and my {b}mom{/b}..."
    show roxxy 1k
    show becca 8
    becca "... And he's handsome."
    show becca 7
    show roxxy 1l
    rox "Huh?"
    rox "Since when do you think he's handsome?"
    show roxxy 1k
    show becca 8
    becca "... Since the {b}Dexter{/b} incident."
    show becca 7
    rox "..."
    show roxxy 1f
    rox "Heh. Yes, he's handsome."
    show roxxy 1e
    show becca 3
    show missy 8
    missy "... And he's got a huge cock!"
    show missy 7
    show roxxy 1i
    rox "!!!"
    show roxxy 1e
    show becca 3b
    becca "Shh! People will hear you, stupid!"
    show becca 3
    show missy 2
    missy "Oh, right... Sorry."
    show missy 8
    missy "... It is big though."
    show missy 7
    show becca 7
    show roxxy 1f
    rox "Yes, we know it's big!"
    show roxxy 1e
    show becca 2
    becca "So what's the problem?!"
    show becca 1
    show roxxy 2 at Position (xpos=567) with dissolve
    rox "You mean other than my psycho ex-boyfriend?"
    show roxxy 1
    show missy 8
    missy "You should totally date, {b}[firstname]{/b}!"
    show missy 7
    show becca 3b
    becca "I just said that!"
    show becca 3
    show missy 2
    missy "You did?"
    show missy 8
    missy "Okay, well... You should date him AND let us play with him!"
    show missy 7
    show becca 7
    becca "..."
    show roxxy 2
    rox "Man, you are some greedy bitches! You know that?"
    show roxxy 1
    becca "..."
    show missy 8
    missy "... But we're your greedy bitches though!"
    show missy 7
    show roxxy 4
    rox "Heh, yeah I know."
    show roxxy 2
    rox "First, we have to figure out this {b}Dexter{/b} situ-"
    show roxxy 2b
    dex "There's the whore!" with hpunch
    show becca 19
    show missy 3
    show roxxy 2bf at Position (xpos=500)
    with dissolve
    rox "!!!"
    show dexter 12d at right with dissolve
    dex "Shouldn't you be off sucking your new loser boyfriends dick or something?!"
    show dexter 12c
    show roxxy 3f
    rox "Excuse me?!"
    show roxxy 3bf
    show dexter 12d
    dex "You heard me, whore!"
    show dexter 12c
    show roxxy 3f
    rox "Don't you fucking talk to me like that!"
    show roxxy 3bf
    show dexter 12d
    dex "I saw you!"
    dex "... Kissing that nerd in your shitty little trailer!"
    show dexter 12c
    show roxxy 2bf
    rox "!!!"
    show roxxy 3cf
    rox "That's none of your business {b}Dexter{/b}!"
    show roxxy 3f
    rox "We're broken up, stupid!"
    show roxxy 3bf
    show dexter 12d
    dex "Grr, I'm not stupid!"
    show dexter 14 with dissolve
    show roxxy 3f
    rox "So what? You're gonna hit me now?"
    show roxxy 3bf
    show dexter 15
    dex "That's right."
    dex "I'm gonna do what I should have done a long time ago..."
    show dexter 14
    show becca 23 at Position (xpos=340)
    hide missy
    show missy 4b at Position (xpos=220)
    show roxxy 2bf at Position (xpos=80)
    with dissolve
    show dexter 12b with dissolve
    dex "!!!"
    show roxxy 3bf
    show dexter 15 with dissolve
    dex "Get outta my way you cunts!"
    show dexter 14
    pause
    show dexter 12d
    dex "I said move!" with hpunch
    show dexter 12c
    show missy 4c with dissolve
    show becca 19
    show erik 53f at Position (xpos=500) with dissolve
    show roxxy 2bf
    show missy 3 with dissolve
    eri "Step away from the girls!"
    show erik 50f
    dex "..."
    show dexter 12 with dissolve
    dex "What the hell did you just say, runt?!"
    show dexter 11
    show erik 3bf
    eri "I err..."
    show erik 5f
    eri "S-step away from them..."
    show erik 52f
    show roxxy 3cf
    rox "Are you crazy?!"
    rox "Get out of here!"
    show roxxy 3df
    show erik 5bf
    eri "... No!"
    eri "I can't just stand here and watch him hurt girls..."
    eri "Especially, not my best friend's girl!"
    show erik 3bf
    show roxxy 2bf
    rox "!!!"
    becca "..."
    show becca 3
    show missy 2
    missy "Who's that?!"
    show missy 2b
    show becca 3b
    becca "It's {b}[firstname]'s{/b} friend..."
    show becca 3
    show missy 1b
    missy "Oooh..."
    show missy 3
    show becca 19
    show dexter 12
    dex "Well, what are you going to do about it?!"
    dex "Dweeb!"
    show dexter 11
    show erik 2f at Position (xoffset=20) with dissolve
    eri "..."
    show erik 3f with dissolve
    eri "{b}*Sigh*{/b} I can't back down!"
    eri "{b}[firstname]{/b} wouldn't back down!"
    show erik 3bf
    show dexter 12
    dex "Yeah, well. {b}[firstname]{/b} isn't here fat boy!"
    dex "It's just you and me."
    show dexter 11
    show erik 4f
    eri "!!!"
    show erik 67f with dissolve
    eri "I didn't want to do this {b}Dexter{/b}..."
    eri "... But you leave me no choice."
    show erik 68f with dissolve
    eri "Today, you face {b}Erik the Mighty{/b}!"
    eri "Champion of Orcette and master of the Sacred Cod Piece!"
    show erik 69f with dissolve
    eri "Tremble in fear cretin, for you behold your own DOOM!"
    show becca 2b with dissolve
    rox "..."
    becca "..."
    show missy 2
    missy "Is he for real?"
    show missy 3
    show becca 19 with dissolve
    show erik 70f with dissolve
    eri "By Rak'thar's hammer, by the suns of Whorevan, you shall be avenged!"
    pause
    hide dexter
    show erik 71f
    with hpunch
    pause
    hide erik
    show dexter 12 at right with dissolve
    dex "HAHAHAHAHA!"
    show dexter 22
    dex "Nice speech, NERD!"
    show dexter 11
    show roxxy 3f
    rox "Jesus, {b}Dexter{/b}! You're such an asshole!"
    show roxxy 3bf
    show dexter 12
    dex "Yeah, so?"
    dex "You used to like this kinda stuff..."
    show dexter 11
    show roxxy 3f
    rox "Well, I don't anymore!"
    rox "Just leave us alone!"
    show roxxy 3bf
    show dexter 15 with dissolve
    dex "I don't think so..."
    dex "Nobody dumps me!"
    dex "I'm gonna teach you some respect-"
    show dexter 14
    show player 15 at Position (xpos=500) with dissolve
    player_name "Back off!"
    show player 16
    show roxxy 2bf
    dex "!!!"
    rox "!!!"
    show missy 1b
    missy "{b}[firstname]{/b}!"
    show missy 1
    show becca 2b with dissolve
    becca "{b}*Gasp*{/b}"
    show dexter 12d with dissolve
    dex "So the coward finally decides to show his face."
    hide player
    show dexter 16 at left
    with dissolve
    pause
    show dexter 17 at right with dissolve
    pause
    show player 10 at Position (xpos=500)
    show dexter 18 at Position (xpos=1175)
    with dissolve
    show player 113
    player_name "You girls okay?"
    show player 114
    show becca 20
    becca "... Yeah."
    show becca 19
    show missy 8
    missy "We are now."
    show missy 7
    show roxxy 2cf
    rox "I'm not!"
    show missy 3
    rox "What the hell are you doing?!"
    rox "He'll kill you!"
    show roxxy 2bf
    show player 12
    player_name "No he won't."
    player_name "Not this time."
    hide player
    show dexter 16 at left
    with dissolve
    pause
    show dexter 16b at right with dissolve
    pause
    show dexter 16bf with dissolve
    pause
    show dexter 42
    show player 16 at Position (xpos=500)
    with dissolve
    show roxxy 2cf
    rox "{b}[firstname]{/b}!!!"
    show roxxy 2bf
    show player 15
    player_name "It's alright, I've got this!"
    player_name "Just grab {b}Erik{/b} and get out of here!"
    show player 16
    show becca 20
    becca "We're on it!"
    hide missy
    hide becca
    with dissolve
    show roxxy 2cf
    rox "I'm not leaving you!"
    show roxxy 2bf
    hide player
    show dexter 16 at left
    pause
    show player 90 at Position (xpos=500)
    show dexter 12d at right
    with dissolve
    dex "Quit dancing and fight me you little shit!"
    show dexter 14 with dissolve
    show player 16
    player_name "( This is it! It's time to put up or shut up! )"
    hide player
    hide dexter
    hide roxxy
    with dissolve
    call screen dexter_fight

label dexter_fight_success(dexter_health):
    show screen dexter_fight_win(dexter_health/2)
    pause
    hide screen dexter_fight_win
    scene expression "backgrounds/location_school_cutscene05.jpg"
    with fade
    show text "The bigger they are...\nThe harder they fall!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show player 24 at left
    show becca 5f at Position (xpos=500)
    show missy 1f at Position (xpos=700)
    show dexter 47 at Position (xpos=950)
    with dissolve
    rox "{b}[firstname]{/b}, you did it!"
    hide player
    show roxxy 59d at left
    with dissolve
    show becca 6f
    becca "Holy shit!"
    show becca 5f
    show missy 4f
    missy "FINISH HIM!"
    show missy 4bf
    show roxxy 59b
    player_name "..."
    show dexter 49 with dissolve
    dex "Ugh..."
    show dexter 47 with dissolve
    show roxxy 59c
    player_name "... No."
    player_name "He's not worth it."
    show roxxy 59b
    show dexter 49 with dissolve
    dex "... Why can't I hit you?!"
    show dexter 48
    show roxxy 59c
    player_name "You're days of bullying my friends are over, {b}Dexter{/b}..."
    player_name "{b}Roxxy{/b} isn't your girl anymore!"
    show roxxy 59b
    dex "..."
    show roxxy 59c
    player_name "You hear me, asshole?!"
    show roxxy 59b
    show missy 3 at Position (xpos=650)
    show becca 5
    with dissolve
    show dexter 49
    dex "Tssh! I fucking hear you, alright?!"
    dex "This isn't over, {b}[firstname]{/b}!"
    dex "I dunno who taught you all that ninja bullshit but you haven't heard the last of me!"
    show dexter 48
    show roxxy 59c
    player_name "That's fine."
    player_name "You want another ass beating, I'll be more than happy to oblige."
    player_name "... But if I ever catch you threatening {b}Roxxy{/b} and her friends again... You won't get off this easily!"
    show roxxy 59b
    show dexter 47 with dissolve
    dex "Grr!"
    hide dexter with dissolve
    pause
    show roxxy 59d
    show missy 8f at Position (xpos=700)
    show becca 5f
    with dissolve
    missy "That was so bad ass!"
    show missy 7f
    show becca 6f
    becca "It really was!"
    show becca 5f
    show roxxy 59e
    player_name "Sorry I was late..."
    show roxxy 59d
    rox "..."
    show roxxy 92 at Position (xoffset=0) with dissolve
    pause
    show becca 7f
    show missy 8f
    missy "Oooh!"
    show missy 7f
    show becca 8f
    becca "Get it girl!"
    show becca 7f
    pause
    show roxxy 59d with dissolve
    rox "That was so freakin' hot!"
    show roxxy 59e
    player_name "Heh, oh yeah?"
    show roxxy 59d
    rox "Totally!"
    rox "I kinda wanna rip those clothes off you right now!"
    show roxxy 59e
    player_name "... You do?!"
    show roxxy 59d
    rox "Mmmhmm."
    show missy 8f
    missy "Can we watch?!"
    show missy 7f
    becca "..."
    show roxxy 92 with dissolve
    pause
    smi "What is all this commotion?!"
    show becca 19 at Position (xpos=475)
    show missy 3 at Position (xpos=625)
    show player 11 at left
    show roxxy 2cf at Position (xpos=150)
    with dissolve
    rox "Oh, shit!"
    show roxxy 2bf
    show principal 27 at right with dissolve
    smi "Do I need to remind you kids about this school's strict no public display of affection policy?!"
    show principal 26
    show player 10
    player_name "No, ma'am."
    show player 5
    show roxxy 33f
    rox "Sorry, {b}Mrs. Smith{/b}..."
    show roxxy 32f
    show missy 8
    missy "Aww, but it was just getting good!"
    show missy 7
    show principal 3b at Position (xoffset=70) with dissolve
    smi "!!!"
    show principal 27 with dissolve
    smi "Is that back talk I'm hearing?!"
    show principal 29
    show missy 3
    missy "!!!"
    show missy 4c at Position (xoffset=13) with dissolve
    missy "What, no! I mean..."
    show missy 4d at Position (xoffset=13)
    show becca 3b
    becca "Haha, nice going {b}Missy{/b}..."
    show becca 3
    show missy 4
    missy "Shut up, {b}Becca{/b}!"
    show missy 4b
    show becca 19
    show principal 27
    smi "That's enough!"
    show missy 3
    show roxxy 2bf
    smi "Both of you report to my office at once!"
    show principal 29
    show becca 20
    becca "Oh man..."
    show becca 19
    show missy 4
    missy "... Crap!"
    hide missy
    hide becca
    with dissolve
    show principal 28 at Position (xoffset=70) with dissolve
    smi "As for you two, you'd better get your butts to class unless you wanna join them?!"
    show principal 29 with dissolve
    show roxxy 33f
    rox "Yes, ma'am."
    show roxxy 32f
    show player 10
    player_name "We're going!"
    show player 5
    show principal 27
    smi "Hmph!"
    hide principal with dissolve
    pause
    show roxxy 1h at center with dissolve
    rox "... She's such a bitch."
    show roxxy 1g
    show player 14
    player_name "Heh, yeah."
    player_name "We'd better get to class though."
    show player 13
    show roxxy 1b
    rox "{b}*Sigh*{/b} Yeah, I suppose you're right."
    show roxxy 1
    pause
    show roxxy 1b
    rox "... Umm, before you go..."
    show roxxy 1
    show player 14
    player_name "Yeah?"
    show player 13
    show roxxy 1h
    rox "Why don't you come by my place tonight?"
    rox "We can pick up where we left off last time..."
    show roxxy 1g
    show player 29 with dissolve
    player_name "{b}*Gulp*{/b} Y-yeah... Okay!"
    show player 13 with dissolve
    show roxxy 1h
    rox "Hehe, see you {b}tonight{/b} then, stud."
    show roxxy 1g
    show player 17 with dissolve
    player_name "See ya."
    hide player
    hide roxxy with dissolve
    $ M_roxxy.trigger(T_roxxy_ninja_dexter)
    $ game.main()

label dexter_fight_fail(dexter_health):
    show screen dexter_fight_fail(dexter_health/2)
    pause
    hide screen dexter_fight_fail
    scene school
    show roxxy 2bf at left
    show dexter 12d at right
    with dissolve
    dex "This is what you left me for?"
    dex "Some nerdy little bitch?!"
    show dexter 12c
    show roxxy 2cf
    rox "... {b}[firstname]{/b}! Get up!"
    show roxxy 2bf
    show dexter 15 with dissolve
    dex "Not so handsome now, is he?"
    show roxxy 2cf
    rox "{b}[firstname]{/b}! Please!"
    show roxxy 33bf at Position (xoffset=34)
    show dexter 12
    with dissolve
    dex "HAHAHAHA!"
    scene black with fade
    pause





    call screen confirm(_('GAME OVER...'),
                        background='menu_condom',
                        no_action=(Hide('confirm'), Jump('dexter_fight_pre')),
                        no_text='Retry',
                        yes_action=ShowMenu('load'),
                        yes_text='Load')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
