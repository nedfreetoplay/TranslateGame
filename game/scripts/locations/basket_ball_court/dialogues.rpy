label basketball_court_dexter_start:
    scene basketball_b
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Что ты здесь делаешь?"
    show dexter 1
    show player 12
    player_name "Почему тебя это волнует? Может, я здесь, чтобы попрактиковаться."
    show player 11
    show dexter 3
    dex "Ха!"
    dex "Это хорошо!"
    show dexter 1
    show player 25
    player_name "{b}*вздох*{/b}"
    show player 12
    player_name "Что тебе надо, {b}Декстер{/b}?"
    show player 5
    show dexter 6 with dissolve
    dex "Держись подальше от моего корта, понял?"
    hide dexter with dissolve
    show player 24
    player_name "..."
    hide player with dissolve
    return

label basketball_court_roxxy_dexter_argument:
    scene basketball_b
    show roxxy 3f at left
    show dexter 2 at right
    with dissolve
    rox "Как ты можешь быть таким глупым?!"
    show roxxy 3bf
    show dexter 6 with dissolve
    dex "Не называй меня глупым!"
    show dexter 2
    show roxxy 3f
    rox "У тебя было одно задание."
    rox "Я сказала: \"принеси мне его домашнее задание.\""
    rox "Разве это не то, что я сказала?"
    show roxxy 3df
    show dexter 8
    dex "Да, но..."
    show dexter 2
    show roxxy 3f
    rox "Заткнись идиот! Я говорю!"
    rox "Итак, ты нашел его."
    rox "Ты прижал его."
    rox "... И он свалил не отдав тебе домашнее задание!"
    show roxxy 3df
    show dexter 4 with dissolve
    dex "Ну, я ударил его, и его очки сломались."
    show dexter 3 with dissolve
    dex "Это было забавно..."
    dex "Я смеялся, он плакал, и я думаю ... Я просто просто забыл."
    show dexter 1
    show roxxy 3f
    rox "Ну, и что я должна теперь делать?!"
    rox "У меня нет ничего, чтобы вернуться в {b}класс французской суки{/b}!"
    show roxxy 3bf
    show dexter 3
    dex "Это не моя проблема!"
    dex "Почему бы тебе самой не украсть домашнее задание?!"
    show dexter 1
    show roxxy 30f
    rox "Грр, я же говорила тебе, я не могу сделать это сама!"
    rox "Ты никогда не слушаешь!"
    show roxxy 3f
    show dexter 2
    rox "Ты такой ГЛУПЫЙ!"
    show roxxy 3bf
    show dexter 8
    dex "Перестань называть меня глупым, {b}Рокси{/b}!"
    show dexter 2
    show roxxy 31f
    rox "... ТЫ ГЛУПЫЙ!"
    show roxxy 3bf
    show dexter 4
    dex "ВСЕ ХВАТИТ!!!" with hpunch
    dex "Я покнчу с этим!"
    show dexter 6 with dissolve
    dex "Всегда, \"{b}Декстер{/b} сделай это.\" \"{b}Декстер{/b} сделай то.\""
    dex "... И что в итоге?"
    dex "Я - глупый."
    dex "Что ж, пошла ты в задницу {b}Рокси{/b}!"
    dex "Больше никаких одолжений!"
    dex "Катаний на тачке!"
    dex "Пивка!"
    show dexter 8 with dissolve
    dex "... и никаких одолжений!"
    show dexter 2
    show roxxy 3cf
    rox "Ты уже говорил это..."
    show roxxy 3f
    rox "... глупец."
    show roxxy 3bf
    show dexter 6 with dissolve
    dex "Ррррр, пошла ты!"
    dex "Я ухожу!"
    hide dexter with dissolve
    show roxxy 3f
    rox "... Ага, мне все равно."
    hide roxxy with dissolve
    pause 1
    show player 13 at left
    show eve 6 at right
    with dissolve

    eve "Воу!"
    eve "Вот это представление!"
    show eve 5
    show player 10
    player_name "Ну, да."
    show player 5
    player_name "..."
    show eve 2b
    eve "В чем дело?"
    show eve 1
    show player 10
    player_name "Я не могу поверить, что собираюсь это сказать, но..."
    player_name "Мне как-то жалко {b}Декстера{/b}."
    show player 5
    show eve 2b
    eve "Ухх..."
    eve "Не говори так."
    eve "Он мудак!"
    show eve 1
    show player 10
    player_name "Да, я знаю."
    show player 5
    show eve 2
    eve "Ты что пропустил ту часть где он разбил очки без причины и его это развеселило?"
    show eve 1
    show player 14
    player_name "... Ты права."
    player_name "Он заслуживает немного страданий, не так ли?"
    show player 13
    show eve 2
    eve "Да, заслуживает."
    eve "Давай, мы должны вернуться в класс."
    hide player
    hide eve
    with dissolve
    return

