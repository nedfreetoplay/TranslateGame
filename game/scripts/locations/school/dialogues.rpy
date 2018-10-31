label school_erik_intro_started:
    scene outside_school_b
    show duo 6 at left with dissolve
    show mia 1 at right with dissolve
    player_name "Эй, {b}Мия{/b}!"
    show duo 1 at left
    show mia 4 at right
    mia "Эй, {b}[firstname]{/b}! Рада снова видеть тебя!"
    mia "Привет, {b}Эрик{/b}! Как выходные?"
    show duo 10 at left
    show mia 1 at right
    eri "Ну... Дома был."
    show duo 1 at left
    show mia 3 at right
    mia "Классно! Я тоже иногда люблю побыть с собой наедине."
    show mia 4 at right
    mia "А ты, {b}[firstname]{/b}? Чем занимался?"
    show mia 2 at right
    show duo 9 at left
    player_name "Ладно, я не знаю, слышала ты или нет, но мой {b}Отец{/b} умер. Я пытался смириться с этим и прийти в себя..."
    show mia 6 at right
    mia "А, точно. Мама же мне рассказывала..."
    show duo 15 at left
    mia "Я не хотела поднимать эту тему. Жаль, что тебе пришлось пройти через всё это. Я очень рада, что ты наконец-то вернулся!"
    show mia 2 at right
    player_name "Спасибо, со мной всё нормально, не волнуйся."
    show mia 4 at right
    mia "Слушай, я искала кого-нибудь, кто может {b}помочь мне подготовиться к итоговым экзаменам{/b}, так что..."
    show duo 7 at left
    mia "... Если тебе это интересно, дай мне знак!"
    show duo 8 at left
    show mia 1 at right
    player_name "Ох, конечно... Наверное."
    player_name "Где бы ты хотела приступить к занятиями? В библиотеке?"
    show duo 1
    show mia 6
    mia "Ну, для начала мне стоит спросить это у своих родителей."
    mia "Они могут быть против этого."
    mia "Мне нельзя долго задержиться после школы или встречаться с друзьями за пределами своего дома."
    show mia 2
    show duo 9
    player_name "Серьёзно? Это отстой."
    show duo 7
    show mia 3
    mia "Да... хи-хи."
    show duo 7
    show mia 6
    mia "В любом случае, будет гораздо проще, если ты сам придёшь ко мне домой."
    show mia 3 at right
    mia "Ты знаешь, где я живу, так что заскакивай, когда сможешь!"
    show duo 7 at left
    show mia 4 at right
    mia "Я лучше пойду. Не хочу пропускать {b}урок химии{/b}."
    show duo 1
    mia "{b}Профессор Окита{/b} сказала, что сегодняшний {b}лабораторный эксперимент{/b} будет настоящим испытанием."
    mia "Это означает, что на его выполнение может уйти весь час."
    show mia 1
    show duo 10
    eri "Ох. Не напоминай мне..."
    show duo 1
    show mia 4
    mia "Увидимся позже, мальчики!"
    hide mia with dissolve
    hide duo with dissolve
    return

label school_roxxy_shower_event:
    scene school
    show jersey 10 with dissolve
    player_name "( Ух, дышать как сложно-то... )"
    player_name "( Какая же жара на улице... )"
    show jersey 33 at Position(xoffset=22) with fastdissolve
    player_name "( ... И я весь ВСПОТЕЛ! )"
    player_name "( Мне стоит {b}принять душ{/b}, прежде чем я пойду на другой урок. )"
    return

label school_roxxy_intense_gymercise:
    scene school
    show erik 28 at right
    show player 1 at left
    with dissolve
    eri "Эй, {b}[firstname]{/b}."
    show erik 27
    show player 14
    player_name "Эй, {b}Эрик{/b}."
    player_name "Почему ты одет в..."
    show erik 28
    show player 11
    eri "Я из-за этого сюда и пришёл! {b}Физручка Бриджет{/b} ищет тебя!"
    eri "Сейчас же физкультура!"
    show erik 27
    show player 10
    player_name "Чёрт, я же уже столько её занятий пропустил. Она прибьёт меня!"
    show erik 28
    show player 5
    eri "Тебе следует поторопиться!"
    show erik 27
    show player 10
    player_name "Спасибо, что предупредил!"
    show erik 29
    show player 11
    eri "Без проблем, чувак!"
    show erik 27
    hide player with dissolve
    pause
    show erik 28
    eri "Удачи!"
    hide erik with dissolve
    return

label school_bissette_challenge:
    scene school
    show player 34 with dissolve
    player_name "( Мне стоит {b}поговорить с мисс Биссет по поводу личных  занятий с ней{/b}. )"
    player_name "( Я вообще ничего не понимаю на её уроках... )"
    player_name "( ...Думаю, что я отстал от программы слишком далеко, чтобы самостоятельно всё навёрстывать... )"
    player_name "( Немного дополнительной помощи ещё никому не навредило... )"
    show player 4 at Position (xoffset=5) with dissolve
    player_name "( ...И я смогу получить ту награду, если успешно пройду финальный опрос!  )"
    hide player with dissolve
    return

label school_mia_glasses_favor:
    scene school
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Эй, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Эй, {b}Мия{/b}."
    show player 12
    player_name "Как дела у твоего отца?"
    show player 5
    show mia 10
    mia "Да нормально всё. Вроде как..."
    show mia 51 with dissolve
    mia "Моя мама убиралась у него в офисе прошлой ночью и нашла эти старые очки..."
    show mia 7
    show player 446
    with dissolve
    pause
    show player 448
    player_name "Прикольно, это же Авиаторы."
    player_name "Он всё ещё носит их?"
    show player 13
    show mia 50
    with dissolve
    mia "Раньше носил, но это было очень давно."
    mia "Я думала, может быть, он снова захотел их носить."
    show mia 50b
    show player 14
    player_name "Классно."
    show player 13
    show mia 50
    mia "А вообще, я думала, что, может быть, ты занесёшь их к нему на работу?"
    mia "Я кое-куда ухожу скоро, так что у меня не будет времени, чтобы сделать это самой."
    show mia 50b
    show player 10
    player_name "Стой, ты хочешь, чтобы {b}я{/b} их отнёс??"
    show player 5
    show mia 50
    mia "А почему бы и нет?"
    mia "Кажется, вы оба хорошо ладите друг с другом."
    mia "...И он точно будет рад увидеть их снова, я уверена!"
    mia "После того, как ты с ним поговорил, его настроение сразу же поднялось!"
    show mia 50b
    show player 12
    player_name "Эмм... Ладно, думаю, что я смогу отнести эти очки к нему на работу."
    show player 447
    show mia 10
    with dissolve
    mia "Спасибо, это так мило, что ты делаешь это ради меня."
    show mia 7
    show player 448
    player_name "Почему бы и нет, я не против навестить его!"
    show player 447
    show mia 10
    mia "Тогда увидимся позже!"
    show mia 7
    show player 448
    player_name "Пока."
    show unlock54 at truecenter with dissolve
    pause
    hide unlock54 with dissolve
    hide player
    hide mia
    with dissolve
    return

label school_erik_bullying_2_started:
    scene school
    show dexter 9 at right with dissolve
    eri "Ух!!!"
    eri "Отпусти... меня... {b}Декстер!{/b}!"
    dex "Неа, жиртрест!"
    dex "Ты мне так и не отдал домашку!"
    dex "Я думаю, что ты так ничего и не понял!"
    eri "Я же сказал тебе! Я сдал её учителю! У меня её больше нету, понимаешь?"
    dex "Ну ладно, отдашь мне что-нибудь другое взамен неё."
    dex "Сколько у тебя бабла с собой?"
    eri "В смысле?!"
    dex "Я повторю ещё раз: сколько денег ты мне добровольно отдашь, пока я не впечатал твоё табло в шкафчик?"
    eri "!!!"
    eri "{b}Декстер{/b}! Я... Я..."
    show player 15 at left with dissolve
    show dexter 10
    player_name "ЭЙ!!!"
    player_name "Отпусти его, {b}Декстер{/b}!"
    show player 16
    show dexter 9
    dex "Хорошо, если это не твой дружок-неудачник."
    show dexter 10
    show player 15
    player_name "{b}Декстер{/b}, хватит приставать к {b}Эрику?{/b}."
    show player 16
    show dexter 9
    dex "Зачем же? Хочешь занять его место?"
    player_name "..."
    show dexter 12 with dissolve
    dex "Давай, {b}[firstname]{/b}."
    show dexter 13
    dex "Посмотрим, что ты можешь!"
    return

label school_erik_bullying_2_started_dex_pass:
    show dexter 14
    show player 387 with dissolve
    player_name "Я не боюсь тебя, {b}Декстер{/b}!"
    show player 388
    show dexter 15
    dex "Естественно, ты должен бояться на меня... А ЭТОГО!"
    hide player
    hide dexter
    show dexter 16 at left
    with dissolve
    pause
    show dexter 17 at right with dissolve
    player_name "Аааай!!!"
    hide dexter
    show player 390 at left
    show dexter 18 at right
    with dissolve
    dex "Агххрр!"
    dex "Ты... Мелкий... Засранец..."
    show dexter 15 with dissolve
    show player 389
    player_name "!!!"
    show player 391
    show dexter 19 with hpunch
    pause
    hide player
    show dexter 20 at left
    with dissolve
    dex "Помедленней, а?"
    dex "Сейчас я тебе покажу..."
    hide player
    with dissolve

    scene school_fight_cs1 with fade
    show text "Даже после моих недавних тренировок в качалке,\n{b}Декстер{/b} всё ещё слишком силён для меня...\n...но теперь я узнал, как можно ему навредить!" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene school_fight_cs2 with fade
    show text "...И, наконец, всё потемнело." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene black with fade
    pause

    scene school with None
    show mia 24 at left
    show dexter 21 at Position (xpos=713)
    with dissolve
    mia "{b}[firstname]{/b}!! Как ты себя чувствуешь?!"
    show mia 23
    pause
    show mia 28 with dissolve
    mia "Это же ты во всём виноват, {b}Декстер{/b}?"
    mia "Ты его сильно поранил!"
    show mia 27
    show dexter 22
    dex "Занимайтесь своим делом!"
    dex "Он сам напросился!!"
    show dexter 23
    show roxxy 30 at right with dissolve
    rox "{b}Декстер{/b}?"
    show roxxy 29
    show dexter 24
    dex "Что?!"
    show dexter 23
    show mia 23 with dissolve
    show roxxy 27
    rox "..."
    show roxxy 28
    rox "Эмм... {b}Декстер{/b}, что происходит?"
    rox "Это ты его так?"
    show roxxy 29
    show mia 27 with dissolve
    show dexter 24
    dex "Ничего не происходит!!"
    show dexter 12
    dex "Я просто провёл с этом засранцем воспитательную беседу!"
    show dexter 23
    show roxxy 30
    rox "Серьёзно? Это ты сделал? В коридоре?"
    show roxxy 29
    show dexter 24
    dex "Заткнись, {b}Рокси{/b}."
    dex "Давай, пошли отсюда!"
    show roxxy 27
    dex "У меня есть дела поважнее, чем смотреть на горстку идиотов вокруг!"
    hide dexter
    hide roxxy
    with dissolve
    hide mia
    show eve 9 at Position (xpos=75)
    show mia 23 at left
    show judith 40 at Position (xpos=600)
    show erik 50 at Position (xpos=900)
    with dissolve
    jud "Ох, чёрт возьми! Что здесь произошло?"
    show judith 41
    show eve 10
    eve "{b}Декстер{/b} такой придурок, что слов нет."
    eve "В этот раз он зашёл слишком далеко."
    show eve 9
    hide erik
    show teacher 15 at Position (xpos=700)
    show erik 50 at Position (xpos=900)
    with dissolve
    bis "!!!"
    bis "Что здесь случилось?"
    bis "{b}[firstname]{/b}... Что с ним?!"
    show teacher 14
    show mia 26 with dissolve
    mia "Он подрался с {b}Декстером{/b} и {b}Декстер{/b} ударил его об эти шкафчики!"
    mia "Он всё ещё дышит, я думаю, что с ним всё нормально."
    show mia 25
    bis "..."
    show teacher 15
    bis "Нам надо вызвать скорую помощь!"
    $ playSound()
    scene black with fade
    hide mia
    hide eve
    hide teacher
    hide erik
    hide judith
    return

label school_erik_bullying_2_started_dex_fail:
    show dexter 14 at right with dissolve
    show player 6 at left with dissolve
    player_name "[dex_warn]Я не хочу драться с тобой, {b}Декстер{/b}!"
    show player 23 with dissolve
    player_name "[dex_warn]Я просто хочу, чтобы ты оставил {b}Эрика{/b} в покое..."
    show player 22
    show dexter 15
    dex "Ты что, серьёзно?"
    show dexter 14
    show player 10
    player_name "[dex_warn]Я всё сказал..."
    show player 22
    show dexter 12 with dissolve
    dex "Хах!"
    dex "Слабый и жалкий..."
    dex "...Прям как твой папка!"
    hide dexter
    with dissolve
    show player 24
    player_name "[dex_warn]..."
    hide player
    with dissolve
    return

