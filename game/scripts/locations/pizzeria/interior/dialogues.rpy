label pizza_interior_pizza_count_0:
    scene location_pizza_day_blur
    show player 10f at right with dissolve
    player_name "Привет! Есть ли здесь кто-"
    show tony f_normal_talk zorder 1 at fliplleft with dissolve
    show player 11f
    tony "Эййй, да ты только взгляни на него!"
    tony "Высокий, молодой, красивый."
    tony "Он напоминает мне самого себя в молодости."
    show tony f_normal
    show player 10f
    player_name "Я?"
    show tony f_question
    show player 13f
    tony "Да, ты, вот что я тебе скажу: Ищешь работёнку?"
    show tony f_normal
    show player 14f
    player_name "Да, я долго искал хоть какую-нибудь."
    show tony f_normal_talk
    show player 203f
    tony "Отлично. Мне пригодится кто-нибудь вроде тебя."
    show player 10f
    show tony f_normal
    player_name "Кто-то вроде меня?"
    show player 11f
    show tony f_normal_talk
    tony "Ну конечно же! Кто-то типа тебя! Подожди здесь, я позову свою жену."
    show player 203f
    show maria f_normal zorder 0 at flip, Position (xpos=750) with dissolve
    show tony f_normal_talk
    tony "Мария: это {b}[firstname]{/b}, {b}[firstname]{/b}: это Мария."
    show tony f_normal
    show maria f_normal_talk at flip
    maria "Привет, {b}[firstname]{/b}. Пологаю ты будешь нашим новым помощником."
    show player 14f
    show maria f_normal
    player_name "Ага, похоже на то."
    show player 203f
    show maria f_shy_talk
    maria "Тони, не большой вопрос: Откуда нам знать будет ли с этого парня хоть какая-то польза?"
    show maria f_shy
    show tony f_normal_talk
    tony "Ниоткуда, но ты только взляни на него! Он молод, полон энергии, и выглядит здаровым!"
    tony "Что ещё нам нужно?"
    show maria f_normal_talk
    show player 11f
    show tony f_normal
    maria "Кто-то кто бы работал, потому как прошлый ребёнок которого ты нанял, был ленивым подростком."
    show maria f_normal
    show tony f_question
    tony "Он будет работать. Я ручаюсь за него. Верно {b}[firstname]{/b}?"
    show tony f_normal
    show player 14f
    player_name "Ага. Вы предложили, и мне нужно работа."
    show tony f_normal_talk
    show player 203f
    tony "Тогда решено! Приходи позже, и мы обсудим дальнейшие дела."
    show maria f_normal_talk
    tonymaria "Хорошего дня!"
    hide tony
    hide maria
    hide player
    with dissolve
    return

label pizza_interior_diane_delivery_1:
    scene pizza_behind_c
    show xtra 12 zorder 2 with None
    show player 13f zorder 3 at right
    show tony f_normal_talk zorder 0 at flip, Position (xpos=750)
    with dissolve
    tony "Well, hey there, kiddo."
    tony "What brings you in today?"
    show tony f_normal at flip
    show player 14f
    player_name "I have a delivery for you."
    show player 13f
    show tony f_suspicious
    tony "Delivery, eh?"
    show tony f_normal_talk
    tony "... Oh, from the milk place!"
    show tony f_normal
    show player 14f
    player_name "That's right."
    show player 239_240f with dissolve
    pause
    show player 163df with dissolve
    show tony f_normal_talk
    tony "Excellent!"
    tony "I dunno what kind of cows you're using but this milk is amazing!"
    tony "It really takes our pizza dough to a whole 'nother level!"
    show tony f_normal
    show player 163ef
    player_name "Hehe, I'm sure {b}Diane{/b} will be happy to hear that."
    show player 163df
    show tony f_normal_talk
    tony "I'm not joking, kiddo."
    tony "You tell her, that next time, I'm gonna triple my order."
    show tony f_normal
    show player 163ef
    player_name "Heh, okay."
    player_name "Umm, where should I put this?"
    show player 163df
    show tony f_normal_talk
    tony "Oh, right. One second..."
    show tony f_suspicious
    tony "Hey, {b}Maria{/b}!"
    tony "Getcha' butt up here for a second!"
    show tony f_normal
    pause
    show maria f_normal_talk zorder 1 at fliplleft with dissolve
    maria "{b}*Sigh*{/b} What's the matter now, {b}Tony{/b}?"
    show maria f_normal
    show tony f_question
    tony "Ain't nothing the matter, the milk order is here."
    tony "Why don't you take the kid in back and show him where you keep it?"
    show tony f_normal
    show maria f_shy_talk
    maria "{b}*Sigh*{/b} Yeah, yeah... Alright."
    show maria f_normal_talk
    maria "What's your name, kid?"
    show maria f_normal
    show player 163ef
    player_name "{b}[firstname]{/b}."
    show player 163df
    show maria f_normal_talk
    maria "Oh, that's a nice name!"
    maria "Follow me {b}into the back{/b}, {b}[firstname]{/b}."
    hide maria with dissolve
    player_name "..."
    scene black with fade
    hide player
    hide tony
    hide xtra
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
