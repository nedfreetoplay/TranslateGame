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
    player_name "Ага! Я!"
    player_name "Ты сказала, что я должен прийти за ней. Ну вот и я!"
    player_name "А теперь верни мне блесну!"
    show player 16
    show aqua 1
    aqua "Хахаха! Ты веселый человечек!"
    aqua "Ты проделал доллллгий путь. Ты должно быть хорррроший пллловец, как Аква!"
    show player 24
    show aqua 2
    player_name "*кашель* Наверно..."
    show player 30
    player_name "Что это вообще за место?"
    show player 16
    show aqua 1
    aqua "Эттто гнннездо Аква!"
    show player 12
    show aqua 2
    player_name "Ты живешь здесь?"
    show player 11
    show aqua 1
    aqua "Даааа."
    show player 10
    show aqua 2
    player_name "В одиночку?"
    show player 11
    show aqua 4
    aqua "Дааа."
    show player 10
    show aqua 3
    player_name "А еще много таких как ты?"
    show player 11
    show aqua 4
    aqua "Больше... как я?"
    show player 10
    show aqua 3
    player_name "Ты знаешь, другие гнезда с другими... Ааа, Аква?"
    show player 11
    show aqua 4
    aqua "Ооо, нет."
    show aqua 5
    aqua "Нет дррругих. Только Аква. Последняя."
    show player 10
    show aqua 3
    player_name "Ну, это немного грустно. Звучит одиноко."
    show player 5
    show aqua 1
    aqua "Не одиноко. Есть рыбки!"
    show aqua 2b
    aqua "Рыбок вы воруете!"
    show player 15
    show aqua 1b
    player_name "Я говорил тебе, что это не я! Это {b}КАПИТАН Терри{/b}."
    show player 16
    show aqua 4
    aqua "Каплан Терри? Хмм..."
    show aqua 5
    pause
    show aqua 4
    aqua "Возможно, ты говоришь правду..."
    show player 12
    show aqua 3
    player_name "Я говорю правду, Аква. Обещаю."
    show player 16
    show aqua 2b
    aqua "Ну что Aqua делать тогда? Рыбок продолжают воровать!"
    show aqua 4
    aqua "Если рыбки все уйдут, с кем тогда будет разговаривать Аква?"
    show player 11
    show aqua 5
    aqua "Аква сойдет с ума пока найдет партнера."
    show player 10
    show aqua 3
    player_name "Партнера?"
    show player 11
    show aqua 4
    aqua "Даааа, Аква ждет партнера. Чтобы делать деток Аква'ссс."
    show player 10
    show aqua 5
    player_name "Правда? Как долго ты ждешь?"
    show aqua 4
    show player 11
    aqua "Аква не знает. Ооооочень долго. Никто не приходит. Никто не найдет Аква."
    show player 10
    show aqua 5
    player_name "Хмм... Ну, я нашел тебя."
    show player 13
    show aqua 1
    aqua "Дааа! Ты нашел Аква!"
    show aqua 2
    aqua "..."
    show aqua 9
    aqua "Если ты говоришь правду и обещаешь не красть рыбок. Я верну тебе блестяшку."
    show player 14
    show aqua 8
    player_name "Да! Спасибо Аква."
    show player 13
    show aqua 9
    aqua "Ты обещааааешь?"
    show player 14
    show aqua 8
    player_name "Я обещаю, Я не буду красть 'рыбок.'"
    show player 13
    show aqua 9
    aqua "Хооороошооо."
    show aqua 10
    pause
    show aqua 2
    show player 471
    show popup_lure zorder 3 at truecenter with dissolve
    pause
    hide popup_lure with dissolve
    player_name "Уфф... Спасибо Аква!"
    show player 470
    show aqua 1
    aqua "Запомни не воровать рыбок Аква..."
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
    player_name "Аква, У меня хорошие новости!"
    show player 1
    show aqua 1
    aqua "*ах* Ты учишься дышать под водой, как Аква?!"
    show player 12
    show aqua 2
    player_name "Что? ... Нет."
    show player 1
    show aqua 7
    aqua "Ох. Хооороошооо. Тогда что?"
    show player 2
    show aqua 6
    player_name "Я убедил {b}Капитана Терри{/b} не ловить рыбу!"
    show player 1
    show aqua 7
    aqua "В смысле, рыбки в безопасности!?"
    aqua "Нет больше {b}Капитана Терри{/b}!?"
    show player 17
    show aqua 6
    player_name "Эй, ты сказала это правильно в тот раз!"
    show player 1
    show aqua 7
    aqua "А?"
    show player 2
    show aqua 6
    player_name "Ты сказала '{b}Капитана Терри{/b}' правильно."
    show player 1
    show aqua 7
    aqua "Дааа. Каплан Терри!"
    show player 90
    show aqua 6
    player_name "..."
    show aqua 6b
    aqua "..."

    show player 37
    player_name "... Просто забудь."
    show player 2
    player_name "Твои рыбки в бозопасности."
    show player 1
    show aqua 7
    aqua "Ох спасибо! спасибо! спасибо!"
    show aqua 14
    aqua "Ты хороший человек! Сильный человек!"
    show player 29
    show aqua 13
    player_name "Пожалуйста, Аква..."
    show player 1
    show aqua 11
    aqua "..."
    show aqua 12
    aqua "Есть... человек готовый к спариванию с Аква?"
    show player 21
    show aqua 13
    player_name "Сейчас?"
    show player 297
    show aqua 14
    aqua "Дааа. Аква ждала достаточно долго. Напарник должен взять меня в воде!"
    show player 10
    show aqua 13
    player_name "В воде?"
    show player 11
    show aqua 14
    aqua "Да. Пошли!"
    return

