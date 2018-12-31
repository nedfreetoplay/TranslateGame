label button_ross_ask_model:
    scene location_school_art_closeup
    show ross 25 at left
    show player 1f at right
    ross "Есть успехи?"
    show player 2f
    show ross 24
    player_name "Пока нет."
    show player 1f
    show ross 25
    ross "Ну убедитесь что вы {b}спросили всех своих одноклассников{/b}."
    show ross 25b
    ross "Надеюсь, кто-то будет достаточно храбр, чтобы позировать для нас..."
    return

label button_ross_found_model:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show judith 1 zorder 2 at Position(xpos=0.65, ypos=1.0)
    show ross 10 zorder 2 at left
    with dissolve
    player_name "Я вернулся {b}Мисс Росс{/b} и я нашел нам модель!"
    show player 1f
    show ross 11
    ross "{b}*Вздох задыхаясь* Джудит{/b}!"
    show ross 27 with dissolve
    ross "Это идеально! У нее прекрасное тело для этого!"

    show ross 26
    show judith 4
    pause
    show judith 5
    jud "О, эмм, {b}Мисс Росс{/b} будет здесь тоже мм?"
    show player 10f
    show judith 1
    player_name "Да, ты ведь не против?"
    show player 11f
    show judith 3
    jud "Я не знаю..."
    show judith 6
    show ross 27
    ross "О, посмотри, как она покраснела, как восхитительно!"
    show ross 60 with dissolve
    ross "Вот, милая, возьми это и иди переоденься."

    ross "Мы подождем тебя прямо здесь ."
    show ross 59
    show judith 3
    jud "Эмм..."
    show ross 60
    show judith 6
    ross "Не теряй зря время, мы хотим как можно больше времени с тобой."

    hide judith
    show ross 11
    with dissolve
    ross "Отличная работа, {b}[firstname]{/b}! Она будет превосходной моделью!"
    show ross 10
    show player 1f
    pause
    show mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    pause
    show ross 11

    ross "...А вот и наш маленький пирожочек, как раз вовремя!"
    show ross 10
    show mia 12b
    mia "Да, я не смогла никого найти. Извините ребята..."
    show ross 11
    show mia 8b
    ross "О, не беспокойся! {b}[firstname]{/b} справился как и всегда."
    show ross 10
    show mia 10b
    mia "Серьезно? Ты на самом деле нашел добровольца?"
    show mia 9
    mia "Это потрясающе, {b}[firstname]{/b}!"
    show mia 11
    show player 2f
    player_name "... Да, {b}Джудит{/b} согласилась-"
    show judith 59f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show player 11f
    with dissolve
    pause
    show judith 44f
    show judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show mia 7
    pause
    show judith 45f
    jud "... Что {b}Мия{/b} здесь делает?!"
    show judith 44f
    show ross 11
    ross "Она тоже будет тебя рисовать, милая."
    show judith 45f
    show ross 10
    jud "Я передумала насчет всего этого..."
    show judith 52f
    jud "Я думала, что это будем только ты и я, {b}[firstname]{/b}!"
    show judith 51f
    show ross 25
    ross "Успокойся, {b}Джудит{/b}... все будет в порядке, дорогая."
    show ross 11
    ross "Тебе нечего стыдиться. Неправда ли ребята?"
    show ross 10
    show player 2f
    player_name "Вовсе нет."
    show player 1f
    show mia 10
    mia "Да, не переживай, {b}Джудит{/b}. {b}Мисс Росс{/b} научила нас, что тело каждого человека прекрасно."
    show mia 7
    show ross 11
    ross "Так и есть, {b}Мия{/b}. Все Все прекрасны по-своему."
    ross "Ты должны гордиться своим телом, {b}Джудит{/b}."
    show ross 10
    show judith 52f
    jud "Я не знаю..."
    show judith 51f
    show ross 58 with dissolve
    ross "У меня есть идея!"
    hide ross with dissolve
    pause
    show ross 40 zorder 2 at left with dissolve

    ross "Это всегда успокаивают меня, когда я волнуюсь...."
    ross "Все возьмите по одному."
    show ross 41
    show player 2f
    player_name "О, Я слышал, ты делаешь лучшие пирожные!"
    show player 1f
    show ross 40
    ross "Хехе, тебе лучше поверить в это!"
    ross "Это мой секретный рецепт..."
    show ross 44 with dissolve
    pause
    show ross 43 with dissolve
    ross "... 100%%, все натуральное."
    hide player
    show player 602 zorder 4 at right
    with dissolve
    show ross 42
    pause
    show player 599f with dissolve
    pause
    show player 600f
    show mia 73 zorder 3 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    pause
    hide judith
    hide judithr
    show mia 71
    show judith 60 zorder 5 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    pause
    hide judith
    show mia 71 at Position(xpos=0.65, ypos=1.0)
    show judith 47f zorder 0 at Position(xpos=0.35, ypos=1.0)
    show judithr 1f zorder 1 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show mia 72

    mia "Ням!! Они восхитительны!"
    show mia 71
    show judith 48f
    jud "Ном ном ном."
    show ross 43
    show judith 47f
    ross "Помедленней, {b}Джудит{/b}. Ты же не хочешь съесть их слишком быстро."
    show ross 42
    show judith 48f
    jud "О мой бог! Они так хороши!"
    show judith 49f
    jud "Ммм..."
    show mia 74f
    show player 26f
    player_name "Хех, у них есть своего рода... Земляной аромат."
    show player 13f
    show ross 13
    ross "Как все себя чувствуют?"
    show ross 12
    show player 26f
    player_name "Хооорошо. Очень хоооорошо."
    show player 13f
    show judith 50f
    jud "Я тоже."
    show judith 49f
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Хехехехехехехехехехехехе!"
    show judith 50f
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    jud "Этот халат очень чешется!"
    show judith 49f
    show ross 13
    ross "Ну, сейчас, когда ты чувствушь себя более расслабленной, почему бы тебе не снять его, милашка."
    ross "Мы сможем приступить к делу."
    show ross 12
    show judith 50f
    jud "Ммм да, хорошо..."
    hide judith
    hide judithr
    show judith 56f zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show judith 49f with dissolve
    pause
    show ross 13
    ross "Очень хорошо, Дорогая."
    show ross 11
    ross "Теперь, {b}[firstname]{/b} и {b}Мия{/b}, почему бы вам двоим не присесть и не найти ваши угли."
    show ross 10
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Хехехехеехехахаха!"
    mia "Все это так странно!!"
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 11
    ross "Да, наверняка, моя сладенькая."
    show ross 13
    ross "{b}Джудит{/b} тебе нужно снять нижнее белье тоже, милая."
    show ross 12
    show judith 51f
    jud "Хмм?"
    show judith 52f
    jud "Вы имеете в виду, что я должна показать..."
    jud "Мою..."
    jud "... Киску?"
    show judith 51f
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Пффффф!!! Ахахахаха! Это такое смешное слово!"
    mia "Кииииска! Хахахах!"
    show mia 74f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 11
    ross "Хех, Успокойся, {b}Мия{/b}!"
    show ross 25
    ross "Ты всё ещё чувствуешь себя стеснительно, {b}Джудит{/b}?"
    show ross 24
    jud "Мммхмм..."
    show ross 11
    ross "Чтож, а что если нам тоже раздеться?"
    show ross 10
    show judith 54f
    pause
    show judith 55f
    jud "... Да! Это хорошая идея!"
    show judith 54f
    show player 26f
    player_name "Ты хочешь, чтобы мы тоже обнажились?"
    show player 13f
    show ross 11
    ross "Мы просто разденемся до нашего нижнего белья.."
    ross "Это должно быть достаточно хорошо, верно {b}Джудит{/b}?"
    show ross 10
    show judith 55f
    jud "... Да! Я хочу посмотреть на нижнее белье {b}[firstname]{/b}!"
    show judith 54f
    show ross 11
    ross "Тогда очень хорошо..."
    hide ross
    show ross 14 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show ross 15 at Position(xpos=0.14, ypos=1.0) with dissolve
    pause
    show ross 16 at Position(xpos=0.13, ypos=1.0) with dissolve
    pause
    show ross 17 with dissolve
    pause
    show ross 36 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Давайте вы оба..."
    show ross 37
    show mia 75f with dissolve
    mia "... Подождите! Я?"
    show mia 74f
    show ross 36
    ross "Особенно ты, золотце!"
    show ross 37
    show mia 75bf at Position(xpos=0.63, ypos=1.0) with dissolve
    mia "Хехехехехехехе, Оки-доки!"
    show mia 76f at Position(xpos=0.62, ypos=1.0) with dissolve
    pause
    show mia 77f at Position(xpos=0.64, ypos=1.0) with dissolve
    pause
    show mia 78f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 79f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 80f at Position(xpos=0.66, ypos=1.0) with dissolve
    pause
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 36
    ross "Тебе не нужно было снимать свой лифчик, милый пирожок!"
    show mia 82f
    show ross 37
    mia "Что нет?"
    show mia 81f
    show ross 36
    ross "Хехе, нет я сказала, 'Снять только нижнее белье.'"
    show mia 82f
    show ross 37
    mia "Ооооо..."
    mia "Оки-доки!"
    show mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Это весело!"
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show ross 36
    ross "Да, это определенно, дорогая."
    ross "Мы ждем, {b}[firstname]{/b}."
    show ross 37
    show player 21f
    player_name "Д-да. Хорошо!"
    show player 8f with dissolve
    pause
    show player 265f with dissolve
    pause
    show judith 53f
    pause
    show player 267f
    player_name "( !!! )" with hpunch
    jud "... Вау!"
    show mia 82bf at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Выглядит немного злым! Пфффф, хахахаха!!!"
    show mia 81f at Position(xpos=0.65, ypos=1.0) with dissolve
    show judith 55f
    jud "Он такой большой..."
    show judith 54f
    show player 265bf
    show ross 36
    ross "Это точно, дорогая."
    ross "... Ты все еще должна снять эти трусики, прежде чем мы сможем нарисовать тебя."
    show ross 37
    show judith 55f
    jud "... И розовый."
    show judith 54f
    show ross 36
    ross "Вот, я помогу!"
    hide ross
    show judith 61f at Position(xpos=0.22, ypos=1.0) with dissolve
    pause
    show judith 62f with dissolve
    pause
    hide judith
    show judith 66f zorder 1 at Position(xpos=0.35, ypos=1.0)
    show ross 36 zorder 0 at left
    with dissolve
    ross "Вот так, хорошая девочка."
    ross "Сейчас, встаньна педистал для меня, хорошо?"
    show ross 37
    show judith 66f
    jud "..."
    show ross 36
    hide judith with dissolve

    ross "Вы двое начинайте рисовать."
    show ross 37
    show player 265cf
    player_name "Да, Мэм."


    scene location_school_art_cutscene08
    with fade
    show text "Я могу сказать что {b}Джудит{/b} по прежнему нервничала, так что {b}Мисс Росс{/b} помогла ей подняться на пьедестал." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Было очень смело от нее позировать на аудиторию." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Но она не совсем в поразительно-вдохновляющей позе там наверху." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show judith 65b zorder 1 at Position(xpos=0.5, ypos=1.0)
    show ross 37 zorder 0 at left
    with dissolve
    pause
    show ross 36
    ross "Милая? Тебе нужно немного расслабиться...."
    show ross 37
    show judith 66
    jud "Я не..."
    jud "В смысле, я..."
    hide ross
    show ross 36f zorder 0 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    show judith 65b
    ross "Шшшш."
    ross "Все в порядке, {b}Джудит{/b}."
    hide ross
    show judithross 2 zorder 0 at Position(xpos=0.685, ypos=1.0)
    with dissolve
    ross "Просто сделай глубокий вдох..."
    show judith 66
    pause
    show judith 65b
    ross "... Вот так."
    show judithross 1
    pause
    show judithross 2
    ross "Ты красивый ангел, {b}Джудит{/b}."
    show judithross 1
    show judith 66
    jud "... Я?"
    show judithross 2
    show judith 65b
    ross "О, да! Ты поразительная, сладкая!"
    show judithross 1
    pause
    hide judithross
    show judith 67 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    ross "Расправь свои крылья, {b}Джуди{/b}."
    ross "Пусть весь мир увидит,как ты летаешь!"
    show judith 68b
    show ross 36f at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "{b}*Вздох*{/b} Идеально!"
    show judith 69
    show ross 37f
    jud "... Вы думаете что я идеальна?"
    show judith 68
    show ross 36f
    ross "Естественно, милая!"
    ross "Только посмотри на это соблазнительное тело..."
    ross "Как кто-то может перед этим устоять?"
    show ross 37f
    pause
    show ross 36f
    ross "Сейчас, не двигайся пару секунд!"
    ross "Дай художникам шанс запечатлеть твою красоту!"
    show ross 37f
    show judith 69b
    jud "Х-хорошо..."

	
	
    scene location_school_art_cutscene07
    with fade
    show text "{b}Мисс Росс{/b} определенно сделала {b}Джудит{/b} более комфортно." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... И она дала мне идеальное вдохновение для моего рисунка!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Хотя было немного трудно сконцентрироваться на моей работе с {b}Мисс Росс{/b} находящейся за моей спиной..." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show judith 68 zorder 1 at Position(xpos=0.4, ypos=1.0)
    show ross 36f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Это очень хорошо, {b}[firstname]{/b} но я думаю что ты можешь сделать лучше."
    ross "Я не уверен, что вы по-настоящему захватил кривые её восхитительного тела."
    show ross 37f
    player_name "Что вы имеете в виду?"
    show ross 36f
    ross "Ну посмотри!"
    ross "Иногда тебе придется на самом деле потрогать руками свой обьект и почувствовать форму."
    ross "... И у {b}Джудит{/b} здесь такие прекрасные контуры!"
    hide ross
    show judith 70
    with dissolve
    pause
    show judith 71 with dissolve
    pause
    show judith 72 with dissolve
    pause
    show judith 72b
    jud "( !!! )" with hpunch
    jud "АААХХ!"
    show judith 72e
    ross "... Ну посмотри кто вышел поиграть!"
    show judith 72c_72d
    pause
    jud "Ммм..."
    show judith 72e
    ross "Как ты себя чувствуешь, милая?"
    show judith 72
    jud "Очень..."
    jud "Ахх, очень хорошо!"
    show judith 72e
    ross "Да, просто наслаждайся,родная."
    show judith 72c_72d
    jud "ННГГХХ!"
    pause
    show judith 72
    jud "Хаааах!"
    show judith 72e
    ross "Прекрасно!"
    show judith 72
    jud "О, Я НЕ МОГУ!"
    show judith 73 zorder 1 at Position(xpos=0.45, ypos=1.0)
    show ross 37f zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    jud "( !!! )" with hpunch
    jud "АААХХХ!"
    show judith 66
    jud "Хааах... Хааах..."
    show judith 65
    show ross 36f
    ross "Очень хорошо, милая!"

    show judith 58f zorder 0 at left
    show ross 37f
    with dissolve
    jud "Это было..."
    show judith 57f
    jud "..."
    show judith 58f
    jud "... Мы можем это повторить?"
    show judith 57f
    show ross 36f
    ross "... Возможно позже, сладкая."
    show ross 36 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    ross "Теперь ты понимаешь,что я имела в виду о чувствах формы, {b}[firstname]{/b}?"
    show ross 37
    player_name "Я не уверен..."
    show mia 82 zorder 1 at Position(xpos=0.35, ypos=1.0) with dissolve

    mia "Я думаю что я поняла, {b}Мисс Росс{/b}!"
    show mia 81
    show ross 36f with dissolve
    ross "Хорошо, тогда ты можешь помочь мне показать ему."
    show ross 36 with dissolve
    ross "Поднимайся сюда и присоединяйся к нам, {b}[firstname]{/b}!"
    show ross 37
    player_name "Серьезно?"
    show ross 36
    ross "Да, это то, что каждый хороший художник должен понять."
    hide mia
    hide ross
    show rossg 3 at Position(xpos=0.60, ypos=1.0)
    with dissolve
    player_name "Х-хорошо."
    show rossg 1
    ross "Сейчас, давайте."
    show rossg 2
    ross "Вы оба..."
    show rossg 1
    ross "... Почувствуйте формы."
    show rossg 4
    mia "Хехехе, хорошо!"
    show rossg 5_6 with dissolve
    pause
    show rossg 3 with dissolve
    player_name "... Вот так?"
    show rossg 1
    ross "Ммммхмм... Прямо вот так..."
    show rossg 4
    mia "Хехехее, Я надеюсь что бог не смотрит..."
    show rossg 2
    ross "Вы оба хорошо работаете."
    show rossg 1
    ross "Продолжаем."
    show rossg 5_6 with dissolve
    pause
    ross "Ммм..."
    pause
    show rossg 1 with dissolve
    ross "Очень хорошо, {b}[firstname]{/b}!"
    show rossg 2
    ross "Теперь попробуем почувствовать, формы {b}Мии{/b}."
    show rossg 3
    player_name "Я эмм..."
    show rossg 4
    mia "Все нормально!"
    mia "Почувствуй формы, {b}[firstname]{/b}!"
    show rossg 7_8 at Position(xpos=0.59, ypos=1.0) with dissolve
    pause
    show rossg 4 at Position(xpos=0.6, ypos=1.0) with dissolve
    mia "Туууу-Туууу!"
    show rossg 9 with dissolve
    mia "Пффф, хахахахаха!!!!"
    show rossg 2 with dissolve
    ross "О, разве она не самая очаровательная на свете?!"
    ross "Отлично, теперь Почувствуйте мои снова..."
    show rossg 5_6 with dissolve
    pause
    show judith 58f
    jud "... Вы, ребята, можете почувствовать мои формы, если захотите."
    show judith 57f
    show rossg 2 with dissolve
    ross "Что ж, бог мой! посмотрите кто наконец-то вылез из своей скорлупы!"
    ross "Мы вернемся к тебе через секунду, сладкая. Почему бы тебе не пойти и проверить шкаф запасов для меня..."
    ross "Там должны быть некоторые благовония и свечи, для создание нам нужного настроения."
    show judith 58f
    show rossg 5_6 with dissolve
    jud "...    Да, Мэм."
    hide judith
    with dissolve
    pause
    show rossg 10 with dissolve
    smi "ДА ЧТО В КОНЦЕ КОНЦОВ ТУТ У ВАС ПРОИСХОДИТ!?" with hpunch
    smi "ПОЧЕМУ ВЫ ВСЕ ГОЛЫЕ?!"
    hide rossg
    show mia 83 zorder 2 at left
    show ross 39 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show player 100 zorder 0 at Position(xpos=0.35, ypos=1.0)
    show principal 3 at right
    with dissolve
    ross "{b}Директриса Смит{/b}! Я просто обучала студентов некоторым техникам искусства..."
    show ross 38
    show principal 38
    smi "ТЕХНИКИ ИСКУССТВА?!?! Я ПОХОЖА НА ИДИОТКУ ПО ВАШЕМУ?!"
    show ross 39
    show principal 3
    ross "Конечно, мы просто-"
    show principal 28
    show ross 38
    smi "Я ДОЛЖНА ТЕБЕ НАПОМНИТЬ ЧТО ЭТО ШКОЛА А НЕ БОРДЕЛЬ!"
    show ross 39
    show principal 3
    ross "Ты ведешь себя нелепо, Я просто пытаюсь помочь им улучшить свое искусство."
    hide principal
    show principal 34 zorder 3 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    show ross 38
    smi "ПРОСТО НАДЕНЬТЕ КАКУЮ-НИБУДЬ ОДЕЖДУ, ВСЕ ВЫ!" with hpunch

    hide mia
    hide player
    show principal 29 at right
    show ross 17 at Position(xpos=0.25, ypos=1.0)
    with dissolve
    pause
    show ross 16 at Position(xpos=0.25, ypos=1.0) with dissolve
    pause
    show ross 15 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show ross 14 at Position(xpos=0.26, ypos=1.0) with dissolve
    pause
    show ross 24 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show mia 41 zorder 2 at left
    show player 8 zorder 0 at Position(xpos=0.35, ypos=1.0)
    with dissolve
    show principal 27
    smi "Тебе лучше иметь чертовски хорошее объяснение этому, {b}Барбара{/b}!"
    show mia 45
    show player 11 at Position(xpos=0.38, ypos=1.0)
    with dissolve
    show ross 25
    show principal 29
    ross "{b}Мия{/b} и я помогали {b}[firstname]{/b} здесь с практикой."
    ross "Пытались подготовить его к-"
    show ross 24
    ross "..."
    show principal 27
    smi "Подготовить его к чему?!"
    show principal 29
    show mia 46
    mia "Этому ар-"
    show mia 45
    show ross 25
    ross "К подарку!"
    ross "... Он собирался что-то нарисовать для вас, {b}директриса Смит{/b}!"
    show ross 24
    pause
    show ross 25
    ross "Подарок,чтобы повесить в твоем кабинете!"
    show ross 24
    show principal 27
    smi "Подарок?! Для меня?! Что-то вроде портрета?"
    show principal 29
    show ross 25
    ross "Да, точно! Если это то что ты хочешь..."
    show principal 27
    show ross 24
    smi "Он так хорош?"
    show ross 25
    show principal 29
    ross "Очень хорош, иди посмотри на себя!"
    show principal 41 with dissolve
    pause
    show principal 42
    smi "Что это за чертовщина?"
    show principal 41
    show mia 46
    mia "О, это эмм... Это моё, Мэм."
    mia "... Я не очень хороша."
    show mia 45
    smi "..."
    show principal 42
    smi "Тогда почему ты здесь, после школы, берешь часные уроки?"
    show principal 41
    show ross 25
    ross "Мои занятия не только для талантливых художников."
    ross "Они открыты для всех, у кого есть желание выразить себя через искусство."
    ross "... И {b}Мия{/b} здесь есть большая любовь к искусств."
    show ross 24
    show principal 42
    smi "Эм ммм..."
    smi "На самом деле, вы только что нашла для себя милый маленький пакет, не так ли?"
    show principal 41
    show ross 25b
    ross "Это нет..."
    show ross 24
    show principal 42
    smi "... И теперь ты просто работаешь, чтобы раскрыть его, мм?"
    smi "Хочешь попробовать на вкус?"
    smi "... Я хорошо знаю твои методы {b}Барбара{/b}."
    hide principal
    show principal 43 at Position(xpos=0.7, ypos=1.0)
    with dissolve
    pause
    show principal 44 at Position(xpos=0.72, ypos=1.0) with dissolve
    smi "Хмм."
    show principal 45
    smi "Мальчик это нарисовал?"
    show principal 44
    show player 10
    player_name "Да, Мэм."
    show player 11
    show principal 45
    smi "Чтож, наверное, я ошибалась насчет тебя, {b}[firstname]{/b}."
    smi "Ты на самом деле в чем-то хорош, в конце концов..."
    show principal 44
    show ross 11
    ross "Он очень талантлив, разве нет?"
    show ross 24
    hide principal
    show principal 27 at right
    with dissolve
    smi "О, заткнись!"
    smi "Я должна тебя уволить, прямо здесь и сейчас!"
    smi "Здесь, облапывая голых учеников..."
    hide principal
    show principal 35b at Position(xpos=0.83, ypos=1.0)
    with dissolve
    smi "..."
    show principal 35c
    smi "Хотя это впечатляющая работа."
    show principal 35
    smi "Хммм..."
    hide principal
    show principal 27 at right
    with dissolve
    smi "Я такая щедрая поэтому я {b}-МОГЛА БЫ-{/b} замять этот инцидент!"
    show ross 25
    show principal 26
    ross "Это было бы замечательно-"
    show ross 24
    show principal 27
    smi "... Но только если твой ученик сможет воссоздать мой портрет в таком же качестве!"
    show principal 26
    show ross 25
    ross "О, это не должно быть проблемой. Правда, {b}[firstname]{/b}?"
    show ross 24
    show player 10
    player_name "Эммм..."
    show player 11
    show principal 27
    smi "И он должен быть сделан по моим точным указаниями!"
    smi "Без всяких глупостей!"
    show principal 29
    show ross 25
    ross "О, безусловно! Всё что вы захотите, Мэм."
    show principal 27
    show ross 24
    smi "Чертовски верно, все что я захочу!"
    show principal 27
    smi "Теперь вы, детки, тащите свои задницы домой, пока я не передумала и не исключила вас обоих!"
    show principal 29
    show ross 25
    ross "Давайте вы двое. Увидимся завтра."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
