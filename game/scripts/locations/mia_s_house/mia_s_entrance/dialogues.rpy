label mias_entrance_mia_parent_blocking:
    scene mia_house_c
    show helen 2 zorder 1 at right
    show player 1 at left
    with dissolve
    helen "...а ты кто такой?"
    show helen 1
    show player 14
    player_name "Я {b}[firstname]{/b}!"
    player_name "Школьный товарищ..."
    show helen 2
    show player 1
    helen "Друг?"
    show player 11
    helen "Наша дочь обычно не приводит друзей домой."
    helen "Она никого не предупредила о твоём визите..."
    helen "Вы с ней познакомились в церкви?"
    show helen 1
    show player 10
    player_name "Нет?"
    show helen 2
    show player 11
    helen "А ты посещаешь церковь, {b}[firstname]{/b}?"
    show helen 1
    show player 10
    player_name "Охх... нечасто, мэм."
    show helen 2
    show player 11
    helen "Конечно не посещаешь."
    show helen 1
    show player 1
    show harold 2 zorder 0 at Position (xpos = 670, ypos = 768) with dissolve
    harold "Эй, дорогая!"
    harold "Это один из друзей {b}Мии{/b}?"
    show harold 1
    show helen 3
    show player 5
    helen "Этот юноша уже собирается уходить."
    hide helen
    hide harold
    hide player
    with dissolve
    return

label mias_entrance_mia_helen_fight:
    scene mia_house_c
    show helen 6f at left
    show mia 46f at right
    with dissolve
    mia "{b}МАМ{/b}!"
    mia "Как ты вообще это допустила?!"
    show mia 45f
    show helen 5f
    helen "Ох, прекрати это ребячество!"
    helen "Твой отец и я решили немного отдохнуть друг от друга..."
    helen "...мы связаны таинством венчания, которое выше всех разногласий!"
    helen "Нет греха в том..."
    hide helen with dissolve
    pause
    show player 10 at left with dissolve
    player_name "{b}Мия{/b}!"
    player_name "Я видел снаружи твоего отца и он-"
    show player 11
    show mia 46f
    mia "Мне нужна твоя помощь!"
    show mia 45f
    show player 10
    player_name "Постой, что?"
    show player 5
    show mia 46f
    mia "Мои родители расходятся и ты можешь помочь мне снова свести их!"
    show mia 45f
    show player 11
    player_name "!!!"
    show mia 46f
    mia "Ты мне... поможешь?"
    show mia 45f
    show player 10
    player_name "Ну, не уверен, что у меня полу-"
    show player 11
    show mia 46f
    mia "Поговори с моей мамой."
    mia "Я уже пыталась, но она меня не слышит..."
    show mia 45f
    show player 12
    player_name "Она никогда меня не слышит."
    show player 5
    show mia 46f
    mia "Ну пожалуйста!"
    show mia 45f
    show player 3 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Хорошо, я постараюсь."
    player_name "Но ничего не обещаю..."
    show player 5
    show mia 46f
    mia "Спасибо, {b}[firstname]{/b}."
    hide player
    hide mia
    with dissolve
    return

label mias_entrance_mia_helen_refusal:
    scene mia_house_c
    show player 5 at left
    show mia 12 at right
    with dissolve
    mia "Ты поговорил с ней?"
    show mia 8
    show player 24
    player_name "Да..."
    show mia 12
    mia "И что она сказала?"
    show mia 8
    show player 12
    player_name "Она очень упертая."
    player_name "Я же говорил, что она меня не послушает..."
    show player 5
    show mia 12
    mia "{b}*Вздох*{/b}"
    mia "{b}Мама{/b} слушается только {b}Бога{/b}...или {b}священника{/b}."
    show mia 8
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Постой."
    show player 29 with dissolve
    player_name "У меня есть идея!"
    show player 13 with dissolve
    show mia 12
    mia "Что за идея?"
    show mia 8
    show player 14
    player_name "Когда твоя мама ходит в церковь?"
    show player 13
    show mia 12
    mia "В {b}воскресение утром{/b}."
    show mia 8
    show player 34
    player_name "Хмм..."
    show player 14
    player_name "Хорошо, спасибо."
    show player 13
    show mia 12
    mia "Что ты собираешься сделать?!"
    show mia 8
    show player 12
    player_name "До конца ещё не придумал, но в случае чего, я всё тебе расскажу."
    show player 13
    show mia 12
    mia "Окей..."
    hide player
    hide mia
    with dissolve
    return

