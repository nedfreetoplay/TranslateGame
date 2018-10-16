label mia_dialogue_helen_route:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene mia_house_c
    show mia 8 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f at right
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "Ох... привет, {b}[firstname]{/b}."
    show mia 8
    show player 10
    player_name "..."
    show player 11
    pause
    show player 10
    player_name "Ну как у тебя дела?"
    show player 5
    show mia 12
    mia "Я все еще чувствую себя немного расстроеной из за моей семьи которая не вместе."
    show mia 46f
    mia "Я скучаю когда просыпаюсь и вижу своего отца каждое утро."
    mia "И мою{b}Маму{/b} по-видимому более отдаленной в последнее время."
    show mia 45f
    show player 10
    player_name "Хмм..."
    show player 12
    player_name "Хэй, хочешь чем нибудь занятся позже?"
    show player 10
    player_name "Приближается еще одна викторина. Хочешь позаниматься?"
    show player 5
    show mia 46f
    mia "Нет. Мне ничего не хочется делать сейчас."
    show mia 45f
    show player 24
    player_name "..."
    show player 10
    player_name "Что ж, Тогда увидимся позже!"
    show player 5
    mia "..."
    hide player
    hide mia
    hide mial
    with dissolve
    return

label mia_dialogue_helen_change_news:
    if player.location == L_miahouse_miaroom:
        scene mia_bedroom_c
    elif player.location == L_school_scienceclassroom:
        scene school_science_c02
    elif player.location == L_miahouse_entrance:
        scene mia_house_c
    show player 13 at left
    show mia 10 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    mia "Что случилось?"
    show mia 7
    show player 14
    player_name "Я разговаривал с твоей мамой. Я думаю я достучался до неё!"
    show player 13
    show mia 10
    mia "Тебе удалось?!Но как..."
    show mia 7
    show player 17
    player_name "Я знаю, эта длинная история..."
    show player 14
    player_name "...Но все будет в порядке. Я обещаю!"
    player_name "Мы поговорили и она согласилась попытаться что то поменять так что может быть они снова будут вместе!"
    show player 13
    show mia 9
    mia "Это потрясающе!"
    show mia 7
    show player 14
    player_name "Я думаю что она будет более мягкой с тобой тоже..."
    player_name "...Я чувствую что она изменит свое отношение."
    show player 13
    show mia 10
    mia "Вау... Ты должно быть действительно хорошо поработал что бы убедить её!"
    show mia 7
    show player 17
    player_name "У меня есть несколько трюков в рукавах. Ха ха!"
    show player 13
    show mia 10
    mia "Я так счастлива! Спасибо, {b}[firstname]{/b}!"
    show mia 7
    pause
    hide player
    show mia 49 at left
    if player.location == L_school_scienceclassroom:
        show mial 1c
    with dissolve
    player_name "!!!"
    show player 11 at left
    show mia 10 at right
    if player.location == L_school_scienceclassroom:
        show mial 1f
    with dissolve
    mia "Увидимся позже, тогда!"
    show mia 7
    show player 21
    player_name "Пока."
    hide player
    hide mial
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_intro:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Я очень счастлива что ты пришел."
    show mia 7
    show player 14
    player_name "Привет, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Ты хочешь потусоваться?"
    mia "Или ты пришел сюда чтобы попробовать мою новую методику обучения?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_mia_end_study:
    player_name "Хочешь...заниматься сегодня голыми?"
    show player 13
    show mia 10
    mia "Да!"
    mia "Сядь на кровать пока я переоденусь."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_leave:
    show mia 8
    show player 10
    player_name "Я бы с радостью... но уже поздно..."
    show mia 12
    show player 5
    mia "Ох, хорошо..."
    mia "...Ты же  еще вернешься?"
    show player 14
    show mia 8
    player_name "Да. Я посмотрю что смогу сделать!"
    show mia 12
    show player 1
    mia "Спокойно ночи..."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Привет!"
    mia "Я так счастлива что ты смог прийти!"
    show mia 7
    show player 17
    player_name "Все хорошо. Просто показалость что у тебя что-то очень важное о чем ты хотела поговорить."
    show player 14
    player_name "Ты хочешь о чем-то меня спросить?"
    show player 13
    show mia 10
    mia "Ну, это не ТАК уж м важно..."
    mia "...Я надеялась что смогу получить твое мнение кое о чем, и возможно ты смог бы мне помочь."
    show mia 7
    show player 10
    player_name "Эмм... Думаю да. Что такое?"
    show player 11
    show mia 10
    mia "Ты что не будь знаешь об татушках?"
    show mia 7
    show player 10
    player_name "Татушках?!"
    show player 12
    player_name "Почему? Ты захотела сделать одну?"
    show player 11
    show mia 12
    mia "Я знаю это плохо..."
    mia "...Но, Я устала от того что мне приказывают  что  делать!"
    mia "Я прсто хочу сделать что то... спонтанно и повеселиться!"
    mia "Чтобы почувствовать себя свободной..."
    show mia 8
    show player 10
    player_name "С твоя мама нормально к этому отнесется?"
    show player 5
    show mia 12
    mia "Мне уже все равно."
    show mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Татушки это очень круто. Я просто не хочу что бы ты влипла в неприятности."
    show player 13
    show mia 12
    mia "Ты мне поможешь?"
    show mia 8
    show player 14
    player_name "Конечно, но как?"
    show player 13
    show mia 10
    mia "Я знаю что тебе нравится рисовать разные штуки и ты их рисуешь в классе все время, и я видела твои рисунки..."
    mia "...Я надеялась что ты смог бы нарисовать мою татушку!"
    show mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29
    player_name "Ты уверена?"
    show player 13 with dissolve
    show mia 10
    mia "Да! Ты в этом очень хорош."
    show mia 7
    show player 21
    player_name "Спасибо но я не знаю чего ты хочешь!"
    show player 13
    show mia 10
    mia "Хмм... Я хочу что то милое!"
    show mia 9
    mia "С красивыми цветами!"
    show mia 7
    show player 24
    player_name "Что если это будет плохо, и ты возненавидишь это?"
    show player 13
    show mia 10
    mia "Я уверена что это будет отлично!"
    show mia 7
    show player 14
    player_name "Если ты так говоришь..."
    show player 13
    show mia 10
    mia "Приходи ко мне когда у тебя что то будет."
    show mia 7
    show player 14
    player_name "Хорошо."
    show player 13
    show mia 10
    mia "Мне надо идти спать Увидимся в школе!"
    show mia 7
    show player 36 with dissolve
    player_name "Спокойной ночи!"
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_church_plan:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 12 at right
    with dissolve
    player_name "Привет, {b}Mia{/b}."
    player_name "Мне удалось подкрасться и увидеть тебя"
    show player 5
    show mia 10
    mia "Ой, спасибо. Мне очень приятно."
    mia "Как дела?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_intro:
    scene location_mia_bedroom_closeup
    show mia 10 at right
    show player 13 at left with dissolve
    mia "Я очень счастлива что ты пришел!"
    show mia 7
    show player 21
    player_name "Привет, {b}Mia{/b}!"
    show player 29
    player_name "чувствую себя немного странно, прокрадываясь в чужой дом ночью..."
    show mia 9
    show player 13
    mia "Все нормально, мы не доставим проблем..."
    show mia 10
    show player 11
    mia "...Мы просто должны {b}сидеть тихо{/b}!"
    show mia 7
    show player 17
    player_name "Если ты так говоришь.Хаха."
    show mia 12
    show player 1
    return

