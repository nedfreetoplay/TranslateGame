label erik_basement:
    $ player.go_to(L_erikhouse_basement)
    if M_dewitt.get_state() == S_dewitt_eve_karaoke and game.timer.is_dark():
        call expression game.dialog_select("eriks_basement_dewitt_eve_karaoke")
        if game.cheat_mode:
            menu:
                "Play Minigame":
                    call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
                "Skip Minigame (Cheat)":
                    jump guitar_hero_minigame_karaoke_pass
        else:
            call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        jump erik_vr

    elif not M_erik.get('seen basement'):
        $ poker_table_seen = False
        call expression game.dialog_select("eriks_basement_first_time")
        $ M_erik.set('seen basement', True)
    $ game.main()

label eriks_basement_dewitt_eve_karaoke:
    scene erik_basement
    show player 13 at left
    show eve 2 at Position (xpos=600)
    show erik 1 at right
    with dissolve
    eve "Хэй, Самое время! Я начала думать что ты кинул меня!"
    show eve 5
    show player 29 with dissolve
    player_name "Извини, Меня задержали! Хэй {b}Эрик{/b}!"
    show player 13 with dissolve
    show erik 4
    eri "Хэй, {b}[firstname]{/b}! Я только что говорил {b}Еве{/b} о моей гильдии в World of Orcette."
    show erik 1
    show eve 6b
    eve "Да, это было захватывающе."
    show eve 5
    show player 14
    player_name "Хех, Я вижу."
    player_name "Спасибо что позволил нам прийти сегодня вечером, {b}Эрик{/b}."
    show player 13
    show erik 4
    eri "Да, без проблем, дружище! Тебе повезло моя что гильдия отменила рейд сегодня вечером."
    show erik 1
    show player 10
    player_name "Рейд?"
    show player 13
    show eve 2b
    eve "Нет, не спрашивай!"
    show eve 1
    show player 11
    show erik 51
    eri "..."
    show eve 2
    eve "Это там выпивка?"
    show eve 5
    show player 13
    show erik 53
    eri "Д-дааа, почему?"
    show erik 52
    show eve 6
    eve "Потому что мне кажется мне нужно немного сегодня вечером!"
    show eve 5
    show player 14
    player_name "Это не плохая идея. Это расслабит нас для караоке."
    show player 13
    show erik 54
    eri "Ох да,думаю что это имеет смысл."
    show erik 52 with dissolve
    show eve 6
    eve "Хэй, у тебя есть виски, шикарно!"
    eve "Почему бы тебе не пойти и не принести несколько бокалов {b}[firstname]{/b} пока я удобно устроюсь на диване."
    show eve 5
    show erik 54
    eri "... Ладно хорошо!"
    hide erik with dissolve
    pause
    show eve 24 with dissolve
    eve "Ты можешь поверить что подвал {b}Эрика{/b} такой крутой?"
    eve "Давай {b}[firstname]{/b}, заглянем в другую комнату!"
    hide player
    show eve 25f
    with dissolve

    pause

    scene erik_basement_back_b_01
    show player 13 at left
    show eve 2b at Position (xpos=500)
    eve "Вау... Как это все офигенно..."
    show eve 5
    show player 14
    player_name "Я знаю правда? Это идеальный дом для вечеринок."
    show player 13
    show eve 2b
    eve "Ты когда-нибудь пил виски раньше?"
    show eve 5
    show player 10
    player_name "Думаю,что нет..."
    show player 5
    show eve 6
    eve "Будь готов к взрыву мозга!"
    show eve 5
    show player 13

    show erik 15f at right with dissolve
    eri "Мне интересно куда вы ребята пошли."
    eri "Это сработает?"
    show erik 15bf

    show eve 9 with dissolve
    pause
    show eve 10
    eve "Конечно."
    show erik 16f with dissolve
    pause
    show erik 17f with dissolve
    show player 185
    show eve 19
    with dissolve
    eve "Пьем до дна!"
    show player 189
    show erik 19f
    show eve 18
    with dissolve
    pause
    show player 190
    show eve 21
    show erik 18f
    with dissolve
    eri "*Кашель* *Кашель* Пошло не в то горло! *Кашель*"
    show erik 17f
    show eve 19
    eve "Ммммхмммм, вкусное дерьмо!"
    show eve 20
    show player 191
    player_name "Вау!!!Оно действительно крепкое!"
    show player 190
    show eve 19
    eve "Не тушуйтесь, парни!"
    show eve 20
    show erik 18f
    eri "конечно..."
    show eve 9
    show player 13
    with dissolve
    show erik 16f with dissolve
    pause
    show erik 17f with dissolve
    show player 188
    show eve 19
    with dissolve
    eve "Пей!"
    show player 189
    show eve 18
    show erik 19f
    with dissolve
    pause
    show erik 17f with dissolve
    show eve 21 with dissolve
    eve "Whooooo!"
    show eve 20
    show player 191 with dissolve
    player_name "Черт!"
    show player 190
    player_name "..."
    show player 187
    player_name "Хорошо, наверное нам уже нужно включить караоке."

    scene erik_basement_back_b_03
    show eve 20 at Position (xpos=500)
    show erik 18f at right
    with dissolve
    eri "Как здесь жарко, кому-небудь еще жарко?"
    show erik 17f
    show eve 19f with dissolve
    eve "Хех,это все спиртное, оно согревает тебя изнутри..."
    show eve 20f
    player_name "{b}Эрик{/b}, как черт возьми эта штука работает?"
    show eve 18f with dissolve
    show erik 18f
    eri "Я сделаю, отойди."

    scene erik_basement_back_b_02
    show eve 18f at Position (xpos=500)
    show player 14 at left
    with dissolve
    player_name "Ты готова растянуть свои трубы?"
    show player 13
    show eve 19 with dissolve
    eve "Да, мне нужно немного больше выпить что бы я была готова петь."
    eve "Почему вы ребята начали без меня?"
    show eve 20
    show player 14
    player_name "... Ох, эээ. Ладно."
    show player 13
    eri "Все готово!"
    show player 14
    player_name "Давайте начнем эту вечернинку!"
    hide player
    hide eve
    with dissolve
    return

