label veronica_dialogue_pre_d05:
    show player 13 at left
    show vero f_normal_talk
    with dissolve
    vero "Добро пожаловать в магазин {b}Consum-R{/b}, где все что вам нужно находится всего в нескольких шагах."
    vero "Чем я могу вам помочь сегодня?"
    show vero f_normal
    return

label veronica_dialogue_pre_d11:
    show player 5 at left
    show vero f_normal_talk
    vero "Добро пожаловать в магазин {b}Consum-R{/b}, где все что вам нужно-"
    vero "{b}[firstname]{/b}?"
    show vero f_normal
    show player 12
    player_name "Привет {b}Вероника{/b}."
    show player 5
    show vero f_normal_talk
    vero "Что привело тебя сюда сегодня?"
    show vero f_normal
    return

label veronica_dialogue_pre_d20:
    show player 5 at left
    show vero f_normal_talk
    with dissolve
    vero "Добро пожаловать в магазин {b}Consum-R{/b}, где все что вам нужно-"
    vero "О."
    show vero f_sexy_talk
    vero "Привет, красавчик!"
    show vero f_sexy
    show player 10
    player_name "Привет {b}Вероника{/b}."
    show player 5
    show vero f_sexy_talk
    vero "Что привело тебя сюда сегодня?"
    show vero f_sexy
    return

label veronica_dialogue_vegatable_stock:
    show player 2
    show vero
    player_name "Я ищу {b}овощной бульон{/b}. У вас есть?"
    show player 1
    show vero f_normal_talk
    vero "Боюсь, мы все распродали на данный момент."
    show player 10
    show vero f_normal
    player_name "О, блин..."
    show player 11
    show vero f_normal_talk
    vero "Может {b}куриный бульон{/b} подойдет? У нас его много."
    show player 10
    show vero f_normal
    player_name "Я не знаю..."
    player_name "Скоро будет доставка или что-то подобное?"
    show player 11
    show vero f_normal_talk
    vero "Мы получаем поставки ежедневно, но я понятия не имею, когда данный товар можно будет купить."
    show player 10
    show vero f_normal
    player_name "Зараза..."
    player_name "Хорошо, спасибо."
    hide vero with dissolve
    show player 10 with dissolve
    player_name "Хмм, думаю {b}куриный бульон{/b} подойдет."
    show player 2
    player_name "Я должен купить немного и отнести к Оките."
    return

label veronica_dialogue_bug_spray:
    show player 4
    player_name "Ух..."
    show player 12
    player_name "Я ищу пестициды?"
    show vero f_laugh
    show player 1
    vero "О да! У нас есть множество средств от вредителей!"
    show vero f_normal
    show player 2
    player_name "Хм ... Как насчет насекомых?"
    show vero f_thinking
    show player 1
    vero "Ну ... Есть много видов пестицидов для насекомых ..."
    show vero f_normal_talk
    show player 11
    vero "Вы знаете, с каким типом жуков вы имеете дело?"
    show vero f_normal
    show player 10
    player_name "Я не совсем уверен, что это такое..."
    show vero f_thinking
    show player 13
    vero "Ну, как {b}они выгледят{/b}?"
    show vero f_normal
    return

label veronica_dialogue_bug_spray_large_wings:
    show player 35
    player_name "У них были большие крылья..."
    show vero f_thinking
    show player 11
    vero "Хмм... Может быть это {b}кузнечики{/b}..."
    show vero f_laugh
    show player 1
    vero "Пожалуй поможет спрей с {b}красной крышкой{/b}. Он называется {b}Уничтожитель жуков{/b}."
    show vero f_normal_talk
    vero "Это должно сработать!"
    show vero f_normal
    show player 17
    player_name "Хорошо, спасибо!"
    return

label veronica_dialogue_bug_spray_pincers:
    show player 35
    player_name "У них были большие клещи..."
    show vero f_thinking
    show player 11
    vero "Хмм... Может быть это {b}уховертки{/b}... Мерзкие твари!"
    show vero f_laugh
    show player 1
    vero "Пожалуй поможет спрей с {b}зеленой крышкой{/b}. Он называется {b}Аннигилятор жуков{/b}."
    show vero f_normal_talk
    vero "Это должно сработать!"
    show vero f_normal
    show player 17
    player_name "Хорошо, спасибо!"
    return