label mia_dialogue_science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Приветик, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "Как ты?"
    show player 5
    show mia 12
    mia "Я хорошо, но нам вообще то не стоит разговаривать."
    mia "У меня и так достаточно проблем.. Извини."
    show mia 8
    show player 24
    player_name "..."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_consult:
    scene school_science_c02
    show player 1 at left
    show mia 9 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Привет, {b}Mia{/b}!"
    show mia 10
    show player 13
    mia "Я хотела поблагодарить тебя за то что пришел ко мне той ночью..."
    show player 11
    mia "... Мне очень понравилось, но..."
    show mia 7
    player_name "..."
    show mia 8
    show player 10
    player_name "Что то не так?"
    show mia 12
    show player 11
    mia "Ну, моя мама становится подозрительной."
    show mia 8
    show player 10
    player_name "Из-за меня?"
    show mia 12
    show player 5
    mia "Да, Я думаю она знает что ты Приходил."
    show mia 8
    show player 10
    player_name "Неужели это так ужасно?"
    show mia 12
    show player 5
    mia "Она определенно не может смериться с этим."
    show player 11
    mia "Я имею в виду, может быть если бы как то... если бы мой отец был на твоей стороне? Я уверена он бы мог поговорить с ней."
    show mia 8
    show player 10
    player_name "Твой отец? Но как?"
    show mia 7
    player_name "Он выглядит очень строгим!"
    show mia 9
    show player 11
    mia "Да ты что, он большой добряк..."
    show mia 10
    show player 1
    mia "Он может быть очень крутыс, ты знаешь?"
    show mia 7
    show player 14
    player_name "Хорошо, и так как же я могу перетянуть его на свою сторону?"
    show mia 10
    show player 1
    mia "Хмм... Я не уверена..."
    mia "Возможно попытайся узнать что ему нравиться, как коробка с пончиками!"
    show mia 7
    show player 14
    player_name "Пончики?"
    show mia 9
    show player 1
    mia "Ха ха. Я знаю... Так типично. Но, он действительно их очень любит!"
    show mia 8
    show player 14
    player_name "У него есть какие то любимые Пончики?"
    show mia 12
    show player 1
    mia "Ох, Я не уверена..."
    show mia 7
    show player 14
    player_name "Отлично! возможно я смогу выяснить и подарить ему что то."
    show mia 10
    show player 1
    mia "Спасибо! Ты такой милый... Я уверена ему понравится!"
    return

