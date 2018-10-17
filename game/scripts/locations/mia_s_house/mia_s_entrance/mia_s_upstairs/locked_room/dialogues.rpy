label helens_locked_room_mia_locked_room:
    scene mia_house_locked_night_b
    show object_bed_11 at Position (xpos=527,ypos=765)
    show player 23 at left with dissolve
    player_name "{b}МИЯ{/b}!"
    player_name "Ты связана?!"
    show player 10
    player_name "Подожди, я помогу тебе..."
    hide player with dissolve
    return

label mia_tied_up:
    call expression game.dialog_select("mia_tied_up_dialogue")
    $ game.timer.tick(3)
    $ M_mia.trigger(T_mia_rescue)
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_tied_up_dialogue:
    scene mia_house_cs01
    with fade
    show text "{b}Мия{/b} была привязана на кровати, в запертой комнате.\nНе было времени обдумать то, что я видел...\n...Я должен был что-то сделать!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve

    scene mia_house_locked_c
    show player 5 at left
    show mia 40f at right
    with dissolve
    pause
    show mia 41f with dissolve
    pause
    show mia 42f at Position (xoffset=-15) with dissolve
    mia "Ох..."
    show mia 43f at Position (xpos=500) with dissolve
    mia "{b}[firstname]{/b}!!!"
    show mia 44f
    show player 10
    player_name "{b}Мия{/b}! Что происходит?!"
    player_name "Я получил твое сообщение на телефон и-"
    show player 11
    show mia 43f
    mia "Мы должны уходить, быстро!"
    show mia 44f
    show player 12
    player_name "Подожди {b}Мия{/b}, что происходит?"
    show player 11
    show mia 43f
    mia "Моя мама становится {b}невменяемой{/b}!!"
    mia "Она заперла меня здесь..."
    mia "...Заставив меня читать Библию и молиться, весь день..."
    show player 22
    mia "...ПРИВЯЗАННОЙ К ЭТОЙ КРОВАТИ!!!"
    show mia 44f
    show player 23
    player_name "Что?! Это безумие!"
    show player 11
    show mia 43f
    mia "Нет времени говорить об этом сейчас."
    mia "Нам нужно убираться отсюда!!!"
    show mia 44f
    show player 10
    player_name "Сейчас?!"
    show player 11
    show mia 46f
    mia "ДА!"
    show mia 45f
    show player 10
    player_name "Подождите, куда?!?!"
    show player 5
    show mia 46f
    mia "Неважно, Я не останусь здесь ни мину-"
    hide player
    show player 22 at left
    show mia 45 at Position (xpos=420)
    show helen 6 at right
    with dissolve
    player_name "!!!"
    show helen 7 with dissolve
    helen "Как ты {b}посмел{/b} вернуться сюда... {b}в мой дом{/b}!"
    show helen 8
    show player 24
    show mia 47 at Position (xpos=465) with dissolve
    mia "{b}Мама{/b}! {b}ОСТАНОВИСЬ{/b}!!!"
    show mia 48
    show helen 7
    helen "Я не позволю этому злодею забрать тебя у меня..."
    show helen 10 at Position (xpos=950) with dissolve
    helen "...{b}ЭТО{/b} единственное, что имеет значение..."
    show player 22
    helen "...Я {b}СПАСУ ТЕБЯ{/b}!!!"
    show helen 11
    pause.5
    show helen 8 at Position (xpos=750)
    show harold 12 at right
    with dissolve
    harold "{b}Хелен{/b}, почему ты так кричишь?!"
    show harold 14
    show helen 7b
    helen "Возвращайся вниз, {b}Harold{/b}."
    show helen 8b
    show harold 13
    show player 11
    harold "Нет, подожди минуточку {b}Helen{/b}!"
    harold "Это слишком, и зашло слишком далеко!!"
    show harold 14
    show helen 7b
    show player 22
    helen "{b}ТИХО{/b}!"
    helen "Мне надоело твое паршивое воспитание..."
    helen "...Ты {b}НИКОГДА{/b} не был способен контролировать нашу дочь!"
    show helen 8
    show player 11
    hide mia
    show mia 46 at Position (xpos=425) with dissolve
    mia "{b}Папа{/b}!"
    show helen 8b
    hide mia
    show harold 15
    with dissolve
    mia "Пожалуйста, остановите это!"
    harold "..."
    show helen 7b
    helen "Она должна остаться здесь."
    show helen 8b
    show harold 17
    harold "Нет."
    show harold 16
    helen "..."
    show harold 17
    harold "Хватит!"
    pause
    show player 22
    harold "А ты!"
    show harold 16
    show helen 8
    player_name "???"
    show harold 17
    harold "Ты не должен быть здесь."
    harold "Иди домой и позволь мне разобраться с этим!"
    show harold 16
    show player 10
    player_name "Да, простите, я обязательно... Я как раз собираюсь уходить."
    hide player with dissolve
    show helen 7b
    helen "Нам нужно поговорить, {b}Harold{/b}."
    show helen 8b
    show harold 17
    harold "Я так не думаю, {b}Хелен{/b}."
    harold "Здесь нечего обсуждать."
    harold "{b}Mia{/b} идет в свою комнату и мы разберемся с этим завтра!"
    hide harold
    hide helen
    scene black
    with fade
    pause

    scene miahouse_night
    show player 12 with dissolve
    player_name "{b}Хелен{/b} сошла {b}С УМА{/b}!!"
    player_name "Я и подумать не мог, что было так плохо с родителями {b}Мии{/b}..."
    player_name "...До того, чтобы связать её?! Это безумие!"
    show player 24
    player_name "{b}*Вздох*{/b}"
    player_name "Я чувствую себя виноватым перед {b}Мией{/b}..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
