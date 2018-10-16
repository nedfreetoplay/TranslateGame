label june_dialogue_bissette_fix_printer_repeat:
    scene computer_room_printer_c
    show xtra 40
    show june 17 at right
    show player 10 at left
    with dissolve
    player_name "Привет {b}June{/b}! Ты уже починила принтер?"
    show player 5
    show june 19
    june "Нет, извини. У меня не было времени вообще возиться с ним."
    show june 17
    player_name "..."
    show player 12
    player_name "Тупая технология!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_first:
    scene computer_room_c
    show player 10 at left
    show june 1 at right
    with dissolve
    player_name "Привет, {b}June{/b}?"
    show player 5
    show june 3
    june "Да, {b}[firstname]{/b}?"
    show june 2
    show player 12
    player_name "У меня проблемы с принтером.Что означает загрузка письма ПК?"
    show player 5
    show june 4
    june "Угх, это опять происходит?!Что за кусок дерьма!"
    show june 2
    show player 10
    player_name "Мне просто нужно отсканировать пару страниц из этой книги и распечатать их."
    player_name "Можешь помочь мне?"
    show player 5
    show june 3
    june "Да, конечно!"
    june "Не хочу хвастаться или что-нибудь но Я неплохо разбираюсь в электронике.."
    show june 2
    show player 14
    player_name "Клево!"
    show player 13
    scene black with fade

    scene computer_room_printer_c
    show xtra 40
    show player 13 at left
    show june 9f at right
    with dissolve
    june "О, иногда тебе просто нужно перезапустить его.Дай мне только проверить питание."
    show june 10f with dissolve
    show player 108f
    player_name "Серьезно?"
    show player 5
    show june 9f with dissolve
    june "Да, технология требовательна типо того."
    june "Просто подождем пока он загрузится..."
    show player 10
    player_name "Ладно"
    show player 5
    pause
    pause
    show june 10f with dissolve
    show player 434
    june "Я думала что это должно сработать нет-"
    show june 9f with dissolve
    show player 5
    june "Грр... ошбика загрузки ПК?!"
    show june 15 with dissolve
    show player 110f
    june "Ты никчемный кусок-"
    show june 16 with vpunch
    pause
    show june 15 with dissolve
    june "Я думаю мне придется его открыть и починить его снова."
    show player 10
    player_name "Сколько времени это займет?"
    show player 5
    show june 19 with dissolve
    june "Это займет некоторое время, У меня нет времени разбираться с этим сегодня."
    show june 17
    show player 10
    player_name "Серьезно?"
    show player 5
    show june 19
    june "Да, эта штука действительно заноза в заднице..."
    show june 17
    show player 12
    player_name "Дурацкая технология!"
    show player 518 with dissolve
    return

label june_dialogue_bissette_fix_printer_fail:
    show player 519 with vpunch
    player_name "..."
    show player 10 with dissolve
    player_name "[str_warn]*Вздох*"
    player_name "[str_warn] Наверно я тогда зайду завтра к тебе..."
    show player 5
    show june 19
    june "[str_warn]Извини, {b}[firstname]{/b}."
    hide player
    hide june
    with dissolve
    return

label june_dialogue_bissette_fix_printer_pass:
    show player 519 with vpunch
    pause
    show player 11 with dissolve
    player_name "!!!"
    show june 18
    june "... Хэй! Он работает!"
    show june 17
    show player 10
    player_name "Реально?"
    show player 5
    show june 18
    june "Да! У тебя должна быть способность превращать в золото все, к чему прикасаешься, {b}[firstname]{/b}!"
    show june 17
    show player 14
    player_name "Хах, Да. похоже на то..."
    show player 13
    show june 18
    june "Теперь ты можешь копировать свои страницы..."
    show june 17
    show player 14
    player_name "Хвала небесам! Мне очень нужно отдать эту книгу назад {b}Judith{/b} прежде чем она расстроится."
    player_name "Спасибо за твою помощь, {b}June{/b}!"
    show player 13
    show june 18
    june "Без проблем."
    hide june with dissolve
    show player 518 with dissolve
    player_name "Печать!"
    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause

    show player 510 with dissolve
    player_name "Отлично! Наконец-то у меня есть полный французский словарь."
    player_name "Сейчас мне просто нужно вернуть ее книгу назад {b}Judith's{/b} и я смогу начать частные уроки с {b}Мисс Bissette{/b}."
    hide player with dissolve
    return

