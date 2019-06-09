label kassy_first_visit:
    show player 1f at right
    show kassy f_normal_talk at flip
    with dissolve
    Kass "Добро пожаловать в магазин {b}Амур{/b}. Меня зовут {b}Касси{/b}, есть что не будь с чем я могу вам сегодня помочь?"
    show player 2f
    show kassy f_normal
    player_name "Нет, спасибо, Я только осматриваюсь."
    show player 1f
    show kassy f_normal_talk
    Kass "Хорошо. Что ж, дайте мне знать если вам понадобится помощь."
    show player 2f
    show kassy f_normal
    player_name "Хорошо! Спасибо, {b}Касси{/b}."
    show player 1f
    show kassy f_normal_talk
    Kass "Рада помочь!"
    return

label kassy_repeat:
    show player 2f at right
    show kassy f_normal at flip
    with dissolve
    player_name "Привет, {b}Касси{/b}!"
    show player 1f
    show kassy f_normal_talk
    Kass "Здравствуйте, чем я могу вам помочь?"
    show player 2f
    show kassy f_normal
    player_name "Пока ничем, я только осматриваюсь."
    show player 1f
    show kassy f_normal_talk
    Kass "Отлично. Дай мне знать, если тебе что то понадобится."
    show player 2f
    show kassy f_normal
    player_name "Конечно! Спасибо, {b}Касси{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