label aqua_sex_pre:
    scene location_lair_cutscene
    with fade
    show text "Прикосновение аквы было мягким и нежным, когда она взяла меня за руку и направилась к люминесцентному бассейну." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я изо всех сил старался идти в ногу, возился с одеждой." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Но она, похоже, не заметила, ее волнение ощутимо, когда она привела своего помощника в воду." at Position (xpos= 512, ypos= 700) with dissolve
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
    aqua "Ооо, у тебя красивое тело."
    show aswim 1
    show pswim 2
    player_name "Спасибо Аква..."
    show aswim 3
    show pswim 1
    pause
    show aswim 2
    aqua "Твой угорь спит."
    show aswim 1
    show pswim 2
    player_name "А?"
    show aswim 3
    pause
    show pswim 3
    pause
    show pswim 2
    player_name "Ох. Да..."
    show aswim 2
    show pswim 1
    aqua "Тебе не нравится тело Аква?"
    show aswim 1
    show pswim 2
    player_name "Да... Умм, 'напарнику' очень нравится тело Аква."
    show aswim 2
    show pswim 1
    aqua "Хороший. Тело аквы теперь принадлежит тебе."
    aqua "Угорь напарника может играть в Аква, когда захочет."
    show aswim 3
    pause
    show aswim 2
    aqua "Внутри Аква очень тепло..."
    show aswim 3
    pause
    show aswim 2
    aqua "... и мягко..."
    show aswim 3
    pause
    show aswim 2
    aqua "... и влажно."
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
    aqua "Угорь ведь это любит, правда?!"
    show aswim 3
    show pswim 7
    player_name "Д-Да..."
    show aswim 4
    aqua "Ммм, хорошо. Aqua хочет этого."
    show aswim 3
    show pswim 8
    player_name "..."
    show aswim 4
    aqua "Aqua хочет сейчас!"
    hide pswim
    show aswim 5 with dissolve
    pause
    show aswim 6 at right with dissolve
    player_name "*глоток*"
    aqua "Аааа, дааа. Иди угорь, поиграй в Aqua."
    aqua "Дай Aqua сильных деток..."
    player_name "Ох вау!"
    aqua "Ммм..."
    return

