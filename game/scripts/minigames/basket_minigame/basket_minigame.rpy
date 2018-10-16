label basketball_minigame_prepare:
    if M_roxxy.get("basketball unlocked"):
        if game.cheat_mode:
            menu:
                "Пропустить (Cheat)":
                    jump basketball_success
                "Играть":

                    call screen basketball_minigame
        else:

            call screen basketball_minigame
    else:

        scene expression L_basketball_court.background_blur
        show player 16 at left
        show dexter 4 at right
        dex "Как ты думаешь, что ты делаешь?!"
        dex "Этот корт для мужчин, а не для худеньких неудачников!"
        show dexter 6
        dex "Убирайся!"
        player_name "( Гррр, он такой засранец! )"
        player_name "( Однажды он получит по заслугам... )"
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_success:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        scene expression "backgrounds/location_basketball_cutscene02.jpg"
        with fade
        show text "Я жжег!\nНарезая круги вокруг {b}Декстера{/b}..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Ударял по мячу и забивал тройные, прежде чем он мог сделать хотя бы шаг." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve
        scene expression "backgrounds/location_basketball_cutscene03.jpg"
        with fade
        show text "... А потом это случилось." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Я сделал обманное движение влево, потом вправо, а потом пронеся мимо него!\n{b}Декстер{/b} хрюкнюл, спотыкаясь о собственные ноги и рухнул на землю." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Я понятия не имею, как ему удалось потерять штаны..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        hide text
        with dissolve
        scene basketball_b
        show chad 5f at Position (xpos=500)
        show tyrone 2f at Position (xpos=300)
        show dexter 43b at right
        show kevin 35f at left
        with dissolve
        tyrone "Вот дерьмо!"
        tyrone "{b}[firstname]{/b} просто подколол этого дурака так сильно, что его штаны спали!"
        show tyrone 1f
        show chad 6f
        chad "Это было круто, йоу!"
        show chad 5f
        show kevin 36f with dissolve
        kev "... Это что за хрень?"
        show chad 12f
        chad "Хах?"
        show tyrone 9f
        kev "Что это?!"
        tyrone "... Это его член?!"
        show tyrone 10f with dissolve
        show dexter 43
        kev "Не знаю, братан,не могу сказать..."
        show kevin 36bf
        kev "... Кто-нибудь принес лупу?!"
        show chad 13f
        chad "Хахахаха! Он похоже на пупок!"
        show tyrone 3f
        tyrone "Хахаха, да! С двумя маленькими орешками, свисающими с него!"
        show tyrone 1f
        show chad 1f
        show dexter 43c
        dex "Заткнитесь!"
        show dexter 43b with hpunch
        show kevin 32f with dissolve
        kev "Хахаха, у {b}Декстера{/b} крошечный пенис!"
        bri "Хорошо, хватит!"
        hide kevin
        hide chad
        hide tyrone
        with dissolve
        tyrone "Он меньше, чем крошечный, чувак..."
        tyrone "Это прямо победитель микропенисов!"
        show coach 2f at Position (xpos=400) with dissolve
        bri "Что за суматоха-"
        show coach 18f with dissolve
        bri "!!!"
        show dexter 44 with dissolve
        dex "!!!"
        bri "..."
        show dexter 44c
        dex "Хватит смеятся!"
        dex "Разве ты не знаешь, кто я?!"
        dex "Никто не смеется надо мной!"
        show dexter 45
        show player 649 at left with dissolve
        player_name "Эй, {b}Дехтер{/b}..."
        player_name "Твой мяч, сучка!"
        show player 664
        show dexter 45b
        with dissolve
        pause
        show player 91
        show coach 19f with dissolve
        bri "ПФФФ, ХАХАХАХАХА!"
        hide coach
        show dexter 45c
        dex "ГРР, ПОШЛИ ВЫ ВСЕ НА ХЕР!" with hpunch
        show player 11
        dex "{b}[firstname]{/b},ты-покойник!"
        dex "ТЫ СЛЫШИШЬ МЕНЯ?!" with hpunch
        dex "ПОКОЙНИК!"
        show dexter 46 with dissolve
        pause 1
        hide dexter with dissolve
        pause
        show kevin 32 at Position (xpos=700)
        show erik 1 at right
        with dissolve
        kev "Йоу, {b}Декстер{/b}! Ты забыл свои штаны, братан!!"
        kev "Хахаха!"
        eri "..."
        kev "{b}[firstname]{/b} это было самое смешное, что я когда-либо видел!"
        show kevin 23
        show player 14
        player_name "А, да?"
        show player 13
        show kevin 9b
        kev "Точно, братан!"
        show kevin 23
        show erik 5
        eri "... Он был такой крошечной."
        show erik 1
        show kevin 32
        kev "Хахаха, точно!"
        kev "О боже мой! Эта новость распространится как лесной пожар!"
        show kevin 23
        show player 12
        player_name "... Ага."
        player_name "{b}*вздыхая*{/b} Теперь этого не избежать."
        show player 5
        show erik 5
        eri "Что ты имеешь в виду?"
        show erik 52
        show player 10
        player_name "{b}Декстер{/b} после этого захочет крови..."
        player_name "В следующий раз мне придется сразиться с ним."
        show player 5
        show erik 5
        eri "Да, я думаю, что ты прав."
        show erik 52
        show kevin 24
        kev "{b}Тебе лучше пойти в спортзал и подготовиться.{/b}"
        show kevin 23
        show player 12
        player_name "Это действительно хорошая идея."
        show player 5
        show kevin 24
        kev "Дай мне знать, если тебе понадобится помощь, хорошо?"
        show kevin 23
        show player 14
        player_name "Спасибо, {b}Кэвин{/b}."
        show player 13
        show kevin 24
        kev "Без проблем, братан."
        hide kevin with dissolve
        show erik 5
        eri "... Давай, пойдем в душ."
        show erik 3
        eri "Я думаю, мне нужно сменить штаны после всего этого!"
        show erik 2 with dissolve
        show player 17
        player_name "Ха-ха, я прямо за тобой."
        hide player
        hide erik
        with dissolve
        show expression "boxes/popup_basketball_minigame.png" at truecenter with dissolve
        pause
        hide expression "boxes/popup_basketball_minigame.png" with dissolve
        $ M_roxxy.trigger(T_roxxy_humiliated_dexter)
        $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "Это было не так уж плохо... Наверное, мне стоит потренироваться, чтобы стать еще лучше."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()

