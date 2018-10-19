label kitchen_sis_telescope_1:
    scene homekitchen
    show player 1 at left
    show debbie 2 at right
    with dissolve
    deb "Привет, милый!"
    deb "Хочешь позавтракать?"
    show debbie 51 at Position(xpos=1025)
    show player 10
    player_name "Не думаю, что у меня есть время, {b}[deb_name]{/b}."
    if game.timer.is_weekend():
        player_name "Я должен встретиться с {b}Эриком{/b}..."
    else:
        player_name "Желательно ещё и в школу не опоздать."
    show player 11
    show debbie 52
    deb "Милый, ты должен поесть!"
    show player 11
    if game.timer.is_weekend():
        deb "Мне не важно, что {b}Эрик{/b} будет ждать тебя..."
    else:
        deb "Мне не важно, будут ли звонить из школы, жалуясь на то, что ты опоздал..."
    show player 1
    deb "Но ты не можешь уйти с пустым животом!"
    show player 14
    show debbie 51
    player_name "Ладно, я думаю, что у меня есть пара минут, чтобы перекусить..."
    show player 1
    show debbie 2
    deb "В {b}столовой{/b} тебя ждет несколько тостов."
    hide player
    hide debbie
    with dissolve
    return

label kitchen_mom_start:
    scene expression game.timer.image("homekitchen{}")
    show player 1 at left with dissolve
    show debbie 2 at right with dissolve
    deb "Доброе утро, любимый! Я приготовила тебе завтрак!"
    deb "Для первого дня в школе я приготовила тебе что-то особенное."
    show player 2
    show debbie 1
    player_name "Спасибо, {b}[deb_name]{/b}, но я не очень голоден да и в школу опаздываю. Так что..."
    show player 1
    show debbie 2
    deb "Ты уверен? Я сделала твои любимые..."
    deb "Улыбающиеся блинчики с тремя кусочками бекона!"
    show debbie 1
    show player 10
    player_name "О боже..."
    show player 11
    player_name "..."
    show player 10
    player_name "Нет, я правда..."
    player_name "Я думаю, что {b}Эрик{/b} опять проспал, а я не хочу опаздывать в первый же день."
    show player 11
    show debbie 3
    deb "Ха, опять?"
    show player 1
    show debbie 2
    deb "Ну тогда тебе следует поспешить."
    show player 2
    show debbie 1
    player_name "Да, всё равно спасибо, {b}[deb_name]{/b}!"
    show player 1f with dissolve
    show debbie 2
    deb "Ничего страшного, Милый- Ой! Подожди!"
    show player 1 with dissolve
    player_name "Хмм?"
    show debbie 3
    deb "Я почти забыла!"
    show debbie 2
    deb "Я вчера говорила с моей подругой, {b}Дианой{/b}, и она сказала, что летом ей может понадобиться {b}помощь с садом{/b}!"
    show player 10
    show debbie 1
    player_name "Хмм, я знаю не так много о садоводстве, {b}[deb_name]{/b}..."
    show player 11
    show debbie 3
    deb "Да ладно, это же просто! {b}Диана{/b} всему тебя научит, а может ещё и заплатит, если будешь стараться!"
    show debbie 2
    deb "Это может стать неплохим способом {b}заработать денег на коледж{/b}, что думаешь?"
    show player 10
    show debbie 1
    player_name "Да, думаю, ты права."
    show player 2
    player_name "Я зайду к ней и спрошу, чем могу помочь."
    show debbie 2
    deb "Это мой мальчик!"
    hide player
    show debbie 4b
    with dissolve
    deb "Я понимаю, что последние недели были непростыми..."
    deb "Но твой {b}отец{/b} хотел бы, чтобы ты был сильным."
    deb "Ты справишься с этим. Я обещаю, скоро всё наладится."
    show debbie 5b
    player_name "Да, я знаю. Спасибо {b}[deb_name]{/b}..."
    deb "Выше нос, милый! Я буду рядом."
    hide debbie with dissolve
    return

