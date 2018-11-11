label terry_dialogue_terry_start:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 13 at left with dissolve
    pause
    show player 36
    player_name "Привет."
    show player 13
    show terry 2
    Terry "Посмотрите-ка, кто тут у нас? Пришел чтобы немного у нас порыбачить?"
    show player 29
    show terry 1
    player_name "С чего ты это взял?"
    show player 3
    show terry 2
    Terry "О-хо, я знаю этот взгляд рыбака когда я тебе увидел впервые."
    show player 11
    Terry "Как тебя зовут приятель?"
    show terry 1
    show player 14
    player_name "{b}[firstname]{/b}."
    show player 13
    show terry 2
    Terry "Рад знакомству с тобой, {b}[firstname]{/b}!"
    Terry "{b}Капитан Терри{/b} к твоим услугам!"
    show player 14
    show terry 1
    player_name "Это твой причал?"
    show player 13
    show terry 2 zorder2
    Terry "Это действительно так. А вот это мой магазин. Рыба и текила, две вещи, которые я люблю больше всего на свете!"
    show terry 1

    show sara 4 zorder1 at right with dissolve
    sara "..."
    show sara 5
    sara "Две вещи, которые ты любишь больше всего, мм?"
    show player 11
    show sara 4
    show terry 17b
    Terry "Ээээ... Ну, не больше чем тебя конечно..."
    show terry 18b
    show sara 5
    sara "Ну да."
    show sara 2
    sara "И кто у нас здесь?"
    show player 13
    show sara 1
    player_name "..."
    show terry 2
    Terry "Вот здесь {b}[firstname]{/b}. Он пришел немного порыбачить."
    show terry 1
    show player 29
    player_name "Здравствуйте, Мисс?"
    show terry 15
    Terry "Познакомься с прекрасной {b}Сарой{/b}."
    show player 14
    show terry 1
    player_name "Твоей женой?"
    show player 13
    show terry 16
    Terry "Боже нет, приятель. Моя жена - это море."
    show terry 15
    show sara 4
    Terry "Сара значит для меня намного больше, чем любая жена!"
    show sara 3
    Terry "Она любовь всей моей жизни! Мой первый помощник и деловой партнер."
    show terry 1
    show sara 6
    sara "Хехе, хорошо, молодец. Я прощаю тебя за высказывание о рыбе и текиле."
    show player 13
    show sara 2
    sara "Если я что угодно могу для вас сделать, мальчики, просто дайте знать."
    show sara 1
    show terry 16
    Terry "Сделаем моя любовь, сделаем!"
    show terry 1
    show sara 2
    sara "Рада была познакомиться, {b}[firstname]{/b}!"
    show player 36
    show sara 1
    player_name "Мне тоже {b}Мисс Сара{/b}!"
    hide sara
    with dissolve

    show player 13
    show terry 15
    Terry "О-хо, Я все время ненавижу смотреть, когда она уходит, но я уверен что люблю наблюдать, как она уходит."
    player_name "..."
    show player 2
    show terry 1
    player_name "Итак, где здесь лучшее место для ловли рыбы {b}Капитан Терри{/b}?"
    show player 1
    show terry 2
    Terry "Ну, прямо с причала, конечно!"
    Terry "Просто бросьте веревку вон с того {b}стула{/b} и рыба не заставит себя долго ждать."
    show player 2
    show terry 1
    player_name "Ладно! Есть ещё советы?"
    show player 1
    show terry 4 at Position(xpos=0.71,ypos=0.7047)
    Terry "Хмм..."
    show terry 2 at Position(xpos=0.6992,ypos=0.7047)
    Terry "Обрати пристальное внимание на какую приманку ты ловишь."
    Terry "Не все рыбы ловятся на одну и туже приманку."
    show player 2
    show terry 1
    player_name "Хорошо, понял."
    show player 1
    show terry 2
    Terry "О, и все, что ты поймаешь там. Я куплю это у тебя по хорошей цене."
    show player 2
    show terry 1
    player_name "Ясно, я постараюсь. Что нибудь еще?"
    show player 1
    show terry 2
    Terry "Не заходи в воду!"
    show player 10
    show terry 1
    player_name "Мм? Почему нет?"
    show player 11
    show terry 2
    Terry "Вокруг дока плавают опасные существа."
    show player 10
    show terry 1
    player_name "Реально?"
    show player 11
    show terry 2
    Terry "И не сомневайся. Рыбачить здорово, но вряд ли ты захочешь здесь поплавать!"
    show player 10
    show terry 1
    player_name "О... Хорошо Капитан. Спасибо за все советы."
    show player 11
    show terry 2
    Terry "Ага, Удачи тебе шкипер!"
    hide player with dissolve
    return

