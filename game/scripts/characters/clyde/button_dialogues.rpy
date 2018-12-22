label button_clyde_pink_beaver:
    scene expression player.location.background_blur with None
    show player 14f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Эй, насчет бобра, которого ты хотел."
    show player 13f
    show clyde 2
    clyde "Да?"
    show clyde 1
    show player 239_240f
    pause
    show player 709f
    player_name "Это он?"
    show player 708f
    show clyde 30
    clyde "!!!"
    show clyde 4 with dissolve
    clyde "Ну, смажь мою попку и назови меня печеньем, ты на самом деле понял!"
    show clyde 3
    show player 709f
    player_name "Я думал, что это может быть."
    show clyde 34
    show player 13f
    with dissolve
    pause
    show clyde 35
    clyde "Как, черт возьми, ты выиграл эту штуку?!"
    show clyde 33 with dissolve
    clyde "Ярмарки не будет еще 2 месяца!"
    show clyde 32
    show player 12f
    player_name "Я купил его в торговом центре, {b}Клайд{/b}."
    show player 5f
    show clyde 2 with dissolve
    clyde "В торговом центре?"
    clyde "А, черт."
    clyde "Я никогда там не был."
    clyde "Куда эта собака убежала сейчас?"
    clyde "Давай, девочка!"
    show clyde 1
    pause
    show player 10f
    player_name "Подожди. Ты никогда не был в торговом центре?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Нет, сэр."
    show clyde 3
    show player 10f
    player_name "Где ты тогда покупаешь продукты?"
    show player 5f
    show clyde 4
    clyde "Пффф, вы горожане и ваши продукты..."
    clyde "Я никому не буду платить за то, что бесплатно прямо здесь, в лесу!"
    show clyde 3
    show player 10f
    player_name "... Ааа?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Я охочусь за едой, приятель."
    show clyde 4 with dissolve
    clyde "Кстати, у меня в хижине есть горшочек тушеной белки."
    clyde "Приходи к нам на ужин!"
    show clyde 3
    show player 12f
    player_name "Йее, нет спасибо."
    show player 5f
    pig "{b}*хрююююю*{/b}"
    show clyde 4
    clyde "Вот ты где!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Где же ты была, моя девочка?!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 38
    with dissolve
    pig "*{b}Хрю{/b}*"
    show clyde 37
    clyde "Посмотри, что {b}[firstname]{/b} принес для тебя!"
    show clyde 38
    pig "{b}*ХРЮЮ ХРЮЮ*{/b}"
    show clyde 37
    clyde "Хехехе, посмотри, как она счастлива!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Иди и повеселись сейчас же!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 3
    with dissolve
    pig "{b}*фырк*{/b}"
    pause
    show clyde 4
    clyde "Теперь это одна счастливая собака."
    clyde "Ладно, парень..."
    show clyde 9 with dissolve
    clyde "Я должен как-то отплатить тебе за это."
    show clyde 3 with dissolve
    show player 12f
    player_name "Не беспокойтесь об этом."
    player_name "Просто считай это подарком."
    show player 5f
    show clyde 4
    clyde "Теперь подожди секунду."
    show clyde 1 with dissolve
    pause
    show clyde 9 with dissolve
    clyde "О!"
    clyde "У меня как раз то, что надо!"
    hide clyde
    hide clyde_hat
    with dissolve
    show player 10f
    player_name "Куда это ты собрался?!"
    show player 5f
    clyde "Подожди здесь!"
    pause
    clyde "Не двигай мышцами!"
    show player 25f
    player_name "О, блин."
    player_name "Правда, хорошо..."
    player_name "Я не-"
    show player 11f
    show clyde 40 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    with dissolve
    clyde "Зацени!"
    show clyde 39
    if player.has_item("mysterious_statue_1"):
        show player 23f
        player_name "!!!"
        show player 30f
        if M_clyde.get("cletus"):
            player_name "{b}Клайд{/b}, Я думал, ты сказал, что ничего не знаешь о статуе своего деда!"
        else:
            player_name "{b}Клетус{/b}, Я думал, ты сказал, что ничего не знаешь о статуе своего деда!"
        show player 90f
        show clyde 40
        clyde "О, точно."
        clyde "Я ведь это и сказал, не так ли?"
        show clyde 39
        pause
        show clyde 11 with dissolve
        clyde "Ну, я просто соврал."
        show clyde 12
        show player 12f
        player_name "Почему?!"
        show player 90f
    else:

        player_name "!!!"
        show player 30f
        player_name "Что это за хрень?"
        show player 5f
        show clyde 40
        clyde "Ну, это принадлежало моему дедушке."
        show clyde 39
        show player 10f
        player_name "Твоему дедушке?!"
        show player 5f
        show clyde 9 with dissolve
        clyde "Точно!"
        clyde "Оле {b}Джебедия Дельмонт{/b} вообще-то!"
        show clyde 3
        pause
        player_name "..."
        show clyde 2 with dissolve
        clyde "Ты никогда не слышал о {b}Джебедия Дельмонте{/b}?"
        show clyde 1
        show player 10f
        player_name "Нет?"
        show player 5f
        show clyde 2
        clyde "{b}*вздыхая*{/b} Боже мой."
        show clyde 4 with dissolve
        clyde "Он славился в этих краях своими коровами и их восхитительным молоком!"
        clyde "Он побеждал во всевозможных конкурсах."
        show clyde 3
        show player 10f
        player_name "Он был молочным фермером?"
        show player 5f
        show clyde 4
        clyde "Ну, он не просто занимался молочной фермой."
        clyde "У него были разные животные."
        show clyde 9 with dissolve
        clyde "Видели бы вы куриные яйца, которые он приносил на ярмарку."
        clyde "Они были размером с футбольный мяч!"
        show clyde 3 with dissolve
        show player 10f
        player_name "Да ну?"
        show player 5f
        show clyde 4
        clyde "Хе, да, чувак!"
        show clyde 3
        pause
        show player 17f
        player_name "Звучит потрясающе!"
        show player 14f
        player_name "Расскажи больше."
        show player 13f
        show clyde 11 with dissolve
        clyde "О, нет. Я эээ-"
        clyde "{b}*ммммм*{/b} Я правда не хочу в это ввязываться..."
        show clyde 12
        show player 10f
        player_name "Хух, почему нет?"
        show player 5f
    show clyde 11
    clyde "Слушай, приятель, мой дедушка не совсем гордость {b}семьи Дельмонт{/b}..."
    clyde "Мы не любим об этом говорить!"
    show clyde 12
    show player 10f
    player_name "Почему?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*вздыхая*{/b} Давайте просто скажем, что Оле' {b}Джебедия{/b} был немного тронутый, хорошо?"
    show clyde 1
    show player 10f
    player_name "Был немного тронутый?"
    show player 5f
    show clyde 2
    clyde "Ну ты понимаешь."
    clyde "У него нехватало несколько винтов."
    show clyde 1
    show player 10f
    player_name "Эээ..."
    show player 5f
    show clyde 9 with dissolve
    clyde "Его колесо поворачивалось, но хомяк был мертв."
    show clyde 3 with dissolve
    show player 10f
    player_name "Я не..."
    show player 5f
    show clyde 4
    clyde "Ему не хватило нескольких карт до полной колоды."
    show clyde 3
    show player 12f
    player_name "О чем ты говоришь?!"
    show player 5f
    show clyde 26 with dissolve
    clyde "Ччч, он был более сумасшедшим, чем горшок с портой на фестивале арахиса, хорошо ?!"
    show clyde 25
    show player 12f
    player_name "Ты хочешь сказать, он был сумасшедшим?"
    show player 5f
    show clyde 26
    clyde "Вот что я хочу сказать..."
    show clyde 25
    show player 10f
    player_name "О."
    show player 5f
    show clyde 2
    clyde "Да."
    clyde "Мама говорит, он всегда был немного эксцентричным."
    clyde "Люди в крике называли его волшебником."
    show clyde 1
    show player 10f
    player_name "Он был волшебником?"
    show player 5f
    show clyde 2
    clyde "Да, но он был не очень хорошим парнем."
    clyde "Помню, однажды он пытался превратить меня в жабу, потому что я ушел и застрял головой на лестнице."
    show clyde 1
    show player 10f
    player_name "У тебя голова застряла на лестнице?!"
    show player 5f
    show clyde 2
    clyde "Мой брат сказал мне, что под лестницей живет лепрекон, а я хотел его увидеть."
    show clyde 1
    show player 17f
    player_name "Пффф, хахаха!"
    show player 13f
    show clyde 2
    clyde "В любом случае, его заклинание не сработало."
    show clyde 11 with dissolve
    clyde "Поэтому маме пришлось смазать меня беконным жиром и вытащить."
    show clyde 12
    show player 17f
    player_name "Хаха!"
    show player 13f
    show clyde 4
    clyde "Потом был один раз, когда я завалил второй класс..."
    clyde "... И дедушка, он сказал, \"Не волнуйся, маленький {b}Клайд{/b}. Дедушка все исправит для тебя.\""
    show clyde 3
    pause
    show player 14f
    player_name "Ладно, и что случилось?"
    show player 13f
    show clyde 2 with dissolve
    clyde "Ну, я не совсем помню. Они вроде нашли его в школе, посреди ночи, голым и покрытым куриной кровью."
    show clyde 1
    show player 23f
    player_name "Куриной кровью?!"
    show player 11f
    show clyde 2
    clyde "Да, он сказал, что выполняет какую-то ритуальную штуку, чтобы помочь мне с учебой."
    clyde "По-видимому, он хулиганил, кричал и продолжал."
    show clyde 1
    show player 10f
    player_name "Да, звучит немного безумно, {b}Клайд{/b}."
    show player 12f
    show clyde 2
    clyde "Да, я думаю, что так и было."
    clyde "Хотя он был славным парнем."
    clyde "Жаль, что все злые духи на него разозлились."
    show clyde 1
    show player 10f
    player_name "Злые духи?"
    show player 11f
    show clyde 2
    clyde "Да, он рассказал мне об этом сразу после того, как разбил эту статую и спрятал осколки."
    clyde "Сказал, что они придут за ним и он хочет, чтобы она была в безопасности."
    show clyde 1
    show player 10f
    player_name "Они?"
    show player 5f
    show clyde 40 with dissolve
    clyde "Дама в статуе, конечно!"
    clyde "Он был очень расстроен, что спрятал ее."
    clyde "В конце концов, она была его талисманом."
    show clyde 39
    show player 12f
    player_name "Странный."
    show player 5f
    show clyde 9 with dissolve
    clyde "Потом мы поймали его на блуде со скотом, и мама отправила его в психушку."
    show clyde 3 with dissolve
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Ты хочешь сказать он-"
    player_name "С животными?!"
    show player 37f
    show clyde 11
    with dissolve
    clyde "{b}*вздыхая*{/b} Да, тоже плачу как ребенок."
    clyde "Эти духи Муста действительно сделали с ним многое, бедняга."
    show clyde 12
    show player 10f with dissolve
    player_name "И эээ..."
    player_name "... Твой дедушка все еще живет в психушке?"
    show player 5f
    show clyde 2 with dissolve
    clyde "А, нет."
    clyde "Примерно через две недели после того, как мама отправила его туда, его комната загорелась, и он погиб в ней."
    show clyde 1
    show player 24f
    player_name "Боже..."
    show clyde 2
    clyde "Они не знают, как начался пожар, но я думаю, что духи, наконец, добрались до него."
    show clyde 1
    player_name "Я даже не знаю..."
    player_name "..."
    show clyde 30
    clyde "Да, это было очень грустно..."
    show clyde 29
    pause
    show player 11f
    show clyde 2
    clyde "В любом случае!"
    show player 5f
    show clyde 40 with dissolve
    clyde "Думаю, он не будет возражать, если я отдам тебе этот кусок статуи."
    clyde "Видя, как ты помог мне и все такое."
    clyde "Кто знает, может, и тебе повезет."
    show clyde 39
    show player 10f
    player_name "Точно."
    player_name "Спасибо, наверно..."
    show player 715f
    show clyde 9
    with dissolve
    clyde "Не упоминай об этом, приятель!"
    show player 5f with dissolve
    clyde "А теперь прошу меня извинить."
    clyde "Я хочу посмотреть, как моя собака даст этому бобру то, что нужно!"
    hide clyde
    hide clyde_hat
    with dissolve
    clyde "Хехехе."
    show player 239_240f with dissolve
    pause
    show player 715f with dissolve
    player_name "( Ну, это многое объясняет насчет {b}Клайда{/b} и почему он такой, какой есть... )"
    pause
    player_name "( Думаю, я должен поискать другие части этой статуи. )"
    hide player with dissolve
    return

