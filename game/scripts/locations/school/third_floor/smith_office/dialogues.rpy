label principals_office_delivery_invoice:
    scene office_clear
    show ronda chair at Position (xoffset=-320,yoffset=-55)
    show principal 22_23f at Position(xpos = 600, ypos = 764)
    player_name "!!!" with hpunch
    player_name "Что за-"
    show principal 25f
    smi "Что все это значит?!"
    show principal 24f
    ann "Мне очень жаль, мэм!"
    scene expression game.timer.image("office{}")
    show annie 3f at Position (xpos=375)
    show player 168b at left
    show titty 1f at right
    show principal 26 at Position (xpos=614)
    with dissolve
    ann "Я не понимю-"
    show annie 9f
    show principal 27
    smi "Ты знаешь, что лучше не перебивать меня, когда я наказываю негодяев!"
    show principal 26
    ron "Я не сделала ничего плохого!"
    show principal 2
    smi "ТИШИНА!"
    show principal 1
    ann "..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "Что принес {b}[firstname]{/b}?"
    show principal 26 with dissolve
    show annie 1f
    show player 168c
    player_name "{b}*глоток*{/b} Это эээ, молоко... мэм."
    player_name "Для столовой."
    show player 168b
    show annie 9f
    show principal 27
    smi "Точно, доставка, которую я заказала."
    smi "Что ты делаешь в моем кабинете?!"
    show principal 26
    show player 168c
    player_name "{b}Энни{/b} сказала-"
    show player 168b
    show principal 27
    smi "Мне все равно, что сказала {b}Энни{/b}!"
    show annie 6f
    smi "Отнеси это вниз в кафетерий, немедленно!"
    show principal 26
    show player 168c
    player_name "{b}*вздыхая*{/b} Вниз по лестнице?"
    show player 168b
    show principal 27
    smi "... Проблемы?"
    show principal 26
    show player 168c
    player_name "Я... Извините, она очень тяжелая и я уже пронес ее всю дорогу сюда..."
    show player 168b
    show principal 27
    smi "Эээ..."
    show principal 28 at Position (xoffset=-54) with dissolve
    smi "Просто {b}развяжи Ронду{/b}, и она поможет тебе отнести коробку вниз."
    show principal 26 with dissolve
    ron "Что?! Почему я должна-"
    show principal 27
    smi "Это достаточно хорошее наказание для нее, и мне надоело слушать ее!"
    show principal 26
    show player 168c
    player_name "Хорошо."
    hide titty
    hide principal
    hide player
    hide annie
    with dissolve
    return

label principals_office_no_entry:
    scene expression game.timer.image("office{}")
    show principal 5 at right with dissolve
    show player 1 at left with dissolve
    smi "Что ты здесь делаешь?!"
    show player 11 at left
    show principal 3 at right
    player_name "Ой... эммм..."
    show player 21 at left
    player_name "Я... искал туалет!"
    show player 22 at left
    show principal 4 at right
    smi "Не строй из меня дуру, {b}[firstname]{/b}!"
    smi "Разве я не сказала тебе раньше, идти на урок??!"
    show player 10 at left
    show principal 1 at right
    player_name "Что ж..."
    show player 22 at left
    show principal 2 at right
    smi "А сейчас убирайся из моего {b}КАБИНЕТ{/b}!!!"
    hide player 22 at left with dissolve
    hide principal 2 at right with dissolve
    return

label principals_office_no_entry_night:
    scene expression L_school_floor3.background_blur
    show player 10 with dissolve
    player_name "Я не могу туда войти прямо сейчас..."
    hide player with dissolve
    return