label kitchen_mom_dinner:
    scene location_home_kitchen_day_blur
    show debbie 2 at right with dissolve
    show player 203 at left with dissolve
    deb "А вот и ты!"
    show debbie 3
    deb "Мне нужна твоя помощь..."
    show debbie 2
    show player 11
    deb "Моя подруга {b}Диана{/b} прийдет сегодня на ужин."
    deb "... Тебе нужно пойти на {b}пристань{/b} и купить {b}морскую форель{/b}."
    deb "Я хочу приготовить ей что-нибудь особенное, а морскую форель она как раз очень любит!"
    show debbie 1
    show player 2
    player_name "Ох, {b}Диана{/b} сегодня придет? Это приятный сюрприз!"
    player_name "Ей будет полезно хоть не на долго выйти из дома..."
    player_name "Я переживавю за неё... Она там совсем одна."
    player_name "Я зайду на {b}пристань{/b} на обратном пути и возьму {b}форель{/b}."
    scene homekitchen
    show player 1 at left
    show debbie 62 at right
    with dissolve
    deb "{b}[firstname]{/b}, пока ты тут, можешь посмотреть на кое-что?"
    show player 14
    show debbie 61
    player_name "Конечно, {b}[deb_name]{/b}. Что тебе нужно?"
    show player 1
    show debbie 62
    deb "Я купила немного одежды для сегодняшнего вечера, мне хотелось бы узнать твое мнение."
    deb "Я сейчас быстро всё надену."
    hide debbie with dissolve
    scene home_livingroom_b
    show player 14
    player_name "Я хочу увидеть {b}[deb_name]{/b} при параде!"
    show player 11
    deb "Милый!"
    deb "Я готова!"
    show player 2
    player_name "Уже иду!"
    hide player with dissolve
    return

label kitchen_mom_dinner_fish:
    scene location_home_kitchen_day_blur
    show player 13 at left
    show debbie 1 at right
    with dissolve
    player_name "Хэй, {b}[deb_name]{/b}. Я купил {b}рыбу{/b}, которую ты хотела."
    show player 2
    deb "Спасибо, милый, теперь я могу закончить готовить ужин."
    show debbie 2
    deb "Я скажу тебе, когда всё будет готово."
    show player 203

    scene expression L_home_entrance.background
    show diane 137 at right
    show debbie 91f
    with fade
    dia "Mмм, это запах {b}морской форели{/b}?!"
    dia "Неужели ты сделала?!"
    show diane 136
    show debbie 93f
    deb "Конечно я сделала!"
    deb "Я ведь знаю, как правильно ублажать мою девочку!"
    show diane 138
    show debbie 91f
    dia "О боже, да я готова тебя расцеловать сейчас!"
    show player 203 at left with dissolve
    show diane 137
    show debbie 92f
    dia "А это..."
    dia "... Главный {b}мужчина этого дома{/b}!"
    show diane 136
    show player 14
    player_name "Хэй, {b}Диана{/b}."
    show player 17
    player_name "Прекрасно выглядешь!"
    show diane 138
    show player 203
    dia "Ох, перестань!"
    show player 13
    show diane 136
    show debbie 93f
    deb "А он мелкий обольститель, не так ли?"
    show diane 137
    show debbie 91f
    dia "Не знаю, как ты можешь держать себя в руках рядом с ним!"
    dia "А где второй ребенок? Она присоединится к нам сегодня,или у неё встреча Сучек Summerville?"
    show player 10
    show diane 136
    player_name "Нет, она будет ужинать с нами."
    show player 12
    player_name "... Она сейчас наверху, заканчивает наводить марафет."
    show player 203
    show diane 138
    dia "Типичная принцесска..."
    show diane 137
    dia "Ладно, но я не буду её ждать! Явно ни когда {b}морская форель{/b} в меню!"
    show debbie 92f
    show diane 136
    deb "Хей, будь тактичнее!"
    show debbie 93f
    deb "Она не такая плохая, как ты думаешь..."
    show debbie 91f
    show diane 138
    dia "Хех, ну если ты так говоришь."
    show debbie 93f
    show diane 136
    deb "Говорю. А теперь сядьте уже за стол, а я пока достану бутылочку вина!"
    show debbie 92f
    deb "Я купила новый сорт, который хотела попробывать."
    hide debbie
    hide diane
    with dissolve
    show player 24
    player_name "Нужно присоединиться к ним в {b}Столовой{/b}."
    player_name "Еда {b}[deb_name]{/b} пахнет просто восхитительно!"
    hide player
    with dissolve
    return

