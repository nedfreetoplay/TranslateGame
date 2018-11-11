label jane_library_dialogue_bissette_find_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Я не могу найти {b}словарь французского{/b}."
    show player 5f
    show jane 2f
    jan "Хмм, секунду..."
    show jane 1b
    pause
    show jane 2b
    jan "Он должен быть на полке рядом с той дверью."
    show jane 1f
    show player 14f
    player_name "Окей, сейчас гляну. Спасибо."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Ну, я нашел только часть словаря."
    show player 503f
    show jane 4f
    jan "Что?"
    show player 5f
    show jane 17bf
    with dissolve
    jan "О нет!"
    jan "Я закажу новый, но доставка займет какое-то время."
    jan "Он тебе ещё будет нужен?"
    show jane 18bf
    show player 10f
    player_name "Да, очень нужен. Надеюсь, что сейчас я смогу обойтись тем, что есть..."
    show player 5f
    show jane 17bf
    jan "Ну окей, прости, если что!"
    show jane 18f
    jan "Можешь оставить его себе, вряд ли в таком состоянии он ещё кому-то пригодится..."
    show jane 1f with dissolve
    show player 504f with dissolve
    player_name "Спасибо!"
    show player 503f
    show jane 3f
    jan "Никаких проблем, удачного дня!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( Нужно отнести это к {b}Мисс Биссетт{/b} и узнать, что она думает... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "Я нашел все книги, которые не вернули в срок!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane 2f
    jan "Правда? Дай-ка посмотреть..."
    show player 13f
    show jane 22f at Position (xoffset=-18) with dissolve
    jan "Ты и правда сделал это! Большое спасибо!"
    jan "У меня тоже для тебя кое-что есть."
    show jane 21f at Position (xoffset=-18)
    show player 10f
    player_name "Да?"
    show jane 20f with dissolve
    jan "Прислали книгу, которую ты заказывал."
    show jane 19f with dissolve
    pause
    show player 521f
    show jane 1f
    with dissolve
    player_name "Спасибо!"
    player_name "{b}101 вид сыра{/b}..."
    show player 5f with dissolve
    show jane 2f
    jan "Это оно?"
    show jane 1f
    show player 10f
    player_name "Эм, да..."
    show player 14f
    player_name "Ещё раз спасибо!"
    show player 13f
    show jane 3f
    jan "Захаживай ещё!"
    return

label jane_library_dialogue_pre:
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Привет! Чем я могу тебе помочь?"
    show player 2f
    show jane 1f
    player_name "Привет, я ищу одну {b}книгу{/b}."
    show player 1f
    show jane 2f
    jan "Ты знаешь название книги?"
    show jane 1f
    return