label basketball_court_bissette_get_books:
    scene basketball_b
    show dexter 2 at right
    show player 10 at left
    with dissolve
    player_name "Хей, эмм, {b}Декстер{/b}..."
    show player 5
    show dexter 3
    dex "Че надо ЧМО?"
    show dexter 1
    show player 10
    player_name "Я надеялся, что у тебя все еще есть библиотечная книга, которую ты взял..."
    show player 5
    show dexter 8
    dex "Библиотечная книга?"
    show dexter 6 with dissolve
    show player 11
    dex "Я че похож на парня, который будет читать библиотечные книги?"
    dex "...Или ты подумал что я какой-то ботаник, как ты или твой друг-имбирь?"
    show dexter 2 with dissolve
    show player 10
    player_name "Что? Нет, Я не..."
    show player 11
    show dexter 4 with dissolve
    dex "Тебе лучше свалить отсюда, {b}[firstname]{/b}, пока я не напинал под сендвич!"
    show dexter 2 with dissolve
    show player 12
    player_name "Хорошо, хорошо, ухожу!"
    hide dexter with dissolve
    show player 10f at center with dissolve
    player_name "Интересно, может библиотекарша ошиблась?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "Он мог и солгать. {b}Я должен проверить его шкафчик{/b}!"
    player_name "Надеюсь, книга там, иначе я не знаю, что делать..."
    hide player with dissolve
    return

label basket_ball_court_take_magazines:
    if player.location.is_here(M_dexter):
        if not M_ross.get("take porno fail"):
            call expression game.dialog_select("basketball_court_ross_magazines_intro")
        else:

            call expression game.dialog_select("basketball_court_ross_magazines_retry")

        if player.has_required_dex(3):
            call expression game.dialog_select("basketball_court_ross_magazines_dex_pass")
            call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
            $ M_ross.set("magazine dexter", True)
        else:

            call expression game.dialog_select("basketball_court_ross_magazines_dex_fail")
            $ M_ross.set("take porno fail", True)
    $ game.main()

label basketball_court_ross_magazines_intro:
    scene basketball_b
    show player 579
    with dissolve

    player_name "Похоже, кто-то оставил несколько журналов, сидя здесь ..."
    show player 579c
    player_name "( Вау !!! )"
    player_name "( Это порно журналы!) "
    becca "Что ты дел-"
    hide player
    show player 578 at left
    show becca 2bf zorder 1 at right
    with dissolve
    becca "ЭЭЭЭЙЙЙЙ!!!"
    show becca 2f
    becca "Ты просто ходишь с этим, извращенец?!"
    show player 579
    show becca 1f
    player_name "Что?! Нет! Я просто нашел их..."
    show player 578
    show becca 2bf
    becca "Без разницы Ты отвратителен!"
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    dex "Что здесь происходит!?"
    show dexter 24
    dex "Это чмо беспокоит тебя, Бекка?"
    show dexter 23
    show becca 2bf
    becca "Он ходит тут с {b}порножурналами{/b} как полный чмошник!"
    show dexter 21
    show becca 1f
    show player 579
    player_name "Нет! Серьезно, они просто лежали здесь."
    show player 578
    show dexter 22
    dex "Ты отталкиваешь {b}друзей Рокси{/b} малыш."
    hide player
    hide dexter
    show becca 2bf
    show dexter 25_26
    with dissolve
    dex "Думаю, мне лучше забрать их, пока ты не заразил её!"
    return

label basketball_court_ross_magazines_retry:
    scene basketball_b
    show player 578 at left
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show becca 1f zorder 1 at right
    with dissolve
    dex "Вернулся за добавкой, да?!"
    show dexter 23
    show becca 2bf
    becca "Как грубо..."
    show dexter 22
    show becca 1f
    dex "Думаю, тебе нужен еще один урок."

    hide player
    hide dexter
    show becca 2bf
    show dexter 25_26
    with dissolve
    dex "Передайте их ничтожеству!"
    return

label basketball_court_ross_magazines_dex_pass:
    show dexter 26b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "Отвали от меня, чертова тупица!"
    hide dexter
    show player 38 at left
    show dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dex "Эй! Иди сюда, я наваляю тебе!"
    show player 15
    show dexter 21
    player_name "Сначала поймай меня! Ты гигант... ЧУДИЛО!"

    hide player with dissolve
    show becca 4f
    show dexter 23
    becca "ПФФФФ, хахахаха!"
    show dexter 22
    dex "Ты думаешь что умнее раз знаешь больше слов?!"
    show dexter 22 at Position(xpos=0.45, ypos=1.0) with dissolve
    show becca 1f
    dex "А ну вернись!"
    hide dexter with dissolve
    show becca 4f
    becca "... чудило! Хахаха!"
    hide becca
    return