label school_roxxy_intro_started:
    scene school with fade
    show duo 1 at left
    show dexter 1 at Position (xpos=700)
    show roxxy 4 at right
    with dissolve
    rox "... И прикинь, {b}Бекка{/b} выкинула это в туалет!"
    show dexter 3
    dex "Ахахахахаха!"
    show roxxy 3d
    rox "..."
    show roxxy 3c
    rox "... Эмм... на что уставились, лузеры?"
    show dexter 2 at Position (xoffset=-2)
    show roxxy 3b
    show duo 2 at left
    eri "Я вижу перед собой общий результат IQ в два балла!"
    show duo 3 at left
    player_name "Хах!!"
    show roxxy 31
    rox "В смысле?!"
    show roxxy 3b
    show dexter 8 at Position (xoffset=-2)
    dex "... Хах, я чего-то не понимаю?"
    show dexter 2 at Position (xoffset=-2)
    show duo 7 at left
    show roxxy 30
    rox "Он назвал нас тупицами!"
    show roxxy 29
    show dexter 8 at Position (xoffset=-2)
    dex "Серьёзно?!"
    show dexter 6 at Position (xoffset=-119) with dissolve
    dex "Слышь, ты назвал нас тупицами?!"
    show dexter 5 at Position (xoffset=-119)
    show duo 10
    show roxxy 3b
    eri "Я... Не-ет, ни-икак не-ет... Я имел ввиду, наверное..."
    show duo 11
    show dexter 4 at Position (xoffset=-20) with dissolve
    dex "Я тебе лицо расквашу, кусок говна!"
    show duo 4
    show dexter 2 at Position (xoffset=-2) with dissolve
    show roxxy 3
    rox "...а {b}ТЫ{/b} над чем уссыкаешься, а?!"
    show roxxy 2
    rox "Разве твой отец-неудачник не прикончил себя, или что там было?"
    show roxxy 1g
    show duo 9
    eri "..."
    show player 15 at left
    player_name "У меня хоть {b}БЫЛ{/b} отец, с которым я рос..."
    player_name "... И я не живу в {b}ТРЕЙЛЕРЕ{/b}, как некоторые!!"
    show player 16
    show roxxy 3c
    rox "!!!" with hpunch
    show roxxy 3
    rox "... Тебе конец!"
    rox "Декстер, задай им жару!!!"
    show roxxy 3d
    show player 11
    show dexter 8 at Position (xoffset=-2)
    dex "Спокойнее, {b}Рокси{/b}. {b}Директриса Смит{/b} идёт!!"
    dex "Если меня ещё раз спалят за дракой, {b}физручка Бриджет{/b} выпнет меня из команды!"
    hide dexter with dissolve
    show roxxy 3c
    show player 16
    rox "Пффф, шикарно..."
    show roxxy 3
    rox "... Это ещё не конец!"
    rox "Я разберусь с тобой позже, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    pause
    hide player
    show duo 1 at left
    show principal 5 at right with dissolve
    smi "Вы двое! А ну бегом сюда, {b}СЕЙЧАС ЖЕ{/b}!!!"
    show duo 11 at left
    smi "Что вы делаете в коридоре в этом время?!"
    show duo 12 at left
    show principal 3 at right
    eri "Извините, {b}миссис Смит{/b}! Мы просто..."
    show duo 11 at left
    show principal 4 at right
    smi "А, {b}[firstname]{/b}! Смотрю, ты наконец-то вернулся..."
    show duo 6
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Д-да, м-ээм..."
    show duo 7
    show principal 27
    smi "Как раз вовремя! Ты мне можешь сказать, как твои оценки умудрились так резко испортиться?"
    show duo 9
    show principal 1
    player_name "... А они испортились?"
    show duo 10
    eri "Это несправедливо!"
    eri "Вы что, не знаете, что его отец..."
    show duo 11
    show principal 2
    smi "Хватит, {b}Эрик{/b}!"
    show principal 4 at right
    smi "Я предлагаю тебе метнуться в класс, пока я тебя не отчислила!"
    show duo 10
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    eri "..."
    show duo 12
    show principal 4 at right
    smi "... А что насчёт тебя, {b}[firstname]{/b}. Нам стоит обсудить с тобой твои подпортившиеся оценки!"
    smi "Жду тебя наверху, в своём офисе, ПРЯМО СЕЙЧАС!"
    show duo 9
    show principal 1 at Position(xpos=0.935, ypos=1.0)
    player_name "Хорошо, {b}миссис Смит{/b}."

    hide principal
    hide duo
    with dissolve
    show player 5 at left
    show erik 3b at right
    eri "Да она чистое зло, чувак."
    show player 2
    show erik 1
    player_name "Ага."
    show player 1
    show erik 5
    eri "Я серьёзно! Не директриса вовсе, а Злая Ледяная Королева из Шлюхкрафта!"
    show player 2
    show erik 1
    player_name "Ладно, {b}я лучше пойду к ней в кабинет{/b}, пока её настроение не ухудшилось."
    show player 1
    show erik 5
    eri "Удачи, чувак..."
    show player 2
    show erik 1
    player_name "... Спасибо."
    show player 1
    show erik 4
    eri "Ох, я почти забыл!"
    eri "{b}Я засунул тебе в шкафчик небольшой подарочек по случаю твоего возвращения в коллектив{/b}!"
    show player 2
    show erik 1
    player_name "Правда?"
    show player 1
    show erik 4
    eri "Рад твоему возвращению, дружище!"
    show player 2
    show erik 1
    player_name "Спасибо, {b}Эрик{/b}!"
    show player 34
    player_name "Хмм..."
    show player 10
    player_name "... Понимаешь, я забыл код от {b}своего шкафчика{/b}."
    show player 11
    show erik 5
    eri "Ты его не записал?"
    show player 10
    show erik 1
    player_name "Неа, но думаю, что следовало это сделать, ага?"
    show player 11
    show erik 5
    eri "Тебе стоит {b}поговорить с {b}миссис Смит{/b} по этому поводу{/b}."
    show player 10
    show erik 1
    player_name "Ох, думаю, что ты прав..."
    player_name "Увидимся позже, {b}Эрик{/b}."
    show player 11
    show erik 5
    eri "Ага, увидимся, {b}[firstname]{/b}."
    return

label school_hallway_dewitt_talent_show_ask_annie:
    scene school
    show player 4f with dissolve
    player_name "( Интересно, с кем мне стоит поговорить в первую очередь? )"
    show player 9f at left with dissolve
    pause
    pause
    show player 22 at left
    show annie 4 at right
    with hpunch
    ann "{b}[firstname]{/b}, не шатайся в коридоре!"
    show annie 1
    show player 12
    player_name "{b}Энни{/b}, я только что вошёл в коридор..."
    show player 5
    show annie 5
    ann "Не важно. Бегом на свои уроки, пока я на тебя докладную не написала!"
    show annie 6
    show player 12
    player_name "Ладно! Пффффф..."
    show player 10
    player_name "Ой, стой! Подожди секунду!"
    player_name "Тебе не доводилось играть на музыкальном инструменте? Или петь там, нет?"
    show player 5
    show annie 3
    ann "Доводилось. Тебе зачем?"
    show annie 1
    show player 10
    player_name "Отлично! Понимаешь, {b}мисс Девитт{/b} ищет людей для выступления на шоу талантов."
    show player 5
    show annie 5
    ann "Да, я наслышана об этом!"
    show annie 6
    player_name "..."
    show player 10
    player_name "Ну так, может быть поучаствуешь?"
    show player 5
    show annie 9
    ann "Пффф, никогда!"
    show annie 5
    ann "Ты должен знать, {b}директриса Смит{/b} добивается того, чтобы это шоу закрыли, верно?"
    show annie 6
    show player 12
    player_name "Да, я знаю."
    show player 5
    show annie 3
    ann "Так что я никак не могу участвовать в этом мероприятии!"
    show annie 1
    show player 12
    player_name "Ты не должна постоянно слушать {b}миссис Смит{/b}, {b}Энни{/b}."
    show player 5
    show annie 5
    ann "Я - глава дисциплинарного комитета, официальный дежурный по коридору, и {b}вторая рука{/b} миссис Смит!"
    show annie 3
    ann "Это мой названный долг подчиняться миссис Смит!"
    show annie 1
    show player 12
    player_name "Это не армия, {b}Энни{/b}..."
    show player 11
    show annie 7
    ann "МОЛЧАТЬ!"
    show annie 1
    show player 10
    player_name "Но..."
    show player 11
    show annie 5
    ann "{b}Директриса Смит{/b} хочет, чтобы это шоу закрылось, и её планы поставлены на реализацию!"
    show annie 6
    show player 12
    player_name "... Планы?"
    show player 5
    show annie 9
    ann "Гррр, уже лишнее сказанула!"
    show annie 1
    show player 11
    player_name "..."
    show annie 5
    ann "Предлагаю тебе забить на эту идею с шоу талантов. Оно не состоится, я тебя уверяю!"
    show annie 8
    ann "А теперь уйди с дороги и дай мне закончить дежурство!"
    hide annie with dissolve
    show player 12
    player_name "Бестолочь..."
    hide player with dissolve
    return

label school_dewitt_school_sneak_mission:
    scene expression game.timer.image("outside_school{}")
    show player 32f with dissolve
    player_name "( Да чёрт, где {b}Эрик{/b}? )"
    player_name "( Он уже должен был быть здесь... )"
    show player 31f
    show erik 5 at right with dissolve
    eri "{b}[firstname]{/b}?"
    show erik 52
    show player 10 at left with dissolve
    player_name "Вот ты где!"
    player_name "Ты чего так долго?"
    show player 5
    show erik 4
    eri "Прости, чувак, я тут рейдил Оркскую деревню... и немного потерял счёт времени..."
    show erik 1
    show player 12
    player_name "... А?"
    player_name "Так, стой. Эта штука нужна для видеоигр?!"
    show player 5
    show erik 5
    eri "... Ага."
    show erik 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Давай прост сосредоточимся на задании, {b}Эрик{/b}."
    show player 5 with dissolve
    show erik 5
    eri "Что представляет из себя это задание?"
    show erik 52
    show player 239_240 with dissolve
    pause
    show player 618 at Position (xoffset=35) with dissolve
    player_name "Мы проникнем в кабинет {b}миссис Смит{/b} и нальём на её кресло {b}немного клеевого раствора{/b}."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "И не это ли мы проворачивали в классе {b}мисс Окиты{/b} некоторое время назад?"
    show erik 52
    show player 618 at Position (xoffset=35)
    player_name "Ага. {b}Кевин{/b} сделал это для меня."
    show player 617 at Position (xoffset=35)
    show erik 5
    eri "Этот раствор крышесносный!"
    eri "... И ты хочешь разлить это на {b}кресло Миссис Смит{/b}?"
    eri "Она не прилипнет к нему?"
    show erik 52
    show player 17 with dissolve
    player_name "Имеено, мой дорогой друг!"
    show player 13
    show erik 3b
    eri "А, точно."
    show erik 3c
    pause
    show erik 3b
    eri "Ну, пошли что ли..."

    scene outside_school_night02a with dissolve
    show text "Школа была закрыта крепко-накрепко, но я решил поискать обходной путь.\nМожет быть, можно пролезть в здание через окно?" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    show outside_school_night02b with dissolve
    show text "{b}Эрик{/b} был не самым подходящим партнёром для скрытных операций, но я рад, что я полностью могу на него положиться.\nБез него я бы не смог сделать такое." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    pause 0.5

    scene outside_school_night02c with dissolve
    show text "Поскольку {b}Эрик{/b} помог мне с окном, мне стало казаться, что всё заметно попростело...\n... Кто знал, что дальше может пройзоийти что-то зловещее..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    scene black
    with dissolve
    pause 0.5

    scene school_night with dissolve
    player_name "!!!"
    player_name "Шшш, я что-то слышу..."

    scene cult_event 1
    with Dissolve(0.3)
    eri "..."
    eri "!!!"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Шшш!"
    player_name "Веди себя тихо!"
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 51 at right
    with dissolve
    pause
    show player 10
    player_name "Что за..."
    player_name "Кто это такие?"
    player_name "... И куда они идут?"
    show player 5
    show erik 53
    eri "Что-то мне это не нравится, {b}[firstname]{/b}!"
    eri "Надо валить отсюда!"
    show erik 52
    show player 10
    player_name "Успокойся, чувак."
    player_name "Они не знают, где мы."
    show player 5
    show erik 53
    eri "Как ты думаешь, что это за жуткие наряды?"
    show erik 52
    show player 10
    player_name "Без понятия."
    show player 92
    player_name "Думаю, что стоит проследить за ними."
    show player 90
    show erik 53
    eri "Ты свихнулся?"
    show erik 52
    show player 92
    player_name "Всё будет хорошо, {b}Эрик{/b}!"
    player_name "Просто оставайся позади меня и веди себя тихо."
    show player 90
    show erik 2 with dissolve
    eri "{b}*вздох*{/b}"
    show erik 3 with dissolve
    eri "... Хорошо."
    hide player
    hide erik
    with dissolve
    return

label school_dewitt_pre_talent_show_chat:
    scene school
    show kevin 23 at Position (xpos=600)
    show eve 6 at right
    with dissolve
    show player 13 at left with dissolve
    eve "Вот он где!"
    show eve 5
    show kevin 22 with dissolve
    kev "Наконец-то!"
    kev "Как всё прошло этой ночью?"
    show kevin 23 with dissolve
    show eve 2b
    eve "Мы начали волноваться, что тебя поймали... или что-то в этом роде."
    show eve 5
    show player 14
    player_name "Неа. Всё прошло гладко."
    player_name "Вы видели {b}миссис Смит{/b} и {b}Энни{/b} этим утром?"
    show player 13
    show kevin 9b
    kev "Пока нет."
    kev "Думаешь, что они правда залипли в её офисе?"
    show kevin 23
    show player 17
    player_name "Хочу надеяться, что да."
    show player 13
    show eve 6
    eve "Ахахах! Шикарно!"
    show eve 5
    show player 14
    player_name "Где {b}мисс Девитт{/b}?"
    show player 13
    show eve 6
    eve "Она в {b}актовом зале{/b} готовится к шоу."
    show eve 5
    show kevin 9b
    kev "Мы только что собирались ей помочь."
    show kevin 23
    show eve 6
    eve "Ага, почему бы тебе не пойти с нами?"
    show eve 5
    show player 14
    player_name "Хмм, я лучше проверю {b}кабинет миссис Смит{/b} для начала."
    player_name "Я хочу убедиться, что никаких сюрпризов не будет."
    show player 13
    show kevin 9b
    kev "Да, хорошая идея."
    show kevin 23
    show eve 2b
    eve "... Просто пообещай мне, что ты будешь осторожен, {b}[firstname]{/b}."
    show eve 1
    show player 17
    player_name "Обещаю."
    show player 13
    show eve 2b
    eve "Заходи {b}в актовый зал{/b}, когда закончишь."
    hide eve
    hide kevin
    hide player
    with dissolve
    return

label school_weekend_lock:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "( Сейчас же {b}выходной{/b}. )"
    player_name "( Школа закрыта {b}до понедельника{/b})"
    hide player 12 with dissolve
    hide event01
    return

label night_closed_school:
    if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
        $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    scene expression game.timer.image("outside_school{}")
    if False:
        if M_erik.get("webcam help"):
            $ player.go_to(L_school_hall)
            call expression game.dialog_select("school_erik_webcam_quest")
            call expression game.dialog_select("school_erik_webcam_quest_sneak_in")

            $ game.main()
        else:

            call expression game.dialog_select("school_erik_webcam_quest_need_help")
    else:

        call expression game.dialog_select("school_closed")
    call expression game.dialog_select("map_dialogue")

label school_closed:
    show player 2 with dissolve
    player_name "( {b}Школа{/b} закрыта по ночам... Следует вернуться сюда утром. )"
    hide player 2 with dissolve
    return

label school_hallway:
    $ player.go_to(L_school_hall)
    $ game.main()

label school_locker_smith_go_to_locker:
    scene location_school_day_blur
    show player 11f at right
    show annie 3f at Position(xpos=0.3, ypos=1.0)
    with dissolve
    ann "Хорошо, давай покончим с этим."
    show annie 17 with dissolve
    pause
    show annie 18 at Position(xpos=0.24, ypos=1.0) with dissolve

    show player 10f
    player_name "Вау, то есть этот ключ открывает все шкафчики в школе?"
    show player 11f
    show annie 17 at Position(xpos=0.3, ypos=1.0) with dissolve
    pause
    show annie 3f with dissolve
    ann "Пффф, этот ключ открывает любую дверь в школе, не говоря о шкафчиках."
    show player 10f
    show annie 1f
    player_name "Серьёзно?!"
    show player 11f
    show annie 5f
    ann "Ага, именно поэтому он и называется {b}универсальным ключом{/b}."
    show player 10f
    show annie 6f
    player_name "Как ты его достала?"
    show player 11f
    show annie 5f
    ann "Эмм, а то, что я рву свою жопу каждый день, помогая {b}миссис Смит{/b} держать вас, малявок, в узде, тебе ничего не говорит!?"
    show player 12f
    show annie 6f
    player_name "Малявок? Мы с тобой одного возраста..."
    show player 16f
    show annie 3f
    ann "... Да, верно. Здесь все такие незрелые."
    show player 10f
    show annie 1f
    player_name "То есть ты постоянно таскаешь с собой {b}универсальный ключ{/b}?"
    show player 11f
    show annie 3f
    ann "Нет, конечно. {b}Миссис Смит хранит его в своём кабинете{/b}, но мы, вроде как, никогда его не использовали."
    show player 10f
    show annie 1f
    player_name "Никогда?"
    show player 11f
    show annie 4f
    ann "В школе нет таких дураков, которые бы забыли код от своего шкафчика..."
    show annie 3f
    ann "Пошевеливайся и бери всё, что тебе нужно!"
    ann "Иначе бы опоздаем на урок {b}физкультуры{/b}!"
    show player 10f
    show annie 1f
    player_name "Да, помню, я уже иду."
    return

