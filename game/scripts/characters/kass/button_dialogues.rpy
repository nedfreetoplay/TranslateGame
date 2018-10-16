label kassy_first_visit:
    show player 1f at right
    show kass 2 at left
    with dissolve
    Kass "Добро пожаловать к {b}Cupid{/b}. Меня зовут {b}Kassy{/b}, есть что не будь с чем я могу вам сегодня помочь?"
    show player 2f
    show kass 1
    player_name "Нет спасибо, Я только остматриваюсь."
    show player 1f
    show kass 2
    Kass "Хорошо. Что ж, дайте мне знать если вам понадобится помощь."
    show player 2f
    show kass 1
    player_name "Хорошо! Спасибо, {b}Kassy{/b}."
    show player 1f
    show kass 2
    Kass "Рада помочь!"
    return

label kassy_repeat:
    show player 2f at right
    show kass 1 at left
    with dissolve
    player_name "Привет {b}Kassy{/b}!"
    show player 1f
    show kass 2
    Kass "Здравствуйте, чем я могу вам помочь?"
    show player 2f
    show kass 1
    player_name "пока ничем, я только остматриваюсь."
    show player 1f
    show kass 2
    Kass "Отлично. Дайте мне знать если тебе что то понадобится."
    show player 2f
    show kass 1
    player_name "Конечно! Спасибо, {b}Kassy{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
