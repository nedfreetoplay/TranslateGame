label music_classroom_dewitt_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Хей, {b}Мисс Девитт{/b}."
    show player 13f
    show dewitt 2
    dewitt "О боже мой, {b}[firstname]{/b}! Это ты, милый?"
    dewitt "Я уже начала думать, что ты перешёл в другую школу или что-то вроде того!"
    show dewitt 1
    show player 10f
    player_name "Хех, нет. У меня были, эм, некоторые \"семейные проблемы\"."
    show player 5f
    show dewitt 2
    dewitt "Да, я слышала о твоем отце. Соболезную..."
    dewitt "Что я могу для тебя сделать?"
    show dewitt 1
    show player 10f
    player_name "Вообще-то, я бы хотел вернуться к вам..."
    show player 5f
    show dewitt 2
    dewitt "Ну, я думаю, мы сможем что-нибудь придумать."
    dewitt "Выбирай инструмент и садись."
    dewitt "Посмотрим, не потерял ли ты чувство ритма."
    show dewitt 3
    show player 11f
    pause
    show dewitt 1
    show player 10f
    player_name "Окей, любой инструмент, {b}Мисс Девитт{/b}?"
    show player 5f
    show dewitt 2
    dewitt "Хмм, почему бы тебе не попробывать барабаны?"
    show dewitt 1
    show player 14f
    player_name "Окей!"
    hide player
    hide dewitt
    with dissolve

    scene music_class_cs01
    with fade
    show text "Я никогда раньше не играл на барабанах." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs01

    scene music_class_cs02
    with fade
    show text "Было очень трудно не сбиваться, но я даже получил удовольствие..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs02

    scene music_class_cs03
    with hpunch
    show text "!!!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide music_class_cs03

    scene music_class_cs04
    with fade
    show text "Мне приятно, что {b}Мисс Девитт{/b} так добра ко мне...\nНо я ужасно..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show dewitt 1 at left
    show player 37f at right
    with dissolve
    player_name "Простите, {b}Мисс Девитт{/b}!"
    player_name "Я не-"
    show player 3f at Position (xoffset=-8) with dissolve
    show dewitt 2
    dewitt "Хехе, всё в порядке, сладкий."
    dewitt "Ты не первый, кто хочет поиграть на этих малышках!"
    show dewitt 3
    show player 11f with dissolve
    player_name "..."
    show player 5f
    show dewitt 2
    dewitt "Может подберем тебе что-нибудь более элегантное?"
    dewitt "Хм, может быть флейта..."
    show dewitt 1
    show player 12f
    player_name "... Хм, может флейта?"
    player_name "Или она больше для женщин?"
    show player 5f
    show dewitt 2
    dewitt "Ох, конечно же нет, сладкий!"
    dewitt "Мужчины играли на флейтах с самых древних времен."
    show dewitt 1
    show player 10f
    player_name "Серьезно?"
    show player 5f
    show dewitt 2
    dewitt "Уж поверь!"
    dewitt "В средневековых армиях использовались флейты что бы задать нужный ритм для марширования."
    dewitt "В этом нет ничего женского, так ведь?"
    show dewitt 1
    show player 12f
    player_name "Нет, я думаю ничего."
    show player 5f
    show dewitt 2
    dewitt "Может тогда обдумаешь это?"
    show dewitt 1
    show player 10f
    player_name "Может быть..."
    show player 5f
    show dewitt 2
    dewitt "Извини, сладкий, но мне нужно не на долго отвлечься."
    hide player
    hide dewitt
    with dissolve

    show studyclass02 with dissolve
    show text "Я потратил целый день на попытки играть в верном ритме..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "... и, наконец, звонок прозвенел." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show dewitt 2 with dissolve
    dewitt "Вы все отлично постарались! Это было прекрасное занятие!"
    dewitt "Но перед тем как вы уйдете, я бы хотела задержать вас на пару минут!"
    show dewitt 14 at Position (xoffset=-127) with dissolve
    dewitt "Хэй!"
    dewitt "{b}Tyrone{/b}, посмотри на меня!"
    show dewitt 13 at Position (xoffset=-127)
    tyrone "..."
    show dewitt 2 with dissolve
    dewitt "Я бы хотела напомнить вам, что скоро начнется смотр музыкальных талантов."
    dewitt "... И у нас остались свободные места, которые нужно заполнить."
    show dewitt 3 at Position (xoffset=-7)
    dewitt "Помни, {b}Я предлагаю дополнительный кредит{/b} всем, кто участвует.."
    player_name "!!!"
    show dewitt 2
    dewitt "Так что я надеюсь на то, что в этом году всё пройдет без каких-либо проблем!"
    dewitt "Так что прошу вас, не стесняйтесь подходить ко мне по этому поводу."
    show dewitt 3 at Position (xoffset=-7)
    dewitt "Спасибо за внимание, удачного вечера!"
    show dewitt 1 at right with dissolve
    pause 0.5
    hide dewitt with dissolve
    pause 1

    show player 17 with dissolve
    player_name "Дополнительный кредит-это то, что мне нужно!"
    show player 14
    player_name "Я сделаю всё, чтобы улучшить свою оценку."
    player_name "Нужно завтра {b}поговорить с Мисс Девитт про смотр талантов{/b}."
    hide player with dissolve
    return