label school_hallway_smith_unlocked_locker:
    scene location_school_day_blur
    show player 34
    with dissolve
    player_name "( Хмм, так {b}миссис Смит хранит универсальный ключ у себя в кабинете{/b}. )"
    player_name "( ... {b}было бы полезно иметь его в своих руках{/b}! )"
    player_name "( ... )"
    player_name "( Есть, над чем подумать. )"
    player_name "( Ладно, пока что мне надо идти в {b}мужскую раздевалку{/b} и переодеться на {b}урок физкультуры{/b}. )"

    return

label school_erik_webcam_quest:
    show player 14 at left
    show erik 1 at right
    player_name "Эй!"
    show player 17
    player_name "Я думал, что ты не появишься."
    show player 1
    show erik 4
    eri "Я сказал {b}миссис Джонсон{/b}, что я пошёл в кинотеатр в торговом центре..."
    show player 17
    show erik 1
    player_name "Классно."
    show player 11
    show erik 5
    eri "Но мне нельзя долго гулять: я должен быть дома до отбоя."
    show player 92
    show erik 1
    player_name "У тебя есть время отбоя?!"
    show player 91
    show erik 3
    eri "... Мне просто не нравится расстраивать {b}миссис Джонсон{/b}."
    show player 113
    show erik 1
    player_name "В любом случае, нам надо быть тише воды, ниже травы!"
    show player 1
    show erik 5
    eri "Там же есть сигнализация, да?"
    show erik 1
    show player 2
    player_name "Нам не надо волноваться об этом, ведь мы залезем туда через окно!"
    player_name "Просто следуй за мной..."
    hide player
    hide erik
    hide event01_night
    hide ui
    scene black
    return

label school_erik_webcam_quest_sneak_in:
    with dissolve
    with Pause(0.5)
    show outside_school_night02a with dissolve
    show text "После моих убеждений {b}Эрик{/b} последовал за мной к правой стороне школы.\nМы быстро пробежали по двору к одному из окно первого этажа." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02b with dissolve
    show text "Я решил позволить {b}Эрику{/b} залезть первым.\n Должен сказать, это оказалось куда труднее, чем я себе представлял..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show outside_school_night02c with dissolve
    show text "Когда настала моя очередь, я вскочил и запрыгнул внутрь.\n Мы наконец-то пробрались внутрь, и никто нас не заметил." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    $ playMusic()
    hide text with dissolve

    hide outside_school_night02a
    hide outside_school_night02b
    hide outside_school_night02c
    scene black
    with dissolve
    with Pause(0.5)
    scene school_night with dissolve
    player_name "!!!"
    player_name "Я что-то слышу..."
    scene cult_event 1
    with Dissolve(0.3)
    eri "Какого х...!?"
    scene cult_event 2
    with Dissolve(0.3)
    player_name "Шшш!"
    player_name "Тише, прошу тебя..."
    scene cult_event 3
    with Dissolve(0.3)
    window hide
    pause
    scene cult_event 4
    with Dissolve(0.3)
    scene school_night
    show player 22 at left
    show erik 5 at right
    with dissolve
    eri "У меня плохое предчувствие..."
    show player 10
    show erik 1
    player_name "Ага, тут явно что-то происходит"
    show player 11
    show erik 5
    eri "Что они делают в школе так поздно?"
    eri "... И что это за странные костюмы на них?"
    show player 92
    show erik 1
    player_name "Давай прокрадёмся за ними и узнаем, куда они идут."
    show player 91
    show erik 5
    eri "Серьёзно? А я думал, что нам просто стоит свалить отсюда..."
    show player 26
    show erik 3
    player_name "Не будь трусом!"
    player_name "И не забывай, что мы всё ещё не сделали то, ради чего пришли сюда!"
    show player 91
    show erik 2
    eri "{b}*Вздох*{/b}"
    show erik 3
    eri "Хорошо..."
    hide player 91 with dissolve
    hide erik 3 with dissolve
    return

label school_erik_webcam_quest_need_help:
    show player 114 with dissolve
    player_name "Хмм..."
    show player 10
    player_name "( Мне нужна {b}помощь{/b}, чтобы незаметно пробраться ночью в школу. )"
    hide player 10 with dissolve
    return

label school_roxxy_dexter_argument:
    scene school
    show eve 2 at right
    show kevin 23f at Position (xpos=500)
    with dissolve
    eve "Да, они там сейчас ругаются друг с другом!"
    show eve 5
    show kevin 9bf
    kev "Хах, ну и ну!"
    kev "Они определённо стоят друг друга!"
    show kevin 23f
    show eve 2
    eve "Я знаю..."
    eve "Давай, нам стоит посмотреть на это шоу, пока оно не закончилось!"
    show eve 5
    show kevin 9bf
    kev "... Да ну. Их разборки меня никаким образом не касаются."
    show kevin 23f
    show player 14 at left with dissolve
    player_name "Что случилось, ребят?"
    show player 13
    show kevin 9b with dissolve
    kev "О, братан!"
    show kevin 23
    show eve 4 with dissolve
    eve "О, {b}[firstname]{/b}."
    show eve 2 with dissolve
    eve "{b}Рокси{/b} и {b}Декстер{/b} закатили целую драму {b}на баскетбольной площадке.{/b}"
    eve "Я как раз хотела сходить и посмотреть на это!"
    eve "... Пойдёшь?"
    show eve 5
    show player 14
    player_name "Да, пожалуй."
    player_name "Погнали."
    show player 13
    show kevin 9b
    kev "Увидимся, ребят!"
    hide player
    hide kevin
    hide eve
    with dissolve
    return

label school_roxxy_dexter_confront:
    scene school
    show player 5 at left
    show dexter 1 at right
    show dexter 4
    with dissolve
    dex "{b}[firstname]{/b}!"
    show dexter 2 with dissolve
    show player 10
    player_name "Всё, приехали..."
    player_name "Что тебе надо, {b}Декстер{/b}?"
    show player 5
    show dexter 6 with dissolve
    dex "Ты что, подглядывал за {b}Рокси{/b} в душе?!"
    show dexter 5
    show player 12
    player_name "Кто тебе такое сказал?"
    show player 11
    show dexter 8 with dissolve
    dex "... {b}Бекка{/b}!"
    show dexter 6 with dissolve
    dex "Это правда?!"
    show dexter 2 with dissolve
    show player 10
    player_name "Нет!"
    player_name "Я просто принимал душ после урока физкультуры."
    player_name "Я не виноват, что {b}Рокси{/b} уже была там."
    show player 5
    dex "..."
    show dexter 6 with dissolve
    dex "Ты ты ПОДГЛЯДЫВАЛ за ней?!"
    show dexter 2 with dissolve
    show player 10
    player_name "Что?"
    show player 12
    player_name "Нет!"
    player_name "Ты что, не слушаешь?"
    player_name "Слушай, чувак, я не подглядывал за {b}Рокси{/b}..."
    player_name "Я просто хотел помыться!"
    player_name "Я пообещал ей, что не буду смотреть на неё!"
    show player 11
    dex "..."
    hide player
    show dexter 7 at left

    player_name "{b}*гхкх*{/b}" with hpunch
    show player 89 at left
    show dexter 1 at right
    show dexter 6
    with dissolve
    dex "Оставь {b}Рокси{/b} в покое!"
    show dexter 5
    show player 88
    player_name "{b}*вхух*{/b}"
    show dexter 6
    dex "Она моя!"
    dex "Тебе это понятно?!"
    show dexter 5
    player_name "{b}*гхкх*{/b}"
    show player 89
    show dexter 4 with dissolve
    dex "Ещё раз появишься рядом с ней - я тебе лицо расквашу!"
    show dexter 2 with dissolve
    show player 88
    player_name "{b}*кхх кхх*{/b}"
    show player 10 with dissolve
    player_name "... А вы разве не расстались?"
    show player 90
    show dexter 8
    dex "... А?"
    dex "Кто такое сказал?"
    show dexter 2
    show player 10
    player_name "Ты!"
    player_name "В тот день, на {b}баскетбольной площадке{/b}."
    show player 90
    show dexter 6 with dissolve
    dex "Нет!"
    dex "Она скоро извинится передо мной, и у нас снова всё будет хорошо!"
    show dexter 2 with dissolve
    show player 10
    player_name "... Я не уверен."
    show player 90
    show dexter 15 at Position (xoffset=2) with dissolve
    dex "Ещё хочешь получить, а?!"
    show dexter 14 at Position (xoffset=2)
    show player 88 with dissolve
    player_name "{b}*кхх*{/b}... Не надо!"
    show player 89
    show dexter 15 at Position (xoffset=2)
    dex "Тогда держись от моей тёлки подальше!"
    dex "Усёк?!"
    show dexter 14 at Position (xoffset=2)
    show player 10 with dissolve
    player_name "... Да, вполне."
    show player 90
    show dexter 15 at Position (xoffset=2)
    dex "Вот и отлично!"
    hide dexter with dissolve
    show player 16
    player_name "( ... )"
    player_name "( Когда-нибудь придёт тот день, когда ты ответишь за всё, {b}Декстер{/b}. )"
    hide player with dissolve
    return

label school_roxxy_assignment:
    scene school
    show teacher 18f at left
    show roxxy 33 zorder 1 at right
    with dissolve
    rox "Нет, {b}мисс Биссет{/b}! Умоляю вас!"
    rox "Пожалуйста, не делайте этого!"
    show roxxy 32
    show teacher 19f
    bis "Я тебе уже говорила, глупая девчонка!"
    bis "Списывать работу у своих одноклассников - это непростительно!"
    bis "Мне уже надоело повторять это!"
    show teacher 18f
    show roxxy 33
    rox "Ну пожалуйста, я смогу исправиться!"
    rox "Дайте мне ещё один шанс!"
    show roxxy 32
    show teacher 3f
    bis "Хах!"
    show teacher 19f
    bis "Я и так уже дала тебе слишком много шансов!"
    show teacher 18f
    show roxxy 33
    rox "Но в этот раз я буду усердно учиться и самостоятельно делать домашнюю работу!"
    rox "Я клянусь!"
    rox "Ещё один шанс, прошу!"
    show roxxy 32
    show teacher 20f
    bis "..."
    show player 13f zorder 0 at Position (xpos=650) with dissolve
    show teacher 2f
    bis "О, {b}[firstname]{/b}!"
    bis "Вовремя ты пришёл, да?"
    show teacher 5f
    bis "{b}Роксана{/b} просто взяла и списала {b}твою домашнюю работу{/b}!"
    show teacher 19f
    bis "... И это после того, как я сказала ей, что у неё будут неприятности, если она ещё раз что-нибудь спишет!"
    bis "А сейчас она хочет ещё один шанс!"
    show teacher 5f
    bis "Что скажешь?"
    bis "Стоит ли мне дать её ещё одну возможность исправиться?"
    show teacher 4f
    rox "..."
    show player 11f
    player_name "..."
    show player 10f
    player_name "Ну..."
    player_name "... скорее всего, да?"
    show player 5f
    show teacher 20f
    bis "Хмм..."
    pause
    show teacher 2f
    bis "Эх, какой же ты добродушный, {b}[firstname]{/b}!"
    show teacher 12f
    bis "... Вы такие милые, чтобы вам отказать!"
    show roxxy 1e
    show player 13f
    bis "Хорошо!"
    show teacher 19f
    bis "Я даю тебе последний шанс, {b}Роксана{/b}!"
    show teacher 18f
    show roxxy 1d
    rox "Фух, спасибо Вам большое!"
    show roxxy 1e
    show teacher 19f
    bis "... И чтобы всё прошло гладко..."
    show teacher 3f
    bis "{b}[firstname]{/b} возьмёт над тобой шефство и будеть помогать в учёбе!"
    show player 22f
    show teacher 1f
    show roxxy 3c with dissolve
    rox "Что?!"
    rox "Я не хочу этого!"
    show roxxy 3d
    show teacher 3f
    bis "Нет!"
    show teacher 2f
    bis "А кто это там говорил: \"Дайте мне ещё один шанс!\" Не помнишь?"
    show teacher 1f
    show roxxy 2
    rox "... Да, но..."
    show roxxy 3c
    rox "... почему именно он?!"
    show roxxy 14
    if M_bissette.is_state(S_bissette_end):
        show teacher 12f
        bis "{b}[firstname]{/b} - мой лучший ученик!"
        bis "Кто сможет тебе помочь лучше, чем он?"
        show teacher 13f
    else:
        show teacher 2f
        bis "{b}[firstname]{/b} изо всех сил старается в учёбе."
        bis "Думаю, что лишняя взаимопомощь вам не повредить, не так ли?"
        show teacher 1f
    show player 10f
    player_name "Мне реально придётся помогать ей?"
    show player 5f
    show teacher 2f
    bis "Ты же сам сказал, что не против дать ей ещё один шанс!"
    bis "Надеюсь, что ты сможешь заставить её учиться!"
    show teacher 1f
    show player 24f
    player_name "{b}*вздох*{/b}"
    player_name "Хорошо..."
    show teacher 3f
    bis "Tres Bien! ( Прекрасно )"
    show teacher 2f
    bis "Ну ладно, удачи вам!"
    hide teacher with dissolve
    show player 5 at left with dissolve
    show roxxy 29
    rox "..."
    player_name "..."
    show roxxy 30
    rox "Полный отстой!"
    show roxxy 29
    show player 10
    player_name "Расслабься... Я не буду тебя доставать!"
    player_name "Пошли лучше к тебе домой, я быстро с тобой позанимаюсь, после чего свалю..."
    show player 5
    show roxxy 2
    rox "Ты хочешь заниматься в моём доме?!"
    show roxxy 3
    rox "Ни в коем случае!"
    show roxxy 3d
    show player 10
    player_name "Может быть, нам стоит пойти в библиотеку или ещё куда-нибудь..."
    show player 5
    show roxxy 3c
    rox "... И светиться на публике с ТОБОЙ..."
    rox "Eww, no."
    show roxxy 14
    show player 12
    player_name "В такое случае..."
    show player 11
    dex "Эй, {b}Мисси{/b}! Ты не видела сегодня {b}Рокси{/b}?!"
    missy "Да, она разговаривала с {b}мисс Биссет{/b}..."
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 2c
    rox "Твою м..."
    rox "Чёрт..."
    rox "Прячься!"
    scene expression "backgrounds/location_school_cutscene03.jpg"
    with fade
    show text "Пока я пытался понять, что случилось, {b}Рокси{/b} быстро запихнула меня в мой школьный шкафчик." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show roxxy 7f at left
    show dexter 8 at right
    with dissolve
    dex "Вот ты где."
    show dexter 2
    show roxxy 11f with dissolve
    rox "... Да, я здесь, как сам?"
    show roxxy 9f
    show dexter 8
    dex "Просто подумал, что ты захочешь наконец-то извиниться передо мной."
    show dexter 2
    show roxxy 11f
    rox "Пффф, извиниться за что?"
    show roxxy 9f
    show dexter 6 with dissolve
    dex "Ты прекрасно знаешь!"
    dex "Ты обзывала меня!"
    show dexter 2
    show roxxy 11f
    rox "А, ты про тупицу?"
    dex "..."
    show roxxy 5f with dissolve
    rox "Хорошо, не веди себя, как тупица, и я не буду называть тебя тупицей... тупица."
    show roxxy 6f with dissolve
    dex "Гррр..."
    show dexter 6
    dex "ХВАТИТ НАЗЫВАТЬ МЕНЯ ТУПИЦЕЙ!" with hpunch
    show dexter 5
    show roxxy 10f with dissolve
    rox "... Или что?"
    show roxxy 7f with dissolve
    show dexter 2 with dissolve
    dex "..."
    show dexter 8
    dex "Везёт тебе, что ты моя девушка!"
    dex "Если бы кто-то другой со мной так разговаривал..."
    show dexter 4
    dex "Я бы его порвал на британский флаг!" with hpunch
    show dexter 2
    show roxxy 11f
    with dissolve
    rox "Ух хух."
    rox "Всё, ты закончил?"
    show roxxy 9f
    show dexter 8
    dex "Все."
    dex "В конце концов ты извинишься."
    show dexter 6 with dissolve
    dex "Просто запомни. Пока ты этого не сделаешь, не проси меня ни о чем!"
    show dexter 2 with dissolve
    show roxxy 10f
    rox "Как будто мне от тебя что-то нужно!"
    rox "Ты бы, наверное, просто облажался, даже если бы я попросила!"
    show roxxy 6f with dissolve
    dex "..."
    show dexter 4 with dissolve
    dex "Рррааааар!!!!" with hpunch
    show dexter 6 with dissolve
    dex "Какая же ты сука!"
    hide dexter with dissolve
    show roxxy 7f
    rox "..."
    show roxxy 1b at right with dissolve
    rox "Всё, можешь выходить, {b}[firstname]{/b}."
    show roxxy 1
    pause
    show player 12 at left with dissolve
    player_name "Неужели игра стоит свеч, чтобы противостоять такому человеку, как Декстеру?"
    show player 5
    show roxxy 1b
    rox "А?"
    show roxxy 3c
    rox "Пофигу. В жопу Декстера! Совсем достал!"
    show roxxy 3d
    show player 10
    player_name "Да, но он далеко не самый уравновешенный человек..."
    player_name "Почему ты с ним вообще встречаешься?"
    show player 12
    player_name "Мне кажется, что ты выше его уровня."
    show player 5
    show roxxy 2
    rox "Пффф, умоляю! Я выше любого уровня!"
    rox "Встречаться с {b}Декстером{/b} стоит хотя бы из-за того, что никто не путается под ногами!"
    show roxxy 1h
    rox "Так гораздо проще, поверь."
    show roxxy 1g
    show player 10
    player_name "Да, может быть, но он такой..."
    show player 5
    show roxxy 2
    rox "... тупой?"
    show roxxy 1
    show player 17
    player_name "Ахаха, именно!"
    show player 13
    show roxxy 4
    rox "Ахахахаха!"
    show roxxy 1
    pause
    show player 11
    player_name "..."
    rox "..."
    show player 10
    player_name "{b}*вздох*{/b} Значит... Встречаемся {b}у тебя сегодня вечером{/b}?"
    show player 5
    show roxxy 30
    rox "{b}*вздох*{/b} Да."
    rox "Но даже не думай о том, что учиться со мной будет просто. Это не мой конёк!"
    show roxxy 29
    show player 14
    player_name "Не волнуйся. Я введу тебя в курс дела!"
    show player 13
    rox "..."
    show player 36 with dissolve
    player_name "Увидимся {b}вечером{/b}."
    show player 13
    show roxxy 30
    rox "... Угу."
    show roxxy 29
    hide player with dissolve
    rox "..."
    pause
    show roxxy 1g
    pause
    return