label eriks_basement_dewitt_get_beer:
    scene erik_basement
    show player 571 with dissolve
    player_name "Да, этого будет много."
    hide player with dissolve
    show popup_item_beer1 at truecenter with dissolve
    pause
    $ player.get_item("beer")
    hide popup_item_beer1 with dissolve
    $ game.main()

label eriks_basement_dewitt_replace_guitar:
    scene erik_basement
    show player 575 at right with dissolve
    player_name "( Хммм. )"
    show player 574
    player_name "( Это не так уж и заметно. )"
    show player 575
    player_name "( ... Да, Я думаю это может действительно сработать! )"
    show player 577 with dissolve
    pause
    show mrsj 50f at left with dissolve
    player_name "( Сейчас мне просто нужно вытащить реальную гитару от сюда так чтобы {b}Mrs. Johnson{/b} не увидела меня. )"
    show player 576
    show mrsj 52f
    mrsjo "Что это черт подери?"
    show mrsj 38f
    show player 577df with hpunch
    player_name "!!!"
    show player 577cf
    player_name "Х-хэй, {b}Mrs. Johnson{/b}..."
    player_name "Я не слышал как вы спустились."
    show player 577bf
    show mrsj 52f
    mrsjo "Это ты сделал эту штуку, {b}[firstname]{/b}?"
    show mrsj 38f
    show player 577cf
    player_name "Д-даа. Вам нравится?"
    show player 577bf
    show mrsj 49f
    mrsjo "Хехехе, это думал что  Я не замечу что ты уходишь с гитарой моего бывшего мужа?"
    show mrsj 50f
    show player 577cf
    player_name "... Мне просто нужно одолжить её для школьного шоу талантов и {b}Эрик{/b} подумал что вы можете расстроится."
    show player 577bf
    show mrsj 18f
    mrsjo "Он?"
    show mrsj 49f
    mrsjo "Aww, он такой милый молодой парень что бы так сильно заботиться о моих чувствах."
    show mrsj 50f
    show player 577cf
    player_name "Вы не против если я одолжу эту гитару хоть ненадолго?"
    show player 577bf
    show mrsj 18f
    mrsjo "Пффф, не совсем, дорогой."
    show mrsj 49f
    mrsjo "Я никогда не понимала причину за что я так любила ни на что не годного бывшего. Он даже не умел хорошо играть на ней."
    mrsjo "Ты можешь оставить ей себе навсегда Мне все равно"
    mrsjo "Она просто так там лежала и собирала пыль."
    show mrsj 50f
    show player 577f
    player_name "Реально?"
    show player 576f
    show mrsj 49f
    mrsjo "Ну конечно!Ты стал хорошим другом {b}Эрику{/b}!"
    mrsjo "Это меньшее что я могу сделать!"
    show mrsj 50f
    show player 577f
    player_name "Большое спасибо, {b}Mrs. Johnson{/b}!"
    show player 576f
    show mrsj 49f
    mrsjo "Без проблем, дорогой!"
    mrsjo "Только поскорее возвращайся и расскажи мне все о твоем шоу талантов!"
    show mrsj 50f
    show player 577f
    player_name "Да, хорошо! Скоро увидимся {b}Mrs. Johnson{/b}!"
    hide player
    hide mrsj
    with dissolve
    $ player.remove_item("fake_guitar")
    $ player.get_item("guitar")
    $ M_dewitt.trigger(T_dewitt_get_fender_guitar)
    $ game.main()

