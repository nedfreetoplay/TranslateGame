init python:
    panty_lie_seen = False

label bag_minigame_attack:
    if cheat_pass:
        $ training_done = True
        $ cheat_pass = False
    if training_tier == 1:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a with hpunch
    elif training_tier == 2:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a2 with hpunch
    elif training_tier == 3:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a3 with hpunch
    elif training_tier == 4:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a4 with hpunch
    player_name "Huah!!"
    jump training01_done_dialogue

label training01_payment_dialogue:
    scene expression game.timer.image("training{}_b")
    pause 0.001
    show player 1 at left
    show master 2 at right
    with dissolve
    if (M_jenny.between_states(S_jenny_somrak_panty_trade, S_jenny_somrak_more_panty) and player.stats.dex() >= 2) or (M_jenny.between_states(S_jenny_somrak_panty_trade_tier_2, S_jenny_panty_deal_tier_3) and player.stats.dex() >= 5) or (M_jenny.between_states(S_jenny_somrak_panty_trade_tier_3, S_jenny_panty_deal_tier_4) and player.stats.dex() >= 7) or (M_jenny.finished_state(S_jenny_somrak_panty_trade_tier_4) and player.stats.dex() >= 10):
        mas "Пока я не могу научить тебя ничему большему."
        mas "Получи еще немного жизненного опыта! Может быть, провести еще немного времени с милой женщиной, которая дала тебе эти трусики!"
        show player 40 at left
        show master 6 at right
        player_name "Да, {b}Мастер Сомрак{/b}!!!"

    elif training_skip_payment:
        mas "Ахх!"
        mas "Вы вернулись!"
        mas "Вы готовы продолжить обучение, юный ученик?"
        show master 1
        menu:
            "Тренироваться.":
                show player 40 at left
                show master 6 at right
                player_name "Да, {b}Мастер Сомрак{/b}!!!"
                show master 2
                show player 1
                mas "Хорошо, хорошо! Тогда давайте начнем, наконец!"
                hide player
                hide master
                with dissolve
                jump training_during_dialogue

            "Пропустить мини-игру (Чит)." if game.cheat_mode:
                $ cheat_pass = True
                show player 40 at left
                show master 6 at right
                player_name "Да, {b}Мастер Сомрак{/b}!!!"
                show master 2
                show player 1
                mas "Хорошо, хорошо! Тогда давайте начнем, наконец!"
                hide player
                hide master
                with dissolve
                jump training_during_dialogue
            "Не сейчас.":

                show master 5 at right
                show player 10 at left
                player_name "Вообще-то, забудь..."
                show master 4
                show player 11
                mas "Тогда возвращайся, когда передумаешь, юный ученик!"
                show master 6
                show player 40
                player_name "Да, {b}Мастер Сомрак{/b}!!!"
                hide player
                hide master
                with dissolve
    else:

        mas "Ахх!"
        mas "Вы вернулись!"
        mas "Вы принесли то, что я ищу?"
        show master 1
        if player.has_item("panties"):
            menu:
                "У меня есть трусики." if training_tier == 1 and M_jenny.is_state(S_jenny_somrak_panty_trade):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Даа..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Нюхает*{/b}"
                    show master 3
                    mas "Очень хорошо!" with fastdissolve
                    show player 12
                    player_name "Они мне очень дорого обошлись... Надеюсь, обучение того стоит."
                    show player 1
                    show master 4
                    mas "Искусство муай тай бесценно, молодой ученик!"
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ player.remove_item("panties")
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "У меня есть трусики (Чит)." if training_tier == 1 and M_jenny.is_state(S_jenny_somrak_panty_trade) and game.cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Да..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Нюхает*{/b}"
                    show master 3
                    mas "Очень хорошо!" with fastdissolve
                    show player 12
                    player_name "Они мне очень дорого обошлись... Надеюсь, обучение того стоит."
                    show player 1
                    show master 4
                    mas "Искусство муай тай бесценно, молодой ученик!"
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ player.remove_item("panties")
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "У меня есть трусики." if training_tier == 2 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_2):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Даа..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Нюхает*{/b}"
                    show master 3
                    mas "Очень хорошо!" with fastdissolve
                    show player 12
                    player_name "Они мне очень дорого обошлись... Надеюсь, обучение того стоит."
                    show player 1
                    show master 4
                    mas "Искусство муай тай бесценно, молодой ученик!"
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_2)
                    jump training_during_dialogue

                "У меня есть трусики. (Чит)" if training_tier == 2 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_2) and game.cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Да, {b}Мастер Сомрак{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Даа..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Нюхает*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    mas "Ты хорошо поработал, молодой ученик!" with fastdissolve
                    show player 1
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 16
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_2)
                    jump training_during_dialogue

                "У меня есть трусики." if training_tier == 3 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_3):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Да, {b}Мастер Сомрак{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Даа..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Нюхает*{/b}"
                    pause
                    show player 11
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 14
                    pause
                    mas "Ты хорошо поработал, молодой ученик!" with fastdissolve
                    show player 1
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_3)
                    jump training_during_dialogue

                "У меня есть трусики. (Чит)" if training_tier == 3 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_3) and game.cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Да, {b}Мастер Сомрак{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Да..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Нюхает*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 3
                    mas "Очень хорошо!" with fastdissolve
                    show player 1
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_3)
                    jump training_during_dialogue

                "У меня есть трусики." if training_tier == 4 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_4):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Да, {b}Мастер Сомрак{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Даа..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Нюхает*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    show master 3
                    mas "Ты хорошо поработал, молодой ученик!" with fastdissolve
                    show player 40
                    show master 16
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 17
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_4)
                    jump training_during_dialogue

                "У меня есть трусики (Чит)." if training_tier == 4 and M_jenny.is_state(S_jenny_somrak_panty_trade_tier_4) and game.cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Даа..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Нюхает*{/b}"
                    show master 3
                    mas "Очень хорошо!" with fastdissolve
                    show player 12
                    player_name "Они мне очень дорого обошлись... Надеюсь, обучение того стоит."
                    show player 1
                    show master 4
                    mas "Искусство муай тай бесценно, молодой ученик!"
                    show master 2
                    mas "Готовы ли вы тренироваться?"
                    show player 40
                    show master 6
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ player.remove_item("panties")
                    $ M_jenny.trigger(T_jenny_somrak_panty_traded_tier_4)
                    jump training_during_dialogue
                "Не сейчас.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Вообще-то, забудь..."
                    show master 4
                    show player 11
                    mas "Тогда возвращайся, когда передумаешь, юный ученик!"
                    show master 6
                    show player 40
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
        else:


            menu:
                "У меня есть трусики." if not panty_lie_seen:
                    show master 2 at right
                    show player 11 at left
                    mas "Я не вижу никаких трусиков, ученик!"
                    show master 5
                    show player 10
                    player_name "Ах, да, об этом..."
                    player_name "Я их ещё не нашел..."
                    show master 4
                    show player 11
                    mas "Продолжай искать, мой молодой ученик!"
                    show player 1
                    mas "Возвращайся ко мне, когда найдешь их!"
                    show master 6
                    show player 40
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master with dissolve
                    $ panty_lie_seen = True

                "<>У меня есть трусики." if panty_lie_seen:
                    $ pass
                "Не сейчас.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Вообще-то, забудь..."
                    show master 4
                    show player 11
                    mas "Тогда возвращайся, когда передумаешь, молодой ученик!"
                    show master 6
                    show player 40
                    player_name "Да, {b}Мастер Сомрак{/b}!!!"
                    hide player
                    hide master
                    with dissolve
    $ game.main()

