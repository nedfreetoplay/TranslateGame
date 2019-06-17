label hospital_second_floor_have_access_card:
    show player 410
    with dissolve
    player_name "( Вот она! )"
    player_name "( Теперь посмотрим, сработает ли... )"
    return

label hospital_second_floor_roz_storage_started:
    show player 12
    with dissolve
    player_name "( На проходной есть дубликаты всех ключей... )"
    player_name "( Может, я найду что-нибудь на её столе? )"
    return

label hospital_second_floor_mrsj_sex_ed_started:
    show player 35
    with dissolve
    player_name "Хмм..."
    player_name "( Где же хранятся лекарства? )"
    show player 30
    player_name "( Нужно найти {b}склад{/b}. )"
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
    player_name "Здрасьте!"
    pause
    player_name "Там... Это... на втором этаже сигнализация сработала!!"
    show player 407
    pause
    show player 408
    pause
    show player 407
    pause
    pause
    show player 406
    player_name "А, да, тут какой-то левый пациент шляется..."
    show player 407
    pause
    pause
    show player 406
    player_name "Да, это срочно!"
    show player 408
    pause
    pause
    show player 407
    pause
    show player 406
    player_name "Спасибо..."
    show player 407
    pause
    show player 405 with dissolve
    player_name "( Ну... должно сработать... )"
    player_name "( Теперь бегом к её столу... )"
    hide player
    with dissolve
    return

label hospital_second_floor_phone_nothing:
    player_name "( Мне не нужно никому звонить. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