label jane_library_dialogue_milk_production_books:
    show player 14f
    player_name "Это может прозвучать странно, но есть ли у вас в библиотеке что-нибудь про увеличение выработки молока?"
    show player 13f
    pause
    show jane 4f
    jan "Эм... Зачем? Не думаю, что ты сможешь кормить кого-нибудь грудью."
    show jane 2f
    jan "Ох! Упс! Ты, наверное, говоришь про фермерство?"
    show jane 1f
    show player 10f
    player_name "Эмм... Вообще-то, я хотел бы узнать про обе темы, наверное..."
    show player 13f
    show jane 4f
    jan "Проверь на той полке, у нас должно что-то быть."
    show jane 1f
    show player 14f
    player_name "Спасибо!"
    show player 13f
    show jane 2f
    jan "Всегда пожалуйста!"
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "У вас есть французская поэзия?"
    show player 5f
    show jane 1b
    jan "Хмм..."
    show jane 2f
    jan "Вообще-то..."
    jan "Какие-то девочки читали что-то подобное {b}вчера вечером{/b}."
    show jane 1f
    show player 10f
    player_name "Правда?"
    show player 12f
    player_name "Они записывались?"
    show player 5f
    show jane 2f
    jan "Нет."
    show jane 1f
    show player 10f
    player_name "Ты не знаешь, где они?"
    show player 5f
    show jane 5f
    jan "..."
    show jane 4f
    jan "Нет..."
    jan "Но, может быть, они будут здесь сегодня {b}вечером{/b}."
    jan "Можешь спросить у них, куда они положили книгу."
    show jane 1f
    show player 12f
    player_name "Спасибо."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "Есть ли у вас книги о еде на французском?"
    show player 13f
    show jane 3f
    jan "Интересный запрос..."
    show jane 1f
    show player 14f
    player_name "Да, мне просто нужно это для домашнего задания."
    show player 13f
    show jane 2f
    jan "Окей, сейчас я проверю."
    show jane 1b
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane 2b
    jan "Хмм, судя по всему, у нас нет ничего подобного."
    show jane 1f
    show player 12f
    player_name "Вообще?"
    show player 5f
    show jane 2b
    jan "Ага... Ох, одну секунду!"
    jan "Один из наших филиалов заказывал книгу о сыре на французском."
    show jane 2f
    jan "Подойдет?"
    show jane 1f
    show player 14f
    player_name "Конечно, я люблю сыр! Где я смогу взять её?"
    show player 13f
    show jane 2f
    jan "Я могу заказать её сюда, но это займет несколько дней..."
    jan "А пока она будет сюда ехать, можешь ли ты помочь мне с кое-чем?"
    show jane 1f
    show player 10f
    player_name "... Да, я думаю. Что тебе нужно?"
    show player 5f
    show jane 2f
    jan "{b}Некоторые твои одноклассники брали у меня книги{/b}, я бы хотела, чтобы они вернулись обратно."
    jan "Я отослала оповещения им домой, но это не помогло."
    jan "Очень не хотелось бы терять эти книги."
    show jane 1f
    show player 10f
    player_name "Ну, я мог бы {b}поговорить с ними{/b}. Как их зовут?"
    show player 5f
    show jane 2b
    jan "Хмм, первая - {b}Мисс Мартинес{/b}."
    jan "Второй - {b}Мр. Эрик Ж-{/b}."
    show jane 1f
    show player 14f
    player_name "{b}Эрик{/b} не вернул книгу?!"
    player_name "Ну, это будет просто."
    show player 13f
    show jane 2b
    jan "...И последний..."
    jan "Ха. Тут написано просто {b}Декстер{/b}."
    jan "Знаешь его?"
    show jane 1f
    show player 12f
    player_name "О боже, только не {b}Декстер{/b}... Ты уверена?"
    show player 11f
    show jane 2f
    jan "Ну, так написано..."
    show jane 1f
    show player 12f
    player_name "Чёрт! Ладно, посмотрю, что можно сделать."
    show player 5f
    show jane 3f
    jan "Спасибо, я правда ценю это!"
    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Ух, ну почему это должен быть {b}Декстер{/b}?"
    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "Ещё раз, как зовут тех учеников?"
    player_name "Ну знаешь, которые не вернули книги."
    show player 5f
    show jane 2f
    jan "Секунду..."
    show jane 2b
    jan "Хмм, {b}Мисс Мартинес{/b}, {b}Мр. Эрик{/b}, и {b}Декстер{/b}."
    show jane 1f
    show player 12f
    player_name "Эх, я забыл про {b}Декстера{/b}..."
    player_name "Ладно, посмотрю, что можно сделать."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "Я делаю коллаж для класса искусств, так что мне нужны некоторые старые журналы."
    player_name "Где я могу их найти?"
    show player 1f
    show jane 2f
    jan "Я боюсь, что тебе неповезло. Мы перестали их держать у себя несколько месяцев назад."
    show player 10f
    show jane 1f
    player_name "У вас нет вообще никаких?"
    show player 1f
    show jane 2f
    jan "Нет, мы отправили их все на переработку."
    show player 10f
    show jane 1f
    player_name "О черт..."
    player_name "Спасибо в любом случае."
    show player 11f
    show jane 2f
    jan "Извини."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "И что же мне делать?"
    show player 11
    player_name "..."
    show player 10
    player_name "Думаю, {b}нужно посмотреть в школе{/b}."
    player_name "Там должны быть какие-нибудь журналы."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "Так у вас нет ни одного журнала?"
    show player 11f
    show jane 2f
    jan "Неа."
    jan "Мы отменили подписки и избавились от тех, что были."
    show jane 1f
    show player 10f
    player_name "Окей, всё равно спасибо."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{b}*Вздох*{/b}"
    player_name "Думаю, {b}нужно посмотреть в школе{/b}."
    player_name "... Может мне повезет?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "Я хотел бы вернуть книгу."
    show player 13f
    show jane 3f
    jan "Отлично!"
    return

label jane_library_dialogue_return_books_first:
    show jane 2f
    jan "Не многие это делают."
    show jane 1f
    show player 10f
    player_name "Что тогда обычно происходит?"
    show player 5f
    show jane 8f
    jan "Я выслеживаю их, а потом ломаю им ноги, обычно, это помогает."
    show jane 12f
    show player 22f
    player_name "!!!"
    show jane 3f
    jan "Просто шутка!"
    show jane 1f
    show player 29f with dissolve
    player_name "Оу."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane 2f
    jan "Просто поставь их туда, я разберусь с этим позже."
    show jane 3f
    jan "Приходи ещё!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane 4f
    player_name "Извини, я вернусь, когда вспомню название книги."
    show player 5f
    show jane 2f
    jan "Окей, удачи тогда."
    return

