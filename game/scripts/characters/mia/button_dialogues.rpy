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
    player_name "Привет, {b}Мия{/b}."
    show player 5
    show mia 12
    mia "Ох... Привет, {b}[firstname]{/b}."
    show mia 8
    show player 10
    player_name "..."
    show player 11
    pause
    show player 10
    player_name "Итак, как у тебя дела?"
    show player 5
    show mia 12
    mia "Мне все ещё немного грустно из-за того, что моя семья не вместе."
    show mia 46f
    mia "Я скучаю по пробуждению и встречам с отцом каждое утро."
    mia "И {b}мама{/b} в последнее время кажется более отстраненной."
    show mia 45f
    show player 10
    player_name "Хех..."
    show player 12
    player_name "Эй, хочешь сделать что-нибудь позже?"
    show player 10
    player_name "Скоро будет еще один тест. Хочешь заняться учёбой?"
    show player 5
    show mia 46f
    mia "Нет. Мне сейчас не хочется ничего делать."
    show mia 45f
    show player 24
    player_name "..."
    show player 10
    player_name "Хорошо, тогда я догоню тебя позже!"
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
    player_name "Я разговаривал с твоей мамой. Я думаю, что достучался до нее!"
    show player 13
    show mia 10
    mia "Ты сделал это?! Но как..."
    show mia 7
    show player 17
    player_name "Я знаю, это длинная история..."
    show player 14
    player_name "...Но все будет в порядке. Я обещаю!"
    player_name "Мы поговорили, и она согласилась попробовать все изменить, чтобы они снова были вместе!"
    show player 13
    show mia 9
    mia "Это потрясающе!"
    show mia 7
    show player 14
    player_name "Я думаю, она будет более снисходительна и к тебе..."
    player_name "...Я чувствую, что она изменит свое отношение."
    show player 13
    show mia 10
    mia "Вау... Ты, должно быть, очень старался убедить её!"
    show mia 7
    show player 17
    player_name "У меня есть пара трюков в рукаве. Ха-ха!"
    show player 13
    show mia 10
    mia "Я так счастлива! Спасибо тебе, {b}[firstname]{/b}!"
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
    mia "Тогда увидимся позже!"
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
    mia "Я так рада, что ты пришел."
    show mia 7
    show player 14
    player_name "Привет, {b}Мия{/b}."
    show player 13
    show mia 10
    mia "Так ты хочешь болтаться?"
    mia "Или ты здесь, чтобы попробовать мою новую методику обучения?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_mia_end_study:
    player_name "Хочешь...снова учиться голышом?"
    show player 13
    show mia 10
    mia "Да!"
    mia "Сядь на кровать, пока я переоденусь."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_end_leave:
    show mia 8
    show player 10
    player_name "С удовольствием... Но уже поздно..."
    show mia 12
    show player 5
    mia "О, хорошо...."
    mia "...Ты скоро вернешься?"
    show player 14
    show mia 8
    player_name "Да. Посмотрим, что я смогу сделать!"
    show mia 12
    show player 1
    mia "Спокойной ночи..."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_mia_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show mia 10 at right
    with dissolve
    mia "Эй!"
    mia "Я так рада, что ты смог прийти!"
    show mia 7
    show player 17
    player_name "Все нормально. Просто мне показалось, что тебе нужно поговорить о чем-то важном."
    show player 14
    player_name "Ты хотела меня о чем-то спросить?"
    show player 13
    show mia 10
    mia "Ну, это не так уж и важно..."
    mia "...Я надеялся узнать твое мнение о чем-нибудь, и, может, ты мне поможешь."
    show mia 7
    show player 10
    player_name "Ох... Думаю, да. В чем заключается дело?"
    show player 11
    show mia 10
    mia "Ты знаешь что-нибудь о татуировках?"
    show mia 7
    show player 10
    player_name "Татуировках?!"
    show player 12
    player_name "Зачем? Ты думаешь о её нанесении?"
    show player 11
    show mia 12
    mia "Я знаю, что это плохо..."
    mia "...Но, я устала от того, что мне говорят, что делать!"
    mia "Мне просто хочется что-то сделать... спонтанно и весело!"
    mia "Не стесняться..."
    show mia 8
    show player 10
    player_name "Твоя мама не будет возражать?"
    show player 5
    show mia 12
    mia "Меня это больше не волнует."
    show mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Татуировки довольно крутые. Я просто не хочу, чтобы у тебя были неприятности."
    show player 13
    show mia 12
    mia "Ты собираешься мне помочь?"
    show mia 8
    show player 14
    player_name "Конечно, но как?"
    show player 13
    show mia 10
    mia "Я знаю, ты любишь рисовать в классе все время, и я видела твое искусство..."
    mia "...Я надеялась, ты нарисуешь что-нибудь для моей татуировки!"
    show mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29
    player_name "Ты уверена?"
    show player 13 with dissolve
    show mia 10
    mia "Да! У тебя хорошо получается."
    show mia 7
    show player 21
    player_name "Спасибо, но я даже не знаю, чего ты хочешь!"
    show player 13
    show mia 10
    mia "Хм... Я хочу что-нибудь милое!"
    show mia 9
    mia "С красивыми цветами!"
    show mia 7
    show player 24
    player_name "Что, если будет плохо, и ты в конечном итоге буедшь ненавидить её?"
    show player 13
    show mia 10
    mia "Я уверена, что все будет хорошо!"
    show mia 7
    show player 14
    player_name "Если ты так говоришь..."
    show player 13
    show mia 10
    mia "Приходи ко мне, когда у тебя что-нибудь будет."
    show mia 7
    show player 14
    player_name "Хорошо."
    show player 13
    show mia 10
    mia "Мне нужно идти спать. Увидимся в школе!"
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
    player_name "Привет, {b}Мия{/b}."
    player_name "Думал подкрасться и увидеть тебя."
    show player 5
    show mia 10
    mia "Спасибо. Я ценю это."
    mia "В чем дело?"
    show mia 7
    return

