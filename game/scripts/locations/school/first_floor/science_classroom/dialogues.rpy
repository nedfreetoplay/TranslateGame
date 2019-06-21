label science_classroom_first_visit:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "Привет, {b}Мисс Окита{/b}."
    show player 1
    show okita 3
    okita "Вот ты где, {b}[firstname]{/b}. Ты хоть представляешь, как далеко ты отстал?!"
    show player 5
    okita "Твои оценки ниже, чем они могут быть. Надеюсь, у тебя есть оправдание!"
    show player 10
    show okita 4
    player_name "Да, мой ... .. Мой отец умер."
    show player 5
    show okita 3
    okita "... Ой."
    show okita 5
    okita "Что ж, какая жалость. Извините, что так вышло {b}[firstname]{/b}."
    show player 10
    show okita 4
    player_name "Вам никто не сказал?"
    show player 5
    show okita 9
    okita "Ты же не ждешь, что я буду слушать каждую сплетню, которую эти простаки приносят в мою дверь?"
    show okita 4
    player_name "..."
    show okita 5
    okita "Клянусь, мой IQ упал на двадцать пунктов с тех пор, как я взялся за эту дурацкую работу..."
    show okita 11
    okita "... Имбецилы из Cuntech."
    show player 10
    show okita 4
    player_name "Cuntech?"
    show player 5
    show okita 5
    okita "Неважно."
    show player 10
    show okita 4
    player_name "... Ладно, я надеялся, что у вас есть способ повысить мои оценки."
    player_name "Дополнительный кредит или что?"
    show player 5
    show okita 2
    okita "Дополнительный кредит?"
    show okita 2b
    okita "... Нет, я не делаю дополнительных кредитов."
    show player 10
    show okita 1
    player_name "Серьезно? Я ничего не могу сделать?"
    player_name "Чем я могу вам помочь?"
    show player 5
    show okita 10
    okita "Хмм..."
    show okita 2
    okita "... Я сомневаюсь. Насколько ты знаком с Абиогенезом?"
    show player 10
    show okita 1
    player_name "Абио-что?"
    show player 11
    show okita 8
    okita "..."
    show okita 2
    okita "Ты когда-нибудь работал с нейтрино?"
    show player 10
    show okita 1
    player_name "Что такое нейтрино?"
    show player 11
    show okita 7
    okita "О, ясно!"
    okita "У меня сложный эксперимент с магнитными Монополями. Может, поможешь мне с этим делом, а?"
    show player 10
    show okita 6
    player_name "Ты сейчас вообще говоришь по-английски?"
    show player 11
    show okita 7
    okita "Хе-хе, ну прости, {b}[firstname]{/b}. Я бы сказала, что ты привязан к другому объекту наклонной плоскостью, спирально обернутой вокруг оси."
    show player 34
    show okita 6
    player_name "..."
    show player 35
    player_name "Хух?"
    show player 11
    show okita 2b
    okita "Ты облажался..."
    show player 12
    show okita 1
    player_name "Фу, это отстой!"
    show player 5
    show okita 5
    okita "Мммм. Я вот что тебе скажу..."
    okita "Мы только что закончили изучение репродуктивных процессов Двукрылых."
    show player 10
    show okita 4
    player_name "... Двукрылых?"
    show player 11
    show okita 3
    okita "Дом мух."
    show player 10
    show okita 4
    player_name "Ой."
    show player 5
    show okita 5
    okita "И сегодня мы начинаем наше Введение в базовую химию."
    okita "Так почему бы вам не начать с этого, и я постараюсь придумать какой-то способ для вас, чтобы заработать проходной балл до окончания семестра."
    show player 11
    show okita 3
    okita "Это звучит приемлемо?"
    show player 10
    show okita 4
    player_name "Да, полагаю, это все, на что я могу надеяться в данный момент."
    show player 1
    show okita 7
    okita "Возможно, это самая умная вещь, которую когда-либо говорил студент в этом классе!"
    show player 5
    show okita 4
    player_name "..."
    show okita 5
    okita "Начнем, {b}[firstname]{/b}."
    show okita 3
    okita "... И, пожалуйста, следуй инструкциям учебника."
    show player 10
    show okita 4
    player_name "*вздыхая*"
    player_name "Да, мэм."
    return

label science_classroom_cutscene:
    scene location_school_science_cutscene01
    with fade
    show text "Интересно, почему {b}Мисс Окита{/b} всегда такая сварливая?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Она казалась довольно непреклонной в отсутствии дополнительных кредитов." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene02
    with fade
    show text "Держу пари, я могу изменить ее мнение!\nМне просто нужно доказать, что я не такой глупый, каким она меня видит..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Это не должно быть слишком сложно!\nЭто просто базовая химия, и я довольно умный в конце концов..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Что может пойти не так?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene03
    with fade
    show text "( !!! )" at Position (xpos= 512, ypos= 700) with hpunch
    with dissolve
    pause
    hide text
    with dissolve
    return

