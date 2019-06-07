label erik_indoors:
    $ player.go_to(L_erikhouse_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.over(erik_gf) and not erik.known(erik_gf_2):
        call expression game.dialog_select("erikentrance_erik_gf_over")
        $ erik.add_event(erik_gf_2)
        $ erik_gf_2.finish()
        $ M_june.set_default_locations([[L_school_computerlab, L_erikhouse_erikroom, L_NULL, L_NULL],
                                        [L_NULL, L_erikhouse_erikroom, L_NULL, L_NULL]])
        $ M_erik.set_default_locations([[L_school_computerlab, L_school_cafeteria, L_erikhouse_erikroom, L_erikhouse_erikroom],
                                        [L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_erikroom]])

    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):

        call expression game.dialog_select("erikentrance_erik_sex_ed_block")

    elif mrsj.over(mrsj_poker_night) and not mrsj.known(mrsj_poker_night_2):
        call expression game.dialog_select("erikentrance_mrsj_poker_night_over")
        $ mrsj.add_event(mrsj_poker_night_2)
        $ mrsj_poker_night_2.finish()

    elif erik.over(erik_thief_2) and not mrsj.known(mrsj_poker_night):
        call expression game.dialog_select("erikentrance_erik_thief_2_over")
        $ mrsj.add_event(mrsj_poker_night)

    elif erik.over(erik_thief) and not erik.known(erik_thief_2):
        call expression game.dialog_select("erikentrance_erik_thief_over")
        $ erik.add_event(erik_thief_2)
        $ erik_thief_2.finish()
        $ M_mrsj.unforce()
        $ player.go_to(L_erikhouse)

    elif mrsj.over(mrsj_yoga_help_2) and not erik.known(erik_breastfeeding) and game.timer.is_dark():
        call expression game.dialog_select("erikentrance_mrsj_yoga_2_over")
        $ erik.add_event(erik_breastfeeding)


    elif mrsj.started(mrsj_yoga_help_2):
        call expression game.dialog_select("erikentrance_mrsj_yoga_2_started")
        $ mrsj_yoga_help_2.finish()
        $ M_mrsj.place(place = L_erikhouse_mrsjroom)
        $ M_mrsj.force(tod = [2,3])
        $ M_erik.place(place = L_erikhouse_mrsjroom)
        $ M_erik.force(tod = [2,3])

    elif erik.over(erik_vr) and not mrsj.known(mrsj_yoga_help):
        call expression game.dialog_select("erikentrance_erik_vr_over")

        show unlock41 at truecenter with dissolve
        $ player.get_item("instructions1")
        pause
        $ mrsj.add_event(mrsj_yoga_help)
        $ M_anna.set_default_locations([[L_NULL, L_NULL, L_yoga_room, L_NULL]])
        hide unlock41 with dissolve

        show player 381
        player_name "I should have a look at those instructions before I go to yoga class tonight..."
        hide player with dissolve

    elif mrsj.started(mrsj_intro) and not game.timer.is_morning():
        call expression game.dialog_select("eriks_house_intro")
        if not game.timer.is_dark():
            call expression game.dialog_select("erikentrance_mrsj_intro_started_day")
        else:


            call expression game.dialog_select("erikentrance_mrsj_intro_started_night")
        $ mrsj_intro.finish()
        hide mrsj
        hide player
        with dissolve

    elif erik.completed(erik_orcette) and player.has_item("orcette") and not erik.known(erik_orcette_2):
        call expression game.dialog_select("erikentrance_erik_orcette_completed")
        $ erik.add_event(erik_orcette_2)
        hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
