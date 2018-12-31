label tatiana_dialogue_pre:
    scene comic_c
    show xtra 17 zorder 2
    show lilly f_normal_talk zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    lilly "Что случилось?"
    show lilly f_normal
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "Мне кажется, я тебя где-то видел."
    show lilly f_laugh
    show player 1
    lilly "Правда. Ну, вы, наверное, видели меня в интернете..."
    show lilly f_normal_talk
    lilly "Я делаю много трансляций {b}видеоигр{/b}, и я публикую их на своем {b}YT канал{/b}."
    show lilly f_sexy_talk
    lilly "Я обычно выступаю под ником {b}VirginLilly69{/b}."
    show lilly f_sexy
    show player 17
    player_name "А, точно! Мой друг {b}Эрик{/b} любит твои стримы!"
    show player 21
    player_name "Он продолжает говорить о твоих видео и твоих {b}огромных{/b}... эмм... фанатах!"
    show lilly f_laugh
    show player 1
    lilly "Ох... Ребята, вы такие милые."
    show lilly f_normal_talk
    lilly "Хочешь еще о чем-нибудь поговорить?"
    show lilly f_normal
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "Есть ли у вас какие-либо предложения? Новые продукты которые вы порекомендовали бы?"
    show player 1
    lilly "Хммм..."
    show lilly f_normal_talk
    lilly "Ну, я действительно люблю {b}косплей{/b}!"
    show lilly f_sexy_talk
    lilly "Мне нравится носить {b}сексуальные наряды{/b}. На самом деле, у нас есть новая линия костюмов, которые только что пришли!"
    show lilly f_sexy
    show player 21
    player_name "О, правда? Звучит интересно..."
    show lilly f_sexy_talk
    show player 1
    lilly "Это иногда трудно, чтобы соответствовать моим... Ммм... формам."
    lilly "Они делают их такими тугими, понимаешь?"
    show lilly f_laugh
    lilly "Но парни обычно не возражают!"
    show lilly f_sexy
    show player 29
    player_name "Хаха. Я вижу."
    show player 2
    player_name "Спасибо, я сейчас посмотрю."
    show lilly f_normal
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Да, думаю, у меня есть все, что мне нужно. Спасибо!"
    show lilly f_normal_talk
    show player 1
    lilly "Отлично! Спасибо за покупки в {b}Cosmic Cumics{/b}..."
    show lilly f_laugh
    show player 13
    lilly "И расскажите о нас друзьям!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
