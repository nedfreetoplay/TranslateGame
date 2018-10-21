label jenny_dialogue_panties_trade_pre:
    scene jennybedroom with None
    show jenny 9 at right
    show jenny 9 at Position(xpos=937)
    show player 11 at left
    with dissolve
    jen "Если ты здесь за {b}трусишками{/b}, Я тебе говорила, или {b}$100{/b} или ничего."
    show jenny 6
    return

label jenny_dialogue_panties_trade_buy:
    show player 12 at left
    show jenny 18 at right
    player_name "Хорошо."
    play audio coins2
    show player 41 at Position (xpos=38) with fastdissolve
    pause
    show jenny 80 at Position(xpos=945)
    show player 1 at left
    jen "Ладно, можешь оставить себе..." with fastdissolve
    show jenny 81
    show player 11
    jen "А теперь убирайся из моей комнаты, извращенец!"
    show jenny 14
    show unlock17 at truecenter
    pause
    hide unlock17 with dissolve
    hide player
    hide jenny
    return

label jenny_dialogue_panties_trade_do_not_buy:
    show jenny 10 at Position(xpos=937)
    show player 35 at left
    player_name "Вообще-то, мне сейчас ничего не нужно..."
    show jenny 9
    show player 39 at Position (xpos=38)
    jen "Тогда верни их и убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    return

label jenny_dialogue_panties_trade_cant_buy:
    show player 24 at left
    show jenny 10 at Position(xpos=937)
    player_name "У меня с собой не так много денег..."
    show jenny 9
    show player 5
    jen "Очень жаль! Убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    return

label jenny_dialogue_pre:
    scene jennybedroom with None
    show player 11 at left
    show jenny 19 at right
    with dissolve




    jen "Так, так..."
    jen "Что захотел маленький извращенец на этот раз?"
    if not sister.over(sis_panty02):
        jen "Еще {b}трусишек{/b}, возможно?"

    elif not sister.over(sis_panty03):
        jen "Дай угодаю, еще {b}труселей{/b}?"

    elif not sister.over(sis_panty04):
        show player 1
        jen "Не говори: еще {b}труселей{/b}."
    show jenny 18
    return

label jenny_dialogue_talk_before_cuddle:
    show player 14
    player_name "Я хотела сказать, что мне нравится обниматься с тобой по ночам..."
    show player 18
    player_name "...Я просто рад, что начинаю нравиться тебе больше."
    show player 13
    show jenny 10 at Position(xpos = 937)
    jen "..."
    show player 11
    show jenny 9
    jen "Правда?"
    show jenny 7 at right
    jen "Ты думаешь, я делаю это, потому что ты мне нравишься?!"
    show jenny 9 at Position(xpos = 937)
    jen "Чувак, ты такой жалкий."
    show player 5
    show jenny 6
    player_name "..."
    show jenny 12
    jen "Только не жадничай слишком сильно. Тебе повезло, что я впустила тебя в свою комнату."
    show jenny 9
    jen "Есть еще что-нибудь, о чем ты хотела бы поговорить, или я могу просто вышвырнуть тебя из своей комнаты?"
    return

label jenny_dialogue_confess_first:
    show player 2 at left
    player_name "Привет, {b}[jen_name]{/b}..."
    show player 29
    player_name "Я... Я хотел сказать кое-что..."
    show player 1
    show jenny 10 at Position(xpos = 937)
    jen "Эээ... хорошо?"
    show player 2
    player_name "Ну..."
    show player 3
    show jenny 9
    jen "Короче! У меня нет на это времени!"
    show player 21
    show jenny 9b
    player_name "Я думаю что люблю тебя."
    show jenny 10
    jen "?!?" with hpunch
    show player 5
    show jenny 7 at right
    jen "Эээ! Что за хрень!?"
    jen "Что с тобой не так??"
    show player 22
    show jenny 8
    player_name "!!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Почему ты так разговариваешь?"
    show player 25
    show jenny 6
    player_name "Я не знаю... Это просто чувство, у меня!!"
    show player 22
    show jenny 7 at right
    jen "Я не твоя подружка, ты ИДИОТ!!"
    show player 6
    show jenny 8
    player_name "Прости!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Если я позволяю тебе трахать меня на моих шоу, это не значит, что у меня есть чувства к тебе! Понял?!"
    show player 25
    show jenny 6
    player_name "Да... Я понял..."
    show player 5
    show jenny 7 at right
    jen "Хорошо! Теперь, {b}ВАЛИ ИЗ МОЕЙ КОМНАТЫ{/b}!!" with hpunch
    show player 22
    show jenny 8
    player_name "!!!"
    hide player
    show jenny 9 at Position(xpos = 937)
    with fade
    jen "Ух... Неужели я зашла слишком далеко?"
    jen "Я знала, что нравлюсь ему, но..... Не могу поверить, что этот маленький извращенец начинает испытывать ко мне чувства."
    jen "Он был очень полезен... Я зарабатываю кучу денег на своем шоу из-за него..."
    jen "Ух!! Он, наверное, просто возбужден."
    hide jenny
    hide jennybedroom
    return

