label shooting_range_dialogue:
    if M_roxxy.finished_state(S_roxxy_beat_clyde) and L_trailer_tractor.is_here(M_clyde):
        show player 14f at right
        player_name "Хочешь попасть в зону поражения?"
        show player 13f
        show clyde 4 at left
        clyde "Пшш, вы знаете, что я делаю!"
        clyde "Я всегда в настроении выпить пива и пострелять!"
        show clyde 9 with dissolve
        clyde "Хочешь, чтобы было интересно?"
        show clyde 3 with dissolve
        menu:
            "$100." if player.has_money(100):
                show clyde 4
                clyde "Нет проблем, братан!"
                clyde "Приготовь бумажник, сейчас же!"
                clyde "Вооу!"
                show clyde 8 with dissolve
                $ player.spend_money(100)
                $ player.earnings = 100
                jump shooting_minigame_prepare
            "$200." if player.has_money(200):
                show clyde 4
                clyde "Нет проблем, братан!"
                clyde "Приготовь бумажник, сейчас же!"
                clyde "Вооу!"
                show clyde 8 with dissolve
                $ player.spend_money(200)
                $ player.earnings = 200
                jump shooting_minigame_prepare
            "$400." if player.has_money(400):
                show clyde 4
                clyde "Ох, у нас тут большой транжира!"
                clyde "Берегитесь, дамы {b}[firstname]{/b} вспыхивает и смотрит действие ФЕР!"
                show clyde 3
                show player 14f
                if M_clyde.get("cletus"):
                    player_name "Хех, заткнись и стреляй, {b}Клетус{/b}!"
                else:
                    player_name "Хех, заткнись и стреляй, {b}Клайд{/b}!"
                show player 13f
                show clyde 4
                clyde "Хахаха, ты справишься, брат!"
                show clyde 8 with dissolve
                $ player.spend_money(400)
                $ player.earnings = 400
                jump shooting_minigame_prepare
            "Неважно.":
                show player 12f
                player_name "Вообще-то, забудь."
                show player 10f
                player_name "Может в другой раз?"
                show player 5f
                show clyde 4
                clyde "Пшш, черт возьми!"
                clyde "Ты знаешь, где меня найти."
                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ game.main()
    else:
        $ pass
    $ game.main()

label shooting_minigame_prepare:
    $ game.failed_minigame_counter = 0
    if not game.cheat_mode:
        if not renpy.variant("mobile"):
            $ config.mouse = {"default": [("buttons/shooting_cursor.png", 48, 49)]}
        call screen shooting_minigame
    else:
        menu:
            "Играть в мини-игру.":
                if not renpy.variant("mobile"):
                    $ config.mouse = {"default": [("buttons/shooting_cursor.png", 48, 49)]}
                call screen shooting_minigame
            "Пропустить мини-игру (чит).":
                $ M_roxxy.set("lost shooting", True)
                jump shooting_range_success


label shooting_range_fail:
    $ config.mouse = None
    $ game.failed_minigame_counter += 1
    if M_roxxy.is_state(S_roxxy_beat_clyde):
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("shooting_range_fail_repeat")
        else:
            call expression game.dialog_select("shooting_range_fail_first")
            $ M_roxxy.set("lost shooting", True)
        if game.failed_minigame_counter <=3:
            jump shooting_minigame_prepare
        else:
            menu:
                "Повторить.":
                    jump shooting_minigame_prepare
                "Пропустить.":
                    jump shooting_range_success
    elif player.earnings != 0:
        show player 5f at right
        show clyde 4 at left
        if M_clyde.get("cletus"):
            show clyde_hat at left
        with dissolve
        clyde "Не повезло, брат...."
        if M_clyde.get("cletus"):
            clyde "... Но вы должны были знать лучше, чем проверять свою мощь против {b}Клетуса Дельмонта{/b}!!!"
        else:
            clyde "... Но вы должны были знать лучше, чем проверить свою мощь против  {b}Клетуса Дельмонта{/b}!!!"
        clyde "Хахаха, теперь плати!"
        show clyde 3
        show player 174bf with dissolve
        player_name "..."
        show player 5f with dissolve
        show clyde 4
        clyde "Хочешь еще раз?"
        show clyde 3
        menu:
            "Да.":
                show player 14f
                if M_clyde.get("cletus"):
                    player_name "Ты идешь вниз, {b}Клетус.{/b}!"
                else:
                    player_name " Ты пойдешь ко дну, {b}Клайд{/b}!"
                show player 13f
                show clyde 4
                clyde "Хех, это будет самые легкие деньги, которые я когда-либо делал!"
                show clyde 3
                jump shooting_range_dialogue
            "Нет.":
                show player 12f
                player_name "Нет. Может, как-нибудь в другой раз."
                show player 5f
                show clyde 4
                clyde "Хех, бросаешь полотенце, да?!"
                clyde "Может, в следующий раз мы пропустим стрельбу и ты просто дашь мне свои деньги..."
                show clyde 9 with dissolve
                clyde "Что скажешь?"
                show clyde 3 with dissolve
                show player 12f
                if M_clyde.get("cletus"):
                    player_name "Заткнись, {b}Клетус{/b}."
                else:
                    player_name "Заткнись, {b}Клайд{/b}."
                show player 90f
                show clyde 4
                clyde "Ахахаха!"
                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ game.main()
    $ game.main()

