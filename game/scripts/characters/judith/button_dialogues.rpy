label judith_dialogue_start:
    scene lefthall_c
    show player 1 at left
    show judith 5 at right
    with dissolve
    jud "Эй {b}[firstname]{/b}!"
    show player 2 at left
    show judith 4 at right
    player_name "Эй {b}Judith{/b}, как дела?"
    show player 1 at left
    show judith 5 at right
    jud "О, Я в порядке!"
    show judith 2 at right
    jud "Я... я просто хотела поблагодарить тебя."
    show judith 4 at right
    show player 21 at left
    player_name "Ох,за что?"
    show judith 3 at right
    show player 13 at left
    jud "В раздевалке... с тобой я чувствовала себя в... безопасности."
    show judith 4 at right
    show player 11 at left
    player_name "Oх..."
    show judith 5 at right
    jud "И,ты знаешь... ты дал отпор {b}Annie{/b}.Я думаю, это было очень смело."
    show judith 4 at right
    show player 29 at left
    player_name "Все в порядке, {b}Judith{/b}.Я просто пытался поступить правильно.."
    player_name "Это я должен извиниться... я показал тебе мой... ты знаешь..."
    show judith 5 at right
    show player 11 at left
    jud "Ох все в порядке!!Мне понравилось-"
    show judith 3 at right
    jud "Я имею в виду... Я вообше не возражала."
    show judith 5 at right
    jud "Нам просто надо... узнать друг друга немного лучше!"
    show judith 4 at right
    show player 21 at left
    player_name "Хаха. Да. Я так думаю..."
    show judith 5 at right
    show player 1 at left
    jud "Я должна идти!Увидимся в классе тогда.!"
    show player 14 at left
    show judith 4 at right
    player_name "Увидимся позже!"
    return

label judith_dialogue_left_hallway_intro:
    scene lefthall_c
    show judith 1 at right
    show player 14 at left
    with dissolve
    player_name "Хэй, {b}Judith{/b}!"
    show player 13
    show judith 5
    jud "Ох привет, {b}[firstname]{/b}."
    jud "Как дела?"
    show judith 4
    show player 14
    player_name "Очень хорошо.Как ты?"
    show player 13
    show judith 6
    jud "..."
    show judith 2
    jud "Хорошо, я думаю."
    show judith 1
    return

label judith_dialogue_art_classroom_intro:
    scene art_classroom_c
    show judith 1 at right
    show player 14 at left
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    player_name "Наслаждаешься искусством, {b}Judith{/b}?"
    show player 13
    show judith 5
    jud "Да!"
    jud "Это одна из моих любимых тем."
    show judith 4
    show player 14
    player_name "Да, мне тоже!"
    show player 13
    show judith 5
    jud "Мне это нравится, потому что независимо от того, насколько плохи мои рисунки, это все еще считается искусством!"
    show judith 4
    show player 17
    player_name "Хех, это хорошо."
    show judith 1
    return

label judith_dialogue_bathroom_fun:
    show player 2
    player_name "Скажи, ты бы хотел прокрасться в женскую раздевалку на немного... Ты знаешь?"
    show player 1
    show judith 5
    jud "... Ты действительно хочешь..."
    jud "... С-со мной?"
    show player 2
    show judith 4
    player_name "В всмысле, да!"
    player_name "Если ты не против?"
    show player 1
    show judith 5
    jud "О,определенно!"
    jud "Пошли!"
    return

label judith_dialogue_dictionary_return:
    show player 14
    player_name "Привет, {b}Judith{/b}!Возвращаю твою книгу."
    show player 239_240 with dissolve
    pause
    show player 522 with dissolve
    player_name "Спасибо еще раз!"
    show player 13
    show judith 43
    with dissolve
    jud "Ох,хорошо Я уже начала волноваться...."
    show judith 4 with dissolve
    show player 14
    player_name "Не нужно беспокоиться.Она отличной форме... Посмотри."
    show player 13
    show judith 5
    jud "Спасибо что бы осторожен с ней, {b}[firstname]{/b}."
    jud "Не знаю, почему я так волнавалась..."
    show judith 4
    show player 14
    player_name "Спасибо, что одолжила мне её.!"
    show player 13
    show judith 5
    jud "Все что угодно для те-"
    show judith 3
    jud "В смысле... в любое время!"
    show judith 1
    show player 10
    player_name "Хорошо, ну, увидимся позже.."
    show player 5
    show judith 3
    jud "Пока, {b}[firstname]{/b}."
    return

