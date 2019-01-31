label erik_room_dialogue:
    $ player.go_to(L_erikhouse_erikroom)
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        scene expression game.timer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( Хм, {b}Эрика{/b} здесь нет. Он должен быть в подвале... )"
        hide player with dissolve

    elif erik.completed(erik_bullying) and not erik.known(erik_bullying_2):
        call expression game.dialog_select("erik_bullying")
        $ erik.add_event(erik_bullying_2)
        $ M_erik.unforce()

    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        call expression game.dialog_select("eriksroom_erik_bullying_3_completed")

    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        call expression game.dialog_select("erik_sex_ed")
        $ erik_sex_ed.finish()
        $ M_erik.place(place = L_erikhouse_mrsjroom)

    elif June.started(june_intro):
        call expression game.dialog_select("june_intro")
        $ june_intro.finish()
        jump erik_talk

    elif erik.started(erik_breastfeeding):
        call expression game.dialog_select("eriksroom_erik_breastfeeding_started")
        $ erik_breastfeeding.finish()
        $ M_mrsj.set_default_locations([[L_erikhouse_entrance, L_yoga_room, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom],
                                        [L_erikhouse_entrance, L_yoga_room, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom]])

    if player.location.is_here(M_erik):
        if not erik.started(erik_card_hunt) and not player.location.is_here(M_june):
            $ playSound("<loop 3>audio/ambience_erikroom.ogg")
    $ game.main()

label erik_cards:
    if player.has_item("eriks_cards"):
        show erik 1 at right
        show player 14 at left
        player_name "Я нашел твои карты, {b}Эрик{/b}!"
        show player 239_240
        pause
        show player 374 with dissolve
        player_name "Вот держи..."
        show player 5 with dissolve
        if player.location == L_school_scienceclassroom:
            show erikl 35 at right
        show erik 36 at Position (xpos=1014)
        with dissolve
        eri "Круто!"
        eri "Вот, ты должен увидеть новую карту которую я получил."
        eri "Я почти уверен что это будет быстрая победа в предстоящем турнире!"
        show erik 38
        eri "..."
        eri "Где она?"
        pause
        show player 11
        eri "НЕТ! Её здесь нет!"
        show player 12
        player_name "Ты уверен?"
        show player 11
        show erik 37
        eri "Да, я уверен! Я немогу в это поверить! Моя карта {b}Кольцо с шипами на королевский член{/b} пропала!!"
        show erik 2 at right
        if player.location == L_school_scienceclassroom:
            show erikl 2 at right
        with dissolve
        eri "Что мне теперь делать?"
        eri "Я в полной жопе."
        show erik 3
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        with dissolve
        eri "Она была самой... Ценной..."
        show player 34
        player_name "Хмм..."
        show player 33
        player_name "Возможно я смогу помочь."
        show player 13
        show erik 5
        eri "И как же?"
        show erik 3b
        show player 17
        player_name "Я могу достать тебе ещё одну."
        show player 13
        show erik 5
        eri "И как ты собираешься это сделать?"
        show erik 3b
        show player 35
        player_name "Они продают эти карты в {b}Cosmic Cumics{/b} не так ли?"
        show player 13
        show erik 5
        eri "Да но они очень дорогие!"
        show erik 5b
        eri "... А я на мели."
        show erik 3b
        pause
        show player 14
        player_name "Не волнуйся, чувак. Я работаю сейчас на {b}[deb_name]{/b}, подругу {b}Дианы{/b}."
        show player 13
        show erik 4
        eri "Ты реально купишь мне новую? Ты лучший, чувак!"
        show erik 1
        show player 14
        player_name "Я рад помочь!"
        show player 17
        player_name "Кроме того, Я хочу увидеть как ты выиграешь этот турнир!"
        $ player.remove_item("eriks_cards")
        $ erik_card_hunt.finish()
        $ erik.add_event(erik_crown_card)
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Где ты видел свои карты в последний раз?"
        show player 11
        show erik 5
        eri "Хммм... Я думаю что в последний раз Я взял их отсюда и оставил здесь."
        eri "Я играл в подвале... Но, {b}Миссис Джонсон{/b} возможно куда-то их засунула..."
        show erik 1
        show player 14
        player_name "Я помогу тебе их найти."
        show player 13
        show erik 5
        eri "Спасибо."
        show erik 3
        eri "Я действительно должен их найти перед турниром на следующих выходных..."
    hide erik
    hide erikl
    hide player
    with dissolve
    return

