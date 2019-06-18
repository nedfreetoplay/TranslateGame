label backroom_blocked_dialogue:
    scene library
    show player 35 with dissolve
    player_name "Хмм... Я не знаю где искать школьные {b}учебники{/b}..."
    player_name "Наверное надо спросить {b}библиотекаря{/b} за {b}стойкой{/b}."
    hide player 35 with dissolve
    $ game.main()

label backroom_dialogue_backroom_count:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707) with dissolve
    player_name "( ВОТ ДЕРЬМО!!! )"
    player_name "..."
    player_name "( Здесь люди занимаются сексом... )"
    pause 4
    player_name "..."
    player_name "( Это веб камера на полке? )"
    player_name "( По-моему она снимает... А они хоть знают что она там? )"
    player_name "( Должен ли я сказать {b}библиотекарше{/b}? )"
    return

label backroom_couple_finish:
    call expression game.dialog_select("backroom_couple_finish_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jane"]["unlocked"] = True
    $ persistent.cookie_jar["Jane"]["gallery"]["01_unlocked"] = True
    $ backroom_count = 2

    $ game.main()

label backroom_couple_finish_dialogue:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707)
    pause 4
    hide library 1_2
    pause .2
    show library 3 at Position(xpos = 486, ypos = 707) with dissolve
    window hide
    pause
    show library 4
    window hide
    pause
    player_name "( Вот блин! )"
    player_name "( Я слышу как кто-то идет!! )"
    show library 5 at Position(xpos = 512, ypos = 707) with hpunch
    window hide
    pause
    hide library with dissolve

    scene backroom01
    show jane f_mad_talk
    show player 23 at left
    with dissolve
    jan "Что тут за крики!"
    show player 11
    jan "ТОЛЬКО НЕ ОПЯТЬ!!!" with hpunch
    show jane f_eyeroll_talk a_dressed_up with dissolve
    jan "Эхх..."
    show jane f_mad with dissolve
    show player 10
    player_name "Это обычное дело?"
    show player 5
    show jane f_normal_down
    jan "..."
    show jane 4
    jan "Понимаешь..."
    jan "Людям нравится делать это здесь, и я не собираюсь их останавливать."
    jan "Просто держи это при себе, пожалуйста."
    show jane f_normal
    show player 12
    player_name "Да, я никому не расскажу..."
    show player 5
    show jane f_normal_talk
    jan "Спасибо."
    jan "Я возвращаюсь на своё рабочее место."
    jan "Если тебе нужна помощь в поиске чего-то или ты видишь, что кто-то ещё делает это здесь, дай мне знать!"
    hide jane with dissolve
    show player 17
    player_name "Мне надо почаще посещать библиотеку!"
    hide player with dissolve
    return

label poem_assignment_book:
    call expression game.dialog_select("poem_assignment_book_dialogue")
    $ M_bissette.trigger(T_bissette_reference_book_found)
    $ player.get_item("french_love")

    $ game.main()

label poem_assignment_book_dialogue:
    scene backroom01
    show book_01 at Position (xpos=376,ypos=426,xanchor=0,yanchor=0)
    player_name "Это должно быть та книга-"
    show book_07_c with dissolve
    player_name "!!!" with hpunch
    player_name "Воу!"
    player_name "{b}Мия{/b} была права. Эта штука реально очень наглядная!"
    player_name "Хмм, интересно что {b}Джудит{/b} делала с ней в той темной комнате?"
    player_name "..."
    player_name "Хорошо, надо идти домой к {b}компьютору{/b} и начать писать стихи для {b}Мисс Биссетт{/b}."
    pause
    hide book_01
    hide book_07_c with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
