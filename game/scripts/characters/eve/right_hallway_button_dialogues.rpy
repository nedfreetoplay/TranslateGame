label button_eve_intro:
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 13 at left
    show eve 1 at right
    with dissolve
    return

label button_eve_talent_show_help:
    show player 10
    player_name "Ты играешь на каких-нибудь инструментах?"
    show player 5
    show eve 2
    eve "Нет, я не играю. Я всегда хотела учиться, но у меня просто не было времени, понимаешь?"
    show eve 1
    show player 10
    player_name "Хорошо, а как насчет пения?"
    show player 5
    show eve 6
    eve "Ох, ммм..."
    show eve 2b
    eve "Да, мне нравится петь, наверное. Не знаю, насколько я хорошо это делаю."
    show eve 1
    show player 14
    player_name "Я уверен в тебе! Ты должна участвовать в шоу талантов вместе со мной!"
    player_name "Нам действительно не хватает добровольцев."
    show player 13
    show eve 2b
    eve "... Да, я не знаю."
    eve "Ты хочешь, чтобы я пела перед всей школой? Звучит довольно неловко."
    eve "... И я давно не пела. С тех пор, как сломалась моя караоке-машина."
    eve "Я даво не практиковалась."
    show eve 1
    show player 4 with dissolve
    player_name "Хмм..."
    show player 14 with dissolve
    player_name "Знаешь, у моего друга {b}Erik{/b} была {b}караоке-машина{/b} в подвале."
    show player 13
    show eve 2
    eve "Ох, да?"
    show eve 1
    show player 17
    player_name "Точно! Приходи как-нибудь и потренируйся!"
    show player 13
    show eve 6
    eve "Ха, ты хочешь, чтобы я спела для тебя и твоего друга?"
    show eve 5
    show player 14
    player_name "Нет, мы можем петь все вместе! Давай, сделаем это сегодня вечером, будет весело!"
    show player 13
    show eve 1
    eve "..."
    show eve 6b
    eve "Ладно, думаю, я могу зайти ненадолго."
    show eve 5
    show player 14
    player_name "Потрясающе! {b}Встретимся у Эрика в доме{/b} сегодня ночью."
    return

label button_eve_ross_find_art_pad:
    show player 2
    player_name "Мне нужна услуга."
    show player 1
    show eve 2
    eve "А?"
    show player 2
    show eve 1
    player_name "Видишь ли, я помогаю {b}Miss Ross{/b} в одном деле и мне нужен твой блокнот."
    show player 1
    show eve 2
    eve "Ну, это не проблема."
    eve "Сначала ты {b}должен помочь мне найти мой рюкзак{/b}."
    show player 10
    show eve 1
    player_name "Ты потеряла свой рюкзак?"
    show player 11
    show eve 2
    eve "Да..."
    eve "Блокнот должен быть в нем."
    show player 10
    show eve 1
    player_name "Где он был в последний раз?"
    show player 11
    show eve 2
    eve "Хм, ну, я думаю, что он был у меня, когда {b}я пошла тусоваться с парнями в парке прошлой ночью{/b}."
    show player 2
    show eve 1
    player_name "Хорошо, я понял!"
    return

label button_eve_ross_find_eve_backpack_have_backpack:
    show player 610
    player_name "Смотри что я нашел!"
    show player 609
    show eve 2
    eve "Клееево!"
    show player 1 with dissolve
    eve "Спасибо, {b}[firstname]{/b}!"
    show player 2
    show eve 1
    player_name "Не беспокоиться. Я не смог найти твой {b}блокнот{/b}."
    show player 1
    show eve 2
    eve "Его не было в рюкзаке?"
    show player 2
    show eve 1
    player_name "Нет."
    show player 1
    show eve 2
    eve "Блин."
    show eve 6b
    eve "Возможно {b}Chad{/b} стащил его опять."
    show player 10
    show eve 1
    player_name "Chad?"
    show player 11
    show eve 2
    eve "Да, ему нравятся мои рисунки."
    show player 10
    show eve 1
    player_name "Интересно..."
    show player 2
    player_name "Надо пойти и спросить у него."
    show player 1
    show eve 2
    eve "Отлично. До встречи, {b}[firstname]{/b}."
    show player 2
    show eve 1
    player_name "До встречи, {b}Eve{/b}."
    return