label poker_table:
    scene erik_basement
    if not poker_table_seen:
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "У тебя даже чертов{b}Покерный стол{/b} здесь внизу?"
        show player 1
        show erik 4
        eri "Да. Ты хочешь сыграть?"
        $ poker_table_seen = True
        menu:
            "Играть в покер с {b}Эриком{/b}?"
            "Да":
                player_name "Я хотел бы, но я никогода раньше не играл в покер..."
                show player 14
                eri "Все хорошо, я обьясню тебе правила."
                show player 1
                show erik 4
                player_name "В таком случае, давай играть!"
                show player 14
                show erik 1

                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                $ game.main()
            "Нет":

                player_name "Может быть в другой раз, чувак. Я сейчас не в настроении."
                show player 14
                show erik 1
                eri "Все круто. без проблем."
                show player 1
                show erik 4
                hide player
                hide erik
    else:

        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Давай сыграем в покер!"
        show player 1
        show erik 5
        eri "Да я думаю мы можем попробовать..."
        eri "Но нам нужно больше игроков?"
        show erik 1
        show player 4
        player_name "Хммм..."
        player_name "Да.Ты прав."
        player_name "Мы должны {b}найти кого-то{/b} кто бы захотел поиграть с нами."
        hide erik
        hide player
        with dissolve
    $ game.main()

label mrsj_poker:
    if poker_bot02 == "mrsj" and not poker_drunk:
        scene erik_basement_c
        show mrsj 19 at right with fastdissolve
        show erik 1f at Position(xpos=300,ypos=768) with fastdissolve
        show player 1 at left with dissolve
        mrsjo "Мальчики разве вы не планируете играть вот так, так ведб?"
        show player 11
        show mrsj 14
        player_name "..."
        show player 10
        player_name "Что вы имеете в виду?"
        show player 11
        show mrsj 18
        mrsjo "Ты не можешь играть в покер без отлично выпивки!"
        show mrsj 14
        show player 1
        show erik 4f
        eri "Выпивки?"
        show erik 1f
        show mrsj 18
        mrsjo "Давайте посмотрим что осталось в {b}шкавчике с напитками{/b}, Давайте?"
        hide player
        hide mrsj
        hide erik
        with dissolve

    elif poker_bot02 == "mrsj" and poker_drunk:
        scene poker_table
        show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
        show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
        show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
        with fade

        mrsjo "Итак..."
        mrsjo "Играем мы в {b}Omaha{/b}, или {b}Texas Hold'em{/b}?"
        show mrsjpoker 1
        player_name "..."
        player_name "Мы только знаем {b}покер на раздевание{/b}..."
        show mrsjpoker 2
        mrsjo "Ха ха! Ты что шутишь?"
        show mrsjpoker 10 at Position(xpos=856,ypos=627)
        player_name "Это единственое во что играют люди в школе..."
        show erikpoker 2
        eri "Ты не должна... {b}Mrs. Johnson{/b}."
        show erikpoker 11
        show mrsjpoker 9 at Position(xpos=856,ypos=627)
        mrsjo "Я буду играть!"
        show mrsjpoker 4 at Position(xpos=857,ypos=626)
        mrsjo "Я не монашка.Я тоже могу веселиться!"
        show mrsjpoker 2
        mrsjo "Я играла в покер на раздевание давным-давно..."
        show mrsjpoker 5
        mrsjo "...И я была {b}лучшая{/b} в ней!"
        show erikpoker 12
        show mrsjpoker 1
        eri "Итак, что будем теперь делать?"
        show erikpoker 1
        menu mrsj_poker_repeat:
            "Играть.":
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
                show erikpoker 1
                player_name "Давайте играть!!"
                jump start_poker
            "Как играть.":

                player_name "Напомни мне еще ращ, как играть в покер?"
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                jump mrsj_poker_repeat

            "Пропустить мини-игру (Cheat)" if game.cheat_mode:
                menu:
                    "{b}Mrs. Johnson{/b} Проигрывает":
                        jump mrsj_lost
                    "{b}Erik{/b} Проигрывает":
                        jump erik_lost
                    "{b}[firstname]{/b} Проигрывает":
                        jump player_lost
    $ game.main()

