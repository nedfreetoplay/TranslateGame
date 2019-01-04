label MC_computer_night_locked:
    scene expression game.timer.image("bedroom{}")
    show player 24 at left
    player_name "( Я очень устал, я должен поспать... )"
    hide player 17 at left
    return

label egay_search_dialogue:
    if erik.started(erik_orcette):
        call expression game.dialog_select("egay_search_dialogue_erik_orcette_started")
    show screen MC_computer
    call screen egay("Search")

label egay_search_dialogue_erik_orcette_started:
    scene player_computer_bg
    show player_computer_egay_search
    player_name "( Хм... Думаю, я должен просто ввести название предмета, который хотел {b}Эрик{/b}. )"
    player_name "( Что это было снова? )"
    hide player_computer_egay_search
    hide player_computer_bg
    return

label egay_purchased_dialogue:
    scene player_computer_bg
    show player_computer_egay_purchased
    player_name "( Похоже, что я должен получить пакет в почтовом ящике во {b}Вторник{/b}. )"
    hide player_computer_egay_purchased
    hide player_computer_bg
    show screen MC_computer
    call screen egay("Purchased")

label egay_search:
    if erik.started(erik_orcette):
        if egay_search.lower() == "orcette":
            show screen MC_computer
            call screen egay("Found")
    show screen MC_computer
    call screen egay("Fail")

label webcam_dialogue:
    scene expression game.timer.image("MC_computer{}_b")
    if not connected:
        call expression game.dialog_select("webcam_dialogue_not_connected")
        call screen MC_computer

    elif (L_home_sisbedroom.is_here(M_jenny) and game.timer.is_morning()):
        if M_jenny.is_state(S_jenny_watch_stream) or M_jenny.is_state(S_jenny_watch_stream_tier_2) or M_jenny.is_state(S_jenny_watch_stream_tier_3) or M_jenny.finished_state(S_jenny_prepare_stream_tier_4):
            hide screen MC_webcam
            hide screen MC_computer
            $ A_computer_genius.unlock()
            if M_jenny.is_state(S_jenny_watch_stream):
                label electroclit_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam01_started_pre")
                $ current_camshow = 1

            elif M_jenny.is_state(S_jenny_watch_stream_tier_2):
                label ultravibrator_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam02_started_pre")
                $ current_camshow = 2

            elif M_jenny.is_state(S_jenny_watch_stream_tier_3):
                label dualsybian_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam03_started_pre")
                $ current_camshow = 3

            elif M_jenny.finished_state(S_jenny_prepare_stream_tier_4):
                $ sis_lastwebcam_show_seen = True
                label badmonster_replay:
                    call expression game.dialog_select("webcam_dialogue_sis_webcam_started_pre")
                call expression game.dialog_select("webcam_dialogue_sis_webcam04_started_pre")
                $ current_camshow = 4
            $ anim_toggle = False
            $ xray_toggle = False
            jump expression game.dialog_select("sis_camshow_loop")
        else:

            call expression game.dialog_select("webcam_dialogue_nothing_showing")
    else:

        call expression game.dialog_select("webcam_dialogue_nothing_showing")
    show screen MC_computer
    call screen MC_webcam