label erik_crown_card:
    if player.has_item("card02"):
        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 14 at left
        player_name "Я получил карту которую ты хотел."
        show player 13
        show erik 4
        eri "{b}Кольцо с шипами на королевский член{/b}!?"
        show erik 1
        show player 2
        player_name "Ага!"
        show player 239_240
        pause
        show player 372 with dissolve
        player_name "Вот держи..."
        show player 13 with dissolve
        show erik 40 at Position (xpos=1014)
        if player.location == L_school_scienceclassroom:
            show erikl 40 at right
        with dissolve
        eri "Ты крутой! Большое тебе Спасибо!"
        eri "С этой картой моя победа будет гарантирована!"
        eri "Я буду непобедимый! Крестьяне будут преклоняться передо мной..."
        show erik 39
        show player 17
        player_name "Ха ха."
        show player 13
        pause
        show erik 41
        eri "Подожди секундочку."
        show erik 36
        if player.location == L_school_scienceclassroom:
            show erikl 35 at right
        with dissolve
        eri "Я хочу тебе дать одну из моих карт..."
        show erik 30 at Position (xpos=1025)
        if player.location == L_school_scienceclassroom:
            show erikl 30 at right
        with dissolve
        show player 10
        player_name "Карт-"
        show player 11
        show erik 31
        eri "Это одна из моих любимых... Но у меня есть несколько экземпляров..."
        show erik 1
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        with dissolve
        show player 371 with dissolve
        player_name "Хм..."
        hide player
        hide erik
        hide erikl
        with dissolve
        show card_03_c at Position (ypos=650) with dissolve
        pause
        hide card_03_c with dissolve
        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 370 at left
        with dissolve
        player_name "...Спасибо!"
        show player 13 with dissolve
        show erik 4
        eri "Не волнуйся об этом!"
        eri "Это благодарность тебе за то что достал для меня эту карту."
        eri "Плюс, Я знаю что ты позоботишься о ней должным образом."
        show erik 1
        show player 14
        player_name "Что ж, спасибо бро!"
        show player 13
        show erik 5
        eri "Только.. Не отставляй ее на солнце потому что она станет увядать."
        show erik 1
        show player 17
        player_name "Ха ха, Я обещаю..."
        $ player.remove_item("card02")
        show unlock37 at truecenter with dissolve
        $ player.get_item("card03")
        pause
        hide unlock37 with dissolve
        $ erik_crown_card.finish()
        $ M_erik.place(place = L_erikhouse_basement)
        $ M_erik.force()
    else:

        show erik 1 at right
        if player.location == L_school_scienceclassroom:
            show erikl 1f at right
        show player 10 at left
        player_name "Какая карта пропала ещё раз?"
        show player 11
        show erik 5
        eri "Хмм... Она назывется {b}Кольцо с шипами на королевский член{/b}."
        eri "Ты сказал что ты сможешь её найти в {b}Cosmic Cumics{/b}?"
        show erik 1
        show player 14
        player_name "Ох точно!"
        player_name "Посмотрю если ли она там..."
    hide erik
    hide erikl
    hide player
    with dissolve
    $ game.main()

label erik_package:
    if player.has_item("orcette"):
        show erik 1 at right
        show player 376 at left with dissolve
        player_name "Вот она твоя новая игрушка!"
        show player 378
        show erik 4
        eri "Что? Ты ее уже получил?"
        show erik 1
        show player 376
        player_name "Ага!"
        show player 13 with dissolve
        show erik 43 at Position (xpos=1014)
        if player.location == L_school_scienceclassroom:
            show erikl 42 at right
        with dissolve
        eri "Приятно!"
        eri "Эта штука выглядит... Круто!"
        eri "Он даже имеет цвет в самый раз..."
        show player 14
        player_name "Ты когда нибудь пользовался этим раньше?"
        show player 13
        show erik 44
        eri "Нет, но я всегда хотел попробовать!"
        eri "{b}Миссис Джонсон{/b} ничего не видела? Я не хочу чтобы она была в бешенстве..."
        show erik 42
        show player 12
        player_name "Хех, я думаю она бы с этим смирилась. Она кажется очень классной!"
        show player 13
        show erik 44
        eri "Может быть..."
        show erik 42
        show player 12
        player_name "Эту штуку... Легко чистить?"
        show player 13
        show erik 43
        eri "Я думаю она пришла с инструкциями, но сначала я её должен ополоснуть."
        show erik 42
        pause
        show erik 43
        pause
        show player 18
        player_name "..."
        show player 17
        player_name "Ох, {b}Эрик{/b}..."
        show player 18
        show erik 44
        eri "Что?!"
        show erik 42
        show player 14
        player_name "Ничего."
        show player 13
        show erik 43
        pause
        show player 33
        player_name "Что ж, Мне лучше оставить вас обоих на едине..."
        show player 13
        show erik 44
        eri "{b}[firstname]{/b}, спасибо еще раз."
        show erik 43
        show player 14
        player_name "Все хорошо..."
        player_name "...Просто убедись что дверь заперта!"
        $ player.remove_item("orcette")
        $ erik_orcette_2.finish()
        $ event_wait_till = game.timer.game_day() + 2
    else:
        show erik 1 at right
        show player 12 at left
        player_name "Что за предмет ты хотел?"
        show player 13
        show erik 5
        eri "Это что-то вроде резиновой трубы... Называется {b}Orcette{/b}..."
        eri "Ты можешь найти его в Интернете."
        show erik 1
        show player 14
        player_name "Отлично, понял."
        show player 13
        show erik 4
        eri "Спасибо, {b}[firstname]{/b}."
    hide erik
    hide erikl
    hide player
    with dissolve
    $ game.main()

