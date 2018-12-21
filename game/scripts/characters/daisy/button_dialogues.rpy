label daisy_button_baby_leave:
    show player 14b
    player_name "Я оставлю вас в покое, ребята."
    show player 1b
    show daisy f_normal_talk
    daisy "Хорошо."
    show daisy f_down_talk
    daisy "Скажи, пока, папочке."
    show daisy f_down
    show player 17
    player_name "Хехе."
    show player 14b
    player_name "До свидания, малыш."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_anything_baby:
    show player 14b
    player_name "Принести тебе что-нибудь?"
    show player 1b
    show daisy f_normal_talk
    daisy "Нет, все нормально."
    daisy "Спасибо, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Пожалуйста."
    show player 1b
    return

label daisy_button_hows_baby_doing_boy:
    show player 14b
    player_name "Как у него дела?"
    show player 1b
    show daisy f_normal_talk
    daisy "Он много спит ..."
    daisy "... А когда он не спит, он ест!"
    show daisy f_normal
    show player 14b
    player_name "Значит, он похож на свою маму?"
    show player 1b
    show daisy f_laugh
    daisy "Ну эээ!"
    show daisy f_normal
    show player 17
    player_name "Хехехе."
    show player 1b
    return

label daisy_button_hows_baby_doing_girl:
    show player 14b
    player_name "Как у нее дела?"
    show player 1b
    show daisy f_normal_talk
    daisy "Она много спит ..."
    daisy "... А когда она не спит, она ест!"
    show daisy f_normal
    show player 14b
    player_name "Значит, она похож на свою маму?"
    show player 1b
    show daisy f_laugh
    daisy "Ну эээ!"
    show daisy f_normal
    show player 17
    player_name "Хехехе."
    show player 1b
    return

label daisy_button_gave_birth_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_baby f_down
    with dissolve
    player_name "Привет, {b}Дэйзи{/b}."
    show player 1b
    show daisy f_down_talk
    if M_daisy.pregnancy.baby_gender == "boy":
        daisy "Разве он не прекрасен, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "Верно!"
        show player 1b
        show daisy f_normal_talk
        daisy "У него твои глаза."
    else:
        daisy "Разве она не прекрасна, {b}[firstname]{/b}?"
        show daisy f_down
        show player 14b
        player_name "Верно!"
        show player 1b
        show daisy f_normal_talk
        daisy "У нее твои глаза."
    show daisy f_normal
    pause
    show daisy f_down_talk
    daisy "И мои рога!"
    show daisy f_laugh
    daisy "Хехехе!"
    show daisy f_normal
    return

label daisy_button_hows_the_baby_1:
    show player 14b at left
    show daisy
    player_name "Как ребенок?"
    show player 1b
    show daisy f_normal_talk
    daisy "Ммм, я не знаю."
    daisy "Меня тошнит по утрам, но в остальном я чувствую себя так же, как всегда."
    show daisy f_normal
    show player 14b
    player_name "Что ж, это хорошо."
    player_name "Убедись и скажи {b}Диане{/b} или мне, если почувствуешь, что что-то не так, хорошо?"
    show player 1b
    show daisy f_normal_talk
    daisy "Д-да, хорошо {b}[firstname]{/b}."
    show daisy f_normal
    return

label daisy_button_hows_the_baby_2:
    show player 1b at left
    show daisy f_normal_talk
    daisy "Хехе, смотри {b}[firstname]{/b}!"
    show daisy f_down_talk
    daisy "Мои сиськи становятся больше!"
    show daisy f_down
    show player 14b
    player_name "Да, ты производишь больше молока, готовясь к рождению ребенку."
    show player 1b
    show daisy f_normal_talk
    daisy "О, это сделает {b}Диану{/b} счастливой ,не так ли?"
    show daisy f_normal
    show player 14b
    player_name "Да, будь уверена."
    show player 1b
    pause
    show daisy f_down_talk a_naked_touch with dissolve
    daisy "Ты видел мой животик?"
    show daisy f_normal
    show player 14b
    player_name "Да."
    show player 1b
    show daisy f_sad_talk
    daisy "Ты думаешь, это уродливо?"
    show daisy f_sad
    show player 14b
    player_name "Нет, вовсе нет!"
    player_name "Я думаю, это довольно мило, на самом деле..."
    show player 1b
    show daisy f_laugh
    daisy "Правда?!"
    daisy "Хе-хе, ты странный {b}[firstname]{/b}!"
    show daisy f_normal a_naked_sides with dissolve
    show player 17
    player_name "Хехе!"
    show player 1b
    return

label daisy_button_hows_the_baby_3:
    show player 1b at left
    show daisy a_naked_touch f_sad_talk
    daisy "{b}*вздыхает*{/b}"
    daisy "Этот детский бизнес-настоящая проблема, понимаешь?!"
    show daisy f_sad
    show player 10b
    player_name "О?"
    show player 5b
    show daisy f_sad_talk
    daisy "Мне хочется писать каждые пять минут!"
    show daisy f_sad
    show player 14b
    player_name "Хех, да, это звучит как морока!"
    show player 1b
    show daisy f_down_talk
    daisy "... И ребенок все время танцует!"
    show daisy f_down
    show player 14b
    player_name "Танцует?"
    show player 1b
    show daisy f_normal_talk
    daisy "Да, {b}Диана{/b} говорит, что он пинается, но я не знаю, почему он пинает меня..."
    daisy "Я все-таки мамочка."
    show daisy f_normal
    show player 14b
    player_name "Хех, я уверен, что ты права."
    player_name "Наверное, просто взволнован, чтобы выйти."
    show player 1b
    show daisy f_laugh
    daisy "Да!"
    daisy "В смысле, я танцую, когда возбуждена."
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Хех, ты точно знаешь."
    show player 1b
    return