label principals_office_smith_intro:
    scene expression game.timer.image("office{}")
    show player 10 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 1 zorder 1 at right
    with dissolve
    player_name "Вы хотели видеть меня, {b}Директриса Смит{/b}?"
    show player 11
    show principal 27
    smi "Безусловно, {b}[firstname]{/b}."
    smi "Нам нужно обсудить твои оценки и собираешся ли ты получить свой диплом."
    show player 10
    show principal 1
    player_name "Неужели все так плохо?"
    show player 11
    show principal 4b with dissolve
    smi "Сам посмотри..."
    show expression ReportCard() zorder 2 with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    pause
    hide expression ReportCard() with dissolve
    show player 10
    show principal 1 with dissolve
    player_name "Ох, блин, Я все завалил?!"
    show player 11
    show principal 27
    smi "Я говорила тебе..."
    show principal 1
    show annie 3
    ann "Вот что происходит когда ты прогуливаешь школу целый месяц!"
    show player 10
    show annie 1
    player_name "Я не прогуливал! Мой отец умер!"
    show player 11
    show principal 2
    smi "Молчать! {b}Энни{/b}!"
    show principal 1
    show annie 3
    ann "И-извините Мэм."
    show principal 27
    show annie 1
    smi "... Вне зависимости от обстоятельств."
    smi "Ты должен {b}Найти способ улучшить свои оценки{/b} если ты не хочешь остаться на второй год."
    smi "Я бы посоветовала тебе {b}поговорить с твоми учителями{/b} чтобы сделать все работы которые ты пропустил."
    smi "Возможно они смогут тебе дать некоторые {b}Дополнительные оценки{/b} за задания или типо того?"
    show player 10
    show principal 1
    player_name "Д-да, хорошо."
    show player 11
    show principal 27
    smi "Сделай все возможное!"
    show player 10
    show principal 1
    player_name "Да, Мэм."
    show player 11
    show principal 27
    smi "Хорошо, теперь иди на урок."
    show player 10
    show principal 1
    player_name "... На самом деле, Мэм?"
    show player 11
    show principal 27
    smi "Да?"
    show player 10
    show principal 1
    player_name "Я забыл комбинацию от моего шкафчика. Вы можете помочь мне его открыть?"
    show player 11
    show annie 4
    ann "Всмысле ты забыл?!"
    ann "В начале годе всем сказали записать их комбинации!"
    show player 10
    show annie 1
    player_name "Я эммм..."
    player_name "Я потерял его!"
    show player 11
    show annie 5
    ann "Пфффф, типично."
    show annie 1
    show principal 27
    smi "Это очень досадно, {b}[firstname]{/b}."
    smi "Мы дадим тебе новый замок."
    show principal 1
    player_name "..."
    show principal 27
    smi "Я пошлю {b}Энни{/b} вниз с её {b}Универсальным ключем{/b} немедленно..."
    smi "Я полагаю что сейчас ты получил все в чем ты нуждался."
    smi "Это может занять некоторое время прежде чем прибудет новый замок."
    show player 10
    show principal 1
    player_name "Да, мэм."
    show player 11
    show principal 27
    smi "Напровляйся прямо туда сейчас и тогда когда закончишь, после этого, тащи свой зад на урок!"
    $ M_smith.trigger(T_smith_go_to_locker)
    $ game.main()
    return

label principals_office_smith_go_to_locker:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show annie 4 zorder 1 at right
    with dissolve
    ann "Разве {b}Директриса Смит{/b} не сказала тебе проваливать?!"
    show annie 3
    ann "Иди к {b}своему шкафчику{/b} и я встречу тебя там с минуты на минуту!"
    $ game.main()
    return

label principals_office_smith_no_desk:
    scene expression game.timer.image("office{}")
    show player 11 at left
    show principal 1 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    smi "Что ты делаешь?"
    show principal 2
    smi "Убирайся к черту из моего кабинета!" with hpunch
    $ game.main()
    return

