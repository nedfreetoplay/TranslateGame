label button_ross_grab_clay:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "Иди возьми плитку глины, {b}[firstname]{/b}, чтобы мы могли начать."
    show player 2f
    show ross 1
    player_name "Да, Мэм."

    return

label button_ross_find_partner:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    with dissolve
    player_name "Здравствуйте, {b}Мисс Росс{/b}. Вы готовы начать?"
    show player 1f
    show ross 2
    ross "Привет, {b}[firstname]{/b}! Почти..."
    show ross 11 with dissolve
    ross "Сначала я хотела с тобой кое-что обсудить."
    show player 2f
    show ross 10
    player_name "Оу?"
    show ross 11
    show player 1f
    ross "Я думаю,мы должны найти тебе партнера для этих занятий,что ты думаешь?"
    show ross 10
    show player 10f
    player_name "Партнера?"
    show ross 11
    show player 11f
    ross "Да, кто-то кто будет работать поралельно с тобой и подкидывал тебе идеи вперед!"
    show ross 10
    show player 2f
    player_name "Конечно, Хорошо."
    player_name "У тебя есть кто-нибудь на примете?"
    show player 1f
    show ross 10b with dissolve
    ross "Хмм..."
    show ross 11 with dissolve
    ross "Ну, моя первоначальная мысль {b}Ева{/b}. Она талантливая художница, как и вы..."
    ross "... Но я сомневаюсь, что у нее будет время со всеми ее музыкальными обучениями."
    show ross 10b with dissolve
    pause
    show ross 11 with dissolve
    ross "Ты думаешь {b}Мии{/b} было бы интересно?"
    ross "Она просто такая милашка, не так ли!?"
    show ross 10
    show player 2f
    player_name "Ээээ, да. Наверно."
    show player 1f
    show ross 11
    ross "Отлично! Почему бы тебе не пойти поговорить с ней?"
    ross "Скажи её что я сказала чтобы она притащила свою миленькую задницу сюда!"
    show player 11f
    show ross 10
    player_name "..."

    return

label button_ross_ask_mia_partner:
    scene location_school_art_closeup
    show player 1f at right
    show ross 2 at left
    with dissolve
    ross "{b}[firstname]{/b}, ты вернулся!"
    ross "Где {b}Мия{/b}?"
    show player 10f
    show ross 1
    player_name "Ох, эмм... я еще не убедил её."
    show player 11f
    show ross 2
    ross "Ну чтож поторопись, {b}[firstname]{/b}!"
    ross "Нам нужен ее энтузиазм, если мы собираемся выиграть эту вещь!"
    return

label button_ross_mia_is_partner:
    scene location_school_art_closeup
    show player 1f zorder 1 at right
    show ross 2 at left
    show mia 7 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    ross "Привет, милашка!"
    show ross 1
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "... О, эммм. П-привет."
    show ross 2
    show mia 55
    ross "Я так рада что, {b}[firstname]{/b} убедил тебя присоединиться к нас!"
    show ross 1
    show mia 56
    mia "Хехе, да... Он сказал, что вам ребята очень нужна моя помощь?"
    show ross 2
    show mia 55
    ross "Нам разумеется!"
    show ross 1
    show player 2f
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    player_name "Итак, сейчас мы готовы начать?"
    show player 1f
    show ross 11 with dissolve
    ross "Ага! Почему бы вам обоим не достать свои художественные альбомы и не сесть напротив друг друга."
    show player 2f
    show ross 10
    player_name "Хорошо."
    show mia 8
    show player 596f with dissolve
    mia "..."
    show mia 12
    mia "Эмм, вопрос..."
    show mia 8
    show ross 11
    ross "Да, дорогая?"
    show mia 12
    show ross 10
    mia "Что если у меня нет художественного альбома?"
    show mia 8
    show ross 25
    ross "Ох, правильно."
    show ross 25b
    ross "Ну, обычно я бы предоставила тебе один из этих..."
    show ross 25
    ross "... Но я боюсь,что мы исчерпали запасы.."
    show ross 24
    show player 598f
    player_name "Это хреново!"
    show player 596f
    show mia 12b
    mia "О, ну, ничего страшного. Я не очень хорошо рисую в любом случае..."
    show mia 10
    mia "Я просто посмотрю."
    show mia 7
    show ross 11
    ross "Глупости!"
    ross "Мы достанем тебе один!"
    show ross 27 with dissolve
    ross "{b}[firstname]{/b}, почему бы тебе не спросить {b}Еву{/b} если мы можем одолжить у неё один."
    show ross 26
    show player 598f
    player_name "... Д-да, хорошо!"
    show ross 27
    show player 596f
    ross "Увидишь, {b}[firstname]{/b} поможет!"
    show player 1f
    show ross 11
    with dissolve
    ross "Мы просто останемся здесь и поговорим о женском."
    show ross 13
    ross "Правильно, милашка?"
    show ross 12
    show mia 56 at Position(xpos=0.635, ypos=1.0) with dissolve
    mia "Хех, хорошо..."
    show mia 55
    show player 2f
    player_name "Скоро вернусь."
    return