label erik_vr_game:
    if player.has_item("game02") and player.has_item("virtualsaga"):
        show erik 1 at right with dissolve
        show player 14 at left with dissolve
        player_name "Понял!"
        show player 239_240
        pause
        show player 400
        player_name "Я получил VR Гарнитуру!"
        show player 399
        show erik 4
        eri "Ох, да?!"
        show player 13 with dissolve
        show erik 46
        if player.location == L_school_scienceclassroom:
            show erikl 45 at right
        with dissolve
        eri "Вау... Это наверное было очень дорого..."
        show erik 47
        eri "Сколько это стоило?!"
        show erik 45
        show player 17
        player_name "Эээ, не волнуйся об этом."
        show player 14
        player_name "Я накопил много денег."
        show player 13
        show erik 46
        eri "Это... круто."
        show erik 45
        show player 12
        player_name "Ох, вот и игра, тоже!"
        show player 13
        show erik 47
        eri "Спасибо, {b}[firstname]{/b}."
        eri "Я уже упоминал о наличие людей в подвале с {b}Миссис Джонсон{/b}."
        eri "Она не возражала чтобы мы использовали его."
        eri "Она всегда была печальна от того что у меня никогда не было друзей..."
        show erik 45
        show player 14
        player_name "Круто!"
        show player 33
        player_name "Хмм... Я уже начал думать кого же мы могли бы пригласить."
        show player 13
        show erik 47
        eri "Я никого не знаю, но я бы пошел неважно кого бы ты там не нашел!"
        show erik 45
        show player 14
        player_name "Хорошо!"
        show player 13
        show erik 46
        eri "Спасибо еще раз за Гарнитуру! Не терпится уже ее опробовать!"
        show erik 49
        if player.location == L_school_scienceclassroom:
            show erikl 48 at right
        with dissolve
        show player 14
        player_name "Всегда пожалуйста."
        eri "Круто..."
        show erik 49
        pause
        player_name "Увидимся позже, {b}Эрик{/b}."
        $ player.remove_item("game02")
        $ player.remove_item("virtualsaga")
        $ erik_vr.finish()
        $ M_mrsj.place(place = L_erikhouse_entrance)
        $ M_mrsj.force()
    else:

        show erik 1 at right
        show player 10 at left
        with dissolve
        player_name "Что бы ты хотел взамен за использование подвала?"
        show player 5
        show erik 5
        eri "Хмм... VR Гарнитуру {b}Virtual Saga X{/b}..."
        show erik 4
        eri "...И новую игру, называется {b}World of Orcette{/b}..."
        show erik 1
        show player 10
        player_name "Где ты говоришь его продают?"
        show player 5
        show erik 5
        eri "В {b}Cosmic Cumics{/b}."
        show erik 1
        show player 14
        player_name "Хорошо. Пойду посмотрю если смогу найти его там."
        show player 13
        show erik 4
        eri "Спасибо, {b}[firstname]{/b}!"
    hide player
    hide erik
    hide erikl
    with dissolve
    $ game.main()

label sock_pile_book_search:
    scene expression game.timer.image("eriks_room{}_c")
    show player 517 with dissolve
    player_name "Хмм, что с этими носками?"
    player_name "Они твердые как дерево."
    show player 516
    player_name "..."
    show player 517
    player_name "Грубое..."
    player_name "Я даже не буду беспокоится чтобы капаться здесь ради книги..."
    hide player with dissolve
    $ game.main()

label dresser_book_search:
    scene expression game.timer.image("backgrounds/location_erik_house_bedroom_dresser_day{}.jpg")
    player_name "!!!"
    player_name "Они испачканы?"
    pause
    player_name "В его комоде такой же беспорядок как и в его комнате!"
    $ game.main()

label under_bed_book_search:
    scene expression game.timer.image("under_eriks_bed{}")
    show book_03 at Position (xpos=431,ypos=425,xanchor=0,yanchor=0)
    player_name "Просто кучка пыли..."
    player_name "...Подождите минутку! Вот и книга под этим!"
    call screen under_eriks_bed

    player_name "Мило, вот она!"
    hide book_03
    show book_04_c with dissolve
    player_name "{b}Oedipuss{/b}?"
    player_name "Это очень древний метод..."
    player_name "С какой стати {b}Эрик{/b} хочет это?"
    hide book_04_c with dissolve

    scene expression game.timer.image("eriks_room{}_c")
    if M_bissette.get_state() == S_bissette_jane_return_books:
        show player 12 with dissolve
        player_name "Что ж, еще 2 книги остались."

    elif M_bissette.get_state() in [S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]:
        show player 14 with dissolve
        player_name "Осталась еще 1 книга."
    else:

        show player 14 with dissolve
        player_name "Отлично! Эта последняя книга!"
        player_name "Сейчас мне надо только вернуть их в библиотеку!"
    hide player with dissolve
    $ M_bissette.trigger(T_bissette_ask_erik)
    $ player.get_item("oedipuss")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