label terry_dialogue_terry_nemesis:
    show player 2 at left
    player_name "Эй, {b}Капитан Терри{/b}, Я-"
    show player 10
    player_name "О..."

    show player 11
    show tstand 3 at right with dissolve
    Terry "Я почти поймал его, Сара! Он был у меня *Ик* был у меня в руках вот здесь прямо на пирсе!"
    show tstand 14
    sara "Да, я знаю дорогой..."
    show tstand 3
    Terry "Этот маленький демон сорвался у меня с руки и я упустил его!"
    Terry "Обратно- *Ик* ушел обратно в воду!"
    show tstand 14
    sara "Ну да..."
    show tstand 3
    Terry "Одни брызгииииии! О хохохохо!"
    show player 10
    show tstand 5
    player_name "Эмм... Ты в порядке {b}Капитан Терри{/b}?"
    show player 11
    show tstand 3
    Terry "Шкипер!"
    show tstand 15
    Terry "Ооооо... О-хо... Я *ик* Я в поряяядке."
    Terry "Чувствую себя просто замееечательно."
    show tstand 6
    sara "Приветик {b}[firstname]{/b}."
    show player 36
    show tstand 5
    player_name "Привет, {b}Мисс Сара{/b}."
    show player 10
    player_name "Что случилось с капитаном?"
    show player 11
    show tstand 6
    sara "Ничего такого. У него был просто плохой день и слишком много текилы."
    show tstand 3
    Terry "Ооо неееет... Нет, я *Ик* Я трезв как... *Ик* трезв как церковная мышь."
    show tstand 6
    sara "Я уложу его в кровать."
    show player 10
    show tstand 5
    player_name "О, хорошо."
    show player 11
    show tstand 3
    Terry "Эта *Ик* дьявольская рыба не знает, с кем она связалась, я скаааажу тееебе!"
    show tstand 14
    sara "Ойй, Терри..."
    sara "Ты не можешь продолжать это с собой."
    show tstand 4
    show player 38
    player_name "Дьявольская рыба? О чем это он?"
    show player 11
    show tstand 6
    sara "{b}*Вздох*{/b}"
    sara "Я не думаю, что он хотел бы, чтобы я тебе рассказала."
    show tstand 3
    Terry "О-хо, нет- *Ик* чепуха! Здесь я доверяю Шкиперу."
    show tstand 4
    sara "..."
    show tstand 14
    sara "Ты уверен?"
    show tstand 3
    Terry "Агааа."
    show tstand 6
    sara "Ты видишь, Терри здесь..."
    sara "... Он охотился за этой особенной рыбой в течение многих лет."
    show tstand 15
    Terry "Тигруля! Будь проклята его чешуйчатая шкура!"
    show player 10
    show tstand 5
    player_name "Это странное название для рыбы."
    show player 11
    show tstand 15
    Terry "Он не рыба! Он дьявол который насрал в океане, чтобы замучить меня, я говорю тебе."
    show tstand 5
    player_name "..."
    show player 10
    player_name "Зачем Терри он так сильно нужен?"
    show player 11
    show tstand 6
    sara "Видишь ли, несколько лет назад, Тигруля вроде как... напал на Терри."
    show tstand 5
    show player 12
    player_name "Напал на него?!"
    show player 11
    show tstand 3
    Terry "Забрал у меня- *Ик* Забрал мою маленькую хрюшку."
    show player 10
    show tstand 5
    player_name "Маленькую хрюшку?"
    show player 11
    show tstand 15
    Terry "Ты знаешь... Тот который прошел мало по малу всю дорогу домой?"
    show player 3
    show tstand 5
    player_name "..."
    show tstand 6
    sara "... Его палец."
    show player 29
    show tstand 5
    player_name "Ооооооо!"
    show player 30
    player_name "Отвратительно."
    show player 2
    player_name "Так вот почему ты предупредил меня не плавать вокруг причала."
    show player 1
    show tstand 15
    Terry "Вот именно!"
    show player 2
    show tstand 5
    player_name "Я могу помочь?"
    show player 1
    show tstand 3
    Terry "О нет, парень. Тигруля это моё проклятье. Я не могу натравить его на кого-то другого!"
    show tstand 6
    sara "Я правда думаю, что будет лучше, если я уложу его в постель."
    sara "{b}[firstname]{/b}, почему бы тебе не вернуться в другой раз?"
    show player 10
    show tstand 5
    player_name "О, хорошо {b}Мисс Сара{/b}."
    show player 11
    show tstand 14
    sara "Давай ка Терри..."
    show tstand 3
    Terry "Все что ты скажешь, моя- *Ик* моя любовь!"

    show tstand 3f at Position(xpos=1.05,ypos=1.0):
    Terry "♪Оооо, лучше долго жить и умереть...♪"
    show tstand 3f at Position(xpos=1.25,ypos=1.0):
    Terry "♪Под отважным черным флагом я летаю...♪"
    hide tstand with dissolve

    show player 10
    player_name "Я сочувствую капитану... я хотел бы помочь ему."
    hide player with dissolve
    return

label terry_dialogue_terry_retire:
    show tstand 11 at right with dissolve
    Terry "Я говрю тебе, любимая. Что дни этой рыбы уже сочтены!"
    Terry "Я положу ету проклятую шкуру в магазине, чтобы все могли её увидеть!"
    show tstand 16
    sara "О Терри, я не понимаю, как компас собирается это сделать..."
    show tstand 10
    show player 36 at left with dissolve
    player_name "Привет Капитан!"
    show tstand 12
    pause
    player_name "Привет, {b}Мисс Сара{/b}."
    show player 1
    show tstand 13
    sara "Ну привет, {b}[firstname]{/b}. Пришел выпить?"
    show tstand 11
    Terry "Ага, хороший стаканчик текилы, прежде чем отправиться на рыбалку!"
    show player 29
    show tstand 17
    player_name "О, нет спасибо..."
    player_name "Вообще-то, я пришел, чтобы отдать тебе кое-что, Капитан."
    show player 3
    show tstand 17
    Terry "О-хо, ты слишком добр, Шкипер. Что ты припас для меня на этот раз?"
    show player 2
    player_name "Чтож..."
    show player 239_240
    pause
    show player 465 with hpunch
    show tstand 18
    player_name "Это!"
    show player 464

    Terry "Господи Иисусе!"
    show tstand 2 zorder 1 at Position(xpos=.9,ypos=1.0)
    show sara 4 zorder 2 at Position(xpos=.8325,ypos=1.0) with dissolve
    Terry "Это он!"
    Terry "Шкипер поймал старого Тигрулю!"
    show player 465
    show tstand 1
    player_name "Я сделал!"
    show player 464
    show sara 2
    sara "Вау, Это одна из уродливых рыб..."
    show sara 1
    show tstand 2
    Terry "Я говорил тебе! Эта рыба прямо из ада!"
    Terry "Дай мне посмотреть на неё."

    show player 1
    show tstand 7
    Terry "Я не могу в это поверить."
    show tstand 9
    Terry "..."
    show tstand 8
    Terry "Я НЕ МОГУ поверить в это!"
    Terry "Ты видишь Сара! Я говорил тебе, что компас добьется цели!!"
    show tstand 9
    show sara 5
    sara "Терри, компас этого не делал. {b}[firstname]{/b} это сделал!"
    show tstand 8
    show sara 4
    Terry "Ага, он сделал. Потому что у меня был компас! Разве ты не видишь!?"
    Terry "Я должен положить его внутрь. Скоро вернусь!"
    show tstand 9
    hide tstand with dissolve

    show sara 2
    sara "Наконец-то это закончилось."
    sara "Его одержимость наконец-то подошла к концу!"
    sara "Ты понятия не имеешь, как много это для меня значит, {b}[firstname]{/b}."
    sara "Я боюсь, что я никогда не смогу отплатить тебе!"
    show player 2
    show sara 1
    player_name "О, все нормально, Мисс Сара."
    player_name "Я просто хотел помочь {b}Капитану Терри{/b}."
    show player 1
    sara "..."
    show sara 2
    sara "Ты хороший парень."
    sara "Я..."
    show sara 1

    show tstand 2 at Position(xpos=.725,ypos=1.0)
    show sara 3
    Terry "Ты знаешь что это значит?!"
    show tstand 1
    player_name "..."
    show sara 6
    sara "Что мы наконец-то можем поговорить о твоей отставке?"
    show tstand 2
    show sara 3
    Terry "Что?! ...О, конечно, Конееечно! Мы сразу перейдем к этому вопросу."
    Terry "После того, как я накупаюсь, после этого длительного времени!"
    hide tstand with dissolve
    show sara 4f
    Terry "Хахахахахаха!"
    show sara 5f

    sara "Подожди секундочку!"
    show sara 4f
    pause
    show sara 5f
    sara "Терри!!!"
    show player 23
    sara "О боже мой, Не снимай их!"
    sara "Терри, там люди смотрят!"
    show player 11
    show sara 4f
    pause
    show sara 5f
    sara "Агх"
    hide sara with dissolve

    show player 13
    player_name "..."

    scene location_pier_running
    with fade
    show text "{b}Капитан Терри{/b} многие годы избегал этой воды..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Но Тигруля, наконец, исчез, похоже он не мог дождаться чтобы окунуться." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я не мог сдержать улыбку, смотря, как он радостно прыгает в воду." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Гордость которую я почувстовал, когда вернул ему этот момент..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Это то что я никогда не забуду." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label terry_dialogue_terry_tigger_sign:
    scene location_pier_cutscene
    with fade
    show text "Мое первое возвращение в капитанскую лачугу заставило его тяжело работать." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Казалось что {b}Капитан Терри{/b} потратил немного времени на то, чтобы нафаршировать и установить Тигрулю." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Сдержал свое слово, он повесил свой трофей на всеобщее обозрение." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_pier_closeup_day
    show tstand 1f with dissolve
    show tstand 2f
    Terry "Хаха! Держу пари, сейчас мой палец не так хорош на вкус, да, большой уродливый ублюдок?!"
    show tstand 1f
    show player 13 at left with dissolve
    player_name "..."
    show player 14
    player_name "Мне нравится новое настенное украшение, Капитан."
    show player 13
    show tstand 2 at right
    Terry "Ага, разве это адская штука, Шкипер?"
    Terry "Спасибо еще раз, что поймал это зло."
    show tstand 1
    show player 14
    player_name "Я просто счастлив, что смог помочь."
    show tstand 2
    show player 13
    Terry "Чтож... Ты хороший парень."
    Terry "Дай мне знать если что-нибудь я и мой магазин сможем сделать для тебя."
    show tstand 1
    show player 14
    player_name "Хорошо, Капитан. Я обещаю!"
    show tstand 2
    show player 13
    Terry "Все что угодно! Ты слышишь меня?"
    show tstand 1
    show player 14
    player_name "Я слышу тебя."
    show player 13
    pause
    show player 12
    player_name "Итак, где сегодня {b}Мисс Сара{/b}?"
    show tstand 2
    show player 11
    Terry "Ахх, она планирует наш отпуск."
    show tstand 1
    show player 10
    player_name "Отпуск, ммм?"
    player_name "Куда вы едите?"
    show tstand 2
    show player 11
    Terry "Куда угодно, куда леди скажет... Хах!"
    show tstand 1
    show player 14
    player_name "Хаха! Ну, я счастлив за вас, ребята."
    player_name "Когда вы уезжаете?"
    show tstand 2
    show player 13
    Terry "Ну, Держу пари, ещё не скоро, Шкипер."
    Terry "Маленькая леди сейчас просто перевозбуждена в прямо сейчас."
    Terry "Что со мной, наконец, повесил шляпу и все."
    show tstand 1
    show player 14
    player_name "О, Хорошо!"
    show tstand 2
    show player 13
    Terry "Кстати говоря о моем выходе на пенсию; я хочу чтобы ты знал..."
    Terry "Я все равно куплю любую рыбу, которую ты поймаешь у моего причала, Шкипер."
    show tstand 1
    show player 10
    player_name "... Но я думал, что ты больше не будешь их продавать?"
    show tstand 2
    show player 11
    Terry "Ну, мне все же разрешено их есть разве нет?"
    show tstand 1
    show player 10
    player_name "О, д-да! Конечно!"
    show tstand 2
    show player 11
    Terry "О-хо... Ты же знаешь что я не могу без моей рыбы и текилы."
    show player 13
    Terry "... И чем свежее рыба, тем лучше!"
    show tstand 1
    show player 14
    player_name "Ладно, Я буду иметь это в виду Капитан."
    show tstand 2
    show player 13
    Terry "Хорошо парень!"
    Terry "Чтож, я думаю я лучше пойду."
    show tstand 1
    pause
    show tstand 2
    Terry "Сейчас запомни, если что понадобится, я твой человек!"
    show tstand 1
    show player 14
    player_name "Хорошо, Капитан! Ещё увидимся!"
    show player 13
    hide tstand with dissolve
    show player 4
    player_name "( Хмм, Бьюсь об заклад, Аква позволила бы мне поймать несколько рыб здесь и там. )"
    player_name "( Теперь, когда Терри на пенсии. )"
    return

