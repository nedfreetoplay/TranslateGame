label okita_office_door:
    $ player.go_to(L_school_floor3)
    if M_okita.is_set("office locked"):
        if player.has_item("keycode_note"):
            call screen okita_keypad
        else:

            call expression game.dialog_select("okita_office_door_need_keycode")
    else:

        if M_okita.is_state(S_okita_tired_from_belt):
            call expression game.dialog_select("okita_office_door_okita_tired")
        else:

            jump expression game.dialog_select("okita_office_dialogue")
    $ game.main()

label okita_office_door_need_keycode:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Хмм, Я думаю {b}Мисс Окита{/b} держит свой кабинет закрытым когда она не внутри?"
    player_name "Одна из этих автоматических клавиатур тоже заблокирована."
    show player 11
    pause
    show player 10
    player_name "Я определенно не могу туда войти без {b}кода{/b}."
    return

label okita_office_door_okita_tired:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Я должен дать ей отдохнуть на время."
    return

label okita_office_unlock:
    $ M_okita.set("office locked", False)
    jump expression game.dialog_select("okita_office_dialogue")

label okita_office_locked:
    $ player.go_to(L_school_floor3)
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10
    with dissolve
    player_name "Упс! Это не правильный код..."
    show player 34
    player_name "Хмм,мне лучше дважды проверить {b}код{/b} который я достал из стола {b}Директрисы Смит{/b} прежде чем попыться снова."
    $ game.main()

label third_floor_okita_get_ingredients:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 with dissolve
    player_name "Хмм, мне нужно попасть в кабинет к {b}Директрисе Смит{/b} еще раз чтобы поискать какие-то образцы ДНК..."
    player_name "Я должен туда пойти пока её там нет."
    return

label annie_enter_office_dialogue:
    $ player.go_to(L_school_floor3)
    if not M_okita.is_set("talked to annie"):
        call expression game.dialog_select("smith_office_annie_guarding")
        $ M_okita.set("talked to annie", True)
    else:

        call expression game.dialog_select("smith_office_annie_guarding_repeat")
        if player.has_required_chr(7):
            call expression game.dialog_select("smith_office_annie_guarding_distract_pass")
            $ player.go_to(L_school_smithoffice)
            $ game.main()
        else:

            call expression game.dialog_select("smith_office_annie_guarding_distract_fail")
    $ game.main()

label smith_office_annie_guarding_distract_pass:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 2 at left
    show annie 1 at right
    player_name "Я только подслушал твоего вора который хвастался возле раздевалки мальчиков..."
    show player 1
    show annie 3
    ann "Что? Серьезно!?"
    show player 2
    show annie 1
    player_name "Да и если ты поспешишь ты все еще можешь поймать его..."
    show player 1
    show annie 3
    ann "Директриса Смит безусловно наградит меня за это!"
    ann "Не присмотришь за этой дверю для меня?"
    show player 2
    show annie 1
    player_name "Не за что. Иди приведи его!"
    hide annie
    hide player
    show player 1f
    show annie 16 at left
    with dissolve
    ann "Хахаххахаха!"
    hide annie with dissolve

    show player 2f
    player_name "Что ж это должно занять её на какое-то время..."
    player_name "Сейчас я обыщу кабинет для того чтобы найти  {b}ДНК Директрисы Смит{/b}в нём."
    return

label smith_office_annie_guarding_distract_fail:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    player_name "[chr_warn]Х-хорошо..."
    player_name "[chr_warn]... Я просто искал {b}Директрису Смит{/b}."
    show player 11
    show annie 3
    ann "[chr_warn]Да, чтож её здесь нет."
    show annie 4
    ann "[chr_warn]Так что вали отсюда!"
    show player 12
    show annie 1
    player_name "[chr_warn]Хорошо, блин! Ты не сможешь получить кучу своих трусиков!"
    return

label smith_office_annie_guarding_repeat:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 11 at left
    show annie 3 at right
    with dissolve
    ann "Никто не пройдет мимо меня, {b}[firstname]{/b}!"
    return

label smith_office_annie_guarding:
    scene expression game.timer.image("location_school_third{}_blur")
    show player 10 at left
    show annie 1 at right
    with dissolve
    player_name "Энни, что ты здесь делаешь?"
    show player 11
    show annie 3
    ann "Я {b}охраняю кабинет Деректрисы Смит{/b} пока её нет."
    show player 10
    show annie 1
    player_name "... Почему?"
    show player 11
    show annie 3
    ann "Эммм, Может потому что она попросила меня? Ежу понятно."
    show annie 1
    player_name "..."
    show annie 3
    ann "Она сказала что кто то уже пробирался туда и она переживает за свои вещи."
    show annie 5
    ann "Тебе случаем ничего об этом не известно, не так ли?!"
    show player 10
    show annie 6
    player_name "М-мне? Нет, я ничего не знаю об этом!"
    show player 11
    show annie 5
    ann "Ну да..."
    show annie 3
    ann "Ладно кто бы это не был, {b}они не пройдут через меня!{/b}"
    show player 10
    player_name "Хорошо, ну удачи тебе с этим..."
    hide annie with dissolve
    hide player
    show player 5 with dissolve
    player_name "( Мне нужно придумать как пробраться в тот офис... )"
    show player 34
    player_name "(Возможно я смогу {b}развести её{/b} как-то? )"
    return

label third_floor_roxxy_intro:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show player 30 with dissolve
    player_name "( ... )"
    player_name "( Это похоже как {b}Рокси{/b} спорит с некоторыми учителями... )"
    show player 33
    player_name "( Я должен взглянуть поближе! )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