label button_clyde_mysterious_statue_1:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 688cf
    player_name "Ты знаешь что-нибудь об этом {b}Клайд{/b}?"
    show player 688bf
    show clyde 30
    clyde "{b}*вздыхая*{/b} Где ты это нашел?!"
    show clyde 29
    show player 688cf
    player_name "Он был похоронен под домом моих друзей."
    show player 688bf
    pause
    show player 688cf
    player_name "Имя {b}Делмонт{/b} выгравировано внизу."
    show player 688bf
    show clyde 2
    clyde "Да."
    show clyde 4 with dissolve
    clyde "Это часть талисмана моего дедульки."
    show clyde 3
    show player 688cf
    player_name "Дедульки?"
    player_name "Ты имеешь в виду своего дедушку?"
    show player 13f with dissolve
    show clyde 4
    clyde "Ага, {b}Джебедия Делмонт{/b}."
    clyde "Он был очень известен в этих краях много лет назад молоком, которое производили его коровы."
    show clyde 3
    show player 10f
    player_name " Коровье молоко?"
    show player 5f
    clyde "Мммммм."
    show clyde 4
    clyde "Это было восхитительно!"
    clyde "Выиграл с ним кучу конкурсов."
    show clyde 3
    show player 14f
    player_name "Это довольно круто."
    show player 13f
    show clyde 4
    clyde "У него также были удивительные куриные яйца."
    clyde "Они были большими, как футбольный мяч!"
    show clyde 3
    pause
    show player 12f
    player_name "Ага..."
    show player 5f
    pause
    show player 10f
    player_name "Ну и..."
    player_name "Ты знаешь, где может быть другая часть этой статуи?"
    show player 5f
    show clyde 11 with dissolve
    clyde "Нет!"
    show clyde 12
    pause
    show player 10f
    player_name "О, потому что я просто подумал-"
    show player 5f
    show clyde 9 with dissolve
    clyde "Извини, приятель, ничем не могу помочь!"
    clyde "Я ничего не знаю!"
    show clyde 3 with dissolve
    show player 10f
    player_name "Хорошо..."
    show player 24f
    player_name "В любом случае спасибо, я думаю."
    show player 5f
    show clyde 1 with dissolve
    return

