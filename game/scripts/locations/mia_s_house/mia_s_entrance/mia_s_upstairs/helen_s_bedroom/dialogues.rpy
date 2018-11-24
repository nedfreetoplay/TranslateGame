label helens_bedroom_mia_midnight_help:
    scene mia_house_helen_night_b
    player_name "( The key must be somewhere in here... )"
    return

label helens_bedroom_mia_helen_talk:
    scene expression game.timer.image("mia_house_helen_c{}")
    show helen 1f at right
    show player 10 at left
    with dissolve
    player_name "Uhm... Hello?"
    show player 5
    show helen 4
    helen "!!!"
    show helen 5
    helen "You again?!"
    show helen 6
    show player 10
    player_name "{b}Mia{/b} asked me to come and speak with you."
    show player 5
    show helen 2
    helen "{b}Mia{/b} asked you?"
    show helen 1
    show player 12
    player_name "I don't know what's going on exactly, and it's none of my business..."
    show player 10
    player_name "...But I don't think {b}Mia{/b} wants her parents to split up like this."
    show player 11
    show helen 5
    helen "You're right. It is none of your business!"
    show helen 4
    helen "Besides... there's nothing we can do at the moment..."
    show helen 3
    helen "...everything is in the hands of {b}God{/b}!"
    show helen 1
    show player 12
    player_name "Huh?"
    show player 5
    show helen 4
    helen "You should leave now..."
    hide player
    hide helen
    with dissolve
    return

label helens_bedroom_mia_unexpected_visit:
    label helen_baton_replay_1:
        scene mia_house_helen_sneak
    show helens 1_2 at Position (xpos=465,ypos=565) with dissolve
    player_name "!!!"
    player_name "( ...{b}Helen{/b}?! )"
    player_name "( Is that... A police baton?! )"
    helen "Uuuhh! Ooohh yesss..."
    helen "{b}Harold{/b}..."
    helen "Uuhhhh..."
    helen "It's been... so long..."
    show helens 3 with dissolve
    player_name "!!!" with hpunch
    player_name "( She saw me!! )"
    scene black
    scene mia_house_helen_c
    show helen 33 at right
    show player 10 at left
    with dissolve
    player_name "I'm so sorry, {b}Helen{/b}!!!"
    player_name "I heard voices and thought {b}Mia{/b} was in here with you..."
    player_name "...I didn't mean to see..."
    show player 5
    show helen 34
    helen "I... I'm sorry you had to see me like this..."
    show helen 29
    show player 24
    player_name "I didn't see much anyway... I just..."
    player_name "I should really leave, this was innapropriate of me."
    show player 11
    show helen 30
    helen "Wait!"
    helen "I need you to tell me something."
    show helen 29
    show player 3 with dissolve
    player_name "..."
    show helen 34
    helen "Do you think I still look... attractive?"
    show helen 33
    show player 22 with dissolve
    player_name "!!!" with hpunch
    show player 10
    player_name "Emm... I don't know if I should-"
    show player 11
    show helen 30
    helen "Just tell me!"
    show helen 29
    show player 37 with dissolve
    player_name "...Yes?"
    show player 24
    show helen 41 at Position (xoffset=1)
    with dissolve
    helen "{b}*Sigh*{/b}"
    show helen 42 at Position (xoffset=1)
    show player 11
    helen "Ever since I started attending those sessions with {b}Sister Angelica{/b}..."
    helen "...I've been having these desires and sexual urges that I never felt before!"
    helen "My body is constantly craving attention..."
    helen "...But what if my husband won't take me back?"
    show helen 33 with dissolve
    show player 12
    player_name "From what I've seen, I think {b}Harold{/b} likes you a lot, {b}Helen{/b}."
    show player 5
    show helen 34
    helen "I'm just not sure he finds me attractive anymore..."
    helen "...And I realise that I should have been more... sexual, towards my husband."
    helen "Which is why I want to change a few things."
    show helen 29
    show player 12
    player_name "Change things?"
    show player 5
    show helen 30
    helen "I want to change my looks, {b}[firstname]{/b}."
    show helen 29
    show player 10
    player_name "Oh..."
    show player 5
    show helen 30
    helen "I want him to desire me again. I have to find... something sexy!"
    show helen 29
    show player 11
    player_name "..."
    show helen 34
    helen "Do you think you could... do me a favor?"
    show helen 33
    show player 12
    player_name "A favor?"
    show player 5
    show helen 30
    helen "I need to find something sexy to wear for him..."
    show helen 29
    show player 23
    player_name "!!!"
    show player 30
    player_name "I'm not sure how I could help with that, {b}Helen{/b}. I just-"
    show player 11
    show helen 30
    helen "Just go and find me something to wear for him..."
    helen "...And I'll give you some money!!"
    show helen 29
    show player 12
    player_name "Why not go yourself? I'm sure you have a better idea of what to wear."
    show player 5
    show helen 30
    helen "There's no way I can be seen walking into a {b}sex shop{/b}."
    helen "You must help me... Please?!"
    show helen 29
    show player 10
    player_name "Uhh... What do you want me to buy?"
    show player 5
    show helen 34
    helen "I always wanted to wear a corset... and {b}Harold{/b} loves to see me in red."
    show helen 29
    show player 12
    player_name "A {b}red corset{/b}, then?"
    show player 5
    show helen 30
    helen "If you can find one, bring it back to me."
    show helen 29
    show player 10
    player_name "I'll try to..."
    show player 5
    show helen 34
    helen "Thank you, {b}[firstname]{/b}."
    hide player
    hide helen
    with dissolve
    if not store._in_replay == None:
        scene black with dissolve
        pause 0.5
        scene mia_house_helen_c with dissolve
        jump helen_baton_replay_2
    return