label school_roxxy_missing_outfit:
    scene school
    show becca 1 at Position(xpos=315)
    show missy 2b at left
    show roxxy 3c zorder 1 at right
    with dissolve
    rox "... Ух, вы нашли его?"
    show roxxy 3b
    show becca 2
    becca "Нет."
    show becca 1
    show missy 2
    missy "Ты уверена, что не оставила его дома?"
    show missy 2b
    show roxxy 3c
    rox "Конечно уверена, {b}Мисси{/b}!"
    rox "Я что, выгляжу, как идиотка?"
    show roxxy 3b
    show becca 3
    show missy 1b
    missy "Я этого не говорила!"
    show missy 3
    show becca 3b
    becca "Но ты имела это ввиду..."
    show becca 3
    show missy 2
    missy "Я просто хочу помочь!"
    show missy 2b
    show becca 4
    becca "Ахаха, лучшая помощь на свете!"
    show becca 5
    show roxxy 30
    rox "{b}*Вздох*{/b}У вас же нету запасной формы?"
    show roxxy 29
    show becca 2
    becca "Нет. Моя запасная форма в стирке."
    show becca 3
    show missy 1b
    missy "Я тоже не принесла её."
    show missy 1
    show becca 8
    becca "С маленькими сиськами {b}Мисси{/b}... Нет, её форма не налезла бы на тебя в любом случае!"
    show becca 7
    show missy 4
    missy "Завались, уродина!"
    show missy 2b
    show becca 4
    becca "Ахаха, да не переживай ты. Когда-нибудь вырастут..."
    show becca 5
    show roxxy 3c
    rox "{b}*Вздох*{/b} Какие же вы бесполезные!"
    show roxxy 3b
    show becca 2
    becca "Пшшш, ну и ну."
    show becca 1
    show missy 2
    missy "Это не наша вина, что ты забыла свою форму дома!"
    show missy 2b
    show roxxy 30
    rox "Думаю, что нам стоит сходить за ней ко мне домой."
    show roxxy 3b
    show becca 2b with dissolve
    becca "В смысле?!"
    becca "Ты хочешь, чтобы мы пошли к тебе домой прямо сейчас?!"
    show becca 1 with dissolve
    show missy 2
    missy "Ну нафиг!"
    show missy 2b
    show roxxy 3c
    rox "Да что вы ломаетесь, а?"
    rox "Я не хочу идти домой одна!"
    show roxxy 3b
    show missy 2
    missy "Нет!"
    missy "Если я прогуляю ещё один урок французского, {b}мисс Биссет{/b} вызовет моих родителей в школу..."
    show missy 2b
    show becca 3b
    becca "Ох, твоя мама даст тебе такого леща, если это случится!"
    show becca 3
    show missy 1b
    missy "Я сама знаю, хорошо?"
    show missy 1
    show roxxy 2
    rox "Ну и ладно, мы пойдём без тебя... Верно, {b}Бекка{/b}?"
    show roxxy 1
    show becca 2b with dissolve
    becca "..."
    show roxxy 3b
    rox "Серьёзно??!"
    show roxxy 3c
    show becca 2 with dissolve
    becca "На улице слишком жарко!"
    becca "... А ещё меня в дрожь бросает от твоего двоюродного брата."
    show becca 1
    show roxxy 3b
    show missy 2b
    rox "Ну вы и гадины!"
    show roxxy 3c
    show player 14f zorder 0 at Position (xpos=600) with dissolve
    player_name "Привет, девчонки!"
    player_name "Как дела?"
    show player 13f
    show becca 2
    becca "... Эмм... Зачем ты с нами говоришь, а?"
    show becca 1
    show player 11f
    show missy 1b
    missy "Внимание! Обнаружен задрот!"
    show missy 1
    show roxxy 27 with dissolve
    rox "..."
    show player 5 with dissolve
    show roxxy 28
    rox "Я забыла свою {b}форму черлидерши{/b} дома."
    show roxxy 1n
    rox "... И \"мои друзья\" отказываются пройтись со мной до дома!"
    show roxxy 1m
    show player 5f with dissolve
    show missy 1b
    missy "Нет, я бы с удовольствием прошлась, если бы не {b}мисс Биссет{/b}!"
    show missy 1
    show roxxy 1n
    rox "... Да что бы там ни было."
    show roxxy 1m
    show player 10 with dissolve
    player_name "Я пойду с тобой."
    show roxxy 1k
    player_name "... Ну, если ты хочешь?"
    show player 5
    show roxxy 1i
    show becca 2b with dissolve
    becca "Эмм..."
    becca "Почему она должна хотеть пойти с тобой, задротишка?!"
    show becca 1 with dissolve
    show roxxy 1j
    rox "..."
    pause
    show roxxy 1l
    rox "... Я не против, пошли."
    show roxxy 1k
    show player 13
    show becca 2b with dissolve
    becca "КАКОГО!?!"
    becca "Ты серьёзно пойдёшь с этим неудачником?"
    show becca 1
    show roxxy 3
    with dissolve
    rox "Я просто не хочу идти через весь город одна!"
    rox "... Ведь вы же не хотите прогуляться со мной, да?"
    show roxxy 3c
    show player 5
    rox "... Разве у меня есть выбор?"
    show roxxy 3b
    show becca 2
    show player 5f with dissolve
    becca "Да, но я имела ввиду... Да ты взгляни на него..."
    becca "... Он такой..."
    show becca 1
    show missy 8
    missy "... Задротоподобный?"
    show missy 7
    show becca 4
    becca "Ахаха, да!"
    show becca 5
    show missy 3
    show player 12f
    player_name "Такого слова даже не существует!"
    show player 90f
    show roxxy 3c
    rox "Почему бы вам двоим не заткнуться?!"
    rox "Давай, {b}[firstname]{/b}. Пошли отсюда!"
    hide roxxy with dissolve
    player_name "..."
    show player 12f
    player_name "... Увидимся, страхолюдины!"
    hide player with dissolve
    show becca 1
    becca "..."
    show becca 3
    show missy 6
    missy "Пффф, ахаха!"
    show missy 7
    show becca 2f at Position (xpos=400) with dissolve
    becca "Ты над чем смеёшься?"
    show becca 1f
    show missy 6
    missy "... Этот задрот назвал тебя страхолюдиной!"
    show missy 7
    show becca 2f
    becca "Он нас обеих назвал страхолюдинами, идиотка!"
    show becca 1f
    show missy 3
    missy "..."
    show missy 5
    missy "А, точно..."
    show missy 4
    missy "Эй, ты! Не смей называть меня страхолюдиной!"
    scene black with fade
    return

label school_roxxy_return_to_school:
    scene school
    show player 14 at Position (xpos=500)
    show roxxy 23 at right
    show roxxy_outfit cheer at right
    with dissolve
    player_name "Похоже, что мы вернулись вовремя!"
    show player 13
    show roxxy 24
    rox "... Спасибо за помощь."
    show roxxy 23
    show player 14
    player_name "Без проблем, {b}Рокси{/b}!"
    show player 13
    show becca 5 at Position(xpos=315)
    show becca_outfit cheer at Position (xpos=315)
    show missy 1b at left
    show missy_outfit cheer at left
    with dissolve
    show player 13f at Position (xpos=600) with dissolve
    missy "Эй, ты нашла, что искала?!"
    show missy 1
    show becca 6
    becca "... Да, конечно!"
    becca "Оно на ней, ты не видишь?"
    show becca 5
    show missy 2
    missy "Да ну тебя!"
    show missy 2b
    show becca 8
    becca "Этот задрот всё ещё с тобой?"
    show becca 7
    show player 5f
    show roxxy 23b
    rox "... Не обзывайся его."
    show roxxy 23
    show becca 2
    becca "А?"
    show becca 1
    show roxxy 24
    rox "... Он хороший парень."
    show roxxy 23
    show becca 8
    becca "Ты в него влюбилась что ли?"
    show becca 7
    show roxxy 23c
    rox "Пффф, нет!!"
    show roxxy 24
    rox "Он меня сегодня так выручил, поэтому будьте с ним поласковее."
    show roxxy 23
    show becca 4
    becca "Да что бы то ни было!"
    show becca 8
    becca "Я думаю, что {b}[firstname]{/b} вызывает у тебя чувства!"
    show becca 4
    becca "Ахаха!"
    show becca 8
    becca "А ты что думаешь, {b}Мисси{/b}?"
    show becca 7
    show missy 8
    missy "... Да, он такой милашка!"
    show missy 7
    show becca 3
    becca "!!!" with hpunch
    show becca 3b
    show missy 3
    becca "Я не это имела ввиду!"
    show becca 2
    becca "Что с вами двоими не так?"
    show becca 1
    show missy 1
    rox "..."
    show becca 2
    becca "Ладно, я пойду на занятия!"
    hide becca
    hide becca_outfit cheer
    with dissolve
    show missy 2
    missy "{b}Бекка{/b}, стой!"
    missy "... Я просто не поняла вопрос!"
    hide missy
    hide missy_outfit cheer
    with dissolve
    rox "..."
    show player 10 at Position (xpos=500) with dissolve
    player_name "... Спасибо за твои тёплые слова."
    show player 13
    show roxxy 23b
    rox "А?"
    show roxxy 24
    rox "Точно."
    rox "Без разницы."
    rox "Не ищи тут какой-то скрытый смысл!"
    show roxxy 23b
    rox "Я не люблю тебя... Я просто поблагодарила тебя за помощь!"
    show roxxy 23
    show player 14
    player_name "Ла-адно."
    player_name "Увидимся!"
    show player 13
    show roxxy 24
    rox "Да, увидимся..."
    hide roxxy
    hide roxxy_outfit cheer
    with dissolve
    player_name "( Ну и денёк... )"
    player_name "( Думаю, что {b}Рокси{/b} стала теплее ко мне относиться! )"
    show player 18
    player_name "( Мне надо найти способы сблизиться с ней получше. )"
    return

label school_roxxy_trailer_park_trouble:
    scene school
    show annie 3 at right
    show roxxy 3df zorder 1 at left
    with dissolve
    ann "В Уставе колледжа очень ясно прописано!"
    ann "Студентам запрещено пользоваться телефонами на территории этого здания!"
    show annie 1
    show roxxy 3f
    rox "Уйди отсюда, психонутая со своим надзором!"
    show roxxy 3df
    show player 10f zorder 0 at Position (xpos=500) with dissolve
    player_name "Так, что тут происходит?"
    show player 5f
    show roxxy 3f
    rox "У меня тут проблемы!!!"
    show roxxy 3df
    show player 5 at Position (xpos=400) with dissolve
    show annie 5
    ann "Хватит!"
    ann "Нельзя пользоваться телефонами на территории колледжа!"
    show annie 3
    ann "Убери его!"
    show annie 1
    show roxxy 3f
    rox "Отвали, {b}Энни{/b}, или я тебе леденец на лицо приклею!"
    show roxxy 3bf
    show annie 5
    ann "Пфффф, ты меня на напугаешь..."
    show annie 6
    ann "..."
    show annie 5
    ann "... Я зову {b}миссис Смит{/b}!"
    hide annie with dissolve
    show roxxy 3df
    show player 10f at Position (xpos=600) with dissolve
    player_name "Что случилось?"
    show player 5f
    show roxxy 33f
    rox "По всей видимости, полицейские только что пришли ко мне домой и арестовали {b}мою маму{/b}!"
    show roxxy 32f
    show player 10f
    player_name "Что?!"
    player_name "За что!?"
    show player 11f
    show roxxy 33f
    rox "Я не знаю!"
    rox "Мне срочно нужно домой..."
    show roxxy 32f
    player_name "..."
    show player 10f
    player_name "Хочешь, я пойду с тобой?"
    show player 5f
    show roxxy 32f
    rox "..."
    show roxxy 1lf
    rox "Ты правда это сделаешь?"
    show roxxy 32f
    show player 10f
    player_name "... Конечно, я не против!"
    show player 5f
    rox "..."
    show roxxy 1lf
    rox "Спасибо, {b}[firstname]{/b}."
    rox "Давай, пошли отсюда, пока {b}Энни{/b} не вернулась."
    show roxxy 32f
    show player 12f
    player_name "Пошли!"
    hide roxxy
    hide player
    with dissolve
    return

