label lair_aqua_lair:
    scene location_lair_blur
    show player 25
    player_name "*кашель* О, нет... Я думал что сделал это."
    show player 113
    pause
    show player 10
    player_name "Это место довольно жуткое!"
    player_name "Похоже на то, как рисуют в комиксах."
    show player 113
    player_name "... или одна из игр {b}Эрика{/b}."
    show player 10
    player_name "..."
    show player 12
    player_name "... Но эта странная рыба-дама должна быть где-то здесь!"
    player_name "Если она решила позаимствовать мою приманку, надо её мнение поменять!"
    show player 16
    hide player with dissolve
    return

label seasucc_dialogue:
    scene lair_seasucc
    if M_aqua.is_state(S_aqua_seasucc_intro):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_intro")
        $ M_aqua.trigger(T_aqua_seasucc)

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and not player.has_item("mushroom"):
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_no_mushroom")

    elif M_aqua.is_state(S_aqua_seasucc_mushroom) and player.has_item("mushroom"):
        $ player.remove_item("mushroom")
        call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_intro")
        jump expression game.dialog_select("seasucc_loop")
    else:

        label aqua_succ_replay:
            call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro")
        if not store._in_replay == None:
            jump expression game.dialog_select("succ_replay_jump")
        menu:
            "Да.":
                label succ_replay_jump:
                    call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes")
                jump expression game.dialog_select("seasucc_loop")
            "Нет.":

                call expression game.dialog_select("seasucc_dialogue_aqua_seasucc_mushroom_repeat_no")
    hide aqua
    hide player
    hide player_boner
    hide seasucc
    hide seasucc_bg_01
    hide seasucc_bg_02
    with dissolve
    $ game.main()

label seasucc_dialogue_aqua_seasucc_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02
    show seasucc 1
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Аква{/b}?"
    show player 5
    show aqua 20
    aqua "Даааа..."
    show aqua 19
    show player 10
    player_name "Что это за странная вещь?"
    show player 5
    show aqua 20
    aqua "Это не вещь. Это {b}Ммморесос{/b}!"
    show aqua 19
    show player 12
    player_name "Хмм. И что делает этот {b}Моресос{/b}?"
    show player 5
    show aqua 20
    aqua "Это испооользовалось чтобы предоставлять удовольствия."
    show aqua 19
    show player 12
    player_name "Для получения удовольствия?"
    show player 5
    show aqua 20
    aqua "Дааа. Это доставляет всем друзьям наслаждение."
    show aqua 19
    show player 10
    player_name "Значит {b}МореСос{/b} и мне доставит удовольствие?"
    show player 5
    show aqua 20
    aqua "Дааа, если ты с ним подружишься."
    show aqua 19
    show player 10
    player_name "Как я могу подружиться со стулом?"
    show player 5
    show aqua 20
    aqua "Тебе нужно будет накормить его специальной едой, {b}Falicum Грибами{/b}. {b}Falicum{/b}."
    show aqua 19
    show player 12
    player_name "Кормить его? Странно..."
    player_name "Но я, до сих пор ничего не слышал о {b}Синих Мухоморах{/b}."
    show player 10
    player_name "Где мне найти их?"
    show player 5
    show aqua 20
    aqua "Оно растет на суше. {b}Глубоко в лесу{/b}. Опасно для {b}Аквы{/b}."
    show aqua 19
    show player 12
    player_name "Хмм, в {b}Лесу{/b}?"
    show player 14
    player_name "Ну ладно, попробую поискать."
    show player 13
    show aqua 20
    aqua "Дааа. Достань {b}Falicum{/b}. Подружись с {b}МореСосом{/b}."
    aqua "Тогда мы получим полное наслаждение."
    return