label cabinet:
    scene erik_basement_cabinet
    if poker_bot02 == "":
        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Слишком много алкоголя..."
        show player 1
        show erik 4
        eri "Да, {b}Mr. Johnson{/b} всегда хорошо держалась ."
        show erik 1
        show player 14
        player_name "Что попробуем?"
        show player 1
        show erik 4
        eri "Я подумал может быть мы его оставим для особого случая?"
        show erik 1
        show player 4
        player_name "Я думаю ты прав."
        player_name "Мы должны {b}найти кого-то{/b} кто бы захотел поиграть с нами."
        hide erik
        hide player
        with dissolve

    elif poker_bot02 == "mrsj":
        if mrsj.completed(mrsj_poker_night_2):
            show erik 4f at Position(xpos=300)
            show player 1 at left
            show mrsj 14 at right
            with dissolve
            eri "Я принесу виски!"
            show erik 1f
            show mrsj 19
            show player 11
            mrsjo "Ох, вы оба в этом уверены?"
            show mrsj 19c
            show player 10
            player_name "О чем?"
            show mrsj 19
            show player 11
            mrsjo "С алкоголем, ты помнишь что произошло в прошлый раз, правда?"
            show mrsj 19c
            show erik 5f
            eri "Но, мы хорошо повеселимся, разве нет?"
            show erik 1f
            pause
            show mrsj 14 with fastdissolve
            pause
            show mrsj 17
            show player 1
            mrsjo "Думаю ты прав..."
            show mrsj 18
            mrsjo "Ох, к черту сделаем это!"
        else:

            show erik 5f at Position(xpos=300,ypos=768)
            show player 1 at left
            show mrsj 14 at right
            with dissolve
            eri "Виски..."
            eri "Виски... виски..."
            eri "Виски... виски... виски..."
            eri "Нет ничего но виски здесь..."
            show erik 1f
            show mrsj 17
            mrsjo "Мой муж пил только виски."
            show mrsj 14
            show player 14
            player_name "Все нормально!"
            player_name "Мы возьмем все что бы там ни было, ха ха!"
            show erik 15
            show player 1
            eri "Давайте попробуем его прежде чем ставить на стол?"
            show erik 16
            show mrsj 22
            mrsjo "посмотрим как он на вкус..."
            show erik 20
            show mrsj 21
            show player 185
            with fastdissolve
            eri "Поехали..."
            show player 186
            show erik 17
            player_name "За ваше здоровье!"
            show player 189
            show erik 19
            show mrsj 25
            with fastdissolve

            pause
            show mrsj 26
            show erik 17
            show player 190
            with fastdissolve
            pause
            show player 191
            player_name "Угх!!"
            show player 188
            show mrsj 24
            show erik 17
            mrsjo "Woaa.."
            show erik 20
            show mrsj 14
            eri "Хммм... Не плохо!"
            show erik 17
            player_name "..."
            show player 187
            player_name "Тебе это понравилось?!"
            show player 188
            show erik 20
            eri "Да, это даже мило."
            show player 185
            show erik 17
            show mrsj 18
            mrsjo "Отлично,Мальчики!Давайте вернемся и начнем игру!"
        hide mrsj
        hide erik
        hide player
        with dissolve
        $ poker_drunk = True
    $ game.main()

