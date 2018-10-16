label tatiana_dialogue_pre:
    scene comic_c
    show xtra 17 zorder 2
    show tatia 2 zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    tati "Как дела?"
    show tatia 1
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "Такое чувство, что я вас уже где-то видел."
    show tatia 3
    show player 1
    tati "Точно. Ну, ты вероятно видел меня в интернете..."
    show tatia 2
    tati "Я много {b}стримлю видео-игры{/b} и я выставляю их на {b}YT channel{/b}."
    show tatia 4
    tati "Обычно я подписана под ником {b}PureRuby87{/b}."
    show tatia 5
    show player 17
    player_name "Ах, точно! Мой друг {b}Erik{/b} любит твои материалы!"
    show player 21
    player_name "Он не перестает говорить о твоих видео и о твоих {b}huge{/b}... эмм... поклонниках!"
    show tatia 3
    show player 1
    tati "Ахх... Ребята, вы такие милые."
    show tatia 2
    tati "Есть ли что не будь еще, о чем бы ты хотел поговорить?"
    show tatia 1
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "У вас есть какие-нибудь предложения? Какие новые продукты вы можете порекомендовать?"
    show player 1
    tati "Хммм..."
    show tatia 2
    tati "Что ж, Я очень люблю {b}косплей{/b}!"
    show tatia 4
    tati "Я люблю носить {b}Сексуально белье{/b}. На самом деле, у нас есть новая линия костюмов которую мы только что получили!"
    show tatia 5
    show player 21
    player_name "Ох, даа? Звучит интересно..."
    show tatia 4
    show player 1
    tati "Это иногда трудно запихнуть... эмм... формы в них."
    tati "Они делают их настолько тугими, ты знаешь?"
    show tatia 3
    tati "Но парни обычно не возражают!"
    show tatia 5
    show player 29
    player_name "Хаха. Я вижу."
    show player 2
    player_name "Спасибо, Я посмотрю."
    show tatia 1
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Даа, Я думаю у меня есть все что мне нужно. Спасибо!"
    show tatia 2
    show player 1
    tati "Отлично! Спасибо что совершили покупки в {b}Cosmic Cumics{/b}..."
    show tatia 3
    show player 13
    tati "И расскажи своим друзьям о нас!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