label jenny_dialogue_confess_repeat:
    show player 14 at left
    player_name "Привет {b}[jen_name]{/b}..."
    player_name "Просто знай что ты мне очень нравишься."
    show player 1
    show jenny 9 at Position(xpos = 937)
    jen "Опять??"
    show player 17
    show jenny 9b
    player_name "Я думаю, что, я люблю тебя."
    show jenny 10
    jen "?!?" with hpunch
    show player 25
    show jenny 9
    jen "Ты должен прекратить это!!"
    jen "Что с тобой не так??"
    show player 22
    show jenny 6
    player_name "!!!"
    show jenny 7 at right
    jen "Я не твоя подружка, ты ИДИОТ!!"
    show player 6
    show jenny 8
    player_name "Прости!!"
    show player 5
    show jenny 9 at Position(xpos = 937)
    jen "Только потому, что я позволяю тебе трахать меня на моих шоу, не значит, что у меня есть чувства к тебе! Понял?!"
    show jenny 6
    show player 24
    player_name "Да... Я понял..."
    show jenny 7 at right
    jen "Хорошо! Сейчас, {b}УБИРАЙСЯ ИЗ МОЕЙ КОМНАТЫ{/b}!!"
    show player 22
    show jenny 8
    player_name "!!!"
    hide player
    show jenny 9 at Position(xpos = 937)
    with fade
    jen "Ух!! Он, наверное, просто возбужден."
    hide jenny
    hide jennybedroom
    return

label jenny_dialogue_roxxy_pre:
    show jenny 11
    show player 10
    player_name "Итак, о занятии с {b}Рокси{/b}..."
    show player 5
    show jenny 12
    jen "Ты принес деньги?"
    show jenny 11
    return

label jenny_dialogue_roxxy_pay:
    show player 12
    player_name "Вот."
    show player 41 at Position (xoffset=38) with dissolve
    pause
    show jenny 80 at right
    show player 5
    with dissolve
    jen "Прекрасно."
    jen "Скажи как ее там зовут, она может прийти ко мне завтра после школы."
    show jenny 14
    show player 12
    player_name "Ее зовут {b}Рокси{/b}."
    show player 5
    show jenny 81
    jen "Не важно."
    return

label jenny_dialogue_roxxy_do_not_pay:
    show player 10
    player_name "У меня пока еще нет."
    show player 5
    show jenny 9
    jen "Тогда проваливай, я занята."
    return

label jenny_dialogue_trade_panties:
    menu:
        "Еще нет." if (not sister.known(sis_panty02) or not sister.known(sis_panty03) or not sister.known(sis_panty04)) or (sister.completed(sis_panty02) or sister.completed(sis_panty03) or sister.completed(sis_panty04)):
            call expression game.dialog_select("jenny_dialogue_trade_panties_not_yet")
            jump expression game.dialog_select("hallway_dialogue")

        "Да, больше трусиков." if sister.started(sis_panty02) or sister.started(sis_panty03) or sister.started(sis_panty04):
            if sis_quest_first:
                if sister.started(sis_panty04):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty04")

                elif sister.started(sis_panty03):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty03")

                elif sister.started(sis_panty02):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_first_panty02")

                $ sis_quest_first = False
                jump expression game.dialog_select("hallway_dialogue")
            else:

                label sybian_replay:
                    call expression game.dialog_select("jenny_dialogue_trade_panties_more_panties_repeat")
                    if not store._in_replay == None:
                        call expression game.dialog_select("sybian_replay_continue")
            menu:
                "Вот игрушка." if player.has_item("sybian") and sister.started(sis_panty04):
                    label sybian_replay_continue:
                        call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_sybian")
                    $ sybian_stage = 0
                    $ sis_sybian_speed = 0.8
                    $ player.remove_item("sybian")
                    show screen sybianscr
                    with fastdissolve
                    pause
                    jump expression game.dialog_select("sybian_stage1")

                "Вот игрушка." if player.has_item("ultravibrato") and sister.started(sis_panty03):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_ultravibrato")
                    $ player.get_item("panties")
                    $ player.remove_item("ultravibrato")
                    $ sis_panty03.finish()
                    $ sis_quest_first = True

                "Вот игрушка." if player.has_item("electroclit") and sister.started(sis_panty02):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_have_toy_electroclit")
                    $ player.get_item("panties")
                    $ player.remove_item("electroclit")
                    $ sis_panty02.finish()
                    $ sis_quest_first = True

                "У меня ее нет." if sister.started(sis_panty02) and not player.has_item("electroclit") or sister.started(sis_panty03) and not player.has_item("ultravibrato") or sister.started(sis_panty04) and not player.has_item("sybian"):
                    call expression game.dialog_select("jenny_dialogue_trade_panties_do_not_have_toy")
                "У меня ее нет.":

                    call expression game.dialog_select("jenny_dialogue_trade_panties_do_not_need_panties")
    return