label terry_dialogue_intro:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 36 at left with dissolve
    player_name "Привет Капитан!"
    show player 203
    show terry 2
    Terry "Ну привет, Шкипер!"
    Terry "Что я могу для тебя сделать?"
    return

label terry_dialogue_buy_fish:
    show terry 1
    show player 4
    pause
    show player 12
    player_name "У тебя есть свежая рыба на продажу?"
    show player 203
    show terry 2
    Terry "Конечно! Ты пришел в нужное место."
    Terry "У меня есть {b}Морская форель{/b}, {b}Морской окунь{/b} и {b}Скумбрия{/b}."
    Terry "Что выберешь?"
    return

label terry_dialogue_buy_fish_buy:
    if not player.has_money(100):
        call expression game.dialog_select("terry_dialogue_buy_fish_buy_no_money")
        call expression game.dialog_select("terry_dialogue_buy_fish_nevermind")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_pre")

    if fish == "Seatrout":
        show terry 5
        $ player.get_item("seatrout")

    elif fish == "Snapper":
        show terry 6
        $ player.get_item("snapper")

    elif fish == "Mackerel":
        show terry 7
        $ player.get_item("mackerel")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_after")
    $ player.spend_money(100)
    return

label terry_dialogue_buy_fish_buy_no_money:
    player_name "( У меня не хватает денег... )"
    return

label terry_dialogue_buy_fish_buy_pre:
    show player 4
    pause
    show player 2
    player_name "{b}[fish]{/b}."
    Terry "Это отличный выбор!"
    show terry 4
    Terry "Давай я достану её для тебя..."
    return

label terry_dialogue_buy_fish_buy_after:
    Terry "Это тебе, дрижише!"
    show player 17
    player_name "Спасибо!"
    return

label terry_dialogue_buy_fish_nevermind:
    show player 10
    show terry 1
    player_name "Хмм... Я думаю, я откажусь."
    show player 203
    show terry 2
    Terry "Без проблем, приятель! Может быть в другой раз."
    return

label terry_dialogue_sell_fish:
    scene expression game.timer.image("pier_closeup{}")
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 4 at left
    pause
    show player 13
    show terry 2
    Terry "Поймал что-нибудь хорошее, Шкипер?"
    show terry 1
    show player 14
    player_name "Вообще-то, да, мне было интересно, не хочешь ли ты их купить."
    show player 13
    show terry 2
    Terry "Конечно, приятель."
    Terry "Что у тебя есть?"
    show terry 1
    return

label terry_dialogue_sell_fish_sell:
    call expression game.dialog_select("terry_dialogue_sell_fish_sell_pre")

    if fish == "Seatrout":
        show terry 5
        $ player.remove_item("seatrout")

    elif fish == "Snapper":
        show terry 6
        $ player.remove_item("snapper")

    elif fish == "Mackerel":
        show terry 7
        $ player.remove_item("mackerel")

    call expression game.dialog_select("terry_dialogue_buy_fish_buy_after")
    $ player.get_money(80)
    return