label kitchen_mom_debt_call:
    scene expression game.timer.image("homekitchen{}")
    show debbie 6 at right with dissolve
    deb "Я ведь уже вам сказала! Я не {b}ЗНАЮ{/b} где деньги..."
    deb "Я понятия не имела о том, куда он втянут!"
    show debbie 7 at right
    deb "Но-"
    show debbie 6 at right
    deb "У меня нет столько!!"
    show debbie 7 at right
    deb "..."
    show debbie 6 at right
    deb "Это была {b}угроза{/b}?!"
    deb "Я кладу трубку. Не звоните сюда больше."
    show debbie 8 at right with hpunch
    deb "Просто оставьте нас {b}В ПОКОЕ!!!{/b}"
    show debbie 9 at right
    show player 10 at left with dissolve
    player_name "..."
    player_name "...{b}[deb_name]{/b}?"
    player_name "...Ты в порядке?"
    show player 5 at left
    show debbie 11 at right
    deb "Со мной всё хорошо, милый."
    show debbie 10 at right
    show player 10 at left
    player_name "Ты уверена? Это звучало не очень хорошо..."
    show player 5 at left
    show debbie 11 at right
    deb "Тебе не о чем беспокоиться..."
    show debbie 10 at right
    show player 5 at left
    player_name "..."
    show player 10 at left
    player_name "Я могу попытаться найти хорошую работу. Может я смогу заработать немного денег."
    show player 5 at left
    show debbie 11 at right
    deb "Нет."
    deb "Твой {b}отец{/b} не хотел бы этого, милый."
    deb "Тебе нужно сфокусироваться на школе и {b}найти деньги на обучение{/b}."
    show debbie 10 at right
    show player 10 at left
    player_name "Да, но {b}[deb_name]{/b}, я ведь могу помочь..."
    hide player 10 at left
    show debbie 12 at right
    with dissolve
    deb "Ох, милый..."
    deb "Дай мне со всем разобраться и всё будет в порядке, окей? Я обещаю."
    hide debbie with dissolve
    return