label science_classroom_after_cutscene:
    scene location_school_science_closeup
    show player 428 zorder 4 at Position(xpos=0.35, ypos=1.0)
    show playerb 1 zorder 5 at Position(xpos=0.35, ypos=0.765)
    with dissolve
    pause
    show player 108f
    player_name "... Упппс."

    show player 5
    show mia 43f zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    mia "Боже мой, {b}[firstname]{/b}!"
    show mia 8
    show erik 53f zorder 0 at Position(xpos=0.15, ypos=1.0)
    show erikl 1 zorder 1 at Position(xpos=0.14, ypos=1.0)
    with dissolve
    eri "Срань Господня, чувак! Ты в порядке?"
    show erik 51f
    show player 10
    player_name "Я ... э-э. Думаю, да..."
    show player 5
    pause

    show okita 11 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve
    okita "Серьезно, {b}[firstname]{/b}!?!"
    hide mia
    hide mial
    with dissolve
    show erik 53f
    show player 23
    show mia 43 zorder 2 at Position(xpos=0.5, ypos=1.0)
    show mial 1 zorder 3 at Position(xpos=0.51, ypos=1.0)
    with dissolve
    okita "Неужели трудно следовать инструкциям в книге химии, написанной для детей!?"
    show player 22
    show okita 11b
    player_name "..."
    show okita 11
    okita "Ты мог сжечь всю школу дотла!"
    show player 10
    show okita 11b
    player_name "Простите, {b}Мисс Окита{/b}. Я не-"
    player_name "... Я не знаю, что случилось!"
    show player 5
    show okita 11
    okita "Ты не знаешь, что случилось?!"
    show okita 11b
    pause
    show okita 11
    okita "Я расскажу тебе, что случилось!"
    okita "Ты потерял свои привилегии в лаборатории! Именно это и произошло!!!"
    show player 24
    show okita 11b
    player_name "О, блин..."
    show player 25
    show okita 11
    okita "Клянусь, я не могу оторвать глаз от вас, обезьянки, ни на секунду..."
    okita "То, что вы можете одеться утром, не поддается никакой логике!"
    show player 24
    show okita 11b
    player_name "По крайней мере, я уже провалился. Мне больше нечего терять, правда."
    show player 5
    show okita 11
    okita "Всегда есть что-то, что я могу сделать-"
    show okita 8
    okita "..."
    show okita 9
    okita "Хух."

    hide okita
    with dissolve
    show okita 10cf zorder 8 at Position(xpos=0.85, ypos=1.0)
    okita "Ему нечего терять..."
    show okita 10bf
    show mia 8f
    pause
    show okita 10cf
    okita "... и он в отчаянии."
    show player 10
    show okita 10bf
    player_name "Ухх, {b}Мисс Окита{/b}?"
    show player 5
    okita "..."
    show okita 10cf
    okita "Он тоже очень упрямый человек."
    okita "... и находчивый."
    show okita 10bf
    player_name "..."
    show okita 10cf
    okita "Да, это может сработать."
    show okita 10bf
    show erik 51f
    show mia 43
    mia "Хмм, мэм? Вы же знаете, что мы вас слышим?"
    show mia 8bf
    hide okita with dissolve
    show okita 8 zorder 8 at Position(xpos=0.8, ypos=1.0) with dissolve

    okita "Хмм?"
    show okita 3
    okita "О, да, да!"
    show okita 11
    okita "Вы ребятки возвращайтесь к работе."
    okita "[firstname], ты только смотришь за {b}Мией{/b} и {b}Эриком{/b} сегодня."
    okita "Я не хочу, чтобы ты еще что-нибудь взорвал."
    show okita 11b
    show player 10
    player_name "... Д-да, мэм."
    show player 5
    show okita 11
    okita "... И приходи ко мне после занятий."
    okita "Я просто, думаю, таким образом, ты можешь поднять свои оценки в конце концов."
    hide okita with dissolve
    show okita 4f at Position(xpos=0.85, ypos=1.0) with dissolve
    pause
    hide okita with dissolve

    player_name "..."
    hide mia
    hide mial
    with dissolve
    show mia 8 zorder 6 at Position(xpos=0.65, ypos=1.0)
    show mial 1f zorder 7 at Position (xoffset=162)
    with dissolve
    show erik 53f
    eri "Это звучало немного зловеще..."
    show erik 51f
    show mia 43f
    mia "Да, так и есть."
    show erik 53f
    show mia 8
    eri "Эта женщина пугает меня до усрачки."
    show erik 51f
    show player 10
    player_name "Ну это не может быть хуже, чем недостаток..."
    show player 5
    show erik 53f
    eri "Я не знаю, чувак..."
    show erik 51f
    show mia 43f
    mia "Надеюсь ты прав."
    show mia 8
    show player 24
    player_name "..."

    return

label science_classroom_mia_return_favor:
    scene school_science_c02
    show player 13 at left
    show mia 10 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Привет, {b}Мия{/b}."
    show player 12
    player_name "Как твоя...нога?"
    show player 13
    show mia 9
    mia "О, хорошо... Просто немного болит, ха ха."
    show mia 10
    mia "Уже намного лучше, и я сняла повязку!"
    show mia 7
    show player 17
    player_name "Круто! Как она выглядит?"
    show player 13
    show mia 10
    mia "Вообще-то, я хотел показать тебе... И еще кое-что в знак благодарности за помощь."
    show mia 7
    show player 10
    player_name "Здесь?"
    show player 11
    show mia 9
    mia "Не здесь, глупенький!"
    show mia 7
    show player 17
    player_name "О, ха ха."
    show player 13
    show mia 10
    mia "{b}Приходи ко мне вечером{/b} я тебе покажу."
    show mia 7
    show player 14
    player_name "Хорошо, я приду!"
    show player 13
    show mia 10
    mia "Здорого! Увидемся!"
    hide player
    hide mia
    hide mial
    with dissolve
    return

