label pool_banned_from_pool_day:
    scene pool
    show player 108f at left with dissolve
    player_name "( Я не могу тут находиться. )"
    player_name "( Мне {b}запретили{/b} появляться в бассейне. )"
    show player 34
    player_name "Хмм..."
    show player 35
    player_name "( Может стоит прийти, когда {b}здесь никого не будет{/b}... )"
    hide player with dissolve
    return

label pool_cassie_after_fun:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show ronda 8 at right with dissolve
    ron "А ты долго..."
    show ronda 10
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    player_name "..."
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "Ты о чем?"
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    ron "...Серьезно?"
    ron "Думаешь, я тупая?"
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    show ronda 10
    player_name "...Чего?"
    show ronda 8
    if wearing_swimsuit:
        show player 53f
    else:
        show player 13
    ron "Ты целый час провел вместе с {b}Cassie{/b} в мед комнате."
    show ronda 10
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "...Ну и?"
    show ronda 8
    if wearing_swimsuit:
        show player 53f
    else:
        show player 13
    ron "Это твое представление:Знаешь, ты просто ослепил всех своим... стоячим..."
    show ronda 10
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "Да что ты пытаешься сказать?"
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Все знают, что {b}Cassie{/b} тянет всех понравившихся ей парней в мед комнату!!!"
    show ronda 10
    if wearing_swimsuit:
        show player 45
    else:
        show player 37
    player_name "Думаешь, я ей нравлюсь?"
    show ronda 9
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "{b}OMG{/b}! Перестань косить под дурачка!"
    ron "Тебе не кажется, что она просто возбудилась при виде твоего {b}огромного{/b} члена?!"
    ron "Только поэтому она и повела тебя {b}к себе{/b}!!!"
    show ronda 10
    if wearing_swimsuit:
        show player 45
    else:
        show player 21
    player_name "...Ты думаешь, что у меня большой пенис?"
    show ronda 9
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    ron "!!!"
    ron "Это не-"
    ron "Я этого не говорила"
    show ronda 10
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    player_name "..."
    show ronda 8
    ron "Просто она шлюха, ясно?"
    show ronda 10
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "...Ну, вообще-то, она была очень добра ко мне"
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Угх. Ну ты и свинья"
    hide player
    hide ronda
    with dissolve
    return

label pool_banned_from_pool_night:
    scene pool_night
    show player 14 at left with dissolve
    player_name "( Ну наконец-то! )"
    show player 17
    player_name "( Теперь я смогу спокойно поплавать! )"
    show player 11
    player_name "{b}*Всплеск воды*{/b}"
    show player 90
    player_name "..."
    show player 127
    player_name "( В бассейне кто-то есть? )"
    player_name "( Слишком темно, не могу ничего разглядеть... )"
    hide player with dissolve
    scene pool_night02
    with dissolve
    scene pool_night03
    with Dissolve(0.2)
    scene pool_night04
    with Dissolve(0.2)
    scene pool_night05
    with Dissolve(0.2)
    show player 17 at left with dissolve
    player_name "( Я полагаю, не только мне пришла в голову эта идея... )"
    player_name "( Ну я тоже собираюсь поплавать! )"
    show player 8
    player_name "Вот и я!!!"
    return

label pool_closed_night:
    scene pool_night
    if wearing_swimsuit:
        show player 49f with dissolve
    else:
        show player 2 with dissolve
    player_name "( {b}Бассейн{/b} закрыт. Сомневаюсь, что я смогу поплавать. )"
    hide player with dissolve
    return

label poolrules01_dialogue_pre:
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cas "{b}*СВИСТ*{/b}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cas "Эй!"
    cas "Ты не можешь купаться в этом!"
    cas "Сначала переоденься!"
    return

label poolrules01_dialogue_after:
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Простите, я тут впервые "
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cas "Просто воспользуйся одной из {b}трех раздевалок{/b}..."
    show cassie 3
    cas "...И если у тебя нет {b}плавок{/b}, я не смогу тебя впустить!"
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Окей! Принято!"
    return