label music_classroom_dewitt_smith_berating:
    scene music_classroom_c
    show dewitt 13 at left
    show principal 5 at right
    with dissolve
    smi "Ты не можешь снова пытаться провечти этот смотр!"
    show principal 4 with dissolve
    smi "Разве прошлый год был недостаточно неловким для тебя?!"
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "... Почему вы опять это делаете!?"
    dewitt "Я просто пытаюсь привить этим детям любовь к музыке, а вы постоянно мешаете!"
    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smi "Оу, бедная {b}Мелодия{/b}."
    smi "Но, тебе больше не придется об этом волноваться..."
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Угх, что вы собираетесь делать?"
    show dewitt 13
    show principal 27 at Position (xoffset=-70)
    smi "У меня была встреча со школьным советом."
    smi "И знаешь что? Я рассказала им о том, сколько денег ты потратила на это смехотворное шоу в прошлом году..."
    smi "... И они поручили мне перераспределить ресурсы на что-то более важное."
    show principal 26 at Position (xoffset=-70)
    show dewitt 14
    dewitt "Более важное?"
    dewitt "А вы можете быть настоящей сукой, знаете?"
    show dewitt 13
    show principal 5 with dissolve
    smi "Хаха!"
    smi "Не могу дождаться, как ты провалишься в этот раз..."
    show principal 26 at Position (xoffset=-70) with dissolve
    show dewitt 14
    dewitt "*Грр*"
    dewitt "Просто уходите из моего класса!"
    show dewitt 13
    show principal 38 with dissolve
    smi "Хахаха!"
    hide principal with dissolve
    show dewitt 12
    dewitt "Боже, я её ненавижу."
    hide dewitt with dissolve
    return