label mia_dialogue_mia_bedroom_intro:
    scene location_mia_bedroom_closeup
    show mia 10 at right
    show player 13 at left with dissolve
    mia "Я так рада, что ты пришел!"
    show mia 7
    show player 21
    player_name "Привет, {b}Мия{/b}!"
    show player 29
    player_name "Странное, пробирается в чужой дом ночью..."
    show mia 9
    show player 13
    mia "Всё нормально! У нас не будет неприятностей..."
    show mia 10
    show player 11
    mia "...Мы просто должны {b}молчать{/b}!"
    show mia 7
    show player 17
    player_name "Если ты так говоришь. Хаха."
    show mia 12
    show player 1
    return

label mia_dialogue_science_classroom_mia_strip_aftermath:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Привет, {b}[firstname]{/b}..."
    show mia 8
    show player 10
    player_name "Как поживаешь?"
    show player 5
    show mia 12
    mia "Я в порядке, но нам не стоит разговаривать."
    mia "У меня и так достаточно неприятностей... Прости."
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
    player_name "Привет, {b}Мия{/b}!"
    show mia 10
    show player 13
    mia "Я хотела поблагодарить тебя за то, что пришли навестить меня той ночью..."
    show player 11
    mia "... Мне очень понравилось, но..."
    show mia 7
    player_name "..."
    show mia 8
    show player 10
    player_name "Что-то не так?"
    show mia 12
    show player 11
    mia "Моя мама начинает что-то подозревать."
    show mia 8
    show player 10
    player_name "Меня?"
    show mia 12
    show player 5
    mia "Да, я думаю, она знает, что ты приходил."
    show mia 8
    show player 10
    player_name "Неужели это действительно большая проблема?"
    show mia 12
    show player 5
    mia "Она определенно не в порядке."
    show player 11
    mia "Я имею в виду, может быть, если так или иначе ... ты попал на сторону моего отца? Я уверена, что он мог бы поговорить с ней."
    show mia 8
    show player 10
    player_name "Твой отец? Но как?"
    show mia 7
    player_name "Он кажется довольно строгим!"
    show mia 9
    show player 11
    mia "Это не так, он очень мягкий..."
    show mia 10
    show player 1
    mia "Он был действительно клевым, понимаешь?"
    show mia 7
    show player 14
    player_name "Хорошо, так как я могу попасть на его хорошую сторону?"
    show mia 10
    show player 1
    mia "Хм... Я не уверена..."
    mia "Может быть, попытаться дать ему то, что он любит, как коробка пончиков!"
    show mia 7
    show player 14
    player_name "Пончики?"
    show mia 9
    show player 1
    mia "Ха-ха. Я знаю... Так типично. Но, он действительно любит их!"
    show mia 8
    show player 14
    player_name "У него есть любимый вид пончика?"
    show mia 12
    show player 1
    mia "О, я не совсем уверена..."
    show mia 7
    show player 14
    player_name "Хорошо! Может быть, я могу узнать об этом у кого-нибудь."
    show mia 10
    show player 1
    mia "Спасибо! Ты такой милый... Я уверена, что ему понравиться!"
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
    mia "Ты не поверишь!"
    show player 14
    show mia 7
    player_name "Да? Что случилось?"
    show player 1
    show mia 10
    mia "Прошлой ночью, я слышала, как мой отец говорил о тебе с моей мамой!"
    show player 14
    show mia 7
    player_name "Обо мне? Серьёзно?"
    show player 1
    show mia 9
    mia "Да!"
    show mia 10
    mia "Он говорил, как важно получуть друзей в моём возрасте..."
    mia "... он думает, что она должна позволить мне видеть тебя, так как ты хороший человек, и все..."
    show player 14
    show mia 7
    player_name "Вау..."
    player_name "Итак, твоя мама сейчас крута?"
    show player 11
    show mia 10
    mia "Ну, она не была слишком довольна идеей, это точно!"
    show player 1
    show mia 9
    mia "Но, я думаю, это, возможно, немного сработало."
    show player 17
    show mia 7
    player_name "Ну хоть что-то."
    show player 13
    show mia 10
    mia "Спасибо за разговор с моим отцом..."
    show player 14
    show mia 7
    player_name "Это неважно, и твой папа действительно похож на классного парня!"
    show player 1
    show mia 10
    mia "Да ... У него было больше слов в нашей жизни."
    show player 14
    show mia 8
    player_name "Во всяком случае, я должен вернуться к классу-"
    show player 11
    show mia 12
    mia "Подожди!! Я..."
    mia "Я хотела узнать твое мнение о кое чём."
    show player 14
    show mia 8
    player_name "О чём именно?"
    show player 11
    show mia 12
    mia "Я действительно не чувствую себя комфортно говорить об этом здесь..."
    show player 13
    mia "Но, может быть, ты может зайдёшь ко мне сегодня вечером?"
    show player 14
    show mia 7
    player_name "Мне бы хотелось!"
    show player 1
    show mia 9
    mia "Сладенький!"
    show mia 10
    mia "Тогда я буду ждать тебя дома."
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
    player_name "Доброе утро, {b}Мия{/b}."
    show player 13
    show mia 10
    mia "Я надеюсь, что ты мог бы помочь мне с кое чем..."
    show mia 7
    show player 14
    player_name "Конечно, {b}Мия{/b}. Я не против!"
    show player 13
    show mia 10
    mia "Я хочу, чтобы ты поработал над своей магией и заставил моего папу выйти на ужин с моей мамой и мной."
    mia "Он слушает тебя..."
    show mia 7
    show player 14
    player_name "Ужин? Похоже, что твои родители снова на товарных условиях."
    player_name "Я останавлюсь на его работе и посмотрю, что я могу сделать!"
    show player 13
    show mia 12
    mia "Я ценю твою помощь, {b}[firstname]{/b}. Я просто не знаю, что я сделаю с собой, если они не вернутся вместе."
    show mia 46f
    mia "Я чувствую, что все это моя вина..."
    show mia 45f
    show player 10
    player_name "Ой, да ладно, {b}Миа{/b}... Ты не можешь так думать!"
    show player 14
    player_name "Не волнуйся, я отведу твоего отца к этому свиданию с ужином."
    show player 13
    show mia 46f
    mia "Спасибо... Ты милый."
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
    player_name "Эй, {b}Мия{/b}..."
    player_name "Как твои дела?"
    show player 5
    show mia 12
    mia "У меня всё хорошо."
    show mia 8
    mia "..."
    show player 3 with dissolve
    player_name "..."
    show mia 12
    mia "Я думаю, я просто хочу немного пространства прямо сейчас."
    show mia 8
    show player 10 with dissolve
    player_name "Хорошо..."
    player_name "Я поговорю с тобой позже. Просто дай мне знать, если тебе что-то нужно, хотя."
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
    player_name "Привет, {b}Мия{/b}!"
    player_name "Как твои дела?"
    show player 5
    show mia 12
    mia "Я в порядке."
    mia "Но я хочу, чтобы все могло вернуться к тому, как они были дома."
    show mia 8
    show player 10
    player_name "Прости..."
    show player 5
    show mia 12
    mia "Есть что-то, о чем ты хотел поговорить?"
    show mia 8
    return

