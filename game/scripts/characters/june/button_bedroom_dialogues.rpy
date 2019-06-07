label june_bedroom_dialogue_cosplay_sex_pre:
    scene bedroom_sex2
    show player_sitting 2 zorder 1 at right
    show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
    with fastdissolve
    player_name "So, what're we doing?"
    show june_sitting 10
    show player_sitting 5
    june "Is your door locked?"
    show june_sitting 11
    show player_sitting 2
    player_name "Uhh... I think so? Why?"
    show june_sitting 12
    show player_sitting 5
    june "Well, I don't want your parents seeing me while I'm getting dressed up!"
    show june_sitting 11
    show player_sitting 4
    player_name "Oh, you're doing it... right... here?"
    show june_sitting 10
    show player_sitting 5
    june "Of course, silly!"
    june "I might need your help while I put things on..."
    june "And I want your opinion on the whole process!"
    show player_sitting 3
    june "My cosplay has to look just right."
    show june_sitting 11
    show player_sitting 4
    player_name "I see."
    player_name "So... How do we start?"
    show june_sitting 10
    show player_sitting 5
    june "I should probably get undressed first."
    show june_sitting 11
    player_name "..."
    show june_sitting 10
    june "Hold on, let me just get these clothes off..."
    show june_sitting 14 at Position(xoffset=7) with fastdissolve
    pause
    show player_sitting 7
    show june_sitting 15 with fastdissolve
    pause
    show june_sitting 16 at Position(xpos=288) with fastdissolve
    show player_sitting 10 with hpunch
    pause
    show june_sitting 19
    show june_sitting_underwear zorder 2 at Position(xpos=268,ypos=595)
    with fastdissolve
    june "..."
    show june_sitting 20
    june "Ha ha!"
    show player_sitting 5 with fastdissolve
    june "You don't have to hide your eyes, silly!"
    show june_sitting 19
    show player_sitting 4
    player_name "I just... Didn't want-"
    show june_sitting 20
    show player_sitting 5
    june "It's fine, I want you to watch."
    show june_sitting 19
    show player_sitting 4
    player_name "Okay..."
    show june_sitting 20
    show player_sitting 3
    june "I need to remove ALL of my clothes..."
    hide june_sitting_underwear
    show june_sitting 23
    with fastdissolve
    pause
    show june_sitting 24 with fastdissolve
    pause
    show june_sitting 25 at Position(xoffset=40) with fastdissolve
    june "... If we want to make this cosplay right!"
    show june_sitting 19 with fastdissolve
    show player_sitting 4
    player_name "You... You look really good!"
    show june_sitting 22b at Position(xoffset=18)
    show player_sitting 3
    june "Thanks."
    show june_sitting 20
    june "Now, before I put on the actual costume, I need your help with something..."
    show june_sitting 19
    show player_sitting 4
    player_name "How can I help?"
    show player_sitting 11
    show june_sitting 26 at Position(xoffset=24) with fastdissolve
    june "I have to put on body paint... And there's some spots I just can't reach!"
    june "Here, take this and scoop some out with your fingers..."
    show june_sitting 19
    show player_sitting 12
    with fastdissolve
    player_name "Where do I start?"
    show june_sitting 22b at Position(xoffset=18)
    show player_sitting 13 with fastdissolve
    june "Just let your imagination do the work!"
    show black zorder 3 with dissolve
    show june_sitting 29
    show player_sitting 1
    player_name "... Are you sure you want paint down here too?"
    june "Don't be scared, get in there!"
    june "Ooh, that tickles..."
    hide black with dissolve
    june "So?"
    june "How do I look?"
    show june_sitting 28
    show player_sitting 2
    player_name "It's really... convincing!"
    player_name "You really look like an orcette, that's certain..."
    show june_sitting 29
    show player_sitting 5
    june "Do you feel... attracted to my new look?"
    show june_sitting 28
    show player_sitting 4
    player_name "You mean I-"
    show june_sitting 29
    show player_sitting 5
    june "Do you feel horny... looking at me?"
    show june_sitting 28
    show player_sitting 3
    player_name "..."
    show player_sitting 4
    player_name "I think you're very pretty... in green..."
    show june_sitting 29
    show player_sitting 3
    june "Why don't you come closer and kiss me, Chieftain?"
    hide player_sitting
    show june_sitting 31 at center
    with fastdissolve
    pause
    return

label june_bedroom_dialogue_cosplay_sex_intro:
    show junesex 2b
    hide june_sitting
    hide player_sitting
    with fade
    june "I want that big... chieftain cock..."
    june "... deep inside me!"
    show junesex 3b with fastdissolve
    june "Ahh..."
    show junesex 4b with fastdissolve
    june "Yess!"
    june "Bork me, {b}[firstname]{/b}!!"
    return