label judith_dialogue_bissette_find_full_dictionary:
    show player 14
    player_name "Привет, {b}Judith{/b}! Есть минутка?"
    show player 13
    show judith 5
    jud "Конечно, {b}[firstname]{/b}."
    show judith 4
    show player 14
    player_name "Я надеялся что смогу одолжить у тебя твой Французский словарь.."
    player_name "Мне нужно сделать быструю копию некоторых страниц и я верну его."
    show player 13
    show judith 3
    jud "Мой Французский словарь?"
    show judith 5
    jud "Безусловно!До тех пор, пока ты обещаешь быть осторожен с ним?"
    show judith 4
    show player 11
    player_name "( Что с женщинами и их французскими словарями? )"
    show player 10
    player_name "Да,Я буду очень осторожен,и ты даже не заметишь, что он исчез.."
    show player 13
    show judith 5
    jud "Хорошо,Я верю тебе, {b}[firstname]{/b}."
    pause
    show judith 43 with dissolve
    jud "Вот он..."
    show judith 4
    show player 522
    with dissolve
    player_name "Спасибо{b}Judith{/b}! Я твой должник!"
    hide judith with dissolve
    show player 13
    player_name "( Хорошо, теперь {b}направляйтесь в компьютерный класс{/b} и скопировать эти недостающие страницы. )"
    return

label judith_dialogue_dewitt_find_flute:
    show player 10
    player_name "У тебя все еще есть школьная флейта?"
    player_name "Мне она нужна для шоу талантов ."
    show player 5
    show judith 2
    jud "Ох, эммм..."
    show judith 1
    show player 10
    player_name "Этот интструмент был выписан на твое имя."
    show player 5
    show judith 2
    jud "*Вздох*"
    show judith 3
    jud "У меня она есть.Она в моем шкафчике."
    show judith 1
    show player 12
    player_name "У меня такое чувство, что \"но\" пришло?"
    show player 5
    show judith 3
    jud "Но, Я вроде как сломала её..."
    show judith 1
    show player 1
    player_name "Ты сломала её!?"
    player_name "Как это случилось?!"
    show player 5
    show judith 5
    jud "Хех, ну я как-то нечаянно ..."
    show judith 6
    show player 11
    player_name "..."
    show judith 2
    jud "... Села на неё."
    show judith 1
    show player 10
    player_name "Ты села на неё?"
    show player 11
    show judith 3
    jud "... Да."
    show judith 5
    jud "Это так отстойно потому что я очень наслаждалась ей!"
    show judith 4
    show player 10
    player_name "Я не знал, что ты умеешь играть на флейте?"
    show player 5
    show judith 5
    jud "Ох, Я не могу на ней играть."
    show judith 4
    show player 12
    player_name "Тогда я не понимаю, как тогда она тебе нравилась?"
    show player 5
    jud "..."
    show judith 5
    jud "Хех, неважно."
    show judith 2
    jud "Я надеялась, что никто не спросит меня об этом..."
    show judith 1
    show player 10
    player_name "Может быть, я смогу починить её?"
    show player 5
    show judith 4
    jud "..."
    show judith 5
    jud "Ты можешь попробовать."
    show judith 4
    show player 12
    player_name "Она все еще в твоем шкафчике??"
    show player 5
    show judith 5
    jud "Ага."
    show judith 4
    show player 10
    player_name "Хорошо, спасибо, {b}Judith{/b}."
    return

label judith_dialogue_talent_show_help:
    show player 10
    player_name "Мне интересно, не хочешь ли ты принять участие в предстоящем шоу талантов?"
    show player 5
    show judith 3
    jud "Нет спасибо, {b}[firstname]{/b}.Я не знаю, как играть на инструменте."
    show judith 2
    jud "... И Мне слишком стыдно вставать на сцену перед всей школой."
    show judith 1
    show player 10
    player_name "Что ж, если бы мы играли вместе?"
    show player 5
    show judith 5
    jud "Ты и я?"
    show judith 4
    show player 14
    player_name "Конечно, почему нет?"
    show player 13
    show judith 6
    jud "Хмм..."
    show judith 2
    jud "Нет, прости, {b}[firstname]{/b}."
    show judith 3
    jud "Как бы мне не нравилось играть с тобой;Просто мысль о том, чтобы быть в центре внимания вроде этого..."
    show judith 8f at Position (xoffset=2) with dissolve
    show player 11
    jud "..."
    show judith 9f at Position (xoffset=-4) with dissolve
    jud "Извините, мне нужно в туалет!"
    hide judith with dissolve
    show player 12
    player_name "Блин блинский, Я на секунду подумал, что она согласится."
    show player 10
    player_name "Думаю, мне лучше продолжить поиски..."
    return

