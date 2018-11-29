label milking_game_pre:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "There he is."
    show diane f_smirk_talk
    dia "You ready to give this new milking setup a try?"
    show diane f_smirk
    show player 10
    menu:
        "Sure!":
            player_name "R-right now?"
            show player 13
            show diane f_laugh
            dia "No time like the present."
            show diane f_smirk
            show player 14
            player_name "Okay."
            show player 13
            show diane f_smirk_talk
            dia "Thank goodness."
            dia "These puppies are about to burst!"
            show diane f_smirk
            $ M_diane.set("sex_pre_milking", False)
            call screen milking_minigame
        "Not right now.":

            player_name "Sorry {b}Diane{/b}, I can't right now."
            show diane f_sad
            show diane f_sad_talk with dissolve
            dia "Oh... Too bad! "
            dia "These puppies are about to burst!"
            dia "I guess I'll take care of it myself then..."
            show player 13
            show diane f_sad
            player_name "I'll do it next time!"
            player_name "Take care, {b}Diane{/b}!"
            $ game.timer.tick()
    $ game.main()

label milking_game_pre_after_sex:
    show diane f_smirk b_naked a_naked_sides
    show player 365
    player_name "Yeah?"
    show player 366
    show diane f_smirk
    dia "Mmmhmm!"
    show diane f_smirk_talk
    dia "I've never been fucked like that, {b}[firstname]{/b}!"
    dia "Hehe, my legs are like jello right now..."
    show diane f_smirk
    show player 365
    player_name "Hehe."
    show player 366
    pause
    show diane f_smirk_talk
    dia "Phew, you should milk me before we go home."
    show diane f_smirk
    show player 365
    menu:
        "Sure!":
            player_name "Y-yeah?"
            show player 366
            show diane f_smirk_talk
            dia "Definitely."
            dia "The book says I'll produce the most milk immediately after a breeding session."
            show diane f_smirk
            show player 365
            player_name "O-okay."
            show player 366
            show diane f_smirk_talk
            dia "Just be gentle, {b}[firstname]{/b}."
            hide player
            hide diane
            with dissolve
            $ M_diane.set("sex_pre_milking", True)
            call screen milking_minigame
        "Not right now.":

            show player 366
            player_name "Sorry {b}Diane{/b}, I don't have time."
            show diane f_sad
            show diane f_sad_talk with dissolve
            dia "Oh... Too bad! "
            dia "These puppies are about to burst!"
            dia "I guess I'll take care of it myself then..."
            show player 365
            show diane f_sad
            player_name "I'll do it next time!"
            player_name "Take care, {b}Diane{/b}!"
            $ game.timer.tick()
    $ game.main()