label poolrules02_dialogue:
    if wearing_swimsuit:
        show player 53 at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cas "{b}*СВИСТ*{/b}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cas "Эй, {b}[firstname]{/b}!!"
    cas "Опять забыл переодеться?"
    cas "Ты ведь знаешь, что сначала нужно переодеться..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Оу, эй, {b}Cassie{/b}!"
    player_name "Прости, я забыл!"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cas "Можешь воспользоваться медпунктом... Сейчас там никого нет..."
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Окей! Спасибо..."
    return

label pool_cutscene01:
    $ M_player.set("first swim", False)
    call expression game.dialog_select("pool_cutscene01_dialogue")
    $ changing_count = 0
    return

label pool_cutscene01_dialogue:
    show poolcutscene01 with dissolve
    show text "Я не был в бассейне с начальной школы. \nЯ проплыл всего несколько кругов, но уже устал!\nЕщё хотя бы пару кругов..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show poolcutscene01b with dissolve
    show text "Что происходит...\nМне не хватает сил... слишком тяжело...\nНе могу-" at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)
    return

label pool_cutscene02:
    show poolcutscene01 with dissolve
    show text "Я в бассейне не в первый раз и уже научился держать нужный темп.\nЯ могу без проблем проплыть несколько кругов и закончить свою тренеровку!." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene black with dissolve
    with Pause(0.3)
    return

label ronda_after_swimming:
    scene pool
    show player 46 at left
    show ronda 6 at right
    with dissolve
    ron "Неплохо!"
    ron "По крайней мере, ты не утонул в этот раз..."
    show ronda 5
    show player 47
    player_name "Эмм... Спасибо?"
    show player 48
    show ronda 8
    ron "Не обольщайся. Я видела псов, что плавали лучше..."
    hide player
    hide ronda
    with dissolve
    return

label poolrules03_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    show cassie 1 at right
    with dissolve
    cas "{b}*СВИСТ*{/b}"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 22
    player_name "!!!"
    show cassie 2
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    cas "Эй!"
    cas "Это мед комната."
    cas "Ты не можешь туда войти. Она только для персонала"
    if wearing_swimsuit:
        show player 51f
    else:
        show player 29
    show cassie 4
    player_name "Простите! Просто я тут впервые..."
    if wearing_swimsuit:
        show player 51f
    else:
        show player 13
    show cassie 2
    cas "Просто воспользуйся одной из {b}трех раздевалок{/b}..."
    show cassie 4
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Окей! Принято!"
    hide player
    hide cassie
    with dissolve
    $ game.main()

label changing_dialogue_wearing_swimsuit:
    show player 45 with dissolve
    player_name "Ух..."
    player_name "( Я уже переоделся... Можно выходить. )"
    hide player 45 with dissolve
    return

label changing_dialogue_occupied_pre:
    if rand_girl not in used_changing_girls:
        show expression "changing {}".format(rand_girl) as rand_girl_img at right with dissolve
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 with hpunch
        player_name "..."
        hide rand_girl_img
        show expression "changing {}b".format(rand_girl) at right
    else:
        jump expression game.dialog_select("changing_dialogue")
    return

label changing_dialogue_occupied_after:
    if rand_girl == 1:
        Character("Emma") "Эй! Проваливай отсюда!!!"

    elif rand_girl == 2:
        Character("Lily") "Извращенец! Что ты делаешь?!"

    elif rand_girl == 3:
        Character("Olivia") "Эй, сначала купи мне выпить!"

    elif rand_girl == 4:
        Character("Ivy") "Hey, сначала купи мне выпить!"

    elif rand_girl == 5:
        Character("Amelie") "Эй! Проваливай отсюда!!!"

    elif rand_girl == 6:
        Character("Sammy") "Извращенец! Что ты делаешь?!"

    show player 42
    player_name "Упс!"
    player_name "...Простите!"
    hide player with dissolve
    return

