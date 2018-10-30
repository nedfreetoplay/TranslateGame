label park_count_night_0:
    scene park_night
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "( Я слышу голоса вдалеке... )"
    show player 14
    player_name "( Может мне стоит пойти проверить! )"
    hide player with dissolve
    return

label park_rap_battle:
    scene park_bench
    if M_dewitt.is_state(S_dewitt_eve_meet_up):
        call expression game.dialog_select("park_dewitt_eve_meet_up")
        $ M_dewitt.trigger(T_dewitt_gang_deal)

    elif M_eve.is_set("first park visit"):
        call expression game.dialog_select("park_rap_battle_first_visit")
        $ M_eve.set("first park visit", False)
        menu:
            "Хорошо выглядишь!":
                call expression game.dialog_select("park_rap_battle_first_visit_look_good")
                jump expression game.dialog_select("park_rap_battle_options")
            "Мне нужно вернуться домой.":

                call expression game.dialog_select("park_rap_battle_first_visit_go_home")
    else:

        call expression game.dialog_select("park_rap_battle_pre")
        menu park_rap_battle_options:
            "Давай рэп-битву.":
                call expression game.dialog_select("park_rap_battle_start")
                menu:
                    "Чико":
                        $ rap_opponent = "Chico"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Сад" if player.stats.chr() < 4:
                        $ pass

                    "Чад" if player.stats.chr() >= 4:
                        $ rap_opponent = "Chad"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "<>[chr_warn]Тайрон" if player.stats.chr() < 7:
                        $ pass

                    "Тайрон" if player.stats.chr() >= 7:
                        $ rap_opponent = "Tyrone"
                        call expression game.dialog_select("park_rap_battle_opponent")
                        jump expression game.dialog_select("rapbattle_listing")

                    "Пропустить Мини игру (Cheat)" if game.cheat_mode:
                        $ game.timer.tick()
                        $ player.stats.increase("chr")
                        show unlock23 at truecenter with dissolve
                        pause
                        hide unlock23 with dissolve
            "Я должен идти.":

                call expression game.dialog_select("park_rap_battle_leave")

    hide player
    hide eve
    with dissolve
    $ game.main()

