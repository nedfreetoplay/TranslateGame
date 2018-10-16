label aqua_dialogue_night:
    show player 10 with dissolve
    player_name "Уже поздно..."
    player_name "Я должен найти выход из этой подводной пещеры, пока не стемнело."
    hide player with dissolve
    return

label aqua_dialogue_aqua_found:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    pause
    show player 16 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    show aqua 1
    aqua "(!!!)" with hpunch
    aqua "Ты!!"
    show player 15
    show aqua 2
    player_name "Вот именно! Тебя!"
    player_name "Ты сказал, что я должен прийти за ним. Ну вот и я!"
    player_name "А теперь верни мне блеск!"
    show player 16
    show aqua 1
    aqua "ХаХаХаХа! Ты забавный человек!"
    aqua "Вы проделали долгий путь. Ты обязан'сс быть хорошимсс пловцом, как Аква!"
    show player 24
    show aqua 2
    player_name "*кашель* Я думаю..."
    show player 30
    player_name "Что это за место в любом случае?"
    show player 16
    show aqua 1
    aqua "Это гнездо Аква'сс!"
    show player 12
    show aqua 2
    player_name "Ты живешь здесь?"
    show player 11
    show aqua 1
    aqua "Yesss."
    show player 10
    show aqua 2
    player_name "В одиночку?"
    show player 11
    show aqua 4
    aqua "Да'ссс."
    show player 10
    show aqua 3
    player_name "Есть ли больше вас?"
    show player 11
    show aqua 4
    aqua "Больше... меня?"
    show player 10
    show aqua 3
    player_name "Вы знаете, другие гнезда с другими... Эм, Аквами?"
    show player 11
    show aqua 4
    aqua "ООО, нет."
    show aqua 5
    aqua "Нет других. Аква. Последняя из рода."
    show player 10
    show aqua 3
    player_name "Ой, это очень грустно. Звучит одиноко."
    show player 5
    show aqua 1
    aqua "Не одиноко. Есть рыбы!"
    show aqua 2b
    aqua "Вы крадете Рыб!"
    show player 15
    show aqua 1b
    player_name "Я же говорил, что это не я! Это же {b}КАПИТАН Терри{/b}."
    show player 16
    show aqua 4
    aqua "Капитан Терри? Хмм..."
    show aqua 5
    pause
    show aqua 4
    aqua "Может быть, вы говорите правду..."
    show player 12
    show aqua 3
    player_name "Я говорю правду, Аква. Обещаю."
    show player 16
    show aqua 2b
    aqua "Ну, что Акве делать тогда? Рыбаки продолжают красть рыбу!"
    show aqua 4
    aqua "Если рыбы все ушли, с кем будет разговорить Аква?"
    show player 11
    show aqua 5
    aqua "Аква ждёт Партнера."
    show player 10
    show aqua 3
    player_name "Партнера?"
    show player 11
    show aqua 4
    aqua "Да'ссс, Аква ждет партнера. Сделать ребенка Аква'ссс."
    show player 10
    show aqua 5
    player_name "Реально? Сколько ты уже ждешь?"
    show aqua 4
    show player 11
    aqua "Аква не знает. Доооолго. Никто не придет. Никто не найдет Акву."
    show player 10
    show aqua 5
    player_name "Хм... Ну, я нашел тебя."
    show player 13
    show aqua 1
    aqua "Да'ссс! Ты нашёл Акву!"
    show aqua 2
    aqua "..."
    show aqua 9
    aqua "Если вы говорите верно и обещаете не воровать рыбок. Я верну тебе блестяшку."
    show player 14
    show aqua 8
    player_name "Да! Спасибо тебе Аква."
    show player 13
    show aqua 9
    aqua "Ты обещаешь?"
    show player 14
    show aqua 8
    player_name "Обещаю, я не буду воровать 'рыбок'."
    show player 13
    show aqua 9
    aqua "Хорошоо."
    show aqua 10
    pause
    show aqua 2
    show player 471
    show popup_lure zorder 3 at truecenter with dissolve
    pause
    hide popup_lure with dissolve
    player_name "Фух... Спасибо тебе Аква!"
    show player 470
    show aqua 1
    aqua "Только не забывай про рыбок Аквы...."
    hide player
    hide aqua
    with dissolve
    return