label science_classroom_okita_has_items:
    scene location_school_science_closeup02
    show xtra 36 zorder 6
    show mial 8 zorder 5 at Position (xpos=0.7225, ypos=1.055)
    show okita 94 zorder 3 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f zorder 4 at Position(xpos=0.5, ypos=0.385)
    with dissolve
    mia "Хорошо, я просто добавила перекись водорода..."
    show mial 5

    okita "Ммммммм..."
    show player 14 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    player_name "Привет, {b}Мисс Окита{/b}, Я-"
    show player 10
    player_name "... Ох."
    show okita 3
    show okitag 1 at Position(xpos=0.4, ypos=0.385)
    with dissolve
    show player 11
    show mial 7
    okita "[firstname]! Ты вовремя!"
    show player 10
    show okita 4
    player_name "... Простите?"
    show player 11
    show mial 8
    mia "Привет, {b}[firstname]{/b}!"
    show player 2
    show mial 7
    player_name "Привет {b}Мия{/b}!"
    player_name "{b}Мисс Окита{/b}, Я получил-"
    show player 11
    show okita 9
    okita "Да, да! Мне это прекрасно известно."
    show okita 5
    okita "Я помогала {b}Мие{/b}. Почему бы тебе не присоединиться к нам."
    show player 10
    show okita 4
    player_name "Я думал, мне нельзя трогать химическое оборудование?"
    show player 11
    show okita 5
    okita "О, тебе определенно нельзя прикасаться, просто наблюдай..."
    show okita 4
    show mial 8
    mia "Да ладно, {b}[firstname]{/b}. Я покажу тебе, как это делается!"
    show player 2
    show mial 7
    player_name "Д-да, хорошо!"
    show player 110f at Position(xpos=0.25, ypos=1.0)
    show playerl 1 at Position(xpos=0.2475, ypos=1.0)
    show playerg 1 at Position(xpos=0.265, ypos=0.35)
    show okita 94 at Position(xpos=0.45, ypos=1.0)
    show okitag 1f at Position(xpos=0.5, ypos=0.385)
    with dissolve
    show mial 5
    pause
    show mial 6
    mia "Так на чем я остановилась?"
    show mial 5
    okita "..."
    show mial 3 at Position (xpos=0.71, ypos=1.055)
    mia "Хм, я думаю, что я должен добавить немного дрожжей."
    show mial 4 at Position (xpos=0.695, ypos=1.055)
    okita "..."
    show okita 95
    okita "... Подожди."
    show mial 5 at Position (xpos=0.7225, ypos=1.055)
    hide okita
    hide okitag
    show okita 98 zorder 3 at Position(xpos=0.475, ypos=1.015) with dissolve
    okita "Что ты только что добавила!?"
    show player 109f
    show okita 97
    show mial 6
    mia "Ухх..."
    show okita 98
    okita "Ты только что добавила дрожжи?"
    show player 108f
    show okita 97
    show mial 6
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    okita "..."
    show okita 98b
    show okitagf 3 at Position(xpos=0.6, ypos=0.835)
    okita "( !!! )" with hpunch
    show player 23
    show mial 9 with dissolve
    pause
    show okitagf 2 zorder 7 at Position(xpos=0.6025, ypos=0.835)
    show okita 98c with dissolve
    pause
    hide okitagf
    pause



    scene location_school_science_closeup
    show okita 11 zorder 3 at Position(xpos=0.75, ypos=1.0)
    show okitagf 1 zorder 4 at Position(xpos=0.725, ypos=0.68)
    show mia 45 zorder 5 at Position(xpos=0.35, ypos=1.0)
    show mial 1 zorder 6 at Position(xpos=0.3625, ypos=1.0)
    show player 11 zorder 0 at Position(xpos=0.15, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.1475, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.165, ypos=0.35)
    with dissolve
    okita "Невероятно!"
    okita "Я полностью пропитана!"
    show okita 11b
    mia "..."
    player_name "..."
    show okita 11
    okita "Некомпетентность в этой школе поражает!"
    okita "Никто ничего не может сделать правильно!?"
    show okita 11b
    show mia 46
    mia "П-Простите, мэм."
    mia "Должно быть, я просмотрела не ту страницу..."
    show mia 45
    show okita 11
    okita "Я не хочу слышать твоих оправданий!"
    hide okita
    hide okitagf
    show okita 19 zorder 3 at Position(xpos=0.76, ypos=1.0)
    with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    show okitagf 4 zorder 4 at Position(xpos=0.7175, ypos=0.42)
    show okita 21 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    okita "Тебе повезло, что у меня в школе есть сменная одежда."
    show player 11
    show okita 20
    mia "..."
    player_name "..."


    show okita 21
    okita "Эк! Я вся такая липкая!"

    okita "Отвратительно..."
    okita "Мне нужно принять душ!"
    show okita 20
    show mia 43
    mia "Простите, {b}Мисс Окита{/b}. Я не хотела..."
    show mia 45
    show player 10
    player_name "Все хорошо, {b}Мия{/b}. Не-"
    show player 11
    show okita 21
    okita "Это не хорошо! Я вычту баллы из твоей оценки за это, {b}Мия{/b}!"
    show okita 20
    show mia 46
    mia "Да, мэм."
    show okita 21
    okita "Теперь тащи свою задницу домой!"
    hide mia
    hide mial
    with dissolve
    okita "{b}[firstname]{/b}!!!"
    show player 10 at Position(xpos=0.35, ypos=1.0)
    show playerl at Position(xpos=0.3475, ypos=1.0)
    show playerg at Position(xpos=0.365, ypos=0.35)
    with dissolve
    show okita 20
    player_name "Д-да, мэм?"
    show player 11
    show okita 21
    okita "Приходи ко мне завтра."
    okita "И мы начнем нашу работу."
    show player 10
    show okita 20
    player_name "Д-да, мэм."
    $ game.timer.tick(2)
    return

label science_classroom_okita_has_glasses:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "{b}Мисс Окита{/b}, Они у меня!"
    player_name "У меня есть линзы, которые вам были нужны!"
    show player 1
    show okita 3
    okita "Позволь посмотреть!"

    show okita 16 with dissolve
    okita "Да, они должны хорошо смотреться."
    show okita 14
    okita "Ладно, иди сюда и начинай собирать."
    show player 10
    show okita 15
    player_name "Вы хотите, чтобы я их построил?"
    show player 11
    show okita 9 with dissolve
    okita "Однозначно."
    show player 10
    show okita 4
    player_name "Но я не могу этого сделать!"
    show player 11
    show okita 5
    okita "Почему?"
    show player 10
    show okita 4
    player_name "Я думал, что это важно? Тебе следует это сделать самой."
    show player 11
    show okita 5
    okita "Нет, это обезьянья работа."
    show okita 9
    okita "{b}Тори Окита{/b} не делает обезьянью работу..."
    show okita 4
    player_name "..."
    show player 10
    player_name "Что если я что-нибудь испорчу?"
    show okita 5
    okita "Указания по сборке прямо здесь!"
    show okita 3
    okita "Ты не можешь следовать простым указаниям?!"
    show player 11
    show okita 4
    player_name "... Могу."
    show player 10
    show okita 5
    okita "Ну тогда прояви твердость духа и приступай к работе."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Хорошо."

    return