label principals_office_annie_trouble:
    scene expression game.timer.image("office{}")
    show principal 6 at right
    show player 11 at left
    with dissolve
    ann "{b}Директриса Смит{/b}?"
    show principal 7 at right
    smi "Что такое??"
    show principal 6 at right
    ann "Отчет о многократных правонарушителях как вы и приказывали!"
    show principal 9 at right
    smi "{b}[firstname]{/b}?"
    show principal 8 at right
    ann "Да, мэм. Он вел себя неприемлемо в раздевалке!"
    show principal 9 at right
    smi "У тебя недостаточно проблем?"
    smi "Что с твоими неудовлетворительными оценками и всем..."
    show player 10 at left
    show principal 13
    player_name "Ох, да Мэм!"
    show player 11 at left
    show principal 9
    smi "... И все же, ты выяснила реальную причину проблемы в раздевалке..."
    show principal 7 at right
    smi "Что случилось, конкретно, {b}Энни{/b}?"
    show principal 6 at right
    ann "Чтож, Его... он... Он показывал неприемлимые части своего тела девушкам в раздевалке, Мэм."
    show principal 9 at right
    smi "Это правда?"
    show player 10 at left
    player_name "Что ж... Я могу обьясни-"
    show player 22 at left
    show principal 10 at right with hpunch
    smi "{b}ТИШИНА{/b}!!!"
    show principal 9 at right
    show player 5 at left
    smi "...Я должна увидеть конкретно что произошло. Покажи мне что ты сделал сейчас."
    show principal 6 at right
    ann "Мжм, это не сработает..."
    ann "Кажется это происходит только тогда когда... когда он видит девушек {b}голыми{/b}, Мэм."
    show principal 7 at right
    smi "Ну, чего же ты ждешь, {b}Энни{/b}?"
    smi "Тебе придеться помочь ему с этим."
    show principal 11 at right
    show player 11 at left
    ann "{b}Что??!{/b}"
    show principal 12 at right
    smi "Вы единственая кто это видела и сообщила о правонарушении..."
    smi "...Это твой {b}долг{/b} чтобы выполнить отчет!"
    player_name "Мы действительно не должны этого делать-"
    show principal 10 at right
    show player 22 at left
    smi "Никто отсюда не уйдет пока я не получу полный отчет! Сделай это, или вы оба будете {b}АРЕСТОВАНЫ{/b}!!!"
    show principal 13 at right
    ann "..."
    show player 8 at left
    show principal 14 at right
    window hide
    pause
    show player 63 at left
    show principal 15 at right
    window hide
    pause
    show principal 16 at right
    show player 64 at left
    smi "Сейчас, посмотрим на эту {b}Потрясающую грудь{/b} у неё..."
    show principal 17 at right
    smi "Разве ты не хочешь... пососать их? {b}[firstname]{/b}?"
    show player 65 at left
    player_name "..."
    show player 66 at left
    window hide
    pause
    show player 66 at left with hpunch
    window hide
    pause
    show player 67 at left
    smi "Вот и мы..."
    show principal 18 at right
    smi "Этого достаточно, {b}Энни{/b}. Ты можешь идти..."
    show principal 5 at right with dissolve
    smi "Итак!..."
    smi "Вот что я слышала об этом много раз."
    hide player 67 at left
    show principal 19 at left
    with dissolve
    smi "Ты сделал хорошую репутацию по всей школе..."
    smi "Теперь Я понимаю почему..."
    smi "... Это было..."
    show principal 20 at left
    window hide
    pause
    show principal 21 at left with hpunch
    window hide
    pause
    smi "...отвлекающим маневром!"
    show player 69 at left
    show principal 1 at right
    with dissolve
    player_name "Я извиняюсь, Мэм!"
    player_name "Этого больше не произойдет, Я обещаю!"
    show principal 5 at right
    show player 68 at left
    smi "Хорошо молодй человек: Уговор такой..."
    smi "Я не буду тебя арестововать, пока ты держишь эту... \"проблему\" в твоих... при себе."
    smi "Мой приоритет порядок и дисциплина в этой школе, и я собирюсь сохранить её такой!"
    show principal 1 at right
    show player 69 at left
    player_name "Да, {b}Директриса Смит{/b}!"
    show principal 2 at right
    show player 68 at left
    smi "Сейчас, убирайся с моего {b}КАБИНЕТА{/b}!!"
    hide player 68 at left with dissolve
    hide principal 2 at right with dissolve
    $ renpy.end_replay()
    return