label school_roxxy_selling_meth_ask_roxxy:
    scene school
    show roxxy 14f at Position (xpos=500)
    show becca 1 at Position(xpos=315)
    show missy 1 at left
    show player 14f at right
    with dissolve
    player_name "Эй, {b}Рокси{/b}, мне надо поговорить с тобой!"
    show player 13f
    show becca 2
    becca "Ох, отстань, неудачник!"
    show becca 1
    show missy 2
    missy "Да, неужели ты не видишь, что у неё и так проблем хватает?!"
    show missy 2b
    show player 14f
    player_name "Я нашёл способ, как исправить ситуацию!"
    show player 13f
    show missy 2
    missy "Пффф, конечно!"
    show missy 2b
    show becca 2
    becca "Что может сделать такой задрот, как ты?"
    show becca 1
    show roxxy 29f
    show player 12f
    player_name "Можно выделить мне всего несколько секунд?"
    show player 90f
    show becca 2
    becca "Свали отсюда!"
    show becca 1
    show missy 2
    missy "Да, ид..."
    show missy 3
    show roxxy 30f
    rox "Почему бы вам двоим не заткнуться?"
    show player 11f
    rox "*Вздох* Идите в класс, я хочу поговорить с ним."
    show roxxy 29f
    show player 13f
    show becca 2b with dissolve
    becca "Ты сейчас серьёзно?"
    show becca 1
    show roxxy 3 at Position (xpos=600)
    with dissolve
    rox "Просто. Уйдите."
    show roxxy 3b
    show missy 2b
    show becca 2
    becca "Просто шикарно!"
    show becca 3b
    becca "Пошли, {b}Мисси{/b}!"
    hide becca
    hide missy
    with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "Так вот... Каким образом можно всё исправить?"
    show roxxy 3df
    show player 14f
    player_name "Ну, я убедил {b}Клайда{/b} явиться с повинной!"
    show player 13f
    show roxxy 30f
    rox "... Прекрасно."
    show roxxy 3df
    show player 5f
    player_name "..."
    show player 10f
    player_name "Что-то не так?"
    show player 5f
    show roxxy 3cf
    rox "Ты забыл?"
    rox "Даже если он признается, {b}мою маму{/b} не будут отпускать из изолятора некоторое время."
    rox "И мы потеряем трейлер."
    show roxxy 3df
    show player 14f
    player_name "Хорошо, у меня есть план!"
    player_name "{b}Клайд{/b} сказал, что у него льда имеется на 50000 долларов!"
    show player 13f
    show roxxy 2f
    rox "Пффф, {b}Клайд{/b} сказал..."
    show roxxy 3cf
    show player 5f
    rox "Этот придурок едва может завязать шнурки на ботинках!"
    rox "... И ты думаешь, что он может продать весь лёд?!"
    show roxxy 3df
    player_name "..."
    show player 10f
    player_name "А разве этим он не занимался всё время?"
    show player 5f
    show roxxy 4f
    rox "Ахахахха, прикалываешься?"
    show roxxy 3cf
    rox "Он его готовит, но продаёт его {b}моя мать{/b}!"
    show roxxy 3df
    show player 11f
    player_name "..."
    show roxxy 2bf
    rox "!!!"
    show roxxy 3cf
    rox "Я этого не говорила, если что!"
    show roxxy 3df
    show player 10f
    player_name "Не беспокойся. Я никомун не расскажу."
    show player 5f
    show roxxy 30f
    rox "Слушай, я очень ценю то, что ты пытаешься мне помочь, {b}[firstname]{/b}."
    show roxxy 3cf
    rox "... Но тебе гораздо лучше просто забыть про меня и мои проблемы!"
    hide roxxy with dissolve
    player_name "..."
    show player 4f
    player_name "( Хорошо, что теперь? )"
    player_name "( Я думаю, что мне стоит {b}вернуться к Клайду{/b}... )"
    hide player with dissolve
    return

label school_roxxy_shut_down_lab:
    scene school
    show roxxy 32f at Position (xpos=500)
    show becca 2 at Position(xpos=315)
    show missy 1 at left
    show player 13f at right
    with dissolve
    becca "Снова ты?"
    show becca 1
    show missy 2
    missy "Что сейчас надо, неудачник?!"
    show missy 2b
    show player 5f
    show roxxy 30f at Position (xoffset=34)
    rox "Гос-по-ди."
    show roxxy 3 at Position (xpos=600) with dissolve
    rox "Вы можете прекратить это?"
    rox "У меня сейчас не то настроение."
    show roxxy 3d
    show missy 3
    missy "..."
    show becca 2
    becca "... И что? Нам теперь надо задротам жопу вылизвать?"
    show becca 1
    show roxxy 3c
    rox "Просто дайте нам поговорить."
    show roxxy 3d
    show player 13f
    show becca 2
    becca "Ладно."
    show becca 3b
    becca "Пошли, {b}Мисси{/b}, оставим наедине {b}Рокси{/b} и её задротишку."
    hide becca with dissolve
    show roxxy 3c
    rox "Хватит быть такой сукой, {b}Бекка{/b}!"
    show roxxy 3d
    show missy 1b
    missy "Эй, меня-то подожди!"
    hide missy with dissolve
    pause
    show roxxy 3cf at Position (xpos=500) with dissolve
    rox "Что ты хочешь, {b}[firstname]{/b}."
    show roxxy 3df
    show player 14f
    player_name "Я принёс тебе кое-что."
    show player 239_240f with dissolve
    pause
    show player 650f with dissolve
    pause
    show roxxy 68bf
    show player 13f
    with dissolve
    rox "..."
    show roxxy 68cf
    rox "Боже мой!"
    show roxxy 1f f with dissolve
    show player 14f
    player_name "Ага..."
    show player 13f
    show roxxy 2f
    rox "Я помню, что говорила тебе не волноваться об этом..."
    show roxxy 1f f
    show player 14f
    player_name "Да, говорила."
    show player 13f
    show roxxy 2f
    rox "Так зачем ты..."
    show roxxy 2bf
    show player 14f
    player_name "Я принёс тебе ещё кое-что..."
    show player 239_240f with dissolve
    pause
    show player 638bf
    rox "!!!" with hpunch
    show roxxy 80f at Position (xoffset=47)
    show player 13f
    with dissolve
    pause
    show roxxy 82f at Position (xoffset=47)
    rox "Ничего себе!"
    rox "Никогда не видела столько денег!"
    rox "Как тебе это..."
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Клайд и я продали лёд прошлой ночью."
    show player 13f
    show roxxy 82f at Position (xoffset=47)
    rox "Ты сейчас серьёзно?!"
    show roxxy 81f at Position (xoffset=47)
    show player 14f
    player_name "Да, выручили целых 60000 долларов!"
    player_name "Хватит, чтобы внести залог за {b}твою мать{/b}... Верно?"
    show player 13f
    show roxxy 80f at Position (xoffset=47)
    rox "..."
    show roxxy 1bf with dissolve
    rox "Не могу поверить, что ты сделал это!"
    show roxxy 1f f
    rox "..."
    show roxxy 1bf
    rox "{b}[firstname]{/b}, с какой целью ты это делал?!"
    rox "Я же тебе ничего не должна была, да и постоянно доставала тебя!"
    show roxxy 1f f
    show player 14f
    player_name "... Потому что так надо было."
    show player 13f
    show roxxy 1if at Position (xoffset=-34) with dissolve
    rox "..."
    show roxxy 1lf at Position (xoffset=-34)
    rox "не знаю, что сказать даже..."
    show roxxy 1kf
    show player 14f
    player_name "Тебе не надо ничего говорить."
    player_name "Просто иди и верни свой дом!"
    show player 13f
    pause
    hide player
    show roxxy 59f at right
    player_name "!!!" with hpunch
    rox "Спасибо тебе, {b}[firstname]{/b}!"
    rox "Я этого не забуду!"
    hide roxxy
    show roxxy 1f f at Position (xpos=500)
    show player 14f at right
    with dissolve
    player_name "... Без проблем!"
    show player 13f
    show roxxy 1bf
    rox "Я лучше пойду вытаскивать свою {b}мать{/b}!"
    rox "Позже поговорим, хорошо?"
    show roxxy 1f f
    show player 14f
    player_name "Конечно. Удачи!"
    show player 13f
    hide roxxy with dissolve
    pause
    hide player
    show player 17f
    with dissolve
    player_name "( Вау! )"
    player_name "( {b}Рокси{/b} обняла меня при всех! )"
    show player 13f
    player_name "( Хмм ... Никого вокруг не было, вроде как... )"
    player_name "( ... Но всё равно, это прогресс! )"
    player_name "( Нужно найти возможность побольше проводить с ней время! )"
    hide player with dissolve
    return

label school_roxxy_give_exams:
    scene school
    show player 14 at left
    show roxxy 1 at right
    with dissolve
    player_name "Эй, {b}Рокси{/b}!"
    show player 17
    player_name "У меня есть кое-что для тебя..."
    show player 13
    show roxxy 1b
    rox "Ты имеешь ввиду..."
    rox "Ответы на экзамены?"
    show roxxy 1
    show player 14
    player_name "Именно!"
    player_name "Она хранит их в своей спальне, представляешь?!"
    show player 239_240
    pause
    show player 643
    pause
    hide player
    show roxxy 59 at left
    with dissolve
    rox "Боже мой, ты лучший, {b}[firstname]{/b}!"
    player_name "!!!" with hpunch
    show roxxy 64b at right
    show player 14 at left
    with dissolve
    player_name "Эмм, спасибо..."
    show player 13
    show roxxy 64c
    rox "Знаешь..."
    rox "Мне очень нравятся парни, которые ради своей девушки готовы горы свернуть!"
    show roxxy 64b
    show player 10
    player_name "... С-своей девушки?"
    show player 5
    show roxxy 2b with dissolve
    rox "!!!"
    show roxxy 2c
    rox "Ой, я не то имела ввиду...... Ну в целом..."
    show roxxy 1
    show player 3 with dissolve
    player_name "..."
    show roxxy 2
    rox "Хех, представь, как это было бы странно?"
    show roxxy 1
    show player 29
    player_name "Я даже не зн..."
    show player 3
    show roxxy 2
    rox "Я имею ввиду... Представь, что я и ты..."
    rox "... встречаемся?"
    show roxxy 1
    show player 24 with dissolve
    player_name "..."
    rox "..."
    show player 26
    player_name "Эмм..."
    show player 11
    show roxxy 2b
    ann "Вы действительно думаете, что кто-то из учеников способен на такое?"
    smi "... А кто ещё мог залезть ко мне в дом и свистнуть экзамены?!"
    show roxxy 2c
    rox "Твою мать!"
    rox "{b}Миссис Смит{/b} идёт!"
    show roxxy 2b
    show player 10
    player_name "Нельзя, чтобы она увидела эти экзамены!"
    player_name "Надо валить отсюда!"
    show roxxy 2c at left
    show player 11f at Position (xpos=400)
    with dissolve
    rox "Нет времени!"
    show roxxy 2b
    show player 10f
    player_name "Что ты делае..."
    show player 11f
    show roxxy 3c
    rox "{b}ЗАМОЛЧИ И ДЕЛАЙ ТО, ЧТО Я СКАЖУ!!!{/b}"
    show roxxy 3d
    show player 22f
    player_name "!!!"
    scene black with fade
    scene expression "backgrounds/location_school_cutscene04.jpg"
    with fade
    show text "И {b}Рокси{/b} запихнула меня в мой шкафчик!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show principal 26f at left
    show principal 26f at Position (xoffset=70)
    show annie 3 at right
    with dissolve
    ann "Что будем делать?"
    show annie 1
    show principal 4f with dissolve
    smi "Мы должни вернуть экзамены назад! Если об этом кто-то узнает, это может поставить мою карьеру под откос!"
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 3
    ann "Не волнуйтесь, мэм! Этого не произойдёт!"
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Естественно не произойдёт! Ты найдёшь экзамены и отведёшь ответственного за это ко мне, чтобы я его наказала!"
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "... Есть, мэм!"
    show annie 1
    show principal 27f at Position (xoffset=70)
    smi "Начинай поиски с этих шкафчиков!"
    smi "Наверняка он спрятал их здесь!"
    show principal 26f at Position (xoffset=70)
    show annie 3
    ann "Есть, мэм!"
    show annie 1
    show principal 4f with dissolve
    smi "... И не подведи меня, {b}Энни{/b}!"
    smi "Ты знаешь, что бывает, когда я недовольна..."
    show principal 26f at Position (xoffset=70) with dissolve
    show annie 6
    ann "..."
    show annie 5
    ann "Я Вас не подведу!"
    show annie 6
    show principal 27f at Position (xoffset=70)
    smi "Вот и хорошо!"
    smi "А теперь за работу!"
    hide annie
    hide principal
    with dissolve
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 3
    show roxxy locker 1

    player_name "!!!"
    show player locker 1
    player_name "{b}Энни начала осматривать шкафчики!{/b}"
    player_name "Всё, нам крышка!"
    show player locker 2
    show roxxy locker 2
    rox "Шшш!"
    rox "Тише!"
    show roxxy locker 3
    rox "... И не крутись!"
    show roxxy locker 1
    show player locker 1
    player_name "Извини, я просто волнуюсь..."
    player_name "Ведь нас могут исключить за это!"
    show player locker 2
    show roxxy locker 2
    rox "Ты можешь успокоиться?"
    show roxxy locker 1
    show player locker 4
    player_name "..."
    show player locker 7
    player_name "Извини..."
    show player locker 2
    "Лязг!"
    show player locker 3
    pause
    ann "Ууууу, что это за тряпки?"
    show player locker 1
    player_name "Она приближается!"
    show player locker 8
    "Лязг!"
    show player_boner locker 1 with dissolve
    pause
    show roxxy locker 2
    rox "Эй, ты чег..."
    show player locker 9
    show player_boner locker 2
    show roxxy locker 4
    rox "!!!" with hpunch
    show roxxy locker 3
    rox "Это что такое?!"
    rox "Только не говори, что это твой..."
    show roxxy locker 4
    show player locker 5
    player_name "..."
    "Лязг!"
    show player locker 3
    show roxxy locker 6
    rox "Я не поняла, это твой стояк что ли?!"
    show roxxy locker 5
    show player locker 7
    player_name "Я-я ничего не могу с этим сделать..."
    show player locker 5
    show roxxy locker 7
    rox "Как у тебя мог встать в такой момент?!"
    show roxxy locker 5
    show player locker 7
    player_name "Я без понятия! Я не могу его контролировать!"
    show player locker 5
    show roxxy locker 7
    rox "Попробуй получше..."
    show roxxy locker 8
    hide player_boner
    rox "{b}*глх*{/b}"
    rox "Он трётся об мою..."
    show roxxy locker 9
    show player locker 2
    player_name "Хватит ёрзать!"
    show player locker 1
    show roxxy locker 8
    "Лязг!"
    $ M_roxxy.set('sex speed', .6)
    show roxxy locker 8_9
    show player locker 9
    player_name "Ты делаешь только хуже!"
    show player locker 8
    rox "... Он трогает мою пи..."
    show player locker 9
    player_name "{b}Рокси{/b}, хватит!"
    show player locker 3
    player_name "... Твою мать."
    player_name "Думаю, что наш шкафчик - следующий..."
    show player locker 9
    player_name "Хватит тереться об него!"
    show player locker 8
    $ M_roxxy.set('sex speed', 2)
    show roxxy locker 8_9
    rox "Ааах... Ааааахх..."
    pause
    jud "{b}Энни!{/b}"
    show player locker 3
    jud "Помоги мне открыть шкафчик..."
    ann "Ты сейчас серьёзно?"
    ann "Ты - заноза в моей заднице, понимаешь?"
    jud "Да я понимаю, прости..."
    ann "В последний раз в открываю твой шкафчик!"
    jud "..."
    jud "А зачем ты осматриваешься чужие шкафчики?"
    show player locker 4
    ann "Тебя это не касается!"
    pause
    ann "Всё, открыла, доставай свои вещи и..."
    ann "Что это такое?!"
    show player locker 8
    jud "..."
    ann "Это отвратительно!"
    ann "Что с тобой не так?!"
    jud "Ну я..."
    ann "Хранить пищу в шкафчиках строго запрещено!"
    show player locker 3
    ann "Я напишу на тебя докладную!"
    jud "... Но..."
    ann "Не оправдывайся, пошли!"
    ann "Я отведу тебя к {b}миссис Смит{/b}!"
    show player locker 9
    ann "Я надеюсь, что наказание исправит твои привычки!"
    jud "Н-наказание?"
    ann "Шевелись!"
    jud "... Что за наказание?!"
    pause
    $ M_roxxy.set('sex speed', .4)
    show roxxy locker 8_9
    rox "Ммм..."
    show player locker 7
    player_name "{b}*Вздох*{/b} Пожалуйста... остановись."
    player_name "Я думаю, что {b}Энни{/b}... {b}*Выдох*{/b}... Энни ушла!"
    show player locker 8
    rox "Аааааах!"
    show player locker 7
    player_name "{b}Рокси{/b}?"
    player_name "Ты что делаешь? Нам надо валить отсюда!"
    show player locker 9
    rox "Замолчи-замолчи-замолчи-замолчи..."
    $ M_roxxy.set('sex speed', .2)
    show roxxy locker 8_9
    player_name "Это же..."
    show player locker 9
    show roxxy locker 10
    rox "Ахххнх..." with hpunch
    show player locker 8
    player_name "!!!"
    rox "Ах... Ахах..."
    rox "Твою мать!"
    rox "Это же сейчас..."
    show player locker 5
    player_name "..."
    show player locker 6
    player_name "{b}Рокси{/b}, нам надо сваливать отсюда, пока {b}Энни{/b} не вернулась!"
    show player locker 5
    show player_boner locker 2
    show roxxy locker 2
    with dissolve
    rox "Д-да... Конечно..."
    rox "Просто... Помоги мне... У меня ноги затекли..."
    scene black with fade
    scene school
    show roxxy 1k at right
    show player 10 at left
    with dissolve
    player_name "Это было близко!"
    show player 5
    rox "..."
    show roxxy 1l
    rox "Фух, это было..."
    show roxxy 1m
    pause
    show roxxy 86 at left
    hide player with hpunch
    pause
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ох!"
    show player 12
    player_name "Что это сейчас было?!"
    show player 90
    show roxxy 3c
    rox "А у кого стояк в самый подходяший момент появился?!"
    show roxxy 3d
    show player 10
    player_name "А я-то что?!"
    player_name "Оно всё само!"
    show player 12
    player_name "Ты сама начала ёрзать на нём!"
    show player 90
    show roxxy 3b
    pause
    show roxxy 86 at left
    hide player
    rox "Замолчи!" with hpunch
    show roxxy 3b at right
    show player 15 at left
    with dissolve
    player_name "Ай! Хватит меня бить!"
    show player 16
    show roxxy 3
    rox "Даже не смей рассказывать кому-то о том, что было в этом шкафчике!"
    show roxxy 3c
    rox "Ты меня понял?!"
    show roxxy 3b
    show player 12
    player_name "Да, я понял!"
    player_name "Просто будь аккуратнее на экзамене с этими ответами..."
    show player 90
    show roxxy 3
    rox "Я-то буду аккуратной на экзамене!"
    rox "Это тебе надо быть аккуратнее с языком, чтобы ничего не ляпнуть!"
    rox "Если кто-нибудь узнает об этом, то тебе крышка!"
    show roxxy 29f with dissolve
    show player 12
    player_name "{b}*Вздох*{/b} Ты слишком зависима от мнений других людей... Ты же знаешь это?"
    show player 90
    show roxxy 30f
    rox "Просто замолчи, {b}[firstname]{/b}..."
    show roxxy 29f
    show player 12
    player_name "Хорошо. Я пошёл на свой урок..."
    player_name "Увидимся, {b}Рокси{/b}."
    show player 90
    rox "..."
    show roxxy 30f
    rox "Пока."
    hide player
    hide roxxy
    with dissolve
    show roxxy 29f
    rox "..."
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "Шикарные ощущения..."
    rox "Он такой..."
    rox "... Огромный!"
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Кто знал, что он прячет от всех такой кабачок?"
    show roxxy 32 with dissolve
    pause
    show roxxy 33
    rox "... Может быть, я и действительно сильно зависима от чужих мнений..."
    rox "Я имею ввиду, что мешает мне начать встречаться с ним?"
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "Господи, я только что поняла..."
    rox "{b}Мисси{/b} была права по поводу того, что у всех задротов огромные члены."
    show roxxy 84 with dissolve
    rox "..."
    rox "Ох, а если она это узнает... Ну и ну!"
    hide roxxy with dissolve
    return