label science_classroom_okita_has_glasses_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Хорошо, {b}Мисс Окита{/b}. Думаю, на этот раз у меня получится."
    show player 1
    show okita 9
    okita "Ты не можешь сделать ничего хуже."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Я заставлю это работать на этот раз, я знаю это!"

    show player 16
    show okita 5
    okita "Ну, придется подождать до окончания занятий. Сядь, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "Я готов, давайте сделаем это!"
    show player 1
    show okita 5
    okita "Конечно."
    return

label science_classroom_okita_has_glasses_int_pass:
    $ persistent.cookie_jar["Okita"]["unlocked"] = True
    $ persistent.cookie_jar["Okita"]["gallery"]["01_unlocked"] = True
    scene location_school_science_cutscene05
    with fade
    show text "Поэтому я принялся за работу." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup02
    show xtra 36 zorder 4
    show player 538f zorder 0 at right
    show okita 1f zorder 3 at Position(xpos=0.4, ypos=1.0)
    with dissolve
    player_name "Хорошо!"

    show player 540f with dissolve
    player_name "Одна пара окуляров Окитатрона, готова к тестированию!"
    show player 540bf
    show okita 3f
    okita "Ты проверил уплотнение на корпусе?"
    show player 538f with dissolve
    show okita 1f
    player_name "А, точно! Хорошо, одну секунду."
    show player 538bf
    show okita 4f
    okita "..."
    show kevin 8f zorder 1 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1 zorder 2 at Position(xpos=0.15, ypos=1.0)
    with dissolve
    pause
    show kevin 9f
    kev "Извените, {b}Мисс Окита{/b}?"
    show kevin 8f
    show okita 5f
    okita "И убедись, что блок питания заряжен!"
    show kevin 9f
    show okita 4f
    kev "Эээ, {b}Мисс Окита{/b}? Не могли бы вы нам помочь?"
    show kevin 8f
    show okita 9f
    okita "Ухх."
    show okita 3 at Position(xpos=0.5, ypos=1.0) with dissolve

    okita "Да, {b}Kevin{/b}. Что случилось?"
    show kevin 9f
    show okita 4
    kev "{b}Ронда{/b} и я работали над заданием, которое вы раздали сегодня во время урока, и мы столкнулись с проблемой."
    show kevin 8f
    show okita 9
    okita "*вздох*"
    show okita 5
    okita "Конечно вы столкнулись..."
    show okita 3
    okita "Очень хорошо. Давай сделаем это за моим столом. {b}[firstname]{/b}  работает над чем-то важным для меня."
    hide kevin
    hide kevinl
    with dissolve
    hide okita
    with dissolve
    pause
    hide player
    show player 538f with dissolve
    player_name "Хмм..."
    player_name "Все выглядит неплохо."
    show player 539f with dissolve

    player_name "Это круто!"
    scene location_school_science_closeup
    show xtra 38b zorder 6 with dissolve
    show okita 4 zorder 0 at right
    show kevin 9f zorder 2 at Position(xpos=0.25, ypos=1.0)
    show kevinl 1 zorder 3 at Position(xpos=0.2535, ypos=1.0)
    show ronda b_casual a_casual_sides f_normal o_labcoat1 zorder 4 at flip
    show ronda at Position (xpos=300)
    with dissolve

    player_name "Кажется, все функции работают..."
    player_name "..."
    player_name "Просто нужно проверить камеру."
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1
    player_name "Что за-"
    show okita 5
    show kevin 8f
    player_name "... Это что?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 0.25
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 0.25
    show xtra 38b
    show kevinl 1
    show ronda o_labcoat1
    hide okitax
    pause 1.5
    player_name "Они были обнажены на секунду..."
    show okita 4
    show kevin 9f
    player_name "..."
    player_name "Может, если я нажму на кнопку?"
    show xtra 38
    show kevinl 1b
    show ronda o_labcoat2
    show okitax 1 zorder 1 at Position(xpos=0.86, ypos=1.0)
    pause 1
    player_name "( !!! )" with hpunch
    player_name "Вау!"
    player_name "Это как настоящие рентгеновские очки!"
    pause
    player_name "... Я не думаю, что это должно было произойти."
    pause
    show okita 5
    show kevin 8f
    player_name "Я вижу у {b}Мисс Окита{/b}... "
    pause
    player_name "... и посмотрите на тело {b}Ронды{/b}! Она в форме!"
    pause
    player_name "..."
    show okita 4
    show kevin 9f
    player_name "Ой мой бог! Я вижу у {b}Кевина{/b}..."
    pause
    hide ronda
    show kevin 8 at Position(xpos=0.15, ypos=1.0)
    show kevinl 1bf at Position(xpos=0.1485, ypos=1.0)
    with dissolve
    show okita 9
    player_name "Ох, я застрял в этом режиме!"
    hide kevin
    hide kevinl
    hide okita
    hide okitax
    show okita 4 zorder 0
    show okitax 1 zorder 1 at Position(xpos=0.49, ypos=1.0)
    with dissolve
    player_name "Она возвращается!!!"
    player_name "Нет, нет, нет!"
    scene location_school_science_closeup02
    show player 22f zorder 0 at right
    show playerg 2f zorder 1 at Position(xpos=0.83, ypos=0.35)
    show okita 5f at left
    with dissolve
    okita "Ну?"
    show player 11f
    show okita 4f
    player_name "..."
    show okita 11f
    okita "{b}[firstname]{/b}!?"
    show player 10f
    show okita 11bf
    player_name "Д-да?"
    show player 11f
    show okita 11f
    okita "Что с тобой?!"
    okita "Дай мне очки!"
    show player 10f
    show okita 11bf
    player_name "О, х-хорошо..."
    hide playerg
    show player 540cf
    with dissolve
    player_name "Вот."
    show player 11f
    show okita 4f
    show okitag 4f at Position(xpos=0.17, ypos=0.525)
    with dissolve
    player_name "..."
    show okita 3f
    okita "Почему все зеленое?"
    show okita 4f
    pause
    show okita 3f
    okita "... И почему ты-"
    show okita 8f
    show player 22f
    pause
    show okita 3f
    okita "Хух."
    okita "Это необычно."
    show player 11f
    show okita 4f
    player_name "..."
    show okita 3f
    okita "... Это очень необычно.."
    show okita 5f
    with dissolve
    okita "{b}[firstname]{/b}, у тебя все еще есть Код от моего офиса?"
    show okita 4f
    show player 11f
    player_name "Да, {b}Мисс Окита{/b}."
    show player 73f
    pause
    show player 459f
    pause
    show player 461f
    show okita 5f
    okita "Тогда {b}встретимся наверху в моем офисе{/b}."
    show okita 4f
    show player 460f
    player_name "А?"
    show player 461f
    show okitag 4 at Position(xpos=0.09, ypos=0.525)
    show okita 5 at left
    with dissolve
    okita "Прямо сейчас."

    hide okitag
    hide okita
    hide player
    show player 11f
    with dissolve
    pause
    show player 10f
    player_name "Ух... Хорошо."
    show player 11f
    player_name "( Интересно, почему она хочет видеть меня в своем кабинете? )"

    return