label veronica_dialogue_bug_spray_white_spots:
    show player 35
    player_name "На их панцирях были белые пятна..."
    show vero f_thinking
    show player 11
    vero "Хмм... Может быть это {b}жук-навозник{/b}..."
    show vero f_laugh
    show player 1
    vero "Пожалуй поможет спрей с {b}синей крышкой{/b}. Он называется {b}Ликвидатор жуков{/b}."
    show vero f_normal_talk
    vero "Это должно сработать!"
    show vero f_normal
    show player 17
    player_name "Хорошо, спасибо!"
    return

label veronica_dialogue_leave:
    show player 10 at left
    show vero f_normal
    player_name "Я только осмотрюсь, спасибо."
    show player 5
    show vero f_normal_talk
    vero "Нет проблем."
    vero "ДАйте мне знать если что-нибудь будет нужно."
    show vero f_normal
    show player 10
    player_name "Хорошо."
    hide player
    hide vero
    with dissolve
    return

label veronica_dialogue_what_do_you_sell:
    show player 10 at left
    show vero f_normal
    player_name "Что вы здесь продаете?"
    show player 5
    show vero f_laugh
    vero "Наверное, будет быстрее сказать вам то, что мы не продаем."
    show vero f_normal_talk
    vero "Мы продаем почти все, что нужно человеку."
    show vero f_normal
    show player 10
    player_name "Так я могу купить инструменты здесь?"
    show player 5
    show vero f_normal_talk
    vero "Конечно."
    show vero f_normal
    show player 10
    player_name "Как насчет продуктов?"
    show player 5
    show vero f_normal_talk
    vero "Угу."
    show vero f_normal
    show player 401
    player_name "Детали компьютера?!"
    show player 403
    show vero f_normal_talk
    vero "Есть такие."
    show vero f_normal
    show player 402
    player_name "Одежда?"
    show player 403
    show vero f_laugh
    vero "Во всех размерах."
    show vero f_normal
    show player 402
    player_name "Кухонные принадлежности?!"
    show player 403
    show vero f_normal_talk
    vero "Проход 12."
    show vero f_normal
    show player 4 with dissolve
    player_name "Хмм."
    show player 401 with dissolve
    player_name "Как насчет велосипедов?"
    show player 403
    show vero f_thinking
    vero "Горные велосипеды или BMX?"
    show vero f_sexy_talk
    vero "Потому что у нас есть оба."
    show vero f_sexy
    show player 402
    player_name "Ух ты, ребята, вы действительно продаете все."
    show player 403
    show vero f_sexy_talk
    vero "Я же тебе говорила."
    show vero f_normal
    return

label veronica_dialogue_you_look_nice:
    show player 14 at left
    show vero f_normal
    player_name "Ты сегодня хорошо выглядишь."
    show player 13
    show vero f_rolleyes
    vero "О, прекрати это."
    show vero f_sexy_talk_down
    vero "Никто не может хорошо выглядеть в этой нелепой униформе..."
    show vero f_sexy
    show player 10
    player_name "Ты можешь."
    show player 5
    show vero f_sexy_talk
    vero "О, это очень мило с твоей стороны."
    vero "Даже если я тебе не верю."
    vero "Спасибо, {b}[firstname]{/b}."
    show vero f_sexy
    show player 10
    player_name "Пожалуйста."
    show player 5
    return

label veronica_dialogue_spoken_with_diane_lately:
    show player 10 at left
    show vero f_normal
    player_name "Ты разговаривала с {b}Дайаной{/b} в последнее время?"
    show player 5
    show vero f_normal_talk
    vero "Да, по телефону."
    vero "Я жажду узнать больше об этом побочном бизнесе, которым она занимается!"
    vero "Ты знаешь что-нибудь об этом?"
    show vero f_normal
    show player 10
    player_name "Нет."
    player_name "Ничего."
    show player 5
    show vero f_sexy_talk
    vero "О, да ладно!"
    vero "Мне можешь рассказать."
    show vero f_sexy
    show player 14
    player_name "Хе-хе, я действительно ничего об этом не знаю!"
    show player 10
    player_name "Прости."
    show player 5
    show vero f_rolleyes
    vero "{b}*вздыхая*{/b} Это не знание убивает меня!"
    show vero f_normal
    show player 10
    player_name "Я уверен, что {b}Диана{/b} расскажет вам все об этом достаточно скоро."
    show player 5
    show vero f_normal_talk
    vero "Надеюсь."
    show vero f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
