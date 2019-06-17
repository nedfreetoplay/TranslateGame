label dexter_fight_pre:
    if game.cheat_mode:
        menu:
            "Пропустить мини-игру(чит).":
                $ renpy.call('dexter_fight_success', 0)
            "Играть в мини-игру.":
                call screen dexter_fight
    call screen dexter_fight

label dexter_fight_minigame_prepare:
    scene school
    show becca 2 at Position (xpos=315)
    show roxxy 32 at Position (xpos=600)
    show missy 2b at left
    with dissolve
    becca "... Его там не было когда вы смотрели?"
    show becca 1
    show roxxy 33
    rox "Нет."
    show roxxy 32
    show becca 3
    show missy 2
    missy "Её {b}мама{/b} сказала что он был там, {b}Бекка{/b}."
    show missy 2b
    show becca 3b
    becca "Да, но... Она была пьяна?"
    show becca 1
    show missy 3
    show roxxy 33
    rox "{b}*Вздыхая*{/b} Эта моя {b}мама{/b}. Конечно, она была пьяна... Она постоянно пьет!"
    show roxxy 33b
    show missy 4d
    with dissolve
    missy "..."
    show becca 2
    becca "Прости, я не хотела этого делать..."
    show becca 1
    show missy 2b
    show roxxy 33
    with dissolve
    rox "Ничего, всё хорошо."
    rox "Я понимаю, о чем ты говоришь."
    rox "Я просто немного волнуюсь."
    rox "Ты лучше всех знаешь, что {b}Декстер{/b} с тех пор, как мы расстались, становится все более агрессивным."
    show roxxy 32
    becca "..."
    show roxxy 33
    rox "Если {b}Декстер{/b} узнает, что я встречаюсь с {b}[firstname]{/b}... Кто знает, что он сделает? "
    show roxxy 32
    show missy 1b
    missy "... Ты встречаешься, {b}[firstname]{/b}?"
    show missy 1
    show roxxy 28
    rox "Я..."
    show roxxy 27
    pause
    show roxxy 1l
    rox "... Я не знаю, хорошо?"
    show roxxy 1k
    show becca 2
    becca "Как ты можешь не знать?"
    show becca 1
    show roxxy 28
    rox "Я имею в виду..."
    show roxxy 27
    pause
    show roxxy 1l
    rox "{b}*Вздыхая*{/b} Слушай, он мне нравится, правда?!"
    rox "Он такой милый и забавный. Он заботится обо мне и моей {b}маме{/b}..."
    show roxxy 1k
    show becca 8
    becca "... А ещё он симпатичный парень."
    show becca 7
    show roxxy 1l
    rox "Да?"
    rox "С каких пор ты считаешь его красивым??"
    show roxxy 1k
    show becca 8
    becca "... После инцедента с {b}Декстером{/b}."
    show becca 7
    rox "..."
    show roxxy 1f
    rox "Хех. Да, он красивый."
    show roxxy 1e
    show becca 3
    show missy 8
    missy "... И у него огромный член!"
    show missy 7
    show roxxy 1i
    rox "!!!"
    show roxxy 1e
    show becca 3b
    becca "Тссс! Люди услышат тебя, тупица!"
    show becca 3
    show missy 2
    missy "Ох, конечно, извини."
    show missy 8
    missy "... Он большой!"
    show missy 7
    show becca 7
    show roxxy 1f
    rox "Да, мы знаем, что он большой!"
    show roxxy 1e
    show becca 2
    becca "Так в чем же проблема?!"
    show becca 1
    show roxxy 2 at Position (xpos=567) with dissolve
    rox "Вы имеете в виду, моего сумасшедшего бывшего пареня?"
    show roxxy 1
    show missy 8
    missy "Тебе точно стоит встречатся с {b}[firstname]{/b}!"
    show missy 7
    show becca 3b
    becca "Я просто сказала!"
    show becca 3
    show missy 2
    missy "Ты сделаешь это?"
    show missy 8
    missy "Ладно, хорошо... Ты должна встречаться с ним и позволить нам играть с ним!"
    show missy 7
    show becca 7
    becca "..."
    show roxxy 2
    rox "Вы блять жадные сучки! Вы знаете это?"
    show roxxy 1
    becca "..."
    show missy 8
    missy "... Но мы твои жадные сучки!"
    show missy 7
    show roxxy 4
    rox "Хех, да я знаю."
    show roxxy 2
    rox "Во-первых мы должны выяснить ситуацию с {b}Декстером{/b}."
    show roxxy 2b
    dex "Вот шлюха!" with hpunch
    show becca 19
    show missy 3
    show roxxy 2bf at Position (xpos=500)
    with dissolve
    rox "!!!"
    show dexter 12d at right with dissolve
    dex "Разве ты не должна отсасывать своему новому парню-неудачнику?!"
    show dexter 12c
    show roxxy 3f
    rox "Прости?"
    show roxxy 3bf
    show dexter 12d
    dex "Ты услышала меня, шлюха!"
    show dexter 12c
    show roxxy 3f
    rox "Не смей со мной так разговаривать!"
    show roxxy 3bf
    show dexter 12d
    dex "Я видел тебя!"
    dex "... Целуешь этого ботана в своем дерьмовом трейлере!"
    show dexter 12c
    show roxxy 2bf
    rox "!!!"
    show roxxy 3cf
    rox "Это не твое дело {b}Декстер{/b}!"
    show roxxy 3f
    rox "Мы расстались, тупица!"
    show roxxy 3bf
    show dexter 12d
    dex "Я не тупица."
    show dexter 14 with dissolve
    show roxxy 3f
    rox "Ну и что? Ты собираешься ударить меня?"
    show roxxy 3bf
    show dexter 15
    dex "Вот именно."
    dex "Я сделаю то, что должен был сделать давным-давно..."
    show dexter 14
    show becca 23 at Position (xpos=340)
    hide missy
    show missy 4b at Position (xpos=220)
    show roxxy 2bf at Position (xpos=80)
    with dissolve
    show dexter 12b with dissolve
    dex "!!!"
    show roxxy 3bf
    show dexter 15 with dissolve
    dex "Убирайтесь с дороги, сучки!"
    show dexter 14
    pause
    show dexter 12d
    dex "Я сказал Съебались нахуй." with hpunch
    show dexter 12c
    show missy 4c with dissolve
    show becca 19
    show erik 53f at Position (xpos=500) with dissolve
    show roxxy 2bf
    show missy 3 with dissolve
    eri "Отойди от девчонок!"
    show erik 50f
    dex "..."
    show dexter 12 with dissolve
    dex "Ты чё там вякнул, недомерок?!"
    show dexter 11
    show erik 3bf
    eri "Я..."
    show erik 5f
    eri "О-отойди от них!"
    show erik 52f
    show roxxy 3cf
    rox "Ты с ума сошёл?!"
    rox "Уходи отсюда!"
    show roxxy 3df
    show erik 5bf
    eri "... Нет!!!"
    eri "Я не могу просто стоять и смотреть, как он причиняет боль девушкам..."
    eri "Особенно девушкам моего лучшего друга!"
    show erik 3bf
    show roxxy 2bf
    rox "!!!"
    becca "..."
    show becca 3
    show missy 2
    missy "Это ещё кто?!"
    show missy 2b
    show becca 3b
    becca "Это друг {b}[firstname]{/b}."
    show becca 3
    show missy 1b
    missy "Оххх..."
    show missy 3
    show becca 19
    show dexter 12
    dex "Ну, и что ты собираешься с этим делать?!"
    dex "Придурок!"
    show dexter 11
    show erik 2f at Position (xoffset=20) with dissolve
    eri "..."
    show erik 3f with dissolve
    eri "{b}*Вздыхая*{/b} Я не могу отступить!"
    eri "{b}[firstname]{/b} не отступит."
    show erik 3bf
    show dexter 12
    dex "Да, ну. {b}[firstname]{/b} здесь нет, толстяк!"
    dex "Остались только мы с тобой."
    show dexter 11
    show erik 4f
    eri "!!!"
    show erik 67f with dissolve
    eri "Я не хотел этого делать, {b}Декстер{/b}..."
    eri "... Но ты не оставляешь мне выбора."
    show erik 68f with dissolve
    eri "Сегодня ты встретишься с {b}Эриком могучим{/b}!"
    eri "Чемпион Орсетте и мастер священных кусочков трески!"
    show erik 69f with dissolve
    eri "Трепещи от страха, кретин, ибо ты сейчас увидишь свою Смерть!"
    show becca 2b with dissolve
    rox "..."
    becca "..."
    show missy 2
    missy "Неужели это он?"
    show missy 3
    show becca 19 with dissolve
    show erik 70f with dissolve
    eri "Именем молота Рактара и светом Шкуревана ты будешь отомщен!"
    pause
    hide dexter
    show erik 71f
    with hpunch
    pause
    hide erik
    show dexter 12 at right with dissolve
    dex "Ахахахаха!"
    show dexter 22
    dex "Хорошая речь, ботан!"
    show dexter 11
    show roxxy 3f
    rox "{b}Декстер{/b}! Какой же ты засранец!"
    show roxxy 3bf
    show dexter 12
    dex "Да, и что?"
    dex "Раньше тебе нравились такие вещи...."
    show dexter 11
    show roxxy 3f
    rox "Ну, я больше этого не делаю!"
    rox "Просто оставьте нас в покое!"
    show roxxy 3bf
    show dexter 15 with dissolve
    dex "Я так не думаю...."
    dex "Никто не смеет бросать меня!"
    dex "Я научу тебя меня уважать-"
    show dexter 14
    show player 15 at Position (xpos=500) with dissolve
    player_name "Отъебись от неё!"
    show player 16
    show roxxy 2bf
    dex "!!!"
    rox "!!!"
    show missy 1b
    missy "{b}[firstname]{/b}!"
    show missy 1
    show becca 2b with dissolve
    becca "{b}*Дыша с трудом*{/b}"
    show dexter 12d with dissolve
    dex "А вот и трус наконец решил показать свое лицо."
    hide player
    show dexter 16 at left
    with dissolve
    pause
    show dexter 17 at right with dissolve
    pause
    show player 10 at Position (xpos=500)
    show dexter 18 at Position (xpos=1175)
    with dissolve
    show player 113
    player_name "Девочки, вы в порядке?"
    show player 114
    show becca 20
    becca "... ммм, да."
    show becca 19
    show missy 8
    missy "Мы сейчас."
    show missy 7
    show roxxy 2cf
    rox "Я не собираюсь!"
    show missy 3
    rox "Какого черта ты делаешь?!"
    rox "Он убьет тебя!"
    show roxxy 2bf
    show player 12
    player_name "Нет, он не..."
    player_name "Не в этот раз."
    hide player
    show dexter 16 at left
    with dissolve
    pause
    show dexter 16b at right with dissolve
    pause
    show dexter 16bf with dissolve
    pause
    show dexter 42
    show player 16 at Position (xpos=500)
    with dissolve
    show roxxy 2cf
    rox "{b}[firstname]{/b}!!!"
    show roxxy 2bf
    show player 15
    player_name "Все в порядке, я разберусь с этим!"
    player_name "Просто хватай {b}Эрика{/b} и убирайся отсюда!"
    show player 16
    show becca 20
    becca "Мы им займёмся."
    hide missy
    hide becca
    with dissolve
    show roxxy 2cf
    rox "Я не собираюсь бросать тебя!"
    show roxxy 2bf
    hide player
    show dexter 16 at left
    pause
    show player 90 at Position (xpos=500)
    show dexter 12d at right
    with dissolve
    dex "Хватит убегать, дерись со мной, говнюк!"
    show dexter 14 with dissolve
    show player 16
    player_name "( Вот оно! Пришло время, чтобы положить вверх над этим ублюдком! )"
    hide player
    hide dexter
    hide roxxy
    with dissolve
    call screen dexter_fight