label seasucc_dialogue_aqua_seasucc_no_mushroom:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 12 zorder 3 at left
    with dissolve
    player_name "Что ты сказала нужно {b}МореСосу{/b}?"
    show player 5
    show aqua 20
    aqua "Тебе нужно будет накормить его специальной едой, {b}Falicum Грибами{/b}. {b}Falicum{/b}."
    show aqua 19
    show player 10
    player_name "Где я могу их найти?"
    show player 5
    show aqua 20
    aqua "Они растут на суше. {b}Глубоко в лесу{/b}. Опасно для {b}Аквы{/b}."
    show aqua 19
    show player 14
    player_name "Ладно, попробую найти."
    return

label seasucc_dialogue_aqua_seasucc_mushroom_intro:
    show aqua 19
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 14 zorder 3 at left
    with dissolve
    player_name "{b}Аква{/b}!"
    player_name "Я кое что нашёл."
    show player 239_240 with dissolve
    player_name "..."
    show player 500 with dissolve
    player_name "Видишь?"
    show player 499
    show aqua 20
    aqua "{b}Falicum{/b}! Дааа."
    show aqua 19
    show player 500
    player_name "Это то что надо {b}Моресосу{/b}?"
    show player 499
    show aqua 20
    aqua "Дааа. Скорми {b}Моресосу{/b}. Подружись!"
    aqua "Сяятть... И Скорми {b}Falicum{/b}."
    show aqua 19
    show player 10 with dissolve
    player_name "Ладно..."
    hide player
    show player seasucc 1 zorder 3 with dissolve
    pause
    show aqua 21
    show player seasucc 5 zorder 0
    show player_pants seasucc 2 zorder 0
    with dissolve
    pause
    show player seasucc 6 with dissolve
    pause
    show player seasucc 9 with dissolve
    player_name "Ну вот, {b}МореСос{/b}."
    show seasucc 2 with dissolve
    show player seasucc 8
    player_name "..."
    show seasucc 3
    show player seasucc 10
    with dissolve
    player_name "!!!" with hpunch
    show seasucc 4
    show player seasucc 5
    with dissolve
    show aqua 22
    aqua "Мммм, {b}Моресосу{/b} нравится {b}Falicum{/b}."
    show aqua 21
    show seasucc 1
    show player seasucc 7
    with dissolve
    player_name "Похоже ты и вправду голоден!"
    show player seasucc 3 with dissolve
    show aqua 22
    aqua "Ты попробуй {b}Моресоса{/b} сейчас. Дааа?"
    show aqua 21
    show player seasucc 7 with dissolve
    player_name "Ухх..."
    show player seasucc 5 with dissolve
    show aqua 22
    aqua "Не волнуйся. Покажжи {b}Моресосу{/b} большого угря."
    show aqua 21
    show player seasucc 6 with dissolve
    player_name "..."
    show player seasucc 7
    player_name "Хорошо..."
    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ахх, доброе утро большой змей."
    show aqua 21
    show seasucc 5
    show player seasucc 7
    with dissolve
    player_name "Ты уверена что-"
    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Вау!"
    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "Это... потрясающе!!"
    show player seasucc 14
    show aqua 23
    aqua "Дааа. Отличное удовольствие! {b}Моресосу{/b} хорошо!"
    show aqua 24
    pause
    return