label mia_dialogue_science_classroom_mia_urgent_help:
    scene school_science_c02
    show player 5 at left
    show mia 12 at right
    show mial 1f at right
    with dissolve
    mia "Привет, {b}[firstname]{/b}!"
    mia "Пожалуйста, {b}Остановись у моего дома сегодня позже{/b}, хорошо?"
    show mia 8
    show player 10
    player_name "Хорошо."
    show player 5
    show mia 12
    mia "Что-нибудь ещё нужно?"
    show mia 8
    return

label mia_dialogue_science_classroom_intro:
    scene school_science_c02
    show player 14 at left
    show mia 7 at right
    show mial 1f at right
    with dissolve
    player_name "Эй, {b}Мия{/b}!"
    player_name "Как поживаешь?"
    show player 13
    show mia 10
    mia "У меня все в порядке."
    show mia 12
    mia "Не с нетерпением жду следующего занятия."
    show mia 7
    show player 17
    player_name "Да. Я слышу тебя."
    show player 13
    show mia 10
    mia "Ты хочешь о чем-то поговорить?"
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
    player_name "Доброе утро, {b}Мия{/b}."
    show player 13
    show mia 10
    mia "Я надеялась, что ты мне поможешь кое с чем...еще раз?"
    show mia 7
    show player 14
    player_name "Конечно, {b}Мия{/b}. Я не возражаю!"
    show player 13
    show mia 10
    mia "Я хочу, чтобы ты использовала свою магию и пригласил моего отца на ужин со мной и моей мамой."
    mia "Он прислушивается к тебе..."
    show mia 7
    show player 14
    player_name "Ужин? Похоже, твои родители снова в хороших отношениях."
    player_name "Я зайду к нему на работу и посмотрю, что можно сделать!"
    show player 13
    show mia 12
    mia "Я ценю твою помощь, {b}[firstname]{/b}. Я просто не знаю, что бы я сделала с собой, если бы они не сошлись."
    show mia 46f
    mia "Я чувствую, что все это моя вина..."
    show mia 45f
    show player 10
    player_name "Да ладно, {b}Мия{/b}... Ты не можешь так думать!"
    show player 14
    player_name "Не волнуйся, я приглашу твоего отца на ужин."
    show player 13
    show mia 46f
    mia "Благодаря... Ты такой милый."
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_helen_talk:
    scene mia_house_c
    show player 5 at left
    show mia 12 at right
    with dissolve
    mia "Ты можешь поговорить с моей мамой? Она в {b}своей комнате наверху{/b}..."
    show player 10
    show mia 8
    player_name "Я попробую, {b}Мия{/b}."
    hide mia
    hide player
    with dissolve
    return