label dexter_fight_success(dexter_health):
    show screen dexter_fight_win(dexter_health/2)
    pause
    hide screen dexter_fight_win
    scene expression "backgrounds/location_school_cutscene05.jpg"
    with fade
    show text "Чем человек больше...\nТем больнее ему падать!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene school
    show player 24 at left
    show becca 5f at Position (xpos=500)
    show missy 1f at Position (xpos=700)
    show dexter 47 at Position (xpos=950)
    with dissolve
    rox "{b}[firstname]{/b}, у тебя получилось!"
    hide player
    show roxxy 59d at left
    with dissolve
    show becca 6f
    becca "Вот дерьмо!"
    show becca 5f
    show missy 4f
    missy "ПОКОНЧИ С НИМ!"
    show missy 4bf
    show roxxy 59b
    player_name "..."
    show dexter 49 with dissolve
    dex "Тьфу..."
    show dexter 47 with dissolve
    show roxxy 59c
    player_name "... НЕТ."
    player_name "Он этого не заслуживает."
    show roxxy 59b
    show dexter 49 with dissolve
    dex "... Почему я не могу тебя ударить?!"
    show dexter 48
    show roxxy 59c
    player_name "Твои дни издевательства над друзьями закончились {b}Декстер{/b}..."
    player_name "{b}Рокси{/b} больше не твоя девушка!"
    show roxxy 59b
    dex "..."
    show roxxy 59c
    player_name "Ты слышишь меня, засранец?!"
    show roxxy 59b
    show missy 3 at Position (xpos=650)
    show becca 5
    with dissolve
    show dexter 49
    dex "Тссс! Я, блядь, услышал тебя, хорошо?!"
    dex "Но это ещё не конец, {b}[firstname]{/b}!"
    dex "Я не знаю, кто научил тебя всему этому ниндзя-дерьму, но это не последний раз!"
    show dexter 48
    show roxxy 59c
    player_name "Все нормально."
    player_name "Если хочешь чтобы тебе надрали задницу ещё раз, я буду рад помочь."
    player_name "... Но если я еще раз увижу, как ты угрожаешь {b}Рокси{/b} и её друзьям... Ты так просто не отделаешься!"
    show roxxy 59b
    show dexter 47 with dissolve
    dex "Грр!"
    hide dexter with dissolve
    pause
    show roxxy 59d
    show missy 8f at Position (xpos=700)
    show becca 5f
    with dissolve
    missy "Это было так отвратительно!"
    show missy 7f
    show becca 6f
    becca "Это правда."
    show becca 5f
    show roxxy 59e
    player_name "Простите, что опоздал..."
    show roxxy 59d
    rox "..."
    show roxxy 92 at Position (xoffset=0) with dissolve
    pause
    show becca 7f
    show missy 8f
    missy "Охх!"
    show missy 7f
    show becca 8f
    becca "Давай, девочка!"
    show becca 7f
    pause
    show roxxy 59d with dissolve
    rox "Это было чертовски сексуально!"
    show roxxy 59e
    player_name "Хех, да?"
    show roxxy 59d
    rox "ДА!"
    rox "Я хочу сорвать с тебя эту одежду прямо сейчас!"
    show roxxy 59e
    player_name "... Ты что?!"
    show roxxy 59d
    rox "Мммхмхм."
    show missy 8f
    missy "Можно посмотреть?!"
    show missy 7f
    becca "..."
    show roxxy 92 with dissolve
    pause
    smi "Что это за суматоха такая??!"
    show becca 19 at Position (xpos=475)
    show missy 3 at Position (xpos=625)
    show player 11 at left
    show roxxy 2cf at Position (xpos=150)
    with dissolve
    rox "Вот дерьмо!"
    show roxxy 2bf
    show principal 27 at right with dissolve
    smi "Мне напомнить вам, дети, что в этой школе строго запрещено публичное выражение чувств?!"
    show principal 26
    show player 10
    player_name "Не надо, мэм."
    show player 5
    show roxxy 33f
    rox "Простите, {b}Миссис Смит{/b}..."
    show roxxy 32f
    show missy 8
    missy "ОУ, но все становилось только лучше!"
    show missy 7
    show principal 3b at Position (xoffset=70) with dissolve
    smi "!!!"
    show principal 27 with dissolve
    smi "Что за разговоры?!"
    show principal 29
    show missy 3
    missy "!!!"
    show missy 4c at Position (xoffset=13) with dissolve
    missy "Что, нет! Я имею в виду..."
    show missy 4d at Position (xoffset=13)
    show becca 3b
    becca "Хаха, молодец {b}Мисси{/b}..."
    show becca 3
    show missy 4
    missy "Заткнись, {b}Бекка{/b}!"
    show missy 4b
    show becca 19
    show principal 27
    smi "Всё, хватит!"
    show missy 3
    show roxxy 2bf
    smi "Вы обе ко мне в кабинет быстро!"
    show principal 29
    show becca 20
    becca "Вот блин..."
    show becca 19
    show missy 4
    missy "... Чёрт!"
    hide missy
    hide becca
    with dissolve
    show principal 28 at Position (xoffset=70) with dissolve
    smi "Что касается вас двоих, вам лучше пойти в класс, если Вы не хотите присоединиться к ним?!"
    show principal 29 with dissolve
    show roxxy 33f
    rox "Да, мэм."
    show roxxy 32f
    show player 10
    player_name "Пошли!"
    show player 5
    show principal 27
    smi "Хм!"
    hide principal with dissolve
    pause
    show roxxy 1h at center with dissolve
    rox "... Она такая стерва."
    show roxxy 1g
    show player 14
    player_name "Это точно."
    player_name "Но нам лучше пойти на занятия."
    show player 13
    show roxxy 1b
    rox "{b}*Вздыхая*{/b} Да, ты прав."
    show roxxy 1
    pause
    show roxxy 1b
    rox "... Мм, прежде чем ты уйдешь..."
    show roxxy 1
    show player 14
    player_name "Да?"
    show player 13
    show roxxy 1h
    rox "Почему бы тебе не зайти ко мне сегодня вечером?"
    rox "Мы можем продолжить с того, на чем остановились в прошлый раз..."
    show roxxy 1g
    show player 29 with dissolve
    player_name "{b}*Глоток*{/b} Да, хорошо!"
    show player 13 with dissolve
    show roxxy 1h
    rox "Хе-хе, увидимся {b}сегодня{/b} дурачёк."
    show roxxy 1g
    show player 17 with dissolve
    player_name "Обязательно."
    hide player
    hide roxxy with dissolve
    $ M_roxxy.trigger(T_roxxy_ninja_dexter)
    $ game.main()

label dexter_fight_fail(dexter_health):
    show screen dexter_fight_fail(dexter_health/2)
    pause
    hide screen dexter_fight_fail
    scene school
    show roxxy 2bf at left
    show dexter 12d at right
    with dissolve
    dex "Это то, ради чего ты меня бросила?"
    dex "Какая-то занудная маленькая сучка?!"
    show dexter 12c
    show roxxy 2cf
    rox "... {b}[firstname]{/b}! Встань!"
    show roxxy 2bf
    show dexter 15 with dissolve
    dex "Не такой уж он и красивый, правда??"
    show roxxy 2cf
    rox "{b}[firstname]{/b}! Прошу!"
    show roxxy 33bf at Position (xoffset=34)
    show dexter 12
    with dissolve
    dex "Хахахаха!"
    scene black with fade
    pause





    call screen confirm(_('GAME OVER...'),
                        background='menu_condom',
                        no_action=(Hide('confirm'), Jump('dexter_fight_pre')),
                        no_text='Retry',
                        yes_action=ShowMenu('load'),
                        yes_text='Load')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
