label jane_library_dialogue_bissette_find_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Я не могу найти {b}словарь французского{/b}."
    show player 5f
    show jane f_normal_talk
    jan "Хмм, секунду..."
    show jane f_normal_down
    pause
    show jane f_normal_talk_down
    jan "Он должен быть на полке рядом с той дверью."
    show jane f_normal
    show player 14f
    player_name "Окей, сейчас гляну. Спасибо."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Ну, я нашел только часть словаря."
    show player 503f
    show jane f_sad_talk
    jan "Что?"
    show player 5f
    show jane f_complain_down a_dressed_book1
    with dissolve
    jan "О нет!"
    jan "Я закажу новый, но доставка займет какое-то время."
    show jane f_sad_talk
    jan "Он тебе ещё будет нужен?"
    show jane f_sad
    show player 10f
    player_name "Да, очень нужен. Надеюсь, что сейчас я смогу обойтись тем, что есть..."
    show player 5f
    show jane f_sad_talk
    jan "Ну окей, прости, если что!"
    show jane f_normal_talk
    jan "Можешь оставить его себе, вряд ли в таком состоянии он ещё кому-то пригодится..."
    show jane f_normal a_dressed_sides with dissolve
    show player 504f with dissolve
    player_name "Спасибо!"
    show player 503f
    show jane f_laugh
    jan "Никаких проблем, удачного дня!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( Нужно отнести это к {b}Мисс Биссетт{/b} и узнать, что она думает... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane f_normal at flip
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "Я нашел все книги, которые не вернули в срок!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane f_normal_talk
    jan "Правда? Дай-ка посмотреть..."
    show player 13f
    show jane f_normal_talk a_dressed_book3 with dissolve
    jan "Ты и правда сделал это! Большое спасибо!"
    jan "У меня тоже для тебя кое-что есть."
    show jane f_normal
    show player 10f
    player_name "Да?"
    show jane f_normal_talk a_dressed_book2 with dissolve
    jan "Прислали книгу, которую ты заказывал."
    show jane f_normal
    pause
    show player 521f
    show jane f_normal a_dressed_sides
    with dissolve
    player_name "Спасибо!"
    player_name "{b}101 вид сыра{/b}..."
    show player 5f with dissolve
    show jane f_normal_talk
    jan "Это оно?"
    show jane f_normal
    show player 10f
    player_name "Err, I'll have to make do."
    show player 14f
    player_name "Ещё раз спасибо!"
    show player 13f
    show jane f_laugh
    jan "Захаживай ещё!"
    return

label jane_library_dialogue_pre:
    show jane f_normal_talk at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Привет! Чем я могу тебе помочь?"
    show player 2f
    show jane f_normal
    player_name "Привет, я ищу одну {b}книгу{/b}."
    show player 1f
    show jane f_normal_talk
    jan "Ты знаешь название книги?"
    show jane f_normal
    return