label mia_dialogue_science_classroom_mia_parent_unblock:
    scene school_science_c02
    show player 1 at left
    show mia 9 at right
    show mial 1f at right
    with dissolve
    mia "{b}[firstname]{/b}!"
    show mia 10
    show player 11
    mia "Я не могу в это поверить!"
    show player 14
    show mia 7
    player_name "Хм? Что случилось?"
    show player 1
    show mia 10
    mia "Прошлой ночью, Я слышала что мой отец разговаривал о тебе с моей мамой!"
    show player 14
    show mia 7
    player_name "Обо мне? Серьезно?"
    show player 1
    show mia 9
    mia "Да!"
    show mia 10
    mia "Он говорил как важно заводить друзей в моем возрасте..."
    mia "... Он подумал что надо дать ей возможность посмотреть на тебя, поскольку ты хороший человек и все..."
    show player 14
    show mia 7
    player_name "Woa..."
    player_name "Итак, твоя мама будет хорошо относится ко мне?!"
    show player 11
    show mia 10
    mia "Ну, Она была не слишко удовоетворена этой идеей, это точно!"
    show player 1
    show mia 9
    mia "Но, я думаю это немножко сработало"
    show player 17
    show mia 7
    player_name "Наверное это нечто."
    show player 13
    show mia 10
    mia "Спасибо что поговорил с моим отцом..."
    show player 14
    show mia 7
    player_name "Это ерунда, и видно что твой отец оказался крутым мужиком, вообще-то!"
    show player 1
    show mia 10
    mia "Да... У него большое влияние на нашу жизнь."
    show player 14
    show mia 8
    player_name "Вообщем Мне нужно вернуться в класс-"
    show player 11
    show mia 12
    mia "Подожди!! Я..."
    mia "Я хотела узнать твое мнение о чем то."
    show player 14
    show mia 8
    player_name "О чем то?"
    show player 11
    show mia 12
    mia "Я не чувствую себя спойкойно говоря об этом здесь..."
    show player 13
    mia "Но может быть... ты мог бы прийти сегодня вечером?"
    show player 14
    show mia 7
    player_name "Я бы с радостью!"
    show player 1
    show mia 9
    mia "Мило!"
    show mia 10
    mia "Я буду ждать тебя тогда дома."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_favor:
    scene school_science_c02
    show player 13 at left
    show mia 10 at right
    show mial 1f at right
    with dissolve
    mia "Доброе утро, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Доброе утро, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Я надеялась ты можешь мне помочь с кое чем... еще раз?"
    show mia 7
    show player 14
    player_name "Конечно, {b}Mia{/b}. Я не против!"
    show player 13
    show mia 10
    mia "Я хочу что бы ты применил свою магию и заставил моего отца приглосить мою маму и меня на ужин."
    mia "Он слушает тебя..."
    show mia 7
    show player 14
    player_name "Ужин? Звучит так как будто твои родители снова в хороших отношениях."
    player_name "Я загляну к нему после его работы и и посмотрю что я смогу сделать!"
    show player 13
    show mia 12
    mia "Я ценю твою помощь, {b}[firstname]{/b}. Я просто не знаю что я с собой сделаю если они снова не будут вместе."
    show mia 46f
    mia "Мне кажется что это все моя вина..."
    show mia 45f
    show player 10
    player_name "Ох, Да ладно, {b}Mia{/b}... Ты не должна так думать!"
    show player 14
    player_name "Не волнуйся, я доставлю твоего отца к этому ужину."
    show player 13
    show mia 46f
    mia "Спасибо.. Ты прелесть."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_need_space:
    scene school_science_c02
    show player 10 at left
    show mia 8 at right
    show mial 1f at right
    with dissolve
    player_name "Привет, {b}Mia{/b}..."
    player_name "Как дела?"
    show player 5
    show mia 12
    mia "У меня все хорошо."
    show mia 8
    mia "..."
    show player 3 with dissolve
    player_name "..."
    show mia 12
    mia "Я хочу сейчас побыть одна."
    show mia 8
    show player 10 with dissolve
    player_name "Ладно..."
    player_name "Я поговорю с тобой позже. Просто дай мне знать если тебе что не будь будет нужно, тем не менее."
    show player 5
    show mia 12
    mia "Спасибо, {b}[firstname]{/b}..."
    hide mia
    hide mial
    hide player
    with dissolve
    return