label terry_dialogue_sell_fish_sell_pre:
    show player 14
    player_name "Вот свежая {b}рыба{/b}."
    show player 13
    show terry 2
    Terry "Отличный улов, парень!"
    show terry 4
    Terry "Дай мне принести твои деньги."
    show terry 1
    return

label terry_dialogue_sell_fish_nevermind:
    show player 10
    show terry 1
    player_name "Хмм... На самом деле, она ускользнула..."
    show player 13
    show terry 2
    Terry "Без проблем дружише! Может быть в другой раз."
    show terry 1
    return

label terry_dialogue_buy_drink_pre:
    show player 12
    show terry 1
    player_name "Ты продаешь выпивку?"
    show player 11
    show terry 3
    pause
    show terry 2
    Terry "Только одного вида: Чистейшую золотую текилы!"
    Terry "$5 стаканчик, дружище."
    return

label terry_dialogue_buy_drink:
    if not player.has_money(5):
        call expression game.dialog_select("terry_dialogue_buy_drink_no_money")
    else:

        call expression game.dialog_select("terry_dialogue_buy_drink_buy")
        $ player.spend_money(5)
    return

label terry_dialogue_buy_drink_no_money:
    player_name "( У меня не хватает денег... )"
    return

label terry_dialogue_buy_drink_buy:
    show player 188
    show terry 1
    pause
    show player 189
    pause
    show player 190
    pause
    show player 191
    player_name "Агх! Это действительно сильно!"
    show player 185
    show terry 2
    Terry "Хаха!"
    Terry "Эта хорошая вешь! Ты привыкнешь к этому!"
    return

label terry_dialogue_buy_drink_pass:
    show terry 1
    show player 10
    player_name "Пожалуй я пас. Я не могу пить эту штуку."
    show terry 2
    show player 203
    Terry "Не проблема, парень! Может быть в следующий раз."
    return

label terry_dialogue_fishing:
    show player 2
    show terry 1
    player_name "Могу ли я попытаться половить здесь рыбу?"
    show player 203
    show terry 3
    pause
    show terry 2
    Terry "Я вижу, открытая вода бросается в глаза."
    show player 31f at Position(xpos=-0.1412,ypos=1.0000) with dissolve
    show terry
    Terry "Просто используй {b}стул{/b} в конце пирса. Это отличное место!"
    show player 203 at left with dissolve
    Terry "Убедись, что у тебя есть {b}Удочка{/b}, и то что ты используешь правильную {b}приманку{/b}."
    show terry 3
    pause
    show terry 2
    Terry "О! Если ты что-нибудь поймаешь, возвращайся сюда, и я куплю их у тебя за разумную цену."
    return

label terry_dialogue_fishing_bait:
    show player 2
    show terry 1
    player_name "Можешь ли вы рассказать мне побольше о типах приманки?"
    show player 203
    show terry 2
    Terry "Понятно дела, помощник!"
    Terry "Первое, тебе нужно знать, какую рыбу ты пытаешся поймать."
    Terry "Каждый {b}вид{/b} рыбы любит определенный тип {b}приманки{/b}!"
    Terry "{b}Морской форели{/b} нравятся черви, {b}морскому окуню{/b} нравятся голубые приманки, и {b}Скумбрии{/b} нравятся зеленые приманки!"
    show player 2
    show terry 1
    player_name "Потрясающе! Спасибо за совет!"
    player_name "Но где я могу найти эти различные типы приманки?"
    show player 203
    show terry 2
    Terry "Я не продаю оборудование в своей хижине."
    Terry "Тебе придется {b}посмотреть в городе{/b} чтобы найти их."
    show player 2
    show terry 1
    player_name "Я посмотрю."
    player_name "Спасибо {b}Терри{/b}!"
    return

label terry_dialogue_secret:
    show player 2 at left
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "Как ты так хорошо ловишь рыбу, Капитан?"
    show terry 2
    show player 203
    Terry "О-хо, годы практики Шкипер."
    show player 2
    show terry 1
    player_name "Это все?"
    show terry 2
    show player 203
    Terry "... Ну..."
    Terry "... А ещё у меня есть секретное оружие!"
    show terry 1
    show player 14
    player_name "Реально?! Что это?"
    show terry 15
    show player 203
    Terry "Хах, нельзя ждать что мастер рыбак раскрое все свои секреты!"
    show terry 1
    show player 2
    player_name "Ой, да ладно Капитан. Ты можешь рассказать мне!"
    show terry 2
    show player 203
    Terry "Хмм..."
    show terry 16
    Terry "Ахаха, ну разве ты не настойчив? Мне это нравится!"
    show terry 15
    Terry "Хороший рыбак нуждается в упорстве!"
    show terry 2
    Terry "Хорошо Шкипер, иди сюда и я покажу тебе свою секретную приманку."
    show terry 9 at Position(xpos=0.671,ypos=0.7047)
    show player 14
    player_name "Секретную приманку? Ловко!"
    player_name "Что именно она делает?"
    show terry 10
    show player 203
    Terry "Ох-хо, эта малышка ловит все!"
    Terry "Рыба просто не может устоять!"
    show terry 9
    show player 14
    player_name "Вау!"
    player_name "Не хочешь мне её продать?"
    show terry 11
    show player 203
    Terry "Хаха, продать её тебе?! Парень, она бесценна!"
    show terry 13
    show player 24
    player_name "О, я вижу..."
    show terry 11
    Terry "Хмм... Ну не расстраивайся ты так."
    show terry 10
    Terry "Я тебе скажу вот что. Если ты найдешь мне что-то столь же бесценное, то я обменяюсь с тобой."
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 12
    player_name "Ну, что же ты имеешь в виду?"
    show terry 2
    show player 11
    Terry "Как насчет {b}Золотого Компаса{/b}?"
    show terry 1
    show player 12
    player_name "Что это такое?"
    show terry 2
    show player 11
    Terry "Старая рыбацкая сказка."
    Terry "Много лет назад, в этих краях жил великий строитель кораблей."
    Terry "Говорили, что он обладал {b}Золотым Компасом{/b} и что он может привести тебя к твоему желанию сердца."
    show terry 1
    show player 12
    player_name "По-моему это выдумки!"
    show terry 15
    show player 11
    Terry "Хо хо, ага, так и есть приятель."
    show terry 2
    Terry "Но если бы такая штука существала..."
    Terry "Я думаю, что она бы того стоила чтобы обменять на мою приманку."
    Terry "Что скажешь?"
    show terry 1
    show player 14
    player_name "Хмм... Я думаю я мог бы этим заняться."
    show terry 2
    show player 13
    Terry "Это отлично!"
    show terry 1
    show player 14
    player_name "С чего бы ты посоветовал начать?"
    show terry 2
    show player 13
    Terry "Я бы начал искать с судостроителя."
    Terry "Если бы он действительно существовал, я думаю, он был бы похоронен где-то на городском кладбище."
    show terry 1
    show player 14
    player_name "Звучит неплохо, как его звали?"
    show terry 16
    show player 13
    Terry "О-хо, я не имею ни малейшего понятия."
    show terry 1
    show player 10
    player_name "Ах, блин."
    show terry 2
    show player 11
    Terry "Может быть, тебе стоит поспрашивать в городе. Некоторые из {b}старых жителей{/b} могут что то об этом знать."
    show terry 1
    show player 10
    player_name "Хорошо, я думаю, мне лучше начать."
    show terry 2
    show player 13
    Terry "Всего самого хорошего тебе, Шкипер!"
    show terry 1
    show player 14
    player_name "Спасибо Капитан."
    return