label mrsj_afterpoker_fun_block:
    scene erik_basement
    show player 11 at left
    show erik 4 at right
    with dissolve
    eri "Я думал мы хотели *Hic* пойти в тайную комнату..."
    eri "{b}Mrs. Johnson{/b} ждет нас,помнишь?"
    show player 14
    show erik 1
    player_name "Ох, тоооочн!"
    player_name "Давай вернемся обратно и посмотрим чего она хотела."
    show player 1
    show erik 4
    eri "Я*Hic* согласен."
    hide erik
    hide player
    with dissolve
    $ game.main()

label erik_vr:
    scene location_erik_basement01_closeup
    show erik 15f at right
    show player 13 at left
    with dissolve
    eri "Хэй, {b}[firstname]{/b}."
    show erik 15bf
    show player 14
    player_name "Хэй!"
    show player 11
    player_name "..."
    show player 12
    player_name "Ты... пил?"
    show player 11
    show erik 15f
    eri "Ох, {b}Mrs. Johnson{/b} хотела чтобы я прибрался в подвале."
    eri "Я как раз собирался выбрасить весь старую выпивку."
    show erik 15bf
    pause
    show player 38 with dissolve
    player_name "!!!" with hpunch
    show player 23 with dissolve
    player_name "Подожди!"
    player_name "Ты не видишь?"
    show player 18
    show erik 15f
    eri "Хмм?"
    show erik 15bf
    show player 14
    player_name "Мы можем использовать все эти вещи!!"
    show player 13
    show erik 5 with dissolve
    eri "Для чего?"
    show erik 3b
    show player 17
    player_name "Ну, у меня есть одна идея."
    show player 14
    player_name "Что если мы используем этот алкоголь с пользой!"
    show player 17
    player_name "Я имею в виду, это просто глупо все это добро выкидывать..."
    show player 13
    show erik 5
    eri "Хммм.... Да, я думаю."
    show erik 3b
    show player 14
    player_name "Что если мы приглоси сюда друзей со школы и... повеселимся!"
    show player 33
    player_name "Это место идеальное для вечернинок!"
    show player 14
    player_name "Только подумай, мы могли бы приглосить девченок к себе,играть в покер, и напиваться!"
    show player 13
    show erik 5
    eri "Я в этом не уверен."
    eri "{b}Mrs. Johnson{/b} будет в ярости если все выйдет из-под контроля..."
    show erik 3b
    show player 12
    player_name "Давай, {b}Эрик{/b}... Это место иделаное!"
    show player 14
    player_name "Просто подумай сколько крутых вещей мы могли бы тут сделать!"
    show player 33
    player_name "Мы погли бы даже приглосить девченок и поиграть в покер на раздевание..."
    show player 18
    show erik 4 with hpunch
    eri "!!!"
    eri "Я не знаю, {b}[firstname]{/b}..."
    show erik 1
    show player 30
    player_name "Хмм..."
    pause
    show player 12
    player_name "Что если я бы купил тебе то о чем ты всегда мечтал?"
    player_name "И ты помог бы мне пригласить сюда друзей?"
    show player 14
    player_name "Я немного подзаработал денег! Я определенно могу помочь тебе получить то что ты хотел..."
    show player 13
    eri "..."
    show erik 4
    eri "Ну, есть кое-что о чем я всегда мечтал... но это стоит очень дорого!"
    show erik 1
    show player 14
    player_name "Да? Что это?"
    show player 13
    show erik 4
    eri "В {b}Cosmic Cumics{/b}, я видел что они там продают VR шлем для {b}Virtual Saga X{/b}."
    show erik 1
    show player 17
    player_name "Сделано!"
    show player 13
    show erik 5
    eri "Серьезно?!"
    eri "Но, Подожди! Я... Я с этим хочу еще и игру тоже."
    show erik 4
    eri "Называется... {b}World of Orcette{/b}."
    show erik 1
    show player 11
    player_name "..."
    show player 12
    player_name "Я слышал что это та одна из тех непристойных игр-"
    show player 5
    show erik 5b
    eri "Эммм!!"
    show erik 5
    eri "В общем!"
    show erik 4
    eri "Ты  это зделаешь, Я думаю"
    eri "Ты сможешь найти их в {b}Cosmic Cumics{/b}, в торговом центре."
    show erik 1
    show player 14
    player_name "Отлично."
    player_name "Договорились!"
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_vr)
    $ M_erik.unforce()
    $ game.main()