label jenny_dialogue_trade_panties_not_yet:
    show player 12 at left
    show jenny 10 at Position(xpos=937)
    player_name "На данный момент я в порядке."
    show jenny 9
    show player 11
    jen "Так... Тогда что ты здесь делаешь?"
    show jenny 10
    show player 10
    player_name "Я эээ... Я только-"
    show jenny 7 at right
    show player 11
    jen "Я сейчас занята, разве ты не видишь!?"
    show jenny 8
    show player 12
    player_name "Хорошо..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "И закрой дверь, когда будешь уходить!"
    jen "Я бы не хотела, чтобы извращенец шпионил за мной."
    show jenny 6
    player_name "..."
    show player 10
    player_name "Хорошо..."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty02:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Да, еще трусиков, вообще-то."
    show jenny 10
    player_name "В этот раз... Мне нужны {b}использованные трусики{/b}..."
    show player 11
    show jenny 7 at right
    jen "ИСПОЛЬЗОВАННЫЕ?!" with hpunch
    show jenny 8
    show player 10
    player_name "Я знаю... Хотя, это то, что он сказал..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Просто дай ему пару из моего ящика!"
    show jenny 10
    show player 10
    player_name "Я не могу! Он сказал, что мне нужно {b}убедиться{/b}, что они были {b}поношены{/b}..."
    show jenny 55 at right
    show player 11
    jen "Ты имеешь в виду, что я должна дать тебе {b}ЭТИ{/b}??"
    show jenny 6 at Position(xpos=937)
    show player 21
    player_name "Да... Наверно..."
    show jenny 11
    show player 11
    jen "Хммм..."
    show jenny 9
    show player 13
    jen "Хорошо! Я дам эти!"
    show jenny 12
    show player 11
    jen "Но тебе придется {b}купить{/b} мне кое-что."
    show jenny 18 at right
    player_name "..."
    show jenny 19
    jen "Ты слышал меня."
    jen "Ты должен купить мне {b}игрушки для девочек{/b}."
    show jenny 10 at Position(xpos=937)
    show player 12
    player_name "Что?"
    show jenny 9
    show player 11
    jen "Прекрати вести себя так невинно! Ты знаешь, о чем я говорю!"
    jen "{b}Секс{/b} игрушки!!"
    show jenny 61 at right with fastdissolve
    jen "Как одна из этих!"
    show jenny 18 with fastdissolve
    player_name "!!!"
    show player 14
    player_name "Думаю, что смогу..."
    show player 10
    player_name "Но... разве они не дорогие? И где же я возьму их?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Я знаю, что у тебя есть на это деньги..."
    show jenny 12
    jen "И ты можешь купить их в магазине {b}Pink{/b}, в {b}торговом центре{/b}."
    show jenny 82
    show player 12
    player_name "Какую ты хочешь?"
    show jenny 12
    show player 11
    jen "Я хочу {b}Электро Клитор{/b}. Он такой фиолетовый."
    show jenny 10
    show player 10
    player_name "Я не знаю, смогу ли я это сделать... люди могут увидеть меня в этом магазине..."
    show jenny 7 at right
    show player 11
    jen "{b}СЛУШАЙ{/b}! Я делаю тебе одолжение, хорошо?!"
    show jenny 9 at Position(xpos=937)
    jen "Если ты не собираешься торговаться за них, то уходи!!"
    show player 21
    show jenny 82
    player_name "Ну... Наверное, мне придется это сделать..."
    show jenny 19 at right
    show player 11
    jen "Возвращайся ко мне, когда у тебя будет эта {b}игрушка{/b}."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty03:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Да, еще трусиков, вообще-то."
    show jenny 10
    player_name "Но на этот раз... нужны... {b}мокрые трусики{/b}..."
    show jenny 7 at right
    show player 11
    jen "Сначала ношеные, теперь {b}мокренькие{/b} подавай?!"
    show jenny 9 at Position(xpos=937)
    jen "Кто, черт возьми, этот урод?"
    show jenny 6
    show player 10
    player_name "Слушай, это неважно, он сказал, что мне нужно убедиться, что они мокрые..."
    show jenny 9
    show player 11
    jen "Ты должно быть шутишь надо мной!!"
    jen "Ты имеешь в виду, что я должна сделать их {b}мокрыми{/b}??"
    show jenny 6
    show player 21
    player_name "Да... наверно..."
    show jenny 9
    show player 11
    jen "Ты начинаешь настаивать на этих требованиях..."
    jen "...но я сделаю это."
    jen "Тебе придется купить мне еще {b}игрушек для девочек{/b}."
    show jenny 82
    show player 14
    player_name "Конечно..."
    player_name "Думаю, что смогу..."
    player_name "Что ты хочешь на этот раз?"
    show player 11
    show jenny 12
    jen "Я хочу {b}Ультравибратор 2000{/b}."
    show jenny 10
    show player 12
    player_name "Черт... Мне правда не нравится ходить в этот магазин..."
    show jenny 7 at right
    show player 11
    jen "{b}СЛУШАЙ{/b}!Ты просишь у меня {b}мокрые{/b} трусики, хорошо?!" with hpunch
    jen "Если ты не собираешься торговаться за них, то уходи!!"
    show jenny 18 at right
    show player 21
    player_name "Ну... Наверное, мне придется это сделать..."
    show jenny 19
    show player 11
    jen "Возвращайся ко мне, когда у тебя будет эта {b}игрушка{/b}."
    hide player
    hide jenny
    return