label school_roxxy_dexter_flirt:
    scene school
    show player 13f at right
    show dewitt 43 at left
    with dissolve
    dewitt "О, {b}[firstname]{/b}. Ты как раз вовремя!"
    show dewitt 42
    show player 14f
    player_name "Ох, {b}мисс Девитт{/b}."
    player_name "Ух ты, как много всего!"
    show player 13f
    show dewitt 41
    dewitt "Будь другом, сходи в актовый зал и проверь там всё!"
    dewitt "У меня сейчас просто лекция по акустическим инструментам..."
    show dewitt 42
    show player 14f
    player_name "Да, конечно."
    show player 13f
    show dewitt 43
    dewitt "Ох, спасибо, сладенький!"
    hide dewitt
    show player 642f
    with dissolve
    pause
    player_name "( Хмм, {b}актовый зал{/b} в конце {b}правого коридора на первом этаже{/b}. )"
    player_name "( {b}Я должен сходить туда!{/b} )"
    hide player with dissolve
    return

label school_roxxy_do_pushups_intro:
    scene school
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "{b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Эй, {b}Эрик{/b}."
    player_name "Как дела, чувак?"
    show player 13
    show erik 4
    eri "Ох, знаешь... Нормально."
    eri "Вчера рейдил подземелье, и опять порвал ширинку!"
    show erik 1
    show player 12
    player_name "Ширинку?"
    show player 13
    show erik 4
    eri "Да, чувак. Зелёные девушки очень любят... Не суть важно..."
    show erik 1
    show player 17
    player_name "... Ахаха, окей, чувак."
    show player 13
    show erik 4
    eri "Как всё прошло на конкурсе бикини?"
    show erik 1
    show player 14
    player_name "Всё было превосходно!"
    player_name "Тебе следовало бы пойти со мной..."
    show player 13
    show erik 4
    eri "То есть ты видел {b}Рокси{/b} в обтягивающем бикини?"
    show erik 1
    show player 14
    player_name "Ты даже представить себе не можешь!"
    player_name "Она так сексуально выглядела!!"
    show player 13
    show erik 4
    eri "Класс!"
    eri "Она действительно тебе нравится?"
    show erik 1
    show player 14
    player_name "... Да. Она довольно хорошая личность."
    player_name "Правда, с первого взгляда этого и не увидишь..."
    show player 13
    show erik 4
    eri "Ахаха!"
    eri "Она даже стала со мной здороваться по утрам..."
    show erik 1
    show player 12
    player_name "Серьёзно?"
    show player 13
    show erik 3b
    eri "Я имею ввиду, что она не знает моего имени..."
    show erik 4
    eri "Но зато она не называет меня задротом или жиртрестом!"
    show erik 1
    show player 14
    player_name "Эх!"
    show player 13
    show erik 4
    eri "Нет, серьёзно, это большой прогресс!"
    eri "Ты ей тоже, наверное, нравишься, {b}[firstname]{/b}!"
    show erik 1
    show player 14
    player_name "Даже не знаю..."
    show player 13
    show erik 4
    eri "Да ладно тебе!"
    eri "Раньше она даже не разговаривала с нами!"
    eri "А теперь она приглашает тебя на вечеринку с её подружками!"
    show erik 1
    show player 5
    player_name "..."
    show player 10
    player_name "Мы же сейчас опоздаем на урок физкультуры!"
    show player 5
    show erik 3b
    eri "Ох, чёрт! Ты прав!"
    show erik 4
    eri "Пошли, можешь рассказать мне о конкурсе бикини по дороге!"
    hide player
    hide erik
    with dissolve
    scene gym
    show player 13 at left
    show erik 3b zorder 1
    with dissolve
    eri "У неё порвался лифчик?"
    show erik 1
    show player 14
    player_name "Имеено!"
    show player 13
    show erik 3b
    eri "Стой... Ты видел её..."
    show erik 1
    show player 14
    player_name "Да, её сиськи!"
    show player 13
    show erik 4
    eri "... Ох!"
    show erik 1
    show player 14
    player_name "Но это не так уж и важно!"
    show player 13
    show erik 4
    eri "Ох, чувак!"
    eri "Это же шикарно!"
    eri "Вот на твоём месте я бы..."
    show erik 1b
    show dexter 15 zorder 0 at right
    with dissolve
    show player 90
    dex "Свали, поросёночек."
    show dexter 14
    show erik 5b
    eri "А?"
    show erik 5b
    show player 12
    player_name "Оставь нас в покое, {b}Декстер{/b}..."
    show player 90
    show dexter 15
    dex "СВАЛИЛ ОТСЮДА, ЖИРОБАСИНА!"
    hide erik
    show dexter 21c
    with dissolve
    pause
    show dexter 21d with dissolve
    pause
    show dexter 14 with dissolve
    show player 15
    player_name "Что за чертовщина, чувак?!"
    show player 16
    show dexter 15 with dissolve
    dex "Я тебе разве не говорил отстать от {b}Рокси{/b}?!"
    show dexter 14
    show player 5
    player_name "..."
    show dexter 15
    dex "А теперь я узнаю, что ты тусовался с ней на пляже?!?!"
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Мне что, надо тебе в табло дать, чтобы ты понял?!"
    show dexter 14 with dissolve
    show player 12
    player_name "Отвали, {b}Декстер{/b}!"
    player_name "Она сама меня позвала."
    show player 90
    show dexter 12 with dissolve
    dex "Пфф, ага!"
    dex "Зачем ей тусоваться с таким неудачником, как ты?"
    show dexter 11
    show player 12
    player_name "Это я неудачник?!"
    player_name "Это ты лапаешь девушек без их разрешения, потому что сам ни на что не способен!"
    show player 90
    show dexter 15 with dissolve
    dex "Что ты сейчас сказал, засранец?!"
    show dexter 14
    show player 15
    player_name "... Ты прекрасно всё слышал!"
    show player 12
    player_name "Ты жалок, {b}Декстер{/b}!"
    show player 90
    show dexter 21b at Position (xpos=950) with dissolve
    dex "Тебе крышка, {b}[firstname]{/b}!"
    show dexter 14
    show coach 3f with dissolve
    bri "Что за чертовщина тут происходит?!"
    show coach 1 with dissolve
    show dexter 11
    dex "!!!"
    show player 12
    player_name "Н-ничего, мэм!"
    show player 90
    show coach 3
    bri "Это не выглядит, как ничего!"
    show coach 3f with dissolve
    bri "{b}Декстер{/b}, сколько раз я тебе буду повторять, что драться в школах нельзя?!"
    show coach 1f
    show dexter 22
    dex "Но мэм, он же сам напро..."
    show dexter 21
    show coach 4f
    bri "Я не хочу ничего слышать!" with hpunch
    bri "Если вам необходимо разрешить спор, то сделать это мирным путём..."
    show coach 1f
    show player 12
    player_name "... Каким? Просто поговорить?"
    show player 90
    show dexter 22
    dex "Я не понимаю..."
    show dexter 21
    show coach 4f
    bri "Отжимания!"
    show coach 1f
    show player 10
    player_name "А?!"
    show player 5
    show coach 4
    bri "Пятдесят отжиманий, сейчас же!" with hpunch
    show coach 1
    show player 11
    player_name "!!!"
    dex "!!!"
    show coach 3
    bri "Кто преуспеет, тот и выиграл спор!"
    show coach 1
    show dexter 12
    dex "Этот засранец не способен сделать пятьдесят отжиманий..."
    show dexter 11
    show player 12
    player_name "Бьюсь об заклад, что сделаю это быстрее тебя!"
    hide player with dissolve
    show dexter 12
    dex "Пфф, ага!"
    show dexter 11
    dex "..."
    hide dexter with dissolve
    pause
    show coach 5 with dissolve
    bri "Начали!"
    return

label school_roxxy_trailer_park_romance_intro:
    scene school
    show player 13 at left
    show roxxy 1b at right
    with dissolve
    rox "{b}[firstname]{/b}!"
    show roxxy 1
    show player 14
    player_name "О, {b}Рокси{/b}."
    player_name "Как дела?"
    show player 13
    show roxxy 1b
    rox "Я ждала тебя."
    show roxxy 1
    show player 10
    player_name "Ты ждала меня?"
    show player 5
    show roxxy 1b
    rox "Да, я думала, что мы можем вместе войти в класс."
    show roxxy 1
    show player 12
    player_name "Ты серьёзно?"
    show player 14
    player_name "Ой, я хотел сказать, что да, конечно. Я не против!"
    show player 13
    show roxxy 1b
    rox "Класс."
    show roxxy 1
    player_name "..."
    rox "..."
    show player 14
    player_name "Так ты забрала свой приз домой?"
    show player 13
    show roxxy 4
    rox "Да!"
    show roxxy 1b
    rox "Я поставила его в своей комнате."
    rox "До сих пор не могу поверить, что я победила..."
    show roxxy 1
    show player 14
    player_name "Да, ты сделала это!"
    player_name "У других девушек и шанса не было!"
    show player 13
    show roxxy 1b
    rox "Хех, правда?"
    show roxxy 1
    show player 14
    player_name "Конечно."
    player_name "Ты же выше их уровня."
    show player 13
    rox "..."
    show roxxy 1b
    rox "... Спасибо, {b}[firstname]{/b}."
    rox "Знаешь, я тут думала..."
    rox "... Если ты сегодня не занят..."
    show roxxy 1
    show player 5
    player_name "Хм?"
    show roxxy 2
    rox "... Может быть, встретимся сегодня?"
    show roxxy 1
    show player 10
    player_name "Ты хочешь встретиться со мной?"
    show player 5
    show roxxy 2
    rox "Только если ты будешь не против!"
    rox "... Просто я подумала... Может быть... Ты заглянешь ко мне домой?"
    show roxxy 1b
    rox "Я могу приготовить нам ужин!"
    rox "Знаешь... Как награда за твою помощь!"
    show roxxy 1
    show player 10
    player_name "Ты умеешь готовить?"
    show player 5
    show roxxy 2
    rox "Нет, не совсем..."
    show roxxy 1b
    rox "... Прости, я в этом не очень сильна."
    show roxxy 1
    show player 5
    player_name "Хм?"
    show player 10
    player_name "А что ты имела ввиду?"
    show player 5
    show roxxy 2
    rox "... Неважно."
    rox "Сделаем вид, что я ничего не говорила..."
    show roxxy 1
    return

label school_roxxy_trailer_park_romance_no:
    show player 10
    player_name "Знаешь, я бы не против, {b}Рокси{/b}, но у меня на вечер другие планы..."
    show player 5
    show roxxy 1l with dissolve
    rox "Ох, ладно..."
    rox "У меня тоже много дел, которыми мне стоит заняться."
    show roxxy 1k
    show player 12
    player_name "... Может бытЬ, в другой раз?"
    show player 5
    show roxxy 1l
    rox "Да, наверное. Посмотрим..."
    hide roxxy with dissolve
    pause
    show player 12
    player_name "Какая-то она сегодня странная..."
    hide player with dissolve
    return

