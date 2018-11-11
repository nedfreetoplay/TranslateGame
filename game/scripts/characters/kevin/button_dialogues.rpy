label kevin_dialogue_ross_find_magazines:
    show player 2 at left
    show kevin 29b at right
    with dissolve
    player_name "Привет, {b}Кевин{/b}!"
    show player 1
    show kevin 30
    kev "Как дела, {b}[firstname]{/b}?"
    show player 2
    show kevin 29b
    player_name "Не очень. Что ты читаешь?"
    show player 1
    show kevin 30b
    kev "Ох, просто некоторые журналы, которые я взял, в спортзале."
    show player 2
    show kevin 29b
    player_name "Круто, ты ищешь новую работу или типо того?"
    show player 1
    show kevin 30
    kev "Нет, почему?"
    show player 11
    show kevin 29
    player_name "..."
    show kevin 31 with dissolve
    kev "Иди посмотри на этого красавчика, {b}[firstname]{/b}!"
    show player 10
    show kevin 31b
    player_name "... Красавчика?"
    show player 11
    player_name "..."
    show player 10
    player_name "Ох, точно... Ты думаешь, я могу взять один из этих журналов?"
    show player 11
    show kevin 30 with dissolve
    kev "Хех, Я не знал что ты был знатаком мужских форм..."
    show player 10
    show kevin 29
    player_name "Вообще-то я уже в Колледже."
    show player 11
    show kevin 30b
    kev "Ох, точно. Колледж."
    show kevin 31 with dissolve
    kev "Я понял тебя Бро! Ни слова больше!"
    kev "Бери все что тебе нужно! Вот этот займет меня на некоторое время."
    show player 2
    show kevin 31b
    player_name "Крутяк! Спасибо, эмм, Бро..."
    show player 1
    show kevin 31c
    kev "Чееерт возьми, он блестит..."
    show player 10
    player_name "..."
    return

label kevin_dialogue_ross_ask_model:
    show player 2 at left
    show kevin 1 at right
    player_name "Я работаю надо проектом для {b}Мисс Росс{/b} и для этого требуется живая модель."
    player_name "Тебя не заинтересует?"
    show kevin 2
    show player 1
    kev "Моделирование. Я просто должен стоять там?"
    show player 2
    show kevin 1
    player_name "Да, тебе просто нужно будет стоять там."
    show player 10
    player_name "Голым."
    show kevin 3
    show player 11
    kev "Голым!?"
    kev "Ох, мужик. Я не знаю, Бро."
    kev "Это только ты там будешь рисовать?"
    show player 10
    show kevin 1
    player_name "Ну, {b}Мия{/b} и я - оба будем рисовать."
    player_name "{b}Мисс Росс{/b} тоже там будет."
    show player 11
    show kevin 4
    kev "Агх, пасс..."
    show kevin 3
    kev "Я не хочу чтобы девочки видели меня голым, Бро. Это немного стремно."
    show kevin 1
    player_name "..."
    show player 10
    player_name "Х-хорошо."
    return

label kevin_dialogue_intro:
    show kevin 23 at right
    show player 14 at left
    with dissolve
    player_name "Привет, {b}Кевин{/b}!"
    show player 13
    show kevin 9b
    kev "Привет, {b}[firstname]{/b}."
    show kevin 23
    show player 14
    player_name "Как дела?"
    show player 13
    show kevin 9b
    kev "Не очень. Вчера у меня был ягодичный день."
    kev "Моя задница болит!"
    kev "Хотя потрогай какая она тугая!"
    show kevin 23
    show player 10
    player_name "Эмммм... Нет спасибо чувак."
    show player 13
    show kevin 9b
    kev "Ты многое потерял!"
    return

label kevin_dialogue_erik_favor_2_completed:
    kev "Лучше увидимся в спортзале чуть позже!"
    show kevin 23
    show player 14
    player_name "Может быть..."
    show player 13
    show kevin 9b
    return