label aqua_sex:
    $ game.timer.tick()
    if M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_pre_first")

    call expression game.dialog_select("aqua_sex_pre")
    if M_aqua.is_state(S_aqua_mate):
        label aqua_sex_replay:
            call expression game.dialog_select("aqua_sex_after_first")

    call expression game.dialog_select("aqua_sex_after")
    jump expression game.dialog_select("aqua_sex_loop")

label aqua_sex_pre_first:
    scene location_lair_mount
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, у меня хорошие новости.!"
    show player 1
    show aqua 1
    aqua "*Отдышка* Ты учишься дышать под водой, как Аква?!"
    show player 12
    show aqua 2
    player_name "Что? ... Нет."
    show player 1
    show aqua 7
    aqua "Ох. Хорошо. Какие новости?"
    show player 2
    show aqua 6
    player_name "Я убедил {b}Капитана Терри{/b} прекратить воровать рыбок!"
    show player 1
    show aqua 7
    aqua "То есть рыбки в безопасности!?"
    aqua "{b}Капитана Терри{/b} больше не будет!?"
    show player 17
    show aqua 6
    player_name "Эй, ты правильно сказала в тот раз!"
    show player 1
    show aqua 7
    aqua "Да?"
    show player 2
    show aqua 6
    player_name "Вы правильно сказали: '{b}Капитан Терри{/b}' на этот раз."
    show player 1
    show aqua 7
    aqua "Да. Капитан Терри!"
    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "... Просто забудь."
    show player 2
    player_name "Теперь ваша рыба должна быть в безопасности."
    show player 1
    show aqua 7
    aqua "Ох, спасибо тебе! Спасибо! Спасибо!"
    show aqua 14
    aqua "Ты хороший человек! Сильный человек!"
    show player 29
    show aqua 13
    player_name "Всегда пожалуйста, Аква..."
    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "Это... человек готов к спариванию с Аква?"
    show player 21
    show aqua 13
    player_name "Прямо сейчас?"
    show player 297
    show aqua 14
    aqua "Да'ссс. Аква ждёт достаточно долго. Партнер возьмёт её в воде!"
    show player 10
    show aqua 13
    player_name "В воде?"
    show player 11
    show aqua 14
    aqua "Да. Приходи!"
    return

label aqua_sex_pre:
    scene location_lair_cutscene
    with fade
    show text "Прикосновение Аквы было мягким и нежным, когда она взяла меня за руку и направилась к люминесцентному бассейну." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я изо всех сил старался идти в такт, возился со своей одеждой." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Но она, казалось, не замечала, ее волнение ощутимо, когда она ведет своего партнера в воду." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label aqua_sex_after_first:
    scene location_lair_water with fade
    show aswim 1 at left
    show pswim 1 at right
    pause
    show aswim 2
    aqua "О, у приятеля хорошее тело.."
    show aswim 1
    show pswim 2
    player_name "Спасибо Аква..."
    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Твой угорь уснул."
    show aswim 1
    show pswim 2
    player_name "Да?"
    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Ох. Да..."
    show aswim 2
    show pswim 1
    aqua "Партнеру нравиться тело Аквы?"
    show aswim 1
    show pswim 2
    player_name "Да... хмм, 'партнеру' очень нравиться тело Аквы."
    show aswim 2
    show pswim 1
    aqua "Хорошо. Тело Аквы теперь принадлежит тебе."
    aqua "Угорь партнера может играть внутри Аквы когда захочет."
    show aswim 3
    pause
    show aswim 2
    aqua "Внутри Аквы тепло..."
    show aswim 3
    pause
    show aswim 2
    aqua "... и мягко..."
    show aswim 3
    pause
    show aswim 2
    aqua "... и мокро."
    show pswim 3
    pause
    show aswim 3
    show pswim 4
    pause
    show aswim 4
    show pswim 5
    pause
    show pswim 9
    pause
    show aswim 2
    show pswim 6
    aqua "Ох, угорю это нравиться, да?!"
    show aswim 3
    show pswim 7
    player_name "Д-аа..."
    show aswim 4
    aqua "Ммм, Хорошо. Аква хочет его."
    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "Аква хочет его сейчас!"
    hide pswim
    show aswim 5 with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "*Глоток*"
    aqua "Аахх, да'ссс. Твой... Угорь Играет внутри Аквы."
    aqua "Подари Акве сильного ребенка..."
    player_name "Ух ты!"
    aqua "Ммм..."
    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    aqua "{b}Акве{/b} нужно внутрь его!"
    aqua "Поспеши мой друг!"
    player_name "..."
    show aquas 2
    aqua "Он'ссс."
    aqua "Твой угорь очень большой!"
    aqua "Возьми меня силой!"
    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
    with fade
    aqua "Ооохх!."
    pause
    aqua "Так сильно!"
    pause
    aqua "и глубоко!"
    $ M_aqua.set("sex speed", .125)
    aqua "Ааахх!"
    pause
    aqua "Ммм, мой партнер."
    aqua "Быстрее!"
    $ M_aqua.set("sex speed", .075)
    pause
    return