label mia_dialogue_mias_house_entrance_mia_church_plan:
    scene mia_house_c
    show player 13 at left
    show mia 12 at right
    with dissolve
    mia "Привет, {b}[firstname]{/b}."
    show player 5
    pause
    show player 10
    show mia 8
    player_name "Привет, {b}Мия{/b}."
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
    mia "Привет, {b}[firstname]{/b}."
    show player 14
    show mia 7
    player_name "Привет, {b}Мия{/b}."
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
    player_name "Ммм... Ты не обязана отвечать на этот вопрос, но..."
    show mia 8
    player_name "Тебе не кажется странным, что твои родители не разрешают тебе приводить друзей?"
    show player 5
    mia "..."
    show mia 12
    mia "Это просто... так оно и есть, с моей мамой."
    show mia 8
    show player 12
    player_name "И ты не возражаешь??"
    show player 11
    show mia 12
    mia "Она просто защищает меня!"
    mia "Я знаю, что она просто любит меня и хочет для меня самого лучшего..."
    show mia 8
    show player 12
    player_name "Но тебе придется тайно встречаться с друзьями..."
    show mia 12
    show player 5
    mia "Я знаю... Но она ничего не поймет."
    show mia 8
    show player 24
    player_name "Я вижу..."
    show player 21
    player_name "До тех пор, пока ты счастлива?"
    show mia 9
    show player 13
    mia "Да!"
    return