label basketball_court_ross_magazines_dex_fail:
    show becca 1f
    player_name "[dex_warn]Хей, отвали громила!"
    dex "[dex_warn]Отпусти журналы, Чмо!"
    hide dexter
    show dexter 27 with dissolve
    player_name "[dex_warn]Хорошо! Забирай!"

    show player 16 at left
    show dexter 22 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dex "[dex_warn]Я так и думал!"
    dex "[dex_warn]А теперь проваливай, пока я тебя не побил!"

    show player 15
    show dexter 21
    player_name "[dex_warn]Гррр, ты такой засранец!"
    hide player
    show dexter 28
    show becca 4f
    with dissolve
    dex "[dex_warn]Да, так и есть, Сосунок! Беги отсюда!"
    return

label basketball_court_roxxy_dexter_alcohol_fight:
    scene basketball_b
    show dexter 2 at right
    show becca 1 at Position(xpos=315)
    show missy 2b at left
    show roxxy 30f at Position (xpos=500)
    with dissolve
    rox "Ты серьезно не принесешь нам выпивки?!"
    show roxxy 29f
    show dexter 8
    dex "... Нет пока ты не извенишься!"
    show dexter 2
    show roxxy 30f
    rox "Забудь!"
    show roxxy 29f
    show becca 2
    becca "Давай {b}Рокси{/b}, извинись..."
    becca "Вечеринка будет отстойной без алкоголя!"
    show becca 1
    show roxxy 30f
    rox "Низачто!"
    rox "Он ведет себя как большой ребенок..."
    show roxxy 29f
    show dexter 8
    dex "О, сначала я глупый, а теперь ещё и ребенок..."
    dex "Уточни?"
    show dexter 2
    show roxxy 3bf
    rox "..."
    show roxxy 30f
    rox "И то и другое!"
    rox "Просто глупый ребенок-переросток!"
    show roxxy 29f
    show missy 6
    missy "Пффф, хахаха!"
    show missy 3
    show dexter 8
    dex "Эй!! Не смейся надо мной, {b}Мисси{/b}!"
    show dexter 2
    show missy 2b
    missy "..."
    show missy 2
    missy "Моя ошибка..."
    show missy 2b
    show dexter 3 with dissolve
    dex "Если ты так сильно хочешь алкоголя, почему бы тебе не пойти и не спросить того никчемного пьяницу, которого ты называешь {b}мамой{/b}?"
    show dexter 1
    show roxxy 2bf
    rox "!!!"
    show roxxy 30f
    rox "... Пошёл нахуй!"
    rox "Знаешь что?!"
    rox "Все, с меня хватит!"
    show roxxy 29f
    show dexter 8
    dex "Да ну, меня это устраивает!"
    show dexter 2
    show roxxy 3c with dissolve
    rox "Пошли девочки."
    rox "Оставим этого ГЛУПОГО засранца!"
    hide roxxy with dissolve
    show becca 2b
    becca "Угх..."
    show becca 2f at Position(xpos=315) with dissolve
    becca "{b}Рокси{/b}, что мы будем делать с выпивкой?!"
    hide becca
    hide missy
    show missy 3f at Position(xpos=250)
    with dissolve
    missy "..."
    show missy 3 with dissolve
    missy "..."
    show dexter 6 with dissolve
    dex "На что уставилась, тощая сучка?!"
    show dexter 2
    show missy 4c
    with dissolve
    missy "!!!"
    hide missy with dissolve
    dex "..."
    show dexter 4 with dissolve
    dex "Гррр, мне нужно ударить что-нибудь!"
    hide dexter with dissolve
    pause
    show player 13 at left
    show eve 2 at right
    with dissolve
    eve "Черт!"
    eve "{b}Декстера{/b} отшили!"
    show eve 5
    show player 14
    player_name "Да, не хотел бы я попасться ему на пути."
    show player 13
    show eve 5
    eve "Реально!"
    eve "Пойдем, нам нужно вернуться в {b}класс Мисс Биссетт{/b}."
    hide eve
    hide player
    show player 4
    with dissolve
    player_name "( ... )"
    player_name "( Да, похоже, что {b}Рокси{/b} тоже туда направляется.)"
    player_name "( ... Может мне {b}поговорить с ней{/b}? )"
    scene black with fade
    return

label basketball_court_roxxy_basketball_challenge:
    scene basketball_b
    show player 90 at left
    show dexter 32 at right
    with dissolve
    dex "Готов к матчу-реваншу, неудачник?!"
    show dexter 31
    show player 12
    player_name "{b}Декстер{/b}, на этот раз ты проиграешь."
    show player 90
    show dexter 3
    dex "Хахаха!"
    dex "Ага, точно."
    show player 647
    show dexter 33
    with dissolve
    dex "Твой мяч, сука!"
    show dexter 11 at Position (xoffset=2) with dissolve
    show player 648 with dissolve
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
