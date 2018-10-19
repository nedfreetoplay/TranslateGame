label tatiana_dialogue_pre:
    scene comic_c
    show xtra 17 zorder 2
    show tatia 2 zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    tati "Чего желаем?"
    show tatia 1
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "Мне кажется, я тебя где-то видел."
    show tatia 3
    show player 1
    tati "Правда. Ну, вы, наверное, видели меня в интернете..."
    show tatia 2
    tati "Я делаю много трансляций {b}видеоигр{/b}, и я публикую их на своем {b}YT канал{/b}."
    show tatia 4
    tati "Я обычно пишу под именем {b}PureRuby87{/b}."
    show tatia 5
    show player 17
    player_name "А, точно! Мой друг {b}Эрик{/b} любит твои вещи!"
    show player 21
    player_name "Он продолжает говорить о твоих видео и твоих {b}огромных{/b}... эмм... фанатах!"
    show tatia 3
    show player 1
    tati "Ох... Ребята, вы такие милые."
    show tatia 2
    tati "Хочешь еще о чем-нибудь поговорить?"
    show tatia 1
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "Есть ли у вас какие-либо предложения? Новые продукты которые вы порекомендовали бы?"
    show player 1
    tati "Хммм..."
    show tatia 2
    tati "Ну, я действительно люблю {b}косплей{/b}!"
    show tatia 4
    tati "Мне нравится носить {b}сексуальные наряды{/b}. На самом деле, у нас есть новая линия костюмов, которые только что пришли!"
    show tatia 5
    show player 21
    player_name "О, правда? Звучит интересно..."
    show tatia 4
    show player 1
    tati "Это иногда трудно, чтобы соответствовать моим... Ммм... формам."
    tati "Они делают их такими тугими, понимаешь?"
    show tatia 3
    tati "Но парни обычно не возражают!"
    show tatia 5
    show player 29
    player_name "Хаха. Я вижу."
    show player 2
    player_name "Спасибо, я сейчас посмотрю."
    show tatia 1
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Да, думаю, у меня есть все, что мне нужно. Спасибо!"
    show tatia 2
    show player 1
    tati "Отлично! Спасибо за покупки в {b}Космических комиксах{/b}..."
    show tatia 3
    show player 13
    tati "И расскажите о нас друзьям!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