label mia_dialogue_talent_show_help:
    show player 10
    player_name "Ты играешь на каких-нибудь инструментах или поёшь?"
    show player 5
    show mia 9
    mia "Да, я постоянно пою в церковном хоре!"
    show mia 7
    show player 14
    player_name "Ты? Потрясающе!"
    player_name "Ты должна петь у {b}Мисс Девитт{/b} на шоу талантов!"
    player_name "Нам действительно нужно больше добровольцев."
    show player 13
    show mia 12
    mia "Ох, ммм."
    mia "Я бы с удовольствием, но не могу."
    show mia 8
    show player 10
    player_name "А? Почему нет?"
    show player 5
    show mia 12
    mia "Моя мама даже не пускает меня на шоу талантов, не говоря уже об участии."
    show mia 8
    show player 12
    player_name "Почему?"
    show player 5
    show mia 12
    mia "Она не хочет, чтобы я слушал рок или рэп..."
    mia "Она боится, что это затемнит мой юный разум или что-то в этом роде."
    show mia 8
    show player 12
    player_name "Вот отстой!"
    show player 5
    show mia 12
    mia "Да. Прости."
    show player 10
    player_name "Все в порядке., {b}Мия{/b}. Спасибо в любом случае!"
    return

label mia_dialogue_parents:
    show player 14
    player_name "Как поживают твои родители?"
    show player 13
    show mia 10
    mia "Заняты. Моя мама всегда в церкви, и папа всегда работает."
    show mia 12
    mia "Наверное, так будет лучше."
    show mia 8
    show player 10
    player_name "Как так?"
    show player 11
    show mia 12
    mia "Когда мои родители собираются вместе, они только спорят."
    show player 5
    mia "Я так сильно это ненавижу."
    mia "Хотел бы я, чтобы они ладили лучше, как раньше..."
    show mia 8
    show player 10
    player_name "Я не знал, что это такое. Они казались нормальными."
    show player 5
    show mia 12
    mia "Да, но моя мама, кажется, больше всего помешивает."
    mia "Она очень тяжелая и не примет \"нет\" в качестве ответа."
    mia "Так что {b}папа{/b} просто повторяет все, что она сейчас говорит..."
    show mia 8
    show player 10
    player_name "Это отстой."
    show player 5
    show mia 12
    mia "Она даже заставляла меня заниматься изучением Библии в последнее время..."
    mia "...И говорит, что я должна встречаться с парнем из церкви, когда буду готова."
    show mia 8
    show player 11
    player_name "..."
    show mia 12
    mia "Я знаю, это... жутко."
    show mia 9
    mia "Все равно! Давайте поговорим о чем-нибудь другом."
    show mia 7
    show player 13
    return

label mia_dialogue_mia_clues:
    show player 10
    player_name "Где, ты сказала, я могу найти подсказки о местонахождении {b}Гарольда{/b}?"
    show player 5
    show mia 12
    mia "Начните с допроса его коллег в {b}полицейском участке{/b}..."
    mia "...И найди {b}руководство{/b} вокруг его рабочего места."
    show mia 8
    show player 12
    player_name "Полагаю, я могу поспрашивать, где он может быть..."
    show player 5
    show mia 12
    mia "Спасибо тебе..."
    return

label mia_dialogue_mia_convince_harold:
    show player 10
    player_name "Что я должен был сделать твоему отцу еще раз?"
    show player 13
    show mia 10
    mia "Я хочу, чтобы ты пригласил его на ужин со мной и моей матерью."
    mia "Вы оба хорошо ладите вместе. Может быть, ты сможешь покрутить его руку, если потребуется."
    show mia 7
    show player 14
    player_name "Конечно! Я догоню его в {b}полицейском участке{/b}."
    show player 13
    show mia 10
    mia "Спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_glasses:
    show player 12
    player_name "Еще раз, что ты хочешь, чтобы я сделал с этими очками?"
    show player 5
    show mia 10
    mia "Я надеялась, что ты сможешь подбросить их на работу моего отца."
    show mia 7
    show player 14
    player_name "Это верно... Я сейчас вспомнил."
    player_name "Тогда я займусь этим делом!"
    return

label mia_dialogue_donuts:
    show player 14 at left
    show mia 7 at right
    player_name "Есть идеи, как мне узнать, какие пончики нравятся твоему отцу?"
    show player 1
    show mia 10
    mia "О, Эмм..."
    mia "Может, поспрашивать на его работе?"
    mia "Они любят есть там пончики..."
    show mia 7
    show player 17
    player_name "Ха-ха, возможно ты права, это может сработать."
    show mia 10
    show player 1
    mia "Хочешь еще о чем-нибудь поговорить?"
    show mia 7
    show player 1
    return