label changing_dialogue_change:
    show player 43 with dissolve
    player_name "Наконец-то! Свободная кабинка!"
    show player 35
    player_name "( Они явно должны добавить какие-нибудь знаки, чтобы можно было понять, занята ли кабинка... )"
    show player 8
    window hide
    pause
    hide player 8
    show player 44
    player_name "( Ну вот! Я готов! )"
    hide player with dissolve
    return

label changing_caught:
    scene changeroom01
    show player 5f at right
    show cassie 61 at left
    with dissolve
    cas "Что здесь происходит?!"
    show cassie 60
    show player 22f
    player_name "!!!"
    show cassie 59
    show player 13f
    cas "Опять {b}Ты{/b}?!"
    cas "Мне только что сообщили о домагательствах-"
    show cassie 60
    show player 10f
    player_name "Нет, это не то, что вы думаете!!"
    show player 11f
    show cassie 59
    cas "А мне кажется, что ты просто подглядываешь за переодевающимися девушками..."
    show player 10f
    show cassie 60
    player_name "Я просто пытался найти кабинку-"
    show player 5f
    show cassie 59
    cas "И не додумался сначала проверить, пустая ли она??"
    show player 10f
    show cassie 60
    player_name "Но тут нет двери, чтобы постучать-"
    show player 11f
    show cassie 59
    cas "Можешь оправдываться перед кем-то ещё"
    show player 23f with hpunch
    cas "Тебе {b}запрещено{/b} посещать бассейн."
    show player 10f
    show cassie 60
    player_name "Что?!"
    player_name "Но я должен готовиться к моим школьным-"
    show player 5f
    show cassie 61
    cas "А я тут причем?"
    cas "Я прошу тебя прямо сейчас {b}покинуть{/b} бассейн."
    show player 10f
    show cassie 60
    player_name "..."
    hide player
    hide cassie
    with dissolve
    return

label pool_banned_from_pool_night_swim:
    scene pool_water_night
    show cassie 62 zorder 2 at right
    with fade
    window hide
    pause
    show player 115 zorder 1 at Position(xpos = 230, ypos = 470) with Dissolve(0.3)
    window hide
    show player 116 zorder 1 at left
    show cassie 63 zorder 2
    with Dissolve(0.4)
    cas "!!!"
    show player 123 with dissolve
    player_name "Вот дерьмо!"
    show cassie 73
    player_name "Ты {b}голая{/b}!!?"
    show cassie 67
    show player 125
    cas "ЧТО ТЫ ТУТ ДЕЛАЕШЬ??!"
    show player 120
    show cassie 73
    player_name "Эй! Ты же та {b}спасательница{/b}, что тут работает!!"
    show player 121
    show cassie 72
    cas "..."
    show player 124
    show cassie 67
    cas "Подожди... Ты же тот извращенец, что подглядывает за девушками!"
    show player 125
    cas "Разве я не сказала, что тебе нельзя тут появляться??"
    show player 120
    show cassie 66
    player_name "Эй!! Это {b}не то{/b}, что я делал!"
    show player 126
    player_name "И раз уж я не могу появляться тут днем - буду приходить ночью!"
    show player 120
    player_name "...Секундочку..."
    show cassie 73
    player_name "А что {b}ТЫ{/b} тут делаешь голой посреди ночи??"
    show player 121
    show cassie 64
    cas "Я... Эм... Только не говори никому!"
    show player 124
    cas "У нас обоих могут быть проблемы, если об этом случае узнают..."
    show cassie 65
    show player 126
    player_name "Ладно... Я никому не скажу, но тогда ты разрешишь мне тренироваться!"
    show cassie 64
    show player 122
    cas "Угх... Просто передай мне полотенце..."
    show cassie 65
    show player 118
    window hide
    pause
    show player 119
    player_name "Держи."
    show player 117
    show cassie 68
    with dissolve
    cas "Спасибо."
    show cassie 69
    cas "..."
    show player 124
    show cassie 68
    cas "Прости, что выгнала..."
    cas "Я впущу тебя в следующий раз, обещаю."
    show player 122
    show cassie 70
    player_name "Прекрасно! Спасибо!"
    player_name "Я тут поплаваю немного, окей?"
    show player 124
    show cassie 71
    cas "С ума сошел?! Сейчас мы оба уходим, пока кто-нибудь нас не увидил!"
    show player 126
    show cassie 70
    player_name "Ладно, ладно!"
    hide cassie
    hide player
    with dissolve
    return

