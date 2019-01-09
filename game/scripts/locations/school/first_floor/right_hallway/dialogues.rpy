label prom_poster:
    show expression game.timer.image("prom_poster_day{}")
    pause
    player_name "( Скоро приближается выпускной. )"
    player_name "( Кажется это было бы подходящим временем ... если бы я уже встречался. )"
    player_name "( Мне лучше поторопиться и найти кого-то. )"
    player_name "( Интересно кого я мог бы попросить. )"
    $ game.main()

label school_righthallway_roxxy_go_in_auditorium:
    scene expression player.location.background_blur
    show player 642 at left
    show erik 4 at right
    with dissolve
    eri "Привет!"
    eri "Как дела, чувак?!"
    show erik 1
    show player 641
    player_name "Ох, привет, {b}Эрик{/b}."
    player_name "Я просто взял эти записи с {b}Актового зала{/b} для {b}Мисс Девитт{/b}..."
    show player 642
    show erik 4
    eri "Ах, прямо за..."
    eri "Это выглядит тяжелым!"
    show erik 1
    show player 641
    player_name "Немного, да."
    player_name "Что ты здесь делаешь?"
    show player 642
    show erik 4
    eri "Я как раз шел Актовый зал тоже."
    eri "У меня небольшой перерыв до моего следующего урока и обычно тихо и темно в {b}Актовом зале{/b}."
    eri "Идеально подходит для того чтобы играть в игры на моем смартфоне!"
    show erik 1
    show player 641
    player_name "Хмм, зачем тебе нужна темнота и тишина?"
    show player 642
    show erik 5
    eri "Я эмм... Я не знаю."
    show erik 4
    eri "Это просто более умиротворенней я думаю!"
    show erik 5
    eri "Ты хочешь чтобы я помог тебе с этим?"
    show erik 1
    show player 641
    player_name "Нет, я справлюсь."
    player_name "В какую игру ты играешь-"
    show player 642
    show erik 1b
    dex "Ой, Давай {b}Бекка{/b} просто дай взглянуть..."
    player_name "..."
    show erik 3b
    eri "Подожди секунду. Это был {b}Декстер{/b}?"
    show erik 52
    show player 641
    player_name "Да, похоже на него..."
    show player 642
    show erik 3b
    eri "Какого черта он забыл в Актовом зале?"
    show erik 52
    show player 641
    player_name "Без понятия..."
    player_name "Мы должны пойти и выяснить!"
    show player 642
    show erik 3b
    eri "... Эххх, Серьезно?"
    show erik 52
    show player 641
    player_name "Да, мужик. Давай!"
    hide player
    hide erik
    with dissolve
    scene expression "backgrounds/location_school_assembly_hall_cutscene08.jpg"
    with fade
    show text "Что происходило в Актовом зале?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    pause
    scene assembly_hall_paint02_c
    show dexter 34
    show becca 2 at left
    with dissolve
    becca "{b}Декстер{/b} остановись!"
    becca "Угх, и ради этого ты меня сюда позвал?!"
    show becca 1
    show dexter 35
    dex "Хмм?!"
    dex "В чем проблема?"
    dex "{b}Рокси{/b} и я взяли перерыв и ты всегда носишь это такое низкое декольте с твоими болтающимеся сиськами везде..."
    dex "Просто покажи мне их на секунду."
    show dexter 34
    show becca 2
    becca "Ни в коем случае!"
    becca "Мы в школе!"
    becca "... И даже если бы мы небыли. Ты мне не нравишься таким образом."
    show becca 1
    show dexter 35
    dex "ШШ, перестань претворятся что тебе этого не хочется..."
    show dexter 34
    show becca 2
    becca "Я никогда не притворяюсь!"
    show becca 1
    show dexter 36
    dex "Хэй, что это такое у тебя на джинсах?!"
    show becca 14 at Position (xoffset=86) with dissolve
    becca "Хммм?"
    show dexter 37 at left
    hide becca
    with dissolve
    becca "Ауч! Что за херня, {b}Декстер{/b}!"
    show becca 14 at left
    show becca 14 at Position (xoffset=86)
    hide dexter
    show dexter 35
    with dissolve
    dex "Хахахаха, Мне всегда казалось что у тебя отличная задница..."
    show dexter 34
    hide becca
    show dexter 38 at left
    with dissolve
    becca "Черт побери. Я ухожу!"
    show dexter 40 with dissolve
    dex "Хэй!"
    dex "Ты никуда не пойдешь пока я не увижу эти сиськи!"
    show dexter 39
    becca "Что черт возьми с тобой сегодня?!"
    becca "Я сказала нет!"
    show dexter 40
    dex "Никто не говорит мне нет!"
    scene black with fade
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 12f at right
    show erik 51f
    with dissolve
    player_name "Мы должны что-то сделать!"
    show player 90f
    show erik 3bf
    eri "Н-но... {b}Декстер{/b} убьет нас!"
    show erik 51f
    show player 12f
    player_name "Мы не может просто стоять здесь! Пошли!"
    hide player
    hide erik
    with dissolve
    scene assembly_hall_paint02_c
    show erik 51 at Position (xpos=950)
    show player 12f at Position (xpos=775)
    show dexter 34 at Position (xpos=400)
    show becca 16 zorder 1 at left
    with dissolve
    player_name "Отвали от нее!"
    show player 90f
    show dexter 24 at Position (xoffset=47)
    dex "Хмм?!"
    show dexter 23 at Position (xoffset=47)
    show becca 17 with dissolve
    becca "Да пошел ты, {b}Декстер{/b}!"
    hide dexter
    show becca 18
    dex "Гр, больно!" with hpunch
    show dexter 41 at Position (xoffset=-80)
    show becca 2b
    with dissolve
    becca "Ублюдок!"
    show becca 19
    hide dexter with dissolve
    dex "*Кашель*"
    hide player
    show becca 21f at Position (xpos=421)
    with dissolve
    player_name "!!!"
    show erik 3b
    eri "Не хрена себе!"
    show erik 52
    show becca 19 at Position (xpos=400)
    show player 10f at Position (xpos=775)
    with dissolve
    player_name "{b}Бекка{/b}, ты в порядке?"
    show player 11f
    show becca 20
    becca "{b}[firstname]{/b}!!!"
    becca "Я только... Я имею в виду, {b}Декстер{/b} был..."
    show becca 19
    show player 12f
    player_name "Я знаю. Мы видели это..."
    show player 5f
    becca "..."
    show erik 4
    eri "Ты просто отправила его орехи на луну!"
    eri "Это было круто!"
    show erik 1
    show becca 20
    becca "... Это было?"
    show becca 19
    show player 14f
    player_name "Хаха, полностью."
    show player 13f
    dex "Угх... {b}*кашель* *Пормочет*{/b}"
    show player 12f
    player_name "... Ты уверена что с тобой все хорошо несмотря?"
    show player 5f
    show becca 20
    becca "{b}*Вдох*{/b} Да, вроде того..."
    becca "Я никогда раньше его таким не видела!"
    show becca 19
    show player 12f
    player_name "Что ж не волнуйся. Я не думаю что он попробует сделать что-то подобное снова..."
    show player 14f
    show dexter 41 zorder 0 at Position (xpos=400) with dissolve
    player_name "... Черт, ты действительно получил хорошо!"
    show player 13f
    dex "{b}*Кашель*{/b} Охх... Мои... Бубенчики..."
    show roxxy 3cf at Position (xpos=75) with dissolve
    rox "Что, черт возьми, здесь проиходит?"
    show roxxy 2cf
    rox "Что случилось с {b}Беккой{/b}?"
    show roxxy 27f at Position (xoffset=34) with dissolve
    rox "..."
    show roxxy 28f at Position (xoffset=34)
    rox "... И почему ты держишся за свои яйца, {b}Декстер{/b}?"
    show roxxy 27f at Position (xoffset=34)
    menu:
        "Сказать {b}Рокси{/b}.":
            show player 12f
            player_name "{b}Декстер{/b} пытался заставить {b}Бекку{/b} перепихнуться с ним."
            show player 90f
            show becca 19f
            show roxxy 3cf
            with dissolve
            rox "... Серьезно?"
            show roxxy 3bf
            show erik 3b
            eri "Да, мы это видели."
            show erik 52
            show roxxy 3f
            rox "Ты идиот!"
            rox "Да что с тобой черт подери?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Удушье* *Хрип*{/b} ... Помоги."
            show dexter 41 at Position (xoffset=0)
            show becca 20f
            becca "{b}*Вдох*{/b} {b}[firstname]{/b} вбежал и пытался его остановить."
            show becca 19f
            show roxxy 2cf
            rox "Ты дал отпор {b}Декстеру{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Эрр, отчасти..."
            show player 5f
            show roxxy 3cf
            rox "Ты рехнулся?"
            rox "Ты же понимаешь что он мог тебя убить, правда?"
            show roxxy 3df
            show player 12f
            player_name "... Нет?"
            show player 90f
            show roxxy 2f
            rox "Охх, да. Он бы просто уничтожил тебя."
            rox "Не будь идиотом."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Охх... Ты труп, {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Ох, Заткнись!"
            rox "Ты ни черта не сделаешь!"
            show player 13f
            rox "Если об этом узнают тебя наверняка исключат!"
            rox "... И это будет наименьшая из твоих проблем!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3f
            rox "Ох хм. Вот что я думаю."
            show roxxy 3cf
            rox "Давай, {b}Бекка{/b}. Я провожу тебя до раздевалки."
            show roxxy 3df
            becca "..."
            show roxxy 3d with dissolve
            show becca 20f
            becca "Подожди!"
            show becca 5 with dissolve
            pause
            show becca 22f at Position (xpos=457)
            hide player
            with dissolve
            show roxxy 3df
            player_name "!!!" with hpunch
            show becca 8 at Position (xpos=400)
            show player 13f at Position (xpos=775)
            with dissolve
            show roxxy 2bf
            becca "Спасибо."
            show becca 7
            show roxxy 1f f
            show player 14f
            player_name "Хех, Я ничего не сделал."
            show player 13f
            show becca 8
            becca "Да, ты сделал!"
            becca "Я..."
            becca "... Просто Спасибо!"
            hide becca
            hide roxxy
            with dissolve
        "Молчание.":

            show player 10f
            player_name "Я эмм..."
            show player 5f
            player_name "..."
            show becca 20f with dissolve
            becca "{b}Декстер{/b} заставлял меня перепихнуться с ним!"
            show becca 19f
            show roxxy 3cf with dissolve
            rox "... Серьезно?"
            show roxxy 3bf
            show erik 3b
            eri "Да, мы это видели."
            show erik 52
            show roxxy 3f
            rox "Ты идиот!"
            rox "Да что с тобой черт подери?!"
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "{b}*Удушье* *Хрип*{/b} ... Помоги."
            show dexter 41 at Position (xoffset=0)
            show becca 20 with dissolve
            becca "{b}*Вдох*{/b} {b}[firstname]{/b} вбежал и пытался его остановить."
            show becca 19f with dissolve
            show roxxy 2cf
            rox "Ты выстоял против {b}Декстера{/b}?"
            show roxxy 2bf
            show player 10f
            player_name "Эрр, отчасти..."
            show player 5f
            show roxxy 3cf
            rox "Ты рехнулся?"
            rox "Ты же понимаешь что он мог тебя убить, правда?"
            show roxxy 3df
            show player 10f
            player_name "... Нет?"
            show player 5f
            show roxxy 2f
            rox "Охх, да. Он бы просто уничтожил тебя."
            rox "Не будь идиотом."
            show roxxy 1f f
            show dexter 41 at Position (xoffset=2)
            dex "Охх... Ты труп, {b}[firstname]{/b}..."
            show dexter 41 at Position (xoffset=0)
            show player 11f
            show roxxy 3f
            rox "Ох, Заткнись!"
            rox "Ты ни черта не сделаешь!"
            rox "Если об этом узнают тебя наверняка исключат!"
            show player 5f
            rox "... И это будет наименьшая из твоих проблем."
            show roxxy 3bf
            show dexter 41 at Position (xoffset=2)
            dex "..."
            show dexter 41 at Position (xoffset=0)
            show roxxy 3cf
            rox "Ох хм. Вот что я думаю."
            rox "Давай, {b}Бекка{/b}. Я провожу тебя до раздевалки."
            hide becca
            hide roxxy
            with dissolve
    show player 13f
    player_name "..."
    show erik 3b
    eri "... Итак, ты теперь подружился с ними, хм?"
    show erik 52
    show player 14 at Position (xpos=700) with dissolve
    player_name "Да, немного."
    show player 13
    show erik 4
    eri "Это круто, чувак!"
    show erik 1
    show dexter 41 at Position (xoffset=2)
    dex "{b}*Хныканье*{/b}"
    show dexter 41 at Position (xoffset=0)
    show player 11
    show erik 3b
    eri "... Охх, нам стоит убираться отсюда."
    show erik 52
    show player 12
    player_name "Да, пошли."
    hide player
    hide erik
    with dissolve
    scene school
    show player 13 at left
    show erik 4
    with dissolve
    eri "... Что случилось потом после поддельного ID?"
    show erik 1
    show player 14
    player_name "Я не думаю что могу сказать..."
    player_name "... Но я помог {b}Рокси{/b} с некоторыми личными делами."
    show player 13
    eri "..."
    show erik 4
    eri "Ооох, Я понял. 10-4, чувак."
    eri "Я услышал что ты сказал."
    show erik 1
    show player 14
    player_name "Хех, что? Я не думаю что ты понял..."
    show player 13
    show roxxy 3c at right with dissolve
    rox "Что ж, это была неразбериха..."
    show roxxy 3d
    show erik 1f with dissolve
    show player 10
    player_name "С {b}Беккой{/b} все хорошо?"
    show player 5
    show roxxy 33 with dissolve
    rox "Да, она в порядке."
    rox "Она была просто немного шокирована всем этим."
    show roxxy 30 with dissolve
    rox "Я не могу поверить что {b}Декстер{/b} это сделал!"
    rox "Я имею в виду, он совершал много тупого дерьма в прошлом..."
    show roxxy 3c
    rox "... Но никогда ничего мерзкого!"
    show roxxy 3d
    show player 10
    player_name "Чтож, я просто рад что {b}Эрик{/b} и я были там..."
    show player 5
    show roxxy 2
    rox "... Кто этот {b}Эрик{/b}?"
    show roxxy 1
    show erik 2f with dissolve
    eri "..."
    show player 12
    player_name "Эмм, мой друг {b}Эрик{/b}..."
    show player 90
    show roxxy 1b
    rox "Ох, правда!"
    rox "Извини, я забыла что ты был там."
    show roxxy 1
    show erik 3bf with dissolve
    eri "... Все в порядке."
    show erik 1f
    show roxxy 1b
    rox "Так ну, я собираюсь рассказать тебе..."
    rox "Девченки и я будем устраивать конкурс бикини в эти выходные и ты должен точно прийти!"
    show roxxy 1
    show erik 51f
    show player 10
    player_name "Серьёзно?"
    show player 14
    player_name "Это звучит круто!"
    show player 13
    show roxxy 2
    rox "Я знаю?!"
    show roxxy 1b
    rox "Просто приходи на пляж в {b}Субботу вечером{/b}!"
    show roxxy 1
    show erik 1f
    show player 14
    player_name "Хорошо, я буду там."
    show player 13
    show roxxy 1b
    rox "Хех, круто."
    rox "Увидимся, {b}[firstname]{/b}!"
    hide roxxy with dissolve
    pause
    show erik 4 with dissolve
    eri "Вау, чувак!"
    eri "Конкурс бикини?!"
    eri "Это так круто!"
    show erik 1
    show player 14
    player_name "Хочешь пойти со мной?"
    show player 13
    show erik 3b
    eri "Ой, я не могу."
    eri "Я хочу Я мог бы но у меня будет рейд с моей гильдией в {b}Субботу вечером{/b}..."
    show erik 52
    show player 12
    player_name "Забей на это!"
    show player 14
    player_name "Давай мужик, подумай о всех тех бикини!"
    show player 13
    show erik 3b
    eri "Ты спятил?! Я не могу пропустить рейд!"
    eri "Это МИНУС 50 ДКР!"
    show erik 52
    show player 10
    player_name "... Хм?"
    show player 5
    show erik 3b
    eri "Это очень важно, чувак!"
    show erik 52
    show player 14
    player_name "Хех, хорошо. Отлично."
    player_name "Я думаю, я тогда пойду один..."
    show player 13
    show erik 3b
    eri "Выстрел, я должен добраться до компьютерного класса."
    show erik 3
    eri "Увидимся позже, чувак."
    show erik 4
    show player 14
    player_name "Увидимся, {b}Эрик{/b}."
    hide player
    hide erik
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