label button_ross_find_art_pad:
    scene location_school_art_closeup
    show ross 13 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 1f at right
    with dissolve
    ross "... Ты знаешь, {b}Мию{/b}. Я дружила с девушкой, которая была похожа на тебя!"
    show ross 12
    show mia 56
    mia "Реально?"
    show ross 13
    show mia 55
    ross "Абсолютно! Ей звали Старчайлд и мы следили за нашей любимой группой по всей стране."
    show ross 12
    show mia 12b at Position(xpos=0.45, ypos=1.0) with dissolve
    mia "Ну это звучит очень здорово!"
    show ross 13
    show mia 8b
    ross "О, именно!"
    ross "У этой девушки были всегда лучшие наркотики!"
    show ross 11
    ross "... И как целуется! Она могла делать своим языком такие вещи, которые-"
    show player 10f
    show ross 10
    show mia 55 at Position(xpos=0.435, ypos=1.0) with dissolve
    player_name "*Кхм* Я вам не помешал?"
    show player 11f
    show mia 12f with dissolve
    mia "{b}[firstname]{/b}, ты вернулся!"
    show mia 12bf
    mia "Слава богу!"
    show mia 8bf
    show ross 11
    ross "Тебе удалось взять {b}Евин альбом{/b}?"
    show player 10f
    show ross 10
    player_name "Нет, извините. Я все еще работаю над этим."
    show player 11f
    show ross 11
    ross "Тсс, ну брысь тогда! У нас девчачьи разговоры..."
    show ross 10
    show player 10f
    player_name "... Х-хорошо. Я скоро вернусь."
    hide player with dissolve
    show mia 12f at Position(xpos=0.55, ypos=1.0) with dissolve

    mia "Нет! Подожди! Погоди!"
    show mia 8f
    pause
    show ross 13 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Сейчас на чем я остановилась?"
    show ross 12
    show mia 8b with dissolve
    mia "..."
    show ross 13
    ross "Да,точно! Она могла делать ее языком такое, что заставило бы шлюху покраснеть!"
    show ross 12
    show mia 56 a Position (xpos=0.535, ypos=1.0) with dissolve
    mia "... О боже."
    return