label pool_rescued_dialogue:
    scene rescued
    show cassie 6 at Position (xpos = 564, ypos = 768) with dissolve
    cas "ТАК, ВСЕ, СЛУШАЙТЕ!!!"
    cas "ВАМ НУЖНО РАЗОЙТИСЬ!"
    show cassie 7
    cas "Я должна сделать {b}непрямой массаж сердца{/b}!"
    show cassie 8
    window hide
    pause
    show cassie 8
    cas "Окей, это должно сработать..."
    show cassie 9
    window hide
    pause
    show cassie 8
    cas "Давай же..."
    show cassie 9
    window hide
    pause
    show cassie 10
    window hide
    pause
    show cassie 11
    window hide
    pause
    show cassie 12 with hpunch
    window hide
    pause
    show cassie 12
    cas "..."
    show cassie 13
    cas "Тут не на что смотреть!!!"
    cas "Можете просто вернуться в бассейн..."
    show cassie 15
    player_name "{b}*Кха*{/b}"
    show cassie 14
    cas "...От тебя как-то слишком много проблем..."
    cas "Я забираю тебя в мед команту, пока ты не придешь в себя."
    return

label medic_room_dialogue_count_0:
    show cassie 36 with dissolve
    cas "Как ты себя чувствуешь?"
    show cassie 38
    player_name "{b}*Кха*{/b}"
    show cassie 37
    player_name "Я в норме..."
    show cassie 36
    cas "Хоршо, что ты не захлебнулся..."
    show cassie 41
    cas "...Ты что, не умеешь плавать?!"
    show cassie 38
    player_name "{b}*Кха*{/b}, дело не в этом..."
    show cassie 37
    player_name "...Я, {b}*кха*{/b}, тренировался..."
    player_name "...Мне просто не хватило выносливости."
    show cassie 41
    cas "Слушай, тренировка - это прекрасно, но начинать нужно с малого."
    cas "Я не против того, чтобы ты остался и продолжил тренироваться, но..."
    cas "...Я не могу позволить тебе разгуливать вот так..."
    show cassie 38
    player_name "{b}*Кха*{/b}, извини за это."
    show cassie 39
    player_name "Когда я почувствовал твои губы... Я..."
    player_name "...Я не понимаю, почему это происходит последнее время..."
    show cassie 40
    cas "Хаха!"
    cas "Хмм... Ладно..."
    show cassie 41
    cas "Ты когда нибудь был... Ну знаешь, близок с девушкой?"
    show cassie 44
    player_name "Да... Конечно! Это постоянно происходит..."
    show cassie 41
    cas "...Серьезно?"
    show cassie 39
    player_name "{b}*Ох*{/b}"
    player_name "Я почти был на свидании однажды..."
    show cassie 40
    cas "Хаха!"
    cas "Да ладно??"
    show cassie 39
    player_name "Это правда! ...Мы деражлись за руки и всё такое..."
    player_name "...А потом, {b}это{/b} случилось... Она закричала, и..."
    player_name "В любом случае, это было давно..."
    show cassie 41
    cas "Вау... Так ты, типа, девственник?"
    show cassie 39
    player_name "Я думаю, что да?"
    show cassie 40
    cas "Ты такой милый."
    show cassie 45
    player_name "..."
    show cassie 46
    cas "Ты не против, если я осмотрю нашу, эм, проблему?"
    player_name "Эмм... Почему нет?"
    show cassie 42 with hpunch
    window hide
    pause
    show cassie 43 with hpunch
    window hide
    pause
    show cassie 42 with hpunch
    window hide
    pause
    show cassie 46
    cas "Окей, я знаю, как тебе помочь."
    cas "Слушай внимательно..."
    show cassie 47 at Position (xpos=447)
    cas "Всё что тебе нужно сделать, это засунуть свой член в эту дыру в стене."
    cas "И ты сразу почувствуешь приятное тепло..."
    show cassie 49
    cas "...А потом ты будешь чувствовать себя {b}намного{/b} лучше. Поверь мне..."
    show cassie 48
    player_name "Ты говоришь, что я должен засунуть свой пенис в эту дыру?!"
    show cassie 49
    cas "Именно. Ничего сложного, правда?"
    return

