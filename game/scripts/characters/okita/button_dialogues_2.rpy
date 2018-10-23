label button_okita_ingredients_mushroom:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "{b}Фалькумный Гриб{/b} растет здесь в лесу, в Саммервилле."
    show okita 3
    okita "Их легко заметить из-за своей фаллической формы."
    show player 10
    show okita 1
    player_name "... Отврат."
    return

label button_okita_ingredients_toad:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "Это сезон размножения {b}Возбуженных жаб{/b}. Так что ищи {b}в пруде или ручье.{/b}"
    okita "Они должны быть легко опознаваемы по их бугристым фиолетовым спинкам."
    show player 10
    show okita 1
    player_name "Похоже на уродливую лягушку...."
    return

label button_okita_ingredients_flower:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "{b}Психотропный Молочай{/b} это свитящийся цветок, который растет только в тёмных местах."
    okita "Твоим лучшим выбором будет {b}пещера{/b}."
    show player 35
    show okita 1
    player_name "Хмм, в {b}пещере{/b}..."
    return

label button_okita_ingredients_stock:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "Нам нужно что-то легкое, чтобы действовать в качестве основы для сыворотки. Овощной бульон будет работать лучше всего."
    okita "Ты должен забрать несколько в Консумер."
    show player 2
    show okita 1
    player_name "... По крайней мере, один из ингредиентов прост."
    return

label button_okita_ingredients_tissue:
    scene location_school_science_closeup
    show player 11 at left
    show okita 2 at right
    okita "Образец волос или слюны будет работать лучше всего."
    show player 10
    show okita 1
    player_name "Да, но как я должен достать это?"
    show player 11
    show okita 9
    okita "... Я уверена, ты что-нибудь придумаешь.."
    show okita 4
    player_name "..."
    return

label button_okita_got_all_ingredients:
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "Хорошо Мэм, я думаю, у меня есть все."
    show player 1
    show okita 3
    okita "... Ты думаешь?"
    show okita 1
    show player 533 with dissolve
    player_name "Ну, есть одна маленькая проблема..."
    show okita 3
    show player 532
    okita "... Это {b}Куриный бульен{/b}?"
    show player 533
    show okita 1
    player_name "Да. Это всё что есть в {b}Консумере{/b}..."
    player_name "Я подумал, может быть {b}куриный бульон{/b} всё равно сработает?"
    show player 532
    show okita 2b
    okita "Хах, да. Это будет здорово..."
    show player 11 with dissolve
    show okita 6
    player_name "..."
    show okita 7
    okita "Похоже, все остальное в порядке."
    okita "Встретимся в моем кабинете этим вечером и мы начнем смешивать."
    show player 10
    show okita 6
    player_name "Этой ночью?"
    show player 11
    show okita 3
    okita "Проблемы?"
    show player 10
    show okita 4
    player_name "Нет! ...Нет. Увидимся тогда."

    return

label button_okita_extract_cum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 4 at right
    player_name "Поэтому у нас есть всё необходимое, чтобы сделать нашу сыворотку?"
    show player 11
    show okita 5
    okita "... Эмм, да Разве это не то что я тебе только что сказала?!"
    okita "{b}Встретимся в моем офисе этим вечером{/b} и мы сможем над эти поработать."
    show okita 4
    show player 10
    player_name "... Х-хорошо."
    return

label button_okita_dose_smith:
    scene location_school_science_closeup
    show player 1 at left
    show okita 5 at right
    with dissolve
    okita "Ты ещё не принес дозу {b}Директрисе Смит{/b}?!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "Чего же ты ждешь?"
    show player 12
    show okita 4
    player_name "Вы знаете, это не совсем легко!"
    player_name "Не могли бы вы дать мне совет или что-то?!"
    show player 16
    show okita 3
    okita "Вот несколько советов: Поторопитесь и сделай это уже!"
    show okita 5
    okita "Всё, что тебе нужно сделать, это {b}подсунуть ей это в еду или еще куда-нибудь{/b}."
    show player 12
    show okita 4
    player_name "Ладно, ладно. Я скоро вернусь."
    return