label button_ross_found_art_pad:
    scene location_school_art_closeup
    show ross 46 at left
    show mia 55 at Position(xpos=0.435, ypos=1.0)
    show player 11f zorder 1 at right
    with dissolve
    ross "... Хмм, Я думаю, что мой любимый в {b}Прая-ду-Абрико{/b}"
    show ross 11 with dissolve
    ross "Он вернулся домой в Рио-де-Жанейро."
    show ross 10
    show mia 56
    mia "О, я не знаю..."
    mia "... Я не думаю, что я достаточно храбрая для для нудистского пляжа."
    show ross 13
    show mia 55
    ross "О, уверена что готова, милашка!"
    ross "Никто не должен стыдиться своего тела. Человеческая тело-это ведь произведение искусства..."
    show ross 13
    ross "... Особенно твое."
    ross "Ты совершенно прекрасна, {b}Мия{/b}!"
    show ross 12
    show mia 56
    mia "Вау, я... эмм..."
    show player 10f

    player_name "{b}*Кхм*{/b}"
    show player 11f
    show mia 12bf with dissolve
    mia "О, {b}[firstname]{/b}, слава богу ты вернулся!"
    show mia 8b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    show player 2f
    player_name "Вам ребята было весело?"
    show player 1f
    show ross 11
    ross "Мы оторвались!"
    ross "Я думаю что ты получил {b}художественный альбом{/b}?"
    show ross 10
    show player 598f with dissolve
    player_name "Ага, Я взял его вот он здесь."
    show player 596f
    show ross 11 with dissolve
    ross "Хорошая работа, {b}[firstname]{/b}!"
    ross "Итак мы должны начать."
    ross "Я хочу, чтобы вы оба сели друг напротив друга."
    show ross 58 with dissolve
    ross "... Потому что сегодня вы будете рисовать портреты друг друга используя карандаш и бумагу."
    show player 598f
    show ross 10 with dissolve
    player_name "Значит вы хотите что бы я нарисовал {b}Mia{/b}?"
    show player 596f
    show ross 11
    ross "Вот именно и {b}Mia{/b}, Я хочу чтобы ты нарисовала {b}[firstname]{/b}."
    show ross 10
    show mia 12b
    mia "Я попробую..."
    show ross 13
    show mia 8b
    ross "Ты слишком восхитительна,не правда ли?"
    show ross 12
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    ross "Не волнуйся, нет такого понятия, как плохое искусство!"
    show mia 56
    mia "... Если вы так говорите."
    show mia 55
    show ross 11
    ross "Итак,давайте начинать."


    scene location_school_art_cutscene06
    with fade
    show text "Мне всегда нравилось искусство, но рисование живой модели было совершенно другим опытом..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Я рад что {b}Miss Ross{/b} выбрала {b}Mia{/b} как моего напарника для этого." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Она на самом деле милашка!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 1 zorder 1 at left
    show mia 8b at right
    show ross 11f zorder 0 at Position(xpos=0.535, ypos=1.0)
    with dissolve
    ross "Вы оба, отлично поработали!"
    ross "Это такой красивый рисунок, {b}[firstname]{/b}!"

    show ross 28f at Position(xpos=0.435, ypos=1.0) with dissolve
    ross "Я чувствую что у нас хорошие шансы в этом конкурсе..."
    ross "Ты должна показать {b}Mia{/b}."
    show ross 12 at Position(xpos=0.35, ypos=1.0)
    show player 560
    with dissolve

    pause
    show mia 69
    mia "*В ужасе*"
    show mia 10
    mia "Вау Это так здорово!"
    show mia 7
    show ross 11
    ross "Разве нет!?"
    show ross 13
    ross "Это почти так же красиво, как и в реальной жизни!"
    show ross 13c
    ross "Ты не думаешь, {b}[firstname]{/b}?"
    show player 561
    show ross 12b
    player_name "Д-да, практически..."

    show player 560
    show ross 12
    show mia 56 with dissolve
    mia "Ой, спасибо {b}[firstname]{/b}."
    show mia 55
    show ross 13
    ross "Ладно,тогда, давай посмотрим, как ты это справилась {b}Mia{/b}?"
    show mia 59b with dissolve
    mia "Mмм, нет.Все в порядке.Я бы не хотела."
    show ross 11
    show mia 59d
    ross "О,Чепуха!Только не строй из себя недотрогу!"
    ross "Запомни, нет такого понятия, как плохое искусство..."
    show ross 10
    show mia 59e
    mia "... Хорошо."
    show mia 59c
    show ross 24

    ross "..."
    show mia 59
    mia "Я говорила вас, Я не очень хороша..."
    show mia 59c
    show ross 25
    ross "Ну нет, это -- интересно..."
    show ross 11
    ross "Есть определенно простор для совершенствования."
    show player 561
    show ross 10
    player_name "Мне это нравится, {b}Mia{/b}!"
    show player 560
    show mia 57
    mia "Тебе?"
    show player 561
    show mia 58
    player_name "Да, это правда мило!"

    show player 560
    show ross 11
    ross "Теперь смотри, {b}Mia{/b}. {b}[firstname]{/b} это нравится!"
    show ross 10
    mia "..."
    show ross 11
    ross "Чтож, я думаю что нам лучше назвать его на сегоднешний день."
    ross "Мы с вами добились очень хорошего прогресса!"
    show ross 58 at Position(xpos=0.41, ypos=1.0) with dissolve
    ross "Убедитесь,что бы вы оба много отдыхали и не забывайте делать те медитации, которым я вас учила!"
    show ross 10 at Position(xpos=0.35, ypos=1.0) with dissolve
    show player 2
    with dissolve
    player_name "Ладно,я постараюсь, {b}Мисс Ross{/b}."
    player_name "Увидимся, {b}Mia{/b}!"
    show player 1
    show mia 56 with dissolve
    mia "Пока, {b}[firstname]{/b}."
    return