label medic_room_dialogue_count_0_lets_try:
    show cassie 37 at center
    player_name "Эмм... Ладно, только не смотри."
    show cassie 46
    cas "Оу, не беспокойся об этом..."
    show cassie 44
    player_name "Почему? Ты уходишь?"
    show cassie 40
    cas "Конечно! Но я скоро вернусь..."
    hide cassie with dissolve
    return

label medic_room_dialogue_count_0_do_not_feel_like_it:
    show cassie 39 at center
    player_name "Ну не знаю... Я чувствую себя очень некомфортно."
    show cassie 41
    cas "..."
    show cassie 41
    cas "Ничего удивительного, ты ведь никогда не был с девушкой..."
    show cassie 44
    player_name "Я просто подожду, пока это не пройдет..."
    player_name "И спасибо, что спасли меня..."
    show cassie 41
    cas "...Без проблем..."
    hide cassie with dissolve
    return

label medic_room_dialogue_count_1:
    show player 49 at right
    show cassie 58 at left
    with dissolve
    player_name "Воу... Это же..."
    show cassie 50
    show player 53
    cas "...Просто потрясающе?"
    show player 52
    show cassie 53
    player_name "Даа..."
    show cassie 52
    show player 51
    cas "Слушай, эта комната только для персонала, окей?"
    cas "Так что я не могу впускать сюда кого попало..."
    show cassie 54
    cas "...Но для тебя я сделаю исключение."
    show cassie 53
    show player 52
    player_name "Правда?"
    show cassie 52
    show player 51
    cas "Только не говори никому"
    show cassie 53
    show player 50
    player_name "...конечно {b}Cassie{/b}!"
    show cassie 55
    show player 52
    cas "Отлично, ещё увидимся... мой большой парень!"
    hide player
    hide cassie
    with dissolve
    return

label medic_room_dialogue_count_2:
    if wearing_swimsuit:
        show player 51 at right
    else:
        show player 1f at right
    show cassie 52 at left
    with dissolve
    cas "Я заметила, как ты шел сюда..."
    show cassie 53
    if wearing_swimsuit:
        show player 49
    else:
        show player 14f
    player_name "Хей, {b}Cassie{/b}!"
    show cassie 52
    if wearing_swimsuit:
        show player 51
    else:
        show player 1f
    cas "Дай угадаю..."
    cas "У тебя опять проблемы там внизу, большой парень?"
    show cassie 54
    cas "Тебе нужно... облегчение?"
    if wearing_swimsuit:
        show player 51
    else:
        show player 29f
    show cassie 53
    player_name "Ну..."
    return

label medic_room_dialogue_count_2_love_to:
    if wearing_swimsuit:
        show player 52
    else:
        show player 21f
    show cassie 53
    player_name "Да, вообще-то нужно..."
    show cassie 52
    if wearing_swimsuit:
        show player 53
    else:
        show player 13f
    cas "Так я и подумала..."
    show cassie 53
    if wearing_swimsuit:
        show player 52
    else:
        show player 21f
    player_name "Думаешь, я могу сделать это снова? ...Засунуть его в дыру?"
    show cassie 55
    if wearing_swimsuit:
        show player 53
    else:
        show player 13f
    cas "Конечно! Вставляй его туда, а я скоро вернусь..."
    hide player
    hide cassie
    with dissolve
    return