label helens_bedroom_mia_helen_outfit_request:
    label helen_baton_replay_2:
        scene mia_house_helen_c
    show helen 23 at right
    show player 14 at left
    with dissolve
    player_name "Hi, {b}Helen{/b}!"
    show player 13
    show helen 24
    helen "There you are."
    helen "How's your search going?"
    show helen 23
    show player 33
    player_name "I think I found something you will like..."
    show player 239_240 with dissolve
    pause
    show player 449 with dissolve
    pause
    show player 451
    player_name "Here it is!"
    player_name "It's a sexy red corset, just like you asked."
    show player 450
    show helen 24
    helen "Wow."
    show player 13
    show helen 18
    with dissolve
    helen "This is... quite extravagant..."
    show helen 17
    show player 10
    player_name "You don't like it?"
    show player 5
    show helen 18
    helen "No, it's just that... I've never worn anything like that before."
    show helen 17
    show player 36 with dissolve
    player_name "Well, I should get going, then."
    show player 11 with dissolve
    show helen 20
    helen "Wait!"
    helen "You won't stay and give me your thoughts?"
    show helen 19
    show player 12
    player_name "Huh?"
    show player 5
    show helen 20
    helen "Let me put it on first and you can tell me if I look good in it!"
    show helen 21 with dissolve
    pause
    show helen 22 at Position (xoffset=-14) with dissolve
    pause
    show helen 35 with dissolve
    pause
    show helen 36 with dissolve
    pause
    show helen 38 with dissolve
    show player 433
    player_name "!!!"
    show helen 45 with dissolve
    pause
    show helen 46 with dissolve
    pause
    show player 11
    show helen 48 at Position (xpos=970) with dissolve
    helen "It's a little tight... But it pushes my breasts up a bit which is good..."
    show helen 49 at Position (xoffset=18) with dissolve
    helen "And what's this crack at the bottom here?!"
    show player 433
    pause
    show player 435
    player_name "Oh, that, I ehh... didn't see that when I bought it!"
    show player 79 with dissolve
    player_name "Ha ha..."
    show player 82
    show helen 48
    with dissolve
    helen "What do YOU think?"
    show helen 47
    show player 83
    player_name "Oh, I... I think it looks great!"
    player_name "I was just really hoping it would fit you well..."
    show player 82
    show helen 48
    helen "It's fine... I think {b}Harold{/b} will definitely like this."
    helen "Thank you, {b}[firstname]{/b}."
    show helen 47
    show player 79 with dissolve
    player_name "You're welcome, {b}Helen{/b}... But I should really go now."
    player_name "See you later!"
    hide player
    hide helen
    with dissolve
    $ renpy.end_replay()
    return

