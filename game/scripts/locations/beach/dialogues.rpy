label treasure_open_no_key:
    player_name "( Даже если бы у меня была комбинация, мне всё равно надо найти {b}ключ{/b}! )"
    return

label beach_island_aqua_treasure_search:
    scene location_beach_island_blur
    show player 11 at left with dissolve
    pause
    show player 10
    player_name "Какая {b}интересная статуя{/b}."
    show player 2
    player_name "..."
    player_name "Согласно карте, {b}сокровища{/b} должны быть здесь."
    hide player with dissolve
    return

label beach_statue_no_shovel:
    scene location_beach_island_blur
    show player 2 at left
    player_name "( Без лопаты я {b}клад{/b} не {b}выкопаю{/b}. )"
    show player 4
    player_name "( ...Кажись, я видел её где-то {b}дома{/b}. )"
    hide player with dissolve
    return

label beach_statue_aqua_treasure_search:
    scene location_beach_digging01 with fade
    show text "Я копал несколько часов..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "...пока не устал, и руки не начали болеть." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Обессилив, я готов был отбросить эту затею." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Может не тут надо было копать?" at Position (xpos= 512, ypos= 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    scene location_beach_digging02 with fade
    show text "... Вдруг! Лопата ударилась об что-то твёрдое!" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    show text "Силы в миг вернулись, и вот, я уже достовал то, что тут спрятал Бен Довэр." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    show text "...это был большой, тяжёлый сундук; Это оно! Я нашёл клад!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label treasure_lock_intro:
    scene location_beach_lock with fade
    player_name "О, нет..."
    player_name "( Похоже что мне нужен {b}ключ{/b}...и {b}комбинация{/b} шифра чтобы открыть. )"
    return

label treasure_unlocked:
    scene location_beach_treasure
    if M_aqua.is_state(S_aqua_treasure_unlock):
        call expression game.dialog_select("treasure_aqua_treasure_unlock")
        $ player.get_item("golden_compass")
        $ M_aqua.trigger(T_aqua_treasure_unlocked)
    else:

        with fade
        pause
    $ game.main()

label treasure_aqua_treasure_unlock:
    show expression "objects/object_compass_01.png" at Position(xpos = 537, ypos = 473)
    with fade
    hide expression "objects/object_compass_01.png"
    call screen treasure_chest
    show closeup_compass_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
    player_name "Урааа!!"
    player_name "( Не могу поверить! Я нашёл сокровища! )"
    player_name "( Это должно быть компас, о котором рассказывал Терри. )"
    show popup_item_compass1 at truecenter with dissolve
    pause
    hide popup_item_compass1 with dissolve
    hide closeup_compass_01 with dissolve
    return

