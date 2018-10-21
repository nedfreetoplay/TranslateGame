label yumi_police_basement_dialogue_pre:
    scene police_c_3 with None
    show yumi 2 at right
    show player 1 at left
    with dissolve
    yum "Здравствуйте, вы гость или пришли внести залог?"
    show yumi 1
    return

label yumi_police_basement_dialogue_donuts:
    show player 14 at left
    show yumi 1 at right
    player_name "Я знаю, что вы только недавно начали работать с ним..."
    show yumi 3
    player_name "... Но вы случайно не знаете, какие пончики нравятся {b}Гарольду{/b}?"
    show player 1
    show yumi 4
    yum "Да?"
    yum "Почему вы спрашиваете?"
    show yumi 1
    show player 14
    player_name "О, да... пытаясь заставить его полюбить меня."
    show player 1
    show yumi 2
    yum "Да. Это... странно."
    show player 14
    show yumi 1
    player_name "Я знаю, но я дружу с его дочерью и-"
    show player 11
    show yumi 2
    yum "Тебе не нужно объяснять. Я думаю, у меня есть фотография."
    show player 1
    yum "Ну, каждый раз, когда мы посещаем магазин пончиков... он ставит {b}[harold_topping]{/b} на вершине его пончика."
    show player 14
    show yumi 1
    player_name "Серьёзно?"
    show player 1
    show yumi 2
    yum "Да, он всегда получает это."
    show player 17
    show yumi 1
    player_name "Хорошо, спасибо за помощь!"
    show player 1
    show yumi 2
    yum "Нет проблем!"
    return

label yumi_police_basement_dialogue_harold:
    show player 12
    player_name "Ты знаешь, где может быть {b}Гарольд{/b}?"
    player_name "Мне нужно эмм... вернуть ему что-то!"
    show player 5
    show yumi 4
    yum "Знаешь, я видела его только сегодня утром!"
    yum "Он посмотрел... прочь... и пахло алкоголем..."
    show yumi 3
    show player 10
    player_name "Алкоголем?!"
    show player 11
    show yumi 4
    yum "Да, но никому не говори!"
    yum "У бедняги проблемы с женой."
    yum "Я просто не понимаю, понимаешь? Он такой замечательный парень..."
    yum "...Я думаю, он заслуживает лучшего, это точно!"
    show yumi 3
    show player 12
    player_name "Ты не знаешь, куда он пошел этим утром, не так ли?"
    show player 5
    show yumi 4
    yum "Хм... Я не уверена, но он взял свою машину."
    show yumi 3
    show player 35
    player_name "Поэтому он поехал куда-то кататься..."
    show player 14
    player_name "... Хорошо, спасибо!"
    hide player
    hide yumi
    with dissolve
    return

label yumi_police_basement_dialogue_leave:
    show player 14 at left
    show yumi 1 at right
    player_name "Я здесь, чтобы навестить кое-кого."
    show yumi 2
    show player 1
    yum "Конечно. Не забудь оставить рюкзак в мусорном ведре и оставаться за линией."
    yum "Никаких прикосновений."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