label school_roxxy_trailer_park_romance_yes:
    show player 10
    player_name "Стой!"
    show player 14
    player_name "Я приду!"
    show player 13
    show roxxy 1b
    rox "Правда?!"
    show roxxy 1
    show player 14
    player_name "Определённо! Я просто немного впал в ступор с твоего вопроса..."
    show player 13
    show roxxy 2
    rox "Хех, да..."
    show roxxy 1
    player_name "..."
    rox "..."
    show roxxy 1b
    rox "Значит, встречаемся {b}после полудня{/b} у {b}меня дома{/b}?"
    show roxxy 1
    show player 14
    player_name "Да."
    show player 13
    show roxxy 4
    rox "Прекрасно! Только не забудь!"
    show roxxy 1
    show player 14
    player_name "Не забуду, хех."
    hide roxxy with dissolve
    pause
    show player 17
    player_name "( Ух ты, {b}вечерний ужин с Рокси у неё дома{/b}! )"
    player_name "( Наверное, мы окончательно стали друзьями! )"
    show player 13
    player_name "( Но почему она ведёт себя так странно? Не понимаю. )"
    hide player with dissolve
    return

label school_roxxy_dexter_basketball:
    scene school
    show player 5f with dissolve
    player_name "( Хмм, что-то {b}Декстера{/b} не видно... )"
    player_name "( Надеюсь, что он не видел, как я целуюсь с {b}Рокси{/b} )"
    player_name "( Он непременно закатит драку. )"
    show erik 4 at right
    eri "Как дела, чу..."
    show erik 5
    show player 6f at left
    player_name "Ааааа!!!" with hpunch
    show player 22 with dissolve
    eri "Ааа?!"
    show player 37 with dissolve
    eri "Какого..."
    show erik 3b
    player_name "Фух, прости, чувак."
    show player 38
    player_name "Ну ты меня и напугал!"
    show player 5 with dissolve
    show erik 5
    eri "А чего ты так испугался?"
    show erik 3b
    show player 10
    player_name "{b}*Вздох*{/b} Мне кажется, что {b}Декстер{/b} видел, как я целуюсь с {b}Рокси{/b}..."
    show player 5
    show erik 5
    eri "!!!" with hpunch
    eri "Ты целовался с {b}Рокси{/b}?!"
    show erik 51
    show player 38 with dissolve
    player_name "Шшш, не так громко!"
    show player 3
    show erik 53
    eri "Прости... Просто как-то неожиданно это слышать, ведь по сути дела..."
    show erik 4
    eri "Мой друг целовался с самой популярной девушкой в колледже!"
    show erik 1
    show player 5 with dissolve
    player_name "..."
    show player 12
    player_name "Наверное, ты не расслышал, что гигантский перекачанный громила видел, как я целуюсь с его бывшшей девушкой?"
    show player 5
    show erik 3b
    eri "А, точно."
    show erik 5
    eri "Да, не к добру это. {b}Декстер{/b} тебя уничтожит, чувак..."
    show erik 52
    show player 12
    player_name "Знаю. Поэтому я и на взводе."
    player_name "Я всё жду, когда он застанет меня врасплох, когда я буду входить в класс..."
    show player 5
    show erik 4
    eri "Не беспокойся, чувак: я тебя прикрою!"
    eri "Мы можем ходить вместе и я буду следить за тем, чтобы тебя никто не подловил."
    show erik 1
    show player 10
    player_name "Хех, спасибо, {b}Эрик{/b}..."
    show player 5
    show erik 5
    eri "Только учти, что если дело дойдёт до драки, то я стану гораздо бесполезнее."
    player_name "..."
    show erik 3b
    eri "Я серьёзно, чувак... Не суди меня слишком строго, если я обоссу штаны и убегу отсюда!"
    show erik 1
    show player 17
    player_name "Ахаха!"
    show player 13
    show erik 4
    eri "Пошли, у нас сегодня физкультура на {b}баскетбольной{/b} площадке. {b}Декстер{/b} ни за что не начнёт драку перед {b}физручкой Бриджет{/b}."
    show erik 1
    show player 10
    player_name "Да, думаю, что ты прав."
    hide player
    hide erik
    with dissolve
    scene basketball_b
    show kevin 23f at Position (xpos=500)
    show erik 52f at Position (xpos=300)
    show player 5 at left
    show coach 15b at right
    with dissolve
    bri "... Итак, ребята: я знаю, что вы видели, как играют профессионалы по телевизору..."
    bri "... Дриблинг между их ног и обводы за спиной!"
    show coach 15c
    bri "Это всё глупости!" with hpunch
    show coach 15b
    bri "Весь баскетбол - в основах!"
    bri "Интеллектуальная игра с точным исполнением..."
    show coach 15
    show kevin 32f
    kev "... И смешные подачи с трёхочковой линии!"
    show kevin 23f
    player_name "..."
    eri "..."
    show coach 15b
    bri "Ох, то есть для тебя это всё большая шутка, да?"
    show coach 15
    show kevin 34f with dissolve
    kev "{b}*Глык*{/b} ... Я не это имел ввид..."
    show kevin 23f with dissolve
    show coach 15b
    bri "Нет, нет, нет. Это моя вина..."
    bri "... Я не понимала, что ты слишком хорош для обычного баскетбола..."
    show coach 15
    show kevin 34f with dissolve
    kev "Да нет, я не..."
    show kevin 34bf
    show coach 15c
    bri "Почему бы тебе не пробежать вокруг площадки кружок-другой, пока класс будет смотреть на это, а?"
    show coach 15
    kev "!!!"
    show kevin 24f with dissolve
    kev "... Но мэм..."
    show kevin 24bf
    show coach 15b
    bri "Тебе этого мало?"
    bri "Можем собраться здесь после уроков, если тебе этого мало."
    show coach 15
    show kevin 24f
    kev "{b}*Вздох*{/b} Нет, мэ-эм..."
    show kevin 24bf
    show coach 15b
    bri "Хорошо."
    show coach 15c
    bri "Вперёд!" with hpunch
    show coach 16
    hide kevin
    with dissolve
    pause
    show coach 15b with dissolve
    bri "Так, где я остановилась?"
    show coach 15
    show player 10
    player_name "Основы баскетбола, мэм!"
    show player 5
    show coach 15b
    bri "Ах, да!"
    bri "Итак, весь баскетбол заключается в основ..."
    show coach 15
    show player 22
    dex "Вот ты где, задротишка!" with hpunch
    show player 23
    player_name "Чёрт..."
    show player 22
    show erik 5f
    eri "Только не это..."
    show erik 51f
    show dexter 14 at right with dissolve
    show coach 15b
    bri "Что происходит?!"
    show coach 15
    show dexter 15
    dex "Думал, что я тебя не найду, сучёнок?!"
    show dexter 14
    show coach 15c
    bri "Не поняла?! {b}Декс{/b}..."
    show coach 15
    show dexter 13 at Position (xoffset=-18) with dissolve
    dex "Свалил с дороги, жиробасина, или я выбью из тебя эти веснушки!" with hpunch
    show erik 64f with fastdissolve
    show erik 65f with fastdissolve
    show erik 66f with fastdissolve
    hide erik
    show dexter 15
    with dissolve
    dex "Я видел тебя и эту шлюху, так называемую бывшую девушку!"
    show dexter 14
    show player 15
    player_name "Эй, не смей так говорить о {b}Рокси{/b}!"
    show player 16
    show dexter 15
    dex "Я буду говорить то, что я хочу!"
    dex "Что ты посмеешь мне сделать, ЗАДРОТ?!"
    show dexter 14
    show player 11 at Position (xpos=-150)
    show coach 15cf at left
    bri "Хватит, {b}Декстер{/b}, сейчас самое время, чтобы остановиться!" with hpunch
    bri "Ибо я не позволю, чтобы эти разборки проходили посреди урока!"
    show coach 15f
    show dexter 15
    dex "... Но {b}учитель{/b}, вы же не понимаете!"
    dex "Этот кусок говна..."
    show dexter 14
    show coach 15cf
    bri "Я не хочу ничего слышать, {b}Декстер{/b}!"
    bri "Ты знаешь правила на моих уроках!"
    bri "Мы всё решаем здесь без насилия!"
    show coach 15f
    show dexter 15
    dex "Нет, пока я не разберусь с этим гадом, я не успокоюсь..."
    show dexter 14
    show coach 17f with dissolve
    player_name "..."
    show coach 1f
    show dexter 29
    with dissolve
    dex "Хмм..."
    show coach 2f
    bri "Так разберись с ним в баскетболе!"
    hide coach
    show player 16 at left
    with dissolve
    show dexter 30
    dex "В смысле?.."
    show dexter 29
    show player 12
    player_name "Она сказала, что нам стоит решить проблему, сыграв в баскетбол... придурок."
    show player 16
    dex "!!!"
    show dexter 30
    dex "Всё, тебе конец..."
    show dexter 33
    show player 647
    with dissolve
    dex "Отлично!"
    show dexter 15 with dissolve
    dex "Твой мяч, ЗАДРОТ!"
    hide player
    hide dexter
    with dissolve
    return

label school_roxxy_fight_dexter:
    scene expression game.timer.image("outside_school{}")
    show player 12 with dissolve
    player_name "Мне стоит убедиться, что я готов к драке, перед тем, как войду в школу."
    player_name "Нет никаких сомнений в том, что {b}Декстером{/b} сейчас правит жажда крови из-за вчерашней оказии на баскетбольной площадке."
    show player 4 at Position (xoffset=7) with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Мне нужна хорошая {b}ловкость{/b}, чтобы уворачиваться от его атак, и хорошая {b}сила{/b}, чтобы дать ему отпор."
    player_name "В противном случае, у меня не будет шанса..."
    show player 5
    player_name "..."
    show player 38 at Position (xoffset=51) with dissolve
    player_name "Готов ли я или нет?.."
    show player 3 at Position (xoffset=26) with dissolve

    return

label school_roxxy_locker_sex:
    scene expression "backgrounds/location_school_locker_room_backpack_day_blur.jpg"
    show becca 6 at Position (xpos=315)
    show roxxy 1g at Position (xpos=600)
    show missy 7 at left
    with dissolve
    becca "... И как тебе?"
    show becca 5
    show roxxy 1h
    rox "Просто. Крышесносно."
    show roxxy 1g
    show missy 5
    missy "Мммххх, я намокаю, как только думаю об этом..."
    show missy 7
    show roxxy 1h
    rox "Я не знаю, что сказать... Это неописуемые ощущения!"
    show roxxy 1g
    show becca 2
    becca "... Больно же?"
    show becca 1
    show roxxy 2
    rox "Да, сначала очень даже!"
    show missy 3
    show roxxy 1b
    rox "... Но потом боль пропадает..."
    show roxxy 1h
    rox "... и лишь немного поднывает, но при этом ты испытываешь космические ощущения!"
    show roxxy 1g
    show becca 5
    becca "Ммм..."
    show missy 8
    missy "Ох, как же возбуждающе!"
    show missy 7
    show becca 3b
    becca "Даже звучит невероятно..."
    show becca 5
    show roxxy 1h
    rox "Вы и представить себе такого не можете!"
    show roxxy 1g
    becca "..."
    show missy 8
    missy "Ну так... А когда нам можно будет с ним... позабавиться?"
    show roxxy 2b
    show missy 7
    show becca 3b
    becca "{b}Мисси{/b}!!!"
    show becca 3
    show missy 8
    missy "... Что?!"
    show roxxy 3d
    missy "Не говори только, что ты об этом не думала!"
    show missy 7
    show becca 26 with dissolve
    becca "..."
    show becca 24 with dissolve
    show roxxy 3c
    rox "... Вы серьёзно?!"
    rox "Он {b}МОЙ{/b} парень так-то! Почему я должна разрешать вам трахаться с ним?!"
    show roxxy 3d
    show missy 1b
    missy "Потому что... мы твои лучшие подруги?"
    show missy 8
    missy "... Кроме того, мы знаем, что это тебя заводит..."
    show missy 7
    show roxxy 2b
    rox "!!!" with hpunch
    show roxxy 3c
    rox "О чём вы говорите, а?!"
    show roxxy 3d
    show missy 8
    missy "Пфф, да ладно тебе!"
    show missy 7
    show becca 25
    becca "Мы прекрасно видели, как ты наяривала себе, когда мы играли в бутылочку на пляже... {b}Рокси{/b}..."
    show becca 24
    show roxxy 2c
    rox "... Не было такого!"
    show roxxy 2b
    show missy 1b
    missy "Было!"
    show missy 7
    show becca 25
    becca "Это было очень даже заметно..."
    show becca 24
    show roxxy 29
    rox "..."
    show roxxy 30
    rox "Ла-адно. Хорошо."
    show roxxy 3c
    rox "Признаюсь, что в тот раз мне действительно снесло крышу."
    rox "Но это не означает, что я позволю вам трахаться с моим парнем..."
    show roxxy 3d
    show becca 25
    becca "..."
    show missy 4
    missy "Почему?!"
    show missy 2b
    show roxxy 3
    rox "Потому что он {b}мой парень{/b}!"
    rox "Не ваш! {b}МОЙ{/b}!"
    show roxxy 3b
    becca "..."
    show missy 8
    missy "Да, но..."
    missy "Только представь, {b}Рокси{/b}."
    missy "{b}Голая{/b} Бекка... Лежит на спине... Её бледноватые, веснушчатые сиськи так и ждут, чтобы в них..."
    show missy 7
    show roxxy 1
    show becca 27 with dissolve
    becca "Чтобы в них что?! Что ты несёшь?!"
    show becca 26
    show missy 4
    missy "Умолкни! Я просто пытаюсь представить!"
    show missy 2b
    rox "..."
    show missy 8
    missy "{b}[firstname]{/b} достаёт свой болт, трёт им об её клитор, и та умоляет его, чтобы он вошёл в неё..."
    show missy 7
    becca "..."
    show roxxy 1b
    rox "... Я слушаю."
    show roxxy 1
    show missy 8
    missy "{b}*Вздох*{/b}!!!"
    show missy 7
    show becca 27
    becca "Что?!"
    show becca 26
    show missy 8
    missy "{b}Бекка{/b} молит о том, чтобы он вошёл в неё..."
    show missy 7
    show becca 27
    becca "Серьёзно?!"
    show becca 26
    show missy 4
    missy "Давай, сделай это! Не подведи меня!"
    show missy 2b
    show becca 24 with dissolve
    becca "..."
    show becca 25
    becca "Разреши мне сделать это, {b}Рокси{/b}..."
    show missy 7
    show roxxy 4
    rox "Ахаха, ты правда будешь умолять меня об этом, {b}Бекка{/b}?"
    show roxxy 1
    show becca 25
    becca "... Не знаю."
    show becca 24
    show missy 8
    missy "Ох, само собой! Посмотри, как она завелась, только подумав об этом..."
    show missy 7
    show becca 27 with dissolve
    becca "Нет!"
    show becca 26
    show missy 8
    missy "Да ты дышишь, как после пятикилометрового кросса!"
    show missy 7
    becca "..."
    show becca 24 with dissolve
    show roxxy 1g
    rox "Хмм."
    show roxxy 1h
    rox "... А что насчёт тебя?!"
    show roxxy 1g
    show becca 26 with dissolve
    show missy 1b
    missy "Меня?!"
    show missy 1
    show roxxy 1h
    rox "Ты же тоже будешь меня упрашивать?"
    show roxxy 1g
    show missy 8
    missy "Да я сделаю всё, что угодно, лишь бы заняться этим!"
    missy "Хочешь, чтобы я тебя умоляла? Я буду."
    missy "Буду ласкать твою грудь или вылизавать твою пизду... Чёрт, да я даже твою жопу съесть готова!"
    missy "Только позволь мне прокатиться на его члене!"
    show missy 7
    show roxxy 4
    rox "Ахахаха!"
    show roxxy 1g
    show missy 8
    missy "Ну признай же, что это нереально заводит!"
    missy "Твои личные сучки, которые готовы сделать всё, лишь бы заполучить член твоего парня..."
    show missy 7
    show becca 27
    becca "Я не буду есть её жопу..."
    show becca 26
    show missy 2
    missy "Пфф, ты будешь, {b}Бекка{/b}. Не надо мне тут!"
    show missy 7
    show becca 24 with dissolve
    becca "..."
    show roxxy 1h
    rox "И вы ведь действительно думали об этом..."
    show roxxy 1h
    show missy 6
    missy "Гораздо больше, чем ты можешь себе это представить!"
    show missy 7
    rox "..."
    show missy 8
    missy "Так что скажешь?!"
    show missy 7
    rox "..."
    show roxxy 1g
    rox "... Может быть."
    show roxxy 1h
    show missy 3
    show becca 2
    becca "!!!"
    show missy 1b
    missy "{b}*вдох*{/b} Правда?!"
    show missy 1
    show roxxy 1b
    rox "Только надо кое-что обговорить..."
    rox "... Например, вы будете полностью подчиняться мне!"
    show roxxy 1g
    show missy 1b
    missy "Я полностью согласна!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Бекка{/b}?"
    show roxxy 1
    show missy 7b with dissolve
    becca "!!!"
    show missy 1 with dissolve
    show becca 25
    becca "... Да, я сделаю всё, что ты скажешь."
    becca "Без лишних слов..."
    show becca 24
    show roxxy 1h
    rox "... Даже если я скажу, чтобы ты взяла в рот его кончу и проглотила??"
    show roxxy 1g
    show missy 4
    missy "Да чёрт, да! Хорошо!"
    show missy 1b
    missy "Всё, что ты захочешь, {b}Рокси{/b}! Я твоя рабыня!"
    show missy 1
    becca "..."
    show roxxy 1b
    rox "{b}Бекка{/b}?"
    show roxxy 1g
    show becca 25
    becca "... Хорошо, я..."
    show becca 24
    show roxxy 1h
    rox "Что ты?"
    show roxxy 1g
    show becca 25
    becca "Я буду твоей рабыней тоже, ясно?!"
    show becca 24
    show roxxy 4
    rox "Ахаха!"
    show roxxy 1h
    rox "... Хмм, я подумаю над этим."
    show roxxy 1g
    show missy 7
    missy "..."
    becca "..."
    show roxxy 1b
    rox "А теперь, если позволите..."
    show roxxy 1h
    rox "Я пойду поищу {b}своего парня{/b}!"
    hide roxxy with dissolve
    pause
    show becca 1f at Position (xpos=400) with dissolve
    show missy 4
    missy "Да чёрт, я надеялась, что она сразу же согласится..."
    show missy 2b
    show becca 2f
    becca "... Я тоже."
    show becca 1f
    show missy 1b
    missy "Я же знала, что ты согласишься!"
    show missy 1
    show becca 2f
    becca "Заткнись!"
    show becca 1f
    show missy 8
    missy "Ты такая шлюха..."
    show missy 7
    show becca 2f
    becca "Ну и пусть... Но не такая шлюха, как ты!"
    show becca 1f
    show missy 5
    missy "Да и похер."
    show missy 2
    missy "Если что, то моя шлюховатость обеспечивает нам доступ к члену такого человека, как {b}[firstname]'s{/b}!"
    missy "Ты ещё меня благодарить должна!"
    show missy 2b
    show becca 7f
    becca "..."
    hide becca
    hide missy
    with dissolve

    scene school
    show player 13 at left
    with dissolve
    show roxxy 1b at right with dissolve
    rox "Вот ты где!"
    show roxxy 1
    show player 14
    player_name "О, {b}Рокси{/b}!"
    player_name "Чем занимаешься?"
    show player 13
    show roxxy 1h
    rox "Да вот, думала о тебе..."
    show roxxy 1g
    show player 14
    player_name "Серьёзно?"
    player_name "Обо мне?"
    show player 13
    show roxxy 1h
    rox "Ох, знаешь... Какой же ты сильный и мужественный..."
    rox "... И знаешь, я бы с удовольствием поскакала на твоём члене прямо сейчас!"
    show roxxy 1g
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Чего?! Мы не можем заняться этим здесь..."
    player_name "Мы же в колледже!"
    show player 5
    show roxxy 4
    rox "Хехехе, да не бойся!"
    show roxxy 1h
    rox "Нас никто не увидит..."
    show roxxy 1g
    show player 11
    player_name "..."
    show roxxy 1g
    rox "У меня есть план!"
    hide roxxy with dissolve
    show player 12
    player_name "Какого..."
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "И снова {b}Рокси{/b} запихнула меня в шкафчик, как какую-то куклу!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 1
    show roxxy locker 1b
    with dissolve
    player_name "Шикарно, мы снова в моём шкафчике..."
    show player locker 2
    show roxxy locker 1
    rox "Хехе, закрой рот и доставай свой хуй!"
    show roxxy locker 1b
    show player locker 7
    player_name "Ты сейчас серьёзно?!"
    show player locker 5
    show roxxy locker 1
    rox "Ещё бы!"
    rox "Я хочу, чтобы ты вошёл в меня!"
    show roxxy locker 1b
    show player locker 6
    player_name "Чего это ты так завелась?!"
    show player locker 5
    show roxxy locker 1
    rox "Ммм, скоро сам узнаешь."
    show roxxy locker 1b
    show player locker 11 with dissolve
    player_name "..."
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "... Но сейчас я хочу сосредоточиться на..."
    show player locker 14 with dissolve
    pause
    rox "... На ебле с тобой!"
    player_name "Х-хорошо..."
    show player locker 15
    rox "!!!" with hpunch
    rox "Ааааах..."
    return