label training_during_dialogue:
    scene minigame02b
    if training_skip_payment:
        scene minigame02b
        show master 3f at left
        with dissolve
        mas "Ты знаешь, что делать, юный ученик!"
        show master 2f
        mas "Как мы практиковались в прошлый раз."
        show master 4f
        mas "А теперь покажи мне!!"
    else:

        if training_tier == 1:
            show master 3f at left
            with dissolve
            mas "Во-первых, вы научитесь использовать удары!"
            show master 2f
            mas "Вы должны владеть бедерами! Начать оттуда..."
            show master 4f
            mas "...затем поверните плечо, вытяните руку прямо..."
            show master 10f
            mas "...и {b}УДАР{/b}!" with hpunch
            show master 4f
            mas "Теперь покажи мне!!"

        elif training_tier == 2:
            show master 3f at left
            with dissolve
            mas "Теперь вы научитесь приёмам с руками!"
            show master 2f
            mas "Это самый полезный метод на коротком расстоянии; он может вырезать кожу вокруг глаз..."
            show master 4f
            mas "...под любым углом, прямо от плеча..."
            show master 10f
            mas "...и {b}УДАР{/b}!" with hpunch
            show master 4f
            mas "А теперь покажи мне!!"

        elif training_tier == 3:
            show master 3f at left
            with dissolve
            mas "Теперь вы научитесь использовать удары ногами!"
            show master 2f
            mas "Ноги на коврик, ваш удар начинается оттуда!"
            show master 4f
            mas "Повернись бедрами, повернись..."
            show master 10f
            mas "...и {b}УДАР{/b}!" with hpunch
            show master 4f
            mas "А теперь покажи мне!!"

        elif training_tier == 4:
            show master 3f at left
            with dissolve
            mas "Наконец, Вы научитесь пользоваться коленями!"
            show master 2f
            mas "Вы должны целиться в солнышко или в голову, тогда с огромной силой..."
            show master 4f
            mas "...поверните бедра, приготовьтесь к прыжку..."
            show master 10f
            mas "...и {b}УДАР{/b}!" with hpunch
            show master 4f
            mas "А теперь покажи мне!!"
    $ training_skip_payment = True
    hide master
    with dissolve
    hide minigame02b
    if cheat_pass:
        jump bag_minigame_attack
    call screen muay_thai(training_tier)

