label home_diane_checkup_results:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Thanks for going with me, {b}[firstname]{/b}."
    dia "You were so great today!"
    show diane f_normal
    show player 14
    player_name "No problem."
    player_name "I'm just glad we got good news."
    show player 13
    show diane f_normal_talk
    dia "Me too."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "We'll get started tomorrow, okay?"
    show diane f_normal
    show player 14
    player_name "Alright."
    show player 13
    show diane f_normal_talk
    dia "You'd better head up to bed and get a good nights sleep."
    show diane f_wink
    pause
    show diane f_smirk_talk
    dia "Lots of hard work waiting for you tomorrow, stud."
    show diane f_smirk
    show player 29 with dissolve
    player_name "{b}*Gulp*{/b} Y-yeah, okay."
    hide player
    hide diane
    with dissolve
    return

label home_front_mom_mrsj_visit:
    scene home_front
    show debbie 164f zorder 2 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Hey, {b}[deb_char_name]{/b}!"
    show debbie 165f
    show mrsj 14
    deb "Oh, hello there, {b}Tammy{/b}."
    show debbie 164f
    show mrsj 17
    mrsjo "I wanted to stop by and give my condolences for your loss. I know he was your close friend..."
    show debbie 165f
    show mrsj 14
    deb "Oh, thank you. That's very... thoughtful of you."
    show debbie 169f
    show mrsj 19
    mrsjo "I just want you to know that {b}Erik{/b} and I are right next door if you ever need anything."
    mrsjo "... Even if you just need to talk."
    show debbie 168f
    show mrsj 14
    deb "That's very generous."
    show debbie 169f
    show mrsj 17
    mrsjo "I know this is a completely different situation for you, but I can relate you know?"
    show debbie 168f
    show mrsj 14
    deb "You mean, because of your husband?"
    show debbie 169f
    show mrsj 17
    mrsjo "Of course!"
    show mrsj 20
    mrsjo "I mean, my husband walked out on me... So it's a bit different."
    show mrsj 18
    mrsjo "... But I was on my own for a long time!"
    show debbie 168f
    show mrsj 14
    deb "It gets lonely, doesn't it?"
    deb "It's not easy being all by yourself."
    show debbie 169f
    show mrsj 20
    mrsjo "Yeah, I had a rough time of it for awhile there..."
    show mrsj 17
    mrsjo "... But then I decided to sublet my house and ended up living with {b}Erik{/b}"
    mrsjo "He's been such a blessing!"
    show debbie 168f
    show mrsj 14
    deb "Oh, how so?"
    show debbie 169f
    show mrsj 17
    mrsjo "He's such a sweet young man and he needs me to take care of him!"
    show debbie 169bf
    mrsjo "It feels good to be needed like that again. It really gives me a sense of purpose, you know?"
    show debbie 169f
    mrsjo "I cook for him and do his laundry. I ask him about his day and show him affection when he needs it."
    show debbie 168f
    show mrsj 14
    deb "I see..."
    show debbie 169f
    show mrsj 18
    mrsjo "I think it's helping him come out of his shell too! So it's mutually beneficial!"
    show debbie 168f
    show mrsj 14
    deb "I just don't know how to talk to {b}[firstname]{/b}. I mean, I know he needs guidance but I'm not his Mother..."
    show debbie 169f
    show mrsj 17
    mrsjo "Well keep at it, Honey. It's not going to sort itself out overnight."
    mrsjo "Just focus on him and how he's feeling. It's what I did!"
    mrsjo "The rest will fall into place soon enough."
    show debbie 168f
    show mrsj 14
    deb "I hope you're right."
    show debbie 169f
    pause
    show player 1 zorder 1 at Position(xpos=300) with dissolve
    show debbie 165f
    deb "Oh! Hi, sweetie!"
    show debbie 164f
    show player 14
    player_name "Hey, {b}[deb_name]{/b}... Hi, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Hello there, {b}[firstname]{/b}."
    mrsjo "{b}[deb_char_name]{/b} was just telling me how happy she is that you came to live with her..."
    show mrsj 14
    show player 14
    player_name "Oh, yeah? I'm just thankful she was willing to take me in."
    show mrsj 17
    show player 13
    mrsjo "She's a good woman, so you had better take good care of her!"
    show mrsj 14
    show player 14
    player_name "I will!"
    show player 1
    show mrsj 17
    mrsjo "Hehe, See {b}[deb_name]{/b}? You guys are gonna be just fine!"
    mrsjo "Well, I'd best be getting home."
    show mrsj 14
    show debbie 165f
    deb "You sure you don't want to come in?"
    show debbie 164f
    show mrsj 17
    mrsjo "No, thanks! I should really get home and check on {b}Erik{/b}. See if there's anything he needs..."
    show mrsj 14
    show debbie 165f
    deb "Well, thanks for the chat {b}Tammy{/b}. Come see us again real soon!"
    show debbie 164f
    show mrsj 17
    mrsjo "I'll do that! You two take care of each other now, you hear?"
    hide mrsj
    hide debbie
    hide player
    with dissolve
    return