label mia_dialogue_science_classroom_mia_church_plan:
    scene school_science_c02
    show player 12 at left
    show mia 8 at right
    show mial 1f at right
    with dissolve
    player_name "Привет, {b}Mia{/b}!"
    player_name "Как дела?"
    show player 5
    show mia 12
    mia "У меня все хорошо."
    mia "Но бы хотела что бы все вещи вернулись на свои места как было раньше дома."
    show mia 8
    show player 10
    player_name "Извини..."
    show player 5
    show mia 12
    mia "Есть что то о чем ты бы хотел поговорить?"
    show mia 8
    return

label mia_dialogue_science_classroom_mia_urgent_help:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Привет, {b}[firstname]{/b}!"
    mia "Пожалуйста {b}давай встретимся возле дома чуть позже{/b}, хорошо?"
    show mia 8
    show player 10
    player_name "Ладно."
    show player 5
    show mia 12
    mia "Тебе нужно что нибудь еще?"
    show mia 8
    return

label mia_dialogue_science_classroom_intro:
    scene school_science_c02
    show player 14 at left
    show mia 7 at right
    show mial 1f at right
    with dissolve
    player_name "Хэй, {b}Mia{/b}!"
    player_name "Как дела?"
    show player 13
    show mia 10
    mia "У меня все нормально."
    show mia 12
    mia "Действительно с нетерпением жду мой следующий урок."
    show mia 7
    show player 17
    player_name "Да. Я тебя понимаю."
    show player 13
    show mia 10
    mia "Есть ли что то о чем бы ты хотел поговорить?"
    show mia 7
    return

label mia_dialogue_mias_house_entrance_mia_favor:
    scene mia_house_c with fade
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Доброе утро, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Доброе утречко, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Я надеялась ты можешь мне помочь с кое чем... еще раз?"
    show mia 7
    show player 14
    player_name "Конечно, {b}Mia{/b}. Я не против!"
    show player 13
    show mia 10
    mia "Я хочу что бы ты применил свою магию и заставил моего отца приглосить мою маму и меня на ужин."
    mia "Он слушает тебя..."
    show mia 7
    show player 14
    player_name "Ужин? Звучит так как будто твои родители снова в хороших отношениях."
    player_name "Я загляну к нему после его работы и и посмотрю что я смогу сделать!"
    show player 13
    show mia 12
    mia "Я ценю твою помощь, {b}[firstname]{/b}. Я просто не знаю что я с собой сделаю если они снова не будут вместе."
    show mia 46f
    mia "Мне кажется что это все моя вина..."
    show mia 45f
    show player 10
    player_name "Ох, Да ладно, {b}Mia{/b}... Ты не должна так думать!"
    show player 14
    player_name "Не волнуйся, я доставлю твоего отца к этому ужину."
    show player 13
    show mia 46f
    mia "Спасибо.. Ты прелесть."
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_helen_talk:
    scene mia_house_c
    show player 5 at left
    show mia 12 at right
    with dissolve
    mia "Можешь поговорить с моей мамой Она в {b}в своей комнате на 2-ом этаже{/b}..."
    show player 10
    show mia 8
    player_name "я попытаюсь, {b}Mia{/b}."
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_church_plan:
    scene mia_house_c
    show player 13 at left
    show mia 12 at right
    with dissolve
    mia "Приветик, {b}[firstname]{/b}."
    show player 5
    pause
    show player 10
    show mia 8
    player_name "Привет, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "Как дела?"
    show mia 8
    return

label mia_dialogue_mias_house_entrance_intro:
    scene mia_house_c
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Приветик, {b}[firstname]{/b}."
    show player 14
    show mia 7
    player_name "Привет, {b}Mia{/b}."
    show player 13
    show mia 10
    mia "Как дела?"
    show mia 7
    return