label park_dewitt_eve_meet_up:
    show eve 1 zorder 1 at Position (xpos=450)
    show player 12 at left
    with dissolve
    player_name "Хорошо, я тут. Какие идеи?"
    show player 5
    show eve 2b
    eve "Ну для начала нам, наверное, надо вычистить зал для шоу талантов?"
    show eve 1
    show player 10
    player_name "Да."
    show player 5
    show eve 2
    eve "Поздоровайся с помощниками."
    show eve 1
    show tyrone 2 at Position (xpos=650)
    show chad 1 at right
    show chad 1 at Position (xoffset=-46)
    with dissolve
    tyrone "Что стряслось, чувак?"
    show tyrone 1
    show player 12
    player_name "Тпру. Хочешь сказать, эти парни помогут нам убраться?"
    show player 5
    show chad 4 with dissolve
    chad "Точняк! Ты думаешь, потому, что мы гангста, мы не можем делать небольшую благотворительную работу время от времени?"
    show chad 1 at Position (xoffset=-46) with dissolve
    show player 10
    player_name "Нет, но я не думал-"
    show player 11
    show tyrone 2
    tyrone "Хорошо, потому что ты был прав! Хахаха!"
    show tyrone 1
    show player 12
    player_name "Ну ладно, признаю что я удивлён."
    show player 5
    show eve 2
    eve "Хех, они помогут нам."
    eve "... Но тебе тоже что-то надо сделать."
    show eve 1
    show player 14
    player_name "Понятно."
    show player 12
    player_name "И что мне делать?"
    show player 5
    show chad 2 at Position (xoffset=-46)
    chad "Ты должен {b}достать немного 40s{/b}, йоу!"
    show chad 1 at Position (xoffset=-46)
    show player 10
    player_name "А, 40s?"
    show player 5
    show eve 1bf with dissolve
    eve "Не надо 40s! Я сказала банки!"
    show eve 1cf
    show chad 2 at Position (xoffset=-46)
    chad "Пфф, ладно! Не важно."
    show chad 1 at Position (xoffset=-46)
    show eve 2 with dissolve
    eve "Они просто хотят чтобы ты {b}достал им пиво{/b}."
    show eve 1
    show player 10
    player_name "Что?! Я не достаточно взрослый чтобы покупать пиво!"
    show player 5
    show eve 6b
    eve "Ну да. Я знаю!"
    show eve 6
    eve "А твоему другу не достаточно лет?"
    show eve 1
    show player 12
    player_name "Хух?"
    show player 5
    show eve 6
    eve "Парню с караоке машиной! {b}Эван{/b}?"
    show eve 1
    show player 12
    player_name "Ты имеешь в виду {b}Эрика{/b}?"
    show player 5
    show eve 2
    eve "Да, его!"
    show eve 6
    eve "{b}У него дома была куча пива.{/b}!"
    show eve 1
    show player 37 with dissolve
    player_name "Эй, чел."
    show player 38 with dissolve
    player_name "... Они помогут нам очистить все, не так ли?"
    show player 5 with dissolve
    show tyrone 2
    tyrone "Договор был такой, чучуло."
    show tyrone 1
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Хорошо, я посмотрю, что я могу сделать."
    player_name "Встретимся завтра в {b}актовом зале{/b} для уборки!"
    show player 5
    show eve 2
    eve "Они будут там!"
    hide eve
    hide chad
    hide tyrone
    with dissolve
    show player 10
    player_name "Я должен поговорить с {b}Эриком{/b} можно ли {b}взять немного пива Миссис Джонсон{/b}."
    return

label park_rap_battle_first_visit:
    show player 1 at left
    show eve 2 at right
    with dissolve
    eve "Так ты решил показаться, да?"
    show eve 1
    show player 2
    player_name "Ну, ты сказала, что я должен..."
    show eve 6
    show player 11
    eve "Не поздновато ли для тебя?"
    eve "У тебя что, нет комендантского часа?"
    show eve 1
    show player 5
    player_name "..."
    show eve 6
    show player 11
    eve "Я шучу!!"
    show eve 1
    show player 17
    player_name "Хаха..."
    show player 1
    show eve 2
    eve "Итак, что случилось?"
    show eve 1
    return

label park_rap_battle_first_visit_look_good:
    show player 21
    player_name "Не знаю, говорил ли я тебе, но мне очень нравятся твои волосы! "
    show eve 4
    show player 13
    eve "Хаха! Они разные!"
    show player 29
    player_name "Просто говорю... Синий действительно хорошо на тебе смотрится."
    show eve 3
    show player 13
    eve "..."
    show eve 4
    eve "О... Спасибо?"
    show eve 6
    show player 11
    eve "Хм... Эй, тебе стоит остаться здесь ненадолго!"
    eve "Ребята скоро устроят {b}рэп-битву{/b}."
    show eve 1
    show player 2
    player_name "О, да? Как ... рассеять друг друга микрофоном?"
    show eve 6
    show player 1
    eve "Да!"
    show eve 7
    show player 11
    eve "Я думаю ты должен это сделать."
    show eve 5
    show player 23 with hpunch
    player_name "Что?!"
    show eve 6
    show player 5
    eve "Да ладно. Не стесняйся."
    eve "Давай повеселимся!"
    show eve 5
    show player 21
    player_name "Думаю можно попробовать..."
    show player 13
    show eve 6
    eve "Ну что? Идешь?"
    return

label park_rap_battle_first_visit_go_home:
    show player 10
    player_name "О, дерьмо! Мне нужно идти. У меня есть дела."
    show eve 2
    show player 13
    eve "Наверное, у тебя действительно есть комендантский час..."
    show eve 1
    show player 2
    player_name "Сожалею. Я приду в другой раз!"
    show eve 7
    show player 13
    eve "Хорошо."
    return