label june_dialogue_okita_faptic_engine:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "{b}Miss Okita{/b} хочет, чтобы я достал ей что-нибудь  назывемое как {b}Faptic Механизм{/b}. Она сказала, что ты можешь помочь?"
    show player 1
    show june 4
    june "Какого черта она хочет с одним из них?"
    show player 2
    show june 2
    player_name "Она говорит, что ей это нужно для ее нового изобретения."
    show player 1
    show june 4
    june "Хах. Что за безумную вещь она придумала на этот раз?"
    show player 2
    show june 2
    player_name "Это звучит довольно здорово вообще-то, Это-"
    show player 1
    show june 3
    june "Нет, не говори мне!.Я уверена,я не хочу этого знать."
    show player 11
    show june 2
    player_name "..."
    show player 10
    player_name "Ты можешь мне помочь или нет?"
    show player 11
    show june 4
    june "Вряд ли. Должен ли он быть подлинным?"
    show player 10
    show june 2
    player_name "Эээ, я думаю так."
    show player 11
    show june 4
    june "Ну, это будет трудно достать."
    show player 10
    show june 2
    player_name "Что такое {b}Faptic Механизм{/b} в любом случае?"
    show player 11
    show june 3
    june "О,ты не знаешь?"
    june "Это крошечный механизм, который обеспечивает чувствительные ощущения. Они просто начали ставить их в топовые линии смартфонов."
    show player 10
    show june 2
    player_name "чувствительные ощущения?"
    show player 11
    show june 4
    june "Ощущения, которые ты ощущашь своей кожей.В этом случае,вибрации."
    show player 2
    show june 2
    player_name "О, теперь я понял."
    player_name "Так почему же так трудно это достать?"
    show player 1
    show june 3
    june "Ну, отложив в сторону тот факт, что эти телефоны очень дорогие..."
    show player 11
    show june 4
    june "Они сейчас все распроданы, во всем мире!"
    show player 10
    show june 2
    player_name "О какой цене мы говорим?"
    show player 11
    show june 4
    june "Примерно $2000."
    show player 23
    show june 2
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Что!?За телефон!?"
    show player 11
    show june 4
    june "Я же говорила, что они лучшие.."
    show june 3
    june "На самом деле это не важно однако, ты не слышал меня? Они полностью все распроданы."
    show player 10
    show june 2
    player_name "Убейтесь! Что я скажу Оките?"
    show player 11
    show june 3
    june "Жаль, что она хочет настоящую. Есть некоторые с довольно хорошим качеством, поддельных версий, которые ты мог бы достать."
    show player 10
    show june 2
    player_name "Хмм, будет ли оно работать, а также подлинные?"
    show player 11
    show june 4
    june "Ну нет, но очень близко. Это будет зависеть от того,для чего ты будешь его использовать."
    show june 3
    june "В большинстве случаев, я бы сказала что подделки добьются цели."
    show june 2
    player_name "..."
    show player 10
    player_name "Отлично, где я могу получить поддельные версии?"
    show player 11
    show june 3
    june "Чтож, они достовляли их в {b}Мастер Бластер{/b} контролерами несколько лет тому назад."
    show player 10
    show june 2
    player_name "{b}Мастер Бластер{/b}? Как в видеоигре?"
    show player 11
    show june 3b
    june "Да! Я всегда хотел один, но мои родители не могли себе этого позволить."
    show player 2
    show june 2
    player_name "Ты знаешь что? У моего приятеля{b}Erik{/b} раньше была одна такая!"
    show player 1
    show june 6
    june "У него она еше есть?"
    show player 2
    show june 5
    player_name "Без понятия."
    show player 1
    show june 6
    june "Ну Хорошо, если бы ты смог взать одну такую,то я бы смогла достать один {b}Faptic механизм{/b} для тебя."
    show player 2
    show june 2
    player_name "Прекрсно! Я поговорю с {b}Erik{/b} и посмотрим, есть ли она еще у него."
    player_name "Спасибо за информацию, {b}June{/b}."
    show player 1
    show june 3
    june "Удачи!"
    return

label june_dialogue_okita_get_controller_info:
    scene location_school_computer_day_blur
    show player 2 at left
    show june 2 at right
    with dissolve
    player_name "Как назвался этот контроллер еще раз?"
    show player 1
    show june 4
    june "{b}Мастер Бластер{/b}."
    show june 3
    june "Разве ты не говорил, что у твоего приятеля {b}Erik{/b} есть одна?"
    show player 2
    show june 2
    player_name "Да, у него раньше была.."
    player_name "Я пойду спрошу его об этом."
    player_name "Спасибо, {b}June{/b}."
    show player 1
    show june 3
    june "Удачи!"
    return

