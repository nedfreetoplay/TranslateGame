label library_diane_breeding_intro:
    scene library
    show player 10 with dissolve
    player_name "( Возможно тут можно найти книгу, которая поможет {b}тёте Диане{/b} увеличить производство молока. )"
    show player 11
    pause
    show player 35
    player_name "( Где же искать? )"
    show player 10
    player_name "( Наверное надо поговорить с библиотекаршей, чтобы помогла. )"
    hide player with dissolve
    return

label library_jane_intro:
    call expression game.dialog_select("library_jane_intro_pre")
    menu:
        "Конечно." if player.has_money(20):
            call expression game.dialog_select("library_jane_intro_sure")
            $ player.spend_money(20)
            $ M_player.set("library subscription", True)
            $ M_jane.trigger(T_jane_library_pass)
        "Я откажусь.":

            call expression game.dialog_select("library_jane_intro_not_yet")
            $ player.go_to(L_map)

    hide player
    hide jane
    with dissolve
    return

label library_jane_intro_pre:
    scene library
    show player 1 at left
    show jane 2 at right
    with dissolve
    jan "Привет!"
    show player 14
    show jane 1
    player_name "Ох, привет!"
    player_name "Я ищу некоторые школьные {b}учебники{/b}."
    show player 1
    show jane 2
    jan "Подписка на клуб читателей есть?"
    show jane 1
    show player 10
    player_name "Эммм... Я не думаю что у меня есть."
    show player 13
    show jane 3
    jan "Ох. Ничего страшного!"
    show jane 2
    jan "Хочешь её получить?"
    show jane 3
    show player 11
    jan "Членский взнос всего {b}$20{/b}, и ты получишь доступ во все секции!"
    show jane 1
    show player 2
    player_name "Ухх... Я думаю у меня нет выбора. Хаха."
    show jane 3
    show player 13
    jan "Знания бесценны, не так ли?"
    show jane 2
    jan "Будете платить взнос?"
    show jane 1
    return

label library_jane_intro_sure:
    show player 4
    player_name "Хмм..."
    show player 174b at Position(xoffset=38) with fastdissolve
    player_name "Ладно. Вот {b}$20.{/b}"
    show player 1 with fastdissolve
    show jane 3
    jan "Спасибо!"
    show jane 2
    jan "Если ищете конкретную {b}книгу{/b}, подходите ко мне."
    jan "Я постораюсь найти их для тебя!"
    show jane 1
    show player 2
    player_name "Это приятно слышать! Спасибо!"
    return

label library_jane_intro_not_yet:
    show player 4
    player_name "Хмм..."
    show player 35
    player_name "Вообще-то, Я думаю что я откажусь..."
    show jane 2
    show player 1
    jan "Ох... ну хорошо тогда."
    show jane 1
    show player 2
    player_name "Я могу вернуться в другое время!"
    show jane 2
    show player 1
    jan "Окей, в любой день!"
    return

label library_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "Сейчас, надо найти что не будь во Французком романе."
    show player 12f
    player_name "Это будет не легко-"
    show player 32f at Position(xoffset=-69) with dissolve
    player_name "Это {b}Мия{/b}?"
    show player 14f with dissolve
    player_name "Интересно что она здесь делает?"
    player_name "Я должен пойти и сказать Привет!"
    hide player with dissolve
    return

label library_ross_find_magazines:
    scene library
    show player 2
    with dissolve
    player_name "Хмм, Мне нужно {b}найти библиотекаршу{/b}, где она хранит эти журналы."
    return

label check_out_lock:
    scene library
    show player 5 with dissolve
    player_name "( Сначала надо найти эту книгу. )"
    player_name "( Надо {b}снова поговорить с библиотекаршей{/b}. )"
    hide player with dissolve
    $ game.main()

label poem_assignment_lock:
    if M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("poem_assignment_lock_bissette_find_poem_reference_book")
    else:

        call expression game.dialog_select("poem_assignment_lock_bissette_reference_book_search")
    $ game.main()

label poem_assignment_lock_bissette_find_poem_reference_book:
    scene library
    show player 14f with dissolve
    player_name "Надо поздороваться с {b}Мией{/b}."
    hide player with dissolve
    return

label poem_assignment_lock_bissette_reference_book_search:
    scene library
    show player 14 with dissolve
    player_name "Надо посмотреть в {b}задней комнате{/b} книгу, о которой говорила {b}Мия{/b}."
    hide player with dissolve
    return

label kamasutra:
    $ player.get_item("kamasutra")
    call expression game.dialog_select("kamasutra_dialogue")
    $ player.location.call_screen(ui = False)

label kamasutra_dialogue:
    scene libraryshelf with None
    show book_02_c at truecenter with dissolve
    player_name "Вау..."
    player_name "В этой книге есть все сексуальные...позиции?"
    player_name "Это должно быть то что она просила..."
    hide book_02_c with dissolve
    return

label french_dictionary:
    $ player.get_item("french_dictionary")
    call expression game.dialog_select("french_dictionary_dialogue")

    $ player.location.call_screen(ui = False)

label french_dictionary_dialogue:
    scene libraryshelf with None
    player_name "Ага! Французко - Английский словарь!"
    player_name "Великолепно! Теперь я мо-"
    show book_03_c at truecenter with dissolve
    player_name "Минуточку..."
    player_name "Некоторых страниц не хватает!"
    player_name "Что мне теперь делать?"
    pause
    player_name "Надеюсь что важные страницы остались."
    hide book_03_c with dissolve
    return

label library_old_book:
    $ player.get_item("old_book")
    call expression game.dialog_select("library_old_book_dialogue")
    $ player.location.call_screen(ui = False)

label library_old_book_dialogue:
    scene libraryshelf with None
    show closeup_book_09 at truecenter with dissolve
    player_name "Эта книга будет полезна всем кто хочет расшифровать что-то."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Хех. Может быть некоторые {b}спрятаные пиратские сокровища{/b} были кем нибудь беспечно выбрашенны."
        player_name "Но это только мои {b}беспочвенные желания{/b}."
    else:

        player_name "Я думаю что {b}пиратская монета{/b} имела четырехзначное число."
        player_name "Мне нужно посмотреть на неё ешё раз."
    show popup_item_book6 at truecenter with dissolve
    pause
    hide popup_item_book6 with dissolve
    hide closeup_book_09 with dissolve
    return

label breeding_guide:
    $ player.get_item("breeding_guide")
    call expression game.dialog_select("breeding_guide_dialogue")
    $ player.location.call_screen(ui = False)

label breeding_guide_dialogue:
    scene libraryshelf with None
    player_name "( Книга должна быть где то здесь... )"
    show book_01_c at truecenter with dissolve
    player_name "( Похоже это она! )"
    player_name "Хмм..."
    player_name "( Выглядит довольно просто. )"
    player_name "( Это должно сработать с {b}тётей Дианой{/b} также. )"
    player_name "( Я просто не уверен, если она захочет {b}забеременеть{/b}, хотя... )"
    player_name "( Посмотрим что она скажет... )"
    hide book_01_c with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