label park_rap_battle_pre:
    show player 1 at left
    show eve 6 at right
    with dissolve
    eve "Привет {b}[firstname]{/b}!"
    show eve 5
    show player 14
    player_name "Привет, {b}Ева{/b}!"
    show eve 6
    show player 1
    eve "Я рада, что ты появился!"
    show eve 3
    show player 14
    player_name "Приятно видеть тебя снова..."
    show eve 4
    show player 1
    eve "Че как дела?"
    show eve 1
    return

label park_rap_battle_start:
    show player 33
    show eve 5
    player_name "Я хочу снова рэп-битву!"
    show eve 6
    show player 1
    eve "Да??"
    show eve 5
    show player 26
    player_name "Да! Думаю, мне лучше."
    show eve 6
    show player 1
    eve "Клево!"
    show eve 8
    eve "Okay. Вот твой микрофон..."
    show eve 1
    show player 70
    player_name "Хммм... С кем мне следует сражаться?"
    show player 71
    return

label park_rap_battle_leave:
    show player 10
    player_name "Вообще-то, мне нужно идти. Мне нужно кое-что сделать."
    show player 13
    show eve 6
    eve "Но, ты только пришел..."
    show eve 1
    show player 2
    player_name "Сожалею. Я приду в другое время, чтобы потусоваться!"
    show eve 7
    show player 13
    eve "Хорошо..."
    return

label park_rap_battle_opponent:
    if rap_opponent == "Chico":
        player_name "Я пойду против {b}[rap_opponent]{/b} первый."
        hide eve with dissolve
        call expression game.dialog_select("park_rap_battle_opponent_chico")
    else:

        player_name "Я пойду против {b}[rap_opponent]{/b}."
        hide eve with dissolve
        if rap_opponent == "Chad":
            call expression game.dialog_select("park_rap_battle_opponent_chad")
        else:

            call expression game.dialog_select("park_rap_battle_opponent_tyrone")

    hide player
    hide chico
    hide chad
    hide tyrone
    hide douche
    with dissolve
    return

label park_rap_battle_opponent_chico:
    if chico_battle_count == 0:
        call expression game.dialog_select("park_rap_battle_opponent_chico_first")
        $ chico_battle_count = 1
    else:

        call expression game.dialog_select("park_rap_battle_opponent_chico_repeat")
    return

label park_rap_battle_opponent_chico_first:
    show player 77
    show douche 1 at right
    with dissolve
    player_name "Привет ребята!"
    show douche 2
    show player 74
    show chico 3 with dissolve
    chi "Ты кто такой, черт возьми?!"
    show chico 1
    show player 71
    player_name "Привет! Я {b}[firstname]{/b}!"
    player_name "И я предполагаю, что ты... {b}Чико{/b}?"
    show chico 2
    show player 74
    chi "Ты меня не знаешь, фу!"
    show chico 1
    show player 71
    player_name "Ну, {b}Eve{/b} сказала мне только твое имя-"
    show chico 3 with hpunch
    show player 74
    chi "{b}ЙОУ{/b}! Заткнись {b}нахуй{/b}!"
    show player 75
    show chico 1
    player_name "..."
    show chico 4
    show player 74
    chi "Я иду первым, {b}подвинься{/b}!"
    return

label park_rap_battle_opponent_chico_repeat:
    show player 77
    show douche 1 at right
    with dissolve
    player_name "Привет ребята!"
    show douche 2
    show player 74
    show chico 3 with dissolve
    chi "Ты вернулся за добавкой? Мелкий сопляк!"
    show chico 1
    show player 71
    player_name "Привет {b}Чико{/b}!"
    player_name "Давай начнем!"
    show chico 4
    show player 74
    chi "Я иду первым, {b}подвинься{/b}!"
    return