label home_front_mom_mow_lawn:
    show expression "backgrounds/location_home_grass_cutscene_01.jpg"
    show expression FilteredText("This is a lot harder than I expected. I should've paid more attention to how {b}Dad{/b} used to do it.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_02.jpg"
    show expression FilteredText("It doesn't look half bad. I Hope {b}[deb_name]{/b} thinks the same.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_03.jpg"
    show expression FilteredText("Hmm, I wonder how long she's been standing there? I was so focused I didn't notice her come out.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    pause 0.5

    scene home_front
    show player 2 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show debbie 1 at right
    with dissolve
    player_name "{b}[deb_name]{/b}, I finished the lawn."
    show player 203
    show debbie 2
    deb "I saw that. It looks great, sweetie!"
    show debbie 3
    deb "You did a wonderful job!"
    show debbie 2
    deb "I'm proud of you."
    show player 2
    show debbie 1
    player_name "I was just doing it the way I thought {b}Dad{/b} would."
    show player 11
    show debbie 2
    deb "Well, I'm sure he'd be proud too."
    deb "He always went out of his way to help me out around here."
    show player 21
    show debbie 1
    player_name "I will too, {b}[deb_name]{/b}. I feel like it's what he'd want."
    show player 2
    player_name "Should we go inside now?"
    show debbie 1
    deb "Sure!"
    scene home_front with None
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 10 zorder 1
    with dissolve
    player_name "{b}*Panting*{/b}"
    show player 14
    player_name "Wow, that was a lot of work!"
    show player 24
    player_name "I need to get out of these stinky clothes and shower now..."
    show player 4 at Position(xoffset=5)
    player_name "I should head {b}downstairs to put these clothes in the wash{/b}."
    hide player with dissolve
    return

label home_front_mom_car_fixed:
    scene expression game.timer.image("home_front_mechanic{}_b")
    show jai 2 at left
    show debbie 1 at right
    with dissolve
    jaing "Everything should be good as new, ma'am."
    show jai 1
    show debbie 3
    deb "Really? That was fast!"
    show debbie 1
    show jai 2
    jaing "You betcha!"
    jaing "I always work hard when a beautiful woman is involved!"
    jaing "You just give me a call if you have anymore trouble."
    jaing "I love making pretty little ladies engines purr. Know what I mean?"
    show jai 1
    show debbie 3
    deb "Oh, stop. You're hilarious!"
    deb "Ha Ha Ha."
    show jai 2
    jaing "Huck Huck Huck."
    show jai 1
    show debbie 1
    show player 14 zorder 1
    player_name "Hey, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "There he is!"
    show debbie 1
    show player 10f with dissolve
    player_name "Engine repairs all finished?"
    show player 5f
    show jai 2
    jaing "Well, I had to replace the whole damn thing, but yeah. It's all finished."
    jaing "Just another day in the life of {b}Jiang{/b} the Car Whisperer. No need to thank me."
    show player 11f
    jaing "Huck Huck."
    jaing "We'll I'd best be off!"
    show player 5f
    jaing "Just gonna take a quick peek under your hood to make sure I didn't leave my tool in her. Know what I mean?"
    show jai 1
    show debbie 2
    deb "{b}*Ahem*{/b} Yes, well. Thanks again!"
    show debbie 1
    show jai 2
    jaing "Not a problem, ma'am."
    hide jai with dissolve
    show player 13 with dissolve
    show debbie 2
    deb "Want to give it a test drive?"
    show debbie 1
    show player 14
    player_name "Sure!"
    show player 12
    player_name "I hope he's not trying to screw us over."
    show player 5
    show debbie 14
    deb "( He was trying to screw someone alright... )"
    hide player
    hide debbie
    with dissolve
    return

label home_front_mom_car_fixed_check_car:
    scene car_interior
    show debbie car 2b at right
    show player car 1b
    show player_arms car 1
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    deb "Let's see..."
    show player car 2b
    show debbie car 1
    hide debbie_arms_car
    with dissolve
    deb "Hmm..."
    show debbie car 2b
    show debbie_arms_car 1
    with dissolve
    deb "It works!"
    show debbie car 3
    show player car 2
    player_name "Great!"
    show player car 1
    show debbie car 2
    player_name "Sounds good, too."
    show player car 2b
    show debbie car 3b
    deb "How did you get them to come out so quickly?"
    show debbie car 3
    show player car 2
    player_name "It was nothing {b}[deb_name]{/b}."
    show player car 5
    player_name "I guess, I can be quite persuasive..."
    player_name "I'm just relieved to see you smiling again..."
    show player car 6
    pause
    show player car 5b
    show debbie car 3b
    show debbie_arms_car 2 with dissolve
    deb "Aww..."
    deb "Thanks, sweetie."
    scene car_interior kiss
    hide player car
    hide debbie_arms_car
    hide player_arms car
    show debbie car 6 at right
    show xtra 30 at right
    with dissolve
    pause
    show player_boner car 1 with dissolve
    pause
    scene car_interior
    show player car 3b
    show player_arms car 2
    show debbie car 3 at right
    show debbie_arms_car 2
    show xtra 30 at right
    show player_boner car 1
    with dissolve
    pause
    show debbie car 4c
    show debbie_arms_car 4 with dissolve
    deb "( !!! )"
    show debbie car 5b
    deb "Oh!"
    show debbie car 4c
    show player car 4c
    player_name "Sorry, {b}[deb_name]{/b}..."
    show player car 3
    show debbie car 5b
    deb "It's alright, sweetie."
    deb "You seem to be getting these quite often when I'm around."
    show debbie car 4b
    show debbie_arms_car 2 with dissolve
    deb "I'm not sure If I should be worried of flattered?"
    show debbie car 3
    show player car 4c
    show player_arms car 1 with dissolve
    player_name "I know... I'm really trying hard not to but you're just so pretty."
    show player car 3
    show debbie car 4
    deb "..."
    show debbie car 5b
    deb "Oh, sweetie..."
    hide player_boner car
    show debbie_arms_car 5b at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    deb "I suppose it's not such a bad thing."
    show debbie car 5
    show player car 4c
    player_name "{b}[deb_name]{/b}?"
    show player car 3
    show debbie car 3b
    deb "Shhh."
    show debbie car 5b
    show debbie_arms_car 5 with dissolve
    deb "It's normal for young men your age to get excited at the drop of a hat."
    show debbie car 5
    show player car 3b
    player_name "{b}*Gulp*{/b}"
    show player car 3
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    pause 1.2
    show debbie_arms_car 5 with dissolve
    show debbie car 5b
    deb "I really wish I could help you out with this, sweetie."
    deb "... But it just wouldn't be right."
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    show debbie car 3b
    deb "You need to find someone your own age..."
    deb "Someone cute to be your girlfriend. Wouldn't that be nice?"
    show debbie car 3
    show debbie_arms_car 5c with dissolve
    show player car 5
    player_name "Y-Yeah, okay..."
    show player car 5b
    show debbie car 3b
    deb "That's good."
    show debbie_arms_car 5 with dissolve
    deb "Do you want me to keep going?"
    show debbie car 3
    return

label home_front_mom_car_fixed_check_car_little_longer:
    show player car 5
    player_name "Can... Can you keep going a little longer?"
    show player car 2
    player_name "It feels so good!"
    show player car 2b
    show debbie car 3b
    deb "Alright, {b}[firstname]{/b} but I'm not going to finish you if that's what you're hoping for..."
    show debbie car 3
    return

label mom_car_jerk_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                $ animated = True
        else:

            $ pose_counter = 0
            $ pose_list = [5,"5b","5c","5b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1

        if animcounter == 1 or M_mom.get("jerk count") == 1:
            show debbie car 3
        else:
            show debbie car 4
            show player car 4b
        pause 2

        if animcounter == 3 and M_mom.get("jerk count") >= 1:
            show player car 4c
            pause 1
        $ animcounter += 1

    $ M_mom.set("jerk count", M_mom.get("jerk count") + 1)

    if M_mom.get("jerk count") == 2:
        jump expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")
    call screen car_mom_jerk_options

label home_front_mom_car_fixed_check_car_finished:
    if M_mom.get("jerk count") == 2:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_too_much")
    else:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_not_enough")
    call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_after")
    $ M_mom.trigger(T_mom_car_fun)
    $ game.timer.tick()
    $ game.main()

label home_front_mom_car_fixed_check_car_finished_too_much:
    show player car 3
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "I... I don't think I should keep doing this..."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "but, {b}[deb_name]{/b}-"
    show player car 3
    return

label home_front_mom_car_fixed_check_car_finished_not_enough:
    show player car 4c
    player_name "I guess we should probably stop, huh?"
    show player car 4b
    show debbie car 5
    deb "..."
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "That's a good idea, Sweetheart."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "... Yeah."
    show player car 5b
    return

label home_front_mom_car_fixed_check_car_finished_after:
    show debbie car 5b
    deb "If you feel yourself getting hard, you should go up to your room and take care of it."
    show debbie car 3b
    deb "...Okay, sweetie?"
    show debbie car 3
    show player car 4c
    player_name "... Yes, ma'am."
    scene black with fade
    hide debbie
    hide debbie_arms_car
    hide xtra
    hide player
    hide player_arms car
    hide player_boner car
    return

label home_front_mom_bad_guys_revisit:
    scene home_front_car
    $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
    show player 11f at right with dissolve
    player_name "!!!"
    player_name "( It's that car again! )"
    player_name "( ... with that creep who's been threatening {b}[deb_name]{/b}! )"
    hide player
    $ playSound()
    show expression "backgrounds/location_home_entrance_cutscene01.jpg"
    show expression FilteredText("As I looked through the window, I spotted the guy who'd been delivering all the threats.\nIt would seem he brought backup this time.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene02.jpg"
    show expression FilteredText("I couldn't hear what they were saying, but {b}[deb_name]{/b} looked terrified.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    play audio smack
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene03.jpg"
    show expression FilteredText("... Then one of the goons knocked her to the floor!") as cutscene at Position (xpos= 512, ypos= 700)
    with hpunch
    pause
    hide cutscene
    show expression FilteredText("There was no way I could just stand there and watch...\nI {b}had{/b} to do something!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene

    scene home_entrance_fight
    show debbie 40 at Position(xpos=156,ypos=768)
    show henchman2 1 at right
    with dissolve
    python:
        tmp = deb_name.upper()
    player_name "{b}[tmp]{/b}!!"
    show player 205 at Position(xpos=350,ypos=768) with dissolve
    player_name "What the hell's the matter with you?!"
    show player 204
    deb "{b}[firstname]{/b}, just leave it..."
    show player 205
    player_name "What kind of man hits a defenseless woman?!"
    show player 204
    show henchman2 2
    henchman2 "Don't be stupid, Kid. This doesn't concern you."
    show player 205
    show henchman2 1
    player_name "Back off! If you touch her again I'm going to-"
    show player 204
    show henchman2 3
    henchman2 "Hah! What are you gonna do?!"
    show henchman2 1
    player_name "..."
    show player 205
    player_name "I'm calling the cops and you can deal with-"
    show player 204
    show henchman2 3
    hide debbie with dissolve
    henchman2 "I don't think so."
    show henchman2 1
    hide player
    show henchman1 7 at Position(xpos=350,ypos=768) with hpunch
    player_name "Hey! Let go of me!"
    show henchman1 8
    hide henchman2
    show henchman2 3 at right
    henchman2 "Hahah, easy there, Killer..."
    henchman2 "Your {b}Father{/b} owed us a {b}LOT{/b} of money..."
    henchman2 "A {b}debt{/b} that now belongs to the two of you!"
    show henchman2 2
    henchman2 "... And you're going to pay up. Otherwise..."
    show henchman1 9
    show henchman2 5
    with hpunch
    deb "{b}[firstname]{/b}!!!"
    show henchman2 3
    show henchman1 10 at Position(xpos=340,ypos=768)
    henchman2 "As for the authorities..."
    show henchman2 2
    henchman2 "... I'd leave them out of it unless you want this to get {b}REAL{/b} messy!"
    henchman2 "If you care about your lives, you'll {b}bring the money{/b} to the {b}warehouse{/b} like you were told!"
    show henchman2 4
    henchman2 "You don't want us coming back here! {b}Got it{/b}, Lady?!"
    show player 184
    show henchman1 6f at left
    show henchman2 2
    with vpunch
    henchman2 "C'mon, let's get out of this dump."
    $ playMusic()
    hide henchman1
    hide henchman2
    with dissolve
    pause
    hide player
    show debbie 41 at left
    with dissolve
    deb "Easy, sweetie. I've got you."
    show debbie 44 at left
    show jenny 39 at right
    with dissolve
    jen "What the hell is going on?"
    jen "I heard screams and-"
    show jenny 40 at Position(xpos=0.885, ypos=1.0) with dissolve
    jen "( !!! )"
    jen "Oh God, is he okay?!"
    show debbie 43
    show jenny 43 at Position(xpos=1.0, ypos=1.0) with dissolve
    deb "He'll be alright. Just calm down..."
    deb "They're gone."
    show debbie 44
    show jenny 39
    jen "We need to call someone!"
    show jenny 43
    show debbie 43
    deb "NO! We can't do that!"
    show debbie 44
    show jenny 39
    jen "What?! {b}[deb_name]{/b} those men broke in here and assaulted you guys!"
    jen "We can't just let them-"
    show jenny 43
    show debbie 45
    deb "I said {b}NO{/b}, {b}[jen_name]{/b}!"
    show debbie 43
    deb "... Just..."
    deb "Go back to your room and let me handle this. Okay?"
    show debbie 44
    show jenny 39
    jen "I... Okay..."
    hide jenny
    with dissolve
    show debbie 41
    deb "It's gonna be alright, sweetie."
    show debbie 42
    player_name "Sorry. I couldn't stop them, {b}[deb_name]{/b}..."
    show debbie 41
    deb "Don't be sorry. It was very brave of you to try!"
    deb "You were trying to protect us."
    show debbie 42
    player_name "What are we going to do?"
    show debbie 41
    deb "Don't worry about that right now; We're safe."
    show debbie 42
    deb "..."
    show debbie 41
    deb "How's your face?"
    show debbie 42
    player_name "My nose hurts..."
    player_name "... And I'm bleeding everywhere."
    show debbie 41
    deb "Come on, let's get you cleaned up."
    hide debbie with dissolve
    scene shower2
    show debbie 39f at left
    show player 209f
    with dissolve
    deb "Looks like the bleeding stopped..."
    show debbie 63f
    deb "You should take a shower, sweetie."
    deb "It'll help with the swelling."
    show player 210
    deb "I'll go fetch you some clean clothes."
    show debbie 38f
    hide debbie
    hide player
    scene hallway
    show debbie 38
    with fade
    deb "( ... )"
    deb "( I feel like I should be in there with him... Making sure he's okay. )"
    deb "( Maybe it's better that I give him some privacy... )"
    deb "( I'll just leave his clothes outside the door. )"
    pause
    show debbie 125 with fastdissolve
    deb "( Poor Kid. )"
    deb "( I can't believe he stood up to those men... For me. )"
    deb "( That was the bravest thing I've ever seen! )"
    deb "( Hmm... )"
    deb "( ... Maybe I should go in and check on him. )"
    deb "( Just to make sure he doesn't need my help. )"
    scene shower_closeup
    show debbies 26 zorder 2
    with fade
    player_name "Man... So that's what getting punched in he face feels like..."
    show debbies 27 with dissolve
    pause
    show debbies_b zorder 1 at Position(xpos=350,ypos=768) with dissolve
    pause
    hide debbies_b
    show debbies 28 at Position(xpos=487,ypos=768)
    with dissolve
    pause
    show debbies 29 at Position(xpos=492,ypos=768)
    player_name "... Is my nose supposed to be this soft?"
    show debbies 31 at Position(xpos=484,ypos=768) with vpunch
    player_name "{b}[deb_name]{/b}??"
    player_name "Why are you-"
    show debbies 30
    deb "Shhh, It's okay, sweetie."
    deb "Let me help you..."
    show debbies 34
    deb "You deserve it, after what you did back there."
    show debbies 37_36
    pause 4
    show debbies 34
    deb "How's your face?"
    show debbies 35
    player_name "Better."
    show debbies 34
    deb "I'm glad to hear it."
    deb "I don't want anything to happen to my brave little man..."
    show debbies 36
    show debbies 76 with dissolve
    show debbies 41_76
    pause
    show debbies 42 with hpunch
    with dissolve
    deb "Here, sweetie, let me help you."
    show debbies 72
    player_name "... You're sure?"
    show debbies 43
    deb "I'm sure, sweetie. Let me take care of you..."
    show debbies 44
    deb "You were so brave down there. Standing up to those men for us."
    show debbies 45 with dissolve
    deb "I'm very proud of you..."
    show debbies 74
    player_name "... Ohh, that feels really good, {b}[deb_name]{/b}!"
    show debbies 73_74
    pause 4
    show debbies 73
    player_name "{b}[deb_name]{/b}, I'm gonna..."
    show debbies 46
    deb "It's okay, sweetie, just let it out!"
    show debbies 47 at Position(xpos=498,ypos=768)
    player_name "!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=498,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=521,ypos=508)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Wow, you had a lot in there..."
    show debbies 44 at Position(xpos=484,ypos=768) with dissolve
    deb "Good boy..."
    show debbies 34 at Position(xpos=447,ypos=768) with dissolve
    deb "Now doesn't that feel better?"
    show debbies 35 at Position(xpos=447,ypos=768)
    player_name "Oooh, you have no idea..."
    player_name "... Thanks, {b}[deb_name]{/b}!"
    show debbies 34
    deb "Now let's get you cleaned up."
    scene shower2
    with fade
    show player 261f at left with dissolve
    show debbie 35b with dissolve
    pause
    show player 8 with dissolve
    show debbie 35c with dissolve
    pause
    show player 21 with dissolve
    show debbie 34 with dissolve
    with dissolve
    player_name "{b}[deb_name]{/b}, was this just a one time thing?"
    show player 1
    show debbie 34
    deb "..."
    show debbie 35
    deb "Oh, sweetie... I don't know."
    show debbie 34
    deb "..."
    show debbie 35
    deb "I suppose, we can do it again."
    show debbie 36
    deb "But you can't tell {b}ANYBODY{/b} and we can't take things too far!"
    show debbie 34
    deb "..."
    show debbie 36
    deb "... And we {b}ABSOLUTELY CAN'T{/b} let {b}[jen_name]{/b} find out, either!"
    deb "Do you {b}understand{/b}?"
    show debbie 34
    show player 21
    player_name "I understand, {b}[deb_name]{/b}."
    show debbie 35
    show player 1
    deb "Alright..."
    deb "I have to go clean up the mess downstairs..."
    show debbie 36
    deb "I want you to wait a couple minutes before coming out of the bathroom."
    deb "Otherwise {b}[jen_name]{/b} will suspect something. Okay?"
    show debbie 32
    show player 28
    player_name "O-okay, {b}[deb_name]{/b}."
    show debbie 33
    show player 1
    deb "Good boy."
    hide debbie with dissolve
    pause
    show player 21f at Position(xpos=0.4, ypos=1.0) with dissolve
    player_name "... Wow!"
    player_name "That was totally worth a punch in the face!"
    hide player
    with dissolve
    show popup_debbieshower at truecenter with dissolve
    pause
    hide popup_debbieshower with dissolve
    return

label player_mailbox:
    $ player.go_to(L_home_mailbox)
    $ player.location.call_screen(False)

label player_mailbox_dialogue:
    $ player.go_to(L_home_mailbox)
    scene expression game.timer.image("player_mailbox{}")

    if erik.completed(erik_orcette) and not player.has_item("orcette") and not erik.known(erik_orcette_2) and orcette_mail_lock:
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_pre")
        menu:
            player_name "The package is addressed to me. This must be {b}Erik's{/b} toy."
            "Leave it alone.":
                pause
            "Open it.":


                call expression game.dialog_select("player_mailbox_erik_orcette_completed_open")

        $ player.get_item("orcette")
        $ game.mail["player"] = ""
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_after")

    elif game.mail["player"] == "m_pizza_pamphlet":
        call expression game.dialog_select("player_mailbox_pizza_pamphlet")
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["player"] == "m_newspaper":
        call expression game.dialog_select("player_mailbox_newspaper")
    $ player.location.call_screen(False)

label player_mailbox_erik_orcette_completed_pre:
    player_name "( Sweet! It looks like I'm the first one to get the mail! )"
    return

label player_mailbox_erik_orcette_completed_open:
    show mailbox_item04_c at truecenter
    with dissolve
    pause
    player_name "( So this is what he's been waiting for... )"
    player_name "( The {b}Orcette{/b}. )"
    player_name "( I'd better put this back in the box. )"
    return

label player_mailbox_erik_orcette_completed_after:
    show unlock38 at truecenter with dissolve
    pause
    hide unlock38
    hide mailbox_item04_c
    with dissolve
    player_name "( Time to get this to {b}Erik{/b} before someone catches me carrying this thing around. )"
    return

label player_mailbox_pizza_pamphlet:
    player_name "( This is probably junk mail.)"
    show expression "objects/object_mailbox_item02_closeup.png" with dissolve
    player_name "( {b}Tony's Pizza{/b}? I haven't been to that place in a while. )"
    player_name "( I'd better put this back. )"
    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label player_mailbox_newspaper:
    player_name "( Local news. This should be interesting... )"
    show expression "objects/object_newspaper.png" with dissolve
    player_name "( The thief is still on the loose? You'd think they would've caught him by now... )"
    player_name "( I'd better put this back. )"
    hide expression "objects/object_newspaper.png" with dissolve
    return

label bad_guys_driveby:
    $ player.go_to(L_home)
    call expression game.dialog_select("bad_guys_driveby_dialogue")
    $ M_mom.trigger(T_mom_bad_guys_watching)
    $ game.main()

label bad_guys_driveby_dialogue:
    scene location_home_driveby_cutscene1
    with fade
    show text "Hmm, why is that car driving so slow?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Wait a second..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_home_driveby_cutscene2
    with fade
    show text "It's that strange man who was over here making threats the other day!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "What's his problem..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_home_front_day_blur
    show player 11
    player_name "..."
    show player 10
    player_name "I know {b}[deb_name]{/b} said not to worry about this..."
    player_name "... But that guy really freaks me out!"
    show player 11
    player_name "..."
    hide player with dissolve
    return

label home_roxxy_studying_at_mcs:
    scene expression L_home_entrance.background
    show player 13 at left
    show roxxy 1f f at Position (xpos=400)
    show debbie 2 at right
    with dissolve
    deb "Hey, sweetie!"
    deb "How was sch-"
    show debbie 13
    deb "... Oh."
    deb "Who's this?"
    show debbie 14
    show player 14
    player_name "{b}[deb_name]{/b}, this is {b}Roxxy{/b}."
    player_name "I'm helping her study for French class."
    show player 13
    show debbie 3
    deb "Well that's nice!"
    show debbie 2
    deb "I'm happy to meet you, {b}Roxxy{/b}."
    show debbie 1
    show roxxy 1bf
    rox "... Thanks."
    rox "Nice to meet you too."
    show roxxy 1f f
    show debbie 2
    deb "I was just finishing up dinner."
    deb "You want me to bring you kids up a couple plates?"
    show debbie 1
    show player 14
    player_name "Yeah, that would be great!"
    show player 13
    show roxxy 1bf
    rox "Oh, I don't wanna impose..."
    show roxxy 1f f
    show debbie 3
    deb "Psh, not at all, dear!"
    show debbie 2
    deb "You kids get on up there and have fun!"
    deb "I'll bring you dinner as soon as it's ready."
    show debbie 1
    show player 14
    player_name "Thanks, {b}[deb_name]{/b}!"
    hide player
    hide roxxy
    hide debbie
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 13 at left
    show roxxy 2 at right
    with dissolve
    rox "Your landlady is really nice..."
    show roxxy 1
    show player 33
    player_name "Yeah, I'm pretty lucky."
    show player 13
    show roxxy 30
    rox "So this is your room?"
    show roxxy 1
    show player 10
    player_name "Uh huh..."
    show player 5
    show roxxy 2
    rox "Well, it's pretty dorky..."
    rox "... But I guess, it's nice too."
    show roxxy 1
    show player 14
    player_name "Heh, was that a compliment?"
    show player 13
    show roxxy 2
    rox "No. Don't be stupid."
    show roxxy 1
    show player 10
    player_name "Alright, sorry."
    player_name "You okay with studying here?"
    show player 5
    show roxxy 1b
    rox "The bed looks comfy."
    show roxxy 1
    show player 10
    player_name "... You wanna study on my bed?"
    show player 11
    show roxxy 2
    rox "Sure. Why not?"
    show roxxy 1
    show player 29 with dissolve
    player_name "Fine by me."
    hide player
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_home_bedroom_bed_dialogue.jpg"
    show player bed 1 at right
    show roxxy 36b at left
    show roxxy_outfit at left
    with dissolve
    rox "So..."
    show roxxy 35b
    rox "..."
    show roxxy 35e
    rox "You have girls up here often?"
    show roxxy 35d
    show player bed 3
    player_name "Huh?"
    player_name "... No, not really."
    show player bed 2
    show roxxy 35e
    rox "Is this the first time you've had a girl on your bed?"
    show roxxy 35d
    player_name "..."
    show player bed 3
    player_name "... No?"
    show player bed 2
    show roxxy 35e
    rox "You're not a virgin are you?"
    show roxxy 35d
    show player bed 6
    player_name "!!!" with hpunch
    show player bed 3
    player_name "What?!"
    player_name "That's not... I mean, I'm not really comfortable..."
    show player bed 2
    player_name "..."
    show player bed 5
    player_name "Are you?"
    show player bed 4
    show roxxy 35c
    rox "Pfft!"
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Haha, as if I'd tell you! I'm just having a laugh!"
    show roxxy 35e at left
    rox "I told you, studying isn't really my strong suit."
    show roxxy 35d
    show player bed 5
    player_name "Oh, c'mon. You aren't even trying."
    player_name "I think you're smarter than you give yourself credit, {b}Roxxy{/b}."
    show player bed 4
    show roxxy 38b
    rox "..."
    show roxxy 36 at Position (xoffset=120, yoffset=-100)
    rox "Tch, whatever..."
    show roxxy 35b
    show player bed 5
    player_name "I'm serious!"
    show player bed 4
    rox "..."
    show roxxy 35c
    rox "Have you ever had a girlfriend?"
    show roxxy 35b
    show player bed 6
    player_name "!!!" with hpunch
    player_name "..."
    show player bed 3
    player_name "Why would you ask me that?"
    show player bed 2
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Haha, boredom mostly..."
    show roxxy 35b
    show player bed 5
    player_name "Here look, I'll show you a trick to make this more interesting..."
    show player bed 4
    show roxxy 40 at Position (xoffset=120, yoffset=-100)
    rox "Pfft, yeah right."
    show roxxy 35b
    show player bed 5
    player_name "Just look!"
    hide player
    hide roxxy
    hide roxxy_outfit
    with dissolve
    scene expression "backgrounds/location_home_bedroom_cutscene10.jpg"
    with fade
    show text "I spent hours trying to coax {b}Roxxy{/b} into studying.\nShe mostly just watched me work and asked awkward questions about my experience with girls.\n... But eventually I managed to teach her what she needed to know." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression L_home_entrance.background
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "So, I guess we might have to do this again sometime, huh?"
    show player 5
    show roxxy 2
    rox "Let's hope not!"
    show roxxy 1
    show player 12
    player_name "Oh, c'mon... It wasn't that bad!"
    show player 5
    rox "..."
    show roxxy 1b
    rox "... No, it wasn't that bad."
    rox "Just..."
    show roxxy 1
    rox "..."
    show roxxy 1b
    rox "Thanks... For being cool about all this..."
    show roxxy 1
    show player 13
    player_name "..."
    rox "..."
    show roxxy 2
    rox "... Why are you looking at me like that?"
    show roxxy 1
    show player 29 with dissolve
    player_name "S-sorry... It's just... I'm not used to you, being nice, like this..."
    show player 3
    show roxxy 2
    rox "... Well don't get used to it!"
    rox "You're still a dork and I'm gonna treat you like one at school!"
    show roxxy 28 with dissolve
    rox "... but."
    show roxxy 27
    rox "..."
    hide player
    show roxxy 59 at left with dissolve
    player_name "!!!" with hpunch
    show player 11 at left
    show roxxy 1e at right
    with dissolve
    player_name "..."
    show player 10
    player_name "What was that for?"
    show player 11
    show roxxy 1b
    rox "... Just a little show of gratitude."
    show player 13
    rox "Nothing more!"
    show roxxy 2
    rox "Don't go thinking it means anything!"
    show roxxy 1
    player_name "..."
    show player 29 with dissolve
    player_name "... Right."
    player_name "I'll walk you home, then."
    show player 3
    show roxxy 1b
    rox "Nah, I'll be fine."
    rox "Later, nerd!"
    hide roxxy with dissolve
    pause
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "Pigs must be flying somewhere..."
    hide player with dissolve
    return

label home_front_roxxy_cookies_and_milk:
    scene expression L_home_entrance.background
    show player 5 at Position (xpos=400)
    show roxxy 32f at left
    show debbie 13 at right
    with dissolve
    deb "{b}[firstname]{/b}?"
    deb "What on earth are you doing home so early?"
    show debbie 14
    show player 10
    player_name "Hey, {b}[deb_name]{/b}."
    player_name "My friend here is having a really rough day."
    show player 5
    show debbie 13
    deb "Oh!"
    show debbie 2
    deb "Hello again, dear..."
    show debbie 1
    show player 10
    player_name "I brought her here to talk things over."
    player_name "... And I offered her lunch."
    player_name "I hope that's okay?"
    show player 5
    show debbie 3
    deb "Of course, it's okay!"
    show debbie 2
    deb "... It's {b}Roxxy{/b}, isn't it?"
    show debbie 1
    show roxxy 33f
    rox "Yes, ma'am."
    rox "Sorry to inconvenience you again..."
    show roxxy 32f
    show debbie 3
    deb "It's no trouble at all, dear!"
    show debbie 2
    deb "Why don't you two go on upstairs and I'll whip something up for you."
    show debbie 1
    show player 14
    player_name "Thanks, {b}[deb_name]{/b}."
    scene black with fade
    pause

    scene expression game.timer.image("backgrounds/location_home_bedroom_day{}.jpg")
    show player 5 at left
    show roxxy 1l
    with dissolve
    rox "Does your {b}Landlady{/b} ever wear clothes?"
    show roxxy 1k
    show player 10
    player_name "Huh?"
    player_name "What do you mean?"
    show player 5
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "... Nevermind."
    show roxxy 30 at Position (xoffset=-33) with dissolve
    rox "Ugh, this is such a disaster..."
    rox "What the hell am I gonna do!"
    show roxxy 29 at Position (xoffset=-33)
    show player 10
    player_name "Calm down, {b}Roxxy{/b}."
    player_name "There's no sense getting yourself all worked up before we have all the details."
    show player 5
    show roxxy 3c at Position (xoffset=-33)
    rox "What do you mean?"
    show roxxy 3d at Position (xoffset=-33)
    show player 10
    player_name "All we know is that {b}your mom{/b} was arrested for possession and that the police are investigating."
    player_name "There might still be a way to salvage the situation."
    show player 5
    show roxxy 1k with dissolve
    rox "..."
    show roxxy 1l
    rox "You really think so?"
    show roxxy 1k
    show player 10
    player_name "... Maybe."
    player_name "We should go down to the {b}Police Station{/b} and find out exactly what's going on."
    show player 5
    show roxxy 27
    rox "..."
    show roxxy 1l
    rox "You're right..."
    show roxxy 1k
    rox "..."
    show player 10
    player_name "For now, just breathe and relax."
    player_name "I'm sure we can find a way to fix this."
    show player 5
    show roxxy 1l
    rox "... Why are you being so nice to me?"
    show roxxy 1k
    show player 10
    player_name "Huh?"
    player_name "I..."
    show player 5
    show debbie 218 at right with dissolve
    deb "I brought snacks!"
    show roxxy 1kf at Position (xpos=400) with dissolve
    show player 13
    show debbie 217
    deb "Some fresh milk and oven baked cookies..."
    deb "It's the perfect thing to get you feeling better after a rough day, {b}Roxxy{/b}!"
    show debbie 219 with dissolve
    show roxxy 27f at Position (xoffset=33)
    show player 428
    pause
    show roxxy 1bf with dissolve
    rox "{b}*Sniff*{/b} Oh, wow!"
    show debbie 1 with dissolve
    show player 11
    rox "Those looks wonderful, ma'am!"
    show roxxy 1f f
    show debbie 3
    deb "Aww, well thank you, dear."
    show roxxy 32f at Position (xoffset=-34)
    show player 13
    with dissolve
    deb "The recipe has been in my family for generations!"
    show debbie 14b
    show roxxy 27f at Position (xoffset=33)
    deb "..."
    show debbie 13
    deb "Your mascara is running, dear..."
    show player 5
    show debbie 14b
    show roxxy 33f at Position (xoffset=-34)
    rox "{b}*Sniff*{/b} Oh, sorry..."
    show roxxy 33bf with dissolve
    pause
    show debbie 13
    deb "There's nothing to be sorry for!"
    show roxxy 32f at Position (xoffset=-34)
    deb "You guys just eat up and let me know if there's anything else I can do for you."
    deb "I just hate seeing a pretty thing like you all upset..."
    show debbie 14
    show player 13
    show roxxy 33f at Position (xoffset=-34)
    rox "... Thanks, ma'am."
    show roxxy 32f at Position (xoffset=-34)
    show debbie 2
    deb "Please, call me {b}[deb_name]{/b}, dear."
    hide debbie with dissolve
    rox "..."
    show roxxy 33 at center with dissolve
    rox "Thanks, for all this {b}[firstname]{/b}..."
    show roxxy 32
    show player 14
    player_name "Anytime!"
    show player 13
    show roxxy 33b
    rox "{b}*Sniff*{/b}."
    show roxxy 32
    show player 10
    player_name "Let's eat and then we'll head down to the {b}Police Station{/b} and sort things out."
    show player 13
    show roxxy 33
    rox "... Yeah, okay."
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