label helens_bedroom_helen_master_servant_fun:
    scene mia_house_helen_window0 with fade
    show expression "objects/character_helen_02.png" at Position (xpos = 211, ypos = 732)
    player_name "Woah..."
    player_name "It's kind of dark in here."
    return

label helens_mary_statue:
    scene mia_house_statue
    show key3 at Position (xpos=450,ypos=450):
        rotate -45
    player_name "There's a golden key on this rosery... Could it be the one to unlock that room?"
    player_name "I could try it..."
    show unlock52 at truecenter with dissolve
    $ player.get_item("key03")
    pause
    hide unlock52 with dissolve
    $ M_mia.trigger(T_mia_key_found)
    $ game.main()

label helen_bedroom_sex:
    call expression game.dialog_select("helen_bedroom_sex_intro")
    if not store._in_replay == None:
        call expression game.dialog_select("helen_bedroom_sex_yes")
        jump expression game.dialog_select("helen_bedroom_sex_start")
    menu:
        "Another time.":
            call expression game.dialog_select("helen_bedroom_sex_leave")
        "I want to.":

            call expression game.dialog_select("helen_bedroom_sex_yes")

            label helen_bedroom_sex_start:
                menu:
                    "Keep the corset.":
                        $ M_helen.set("corset lingerie", True)
                    "Get naked.":

                        $ M_helen.set("corset lingerie", False)

            call expression game.dialog_select("helen_bedroom_sex_start_after")
            $ anim_toggle = True
            $ animated = False
            jump expression game.dialog_select("helen_bedroom_sex_loop")
    hide player
    hide helen
    with dissolve
    $ game.main()

label helen_bedroom_sex_intro:
    scene mia_house_helen_closed_c with fade
    show player 5 at left
    show helen 63 at right
    with dissolve
    helen "Hello, {b}[firstname]{/b}."
    helen "I'm glad to see you've come."
    helen "Now I can finally serve you, {b}Master{/b}."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Did you close the door behind you?"
    show helen 62
    show player 12
    player_name "No, I didn't."
    show player 11
    show helen 63
    helen "Good. I don't mind if someone comes in and sees us...together."
    show helen 62
    show player 10
    player_name "Umm... But...what about {b}Mia{/b}?"
    player_name "Don't you think she'd be...upset?"
    show player 5
    show helen 63
    helen "Don't worry about chasing after young girls like her."
    helen "Helping me exorcise my sins is a greater deed."
    show helen 62
    show player 11
    player_name "..."
    show helen 63
    helen "Do you like my attire? Does it please you?"
    show helen 62
    show player 10
    player_name "I... I think you are pretty with or without that outfit."
    show player 5
    show helen 49 with dissolve
    helen "Oh? Would you prefer I be fully naked?"
    pause
    show helen 62 with dissolve
    show player 23
    player_name "!!!"
    show player 37 with dissolve
    player_name "No, {b}Helen{/b}! I mean...yes, but..."
    show player 29 with dissolve
    player_name "I meant you look good naked too."
    show player 3
    show helen 63
    helen "Hee Hee... I'll always wear this outfit for you then."
    helen "You know that...I'm here to serve you, {b}Master{/b}."
    show helen 62
    show player 29
    player_name "Heh...Heh... You really don't have to, {b}Helen{/b}."
    show player 5 with dissolve
    show helen 63
    helen "Oh, but I must!"
    helen "{b}Sister Angelica{/b} said that your seed is the only way to stay pure."
    helen "My sinful body needs to be cleansed by your holy seed."
    helen "Therefore, I offer you my body and will use it to grant any wish of yours."
    show helen 62
    show player 11
    player_name "..."
    return