label training01_done_dialogue:
    $ game.timer.tick()
    if training_tier == 1:
        if player.stats.dex() < 2:
            $ player.stats.increase("dex")
        if player.stats.dex() > 1:
            $ training_skip_payment = False

    elif training_tier == 2:
        if player.stats.dex() < 5:
            $ player.stats.increase("dex")
        if player.stats.dex() > 4:
            $ training_skip_payment = False

    elif training_tier == 3:
        if player.stats.dex() < 7:
            $ player.stats.increase("dex")
        if player.stats.dex() > 6:
            $ training_skip_payment = False

    elif training_tier == 4:
        $ player.stats.increase("dex")
    scene expression game.timer.image("training{}_b")
    if training_skip_payment:
        show masterplayer 28 at left
        show master 3 at right
        with dissolve
        mas "Ты хорошо поработал, юный ученик!"
        show master 6
        show unlock9 at truecenter
        pause
        hide unlock9 with dissolve
        show master 2
        show masterplayer 27
        mas "Тем не менее, я все ещё вижу возможности для улучшения!"
        show master 3
        mas "Иди отдыхай!"
        mas "Мы продолжим ваше обучение, когда вы вернетесь."
        show masterplayer 40
        show master 6
        player_name "Да, спасибо, {b}Мастер Сомрак{/b}!!!"
        hide masterplayer
        hide master
        with dissolve
    else:

        if training_tier == 1:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Молодец, молодой ученик!"
            show master 2
            mas "Вы улучшились, я чувствую это!"
            show masterplayer 28
            mas "Подойдите! Вы заработали себе новый пояс!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            show masterplayer 27
            mas "Теперь... продолжи свое обучение, все что вам нужно сделать..."
            show master 2
            show masterplayer 21
            mas "...принесите мне больше {b}трусикив{/b}!"
            show masterplayer 40
            show master 6
            player_name "Да! Спасибо вам, {b}Мастер Сомрак{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "У меня хорошее предчувствие насчет этого..."
            $ training_tier = 2

        elif training_tier == 2:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Молодец, молодой ученик!"
            show master 2
            show masterplayer 28
            mas "Вы улучшились, я чувствую это!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Теперь отдыхай!"
            mas "Мы обсудим следующую часть вашего обучения, когда вы вернетесь."
            show masterplayer 40
            show master 6
            player_name "Да, спасибо вам, {b}Мастер Сомрак{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Он быстро учится..."
            $ training_tier = 3

        elif training_tier == 3:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Молодец, молодой ученик!"
            show master 2
            show masterplayer 28
            mas "Вы улучшились, я чувствую это!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Теперь отдыхай!"
            mas "Мы обсудим следующую часть вашего обучения, когда вы вернетесь."
            show masterplayer 40
            show master 6
            player_name "Да! Спасибо вам, {b}Мастер Сомрак{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Он быстро учится..."
            $ training_tier = 4

        elif training_tier == 4:
            show masterplayer 28 at left
            show master 3 at right
            with dissolve
            mas "Молодец, молодой ученик!"
            show master 2
            show masterplayer 28
            mas "Или я должен сказать, {b}Мастер{/b}?"
            mas "Вы преуспели в каждом задании, которое я вам дал."
            mas "Вы значительно улучшились с момента нашей первой встречи!"
            mas "А теперь..."
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Нет ничего, чему я могу тебя научить."
            show master 2
            mas "...но я не буду говорить \"нет\" больше {b}трусикам{/b}!"
            show master 6
            pause
            show master 4
            mas "А теперь иди и используй свои новые навыки!" with hpunch
            show masterplayer 40
            show master 6
            player_name "Да, {b}Мастер Сомрак{/b}!!!"
            player_name "Спасибо вам!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Он напоминает мне меня, когда я был маленьким..."
    hide master
    with dissolve
    $ game.main()

label training_failed_dialogue:
    scene expression game.timer.image("training{}_b")
    show masterplayer 27 at left
    show master 7 at right
    mas "{b}НЕПРАВИЛЬНО!!{/b}" with vpunch


    mas "Ты меня не слушаешь! Ты дерешься как глупая собака!"
    mas "Используй мозг, а не силу!"
    show master 4
    mas "Тренируйся больше, потом возвращайся..."
    hide masterplayer
    hide master
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
