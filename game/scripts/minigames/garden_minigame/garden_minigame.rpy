label job_done_dialogue(earnings):
    $ renpy.checkpoint()
    if M_diane.between_states(S_diane_bug_infested_garden, S_diane_clear_bug_infested_garden):
        scene garden_dead
    elif M_diane.finished_state(S_diane_barn_news):
        scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    else:
        scene garden

    if M_diane.is_state(S_diane_clean_garden):
        scene garden_dead
        show player 14 with dissolve
        player_name "Phew!"
        player_name "Alright, I think I finally got everything..."
        show player 31f with dissolve
        player_name "..."
        show player 32f
        player_name "Now, where did {b}Diane{/b} sneak off to?"
        player_name "She must have gone inside..."
        hide player with dissolve
        $ M_diane.trigger(T_diane_cleaned_garden)

    elif M_diane.is_state(S_diane_drunken_garden_work):
        call expression game.dialog_select("dianes_garden_diane_drunk_like_a_sailor")
        $ M_diane.trigger(T_diane_drunken_massage)
        $ game.timer.tick(3)
        $ player.go_to(L_map)

    elif M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden) and player.has_item("annihilator"):
        scene black with dissolve
        with Pause(0.5)
        show expression "backgrounds/location_diane_garden_cutscene03.jpg"
        show expression FilteredText("I began to spray the whole lot with green napalm...\n Emptied the entire can of spray on the nasty buggers...\nUntil nothing remained!") as cutscene at Position (xpos= 512, ypos = 700)
        with fade
        $ player.remove_item("annihilator")
        if player.has_item("exterminator"):
            $ player.remove_item("exterminator")

        if player.has_item("eradicator"):
            $ player.remove_item("eradicator")
        pause
        hide cutscene
        scene black
        with dissolve
        pause 0.5
        show unlock27 at truecenter with dissolve
        pause
        hide unlock27 with dissolve
        hide black
        $ M_diane.trigger(T_diane_use_bug_spray_on_garden)
        scene garden
        show player 13 at left
        show diane f_normal_talk a_dressed_blush
        with dissolve
        dia "Phew, what a day!"
        show diane f_normal a_dressed_shovel with dissolve
        show player 14
        player_name "Heh, I know... I'm exhausted."
        player_name "We got it all finished though."
        show player 13
        show diane f_normal_talk
        dia "We sure did."
        show diane f_laugh
        dia "It'll be even better than it was before!"
        show diane a_dressed_finger with dissolve
        dia "You wait and see!"
        show diane f_normal a_dressed_shovel with dissolve
        show player 14
        player_name "Hehe, I hope so."
        show player 13
        show diane f_normal_talk
        dia "Thanks for all your help today, stud."
        show diane f_normal
        show player 17
        player_name "My pleasure!"
        hide player
        show diane kiss
        with dissolve
        pause
        show player 13 at left
        show diane f_normal_talk
        dia "Tell {b}[deb_name]{/b} hi for me."
        show diane f_normal
        show player 14
        player_name "Will do."
        hide player
        hide diane
        with dissolve
        $ game.timer.tick(2)
        $ M_diane.trigger(T_diane_inform_diane)

    elif M_diane.is_state(S_diane_work_on_garden):
        scene expression "backgrounds/location_diane_garden_closeup.jpg"
        show player 13 at right
        show diane f_normal_talk at flip
        with dissolve
        dia "Hey, that's looking great!"
        show diane f_normal
        show player 22
        player_name "!!!" with hpunch
        show player 29f with dissolve
        player_name "H-hey, {b}Diane{/b}."
        show player 3f at Position (xoffset=-8)
        show diane f_normal_talk
        dia "I'm sorry I wasn't out here to greet you..."
        show diane f_thinking
        dia "... Something urgent came up that I had to take care of."
        show diane f_cheese
        show player 10f
        player_name "... Oh, y-yeah?"
        show player 14f
        show diane f_normal
        player_name "I mean... Heh, no worries!"
        show player 29f with dissolve
        player_name "I was just out here... Umm..."
        show player 3f at Position (xoffset=-8)
        pause
        show diane f_smirk_talk
        dia "... Working?"
        show diane f_smirk
        show player 29f
        player_name "Y-yeah!"
        show player 3f at Position (xoffset=-8)
        show diane f_laugh
        dia "Hehe?"
        show diane f_normal_talk
        dia "What's got you so tongue tied all of a sudden?"
        show diane f_normal
        show player 29f
        player_name "N-nothing..."
        player_name "I was just... Umm..."
        show player 3f at Position (xoffset=-8)
        show diane f_normal_talk
        dia "Well the garden really does look great!"
        dia "I think it's even better than it was before the earwig fiasco!"
        show diane grab_cucumber with dissolve
        show player 428f with dissolve
        dia "Just look at these beauties!"
        player_name "..."
        show diane a_dressed_cucumber_touch f_normal_talk with dissolve
        show player 11f
        dia "What a monster!"
        show diane a_dressed_cucumber_rub with dissolve
        dia "And it's really bumpy!"
        show diane f_cheese
        show player 78f with dissolve
        pause
        show player 81f
        player_name "!!!" with hpunch
        show diane f_normal_talk a_dressed_cucumber_touch with dissolve
        dia "With vegetables like this, I might have to give you a-"
        show diane f_surprised_down
        dia "Raaaaaise!"
        dia "!!!"
        show diane f_surprised
        player_name "..."
        dia "..."
        show player 79f with dissolve
        player_name "I uhh..."
        show player 78f with dissolve
        show diane f_surprised_down
        dia "... Is that?"
        show diane f_surprised
        show player 83f
        player_name "I have to go!!"
        show player 78f with dissolve
        show diane f_laugh
        dia "Wait!"
        show player 81f
        player_name "Bye, {b}Diane{/b}!"
        hide player with dissolve
        pause
        show diane f_sad_talk
        dia "{b}[firstname]{/b}?!"
        show diane f_sad
        dia "..."
        hide diane with dissolve
        scene expression "backgrounds/location_diane_front_day_blur.jpg"
        show player 83 with dissolve
        player_name "Oh my god..."
        player_name "I can't believe I got a boner in front of {b}Diane{/b}!"
        player_name "That was so embarrassing!"
        player_name "I've gotta get outta here!"
        hide player with dissolve
        $ game.timer.tick(2)
        $ player.go_to(L_map)
        $ M_diane.trigger(T_diane_worked_on_garden)

    elif M_diane.get("garden first time"):
        if earnings > 0:
            scene black
            with Pause(0.5)
            call expression game.dialog_select("garden_firsttime_text")
            pause
            scene black with dissolve
            with Pause(0.5)
            scene expression player.location.background_blur with None
            show player 1 at left
            show diane f_normal_talk at lright
            with dissolve
            dia "Oh, wow! My garden looks absolutely gorgeous, {b}[firstname]{/b}!"
            show player 2
            show diane f_smirk
            player_name "Yeah... I had to get rid of a lot of stuff..."
            show diane a_dressed_cucumber f_teasing_look with dissolve
            show player 11
            dia "Just look at that big, hard cucumber!"
            show diane f_smirk
            player_name "..."
            show player 10
            player_name "Why do you only want the vegetables that are long and hard?"
            show player 5
            show diane f_shamed_talk_smile
            dia "I err..."
            show diane f_shamed_talk_look
            dia "Well, you see they... Umm..."
            show diane f_shamed
            show player 10
            player_name "Do they sell better or something?"
            show player 5
            show diane f_laugh
            dia "Yes!! That's exactly it!"
            show diane f_teasing_look
            dia "They sell better."
            show diane f_smirk
            show player 12
            player_name "Hmm, interesting."
            show player 14
            player_name "I guess I have a lot to learn about vegetables..."
            show player 13
            show diane f_normal_talk a_dressed_shovel with dissolve
            dia "Well don't you worry, {b}[firstname]{/b}."
            dia "I can teach you everything there is to know about gardening."
            show diane f_normal
            show player 14
            player_name "How did you get into this stuff anyways?"
            show player 13
            show diane f_normal_talk
            dia "Oh, I've always had a bit of a green thumb. Even when I was a kid."
            show diane f_normal
            show player 14
            player_name "Really?"
            show player 13
            show diane f_laugh
            dia "You betcha!"
            show diane f_normal_talk
            dia "You know, I used to dream about owning a farm of my own..."
            show diane f_normal
            show player 14
            player_name "Like a for real farm? With fields of crops and animals?"
            show player 13
            show diane f_normal_talk
            dia "That's right! I wanted the whole nine yards!"
            show diane f_normal
            show player 14
            player_name "You should totally do that, {b}Diane{/b}!"
            show player 17
            player_name "I'd help you!"
            show player 13
            show diane f_laugh
            dia "Haha, yeah well, thanks {b}[firstname]{/b}... I'm afraid it's not as easy as all that."
            show diane f_normal
            show player 14
            player_name "Yeah, I suppose you're right."
            show diane f_laugh
            show player 13
            dia "Thanks for your help today!"
            show diane f_normal_talk
            dia "Why don't you come back tomorrow and we'll continue where we left off?"
            show diane f_normal
            show player 14
            player_name "Alright, I'll see you tomorrow then."
            show player 13
            show diane f_smirk_talk
            dia "Bye, handsome."
            hide player
            hide diane
            with dissolve
        else:
            call expression game.dialog_select("garden_firsttime_fail")
        $ M_diane.set("garden first time", False)
    $ game.timer.tick()
    if earnings < 0:
        $ earnings = 0
    $ after_minigame = True
    $ player.get_money(earnings)
    call screen money_popup(earnings, "garden")
    with dissolve
    if M_daisy.is_state(S_daisy_pizza_craving):
        call expression game.dialog_select("barn_front_daisy_pizza_craving")
        $ M_daisy.trigger(T_daisy_find_food)
        $ player.go_to(L_diane_barn_interior)
        $ game.main()
    $ game.main()