label mia_dialogue_mia_draw_tattoo:
    show mia 7 at right
    show player 10 at left
    player_name "О татуировке, которую ты хотела..."
    show player 5
    show mia 10
    mia "О! Она у тебя есть?!"
    show mia 7
    show player 10
    player_name "Нет, не сейчас."
    player_name "Но, что ты хотела?"
    show player 5
    show mia 10
    mia "Хмм... Что-то симпатичное и красочное!"
    show mia 7
    show player 17
    player_name "Ха-ха, хорошо."
    show player 14
    player_name "Посмотрим, что я смогу сделать."
    show player 13
    show mia 9
    mia "Огромное спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_fail:
    show mia 7 at right
    show player 2 at left
    player_name "О татуировке, которую ты хотела..."
    show player 13
    show mia 10
    mia "О! Она у тебя есть?!"
    show mia 7
    show player 14
    player_name "Да!"
    show player 239_240 with dissolve
    player_name "Мне потребовалось время, чтобы сделать это..."
    show player 386 with dissolve
    player_name "Вот оно что!"
    show player 13
    show mia 32
    if player.location == L_school_scienceclassroom:
        show mial 1b
    with dissolve
    mia "Хмм..."
    show player 10
    player_name "Что-то не так?"
    show player 11
    show mia 33
    mia "Ну, я надеялась на что-то другое."
    show mia 34
    show player 25
    player_name "Ох..."
    show player 24
    show mia 30
    mia "Мне нравится!!"
    show mia 33
    mia "Но может быть, ты нарисуешь что-то другое?"
    show mia 34
    show player 10
    player_name "Например?"
    show player 5
    show mia 30
    mia "Попробуйте что-то мило, что имеет больше цветов!"
    show mia 31
    show player 14
    player_name "Хорошо, я попробую сделать что-нибудь другое..."
    show player 13
    show mia 30
    mia "Огромное спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_mia_show_tattoo_pass:
    show mia 7 at right
    show player 2 at left
    player_name "О татуировке, которую ты хотела..."
    show player 13
    show mia 10
    mia "О! Она у тебя есть?!"
    show mia 7
    show player 14
    player_name "Да!"
    show player 239_240 with dissolve
    player_name "Мне потребовалось время, чтобы сделать это..."
    show player 386 with dissolve
    player_name "Вот оно что!"
    show player 13
    show mia 29
    if player.location == L_school_scienceclassroom:
        show mial 1b at right
    with dissolve
    mia "ВАУ!!!"
    show mia 30
    mia "Мне это очень нравится!"
    show mia 31
    show player 17
    player_name "Очень?"
    show player 18
    show mia 30
    mia "Да!"
    show mia 29
    mia "Это так красиво..."
    show mia 31
    show player 14
    player_name "Круто! Я рад, что тебе понравилось."
    show player 13
    show mia 30
    mia "Мы должны посетить салон {b}Сахарные татушки{/b} и посмотрим, смогут ли они сделать это для меня."
    show mia 7
    if player.location == L_school_scienceclassroom:
        show mial 1f
    with dissolve
    show player 12
    player_name "Сейчас?!"
    show player 5
    show mia 9
    mia "Не сейчас, глупо!"
    show mia 10
    mia "Как насчет {b}субботы{/b}?"
    show mia 7
    show player 10
    player_name "Хорошо, встретимся там в {b}субботу{/b}."
    show player 5
    show mia 10
    mia "Обещай, что встретишь меня там в {b}течение дня{/b}!"
    show mia 7
    show player 14
    player_name "Я обещаю!"
    show player 13
    show mia 10
    mia "Ладно, хорошо. Я не уверена, что смогу сделать это сама, ха-ха."
    mia "Тогда увидимся."
    hide player
    hide mia
    hide mial
    with dissolve
    return

