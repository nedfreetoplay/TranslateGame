label bissette_book_search_2_books_left:
    show player 12 with dissolve
    player_name "Ладно, осталось ещё две книги."
    hide player with dissolve
    return

label bissette_book_search_1_book_left:
    show player 14 with dissolve
    player_name "Осталась всего одна книга."
    hide player with dissolve
    return

label bissette_book_search_no_books_left:
    show player 14 with dissolve
    player_name "Прекрасно! Я нашёл все книги!"
    player_name "Осталось только вернуть их в библиотеку!"
    hide player with dissolve
    return

label annie_locker_first_visit:
    player_name "Окей. Этого я и ожидал."
    player_name "{b}Энни{/b} прям помешана на {b}директоре Смит{/b}."
    return

label dexter_locker_first_visit:
    player_name "Лучше {b}Декстеру{/b} меня сейчас не видеть."
    player_name "Типичные шмотки спортсмена."
    player_name "Тут ещё и эта отвратная помпа."
    return

label dexter_locker_book_search:
    player_name "Он врал! Я так и знал!"
    return

label dexter_locker_book_found:
    scene dexter_locker
    show book_05_c with dissolve
    player_name "{b}Мафематика для чайников{/b}?"
    player_name "Это ж книга для первоклашек..."
    player_name "Хех, думаю, она показывает его уровень мафе-"
    player_name "Математики!"
    player_name "Нужно убираться отсюда!"
    player_name "Походу я начинаю тупеть рядом со шкафчиком {b}Декстера{/b}!"
    hide book_05_c with dissolve
    show expression game.timer.image("location_school_right_hall_day{}_blur")
    return

label erik_locker_first_visit:
    player_name "У {b}Эрика{/b} полно всякого барахла по {b}Подземельям и орчихам{/b}."
    player_name "А это его ланчбокс."
    player_name "Его мама всегда кладёт ему туда домашнюю еду."
    player_name "Счастливчик. Его мама должно быть любит его."
    return

label eve_locker_first_visit:
    player_name "Нифига себе! Лучше бы ей никому не показывать свой шкафчик."
    player_name "Эти наушники выглядят удобными."
    return

label eve_locker_drawing_pick_up:
    $ player.get_item("eve_drawing")
    call expression game.dialog_select("eve_locker_drawing_picked_up")
    $ player.location.call_screen(False)

label eve_locker_drawing_picked_up:
    scene eve_locker
    show closeup_drawing_01
    with dissolve
    player_name "Ох, это РЕАЛЬНО круто!"
    player_name "... {b}Чад{/b} был прав. Это правда сексуально!"
    player_name "Интересно, что она подумает о таком наряде?"
    show expression "boxes/popup_item_drawing1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_drawing1.png"
    hide closeup_drawing_01
    with dissolve
    return

label judith_locker_first_visit:
    player_name "Ммм... {b}Маунтин Джиз{/b}."
    player_name "Этой штукой не сложно замараться."
    player_name "Должно быть из-за сахара, который делает его таким липким."
    pause
    player_name "Наверное ей нравятся коровы."
    player_name "Да и мне то-"
    player_name "Эй! Откуда у неё моё фото?"
    return

label take_judith_glasses:
    scene judith_locker
    player_name "Должно быть это её запасные очки."
    show expression "boxes/popup_item_glasses1.png" at truecenter with dissolve
    $ player.get_item("judith_glasses")
    pause
    player_name "Теперь мне нужно отнести их Оките."
    pause
    $ game.main()

label take_broken_flute:
    scene judith_locker
    player_name "( Это наверное {b}флейта{/b}, которую сломала Джудит. )"
    scene lefthall_c with fade
    $ player.get_item("broken_flute")
    call expression game.dialog_select("take_broken_flute_dialogue")
    $ M_dewitt.trigger(T_dewitt_get_flute)
    $ game.main()

label take_broken_flute_dialogue:
    show player 563f at left with dissolve
    player_name "Вау, эту штуку нехило сплющило..."
    player_name "Её всю перекорёжило!"
    show player 564f with dissolve
    pause
    show player 565f with dissolve
    player_name "Хмм, на запах тоже ничего."
    show player 564f with dissolve
    show erik 5 at right with dissolve
    eri "Эмм, что ты тут делаешь, чувак?"
    show erik 52
    show player 22f at Position (xoffset=139) with hpunch
    player_name "!!!"
    show player 29 with dissolve
    player_name "Н-ничего! Ты меня блин напугал!"
    show player 14 with dissolve
    player_name "Что ты тут делаешь?"
    show player 13
    show erik 5
    eri "Просто иду на следующий урок..."
    show erik 53
    eri "Это была флейта?"
    show player 563
    show erik 3c
    with dissolve
    player_name "Д-да. Ну, она уже видала виды."
    show player 562
    show erik 53
    eri "Да уж..."
    show erik 3c
    show player 563
    player_name "Она нужна мне, для шоу талантов {b}Мисс Девитт{/b}."
    show player 13 with dissolve
    show erik 5
    eri "Хмм, может ты скрафтишь свою?"
    show erik 52
    show player 10
    player_name "Думаешь?"
    show player 5
    show erik 54
    eri "Конечно!"
    show erik 4
    eri "Я как то скрафтил флейту в одной игре."
    eri "Тебе нужна хорошая деревяшка и дрель, чтобы проделать дырочки."
    show erik 1
    show player 12
    player_name "Ты сделал флейту в видеоигре?"
    show player 5
    show erik 4
    eri "Ага! Я заюзал её, чтобы склеить всех орчих в деревне!"
    eri "А потом у нас была шикарная оргия в хижине Шефа!"
    show erik 1
    show player 10
    player_name "Оу, это... здорово."
    show player 5
    show erik 4
    eri "Эй, чувак, это было офигенно. Я прям отвечаю!"
    show player 13
    show erik 54
    eri "Зелёные чики просто огонь в постели!"
    show erik 1
    show player 14
    player_name "Ладно, пойду делать флейту из говна и палок."
    show player 13
    show erik 4
    eri "Оу, хорошо. Я тебя понял."
    show erik 1
    show player 14
    player_name "Спасибо, {b}Эрик{/b}."
    show player 13
    show erik 4
    eri "Да не за что, чувак!"
    hide player
    hide erik
    with dissolve
    return

label kevin_locker_first_visit:
    player_name "Что?"
    player_name "Это похоже на мои пропавшие трусы!"
    pause
    player_name "Не знал, что мы купили один комплект."
    return

label mia_locker_first_visit:
    player_name "От шкафчика {b}Мии{/b} приятно пахнет."
    return

label mia_locker_first_visit_early_route:
    player_name "У неё такая классная жизнь."
    return

label mia_locker_first_visit_helping_parents:
    player_name "Мне нужно помочь её родителям воссоединиться."
    return

label mia_locker_first_visit_helen_route:
    player_name "Наверное стоило помочь её родителям воссоединиться..."
    return

label ronda_locker_first_visit:
    player_name "Есть вообще какой-то вид спорта, в котором она ничего не умеет?"
    player_name "Наверное, благодаря этому она поступит в колледж на бюджет."
    player_name "Она с головой уходит в школьную жизнб."
    return

label roxxy_locker_first_visit:
    player_name "Вау."
    player_name "Шкафчик {b}Рокси{/b} такой милый."
    player_name "Похоже она выиграла в лотерею целую банку {b}Черри-чупсов{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