label seasucc_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                $ animated = True
            pause 4
            call expression game.dialog_select("seasucc_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [8,"8b","8c","8d","8e","8f","8g","8h","8i"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "seasucc {}".format(pose_list[pose_counter]) as seasucc at Position(xalign = 0.35, yalign = 0.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("seasucc_hscene_dialog")
        $ animcounter += 1
    call screen seasucc_options

label seasucc_hscene_dialog:
    if animcounter == 0:
        show player seasucc 13
        if randomizer() <= 50:
            player_name "Охх...{p=1}{nw}"
        else:
            player_name "Ухх!{p=1}{nw}"
        show player seasucc 14
    elif animcounter == 2 and randomizer() <= 50:
        show aqua 23
        aqua "Сссоси {b}SsseaSucc{/b}!{p=2}{nw}"
        show aqua 24

    elif animcounter == 3 and randomizer() <= 50:
        show player seasucc 13
        pause 2
        show player seasucc 14
    return

label seasucc_cum:
    call expression game.dialog_select("seasucc_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["02_unlocked"] = True
    $ game.timer.tick()
    $ M_aqua.trigger(T_aqua_seasucc_fuck)
    $ game.main()

label seasucc_cum_pre:
    show player seasucc 13
    show aqua 23
    aqua "Дай {b}Моресосу{/b} семена."
    aqua "Кончи для {b}Моресоса{/b}!!!"
    show aqua 24
    pause
    hide player
    hide seasucc
    show seasucc 9 zorder 0
    with flash
    pause
    show seasucc 3
    show player seasucc 14 zorder 0
    show player_boner seasucc 15 zorder 0
    with dissolve
    pause
    show seasucc 4 with dissolve
    pause
    show seasucc 1 with dissolve
    show player seasucc 3
    show aqua 25
    if M_aqua.is_state(S_aqua_seasucc_mushroom):
        aqua "Теперь когда {b}Моресос{/b} попробовал твоё сссемя, он запомнит."
        aqua "Вы теперь друзья!"
        aqua "Теперь он будет доставлять удовольстие всегда."
        show popup_seasucc at truecenter with dissolve
        pause
        hide popup_seasucc with dissolve
    else:

        aqua "{b}Моресосу{/b} нравятся твои сссемена!"
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_intro:
    scene lair_seasucc
    show aqua 20
    show seasucc_bg_01
    show seasucc_bg_02 zorder 1
    show seasucc 1 zorder 2
    show player 13 zorder 3 at left
    with dissolve
    aqua "Вернешься за добавввкой?"
    show aqua 19
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_yes:
    show player 4 with dissolve
    player_name "..."
    show player 26 with dissolve
    player_name "Да."
    show player 13
    show aqua 20
    aqua "{b}Моресос{/b} этто хорошо!"
    aqua "Сядь... И скорми {b}Моресосу{/b}."
    show aqua 19
    hide player
    show player seasucc 1 zorder 3 with dissolve
    pause
    show aqua 21
    show player seasucc 5 zorder 0
    show player_pants seasucc 2 zorder 0
    with dissolve
    pause
    show aqua 22
    aqua "Ппокажи {b}Моресосу{/b} большого угря."
    show aqua 21
    hide player_pants
    show player seasucc 11 with dissolve
    pause
    show player seasucc 3
    show player_boner seasucc 2b
    with dissolve
    show aqua 25
    aqua "Ахх, доброе утро большой змей. "
    show aqua 21
    show seasucc 5
    with dissolve
    show aqua 24
    show player seasucc 5
    show seasucc 6
    with dissolve
    pause
    show seasucc 7 with dissolve
    player_name "!!!"
    hide player_boner
    show seasucc 8 at Position(xalign = 0.35, yalign = 0.0)
    with dissolve
    pause
    show seasucc 8b
    pause
    show seasucc 8c
    pause
    show seasucc 8d
    pause
    show seasucc 8e
    show player seasucc 12
    player_name "Вау!"
    $ M_aqua.set("sex speed", 0.175)
    show expression AnimatedImage("seasucc", [8,"8b","8c","8d","8e","8f","8g","8h","8i"], M_aqua) as seasucc at Position(xalign = 0.35, yalign = 0.0)
    pause
    pause
    show player seasucc 13
    player_name "Эта штука чувствует себя... великолепно!!"
    show player seasucc 14
    show aqua 23
    aqua "Дааа. Наилучшее удовольствие! {b}Моресосу{/b} хорошо!"
    show aqua 24
    return

label seasucc_dialogue_aqua_seasucc_mushroom_repeat_no:
    show player 14
    player_name "Не сейчас, может как нибудь позже."
    return

label aqua_lure_steal:
    call expression game.dialog_select("aqua_lure_steal_pre")
    $ player.remove_item("special_lure")
    $ M_aqua.trigger(T_aqua_lure_steal)
    label follow_aqua:
        call expression game.dialog_select("aqua_lure_steal_after")
    menu:
        "Ныряй!":
            call expression game.dialog_select("aqua_lure_steal_dive_pre")
            $ playSound()
            call expression game.dialog_select("aqua_lure_steal_dive_after")
            $ M_aqua.trigger(T_aqua_dive)
            if game.cheat_mode:
                menu:
                    "Пропустить Мини-Игру (Чит).":
                        jump expression game.dialog_select("squid_attack")
                    "Играть В Мини-Игру.":

                        $ pass

            call screen squid_fight
        "Ещё нет.":

            call expression game.dialog_select("aqua_lure_steal_not_yet")
    $ game.main()

label aqua_lure_steal_pre:
    scene location_pier_dock_cutscene
    with fade
    show text "Что ж это перешло черту, мое сердце отстановилось. Я думаю что моя приманка потерялась..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...Но вдруг, нечто нарушило поверхность воды!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...Или лучше сказать, кто-то..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_pier_minigame06b
    show player 472 at Position(xpos=0.715,ypos=.9425)
    show aqua 16 at Position (xpos=0.4175,ypos=1.0)
    aqua "Блестяшка..."
    show player 473
    show aqua 15
    player_name "!!!"
    player_name "Т-Ты кто?!"
    show player 472
    show aqua 18
    aqua "Я? Я Аква. Что ты?"
    show player 473
    show aqua 17
    player_name "Хм?"
    show player 472
    show aqua 18
    aqua "Я Аква. Это ты человек которы крадет всю Аквину рыбу?!"
    show player 473
    show aqua 17
    player_name "Рыбу?"
    show player 472
    show aqua 16b
    aqua "Дааа, рыбу! Ты используешь Блестяшку что бы украсть мою рыбу!"
    show player 473
    show aqua 15b
    player_name "Что? Нет, я только эмм... 'Блестяшка?'"
    player_name "Это мне дал {b}Капитан Терри{/b}."
    show player 472
    show aqua 16b
    aqua "Капитан Терри?"
    show player 473
    show aqua 15b
    player_name "Да, {b}Капитан Терри{/b}."
    show player 472
    show aqua 16
    aqua "Хмм... Не увверен что ты говоришь правду."
    show aqua 16b
    aqua "Неважно, блестяшка теперь моя!"
    show player 474
    show aqua 17
    player_name "Подожди! Пожалуйста, я тяжёлым трудом достал её!"
    show player 475
    show aqua 16b
    aqua "Очень жаль. Она вам нужна? {b}Иди и забери её{/b}!!!"
    hide aqua with dissolve
    show player 474
    player_name "Эй!!"

    show player 476
    player_name "Бля!"
    player_name "..."
    show popup_lure2 at truecenter with dissolve
    pause
    hide popup_lure2 with dissolve
    return

label aqua_lure_steal_after:
    player_name "!!!"
    player_name "( Черт! Я должен буду идти за ней, если я хочу вернуть приманку. )"
    player_name "( ... Это может быть опасно, хотя. )"
    player_name "( Нужно лучше удостовериться что Я сначала готов. )"
    return

label aqua_lure_steal_dive_pre:
    player_name "К черту все! Я слишком тяжело работал ради этой особенной приманки."
    player_name "Я не могу её так упустить!"
    show player 477
    return

label aqua_lure_steal_dive_after:
    scene location_lair_dive
    with fade
    show text "Надо направляться прямиком за ней..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... нырять головой в перед в темно-синюю воду." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я решил получить мою приманку назад!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_lair_ocean_look
    player_name "( Она должна быть где то здесь. )"
    player_name "..."
    player_name "( Гррр... Куда она смылась?! )"

    scene location_lair_ocean_prefight
    player_name "( !!! )" with hpunch
    player_name "( Что за- !! )"
    player_name "( Гиганский кальмар!?! )"

    scene versus_squid with vpunch
    $ renpy.pause(1.0, hard = True)
    return

label aqua_lure_steal_not_yet:
    show player 476b
    player_name "( Неа... Я не буду нырять за ней. )"
    player_name "( Не знаю что меня там ждёт. )"
    player_name "( Возможно позже... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
