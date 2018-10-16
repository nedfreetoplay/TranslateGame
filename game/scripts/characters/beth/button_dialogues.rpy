label beth_dialogue_pre:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Привет, мистер!"
    show player 14
    show beth 1
    player_name "Привет."
    show player 1
    show beth 2
    beth "Хотите купить сладких пончиков, не так ли?"
    show beth 1
    return

label beth_dialogue_do_not_know:
    show player 14
    player_name "Хмм... Я еще не уверен, что мне это нужно купить."
    show player 1
    show beth 2
    beth "Не знаете?"
    show player 14
    show beth 1
    player_name "Ну, я покупаю это в подарок, но не знаю, что нравится."
    show player 1
    show beth 2
    beth "Я не смогу тебе помочь, если ты не знаешь, чего хочешь!"
    show player 14
    show beth 1
    player_name "Я вернусь позже, когда узнаю."
    return

label beth_dialogue_want_donuts:
    show player 14
    player_name "Я бы хотел купить маленькую коробочку, пожалуйста."
    show player 1
    show beth 2
    beth "Конечно!"
    beth "Какую глазурь и начинку вы бы хотели?"
    return

label beth_dialogue_leave:
    show player 14
    player_name "Хорошо, спасибо!"
    player_name "Возможно в другой раз..."
    show player 1
    show beth 2
    beth "Конечно, пока!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