label june_dialogue_okita_has_controller:
    scene location_school_computer_day_blur
    show player 502 at left
    show june 2 at right
    with dissolve
    player_name "Это то, о чем вы говорили?"

    show player 1
    show june 11
    with dissolve
    june "Эй, ты и вправду взял одну.Круто!"
    show player 2
    show june 12
    player_name "Так что ты можешь принести {b}Faptic механизм{/b} сюда"
    show player 1
    show june 11
    june "Безусловно."
    june "Просто дай мне несколько минут, чтобы разобрать его."
    show player 2
    show june 12
    player_name "Отлично."
    show player 1
    show june 11

    june "Это так круто!"

    pause
    scene location_school_computer_day_blur
    show player 1 at left
    show june 13 at right
    with dissolve
    june "Вот и все, один поддельный {b}Faptic механизм.{/b}"
    show player 2
    show june 14
    player_name "Это она?Оно такое крошечное..."
    show player 505
    show june 18
    with dissolve
    june "Ага, это мелочь, но она наносит удар."
    show player 506
    show june 17
    player_name "Зорошо, мне лучше отнести это Оките.."
    show player 505
    show june 19
    june "Скажи, {b}[firstname]{/b}?"
    june "Вы не возражаешь, если я оставлю этот контроллер?"
    show player 2 with dissolve
    show june 17
    player_name "Нет, вовсе нет. ни в чем себе не отказывай!"
    show player 1
    show june 18
    june "Приятно! Спасибо, {b}[firstname]{/b}!"
    return

label june_dialogue_mc_intro:
    show player 14 at left
    show june 5 at right
    player_name "Хэй, {b}June{/b}!"
    show player 1
    show june 6
    june "Приветик, {b}[firstname]{/b}!"
    june "Как дела?"
    show june 5
    return

label june_dialogue_intro:
    if player.location.is_here(M_erik):
        show erik 1b at Position (xpos=700)
    show june 1 at right
    show player 14 at left
    with dissolve
    player_name "Привет!"
    show june 3
    show player 1
    june "О, эм,привет?"
    june "Как делишки?"
    show june 2
    return

label june_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Привет, так эмм..."
    player_name "Я вроде как помогаю {b}Мисс Okita{/b} с проектом."
    show player 1
    show june 4
    june "{b}Miss Okita{/b} попросила тебя о помощи с ее проектами?"
    show player 10
    show june 2
    player_name "Да."
    player_name "...И нам нужно немного {b}линз{/b}; например с пары очков?"
    show player 11
    show june 4
    june "Ты хочешь мои очки?"
    show player 10
    show june 2
    player_name "Ну, Я надеялся, что у тебя есть запасной комплект?"
    show player 11
    show june 4
    june "Неа, только один."
    show player 10
    show june 2
    player_name "Может, я смогу тебя убедить тебя отдать мне эту пару?"
    show player 11
    show june 4
    june "Вряд ли."
    show player 10
    show june 2
    player_name "Хмм, ты дальнозоркая или близорукая?"
    show player 11
    show june 3
    june "Близорукая."
    show player 29 with dissolve
    show june 2
    player_name "О, забудь тогда."
    player_name "Мне нужна пара от кого-то кто является и тем и другим."
    show player 3
    show june 4
    june "Я не могу поверить чир {b}Мисс Okita{/b} попросила {b}ТЕБЯ{/b} помочь с ее проектами..."
    show player 29
    show june 2
    player_name "Ну она своего рода, заставила меня..."
    show player 3
    show june 6
    june "Да,это больше похоже на нее."
    show june 3
    june "Чтож, удачи."
    show player 2 with dissolve
    show june 2
    player_name "Да, спасибо."
    return

label june_dialogue_ross_ask_model:
    show player 2
    player_name "Я работаю над проектом для {b}Мисс Ross{/b} и для этого требуется живая модель."
    player_name "Ты былА бы заинтересована?"
    show player 1
    show june 3
    june "Моделирование?"
    show june 3b
    june "Разве я похожа на модель для тебя?"
    show player 10
    show june 5
    player_name "Конечно,почему нет?"
    show player 11
    show june 3b
    june "Пфффф,хорошая попытка."
    show june 3
    june "У меня есть другие запланированные дела ,в любом случае..."
    show player 10
    show june 5
    player_name "У тебя?"
    show june 3
    show player 11
    june "Да, пакет расширения для Орсетте's Подземелья запущен сегодня."
    june "Тебе лучше верить, чтобы я получила эту копию!"
    show player 10
    show june 5
    player_name "Ладно, повеселись,я думаю."
    show player 11
    show june 3b
    june "О, я повеселюсь!"
    return

