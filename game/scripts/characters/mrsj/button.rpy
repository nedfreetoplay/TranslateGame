label mrsj_button_dialogue:
    if player.location == L_erikhouse_entrance:
        scene expression game.timer.image("erik_entrance{}_c")
    elif player.location == L_erikhouse_mrsjroom:
        if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
            call expression game.dialog_select("button_mrsj_sex_ed_intro")
            jump mrsj_button_dialogue_repeat

        elif game.timer.is_dark() and erik.over(erik_gf):
            call expression game.dialog_select("button_mrsj_private_yoga_intro")
            jump mrsj_button_dialogue_repeat
        scene erik_house_upstairs_night_c01
    call expression game.dialog_select("button_mrsj_greetings")
    menu mrsj_button_dialogue_repeat:
        "About {b}Erik{/b}." if erik.started(erik_path_split):
            call screen route_warning
            call expression game.dialog_select("button_mrsj_about_erik")
            menu mrsj_route_split:
                "Sex education.":
                    call expression game.dialog_select("button_mrsj_route_sex_ed")
                    $ erik_path_split.finish()
                    $ erik.add_event(erik_sex_ed)
                    $ M_mrsj.place(place = L_erikhouse_mrsjroom)
                    $ M_mrsj.force()
                    $ M_erik.place(place = L_erikhouse_erikroom)
                    $ M_erik.force()
                    jump mrsj_button_dialogue_repeat
                "Get him a girlfriend.":

                    call expression game.dialog_select("button_mrsj_route_gf")
                    $ erik_path_split.finish()
                    $ June.add_event(june_intro)
                    jump mrsj_button_dialogue_repeat

        "Sex education." if mrsj.started(mrsj_sex_ed):
            call expression game.dialog_select("button_mrsj_sex_ed_prep")

        "Sex education." if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
            jump mrsj_3some

        "Private Yoga." if game.timer.is_dark() and erik.over(erik_gf):
            jump mrsj_private_yoga

        "Girlfriend." if erik.started(erik_gf):
            call expression game.dialog_select("button_mrsj_erik_got_gf")
            $ erik_gf.finish()
            call expression game.dialog_select("erik_house_dialogue")

        "Girlfriend." if erik.in_progress(erik_gf_stolen):
            call expression game.dialog_select("button_mrsj_erik_stole_gf")
            call expression game.dialog_select("erik_house_dialogue")

        "Girlfriend." if June.started(june_intro_2):
            call expression game.dialog_select("button_mrsj_erik_introduce_june")
            $ june_intro_2.finish()
            jump mrsj_button_dialogue_repeat

        "Breastfeeding." if erik.over(erik_breastfeeding_2) and (not erik.known(erik_sex_ed) and not mrsj.known(mrsj_sex_ed) and not June.known(june_intro)):
            call expression game.dialog_select("button_mrsj_breastfeeding")

        "What did you need me to do?" if mrsj.started(mrsj_yoga_help):
            call expression game.dialog_select("button_mrsj_yoga_help_repeat")

        "Where's {b}Erik{/b}?" if not game.timer.is_dark():
            show player 14
            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show mrsj 17
                mrsjo "Well, he should be at {b}school{/b} right now."
            else:

                show mrsj 14
                player_name "Do you know where I could find {b}Erik{/b}?"
                show player 1
                show mrsj 17
                mrsjo "Well, I think I saw him go into the {b}basement{/b}."
                mrsjo "If he's not down there, he might be in his room."
                show mrsj 14
                show player 17
                player_name "Thanks, {b}Mrs. Johnson{/b}!"
            show mrsj 14
            jump mrsj_button_dialogue_repeat

        "You're so fit!" if not game.timer.is_dark():
            call expression game.dialog_select("button_mrsj_youre_so_fit")
            jump mrsj_button_dialogue_repeat

        "Invite to poker." if mrsj.known(mrsj_poker_night) and not game.timer.is_night():
            show player 14 at left
            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39 at right
            elif game.timer.is_dark() and erik.over(erik_gf):
                show mrsj 53
            else:
                show mrsj 14 at right

            if game.timer.is_morning() and not game.timer.is_weekend():
                player_name "I was wondering if you could teach us how to play poker?"
                show player 11
                show mrsj 19
                mrsjo "Shouldn't you be at school right now??"
                mrsjo "{b}Erik{/b} already left!"
                show player 29
                show mrsj 14
                player_name "Oh, crap! You're right..."
                player_name "Maybe later then!"

            elif player.stats.chr() >= 5 and poker_bot02 == "" and not game.timer.is_morning():
                if mrsj.completed(mrsj_poker_night_2):
                    show player 14 at left
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14 at right
                    player_name "Would you like to play some poker with us again?"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "Still looking for friends to play with?."
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Well, It's just that-"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "It's fine!!"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "I'll play with you boys..."
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Really?"
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40b
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 20
                    mrsjo "Well... last time was a bit much..."
                    show player 13
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "But, why not?"
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "Okay."
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "When are we playing?"
                    show player 14
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 39
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 53
                    else:
                        show mrsj 14
                    player_name "After dinner tonight."
                    player_name "{b}Erik{/b} and I will set up the game."
                    show player 1
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40b
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 18
                    mrsjo "Haha, alright."
                    if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show mrsj 40
                    elif game.timer.is_dark() and erik.over(erik_gf):
                        show mrsj 54
                    else:
                        show mrsj 17
                    mrsjo "See you then!"
                else:

                    call expression game.dialog_select("button_mrsj_invite_poker")
                $ poker_bot02 = "mrsj"
                $ poker_sayer02 = mrsjo
                $ M_mrsj.place(place = L_erikhouse_basement)
                $ M_mrsj.force(tod = [2,3])
                $ M_erik.place(place = L_erikhouse_basement)
                $ M_erik.force(tod = [2,3])
            else:

                if player.stats.chr() < 5 and not game.timer.is_morning():
                    $ stat_warn = chr_warn
                else:
                    $ stat_warn = ""
                player_name "[stat_warn]I was wondering if you could teach us to play poker?"
                show mrsj 17
                show player 1
                mrsjo "[stat_warn]The card game?"
                show mrsj 14
                show player 14
                player_name "[stat_warn]Yeah, {b}Erik{/b} and I are just looking for a third player."
                show mrsj 17
                show player 14
                mrsjo "[stat_warn]Oh, I'd love to."
                show player 19
                mrsjo "[stat_warn]But I really just don't have the time right now, sorry..."
                show mrsj 14
                show player 14
                player_name "[stat_warn]That's alright, maybe some other time."
        "I have to go!":

            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39
                show player 14 at left
                player_name "I have to go, but I'll be back though!"
            else:
                if game.timer.is_dark() and erik.over(erik_gf):
                    show mrsj 53
                else:
                    show mrsj 14 at right
                show player 14 at left
                player_name "I should go find {b}Erik{/b}!"
            if game.timer.is_dark() and (mrsj.over(mrsj_sex_ed) or erik.over(erik_gf)):
                if mrsj.over(mrsj_sex_ed):
                    show mrsj 40
                elif erik.over(erik_gf):
                    show mrsj 54
                show player 1 at left
                mrsjo "Really?"
                mrsjo "Well be sure to come back soon!"
            else:
                show mrsj 18 at right
                show player 1 at left
                mrsjo "Alright, then!"
            if game.timer.is_dark() and mrsj.over(mrsj_sex_ed):
                show mrsj 39
            elif game.timer.is_dark() and erik.over(erik_gf):
                show mrsj 53
            else:
                show mrsj 14 at right
            show player 17 at left
            player_name "Bye, {b}Mrs. Johnson{/b}!"
    hide player
    hide erik
    hide mrsj
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
