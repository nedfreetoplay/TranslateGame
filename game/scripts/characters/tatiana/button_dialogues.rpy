label tatiana_dialogue_pre:
    scene expression player.location.background_closeup with None
    show xtra 17 zorder 2
    show lily f_normal_talk zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    lily "Что случилось?"
    show lily f_normal
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "Мне кажется, я тебя где-то видел."
    show lily f_laugh
    show player 1
    lily "Правда. Ну, вы, наверное, видели меня в интернете..."
    show lily f_normal_talk
    lily "Я делаю много трансляций {b}видеоигр{/b}, и я публикую их на своем {b}YT канале{/b}."
    show lily f_sexy_talk
    lily "Я обычно выступаю под ником {b}VirginLilly69{/b}."
    show lily f_sexy
    show player 17
    player_name "А, точно! Мой друг {b}Эрик{/b} любит твои стримы!"
    show player 21
    player_name "Он продолжает говорить о твоих видео и твоих {b}огромных{/b}... эмм... фанатах!"
    show lily f_laugh
    show player 1
    lily "Ох... Ребята, вы такие милые."
    show lily f_normal_talk
    lily "Хочешь еще о чем-нибудь поговорить?"
    show lily f_normal
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "Есть ли у вас какие-либо предложения? Новые продукты которые вы порекомендовали бы?"
    show player 1
    lily "Хммм..."
    show lily f_normal_talk
    lily "Ну, я действительно люблю {b}косплей{/b}!"
    show lily f_sexy_talk
    lily "Мне нравится носить {b}сексуальные наряды{/b}. На самом деле, у нас есть новая линия костюмов, которые только что пришли!"
    show lily f_sexy
    show player 21
    player_name "О, правда? Звучит интересно..."
    show lily f_sexy_talk
    show player 1
    lily "Это иногда трудно, чтобы соответствовать моим... Ммм... формам."
    lily "Они делают их такими тугими, понимаешь?"
    show lily f_laugh
    lily "Но парни обычно не возражают!"
    show lily f_sexy
    show player 29
    player_name "Хаха. Я вижу."
    show player 2
    player_name "Спасибо, я сейчас посмотрю."
    show lily f_normal
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Да, думаю, у меня есть все, что мне нужно. Спасибо!"
    show lily f_normal_talk
    show player 1
    lily "Отлично! Спасибо за покупки в {b}Cosmic Cumics{/b}..."
    show lily f_laugh
    show player 13
    lily "И расскажите о нас друзьям!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