label button_eve_ross_find_eve_backpack_no_backpack:
    show player 2
    player_name "Еще раз, где ты оставила свой рюкзак?"
    show player 1
    show eve 2
    eve "Я не совсем уверена. Я помню, что он был со мной в парке прошлой ночью."
    show player 2
    show eve 1
    player_name "Хорошо, я проверю!"
    return

label button_eve_ross_get_eve_drawing:
    show player 10
    player_name "Еще раз, у кого может быть твой {b}Блокнот{/b}?"
    show player 11
    show eve 6b
    eve "А, возможно он у {b}Chad{/b}."
    show eve 2
    eve "Он балдеет от моих рисунков."
    show player 2
    show eve 1
    player_name "Понял, спасибо!"
    return

label button_eve_ask_model:
    show player 2
    show eve 1
    player_name "Я работаю над пректом для {b}Miss Ross{/b} и нам нужна живая модель."
    player_name "Тебе это интересно?"
    show player 1
    show eve 2
    eve "Моделью? Это может быть весело."
    show player 2
    show eve 1
    player_name "Правда!? Потрясающе! Я надеялся, что ты это скажешь!"
    show player 1
    show eve 2
    eve "Да, я не возражаю. Хорошо, что я сегодня надела этот милый наряд."
    show player 10
    show eve 1
    player_name "... Ох, ммм. Это будет обнаженная модель."
    show player 11
    show eve 2b
    eve "Обнаженная?!"
    show eve 6
    eve "О, нет!"
    show player 10
    show eve 5
    player_name "Так ты не будешь? Я думал, ты увлекаешься искусством?"
    show player 11
    show eve 6
    eve "Да, но это не значит, что мне нравится публичная нагота!"
    show player 10
    show eve 5
    player_name "Хорошо. Прости."
    show player 11
    show eve 2
    eve "Все в порядке. Просто не интересно."
    show player 2
    show eve 1
    player_name "Ну, спасибо все равно..."
    return

label button_eve_ross_get_paint:
    show player 2
    show eve 1
    player_name "Мне нужно немного краски. Есть идеи, где я могу их найти?"
    show player 1
    show eve 6b
    eve "Не знаю, может в магазине?"
    show player 2
    show eve 1
    player_name "Ну да, конечно, я знаю... Да, точно?"
    player_name "... Но эта краска для {b}Miss Ross{/b} и она не может позволить себе купить ее."
    show player 1
    show eve 6
    eve "О, хехе."
    show eve 4 with dissolve
    eve "Хмм, бесплатная краска. Это сложно."
    show eve 3
    show player 2
    player_name "Расскажи мне..."
    show player 1
    show eve 2 with dissolve
    eve "Мы должны спросить {b}мою сестру{/b}."
    show player 2
    show eve 5
    player_name "Она {b}Тату мастер{/b}, правильно?"
    show player 1
    show eve 6
    eve "Она лучший {b}Тату мастер{/b}!"
    eve "Ты должен сходить и посмотреть на ее работы, они прикольные!"
    show player 2
    show eve 5
    player_name "Думаешь, она разрешит мне взять немного краски?"
    show player 1
    show eve 2
    eve "Спроси ее."
    show eve 5
    show player 10
    player_name "Не ее ли салон называется {b}Sugar Tats{/b}?"
    show player 11
    show eve 6
    eve "Ага. Он находится на {b}Севере{/b} города."
    show player 2
    show eve 5
    player_name "Хорошо, встретимся там!"
    return

label button_eve_ross_get_paint_grace:
    show player 10
    show eve 5
    player_name "Еще раз, как называется салон твоей сестры?"
    show player 11
    show eve 2
    eve "{b}Sugar Tats{/b}. Он находится на {b}Севере{/b} города."
    show player 2
    show eve 5
    player_name "Хорошо, {b}встретимся там{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
