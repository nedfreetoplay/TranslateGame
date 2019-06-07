label hospital_second_floor_have_access_card:
    show player 410
    with dissolve
    player_name "( This must be it! )"
    player_name "( Let's see if it works... )"
    return

label hospital_second_floor_roz_storage_started:
    show player 12
    with dissolve
    player_name "( The receptionist probably has duplicates of all the keys... )"
    player_name "( Perhaps I could find some at her desk? )"
    return

label hospital_second_floor_mrsj_sex_ed_started:
    show player 35
    with dissolve
    player_name "Hmm..."
    player_name "( I wonder where they store all their medicine... )"
    show player 30
    player_name "( I should find the {b}storage room{/b}. )"
    return

label hospital_second_floor_phone_dialogue:
    scene hospital_phone
    pause
    if mrsj.started(mrsj_sex_ed) and Roz.completed(roz_intro) and Roz.known(roz_storage) and not Roz.known(roz_trick):
        call expression game.dialog_select("hospital_second_floor_phone_mrsj_sex_ed_started")
        $ Roz.add_event(roz_trick)
        $ M_roz.place(place = L_NULL)
        $ M_roz.force()
    else:

        call expression game.dialog_select("hospital_second_floor_phone_nothing")
    $ game.main()

label hospital_second_floor_phone_mrsj_sex_ed_started:
    show player 404 with dissolve
    pause
    show player 406 with dissolve
    player_name "Hi!"
    pause
    player_name "I... Umm... There's an emergency on the second floor!!"
    show player 407
    pause
    show player 408
    pause
    show player 407
    pause
    pause
    show player 406
    player_name "Oh, yes, it's about an unregistered patient..."
    show player 407
    pause
    pause
    show player 406
    player_name "Yes, it's urgent!"
    show player 408
    pause
    pause
    show player 407
    pause
    show player 406
    player_name "Thank you..."
    show player 407
    pause
    show player 405 with dissolve
    player_name "( Well... that should work... )"
    player_name "( Let's see if she left her desk... )"
    hide player
    with dissolve
    return

label hospital_second_floor_phone_nothing:
    player_name "( I have no reason to call anyone. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