label daisy_button_intro_end:
    scene expression player.location.background_blur with None
    show daisy f_normal_talk
    show player 1b at left
    with dissolve
    daisy "{b}*вздыхая* [firstname]{/b}!!!"
    show daisy f_normal
    show player 14b
    player_name "Привет {b}Дейзи{/b}."
    hide player
    show daisy b_naked_hug f_empty a_empty
    with dissolve
    daisy "Я скучала по тебе!"
    pause
    show daisy b_naked a_naked_sides f_normal
    show player 14b at left
    player_name "Д-да, я тоже скучал."
    show player 1b
    return

label daisy_button_have_sex_first:
    show player 14b at left
    show daisy
    player_name "Ты все еще хочешь заняться сексом?"
    show player 1b
    show daisy f_normal_talk
    daisy "О, да!"
    daisy "Очень!"
    show daisy f_normal
    pause
    show player 14b
    player_name "Хорошо, давай."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*вздыхая*{/b} Правда?!"
    show daisy f_laugh
    daisy "Ура!!!"
    show daisy f_normal
    show player 14b
    player_name "Пойдем к одному из доильных аппаратов."
    show player 1b
    show daisy f_laugh
    daisy "Хорошо!"
    hide player
    hide daisy
    with dissolve
    pause
    return

label daisy_button_have_sex_repeat:
    show player 10b at left
    show daisy
    player_name "Ты хочешь... Ты знаешь?"
    show player 5b
    show daisy f_normal_talk
    daisy "{b}*вздыхая*{/b} Заняться сексом?!"
    show daisy f_normal
    show player 14b
    player_name "Д-да."
    show player 1b
    show daisy f_normal_talk
    daisy "Конечно!"
    daisy "Обожаю, когда мы занимаемся сексом!"
    show daisy f_normal
    show player 14b
    player_name "Хех, тогда давай пойдем к доильным аппаратам."
    show player 1b
    show daisy f_laugh
    daisy "Хорошо!"
    hide player
    hide daisy
    with dissolve
    pause
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show daisy_sex_breed pre_talk
    show daisy_sex_breed_mc
    with dissolve
    daisy "Хорошо, ласка... Входи уже!"
    daisy "Хехехе!"
    hide daisy_sex_breed_mc
    show daisy_sex_breed insert_and_pullout
    with dissolve
    pause
    show daisy_sex_breed creampie_pullout with dissolve
    pause 1
    show daisy_sex_breed creampie
    daisy "!!!" with hpunch
    $ animated = False
    return