label milking_minigame_done(earnings):
    scene expression "backgrounds/location_barn_day_blur.jpg"
    if M_diane.between_states(S_diane_return_production_book, S_diane_return_outfit_package):
        scene expression "backgrounds/location_barn_day_blur.jpg"
        show player 13 at left
        show diane f_laugh b_shirtless a_shirtless_sides
        with dissolve
        dia "Phew!"
        dia "That feels so much better!"
        show diane f_cheese
        pause
        show diane f_normal_talk
        dia "Thank you, {b}[firstname]{/b}."
        show diane f_normal
        show player 17
        player_name "You're welcome."
        show player 13
        show diane f_normal_talk
        dia "I don't know if it's you or this new equipment but that was the smoothest milking session I've ever had."
        dia "Just look at all that milk!"
        show diane f_normal
        show player 14
        player_name "Yeah, you had a lot in there."
        show player 13
        show diane f_laugh
        dia "Hehe!"
        show diane f_normal_talk
        dia "Keep this up and we'll fill my orders no problem!"
        show diane f_normal
        pause
        show diane f_normal_talk
        dia "I'm gonna go ahead and give you your cut now."
        show diane f_normal
        show player 5
        player_name "Hmm?"
        show diane f_normal_talk a_shirtless_money with dissolve
        dia "Here ya go."
        show diane f_normal b_shirtless a_shirtless_sides
        show player 640e
        with dissolve
        player_name "You're gonna pay me to do this?"
        show player 13 with dissolve
        show diane f_normal_talk
        dia "Well, of course."
        dia "It's a job afterall."
        show diane f_normal
        show player 14
        player_name "Yeah, but-"
        show player 13
        show diane f_smirk_talk
        dia "Believe me, those magic hands of yours are worth every penny."
        show diane f_smirk
        show player 14
        player_name "You're sure?"
        show player 13
        show diane f_smirk_talk
        dia "Yep."
        show diane f_normal_talk
        dia "Just remember, you have a garden to tend as well."
        show diane f_normal
        show player 14
        player_name "I remember."
        show player 13
        show diane f_normal_talk
        dia "Well, you'd best get to it then."
        show diane f_normal
        show player 14
        player_name "Thanks, {b}Diane{/b}."
        show player 13
        show diane f_normal_talk
        dia "You're welcome, handsome."
        hide player
        hide diane
        with dissolve

        $ game.timer.tick()
    else:

        if M_diane.is_set("breed first time"):
            if M_diane.get("sex_pre_milking"):
                show player 365 at left
            else:
                show player 14 at left
            show diane b_naked a_naked_sides f_smirk
            with dissolve
            player_name "That was a lot of milk!"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "Yeah it was."
            dia "You did well, {b}[firstname]{/b}!"
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "T-thanks!"
            hide player
            if M_diane.get("sex_pre_milking") or M_diane.outfit == "cow":
                show diane kiss_both_naked at Position (xoffset=-217)
            else:
                show diane kiss_shirtless
            with dissolve
            dia "Mmm."
            pause
            if M_diane.get("sex_pre_milking"):
                show player 366 at left
            else:
                show player 13 at left
            show diane b_naked a_naked_sides f_smirk_talk
            with dissolve
            dia "I should get cleaned up."
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Yeah, alright."
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "We're gonna do this a lot, {b}[firstname]{/b}..."
            show diane f_laugh
            dia "... And I mean, A LOT!"
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Heh, okay."
            player_name "See you at home?"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "You betcha."
            hide player
            hide diane
            with dissolve
            $ M_diane.set("breed first time", False)
            $ player.go_to(L_map)
            $ game.timer.tick(2)
        else:

            if M_diane.get("sex_pre_milking"):
                show player 366 at left
            else:
                show player 13 at left
            show diane b_naked a_naked_sides f_smirk_talk
            with dissolve
            dia "Nice work today, handsome."
            show diane f_smirk
            if M_diane.get("sex_pre_milking"):
                show player 365
            else:
                show player 14
            player_name "Thanks!"
            hide player
            if M_diane.get("sex_pre_milking"):
                show diane kiss_both_naked at Position (xoffset=-217)
            else:
                show diane kiss_shirtless
            with dissolve
            pause
            if M_diane.get("sex_pre_milking"):
                show player 365 at left
            else:
                show player 14 at left
            show diane b_naked a_naked_sides f_smirk
            with dissolve
            player_name "See you at the house tonight?"
            if M_diane.get("sex_pre_milking"):
                show player 366
            else:
                show player 13
            show diane f_smirk_talk
            dia "You betcha!"
            hide player
            hide diane
            with dissolve
            $ game.timer.tick()
    $ player.get_money(earnings)
    show expression "boxes/popup_minigame_07.png" as popup_milking at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide popup_milking
    with dissolve
    $ game.main()

label milking_minigame_fail:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    if M_diane.get("sex_pre_milking"):
        show player 368 at left
    else:
        show player 5 at left
    if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package):
        $ M_diane.outfit = "shirtless"
    show diane f_sad_talk b_naked a_naked_sides
    with dissolve
    dia "Hmm, well that was disappointing..."
    show diane f_sad
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Sorry, {b}Diane{/b}."
    player_name "I don't know what happened."
    if M_diane.get("sex_pre_milking"):
        show player 368
    else:
        show player 5
    show diane f_shamed_talk_smile
    dia "It's alright, handsome."
    dia "I'm probably just having a off day."
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "We'll can try again later, okay?"
    show diane f_shamed
    if M_diane.get("sex_pre_milking"):
        show player 367
    else:
        show player 10
    player_name "Y-yeah, okay."
    hide player
    hide diane
    with dissolve
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
