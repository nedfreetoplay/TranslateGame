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
    tony "Ну, привет, малыш."
    tony "Что привело тебя сегодня?"
    show tony f_normal at flip
    show player 14f
    player_name "У меня для тебя доставка."
    show player 13f
    show tony f_suspicious
    tony "Доставка, да?"
    show tony f_normal_talk
    tony "... О, из молочного магазина!"
    show tony f_normal
    show player 14f
    player_name "Верно."
    show player 239_240f with dissolve
    pause
    show player 163df with dissolve
    show tony f_normal_talk
    tony "Прекрасно!"
    tony "Я не знаю, каких коров вы используете, но это молоко потрясающее!"
    tony "Это действительно поднимает наше тесто для пиццы на совершенно другой уровень!"
    show tony f_normal
    show player 163ef
    player_name "Хе-хе, я уверен, что {b}Диана{/b} будет рада это услышать."
    show player 163df
    show tony f_normal_talk
    tony "Я не шучу, малыш."
    tony "Скажи ей, что в следующий раз я утрою свой заказ."
    show tony f_normal
    show player 163ef
    player_name "Хе, хорошо."
    player_name "Хм, где я должен положить это?"
    show player 163df
    show tony f_normal_talk
    tony "О, да. Подожди..."
    show tony f_suspicious
    tony "Эй, {b}Мария{/b}!"
    tony "Тащи сюда свою задницу на секунду!"
    show tony f_normal
    pause
    show maria f_normal_talk zorder 1 at fliplleft with dissolve
    maria "{b}*вздыхая*{/b} Что случилось сейчас, {b}Тони{/b}?"
    show maria f_normal
    show tony f_question
    tony "Ничего страшного, заказ молока здесь."
    tony "Почему бы тебе не проводить паренька и не показать, где ты его хранишь?"
    show tony f_normal
    show maria f_shy_talk
    maria "{b}*вздыхая*{/b} Да, да... Хорошо."
    show maria f_normal_talk
    maria "Как тебя зовут, малыш?"
    show maria f_normal
    show player 163ef
    player_name "{b}[firstname]{/b}."
    show player 163df
    show maria f_normal_talk
    maria "О, Какое красивое имя!"
    maria "Иди за мной {b}в кладовку{/b}, {b}[firstname]{/b}."
    hide maria with dissolve
    player_name "..."
    scene black with fade
    hide player
    hide tony
    hide xtra
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