label beach_roxxy_spin_bottle_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 13f at right with dissolve
    player_name "( Вау, это идеальный день для пляжа! )"
    player_name "( Интересно, а девочки уже здесь? )"
    hide player
    show roxxy bikini 17f at right
    with dissolve
    rox "{b}[firstname]{/b}!!"
    player_name "!!!"
    pause
    hide roxxy
    show roxxy bikini 1f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "Э-эй, {b}Рокси{/b}..."
    show player 13f
    show roxxy bikini 2f
    rox "Я рада, что у тебя получилось!"
    show becca bikini 11 at Position(xpos=315)
    show missy bikini 1 at left
    with dissolve
    show roxxy bikini 1f
    becca "Ого, вы обнимаетесь?"
    show becca bikini 12
    show missy bikini 2
    missy "Привет, {b}[firstname]{/b}!!!"
    show missy bikini 1
    show player 14f
    player_name "Привет, {b}Мисси{/b}! {b}Бекка{/b}..."
    player_name "Вы выглядите красивыми в купальниках!"
    show player 13f
    show missy bikini 2b
    missy "Хехехе, правда?!"
    show missy bikini 1b
    becca "..."
    show becca bikini 11
    becca "Постарайся не пялиться, извращенец."
    show becca bikini 12
    show missy bikini 2b
    missy "Этот топ делает мою грудь больше?"
    show missy bikini 1b
    show becca bikini 14
    becca "Силикон - это то, что заставит эти крошечные сиськи выглядеть больше..."
    show becca bikini 12
    show missy bikini 11
    show player 5f
    player_name "..."
    show roxxy bikini 19 at Position (xpos=600) with dissolve
    rox "{b}Бекка{/b}, ты собираешься быть стервой весь день?"
    show roxxy bikini 20
    show becca bikini 11
    becca "... возможно."
    becca "ОН будет здесь весь день?"
    show becca bikini 12
    show roxxy bikini 19
    rox "{b}*Вздох*{/b}"
    show roxxy bikini 20
    show player 10f
    player_name "... {b}Бекка{/b}, Я..."
    show missy bikini 1
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "... Я принес тебе кое-что!"
    show player 239_240f with dissolve
    show becca bikini 11
    becca "Почему я должна что-то хотеть от-"
    show player 654bf with dissolve
    show becca bikini 6
    becca "!!!"
    becca "ООО, Бог мой!"
    becca "Это же {b}GoldSchwagger{/b}!!!?"
    show player 654f
    player_name "... Д-да?"
    show player 654bf
    show becca 17
    becca "ОООООООДДДДДДДДАААААА!!!"
    show becca bikini 8
    show player 13f
    with dissolve
    show roxxy bikini 1 at Position (xpos=600) with dissolve
    becca "Эта. штука. она. ЛУЧШАЯ!"
    show becca bikini 7 with dissolve
    becca "Спасибо за-"
    show becca bikini 7c
    becca "..."
    show becca bikini 7
    becca "То есть..."
    show becca bikini 7b
    show roxxy bikini 2
    rox "Видишь {b}Бекка{/b}."
    rox "{b}[firstname]{/b} хороший парень!"
    show roxxy bikini 1
    show missy bikini 2b
    missy "И милый!"
    show missy bikini 1b
    show becca bikini 7
    becca "... Да, ну..."
    becca "Полагаю, он неплох."
    becca "Для ботана."
    show becca bikini 7b
    show missy bikini 2b
    missy "Милый ботан!"
    show missy bikini 1b
    show roxxy bikini 2
    rox "Ладно, {b}Мисси{/b}! Мы поняли!"
    show roxxy bikini 2f at Position (xpos=500) with dissolve
    rox "Давайте начнем вечеринку."
    rox "Мне нужно немного солнца!"
    hide roxxy
    show becca bikini 8
    with dissolve
    becca "Не могу поверить, что он принес мне {b}GoldSchwagger{/b}!"
    hide becca with dissolve
    becca "{b}Декстер{/b} всегда забывал!"
    show player 17f
    player_name "..."
    show missy bikini 2b
    missy " {b}[firstname]{/b}, можешь сесть рядом со мной!"
    show missy bikini 1b
    show player 14f
    player_name "Хех, звучит неплохо."
    hide player
    hide missy
    with dissolve
    scene expression "backgrounds/location_beach_cutscene02.jpg"
    with fade
    show text "Прекрасная погода. Красивый пляж. Красивые девушки...\n... Что еще нужно пареньку?!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Бекка{/b} и {b}Мисси{/b} возможно, не были величайшими собеседниками в мире...\nНо они восполнили эти недостатки другими способами!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... и {b}Рокси{/b} оказалась на удивление хорошей компанией!\nМне показалось, что мы близки к тому, чтобы стать друзьями..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause

    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 3 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "... А потом вся эта пирамида рухнула!!"
    show roxxy sitting 2
    show missy sitting 5
    missy "Хахахаха!"
    show missy sitting 2
    show player_sitting 4
    player_name "Все это?!"
    show player_sitting 3
    show becca sitting 3
    becca "Да... и эта тощая сучка приземлилась первой, прямо мне на лицо!"
    show becca sitting 2
    show missy sitting 5
    missy "Ааахахахаха!"
    show player_sitting 4
    player_name "... Правда?!"
    show player_sitting 3
    show roxxy sitting 3
    rox "Это было довольно весело!"
    show roxxy sitting 2
    missy "{b}*фырк*{/b} Хахахаха!"
    show becca sitting 7
    becca "... Для тебя возможно!"
    becca "Она тяжелее, чем кажется!"
    show becca sitting 8
    show missy sitting 3
    missy "По крайней мере ..."
    show missy sitting 5
    missy "{b}*фырк*{/b} ... по крайней мере, в тот день на мне были трусики."
    show becca sitting 7
    becca "Нет, те розовые стринги не в счет!"
    show becca sitting 2
    show missy sitting 6
    show player_sitting 4
    player_name "Ты помнишь цвет?"
    show player_sitting 3
    show becca sitting 3
    becca "Ты шутишь? Изображение этих крошечных розовых стрингов, идущих на меня со скоростью сто миль в час, похоже на... Разрыв мозга!"
    show becca sitting 5
    becca "Как в кошмарном сне!"
    show player_sitting 5
    show missy sitting 5
    show roxxy sitting 5
    rox "Пффф, Хахаха!"
    missy "Хахаха!"
    becca "Хахаха!"
    show roxxy sitting 1
    show becca sitting 1
    show player_sitting 3
    player_name "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Уже поздно... Нам действительно нужно развести костер, если мы собираемся остаться."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Это хорошая идея-"
    becca "У меня голова кругом идет..."
    show becca sitting 2
    show missy sitting 5
    missy "Хахаха! {b}*фырк*{/b}"
    show player_sitting 3b
    show roxxy sitting 3
    rox "Блин, вы двое действительно не можете держать свой ликер."
    show missy sitting 2
    show roxxy sitting 2
    show player_sitting 4
    player_name "Я сделаю это."
    player_name "Девочки, вы просто расслабьтесь."
    hide player_sitting with dissolve
    show becca sitting 3
    becca "Вау, такой джентльмен..."
    show becca sitting 2
    rox "..."
    show roxxy sitting 3
    rox "... наконец-то потеплела к нему?"
    show roxxy sitting 2
    show becca sitting 3
    becca "... может быть."
    becca "Немного."
    show becca sitting 2
    show roxxy sitting 3
    rox "Сейчас самое подходящее время!"
    show roxxy sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "Серьезно."
    show becca sitting 1
    missy "Хей, {b}[firstname]{/b}?"
    show missy sitting 2
    player_name "Хмм?"
    show missy sitting 3
    missy "Правда ли, что у ботаников огромные члены?!"
    show becca sitting 8
    show roxxy sitting 8
    becca "!!!" with hpunch
    rox "!!!"
    show missy sitting 2
    show becca sitting 7b
    show roxxy sitting 7
    becca "Какого черта, {b}Мисси{/b}?!"
    show becca sitting 6b
    show roxxy sitting 3
    rox "Хорошоооо!"
    show becca sitting 6
    rox "Нет, больше пива для нее..."
    show roxxy sitting 2
    show missy sitting 3
    missy "Да ладно, разве вам не любопытно?!"
    show missy sitting 2
    show becca sitting 3
    becca "Хахаха, ты такая тупая шлюха, {b}Мисси{/b}..."
    show becca sitting 2
    show roxxy sitting 5
    rox "Хахаха!"
    show roxxy sitting 2
    show missy sitting 3
    missy "... И что?"
    missy "Я хучу!"
    show missy sitting 6
    missy "..."
    show missy sitting 3
    show becca sitting 8
    missy "О, боже! У меня появилась отличная идея!"
    show becca sitting 2
    show missy sitting 2
    show roxxy sitting 3
    rox "Ой-ё-ёй."
    show roxxy sitting 2
    show becca sitting 3
    becca "Это должно быть круто."
    show becca sitting 2
    show missy sitting 7
    missy "Нет, серьезно, заткнись!"
    show missy sitting 3
    show becca sitting 8
    missy "Мы должны поиграть в {b}Бутылочку{/b}!"
    show becca sitting 1
    show missy sitting 2
    show roxxy sitting 3
    rox "Что?!"
    show roxxy sitting 2
    show missy sitting 3
    missy "Да, давай! Это будет так весело!"
    show missy sitting 2
    show roxxy sitting 6
    rox "Ты просто хочешь поцеловать {b}[firstname]{/b}..."
    show roxxy sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "Черт возьми!"
    missy "Не так ли?!"
    show becca sitting 1
    show missy sitting 2
    show roxxy sitting 7
    rox "..."
    show roxxy sitting 6
    rox "О, нет ... Не совсем."
    rox "... Я сомневаюсь что {b}Бекка{/b} хоч-"
    show roxxy sitting 2
    show becca sitting 3
    becca "Я в игре!"
    show becca sitting 2
    show roxxy sitting 7
    rox "!!!" with hpunch
    show roxxy sitting 8
    rox "Правда?!"
    show roxxy sitting 7
    show becca sitting 3
    becca "Ну, почему бы и нет?"
    becca "Я очень пьяна, так что, наверное, все равно не вспомню.."
    show roxxy sitting 1
    show becca sitting 2
    show missy sitting 5
    missy "Это дух!"
    show missy sitting 2
    show roxxy sitting 2
    rox "..."
    show roxxy sitting 6
    rox "Ну, я думаю, если вы, ребята, действительно хотите... Я буду играть."
    show player_sitting 1 zorder 0 at Position (xpos=650) with dissolve
    show roxxy sitting 3
    rox "Ты не против поиграть в бутылочку {b}[firstname]{/b}?"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "Ох... Не знаю."
    player_name "Как это работает?"
    show player_sitting 3b
    show roxxy sitting 6
    rox "Ты серьезно не знаешь?"
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Конечно, нет, он ботан..."
    becca "Мы покажем тебе"
    show becca sitting 2
    show missy sitting 3
    show becca sitting 8
    missy "О, я первая!"
    show becca sitting 2
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "{b}*вздыхая*{/b} Хорошо."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 5
    missy "УРА!!"
    show missy sitting 3
    show becca sitting 8
    missy "Хорошо,так что все, что вам нужно сделать, это крутануть {b}Бутылочку{/b} и потом {b}Поцеловать того на кого она покажет{/b} когда остановится."
    show becca sitting 2
    show missy sitting 2
    show player_sitting 5
    player_name "!!!" with hpunch
    show player_sitting 4
    player_name "Поцеловать?!"
    player_name "В губы?"
    show player_sitting 5
    show missy sitting 3
    missy "Ага!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "МЫ не будем играть если не хочешь..."
    show roxxy sitting 2
    show player_sitting 4
    player_name "Н-нет! Я буду играть!"
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 6 zorder 1 at right
    show becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Хе-хе, Я была уверена..."
    show becca sitting 2
    rox "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Хорошо."
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 4 with dissolve
    missy "Хорошо, Я кручу первая!"
    call screen spin_bottle("becca", True)
    show missy sitting 6
    missy "..."
    show missy sitting 3
    missy "... И {b}[firstname]{/b} целует меня!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 6
    rox "Подожди-ка!"
    rox "... она остановилась на {b}Бекка{/b}. А не на {b}[firstname]{/b}!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    show becca sitting 8
    missy "Ох, правда?"
    missy "{b}*вздыхая*{/b} Хорошо."
    hide becca
    hide missy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show missy front sitting 1 at Position (xoffset=8)
    show becca front sitting 1f at Position (xoffset=-8)
    with dissolve
    pause
    show missy front sitting 3 at Position (xoffset=8)
    show becca front sitting 3f at Position (xoffset=-8)
    show missy_arm front sitting 1 at Position (xoffset=8)
    with dissolve
    pause
    hide becca
    hide missy
    hide missy_arm
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 1 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show player_sitting 3
    show missy sitting 7
    missy "Вот."
    show missy sitting 2
    show becca sitting 7b
    becca "Что это было?!"
    show becca sitting 6b
    show missy sitting 7
    missy "А?"
    show missy sitting 8
    show becca sitting 7b
    becca "Ты называешь это поцелуем?"
    show becca sitting 6b
    show missy sitting 1
    missy "..."
    show roxxy sitting 2
    rox "..."
    show missy sitting 7
    missy "Что, ты хочешь, чтобы я тебя за язык или что?!"
    show missy sitting 8
    show becca sitting 7b
    becca "А?! Нет!"
    becca "Я только..."
    becca "Ты паршиво целуешься... Это все, что я хочу сказать."
    show becca sitting 6b
    show missy sitting 7
    missy "Заткнись!"
    missy "Это нечестно, я не пыталась!"
    missy "{b}[firstname]{/b}, я не пыталась!"
    show missy sitting 8
    show becca sitting 1
    show player_sitting 5
    player_name "..."
    show player_sitting 4
    player_name "Я не... Я имею в виду-"
    show player_sitting 5
    show missy sitting 7
    missy "Серьезно, я не был'-"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 6
    rox "ДАЛЬШЕ!"
    show roxxy sitting 3
    show missy sitting 6
    rox "{b}[firstname]{/b} твой черед."
    show roxxy sitting 2
    show missy sitting 2
    show player_sitting 4b
    player_name "Хо-орошо..."
    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("becca", True)
    show player_sitting 3
    show missy sitting 7
    missy "{b}Бекка{/b} опять!"
    missy "Это подстроено!"
    show missy sitting 8
    hide player_sitting
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 2
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    becca "Это бутылка пива... Как бы мы подст-"
    show player front sitting 7b
    show player_arms front sitting 3
    show becca front sitting 3
    show player_shadow front sitting 1 zorder 0
    becca "!!!" with hpunch
    show becca front sitting 3b
    show player front sitting 7
    pause
    show becca front sitting 3
    show player front sitting 7b
    pause
    hide becca
    hide player_shadow
    hide player
    hide player_arms
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 2 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "..."
    rox "..."
    show missy sitting 7
    missy "... Как все прошло?!"
    show missy sitting 8
    show becca sitting 3
    becca "... пока."
    show becca sitting 1
    show player_sitting 5
    show missy sitting 3
    missy "Было круто?!"
    show missy sitting 2
    show becca sitting 2
    becca "..."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Это выглядело довольно хорошо!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "{b}Бекка{/b}!!!"
    show missy sitting 8
    show becca sitting 6b
    becca "Хмм?"
    show missy sitting 7
    missy "Как все прошло?!"
    show missy sitting 8
    pause
    show becca sitting 3
    becca "Очень хорошо..."
    show becca sitting 2
    show player_sitting 4
    player_name "Да?"
    show player_sitting 3
    show missy sitting 2
    show becca sitting 3
    becca "{b}*гммм*{/b} Я думаю... Да, наверное."
    becca "... Для ботаника. Ты знаешь?"
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 4 with dissolve
    rox "Хорошо, теперь моя очередь!"
    call screen spin_bottle("missy", True)
    show player_sitting 3b
    show roxxy sitting 3
    rox "Хммм, {b}Мисси{/b}..."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Предупреждаю. Она отстой."
    show becca sitting 2
    show missy sitting 7
    missy "Я не!"
    missy "Смотри!"
    hide missy
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=2)
    show missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    show missy_arm front sitting 1f at Position (xoffset=-2)
    show roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    pause
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide missy
    hide missy_arm
    hide roxxy_arm
    hide roxxy
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    player_name "!!!"
    show roxxy sitting 6
    rox "... Блин, ты наговорился?!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 3
    missy "Воу... {b}Рокси{/b}, ты на вкус как вишня!"
    show missy sitting 2
    show roxxy sitting 6
    rox "Охх... хорошо."
    show roxxy sitting 3
    rox "{b}Бекка{/b} твоя очередь."
    show roxxy sitting 2
    show becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show becca sitting 2 with dissolve
    show missy sitting 7
    missy "{b}[firstname]{/b} опять?!"
    missy "Это так несправедливо!"
    show missy sitting 8
    becca "..."
    rox "..."
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player front sitting 7b
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3
    show becca front sitting 3
    with dissolve
    becca "Ммм..."
    show player front sitting 7
    show becca front sitting 3b
    missy "О, боже..."
    show player front sitting 7b
    show becca front sitting 3
    rox "..."
    show player front sitting 7
    show becca front sitting 3b
    rox "... Ты должен поиграть с её титьками, {b}[firstname]{/b}."
    hide player
    hide player_arms
    hide player_shadow
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 7 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Что?!"
    missy "Сиськи-это не часть игры!"
    show missy sitting 8
    show roxxy sitting 6
    rox "Почему нет?"
    show roxxy sitting 3
    rox "Я просто говорю, они там."
    show roxxy sitting 2
    show becca sitting 3
    becca "... Хорошо. Я солгала."
    becca "Он действительно хорош в этом!"
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "Ха, теперь кто хочет его?"
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 3
    becca "Заткнись!"
    show becca sitting 2
    show missy sitting 4 with dissolve
    missy "Обе заткнитесь, моя очередь!"
    show missy sitting 2 with dissolve
    call screen spin_bottle("becca", True)
    show missy sitting 7
    missy "Да ладно, {b}Бекка{/b} опять?!"
    missy "Что за черт!"
    show missy sitting 8
    show roxxy sitting 3
    rox "Заткнись и целуй ее!"
    rox "Правильно на этот раз!"
    show roxxy sitting 2
    show missy sitting 7
    missy "{b}*вздох*{/b} Хорошо."
    hide missy
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1f at Position (xoffset=-4)
    show missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    show missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "Теперь это намного лучше."
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    player_name "..."
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "Готова поспорить, ты рад, что сегодня вечером пошёл к нам. Хм, {b}[firstname]{/b}?"
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    player_name "... Определенно!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    rox "Хах!"
    hide missy
    hide becca
    hide missy_arm
    with dissolve
    pause
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 6b at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 3 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    missy "Видите, я же говорила что хорошо целуюсь!"
    show missy sitting 2
    show becca sitting 7b
    becca "Не знаю кто тебе это сказал, но они солгали!"
    becca "Ты... весь язык!"
    show missy sitting 8
    show becca sitting 2
    show roxxy sitting 5
    rox "Хаха!"
    show roxxy sitting 2
    show missy sitting 7
    missy "Да пошли вы обе!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "Ладно, теперь очередь {b}[firstname]{/b}!"
    show roxxy sitting 2
    show missy sitting 2
    show player_sitting 15 with dissolve
    pause
    call screen spin_bottle("roxxy", True)
    show player_sitting 3b
    show missy sitting 8
    show roxxy sitting 3
    rox "О, похоже, это твоя счастливая ночь."
    show roxxy sitting 2
    show missy sitting 7
    missy "Это отстой..."
    show missy sitting 8
    hide player_sitting
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    show roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    rox "Ммм..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    becca "Он неплох, верно!"
    show player front sitting 7 at Position (xoffset=-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    missy "... Так нечестно."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide roxxy
    hide roxxy_arm
    hide player_arms
    hide player_shadow
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 8 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3b zorder 0 at Position (xpos=650)
    show missy sitting 8 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Черт, {b}[firstname]{/b}..."
    show roxxy sitting 6
    rox "Почему у тебя это так хорошо получается?!"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "... Я не знаю."
    show player_sitting 3b
    show roxxy sitting 3
    rox "Просто... Вау!"
    show roxxy sitting 2
    show missy sitting 3
    show player_sitting 7
    missy "Давай, продолжим в том же духе!"
    show missy sitting 8
    rox "..."
    show missy sitting 7
    missy "{b}Рокси{/b}!!!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "Хмм?"
    show roxxy sitting 2
    show missy sitting 7
    missy "Твой черёд!"
    show missy sitting 8
    show roxxy sitting 3
    rox "Ой, прости..."
    show roxxy sitting 4 with dissolve
    call screen spin_bottle("becca", True)
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "{b}Бекка{/b} опять."
    show missy sitting 8
    rox "..."
    show missy sitting 7
    missy "Почему всегда {b}Бекка{/b}?!"
    show missy sitting 8
    hide roxxy
    hide becca
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show roxxy front sitting 1 at Position (xoffset=5)
    show becca front sitting 1f
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    becca "!!!" with hpunch
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    missy "Вау!"
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    missy "Она на самом деле потянулась за её сиськами!"
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    player_name "..."
    hide roxxy
    hide roxxy_arm
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 7 at Position (xpos=300)
    show player_sitting 5 zorder 0 at Position (xpos=650)
    show missy sitting 2 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Какого черта, {b}Рокси{/b}?!"
    show becca sitting 6
    show roxxy sitting 6
    rox "О, не делай вид, будто тебе это не нравится."
    show roxxy sitting 3
    rox "Твои соски как камень."
    show roxxy sitting 2
    show becca 8b
    becca "!!!"
    show player_sitting 3b
    show roxxy sitting 6
    rox "Кроме того, это скучно, если это просто поцелуи."
    show roxxy sitting 2
    show player_sitting 3
    show becca sitting 1
    becca "..."
    show missy sitting 3
    missy "Я согласна!"
    show missy sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "Уверена, что {b}[firstname]{/b} понравилось!"
    show roxxy sitting 2
    show player_sitting 4
    player_name "Д-да!"
    player_name "Это было круто!"
    show player_sitting 3
    show roxxy sitting 5
    show missy sitting 5
    show becca sitting 5
    rox "Хахаха!"
    missy "Хахаха!"
    becca "Хахаха!"
    show roxxy sitting 3
    show missy sitting 2
    show becca sitting 2
    show player_sitting 3b
    rox "Смотри {b}Becca{/b}, я знаю, что я делаю."
    rox "Вращай, сучка!"
    show roxxy sitting 2
    show player_sitting 3
    becca "..."
    show becca sitting 4 with dissolve
    call screen spin_bottle("mc", True)
    show becca sitting 2 with dissolve
    show roxxy sitting 3
    rox "{b}[firstname]{/b}."
    show roxxy sitting 2
    show missy sitting 6
    missy "!!!"
    show missy sitting 7
    missy "Это какое-то дерьмо!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 6
    rox "Заткнись, {b}Мисси{/b}!"
    show roxxy sitting 3
    rox "Некоторые из нас пытаются насладиться шоу!"
    rox "Иди {b}[firstname]{/b} и поиграй с её сиськами на этот раз!"
    show roxxy sitting 2
    show player_sitting 4b
    player_name "... Правда?"
    show player_sitting 3b
    show roxxy sitting 3
    rox "Черт возьми, да!"
    rox "У {b}Бекки{/b} хорошая стойка."
    show roxxy sitting 6
    rox "... Не так хороша, как у меня, но..."
    show roxxy sitting 2
    show becca sitting 7
    becca "Пошла ты, {b}Рокси{/b}."
    show becca sitting 6
    show roxxy sitting 3
    rox "Ты же знаешь, что хочешь, сука..."
    show roxxy sitting 2
    show missy sitting 3
    missy "Я хочу!"
    show missy sitting 5
    missy "Ахахаах!"
    show becca sitting 6b
    becca "..."
    show roxxy sitting 3
    rox "Видишь, она полностью возбуждена!"
    show becca sitting 9
    rox "Давай, {b}[firstname]{/b}!"
    show roxxy sitting 2
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show becca front sitting 1
    show player car 2b zorder 1
    show player_arms car 1 zorder 2
    with dissolve
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    with dissolve
    becca "Мммм..."
    show player front sitting 7b
    show player_arms front sitting 4d
    show becca front sitting 3
    missy "Я как желе..."
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    rox "..."
    show player front sitting 7b
    show player_arms front sitting 4d
    show becca front sitting 3
    becca "Нннн!"
    show player front sitting 7
    show player_arms front sitting 4
    show becca front sitting 3b
    missy "Черт!"
    hide player
    hide player_shadow
    hide player_arms
    hide becca
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_fire_dialogue.jpg" with fade
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 3 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 6 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    becca "Ахх..."
    show becca sitting 2
    show player_sitting 3b
    show roxxy sitting 3
    rox "Продолжай!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "Что?! Ни за что, теперь моя очередь!"
    show missy sitting 8
    show player_sitting 3b
    show roxxy sitting 3
    rox "... Ох, заткнись, {b}Мисси{/b}."
    show roxxy sitting 6
    rox "Посмотрите на нее."
    rox "Пару часов назад она не хотела с ним ничего делать."
    show roxxy sitting 3
    rox "А сейчас готова запрыгнуть на него."
    show roxxy sitting 2
    show player_sitting 5
    show becca sitting 7
    becca "Не готова!"
    show becca sitting 6
    show player_sitting 3b
    show roxxy sitting 5
    rox "Ага. Щас!"
    show roxxy sitting 2
    show player_sitting 3
    show missy sitting 7
    missy "Могу я покрутить, пожалуйста?"
    show missy sitting 8
    show roxxy sitting 6
    rox "Бьюсь об заклад, твоя киска сейчас намокнет!"
    show roxxy sitting 2
    show becca sitting 8b
    show player_sitting 5
    becca "..."
    show missy sitting 7
    missy "К черту все, я верчу!"
    show player_sitting 3
    show missy sitting 8
    show roxxy sitting 3
    rox "Признай это!"
    show roxxy sitting 2
    show becca sitting 10b
    becca "... Заткнись!"
    show roxxy sitting 5
    show becca sitting 10
    rox "Ахаха, я так и знала!"
    show missy sitting 4 with dissolve
    player_name "..."
    call screen spin_bottle("mc", True)
    show missy sitting 5
    show becca sitting 9
    missy "ДА!"
    missy "НАКОНЕЦ!"
    show missy sitting 2
    becca "..."
    show missy sitting 3
    missy "Ладно, не стесняйся, можешь щупать все, что хочешь, {b}[firstname]{/b}!"
    show missy sitting 2
    show roxxy sitting 5
    rox "Хахаха!"
    show roxxy sitting 3
    rox "Ты грязная шлюшка, {b}Мисси{/b}!"
    show roxxy sitting 2
    show becca sitting 2
    show missy sitting 7
    missy "Шшшш, не порти все!"
    show missy sitting 9
    show player_sitting 3b
    show roxxy sitting 3
    rox "Вперед, {b}[firstname]{/b}."
    rox "Дай ей это."
    show roxxy sitting 2
    hide becca
    hide player_sitting
    with dissolve
    scene expression "backgrounds/location_beach_fire_kiss.jpg" with fade
    show missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    show missy_arm front sitting 1 zorder 3
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    pause
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    hide missy
    hide missy_arm
    hide player
    hide player_arms
    scene black
    with dissolve
    scene expression "backgrounds/location_beach_cutscene03.jpg" with fade
    show text "Это оказалась замечательная ночь!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Не могу поверить что встречался с {b}Рокси{/b} и {b}её подружками{/b}!\nНикто мне не поверит!\n... И {b}Рокси{/b} подталкивала их к дальнейшему!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Интересно, зачем она это делала?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause
    scene expression "backgrounds/location_beach_water_evening_blur.jpg"
    show roxxy bikini 1f at Position (xpos=500)
    show becca bikini 9 at Position(xpos=315)
    show missy bikini 1b at left
    show player 14f at right
    with dissolve
    player_name "Я должен ... На самом деле вернуться домой."
    player_name "Очень поздно."
    show player 13f
    show missy bikini 2
    missy "О, нет....."
    show missy bikini 1
    show roxxy bikini 2 at Position (xpos=600) with dissolve
    rox "{b}[firstname]{/b} прав."
    rox "Мы должны отвезти пышку домой, пока она не вырубилась."
    show roxxy bikini 1
    show becca bikini 10
    becca "Хмм?"
    becca "Нет, Я... {b}*зевая*{/b}..."
    becca "... Я в порядке!"
    show becca bikini 9
    show roxxy bikini 2
    rox "Ага, точно."
    rox "Я её не понесу!"
    show roxxy bikini 1
    show missy bikini 8
    missy "Эй, в последний раз я её несла!"
    show missy bikini 1
    show roxxy bikini 2
    rox "Ну, тебе лучше надеяться, что она сама дойдет до дома."
    rox "'Потому, что я её не понесу!"
    show roxxy bikini 1
    show missy bikini 8
    missy "Ахх, блин..."
    show missy bikini 1
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    show player 14f
    player_name "Спасибо за прекрасный вечер дамы!"
    show player 13f
    show becca bikini 10
    becca "Спасибо за {b}GoldSchwagger, [firstname]{/b}!"
    show becca bikini 9
    show player 14f
    player_name "Хех, незачто!"
    hide becca with dissolve
    pause
    hide player
    show roxxy bikini 17f at right
    with dissolve
    rox "Увидемся в школе, {b}[firstname]{/b}."
    show roxxy bikini 18f
    player_name "Спасибо за приглашение, {b}Рокси{/b}!"
    hide roxxy
    show roxxy bikini 2f at Position (xpos=500)
    show player 13f at right
    with dissolve
    rox "Да, было весело!"
    rox "... Может повторим в {b}следующии выходные{/b}!"
    hide roxxy with dissolve
    show missy bikini 1b
    missy "..."
    player_name "..."
    show missy bikini 2b
    missy "Ну... Ааа..."
    missy "Звони... как-нибудь?"
    show player 11f
    missy "K, пока!"
    hide missy with dissolve
    show player 10f
    player_name "Подожди!"
    show player 5f
    player_name "..."
    show player 12f
    player_name "Ты не давала мне свой номер..."
    show player 5f
    player_name "..."
    show player 10f
    player_name "О, ну."
    show player 17f
    player_name "( Чувак, ну и ночка выдалась! )"
    player_name "( Мне лучше вернуться домой, пока {b}[deb_char_name]{/b} не начала волноваться. )"
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_no_goldschwagger:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 5 with dissolve
    player_name "( {b}Рокси{/b} и ее друзья там, но я не могу пойти с пустыми руками! )"
    player_name "Я должен поговорить с {b}Капитаном Терри{/b} о бутылке {b}GoldSchwagger{/b} для {b}Бекки{/b} сначала... )"
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_wrong_time:
    scene expression "backgrounds/location_beach_water_night_blur.jpg"
    show roxxy bikini 19f at Position (xpos=500)
    show becca bikini 1b at Position(xpos=315)
    show missy bikini 12 at left
    show player 13f at right
    with dissolve
    rox "Пфф, ну посмотрите, кто, наконец, решил появился!"
    show roxxy bikini 20f
    show player 5f
    show becca bikini 17
    becca "Ботан!"
    show missy bikini 8
    missy "Ты пропустил всю вечеринку, {b}[firstname]{/b}!"
    show missy bikini 12
    becca "Хахаха, ботанский ботан!"
    show becca bikini 1b
    show player 12f
    player_name "{b}Бекка{/b} вставило?"
    show becca bikini 17
    show missy bikini 1
    show player 5f
    show roxxy bikini 19bf
    rox "Да, мы собирались отвезти её домой..."
    show roxxy bikini 20f
    show player 10f
    player_name "О, понятно."
    show becca bikini 1b
    player_name "Вам нужна помощь или что-то ещё?"
    show player 5f
    show roxxy bikini 19f
    rox "Нет, мы сами."
    rox "Я думала, когда самая популярная девушка в школе приглашает тебя на вечеринку, ты приходишь вовремя..."
    show roxxy bikini 20f
    show player 10f
    player_name "Прости, {b}Рокси{/b}. Я, должно быть, запуталась..."
    show player 5f
    show roxxy bikini 19f
    rox "Да, или ты меня не слушал!"
    rox "В любом случае, я должен позаботиться о пьяной заднице {b}Бекки{/b} ..."
    hide roxxy
    hide becca
    with dissolve
    becca "БББОООТТТТАААННН!!!"
    becca "Хахаха!"
    show player 37f with dissolve
    player_name "Я действительно облажался..."
    show player 5f with dissolve
    show missy bikini 2
    missy "Ничего страшного, {b}[firstname]{/b}"
    missy "{b}Просто приходи днем в следующие выходные{/b}."
    missy "{b}Рокси{/b} будет здесь."
    show missy bikini 1
    show player 10f
    player_name "А, хорошо."
    player_name "Спасибо, {b}Мисси{/b}."
    show player 5f
    show missy bikini 2b
    missy "Пока!"
    hide player
    hide missy
    with dissolve
    return

label beach_roxxy_invite_to_bikini_contest:
    scene expression "backgrounds/location_beach_water_contest_day_blur02.jpg"
    show player 14f at right with dissolve
    player_name "Вау, посмотрите на это место!"
    player_name "Здесь так много бикини!"
    show player 31f with dissolve
    player_name "..."
    show player 32f
    player_name "Хей, это же {b}Капитан Терри{/b} там?!"
    player_name "Я должен пойти и посмотреть, что он делает здесь."
    hide player with dissolve
    return

label beach_cabin_roxxy_in_cabin:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 13f at right
    show player 10 at left
    with dissolve
    player_name "... {b}Рокси{/b}?"
    player_name "Ты в порядке?"
    show player 5
    show roxxy bikini 15f
    rox "... Нет."
    rox "Фу, это было так неловко!"
    show roxxy bikini 14f
    show player 10
    player_name "Не так все плохо."
    player_name "Я не думаю, что кто-нибудь видел кроме {b}Бекки{/b} и меня..."
    show player 5
    show roxxy bikini 15f
    rox "... Правда?"
    show roxxy bikini 14f
    show player 14
    player_name "Да."
    player_name "Кроме того, даже если кто-то видел... Какая разница?"
    show player 18
    player_name "У тебя потрясающая грудь!"
    player_name "Определенно нечего стыдиться ..."
    show player 13
    rox "..."
    show roxxy bikini 15 with dissolve
    rox "Да, я думаю, ты прав."
    show roxxy bikini 14
    rox "..."
    show roxxy bikini 13
    rox "... но что мне теперь делать?!"
    rox "Я не могу участвовать в конкурсе в порваном бикини!"
    show roxxy bikini 14
    show player 10
    player_name "У тебя есть запасной?"
    show player 5
    show roxxy bikini 13
    rox "... Нет."
    show roxxy bikini 14
    show player 34
    player_name "..."
    show player 14
    player_name "Не волнуйся, {b}Рокси{/b}."
    player_name "Я щас пойду и куплю тебе новый!"
    show player 13
    show roxxy bikini 15
    rox "Ты не успеешь!"
    show player 5
    rox "Сорревнование вот вот начнется, {b}[firstname]{/b}!"
    show roxxy bikini 13
    rox "... Я облажалась."
    show roxxy bikini 14
    show player 10
    player_name "Успокойся."
    player_name "Я что нибудь придумаю!"
    show player 5
    show roxxy bikini 15
    rox "Да, хорошо!"
    rox "Где ты его найдешь?"
    show roxxy bikini 14
    show player 10
    player_name "Ну, на пляже..."
    show player 14
    player_name "{b}Где-то же должен быть ещё купальник{/b}."
    show player 13
    show roxxy bikini 15b
    rox "Иди и скажи {b}Бекка{/b} чтобы она отдала мне свой!"
    show roxxy bikini 15c
    show player 12
    player_name "Ааа?"
    player_name "Ты хочешь взять купальник {b}Бекки{/b}?"
    show player 5
    show roxxy bikini 15b
    rox "Да, эта сука отдаст его мне, если я ей скажу."
    show roxxy bikini 15c
    show player 12
    player_name "... Но тогда, что она будет носить?"
    show player 5
    show roxxy bikini 15b
    rox "Умм, кого это волнует?"
    rox "Не похоже, что она все равно выиграет!"
    show roxxy bikini 15c
    show player 10
    player_name "Не надо, {b}я найду тебе другой!{/b}"
    show player 5
    show roxxy bikini 15b
    rox "Хмм, ладно!"
    rox "Я дам тебе 10 минут, а потом забуру у {b}Бекки{/b}..."
    show roxxy bikini 15c
    show player 10
    player_name "Я быстро."
    hide player with dissolve
    show roxxy bikini 15b
    rox "... только не уродливый!"
    hide roxxy with dissolve
    return

label beach_cabin_roxxy_get_new_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show player 5 at left
    show roxxy bikini 15 at right
    with dissolve
    rox "Ну что, нашел?!"
    show roxxy bikini 14
    show player 10
    player_name "Не волнуйся, {b}я найду тебе купальник!{/b}"
    show player 5
    show roxxy bikini 15b
    rox "Хррр!"
    rox "Ну, лучше найди побыстрее, или я заберу у {b}Бекки{/b}..."
    hide roxxy with dissolve
    show player 10
    player_name "Хмм, {b}Я должен найти здесь бикини, которую никто не использует{/b}."
    hide player with dissolve
    return

label beach_cabin_roxxy_has_bikini:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 14 at right
    show player 14 at left
    with dissolve
    player_name "{b}Рокси{/b}, вроде нашел!"
    show roxxy bikini 15
    rox "Правда?!"
    rox "Покажи, покажи!"
    show roxxy bikini 14
    show player 239_240 with dissolve
    pause
    show player 656b with dissolve
    show roxxy bikini 15
    rox "*ах*"
    show roxxy bikini 15d
    show player 13
    with dissolve
    rox "Красивый!"
    show roxxy bikini 15e
    show player 14
    player_name "Ага, он... Патриотический."
    show player 13
    show roxxy bikini 15d
    rox "Хахаха!"
    show roxxy bikini 9 with dissolve
    show player 433
    pause
    show roxxy bikini usa 5
    show player 296
    with dissolve
    pause
    show roxxy 22 with dissolve
    pause
    show roxxy 23b with dissolve
    rox "Что ты делаешь?"
    show roxxy 23
    pause
    player_name "Хмм?"
    show roxxy 24
    rox "Ты уже видел меня голой, помнишь?"
    show roxxy 23
    player_name "Да, Я... Я только..."
    show roxxy 23b
    rox "Пш, перестань ботанить!"
    show player 433 with dissolve
    show roxxy 22 with dissolve
    pause
    show player 434
    show roxxy bikini usa 6 with dissolve
    pause
    show roxxy bikini usa 14 with dissolve
    show player 435
    player_name "... Вау!"
    show roxxy bikini usa 11 with dissolve
    show player 434
    rox "Я знаю!"
    show roxxy bikini usa 6b with dissolve
    rox "Хм, немного жмет ..."
    show roxxy bikini usa 6c with dissolve
    pause
    show roxxy bikini usa 6b with dissolve
    rox "Он не слишком маленький?"
    pause
    show roxxy bikini usa 6c with dissolve
    player_name "..."
    show roxxy bikini usa 6b
    rox "... Что думаешь?"
    show roxxy bikini usa 9 with dissolve
    player_name "..."
    show roxxy bikini usa 12 with dissolve
    rox "{b}[firstname]{/b}!!!"
    show roxxy bikini usa 13
    show player 435
    player_name "Хмм?"
    show player 434
    show roxxy bikini usa 8 with dissolve
    rox "Как выглядит?"
    show player 435
    player_name "... Действительно, ДЕЙСТВИТЕЛЬНО хорошо!"
    player_name "... Это как, мое любимое бикини когда-либо!"
    show player 434
    show roxxy bikini usa 10 with dissolve
    rox "Хахаха!"
    rox "Ты думаешь я выйграю?"
    show roxxy bikini usa 9
    show player 17
    player_name "Без сомнения!"
    show player 13
    show roxxy bikini usa 10
    rox "Отлично!"
    rox "Теперь мне просто нужно, чтобы ты смазал меня маслом!"
    show roxxy bikini usa 9
    show player 22
    player_name "!!!" with hpunch
    show player 23
    player_name "Ты сказала, хочешь что бы Я что..."
    show player 22
    player_name "{b}*глоток*{/b}"
    show roxxy bikini usa 12 with dissolve
    rox "Ха, ты стесняешься меня, {b}[firstname]{/b}?"
    rox "Я могу попросить {b}Бекки{/b} если ты не можешь..."
    rox "Я просто подумала, ты нашел бикини и ещё..."
    show roxxy bikini usa 13
    show player 36 with dissolve
    player_name "Н-нет! Я готов!"
    show player 14 with dissolve
    player_name "Я обязательно это сделаю!"
    show player 13
    show roxxy bikini usa 12
    rox "Ха-ха, я так и думала!"
    rox "{b} Они обычно держат немного в башне спасателя.{/b}"
    rox "Почему бы тебе не пойти и взять бутылку, а я буду ждать тебя здесь."
    show roxxy bikini usa 13
    show player 14
    player_name "Ясно! Я скоро вернусь!"
    show player 12
    player_name "Не двигайся!"
    hide player with fastdissolve
    pause
    show roxxy bikini usa 6b with dissolve
    rox "Ха-ха, поспеши, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    return

label beach_tower_roxxy_get_oil:
    scene expression "backgrounds/location_beach_cutscene01.jpg"
    with fade
    show text "Я практически поднялся по лестнице на башню спасателя!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Рокси{/b} действительно позволит мне втереть масло в ее тело перед соревнованием!\nПросто неверится!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я должен быстрее найти бутылку, чтобы быть как можно больше времени с ней!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_beach_tower_day_blur.jpg"
    show player 14 with fastdissolve
    player_name "( Хмм, {b}Рокси{/b} сказала что я найду {b}бутылку с маслом{/b} где-то здесь! )"
    hide player with fastdissolve
    return

label beach_cabin_roxxy_get_oil:
    scene expression "backgrounds/location_beach_water_contest_day_blur.jpg"
    show player 29 with fastdissolve
    player_name "Боже мой! Что я делаю?!"
    show player 29f with fastdissolve
    player_name "Я должен {b}найти эту бутылку масла{/b} на {b}вышке спасателя{/b} прежде чем {b}Рокси{/b} передумает!"
    hide player with fastdissolve
    return

label beach_cabin_roxxy_has_oil:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 9 at right with None
    show player 184b at left
    with fastdissolve
    player_name "{b}*Уфф*{/b} Я сделал..."
    player_name "Я сделал это..."
    player_name "{b}*Уфф*{/b}"
    show player 658 with dissolve
    player_name "Уф! Вот масло..."
    show roxxy bikini usa 10
    rox "Шиш, ты бежал всю дорогу или что?!"
    show roxxy bikini usa 9
    show player 184b with dissolve
    player_name "..."
    show roxxy bikini usa 10
    rox "Хахахахаха!"
    show roxxy bikini usa 10
    rox "Ну, молодец чтоли..."
    show roxxy bikini usa 9
    player_name "..."
    show roxxy bikini usa 10
    rox "Ладно..."
    rox "Давай начнем смазывать маслом, хорошо?!"
    show roxxy bikini usa 9
    show player 658 with dissolve
    player_name "Д-да, хорошо!"
    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show roxxy massage 2 with dissolve
    rox "Просто убедись, что смажешь все, хорошо?"
    show roxxy massage 3 with dissolve
    rox "Начни с моих плеч..."
    show roxxy massage 1 with dissolve
    player_name "Хорошо!"
    show roxxy massage 4_5 with dissolve
    rox "Ммм..."
    player_name "..."
    pause
    show roxxy massage 1 with dissolve
    player_name "Я все правильно делаю?"
    show roxxy massage 2
    rox "... Ты что, никогда раньше не тер плечи девушкам?"
    show roxxy massage 1
    player_name "Ну - Нет!"
    player_name "Я имею в виду... Конечно, я натирал плечи многим девушкам!"
    show roxxy massage 2
    rox "Ух хух..."
    rox "Тогда не задавай глупых вопросов!"
    show roxxy massage 1
    player_name "..."
    pause
    label roxxy_massage_45:
        show roxxy massage 4_5 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_45")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8_9 with dissolve
    rox "Ммм... Так хорошо."
    rox "Убедись, что не пропустил ни одного места!"
    player_name "Ага, я знаю."
    player_name "Я обязательно покрою все!"
    pause
    rox "О, это действительно хорошо."
    player_name "..."
    label roxxy_massage_89:
        show roxxy massage 8_9 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_89")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 5 with dissolve
    pause
    show roxxy massage 6_7 with dissolve
    rox "ААА... Это очень приятно, {b}[firstname]{/b}..."
    player_name "... Д-да?"
    rox "Мммммм, не останавливайся..."
    player_name "Х-хорошо."
    pause
    label roxxy_massage_67:
        show roxxy massage 6_7 with dissolve
        pause
        pause
    call screen roxxy_massage("roxxy_massage_67")
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8 with dissolve
    pause
    show roxxy massage 9_10 with dissolve
    rox "Ннннн!!"
    rox "..."
    rox "О, вау!"
    player_name "..."
    rox "Потрясающие ощущения!"
    pause
    show roxxy massage 3 with dissolve
    rox "Ааа, продолжай!"
    show roxxy massage 9_10 with dissolve
    rox "Не останавливойся!"
    rox "Не остан-"
    becca "{b}Рокси{/b} время начинать -"
    scene expression "backgrounds/location_beach_cutscene04.jpg"
    with fade
    show text "Повезло...\n{b}Мисси{/b} и {b}Бекка{/b} были у входа в кабинку..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 1 at right
    rox "!!!" with hpunch
    show becca bikini 18 at Position(xpos=315)
    show missy bikini 12 at left
    with dissolve
    becca "... Вот дерьмо!"
    show becca bikini 1b
    hide roxxy
    show roxxy bikini usa 15 zorder 1 at Position (xpos=650)
    show player 81f zorder 0 at right
    with dissolve
    show missy bikini 14
    pause
    show missy bikini 15 with dissolve
    missy "Я так и знала, черт возьми!"
    missy "Смотри, {b}Бекка{/b}?"
    missy "Я же говорила что у ботанов огромные члены!"
    show becca bikini 15
    show missy bikini 14
    becca "..."
    show player 78f
    show becca bikini 18
    becca "Извени, мы не верили-"
    show becca bikini 15
    becca "..."
    show becca bikini 18
    becca "Если серьезно... черт возьми {b}[firstname]{/b}!"
    show becca bikini 15
    show player 82f
    show roxxy bikini usa 18 with dissolve
    rox "Мы ничего не делали..."
    show becca bikini 1b
    rox "Он просто мазал меня маслом для соревнований!!!"
    show roxxy bikini usa 17
    becca "..."
    show becca bikini 2b
    becca "Ну, это не выглядит безобидно {b}Рокси{/b}..."
    show becca bikini 1b
    show missy bikini 13
    missy "Серьезно!"
    missy "Можно мне тоже?"
    show missy bikini 14
    show becca bikini 14
    becca "Заткнись, {b}Мисси{/b}!"
    show becca bikini 16
    show missy bikini 2
    missy "... Что?!"
    show missy bikini 13
    missy "Я тоже хочу масла!"
    missy "Ты намажешь меня маслом, не так ли {b}[firstname]{/b}?"
    show becca bikini 1b
    show missy bikini 14
    show player 83f
    player_name "... Я..."
    show player 82f
    show roxxy bikini usa 18
    rox "Вы, ребята, серьезно!"
    rox "Вы не должны никому об этом говорить!"
    show roxxy bikini usa 17
    show becca bikini 2b
    becca "Да, {b}Декстер{/b} убьет вас если узнает."
    show becca bikini 1b
    player_name "..."
    rox "..."
    show becca bikini 2
    becca "Мы никому не расскажем."
    show becca bikini 14
    becca "Правда, {b}Мисси{/b}?!"
    show becca bikini 16
    show missy bikini 2b
    missy "Хмм?!"
    missy "Рассказать что?"
    show missy bikini 14
    show becca bikini 14
    becca "... Точно."
    show becca bikini 2
    becca "Да ладно, они зовут всех на сцену."
    show becca bikini 16
    missy "..."
    show becca bikini 14
    becca "Хватит пялиться на его член и пойдем!"
    show becca bikini 16
    show missy bikini 13
    missy "... Ааа."
    hide missy with dissolve
    show becca bikini 15
    pause
    show becca bikini 18
    becca "... вот дерьмо."
    hide becca with dissolve
    pause
    show roxxy bikini usa 19
    rox "..."
    show player 83f
    player_name "... Ты в порядке?"
    show player 82f
    show roxxy bikini usa 18f at Position (xpos=550) with dissolve
    rox "Д-да."
    rox "Только нервничаю из-за соревнования."
    show roxxy bikini usa 17f
    show player 83f
    player_name "Ага."
    player_name "Не волнуйся, ты великолепна!"
    show player 82f
    rox "..."
    show player 83f
    player_name "Давай, нам лучше поторопиться!"
    hide player with dissolve
    rox "..."
    show roxxy bikini usa 13f
    pause
    hide roxxy with dissolve
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    show tstand 19b zorder 0 at Position (xpos=729)
    Terry "О, хо-хо! Однажды ты станешь причиной моей смертью, дорогая..."
    show tstand 20b
    sara "Хехе, ну, по крайней мере, ты умрешь счастливым!"
    show tstand 19b
    Terry "Бог с ним!"
    show player 11 zorder 2 at left with dissolve
    show tstand 19
    Terry "Ну тогда, если это не шкипер, еще раз."
    Terry "Как дела, дружище?"
    show tstand 19d
    show player 14
    player_name "Все отлично, {b}Капитан{/b}!"
    player_name "Я просто проводил своего друга на сцену."
    show player 13
    show roxxy bikini usa 9f zorder 1 at Position (xpos=400) with dissolve
    pause
    show tstand 19
    Terry "Уфф, какая красотка!"
    show tstand 19d
    show roxxy bikini usa 10f
    rox "... Спа-спасибо!"
    show roxxy bikini usa 9f
    show tstand 20c with dissolve
    sara "{b}*ах*{/b}"
    sara "Это мое бикини?"
    show tstand 19d
    show roxxy bikini usa 16f
    with dissolve
    rox "!!!"
    show player 21
    player_name "Да."
    show roxxy bikini usa 17f
    player_name "У {b}Рокси{/b} порвался топ в последнюю минуту и я нашел только этот."
    player_name "Надеюсь вы не против, {b}Мисс Сара{/b}?"
    player_name "... Я бы спросил но..."
    show player 11
    show tstand 20
    sara "Хахаха, ни слова больше."
    sara "Нет проблем, дорогуша."
    show roxxy bikini usa 13f
    show player 13
    sara "Был бы он чуть побольше..."
    show tstand 19d
    show roxxy bikini usa 11f with dissolve
    rox "Это выглядит плохо?"
    show roxxy bikini usa 9f
    show tstand 19
    Terry "Нет!"
    Terry "Он немного туговот, но ничего..."
    Terry "На самом деле он заставляет меня салютовать все больше и больше!"
    Terry "Oh ho ho!"
    show tstand 20
    sara "Хаха, {b}Терри{/b} ты ужасен!"
    sara "Ты выглядишь великолепно, милая!"
    sara "Иди и оставь его!"
    show tstand 20d at right with dissolve
    sara "Но сначала ты должна пойти и выиграть!"
    hide tstand
    show tstand 19d at Position (xpos=729)
    with dissolve
    show roxxy bikini usa 10f
    rox "Точно!"
    show roxxy bikini usa 10 zorder 1 at Position (xpos=450) with dissolve
    rox "Пожелай мне удачи, {b}[firstname]{/b}!"
    show roxxy bikini usa 9
    show player 14
    player_name "Хах, тебе не нужно это, но удачи!"
    show roxxy bikini usa 10
    rox "Ааа, спасибо {b}[firstname]{/b}!"
    hide player
    show roxxy bikini usa 7 at left
    with dissolve
    pause
    hide roxxy
    show player 13 at left
    with dissolve
    show tstand 19
    Terry "Я так понимаю, всё идет хорошо?"
    show tstand 19d
    show player 10
    player_name "А?"
    show player 5
    show tstand 19c
    Terry "Ох хо хо!"
    Terry "Неважно, шкипер."
    show tstand 19
    Terry "Почему бы тебе не взять мою {b}Сара{/b} и не найти пару мест?"
    Terry "Мне нужно вести шоу!"
    show player 13
    show tstand 20b
    sara "Вперед, любовь моя."
    show tstand 20e with dissolve
    pause
    show tstand 20 with dissolve
    sara "Давай, {b}[firstname]{/b}! найдем свободные места!"
    hide tstand with dissolve
    show player 14
    player_name "Да, мэм."
    hide player with dissolve
    scene expression "backgrounds/location_beach_cutscene05.jpg"
    with fade
    show text "Соревнование было так здорово смотреть!\nВсе эти красивые женщины в скудных бикини...\n... И {b}Мисс Сара{/b} сидит рядом со мной все представление.\nКакой прекрасный день!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "{b}Рокси{/b} и ее подружки попали в финал!\n... Но ни у кого не было сомнений, кто победит." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Ни одна из них не могла сравниться с {b}Рокси{/b}!!!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_water_contest_closeup.jpg"
    show player 13 at Position (xpos=500)
    show missy bikini 13 at left
    show becca bikini 17 at Position (xpos=315)
    show roxxy bikini usa 4 at right
    with dissolve
    rox "Вууу!!!"
    missy "Хахаха!"
    show roxxy bikini usa 2
    becca "Так держать, девочка!"
    show missy bikini 1
    show becca bikini 1
    show player 14
    player_name "Поздравляю, {b}Рокси{/b}!"
    show player 14f at Position (xpos=550) with dissolve
    player_name "Всем вам, правда!"
    show player 13f
    show missy bikini 2
    missy "Я добрался до финала!"
    show missy bikini 13
    missy "Ты видел меня, {b}[firstname]{/b}?!"
    show missy bikini 1
    show becca bikini 14
    becca "... Конечно, он видел тебя, дура..."
    becca "Он был в толпе, наблюдая все это время."
    show becca bikini 16
    show missy bikini 2b
    missy "Вы проверяли, не смотрит ли он?!"
    show missy bikini 1b
    show becca bikini 14
    becca "Что?!"
    becca "Н-нет!"
    becca "Заткнись!"
    show becca bikini 1
    show roxxy bikini usa 4
    rox "Хахаха!"
    show roxxy bikini usa 3
    rox "Вы прекратите или нет!"
    show player 13 at Position (xpos=500) with dissolve
    show roxxy bikini usa 4
    rox "Не могу поверить, я победила!"
    show player 18
    rox "{b}[firstname]{/b}, я победила!!!"
    show roxxy bikini usa 2
    show player 14
    player_name "Я знаю! Ты была великолепна!"
    show player 13
    show roxxy bikini usa 4
    rox "Хахаха!"
    show roxxy bikini usa 3
    rox "Спасибо за большую помощь сегодня!"
    show roxxy bikini usa 2
    show becca bikini 2b
    becca "Ха, да... Это была \"большая помощь\" правда, {b}Рокси{/b}?!"
    show becca bikini 1b
    rox "..."
    show missy bikini 8
    missy "... А?"
    show missy bikini 2
    missy "Подожди! Поняла!"
    show missy bikini 13
    show becca bikini 16
    missy "Ты говоришь про его член, правда?!"
    show becca bikini 17
    show roxxy bikini usa 4
    show player 37 at Position (xoffset=41) with dissolve
    becca "Хахаха!"
    missy "Хахаха!"
    rox "... Хахаха!"
    show becca bikini 1
    show missy bikini 1
    show roxxy bikini usa 3
    rox "Не обращай внимания, {b}[firstname]{/b}."
    rox "Серьезно, спасибо тебе!"
    show roxxy bikini usa 2
    show player 14 with dissolve
    player_name "Пожалуйста."
    player_name "Нужна помощь чтобы добраться домой?"
    show player 13
    show roxxy bikini usa 3
    rox "Не, я заставлю этих двух сучек."
    show roxxy bikini usa 2
    becca "..."
    show missy bikini 2
    missy "О, я помогу!"
    show missy bikini 1
    show roxxy bikini usa 3
    rox "Увидемся в школе?"
    show roxxy bikini usa 2
    show player 14
    player_name "Конечно. Увидемся завтра."
    show player 13
    show becca bikini 2b
    becca "Пока, {b}[firstname]{/b}."
    show becca bikini 1b
    show missy bikini 13
    missy "Поккккка, {b}[firstname]{/b}!!!"
    hide becca
    hide missy
    hide roxxy
    hide player
    with dissolve
    return

label beach_cabin_roxxy_massage:
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini 2 at right
    show player 13 at left
    with dissolve
    rox "Прости, мне понадобилась целая вечность, чтобы ускользнуть от них!"
    show roxxy bikini 1
    show player 14
    player_name "Без проблем."
    player_name "Ты готова для массажа?"
    show player 13
    show roxxy bikini 2
    rox "Да!"
    rox "У тебя лучший массаж!"
    show roxxy bikini 1
    show player 12
    player_name "Эй, это же бикини {b}Мисс Сары{/b}?"
    show player 13
    show roxxy bikini 2
    rox "Да, она сказала мне сохранить, помнишь?"
    rox "Я подумала, ты захочешь, чтобы я надела его на наши сеансы массажа?"
    show roxxy bikini 1
    show player 14
    player_name "Д-да, определенно!"
    show player 13
    show roxxy bikini 2
    rox "Хахаха!"
    show roxxy bikini 5 with dissolve
    pause
    show roxxy bikini 6 with dissolve
    show player 434
    pause
    show roxxy bikini 7 with dissolve
    pause
    show roxxy bikini 8 with dissolve
    pause
    show roxxy bikini 9 with dissolve
    pause
    show roxxy bikini usa 5 with dissolve
    pause
    show roxxy 22 with dissolve
    pause
    show roxxy bikini usa 6 with dissolve
    pause
    show roxxy bikini usa 14 with dissolve
    pause
    show roxxy bikini usa 12 with dissolve
    rox "Хватит стоять и смотреть на мои сиськи, начинай растирать!"
    hide roxxy
    hide player
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup_massage.jpg"
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 4_5 with dissolve
    rox "Ммм..."
    player_name "..."
    pause
    show roxxy massage 1 with dissolve
    player_name "Так хорошо?"
    show roxxy massage 2
    rox "... О, да."
    rox "Три немного сильнее."
    show roxxy massage 1
    player_name "Так!"
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 4_5 with dissolve
    pause
    rox "Пф, хорошо!"
    player_name "..."
    pause
    label roxxy_massage_45_repeat:
        show roxxy massage 4_5 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_45_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8_9 with dissolve
    rox "Ммм... хорощо."
    rox "Убедись, что не пропустил ни одного места!"
    player_name "Ага, я знаю."
    player_name "Я обязательно покрою все!"
    pause
    rox "О, вот так!"
    player_name "..."
    label roxxy_massage_89_repeat:
        show roxxy massage 8_9 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_89_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 5 with dissolve
    pause
    show roxxy massage 6_7 with dissolve
    pause
    rox "ААА... Это очень приятно, {b}[firstname]{/b}..."
    player_name "... Д-да?"
    rox "Мммммм, не останавливайся..."
    player_name "Х-хорошо."
    pause
    label roxxy_massage_67_repeat:
        show roxxy massage 6_7 with dissolve
        pause
    call screen roxxy_massage("roxxy_massage_67_repeat")
    pause
    show roxxy massage 3 with dissolve
    pause
    show roxxy massage 8 with dissolve
    pause
    show roxxy massage 9_10 with dissolve
    rox "Ннннн!!"
    rox "..."
    rox "О, вау!"
    player_name "..."
    rox "Потрясающие ощущения!"
    pause
    show roxxy massage 3 with dissolve
    rox "Ааа, продолжай!"
    show roxxy massage 9_10 with dissolve
    rox "Не останавливойся!"
    rox "Не остан-"
    missy "{b}Рокси{/b}, ты здесь?"
    scene expression "backgrounds/location_beach_cutscene04.jpg"
    with fade
    show text "Опять, {b}Мисси{/b} и {b}Бекка{/b} были у входа в кабинку..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_beach_cabin_closeup.jpg"
    show roxxy bikini usa 1 at right
    show becca bikini 1b at Position(xpos=315)
    show missy bikini 1b at left
    with dissolve
    rox "!!!" with hpunch
    hide roxxy
    show roxxy bikini usa 15b zorder 1 at Position (xpos=650)
    show player 82f zorder 0 at right
    with dissolve
    rox "Черт побери, вы двое!"
    rox "Вы опять шпионили?!"
    show roxxy bikini usa 15
    show missy bikini 13
    missy "Да."
    show missy bikini 1b
    show becca bikini 14
    becca "Ха?! Нет!"
    show roxxy bikini usa 17 with dissolve
    becca "Заткнись, {b}Мисси{/b}!"
    show becca bikini 16
    show missy bikini 8
    missy "Что?"
    show missy bikini 15 with dissolve
    missy "Мы тоже хотим массаж..."
    show missy bikini 14 with dissolve
    show becca bikini 18
    becca "О. Мой. Бог."
    show becca bikini 1
    show roxxy bikini usa 15b with dissolve
    rox "{b}*вздох*{/b}"
    show roxxy bikini usa 18 with dissolve
    rox "Мы как раз заканчивали..."
    show roxxy bikini usa 17
    show missy bikini 13
    missy "Отлично, я следующая!"
    show missy bikini 14
    show roxxy bikini usa 18
    rox "Да, я так не думаю!"
    rox "Тащите свои тупые задницы обратно в воду!"
    show roxxy bikini usa 17
    show missy bikini 10
    missy "Ауф..."
    hide becca
    hide missy
    with dissolve
    show roxxy bikini usa 18f at Position (xpos=550) with dissolve
    rox "Извини за них, {b}[firstname]{/b}..."
    show roxxy bikini usa 17f
    show player 83bf
    player_name "Хех, все в порядке."
    player_name "На самом деле это действительно мило."
    show player 83cf
    show roxxy bikini usa 12f
    rox "Хе-хе, да, я знаю..."
    rox "... Но я не могу дать им все, что они хотят."
    rox "Бунча жадные суки, эти две!"
    show roxxy bikini usa 13f
    show player 83bf
    player_name "Хахаха!"
    show player 83cf
    show roxxy bikini usa 10f with dissolve
    rox "Ну, спасибо за массаж."
    show roxxy bikini usa 9f
    show player 83bf
    player_name "Пожалуйста."
    show player 83cf
    show roxxy bikini usa 11f
    rox "Кто знает? Может, в следующий раз мы закончим..."
    show roxxy bikini usa 9f
    show player 82f
    player_name "{b}*глоток*{/b}"
    show roxxy bikini usa 10f
    rox "Хехехе."
    hide roxxy with dissolve
    hide player with dissolve
    return

label beach_roxxy_spin_bottle_sex_intro:
    scene expression game.timer.image("backgrounds/location_beach_water_day{}_blur.jpg")
    show player 14f at right
    show missy bikini 1 zorder 2 at left
    with dissolve
    player_name "Привет, {b}Мисси{/b}."
    show player 13f
    show missy bikini 16 with dissolve
    missy "{b}*вздох*{/b}!"
    show missy bikini 13 with dissolve
    missy "Он здесь!"
    missy "{b}Рокси{/b}, {b}Бекка{/b}!! Он здесь, Он здесь, Он здесь!!!"
    show missy bikini 1 with None
    show becca bikini 2 zorder 1 at Position (xpos=315)
    show roxxy bikini 1f zorder 0 at Position (xpos=500)
    with dissolve
    becca "Привет, {b}[firstname]{/b}."
    show becca bikini 1
    show player 14f
    player_name "Привет, {b}Becca{/b}."
    show player 13f
    show missy bikini 2
    missy "Наконец-то он здесь!!"
    show missy bikini 1
    show roxxy bikini 19bf
    rox "Боже мой, заткнись наконец."
    rox "Мы тебя и в первый раз слышали."
    show roxxy bikini 1f
    show missy bikini 10
    missy "Тсс, заткнись!"
    show missy bikini 13
    show roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "Я взволнована..."
    show missy bikini 1
    show becca bikini 19
    becca "..."
    show roxxy bikini 19
    rox "Вы хотите чтобы я все рассказала?!"
    show roxxy bikini 20
    show becca bikini 6
    show missy bikini 8
    becca "Что?!"
    missy "Нет, пожалуйста!"
    show becca bikini 6b
    missy "Прости меня! Слушай, я затыкаюсь прямо сейчас!"
    show missy bikini 16 with dissolve
    show roxxy bikini 2
    rox "Посмотрим, как долго это продлится..."
    show roxxy bikini 1
    show player 17f
    player_name "Хахаха, девчонки вы такие смешные!"
    show player 14f
    show roxxy bikini 1f at Position (xpos=500) with dissolve
    player_name "Итак, что случилось?"
    player_name "{b}Рокси{/b} сказала что-то о сюрпризе?"
    show player 13f
    show roxxy bikini 2f
    rox "Да, сказа-"
    show missy bikini 13 with dissolve
    missy "Большой сюрприз!"
    show roxxy bikini 24f
    show becca bikini 13
    with dissolve
    pause
    show roxxy bikini 20 at Position (xpos=600) with dissolve
    missy "Вы будете любить-"
    hide becca
    show missy bikini 18
    with dissolve
    becca "{b}Мисси{/b} заткнись!"
    show missy bikini 18b
    show roxxy bikini 19
    rox "Серьезно?!"
    rox "Ты даже 5 секунд помолчать не можешь?!"
    show roxxy bikini 20
    show missy bikini 19
    becca "Не волнуйся, она помолчит."
    show missy bikini 19b
    show roxxy bikini 19b
    rox "{b}*ох*{/b}"
    show roxxy bikini 2f at Position (xpos=500) with dissolve
    rox "Мы будем играть в бутылочку или нет."
    show roxxy bikini 1f
    show player 14f
    player_name "Хе, опять в бутылочку?"
    show player 13f
    show roxxy bikini 22f with dissolve
    rox "Да, но с небольшим изменением правил."
    show roxxy bikini 21f
    show player 12f
    player_name "Изменением правил?"
    show player 13f
    rox "Ммммммм..."
    show roxxy bikini 22f
    rox "Видишь ли, в определенный момент... Я укажу {b}финальное вращение{/b}."
    rox "Затем ты будешь вращать в последний раз.."
    rox "... И тот, на кого покажет бутылка, присоединится к нам в раздевалке за особую награду."
    show roxxy bikini 21f
    show player 14f
    player_name "О?"
    player_name "Что за особая награда?"
    show player 13f
    show missy bikini 17 with dissolve
    missy "Мммммффффммм!"
    show roxxy bikini 19bf with dissolve
    rox "..."
    show missy bikini 18b with dissolve
    rox "Она просто не может держать рот на замке!"
    show missy bikini 19b
    show roxxy bikini 2f
    rox "В любом случае, это сюрприз."
    rox "Тебе придется играть, чтобы узнать."
    show roxxy bikini 1f
    show player 14f
    player_name "Ну, хорошо."
    player_name "Давай!"
    show player 13f
    show missy bikini 17 with dissolve
    missy "Ммммррррффф!!"
    show player 14f
    player_name "Хех, она так взволнована..."
    show player 13f
    show missy bikini 18b with dissolve
    show roxxy bikini 19f
    rox "{b}*ох*{/b}..."
    show roxxy bikini 1f
    show missy bikini 19
    becca "Ты понятия не имеешь..."
    hide roxxy
    hide missy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