label garden_firsttime_text:
    show expression "backgrounds/location_diane_garden_cutscene01.jpg"
    show expression FilteredText("{b}Diane{/b} went to lie down as I began digging up her garden.\n It was so hot outside and there were so many weeds and bugs!\nI grit my teeth and set myself to the task...\n... I hope she's planning to pay me well for all this physical labor!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with dissolve
    pause 0.5
    show expression "backgrounds/location_diane_garden_cutscene02.jpg"
    show expression FilteredText("As I worked, I noticed {b}Diane{/b} was watching me intently...\nI suppose she was just trying to make sure I did a good job.\nWe exchanged a few words here and there but mostly just small talk.\nHer eyes seemed fixed upon me.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    scene black
    hide cutscene
    with dissolve
    return

label garden_firsttime_fail:
    scene expression player.location.background_blur with None
    show player 5 at left
    show diane f_sad_talk
    with dissolve
    dia "Hmm... There's some room for improvement."
    show diane f_sad
    show player 24 at left
    player_name "Yeah... I didn't do too well. Sorry {b}Diane{/b}!"
    show diane f_shamed_talk_smile
    show player 13 at left
    dia "It's okay... You're new at this..."
    show diane f_laugh
    dia "And I'm sure you'll get better at it!"
    show diane f_normal_talk
    dia "I always need fresh vegetables..."
    show diane f_normal
    show player 10 at left
    player_name "I guess so..."
    show player 5
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Just make sure you {b}only{/b} keep the vegetables that are {b}long{/b} and {b}hard{/b}!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 10
    player_name "I'll do better next time..."
    show player 14
    player_name "Thanks {b}Diane{/b}!"
    hide player
    hide diane
    with dissolve
    return

label garden_listing:
    call screen garden_minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