label jane_library_dialogue_production_ask_librarian:
    scene librarydesk
    show jane f_normal at flip
    show jane at Position (xpos=100)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "У вас случайно нет книг по увеличению выработки молока?"
    show player 5f
    show jane f_sad_talk
    jan "... Эээ, это странный вопрос."
    show jane f_normal
    show player 29f with dissolve
    player_name "Эх, да. Наверное."
    player_name "Это для моего ... эээ..... Друга."
    show player 3f at Position (xoffset=-8)
    show jane f_laugh
    jan "Хех, конечно."
    show jane f_eyeroll_talk a_dressed_up with dissolve
    jan "Ммм, я не знаю."
    jan "Я уверен, что у нас есть что-то о коровах, но что касается доения..."
    show jane f_normal_talk
    jan "{b}Попробуй вон ту полку.{/b}"
    show jane f_normal a_dressed_sides
    show player 14f
    with dissolve
    player_name "Спасибо!"
    hide player with dissolve
    pause
    show jane f_sad_talk
    jan "Какой чудак..."
    hide jane
    with dissolve
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "У вас есть французская поэзия?"
    show player 5f
    show jane f_normal_down
    jan "Хмм..."
    show jane f_normal_talk
    jan "Вообще-то..."
    jan "Какие-то девочки читали что-то подобное {b}вчера вечером{/b}."
    show jane f_normal
    show player 10f
    player_name "Правда?"
    show player 12f
    player_name "Они записывались?"
    show player 5f
    show jane f_normal_talk
    jan "Нет."
    show jane f_normal
    show player 10f
    player_name "Ты не знаешь, где они?"
    show player 5f
    show jane f_normal_down
    jan "..."
    show jane f_sad_talk
    jan "Нет..."
    jan "Но, может быть, они будут здесь сегодня {b}вечером{/b}."
    jan "Можешь спросить у них, куда они положили книгу."
    show jane f_normal
    show player 12f
    player_name "Спасибо."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "Есть ли у вас книги о еде на французском?"
    show player 13f
    show jane f_laugh
    jan "Интересный запрос..."
    show jane f_normal
    show player 14f
    player_name "Да, мне просто нужно это для домашнего задания."
    show player 13f
    show jane f_normal_talk
    jan "Окей, сейчас я проверю."
    show jane f_normal_down
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane f_normal_talk_down
    jan "Хмм, судя по всему, у нас нет ничего подобного."
    show jane f_normal
    show player 12f
    player_name "Вообще?"
    show player 5f
    show jane f_normal_talk_down
    jan "Ага... Ох, одну секунду!"
    jan "Один из наших филиалов заказывал книгу о сыре на французском."
    show jane f_normal_talk
    jan "Подойдет?"
    show jane f_normal
    show player 14f
    player_name "Конечно, я люблю сыр! Где я смогу взять её?"
    show player 13f
    show jane f_normal_talk
    jan "Я могу заказать её сюда, но это займет несколько дней..."
    jan "А пока она будет сюда ехать, можешь ли ты помочь мне с кое-чем?"
    show jane f_normal
    show player 10f
    player_name "... Да, я думаю. Что тебе нужно?"
    show player 5f
    show jane f_normal_talk
    jan "{b}Некоторые твои одноклассники брали у меня книги{/b}, я бы хотела, чтобы они вернулись обратно."
    jan "Я отослала оповещения им домой, но это не помогло."
    jan "Очень не хотелось бы терять эти книги."
    show jane f_normal
    show player 10f
    player_name "Ну, я мог бы {b}поговорить с ними{/b}. Как их зовут?"
    show player 5f
    show jane f_normal_talk_down
    jan "Хмм, первая - {b}Мисс Мартинес{/b}."
    jan "Второй - {b}Мр. Эрик Ж-{/b}."
    show jane f_normal
    show player 14f
    player_name "{b}Эрик{/b} не вернул книгу?!"
    player_name "Ну, это будет просто."
    show player 13f
    show jane f_normal_talk_down
    jan "...И последний..."
    jan "Ха. Тут написано просто {b}Декстер{/b}."
    jan "Знаешь его?"
    show jane f_normal
    show player 12f
    player_name "О боже, только не {b}Декстер{/b}... Ты уверена?"
    show player 11f
    show jane f_normal_talk
    jan "Ну, так написано..."
    show jane f_normal
    show player 12f
    player_name "Чёрт! Ладно, посмотрю, что можно сделать."
    show player 5f
    show jane f_laugh
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
    show jane f_normal_talk
    jan "Секунду..."
    show jane f_normal_talk_down
    jan "Хмм, {b}Мисс Мартинес{/b}, {b}Мр. Эрик{/b}, и {b}Декстер{/b}."
    show jane f_normal
    show player 12f
    player_name "Эх, я забыл про {b}Декстера{/b}..."
    player_name "Ладно, посмотрю, что можно сделать."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "Я делаю коллаж для класса искусств, так что мне нужны некоторые старые журналы."
    player_name "Где я могу их найти?"
    show player 1f
    show jane f_normal_talk
    jan "Я боюсь, что тебе неповезло. Мы перестали их держать у себя несколько месяцев назад."
    show player 10f
    show jane f_normal
    player_name "У вас вообще никаких нет?"
    show player 1f
    show jane f_normal_talk
    jan "Нет, мы отправили их все на переработку."
    show player 10f
    show jane f_normal
    player_name "О черт..."
    player_name "Спасибо в любом случае."
    show player 11f
    show jane f_normal_talk
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
    show jane f_normal_talk
    jan "Неа."
    jan "Мы отменили подписки и избавились от тех, что были."
    show jane f_normal
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
    show jane f_laugh
    jan "Отлично!"
    return

label jane_library_dialogue_return_books_first:
    show jane f_normal_talk
    jan "Не многие это делают."
    show jane f_normal
    show player 10f
    player_name "Что тогда обычно происходит?"
    show player 5f
    show jane f_mad_talk
    jan "Я выслеживаю их, а потом ломаю им ноги, обычно, это помогает."
    show jane f_mad
    show player 22f
    player_name "!!!"
    show jane f_laugh
    jan "Просто шутка!"
    show jane f_normal
    show player 29f with dissolve
    player_name "Оу."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane f_normal_talk
    jan "Просто поставь их туда, я разберусь с этим позже."
    show jane f_laugh
    jan "Приходи ещё!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane f_sad_talk
    player_name "Извини, я вернусь, когда вспомню название книги."
    show player 5f
    show jane f_normal_talk
    jan "Окей, удачи тогда."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