label medic_room_dialogue_count_2_just_changing:
    if wearing_swimsuit:
        show player 50
    else:
        show player 17f
    show cassie 53
    player_name "Я хотел бы просто переодеться..."
    show cassie 57
    if wearing_swimsuit:
        show player 51
    else:
        show player 11f
    cas "..."
    show cassie 56
    cas "Это, эм, печально..."
    show cassie 57
    if wearing_swimsuit:
        show player 52
    else:
        show player 10f
    player_name "Прости..."
    player_name "Я бы хотел побыть тут немного, но мне нужно тренироваться!"
    show cassie 55
    if wearing_swimsuit:
        show player 53
    else:
        show player 1f at right
    cas "...Ничего страшного. Только захаживай сюда как-нибудь."
    hide cassie with dissolve
    if wearing_swimsuit:
        show player 33f
    else:
        show player 44f
    player_name "Обязательно!"
    hide player with dissolve
    return

label medic_room_dialogue_count_finished:
    show player 17f at right
    show cassie 50 at left
    with dissolve
    player_name "Это было... Прекрасно..."
    show player 13f
    show cassie 51
    cas "Рада, что тебе лучше..."
    show player 14f
    show cassie 53
    player_name "Большое спасибо..."
    show cassie 54
    show player 1f
    cas "Только держи это между нами, окей?"
    show cassie 53
    show player 18f
    player_name "Да, конечно!"
    show cassie 55
    show player 1f
    cas "Отлично. Тогда ещё увидимся."
    hide player
    hide cassie
    with dissolve
    return

label gloryhole_medic:
    call expression game.dialog_select("gloryhole_medic_dialogue")
    $ game.timer.tick()
    if not store._in_replay == None:
        jump expression game.dialog_select("gloryhole_medic_bj")
    call screen gloryhole_stage01

label gloryhole_medic_dialogue:
    scene changeroom03
    show cassie 16 at Position(xpos = 431, ypos = 768)
    with fade
    window hide
    pause
    show cassie 17
    window hide
    pause
    show cassie 18 with hpunch
    window hide
    pause
    cas "!!!"
    show cassie 19
    cas "Вау..."
    cas "( Я люблю его член... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    cas "( Эта длина... )"
    show cassie 21 at Position (xpos = 440, ypos = 768)
    cas "( ...эта толщина... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 21 at Position (xpos = 440, ypos = 768)
    window hide
    pause
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 22 at Position (xpos = 434, ypos = 768) with hpunch
    window hide
    pause
    show cassie 23 at Position (xpos = 430, ypos = 768)
    cas "( Он только что дернулся! )"
    show cassie 24 at Position (xpos = 431, ypos = 768)
    cas "( Посмотрим... ну и что мне с этим делать? )"

label gloryhole_medic_bj:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_27 at Position (xpos = 444, ypos = 768)
    pause 4
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    call screen gloryhole_stage02

label gloryhole_medic_bjfacefinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 29 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 30 with hpunch
    pause .3
    show cassie 31
    pause .5
    show cassie 31
    cas "Вау... Так много спермы..."
    $ renpy.end_replay()
    jump expression game.dialog_select("medic_room_dialogue")

label gloryhole_medic_bjtitsfinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 32 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 33 with hpunch
    pause .3
    show cassie 34
    pause .5
    show cassie 34
    cas "Вау... столько спермы..."
    $ renpy.end_replay()
    jump expression game.dialog_select("medic_room_dialogue")

label gloryhole_medic_fuck_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Я знаю его не настолько хорошо, чтобы делать подобное... )"
    call screen gloryhole_stage01

label gloryhole_medic_fuckraw_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Это сумасшествие!!! Я не могу сделать это... )"
    call screen gloryhole_stage01

label gloryhole_medic_swallow_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Я знаю его не настолько хорошо, чтобы делать подобное... )"
    call screen gloryhole_stage02

label locked_door26_dialogue:
    scene pool
    show player 35 with dissolve
    player_name "( Я должен купить {b}плавки{/b} прежде чем переодеваться... )"
    player_name "( ...Они должны быть в {b}торговом цетре{/b}. )"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
