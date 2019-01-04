label button_lucy_baby_dialogue:
    show player 14 at left
    show lucy
    player_name "Как поживает мой малыш?"
    show player 13
    show lucy f_laugh
    lucy "О, все хорошо!"
    show lucy f_normal_talk
    lucy "Все прекрасно проводят время!"
    lucy "Маленький {b}Джек{/b} преследовал всех девочек сегодня."
    lucy "За этим ребенком мы должны присматривать, когда он подрастет."
    show lucy f_normal
    show player 14
    player_name "Глупые дети."
    player_name "Ну, они все выглядят так, будто им весело!"
    show player 13
    show lucy f_laugh
    lucy "О да! Это все, что мы делаем каждый день, это веселимся, веселимся, веселимся!"
    show lucy f_normal
    show player 14
    player_name "Хорошо. Ну, я просто подумал, что зайду и посмотрю, что все делают."
    show player 13
    show lucy f_normal_talk
    lucy "Ауууууу."
    lucy "Должна сказать, это так приятно видеть, как папа заходит и проверяет своего малыша."
    show lucy f_normal
    return

label button_lucy_baby_dialogue_multiple:
    show player 14 at left
    show lucy
    player_name "Как поживают мои дети?"
    show player 13
    show lucy f_laugh
    lucy "О, все хорошо!"
    show lucy f_normal_talk
    lucy "Все прекрасно проводят время!"
    if randomizer() > 50:
        lucy "Пришлось следить за {b}Джейкобом{/b}."
        lucy "Он нашел несколько наклеек и расклеял их повсюду."
    elif randomizer() > 50:
        lucy "Маленький {b}Джек{/b} преследовал всех девочек сегодня."
        lucy "За этим ребенком мы должны присматривать, когда он подрастет."
    else:
        lucy "В остальном дети вели себя довольно хорошо."
        lucy "Я бы хотела, чтобы все дни были такими."
    show lucy f_normal
    show player 14
    player_name "Глупые дети."
    player_name "Ну, они все выглядят так, будто им весело!"
    show player 13
    show lucy f_laugh
    lucy "О да! Это все, что мы делаем каждый день, это веселимся, веселимся, веселимся!"
    show lucy f_normal
    show player 14
    player_name "Хорошо. Ну, я просто подумал, что зайду и посмотрю, что все делают."
    show player 13
    show lucy f_normal_talk
    lucy "Ауууу."
    lucy "Должна сказать, это так приятно видеть, как папа заходит и проверяет своих малышей."
    show lucy f_normal
    return

label lucy_button_intro_day:
    show player 13 at left
    show lucy f_normal_talk
    with dissolve
    lucy "Привет, {b}[firstname]{/b}."
    lucy "Что привело тебя сегодня?"
    show lucy f_normal
    show player 14
    player_name "О, я просто была по соседству и подумала поздороваться."
    show player 13
    show lucy f_normal_talk
    lucy "Что ж, это замечательно."
    show lucy f_normal
    return

label lucy_button_intro_night:
    show player 13 at left
    show lucy f_sad_talk b_messy a_dressed_cover
    with dissolve
    lucy "О, боже."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "Я не знала, что ты прийдешь, {b}[firstname]{/b}."
    show lucy f_normal_talk_down
    lucy "Я думаю, я выгляжу как чучело..."
    show lucy f_normal
    show player 14
    player_name "Нет, все не так."
    player_name "Ты всегда хорошо выглядишь, {b}Люси{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "Ну, это приятно слышать."
    show lucy f_normal
    return

label button_lucy_how_are_you:
    show player 14 at left
    show lucy f_normal
    player_name "Ты в порядке?"
    show player 13
    lucy "Хмм?"
    show lucy f_normal_talk
    lucy "О, со мной все в порядке."
    show lucy f_laugh
    lucy "Эти дети просто просветляют мне день."
    show lucy f_normal
    show player 12
    player_name "{b}Ричард{/b} хорошо с тобой обращается?"
    show player 5
    show lucy f_normal_talk
    lucy "О, ты знаешь {b}Ричарда{/b}."
    lucy "Он твердо стоит на своем."
    show lucy f_normal
    show player 12
    player_name "Дай мне знать, если тебе когда-нибудь понадобится помощь, хорошо?"
    show player 5
    show lucy f_normal_talk
    lucy "Ты такой милый."
    lucy "Спасибо, {b}[firstname]{/b}."
    show lucy f_normal
    return

label button_lucy_hows_the_milk:
    show player 14 at left
    show lucy f_normal
    player_name "Удовлетворены ли вы последней партией молока?"
    show player 13
    show lucy f_laugh
    lucy "О, да."
    show lucy f_normal_talk
    lucy "Малыши просто не могут насытиться."
    show lucy f_normal
    show player 10
    player_name "Тебе правда нравится присматривать за всеми этими детьми?"
    show player 5
    show lucy f_laugh
    lucy "Я обожаю их!"
    show lucy f_normal_talk
    lucy "Это делает меня молодой, понимаешь?"
    show lucy f_normal
    show player 14
    player_name "Ну, ты определенно выглядишь молодо."
    show player 13
    show lucy f_smirk_talk
    lucy "Ауу, ты такой очаровашка, {b}[firstname]{/b}!"
    show lucy f_smirk
    return

label button_lucy_annie_around_day:
    show player 10 at left
    show lucy f_normal
    player_name "{b}Энни{/b} тут?"
    show player 5
    show lucy f_normal_talk
    lucy "Нет, я думаю, она в школе."
    lucy "Хочешь, я скажу ей, что ты заходил?"
    show lucy f_normal
    show player 10
    player_name "Нет, все в порядке."
    player_name "Мне просто было любопытно."
    show player 5
    return

label button_lucy_annie_around_night:
    show player 10 at left
    show lucy f_normal
    player_name "{b}Энни{/b} тут?"
    show player 5
    show lucy f_normal_talk
    lucy "Я думаю, она упомянула, что ей нужно сделать домашнее задание."
    lucy "Ты знаешь ее, она очень придирчива к своей школьной работе."
    show lucy f_normal
    show player 10
    player_name "О, я знаю."
    show player 14
    player_name "Спасибо, {b}Люси{/b}."
    show player 13
    lucy "Мммммммм."
    return

label button_lucy_leave:
    show player 14 at left
    show lucy f_normal
    player_name "Мне нужно идти."
    show player 13
    show lucy f_normal_talk
    lucy "Хорошо, милый."
    show lucy f_normal
    show player 14
    player_name "Было приятно увидеть тебя снова."
    show player 13
    show lucy f_normal_talk
    lucy "Мне тоже, дорогуша."
    hide player
    hide lucy
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
