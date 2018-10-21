label mia_dialogue_mias_house_front_intro:
    scene location_mia_closeup
    show player 14 at left
    show mia 1 at right
    with dissolve
    player_name "Эй {b}Мия{/b}!"
    show mia 4
    show player 1
    mia "Привет {b}[firstname]{/b}!"
    mia "Что ты здесь делаешь?"
    show mia 1
    show player 29
    player_name "Эм... Я хотела спросить тебя кое о чем!"
    return

label mia_dialogue_mias_house_front_homework:
    show player 21
    player_name "Вам все еще нужна помощь в обучении для сдачи экзаменов?"
    show mia 3
    show player 13
    mia "Конечно! Я ищу {b} кого-то с кем можно вместе учиться{/b}..."
    show mia 6
    show player 11
    mia "...Но ты уже догнал класс?"
    show mia 2
    show player 10
    player_name "О! Точно! Мне, вероятно, следует получить частное репетиторство от {b}Мисс Биссетт{/b}, чтобы наверстать упущенное..."
    show mia 6
    show player 13
    mia "Да, ты, вероятно, должен сделать это впервую очередь!"
    show mia 4
    mia "Тогда ты можешь приходить ко мне домой..., и мы будем учиться в моей комнате!"
    show mia 1
    show player 14
    player_name "Д... да?"
    show mia 3
    show player 1
    mia "Я уверена! Это будет весело!"
    show mia 1
    show player 17
    player_name "Хорошо... Я дам тебе знать, когда я закончу с этим!"
    show mia 4
    show player 1
    mia "Скоро увидимся!"
    hide mia with dissolve
    show player 5 with dissolve
    player_name "( Я должен попытаться закончить домашнюю домашнюю работу {b}французскому{/b}, с этим я смогу учиться с {b}Мией{/b}. )"
    show player 4
    pause
    player_name "( Интересно, почему она выбрала меня, чтобы помочь ей учиться. )"
    player_name "( Обычно она учится с {b}Джуди{/b}, и она очень хорошо говорит по-французски... )"
    player_name "( ...Я не знаю, как я могу ей помочь. )"
    show player 13
    player_name "( По крайней мере, мы потусуемся, и она очень милая... )"
    hide player with dissolve
    return

label mia_dialogue_mias_house_front_leave:
    show player 4
    player_name "Хмм... Да, но я забыл!"
    show mia 3
    show player 11
    mia "Хаха! Ты забавный~"
    show mia 1
    show player 17
    player_name "Прости! Я не могу вспомнить, что я хотел сказать!"
    show player 14
    player_name "Я должен идти."
    show mia 4
    show player 1
    mia "Спокойной ночи!"
    hide player
    hide mia
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
