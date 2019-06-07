label sis_bedroom_dialogue:
    $ player.go_to(L_home_sisbedroom)
    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    if not game.timer.is_dark():
        if not M_jenny.pregnancy.announced_pregnancy and M_jenny.pregnancy.stage == 1:
            if M_jenny.pregnancy.first_baby:
                call expression game.dialog_select("sis_bedroom_jenny_pregnancy_announcement_first")
            else:
                call expression game.dialog_select("sis_bedroom_jenny_pregnancy_announcement_repeat")
            $ M_jenny.pregnancy.announced_pregnancy = True

        if M_bissette.is_state(S_bissette_roxxy_cheerleader_deal):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_cheerleader_deal")
            $ M_bissette.trigger(T_bissette_jenny_deal)

        elif M_bissette.is_state(S_bissette_roxxy_jenny_spying):
            call expression game.dialog_select("jennys_bedroom_bissette_roxxy_jenny_spying")
            $ M_bissette.trigger(T_bissette_roxxy_jenny_spied)
            $ game.timer.tick()
            $ player.go_to(L_home_hallway)

        if M_jenny.is_state(S_jenny_snoop_around):
            $ M_bissette.trigger(T_bissette_jenny_deal)
            call expression game.dialog_select("jennys_bedroom_jenny_snoop_around")
        elif M_jenny.is_state(S_jenny_go_to_her_room) and not M_jenny.get("went_to_her_room"):
            if M_jenny.get("dominance") > 0:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant")
                if player.has_money(200):
                    call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_has_money")
                    $ player.spend_money(200)
                    $ game.timer.tick()
                    $ M_jenny.trigger(T_jenny_pay_for_favors)
                else:
                    call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_no_money")
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive")
                if player.has_money(200):
                    call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_has_money")
                    $ player.spend_money(200)
                    $ game.timer.tick()
                    $ M_jenny.trigger(T_jenny_pay_for_favors)
                else:
                    call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_no_money")
            $ M_jenny.set("went_to_her_room", True)
            $ game.main()
        elif M_jenny.is_state(S_jenny_get_a_toy):
            call expression game.dialog_select("sis_bedroom_jenny_get_a_toy")
            if M_jenny.get("dominance") <= 0:
                call expression game.dialog_select("sis_bedroom_jenny_get_a_toy_submissive")
            else:
                call expression game.dialog_select("sis_bedroom_jenny_get_a_toy_dominant")
            call expression game.dialog_select("sis_bedroom_jenny_get_a_toy_end")
            $ M_jenny.trigger(T_jenny_get_a_toy)
        elif M_jenny.is_state(S_jenny_deliver_bad_monster) and player.has_item("badmonster"):
            call expression game.dialog_select("jenny_bedroom_jenny_deliver_bad_monster")
            $ player.remove_item('badmonster')
            $ M_jenny.trigger(T_jenny_gave_bad_monster)
        elif M_jenny.is_state(S_jenny_get_a_mask_quest) and game.timer.is_afternoon():
            call expression game.dialog_select("sis_bedroom_jenny_get_a_mask_quest")
            $ M_jenny.trigger(T_jenny_get_a_mask)
        elif M_jenny.is_state(S_jenny_start_camshow_blowjob) and game.timer.is_afternoon():
            call expression game.dialog_select("sis_bedroom_jenny_start_camshow_blowjob")
        elif M_jenny.is_state(S_jenny_get_cheerleader_outfit):
            call expression game.dialog_select("sis_bedroom_jenny_get_cheerleader_outfit")
            $ player.go_to(L_home_hallway)
            $ game.main()
        elif M_jenny.is_state(S_jenny_cheerleader_sex) and game.timer.is_afternoon():
            call expression game.dialog_select("sis_bedroom_jenny_cheerleader_sex")
            jump jenny_cheer_sex_loop_tied

    elif game.timer.is_dark():
        if M_jenny.is_state(S_jenny_figure_out_password) and not M_jenny.get("hacked pc") and not M_jenny.get("figure_out_pass_dialogue"):
            call expression game.dialog_select("upstairs_bedroom_jenny_figure_out_password")
            $ M_jenny.set("figure_out_pass_dialogue", True)
    $ game.main()