label mias_entrance_mia_urgent_help:
    scene mia_house_c
    show helen 25 at Position (xpos=700)
    show player 5 at left
    show mia 12 at right
    with dissolve
    mia "Ты получил мое сообщение?"
    show mia 8
    show helen 23
    show player 10
    player_name "Ага, что случилось?"
    show player 11
    show helen 25
    show mia 46f
    mia "Мы не можем найти папу..."
    show mia 45f
    show helen 26
    helen "Пока особо не о чем волноваться. Но всё же..."
    show player 5
    show helen 24
    helen "...он не звонил несколько дней. Это совсем на него не похоже."
    show helen 25
    show mia 46f
    mia "Обычно он звонил каждый день и спрашивал как мы..."
    mia "...что, если с ним произошло что-то {b}УЖАСНОЕ{/b}?!"
    show mia 45f
    show player 22
    player_name "!!!"
    show helen 26
    helen "{b}Мия{/b}!"
    helen "Не говори так, я уверена, он скоро вернётся."
    show helen 23
    show player 10
    player_name "Не уверен, что смогу быть полезен..."
    player_name "...но я хочу помочь!"
    show player 5
    show helen 24
    helen "Если хочешь помочь, опроси его коллег в {b}полицейском участке{/b}..."
    helen "...и поищи {b}зацепки{/b} на его рабочем месте."
    helen "С этого, я думаю, следует начать."
    show helen 25
    show mia 46f
    mia "Ты поможешь, {b}[firstname]{/b}?"
    show mia 45f
    show helen 23
    show player 35
    player_name "Думаю, я могу поспрашивать людей о том, где он может быть..."
    show player 34
    helen "..."
    show helen 24
    helen "Возможно я была неправа насчет тебя, {b}[firstname]{/b}."
    show player 13
    helen "Спасибо...за то, что помогаешь нашей семье."
    show helen 23
    show player 12
    player_name "Ладно, пойду попробую найти {b}Гарольда{/b}."
    show player 5
    show helen 25
    show mia 46f
    mia "Возвращайся, если разузнаешь что-нибудь!!"
    show mia 45f
    show helen 23
    show player 14
    player_name "Хорошо!"
    hide player
    hide mia
    hide helen
    with dissolve
    return

label mias_entrance_mia_harold_found_news:
    scene mia_house_c
    show player 13 at left
    show helen 24 at Position (xpos=700)
    with dissolve
    helen "{b}[firstname]{/b}?"
    show helen 23
    show player 14
    player_name "Здравствуйте, {b}Хелен{/b}!"
    show player 13
    show helen 24
    helen "Ну как... Ты узнал где мой муж?"
    show helen 23
    show player 12
    player_name "Ну да, я недавно поговорил с ним лично."
    show player 10
    player_name "Он...отдыхает, катаясь по городу."
    show player 5
    show helen 24
    helen "Понимаю."
    helen "И как он?"
    show helen 23
    show player 10
    player_name "Ему немного... тяжело."
    show player 5
    show helen 24
    helen "Я... я хочу знать всё. Что сказал тебе {b}Гарольд{/b}?"
    show helen 23
    show player 10
    player_name "Не уверен, что он вернётся домой... но он сказал, что перезвонит."
    show player 5
    show helen 24
    helen "Хмм... Он говорил что-нибудь обо мне?"
    show helen 23
    show player 10
    player_name "Охх... Ну, он сказал, что вы изменились... и что раньше он был намного счастливее..."
    show player 5
    show helen 3 with dissolve
    helen "{b}*Вздох*{/b}"
    show helen 24 with dissolve
    helen "Хорошо, спасибо, что всё рассказал..."
    show helen 25
    show mia 10 at right with dissolve
    mia "{b}[firstname]{/b}?!"
    show mia 7
    show helen 23
    show player 14
    player_name "Привет, {b}Мия{/b}!"
    show player 13
    show helen 25
    show mia 10
    mia "Когда ты пришёл?"
    show mia 7
    show helen 23
    show player 14
    player_name "Да только что."
    show player 12
    player_name "Я нашел твоего папу."
    show player 5
    show helen 25
    show mia 12
    mia "С ним все в порядку?!"
    show mia 8
    show helen 3 with dissolve
    helen "Твой отец в порядке, милая."
    show helen 26 with dissolve
    helen "Он просто...отдыхает, но вскоре он навестит нас. Обещаю."
    show helen 25
    show mia 10
    mia "...Правда?"
    show mia 7
    show helen 23
    show player 29 with dissolve
    player_name "Я думаю, да."
    show player 3
    show helen 25
    show mia 10
    mia "Это замечательно!"
    mia "Огромное спасибо, {b}[firstname]{/b}..."
    mia "...прости, что втянула тебя во всё это."
    mia "Я просто рада, что ничего серьёзного не случилось."
    show mia 7
    show helen 23
    show player 12
    player_name "{b}Гарольд{/b} вернётся, не волнуйся."
    show player 14
    player_name "Увидимся в школе!"
    hide player
    hide mia
    hide helen
    with dissolve
    return