label june_bedroom_dialogue_sex_pre_cosplay:
    show june_sitting 3 at Position(xpos=300,ypos=787)
    show player_sitting 1 at right
    with dissolve
    june "Cool room!"
    june "I love your posters and figurines!"
    show june_sitting 4
    show player_sitting 2
    player_name "Ha ha, yeah, they're pretty nice."
    player_name "I've had them since I was a kid."
    player_name "They're sort of... geeky, I guess."
    show june_sitting 3
    show player_sitting 1
    june "I really like them!"
    show june_sitting 4
    show player_sitting 2
    player_name "Thanks."
    show june_sitting 3
    show player_sitting 1
    june "So... What do you wanna do?"
    show june_sitting 4
    return

label june_bedroom_dialogue_sex_pre_no_cosplay:
    show player_sitting 2 zorder 1 at right
    show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
    with fastdissolve
    player_name "So, what's the plan?"
    show june_sitting 10
    show player_sitting 1
    june "Is your door locked?"
    show player_sitting 2
    show june_sitting 11
    player_name "Yeah. I don't think [deb_char_name] will be bothering us."
    show june_sitting 10
    june "Cool."
    show player_sitting 1
    show june_sitting 12
    june "It's just that... I really like hanging out in your room..."
    show player_sitting 3
    june "It's so... cozy. I just feel like we can do anything we want, in secret..."
    show player_sitting 4
    show june_sitting 13
    player_name "I like it, too."
    show player_sitting 1
    show june_sitting 10
    june "So, what does my... orc chieftain want from me tonight?"
    show june_sitting 11
    return

label june_bedroom_dialogue_sex_normal_pre:
    show player_sitting 2 zorder 1 at right
    show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
    player_name "Do you want to... have sex?"
    show player_sitting 1
    show june_sitting 10
    june "Should I get my costume?"
    show player_sitting 4
    show june_sitting 11
    player_name "Eh, maybe another time?"
    show player_sitting 3
    show june_sitting 12
    june "Okay... I guess we can do it like this."
    show player_sitting 4
    show june_sitting 13
    player_name "You don't mind?"
    show player_sitting 3
    show june_sitting 10
    june "Role playing is really fun, but sure, I'm fine with it..."
    show june_sitting 14 at Position(xoffset=7) with fastdissolve
    pause
    show june_sitting 15 with fastdissolve
    pause
    show june_sitting 16 at Position(xpos=288) with fastdissolve
    pause
    hide june_sitting_underwear
    show june_sitting 23
    with fastdissolve
    pause
    show june_sitting 24 with fastdissolve
    pause
    show june_sitting 25 at Position(xoffset=40) with fastdissolve
    june "Well? What are you waiting for? I'm right here..."
    show june_sitting 30 at center
    hide player_sitting
    with fastdissolve
    pause
    return

label june_bedroom_dialogue_sex_cosplay_pre:
    show player_sitting 6 at right
    show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
    player_name "I could help you dress up like last time... and be your chieftain?"
    show player_sitting 3
    show june_sitting 10
    june "I was hoping you would suggest that!"
    june "All I've been thinking about is dressing up and becoming your orcette..."
    june "Okay, let put the costume on..."
    show june_sitting 29
    with fade
    june "Why don't you come closer... And kiss me, Chieftain?"
    hide player_sitting
    show june_sitting 31 at center
    with fastdissolve
    pause
    return

label june_bedroom_dialogue_play_games_cosplay_over:
    show june_sitting 11 at Position(xpos=300,ypos=787)
    show player_sitting 2 at right
    player_name "Do you want to play games again?"
    show june_sitting 10
    show player_sitting 1
    june "Sure, there's still some quests I haven't finished in Orc Bork."
    show june_sitting 11
    show player_sitting 6
    player_name "Let's do it!"
    show player_sitting 2
    player_name "Just one thing, could you tell me how to play it again?"
    show june_sitting 10
    show player_sitting 1
    june "Ha ha."
    june "Sure, come closer so you can see the screen better..."
    show june_sitting 7 at center
    hide player_sitting
    with fastdissolve
    june "We have to play together and time our attacks."
    june "When the arrow is in the green bar, press the button!"
    show june_sitting 8
    player_name "Oh, okay! Sounds pretty simple."
    show june_sitting 7
    june "Let's give it a try!"
    return