label kitchen_mom_diane_visit:
    scene homekitchen_secret
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "... Не вижу тут никакой проблемы. Это ведь хорошо, что он помагает тебе по дому?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Я понимаю, просто..."
    deb "Просто я чувствовала... его влечение к себе..."
    show diane 122 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Это не удивительно, он только что потерял ту семью, к которой привык..."
    show diane 121
    dia "Ему, скорее всего, просто нужно почувствовать близость..."
    dia "Особенно, учитывая то, что произошло с вами за последнее время."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "Я не о том. Тут что-то большее! Я говорю о том, как он на меня смотрит."
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    dia "..."
    show diane 121
    dia "Что ты имеешь ввиду?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Ну, не так давно я... Я начала замечать некоторые вещи..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "...Например?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Например, он всегда возбуждается, когда находится рядом со мной..."
    deb "... И трогает меня... Определенным образом."
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "..."
    show debbie 60f
    deb "... А однажды, я увидела, как он мастурбирует; в моей постели!"
    deb "... С помощью моего белья!"
    show diane 121
    show debbie 59f at Position(xpos=0.3318,ypos=1.000)
    dia "И что ты сделала?!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "Мы обсудили это!"
    deb "Я сказала ему не делать подобных вещей у меня в кровати, но..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Но что?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Я снова его поймала за этим делом! Он извинился и начал говорить о желаниях, с которыми не может справиться..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Окей, и что ты на это ответила?"
    show diane 124
    show debbie 17f at Position(xpos=0.3318,ypos=1.1130)
    deb "... Я типа... Дала ему закончить."
    show diane 121
    show debbie 20f at Position(xpos=0.3318,ypos=1.1130)
    dia "Ты смотрела, как он мастурбирует?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f at Position(xpos=0.3318,ypos=1.000)
    deb "Я не знала, что мне делать!"
    deb "Я думала, если он закончить, то..."
    deb "..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Это так неправильно..."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 60f
    deb "И ещё кое-что..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "Ёщё?!"
    dia "Ты серьёзно?!"
    dia "Расскажи мне!"
    show diane 124
    show debbie 60f
    deb "Диана..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 59f
    dia "{b}[deb_name]{/b}, расскажи!"
    show diane 124
    show debbie 60f
    deb "... Мы вместе принимали душ."
    show diane 121
    show debbie 59f
    dia "Вау..."
    show diane 125
    dia "... И как он?"
    show diane 124
    show debbie 60f
    deb "Диана!!"
    show diane 122
    show debbie 59f
    dia "Что?!"
    show diane 123
    dia "Не прикидывайся ханжой! Мы ведь обе знаем, что ты хочешь мне рассказать!"
    show diane 124
    show debbie 60f
    deb "... {b}*Эх*{/b}"
    show diane 125
    show debbie 59f
    dia "Ты... Трогала её?"
    show diane 126
    show debbie 60f
    deb "... Да."
    deb "Я типа, дрочила ему..."
    show diane 125
    show debbie 59f
    dia "До самого конца?"
    show diane 126
    show debbie 60f
    deb "... Пока он ни кончил, да."
    show diane 125
    show debbie 59f
    dia "И как он?"
    show diane 126
    show debbie 60f
    deb "... О чем ты?"
    show diane 125
    show debbie 59f
    dia "Его {b}член{/b}, {b}[deb_name]{/b}! Он большой?"
    show diane 126
    show debbie 60f
    deb "( !!! )"
    show debbie 59f
    deb "..."
    show diane 127
    dia "Не скромничай, девонька. Расскажи мне всё!"
    show debbie 60f
    show diane 126
    deb "{b}Диана{/b}, у него самый большой... {b}Член{/b}, из всех, что я видела!"
    show diane 125
    show debbie 59f
    dia "... Да ладно?!"
    show diane 122
    dia "Тогда я удивлена, что ты остановилась на хэнджобе..."
    show diane 126
    show debbie 16f at Position(xpos=0.3318,ypos=1.1130)
    deb "{b}Диана{/b}, он ведь ещё ребенок!"
    show diane 125
    show debbie 15f
    dia "Пфф, он уже выпускник!"
    show diane 126
    show debbie 16f
    deb "Да, но я уже достаточно старая, чтобы быть лишь его {b}мамочкой{/b}!"
    show diane 122
    show debbie 15f
    dia "... Но {b}ты не{/b} его {b}мать{/b}, {b}[deb_name]{/b}!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Oх, ну я не знаю, {b}Диана{/b}..."
    show diane 124 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Он очевидно этого хочет."
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Пожалуйста, скажи мне, что я не делаю чего-то ужасного..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Это твое решение, но..."
    dia "Я думаю, что тебе стоит немного расслабиться. Кому какое дело до разницы в возрасте?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Серьезно, ты не думаешь, что я поступаю неправильно?"
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Нет. Я не думаю, что ты делаешь что-то плохое!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Я полагаю, что мы не вредим друг другу...  Это ведь происходит по согласию двух взрослых людей."
    show diane 122 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "Плюс это, должно быть, очень {b}ГОРЯЧО{/b}!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 16f
    deb "Ты так плохо на меня влияешь! Не знаю, почему я тебя вообще слушаю!"
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 15f
    dia "... Потому что ты знаешь, что я права! Просто попробуй. Может так и должно произойти?"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 62f at Position(xpos=0.3318,ypos=1.000)
    deb "Да, я думаю, что это возможно..."
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    show debbie 61f
    dia "Ладно, нужно идти домой. Уже достаточно поздно."
    show diane 125
    dia "Продолжим этот разговор позже. Я хочу знать все самые сочные детали!"
    show diane 120 at Position(xpos=0.7746,ypos=0.7464)
    show debbie 62f
    deb "{b}Диана{/b}! Ты ужасна!"
    deb "Почему бы тебе не прийти как-нибудь ещё? Я бы хотела видеть тебя чаще!"
    show debbie 61f
    show diane 121 at Position(xpos=0.7796,ypos=0.7464)
    dia "Я всегда готова к ужину, {b}[deb_name]{/b}. До тех пор, пока готовка не на мне!"
    dia "Удачи, милая."
    scene expression L_home_entrance.background
    show player 5
    player_name "( Это... было крайне спорно. )"
    player_name "( {b}[deb_name]{/b} не очень комфортно из-за этой ситуации... )"
    show player 203
    player_name "( Хотя она сказала, что ей понравилось. )"
    player_name "( В любом случае, я рад, что {b}Диане{/b} это нормально для нас, заниматься чем-то подобным! )"
    return