label sis_panties_dialogue:
    scene expression player.location.background_blur with None
    show player 723 with dissolve
    $ player.get_item("jenny_panties")
    player_name "( These are {b}[jen_name]'s{/b} panties. )"
    player_name "( I wonder why she keeps a pair in her nightstand? )"
    pause
    if M_somrak.finished_state(S_somrak_start):
        player_name "( I bet {b}Master Somrak{/b} would like these. )"
    elif M_jenny.is_state(S_jenny_snoop_around, S_jenny_snoop_diary):
        player_name "( Better put them back before she catches me. )"
        $ player.remove_item("jenny_panties")
        $ player.inventory.remove_picked_up("jenny_panties")
    hide player with dissolve
    jump jenny_out_of_bedside_table

label jenny_out_of_bedside_table:
    if M_jenny.is_state(S_jenny_snoop_around, S_jenny_snoop_nightstand):
        $ M_jenny.trigger(T_jenny_looked_at_nightstand)
        call jenny_return_from_shower_check
    $ game.main()

label upstairs_bedroom_out_of_diary:
    if M_jenny.is_state(S_jenny_snoop_around, S_jenny_snoop_diary):
        $ M_jenny.trigger(T_jenny_looked_at_diary)
        scene expression player.location.background_closeup with None
        show player 5 with dissolve
        player_name "( Wow, I can't believe how conceited she is... )"
        player_name "( I should hurry up and {b}find that camera{/b}! )"
        if M_jenny.is_state(S_jenny_snoop_nightstand):
            show player 4 with dissolve
            player_name "( ... Maybe it's {b}in her nightstand{/b}? )"
        hide player with dissolve
        call jenny_return_from_shower_check
    elif M_jenny.is_state(S_jenny_snoop_around_for_laptop):
        scene expression player.location.background_closeup with None
        show player 23 with dissolve
        player_name "Whoa!!"
        player_name "{b}[jen_name]{/b} is masturbating for men over the internet?!"
        player_name "She's completely lost her mind!"
        player_name "{b}[deb_name]{/b} would totally freak if she found out about this..."
        show player 22
        pause
        show player 35
        player_name "I wonder if I can sneak a peek at this somehow?"
        show player 34
        pause
        show player 35
        player_name "... Maybe I can find some stuff on {b}her laptop{/b}?"
        hide player with dissolve
        $ M_jenny.trigger(T_jenny_check_laptop)
    elif M_jenny.is_state(S_jenny_diary_clue) and not M_jenny.get("checked_diary_j22"):
        $ M_jenny.set("checked_diary_j22", True)
        scene expression player.location.background_blur
        show player f_laugh with dissolve
        player_name "( That's it! )"
        show player f_normal
        player_name "( {b}I should buy her something nice and see if that makes her re-think this whole dating thing!{/b} )"
        show player f_thinking
        player_name "( Now the only question is, what do I buy her? )"
        show player a_dressed_thinking with dissolve
        player_name "( Hmm, {b}she'll want something expensive{/b}, no doubt! )"
        show player f_normal a_dressed_pocket with dissolve
        player_name "( {b}I should head to the mall and see about getting her a necklace or something.{/b} )"
        hide player with dissolve
    $ game.main()

label bedside01_dialogue:
    if L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_bedroom_cannot_snoop")
        $ game.main()
    if M_jenny.is_state(S_jenny_snoop_around, S_jenny_snoop_nightstand):
        call expression game.dialog_select("sister_bedtable_panties")
    call screen bedside01

label jenny_return_from_shower_check:
    if M_jenny.is_state(S_jenny_caught_snooping):
        call expression game.dialog_select("jennys_bedroom_jenny_caught_snooping")
        $ M_jenny.trigger(T_jenny_caught_snooping)
        $ game.timer.tick()
    return

label jenny_sleeping_button:
    if game.timer.is_evening():
        scene expression "backgrounds/location_home_jennybedroom_jenny_evening_blur.jpg"
        show popup_unfinished at truecenter with dissolve
        pause
        hide popup_unfinished with dissolve
    else:
        scene expression player.location.background_closeup with None
        show player 22b with dissolve
        player_name "( Whoa, don't be crazy {b}[firstname]{/b}! )"
        player_name "( She will definitely kill me if I wake her up! )"
        hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