label webcam_dialogue_not_connected:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( Странно. Здесь говорится, что я могу подключить свой компьютер к {b}веб-камере{/b}, но, кажется, я не могу сделать это отсюда. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label webcam_dialogue_sis_webcam_started_pre:
    scene player_computer_bg with None
    show player_computer_webscreen_connecting
    $ renpy.pause(2, hard=True)
    hide player_computer_webscreen_connecting
    scene jennycam1
    show xtra 16 zorder 2
    show jennysex 6 zorder 1 at Position(xpos = 533, ypos = 746)
    jen "Приивет пааарни!"
    jen "Готовы ли вы к чему-то горяченькому?"
    jen "Я с нетерпением жду, чтобы промокать весь день!!"
    jen "Ой! Не забудьте подписаться чтобы посмотреть следующую часть шоу..."
    jen "Потому что эта красота здесь нуждается в деньгах!"
    show jennysex 8 with fastdissolve
    jen "Теперь для моих вип подписчиков..."
    jen "... У меня есть эта новая игрушка, которую я хотела попробовать!"
    show jennysex 7 with fastdissolve
    pause
    return

label webcam_dialogue_sis_webcam01_started_pre:
    show jennysex 10 with fastdissolve
    pause
    show jennysex 9
    jen "{b}Electro Clit{/b}!"
    jen "Это маленькое вибрирующее чудо ... для моего клитора!"
    show jennysex 11
    jen "Я всегда хотела один из них!"
    show jennysex 21 at Position(xpos = 543, ypos = 767) with dissolve
    jen "Давайте попробуем, парни..."
    show jennysex 22 with fastdissolve
    jen "Эй! Эта штука быстрая..."
    return

label webcam_dialogue_sis_webcam02_started_pre:
    show jennysex 13 with fastdissolve
    pause
    show jennysex 12
    jen "{b}Ultra Vibrator 2000{/b}!"
    jen "Это фаллоимитатор! Красивый и ребристый..."
    jen "Теперь, так как вы и просили, некоторые вставки с моими игрушками..."
    jen "... Я решила дать вам всем маленький подарок!"
    jen "Погнали, парни!"
    show jennysex 26 at Position(xpos = 0.5, ypos = 770) with dissolve
    jen "Размерчик под меня."
    jen "Давайте проверим это на практике..."
    show jennysex 27 with fastdissolve
    pause
    show jennysex 31 at Position(xpos = 512, ypos = 770)
    return

label webcam_dialogue_sis_webcam03_started_pre:
    show jennysex 19 at Position(xpos = 577) with fastdissolve
    pause
    show jennysex 18 with fastdissolve
    jen "{b}Dual Sybian{/b}!"
    show jennysex 20
    jen "Я читала жалобы онлайн, что я боюсь сделать в анус..."
    jen "Так вот доказательство того, что я не боюсь попробовать!"
    jen "В самом деле, зачем останавливаться на одной дырке?"
    jen "Для моих фанатов я сделаю Двойное проникновение!"
    show jennysex 18
    jen "Давайте я вскочу на этого быка и вскрою свою розовую анальную вишенку..."
    show jennysex 34 at Position(xpos = 344, ypos = 727) with dissolve
    pause
    show jennysex 35 at Position(xpos = 540, ypos = 582) with fastdissolve
    jen "... О боже! Какое странное чувство."
    return

label webcam_dialogue_sis_webcam04_started_pre:
    show jennysex 16 with fastdissolve
    pause
    show jennysex 15
    jen "А вот и он..."
    jen "{b}Bad Monster{/b}!"
    show jennysex 17
    jen "Все говорили об этой особенной игрушке..."
    jen "... а некоторые из вас помогли мне приобрести его, чтобы опустошить мою киску."
    show jennysex 15
    jen "Мне наконец-то удалось заполучить его!"
    show jennysex 17
    jen "А теперь приготовь свои кошельки, потому что я собираюсь приручить этого монстра!"
    show jennysex 40 at Position(xpos = 427)
    jen "Этому нужно МНОГО смазки..."
    show jennysex 41
    jen "... о БОГ!"
    jen "Очень большой!"
    return

label webcam_dialogue_nothing_showing:
    scene player_computer_bg
    show player_computer_webscreen
    player_name "( На данный момент ничего нет. )"
    hide player_computer_webscreen
    hide player_computer_bg
    return

label sis_camshow_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
		if not animated:
            if current_camshow == 1:
                show expression AnimatedImage("jennysex", [23,24,25,22], M_jenny) as jennysex zorder 1 at Position(xpos = 543, ypos = 767)

            elif current_camshow == 2:
                show expression AnimatedImage("jennysex", [28,29,30,31], M_jenny) as jennysex zorder 1 at Position(xpos = 512, ypos = 770)

            elif current_camshow == 3:
                show expression AnimatedImage("jennysex", [36,37,38,35], M_jenny) as jennysex zorder 1 at Position(xpos = 540, ypos = 582)

            elif current_camshow == 4:
                show expression AnimatedImage("jennysex", [42,43,44,41], M_jenny) as jennysex zorder 1 at Position(xpos = 427, ypos = 746)
             $ animated = True
			pause 8
        else:

            $ pose_counter = 0
            if current_camshow == 1:
                $ pose_list = [23,24,25,22]
                $ xpos_list = [543]
                $ ypos_list = [767]

            elif current_camshow == 2:
                $ pose_list = [28,29,30,31]
                $ xpos_list = [512]
                $ ypos_list = [770]

            elif current_camshow == 3:
                $ pose_list = [36,37,38,35]
                $ xpos_list = [540]
                $ ypos_list = [582]

            elif current_camshow == 4:
                $ pose_list = [42,43,44,41]
                $ xpos_list = [427]
                $ ypos_list = [746]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex zorder 1 at Position(xpos = xpos_list[0], ypos = ypos_list[0])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1

label sis_camshow_finish:
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    if current_camshow == 1:
        call expression game.dialog_select("sis_camshow_01_finish")
		$ M_jenny.trigger(T_jenny_watched_stream)

    elif current_camshow == 2:
        call expression game.dialog_select("sis_camshow_02_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_2"
        $ M_jenny.trigger(T_jenny_watched_stream_tier_2)

    elif current_camshow == 3:
        call expression game.dialog_select("sis_camshow_03_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_3"
        $ M_jenny.trigger(T_jenny_watched_stream_tier_3)

    elif current_camshow == 4:
        call expression game.dialog_select("sis_camshow_04_finish")
        $ persistent.cookie_jar["Jenny"]["gallery_labels"]["05_label"] = "webcam_menu_4"
    $ game.timer.tick()
	$ game.main()

label sis_camshow_01_finish:
    show jennysex 25b
    jen "Ааааа!!!" with vpunch
    jen "{b}*пыхтит*{/b}"
    jen "Это было круто!"
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "Вау..."
    player_name "( {b}[jen_name]{/b} устраивает Эротический видеочат?! )"
    show player 310
    player_name "( Так странно видеть ее такой... )"
    show player 312
    player_name "( Блин, она такая горячая... )"
    show player 310
    player_name "( Думаю, на сегодня достаточно. )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_02_finish:
    show jennysex 28b
    jen "Ой... Я уже почти..."
    show jennysex 29b
    jen "Я... кончаю!!"
    show jennysex 32
    jen "Аааа!!!" with vpunch
    show jennysex 33 with dissolve
    jen "У... У меня никогда раньше такого не было..."
    jen "Как много..."
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "( Так вот как выглядит сквиртинг. )"
    show player 310
    player_name "Было много! Даже на камеру попало!"
    player_name "( Я понятия не имел, что {b}[jen_name]{/b} может так сделать... )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_03_finish:
    show jennysex 39 at Position(xpos = 540)
    jen "Аааа!!!" with hpunch
    jen "{b}*пыхтит*{/b}"
    jen "Я никогда не кончала так раньше..."
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "Вау..."
    player_name "( Она очень любит кататься на этой штуке. )"
    show player 310
    player_name "( Интересно, что еще она хочет сделать на камеру... )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label sis_camshow_04_finish:
    show jennysex 43 at Position(xpos = 427)
    jen "Ааааа!!!" with vpunch
    show jennysex 45 with fastdissolve
    jen "Какой хороший монстр..."
    jen "... моя киска будет болеть несколько дней!"
    hide xtra
    hide jennycam1
    hide jennysex
    scene bedroom_desk
    show player 311 at Position(xpos = 672)
    with fade
    player_name "( Я думал, это просто для показухи. )"
    player_name "( Видимо, это может там поместиться!)"
    player_name "Она так легко сделала это..."
    player_name "( Надеюсь, у нее не будет проблем из-за того, что она снимает все на камеру. )"
    hide player
    with dissolve
    $ renpy.end_replay()
    return

label webcam_menu_2:
    label webcam_menu_3:
        label webcam_menu_4:
            scene blank
    menu:
        "Электро Клитор.":
            jump expression game.dialog_select("electroclit_replay")

        "Ультравибратор 2000." if store._in_replay in ["webcam_menu_2", "webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("ultravibrator_replay")

        "Двойной Вибратор." if store._in_replay in ["webcam_menu_3", "webcam_menu_4"]:
            jump expression game.dialog_select("dualsybian_replay")

        "Плохой Монстр." if store._in_replay == "webcam_menu_4":
            jump expression game.dialog_select("badmonster_replay")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