label music_classroom_dewitt_talent_show_help:
    scene music_classroom_c
    show dewitt 10b at left
    show player 10f at right
    with dissolve
    player_name "Хей, {b}Мисс Девитт{/b}."
    show player 5f
    show dewitt 11b
    dewitt "Привет, сладкий. Как ты?"
    show dewitt 10b
    show player 10f
    player_name "Я в порядке."
    show player 14f
    player_name "Можно поговорить с вами об этом смотре талантов?"
    show player 13f
    show dewitt 11b
    dewitt "Ох, конечно же-"
    show dewitt 9
    pause 2
    show dewitt 11
    dewitt "Стоп, ты только что спросил о смотре талантов?!"
    show dewitt 9
    show player 12f
    player_name "... Да?"
    show player 5f
    show dewitt 3 with dissolve
    dewitt "О мой бог!"
    show dewitt 4 with dissolve
    show player 10f
    player_name "Ух, вы в порядке, {b}Мисс Девитт{/b}?"
    show player 5f
    show dewitt 11
    dewitt "Я просто немного на эмоциях."
    show dewitt 11b
    dewitt "{b}Директриса Смит{/b} пытается найти способ отменить шоу в этом году."
    show dewitt 12
    dewitt "... Так что у меня только один доброволец."
    show dewitt 10b
    show player 12f
    player_name "Кто?"
    show player 5f
    show dewitt 11
    dewitt "{b}Тайрон{/b}."
    dewitt "... Но он ни разу ещё не смог сыграть соло!"
    show dewitt 10
    show player 14f
    player_name "Что же, я тоже хочу присоединиться!"
    show dewitt 4
    player_name "Может я попытаюсь найти ещё добровольцев?"
    hide player
    show dewitt 6 at right
    with dissolve
    dewitt "Ох, спасибо тебе, милый!"
    dewitt "Это было бы просто прекрасно!"
    show dewitt 7
    pause
    show dewitt 15 at left
    show player 14f at right
    with dissolve
    player_name "Хех, никаких проблем..."
    show player 13f
    show dewitt 3 with dissolve
    dewitt "Ох, {b}[firstname]{/b}, ты только что заставил меня переосмыслить мой взгляд на сегодняшний день!"
    show dewitt 1
    show player 14f
    player_name "Я рад, что вам стало лучше!"
    show player 13f
    show dewitt 2
    dewitt "Какой милый молодой человек..."
    dewitt "На каком инструменте ты хочешь играть?"
    show dewitt 1
    show player 14f
    player_name "Ну, я даже не знаю. Мне вроде понравились барабаны."
    show player 13f
    show dewitt 8 with dissolve
    dewitt "Хех, о да. Я помню, как мы вчера поиграли на барабанах."
    show dewitt 15
    show player 10f
    player_name "... И я хочу ещё раз за это извиниться."
    show player 5f
    show dewitt 16
    dewitt "Не переживай об этом, сладкий."
    show dewitt 17 with dissolve
    show player 11f
    dewitt "Эти девочки имеют некоторые неудобные привычки."
    dewitt "Ты не представляешь, как сильно они мне мешают играть на гитаре."
    dewitt "... Я думаю, что они просто любят привлекать к себе внимание."
    show dewitt 15 with dissolve
    show player 13f
    player_name "..."
    show dewitt 5
    dewitt "Но я боюсь, что {b}Тайрон{/b} уже записался на барабаны."
    show dewitt 16
    dewitt "Я знаю, что ты бы играл на них с присущим тебе энтузиазмом."
    show dewitt 4
    show player 10f
    player_name "Он уже?"
    show player 12f
    player_name "Хмм, даже не знаю, что выбрать..."
    show player 10f
    player_name "А вы что думаете?"
    show player 5f
    show dewitt 5
    dewitt "Ну, что надумал про флейту?"
    show dewitt 4
    show player 12f
    player_name "Ух, только не опять..."
    show player 5f
    show dewitt 8
    dewitt "Да ладно тебе!"
    show dewitt 5
    dewitt "Нет ничего лучше чем мужчина, который знает, как обращаться со своей флейтой!"
    show dewitt 4
    player_name "..."
    show player 12f
    player_name "Серьёзно?"
    show player 5f
    show dewitt 5
    dewitt "Ну уж поверь мне!"
    show dewitt 8
    dewitt "Я даже дам тебе несколько бесплатных уроков!"
    show dewitt 4
    show player 10f
    player_name "Ты умеешь играть на флейте?"
    show player 5f
    show dewitt 16
    dewitt "Ох, милый. Мои умения просто невероятны!"
    dewitt "Я могу творить чудеса этим ртом!"
    show dewitt 15
    show player 14f
    player_name "Ладно, я попробую, если вы и правда собираетесь дать мне бесплатные уроки."
    show player 13f
    show dewitt 16
    dewitt "О, ещё как собираюсь."
    show dewitt 15
    show player 14f
    player_name "Окей, тогда я попробую флейту."
    show player 13f
    show dewitt 5
    dewitt "Отличное решение, {b}[firstname]{/b}!"
    dewitt "Сейчас её принесу. Секунду."
    hide dewitt with dissolve
    pause
    pause
    show player 55f with dissolve
    player_name "{b}*Зевает*{/b}"
    pause
    show player 13f with dissolve
    pause
    show dewitt 11 at left with dissolve
    dewitt "Ну, одна у нас точно была."
    show dewitt 10b
    dewitt "Хмм, куда же она делась."
    show dewitt 11
    dewitt "Я вроде давала её кому-то в этом году."
    dewitt "Хотя, обычно их не возвращают, да?"
    dewitt "Почему бы вам не заглянуть на лист входа инструмента {b}в шкафчике класса{/b}."
    show dewitt 4
    show player 14f
    player_name "Окей, я гляну!"
    show player 13f
    show dewitt 5
    dewitt "Возвращайся скорее, сладкий!"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_music_sheet:
    scene music_classroom_c
    show music_checkout_form with dissolve
    pause
    player_name "Хмм..."
    player_name "Судя по всему, {b}Джуди{/b} была последней, кто брал школьную флейту."
    player_name "{b}Лучше бы мне её поскорее найти{/b}!"
    hide music_checkout_form with dissolve
    $ game.main()