label aqua_sex_after:
    scene location_lair_watersex
    show aquas 1 at Position(xalign = 1.0, yalign = 1.0)
    aqua "{b}Аква{/b} нуждается в нем!"
    aqua "Быстрее, дружище!"
    player_name "..."
    show aquas 2
    aqua "Его."
    aqua "Твой угорь очень большой!"
    aqua "Возьми меня сильнее!"
    $ M_aqua.set("sex speed", .175)
    show expression AnimatedImage("aquas", [3,4,5,6,7], M_aqua) as aquas
    with fade
    aqua "Оооххх!."
    pause
    aqua "Очень сильно!"
    pause
    aqua "и глубоко!"
    $ M_aqua.set("sex speed", .125)
    aqua "Ааааа!"
    pause
    aqua "Мммм, мой напарник."
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
        aqua "Аххххх!!!{p=1}{nw}"

    elif animcounter == 3:
        aqua "Возьми меня!!!{p=1}{nw}"
        player_name "Уххх...{p=1}{nw}"
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
    player_name "{b}Аква{/b}, Я кончаю..."
    aqua "Даааа... ДАААА МОЙ НАПАРНИК!"
    aqua "Дай {b}Аква{/b} свое сссееееммммяяя!"
    aqua "ООООННННН!!!"
    show aquas 8 with flash
    player_name "УХХХ!!"
    aqua "ААААХХХХХ!!!!"
    pause
    show aquas 9
    player_name "Вау!"
    player_name "Это было невероятно!"
    aqua "Дааа..."
    aqua "... {b}Аква{/b} может чувствовать своих сильных детей, плавающих внутри нее!"
    pause
    scene black with fade
    return

label aqua_sex_cum_first:
    scene location_lair_mount
    show aqua 11 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Тебе понравилось?"
    show player 1
    show aqua 12
    aqua "Дааа. Аква нравится! Все еще чувствую покалывание в ногах!"
    show player 2
    show aqua 11
    player_name "Ты была великолепна! Я никогда не чувствовал ничего подобного."
    show player 1
    show aqua 14
    aqua "Дааа, Аква тоже."
    show aqua 12
    aqua "... но Аква хочет больше."
    show aqua 14
    aqua "Напарник вернется, и даст Аква больше семени. Да?"
    show player 2
    show aqua 13
    player_name "Конечно, я очень скоро вернусь!"
    show player 1
    show aqua 14
    aqua "Напарник обещает?"
    show player 2
    show aqua 13
    player_name "Обещаю!"
    show player 1
    show aqua 12
    aqua "Хорошо. Аква хочет больше!"
    show aqua 14
    aqua "Возвращайся скорее, Человечек."
    show aqua 11
    aqua "Аква подождет здесь пока не пройдет покалывание в ногах..."
    return

label aqua_dialogue_pre:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0) with dissolve
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0) with dissolve
    player_name "Привет, Аква!"
    show player 1
    show aqua 1
    aqua "Дааа..."
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
    aqua "Хммм, Аква не уверена. Они просто исчезли однажды. Аква-последний."
    show aqua 5
    show player 10
    player_name "Ааа, Прости Аква."
    show player 11
    show aqua 1
    aqua "Ещё вопросы?"
    show aqua 2
    return

label aqua_dialogue_how_are_you:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, как дела?"
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
    aqua "... но нравится что человеческий мальчик навещает."
    show player 2
    show aqua 3
    player_name "Мне тоже нравится с тобой разговаривать Аква."
    show player 1
    show aqua 1
    aqua "Да, как будто разговариваешь."
    aqua "Еще вопросы?"
    show aqua 2
    return

label aqua_dialogue_mating_pre:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 10 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Аква, какого напарника ты ищешь?"
    show player 11
    show aqua 4
    aqua "Мужчину. Сильного мужчину. Сделать Aqua сильных деток."
    show aqua 1
    aqua "знаешь такого?"
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
    aqua "[chr_warn]Ты силен?"
    show player 29
    show aqua 3
    player_name "[chr_warn]Да?"
    show player 3
    show aqua 5
    aqua "..."
    aqua "Хмм..."
    pause
    show aqua 4
    aqua "[chr_warn]Аква думает... нет. Плохая идея."
    show player 24
    show aqua 3
    player_name "[chr_warn]Облом..."
    return

