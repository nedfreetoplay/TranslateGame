label pushups_minigame_win:
    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 13 at left
        show bridget a_dressed_crossed f_normal at flip
        show bridget at Position (xpos=150)
        show dexter 42 at right
        with dissolve
    else:

        show player 109f at left
        with dissolve

    $ renpy.pause(1, hard = True)

    if M_roxxy.is_state(S_roxxy_do_pushups):
        dex "{b}*Кхм*{/b} Ого..."
        show dexter 42b
        show bridget a_dressed_crossed f_normal_talk
        bri "Ты в порядке, {b}Декстер{/b}?"
        bri "Ты выглядишь не очень хорошо..."
        show bridget a_dressed_crossed f_normal
        hide dexter
        show player 106
        dex "{b}*Кхм*{/b}!!!" with hpunch
        show bridget b_bend a_empty f_bend_angry_talk_down with dissolve
        dex "..."
        bri "... Декстер?"
        dex "..."
        show bridget b_dressed a_dressed_crossed f_normal_talk with dissolve
        bri "Похоже {b}[firstname]{/b} Победил!"
        show bridget a_dressed_crossed f_normal
        show erik 4 at right with dissolve
        eri "Это было потрясающе, чувак!"
        eri "Ты уничтожил его!"
        show erik 1
        dex "..."
        show player 108f
        player_name "... С ним все хорошо?"
        show player 109f
        show erik 50
        eri "..."
        show bridget a_dressed_crossed f_normal_talk
        bri "Шшш, он будет в порядке."
        bri "Знаешь, {b}[firstname]{/b} тебе стоит попробовать себя в баскетбольной команде."
        show bridget a_dressed_crossed f_normal
        show erik 51
        show player 108f
        player_name "Правда?"
        show player 109f
        show bridget a_dressed_crossed f_normal_talk
        bri "Yeah! I could use a player with your... stamina."
        show bridget a_dressed_crossed f_normal
        show player 10
        player_name "Д-да, может быть."
        player_name "Я подумаю об этом, {b}тренер{/b}..."
        show player 5
        show bridget a_dressed_crossed f_normal_talk
        bri "Ну, ты знаешь, где меня найти."
        hide bridget with dissolve
        show erik 5
        eri "...Это было странно."
        show erik 1
        show player 14
        player_name "Хех, да. {b}Тренер Бриджит{/b} сказала мне что-то приятное..."
        show player 13
        show erik 4
        eri "Ну, ты только что убил людоеда..."
        show erik 1
        show player 17
        player_name "Ахахах!!"
        show player 14
        dex "{b}*Плачет*{/b}"
        show erik 50
        eri "..."
        show player 14
        player_name "Давай, давай снимем эту одежду."
        show player 13
        show erik 5
        eri "Прямо за тобой."
        hide player
        hide erik
        with dissolve
        dex "..."
        $ M_roxxy.trigger(T_roxxy_beaten_dexter_pushups)
    else:

        dex "..."
        show player 108f
        player_name "{b}Декстер{/b}?"
        show player 109f
        dex "..."
        show player 109f
        player_name "{b}*Эх*{/b} Не знаю, зачем ты так с собой поступаешь..."
        show player 108f
        dex "{b}*Плачет*{/b}"
        hide player with dissolve
        dex "..."
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label pushups_minigame_lose:
    scene gym with fade
    if M_roxxy.is_state(S_roxxy_do_pushups):
        show player 25 at left
        show bridget a_dressed_crossed f_normal at flip
        show bridget at Position (xpos=150)
        show dexter 11 at right
        with dissolve
    else:

        show player 24 at left
        show dexter 12 at right
        with dissolve

    $ renpy.pause(1, hard = True)

    if M_roxxy.is_state(S_roxxy_do_pushups):
        player_name "{b}*Хрр*{/b} Не могу... дышать..."
        show dexter 12
        dex "Хахаха!"
        show dexter 11
        show bridget a_dressed_crossed f_normal_talk at flip
        bri "Похоже {b}Декстер{/b} победил."
        show bridget a_dressed_crossed f_normal
        show dexter 12
        dex "У этого маленького ботаника никогда не было шанса..."
        show dexter 11
        show bridget a_dressed_crossed f_normal_talk
        bri "Держи себя в руках!"
        hide bridget with dissolve
        show dexter 12
        dex "Думаю, мне не нужно беспокоиться о тебе и о {b}Рокси{/b}..."
        dex "... Она не встречается с неудачниками."
        show dexter 11
        show player 24
        player_name "..."
        show dexter 12
        dex "Hahahaha!"
        show dexter 11
        show player 25
        player_name "Все, {b}Декстер{/b}. Тебе просто повезло, вот и все..."
        show dexter 12
        dex "Хахаха!"
        show dexter 11
        show player 15
        player_name "Грр... Я достану тебя в следующий раз."
        show player 16
        show dexter 28 with dissolve
        dex "Давай, лузер!"
        dex "Я буду бить тебя каждый раз."
        hide dexter with dissolve
        show player 5
        player_name "( Дерьмо! Теперь об этом будет знать вся школа. )"
        player_name "( Мне нужно показать всем, что я не боюсь встать против {b}Декстера{/b}! )"
        player_name "( ... Иначе {b}Рокси{/b} никогда не воспримет меня всерьёз. )"
        hide player with dissolve
    else:

        dex "Да!"
        dex "Я победил этого лузера!"
        show dexter 11
        show player 25
        player_name "Пфф, кого это волнует?"
        hide player with dissolve
        show dexter 12
        dex "Хахаха!"
        show dexter 15 with dissolve
        dex "... Ждать... Чего?!"
        dex "Куда это вы собрались?!"
        dex "... Вернись и дай мне посмеяться тебе в лицо!"
        show dexter 14
        dex "..."
        dex "Грр..."
        hide dexter with dissolve
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