label terry_dialogue_lure:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 14 at left
    player_name "Ещё раз, что ты хотел взамен на приманку?"
    show terry 2
    show player 13
    Terry "Боюсь, ничего, кроме {b}Золотого компаса{/b} не поможет, Шкипер."
    show terry 1
    show player 14
    player_name "О, да, точно! Где я должен начать искать?"
    show terry 2
    show player 13
    Terry "На твоем месте я бы поспрашивал в городе."
    Terry "Посмотрим, знает ли кто-нибудь из {b}пожилых жильцов{/b} что-нибудь о парне, который им владел."
    Terry "Говорят, он был великим строителем кораблей."
    show terry 1
    show player 14
    player_name "Хорошо, Спасибо капитан."
    return

label terry_dialogue_golden_compass:
    show player 2 at left
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "Приманка ещё у вас, капитан?"
    show player 1
    show terry 15
    Terry "Еще бы! Никогда не спускаю с нее глаз."
    show player 2
    show terry 1
    player_name "Хорошо, потому что угадай, что я тебе принес?"

    show terry 19
    show player 239_240
    pause
    show player 466
    show terry 17
    Terry "Не может быть..."
    show player 467
    show terry 19
    player_name "Я нашел его! Я нашел Золотой компас!"
    show player 466
    show terry 17
    Terry "Ты шутишь!"
    show player 467
    show terry 19
    player_name "Вот, взгляни на это!"

    show player 1
    show terry 21 at Position(xpos=0.654,ypos=0.712)
    pause
    show terry 22
    Terry "Сделано черносердечно на задней стороне!"
    Terry "Эта Проклятая вещь действительно существует!"
    show player 10
    show terry 21
    player_name "..."
    player_name "Ты действительно не веришь в это?"
    show player 5
    show terry 22
    Terry "Господи нет, парень. Я никогда не собирался расставаться с приманкой..."
    Terry "Она мне нужна, чтобы поймать Тигра, а моя приманка - единственная, на которую он клюет."
    Terry "Ну, не считая моего пропавшего поросенка, конечно."
    show player 24
    show terry 21
    player_name "Ох, Понятно."

    show terry 4 at Position(xpos=0.71,ypos=0.7047)
    pause
    show terry 10 at Position(xpos=0.671,ypos=0.7047)
    Terry "Думаю, теперь это принадлежит тебе!"

    show player 470
    show terry 2 at Position(xpos=0.6992,ypos=0.7047)
    pause
    show player 471
    player_name "Что? Но ты только что сказал-"
    show player 470
    show terry 15
    Terry "Ну, мне она не нужна сейчас, не так ли, Шкипер?!"
    show terry 16
    Terry "У меня есть Золотой Компасс."
    show terry 15
    show player 13
    Terry "Золотой компас, который приведет меня к желанию моего сердца."
    Terry "И так как мое сердце желает голову этого маленького ублюдка..."
    Terry "Ну, я бы сказал, что это справедливая сделка, не так ли?"

    show player 14
    show terry 1
    player_name "Да!"
    show player 13
    show terry 2
    Terry "Теперь будь осторожен, используя эту приманку!"
    Terry "Иногда попадаются... {b}Неожиданные вещи{/b}."
    show player 14
    show terry 1
    player_name "Я буду осторожен, капитан."
    show player 13
    show terry 22 at Position(xpos=0.654,ypos=0.712)
    Terry "Молодец. Теперь, позвольте мне взглянуть на эту красоту!"
    show terry 21
    show player 34f
    player_name "( Хмм... {b}Неожиданные вещи?{/b} )"
    player_name "( Интересно, что это значит? )"
    show popup_lure at truecenter with dissolve
    pause
    hide popup_lure with dissolve
    return

label terry_dialogue_retire:
    show player 2 at left
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    player_name "Эй, капитан. У меня есть вопрос."
    show player 1
    show terry 2
    Terry "Да? Что я могу сделать для тебя, Шкипер?"
    show player 2
    show terry 1
    player_name "Ты когда-нибудь думал уйти из рыболовного бизнеса?"
    show player 1
    show terry 19
    Terry "Хмм..."
    show terry 20
    Terry "Если сказать по правде. Я думаю об этом уже несколько лет."
    show player 2
    show terry 1
    player_name "Правда?"
    show player 1
    show terry 17
    Terry "Не пойми меня неправильно, парень. Мне нравится рыбачить!"
    show terry 20
    Terry "Ничто не сравнится с... днём на море, удочкой в воде, ветерком в моей бороде..."
    show terry 15
    Terry "... Ничего, кроме моей Сары."
    show player 2
    show terry 1
    player_name "Вы действительно любите её, Да, капитан?"
    show player 1
    show terry 15
    Terry "Да, парень, люблю."
    show terry 17
    Terry "И она хотела, чтобы я ушел на пенсию, сколько я себя помню."
    show terry 20
    Terry "Говорит, что хочет немного попутешествовать, повидать мир."
    show terry 17
    Terry "По правде говоря, я думаю, что она просто хочет, чтобы я был рядом с ней почаще."
    show player 2
    show terry 1
    player_name "Так почему бы тебе не сделать это?"
    show player 1
    show terry 17
    Terry "Я не могу, Шкипер!"
    Terry "Не тот случай!"
    Terry "Не тогда, когда этот монстр все еще где-то там скрывается!"
    show player 10
    show terry 18
    player_name "Ааа, Тигр?"
    show player 11
    show terry 20
    Terry "*плюется* Дьявольская Рыба!"
    show terry 2
    Terry "Но теперь, когда ты принес мне Золотой компас..."
    Terry "это лишь вопрос времени, когда этот ублюдок встретит свою смерть!"
    show player 10
    show terry 1
    player_name "Хорошо, спасибо, что был честен со мной, Капитан."
    show player 11
    show terry 2
    Terry "Не стоит, Шкипер!"
    show terry 16
    Terry " Ты показал себя настоящим верным другом для меня и мне."
    show player 34
    show terry 1
    player_name "( Бьюсь об заклад, если бы я поймал Тигра, {b}Капитан Терри{/b} бросил бы рыбалку. )"
    player_name "( Я должен попытаться. Аква рассчитывает на меня! )"
    return