label shooting_range_success:
    $ config.mouse = None
    if M_roxxy.is_state(S_roxxy_beat_clyde):
        if M_roxxy.get("lost shooting"):
            call expression game.dialog_select("shooting_range_success_failed")
        else:
            call expression game.dialog_select("shooting_range_success_first")
        call expression game.dialog_select("shooting_range_success_outro")
        $ game.timer.tick()
        $ M_roxxy.trigger(T_roxxy_beaten_clyde)
    elif player.earnings != 0:
        show player 91f at right
        show clyde 26 at left
        if M_clyde.get("cletus"):
            show clyde_hat at left
        with dissolve
        clyde "Чёрт побери!"
        clyde "Ты же мне изменяешь!"
        clyde "Я просто знаю это..."
        show clyde 25
        show player 92f
        player_name "Да."
        if M_clyde.get("cletus"):
            player_name "Плати, {b}Клетус{/b}."
        else:
            player_name "Плати, {b}Клайд{/b}."
        show player 91f
        show clyde 22
        clyde "{b}*ох*{/b}"
        show clyde 16 at Position (xoffset=96) with dissolve

        pause
        show clyde 22 with dissolve
        clyde "Как насчет повторить?!"
        show clyde 21
        menu:
            "Да.":
                show clyde 4 with dissolve
                clyde "Черт, да!"
                show clyde 26 with dissolve
                clyde "На этот раз ты идешь ко дну, брат!"
                show clyde 3 with dissolve
                $ player.get_money(player.earnings * 2)
                jump shooting_range_dialogue

            "Двойной или ничего!" if random.randint(1, 100) <= 10:
                show clyde 4 with dissolve
                clyde "Двойная ставка или ничего? Запишите меня!"
                show clyde 26 with dissolve
                clyde "На этот раз ты идешь ко дну, брат!"
                show clyde 3 with dissolve
                $ player.earnings *= 2
                jump shooting_minigame_prepare
            "Нет.":

                show clyde 26
                clyde "Ты даже не дашь мне шанс отыграть бабки обратно?!"
                clyde "Пшш, Дат перепутал!"
                show clyde 25
                show player 92f
                if M_clyde.get("cletus"):
                    player_name "Удачи в следующий раз, {b}Клетус{/b}..."
                else:
                    player_name "Удачи в следующий раз, {b}Клайд{/b}..."
                show player 91f
                show clyde 22
                clyde "{b}*Эх*{/b} Да, да..."
                clyde "Не тратьте все деньги в одном месте!"
                hide player
                hide clyde
                hide clyde_hat
                with dissolve
                $ player.get_money(player.earnings * 2)
                $ game.main()
    $ game.main()