label music_classroom_dewitt_return_flute:
    scene music_classroom_c
    show dewitt 1 at left
    show player 14f at right
    with dissolve
    player_name "Хей, {b}Мисс Девитт{/b}."
    player_name "Я нашел эту флейту."
    show player 13f
    show dewitt 2
    dewitt "Я знала, что ты сможешь, сладкий!"
    show dewitt 1
    show player 10f
    player_name "... Но, я боюсь, она сломана."
    show player 5f
    show dewitt 11b with dissolve
    dewitt "Сломана?! И что же нам делать?"
    show dewitt 10b
    show player 14f
    player_name "Ну, я типа, сделал одну флейту!"
    show player 239_240f with dissolve
    pause
    show player 567cf with dissolve
    player_name "Что думаешь?"
    show player 567bf
    show dewitt 5
    dewitt "Вау! Ты сделал это сам?!"
    show dewitt 4
    show player 567cf
    player_name "Да, дома в гараже."
    show player 567bf
    show dewitt 16
    dewitt "А ты не плохо обращаешься с деревом, да?"
    show dewitt 15
    show player 567cf
    player_name "Да, вроде того."
    show player 567bf
    show dewitt 5
    dewitt "Можно мне посмотреть по ближе?"
    show dewitt 4
    show player 567cf
    player_name "Конечно!"
    show player 13f with dissolve
    show dewitt 34 with dissolve
    dewitt "Длина и обхват просто..."
    dewitt "Прекрасны."
    dewitt "Раз уж ты сделал эту флейту, я хочу у тебя спросить, можно мне одолжить её на пару ночей?!"
    show dewitt 33
    show player 11f
    player_name "???"
    show dewitt 34
    dewitt "Что? Я просто люблю новые инструменты!"
    show dewitt 33
    show player 14f
    player_name "Окей, я не против."
    player_name "Я попытался сыграть на ней. Это не очень-то сложно!"
    show player 13f
    show dewitt 40 with dissolve
    dewitt "Прекрасно! Вот список песен для концерта. Твоя часть не должна быть очень тяжелой."
    dewitt "Практикуйся каждую ночь, и ты точно будешь готов."
    show dewitt 4 with dissolve
    show player 386f with dissolve
    player_name "Окей, {b}Мисс Девитт{/b}. Так и поступлю!"
    show player 385f
    show dewitt 5
    dewitt "А теперь, если ты не против, продемонстрируй, что ты можешь! Урок уже скоро начнется."
    show dewitt 4
    show player 386f
    player_name "Окей."
    hide player
    hide dewitt
    with dissolve

    scene music_class_cs05
    with fade
    show text "Было немного странно сидеть не в секторе ударных...\n... Но, я думаю, в секторе духовых есть свои плюшки." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label music_classroom_dewitt_talent_show_progress:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Что ж, привет, {b}[firstname]{/b}."
    dewitt "Ты уже начал практиковать фингеринг, который я тебе показала?"
    show dewitt 1
    show player 10f
    player_name "Ф-фингеринг?"
    show player 11f
    show dewitt 8 with dissolve
    dewitt "Ну, на флейте, глупышка."
    show dewitt 4
    show player 17f
    player_name "О-ох, да! Я думаю, что становлюсь неплохим музыкантом."
    show player 14f
    player_name "Вы прекрасный учитель, {b}Ms. Dewitt{/b}!"
    show player 13f
    show dewitt 5
    dewitt "А ты быстро учишься, сладкий."
    show dewitt 11
    dewitt "Я просто надеюсь, что запишется больше учеников. Или нам придется отменить смотр."
    show dewitt 10
    show player 12f
    player_name "До сих пор нет новых добровольцев?"
    show player 5f
    show dewitt 11b
    dewitt "Неа, ни одного."
    show dewitt 12
    dewitt "Я начинаю волноваться, {b}[firstname]{/b}..."
    show dewitt 10b
    show player 14f
    player_name "У нас ещё есть время, {b}Мисс Девитт{/b}."
    player_name "Я уверен, что смогу найти ещё людей!"
    show player 13f
    show dewitt 11
    dewitt "Ты правда это сделаешь?"
    show dewitt 10
    show player 33f
    player_name "Абсолютно!"
    show player 13f
    show dewitt 5
    dewitt "Ох, ты такой милый!"
    show dewitt 4
    show player 14f
    player_name "Хех, просто нужно понять, кого я смогу убедить."
    show player 13f
    show dewitt 3 with dissolve
    dewitt "Удачи, сладкий!"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_get:
    scene music_classroom_c
    show dewitt 4 at left
    show dewitt 4 at Position (xpos=110)
    show player 14f at right
    with dissolve
    player_name "Я нашел ещё двух добровольцев на смотр талантов!"
    show player 13f
    show dewitt 5
    dewitt "Правда?! Кого ты нашел, и на чем они играют?"
    show dewitt 4
    show player 14f
    player_name "Ну, {b}Ева{/b} певица."
    show player 13f
    show dewitt 5
    dewitt "Да ладно! И насколько она хороша?"
    show dewitt 4
    show player 14f
    player_name "У неё просто ангельский голос!"
    show player 13f
    show dewitt 5
    dewitt "Это прекрасно! Кто ещё?"
    show dewitt 4
    show player 14f
    player_name "{b}Кевин{/b} будет играть на гитаре."
    show player 13f
    show dewitt 5
    dewitt "Вот сейчас ты меня впечатлил! Я слышала, что {b}Кевин{/b} очень талантливый."
    show dewitt 4
    show player 14f
    player_name "Да, я тоже слышал только хорошее."
    show player 13f
    show dewitt 5
    dewitt "Боже, {b}[firstname]{/b}! Да ты просто сколотил неплохую группу!"
    show dewitt 8
    dewitt "Хей, а это ведь неплохая идея!"
    show dewitt 4
    show player 10f
    player_name "Ха?"
    show player 5f
    show dewitt 5
    dewitt "Нужно чтобы вы сыграли что-нибудь вместе для завершения смотра!"
    show dewitt 4
    show player 10f
    player_name "Серьёзно?"
    show player 11f
    show dewitt 8
    dewitt "Да! Это будет просто прекрасно!"
    show dewitt 4
    show player 14f
    player_name "Хех, окей. Если вы этого хотите..."
    show player 13f
    show dewitt 5
    dewitt "Ох, вау! Я просто не могу дождаться смотра!"
    show dewitt 23 at Position (xoffset=45) with dissolve
    pause
    show dewitt 22 at Position (xoffset=45) with dissolve
    pause
    show dewitt 27 at Position (xoffset=-119) with dissolve
    pause
    show dewitt 24 at Position (xpos=110) with dissolve

    show player 23f
    player_name "!!!"

    show player 11f
    show dewitt 25 at Position (xoffset=69) with dissolve
    dewitt "Ох! Черт!"
    dewitt "Это моя вина, {b}[firstname]{/b}..."
    dewitt "Мои девчёнки тоже хотели это отпраздновать!"

    show player 14f
    player_name "Хех, всё в порядке."
    show player 13f
    show dewitt 16 with dissolve
    dewitt "Я надеюсь на это, сладкий!"
    dewitt "Может подумаешь о дополнительной награде за твои старания?"
    dewitt "Если мы нормально проведем смотр, мы с тобой можем провести приватную сессию."
    show dewitt 15
    show player 11f
    player_name "*Глоть*."
    show dewitt 8
    dewitt "Оу, ты такой милый!"
    show dewitt 4
    show player 14f
    player_name "Мне, наверное, стоит дальше практиковаться."
    show player 13f
    show dewitt 5
    dewitt "Отличная идея. Ещё раз спасибо, {b}[firstname]{/b}."
    show dewitt 4
    show player 36f with dissolve
    player_name "Пока, {b}Мисс Девитт{/b}."
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_music_sheets:
    scene music_classroom_c
    show kevin 23 zorder 2 at right
    show dewitt 1 zorder 3 at left
    with dissolve
    pause
    show player 13f zorder 1 at Position (xpos=700) with dissolve
    show dewitt 2
    dewitt "О, хорошо, что ты тут, {b}[firstname]{/b}."
    dewitt "А я тут готовила нотные листы."
    show dewitt 1
    show player 10f
    player_name "Нотные листы?"
    show player 5f
    show dewitt 2
    dewitt "Для финального выступления, помнишь?"
    show dewitt 1
    show player 17f
    player_name "Ох, точно."
    show player 13f
    show kevin 26 with dissolve
    kev "Это отличная песня!"
    show kevin 23 with dissolve
    show dewitt 2
    dewitt "Хех, кончено же!"
    show dewitt 3
    dewitt "Вы ведь работаете с мастером своего дела!"
    show dewitt 1
    show player 10f
    player_name "Разве {b}Ева{/b} не должна быть здесь?"
    show player 13f
    show kevin 24
    kev "Она здесь..."
    kev "... то есть, она была здесь."
    show kevin 23
    show dewitt 2
    dewitt "Она пошла взять что-то из своего ящичка."
    show dewitt 1
    show player 14f
    player_name "Ей тоже понравилась песня?"
    show player 13f
    show dewitt 2
    dewitt "Ещё как!"
    show dewitt 1
    show player 14f
    player_name "Ну, тогда всё будут практиковаться, да?"
    show player 13f
    show dewitt 2
    dewitt "Да, и всё благодаря тебе, сладкий!"
    show dewitt 4 with dissolve
    show kevin 24
    kev "Я уже не могу дождаться! Толпа будет просто в восторге!"
    show kevin 23
    show player 11f
    show dewitt 9
    eve "{b}Мисс Девитт{/b}!"
    show eve 2b zorder 0 at Position (xpos=500) with fastdissolve
    eve "Быстрее сюда! Вы не поверите!"
    show eve 1
    show dewitt 11
    dewitt "Что случилось, милая?"
    show dewitt 10
    show eve 2b
    eve "Кто-то произвел акт вандализма в аудитории!"
    show eve 1
    show kevin 24
    show player 23f
    show dewitt 11b
    dewitt "Что!?!"
    show dewitt 10b
    show eve 2b
    eve "Да, тут повсюда граффити!"
    show eve 1
    show player 22f
    hide dewitt with dissolve
    show eve 2bf at Position (xpos=300) with dissolve
    eve "Да ладно!"
    hide player
    hide eve
    hide kevin
    with dissolve
    return