label judith_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Judith, вы дальнозоркая или близорукая"
    show player 1
    show judith 2
    jud "Эмм, ну."
    show judith 3
    jud "Оба..."
    show player 2
    show judith 1
    player_name "Реально?!"
    show player 1
    show judith 2
    jud "Да. Я слепа без своих очков..."
    show judith 3
    jud "Довольно тупо.Я знаю..."
    show player 2
    show judith 1
    player_name "Нет,Это классно!"
    show player 1
    show judith 3
    jud "Это так?"
    show player 29 with dissolve
    show judith 1
    player_name "Ну я всмысле, нет.Это хреново, что вы не можете видеть без них."
    show player 2 with dissolve
    player_name "... Но это также хорошая вещь, потому что я ищу пару Варифокальных линз.."
    show player 1
    show judith 5
    jud "Ох.что ж, ты некоторые нашел."
    show player 2
    show judith 4
    player_name "У тебя случайно нет запасной пары?"
    show player 1
    show judith 5
    jud "Конечно."
    show player 2
    show judith 4
    player_name "Круто! Могу ли я их взять?"
    show player 1
    show judith 2
    jud "Хмм,ты хочешь, чтобы я просто тебе отдала свою запасную пару?"
    show player 10
    show judith 1
    player_name "... Да?"
    show player 11
    show judith 3
    jud "Как на счёт сделки?"
    show player 2
    show judith 1
    player_name "Да, хорошо.Что ты хочешь?"
    show player 1
    show judith 2
    jud "Эмм, это немного смущает..."
    show judith 1
    player_name "..."
    show judith 2
    jud "Ну, видишь ли, некоторые другие девушки доставляли мне много хлопот...."
    show judith 3
    jud "... потому что у меня никогда не было парня."
    show player 10
    show judith 1
    player_name "Это фигово."
    show player 11
    show judith 2
    jud "Да."
    jud "Мне было любопытно..."
    show judith 3
    jud "... Ну, я надеялась, что ты притворишься моим парнем."
    show player 23
    show judith 1
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Ты хочешь, чтобы я притворялся твоим парнем?"
    show player 11
    show judith 3
    jud "Достаточно, чтобы сделать пару снимков!"
    show player 10
    show judith 1
    player_name "Снимков?!"
    show player 11
    show judith 2
    jud "Да."
    show judith 3
    jud "Ты встретил меня в парке, мы делаем пару фотографий, как будто мы парень и девушка, и тогда я дам тебе свой запасную пару."
    jud "Сделка?"
    show player 10
    show judith 1
    player_name "Я эмм..."
    show player 11
    show judith 3
    jud "Пожалууууйста? Это была бы такая огромная помощь!"
    show player 2
    show judith 1
    player_name "Да, хорошо, думаю, я смогу это сделать."
    show player 1
    show judith 5
    jud "Ты сделаешь?!"
    jud "Хорошо,встретимся в парке.!Я буду там {b}вечером{/b}."
    show player 2
    show judith 4
    player_name "{b}В парке,вечером.{/b} Понял!"
    show player 1
    show judith 5
    jud "Отлично! Увидимся там!"
    return

label judith_dialogue_okita_take_picture_judith:
    show player 2
    player_name "Где ты хотела сделать эти фотографии снова?"
    show player 1
    show judith 3
    jud "Ох эмм, в парке."
    show player 2
    show judith 1
    player_name "Хорошо."
    show player 1
    show judith 3
    jud "Ты ведь не передумал, не так ли?"
    show judith 2
    jud "Потому что все хорошл, Мы не-"
    show player 2
    show judith 1
    player_name "Нет, {b}Judith{/b}. Все в порядке, правда!"
    show judith 4
    player_name "Встретимся там!"
    show player 1
    show judith 5
    jud "... Спасибо, {b}[firstname]{/b}."
    return

label judith_dialogue_ross_ask_model:
    show player 2
    player_name "Я работаю над проектом для {b}Miss Ross{/b} и для этого требуется живая модель."
    player_name "Ты была бы не заинтересована?"
    show player 1
    show judith 5
    jud "Ты хочешь, чтобы я позировала для тебя?"
    show player 2
    show judith 4
    player_name "Да, это было бы здорово!"
    show player 10
    player_name "Это обнаженное моделирование, хотя..."
    show player 11
    show judith 3
    jud "... Ох."
    show judith 1
    jud "..."
    show judith 3
    jud "... Ты действительно хочешь, чтобы я?"
    show player 10
    show judith 1
    player_name "Конечно!"
    show player 11
    show judith 5
    jud "Тогда я сделаю это! Для тебя, {b}[firstname]{/b}!"
    show player 2
    show judith 4
    player_name "Спасибо {b}Judith{/b}! Это действительно круто с твоей стороны!"
    player_name "Просто встретимся в художественном классе."
    show player 1
    show judith 5
    jud "Хорошо."
    return

label judith_dialogue_left_hallway_leave:
    show player 5
    player_name "..."
    show judith 6
    jud "..."
    show player 29 with dissolve
    player_name "Что ж... Я пожалуй пойду.!"
    show player 3
    show judith 5
    jud "Увидимся позже, {b}[firstname]{/b}."
    return

label judith_dialogue_art_classroom_leave:
    show player 14
    player_name "Увидимся позже, {b}Judith{/b}."
    show player 13
    show judith 5
    jud "Пока, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