label jenny_dialogue_trade_panties_more_panties_first_panty04:
    show player 21 at left
    show jenny 11 at Position(xpos=937)
    player_name "Да, в последний раз, вообще-то."
    show jenny 10
    player_name "Но на этот раз... Мне нужно, чтобы ты {b}брызнула на них{/b}..."
    show player 11
    jen "?!"
    show player 10
    player_name "Я знаю!!... Хотя, это то, что он сказал..."
    show jenny 9
    show player 1
    jen "Брызнуть?"
    show jenny 6
    show player 10
    player_name "Я знаю! Он сказал, что я должен быть {b}УВЕРЕН{/b} что они {b}смочены брызгами{/b}..."
    show jenny 7 at right
    show player 11
    jen "Ты имеешь в виду, что я должна {b}БРЫЗНУТЬ{/b} на них??" with hpunch
    show jenny 8
    show player 21
    player_name "Да, наверное, именно так... они должны быть очень мокрые от этой штуки!"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Ты начинаешь все усложнять..."
    show jenny 12
    show player 13
    jen "...Но мне кажется, у меня есть идея..."
    show player 11
    jen "Но тебе придется купить мне специфическую {b}игрушку{/b}."
    show jenny 82
    show player 21
    player_name "Да, без проблем..."
    player_name "Какую?"
    show player 11
    show jenny 19 at right
    jen "Мне нужен {b}Двойной Вибратор{/b}."
    show jenny 18
    player_name "..."
    show player 10
    show jenny 10 at Position(xpos=937)
    player_name "Чего?"
    show player 11
    show jenny 9
    jen "Он похож на седло, его нельзя пропустить."
    show player 12
    show jenny 10
    player_name "Ухх, сколько он может стоить?"
    show player 11
    show jenny 7 at right
    jen "{b}СЛУШАЙ{/b}, ты просишь меня устроить сквиртинг, хорошо?!" with hpunch
    jen "Если ты не достанешь эту {b}игрушку{/b}, можешь забыть об этом!!"
    show jenny 8
    show player 10
    show jenny 18
    player_name "Ладно, ладно!!"
    show player 11
    show jenny 19
    jen "Возвращайся ко мне, когда получишь его."
    hide player
    hide jenny
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