label music_classroom_dewitt_check_up:
    scene music_classroom_c
    show dewitt 9f at left
    show player 10f at right
    with dissolve
    player_name "{b}Мисс Девитт{/b}, вы тут?"
    show player 11f
    show dewitt 9d with dissolve
    dewitt "Да, я прямо тут, сладкий."
    show dewitt 9c
    show player 10f
    player_name "Вы в порядке?"
    show player 11f
    show dewitt 9d
    dewitt "Ох, всё будет в порядке. Я просто немного подавлена в данный момент."
    show dewitt 9f with dissolve
    show player 25f
    player_name "( Хмм, я думаю, ей нужно немного побыть одной. )"
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_find_dewitt:
    scene music_classroom_c
    show dewitt 9f at left
    show player 14f at right
    with dissolve
    player_name "{b}Мисс Девитт{/b}, вы тут?"
    show player 13f
    show dewitt 9d with dissolve
    dewitt "Да, я тут, сладкий."
    show dewitt 9c
    show player 10f
    player_name "Вы в порядке?"
    show player 5f
    show dewitt 9d
    dewitt "Ох, всё будет в порядке. Я просто немного подавлена в данный момент"
    show dewitt 9f with dissolve
    show player 14f
    player_name "У меня для вас сюрприз!"
    show player 13f
    show dewitt 9d with dissolve
    dewitt "Я не в настроении для игр, {b}[firstname]{/b}..."
    show dewitt 9c
    show player 14f
    player_name "Никаких игр. Серьёзно, у меня есть кое-что, что сможет вас утешить!"
    show player 13f
    show dewitt 9d
    dewitt "Ох, ты такой милый."
    show dewitt 9c
    show player 14f
    player_name "Пойдемте со мной!"
    show player 13f
    show dewitt 9d
    dewitt "*Вдох* Ладно, веди меня."
    hide player
    hide dewitt
    with dissolve
    return