label mia_dialogue_chat:
    show mia 7
    show player 2
    player_name "Конечно!"
    show player 10
    player_name "Эмм.. Ты не обязана на это отвечать, но..."
    show mia 8
    player_name "Тебе не кажется странном что твои родители не разрешают тебе заводить друзей?"
    show player 5
    mia "..."
    show mia 12
    mia "Просто.. так оно и есть с моей мамой."
    show mia 8
    show player 12
    player_name "И ты не возражаешь??"
    show player 11
    show mia 12
    mia "Она просто обо мне беспокоится!"
    mia "Я знаю она очень меня любит, и хочет только лучшего для меня..."
    show mia 8
    show player 12
    player_name "Но ты можешь встречаться с друзьями в тайне..."
    show mia 12
    show player 5
    mia "Я знаю.. но она не поняла бы."
    show mia 8
    show player 24
    player_name "Я вижу.."
    show player 21
    player_name "Лишь бы ты была счастлива?"
    show mia 9
    show player 13
    mia "Ага!"
    return

label mia_dialogue_talent_show_help:
    show player 10
    player_name "Ты играешь на каком не будь иснтрументе или поешь?"
    show player 5
    show mia 9
    mia "Да я пою в хоре в церкве все время!"
    show mia 7
    show player 14
    player_name "Ты? Круто!"
    player_name "Ты должна песть в {b}Ms. Dewitt's{/b} шоу талантов!"
    player_name "Нам нужно больше добровольцев."
    show player 13
    show mia 12
    mia "Ох, эмм."
    mia "Я хотела бы но я не могу."
    show mia 8
    show player 10
    player_name "Хмм? Почему нет?"
    show player 5
    show mia 12
    mia "Моя мама даже не позволит мне участвовать на на шоу талантов."
    show mia 8
    show player 12
    player_name "Почему?"
    show player 5
    show mia 12
    mia "Она не хочет что бы я слушала рок или рэп музыку..."
    mia "Она боится что это осквернит мои молодые мозги или что то вроде этого."
    show mia 8
    show player 12
    player_name "Это дерьмово!"
    show player 5
    show mia 12
    mia "Да. Извини."
    show player 10
    player_name "Все в порядке, {b}Mia{/b}. Все равно спасибо!"
    return

label mia_dialogue_parents:
    show player 14
    player_name "И так, Как поживают твои родители?"
    show player 13
    show mia 10
    mia "Заняты. Моя мама всегда в церкви и мой папа всегда работает."
    show mia 12
    mia "Вероятно это к лучшему."
    show mia 8
    show player 10
    player_name "Как так?"
    show player 11
    show mia 12
    mia "Когда мои родители собираются вместе они все время только и ругаются."
    show player 5
    mia "Я так сильно это ненавижу."
    mia "Я хотела бы что бы они побольше ладили, как раньше..."
    show mia 8
    show player 10
    player_name "Я не знал что такое происходит. Они казались в порядке."
    show player 5
    show mia 12
    mia "Да, моя мама может подлить масло в огонь."
    mia "Она очень жестокая и не принимает отказова."
    mia "Так что {b}Папа{/b}просто делает что она скажет..."
    show mia 8
    show player 10
    player_name "Это отстойно."
    show player 5
    show mia 12
    mia "Она начала заставлять  меня учить библию с недавних пор..."
    mia "...И сказала что я должна  встречаться с парнем только из церкви когда я буду готова."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "Я знаю,это.. странно."
    show mia 9
    mia "Тем не менее! Давай поговорим о чем то другом."
    show mia 7
    show player 13
    return

label mia_dialogue_mia_clues:
    show player 10
    player_name "Где ты сказала я смогу найти информацию о судьбе{b}Harold's{/b}?"
    show player 5
    show mia 12
    mia "Начни опрашивать его коллег в {b}полицейском участке{/b}..."
    mia "...и ищи {b}подсказки{/b} во круг его рабочего места."
    show mia 8
    show player 12
    player_name "Наверно я смогу поспрашивать там поблизости что бы выяснить где он может быть..."
    show player 5
    show mia 12
    mia "Спасибо..."
    return