label kitchen_mom_kissing_practice:
    show player 2 at left
    show debbie 14b at right
    player_name "Оу, да ладно тебе, {b}[deb_name]{/b}!"
    player_name "Ты ведь сама сказала, что мне нужно кого-нибудь найти."
    player_name "Это станет намного проще, если я буду знать, как правильно целовать девушку, разве нет?"
    show player 1
    deb "..."
    show debbie 13
    deb "... Ладно."
    deb "Я думаю, я смогу дать тебе пару советов."
    show debbie 14
    show player 2
    player_name "Это крайне важно для меня, {b}[deb_name]{/b}."
    show player 1
    show debbie 73 at Position(xpos=0.85, ypos=1.0) with dissolve
    deb "Окей, эмм... Подойди поближе."
    show player 227c at Position(xpos=0.25, ypos=1.0) with dissolve
    show debbie 72
    player_name "Ладно."
    show player 227
    show debbie 73
    deb "Хорошо. Сейчас обопрись, вот так."
    show player 227c zorder 1 at Position(xpos=0.30, ypos=1.0) with dissolve
    show debbie 72 zorder 0 at Position(xpos=0.80, ypos=1.0) with dissolve
    player_name "Окей."
    show player 227
    show debbie 73
    deb "... Закрой глаза и чуть-чуть надави своими губами на мои..."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    deb "Mмм."
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show player 227c
    player_name "И как?"
    show player 227
    show debbie 77
    deb "... Вау."
    show player 227c
    show debbie 76
    player_name "Плохо?"
    show player 227
    show debbie 73
    deb "Н-нет. Это было вполне неплохо!"
    show player 227c
    show debbie 72
    player_name "Правда?!"
    show player 227
    show debbie 73
    deb "Да. Ты уверен, что это твой первый раз?"
    show player 227c
    show debbie 72
    player_name "Ха, уверен. Так что там за советы?"
    show player 227
    deb "..."
    show debbie 73
    deb "Ну, давай посмотри..."
    deb "Ох, я знаю!"
    deb "Поцелуй меня ещё раз, и я покажу тебе небольшой трюк!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80c
    player_name "( !!! )" with hpunch
    show debbie 76 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Вау!"
    player_name "То, что ты сделала своим языком, - это было так круто!"
    show player 227
    show debbie 75
    deb "Хехе, да."
    show debbie 73
    deb "Этому я научилась достаточно давно..."
    show player 227c
    show debbie 72
    player_name "Хмм, как мне это попробовать?"
    show player 227
    show debbie 73
    deb "Ох... ах."
    show player 227c
    show debbie 72
    player_name "Пожалуйста?"
    show player 227
    show debbie 73
    deb "Да... Конечно!"
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 80b
    deb "( !!! )" with hpunch
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 227 at Position(xpos=0.30, ypos=1.0) with dissolve
    deb "..."
    show player 227c
    player_name "Как это было?!"
    show player 227
    deb "Mмм..."
    show player 227c
    player_name "{b}[deb_name]{/b}?"
    show player 227
    show debbie 77
    deb "Ох, прости!"
    show debbie 75
    deb "Это было ОЧЕНЬ неплохо, милый!"
    deb "То есть, вау! Ты будешь отличным обольстителем, как окунешься в мир свиданий!"
    show player 227c
    show debbie 76
    player_name "Правда? Спасибо {b}[deb_name]{/b}!"
    show player 227
    deb "Mммхмм."
    hide player
    show debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show debbie 80
    pause
    show debbie 79
    pause
    show debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show debbie 77
    pause
    show debbie 74
    deb "Oх!"
    deb "Oх боже..."
    show player 230
    player_name "..."
    show player 232
    player_name "Прости, {b}[deb_name]{/b}."
    player_name "Я не хотел..."
    show player 231
    show debbie 75
    deb "Хехе, всё в порядке, милый. Я всё понимаю."
    show debbie 73
    deb "Нам лучше сделать перерыв."
    show player 232
    show debbie 72
    player_name "... Да. Конечно."
    player_name "Что думаешь, может, мы сделаем это снова?"
    show player 231
    deb "..."
    show player 232
    player_name "Ну знаешь, чтобы я попрактиковался?"
    show player 231
    show debbie 73
    deb "Я думаю, что это не проблема."
    deb "Но только ради практики!"
    show player 232
    show debbie 72
    player_name "Да, конечно!"
    show player 231
    show debbie 73
    deb "Отлично. Ты можешь попросить меня об этом в любое время."
    show player 232
    show debbie 72
    player_name "Спасибо {b}[deb_name]{/b}!"
    show player 231
    show debbie 73
    deb "Никаких проблем, {b}[firstname]{/b}."
    show player 232
    show debbie 72
    player_name "Увидимся!"
    hide debbie with dissolve
    show player 1 at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "..."
    show player 21f at Position (xpos=0.5, ypos=1.0) with dissolve
    player_name "Это было прекрасно!"
    return