label park_rap_battle_opponent_chad:
    show player 1
    show chad 2 at right with dissolve
    chad "Так ты тот парень, который победил Чико."
    chad "Не знаю, почему ты подходишь ко мне, если не думаешь, что сможешь победить меня."
    show chad 1
    show player 2
    player_name "Это именно то, о чем я думаю."
    show chad 4
    show player 1
    chad "Зацени это! У паренька есть яйца!"
    chad "Я сыграю в твою игру, просто знай, что ты не уйдешь отсюда так же, как пришел."
    return

label park_rap_battle_opponent_tyrone:
    show player 1
    show tyrone 2 at right with dissolve
    tyrone "Ay, кто этот дурак?"
    show tyrone 1
    show player 2
    player_name "Хей Я-"
    show player 3
    show tyrone 3
    tyrone "Разве я спрашивал тебя?"
    show player 12
    show tyrone 1
    player_name "Нет, но я подумал-"
    show tyrone 2
    tyrone "Ты неправильно подумал!"
    tyrone "Теперь ты пытаешься получить по заднице, или ты здесь, чтобы тратить мое чертово время?"
    show tyrone 4
    show player 12
    player_name "Никакой?"
    show player 1
    show tyrone 3
    tyrone "Мальчишка, я дал тебе только два варианта, и ты делаешь последний, прямо сейчас!"
    show tyrone 2
    tyrone "Давай я тебя зажарю, и покончим с этим!"
    return

label park_take_picture_judith:
    call expression game.dialog_select("park_take_picture_judith_pre")
    if player.has_picked_up_item("masterkey"):
        call expression game.dialog_select("park_take_picture_judith_have_master_key")
    else:

        call expression game.dialog_select("park_take_picture_judith_do_not_have_master_key")

    $ M_okita.trigger(T_okita_picture_taken)
    $ game.main()
    return

label park_take_picture_judith_pre:
    scene location_park_closeup
    show player 1 at left
    show judith 5 at right
    with dissolve
    jud "Ты пришел!"
    show player 2
    show judith 4
    player_name "Я же тебе сказал что приду."
    show player 1
    show judith 5
    jud "Это замечательно! Не могу передать, как много это для меня значит."
    show player 2
    show judith 4
    player_name "Нет проблем, {b}Джудит{/b}."
    player_name "Что ты хочешь, чтобы я сделал?"
    show player 1
    show judith 5
    jud "... Просто садись рядом со мной."
    show player 2
    show judith 4
    player_name "Хорошо."

    scene location_park_bench_closeup2
    show playerf 2 zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 4 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show judithfa 3 zorder 1 at Position(xpos=0.6645, ypos=0.635)
    player_name "Так?"
    show playerf 2b
    show judithf 5
    jud "Нет, глупыш."

    scene location_park_bench_closeup3
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 8 zorder 0 at Position(xpos=0.665, ypos=1.0)
    show judithfa 4 zorder 1 at Position(xpos=0.725, ypos=0.4375)
    show juditho 1 zorder 4 at Position(xpos=0.5065, ypos=0.639)
    with dissolve
    jud "Так!"
    jud "Улыбочку!"

    scene location_park_bench_cutscene
    with fade
    show text "Я не знаю, как эта фотография должна была помочь {b}Джудит{/b}?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Но казалось, что это небольшая цена, чтобы заплатить за линзы, которые хотела {b}Okita{/b}." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Плюс это сделает {b}Джудит{/b} по-настоящему счастливой!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_park_bench_closeup2
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show judithf 6 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show judithfa 2 zorder 1 at Position(xpos=0.67, ypos=0.7275)
    with dissolve
    jud "Это идеально!"
    show judithf 5
    jud "Спасибо большое, {b}[firstname]{/b}!"
    show playerf 2
    show judithf 4
    player_name "Нет проблем."
    show playerf 2c
    player_name "Как насчет запасного набора очков..."
    show judithf 2
    show judithfa 1 at Position(xpos=0.67, ypos=0.76) with dissolve
    show playerf 2b
    jud "Ох, Конечно!"
    jud "Я держу их в шкафчике в школе."
    show judithf 3
    jud "Я могу записать комбинацию для тебя, одну секунду."
    show playerf 2c
    show judithf 1
    player_name "Все в порядке, мне не нужна комбинация."
    return