label terry_dialogue_fake_id:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    player_name "Эй, {b}Капитан Терри{/b} могу я спросить у вас кое-что?"
    show player 5
    show terry 2
    Terry "Да, что такое Шкипер?"
    show terry 1
    show player 10
    player_name "Недавно до меня дошли слухи..."
    player_name "Ты знаешь что-нибудь о подделке документов?"
    show player 5
    show terry 17b
    Terry "О-хо! Где ты слышал такие слухи?!"
    show terry 18
    show player 29 with dissolve
    player_name "Хе, Я эээ..."
    show player 10 with dissolve
    player_name "Ну, друг упомянул об этом."
    show player 5
    show terry 17
    Terry "Хмм, Ясно..."
    Terry "Хорошо, если бы я сделал парень... Было бы не слишком умно для меня болтать об этом, не так ли?"
    show terry 18
    show player 10
    player_name "Да, я полагаю, что нет."
    show player 5
    show terry 15
    Terry "Зачем такому хорошему мальчику, как ты, фальшивые документы?"
    Terry "Я более чем счастлив если дам тебе выпить раз или два из бара..."
    show terry 3 with dissolve
    show player 10
    player_name "Это не для меня, {b}Капитан{/b}..."
    show terry 1 with dissolve
    player_name "Для... Девушки."
    show player 5
    show terry 2
    Terry "О! Нашел себе симпатичную, да?"
    show terry 1
    show player 29 with dissolve
    player_name "Д-Да..."
    show player 3
    show terry 15
    Terry "Ну, не слова больше!"
    show terry 16
    Terry "Если фальшивое удостоверение-это то, что нужно, тогда фальшивое удостоверение я предоставлю!"
    show terry 1
    show player 14 with dissolve
    player_name "Правда?"
    show player 13
    show terry 15
    Terry "Да!"
    Terry "Просто принеси мне актуальное фото и 400 долларов."
    Terry "Я позабочусь об остальном!"
    show terry 1
    show player 17
    player_name "Спасибо, {b}Капитан{/b}!"
    show player 13
    show terry 16
    Terry "С удовольствием, Шкипер!"
    show terry 3 with dissolve
    player_name "( Я должен {b}пойти и рассказать Рокси{/b} хорошие новости! )"
    return

label terry_dialogue_fake_id_picture_first:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 14 at left
    player_name "Итак, что насчет {b}поддельных документов{/b}..."
    show player 13
    show terry 15
    Terry "О, ты принес фото?"
    show terry 1
    show player 14
    player_name "Ага, оно у меня."
    show player 239_240 with dissolve
    pause
    show player 646 with dissolve
    player_name "Вот!"
    show player 13
    show terry 9b
    with dissolve
    Terry "Боже милостивый, ты не шутил, Шкипер!"
    Terry "Она просто красавица!"
    show terry 13b
    show player 14
    player_name "Ну, да."
    show player 13
    show terry 10b
    Terry "Ну, не волнуйся, парень."
    Terry "Я сделаю это в мгновение ока!"
    Terry "... У тебя есть 400 баксов, а?"
    show terry 1
    return

label terry_dialogue_fake_id_picture_repeat:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    player_name "Я надеялся, что ты можешь сделать это {b}фальшивое удостоверение{/b} для меня сейчас?"
    show player 5
    show terry 2
    Terry "Конечно могу, Шкипер."
    Terry "У тебя есть 400 долларов?"
    show terry 1
    return