label mia_dialogue_mia_convince_harold:
    show player 10
    player_name "Что я должен заставить твоего отца зделать снова?"
    show player 13
    show mia 10
    mia "Я хочу что бы ты приглосил его на ужин с моей мамой и со мной."
    mia "Вы оба очень хорошо ладите вместе. Может быть ты сможешь воспользоватся его помошью если понадобится."
    show mia 7
    show player 14
    player_name "Конечно! Я присоеденюсь к нему в {b}полицейском участке{/b}."
    show player 13
    show mia 10
    mia "Спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_glasses:
    show player 12
    player_name "Что ты хочешь что бы я сделал с этими очками снова"
    show player 5
    show mia 10
    mia "Ох, я надеялась ты сможешь их подбросить на работу моему отцу"
    show mia 7
    show player 14
    player_name "Тончно... Я вспомнил."
    player_name "Я займусь этим, тогда!"
    return

label mia_dialogue_donuts:
    show player 14 at left
    show mia 7 at right
    player_name "Без понятия как я могу найти пончики которые нравятся твоему отцу?"
    show player 1
    show mia 10
    mia "Ох, эмммм..."
    mia "Может быть поспрашиваешь его коллег возле его работа?"
    mia "Они все там любят есть пончики..."
    show mia 7
    show player 17
    player_name "Ха ха может быть ты права, это может сработать."
    show mia 10
    show player 1
    mia "Хочешь еще о чем не будь поговорить?"
    show mia 7
    show player 1
    return

label mia_dialogue_mia_draw_tattoo:
    show mia 7 at right
    show player 10 at left
    player_name "Об тату арте который ты хотела..."
    show player 5
    show mia 10
    mia "Ох! Он у тебя?!"
    show mia 7
    show player 10
    player_name "Нет, еще нет."
    player_name "Но,что ты хотела еще раз?"
    show player 5
    show mia 10
    mia "Хмм... Что то милое и разноцветное!"
    show mia 7
    show player 17
    player_name "Ха ха, Понятно."
    show player 14
    player_name "Я посмотрю что я смогу сдлеать."
    show player 13
    show mia 9
    mia "Большое спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_fail:
    show mia 7 at right
    show player 2 at left
    player_name "О тату рисунке что ты хотела..."
    show player 13
    show mia 10
    mia "Ох! он у тебя!"
    show mia 7
    show player 14
    player_name "Ага!"
    show player 239_240 with dissolve
    player_name "Мне потребовалось время что бы нарисовать его..."
    show player 386 with dissolve
    player_name "Вот оно!"
    show player 13
    show mia 32
    if player.location == L_school_scienceclassroom:
        show mial 1b
    with dissolve
    mia "Хммм..."
    show player 10
    player_name "Что то не так?"
    show player 11
    show mia 33
    mia "Ну, Я надеялась на что то другое."
    show mia 34
    show player 25
    player_name "Ох..."
    show player 24
    show mia 30
    mia "Мне нравится это!!"
    show mia 33
    mia "Но может быть ты можешь попробовать что то еще?"
    show mia 34
    show player 10
    player_name "Как что?"
    show player 5
    show mia 30
    mia "Попробуй что небудь симпотичное, с яркими цветами!"
    show mia 31
    show player 14
    player_name "Понятно, Я постараюсь нарисовать что то еще..."
    show player 13
    show mia 30
    mia "TСпасибо большое, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_pass:
    show mia 7 at right
    show player 2 at left
    player_name "О тату арте который ты хотела..."
    show player 13
    show mia 10
    mia "Ох! он у тебя?!"
    show mia 7
    show player 14
    player_name "Ага!"
    show player 239_240 with dissolve
    player_name "Мне потребовалось время что бы нарисовать его..."
    show player 386 with dissolve
    player_name "Вот оно!"
    show player 13
    show mia 29
    if player.location == L_school_scienceclassroom:
        show mial 1b at right
    with dissolve
    mia "ВАУ!!!"
    show mia 30
    mia "Я просто влюбилась в неё!"
    show mia 31
    show player 17
    player_name "Серьезно?"
    show player 18
    show mia 30
    mia "Да!"
    show mia 29
    mia "Это так красиво..."
    show mia 31
    show player 14
    player_name "Круто! Я рад что тебе понравилось."
    show player 13
    show mia 30
    mia "Нам нужно съездить в {b}Sugar Tats{/b} и увидеть если они смогут сделать это для меня."
    show mia 7
    if player.location == L_school_scienceclassroom:
        show mial 1f
    with dissolve
    show player 12
    player_name "Сейчас?!"
    show player 5
    show mia 9
    mia "Не сейчас, дурачок!"
    show mia 10
    mia "Как насчет {b}Субботы{/b}?"
    show mia 7
    show player 10
    player_name "Хорошо, Я встречу тебя там  в {b}Субботу{/b}."
    show player 5
    show mia 10
    mia "Пообещай что встретишь меня там {b}в течении дня{/b}!"
    show mia 7
    show player 14
    player_name "Я обещаю!"
    show player 13
    show mia 10
    mia "Хорошо отлично. Я не уверена что смогу это сделать в одиночку, ха ха."
    mia "Увидимся тогда."
    hide player
    hide mia
    hide mial
    with dissolve
    return