label aqua_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
            pause 5
            call expression game.dialog_select("aqua_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "aquas {}".format(pose_list[pose_counter]) as aquas
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("aqua_hscene_dialog")
        $ animcounter += 1
    call screen aqua_sex_options

label aqua_hscene_dialog:
    if animcounter == 1:
        aqua "Аххх!!!{p=1}{nw}"

    elif animcounter == 3:
        aqua "Возьми меня!!!{p=1}{nw}"
        player_name "Оххх...{p=1}{nw}"
    return

label aqua_sex_cum:
    call expression game.dialog_select("aqua_sex_cum_pre")
    if not store._in_replay == None or M_aqua.is_state(S_aqua_mate):
        call expression game.dialog_select("aqua_sex_cum_first")

    $ renpy.end_replay()
    $ persistent.cookie_jar["Aqua"]["unlocked"] = True
    $ persistent.cookie_jar["Aqua"]["gallery"]["01_unlocked"] = True
    $ M_aqua.trigger(T_aqua_mated)
    hide player
    hide aqua
    with dissolve
    $ game.main()

label aqua_sex_cum_pre:
    player_name "Это невероятно!"
    player_name "{b}Аква{/b}, Я собираюсь..."
    aqua "Дааа... Да мой партнер!"
    aqua "Дай {b}Акве{/b} своё семя!"
    aqua "Оннн!!!"
    show aquas 8 with flash
    player_name "Оххх!!"
    aqua "Ахххх!!!!"
    pause
    show aquas 9
    player_name "Офигеть!"
    player_name "Это было невероятно!"
    aqua "Дааа..."
    aqua "... {b}Аква{/b} чувствет сильного младенца, который плавает внутри ее!"
    pause
    scene black with fade
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Так вам понравилось?"
    show player 1
    show aqua 12
    aqua "Да'ссс. Аква много наслаждалась! Все еще чувствую покалывание в ногах!"
    show player 2
    show aqua 11
    player_name "Ты была невероятна! Я никогда не чувствовал ничего подобного раньше."
    show player 1
    show aqua 14
    aqua "Да'ссс, у Аквы это было в первый раз."
    show aqua 12
    aqua "... Но Аква хочет больше."
    show aqua 14
    aqua "Партнер ещё вернется, даст Акве больше семени. Да?"
    show player 2
    show aqua 13
    player_name "Абсолютно, Я очень скоро вернусь.!"
    show player 1
    show aqua 14
    aqua "Партнер обещает?"
    show player 2
    show aqua 13
    player_name "Ох, Я обещаю!"
    show player 1
    show aqua 12
    aqua "Хороший. Аква хочет гораздо больше!"
    show aqua 14
    aqua "Скоро вернется, Человек."
    show aqua 11
    aqua "Аква будет ждать здесь, пока не перестанет покалывать..."
    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Привет, Аква!"
    show player 1
    show aqua 1
    aqua "Да'с..."
    show player 2
    show aqua 2
    player_name "Я хотел поговорить с тобой."
    show player 1
    show aqua 4
    aqua "Чего хочет человеческий мальчик?"
    return

label aqua_dialogue_the_others:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, что случилось с остальными твоего вида?"
    show player 11
    show aqua 4
    aqua "Хмм, Аква не уверена. Они просто однажды ушли. Аква осталась одна."
    show aqua 5
    show player 10
    player_name "Ой, прости, Аква."
    show player 11
    show aqua 1
    aqua "У тебя ещё остались вопросы?"
    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, как ты?"
    show player 1
    show aqua 4
    aqua "Как я?"
    show player 2
    show aqua 3
    player_name "Да, как ты себя чувствуешь?"
    show player 1
    show aqua 5
    aqua "Хм, Аква в порядке. Одиноко с таким количеством рыбешек..."
    show aqua 4
    aqua "... но нравится, что человеческий мальчик приходит в гости."
    show player 2
    show aqua 3
    player_name "Мне тоже нравится с тобой разговаривать.."
    show player 1
    show aqua 1
    aqua "Увлекательно, как говориться."
    aqua "У тебя ещё остались вопросы?"
    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, какого партнера ты ищешь??"
    show player 11
    show aqua 4
    aqua "Мужчину. Упрямого мужчину. Он сделает Акве сильного младенца."
    show aqua 1
    aqua "ты знаешь такого человека,?"
    show player 34
    show aqua 3
    player_name "Хмм."
    return

label aqua_dialogue_mating_stat_fail:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 29 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "[chr_warn]Как насчет меня?"
    show player 3
    show aqua 4
    aqua "[chr_warn]Ты сильный мужчина?"
    show player 29
    show aqua 3
    player_name "[chr_warn]Да?"
    show player 3
    show aqua 5
    aqua "..."
    aqua "хмм..."
    pause
    show aqua 4
    aqua "[chr_warn]Аква думает... Нет. Плохая идея."
    show player 24
    show aqua 3
    player_name "[chr_warn]Облом..."
    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Может быть, я смогу помочь?"
    show player 1
    show aqua 7
    aqua "Ты?"
    show player 2
    show aqua 6
    player_name "Ну, я имею в виду, я проплыл весь путь сюда, чтобы найти тебя."
    show player 1
    show aqua 7
    aqua "Ты сделаешь это."
    show player 2
    show aqua 6
    player_name "... И я сражался с очень злым кальмаром по пути."
    show player 1
    show aqua 7 with hpunch
    aqua "Ты борешься с чернилом?!"
    show player 2
    show aqua 6
    player_name "Чернилом? Да. Я борюсь с чернилом."
    show aqua 7
    aqua "Ооох, Чернил сильный!"
    show aqua 12
    pause
    show aqua 11
    aqua "Может быть, ты сделаешь Акве сильных детей."
    show player 14
    show aqua 13
    player_name "Впрямь?!"
    show player 1
    show aqua 14
    aqua "Да'ссс. Но пока нет партнера. Сначала ты докажешь силу."
    show player 10
    show aqua 13
    player_name "Доказать свою силу? Как я должен это сделать?"
    show player 1
    show aqua 7
    aqua "Скажешь Капитану Терри не воровать рыбу, да?"
    show player 12
    show aqua 6
    player_name "{b}Капитану Терри{/b}. Да, это парень, который ловил рыбу на пристани.."
    show player 11
    show aqua 7
    aqua "Хмм, скажите Каплан Терри прекрать."
    show aqua 11
    aqua "Вы делаете это, а затем спариваетесь с Аква."
    show player 10
    show aqua 13
    player_name "Ну, я полагаю, я могу ему об этом сказать."
    show player 11
    show aqua 14
    aqua "Хороший. Тогда иди ты. Сохрани рыбу!"
    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Что мне нужно сделать еще раз, Аква? Чтобы доказать свою силу?"
    show player 11
    show aqua 7
    aqua "Ты должен сохранить рыбу с помощью Каплана Терри!"
    show player 10
    show aqua 6
    player_name "Ох, понял. {b}Капитан Терри{/b}."
    show player 11
    show aqua 7
    aqua "Это то, что говорит Аква! Каплан Терри!"
    show player 12
    show aqua 6
    player_name "Капи- неважно. Думаю, мне стоит попробовать поговорить с ним."
    show player 5
    show aqua 7
    aqua "Да'ссс. Иди, спаси рыбу!"
    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Я подумала, Может ты захочешь... Снова в воду?"
    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "Ох! Вы хотите сделать детей?"
    show player 21
    show aqua 12
    player_name "Я, ошибся... Конечно?"
    show player 26
    show aqua 11
    aqua "Хахаха! Смешной Человек. Теперь ты друг Аквы."
    show aqua 14
    aqua "Аква всегда готов к большему количеству семени! Партнер может взять ее сильно в воде, когда он хочет."
    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Ничего, я просто поздоровался!"
    show player 1
    show aqua 4
    aqua "Человеческий мальчик... Смешной..."
    show aqua 1
    aqua "...Мне нравится человеческий мальчик..."
    show player 21
    show aqua 2
    player_name "Я чт... Как и вы мне!"
    show player 13
    aqua "..."
    show player 29
    player_name "В любом случае, мне пора идти.."
    show player 3
    show aqua 1
    aqua "Приходи ещё, увидемся ещё."
    show player 17
    show aqua 2
    player_name "Спорим!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