label erik_card_hunt:
    scene location_erik_basement01_closeup
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Привет, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Хэй, {b}Erik{/b}."
    show player 2
    player_name "Я решил заглянуть к тебе и посмотреть чем ты занимаешься."
    show player 1
    show erik 5
    eri "Ох, просто ищу свои {b}Magic the Fappening{/b} карты."
    eri "Мне нужно подготовится к следующему турниру, но я не могу их найти..."
    show erik 1
    show player 14
    player_name "Ох да?"
    show player 13
    show erik 5
    eri "Я обычно оставлял их внизу в подвале, но их там нет."
    show erik 1
    show player 12
    player_name "Хммм..."
    player_name "Я могу помочь тебе найти их. Они не могли куда то изчезнуть."
    show player 13
    show erik 5
    eri "Да, они должны быть где то здесь."
    eri "Не удивлюсь если {b}Mrs. Johnson{/b} переложили их?"
    show erik 1
    show player 14
    player_name "Ох да, я тоже  хотел тебе сказать."
    show player 17
    player_name "Она упоминала что собралась готовить ужин для тебя."
    show player 5
    show erik 5
    eri "Ты хочешь сказать что она уже ушла? убейте меня!"
    eri "Может быть я оставил их наверху."
    eri "Можешь посмотреть внизу?"
    show erik 1
    show player 14
    player_name "Да."
    show player 5

    hide erik with dissolve
    show player 4
    player_name "( Интересно где же он оставил свои карты. )"
    show player 12
    player_name "( Они должны находится где-то здесь... )"
    hide player with dissolve
    return

