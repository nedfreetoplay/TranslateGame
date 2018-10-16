label gym_training_dialogue_first:
    scene expression game.timer.image("training{}_b")
    pause 0.001
    show player 35 at left
    player_name "Вау..." with None
    show player 14
    player_name "В этом месте есть всё!"
    player_name "Тут даже есть секция бокса!"
    show master 2 at right
    show player 11
    with dissolve
    mas "Это не боксерский зал, а тренировочный лагерь {b}Муау Тай{/b}!"
    show master 1
    show player 17
    player_name "Ага. Я вижу..."
    show master 3
    show player 11
    mas "Только самые упорные и дисциплинированные ученики получат мои знания!"
    show master 5
    show player 12
    player_name "Хммм... Разве я не могу просто поднимать какой-нибудь вес и быть сильнее всех?"
    show master 4
    show player 11
    mas "{b}НЕТ!!!{/b}" with hpunch
    show master 3
    show player 1
    mas "Без умственной и физической дисциплины Муай Тай..."
    show master 4
    show player 11
    mas "...ты будешь просто большим куском мяса!"
    show master 3
    mas "Обучаясь использовать восемь частей нашего тела и наносить удары, мы становимся самым эффективным оружием!"
    show master 5
    show player 12
    player_name "Правда? А если у меня есть пушка?"
    show master 4
    show player 11
    mas "Ты {b}ГЛУПЕЦ{/b}!!!"
    show player 6
    show master 7
    window hide
    with vpunch
    pause
    show master 1
    show player 38
    player_name "Ауч!!"
    player_name "Больно!"
    show master 4
    show player 11
    mas "Ты медленый... и слабый! Оружие в твоих руках бесполезно!"
    show master 2
    mas "Это не хорошо, тебе надо поработать над {b}Выдержкой{/b}."
    show master 5
    show player 12
    player_name "Хорошо, так, когда мы начнём?"
    show master 4
    show player 11
    mas "Хах! Мои уроки не бесплатны, молодой ученик."
    show master 3
    mas "Я принимаю только одну форму оплаты..."
    mas "...и она заключается в виде..."
    show player 22
    mas "...{b}трусиков{/b}!"
    show player 21
    show master 6
    player_name "Чего?"
    show master 4
    show player 11
    mas "Может мне повторить, ученик?"
    show master 6
    show player 10
    player_name "Нет... Я постараюсь их найти, Сенсей."
    show master 4
    show player 22
    mas "Прощаясь ты должен поклониться!"
    show master 1
    show player 40
    player_name "Да, Сенсей!"
    show master 4
    show player 22
    mas "Зови меня {b}Мастер Сомрек{/b}!!!"
    show master 1
    show player 40
    player_name "Да, {b}Мастер Сомрек{/b}!!!"
    show master 2
    show player 1
    mas "Хорошо, иди!"
    hide player
    hide master
    with dissolve
    hide training_b
    hide training_night_b
    return

label gym_training_dialogue_second:
    scene expression game.timer.image("training{}_b")
    pause 0.001
    show player 14 at left
    show master 6 at right
    with dissolve
    player_name "{b}Мастер Сомрек{/b}!"
    player_name "Я готов изучать новые приемы!"
    show player 1
    show master 2
    mas "Ты готов учиться! Хорошо, Хорошо!"
    show master 3
    mas "Но мои уроки не бесплатны, молодой ученик."
    mas "Твоей новой платой будет за обучение будет..."
    show player 11
    show master 9
    mas "...пара использованных {b}трусиков{/b}!"
    show master 1
    player_name "..."
    show master 3
    mas "И убедись, что они {b}использованные{/b}!"
    show master 5
    show player 12
    player_name "Использованные?"
    show player 11
    show master 3
    mas "Ты должен увидеть, как женщина снимает их лично!"
    show master 9
    mas "Убедись, что они были ношеные и впитали её запах!"
    show master 6
    show player 21
    player_name "Ох... Я постараюсь их найти, Сенсей."
    show master 4
    show player 5
    mas "Ты должен поклониться перед уходом, идиот!" with hpunch
    show master 6
    show player 40
    player_name "Да, {b}Мастер Сомрек{/b}!!!"
    show master 2
    show player 1
    mas "Хорошо! Теперь в путь!"
    hide player
    hide master
    with dissolve
    hide training_b
    hide training_night_b
    return