label shooting_range_fail_first:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 5 at Position (xpos=500)
    show clyde 3 at left
    show roxxy 3c at right
    with dissolve
    rox "Ты издеваешься надо мной?!"
    show roxxy 3b
    show player 10
    player_name "Прости, {b}Рокси{/b}..."
    show player 5
    show clyde 9 with dissolve
    clyde "Черт, да! Давайте посмотрим на эти красивые вещи!"
    show clyde 3 with dissolve
    show roxxy 3c
    rox "Я думала, ты сказал, что ты хороший стрелок?!"
    show roxxy 3d
    show player 10
    player_name "... Ну, я не привык пользоваться этой винтовкой!"
    show player 5
    show roxxy 30
    rox "Тьфу... Я не хочу этого делать!"
    show roxxy 29
    show clyde 2 with dissolve
    clyde "Эй! Ты обещал мне пять секунд!"
    clyde "Сделка, сделка и ты проиграл!"
    show clyde 4 with dissolve
    clyde "Так что выкинь их, девчонка!"
    show clyde 3
    rox "..."
    show roxxy 3
    rox "... Боже, я никогда не прощу тебя за это {b}[firstname]{/b}..."
    show roxxy 51
    show roxxy_head 55c at right
    with dissolve
    pause
    show roxxy 52 with dissolve
    pause
    show roxxy 53 with dissolve
    show player 109f
    pause
    show roxxy 54 with dissolve
    pause
    hide roxxy_head
    show roxxy 56c
    with dissolve
    show clyde 4
    clyde "Господи Иисусе!"
    clyde "Это самая нужная вещь, которую я когда-либо видел!"
    show clyde 18 with dissolve
    show roxxy 56b
    rox "О мой бог."
    show roxxy 51
    show roxxy_head 55c at right
    with dissolve
    show player 5
    pause
    hide roxxy_head
    show roxxy 31
    with dissolve
    rox "Это просто отвратительно, {b}Клайд{/b}!"
    show roxxy 3b
    show player 109 with dissolve
    show clyde 20
    clyde "Это не мач вина! Дем сладкие олухи Дун его!"
    show player 22f at Position (xpos=600) with dissolve
    show clyde 19
    show roxxy 3
    rox "Я чувствую, что мне нужно принять душ сейчас..."
    show roxxy 3d
    show clyde 20
    clyde "Я счастливее, чем дятел на лесопилке!"
    show clyde 19
    show roxxy 3c
    rox "Могу я получить свою униформу сейчас?"
    show roxxy 3d
    show clyde 20
    clyde "Нет, я так не думаю."
    clyde "А теперь, будьте добры, убирайтесь отсюда."
    clyde "Мне надо немного практики!"
    show clyde 19
    rox "..."
    show player 12f
    player_name "Двойной или ничего!"
    show player 90f
    show roxxy 2c
    rox "ЧТО?!"
    show roxxy 2b
    show player 12f
    player_name "Двойной или ничего!"
    player_name "Если я выиграю, мы получим {b}униформу{/b}!"
    show player 90f
    show clyde 20
    clyde "... А когда я выиграю?"
    show clyde 19
    show player 12f
    player_name "Рокси позолит посмотреть на свои сиськи 10 секунд."
    show player 114f
    show roxxy 31
    rox "ЧТО БЫ ДЛЯТЬ ДЕЛАЕШЬ, {b}[firstname]{/b}?!"
    show roxxy 3b
    show player 113f
    player_name "Он уже видел их ..."
    show player 5f
    show clyde 20
    clyde "Мне нравится твой стиль, {b}[firstname]{/b}!"
    clyde "Я согласен."
    show clyde 19
    show roxxy 3
    rox "... Вы оба засранцы!"
    show roxxy 3d
    show player 113f
    player_name "Я не буду проигрывать дважды."
    show player 114f
    show roxxy 30
    rox "... Тьфу, что?"
    hide roxxy
    hide player
    hide clyde
    with dissolve
    return

label shooting_range_fail_repeat:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 5 at Position (xpos=500)
    show clyde 3 at left
    show roxxy 51 at right
    show roxxy_head 55c at right
    with dissolve
    pause
    show roxxy 52 with dissolve
    pause
    show roxxy 53 with dissolve
    show player 109f
    pause
    show roxxy 54 with dissolve
    pause
    hide roxxy_head
    show roxxy 56c
    show clyde 20
    with dissolve
    clyde "Лучший. День!"
    show clyde 19
    player_name "..."
    show clyde 20
    clyde "Клянусь, я могу ослепнуть прямо сейчас, и мне будет все равно!"
    show clyde 19
    show roxxy 51
    show roxxy_head 55c at right
    with dissolve
    show player 5
    pause
    hide roxxy_head
    show roxxy 3
    with dissolve
    rox "Миллиона душей будет недостаточно, чтобы смыть это..."
    show roxxy 3d
    show player 10
    player_name "... Прости, {b}Рокси{/b}."
    show player 5
    show roxxy 3
    rox "Я не собираюсь забывать это, {b}[firstname]{/b}!"
    show roxxy 3d
    show clyde 20
    show player 114
    clyde "Я тоже!"
    show roxxy 14
    clyde "Ахахаха."
    show clyde 19
    show roxxy 3c
    show player 5
    rox "О, Боже..."
    show roxxy 3d
    show player 114
    show clyde 20
    clyde "Мы идем снова?"
    show roxxy 2b
    clyde "Двойной или ничего!"
    show clyde 19
    show player 113
    player_name "Да!"
    hide roxxy
    hide player
    hide clyde
    with dissolve
    return