label daisy_button_diane_breeding:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_naked a_naked_sides f_shamed_talk_smile
    with dissolve
    dia "Пссс, {b}[firstname]{/b}."
    show diane f_shamed
    show player 5
    player_name "Хмм?"
    show player 10
    player_name "{b}Диана{/b}, что происходит?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Ты приехал повидаться с {b}Дейзи{/b}?"
    show diane f_shamed
    show player 14
    player_name "Да, я как раз собирался ее подоить."
    show player 13
    show diane f_smirk_talk
    dia "Ммм, меня так заводит просмотр, как ты доишь ее-"
    show diane f_smirk
    pause
    hide player
    show diane b_pull_mc_naked f_empty a_empty at flip
    dia "Пойдем со мной!" with hpunch
    dia "{b}Дейзи{/b} может подождать немного."
    dia "Ты нужен мне внутри меня, прямо сейчас!"
    hide diane with dissolve
    player_name "Хо-хорошо-"
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    dia "Давай жеребец, дай его мне!"
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "О, даааааааа!!" with hpunch
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    pause
    dia "Ааа!"
    pause
    dia "Спасибо, {b}[firstname]{/b}."
    dia "Это неправильно с моей стороны украсть тебя у {b}Дейзи{/b}, пока она еще приспосабливается, но ..."
    dia "... Мне правда нужн-"
    dia "А, черт!"
    dia "... Очень нужно это сегодня!"
    pause
    player_name "Хех, это не проблема {b}Диана{/b}."
    pause
    scene location_diane_garden_cutscene12
    with fade
    player_name "Я думаю, что {b}Дейзи{/b} приспосабливается очень хорошо."
    player_name "Она выглядит очень счастливой, живя здесь."
    dia "Я тоже так думаю."
    dia "Нам действительно повезло найти ее."
    dia "Она такая очаровательная!"
    player_name "К тому же, она помогает тебе с твоим бизнесом, верно?"
    dia "Определенно!"
    dia "Она производит больше, чем я, и она даже не-"
    scene location_diane_garden_cutscene12b with fade
    "{b}*звонк*{/b}{p=1}{nw}"
    "{b}*шмяк*{/b} !!!" with hpunch
    player_name "What the-"
    pause
    dia "{b}Дейзи{/b}?!"
    scene expression player.location.background_blur with None
    show player 368f at Position (xpos=650)
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    show daisy b_naked_shy a_naked_shy_front f_shy_sad_talk at flip
    with dissolve
    daisy "Я не-"
    daisy "Я, Я,Я не-"
    show daisy f_shy_sad
    show diane f_smirk_talk
    dia "Ты наблюдала за нами?"
    show diane f_smirk
    pause
    show daisy f_shy_sad_talk
    daisy "Прости, пожалуйста, не злись!"
    show daisy f_shy_sad
    show diane f_laugh
    dia "Хе-хе, все в порядке, милая!"
    hide daisy
    show daisy b_naked_diane_comfort a_empty f_empty at Position (xpos=200)
    show diane b_empty a_empty f_smirk_talk_fardown zorder 1 at Position (xpos=200)
    with dissolve
    dia "Тише, мы не сумасшедшие."
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "{b}*сопя*{/b} В-вы не сумасшедшие?"
    show daisy b_naked_diane_comfort
    show diane f_smirk_talk_fardown
    dia "Конечно нет!"
    dia "Тебе просто было любопытно, не так ли?"
    show diane f_smirk_fardown
    show daisy b_naked_diane_comfort2
    daisy "Д-да..."
    show diane b_naked a_naked_sides f_smirk at Position (xpos=600)
    hide daisy
    show daisy b_naked a_naked_sides f_normal_talk at flip
    with dissolve
    daisy "Я никогда раньше не видела, чтобы кто-то играл в {b}прятки ласки{/b}..."
    show daisy f_normal
    show player 367f
    player_name "{b}Прятки ласки{/b}?"
    show player 368f
    show daisy f_normal_talk
    daisy "Мы с мастером тоже в нее играли!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "Однако его ласка была не такой большой, как у {b}[firstname]{/b} ..."
    show daisy f_normal
    show player 367f
    player_name "Ты имеешь в виду, что {b}Джебедия{/b} занималась с тобой сексом?!"
    show player 368f
    show diane f_shamed_talk_smile
    dia "{b}*вздыхая*{/b} Конечно, так оно и было..."
    dia "... Грязный старый ублюдок."
    show diane f_shamed_talk
    show daisy f_normal_talk
    daisy "Не расстраивайся {b}Диана{/b}..."
    show daisy f_laugh
    daisy "Мастеру просто нужна была моя помощь!"
    daisy "Я не хотела, чтобы его ласка заболела и умерла!"
    show daisy f_normal
    show player 367f
    player_name "Ладно, я в замешательстве."
    show player 368f
    show daisy f_normal_talk
    daisy "Вот почему вы играете с {b}[firstname]{/b}, верно?"
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Милая, что именно тебе сказал этот старик?"
    show diane f_shamed
    show daisy f_normal_talk
    daisy "Ммм, что иногда мужская ласка заболевает и становится жесткой во всем..."
    show daisy f_normal
    player_name "..."
    show daisy f_normal_talk
    daisy "... И когда это случится, ему нужно будет спрятать его в женской скрытой норке."
    daisy "В противном случае он становится синим и отпадает."
    show daisy f_normal
    pause
    show diane f_shamed_talk_smile
    dia "Ну, он был творческим старым ублюдком... Я отдам ему должное."
    show diane f_shamed
    show player 367f
    player_name "... скрытой норке?"
    show player 368f
    show daisy f_normal_talk
    daisy "Да!"
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    show diane f_surprised_front
    daisy "Хозяин сказал, что его ласке больше нравится моя скрытая норка!"
    show player 430f
    with hpunch
    pause
    show player 66f
    daisy "{b}*вздох*{/b}"
    hide daisy
    show daisy b_naked a_naked_sides f_sad_talk at flip
    with dissolve
    show diane f_surprised
    daisy "Смотри {b}Диана{/b}!"
    daisy "Ласка {b}[firstname]{/b} снова заболевает!"
    show diane f_surprised_front
    show daisy f_sad
    show player 67f
    pause
    hide daisy
    show daisy b_naked_behind f_empty a_empty at Position (xpos=100)
    with dissolve
    daisy "Хочешь воспользоваться моей скрытой норкой на этот раз?!"
    show player 430bf
    player_name "Эээ."
    show player 430f
    show diane f_shamed_talk_smile
    dia "Нет, нет, нет..."
    dia "{b}*ммм*{/b} ласка {b}[firstname]{/b}... в порядке."
    show diane f_shamed
    hide daisy
    show daisy b_naked a_naked_sides f_normal at flip
    with dissolve
    show diane f_shamed_talk_smile
    dia "Прямо сейчас, я думаю, нам с тобой нужно поговорить."
    show diane f_shamed
    show daisy f_normal_talk
    daisy "О, хорошо."
    show daisy f_normal
    show diane f_smirk_talk
    dia "Я уверен, что {b}[firstname]{/b} может позаботиться об этом сам, не так ли {b}[firstname]{/b}?"
    show diane f_smirk
    show player 432f
    player_name "Д-да..."
    show player 431f
    show diane f_smirk_talk
    dia "Почему бы тебе не отправиться домой на день и дать нам немного времени для девочек."
    show diane f_smirk
    show player 432f
    player_name "Конечно."
    show player 431f
    show daisy f_laugh
    daisy "Покааа, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 432f
    player_name "Хех, пока {b}Дейзи{/b}."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_more_jebadiah_delmont_2:
    show player 10b
    player_name "Есть кое-что, чего я до сих пор не понимаю, {b}Дейзи{/b}."
    show player 5b
    show daisy f_normal
    daisy "Хмм?"
    show player 10b
    player_name "Почему ты так боялась меня, когда впервые появилась?"
    show player 5b
    show daisy f_sad_talk
    daisy "О."
    show daisy f_surprised_after_appear
    daisy "Умм..."
    pause
    show player 10b
    player_name "Ты не должна говорить мне, если не хочешь."
    show player 5b
    show daisy f_sad_talk
    daisy "Нет, Я-"
    daisy "Я хочу."
    show daisy f_sad_talk_closed
    daisy "Я просто..."
    pause
    show daisy a_naked_cover with dissolve
    daisy "Я была плохой девочкой, {b}[firstname]{/b}!"
    show player 10b
    player_name "Ааа?!"
    player_name "Мне трудно это представить."
    show player 5b
    show daisy f_sad_talk
    daisy "Нет, была!"
    show daisy a_naked_sides
    daisy "Видите ли, однажды хозяин забыл запереть хижину, а я-"
    show daisy f_sad_talk_closed
    daisy "Я-"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Я просто хотела прогуляться!"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Но я заблудился..."
    show daisy f_sad
    show player 10b
    player_name "И?"
    show player 5b
    show daisy f_sad_talk
    daisy "Ух."
    daisy "Это было так страшно!"
    daisy "Я потерялась на несколько дней без еды и воды..."
    daisy "... Но потом, они спасли меня."
    show daisy f_sad
    show player 10b
    player_name "Кто спас тебя?"
    show player 5b
    show daisy f_sad_talk
    daisy "Бернис и Джетро."
    daisy "Они привезли меня домой и дали мне поесть."
    show daisy f_sad
    show player 10b
    player_name "Хорошо, что повезло."
    show player 5b
    show daisy f_sad_talk
    daisy "Ага... "
    show daisy a_naked_wiping_tears with dissolve
    daisy "{b}*сопя*{/b}"
    show daisy a_naked_sides with dissolve
    daisy "Они были очень хорошими людьми."
    daisy "Но мастер так не думал..."
    show daisy f_sad
    player_name "Хмм?"
    show daisy f_sad_talk
    daisy "Он был так зол на меня!"
    daisy "Я сказала ему, что не хотела, но он схватил меня за руку и вытащил из дома."
    daisy "Джетро закричал на него, чтобы он успокоился, и мастер ударил его."
    daisy "Снова и снова и снова."
    daisy "Это было ужасно!"
    show daisy f_sad
    show player 10b
    player_name "Вот же гад..."
    player_name "Почему он так разозлился?!"
    show player 5b
    show daisy f_sad_talk
    daisy "Он сказал, что другим людям нельзя доверять, особенно мужчинам."
    daisy "Что они передадут меня проветильству для похлопывания по голове."
    show daisy f_sad
    show player 10b
    player_name "Проветильству?!"
    show player 5b
    pause
    show player 10b
    player_name "Ты имеешь в виду правительство?"
    show player 5b
    show daisy f_sad_talk
    daisy "Да, точно."
    show daisy f_sad
    player_name "..."
    show player 10b
    player_name "И что случилось потом?"
    show player 5b
    show daisy f_sad_talk
    daisy "После этого хозяин стал заковывать меня ночью в хижине."
    show daisy f_sad
    show player 10b
    player_name "Он приковал тебя цепями?!"
    show player 5b
    show daisy f_sad_talk
    daisy "Да, он сказал, что это для моего же блага..."
    daisy "... потому что я была плохой девочкой."
    show daisy f_sad
    show player 10b
    player_name "Ты не плохая девочка, {b}Дейзи{/b}."
    player_name "Мне кажется, он был плохим мастером."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*сопя*{/b} Пр-правда?"
    show daisy f_sad
    show player 10b
    player_name "Да."
    player_name "Ты определенно не заслуживаешь такого обращения!"
    show player 5b
    show daisy f_sad_talk_closed
    daisy "Трудно уснуть, когда ты прикован."
    show daisy f_sad
    show player 10b
    player_name "Держу пари."
    player_name "Я бы хотел приковать его и показать ему, каково это!"
    show player 5b
    daisy "..."
    show player 10b
    player_name "Так вот почему ты испугалась, когда увидела нас?"
    show player 5b
    show daisy f_sad_talk
    daisy "Ух."
    daisy "Я боялась, что хозяин узнает."
    show daisy f_sad
    show player 10b
    player_name "Ну, об этом не стоит беспокоиться."
    player_name "Мы с {b}Дианой{/b} больше никому не позволим причинить тебе боль."
    show player 5b
    return