label june_bedroom_dialogue_play_games_cosplay_not_over:
    show june_sitting 4 at Position(xpos=300,ypos=787)
    show player_sitting 2 at right
    player_name "We could try beating that game of yours."
    show june_sitting 3
    show player_sitting 1
    june "Yeah? You really want to?"
    show june_sitting 4
    show player_sitting 6
    player_name "Let's do it!"
    show player_sitting 2
    player_name "Just one thing, could you tell me how to play?"
    show june_sitting 3
    show player_sitting 1
    june "Ha ha."
    june "Well, It's just one of those monster hunting games."
    june "You go through dungeons, kill monsters, get items..."
    show player_sitting 5
    june "... But there's this final boss I've been trying to beat for the longest time!!"
    show player_sitting 1
    june "Here, come closer so you can see the screen better..."
    show june_sitting 8 at center
    hide player_sitting
    with fastdissolve
    player_name "Okay, so how do we beat this boss?"
    show june_sitting 7
    june "We have to play together and time our attacks."
    june "When the arrow is in the green bar, press the button!"
    show june_sitting 8
    player_name "Oh, okay! Sounds pretty simple."
    show june_sitting 7
    june "Let's give it a try!"
    return

label june_bedroom_dialogue_leave:
    show player_sitting 4 at right
    show june_sitting 6 at Position(xpos=300,ypos=787)
    player_name "Actually, I should really get to bed..."
    show june_sitting 5
    show player_sitting 3
    june "Already?!"
    show june_sitting 6
    show player_sitting 4
    player_name "Yeah... [tmp_deb_name] said I need to get to bed earlier."
    player_name "Sorry, {b}June{/b}..."
    show june_sitting 5
    show player_sitting 3
    june "It's alright, I guess."
    june "Maybe we can hang out another time?"
    show june_sitting 6
    show player_sitting 4
    player_name "Sure!"
    show june_sitting 4
    player_name "I'd love to."
    show june_sitting 3
    show player_sitting 3
    june "Okay, see you at school?"
    show june_sitting 4
    show player_sitting 4
    player_name "Yeah!"
    hide june_sitting
    hide player_sitting
    with dissolve
    return

label june_bedroom_dialogue_normal_sex_intro:
    show junesex 2
    hide june_sitting
    hide player_sitting
    with fade
    june "I want that big cock of yours..."
    june "... deep inside me!"
    show junesex 3 with fastdissolve
    june "Ahh..."
    show junesex 4 with fastdissolve
    june "Yess!"
    june "Fuck me, {b}[firstname]{/b}!!"
    return