label mia_dialogue_mia_get_tattoo:
    show mia 7 at right
    show player 12 at left
    player_name "Об татушке..."
    show player 5
    show mia 12
    mia "Ты все ещё собираешся прийти?"
    show mia 8
    show player 14
    player_name "Конечно!"
    show player 10
    player_name "Но когда ты хочешь пойти?"
    show player 11
    show mia 12
    mia "Ты уже забыл?!"
    show mia 8
    show player 21
    player_name "Я думаю у меня просто слишком много всего в голове..."
    show player 13
    show mia 9
    mia "Все хорошо, ха ха."
    show mia 10
    mia "Мне нужно что бы ты меня встретил в {b}Субботу{/b} в {b}тату-салоне{/b}, {b}в течении дня{/b}!"
    show mia 7
    show player 14
    player_name "Отлично, я обязательно буду там с тобой."
    show player 13
    show mia 10
    mia "Большое спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_church:
    show player 12
    player_name "Когда твоя мама идет в церковь?"
    show player 5
    show mia 12
    mia "На{b}выходных рано утром{/b}."
    show mia 8
    show player 34
    player_name "Хммм..."
    show player 14
    player_name "Хорошо, спасибо."
    show player 13
    show mia 12
    mia "Что ты собираешся делать?!"
    show mia 8
    show player 12
    player_name "Я не совсем уверен, но мы к этому еще вернемся."
    show player 13
    show mia 12
    mia "Хорошо..."
    return

label mia_dialogue_art_sessions_intro:
    show player 10
    player_name "Хэй, так ну ... {b}Miss Ross{/b} попросила меня что бы я поговорил с тобой."
    show player 11
    show mia 10
    mia "Серьезно?"
    show player 10
    show mia 7
    player_name "Да, Она хочет что бы ты была моим партнером для некоторых частных занятий."
    return

label mia_dialogue_art_sessions_stat_pass:
    show player 10
    player_name "Я действительно хочу что бы ты  пришла помочь, {b}Mia{/b}."
    show player 5
    show mia 12
    mia "Ты бы хотел?"
    show mia 8
    show player 29 with dissolve
    player_name "Полностью."
    show player 3
    show mia 8b
    mia "Хммм.."
    show mia 9
    mia "Хорошо!"
    show player 13 with dissolve
    show mia 10
    mia "Я прийду для тебя, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Мило,спасибо {b}Mia{/b}!"
    show player 13
    show mia 9
    mia "Хехе, без проблем."
    show mia 7
    show player 14
    player_name "Что ж, Увидимся там?"
    show player 13
    show mia 10
    mia "Еще бы!"
    return

label mia_dialogue_art_sessions_stat_fail:
    player_name "[chr_warn]Она довольна неприклонна она должна быть тобой."
    show player 11
    show mia 12
    mia "[chr_warn]... Но я не очень хороша в арте."
    show player 10
    show mia 8
    player_name "[chr_warn]Ты не можешь быть настолько плоха..."
    show player 11
    show mia 12
    mia "[chr_warn]Верь мне, Я очень плоха!"
    mia "[chr_warn]Тебе нужно найти когото другого."
    mia "[chr_warn]К тому же, моя мама просто скажет нет"
    show player 10
    show mia 8
    player_name "[chr_warn]Ох, Хорошо тогда."
    return

label mia_dialogue_homework_want_parents_back:
    show player 14
    player_name "Ты хочешь позаниматься вместе?"
    show player 13
    show mia 12
    mia "Я не в настроении этим сейчас заниматься."
    show mia 8
    show player 10
    player_name "Хорошо..."
    show player 5
    show mia 12
    mia "Извини."
    mia "Я просто хочу что бы мои родители снова были вместе."
    show mia 8
    show player 10
    player_name "Я знаю."
    player_name "Дай мне знать если тебе понадобится моя помощь."
    show player 5
    show mia 12
    mia "Спасибо, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_homework_intro:
    show player 14
    player_name "Ты хочешь позаниматься вместе?"
    show player 13
    show mia 10
    mia "Мы будем заниматься этими вещами на последней {b}Французкой домашней работе{/b}. Ты уже отдал свое задание?"
    show mia 7
    return