label june_dialogue_hang_out:
    show player 14
    player_name "Я хотел спросить, не хочешь ли ты потусоваться у меня дома?"
    show player 1
    show june 6
    june "Конечно!"
    june "После школы?"
    show player 14
    show june 5
    player_name "Да."
    show player 1
    show june 6
    june "Итак, значит,у тебя есть своя комната?"
    show player 10
    show june 5
    player_name "Моя комната?"
    show player 11
    show june 6
    june "Да! Нам нужно хорошее тихое место, чтобы расслабиться и играть в игры."
    show player 14
    show june 5
    player_name "Хех, хорошо!"
    show player 1
    show june 6
    june "Круто!"
    june "У меня скоро занятия,мне пора идти."
    june "Увидимся после школы, {b}[firstname]{/b}!"
    return

label june_dialogue_cosplay_no_costume:
    show player 14
    player_name "Какой косплей ты пыталась снова сделать?"
    show player 1
    show june 3
    june "О, это костюм Орсетта ."
    june "Он должен иметь зубы, ожерелье и пояс!"
    show player 14
    show june 2
    player_name "Ах, точно!"
    player_name "Мне кажется, я знаю одно место в{b}торновом центре{/b} у которыз есть такие костюмы..."
    show player 1
    show june 6
    june "О,да?"
    show player 14
    show june 5
    player_name "Я бы могла туда пойти и проверить это!"
    show player 1
    show june 6
    june "Круто! Увидимся."
    return

label june_dialogue_cosplay_has_costume:
    show player 17
    player_name "Я думаю, я нашел кое-что, что может тебе понравиться!"
    show player 1
    show june 3
    june "Хм?"
    show june 6
    june "Что это?"
    show june 5
    show player 423 with fastdissolve
    player_name "Это костюм Орсетта !!"
    show player 422
    show june 6
    june "Для моего косплея?!"
    show player 1
    show june 7
    with fastdissolve
    pause
    show player 13
    show june 8
    june "О, боже!!"
    june "В нем есть все недостающие части, которые мне нужны!"
    june "Они даже выглядят как настоящие зубы!"
    show player 17
    show june 5 with fastdissolve
    player_name "Я рад, что тебе понравилось."
    show player 14
    player_name "Это будет отлично смотреться на тебе!"
    show player 1
    show june 6
    june "Большое спасибо {b}[firstname]{/b}."
    show player 14
    show june 5
    player_name "Я просто рад, что у вас будет классный косплей на Комик-Кон."
    show player 11
    show june 6
    june "Я, вероятно, получу много внимания от толпы, Я уверена!"
    show player 10
    show june 5
    player_name "Вы имеете в виду,от ребят?"
    show player 11
    show june 6
    june "Ну, я полагаю, что да..."
    show june 5
    player_name "..."
    show june 6
    june "Но ты знаешь что?"
    june "Я думаю, что я должна проверить косплей, прежде чем идти!"
    june "Может быть надеть его... перед своим другом?"
    show june 5
    show player 10
    player_name "Например перед кем?"
    show player 11
    show june 6
    june "Тобой!!Дурачок..."
    show player 17
    show june 5
    player_name "О,ха ха!"
    show player 14
    player_name "Конечно, я мог бы эмм... дать свою оценку!"
    show player 1
    show june 6
    june "Здорово! Как насчет того, чтобы встретиться у тебя дома... Как в прошлый раз?"
    show player 14
    show june 5
    player_name "Хорошо, Увидимся после школы тогда!"
    show player 1
    show june 6
    june "Увидимся позже!"
    return