label aqua_dialogue_mating_stat_pass:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 2 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Может я могу помочь?"
    show player 1
    show aqua 7
    aqua "Ты?"
    show player 2
    show aqua 6
    player_name "Ну, я имею в виду, я проплыл весь путь сюда, чтобы найти тебя."
    show player 1
    show aqua 7
    aqua "Ага."
    show player 2
    show aqua 6
    player_name "... И я сражался с очень злым кальмаром на этом пути."
    show player 1
    show aqua 7 with hpunch
    aqua "Ты побил Инки?!"
    show player 2
    show aqua 6
    player_name "Инки? Да. Я побил Инки."
    show aqua 7
    aqua "Оооо, Инки сильный!"
    show aqua 12
    pause
    show aqua 11
    aqua "Может быть, ты дашь Аква сильных детей."
    show player 14
    show aqua 13
    player_name "Правда?!"
    show player 1
    show aqua 14
    aqua "Да. Но партнера пока нет. Сначала ты докажешь свою силу."
    show player 10
    show aqua 13
    player_name "Доказать свою силу? Как я должен это сделать?"
    show player 1
    show aqua 7
    aqua "Ты говоришь,что Каплан Терри ворует рыбок, да?"
    show player 12
    show aqua 6
    player_name "{b}Капитану Терри{/b}. Да, это тот парень, который ловит рыбу у причала."
    show player 11
    show aqua 7
    aqua "Хмм, ты должен остановить Каплана Терри."
    show aqua 11
    aqua "Ты сделаешь это, а потом спариваешься с Аква."
    show player 10
    show aqua 13
    player_name "Ну, я полагаю, я могу сделать это."
    show player 11
    show aqua 14
    aqua "Хорошо. Иди. Спаси рыбок!"
    return

label aqua_dialogue_mating_hint:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 12 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Что мне нужно сделать, Аква? Чтобы доказать свою силу?"
    show player 11
    show aqua 7
    aqua "Спаси рыбок от Каплан Терри!"
    show player 10
    show aqua 6
    player_name "Ах,да. {b}Капитан Терри{/b}."
    show player 11
    show aqua 7
    aqua "Так Аква и сказала! Каплан Терри!"
    show player 12
    show aqua 6
    player_name "Капи- неважно. Думаю, мне стоит попробовать поговорить с ним."
    show player 5
    show aqua 7
    aqua "Дааа. Иди, спаси рыбок!"
    return

label aqua_dialogue_mate:
    show aqua 2 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 21 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Я подумал, может ты захочешь... Снова залезть в воду?"
    show player 26
    show aqua 3
    aqua "..."
    show aqua 1
    aqua "О! Ты хочешь делать деток?"
    show player 21
    show aqua 12
    player_name "Я... конечно?"
    show player 26
    show aqua 11
    aqua "Хахаха! Забавный Человек. Теперь ты напарник Аквы."
    show aqua 14
    aqua "Aqua всегда готова к большему количеству семяни! Напарник может взять ее в воде когда захочет."
    return

label aqua_dialogue_nothing:
    show aqua 3 zorder 1 at Position(xpos=.5875, ypos=1.0)
    show player 36 zorder 2 at Position(xpos=.125, ypos=1.0)
    player_name "Ничего, я просто поздороваться!"
    show player 1
    show aqua 4
    aqua "Человеческий мальчик... Смешной..."
    show aqua 1
    aqua "...Мне нравится человеческий мальчик..."
    show player 21
    show aqua 2
    player_name "Я ... .. Как и ты тоже!"
    show player 13
    aqua "..."
    show player 29
    player_name "В любом случае, мне пора идти."
    show player 3
    show aqua 1
    aqua "Возвращайся, посмотреть на Аква."
    show player 17
    show aqua 2
    player_name "Конечно!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