label principals_office_dewitt_paint_trail:
    if M_dewitt.is_state(S_dewitt_paint_trail):
        scene smith_office_spying
        show annie spying 1
        show principal spying 2
        with dissolve
        smi "Тебе надо было видеть их лица!"
        smi "Полного и полного уничтожения!"
        smi "Хахах!"
        show principal spying 1
        show annie spying 2
        ann "Так они поверили что это был {b}Тайрон{/b} и его банда как вы и планировали?"
        show annie spying 1
        show principal spying 2
        smi "Нет, {b}Девитт{/b} знает я должна с этим что то сделать но она не сможет ничего доказать."
        show principal spying 1
        show annie spying 3
        ann "Я сожалею, Мэм. Я старалась из-за всех сил сделать так как будто кучка хулиганов это сделала."
        show annie spying 1
        show principal spying 2
        smi "Да, да, Я уверена что ты сделала."
        smi "Я просто не могу выбрасить ту картинку из своей головы!"
        smi "Бедная маленькая {b}Девитт{/b} на грани слез."
        smi "Ее глупое шоу талантов разрушено!"
        show principal spying 3
        smi "Ммм..."
        show principal spying 2
        smi "Это на самом деле заставляет меня работать."
        smi "Почему бы тебе не прийти сюда и не помочь мне."
        show principal spying 1
        show annie spying 3
        ann "Конечно, Мэм."
        show annie spying 4
        show principal spying 4
        with dissolve
        pause
        show annie spying 5 with dissolve
        pause
        show principal spying 3
        smi "Ахх, вот так."
        smi "Хорошая девочка..."
        smi "Хехехехе, Я не могу дождаться уведить ее вырожение лица когда я скажу ей что Комиссия отказалась её финансировать!"
        scene black with fade

        scene outside_smith_office
        show kevin 24 at Position (xpos=800)
        show player 107 at Position (xpos=400)
        with dissolve
        kev "Бро, {b}Директриса Смит{/b} стоит за этим!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "Что за мега Шлюха!"
        kev "Мы должны что то сказать!"
        show kevin 23
        player_name "..."
        show kevin 24
        kev "{b}[firstname]{/b}?"
        kev "{b}[firstname]{/b}?!"
        show kevin 23
        pause 1
        show kevin 25 at Position (xoffset=-82) with hpunch
        kev "Бро!"
        show kevin 23
        show player 12 with dissolve
        player_name "Хэй! Успакойся, чувак!"
        show player 5
        show kevin 24
        kev "Я пытаюсь поговорить с тобой!"
        show kevin 23
        show player 12
        player_name "Что ж, прости но ты видел что они делают там прямо сейчас?!"
        show player 5
        show kevin 24
        kev "Эм, да и это очень грубо!"
        kev "{b}Директриса Смит{/b} вот дьявол, Бьюсь об заклада что её пизда пахнет как сера и она зеленовато-жёлтого цвета!"
        show kevin 23
        show player 113
        player_name "{b}Энни{/b} кажется не против..."
        show player 114
        show kevin 24
        kev "Давай, уже поздно и ты должен встретиться с {b}Евой{/b} в парке, помнишь?!"
        show kevin 23
        show player 113
        player_name "Ну да, только еще 5 минут..."
        show player 114
        show kevin 24
        kev "Пойдем, пока нас не поймали, как извращенцев!"
        hide kevin
        hide player
        with dissolve
    else:

        scene smith_office_spying
        show annie spying 5
        show principal spying 3
        with dissolve
        smi "У тебя очень хорошо получается с моим маленьким зверьком."
        smi "Мммм, вот здесь!"
        smi "Ахх!"
        scene black with fade
    return

label principals_office_dewitt_smith_office_trap:
    scene expression game.timer.image("office{}")
    show erik 51 at right
    show player 12 at left
    with dissolve
    player_name "Ты смотри за дверью пока я применю клей, хорошо?"
    show player 5
    show erik 53
    eri "Да, хорошо."
    eri "Только поторопись, чувак. Я хочу убраться от сюда..."
    show erik 52
    show player 12
    player_name "Хорошо."
    hide player
    hide erik
    with dissolve

    scene smith_office_cs01
    with fade
    show text "Я удоставерился что стулья были склеены к полу перед передвижением подушек.\nЯ ни за что не позволил бы {b}Директрисе Смит{/b} и {b}Энни{/b} испортить {b}Шоу талантов{/b}.\nНе после всей той тяжелой работы которую мы вложили в неё!\nЯ не останавливался до тех пор, пока не использовал последнюю каплю клея." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene smith_office_night_b
    show erik 52 at right
    show player 14 at left
    with dissolve
    player_name "Хорошо, Этого должно хватить."
    show player 17
    player_name "Я отключил её телефон еще с самого начала так что, они никак не смогут позвать на помощь!"
    show player 13
    show erik 54
    eri "Хорошо придумал!"
    show erik 53
    eri "Сейчас давай убераться от сюда, {b}[firstname]{/b}!"
    show erik 52
    show player 14
    player_name "Да, Я прямо за тобой!"
    hide player
    hide erik
    with dissolve

    scene expression game.timer.image("outside_school{}")
    show player 13 at left
    show erik 53 at right
    with dissolve
    eri "Фух."
    eri "Давай больше так делать не будем, хорошо?"
    show erik 52
    show player 14
    player_name "Хех, да."
    player_name "По крайней мере мы сделали то, что мы пришли сюда делать."
    show player 13
    show erik 54
    eri "Миссия прошла успешно!"
    show erik 1
    show player 14
    player_name "Спасибо за твою помощь {b}Эрик{/b}."
    show player 13
    show erik 4
    eri "Не упоминай об этом, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Увидимся позже!"
    show player 13
    show erik 7 with dissolve
    eri "Увидимся!"
    hide player
    hide erik
    with dissolve
    return