label helen_bedroom_sex_leave:
    show player 10
    player_name "Thanks {b}Helen{/b}..."
    player_name "Maybe another time."
    show player 12
    show helen 47
    player_name "I have...other things to do."
    show player 5
    show helen 48
    helen "Oh..."
    helen "I was really hoping to serve you..."
    helen "Don't hesitate to come visit me more often."
    show helen 47
    show player 12
    player_name "Sure... I'll let you know, {b}Helen{/b}."
    return

label helen_bedroom_sex_yes:
    show player 14
    player_name "Sure... I'd like to try..."
    show player 13
    show helen 63
    helen "Great!"
    helen "Before we start, why don't you remove your clothes and I'll let in some light."
    show helen 62
    show player 10
    player_name "Huh? Let in some light?"
    show player 5
    show helen 63
    helen "Don't worry, {b}[firstname]{/b}."
    helen "Just get naked and sit at the foot of the bed."
    helen "I won't take long."
    show helen 62
    show player 10
    player_name "Okay..."
    hide helen
    hide player
    with dissolve

    scene mia_house_helen_window1
    show player helen_sex 52
    with fade
    helen "I've hidden my sinful desires for too long."
    helen "I'm not going to hide anymore."
    scene mia_house_helen_window2
    show player helen_sex 52
    helen "I want {b}God{/b} and all the neighbors to see me for what I am."
    scene mia_house_helen_window3
    show player helen_sex 52
    show helen 54 with dissolve
    helen "A sinful woman trying her best to follow the church's teachings."
    show helen 53
    player_name "!!!"
    player_name "Are you sure that's such a good idea?"
    show helen 54
    helen "You worry too much, {b}[firstname]{/b}."
    helen "There is nothing shameful about our bodies..."
    helen "...Now lay on your back, so I can let the light of {b}God{/b} shine on me."
    show helen 53
    player_name "Alright."
    show player helen_sex 59 with dissolve
    show helen 54
    return

label helen_bedroom_sex_start_intro:
    helen "Before we commence this sacred ritual, would you like me to be naked?"
    show helen 53
    return

label helen_bedroom_sex_start_after:
    show helen 54
    helen "Anything for you, {b}Master{/b}."
    if M_helen.is_set("corset lingerie"):
        show helen 54
    else:

        show helen 55 with dissolve
        pause
        show helen 56 with dissolve
        pause
        show helen 58 with dissolve

    helen "Be a good boy now and let me insert your holy rod."
    helen "Don't hold back either."
    helen "I want you to release every last drop of your holy seed inside me."
    hide player
    if M_helen.is_set("corset lingerie"):
        show helen 61
    else:

        show helen 60
    with dissolve

    if not M_helen.is_state(S_helen_master_servant_fun):
        helen "Oh my..."
        helen "Your...cock..."
        helen "I didn't get to see it last time."
        helen "The {b}Lord{/b} has truly blessed you."
    else:

        pause

    scene mia_house_helen_bed1 with fade
    hide helen
    show helens 22
    if M_helen.is_set("corset lingerie"):
        show h_corset 22b
    with dissolve

    if M_helen.is_state(S_helen_master_servant_fun):
        helen "I'm still amazed at the size of your cock."
        helen "{b}God{/b} truly blessed you."

    helen "Be gentle with me...at first."
    pause
    show helens 23
    if M_helen.is_set("corset lingerie"):
        show h_corset 23b
    with dissolve

    helen "Ohhh!!! {b}[firstname]{/b}!"
    helen "Not so deep yet!"
    helen "I'm still not used to how big your holy cock is."
    helen "But I love it..."
    return