label june_bedroom_dialogue_cosplay_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("junesex", ["4b","5b","6b","7b","8b"], M_june) as junesex
                $ animated = True
            pause 8
        else:

            $ pose_counter = 0
            $ pose_list = ["4b","5b","6b","7b","8b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "junesex {}".format(pose_list[pose_counter]) as junesex
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1
    call screen june_mcbedroom_cosplay_sex_options

label june_bedroom_dialogue_normal_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("junesex", [4,5,6,7,8], M_june) as junesex
                $ animated = True
            pause 8
        else:

            $ pose_counter = 0
            $ pose_list = [4,5,6,7,]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "junesex {}".format(pose_list[pose_counter]) as junesex
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1
    call screen june_mcbedroom_normal_sex_options

label june_bedroom_dialogue_normal_sex_cum_inside:
    call expression game.dialog_select("june_bedroom_dialogue_normal_sex_cum_inside_dialogue")
    call expression game.dialog_select("june_bedroom_dialogue_aftercum_inside")
    $ game.main()

label june_bedroom_dialogue_normal_sex_cum_inside_dialogue:
    show expression AnimatedImage("junesex", [4,5,6,7,8], M_june) as junesex
    pause
    show junesex 9 with hpunch
    june "Ahh!!!"
    show white
    pause 0.3
    hide white with dissolve
    pause
    show junesex 14 with fastdissolve
    june "I... that feels so good..."
    june "... your cum deep inside me..."
    return

label june_bedroom_dialogue_normal_sex_cum_outside:
    call expression game.dialog_select("june_bedroom_dialogue_normal_sex_cum_outside_dialogue")
    call expression game.dialog_select("june_bedroom_dialogue_aftercum_outside")
    $ game.main()

label june_bedroom_dialogue_normal_sex_cum_outside_dialogue:
    show expression AnimatedImage("junesex", [4,5,6,7,8], M_june) as junesex
    pause
    show junesex 9 with hpunch
    player_name "Ahh!!!"
    show white
    pause 0.3
    show junesex 10
    hide white with dissolve
    pause
    show junesex 11 with fastdissolve
    june "..."
    show junesex 12
    june "So much..."
    june "I was hoping you would hold me down and cum inside..."
    june "... with all that strong cum..."
    june "Maybe next time?"
    return

label june_bedroom_dialogue_cosplay_sex_cum_inside:
    call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_cum_inside_dialogue")
    if not store._in_replay == None or June.over(june_cosplay):
        call expression game.dialog_select("june_bedroom_dialogue_aftercum_inside")
    else:
        call expression game.dialog_select("june_bedroom_dialogue_aftercum_initial")
    $ renpy.end_replay()
    $ persistent.cookie_jar["June"]["unlocked"] = True
    $ persistent.cookie_jar["June"]["gallery"]["01_unlocked"] = True
    $ June.complete_events(june_cosplay)
    $ game.main()

label june_bedroom_dialogue_cosplay_sex_cum_inside_dialogue:
    show expression AnimatedImage("junesex", ["4b","5b","6b","7b","8b"], M_june) as junesex
    pause
    show junesex 9b with hpunch
    june "Ahh!!!"
    show white
    pause 0.3
    hide white with dissolve
    pause
    show junesex 14b with fastdissolve
    june "I... that feels so good..."
    june "... your orc seed deep inside me..."
    june "... my chieftain..."
    return

label june_bedroom_dialogue_cosplay_sex_cum_outside:
    call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_cum_outside_dialogue")
    if not store._in_replay == None or June.over(june_cosplay):
        call expression game.dialog_select("june_bedroom_dialogue_aftercum_outside")
    $ renpy.end_replay()
    $ persistent.cookie_jar["June"]["unlocked"] = True
    $ persistent.cookie_jar["June"]["gallery"]["01_unlocked"] = True
    $ June.complete_events(june_cosplay)
    $ game.main()

label june_bedroom_dialogue_cosplay_sex_cum_outside_dialogue:
    show expression AnimatedImage("junesex", ["4b","5b","6b","7b","8b"], M_june) as junesex
    pause
    show junesex 9b with hpunch
    player_name "Ahh!!!"
    show white
    pause 0.3
    show junesex 10b
    hide white with dissolve
    pause
    show junesex 11b with fastdissolve
    june "..."
    show junesex 12b
    june "So much... cum!"
    june "I was hoping you would hold me down and cum inside..."
    june "... with all that strong orc cum..."
    june "Maybe next time?"
    return

label june_bedroom_dialogue_aftercum_initial:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    with fade
    june "That was great!"
    june "It's getting pretty late... I should get home."
    show player_sitting 6
    show june_sitting 11
    player_name "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "I think it was time well spent!"
    show june_sitting 11
    show player_sitting 4
    player_name "I had fun too."
    show june_sitting 10
    show player_sitting 3
    june "Maybe we can do this again soon?"
    show june_sitting 11
    show player_sitting 4
    player_name "Sure!"
    show player_sitting 6
    player_name "I'd love to."
    show june_sitting 10
    show player_sitting 3
    june "Okay, I'll see you at school then?"
    show june_sitting 11
    show player_sitting 4
    player_name "Yeah!"
    return

label june_bedroom_dialogue_aftercum_inside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    with fade
    june "That was great!"
    june "It's getting pretty late... I should get home."
    show player_sitting 6
    show june_sitting 11
    player_name "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "I think it was time well spent!"
    show june_sitting 11
    show player_sitting 4
    player_name "I had fun too."
    show june_sitting 13
    show player_sitting 4
    player_name "Hey, uh, about doing it inside..."
    show june_sitting 12
    show player_sitting 5
    june "Oh, don't worry about that, I'll just take a pill."
    show june_sitting 11
    show player_sitting 4
    player_name "Does that mean we can do this again soon?"
    show june_sitting 10
    show player_sitting 3
    june "That depends... Do you want to?"
    show player_sitting 6
    show june_sitting 11
    player_name "I'd love to."
    show june_sitting 10
    show player_sitting 3
    june "Okay, I'll see you at school then?"
    show june_sitting 11
    show player_sitting 4
    player_name "Of course!"
    return

label june_bedroom_dialogue_aftercum_outside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    with fade
    june "That was great!"
    june "It's getting pretty late... I should get home."
    show player_sitting 6
    show june_sitting 11
    player_name "Yeah, [deb_char_name] is going to get suspicious with all the time we spend in here..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "I think it was time well spent!"
    show june_sitting 11
    show player_sitting 4
    player_name "I had fun too."
    show june_sitting 10
    show player_sitting 3
    june "Maybe we can do this again soon?"
    show june_sitting 11
    show player_sitting 4
    player_name "Sure!"
    show player_sitting 6
    player_name "I'd love to."
    show june_sitting 10
    show player_sitting 3
    june "Okay, I'll see you at school then?"
    show june_sitting 11
    show player_sitting 4
    player_name "Of course!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