label button_clyde_mysterious_statue_2:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 715bf with dissolve
    player_name "Есть идеи, где я могу найти еще от этой статуи?"
    show player 715cf
    show clyde 2
    clyde "Эээ, наврятли."
    clyde "Зная дедушку, последний кусок, вероятно, {b}найдет тебя{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "Что ты имеешь в виду?"
    show player 5f
    show clyde 2
    clyde "Да, я думаю, я бы мог {b}найти хорошее удобное место, чтобы расслабиться{/b}..."
    clyde "... {b}где-то рядом с пляжем, может быть{/b}."
    show clyde 1
    pause
    show clyde 2
    clyde "Бьюсь об заклад, {b}что голова всплывет сама по себе{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "Эээ, ладно..."
    player_name "Ну, спасибо. Я думаю..."
    show player 5f
    show clyde 9 with dissolve
    clyde "Без проблем, приятель."
    show clyde 1 with dissolve
    return


label button_clyde_your_dog:
    scene expression player.location.background_blur with None
    show player 10f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Итак, о вашей собаке..."
    show player 5f
    show clyde 4 with dissolve
    clyde "Ах да, она хорошая девочка, не так ли?"
    show clyde 3
    show player 10f
    player_name "Да, конечно."
    show player 12f
    player_name "Ты ведь понимаешь, что она не собака, правда?"
    show player 5f
    show clyde 4
    clyde "Лучшая собака в моей жизни!"
    show clyde 3
    show player 24f
    player_name "{b}*вздох*{/b}"
    show player 5f
    show clyde 4
    clyde "Вот почему я так усердно тренируюсь, чтобы завоевать ей одного из этих {b}чучел бобров{/b} на ярмарке."
    show clyde 3
    show player 12f
    player_name "Да, ты упоминал об этом."
    show player 10f
    player_name "Почему бы тебе просто не купить ее одну?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Пф, теперь ты говоришь как сумасшедший..."
    clyde "Думаешь, {b}розовые бобры{/b} растут на деревьях или что-то вроде того?"
    show clyde 3 with dissolve
    show player 10f
    player_name "Цвет действительно имеет значение?"
    show player 5f
    show clyde 4
    clyde "Черт возьми, конечно имеет значение!"
    clyde "{b}Розовые бобры{/b} самые лучшие бобры."
    show clyde 9 with dissolve
    clyde "Все знают это!"
    show clyde 3 with dissolve
    show player 402f
    player_name "... Точно."
    show player 10f
    player_name "Ладно, удачи тебе во всем этом..."
    show player 5f
    show clyde 4
    clyde "\"Удача\" это мое второе имя, брат."
    show clyde 3
    pause
    show clyde 2 with dissolve
    clyde "Вообще-то это Корнелиус."
    show clyde 1
    show player 12f
    player_name "А?"
    show player 5f
    show clyde 2
    if M_clyde.get("cletus"):
        clyde "{b}Клетус Корнелиус Делмонт{/b}."
    else:
        clyde "{b}Клайд Корнелиус Делмонт{/b}."
    show clyde 1
    show player 10f
    player_name "Твое второе имя - Корнелиус?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да приятель."
    clyde "Как тот старатель на шоу летающих оленей."
    show clyde 4
    clyde "Ты видел хотябы одно?!"
    show clyde 3
    show player 10f
    player_name "Не думаю..."
    show player 5f
    show clyde 4
    clyde "Чувааак, оно великолепно!"
    show clyde 3
    show player 10f
    player_name "Ты странный парень, {b}Клайд{/b}."
    show player 5f
    show clyde 4
    clyde "Ага!"
    show clyde 1 with dissolve
    return