label principals_office_dewitt_trap_check_up:
    scene office_clear
    show annie 19
    with dissolve
    ann "... Это отличный план, Мэм!"
    ann "Это положит конец этому глупому шоу раз и навсегда."
    show annie 20
    smi "Да, пока ты не облажаешся снова..."
    show annie 19
    ann "Но я не..."
    ann "... Да, Мэм."
    show annie 20
    smi "Просто займись подготовкой!"
    show annie 19
    ann "Сию минуту, Мэм!"
    show annie 20b with dissolve
    ann "..."
    ann "Я прилипла!"
    show annie 20c with dissolve
    smi "Что?"
    show annie 20b with dissolve
    ann "Я не могу встать с моего стула!"
    show annie 20c with dissolve
    smi "Хватит дурачиться, {b}Энни{/b}. У нас нет времени!"
    show annie 20b with dissolve
    ann "Я действительно прилипла к стулу!"
    show annie 20c with dissolve
    smi "Ох Ради всего святого!"
    show annie 21
    smi "( !!! )" with hpunch
    smi "КАКОГО ЧЕРТА?!"
    smi "Я тоже застряла!!!"
    smi "Как это возможно?!"
    ann "..."
    smi "{b}Энни{/b} тащи свою задницу сюда и помоги мне!"
    ann "Я не могу, Я прилипла тоже!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( Это сработало! )"
    show player 14f at Position (xoffset=100)
    player_name "( Они никак не смогут сейчас помешать {b}Шоу талантов{/b}!)"
    player_name "( Они застряли там до тех пор пока кто-то их там не найдет. )"
    player_name "( Мне лучше вернуться быстрее в {b}Актовый зал{/b} или я пропущу начало. )"
    hide player with dissolve
    return

label principals_office_dewitt_office_night_visit_delay:
    scene expression game.timer.image("office{}")
    show annie 22f at left
    show principal 36 at right
    with dissolve
    ann "Можете мне дать эту подушку?"
    show annie 23f
    show principal 37
    smi "Не сейчас, Идиотка!"
    smi "Что я хочу это получить полный отчет о том кто это сделал!"
    smi "Кто бы не разрушил мой стул... и... и мой костюм!"
    smi "Мой красивый костюм!"
    show principal 40 with dissolve
    smi "Посмотри что они сделали!"
    smi "НАЙДИ ИХ!"
    scene black with fade

    scene outside_smith_office
    show player 107 at Position (xpos=400)
    with dissolve
    pause
    show player 17f at Position (xoffset=100) with dissolve
    player_name "( Мне лучше свалить отсюда прежде чем они меня запалят! )"
    hide player with dissolve
    return

label desk03_locked_dialogue:
    scene expression game.timer.image("office{}")
    if player.location.is_here(M_smith):
        show player 30 at left
        player_name "Хммм... Интересно что там внутри?"
        show player 22 at left with hpunch
        show principal 4 at right with dissolve
        smi "Что ты делаешь?"
        show principal 1 at right
        show player 29 at left
        player_name "Ох, Простите... Я просто смотрел!"
        show player 3 at left
        show principal 5 at right
        smi "Если я {b}КОГДА-НИБУДЬ{/b} поймаю тебя когда ты роешься в моих вещах..."
        show principal 2 at right
        smi "...можешь быть уверен, ты проведешь остаток своего года в {b}ЗАКЛЮЧЕНИИ{/b}!!!"
    else:
        $ pass
    $ game.main()

label principle_drawer:
    scene principle_drawer
    show expression "objects/object_papers_01.png" at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "Что со всеми этими... кожаными вещами... здесь?"
    player_name "странно..."
    call screen principle_drawer

label principle_drawer_diane_delivery_3_fetch_invoice:
    scene expression game.timer.image("office{}")
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smi "Ah, wonderful."
    smi "Are those the new {b}milk cartons{/b}?"
    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... Yeah."
    show principal 27f
    show player 163f
    smi "I sampled the last batch..."
    smi "It was quite... delightful. You're lucky I'm in a good mood."
    smi "Please, tell the milk provider I'm doubling our next order."
    smi "We keep running out. The students absolutely love it!"
    show principal 26f
    show player 164f
    player_name "Will do! Where can I put these cartons?"
    show principal 27f
    show player 163f
    smi "You can give them to {b}Annie{/b}, she'll take care of them."
    show principal 4f at Position (xpos = 470)
    show player 167f
    smi "Now, get out of my office, I have some unfinished business to attend to."
    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Yes, {b}Principal Smith{/b}!"
    hide principal
    hide titty
    hide player
    with dissolve
    $ M_diane.trigger(T_diane_delivery_3_got_invoice)
    $ game.main()