label basketball_fail:
    if M_roxxy.is_state(S_roxxy_basketball_challenge) and (game.timer.is_afternoon() or not M_roxxy.is_set("done basketball")):
        if M_roxxy.get("done basketball"):
            scene basketball_b
            show coach 1f at Position (xpos=400)
            show player 24 at left
            show dexter 32 at right
            with dissolve
            dex "Да, именно так, маленькая сучка!"
            dex "Ты не можешь тусоваться с {b}Декстером{/b}!"
            dex "{b}Рокси{/b} должно быть стыдно целоваться с таким неудачником, как ты!"
            show dexter 31
            player_name "..."
            show dexter 32
            dex "Хахахахахаха!"
            show dexter 31
            show coach 2f
            bri "Хорошо, этого достаточно."
            show dexter 29 with dissolve
            bri "{b}Декстер{/b} ты нарушал правила налево и направо."
            show coach 1f
            show player 11
            show dexter 30
            dex "Что?! Только не это снова. Я не-"
            show dexter 29
            show coach 3f
            bri "Это была явная зарядка!"
            show dexter 2 with dissolve
            show coach 2f
            bri "{b}*вздыхая*{/b} Нам снова нужно обсуждать правила?!"
            show coach 1f
            show dexter 8
            dex "... Нет."
            show dexter 2
            show coach 2f
            bri "Боюсь, мне придется дисквалифицировать тебя и отдать победу {b}[firstname]{/b}."
            show coach 1f
            show dexter 8
            dex "Чушь собачья!"
            show dexter 2
            show player 10
            player_name "... Нет."
            show player 12
            player_name "Я не хочу выиграть из-за формальности."
            show player 90
            show dexter 8
            dex "Формальн- Чёёёё?"
            show dexter 2
            show coach 2f
            bri "Ты уверен, {b}[firstname]{/b}?"
            show coach 1f
            show player 12
            player_name "Уверен."
            show player 90
            show coach 2f
            bri "Хорошо."
            bri "Думаю, завтра нам придется сыграть еще одну игру."
            show coach 1f
            show dexter 30 with dissolve
            dex "Пссс, меня это устраивает!"
            show dexter 32 with dissolve
            dex "Я могу победить этого неудачника с завязанными глазами и одной рукой за спиной..."
            show dexter 31
            show player 12
            player_name "Да, посмотрим..."
            show player 90
            show coach 2f
            bri "Мы {b}встретимся здесь завтра днем{/b} для реванша."
            show coach 1f
            show dexter 32
            dex "Ха, увидимся завтра."
            show player 647
            show dexter 33
            with dissolve
            dex "Сучка."
            hide dexter with dissolve
            show player 648 with dissolve
            pause
            show coach 1 at right with dissolve
            player_name "..."
            show coach 2
            bri "Тренируйся, {b}[firstname]{/b}!"
            bri "Он не будет продолжать верить моим оправданиям..."
            show coach 1
            player_name "Хмм?"
            show coach 2
            bri "Я ожидаю лучшего выступления от тебя завтра."
            show coach 1
            show player 649
            player_name "Да, мэм."
            show player 648
            hide coach with dissolve
            player_name "..."
            show player 649
            player_name "Наверное, мне стоит больше тренироваться."
            hide player with dissolve
        else:

            scene expression "backgrounds/location_basketball_cutscene01.jpg"
            with fade
            show text "{b}Декстер{/b} не просто так стал капитаном баскетбольной команды.\nОн побеждал меня на каждом шагу..." at Position (xpos= 512, ypos= 700) with dissolve
            pause
            show text "В обороне он был как стена, я просто не мог пройти мимо него!\nОн был медленным и неуклюжим, если я на него наступал." at Position (xpos= 512, ypos= 700) with dissolve
            pause
            show text "Были возможности и с небольшой практикой, я был уверен, что смогу победить его!" at Position (xpos= 512, ypos= 700) with dissolve
            pause
            hide text
            with dissolve
            scene basketball_b
            show coach 1f at Position (xpos=400)
            show player 24 at left
            show dexter 3 at right
            with dissolve
            dex "Да, именно так, маленькая сучка!"
            dex "Ты не можешь зависать с {b}Декстером{/b}!"
            show dexter 6 with dissolve
            dex "b}Рокси{/b} должно быть стыдно целоваться с таким неудачником, как ты!"
            show dexter 3 with dissolve
            dex "Хахахахаха!"
            player_name "..."
            show coach 2f
            show player 27
            bri "Хорошо, этого достаточно."
            show dexter 2
            bri "{b}Декстер{/b} ты нарушал правила налево и направо."
            show coach 1f
            show player 11
            show dexter 8
            dex "Что?! Нет, это не так..."
            show dexter 2
            show coach 3f
            bri "Да, это так! Я насчитал не менее десятка личных фолов, и пара была довольно вопиющих."
            show coach 2f
            bri "Боюсь, мне придется дисквалифицировать тебя и отдать победу {b}[firstname]{/b}."
            show coach 1f
            show dexter 6 with dissolve
            dex "Это не справедливо!"
            show dexter 2 with dissolve
            show player 12
            player_name "... Нет."
            player_name "Я не хочу выиграть из-за формальности."
            show player 5
            show dexter 8
            dex "Формальн- Чёёёё?"
            show dexter 2
            show coach 2f
            bri "Ты уверен, {b}[firstname]{/b}?"
            show coach 1f
            show player 10
            player_name "Я уверен."
            show player 5
            show coach 2f
            bri "Хорошо."
            bri "Думаю, завтра нам придется сыграть еще одну игру."
            show coach 1f
            show dexter 3
            dex "Пссс, меня это устраивает!"
            dex "Я могу победить этого неудачника с завязанными глазами и одной рукой за спиной..."
            show dexter 1
            show player 12
            player_name "Да, посмотрим..."
            show player 90
            show coach 2f
            bri "Мы {b}встретимся здесь завтра днем{/b} для реванша."
            show coach 1f
            show dexter 3
            dex "Ха, увидимся завтра."
            show player 647
            show dexter 33
            with dissolve
            dex "Сучка."
            hide dexter with dissolve
            show player 5 with dissolve
            player_name "..."
            show coach 2 at right with dissolve
            bri "Предлагаю вам потренироваться, {b}[firstname]{/b}!"
            bri "Возможно, он больше на это не купится..."
            show coach 1
            player_name "Хмм?"
            show coach 2
            bri "Я ожидаю лучшего выступления завтра."
            show coach 1
            show player 10
            player_name "Да, мэм."
            show player 5
            hide coach with dissolve
            player_name "..."
            show player 109f
            eri "Уххххххх..."
            show player 108f
            player_name "{b}*вздыхая*{/b} Я должен отвести его в раздевалку."
            player_name "... Надеюсь, у него есть сменные штаны здесь, в школе."
            hide player with dissolve
            show expression "boxes/popup_basketball_minigame.png"
            pause
            hide expression "boxes/popup_basketball_minigame.png"
            $ M_roxxy.set("done basketball", True)
    else:

        scene basketball_b
        show player 10
        player_name "Черт, я опять проиграл... Наверное, мне стоит потренироваться, чтобы стать лучше."
    $ game.timer.tick()
    $ player.go_to(L_basketball_court)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