label button_okita_wait_for_smith_serum:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    player_name "Хорошо, {b}Мисс Окита{/b}. Все сделано."
    show player 1
    show okita 7
    okita "Прекрасно!"
    okita "Теперь мы просто подождем, чтобы увидеть последствия..."
    show player 10
    show okita 6
    player_name "Сколько времени это займет?"
    show player 11
    show okita 7
    okita "Это сработает быстро. Почему бы тебе не остаться после занятий и мы проверим её?"
    show player 2
    show okita 6
    player_name "Конечно."
    pause 1
    hide player
    hide okita
    scene black
    with dissolve
    scene location_school_lounge_day_blur
    show okita 5f zorder 1 at Position(xpos=0.3, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show principal 33 at right
    with dissolve
    okita "*Кхм*"
    show okita 4f
    show principal 32 with dissolve
    smi "Хмм? О, привет Тори..."
    smi "Как поживает Маленькая Мисс Всезнайка сегодня?"
    show principal 31
    okita "... Мммхм."
    show okita 3f
    okita "Я просто проверяла состояние своего кабинета?"
    show okita 4f
    show principal 32
    smi "Твоего кабинета?"
    show okita 5f
    show principal 31
    okita "Ну, на днях ты казалась довольно непреклонна в смене замков."
    show okita 4f
    show principal 32
    smi "Я?"
    smi "Это смешно... Я не помню."
    show okita 3f
    show principal 31
    okita "О, Реально?"
    smi "..."
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Кудах Кудах."
    show principal 31 at right with dissolve
    show okita 8f
    show player 10
    okita "..."
    show okita 3f
    okita "... Ты в порядке?"
    show okita 4f
    show principal 32
    smi "... Хм?"
    smi "Я в порядке, почему?"
    show player 11
    show okita 5f
    show principal 31
    okita "Ты что то говорила, относительно замка в моем кабинете?"
    show okita 4f
    show principal 32
    smi "Я?"
    smi "Это смешно... Я не-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "КУДАХ!!! Кудах кудах кудах..."
    show principal 31 at right with dissolve
    show okita 6f
    show player 10
    player_name "Эмм..."
    show okita 9f
    show player 11
    okita "Шшш!"
    show principal 33 with dissolve
    okita "Не мешай нам {b}[firstname]{/b}."
    show okita 4f
    show principal 32 with dissolve
    smi "... У этого кофе странный вкус."
    show principal 31
    player_name "..."
    show okita 7f
    okita "Я рассказывала тебе о новом изобретении, над которым работала?"
    show okita 6f
    show principal 32
    smi "Изобретении?"
    smi "Нет, я не думаю что ты-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smi "Кудах кудах..."
    smi "Кудах кудах КУДАХ!!"
    show principal 31 at right with dissolve
    show okita 7f
    okita "Я Когда-нибудь принесу его к тебе в кабинет... Это действительно увлекательно!"
    show principal 32
    show okita 6f
    smi "Конечно, хорошо!"
    show okita 7f
    show principal 31
    okita "О мой, посмотри на время."
    okita "Мы действительно должны идти."
    show okita 7 at Position(xpos=0.05, ypos=1.0) with dissolve
    okita "Пойдем, {b}[firstname]{/b}."
    hide okita with dissolve
    player_name "..."
    show principal 32

    smi "... Этот кофе странное на вкус."


    hide principal
    hide okita
    hide player
    scene black
    with dissolve
    scene location_school_science_closeup
    show player 11 at left
    show okita 7 at right
    okita "Итак, Я думаю, что {b}Куриный бульон{/b} создал немного побочного эффекта в конце концов..."
    show okita 2b
    okita "Пфффф, хахаха!!"
    show player 12
    show okita 6
    player_name "Как это может быть смешным?!"
    player_name "Мы ебали её голову, а она там кудахтала, как курица!"
    show player 11
    show okita 2b
    okita "Да так и есть! Хахаха!"
    show player 16
    show okita 7
    okita "О, ты можешь расслабиться?"
    okita "Это только временно."
    show okita 9
    okita "... Я думаю."
    show player 12
    show okita 6
    player_name "Вы думаете?!"
    show player 16
    show okita 9
    okita "В смысле, Я почти уверена."
    show okita 7
    okita "Смотри, главное чтобы сыворотка сработала!"
    okita "Сейчас она полностью беспристрастна к моим экспериментам!"
    okita "... И она даже не помнила, что хотела запереть мой кабинет!"
    show player 12
    show okita 6
    player_name "Да, но она кудахчет, как курица!"
    show player 16
    show okita 2b
    okita "Пфффф, хахахаха!"
    show player 12
    player_name "Ну, я рад, что вы думаете, что это так смешно..."
    show okita 6
    player_name "Так что теперь?"
    show player 16
    show okita 7
    okita "Сейчас, Мне нужно время, чтобы изучить последствия другой сыворотки.."
    show player 10
    show okita 6
    player_name "О, Я совсем забыл про другую сыворотку!"
    player_name "Вы чувствуете какую-то разницу?"
    show player 11
    show okita 7
    okita "Ммм, может быть..."
    show okita 2b
    okita "Хехехе!"
    show player 10
    player_name "Вы выглядите немного по другому."
    show player 11
    show okita 7
    okita "И как же?"
    show player 10
    show okita 6
    player_name "Вы как... Легкомысленную."
    show player 11
    show okita 2b
    okita "Хехехе! Я просто счастлива."
    show player 10
    player_name "Это немного пугает меня, если честно."
    show player 11
    show okita 7
    okita "... И жарко."
    show okita 3
    okita "Тебе жарко? Как здесь жарко!"
    show player 10
    show okita 6
    player_name "Нет, Я в норм."
    show player 11
    show okita 7
    okita "Хорошо, ну я пойду в свой офис и поработатаю."
    okita "Приходи ко мне через несколько дней."
    show player 10
    show okita 6
    player_name "Эммм, хорошо."
    show player 11
    show okita 2b
    okita "Покааа, {b}[firstname]{/b}!"
    okita "Хехехехе..."
    hide okita with dissolve
    hide player
    show player 10f
    with dissolve
    player_name "Я надеюсь, с ней все будет хорошо..."
    return

label button_okita_wait_for_okita_serum:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "Всё в порядке, Мэм?"
    player_name "Вы заметили какие-то побочные эффекты от вашей сыворотки?"
    show player 11
    show okita 7
    okita "Я все ещё тестирую."
    okita "... Я ценю что ты проверяешь это со мной."
    show player 10
    show okita 6
    player_name "... Вы?"
    show okita 7
    show player 11
    okita "Кончено!"
    show okita 2b
    okita "Это заставляет меня чувствовать себя все тепло и нечетко!"
    show player 11
    show okita 6
    player_name "..."
    show player 10
    player_name "Хорошо, серьезно! Ты ведешь себя очень странно!"
    show player 11
    show okita 7
    okita "Я?"
    show okita 2b
    okita "Я не знаю, что тебе сказать. Я чувствую себя великолепно!"
    show player 10
    show okita 6
    player_name "Хорошо, чтож просто будьте осторожны, я думаю."
    show player 11
    show okita 7
    okita "Сделаем, красавчик!"
    show okita 2b
    okita "Хехехе!"
    player_name "..."
    return

label button_okita_serum_effects:
    scene location_school_science_closeup
    show player 10 at left
    show okita 6 at right
    with dissolve
    player_name "Все же есть какие-то результаты из сыворотки?"
    show player 11
    show okita 7
    okita "Честно говоря, {b}[firstname]{/b}, Я надеялась, что ты поможешь мне протестировать мое новое изобретение?"
    show player 10
    show okita 6
    player_name "О мэн, ты хочешь, чтобы я сделал что-то другое?"
    show player 11
    show okita 3
    okita "Хмм? Нет, нет!"
    show okita 7
    okita "Я создала это сама. Это революционно!"
    show player 10
    show okita 6
    player_name "Ты создала это?"
    player_name "Но создание это мартышкина работа. Я думал, ты не занимаешься обезьяньей работой?"
    show player 11
    show okita 7
    okita "На этот раз я сделала исключение, потому что..."
    okita "Ну, я сделала это изобретение для тебя; В качестве сюрприза."
    show player 10
    show okita 6
    player_name "Для меня?"
    show player 11
    show okita 7
    okita "Да, приходи ко мне в офис сегодня вечером после школы, и я покажу тебе."
    show player 10
    show okita 7
    player_name "Это начинает меня беспокоить..."
    player_name "Что ты задумала?"
    show player 11
    show okita 2b
    okita "Не будь ребенком! Ты ДОЛЖЕН прийти и посмотреть!"
    show player 10
    show okita 6
    player_name "Хорошо."
    show player 11
    show okita 7
    okita "Ты обещаешь?"
    show player 10
    show okita 6
    player_name "Эмм, да."
    player_name "... Я обещаю."
    show player 11
    show okita 2b
    okita "Ура!"
    show okita 7
    okita "До скорой встречи, {b}[firstname]{/b}!"
    hide okita with dissolve
    hide player
    show player 11f
    with dissolve
    player_name "..."
    return

label button_okita_generic_after_q3:
    call expression game.dialog_select("button_okita_generic_after_q3_intro")
    menu:
        "Новое изобретение." if M_okita.is_state(S_okita_is_hypersexual):
            call expression game.dialog_select("button_okita_generic_after_q3_new_invention")
        "Ничего.":

            call expression game.dialog_select("button_okita_generic_after_q3_leave")
    return

label button_okita_generic_before_q3:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Здравствуйте, {b}Мисс Окита{/b}."
    show player 1
    show okita 5
    okita "Что случилось, {b}[firstname]{/b}?"
    show player 11
    okita "Я очень занята..."
    show okita 4
    return

label button_okita_generic_after_q3_intro:
    scene location_school_science_closeup
    show player 2 at left
    show okita 6 at right
    with dissolve
    player_name "Здравствуйте, {b}Мисс Окитаы{/b}."
    show player 1
    show okita 2b
    okita "{b}[firstname]{/b}!"
    show okita 7
    okita "Как здорово что ты заглянул!"
    okita "Чем я могу тебе помочь?"
    show okita 6
    return

label button_okita_generic_after_q3_new_invention:
    show player 2
    player_name "Итак, вы работали над новым изобретением, хм?"
    show player 1
    show okita 7
    okita "О, да!"
    okita "Это революционно! Вы обязательно должен прийти и посмотреть!"
    show player 2
    show okita 6
    player_name "Хех, хорошо! Я {b}встречу вас вашем кабинете сегодня вечером.{/b}"
    show okita 2b
    show player 1
    okita "Ты должен пообещать, что придешь и посмотришь!"
    show okita 6
    show player 11
    player_name "..."
    show player 10
    player_name "... Да. Я обещаю."
    show okita 2b
    show player 11
    okita "Я не могу долждаться!"
    return

label button_okita_generic_after_q3_leave:
    show player 3
    player_name "Ничего, Я просто хотел поздороваться!"
    show okita 5
    okita "Это очень мило с твоей стороны"
    show player 2
    okita "Однако, Я занята работой над некоторыми новыми проектами в данный момент."
    show okita 7
    okita "Приходи ко мне в мой {b}кабинет{/b} если ты хочешь мне помочь."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