label daisy_button_how_are_your_flowers_3:
    show player 14b
    player_name "Как поживают твои цветы?"
    show daisy f_normal_talk
    daisy "О, {b}подсолнухи{/b}, которые ты мне дал, такие красивые!"
    daisy "I love them!"
    show daisy f_normal
    show player 14b
    player_name "Замечательно!"
    player_name "У меня было чувство, что они поднимут тебе настроение."
    show player 1b

    daisy "Мммммм!"
    return

label daisy_button_you_seem_happy:
    show player 14b
    player_name "Ты выглядишь очень счастливой сегодня."
    show player 1b
    show daisy f_normal_talk
    daisy "Я!"
    daisy "Очень, очень счастлива!"
    daisy "Я живу здесь, в хорошем сарае, а {b}Диана{/b} заботится обо мне, а ты приносишь мне вкусную пиццу..."
    show daisy f_normal
    pause

    show daisy f_normal_talk
    daisy "Я рада, что ты нашел меня {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Да, я тоже."
    player_name "Мне нравится видеть тебя счастливой, {b}Дейзи{/b}!"
    show player 1b
    show daisy f_surprised_after_appear
    daisy "!!!"
    show daisy a_naked_touch with dissolve
    pause
    show player 10b
    player_name "Ты в порядке?"
    show player 5b
    show daisy f_normal_talk
    daisy "Д-да."
    show daisy a_naked_sides with dissolve
    daisy "Иногда я чувствую себя странно в животе, когда ты рядом..."
    show daisy f_normal
    player_name "Хмм?"
    show player 10b
    player_name "Больно?"
    show player 5b
    show daisy f_down_talk
    daisy "Н-нет, это чувство ... Все покалывает."
    show daisy f_down
    show player 10b
    player_name "Ха, странно."
    show player 5b
    return

label daisy_button_want_me_to_milk_you:
    show daisy f_normal_talk
    show player 1b at left
    daisy "Эээ, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Да?"
    show player 1b
    show daisy f_normal_talk
    daisy "Ты не мог бы подоить меня?"
    show daisy f_down_talk b_naked_boob a_empty with dissolve
    daisy "Потому что мои сиськи снова полные."
    show daisy f_down
    pause
    show player 14b
    player_name "{b}*глоток*{/b} Ко-конечно."
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Ты хорошо себя чувствуешь?"
    show daisy f_down_talk
    daisy "Д-да."
    show daisy f_down
    player_name "Просто расслабься и наслаждайтся, {b}Дейзи{/b}."
    return

label daisy_button_finished_milking_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh a_naked_up
    with dissolve
    daisy "{b}*вздох* [firstname]{/b}!!!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Привет, {b}Дейзи{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "Что мы будем делать сегодня?!"
    show daisy f_normal
    show player 14b
    player_name "Хех, я еще не знаю."
    show player 1b
    return