label jane_library_dialogue_french_grammar_pre:
    scene librarydesk
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Привет! Чем я могу тебе помочь?"
    show player 2f
    show jane 1f
    player_name "Привет, я ищу одну книгу."
    show player 1f
    show jane 2f
    jan "Окей, как она называется?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1:
    show player 14f at right
    show jane 1f
    player_name "Мне нужна \"{b}Французская грамматика - том 1{/b}\""
    show player 1f
    show jane 4f
    jan "Ты сделал то, о чем я просила?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1_have_webcam:
    show player 12f
    player_name "Да... Вот {b}веб камера{/b}."
    show player 239_240f
    pause
    show player 54 at Position(xoffset=-38) with fastdissolve
    pause
    show player 1f with fastdissolve
    show jane 3f
    jan "Спасибо!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Что насчет {b}книги{/b}?"
    show player 11f
    show jane 3f
    jan "Ох! Точно..."
    show player 11f
    jan "Сегодня она пришла по раньше, я положила её на {b}полку{/b} вон туда."
    jan "Забирай её."
    show player 1f
    show jane 3f
    jan "До скорого!"
    return

label jane_library_dialogue_french_grammar_volume_1_do_not_have_webcam:
    show player 24f
    player_name "У меня её ещё нет..."
    show player 5f
    show jane 2f
    jan "Тогда я ещё не заказала тебе {b}книгу{/b}, ты же знаешь."
    jan "Приходи с {b}веб камерой{/b}, тогда и поговорим."
    return

label jane_library_dialogue_french_grammar_volume_2_first:
    show player 14f
    player_name "Мне нужна {b}Французская грамматика - том 2{/b}"
    show player 1f
    show jane 2f
    jan "Понимаешь..."
    jan "Я до сих пор не могу делать новые заказы."
    show player 12f
    show jane 1f
    player_name "До сих пор??"
    show player 5f
    show jane 4f
    jan "Я бы хотела сделать это для тебя... Но наше финансовое состояние всё ещё оставляет желать лучшего."
    show player 10f
    show jane 1f
    player_name "О чем ты? Разве новая {b}веб камера{/b} не должна была решить проблему?"
    show player 5f
    show jane 4f
    jan "Не пойми меня неправильно: она помогает..."
    jan "Но люди уже устали от одного и того же!"
    show player 10f
    show jane 1f
    player_name "Ну... И что мы можем с этим сделать?"
    show player 5f
    show jane 4f
    jan "Ну, нашим зрителям нужно разнообразие..."
    show player 11f
    show jane 3f
    jan "...и ты можешь с этим помочь!"
    show player 12f
    show jane 1f
    player_name "Но как?"
    show player 11f
    show jane 2f
    jan "Ты ведь ходишь в школу?"
    show player 12f
    show jane 1f
    player_name "Да."
    show player 11f
    show jane 3f
    jan "Тогда просто спрячь одну из моих {b}вебкамер{/b} с дистанционным управлением где-нибудь в школе!"
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Ты с ума сошла?!"
    player_name "А если меня поймают?!"
    show jane 3f
    show player 90f
    jan "Спокойно! Просто иди ночью, когда никого не будет."
    show player 37f
    show jane 1f
    player_name "Ух... Не могу поверить, что мне нужно это сделать..."
    show jane 2f
    jan "Тебе нужны эти книги?"
    show player 24f
    show jane 1f
    player_name "Ладно, я понял..."
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_pre:
    show player 14f
    player_name "Мне нужна {b}Французская грамматика - том 2{/b}"
    show player 1f
    show jane 4f
    jan "Ну? Ты сделал?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_placed_webcam:
    show player 12f
    player_name "Да, я установил её в {b}раздевалке{/b}..."
    player_name "Она в {b}вентеляции{/b}..."
    show player 1f
    show jane 3f
    jan "Спасибо!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Так что там с {b}книгой{/b}?!"
    show player 11f
    show jane 3f
    jan "Ох! Точно..."
    show player 11f
    show jane 15
    jan "Вот она!"
    $ player.get_item("textbook2")
    show player 30f
    show jane 1f
    player_name "Спасибо!"
    show player 1f
    show jane 3f
    jan "Ещё увидимся!"
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_havent_placed_webcam:
    show player 24f
    show jane 4f
    player_name "Я ещё не сделал это..."
    show player 5f
    show jane 2f
    jan "Я не могу заказать тебе эту {b}книгу{/b}, ты же знаешь."
    jan "Возвращайся, когда установишь {b}веб камеру{/b} в школе."
    return

label jane_library_dialogue_french_grammar_volume_3:
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