label mias_entrance_mia_route_split:
    scene mia_indoors with fade
    show player 13 at left
    show harold 1 at right
    show helen 50 at Position (xpos=700)
    show mia 7 at Position (xpos=500)
    with dissolve
    harold "А вот и он!"
    show harold 1
    show player 14
    player_name "Хей! Я не ожидал вас всех здесь увидеть."
    show player 13
    show helen 51
    helen "{b}Гарольд{/b} понемногу начал возвращаться к нам."
    show helen 50
    show harold 2
    harold "Так здорово снова быть дома."
    show harold 1
    show mia 10
    mia "Теперь, когда мы снова вместе, мы можем становится лучше как семья."
    mia "Давайте скажем спасибо {b}[firstname]{/b} за помощь."
    show mia 7
    show harold 2
    harold "Я рад, что мы познакомились поближе..."
    harold "...чувствуй у нас себя как дома, можешь даже с ночёвкой приходить!"
    show harold 1
    show helen 26
    helen "{b}Гарольд{/b}?! Я не уверена, что-"
    show helen 25
    show harold 2
    harold "Да ладно тебе, {b}Хелен{/b}, этот юноша - возможно, наш будущий зять!"
    show harold 1
    show helen 50
    show mia 10
    mia "{b}Пап{/b}!"
    show mia 7
    show helen 51 with dissolve
    helen "{b}Гарольд{/b}!"
    show helen 50
    harold "..."
    show harold 2
    harold "Давай пойдём в гостиную, молодёжи нужно побыть наедине."
    show harold 1
    show helen 26
    helen "Как скажешь, дорогой."
    hide harold
    hide helen
    with dissolve
    show player 14
    player_name "Я так рад, что всё	сработало."
    player_name "Похоже твои родители снова поладили..."
    show player 13
    show mia 9
    mia "Я знаю! Лучше просто и быть не могло!"
    show mia 10
    mia "Спасибо тебе, {b}[firstname]{/b}... за всё."
    show mia 7
    show player 14
    player_name "Да неза-"
    hide player
    show mia 49 at left
    with dissolve
    player_name "!!!" with hpunch
    show player 13 at left
    show xtra 21 at left
    hide mia
    show mia 9 at Position (xpos=500)
    with dissolve
    mia "Слууушай, теперь снова всё как раньше."
    show mia 10
    mia "Мы же можем снова вместе... готовиться к школе?"
    show mia 7
    show player 21
    player_name "Это отличная идея!"
    show player 13
    show mia 10
    mia "Целыми ночами."
    mia "Я тут купила журнал, в котором описана потрясающая методика обучения."
    mia "Я надеюсь что мы... её опробуем."
    show mia 7
    show player 21
    player_name "Здорово! Я в деле!"
    show player 13
    show mia 10
    mia "Буду ждать! До встречи, {b}[firstname]{/b}."
    show mia 7
    show player 21
    player_name "Пока, {b}Мия{/b}."
    hide player
    hide xtra 21
    hide mia
    with dissolve
    return

