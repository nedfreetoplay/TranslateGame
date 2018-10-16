label pizza_exterior_first_visit:
    scene expression game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")
    show player 14 with dissolve
    player_name "( Пицца Тони. Он известен тем, что делает лучшую пиццу в городе. )"
    hide player with dissolve
    return

label pizza_interior_pizza_count_0:
    scene location_pizza_day_blur
    show player 10f at right with dissolve
    show tony 1 at Position(xpos = 300, ypos = 768) with dissolve
    player_name "Привет! Есть ли здесь кто-"
    show tony 2
    show player 11f
    tony "Эййй, да ты только взгляни на него!"
    tony "Высокий, молодой, красивый."
    tony "Он напоминает мне самого себя в молодости."
    show tony 1
    show player 10f
    player_name "Me?"
    show tony 3
    show player 13f
    tony "Да ты, вот что я тебе скажу: Ищешь работёнку?"
    show tony 1
    show player 14f
    player_name "Yeah, I've been looking for one."
    show tony 2
    show player 203f
    tony "Отлично. Мне пригодится кто-нибудь вроде тебя."
    show player 10f
    show tony 1
    player_name "Кто-то вроде меня?"
    show player 11f
    show tony 2
    tony "Ну конечно же! Кто-то типа тебя! Подожди здесь, я позову свою жену."
    show player 203f
    show maria 1 at left
    show tony 2
    tony "Мария: это {b}[firstname]{/b}, {b}[firstname]{/b}: это Мария."
    show tony 1
    show maria 2
    maria "Привет, {b}[firstname]{/b}. Пологаю ты будешь нашим новым помощником."
    show player 14f
    show maria 1
    player_name "Ага, похоже на то."
    show player 203f
    show maria 3
    maria "Тони, не большой вопрос: Откуда нам знать будет ли с этого парня хоть какая-то польза?"
    show maria 1
    show tony 2
    tony "Ни откуда, но ты только взляни на него! Он молод, полон энергии, и выглядит здаровым!"
    tony "Что ещё нам нужно?"
    show maria 2
    show player 11f
    show tony 1
    maria "Кто-то кто бы работал, потому как прошлый ребёнок которого ты нанял, был ленивым подростком."
    show maria 1
    show tony 3
    tony "Он будет работать. Я ручаюсь за него. Верно {b}[firstname]{/b}?"
    show tony 1
    show player 14f
    player_name "Ага. Вы предложили, и мне нужно работа."
    show tony 2
    show player 203f
    tony "Тогда решено! Приходи позже, и мы обсудим дальнейшие дела."
    show maria 2
    tonymaria "Хорошего дня!"
    hide tony
    hide maria
    hide player
    with dissolve
    return

label pizza_closed:
    scene expression "backgrounds/location_pizza_outside_night.jpg"
    show player 14 with dissolve
    player_name "Я не могу пойти туда ночью!"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