label june_dialogue_ask_about_class:
    show player 14
    player_name "Хэй, в каком ты классе??"
    player_name "Я не часто вижу тебя в школе."
    show player 1
    show june 3
    june "О Я не занимаюсь спортом."
    june "Я предпочитаю торчать здесь..."
    show player 14
    show june 2
    player_name "Чем ты занимаешься в компьютерном зале?"
    show player 1
    show june 3
    june "Ты знаешь, просто вещами... как лазить в интернете..."
    june "... смотреть на обьявления, смотреть стримы и играть в игры."
    show june 2
    show player 14
    player_name "Игры, хм?"
    show player 1
    show june 3
    june "Да."
    show june 1
    show player 14
    player_name "Как и ту, которую тв держишь?"
    show player 1
    show june 3
    june "О, эта вешь? Это просто глупая игра..."
    show player 14
    show june 2
    player_name "Как она называется"
    show player 1
    show june 3
    june "Она завется Orc Bork."
    show player 14
    show june 2
    player_name "Игра об орках?"
    show player 1
    show june 3
    june "Да."
    show june 4
    june "Это довольно трудно."
    show player 11
    june "Я пыталась осилить ее в течение нескольких месяцев..."
    show player 14
    show june 2
    player_name "Неужели это так сложно?"
    show player 1
    show june 3
    june "Ну,это легче, когда ты играете с двумя игроками."
    show june 4
    june "Я просто не нашла никого, кто играет в такие игры в школе..."
    show june 3
    june "Если только, может быть, ты знаешь кого-то?"
    show june 1
    return

label june_dialogue_erik_help:
    show player 14
    player_name "Честно говоря, Я знаю!"
    player_name "Мой хороший друг {b}Erik{/b} ЛЮБИТ игры с орками!"
    player_name "Особенно... Орсетты."
    player_name "Я думаю, вы оба должны играть вместе.!"
    show player 1
    show june 3
    june "{b}Erik{/b}?"
    show player 11
    june "Я не думаю, что знаю его...."
    show player 10
    show june 1
    player_name "Он сказал, что однажды ты одолжила один из его карандашей.."
    show player 1
    show june 4
    june "Хм..."
    show player 14
    show june 5
    player_name "Чтож, н проводит много времени в своей комнате... играя в игры..."
    show player 1
    show june 6
    june "Серьезно?"
    show player 14
    show june 5
    player_name "Я думаю, он мог бы помочь тебе пройти эту игру."
    show player 1
    show june 6
    june "Это было бы круто."
    june "Дай мне знать если когда он будет готов!"
    show player 17
    show june 5
    player_name "Славно!!"
    show player 14
    player_name "Я обязательно дам ему знать."
    return

label june_dialogue_mc_help:
    show player 14
    player_name "Я не очень хорош в этих играх... Но я попробую!"
    show player 1
    show june 4
    june "Ты... хочешь поиграть со мной?"
    june "Ты уверен, что хотел бы этого?"
    show player 14
    show june 2
    player_name "Конечно, почему нет?"
    show player 11
    show june 3
    june "Ну, просто раньше никто не спрашивал...."
    show player 17
    show june 2
    player_name "Я с удовольствием стану твоим первым!"
    show player 21
    show june 5
    player_name "Эммм... я в смысле... в другом-"
    show player 11
    show june 6
    june "Ха ха, ты смешной."
    show june 5
    player_name "..."
    show player 14
    player_name "Итак... Ты хочешь сейчас сыграть?"
    show player 11
    show june 6
    june "Эммм... Как насчет того, чтобы поиграть в другом месте?"
    june "Я немного устала проводить все свое время в этой компьютерной комнате..."
    show player 14
    show june 5
    player_name "Хорошо,где тогда?"
    show player 10
    player_name "Если мы будем играть в коридоре, {b}Annie{/b} задержит нас..."
    show player 11
    show june 6
    june "Хмм... Как насчет того,чтобы мы поиграли у тебя дома?"
    show player 12
    show june 5
    player_name "У Меня... Меня дома?!"
    show player 11
    show june 6
    june "Да!"
    june "После школы?"
    show player 10
    show june 5
    player_name "Эмм... Я думаю мы можем?"
    show player 11
    show june 6
    june "Потрясающе!"
    june "Спасибо, что захотел поиграть со мной..."
    show player 13
    june "Это... очень мило с твоей стороны!"
    show player 14
    show june 5
    player_name "О,ха ха.Это ерунда..."
    show player 1
    show june 6
    june "Просто подойди ко мне, когда будешь готов потусоваться.!"
    june "Я буду ждать здесь."
    show player 17
    show june 5
    player_name "Конечно!"
    return

label june_dialogue_leave:
    show june 2 at right
    show player 14
    player_name "О, ничего!"
    player_name "Просто говорю привет."
    show player 1
    show june 4
    june "О, хорошо тогда..."
    show june 1
    show player 29 at Position(xoffset=8)
    player_name "Эээ... Увидимся позже!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