label terry_dialogue_fake_id_yes:
    show player 14
    player_name "Конечно."
    player_name "Я должен позвонить девочкам и сказать, где их забрать."
    show player 13
    show terry 15
    Terry "Звучит как план, Шкипер."
    show terry 1
    show player 14
    player_name "Я сейчас вернусь."
    scene black with fade
    scene expression game.timer.image("pier_closeup{}")
    show terry 2 at Position(xpos=0.6992,ypos=0.7047)
    show player 13 at left
    with dissolve
    Terry "Ещё несколько минут, Шкипер."
    show terry 1
    show player 14
    player_name "Потрясающе! Большое спасибо, {b}Капитан Терри{/b}."
    show player 13
    show terry 15
    Terry "О, хо-хо, мне в удовольствие, парень."
    show terry 1
    rox "Вот ты где! Наконец-то!"
    show roxxy 1bf at Position (xpos=500)
    show becca 1 at Position(xpos=315)
    show missy 1 at left
    show player 13f at right
    with dissolve
    rox "Это место было нелегко найти!"
    show roxxy 1f f
    show missy 2
    missy "Что это за запах такой?"
    show missy 2b
    show terry 18
    show player 10f
    player_name "... Рыба?"
    show player 5f
    show becca 2b with dissolve
    becca "Фу, отвратительно!"
    show becca 1 with dissolve
    Terry "..."
    show terry 17
    Terry "Отвратительно?!"
    Terry "Знаешь, девушка, так я зарабатываю на жизнь..."
    show terry 18
    show becca 2
    becca "Грубый."
    show becca 1
    Terry "..."
    show terry 17
    Terry "Никогда не думал, что ты любишь чопорных снобов, Шкипер."
    show terry 18
    show player 10f
    player_name "... На самом деле это не так."
    show player 5f
    show becca 8
    becca "Пффф, не волнуйся, ботан! У тебя все равно нет шансов!"
    show becca 1
    show missy 6
    missy "Хаха!"
    show missy 1
    show roxxy 28f at Position (xoffset=33) with dissolve
    rox "{b}*вздыхает*{/b}"
    show roxxy 1bf with dissolve
    rox "... Так ты делаешь {b}фальшивые документы{/b}, а?"
    show roxxy 1f f
    show terry 17
    Terry "Да."
    Terry "... Но не распространяйся об этом, слышите?"
    show terry 17b
    Terry "Это не совсем справедливо."
    show terry 18
    show roxxy 4f
    rox "Ну, я думаю, что это довольно круто!"
    show roxxy 1bf
    rox "Как ты познакомился с этим парнем, {b}[firstname]{/b}?"
    show roxxy 1f f
    show terry 15
    Terry "О-хо! Мы со шкипером не разлей вода!"
    Terry "Он неплохой маленький рыбак!"
    show terry 1
    show roxxy 2f
    rox "Ты тоже рыбачишь?"
    show roxxy 1f f
    show player 14f
    player_name " Да, время от времени."
    show player 13f
    show roxxy 2f
    rox "Ого, рыба меня пугает."
    rox "Разве они не похожи... ну, слизкие?"
    show roxxy 1f f
    show player 10f
    player_name "Эх, да... Иногда, я полагаю."
    show player 5f
    show missy 1b
    missy "Потрясающе!"
    show missy 1
    show becca 2b with dissolve
    becca "Фу, нет!"
    show becca 1 with dissolve
    show terry 18
    show missy 2
    missy "А, точно. Я имела в виду..."
    show missy 3
    show roxxy 3cf
    rox "Не могли бы вы обе заткнуться?!"
    show roxxy 3df
    show missy 2b
    Terry "..."
    show roxxy 1f f
    show terry 15
    Terry "Ну, похоже это {b}поддельное удостоверение{/b} получилось неплохо."
    show terry 1
    show roxxy 1bf
    rox "Потрясающе!"
    show roxxy 4f
    rox "Наконец, мне не придется полагаться на {b}Декстера{/b} при покупке выпивки!"
    rox "Не могу дождаться этих выходных!"
    show roxxy 1f f
    show player 14f
    player_name "Да, это звучит очень прикольно!"
    show player 13f
    show becca 2
    becca "Жаль, что тебя не пригласили, неудачник!"
    show becca 3
    show player 5f
    show missy 2
    missy "... Нет?"
    show missy 2b
    show becca 3b
    becca "Никогда!"
    show becca 1
    show player 24f
    player_name "..."
    show roxxy 2f
    rox "Прости {b}[firstname]{/b}."
    rox "Мне нужно поддерживать репутацию..."
    show roxxy 1f f
    show terry 17
    Terry "Теперь подождите минутку!"
    Terry "Шкипер только что потратил на вас 400 долларов, а вы даже не пригласили его на вечеринку..."
    Terry "Это реально дерьмовый поступок."
    show terry 18
    show becca 3
    show missy 1b
    missy "Я думаю, он может прийти..."
    show missy 1
    show becca 3b
    becca "Заткнись, {b}Мисси{/b}!"
    becca "Все увидят его с нами!"
    show becca 1
    show roxxy 2f
    rox "Да, мы не можем показываться с ним вместе."
    show roxxy 1f f
    show terry 17
    Terry "Ну, я думаю, что, возможно, я не отдаю вам это {b}поддельное удостоверение личности{/b} в конце концов..."
    show terry 18
    show player 5f
    show roxxy 2bf
    rox "..."
    show terry 17
    Terry "Это правильно."
    Terry "400 баксов - большие деньги для парня его возраста."
    Terry "Девочки, вам придется скомпенсировать его траты."
    show terry 18
    show roxxy 3cf
    rox "Ты это серьезно, старик?!"
    show roxxy 3f
    rox "У нас нет денег!"
    show roxxy 3bf
    show terry 15
    Terry "Ну, может тогда тебе стоит дать ему что-нибудь другое?"
    show terry 1
    show roxxy 3df
    rox "..."
    show roxxy 3cf
    rox "Что например?"
    show roxxy 3df
    show terry 15
    Terry "Как насчет того, чтобы твои подружки дали нам взглянуть на эти вкусные титяндры?"
    show terry 1
    show player 13f
    show roxxy 2bf
    show becca 2
    becca "ЧТО?!"
    becca "Ни за что, твою мать!"
    show becca 3
    show missy 1b
    missy "Я сделаю это!"
    show roxxy 1f f
    show missy 1
    show becca 3b
    becca "Тьфу, конечно ты..."
    becca "Ты потаскушка."
    show becca 3
    show missy 2
    missy "Эй, я не такая!"
    show missy 2b
    show roxxy 2f
    rox "Меня устраивает."
    show roxxy 1f f
    show becca 2
    becca "{b}Рокси{/b}! Да ладно, я не буду показывать им свои сиськи!"
    show becca 1
    show roxxy 2f
    rox "Заткнись и делай, {b}Бекка{/b}."
    rox "Вокруг никого нет."
    show roxxy 1f f
    show becca 3b
    becca "Да, но..."
    show becca 1
    show roxxy 3 at Position (xpos=550) with dissolve
    rox "Ты хочешь выпить или нет?!"
    show roxxy 3d
    show becca 3
    show missy 1b
    missy "Я!"
    show missy 9 with dissolve
    show roxxy 1
    pause
    show missy 10 with dissolve
    pause
    show roxxy 1f f at Position (xpos=500) with dissolve
    show terry 15
    Terry "Ох хо-хо!"
    show terry 1
    show missy 11
    show terry 15
    Terry "А вот эти хорошие задорные, не правда ли, Шкипер?!"
    show terry 1
    show player 14f
    player_name "... Да!"
    show player 13f
    show missy 10
    missy "Тебе они на самом деле нравятся, {b}[firstname]{/b}?!"
    show missy 11
    show player 17f
    player_name "Хех, определенно!"
    show player 13f
    show missy 11b
    missy "Видишь, {b}Бекка{/b}!"
    show missy 11
    show becca 8
    becca "Тебе правда нравятся эти комариные укусы?!"
    show becca 7
    show player 14f
    player_name "Что тут может не понравиться?"
    show player 13f
    show terry 15
    Terry "Хо-хо, Капитан никогда не встречал пару грудей, которые ему не нравились!"
    show terry 1
    show roxxy 30 at Position (xpos=550) with dissolve
    rox "Давай {b}Бекка{/b}! Все ждут!"
    show roxxy 3d
    show becca 2
    becca "{b}*вздыхая*{/b} Ладно!"
    show becca 9 with dissolve
    show roxxy 1
    pause
    show becca 10
    show terry 15
    Terry "Ох хо-хо, не плохо!"
    show terry 1
    show roxxy 1f f at Position (xpos=500) with dissolve
    show player 14f
    player_name "... Вау!"
    show player 13f
    show becca 11
    becca "Смотри, эти намного лучше чем кеглевидные титьки {b}Мисси{/b}..."
    show becca 11b
    show missy 11b
    missy "Пошла ты {b}Бекка{/b}!"
    missy "По крайней мере, мои не покрыты веснушками!"
    show missy 11c
    show becca 11c
    becca "Пффф, и что!"
    becca "Многим парням нравятся мои веснушки!"
    show becca 11b
    show missy 11b
    missy "Да, точно."
    show missy 11c
    show terry 15
    Terry "Хахаха!"
    Terry "Ну, что скажешь, Шкипер?!"
    Terry "Какая пара тебе нравится больше?"
    show terry 1
    show missy 11
    show becca 10
    return

label terry_dialogue_fake_id_yes_becca:
    show player 14f
    player_name "Хе, Мне нравятся у {b}Бекки{/b}!"
    show player 13f
    show becca 11c
    becca "Видишь, Я знала что {b}[firstname]{/b} согласится!"
    show becca 11b
    show missy 4d with dissolve
    missy "..."
    show becca 9 with dissolve
    pause 1
    show becca 2 with dissolve
    becca "... Даже ботанам нравятся девушки с большими сиськами."
    show becca 3
    show missy 4c
    missy "..."
    show missy 4d
    missy "{b}*фырк*{/b}."
    hide missy with dissolve
    show becca 3b
    becca "Блин, что за маленький ребенок..."
    show becca 2
    becca "Теперь мы можем получить {b}документы{/b}?"
    show becca 1
    show terry 15
    Terry "Что ты думаешь, {b}парень{/b}?"
    show terry 1
    show player 14f
    player_name "Да, они это заслужили."
    show player 13f
    show terry 2
    Terry "Очень хорошо, держи, Фея."
    show terry 1
    show roxxy 3cf
    rox "... {b}Рокси{/b}."
    show roxxy 3df
    show terry 2
    Terry "... Как скажешь."
    Terry "Пошли, Шкипер!"
    Terry "Давайте возьмем бутылку текилы и отправимся на пристань ненадолго!"
    Terry "Я расскажу тебе о том, как я заметил русалку у бухты!"
    show terry 15
    show player 14f
    player_name "Да, хорошо!"
    hide terry
    hide player
    with dissolve
    Terry "... Она была голой, как день, когда она родилась, и красивой, как могла бы быть!"
    Terry "У меня было много текилы в тот день, но я клянусь своей матерью, она была голубая, как море!"
    show becca 2
    becca "Пойдем, {b}Рокси{/b}."
    show roxxy 3d at Position (xpos=550) with dissolve
    becca "Нам лучше пойти и найти маленькую мисс плаксу."
    show becca 1
    show roxxy 30
    rox "... Да."
    hide becca with dissolve

    show roxxy 1kf at Position (xpos=500) with dissolve
    rox "..."
    hide roxxy with dissolve
    return

