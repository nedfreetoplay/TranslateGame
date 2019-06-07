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

label milking_minigame_done_daisy(earnings):
    scene expression player.location.background_blur with None
    show player 17 at left
    show daisy f_shy_down b_naked_shy a_naked_shy_front at Position (yoffset=10)
    with dissolve
    player_name "All done!"
    show player 1b
    show daisy f_shy_normal_talk at Position (yoffset=10)
    daisy "Aww, already?"
    show daisy f_shy_normal at Position (yoffset=10)
    show player 14b
    player_name "Heh, I don't think you have anything left in there..."
    show player 1b
    show daisy f_shy_normal_talk at Position (yoffset=10)
    daisy "Yeah, okay..."
    daisy "Can you milk me again later, {b}[firstname]{/b}?"
    show daisy f_shy_normal at Position (yoffset=10)
    show player 14b
    player_name "S-sure, if you want."
    show player 1b
    show daisy f_laugh b_naked a_naked_up with dissolve
    daisy "Yes, please!"
    daisy "It feels so good when you do it."
    show daisy f_normal a_naked_sides with dissolve
    pause
    hide player
    show daisy b_naked_hug f_empty a_empty
    with dissolve
    daisy "Thank you, {b}[firstname]{/b}!"
    daisy "You're the bestest man ever!"
    show player 14b at left
    show daisy b_naked a_naked_sides f_normal
    with dissolve
    player_name "You're welcome."
    player_name "I should probably get started on my other work."
    show player 1b
    show daisy f_normal_talk
    daisy "Okay, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "I'll see you soon, {b}Daisy{/b}."
    show player 1b
    show daisy f_laugh
    daisy "Byeeeee!"
    hide player with dissolve
    pause
    show daisy f_normal

    pause
    hide daisy with dissolve
    $ player.get_money(earnings)
    $ game.timer.tick()
    $ M_daisy.trigger(T_daisy_milked)
    $ game.main()

label milking_minigame_fail_daisy:
    scene expression player.location.background_blur with None
    show player 24 at left
    show daisy f_sad_talk
    with dissolve
    daisy "Are you okay, {b}[firstname]{/b}?"
    show daisy f_sad
    player_name "Y-yeah."
    show player 10b
    player_name "I guess, I'm just a little off my game today..."
    show player 5b
    show daisy f_normal_talk
    daisy "Hehe, that's alright."
    show daisy f_normal
    show player 10b
    player_name "You should go and ask {b}Diane{/b} to finish you off."
    show player 5b
    show daisy f_sad_talk
    daisy "I should?"
    show daisy f_sad
    show player 10b
    player_name "Yeah, I'm not having much luck..."
    show player 5b
    pause
    show player 10b
    player_name "Sorry, {b}Daisy{/b}."
    show player 5b
    show daisy f_normal_talk
    daisy "Aww... It's okay."
    daisy "Byeeeee {b}[firstname]{/b}!"
    hide daisy
    hide player
    with dissolve
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
                show diane kiss_naked
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
    call screen money_popup(earnings, "milking")
    with dissolve
    $ game.main()

label milking_minigame_fail:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    if M_diane.get("sex_pre_milking"):
        show player 368 at left
    else:
        show player 5 at left
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