label erik_orcette:
    scene location_erik_basement01_closeup
    show erik 1 at right
    show player 14 at left
    with dissolve
    player_name "Внизу в подвале, снова?"
    player_name "Что ты делаешь?"
    show player 13
    show erik 5
    eri "Хэй, {b}[firstname]{/b}!"
    eri "... Я как раз думал о продаже покерного стола."
    show erik 1
    show player 23
    player_name "Что?!"
    show player 30
    player_name "Почему!"
    show player 12
    player_name "Этот покерный стол крутой!"
    show player 5
    show erik 3b
    eri "..."
    show player 10
    player_name "В смысле эта штука сделана из твердого дуба!"
    show player 11
    show erik 5
    eri "Да... но никто никогда не использует его."
    eri "И мне бы пригодилось немного деньжат."
    show erik 3b
    show player 12
    player_name "Не Будет ли {b}Mrs. Johnson{/b} против если ты продаешь вещи её бывшего мужа"
    show player 11
    show erik 5
    eri "Я думаю. Она всегда говорит что она готова на все что бы сделать меня счастливым и мне очень нужны наличные..."
    show erik 3b
    show player 12
    player_name "Да ладно, {b}Erik{/b}. Все эти вещи дороги её как память."
    player_name "Что еще такого важного тебе нужно продать из ее вещей?"
    show player 5
    show erik 3
    eri "Ну..."
    show erik 5
    eri "Это своего рода личное?"
    show erik 3b
    show player 26
    player_name "Ох, да ладно."
    pause
    show player 14
    player_name "Слушай, Я куплю тебе все что ты захочеть только если ты пообещаешь мне не продавать этот стол."
    show player 30
    player_name "Договорились?"
    show player 5
    eri "..."
    show erik 4
    eri "Почему ты это делаешь?"
    show erik 1
    show player 43
    player_name "Потому что у меня есть некоторые планы на этот подвал!"
    show player 14
    player_name "Я думаю мы сможем использовать его для тусовок... а может приглосим... людей сюда!"
    show player 13
    show erik 4
    eri "Хорошо..."
    show erik 5
    eri "Но пообщай что не будешь смеятся надо мной?"
    show erik 3b
    show player 12
    player_name "Эээ... конечно?"
    show player 5
    eri "..."
    show erik 5
    eri "Ты можешь купить эту вещб только по онлайну..."
    eri "Итак если твой комп до сих пор сломан, ты должен его починить."
    show erik 1
    show player 12
    player_name "Что ты хочешь что бы я купил для тебя {b}Эрик{/b}?"
    show player 5
    eri "..."
    show erik 4
    eri "Ну, ты когда-нибудь слышал об  {b}Orcette{/b}?"
    show erik 1
    pause
    show player 10
    player_name "Что это?"
    show player 11
    show erik 5
    eri "Это что то вроде... резинку... тоннель?"
    show erik 1
    show player 12
    player_name "Что?"
    show player 11
    show erik 5
    eri "И она зеленая!"
    show erik 1
    show player 14
    player_name "Подожди... Это, сексуальная игрушка?!"
    show player 13
    show erik 5
    eri "Хэй! Ты обещал!"
    show erik 3
    show player 17
    player_name "Хорошо. хорошо."
    show player 26
    player_name "У меня не будет проблем с покупкой этого для тебя."
    show player 13
    show erik 5
    eri "Это было бы круто, {b}[firstname]{/b}!"
    show erik 3
    show player 14
    player_name "Только запомни. Ты ничего не будешь продавать из вещей {b}Mrs. Johnson{/b},хорошо!"
    show player 13
    show erik 5
    eri "Да, Я обещаю."
    eri "Только привези это как можно скорее!"
    show erik 1
    show player 12
    player_name "Я сделаю."
    show player 10
    player_name "Просто расслабся, потому что это займет некторое время для доставки."
    show player 11
    show erik 5
    eri "Посмотри что бы не было жучков на моей поссылке которые смогут меня отследить!"
    show erik 1
    show player 12
    player_name "Чего?"
    show player 11
    show erik 5
    eri "Ты знаешь, компания доставок  в наши дни отслеживает все свои перевозки."
    show erik 4
    eri "Они могут сказать тебе точно когда она придет"
    show erik 1
    show player 12
    player_name "Хорошо. Я посмотрю что я смогу зделать."
    show player 5
    show erik 4
    eri "Спасибо, {b}[firstname]{/b}. Ты лучший!"
    show erik 1
    show player 14
    player_name "Да. ДА."

    hide erik with dissolve
    show player 12
    player_name "( Я думаю я должен залезть в компьютер и найти этот {b}Orcette{/b}... )"
    hide player with dissolve
    $ erik.add_event(erik_orcette)
    $ M_erik.unforce()
    $ game.main()

label eriks_basement_first_time:
    scene erik_basement
    show player 14 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Чувааааак! Это место выглядит четровски здорово!"
    player_name "Почему ты мне не показывал этого места раньше?"
    show player 1
    show erik 4
    eri "Я не знаю. Я думаю я никода об этом не задумывался..."
    eri "Плюс, {b}Mr. Johnson{/b} очень дорожила местом своего мужчины когда он жил здесь."
    show erik 14
    eri "Ему нравилось побыть одному."
    show erik 4
    eri "Но я больше уже об этом не беспокоюсь!"
    show erik 1
    show player 14
    player_name "Могу я тут осмотреться?"
    show erik 1
    show player 1
    eri "Конечно  приятель!"
    show erik 1
    show player 14
    player_name "Мило!"
    show player 1
    show erik 5
    eri "Постарайся ничего не разбить."
    eri "{b}Mrs. Johnson{/b} будет в ярости!"
    show erik 1
    show player 14
    player_name "Я буду осторожен."
    hide player with dissolve
    hide erik with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