label park_take_picture_judith_have_master_key:
    show playerf 2b
    show judithf 2
    jud "Не нужно?"
    show playerf 2c
    show judithf 1
    player_name "У меня есть мастер-ключ от всех шкафчиков."
    show playerf 2b
    show judithf 5
    jud "Правда?! Как тебе удалось получить его?"
    show playerf 2c
    show judithf 4
    player_name "Хех, У меня свои методы."
    show playerf 2b
    show judithf 5
    jud "Это потрясающе!"
    jud "Я понятия не имела, что ты такой плохой мальчик!"
    show playerf 2c
    show judithf 4
    player_name "Ухх, Да. Хе, Похоже..."
    player_name "Спасибо за помощь, {b}Джудит{/b}. Увидимся позже."
    show playerf 2b
    show judithf 5
    jud "Спасибо, {b}[firstname]{/b}! Увидемся!"
    return

label park_take_picture_judith_do_not_have_master_key:
    show playerf 2b
    show judithf 2
    jud "Не нужно?"
    show playerf 2c
    show judithf 1
    player_name "Я знаю, где {b}директрисса Смит хранит свой Мастер-ключ{/b}..."
    show playerf 2b
    show judithf 5
    jud "Правда?! Ты собираешься украсть ключ директора?"
    show playerf 2c
    show judithf 4
    player_name "Украсть?! Я не знаю насчет этого... Я просто хочу одолжить его, пока они не купят мне новый замок."
    show playerf 2b
    show judithf 5
    jud "Это потрясающе!"
    jud "Я понятия не имела, что ты такой плохой мальчик!"
    show playerf 2c
    show judithf 4
    player_name "Ухх, Да. Хе, Похоже..."
    player_name "Спасибо за помощь, {b}Джудит{/b}. Увидимся позже."
    show playerf 2b
    show judithf 5
    jud "Спасибо, {b}[firstname]{/b}! Увидемся!"
    return

label fountain_dialogue:
    $ player.go_to(L_park_fountain)
    scene expression game.timer.image("park_fountain{}")
    if not player.has_item("weird_coin"):
        if game.timer.is_dark():
            show expression "objects/object_coin_01_night.png" at Position(xalign = 0.44, yalign = 0.81)
        else:

            show expression "objects/object_coin_01.png" at Position(xalign = 0.44, yalign = 0.81)
    player_name "( Я вижу там много монет. )"
    $ player.location.call_screen(False, False)

label coin_dialogue:
    call expression game.dialog_select("coin_dialogue_pre")
    $ player.get_item("weird_coin")
    call expression game.dialog_select("coin_dialogue_after")
    $ player.location.call_screen(False, False)

label coin_dialogue_pre:
    hide expression "objects/object_coin_01.png"
    show expression "objects/closeup_coin_01.png" at Position(xalign = 0.5, yalign = 1.0)
    with dissolve
    player_name "Хух?"
    player_name "Похоже на очень старую монету."
    player_name "Только посмотрите на эти странные {b}символы{/b}!"
    player_name "Мне следует оставить ее себе. Может, она чего-то стоит?"
    show popup_item_coin1 at truecenter with dissolve
    return

label coin_dialogue_after:
    pause
    hide popup_item_coin1 with dissolve
    hide expression "objects/closeup_coin_01.png" with dissolve
    return

label park_night_closed:
    scene park_night
    show player 10 with dissolve
    player_name "( Уже поздно. Мне нужно вернуться домой. )"
    hide player
    hide park_night
    $ game.main()