label gym_training_dialogue_third:
    scene expression game.timer.image("training{}_b")
    pause 0.001
    pause 0.001
    show player 14 at left
    show master 6 at right
    with dissolve
    player_name "{b}Мастер Сомрек{/b}!"
    player_name "Я готов изучать новые приемы!"
    show player 1
    show master 2
    mas "Ты готов учиться! Хорошо, хорошо!"
    show master 3
    mas "Но мои уроки не бесплатны, молодой ученик."
    mas "Твоей новой платой будет за обучение будут..."
    show player 11
    show master 9
    mas "...влажные {b}трусики{/b}!"
    show master 1
    player_name "..."
    show master 3
    mas "И убедись, что они {b}влажные{/b}!"
    show master 5
    show player 12
    player_name "Влажные?"
    show player 11
    show master 3
    mas "Ты должен быть свидетелем!"
    show master 9
    mas " {b}Трусики{/b} должны быть {b}пропитаны{/b} соками!"
    show master 3
    mas "Убедись, что их носила возбужденная женщина!!"
    show master 6
    show player 21
    player_name "Ох... Я постараюсь их найти, Сенсей."
    show master 4
    show player 5
    mas "Ты должен поклониться прежде чем уйти, идиот!"
    show master 6
    show player 40
    player_name "Да, {b}Мастер Сомрек{/b}!!!"
    show master 2
    show player 1
    mas "Хорошо! Теперь в путь!"
    hide player
    hide master
    with dissolve
    hide training_b
    hide training_night_b
    return

label gym_training_dialogue_fourth:
    scene expression game.timer.image("training{}_b")
    pause 0.001
    show player 14 at left
    show master 6 at right
    with dissolve
    player_name "{b}Мастер Сомрек{/b}!"
    player_name "Я готов изучать новые приемы!"
    show player 1
    show master 2
    mas "Великолепно"
    show master 3
    mas "Но мой последний урок не бесплатен, юный ученик."
    mas "Последней платой за твою тренировку будут..."
    show player 11
    show master 9
    mas "...{b}трусики{/b} пропитанные {b}смазкой{/b}!!!"
    show master 1
    player_name "!!!"
    show master 3
    mas "Убедись, что они полностью {b}пропитаны смазкой{/b}!"
    show master 5
    show player 12
    player_name "Смазкой?"
    show master 4
    show player 22
    mas "Ты человек или попугай?!" with hpunch
    show master 5
    show player 5
    player_name "..."
    show player 11
    show master 3
    mas "Ты должен быть свидетелем!"
    show master 9
    mas "Убедись, что они будут {b}пропитаны{/b} и {b}обрызганы{/b} женскими соками!!"
    show player 21
    show master 5
    player_name "Это будет непросто..."
    show master 6
    player_name "...но я постараюсь найти их, Сенсей."
    show master 2
    show player 5
    mas "Ты должен поклониться, помнишь?"
    show master 6
    show player 40
    player_name "Да, {b}Мастер Сомрек{/b}!!!"
    show master 2
    show player 1
    mas "Хорошо! Теперь в путь!"
    hide player
    hide master
    with dissolve
    hide training_b
    hide training_night_b
    return

label cedric_dialogue:
    scene expression game.timer.image("training{}_b")
    show ced 1 at left
    show player 14f at right
    with dissolve
    player_name "Привет!"
    player_name "Можешь меня подстраховать?"
    show ced 2
    show player 1f
    ced "Ох..."
    show player 11f
    ced "Ты хоть раз от груди жал, шкет?"
    show player 10f
    show ced 1
    player_name "Что?"
    show ced 2
    show player 5f
    ced "Извини, не страхую дрищей."
    hide ced
    hide player
    with dissolve
    $ game.main()

label tired_training_dialogue:
    scene expression game.timer.image("training{}_b")
    show player 5 with dissolve
    player_name "( Я устал, пора домой. )"
    hide player with dissolve
    $ game.main()

label cant_solo_lift:
    scene expression game.timer.image("training{}_b")
    show player 11 at left with dissolve
    player_name "( Сам я не справлюсь. )"
    player_name "( Нужно, чтобы кто-то меня подстраховал! )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