label mia_dialogue_mia_get_tattoo:
    show mia 7 at right
    show player 12 at left
    player_name "Насчет татуировки..."
    show player 5
    show mia 12
    mia "Ты все еще придёшь?"
    show mia 8
    show player 14
    player_name "Ну конечно!"
    show player 10
    player_name "Но когда ты хотела пойти?"
    show player 11
    show mia 12
    mia "Ты уже забыл?!"
    show mia 8
    show player 21
    player_name "Думаю, в последнее время у меня много всего на уме..."
    show player 13
    show mia 9
    mia "Все в порядке, ха-ха."
    show mia 10
    mia "Мне нужно, чтобы ты встретилась со мной в {b}субботу{/b} в {b}тату-салоне{/b}, {b}в течение дня{/b}!"
    show mia 7
    show player 14
    player_name "Хорошо, я позабочусь, чтобы быть там с тобой."
    show player 13
    show mia 10
    mia "Огромное спасибо, {b}[firstname]{/b}."
    return

label mia_dialogue_church:
    show player 12
    player_name "Когда твоя мама ходит в церковь?"
    show player 5
    show mia 12
    mia "В {b}выходные утром{/b}."
    show mia 8
    show player 34
    player_name "Хмм..."
    show player 14
    player_name "Хорошо, спасибо."
    show player 13
    show mia 12
    mia "Что ты собираешься делать?!"
    show mia 8
    show player 12
    player_name "Я пока не совсем уверен, но я перезвоню, если найду способ."
    show player 13
    show mia 12
    mia "Окей..."
    return

label mia_dialogue_art_sessions_intro:
    show player 10
    player_name "Привет, ну... {b}Мисс Росс{/b} попросила меня поговорить с тобой."
    show player 11
    show mia 10
    mia "Серьёзно?"
    show player 10
    show mia 7
    player_name "Да, она хочет, чтобы ты была моим партнером на некоторых частных художественных сессиях."
    return

label mia_dialogue_art_sessions_stat_pass:
    show player 10
    player_name "Я бы очень хотел, чтобы ты пришла помочь, {b}Мия{/b}."
    show player 5
    show mia 12
    mia "Ты бы хотел?"
    show mia 8
    show player 29 with dissolve
    player_name "Полностью."
    show player 3
    show mia 8b
    mia "Хмм..."
    show mia 9
    mia "Окей!"
    show player 13 with dissolve
    show mia 10
    mia "Я приду за тобой, {b}[firstname]{/b}."
    show mia 7
    show player 14
    player_name "Мило! Спасибо, {b}Мия{/b}!"
    show player 13
    show mia 9
    mia "Хе-хе, никаких проблем."
    show mia 7
    show player 14
    player_name "Так что, увидимся там?"
    show player 13
    show mia 10
    mia "Держу пари!"
    return

label mia_dialogue_art_sessions_stat_fail:
    player_name "[chr_warn]Она непреклонна, что это должна быть ты."
    show player 11
    show mia 12
    mia "[chr_warn]... Но я даже не очень хорошо разбираюсь в искусстве."
    show player 10
    show mia 8
    player_name "[chr_warn]Ты не можешь быть настолько плохой..."
    show player 11
    show mia 12
    mia "[chr_warn]Поверь мне, я действительно плоха!"
    mia "[chr_warn]Ты должен найти кого-нибудь другого."
    mia "[chr_warn]Кроме того, моя мама сказала бы \"нет\"."
    show player 10
    show mia 8
    player_name "[chr_warn]О, хорошо тогда."
    return

label mia_dialogue_homework_want_parents_back:
    show player 14
    player_name "Что бы ты хотела поизучать вместе?"
    show player 13
    show mia 12
    mia "Я не очень хорошо себя чувствую сейчас."
    show mia 8
    show player 10
    player_name "Хорошо..."
    show player 5
    show mia 12
    mia "Прости."
    mia "Я просто хочу, чтобы мои родители были снова вместе."
    show mia 8
    show player 10
    player_name "Я знаю."
    player_name "Просто дай мне знать, если тебе понадобится моя помощь."
    show player 5
    show mia 12
    mia "Спасибо, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_homework_intro:
    show player 14
    player_name "Что ты хочешь поизучать вместе?"
    show player 13
    show mia 10
    mia "Мы будем изучать вещи, связанные с последним {b}домашним заданием по французскому{/b}. Ты уже сдал это задание?"
    show mia 7
    return