label science_classroom_okita_has_glasses_int_fail:
    scene location_school_science_cutscene05
    with fade
    show text "Поэтому я принялся за работу." at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_cutscene05b
    with fade
    show text "[int_warn]Эта штука должна была курить?" at Position(xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    scene location_school_science_closeup
    show player 16 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Нет, он абсолютно не должен курить!"
    show player 12
    show okita 11b
    player_name "... Ну, простите!"
    player_name "Я говорил вам, я не способен работать над чем-то подобным!"
    show player 16
    show okita 11
    okita "Тебе лучше разобраться и побыстрее!"
    okita "... В противном случае ты можешь забыть об окончании моего класса."
    show player 12
    show okita 11b
    player_name "Фу, хорошо! Завтра попробую еще раз."
    show player 16
    show okita 9
    okita "Да, да. Просто вернись и закончи это поскорее."
    show okita 11
    okita "... и получше, сможешь!?"
    hide okita with dissolve
    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "*вздыхая*"
    show player 25
    player_name "{b}Думаю, я должен идти домой и работать над своим интеллектом{/b}..."


    return

label science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Привет, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "{b}Мия{/b}!"
    player_name "Прости за вчерашнее."
    show player 12
    player_name "Дома все в порядке?"
    show player 5
    show mia 12
    mia "Вообще - то, я хотела поговорить об этом."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "Теперь мне запрещено проводить время с друзьями...и особенно с тобой."
    mia " Моя мама говорит, что я должна быть дома после школы и не говорить с тобой..."
    show mia 8
    show player 10
    player_name "...Но {b}Мия{/b} Я-"
    show player 11
    show mia 12
    mia "Мы не можем разговаривать, прости..."
    hide mia
    hide mial
    with dissolve
    show player 24
    player_name "Я не хотел втягивать тебя в неприятности..."
    hide player with dissolve
    return

label science_classroom_okita_has_faptic:
    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "У тебя получилось?"
    show player 506 with dissolve
    show okita 4
    player_name "Вот, Мисс Окита."

    show player 505
    show okita 3
    okita "Хм, что-то не так..."
    show okita 5
    okita "Это то, что {b}Джун{/b} дала тебе?"
    show okita 4
    show player 10 with dissolve
    player_name "Эээ, да мэм."
    show player 11
    show okita 10b at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "..."
    show okita 5 at right with dissolve
    okita "Возможно, это просто мое воображение."
    player_name "..."
    show okita 4
    okita "Хорошо, останься после уроков и мы начнем с пояса."
    show player 10
    show okita 5
    player_name "Хорошо."




    scene location_school_science_closeup
    show player 1 at left
    show okita 3 at right
    with dissolve
    okita "Хорошо, {b}[firstname]{/b}. Следуй за инструкцией."
    show okita 5
    okita "... И постарайся не облажаться."
    show player 25
    show okita 4
    player_name "*глоток* Да, мэм."

    return

label science_classroom_okita_has_faptic_try_again:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    player_name "Хорошо, {b}Мисс Окита{/b}. Думаю, на этот раз у меня получилось лучше."
    show player 1
    show okita 9
    okita "Ты не можешь сделать ничего хуже."
    show player 16
    show okita 4
    player_name "..."
    show player 12
    player_name "Я заставлю их работать на этот раз, я знаю это!"

    show player 16
    show okita 5
    okita "Ну, придется подождать до окончания занятий. Сядь, {b}[firstname]{/b}."

    show player 2
    show okita 4
    player_name "Я готов, давайте сделаем это!"
    show player 1
    show okita 5
    okita "Конечно."
    return

label science_classroom_okita_has_faptic_int_pass:

    scene location_school_science_closeup
    show player 550 at left
    show okita 4 at right
    with dissolve
    player_name "Вот и все! У меня получилось!"
    show player 549
    show okita 5
    okita "Посмотрим."
    show player 1
    show okita 23
    with dissolve
    pause
    show okita 22
    okita "Хмм, да... Вроде все правильно."
    show okita 23
    pause
    show okita 22
    okita "Давайте направимся в мой офис для следующей части, [firstname]."
    okita "Тестирование потребует немного конфиденциальности..."
    show player 10
    show okita 23
    player_name "... конфиденциальности?"
    hide okita with dissolve
    show player 11
    pause
    show player 10
    player_name "Интересно, что она имела в виду?"
    return

label science_classroom_okita_has_faptic_int_fail:
    scene location_school_science_closeup
    show player 11 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Серьезно, опять?!"
    show player 10
    show okita 11b
    player_name "Простите, я не знаю, что ... "
    show player 11
    show okita 11
    okita "Грр... Ну, тебе лучше разобраться с этим!"
    okita "Мне нужно, чтобы эта штука работала!"
    okita "... В противном случае вы можете забыть о прохождении моего класса."
    show player 12
    show okita 11b
    player_name "Фу, хорошо! Завтра попробую еще раз."
    show player 16
    show okita 9
    okita "Да, да. Просто вернись и закончи это поскорее."
    show okita 11
    okita "... и получше, сможешь!?"
    hide okita

    show player 24 at Position(xpos=0.35, ypos=1.0)
    show playerl 1 zorder 1 at Position(xpos=0.502, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.52, ypos=0.3475)
    with dissolve
    player_name "{b}Я должен вернуться домой и поработать над своим интеллектом{/b} еще."

    return

label button_okita_tinkering_belt:
    scene location_school_science_closeup
    show player 2 at left
    show okita 4 at right
    with dissolve
    player_name "У тебя есть прогресс с поясом?"
    show player 1
    show okita 5
    okita "Пока нет, я все еще работаю над ним..."
    show player 1
    show okita 4
    player_name "Хорошо, я думаю, я свяжусь с тобой завтра."
    return

label button_okita_tinkered_belt:
    $ persistent.cookie_jar["Okita"]["gallery"]["03_unlocked"] = True
    scene location_school_science_closeup
    show player 2 at left
    show okita 1 at right
    with dissolve
    player_name "У тебя есть прогресс с поясом?"
    show player 1
    show okita 2
    okita "Я сузила проблему до нескольких вариантов. Принеси мне пульт с моего стола, и я покажу тебе."
    show player 2
    show okita 1
    player_name "Конечно."
    hide player with dissolve
    pause
    pause
    show player 536 at left with dissolve
    pause
    show player 537
    player_name "Хорошо, что сейчас-"
    show player 536
    smi "Tori!!!" with hpunch
    smi "Где ты, надоедливая маленькая всезнайка?!"
    show okita 3
    okita "О блин..."
    show okita 5
    okita "Иди сядь, {b}[firstname]{/b}.Я должна поговорить с ней."
    show okita 11
    okita "И спрячь этот пульт!"
    show player 2 with dissolve
    show okita 11b
    player_name "Хорошо, {b}Мисс Окита{/b}!"


    scene location_school_science_cutscene06
    with fade
    show text "Боюсь, любопытство взяло надо мной верх..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Но в свою защиту скажу." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_science_cutscene07
    with fade
    show text "Я не знал, что она была одета в ремень прямо тогда и там!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "... Бедная, {b}Мисс Окита{/b}." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_science_closeup
    show okita 11bf zorder 1 at Position(xpos=0.28, ypos=1.0)
    show principal 28 zorder 2 at right
    with dissolve
    smi "Я знаю, что ты снова работала над этими дурацкими устройствами за моей спиной!"
    show okita 9f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Я понятия не имею, о чем ты говоришь..."
    show okita 11bf
    show principal 2
    smi "НЕ ВРИ МНЕ, {b}ТОРИ{/b}!" with hpunch
    show principal 28 at right with dissolve
    smi "Твой кабинет снова не заперт и кто-то рылся в моих ящиках!"
    smi "Я знаю, что тебе помогли, и я хочу знать, кто это был!"
    show okita 11f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "У тебя есть до-"
    show okita 76f at Position(xpos=0.32, ypos=1.0) with dissolve
    okita "*ох*" with hpunch
    show okita 77f at Position(xpos=0.28, ypos=1.0) with dissolve
    pause
    show okita 80f
    pause
    show okita 77f

    okita "У тебя есть..."
    show okita 78f
    smi "..."
    show principal 27
    smi "Есть что?!"
    smi "... Что за звук?!"
    show okita 79f
    show principal 29
    okita "Ахх..."
    show okita 77f
    okita "У тебя есть... доказательства?"
    show principal 27
    show okita 78f
    smi "Пока нет!"
    show principal 28 at right with dissolve
    smi "Но если есть что-то, что можно найти, тебе лучше поверить, что я найду это!"
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Ммммм."
    show okita 79f

    okita "Ооооохххх, Аааааххх..."
    show okita 78f
    show principal 27
    smi "Что, черт возьми, с тобой происходит?!"
    smi "Ты ведешь себя еще более странно, чем обычно..."
    show principal 29
    okita "Хмм?"
    show okita 77f
    okita "Нет, ничего..."
    show okita 79f
    okita "... ничего..."
    okita "... я в порядке."
    show okita 81f
    okita "Оооох, вау!!!"
    show okita 78f
    show principal 28 at right with dissolve
    smi "Должна ли я напоминать тебе, что никто другой не нанял бы твою высокомерную задницу!?"
    smi "Это ваша последняя остановка, {b}Тори{/b}!"
    smi "После этого вы будете работать в окне быстрого питания с минимальной заработной платой!"
    smi "Есть ли у нас понимание здесь!?"
    show okita 79f
    show principal 29 at Position(xpos=0.95, ypos=1.0) with dissolve
    okita "Даааа!! Даааааааа!!!"
    show okita 81f
    okita "АААХХХХХ!!!"
    okita "ДДДАААААААА!!!!"
    show okita 81f at Position(xpos=0.3, ypos=1.25)
    okita "Ооооххх..."
    show okita 79f at Position(xpos=0.32, ypos=1.35)

    smi "( !!! )" with hpunch
    show okita 78f
    show principal 27
    smi "Что с тобой сегодня?!"
    show okita 77f
    show principal 29
    okita "Ааахх, ааааххх..."
    okita "Ничего... Я только..."
    show okita 78f
    pause
    show okita 77f
    okita "Ааахх, ааааххх..."
    okita "Я только... Не чувствую....так хорошо..."
    okita "Надо... прилечь...."
    show okita 78f
    show principal 27
    smi "Господи, {b}Тори{/b}."

    smi "Кто нибудь подойдите и помогите {b}Мисс Окита{/b} пройти в ее кабинет!"
    show player 10 zorder 0 at left
    show principal 29
    player_name "Я-Я помогу."
    show player 11
    player_name "..."
    show principal 27
    smi "Ну?! Не стой! Иди!"
    hide player
    hide okita
    show principal 29
    show okita 81c at Position(xpos=0.35, ypos=1.0)
    with dissolve
    pause
    show okita 81b at Position(xpos=0.15, ypos=1.0)

    okita "Ооооо, это слишком..."
    okita "Я кончаю..."
    hide okita
    hide principal
    show principal 29
    with dissolve
    okita "Я КОНЧАЮ!"
    show principal 27
    smi "Я заменю тебя на сегодня."
    smi "Наслаждайся, пока есть время, {b}Тори{/b}! Я перекодирую замок к концу недели!"
    smi "Это твое последнее предупреждение, и я серьезно!"



    scene location_school_office4_closeup_day
    show okita 81b at Position(xpos=0.55, ypos=1.0)
    with dissolve
    okita "Ааахх!!! Даааа!!"
    okita "О, Я кончаю..."
    show okita 81c
    player_name "Что с вами?"
    show okita 81b
    okita "Пульт!!"

    okita "ООООООХХХХХХ!!!"
    show okita 81c
    player_name "А?"
    hide okita
    show player 11 zorder 1 at Position(xpos=0.25, ypos=1.0)
    show okita 81 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    okita "Выключи! Выключи!"
    show player 10
    show okita 78
    player_name "Выключить?"
    show player 11
    show okita 79
    okita "ПОЯС! ВЫКЛЮЧИ!"
    show player 10
    show okita 78
    player_name "Ты хочешь сказать, что носишь его сейчас?!"
    show player 11
    show okita 79
    okita "ДА! ВЫКЛЮЧИ, ЧЕРТ ПОБЕРИ! ПОЖАЛУЙСТА!!!"
    show player 29 with dissolve
    show okita 78
    player_name "Я, эээ .. оставил пульт внизу в халате."
    show player 3
    show okita 81
    okita "OOO! Я БОЛЬШЕ НЕ ВЫДЕРЖУ!"
    show okita 81e with dissolve
    okita "ПОМОГИ МНЕ СНЯТЬ ЕГО!"
    show okita 81d
    show player 10 with dissolve
    player_name "... Ты этого хочешь?"
    show okita 81e
    okita "СНИМИ ЕГО СЕЙЧАС ЖЕ!"
    show player 520 at Position(xpos=0.4, ypos=1.0)
    show okita 81d
    player_name "Ах, конечно, мэм!"
    player_name "..."
    player_name "Вау, эта штука вибрирует как безумная!"
    show okita 81e
    okita "ПОТОРОПИСЬ!!"
    show okita 81d
    pause
    show okita 81g
    show player 550 at Position(xpos=0.25, ypos=1.0) with dissolve
    player_name "Получилось!"
    show player 549
    okita "Ааахх... Ааахх..."
    okita "Это было... Я никогда..."
    okita "Вау!"
    okita "Я вся мокрая!"
    show player 550
    show okita 83 at Position(xpos=0.62, ypos=1.0) with dissolve
    player_name "Да, ремень тоже весь мокрый..."
    show player 549
    show okita 82
    okita "Ааахх... Ааахх..."
    okita "Я не чувствую ног..."
    show okita 84
    okita "Ааахх... Ааахх..."
    okita "Мне нужно прилечь."
    show okita 83
    show player 10 at Position(xpos=0.22, ypos=1.0) with dissolve
    player_name "Я могу чем-то еще помочь?"
    show okita 84
    show player 11
    okita "А?"
    okita "О, нет."
    show okita 83
    pause
    show okita 82
    okita "Я в поряде. РЕАЛЬНО ХОРОШО..."
    show okita 84
    okita "Просто возвращайся в класс. Мы можем поговорить позже."
    show player 10
    show okita 83
    player_name "Конечно."
    return

label science_classroom_dewitt_science_adhesive:
    scene school_science_c02
    show xtra 36f
    show xtra_lab_clip 46 at Position (xoffset=0,yoffset=0)
    show xtra_sticky_paper 46b at Position (xoffset=0,yoffset=0)
    show kevin labcoat 2 at right
    with dissolve
    show player 14 zorder 1 at Position (xoffset=-84)
    with dissolve
    player_name "Как продвигаются дела, {b}Кэвин{/b}?"
    show player 13 at Position (xoffset=-84)
    show kevin labcoat 3 with dissolve
    kev "Не беспокойся, братан! Я получил его прямо здесь."
    hide xtra_sticky_paper
    show kevin labcoat 4
    with dissolve
    show player 108f at Position (xoffset=-84)
    player_name "... И это все?"
    show player 111f at Position (xoffset=-84)
    player_name "Дай мне взглянуть!"
    show player 617
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "Ух ты! Братан, будь осторожен с этим!"
    show kevin 33 at Position (xoffset=-6)
    show player 619
    player_name "Угг!"
    show player 620 with dissolve
    pause
    show player 621 at Position (xpos=550) with dissolve
    player_name "!!!" with hpunch
    show kevin 33b at Position (xoffset=-6)
    kev "!!!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "... Братан. Какого хрена!"
    show kevin 33 at Position (xoffset=-6)
    show player 621 with dissolve
    player_name "Чувак... Прилипло!"
    show player 622 with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Пфф, вот дерьмо?!"
    kev "Я сказал тебе быть осторожным!"
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "... Что же нам теперь делать?!"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev "Я должен найти растворитель."
    show kevin 24b at Position (xoffset=-6)
    show player 621e with dissolve
    player_name "Сколько времени это займет?"
    show player 621c with dissolve
    show kevin 24 at Position (xoffset=-6)
    kev " Не знаю, она где-то здесь держит бутылку!"
    kev "Было бы намного легче, если бы твоя рука не прилипала к моей гребаной бумаге, Братан!"
    hide kevinl
    show kevin labcoat 2
    show player 621d
    with dissolve
    player_name "{b}*вздох*{/b}"
    player_name "Блин..."
    show player 621c with dissolve
    show eve 2bf zorder 0 at Position (xoffset=-340) with dissolve
    eve "!!!"
    show eve 6f at Position (xoffset=-340)
    eve "Я вас отвлекаю от чего-то? Потому что я могу вернуться позже, если вам нужно побыть наедине."
    show eve 5f at Position (xoffset=-340)
    show player 621f with dissolve
    player_name "Ха... Ха. Ты уморительная, ты знаешь это?"
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "Как вам это удалось?!"
    show eve 5f at Position (xoffset=-340)
    show player 621d with dissolve
    show kevin labcoat 6 with dissolve
    player_name "Я бы предпочел не говорить об этом..."
    show player 621c with dissolve
    show eve 6f at Position (xoffset=-340)
    eve "Хахаха! Могу поспорить, что нет!"
    show eve 5f at Position (xoffset=-340)
    show kevin labcoat 7 with dissolve
    kev "Хорошо, я достал!"
    show player 621e with dissolve
    player_name "Класс."
    show player 621b
    show kevin labcoat 8 with dissolve
    show player 621e
    player_name "Ну и что сейчас?"
    show player 621c
    show kevinl 1f at Position (xoffset=350)
    show kevin 24 at Position (xoffset=-6)
    with dissolve
    kev "... Ух. Потяни?"
    show player 622 with dissolve
    show kevin 33 at Position (xoffset=-6)
    pause
    show player 623 at Position (xoffset=-200) with dissolve
    show kevin 23 at Position (xoffset=-6)
    player_name "!!!"
    show eve 26 at Position (xoffset=-365) with hpunch
    eve "!!!"
    eve "... Это произошло не просто так..."
    show player 625 at Position (xoffset=-205)
    player_name "..."
    show player 624 at Position (xoffset=-205)
    player_name "... Черт."
    show player 625 at Position (xoffset=-205)
    show kevin 32 at Position (xoffset=-6)
    kev "Хахахаха!"
    scene black with fade

    show popup_item_sticky1 at truecenter with dissolve
    pause
    hide popup_item_sticky1 with dissolve

    scene expression game.timer.image("outside_school{}") with fade
    show eve 2b at right
    show kevin 23 at Position (xpos=600)
    show player 13 at left
    with dissolve
    eve "Вы действительно собираетесь проникнуть в {b}кабинет директрисы Смит{/b} сегодня вечером?!"
    show eve 1
    show player 10
    player_name "Ты не идешь?"
    show player 5
    show eve 6b
    eve "Ни за что. Извени, {b}[firstname]{/b}."
    show eve 2b
    eve "Не поймите меня неправильно... Мне нравится немного озорства, но это слишком рискованно!"
    show eve 1
    show player 14
    player_name "Все в порядке, {b}Ева{/b}. {b}Кэвин{/b} и я сделаем все."
    show player 13
    show kevin 33
    kev "..."
    show player 10
    player_name "{b}Кэвин{/b}?"
    show player 5
    show kevin 24
    kev "... Вообще-то, я думал, что эту часть я тоже пропущу."
    show kevin 24b
    show player 12
    player_name "Серьезно?"
    player_name "Что?! После всех твоих громких разговоров?"
    show player 5
    show kevin 22 with dissolve
    kev "... Извини, {b}[firstname]{/b}."
    show kevin 24b with dissolve
    show player 37 with dissolve
    player_name "..."
    show eve 2b
    eve "Что ты собираешь делать?"
    show eve 1
    show player 12 with dissolve
    player_name "Я все еще собираюсь пройти через это."
    player_name "Я не могу позволить {b}Директрисе Смит{/b} зарубить {b}Шоу талантов{/b}!"
    show player 5
    show eve 2b
    eve "... Ты действительно собираешься сделать это в одиночку?"
    show eve 1
    show player 10
    player_name "Похоже, да."
    show player 5
    show kevin 33
    show eve 9f
    eve "..."
    show player 34
    kev "..."
    show player 35
    player_name "Я не знаю, может {b}Эрик{/b} поможет мне?"
    show player 5
    show kevin 24b
    show eve 2b
    eve "... {b}Эрик{/b}?"
    eve "Хех, лучше в одиночку!"
    show eve 1
    show player 12
    player_name "Эй, не говори так... {b}Эрик{/b} хороший парень!"
    player_name "... Он бы не бросил меня в последнюю минуту."
    show player 5
    show eve 9f
    show kevin 33
    eve "..."
    kev "..."
    show eve 2b
    eve "Ты прав. У меня нет места для разговора, {b}[firstname]{/b}."
    show eve 1
    show kevin 24
    kev "Да, только..."
    kev "... Будь осторожен, хорошо?"
    show kevin 24b
    show player 12
    player_name "Постараюсь."
    hide eve
    hide kevin
    with dissolve
    pause
    show player 10
    player_name "... Я должен спросить {b}Эрика{/b}, поможет ли он мне {b}проникнуть в школу сегодня вечером{/b}."
    player_name "В одиночку идти опасно..."
    hide player with dissolve
    return

label science_classroom_microscope_dialogue:
    scene expression "backgrounds/location_school_science_flies_day.jpg"
    player_name "Что за-" with hpunch
    pause
    player_name "Фу..."
    player_name "Теперь я действительно не хочу, чтобы муха приземлилась на меня..."
    $ A_flies.unlock()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