label terry_dialogue_fake_id_yes_missy:
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show roxxy 1f f at Position (xpos=500)
    show becca 10 at Position(xpos=315)
    show missy 11 at left
    show player 17f at right
    with dissolve
    player_name "Хе, Мне нравятся у {b}Мисси{/b}!"
    show player 13f
    show roxxy 2bf
    show missy 10
    missy "ДААА!!!"
    show missy 7
    show becca 11
    becca "ЧТО?!"
    show becca 9 with dissolve
    pause 1
    show becca 1 with dissolve

    show missy 8
    missy "Ты лучший, {b}[firstname]{/b}!"
    show missy 7
    show becca 3b
    becca "Пфф, не важно..."
    becca "Кого волнует, что думает какой-то ботаник?!"
    hide becca with dissolve
    show roxxy 1bf
    rox "... Не обращайте на нее внимания. Иногда она бывает такой стервой..."
    show roxxy 1f f
    show missy 1b
    missy "Ты слышала! {b}[firstname]{/b} сказал что мои титьки лучше чем у {b}Бекки{/b}!!!"
    show missy 1
    show roxxy 3cf
    rox "{b}*вздыхая*{/b} Конечно, я все слышала! Я ведь не глухая!"
    show roxxy 29f
    show missy 6
    missy "Хехехе!"
    show missy 1
    show roxxy 3cf
    rox "Теперь мы можем получить {b}документы{/b}?"
    show roxxy 3df
    show terry 2
    Terry "Что ты думаешь, {b}парень{/b}?"
    show terry 1
    show player 14f
    player_name "Да, они это заслужили."
    show player 13f
    show roxxy 1f f
    show terry 2
    Terry "Очень хорошо, держи, Фея."
    show terry 1
    show roxxy 3cf
    rox "... {b}Рокси{/b}."
    show roxxy 3df
    show terry 2
    Terry "... Как скажешь."
    show terry 15
    Terry "Пошли, Шкипер!"
    Terry "Давайте возьмем бутылку текилы и отправимся на пристань ненадолго!"
    Terry "Я расскажу тебе о том, как я заметил русалку у бухты!"
    show terry 1
    show player 14f
    player_name "Да, хорошо!"
    show player 13f
    show missy 6
    missy "Пока, {b}[firstname]{/b}!"
    show missy 7
    show player 14f
    player_name "Хе, пока {b}Мисси{/b}."
    hide terry
    hide player
    with dissolve
    Terry "... Она была голой, как день, когда она родилась, и красивой, как могла бы быть!"
    show missy 2
    missy "Ух, {b}Бекка{/b} может быть настоящей королевой драмы!"
    show missy 2b
    show roxxy 30f
    rox "... Да, нам лучше пойти и найти ее."
    hide missy with dissolve

    show roxxy 1kf at Position (xpos=500) with dissolve
    rox "..."
    hide roxxy with dissolve
    return

label terry_dialogue_fake_id_no:
    show player 10
    player_name "О, черт."
    player_name "Я забыл про $400."
    show player 5
    show terry 16
    Terry "Ха! Не волнуйся парень."
    show terry 17
    Terry "Просто приходи ко мне, когда получишь их."
    show terry 1
    show player 10
    player_name "Да, хорошо."
    hide player with dissolve
    return

label terry_dialogue_goldschwagger:
    scene expression game.timer.image("pier_closeup{}")
    show terry 1 at Position(xpos=0.6992,ypos=0.7047)
    show player 10 at left
    with dissolve
    player_name "Ты когда нибудь слышал о {b}GoldSchwagger Водке{/b}?"
    show player 5
    show terry 2
    Terry "О, конечно!"
    Terry "Это водка с маленькими кусочками золота, да?"
    show terry 1
    show player 14
    player_name "Да, это она!"
    show player 13
    show terry 2
    Terry "О-хо, моя {b}Сара{/b}... она не может насытиться этой дрянью, благослави её сердце."
    Terry "Я сам не понимаю этого очарования."
    Terry "Это немного её слабая сторона, если ты спросишь меня."
    Terry "Думаю, моя старушка просто любит смотреть на все это золото!"
    show terry 1
    show player 14
    player_name "Хе, да..."
    player_name "Итак, у тебя есть лишняя, которую я могу у купить?"
    show player 13
    show terry 2
    Terry "Хмм, ты знаешь... Я просто могу продать!"
    show terry 4 at Position(xpos=0.71,ypos=0.7047) with dissolve
    Terry "Дай посмотрю..."
    show terry 23 with dissolve
    Terry "ДА, эта целая и свежая..."
    show terry 23b
    show player 14
    player_name "Ничего себе, она такая... Блестящая!"
    show player 13
    show terry 23
    Terry "Ох хо-хо!"
    Terry "Вот что я тебе скажу, {b}шкипер{/b}. Почему бы тебе не подойти и не взять ее."
    Terry "Бесплатно!"
    show terry 23b
    show player 10
    player_name "А?"
    show player 12
    player_name "Тебе не нужны деньги за это?"
    show player 13
    show terry 23
    Terry "У меня такое чувство, что это для тех милых дам, с которыми ты был на днях, да?"
    show terry 23b
    show player 12
    player_name "... Да, это для рыженькой."
    show player 13
    show terry 23
    Terry "О, эта снобистка!"
    Terry "У нее была пара сисек на груди, не так ли?!"
    show terry 23b
    show player 17
    player_name "..."
    show player 13
    show terry 23
    Terry "Займись этим, приятель."
    show player 653
    show terry 16 at Position(xpos=0.6992,ypos=0.7047)
    with dissolve
    Terry "Каким напарником я буду, если возьму с тебя деньги?!"
    show player 654b
    show goldschwagger_label at Position (xoffset=-88,yoffset=-220)
    with dissolve
    show terry 15
    Terry "К тому же, Я думаю моя {b}Сара{/b} нашла себя в Текиле!"
    Terry "Что хорошо!"
    Terry "Настоящий напиток для настоящей леди!"
    Terry "Разве ты не согласен, шкипер?!"
    show terry 1
    show player 654
    player_name "Ха, как скажешь, {b}Капитан Терри{/b}!"
    player_name "Большое спасибо!"
    show player 654b
    show terry 2
    Terry "Не обращай внимания!"
    Terry "А теперь иди и возьми их, шкипер!"
    show terry 1
    hide player
    hide goldschwagger_label
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