label school_roxxy_locker_sex_repeat:
    scene school
    show player 12 with dissolve
    player_name "... Чёрт, и где она?!"
    show player 4 with dissolve
    rox "Пшшшш!"
    show player 11f
    player_name "!!!" with hpunch
    hide player with fastdissolve

    scene expression "backgrounds/location_school_cutscene06.jpg"
    with fade
    show text "И снова {b}Рокси{/b} запихнула меня в шкафчик, как какую-то куклу!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я же не её игрушка, верно?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression "backgrounds/location_school_locker_inside01.jpg"
    show player locker 8
    show roxxy locker 1
    with dissolve
    rox "Наконец-то! Я начал думать, что ты обманула меня!"
    show roxxy locker 1b
    show player locker 6
    player_name "Серьёзно, ты хочешь сделать это снова?!"
    show player locker 5
    show roxxy locker 1
    rox "Именно!"
    show roxxy locker 1b
    show player locker 6
    player_name "Ты понимаешь, что будет, если нас застанут врасплох?!"
    show player locker 5
    show roxxy locker 1
    rox "Да, нас выгонят отсюда!"
    show roxxy locker 1b
    player_name "... Именно!"
    show player locker 11 with dissolve
    pause
    show player locker 12 with dissolve
    pause
    hide roxxy
    show player locker 13
    with dissolve
    rox "Так что давай не будем палиться..."
    show player locker 14 with dissolve
    player_name "... Почему тебя это не вол..."
    rox "{b}[firstname]{/b}, закрой рот и еби меня!"
    show player locker 15
    player_name "Хорошо!" with hpunch
    return

label roxxy_locker_sex_loop_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    $ M_roxxy.set("sex speed", .09)
    show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker with dissolve
    return

label roxxy_locker_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("roxxys_locker", [1,2,3,4,5,6,7,8,9,10], M_roxxy) as roxxys_locker
            pause 5
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_locker {}".format(pose_list[pose_counter]) as roxxys_locker
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("roxxy_locker_hscene_dialog")
        $ animcounter += 1
    if M_roxxy.get("roxxy locker sex first"):
        $ M_roxxy.set("roxxy locker sex first", False)
    call screen roxxy_locker_sex_options

label roxxy_locker_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "Шшш!!!"
            player_name "Потише, а то нас услышат!"
            rox "Я знаю!"
            rox "Это не так просто, знаешь ли!"
            player_name "Тогда давай прекратим и займёмся этим вечером!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                rox "Ммм, как же я обожаю твой хуй!"
                player_name "Шшш!!"
                rox "{b}*хнн*{/b}"

            elif random_count > 66:
                rox "Аааах!!"

    elif animcounter == 1:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Mmm..."

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count <= 33:
                rox "Ммм, какая же тут жаркая обстановка!"
                player_name "... Да, я знаю."
                player_name "Я вспотел, как не знаю кто!"
                rox "Э! Я не это имела ввиду!"
                player_name "..."
                rox "Я имела ввиду, что кто-то может нас спалить!"
                player_name "..."
                rox "Ох, ну и ну!"
                player_name "Ты иногда себя очень странно ведёшь..."
                rox "Хех, лучше рот закрой и ускорь темп!"

            elif random_count > 66:
                rox "Охх, глубже, {b}[firstname]{/b}!"
                player_name "..."
                rox "Быстрее, жёстче!!"
        else:

            rox "{b}[firstname]{/b}!!!"

    elif animcounter == 2:
        if M_roxxy.get("roxxy locker sex first"):
            player_name "{b}Рокси{/b}!!!"
            rox "Заткнись и трахай меня!"
            player_name "..."
            player_name "Ладно!"
            $ M_roxxy.set("sex speed", .06)
            rox "Fuuuuuck..." with hpunch
            player_name "Тише, прошу!"
            rox "{b}*вдох*{/b}"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "Ай!"
                rox "... Что?!"
                player_name "Я бошкой об верх шкафчика ударился!"
                rox "Ахаха, не заплачь только!"
                player_name "Да блин, это больно!"
                rox "Ага, но и ты мои волосы цепляешь... Ты не слышишь, как я жалуюсь?"
                player_name "... Почему ты просто не сказала про это? Я бы перестал!"
                rox "{b}*Глык*{/b} Не смей останавливаться!"
                rox "Давай ещё сильнее!"

            elif random_count > 66:
                player_name "Шшш! Нас же услышат!"
                rox "Да пофигу!"
                rox "Пусть слышат!"
                rox "Пусть знают, как мне классно!!!"
                player_name "Твоб мать, {b}Рокси{/b}!"
                player_name "Нас выгонят отсюда!"
                rox "{b}*Вздох*{/b}"
                rox "... Хорошо."
        else:

            rox "Боже, боже, О, ГОСПОДИ!!!"

    elif animcounter == 3:
        if M_roxxy.get("roxxy locker sex first"):
            rox "Не могу... Ааааа.... ААААА!"
            player_name "Закрой рот и кончи наконец-то!"

        elif not M_roxxy.get("roxxy locker sex first"):
            if random_count > 33 and random_count <= 66:
                player_name "..."
                rox "Ммм! Ааааааа, бляяяяядь!!!"
        else:

            if random_count > 50:
                rox "Ахахах, я уже близко!"
                player_name "Класс, я тоже!"
    return

label roxxy_locker_sex_cum:
    call expression game.dialog_select("roxxy_locker_sex_cum_pre")
    if M_roxxy.get("roxxy locker sex"):
        call expression game.dialog_select("roxxy_locker_sex_cum_repeat")
    else:

        call expression game.dialog_select("roxxy_locker_sex_cum_first")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roxxy"]["unlocked"] = True
    $ persistent.cookie_jar["Roxxy"]["gallery"]["05_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_locker_sex)
    $ player.go_to(L_school_hall)
    $ game.timer.tick()
    $ game.main()

label roxxy_locker_sex_cum_pre:
    scene expression "backgrounds/location_school_locker_inside01.jpg"
    hide roxxy
    show player locker 15_15b
    player_name "ТХ!" with flash
    rox "!!!"
    rox "{b}*Глык*{/b}!!!"
    pause
    show player locker 16 with dissolve
    return

label roxxy_locker_sex_cum_first:
    player_name "Всё в порядке?"
    show player locker 17b with dissolve
    rox "Хааах... Хаах..."
    rox "Да... Дай пару секунд..."
    rox "Фух."
    show player locker 17
    player_name "Это было сумасшедше!"
    show player locker 17b
    rox "Ага, но согласись, что была классно?"
    show player locker 17
    player_name "Хех, да..."
    show player locker 17b
    rox "Думаю, что стоит это повторить!"
    show player locker 17
    player_name "А?! Нет!"
    player_name "А если нас поймают?!"
    show player locker 17b
    rox "Хехе! Надо просто быть аккуратнее..."
    show player locker 17
    player_name "..."
    show player locker 17b
    rox "Давай, натягивай свои труссы с шортами и вылазь отсюда, пока в коридоре никого нету!"
    show player locker 17
    player_name "{b}*вздох*{/b}."
    scene black with fade

    scene school
    show player 14 at left
    show roxxy 1g at right
    with dissolve
    player_name "Серьёзно, из-за чего ты так завелась?"
    show player 13
    show roxxy 4
    rox "Хехе, не скажу!"
    show roxxy 1g
    show player 14
    player_name "Почему?!"
    show player 13
    show roxxy 1h
    rox "... Потому что это будет сюрпризом для тебя!"
    show roxxy 1g
    show player 12
    player_name "А?"
    player_name "Что именно за сюрприз?"
    show player 13
    show roxxy 1h
    rox "Хехе, этого заслуживает {b}только мой парень{/b}..."
    show roxxy 1g
    show player 11
    player_name "..."
    show player 13
    show roxxy 1b
    rox "Просто приходи на {b}вечеринку{/b} в эти выходные!"
    show roxxy 1g
    show player 14
    player_name "{b}Вы с девчонками снова будете тусоваться на пляже?{/b}."
    show player 13
    show roxxy 1h
    rox "Всегда!"
    show roxxy 1g
    show player 14
    player_name "Так что, в {b}субботу вечером{/b} на {b}пляже{/b}?"
    show player 13
    show roxxy 1b
    rox "Угу."
    rox "Не опаздывай!"
    show roxxy 1
    show player 14
    player_name "Хех, хорошо."
    show player 13
    show roxxy 1h
    rox "Увидимся, {b}[firstname]{/b}."
    show roxxy 1g
    show player 14
    player_name "Пока, {b}Рокси{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label roxxy_locker_sex_cum_repeat:
    player_name "Ты в порядке?"
    show player locker 17b with dissolve
    rox "Хааах... Хаах..."
    rox "Да, дай мне пару секунд..."
    rox "Фух."
    show player locker 17
    player_name "Пошли, надо валить отсюда!"
    scene black with fade

    scene school
    show player 10 at left
    show roxxy 1g at right
    with dissolve
    player_name "Знаешь, нам не стоит заниматься эти здесь!"
    show player 5
    show roxxy 1h
    rox "Почему же?!"
    show roxxy 1g
    show player 10
    player_name "Нас когда-нибудь спалят, {b}Рокси{/b}!"
    show player 5
    show roxxy 2
    rox "Пшш, ты слишком много волнуешься по этому поводу!"
    show roxxy 1g
    show player 16
    player_name "..."
    show roxxy 2
    rox "Не смотри на меня так!"
    show roxxy 48 with dissolve
    rox "Ты же знаешь, что я не перестану этим заниматься здесь!"
    rox "Ты не перевоспитаешь меня в этом плане... Понимаешь?!"
    show roxxy 47
    show player 14
    player_name "{b}*Вздох*{/b} Ладно, ладно!"
    player_name "Просто спрячь свои гипно-сиськи!"
    show player 13
    show roxxy 4 with dissolve
    rox "Хехехе, спасибо, {b}[firstname]{/b}!"
    hide player
    show roxxy 92 at left
    with dissolve
    pause
    show roxxy 59e with dissolve
    player_name "Пошли, у нас сейчас урок..."
    show roxxy 59d
    rox "О-ох, да, сэр..."
    rox "Хехехе!"
    hide roxxy with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