label button_ross_collage:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show mia 2f zorder 0 at Position(xpos=0.55, ypos=1.0)
    with dissolve
    player_name "Ты готова к следующему занятию с {b}Miss Ross{/b}?"
    show player 1f
    show mia 6f
    mia "Да,наверное..."
    show player 10f
    show mia 2f
    player_name "Кажется, ты не в восторге от этого.."
    player_name "Я думал, что ты любишь искусство?"
    show player 11f
    show mia 6f
    mia "Я люблю искусство."
    mia "... И мне очень нравится смотреть за тобой и {b}Miss Ross{/b} работающими."
    show mia 6bf
    mia "Это просто..."
    show mia 6f
    mia "{b}Miss Ross{/b} заставляет меня чувствовать себя немного неловко."
    show player 10f
    show mia 2f
    player_name "Она?"
    show player 11f
    show mia 6f
    mia "Она очень прямолинейна со мной, ты не думаешь?"
    show player 2f
    show mia 2f
    player_name "Да, но она такая же со всеми."
    show player 1f
    show mia 6f
    mia "Она?"
    mia "Я не знаю, она прожила такую насыщенную жизнь и у нее много опыта..."
    show mia 6bf
    mia "Она заставляет меня чувствовать себя скучной."
    show player 2f
    show mia 2f
    player_name "Я не думаю что ты скучная, {b}Mia{/b}."
    show player 1f
    show mia 4f
    mia "Ты нет?"
    show mia 1f
    show player 2f
    player_name "Вовсе нет."
    player_name "Я думаю, что тебе просто нужно расслабиться и быть обьективной."
    player_name "Готов поспорить {b}Miss Ross{/b} может научить нас многим классным вещам!"
    show mia 5f
    show player 1f
    mia "..."
    show mia 3f
    mia "Да,может быть ты прав, {b}[firstname]{/b}!"
    show mia 4f
    mia "Я мог-"
    show mia 1f
    show player 11f
    show ross 11 at left with dissolve

    ross "Вот мои любимые ученики!"
    show mia 8b at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "О чем вы, голубки, говорите??"
    show mia 55 at Position(xpos=0.635, ypos=1.0) with dissolve
    show player 10f
    player_name "Голубки?"
    show mia 56
    show player 11f
    mia "Нам было просто интересно,что будет на сегоднешнем занятии?"
    show mia 55
    show ross 13
    ross "Сразу к делу,хм?"
    ross "Ты маленькая хлопушка, Я люблю это!"
    show ross 12
    mia "..."
    show ross 58 with dissolve
    ross "Сегодня каждый из вас сделает коллаж!"
    show ross 10 with dissolve
    show mia 12b at Position(xpos=0.65, ypos=1.0) with dissolve
    mia "Коллаж? Я даже не знаю, что это значит..."
    show mia 8b
    show ross 27 with dissolve
    ross "Ох, они намного веселее!Тебе должно понравится {b}Mia{/b}!"
    ross "Мы собираемся вырезать картинки из журналов и клеить их вместе, чтобы сделать искусство."
    show ross 26
    show player 2f
    show mia 7
    player_name "По-моему, будет интересно."
    show player 1f
    show mia 10
    mia "Да, так и есть."
    show mia 7
    show ross 11 with dissolve
    ross "Хорошо, ну у меня есть почти все, что нам нужно прямо здесь.Нам только не хватает {b}резинового клея{/b} и {b}большую стопку журналов.{/b}"
    ross "Почему бы вам двоим не пойти и не найти нам немного?"
    show ross 10
    show player 2f
    player_name "Мы сможем это сделать, правда {b}Mia{/b}?"
    show player 1f
    show mia 10b
    mia "Абсолютно. В действительности, я думаю что мой {b}Папа{/b} имеет некоторый резиновый цемент дома."
    show mia 10
    mia "Я пойду возьму его!"
    hide mia with dissolve

    show ross 11
    ross "... И она ушла!"
    ross "Я полагаю, это значит, что ты отвечаешь за поиск {b}журналов, [firstname]{/b}."
    ross "Если ты сможешь найти {b}три большие стопки журналов{/b}, думаю, этого должно быть достаточно."
    show player 2f
    show ross 10
    player_name "Есть идеи где я могу найти несколько?"
    show player 1f
    show ross 10b with dissolve
    ross "Хмм..."
    show ross 11
    ross "... Я бы начала с {b}Библиотеки{/b}.У них должен быть огромный выбор на выбор!"
    show player 2f
    show ross 10
    player_name "Отлично, Я пойду это проверю."
    return

label button_ross_find_magazines:
    scene location_school_art_closeup
    show player 2f zorder 1 at right
    show ross 10 at left
    with dissolve
    player_name "Где вы сказали, я должен их искать еще раз?"
    show player 1f
    show ross 11
    ross "{b}Журналы{/b}?"
    ross "Попробуй в {b}Библиотеке{/b}."
    ross "И посмотри,если сможешь ли ты найти {b}три большие стопки журналов{/b}, ладно?"
    if M_ross.get("talked with jane"):
        hide ross with dissolve
        show player 10 with dissolve
        player_name "{b}*Вздох*{/b}"
        player_name "В Библиотеке нет никаких журналов."
        if M_ross.get("magazines remaining") == 3:
            player_name "И мне все еще нужно найти еще 3 журнала."
        elif M_ross.get("magazines remaining") == 2:
            player_name "И мне все еще нужно найти еще 2 журнала."
        elif M_ross.get("magazines remaining") == 1:
            player_name "И мне все еще нужно найти еще 1 журнал."
        player_name "Я думаю я должен {b}осмотреться здесь в школе.{/b}"
    else:
        show ross 10
        show player 2f
        player_name "{b}Библиотека{/b}, понятно!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
