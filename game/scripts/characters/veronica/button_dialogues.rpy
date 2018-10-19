label veronica_dialogue_pre:
    scene location_mall_consumr_closeup
    show player 1 at left
    show veronica 2 at right
    with dissolve
    vero "Добро пожаловать в {b}CONSUM-R{/b}! Меня зовут {b}Вероника{/b}."
    show veronica 4
    vero "Могу ли я вам чем-нибудь помочь?"
    show veronica 1
    return

label veronica_dialogue_vegatable_stock:
    show player 2
    player_name "Мне нужен {b}овощной бульон{/b}. У вас есть он?"
    show player 1
    show veronica 2
    vero "Я боюсь, что мы всё продали."
    show player 10
    show veronica 1
    player_name "Ох черт..."
    show player 11
    show veronica 2
    vero "Может вам подойдет {b}Куриный бульон{/b}? Он у нас ещё есть."
    show player 10
    show veronica 1
    player_name "Я не уверен..."
    player_name "А может его просто скоро доставят?"
    show player 11
    show veronica 2
    vero "У нас ежедневная доставка, но я не знаю, когда именно этот товар будет на прилавке."
    show player 10
    show veronica 1
    player_name "Дерьмо..."
    player_name "Ладно, спасибо."
    hide veronica with dissolve
    show player 10 with dissolve

    player_name "Хмм, думаю {b}куриный бульон{/b} должен сгодиться."
    show player 2
    player_name "Надо просто купить его и отнести Оките."

    return

label veronica_dialogue_bug_spray:
    show player 4
    player_name "Ух..."
    show player 12
    player_name "У вас есть пестицид?"
    show veronica 4
    show player 1
    vero "Да! У нас широкий выбор товаров для уничтожения вредителей!"
    show veronica 1
    show player 2
    player_name "Хмм... Что насчет насекомых?"
    show veronica 3
    show player 1
    vero "Ну... Есть разные препараты от насекомых..."
    show veronica 2
    show player 11
    vero "Вы знаете, какой именно тип жуков вам досаждает?"
    show veronica 1
    show player 10
    player_name "Я не совсем уверен, что это за жуки..."
    show veronica 3
    show player 13
    vero "Ну, как {b}они выглядят{/b}?"
    show veronica 1
    return

label veronica_dialogue_bug_spray_large_wings:
    show player 35
    player_name "У них пара больших крыльев..."
    show veronica 3
    show player 11
    vero "Хмм... Может быть это {b}кузнечики{/b}..."
    show veronica 4
    show player 1
    vero "Возьмите спрей с {b}красной крышкой{/b}. Он называется {b}Истребитель жуков{/b}."
    show veronica 2
    vero "Он должен помочь!"
    show veronica 1
    show player 17
    player_name "Окей, спасибо!"
    return

label veronica_dialogue_bug_spray_pincers:
    show player 35
    player_name "У них большие клешни..."
    show veronica 3
    show player 11
    vero "Хмм... Может это {b}уховертки{/b}... Мерзкие твари!"
    show veronica 4
    show player 1
    vero "Возьмите спрей с {b}зеленой крышкой{/b}. Он называется {b}Уничтожитель жуков{/b}."
    show veronica 2
    vero "Он должен помочь!"
    show veronica 1
    show player 17
    player_name "Окей, спасибо!"
    return

label veronica_dialogue_bug_spray_white_spots:
    show player 35
    player_name "У них белые пятна на панцире..."
    show veronica 3
    show player 11
    vero "Хмм... Может это {b}мраморный хрущ{/b}..."
    show veronica 4
    show player 1
    vero "Возьмите спрей с {b}синей крышкой{/b}. Он называется {b}Ликвидатор жуков{/b}."
    show veronica 2
    vero "Он должен помочь!"
    show veronica 1
    show player 17
    player_name "Окей, спасибо!"
    return

label veronica_dialogue_leave:
    show player 2
    player_name "Эм..."
    show player 17
    player_name "Я думаю, мне не нужна помощь!"
    show veronica 4
    show player 1
    vero "Отлично!"
    show veronica 2
    vero "Просто скажите, если вам что-нибудь понадобится."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
