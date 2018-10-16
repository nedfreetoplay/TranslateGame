label mia_dialogue_mias_house_front_intro:
    scene location_mia_closeup
    show player 14 at left
    show mia 1 at right
    with dissolve
    player_name "Привет {b}Mia{/b}!"
    show mia 4
    show player 1
    mia "Приветик {b}[firstname]{/b}!"
    mia "Что ты здесь делаешь?"
    show mia 1
    show player 29
    player_name "Эммм... Я хотел спросить у тебя кое-что!"
    return

label mia_dialogue_mias_house_front_homework:
    show player 21
    player_name "Тебе еще нужна помощь с подготовкой к экзаменами?"
    show mia 3
    show player 13
    mia "Конечно! Я как раз ищу {b}кого-то с кем можно было бы позаниматься вместе{/b}..."
    show mia 6
    show player 11
    mia "...Но ты догнал классную программу?"
    show mia 2
    show player 10
    player_name "Ох! Точно! стоит взять пару несколько частных занятий с {b}Miss Bissette{/b} что бы наверстать упущенное..."
    show mia 6
    show player 13
    mia "Да, ты должен это сделать в первую очередь!"
    show mia 4
    mia "Тогда ты сможешь прийти ко мне домой... и мы сможем  позаниматься в моей комнате!"
    show mia 1
    show player 14
    player_name "Дд... да?"
    show mia 3
    show player 1
    mia "Конечно! Это будет весело!"
    show mia 1
    show player 17
    player_name "Хорошо... Я тебе скажу когда я закончу!"
    show mia 4
    show player 1
    mia "До скорой встречи!"
    hide mia with dissolve
    show player 5 with dissolve
    player_name "( Я должен постараться и и закончить мою {b}Французкую домашнюю работу{/b}, что бы я смог позаниматься с {b}Mia{/b}. )"
    show player 4
    pause
    player_name "( Интересно почему она выбрала меня что бы помочь ей с подготовкой. )"
    player_name "( Она обычно училась с {b}Judith{/b} и она действительно хороша во Французком... )"
    player_name "( ...Я не уверен как я смогу помочь её. )"
    show player 13
    player_name "( По крайней мере мы потусим вместе, и она действительно очень милая... )"
    hide player with dissolve
    return

label mia_dialogue_mias_house_front_leave:
    show player 4
    player_name "Хмм... Да, но я забыл!"
    show mia 3
    show player 11
    mia "Хаха! Ты смешной~"
    show mia 1
    show player 17
    player_name "Извини! Я не могу вспомнить что я хотел сказать!"
    show player 14
    player_name "Мне пора идти."
    show mia 4
    show player 1
    mia "Спокойной ночи!"
    hide player
    hide mia
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