label mia_dialogue_homework_still_busy:
    show player 24
    player_name "Нет. Она еще в процессе."
    show player 13
    show mia 10
    mia "Что ж как только ты её сделаешь, {b}подходи ко мне домой{/b}."
    hide mia
    hide mial
    with dissolve
    show player 5 with dissolve
    player_name "( Я должен постараться и закончить мою {b}Французкую домашку{/b}, и я смогу позаниматься вместе с {b}Mia{/b}. )"
    show player 4 with dissolve
    pause
    player_name "( Интересно почему она выбрала именно меня помочь с ее подготовкой. )"
    player_name "( Она обычно занималась с {b}Judith{/b} и онаочешь хороша во французком... )"
    player_name "( ...Я не уверен как я могу помочь ей. )"
    show player 13 with dissolve
    player_name "( По крайней мере мы сможем потусить, и она действительно така милашка... )"
    hide player with dissolve
    return

label mia_dialogue_homework_study:
    show player 14
    player_name "Я вернулся совсем не давно."
    show player 13
    show mia 10
    mia "Когда у тебя будет время, {b}прокрадись в мою команту{/b} вечерком и тогда мы сможем позаниматься."
    show mia 7
    show player 17
    player_name "Сделаю!"
    show player 13
    return

label mia_dialogue_study_repeat:
    show player 14
    player_name "Коенечно!"
    scene mia_bedroom_closeup
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Спасибо что прокрался еще раз."
    show mia 13
    show player 142
    player_name "Это не слишком сложно когда твои предки приклеены к ТВ."
    show player 143
    show mia 16
    mia "Да, эта единственная вешь что удерживает их от криков на друг друга."
    mia "Они очень любят смотреть повторы."
    mia "Я иногда смотрю вместе с ними когда когда я закончила свою домашку."
    show mia 22
    mia "Чаще всего я отстаюсь здесь... здесь спокойнее."
    show mia 14
    show player 146
    player_name "Это отстойно что твои родители не ладят."
    show player 141
    show mia 18
    mia "...Да."
    mia "Может быть все вернется в порядок как прежде."
    show mia 14
    pause
    show mia 16
    mia "Тебе лучше уйти до того как мои родители заметят тебя."
    show mia 13
    show player 142
    player_name "Я снова зайду, хорошо?"
    show player 141
    show mia 15
    mia "Отлично! Спокойной Ночи {b}[firstname]{/b}!"
    show mia 13
    show player 142
    player_name "Спкойоной ночи, {b}Mia{/b}."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_study_first:
    show mia 7
    show player 21
    player_name "Я думаю нам нужно позаниматься?"
    show mia 9
    show player 13
    mia "Конечно!"
    show mia 10
    mia "Давай сделаем это, тогда."
    show player 11
    mia "Дай мне достать все учебники и подготовить их на {b}моей кравати{/b}?"
    show mia 7
    show player 21
    player_name "Эм... хорошо!"
    return

label mia_dialogue_study_want_parents_back:
    show player 12
    player_name "Хочешь позаниматься вместе?"
    show player 5
    show mia 12
    mia "Я не очень хорошо себя чувствую что бы заниматься этим в данный момент"
    show mia 8
    show player 10
    player_name "Хорошо..."
    show player 5
    show mia 12
    mia "Извини."
    mia "Я просто хочу чтобы мои родители снова были вместе."
    show mia 8
    show player 10
    player_name "Я знаю."
    player_name "Только дай мне знать если тебе понадобится моя помощь."
    show player 5
    show mia 12
    mia "Спасибо, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_mias_bedroom_leave:
    show mia 8
    show player 10
    player_name "Я бы с удовольствие... но уже поздно..."
    show mia 12
    show player 5
    mia "Ох, хорошо..."
    mia "...Ты скоро вернешься?"
    show player 14
    show mia 8
    player_name "Да. Я посмотрю что я смогу сделать!"
    show mia 12
    show player 1
    mia "Спокойной Ночи..."
    return

label mia_dialogue_science_classroom_leave:
    show player 10
    player_name "Вообще-то, я бы лучше вернулся в класс."
    show player 5
    show mia 12
    mia "ох, хорошо... поговорими с тобой попозже тогда!"
    show mia 8
    show player 14
    player_name "Увидимся!"
    return

label mia_dialogue_mias_house_entrance_leave:
    show player 10
    player_name "Вообще-то, Я вспомнил что у меня было что то что я должен был сделать."
    show player 5
    show mia 12
    mia "ох, хорошо... оговорими с тобой попозже тогда!"
    show mia 8
    show player 14
    player_name "Увидимся!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