label shooting_range_success_failed:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 13f at Position (xpos=600)
    show roxxy 1 at right
    show clyde 4 at left
    with dissolve
    clyde "Чёрт!!!!!"
    clyde "Наконец-то ты меня раскусила!"
    show clyde 3
    show roxxy 3c
    rox "Сейчас самое подходящее время!"
    show roxxy 3d
    return

label shooting_range_success_first:
    scene expression "backgrounds/location_trailer_tractor_day_blur.jpg"
    show player 13f at Position (xpos=600)
    show roxxy 1 at right
    show clyde 4 at left
    with dissolve
    clyde "Черт!"
    clyde "Хорошо стреляешь!"
    show clyde 3
    show roxxy 4
    rox "О, слава Богу!"
    show roxxy 2
    rox "Я в долгу перед тобой за это, {b}[firstname]{/b}!"
    show roxxy 1
    return

label shooting_range_success_outro:
    show clyde 4
    clyde "Думаю, я должен заплатить сейчас..."
    show roxxy 1
    show clyde 7 with dissolve
    show player 110
    clyde "Прости, девочка."
    clyde "Я найду тебе что-нибудь другое, чтобы-"
    show clyde 5b
    pig "{b}Хрю{/b}!"
    clyde "!!!"
    show clyde 2 with dissolve
    show player 11f
    clyde "Теперь вы дун гон и сделал мах, собака убежала!"
    show clyde 1
    show player 114f
    show roxxy 3c
    rox "Ты можешь быть серьезным!"
    rox "Это моя {b}униформа{/b}!"
    show roxxy 3d
    show player 5f
    show clyde 2
    clyde "Я говорил тебе, что она будет склонна отдать ее обратно..."
    clyde "Не волнуйся... Она, наверное, просто побежала домой..."
    show clyde 1
    show player 12f
    player_name "Я достану ее."
    show player 5f
    show clyde 2
    clyde "Ну, тебе лучше быть осторожнее..."
    clyde "Моя собака не особо любит незнакомцев."
    show clyde 1
    show player 14f
    player_name "Хех, со мной все будет хорошо."
    player_name "Я хорошо лажу с животными."
    show player 13f
    show clyde 2
    clyde "Как насчет дэт."
    show clyde 9 with dissolve
    clyde "Доктор Дулиттл датин йер!"
    show clyde 3 with dissolve
    show roxxy 3c
    show player 114f
    rox "Мы не будем встречаться!"
    show roxxy 3b
    show player 5f
    show clyde 4
    clyde "Хех, как скажешь, {b}Роксианна{/b}."
    clyde "Просто убедись, что твой новый парень не будет стрелять на ярмарке в этом году!"
    clyde "Этот чучело ничего не умеет, слышишь?!"
    show clyde 3
    show player 14f
    player_name "Нет, проблем."
    show player 114f
    show roxxy 3c
    rox "Сколько раз я должна повторять, что он не мой парень?!"
    show roxxy 31
    rox "... И не называй меня {b}Роксианна{/b}!"
    show roxxy 3d
    show player 5f
    show clyde 4
    clyde "Как скажешь, сестренка..."
    show clyde 8 with dissolve
    pause
    hide clyde with dissolve
    show roxxy 3
    rox "... Не могу поверить, что я родственница этого придурка!"
    show roxxy 3d
    show player 113f
    player_name "Он, безусловно, красочный парень..."
    show player 114f
    show roxxy 3c
    rox "Давай найдем эту глупую свинью."
    show roxxy 3d
    show player 113f
    player_name "Конечно."
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