label park_pilly_button:
    call expression game.dialog_select("park_pilly_button_dialogue")
    $ player.go_to(L_map)
    $ M_roxxy.trigger(T_roxxy_drug_deal_over)
    $ game.timer.tick()
    $ game.sleep_lock = False
    $ game.main()

label park_pilly_button_dialogue:
    scene park_bench
    show player 90 at Position (xpos=400)
    show player_outfit bb 638e at Position (xpos=400)
    show clyde 2 at left
    with dissolve
    clyde "Ах, вот он где!"
    clyde "Позволь мне говорить прямо сейчас!"
    show clyde 1
    show pilly 2f at right with dissolve
    buyer "... {b}Клайд{/b}?"
    show pilly 1f
    show clyde 4 with dissolve
    clyde "Ох, ох... Как поживает {b}Пилли{/b}..."
    show clyde 3
    show player 10
    player_name "{b}Пилли{/b}?"
    player_name "Что это за имя такое?"
    show player 5
    show pilly 2f
    pilly "Простите?!"
    show pilly 1f
    show clyde 22 with dissolve
    clyde "Тссс, не говори ничего о его имени..."
    clyde "Он чувствительный."
    show clyde 2
    clyde "Не обращай на него внимания, {b}Пилли{/b}. Как насчет покурить, прежде чем мы перейдем к делу?"
    show clyde 1
    pilly "..."
    show pilly 2f
    pilly "Я бросил."
    show pilly 1f
    show clyde 22
    clyde "Да ну на?!"
    clyde "... Ты знаешь, никто не любит слабаков, {b}Пилли{/b}."
    show clyde 21
    show pilly 2f
    pilly "Да, ну... Я получил предложение, от которого не смог отказаться."
    pilly "Где {b}Кристи{/b}?"
    show pilly 1f
    show clyde 22
    clyde "Боюсь, {b}тетушка{/b} занята другим."
    show clyde 21
    pilly "..."
    show pilly 2f
    pilly "Ну, это позор, {b}твоя тетя{/b} обычно предлагает подсластить пилюлю."
    pilly "Кто этот джентльмен?"
    show pilly 1f
    show player 11
    player_name "..."
    show clyde 2
    clyde "А, ну да... Это мой новый помощник."
    clyde "Ты можешь позвонить ему... Эмм..."
    clyde "... {b}Мистер Уайт{/b}!"
    show clyde 1
    show player 18
    pilly "..."
    show pilly 2f
    pilly "Здесь происходит что-то подозрительное, и мне это не нравится, {b}Клайд{/b}."
    show pilly 1f
    show clyde 2
    clyde "Сейчас, сейчас... Что-то не чисто!"
    show player 90
    show clyde 28 with dissolve
    clyde "Я принес товар, как мы и договаривались..."
    clyde "Посмотри сам!"
    show clyde 1
    show pilly 4f
    with dissolve
    pilly "Это намного больше, чем мы обсуждали по телефону."
    show pilly 6f with dissolve
    show clyde 2
    clyde "Видишь ли, у меня небольшая распродажа."
    clyde "Я отдам тебе всю партию за $100,000!"
    show clyde 1
    pilly "..."
    show pilly 5f
    pilly "Хех, как именно вы пришли к такому количеству?"
    show pilly 6f
    show clyde 26
    clyde "Это 5 фунтов лучших вещей прямо сейчас!"
    clyde "Это стоит каждого пенни!"
    show clyde 25
    pilly "..."
    show pilly 5f
    pilly "Думаю, нет."
    pilly "Я дам тебе $60,000."
    show pilly 6f
    show clyde 26
    clyde "Пфф, ты что, совсем из ума выжил?!"
    clyde "Ты не воспользуешься мной!"
    show clyde 25
    show pilly 5f
    pilly "Поступай как знаешь."
    show clyde 27
    show pilly 2f
    with dissolve
    pilly "Удачи вам!"
    show pilly 1f
    show clyde 28
    clyde "Ну, подожди."
    show clyde 22
    show pilly 6f
    with dissolve
    clyde "Не делай ничего радикального, мы просто торгуемся!"
    show clyde 26
    clyde "$75,000!"
    show clyde 25
    show player 12
    player_name "Мы возьмем $ 60,000."
    show player 90
    show clyde 22
    clyde "{b}ЧТО?!{/b}" with hpunch
    show clyde 26
    clyde "А теперь послушай меня!"
    show clyde 25
    show player 12
    player_name "Заткнись, {b}Клайд{/b}!"
    show clyde 21
    player_name "Не забывай, зачем мы здесь!"
    show player 90
    clyde "..."
    show clyde 22
    clyde "Хорошо."
    show clyde 21
    show pilly 5f
    pilly "Хех, приятно видеть, что твой \"помощник\" - разумный человек."
    show pilly 3f with dissolve
    pilly "Приятно вести бизнес с вами, {b}Мистер Уайт{/b}."
    show player 638b
    show player_outfit 638d
    show pilly 1f
    with dissolve
    pause
    show player 638
    show player_outfit 638c
    with dissolve
    player_name "Д-да... Спасибо."
    show player 638b
    show player_outfit 638d
    hide pilly
    with dissolve
    show clyde 22
    clyde "... Чувак, он только что склонил нас над бочкой со сделкой!"
    show clyde 21
    show player 12f at Position (xpos=700)
    show player_outfit 638ef at Position (xpos=700)
    with dissolve
    player_name "Давай, давай выбираться отсюда!"
    show player 90f
    show clyde 22
    clyde "Ну, держись!"
    clyde "А как насчет нас?"
    show clyde 21
    show player 10f
    player_name "Хм?"
    show player 5f
    show clyde 2
    clyde "Мы собираемся разделить эти деньги поровну, не так ли?!"
    show clyde 1
    show player 12f
    player_name "Нет!"
    player_name "Это значит, что {b}Тетя{/b} выйдит из тюрьмы!"
    player_name "... Помнишь?!"
    show player 90f
    show clyde 2
    clyde "Хорошо, но..."
    clyde "Может, просто сходим в стрип-клуб или ещё куда-нибудь?"
    clyde "На такие деньги можно купить кучу приватных танцев..."
    show clyde 1
    show player 12f
    player_name "... Тащи свою задницу домой и начинай писать это письмо!"
    show player 90f
    show clyde 26
    clyde "Хорошо, хорошо."
    clyde "Ты настоящий любитель вечеринок, понимаешь?"
    show clyde 31 with dissolve
    clyde "Кроме того, я написал тебе дурацкое письмо!"
    hide clyde
    hide player
    hide player_outfit
    show expression "objects/closeup_clyde_note_01.png"
    with dissolve
    pause
    hide expression "objects/closeup_clyde_note_01.png"
    show player 13f at Position (xpos=700)
    show player_outfit bb 638ef at Position (xpos=700)
    show clyde 1 at left
    with dissolve
    player_name "..."
    show player 14f
    player_name "Да, это должно сработать."
    show player 13f
    show clyde 2
    clyde "Хорошо."
    clyde "Я рад, что с этим бардаком покончено!"
    show clyde 1
    show player 10f
    player_name "Лучше быстро исчезни, если ты не хочешь оказаться в тюрьме."
    player_name "{b}Рокси{/b}, и я {b}завтра превратим это в полицию{/b}."
    show player 5f
    show clyde 4 with dissolve
    clyde "Не волнуйся, ничего страшного."
    clyde "К тому времени меня уже не будет, приятель!"
    clyde "Просто позаботься о своей кузине!"
    show clyde 3
    player_name "..."
    hide clyde with dissolve
    pause
    show player 14f
    player_name "Я должен отнести письмо {b}к Рокси завтра в школу{/b}."
    hide player
    hide player_outfit
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