label kevin_dialogue_dewitt_kevin_give_guitar:
    show player 14
    player_name "Я нашел для тебя гитару!"
    show player 13
    show kevin 24
    kev "Серьезно?"
    show kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "Что ты думаешь?"
    show player 13 with dissolve
    show kevin 16f with dissolve
    kev "Черт возьми!Где ты достал эту штуку?"
    kev "Эта вешь лучше подделки!"
    show kevin 14f
    show player 10
    player_name "Эта?"
    show player 5
    show kevin 15f
    kev "Эмм, да, Бро!"
    kev "Я надеюсь ты ее не украл или типо того."
    show kevin 14f
    show player 14
    player_name "Вообще-то я её одолжил, у моего друга. Так что будь остороже с ней, хорошо?"
    hide player
    show kevin 27 at left
    with dissolve
    kev "Без проблем!"
    kev "Я буду относиться к этой красоте с уважением, которого она так заслуживает!"
    show kevin 28
    player_name "Круто, так что ты будешь играть на ней на шоу талантов."
    show kevin 27
    kev "Я должен!"
    show kevin 28
    player_name "Потрясно! Увидимся тогда скоро в кабинете {b}Мисс Девитт{/b} чтобы потренироваться!"
    show kevin 27
    kev "Звучит неплохо,Бро!"
    show player 13 at left
    show kevin 16 at right
    with dissolve
    kev "Я буду называть тебя... Дэвин"
    kev "Ты бы хотела это красивая?"
    show player 11
    hide kevin with dissolve
    player_name "..."
    return

label kevin_dialogue_talent_show_help:
    show player 10
    player_name "Я помогаю {b}Мисс Девитт{/b} найти добровольцев для шоу талантов."
    player_name "Разве ты раньше не играл на гитаре?"
    show player 5
    show kevin 24
    kev "Да, я играл."
    show kevin 23
    show player 10
    player_name "Что случилось?"
    show player 5
    show kevin 24
    kev "Ох, моя бывшая вроде как разбила её когда я порвал с ним."
    show kevin 23
    show player 12
    player_name "С ним?"
    show player 11
    show kevin 22 with dissolve
    kev "Я сказал с ним? Извини, я имел в виду с ней."
    kev "... Да, ОНА разбила её на кусочки."
    show kevin 23 with dissolve
    show player 14
    player_name "Хм, ты западаешь на сумашедших девченок, хм?"
    show player 13
    show kevin 22 with dissolve
    kev "Хех, Ты знаешь! Сумашедшие дувченки, Я на пути к ним! Полностью..."
    show kevin 23 with dissolve
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin 24
    kev "Да, Я был бы не против."
    kev "Все же где же я достану гитару? Они очень дорогие!"
    show kevin 23
    show player 35
    player_name "Хмм, возможно я смогу найти одну для тебя..."
    show player 34
    player_name "( У {b}Эрика{/b} в подвале много гитар. Возможно я смогу одолжить одну? )"
    show player 14
    player_name "Я вернусь!"
    show player 13
    show kevin 24
    kev "Хорошо."
    return

label kevin_dialogue_talent_show_replace_guitar:
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin 24
    kev "Да, Я бы не отказался."
    kev "Все же где же я достану гитару? Они очень дорогие!"
    show kevin 23
    show player 34
    player_name "( Я должен поменять мою само-сделанную гитару с той что в подвале у {b}Эрика{/b}! )"
    show player 14
    player_name "Я приду!"
    show player 13
    show kevin 24
    kev "Ладно."
    return

label kevin_dialogue_talent_show:
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin 24
    kev "Да, Я бы не отказался."
    kev "Все же,где же я достану гитару? Они очень дорогие!"
    show kevin 23
    show player 35
    player_name "Хмм, возможно я смогу найти одну для тебя..."
    show player 34
    player_name "( У {b}Эрика{/b} в подвале много гитар. Возможно я смогу одолжить одну? )"
    show player 14
    player_name "Я вернусь!"
    show player 13
    show kevin 24
    kev "Хорошо."
    return

label kevin_dialogue_dewitt_science_adhesive:
    show player 10
    player_name "Что нам нужно для этого {b}клея{/b} ещё раз?"
    show player 13
    show kevin 2
    kev "Просто встреться со мной в {b}Научной лаборатории после уроков{/b}."
    kev "Я позабочусь об остальном."
    show kevin 1
    show player 14
    player_name "Круто! Спасибо, {b}Кевин{/b}!"
    return

label kevin_dialogue_leave:
    show player 14
    player_name "Увидимся позже, {b}Кевин{/b}."
    show player 13
    show kevin 9b
    kev "Позже!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