label daisy_button_daisy_need_milking:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Хорошо, я готова!"
    show daisy f_normal
    show player 10b
    player_name "М-можно тебя кое о чем спросить?"
    show player 5b
    daisy "Hmm?"
    show player 10b
    player_name "Почему ты хочешь, чтобы я-"
    player_name "{b}*ммм*{/b} По-подоил тебя?"
    show player 5b
    show daisy f_normal_talk
    daisy "Ну, {b}Диана{/b} говорит, что у тебя это получается лучше, чем у нее..."
    show daisy f_down_talk
    daisy "... и Я..."
    show daisy f_down
    pause

    show daisy f_down_talk
    daisy "... Ты делаешь меня..."
    daisy "... я не знаю."
    show daisy f_laugh
    show player 14b
    player_name "Эээ, хорошо."
    show daisy f_normal
    player_name "Думаю, нам пора начинать, да?"
    show player 1b
    pause
    hide player
    show daisy b_player_milking a_empty f_down
    with dissolve
    daisy "!!!"
    player_name "Ты хорошо себя чувствуешь?"
    show daisy f_down_talk
    daisy "Д=да."
    show daisy f_down
    player_name "Дайте мне знать, если я сделаю что-то не так, хорошо?"
    show daisy f_normal_smelling
    daisy "Ммммммм."
    pause
    show daisy f_down_talk
    daisy "{b}Диана{/b} была права, ты действительно хорош в этом!"
    show daisy f_down
    player_name "Хе, спасибо."
    show daisy f_down_talk
    daisy "Ааа!"
    show daisy f_down
    player_name "Просто расслабься и наслаждайся, {b}Дейзи{/b}."
    return

label daisy_button_get_new_flowers_has_flowers:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy a_naked_shy_front b_naked_shy f_shy_sad at Position (yoffset=10)
    with dissolve
    player_name "Привет, {b}Дейзи{/b}."
    show player 1b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Привет, {b}[firstname]{/b}."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 14b
    player_name "У меня есть кое-что для тебя."
    show player 1b
    daisy "Хмм?"
    show player 239_240 with dissolve
    pause
    show player 722 with dissolve
    pause
    show daisy f_normal_talk b_naked a_naked_cover with dissolve
    daisy "{b}*вздох*{/b} Вау!!!"
    show player 1b
    show daisy a_naked_sunflower1 f_down_talk
    with dissolve
    daisy "Посмотри, какие они большие и красивые!"
    pause
    show daisy a_naked_sunflower2 f_normal_smelling with dissolve
    daisy "Ммм!"
    show daisy b_naked_hug f_empty a_empty
    hide player
    with dissolve
    daisy "Спасибо, спасибо, спасибо, спасибо!!!"
    show player 14b at left
    show daisy a_naked_sunflower1 b_naked f_down zorder 1 at Position (xpos=300)
    with dissolve
    player_name "Хех, всегда пожалуйста."
    show player 1b
    show daisy f_down_talk
    daisy "Как называются эти цветы?"
    show daisy f_down
    show player 14b
    player_name "Они называются {b}Подсолнухи{/b}."
    show player 1b
    show daisy f_normal_talk
    daisy "Почему они их так называют?"
    show daisy f_normal
    show player 14b
    player_name "Наверное, из-за их желтого цвета."
    show player 1b
    show daisy f_normal_talk
    daisy "О, я понимаю."
    show daisy f_laugh
    daisy "Как солнце!"
    show daisy f_down
    show player 14b
    player_name "Хех, точно."
    show player 1b
    show daisy f_laugh
    daisy "Хехе!"
    show daisy f_normal
    show diane b_shirtless a_shirtless_sides f_shamed_talk_fardown at Position (xpos=600) with dissolve
    show player 13
    dia "О, ты раздобыла новые цветы?"
    show diane f_shamed_fardown with None
    show daisy f_laugh at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "{b}[firstname]{/b} принес мне немного!"
    show daisy f_down
    show diane f_smirk_talk
    dia "Ну разве это не мило с его стороны..."
    show diane f_smirk
    show daisy f_normal_talk
    daisy "Ага!"
    daisy "{b}[firstname]{/b} самый хороший человек на свете!"
    show daisy f_down
    show diane f_smirk_talk
    dia "Конечно."
    show diane f_smirk
    pause
    show diane f_shamed_talk_fardown
    dia "Хорошо, мы должны поставить цветы в воду, чтобы я могла тебя подоить, милая."
    dia "Сегодня предстоит много работы."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "Я хочу, чтобы это сделал {b}[firstname]{/b}."
    show player 11
    player_name "!!!" with hpunch
    show player 10b
    player_name "Ч-что?"
    show player 5b
    show daisy f_normal_talk
    daisy "Это нормально, если {b}[firstname]{/b} подоит меня, {b}Диана{/b}?"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "Со мной все в порядке."
    show diane f_shamed_fardown with None
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show diane f_smirk
    daisy "Будешь доить меня, {b}[firstname]{/b}?"
    show daisy f_normal
    show player 14b
    player_name "Ох, конечно... Если это то, чего ты хочешь."
    show player 1b
    show daisy f_laugh
    daisy "Ура!!"
    show daisy f_normal
    show diane f_smirk_talk
    dia "Просто будь с ней поосторожнее, ладно?"
    show diane f_smirk
    show player 14
    player_name "Д-да, хорошо."
    show player 13
    show diane f_shamed_talk_fardown
    dia "Хорошо, давайте займемся этими цветами."
    show diane f_shamed_fardown
    show daisy f_shy_talk_back
    daisy "Хорошо."
    show daisy f_normal_talk
    daisy "Я сейчас вернусь, {b}[firstname]{/b}."
    show daisy f_normal
    show player 14b
    player_name "Х-хорошо."
    hide player
    hide daisy
    hide diane
    with dissolve
    return