label music_classroom_dewitt_talent_show_practice:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Хей, {b}[firstname]{/b}!"
    show dewitt 1
    show player 14f
    player_name "Хей, {b}Мисс Девитт{/b}!"
    show player 13f
    show dewitt 3
    dewitt "Готов попрактиковаться?"
    show dewitt 1
    show player 17f
    player_name "А то!"
    show player 13f
    show dewitt 2
    dewitt "Тогда присаживайся, сладкий."

    scene music_class_cs06
    with fade
    show text "Практиковаться с {b}Кевин{/b} и {b}Ева{/b} было весело!\nМы просто зажжем на  {b}Смотре Талантов{/b}!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene music_classroom_c
    show eve 5 at right
    show kevin 23 at Position (xpos=600)
    show player 14 at left
    with dissolve
    player_name "Это была отличная репетиция. Мы прекрасно звучим!"
    show player 13
    show eve 6
    eve "Да, и это так весело!"
    show eve 5
    show kevin 24
    kev "Жаль, что мы никогда не поиграем..."
    show kevin 24b
    show player 5
    player_name "..."
    show eve 2b
    eve "Хех? О чем ты, {b}Кевин{/b}?"
    show eve 1
    show kevin 24f with dissolve
    kev "{b}Директриса Смит{/b} никогда не допустит этого {b}Смотра Талантов{/b}!"
    kev "{b}[firstname]{/b} и я слышали планы {b}Annie{/b}."
    kev "У них явно есть что-то в рукаве!"
    show kevin 24bf
    show eve 2b
    eve "... Может расскажем {b}Мисс Девитт{/b}?"
    show eve 1
    show kevin 24f
    kev "Зачем, она всё равно ничего не сможет сделать..."
    show kevin 24bf
    show player 10
    player_name "Это просто её расстроит."
    show player 12
    player_name "Мы сами должны разобраться с {b}Директриса Смит{/b}!"
    show player 13
    show kevin 20 with dissolve
    pause
    show kevin 32 with dissolve
    kev "Я за!"
    show kevin 23
    show eve 9f
    eve "..."
    show eve 2b
    eve "Вы серьёзно?"
    eve "{b}Директриса Смит{/b} выгонет нас, если поймет, что мы пытаемся ей помешать..."
    show eve 1
    show kevin 24f with dissolve
    kev "И? Хочешь позволить ей испортить {b}Смотр Талантов Мисс Девитт{/b}?!"
    show kevin 24bf
    show eve 2b
    eve "Я этого не говорила!"
    eve "... Просто... Нам нужно быть аккуратнее! Только и всего."
    eve "Моя {b}сестра{/b}  {b}убьет{/b} меня, если меня исключат!"
    show eve 1
    show player 14
    player_name "Тебе не нужно сюда влезать, {b}Ева{/b}. Мы с {b}Кевином{/b} сами справимся."
    show player 13
    show eve 7
    eve "Пфф, ну да!"
    show eve 6b
    eve "Не могу дождаться того момента, когда услышу ваш глупый план!"
    show eve 6
    eve "Он точно провалится без моих женских уловок!"
    show eve 5
    show player 14
    player_name "Хех, хорошо, С тремя людьми будет намного проще."
    show player 13
    show kevin 9b with dissolve
    kev "Так что за план, {b}[firstname]{/b}?"
    show kevin 23
    show player 10
    player_name "Нужно просто держать {b}Директриса Смит{/b} и {b}Энни{/b} подальше от {b}аудитории{/b}!"
    show player 5
    show kevin 20 with dissolve
    kev "..."
    show eve 2b
    eve "Ты предлагаешь их где-то запереть?"
    show eve 1
    show player 11
    player_name "!!!"
    show player 35
    player_name "А это неплохая идея..."
    show kevin 23 with dissolve
    player_name "Мы можем запереть их в офисе {b}Директриса Смит{/b} до конца {b}Смотра Талантов{/b}!"
    show player 13
    show eve 6
    eve "Видишь, я же говорила - женские уловки!"
    show eve 5
    show kevin 9b
    kev "Да-да... Мы просто поражены. И как именно мы запрем их в офисе?!"
    show kevin 23
    show player 4 with dissolve
    eve "..."
    player_name "..."
    show eve 6b
    eve "Что? Я должна сама всё продумать?!"
    show eve 1
    show player 10 with dissolve
    player_name "Мы не можем их запереть. У Энни есть {b}мастерключ{/b} для всех замков в школе."
    show player 5
    show kevin 24
    kev "... А даже если и нет. {b}Директриса Смит{/b} просто пошлет её через окно за помощью."
    show kevin 23
    show eve 6
    eve "Хаха, да я бы заплатила за это зрелище!"
    show eve 5
    show player 10
    player_name "Значит нам нужно как-то вывести их из строя..."
    show player 5
    show kevin 20 with dissolve
    kev "..."
    show eve 2
    eve "{b}У моей сестры{/b} есть тайзер в магазине... Может просто пальнем в них?"
    show eve 1
    show player 10
    player_name "Это немного перебор, не думаешь?"
    show player 5
    show kevin 21
    kev "Не то что бы {b}Директриса Смит{/b} не заслужила..."
    show kevin 23 with dissolve
    show player 12
    player_name "Никаких тайзеров!"
    show player 10
    player_name "... {b}Директриса Смит{/b} может и истинное зло, но {b}Энни{/b}..."
    player_name "Она просто запуталась."
    show player 5
    show eve 2
    eve "Это единственная идея, которая у меня есть."
    show eve 1
    show player 34
    player_name "..."
    show kevin 22 with dissolve
    kev "Подождите!"
    show player 13
    kev "Вот оно!"
    kev "Помнишь, клей, который мы сделали в классе {b}Мисс Окиты{/b} некоторое время назад?!"
    show kevin 23 with dissolve
    show player 10
    player_name "... Нет?"
    show player 5
    show kevin 9b
    kev "Да, ты же ещё не вернулся в тот момент."
    show kevin 23f with dissolve
    show eve 2
    eve "Я помню."
    show eve 6
    eve "Эта штука была очень липкая! Чтобы нейтрализовать её, нужен растворитель..."
    show eve 1
    show kevin 32f
    kev "Именно!"
    show player 13
    kev "Вспомни, как {b}Декстер{/b} сунул руку ему в лоб?!"
    show kevin 23f
    show eve 6
    eve "Хаха! Да! Это было очень забавно!"
    eve "{b}Мисс Оките{/b} понадобилась 20 минут чтобы от неё избавиться."
    show eve 5
    show player 14
    player_name "Воу! Она настолько мощная?"
    show player 13
    show kevin 32 with dissolve
    kev "Ага! Эта штука просто ужасна!"
    show kevin 23
    show eve 2b
    eve "Помнишь, как её сделать?"
    show eve 1
    show kevin 9bf with dissolve
    kev "Да, вроде бы."
    show kevin 23f
    show player 14
    player_name "И что вы предлагаете?"
    show player 13
    show kevin 9b with dissolve
    kev "Я думаю, что на нужно пробраться в офис {b}Директрисы Смит{/b} ночью и приклеить её стулья к полу."
    kev "Нужно намазать ещё на подушки! Тогда они приклеются и будут сидеть там, пока кто-нибудь их не найдет."
    kev "Даже тогда... Им понадобится растворитель, чтобы освободиться!"
    show kevin 23
    show eve 2b
    eve "Не хочу это признавать... Но это, типа, прекрасно!"
    show eve 5
    show player 17
    player_name "Отличная работа, {b}Кевин{/b}!"
    show player 13
    show kevin 9b
    kev "... Может наши парни не такие уж и тупые."
    show kevin 23
    show eve 2
    eve "Хех, да... Даже сломанные часы дважды в день показывают правильное время."
    show eve 5
    show player 14
    player_name "Так нам нужно где-то достать ингридиенты?"
    show player 13
    show eve 1
    eve "..."
    show kevin 9b
    kev "Не, чувак. Всё, что нам нужно, есть в лаборатории."
    kev "Найди меня там завтра после уроков, и мы замешаем немного!"
    show kevin 23
    show player 14
    player_name "Отлично, нужно будет собраться ещё раз, чтобы отполировать план о наших действиях в офисе {b}Директрисы Смит{/b}."
    player_name "Помните, ничего не говорим {b}Мисс Девитт{/b}. Не хочу, чтобы она снова расстраивалась."
    hide player
    hide kevin
    hide eve
    with dissolve
    pause
    show dewitt 9c with dissolve
    dewitt "..."
    show dewitt 9d
    dewitt "Он хочет сделать всё это, чтобы я не расстраивалась?"
    show dewitt 9f
    dewitt "{b}*Хнык*{/b} Какой прекрасный ребёнок..."
    hide dewitt with dissolve
    return

label dewitt_talent_show_helping_kevin:
    player_name "( Нужно сначала убедить Кевина принять участие в {b}смотре талантов{/b}."
    return

label dewitt_talent_show_helping_eve:
    player_name "( Нужно сначала убедить Еву принять участие в {b}смотре талантов{/b}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