label mias_entrance_helen_route_split:
    scene mia_indoors with fade
    show mia 45f at right
    show player 10 at left
    with dissolve
    player_name "{b}Мия{/b}?!"
    show player 5
    show mia 46f
    mia "{b}[firstname]{/b}!"
    show mia 45f
    show player 10
    player_name "Что случилось?"
    show player 5
    show mia 46f
    mia "Мои родители расстались навсегда!"
    show mia 45f
    show player 10
    player_name "Мне... очень жаль."
    show player 5
    show mia 46f
    mia "Я чувствую себя виноватой... Я недостаточно старалась."
    mia "Это всё моя вина!"
    show mia 45f
    show player 37 with dissolve
    player_name "..."
    show player 10 with dissolve
    player_name "Нет, {b}Мия{/b}. Это не твоя вина, правда..."
    player_name "Иногда... люди просто не могут быть вместе."
    show player 11
    show mia 47f with dissolve
    mia "Отношения отстой! Не существует никакой любви."
    show mia 48f
    show player 22
    player_name "!!!"
    show player 24
    show mia 45f with dissolve
    mia "..."
    show mia 46f
    mia "Спасибо, что помогал моей семье..."
    show player 25
    mia "Мне нужно побыть одной..."
    hide mia with dissolve
    show player 24
    player_name "Дерьмо..."
    player_name "{b}Мия{/b} переживает это сильнее, чем я думал."
    show player 37 with dissolve
    player_name "Теперь она только и будет винить себя..."
    show player 24 with dissolve
    pause
    show helen 23 at right with dissolve
    show player 11
    player_name "!!!"
    show player 10
    player_name "{b}Хелен{/b}... Здрасьте..."
    show player 5
    show helen 24
    helen "Здравствуй, {b}[firstname]{/b}."
    helen "Я ценю твоё беспокойство за мою дочь."
    helen "Но не нужно волноваться за {b}Мию{/b}, Я обо всём позабочусь."
    show helen 23
    show player 10
    player_name "Ох..."
    show player 5
    show helen 24
    helen "Можешь и дальше приходить к нам домой."
    helen "Ты нужен здесь."
    helen "В моей комнате хватит места для двоих..."
    show helen 23
    show player 21
    player_name "Хехе... Я... Я думал, что все эти ритуалы уже в прошлом."
    show player 5
    show xtra 21 at left
    show helen 24
    helen "Но, {b}[firstname]{/b}, я твоя верная раба."
    show helen 28
    helen "Ты же знаешь, у меня постоянная борьба с моими желаниям."
    helen "На самом деле, я чувствую себя такой... грешной."
    helen "Мне нужен жесткий... глубокий... очистительный..."
    show helen 23
    show player 10
    player_name "Вы мне предлагаете, то-"
    show player 11
    show helen 24
    helen "Конечно! Вы не хотите... {b}мой Господин{/b}?"
    show helen 23
    show player 22
    player_name "!!!"
    show helen 28
    helen "Если вы не будете заняты, приходите днём чтобы очистить меня от греха..."
    helen "...а ночью вы можете наказать мою грешную плоть в келье монахини."
    show helen 27
    show player 10
    player_name "Я действительно вам нужен?"
    show player 5
    show helen 24
    helen "Конечно!"
    helen "Мою страсть нужно держать в узде..."
    helen "В противном случае, мои грешные руки будут творить... непотребства."
    helen "Пожалуйста, поскорее навестите меня, {b}мой Господин{/b}."
    show helen 23
    show player 11
    player_name "..."
    hide xtra
    hide player
    hide helen
    with dissolve
    return

label mias_entrance_mia_unexpected_visit:
    scene mia_indoors
    show player 10 with dissolve
    player_name "Здрасьте?"
    show player 12
    player_name "( Хмм... Никого нет дома? )"
    player_name "( Может быть она наверху... )"
    hide player with dissolve
    return

label helen_masturbating_block:
    scene mia_indoors
    show player 12 with dissolve
    player_name "( Мне нужно найти {b}Мию{/b} пока я не ушёл... )"
    hide player with dissolve
    $ game.main()

label mias_house_sneak:
    $ player.go_to(L_miahouse_entrance)
    scene black with dissolve
    with Pause(0.5)

    scene mia_sneak01 with dissolve
    show text "Дверь открыта.\n Надеюсь, я не влипну ни в какие неприятности...\n Всё, захожу." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    if not M_mia.is_set("harold left"):
        scene black with dissolve
        with Pause(0.5)

        scene mia_sneak02 with dissolve
        show text "Её родители смотрят телек.\n Мне нужно тихонько прокрасться наверх...\n" at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text with dissolve

    scene black
    with dissolve
    with Pause(0.5)
    if M_mia.is_state(S_mia_urgent_help):
        jump expression game.dialog_select("mias_entrance")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