label daisy_button_get_new_flowers_no_flowers:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy a_naked_cover f_sad_talk_closed
    with dissolve
    player_name "Ты в порядке?"
    show player 5b
    show daisy a_naked_wiping_tears with dissolve
    daisy "Да."
    show daisy a_naked_shy_front b_naked_shy f_shy_sad_talk at Position (yoffset=10) with dissolve
    daisy "Я просто скучаю по своим цветам..."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Прости, {b}Дейзи{/b}."
    player_name "Могу я тебе что-нибудь предложить?"
    player_name "Мне не нравится видеть тебя такой грустной..."
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Нет, все в порядке."
    show daisy f_shy_sad at Position (yoffset=10)
    pause
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Спасибо, {b}[firstname]{/b}."
    hide daisy with dissolve
    show player 5
    player_name "( Хмм, я должен пойти в магазин {b}Купидон{/b} в {b}торговом центре{/b} и {b}принести ей новые цветы{/b}. )"
    show player 13
    player_name "( Держу пари, это ее подбодрит. )"
    pause
    player_name "( {b}Диана{/b} сказала, что мне нужно поискать {b}Подсолнухи{/b}. )"
    hide player with dissolve
    return

label daisy_button_sleeping:
    show player 434 with dissolve
    player_name "( Ой, посмотри, какая она милая, когда спит! )"
    player_name "( Я должен оставить ее в покое. )"
    hide player with dissolve
    return

label daisy_button_no_veggie_pizza:
    show player 1b
    show daisy f_normal_talk
    daisy "Ты принес мне еще одну {b}вегетарианскую пиццу{/b}?"
    show daisy f_normal
    show player 10b
    player_name "Нет, не сегодня."
    show player 5b
    show daisy f_sad_talk
    daisy "Ауу..."
    show daisy f_sad
    show player 10b
    player_name "Прости, {b}Дейзи{/b}..."
    player_name "... Может быть, завтра, хорошо?"
    show player 5b
    show daisy f_sad_talk
    daisy "Хорошо."
    show daisy f_sad
    return

label daisy_button_has_veggie_pizza:
    show player 14b
    player_name "Я принес тебе кое-что!"
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*вздох*{/b} Подарок?!"
    show daisy f_normal
    player_name "Ммммм."
    show player 239_240 with dissolve
    pause
    show player 719c with dissolve
    show daisy f_normal_talk
    daisy "{b}Вегетарианская пицца{/b}?!"
    show daisy f_normal
    show player 719d
    player_name "Хе-хе, правильно!"
    show player 719c
    show daisy f_laugh
    daisy "Ура!!"
    show daisy f_normal
    show player 721 with dissolve
    pause
    show player 18
    show daisy a_naked_pizza_slice
    with dissolve
    pause
    show daisy f_laugh a_naked_up with dissolve
    daisy "Я люблю пиццу!!"
    show player 17
    player_name "Я тоже!"
    show player 1b
    show daisy a_naked_pizza_eat with dissolve
    pause
    daisy "Ммм!"
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_more_jebadiah_delmont:
    show player 10b
    player_name "Итак, ты думаешь, что готова рассказать мне больше о своем старом хозяине?"
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "Ммм, возможно..."
    daisy "Что ты хочешь знать?"
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "На кого он был похож?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Хм, хозяин был..."
    daisy "... другим, не таким как ты и {b}Диана{/b}."
    daisy "Он не очень ладил с другими людьми, но и не хотел оставаться один."
    daisy "Поэтому он сделал меня."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Он сделал тебя?"
    show player 5b
    daisy "Ммммм."
    show player 10b
    player_name "Как он это сделал?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Я не знаю..."
    show daisy f_normal_talk b_naked a_naked_sides with dissolve
    daisy "... Может, он использовал свою магию?"
    show daisy f_normal
    pause
    show player 14b
    player_name "Так ты действительно видела, как он колдовал?"
    show player 1b
    show daisy f_laugh
    daisy "О да, чудесная магия!"
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "Он мог убрать большой палец или вытащить деньги из-за моего уха, когда захочет!"
    show daisy f_normal
    show player 5b
    player_name "..."
    show daisy f_normal_talk
    daisy "У него было грозовое облако, которое он поймал в ловушку внутри палки!"
    show daisy f_normal
    show player 10b
    player_name "Ааа?"
    show player 5b
    show daisy f_normal_talk
    daisy "Да, если перевернуть его вверх дном, можно услышать, как внутри идет дождь!"
    show daisy f_normal
    player_name "..."
    show daisy f_laugh
    daisy "О, о, о, и у него был стеклянный шар, полный снега с Северного полюса!"
    show daisy f_normal
    show player 10b
    player_name "Дай угадаю, ты должна была встряхнуть его, а потом падал снег?"
    show player 5b
    show daisy f_normal_talk
    daisy "Да!"
    show daisy f_shy_talk
    daisy "Откуда ты это знаешь?!"
    show daisy f_shy
    show player 14b
    player_name "Они называются снежные шары."
    show player 1b
    show daisy f_sad_talk
    daisy "{b}*вздох*{/b} Ты тоже разбираешься в магии?!"
    show daisy f_sad
    show player 10b
    player_name "{b}Дейзи{/b}, Не думаю, что это было волшебство..."
    show player 5b
    show daisy f_normal_talk
    daisy "А что насчет его палочки?!"
    show daisy f_normal
    show player 10b
    player_name "Палочки?"
    show player 5b
    show daisy f_normal_talk
    daisy "Да, он издавал щелкающий звук, а потом огонь извергался из кончика!"
    show daisy f_laugh
    daisy "Это определенно была магия!"
    show daisy f_normal_talk
    daisy "Я видела это."
    show daisy f_normal
    player_name "..."
    return

label daisy_button_milking_business:
    show player 14b
    player_name "Так тебе нравится, когда {b}Диана{/b} доит тебя?"
    show player 1b
    show daisy f_normal_talk
    daisy "О, да!"
    show daisy f_laugh a_naked_up with dissolve
    daisy "Доение заставляет мои сиськи чувствовать себя хорошо!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "К тому же, она намного мягче делает это, чем хозяин..."
    show daisy f_normal
    pause
    show daisy f_normal_talk
    daisy "... Я просто хочу, чтобы это меня не щекотало!"
    show daisy f_normal
    show player 14b
    player_name "Уверена, она придумает, как это сделать, не щекоча тебя."
    show player 1b
    show daisy f_normal_talk
    daisy "Надеюсь."
    daisy "Я хочу, чтобы {b}Диана{/b} тоже продавала мое молоко и делала людей счастливыми!"
    show daisy f_normal
    return