label kitchen_mom_dishes:
    scene location_home_kitchen_closeup
    show debbie 116 at right
    with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 116 at right
    show player 1 at left with dissolve
    pause
    show debbie 117 at Position(xpos=1014)
    pause
    show debbie 119 at Position(xpos=1014)
    deb "Оу, эй, милый!"
    show debbie 120
    show player 14
    player_name "Хэй, {b}[deb_name]{/b}!"
    show debbie 119
    show player 1
    deb "Тебе нужно что-то?"
    deb "Я как раз домыла посуду..."
    show debbie 120
    return

label kitchen_mom_dishes_yes:
    show debbie 118
    show player 14
    player_name "Почему бы тебе не передохнуть?."
    player_name "Я протру остальное."
    show debbie 119
    show player 1
    deb "Это очень мило с твоей стороны, но ты не обязан."
    show debbie 118
    show player 14
    player_name "Всё в порядке. Я всё равно собирался сменить деятельность."
    show debbie 119
    show player 1
    deb "Ах, но ладно. Раз ты так говоришь..."
    show player 272
    show debbie 62
    deb "Просто вытри и поставь их в шкаф."
    show player 273
    show debbie 61
    player_name "Сделаю."
    show debbie 63
    show player 272
    deb "Спасибо за твою помощь, {b}[firstname]{/b}."
    show player 274
    show debbie 61
    player_name "Не за что, {b}[deb_name]{/b}."
    show expression Cutscene("help_debbie_kitchen_cutscene", "Не думаю, что {b}[deb_name]{/b} кто-нибудь помогал с посудой раньше... \nОна сказала,что её бывший муж вообще ничего не делал по дому, а мой {b}отец{/b} помогал только в саду, или изредко что-то чинил. \nОна стояла со мной на кухне до тех пор, пока я не разложил всю посуду по местам, а после этого мы мило поговорили. \nБыло приятно узнать {b}[deb_name]{/b} по-лучше...") as cutscene with fade
    pause
    hide cutscene with dissolve
    return

label kitchen_mom_dishes_no:
    show player 14 at left
    show debbie 120 at Position(xpos=1014)
    player_name "Окей. Тогда я зайду позже."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