label helen_bedroom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("helens", [23,24,25,26,27], M_helen) as helens
                if M_helen.is_set("corset lingerie"):
                    show expression AnimatedImage("h_corset", ["23b","24b","25b","26b","27b"], M_helen) as h_corset
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("helen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [23,24,25,26,27]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                if M_helen.is_set("corset lingerie"):
                    show expression "h_corset {}b".format(pose_list[pose_counter]) as h_corset
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("helen_hscene_dialog")
        $ animcounter += 1

    helen "I'm...almost..."
    call screen helen_bedroom_sex_options

label helen_hscene_dialog:
    if animcounter == 1:
        helen "Ahhhh!!!{p=1}{nw}"

    elif animcounter == 3:
        helen "{b}[firstname]{/b}!!!{p=1}{nw}"
        player_name "Uhhh...{p=1}{nw}"
    return

label helen_bedroom_sex_cum:
    call expression game.dialog_select("helen_bedroom_sex_cum_intro")
    if not M_helen.is_state(S_helen_master_servant_fun):
        $ game.timer.tick()
        call expression game.dialog_select("helen_bedroom_sex_cum_repeat")
    else:

        $ player.go_to(L_miahouse_upstairs)

        show player 13

    call expression game.dialog_select("helen_bedroom_sex_cum_after")
    $ persistent.cookie_jar["Helen"]["unlocked"] = True
    $ persistent.cookie_jar["Helen"]["gallery"]["02_unlocked"] = True
    $ M_helen.trigger(T_helen_master_servant_sex)
    pause
    jump expression game.dialog_select("mias_upstairs")

label helen_bedroom_sex_cum_intro:
    helen "Cum hard for me {b}[firstname]{/b}! Bury your cock deep in me!"
    show helens 28
    if M_helen.is_set("corset lingerie"):
        show h_corset 28b
    with flash
    player_name "UHHH!!!"
    helen "OHHHH!!!"
    show helens 29
    if M_helen.is_set("corset lingerie"):
        show h_corset 29b
    with dissolve
    pause
    helen "I felt your holy seed pouring into me..."
    show helens 30
    if M_helen.is_set("corset lingerie"):
        show h_corset 30b
    with dissolve
    pause
    show helens 31
    if M_helen.is_set("corset lingerie"):
        show h_corset 31b
    with dissolve
    pause
    show helens 32
    if M_helen.is_set("corset lingerie"):
        show h_corset 32b
    with dissolve
    pause
    helen "Thank you, {b}Master{/b}."
    scene black with fade
    hide helens
    hide h_corset
    pause

    scene mia_house_helen_c with fade
    show player 13 at left
    if M_helen.is_set("corset lingerie"):
        show helen 63 at right
    else:

        show helen 65 at right
    with dissolve
    helen "I must confess, {b}Master{/b}."
    helen "I was waiting for you all day."
    helen "I'm glad you choose to cleanse me..."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 26
    player_name "Yeah... I really enjoyed doing...it...with you."
    show player 13
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Will you be back soon?"
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 10
    player_name "Maybe..."
    show player 35
    player_name "Depends if I don't have a lot of school work..."
    return

label helen_bedroom_sex_cum_repeat:
    show player 29 with dissolve
    player_name "...But could you please do me a favor and not mention what we did here?"
    player_name "I would rather not let {b}Mia{/b} know about this."
    show player 13 with dissolve
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Don't worry about my daughter. She'll understand."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 11
    player_name "..."
    return

label helen_bedroom_sex_cum_after:
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Don't make your servant wait too long."
    helen "My body will be eagerly awaiting your return."
    if M_helen.is_set("corset lingerie"):
        show helen 62
    else:

        show helen 64
    show player 10
    player_name "Okay."
    show player 36 with dissolve
    player_name "Well, I'd better get going."
    show player 13 with dissolve
    if M_helen.is_set("corset lingerie"):
        show helen 63
    else:

        show helen 65
    helen "Goodbye, {b}Master{/b}."
    helen "Thank you for the gift of your holy seed."
    scene black
    hide player
    hide helen
    with fade
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