label daisy_button_how_are_your_flowers_2:
    show player 14b
    player_name "Как поживают твои цветы?"
    show player 1b
    show daisy f_normal_talk
    daisy "Они все еще не завяли."
    daisy "Я даю им воду и солнечный свет каждый день, как ты мне сказал."
    show daisy f_normal
    show player 14b
    player_name "Это замечательно, {b}Дейзи{/b}."
    show player 1b
    daisy "Ммммм."
    show daisy f_normal_talk
    daisy "{b}Диана{/b} говорит, что в мире много цветов, и они тоже бывают разных цветов!"
    daisy "Это правда?"
    show daisy f_normal
    show player 14b
    player_name "Да, это правда."
    show player 1b
    show daisy f_laugh a_naked_cover with dissolve
    daisy "Вау!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Надеюсь, когда-нибудь увижу их все..."
    show daisy f_normal
    return

label daisy_button_finished_pizza_intro:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_normal_talk
    daisy "Привет, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Привет, {b}Дейзи{/b}."
    player_name "Как ты себя чувствуешь сегодня?"
    show player 1b
    show daisy f_sad_talk
    daisy "Ммм, мне скучно."
    show daisy f_normal_talk
    daisy "Что ты делаешь?"
    show daisy f_normal
    return

label daisy_button_get_pizza_has_not_pizza:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh
    with dissolve
    daisy "Пицца!"
    daisy "Хехехе!"
    show daisy f_normal
    show player 14b
    player_name "Хех, Она так взволнована."
    player_name "Мне нужно сходить в {b}пиццерию Тони{/b} и купить ей {b}вегетарианскую пиццу{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_get_pizza_has_pizza:
    scene expression player.location.background_blur with None
    show player 719d at left
    show daisy
    with dissolve
    player_name "{b}Дейзи{/b}?"
    player_name "Смотри, что я тебе принес!"
    show player 719c
    show daisy f_laugh
    daisy "Пицца?!"
    show daisy f_normal
    show player 720 with dissolve
    player_name "Ммммм!"
    show daisy f_normal_talk
    daisy "О, как вкусно пахнет!"
    show daisy f_normal
    pause
    show daisy f_sad_talk
    daisy "Как я могу ее съесть?"
    show daisy f_sad
    show player 720b
    player_name "Хе-хе, позволь показать."
    show daisy f_normal
    show player 721 with dissolve
    player_name "Просто держи вот так и начинай есть с этого конца."
    show player 719d with dissolve
    player_name "Ммм, так хорошо!!"
    show player 719c
    pause
    show player 719d
    player_name "Теперь попробуй ты."
    show daisy a_naked_pizza_hold f_normal_talk
    show player 1b
    with dissolve
    daisy "Х-хорошо."
    show daisy a_naked_pizza_slice f_sad_talk with dissolve
    daisy "Вот так?"
    show daisy f_normal
    show player 14b
    player_name "Да, именно так."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*вздох*{/b} Вау!!! Моя первая пицца!"
    show daisy f_normal
    show player 17 with dissolve
    player_name "Хехе!"
    show player 1b
    show daisy a_naked_pizza_eat f_empty with dissolve
    daisy "Ммммммм!!!"
    show player 11
    player_name "!!!" with hpunch
    pause
    daisy "Еще!"
    show player 10b
    player_name "Да, ешь столько, сколько хочешь..."
    hide player
    hide daisy
    with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene13.jpg"
    show expression FilteredText("Пицца прошла даже лучше, чем я ожидал.\nДо сегодняшнего дня я никогда не видел, чтобы кто-нибудь бросался на еду, как {b}Дейзи{/b}.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("{b}Дейзи{/b} слопала восемь штук за то время, что я съел две!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy o_sauce f_burp
    with dissolve
    daisy "{b}*рыыыыыг*{/b}"
    show daisy f_normal
    show player 14b
    player_name "Хех, ты там в порядке?"
    show player 1b
    show daisy f_laugh
    daisy "Это было так вкусно!!"
    show daisy f_normal_talk
    daisy "Могу я есть пиццу каждый день?!"
    show daisy f_normal
    show player 17
    player_name "Ха-ха, Не думаю, что это хорошая идея..."
    show player 1b
    show daisy f_sad_talk
    daisy "О."
    show daisy f_sad
    show player 14b
    player_name "... но я могу приносить тебе ее время от времени."
    show player 1b
    show daisy f_laugh a_naked_up with dissolve
    daisy "Ура!"
    daisy "Я люблю пиццу!"
    show daisy f_normal a_naked_sides with dissolve
    show player 14b
    player_name "Хехе, я тоже!"
    show player 433
    show daisy f_normal_talk
    daisy "Спасибо, {b}[firstname]{/b}!"
    hide player
    show daisy b_naked_hug f_empty a_empty o_empty
    with dissolve
    player_name "Пожалуйста, {b}Дейзи{/b}."
    show daisy f_normal_talk o_sauce b_naked a_naked_sides
    show player 1b at left
    with dissolve
    daisy "Пойду посмотрю, не хочет ли {b}Диана{/b} тоже пиццы!"
    hide daisy with dissolve
    show player 13
    pause
    show player 14
    player_name "Лучше скажи ей поторопиться, осталось всего несколько кусочков!"
    show player 13
    pause
    show player 18
    player_name "( Я действительно рад, что сделал это. )"
    player_name "( {b}Дейзи{/b} такая милая, когда счастлива. )"
    show player 13
    pause
    show player 426
    player_name "( Хорошо, я лучше закончу здесь и займусь садом до того, как закончится день. )"
    hide player with dissolve
    return

label daisy_button_leave:
    show player 14b at left
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    else:
        show daisy f_normal
    player_name "Мне нужно вернуться к работе."
    player_name "Дай мне знать, если тебе что-нибудь понадобится, хорошо?"
    show player 1b
    if not M_daisy.finished_state(S_daisy_get_pizza):
        show daisy f_shy_shy_talk at Position (yoffset=10)
    else:
        show daisy f_normal_talk
    daisy "Хорошо."
    daisy "Пока, {b}[firstname]{/b}."
    hide player
    hide daisy
    with dissolve
    return

label daisy_button_jebadiah_delmont:
    show player 10b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "So your old master doesn't sound like a very nice guy, huh?"
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    daisy "Mmm, he {i}could{/i} be nice... Sometimes."
    daisy "When I was a good girl."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "Oh?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "He would bring me presents and teach me songs."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Well, that doesn't sound so bad..."
    show player 5b
    show daisy f_shy_sad_talk a_naked_shy_cover at Position (yoffset=10) with dissolve
    daisy "As long as I stayed quiet in the shack and didn't touch his things, I was a good girl."
    show daisy f_shy_sad at Position (yoffset=10)
    show player 10b
    player_name "What happened if you left the shack?"
    show player 5b
    show daisy f_shy_sad_talk_closed at Position (yoffset=10)
    daisy "I don't-"
    daisy "H-he would-"
    show daisy b_naked a_naked_cover f_sad_talk_closed with dissolve
    pause
    show player 10b
    player_name "Do you wanna talk about it?"
    show player 5b
    daisy "No, please no!"
    show player 10b
    player_name "It's okay, we don't have to-"
    show player 433
    daisy "No, no, no, no-"
    show player 10b
    player_name "{b}Daisy{/b}, it's okay..."
    player_name "We don't have to talk about him at all if you don't want to."
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*Sniff*{/b} I-I'm a good girl?"
    show daisy f_sad
    show player 14b
    player_name "Of course!"
    show player 10b
    player_name "I didn't mean to upset you, I-"
    show player 5b
    pause
    show player 14b
    player_name "You don't need to worry, {b}Daisy{/b}."
    player_name "{b}Diane{/b} and I would never hurt you."
    show player 1b
    show daisy f_shy_sad_talk a_naked_shy_front b_naked_shy at Position (yoffset=10) with dissolve
    daisy "O-okay."
    show daisy f_shy_sad at Position (yoffset=10)
    return

label daisy_button_about_yourself:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "Tell me about yourself."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Me?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Yeah, I'd like to know more about you."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "I don't-"
    daisy "There's not much-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Is there anything you like?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Umm, flowers?"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Heh, anything besides flowers?"
    show player 1b
    show daisy f_shy_down at Position (yoffset=10)
    daisy "Hmm."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oats!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Oats?"
    show player 5b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Yeah, Master used to feed me oats all the time."
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "It was yummy!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "What's {b}Diane{/b} been feeding you?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, lots of stuff..."
    daisy "She says I should try other things and not just eat oats all the time."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "She's right."
    player_name "What have you tried so far?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Mmm, I've tried lettuce, carrots, bopples, grapes-"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 10b
    player_name "Bopples?"
    player_name "What's a bopple?"
    show player 1b
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Umm, they are red and crunchy and they make my tongue feel funny."
    show daisy f_shy_shy at Position (yoffset=10)
    player_name "Hmm?"
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "{b}Diane{/b} says it's because they are sweet."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Do you mean an apple?"
    show player 1b
    show daisy f_shy_laugh at Position (yoffset=10)
    daisy "Yes, that's it!"
    show daisy f_shy_down_talk at Position (yoffset=10)
    daisy "Apple."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "It was yummy too, but oats are much better!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, okay."
    show player 1b
    return

label daisy_button_how_are_your_flowers_1:
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "How are your flowers?"
    player_name "Have you been watching them closely?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Yes, very closely!"
    daisy "{b}Diane{/b} was right, they do drink the water!"
    daisy "It's so neat!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 17
    player_name "Hehehe."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Do you wanna watch them with me?!"
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Uhh, no... Sorry {b}Daisy{/b}, I have too much work to do around here."
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Oh, okay."
    show daisy f_shy_shy at Position (yoffset=10)
    return

label daisy_button_still_nervous:
    show player 14b
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    player_name "I still make you nervous, huh?"
    show player 1b
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "Y-yeah... A little."
    show daisy f_shy_shy at Position (yoffset=10)
    pause
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "S-sorry."
    show daisy f_shy_shy at Position (yoffset=10)
    show player 14b
    player_name "Heh, you don't need to be sorry."
    player_name "It's okay, I understand."
    show player 1b
    pause
    show player 14b
    player_name "There's no rush."
    show player 1b
    return

label daisy_button_intro_scared:
    scene expression player.location.background_blur with None
    show player 10b at left
    show daisy b_naked_behind_sad f_empty a_empty
    with dissolve
    player_name "Hi there, uhh-"
    show player 11
    show daisy b_jump_scared
    cow "EEEEP!!!" with hpunch
    show daisy b_naked a_naked_cover f_sad_talk_closed
    pause
    show player 24
    dia "{b}[firstname]{/b}!"
    show diane b_naked a_naked_sides f_shamed_talk_smile at Position (xpos=600)
    dia "She's still frightened of you!"
    show diane f_shamed
    show player 25
    player_name "I'm sorry, I didn't mean to scare her."
    show player 24
    show diane f_shamed_talk_smile
    dia "It's alright."
    dia "Just give me a little more time with her, okay?"
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "{b}I'll let you know when she's ready to speak with you.{/b}"
    show diane f_shamed
    show player 25
    player_name "O-okay."
    hide player with dissolve
    return

label daisy_button_intro:
    scene expression player.location.background_blur with None
    show player 14b at left
    show daisy f_shy_shy b_naked_shy a_naked_shy_front at Position (yoffset=10)
    with dissolve
    player_name "Hey, {b}Daisy{/b}."
    show player 1b
    daisy "..."
    show daisy f_shy_shy_talk at Position (yoffset=10)
    daisy "H-hi."
    show daisy f_shy_shy at Position (yoffset=10)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