label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Нам нужно поговорить об этой ситуации с {b}Кристалл{/b}."
    show player 5f
    show clyde 22
    clyde "Я бы предпочел не..."
    show clyde 21
    show player 10f
    player_name "{b}Клайд{/b}, они собираются отправить ее в тюрьму и забрать трейлер!"
    show player 5f
    show clyde 26
    clyde "Послушай дорогой! Ты думаешь что я не знаю об этом!"
    clyde "Я сожалею, но я ничего не могу, я не могу это прекратить!"
    show clyde 25
    show player 12f
    player_name "Ты можешь сдаться..."
    show player 5f
    show clyde 22
    clyde "Да точно..."
    clyde "Тогда мы оба и окажемся за решёткой!"
    show clyde 21
    show player 10f
    player_name "Нет, если ты скажешь им, что {b}Кристалл{/b} понятия не имела, что ты спрятал там наркотики."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... И зачем мне это?"
    show clyde 1
    show player 12f
    player_name "... Потому что это будет правильным решением!"
    show player 90f
    show clyde 2
    clyde "Пффф."
    clyde "Я не хочу попасть в тюрьму!"
    clyde "Красивому парню как я, эти животные сожрут меня заживо."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Смотри чувак. Она взяла вину на себя, потому что она твоя семья."
    player_name "... Но это было гораздо хуже чем она думала!"
    player_name "Она может изчезнуть на долгое время и {b}Рокси{/b} потеряет свою {b}Маму{/b} и свой дом."
    show player 12f
    player_name "{b}Рокси{/b} не сделала ничего, чтобы заслужить это!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Ох, дерьмо! Ты прав."
    clyde "{b}Роксанна{/b} не должна страдать по моей вине..."
    clyde "... Но Я не вернусь обратно в тюрьму! ... Нет, сэр!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "Что если бы ты послал своё признание в письменном виде?"
    player_name "Расскажи им о своей хижине и пусть они придут и найдут доказательства."
    player_name "Если ты все сделаешь правильно, ты можешь быть уже далеко до того,как они начнут тебя искать."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "Наверное, я мог бы вернуться в долину..."
    clyde "Они никогда не смогут найти меня там."
    clyde "... Я уверен что точно буду скучать по {b}Тете Кристалл{/b} все-таки..."
    show clyde 21
    show player 10f
    player_name "Ты спасешь её из тюрьмы, мужик."
    show player 5f
    show clyde 22
    clyde "Хмм, Я думаю у тебя хороший план."
    show player 13f
    clyde "Значит, я сделаю это, и она выйдет безнаказанной?"
    show clyde 21
    show player 12f
    player_name "... Мы все ещё должны прийти с деньгами за её залог, но для начала неплохо."
    show player 5f
    show clyde 22
    clyde "Сколько денег тебе нужно?"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Мда."
    clyde "Ну, я могу это сделать!"
    show clyde 1
    show player 10f
    player_name "Что?!" with hpunch
    player_name "Ты же не серьезно..."
    player_name "У тебя есть $50,000 завалявшиеся где-то?"
    show player 11f
    show clyde 2
    clyde "Не совсем."
    show clyde 4 with dissolve
    clyde "... Но у меня есть целая куча метамфитомина."
    clyde "Этого будет достаточно что бы получить $100,000 с хорошего покупателя, Я думаю."
    show clyde 3
    show player 10f
    player_name "Это безумие."
    player_name "Ты реально можешь продать его?"
    show player 5f
    show clyde 4
    clyde "Пффф! Да ладно дружище..."
    clyde "Ты хоть знаешь с кем ты разговариваешь?"
    clyde "Я могу продать эскимо с кетчупом девушке в белых перчатках!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Замороженый кетчуп?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да, дружище!"
    show clyde 3 with dissolve
    show player 14f
    player_name "... Когда ты сможешь это сделать?"
    show player 13f
    show clyde 4
    clyde "Хммм, мне нужно будет позвонить моему покупателю."
    clyde "... Но очень скоро, я думаю."
    show clyde 3
    show player 14f
    player_name "Мне надо рассказать {b}Рокси{/b} хорошие новости!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]Ты просто трус!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Эй, тебе не надо называть меня {b}меня{/b} трусом!"
    clyde "[chr_warn]Ты не предстовляешь себе какого это быть в тюрьме для кого то вроде меня!"
    clyde "[chr_warn]Я когда-то был там однажды и будь я проклят если бы я не вернулся назад."
    show clyde 25
    show player 15f
    player_name "[chr_warn]Неважно... {b}ТРУС{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Да пошел ты!"
    clyde "[chr_warn]Я не приму это!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Угх, забей!"
    show player 90f
    show clyde 22
    clyde "Да, это именно то, что я планирую сделать!"
    clyde "Я так кумекаю, шо энто пивко к концу банки и так всю память начисто отшибет!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Когда ты сможешь продать этот Мет?"
    show player 5f
    show clyde 2
    clyde "Притормози конец, парень!"
    clyde "Это требуем времени."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Просто иди и скажи моей сладкой {b}кузине{/b}, что {b}Клайд{/b} позаботитьтся обо всем!"
    show clyde 1
    show player 14f
    player_name "... Верно."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Ты уже связался со своим покупателем?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Да, приятель!"
    show player 13f
    clyde "Я намериваюсь заключить с ним сделку!"
    show clyde 3
    show player 12f
    player_name "{b}Рокси{/b} сказала, что ты не торгавал Метом раньше!"
    show player 90f
    show clyde 26 with dissolve
    clyde "Что?!"
    clyde "Она ничего не знает!"
    clyde "У меня было много таких сделок!"
    show clyde 25
    show player 12f
    player_name "Ты на самом деле имел дело с покупателями раньше?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Ну, я видел как {b}Тетя Кристалл{/b} делала это много раз!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Вздох*{/b} Я пойду с тобой."
    show player 90f with dissolve
    show clyde 2
    clyde "Хм?"
    clyde "Что ты знаешь о продаже наркотиков?!"
    show clyde 1
    show player 12f
    player_name "Ни черта не смыслю в этом."
    player_name "... Но Я точно знаю, что ты определенно недостаточно компетентен, чтобы сделать это в одиночку."
    show player 90f
    show clyde 22
    clyde "Ну, это не... Подожди секунду, что ты имел в виду?!"
    show clyde 1
    show player 12f
    player_name "... Именно."
    show player 90f
    show clyde 2
    clyde "Ччч, Неважно, парень."
    clyde "Пойдешь или не пойдешь. Это не важно для меня!"
    show clyde 26
    clyde "... Но если ты пойдешь то лучше бы тебе {b}встретиться со мной в трейлире вечером{/b}."
    clyde "Ты понял?"
    show clyde 1
    show player 12f
    player_name "Да, я понял."
    player_name "Увидимся {b}сегодня в трейлере Рокси{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Мы все по прежнему хороши что бы продавать мет?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Уверен"
    clyde "Просто будть здесь {b}вечером{/b}, если увязался со мной."
    show clyde 3
    show player 12f
    player_name "Да, понял."
    player_name "Увидимся {b}вечером{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Ты готов идти?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Ты одел это?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "Что не так с моей одеждой?"
    show player 5f
    show clyde 2
    clyde "Ого... Не знаю, приятель. Ты выглядишь ужасно подозрительно..."
    clyde "Я уверен, что ни за что не куплю наркотики у кого-то похожего на тебя."
    show clyde 1
    show player 10f
    player_name "Ну, у меня другой одежды не было..."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Подожди секунду. У меня есть кое что получше для тебя!"
    hide clyde with dissolve
    show player 12f
    player_name "... Это будет интересно."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Давай парень..."
    clyde "Не заставляй нас опоздать!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Я не верю что ты уговорил меня надеть это..."
    player_name "Я чувствую себя глупо!"
    show player 90f
    show clyde 4
    clyde "Шшш, не будь глупцом."
    clyde "Ты похож на настоящего торговца!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Покупатель может придти с секунды на секунду."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Клайд{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Когда ты вернешься в город?!"
    show player 5f
    show clyde 2
    clyde "Эээ, прости приятель."
    clyde "Ты ошибся приятеля..."
    show clyde 1
    show player 10f
    player_name "Хм?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Меня зовут {b}Клетус{/b}!"
    clyde "Рад познакомиться с тобой!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "О чем ты говоришь, {b}Клайд{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Кгхм*{/b} Ешё раз..."
    clyde "Мое имя не {b}Клайд{/b}... а {b}Клетус{/b}."
    show clyde 1
    show player 12f
    player_name "... Но ты так похож на кузена {b}Рокси{/b}, {b}Клайда{/b}."
    show player 5f
    show clyde 2
    clyde "Хмм, что ж извини. Я не знаю этого человека {b}Клайда{/b}."
    show clyde 9 with dissolve
    clyde "Тем не менее это звучит так как будто он красивый сукин сын!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Ты что сейчас прикалываешься надо мной?!"
    show player 13f
    show clyde 4
    clyde "Позвольте спросить у вас..."
    clyde "Этот {b}Клайд{/b} носит шляпу?"
    show clyde 3
    show player 10f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Ну, тогда проехали!"
    clyde "Как вы можете видеть... Клетус никогда никуда не уходит без своей верной шляпы!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Это так странно."
    show player 12f
    player_name "Мне нужно идти."
    show player 5f
    show clyde 4
    clyde "Ладно. Что ж, рад был с тобой познакомиться, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "Я тебе не говорил своего имени!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Ох, ээээ..."
    clyde "... Ну, я..."
    show clyde 11 with dissolve
    clyde "Эммм... Телепатия!"
    show clyde 12
    show player 10f
    player_name "Хмм?!"
    show player 5f
    show clyde 11
    clyde "Я, {b}Клетус{/b}... Я телепат."
    show clyde 4 with dissolve
    clyde "... И я могу прочесть твои мысли силой вввволи!"
    show clyde 3
    show player 10f
    player_name "Мои мысли?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да точно, парень!"
    show clyde 4 with dissolve
    clyde "Так что не говори людям, что я здесь."
    clyde "Потому что я знаю..."
    clyde "Особенно, если эти будет полиция."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Я..."
    player_name "... Только..."
    player_name "... Пока."
    hide player with dissolve
    pause
    show clyde 4
    clyde "До скорого, парень!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Я могу тебе помочь?"
    show clyde 1
    show player 10f
    player_name "Эммм, нет?"
    show player 5f
    show clyde 22
    clyde "О чувак. Ты один из демократов, Иисус любит тебя??"
    show clyde 21
    show player 12f
    player_name "Что?! Нет!"
    show player 5f
    show clyde 26
    clyde "{b}*Задыхаясь*{/b} Ты что коп?!"
    clyde "Ты должен мне сказать, такие правила!"
    show clyde 25
    show player 12f
    player_name "Нет мужик... Мы познакомились только прошлой ночью!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "Я помогал {b}Рокси{/b} с домашним заданием?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Ох, да наверное!"
    clyde "Ты новый парень {b}Рокси{/b}!"
    show clyde 3
    show player 10f
    player_name "Нет, мы только друзья-"
    show player 5f
    show clyde 4
    clyde "Как дела, брат?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "Как дела, брат?!"
    show clyde 3
    show player 14f
    player_name "Ох, привет {b}Клайд{/b}..."
    show player 5f
    show clyde 4
    clyde "Что ты здесь делаешь?!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "И так {b}Клетус{/b}, верно?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Ты прав, парень!"
    show clyde 4 with dissolve
    clyde "Чем я могу тебе помочь?!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Вздох*{/b} У меня все в порядке."
    player_name "Как дела?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Много того, что никто не делает!"
    clyde "Хахаха, знаешь что я имею в виду, брат?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "'Потому что у меня был весь секс... с девушками..."
    clyde "{b}*Кгхм*{/b} человеческими девушками."
    show clyde 12
    show player 12f
    player_name "Да, я понял, {b}Клайд{/b}..."
    show clyde 9 with dissolve
    clyde "Хех, конечно ты!"
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Я никогда не слышал, чтобы кто-то говорил так, как ты, {b}Клайд{/b}..."
    show player 12f
    player_name "В общем откуда ты?"
    show player 5f
    show clyde 4
    clyde "Потому что все вы, городские, говорите странно!"
    clyde "Там в низу в долине, мы все так разговариваем..."
    show clyde 3
    show player 10f
    player_name "... В долине?"
    show player 5f
    show clyde 4
    clyde "Да."
    show clyde 3
    show player 10f
    player_name "Что это?!"
    show player 5f
    show clyde 4
    clyde "Эмм, где я вырос. Ясень пень!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "Это в нескольких округах севернее от сюда."
    clyde "На холмах."
    show clyde 3
    show player 10f
    player_name "Я думал, что на севере сплошные леса."
    show player 5f
    show clyde 4
    clyde "Да, довольно много..."
    show clyde 3
    show player 12f
    player_name "Люди живут там?"
    show player 5f
    show clyde 4
    clyde "Да, большая часть моей семьи все еще живет там."
    clyde "Я думал, что перееду сюда с {b}Тетушкой Кристалл{/b}, чтобы произнести заклинание."
    clyde "Дайте городской жизни справедливую встряску."
    show clyde 3
    show player 10f
    player_name "И как получается?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ээээ, есть свои плюсы и минусы."
    clyde "Я скучаю по родному самогону дома и по всей травке."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Но я и тут готовлю убойные блюда!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "И что ты готовишь?"
    show player 5f
    show clyde 22
    clyde "Э-э-э... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Курицу!"
    show clyde 4 with dissolve
    clyde "Хех, да! Я готовлю жареных цыплят!"
    clyde "Вы, городские, просто не можете насытиться..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "Мне нужно идти..."
    show player 5f with dissolve
    show clyde 4
    clyde "Ага, хорошо."
    clyde "Продолжим в следующий раз, братишка!"
    clyde "Ууу!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "Что у тебя там происходит?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Эээ, извини бро."
    clyde "В эту лачугу строго запрещается заходить!"
    show clyde 9 with dissolve
    clyde "Если только у тебя нет женских прелестей?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Хех, что ж запомни это... Если хижина качается, лучше не стучать!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?!"
    show clyde 3
    show player 401f
    player_name "... Да. несмотря на то что мне бы очень хотелось..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Хороший трактор."
    show player 13f
    show clyde 4
    clyde "Ох, да!"
    clyde "Это {b}Большая Берта{/b}!"
    clyde "Разве она не красавица?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Я сам её построил из остатков металлолома."
    clyde "31.2 лошадиных сил, 2500 об/мин, 8.5 галлонов..."
    clyde "... И только посмотри на этот рубиново красный завершение!"
    clyde "Мммм! Она самая сексуальная вещь на четырех колесах!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "На самом деле, неважно."
    player_name "... Может быть в другой раз?"
    show player 5f
    show clyde 4
    clyde "Пф, Черт возьми да, братишка!"
    clyde "Ты знаешь где меня найти."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Давай, {b}Клайд{/b}! Я знаю это ты!"
    show player 16f
    show clyde 4
    clyde "Я не понимаю о чем ты говоришь..."
    show clyde 3
    show player 15f
    player_name "Это глупо, я никому не скажу, что ты вернулся..."
    show player 16f
    show clyde 4
    clyde "Что ты там куришь, приятель?"
    show player 428f
    clyde "Меня зовут {b}Клетус{/b}, и я здесь впервые."
    clyde "Навсегда."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "Он по-прежнему пишет {b}Клайд{/b} над вашим текстовым полем!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Эй!"
    clyde "Не ломай все стены!"
    clyde "Это обман!"
    clyde "Моё имя {b}Клетус{/b}!!!"
    show clyde 26
    clyde "Скажи это!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Давай, ты знаешь что хочешь сказать это..."
    show clyde 1
    show player 24f
    player_name "{b}*Вздох*{/b}"
    show player 25f
    player_name "{b}Клетус{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "Вот так!"
    clyde "Это было не так сложно, правда?!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