label principals_office_okita_get_keycode_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    show principal 26 at right
    player_name "( Вот дерьмо! Она здесь! )"
    smi "..."
    show principal 27
    smi "... Я могу тебе с чем-то помочь?"
    show player 10
    show principal 26
    player_name "Ох! Я просто-"
    show player 29
    player_name "... Эмм, мне было... просто любопытно..."
    show principal 2
    show player 3
    smi "Говори уже, {b}[firstname]{/b}?!"
    show principal 26
    pause
    show player 10
    player_name "Эмм, Как у вас дела, {b}Директриса Смит{/b}?"
    show player 11
    smi "..."
    show principal 27
    smi "Занята."
    show principal 2
    smi "А теперь убирайся!"
    show player 10
    show principal 26
    player_name "Д-да, Мэм!"


    return

label principals_office_okita_get_keycode_afternoon:
    scene expression game.timer.image("office{}")
    show player 1
    with dissolve
    player_name "( Её здесь нет! Это мой шанс чтобы найти этот код! )"
    player_name "( {b}Мне нужно осмотреться.{/b} )"
    return

label masterkey_taken:
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_key3.png" at truecenter with dissolve
    $ player.get_item("master_key")
    pause
    hide expression "boxes/popup_key3.png" with dissolve
    $ game.main()

label keycode_note_taken:
    scene expression game.timer.image("office{}")
    show player 544
    with dissolve
    pause
    show player 543
    player_name "Ага! Это должно быть здесь! {b}6219{/b}."
    show expression "backgrounds/location_school_office_desk.jpg"
    show expression "boxes/popup_item_note2.png" at truecenter with dissolve
    $ player.get_item("keycode_note")
    pause
    hide expression "boxes/popup_item_note2.png" with dissolve
    pause 1
    player_name "А теперь я могу открыть кабинет {b}Мисс Окиты{/b} чтобы забрать все вещи которые она просила."
    $ M_okita.trigger(T_okita_keycode_acquired)
    $ game.main()
    return

label tissue_taken:
    $ player.go_to(L_school_smithoffice)
    scene location_school_office_day_blur
    show player 528
    with dissolve
    pause
    show player 529
    player_name "Агх, ох мэн..."

    player_name "Отвратительно!"
    show player 528
    pause
    show player 529
    player_name "Думаю это сработает..."
    player_name "Лучше убраться отсюда пока {b}Энни{/b} не вернулась."
    show expression "boxes/popup_item_tissue1.png" at truecenter with dissolve
    $ player.get_item("tissue")
    pause
    hide expression "boxes/popup_item_tissue1.png" with dissolve
    pause 1

    $ game.main()

label desk_open:
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen desk_drawer

label principals_office_okita_get_ingredients_morning:
    scene expression game.timer.image("office{}")
    show player 22 at left
    with dissolve
    player_name "( Вот дерьмо! Она здесь! )"
    show principal 3b at Position(xpos=0.85, ypos=1.0) with dissolve
    smi "..."
    show principal 27 at right with dissolve
    smi "... Я могу тебе с чем-то помочь?"
    show player 29 with dissolve
    show principal 26
    player_name "Ох! Я просто-"
    player_name "... Эмм, мне было... просто любопытно..."
    show player 3
    show principal 27 with dissolve
    smi "Говори уже, {b}[firstname]{/b}!"
    show player 29
    show principal 26
    player_name "Эмм, как у вас дела, {b}Директриса Смит{/b}?"
    show player 3
    smi "..."
    show principal 27
    smi "Занята."
    show player 22
    show principal 2
    with dissolve
    smi "А теперь убирайся!" with hpunch
    show principal 1
    show player 10
    player_name "Д-да, Мэм!"

    return

label principal_trash:
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("tissue"):
        call screen principle_garbage
    else:
        scene location_school_office_day_blur
        show player 10
        player_name "Я не хочу смотреть на мусор Директрисы Смит."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