label mia_dialogue_homework_still_busy:
    show player 24
    player_name "Нет. Я все еще работаю над этим."
    show player 13
    show mia 10
    mia "Ну, как только ты это сделаешь, {b}заходи ко мне{/b}."
    hide mia
    hide mial
    with dissolve
    show player 5 with dissolve
    player_name "( Мне нужно закончить {b}домашнее задание по французскому{/b}, так что я смогу заниматься с {b}Мия{/b}. )"
    show player 4 with dissolve
    pause
    player_name "( Интересно, почему она выбрала меня, чтобы помочь ей учиться. )"
    player_name "( Обычно она учится с {b}Джуди{/b}, и она очень хорошо говорит по-французски... )"
    player_name "( ...Я не знаю, как я могу ей помочь. )"
    show player 13 with dissolve
    player_name "( По крайней мере, мы потусуемся, и она очень милая... )"
    hide player with dissolve
    return

label mia_dialogue_homework_study:
    show player 14
    player_name "Я сдал его не так давно."
    show player 13
    show mia 10
    mia "Когда у тебя будет время, {b}подкрадывайся вечером ко мне в комнату{/b}, чтобы мы могли позаниматься."
    show mia 7
    show player 17
    player_name "Будет сделано!"
    show player 13
    return

label mia_dialogue_study_repeat:
    show player 14
    player_name "Ну конечно!"
    scene mia_bedroom_closeup
    show mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Спасибо, что снова сюда пробрался."
    show mia 13
    show player 142
    player_name "Это не так сложно, когда твои родители прикованы к телевизору."
    show player 143
    show mia 16
    mia "Да, это единственное, что не дает им кричать друг на друга."
    mia "Им нравится смотреть повторы."
    mia "Я иногда смотрю с ними, когда делаю домашнюю работу."
    show mia 22
    mia "Большую часть времени я остаюсь здесь... Здесь тише."
    show mia 14
    show player 146
    player_name "Это отстой, что твои родители не ладят."
    show player 141
    show mia 18
    mia "...Да."
    mia "Возможно, они вернуться к тому, как это было раньше."
    show mia 14
    pause
    show mia 16
    mia "Тебе лучше уйти, пока мои родители тебя не заметили."
    show mia 13
    show player 142
    player_name "Я зайду позже, хорошо?"
    show player 141
    show mia 15
    mia "Отлично! Спокойной ночи {b}[firstname]{/b}!"
    show mia 13
    show player 142
    player_name "Спокойной ночи, {b}Мия{/b}."
    hide player
    hide mia
    with dissolve
    return

label mia_dialogue_study_first:
    show mia 7
    show player 21
    player_name "Думаю, нам надо заниматься?"
    show mia 9
    show player 13
    mia "Ну конечно!"
    show mia 10
    mia "Тогда давайте сделаем это."
    show player 11
    mia "Давай я соберу все учебники и переложу на {b}кровать{/b}?"
    show mia 7
    show player 21
    player_name "Ох... Окей!"
    return

label mia_dialogue_study_want_parents_back:
    show player 12
    player_name "Ты хочешь учиться вместе?"
    show player 5
    show mia 12
    mia "Я не очень хорошо себя чувствую сейчас."
    show mia 8
    show player 10
    player_name "Хорошо..."
    show player 5
    show mia 12
    mia "Прости."
    mia "Я просто хочу, чтобы мои родители были снова вместе."
    show mia 8
    show player 10
    player_name "Я знаю."
    player_name "Просто дай мне знать, если тебе понадобится моя помощь."
    show player 5
    show mia 12
    mia "Спасибо, {b}[firstname]{/b}."
    show mia 8
    return

label mia_dialogue_mias_bedroom_leave:
    show mia 8
    show player 10
    player_name "С удовольствием... Но уже поздно..."
    show mia 12
    show player 5
    mia "О, хорошо..."
    mia "...Ты скоро вернешься?"
    show player 14
    show mia 8
    player_name "Да. Посмотрим, что я смогу сделать!"
    show mia 12
    show player 1
    mia "Спокойная ночь..."
    return

label mia_dialogue_science_classroom_leave:
    show player 10
    player_name "Вообще-то, мне лучше вернуться в класс."
    show player 5
    show mia 12
    mia "О, хорошо... Тогда поговорим с тобой позже!"
    show mia 8
    show player 14
    player_name "Увидимся!"
    return

label mia_dialogue_mias_house_entrance_leave:
    show player 10
    player_name "Вообще-то, я помню, что мне нужно было кое-что сделать."
    show player 5
    show mia 12
    mia "О, хорошо... Тогда поговорим с тобой позже!"
    show mia 8
    show player 14
    player_name "Увидимся!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
