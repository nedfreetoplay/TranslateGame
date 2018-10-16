label police_office_first_visit_pre:
    scene police_office_b
    show yumi 2f at left
    show harold 1 at right
    with dissolve
    yum "Большое спасибо вам за эту возможность,сэр!"
    yum "Я с нетерпением ждала этого момента с тех пор, как поступила в Академию."
    show harold 2
    show yumi 1f
    harold "Это отлично, {b}Yumi{/b}."
    harold "Приятно иметь нового партнера."
    show yumi 2f
    show harold 1
    yum "Мне нужно вернуться в камеру.."
    show yumi 1f
    show harold 2
    harold "О. Хорошо тогда.До скорого."
    show harold 1
    hide yumi with dissolve
    pause
    show player 1 at left with dissolve
    show harold 2
    harold "Хэй!Что ты здесь делаешь?"
    harold "Разве ты не один из {b}Mia's{/b} одноклассников?"
    show harold 1
    show player 14
    player_name "Привет, У меня есть несколько вопросов."
    show player 1
    return

label police_office_first_visit_wheres_mia:
    show player 14
    player_name "Мне было просто интересно: вы знаете где {b}Mia{/b}?"
    show player 11
    show harold 2
    harold "Извини, Сейчас я ничем не могу тебе помочь; мы заняты новым делом..."
    harold "Но, она должна быть в школе или дома."
    show harold 1
    show player 14
    player_name "Хорошо.Спасибо,Сэр!"
    hide player
    hide harold
    with dissolve
    return

label police_office_mia_clues_summary:
    scene expression "backgrounds/location_police_office_missing_blur.jpg"
    show player 35 with dissolve
    player_name "( Хорошо, итак значит он ушел на перерыв и решил покататься этим утром... )"
    player_name "( ...И он пьян. )"
    show player 12
    player_name "Хмм..."
    player_name "( Мне нужно больше {b}подсказок{/b}. )"
    player_name "( Может быть, мне стоит проверить его {b}стол{/b}... )"
    hide player with dissolve
    return

label police_office_mia_harold_gift:
    scene police_c_2
    show player 13 at left
    show harold 2 at right
    with dissolve
    harold "Привет!"
    show harold 1
    show player 14
    player_name "Здравствуйте, сэр!"
    player_name "Эмм... у меня есть кое-что для вас."
    show player 13
    show harold 3
    harold "Что-то для меня?"
    show harold 1
    show player 12
    player_name "Ну, это от {b}Mia{/b}..."
    player_name "...Она сказала, что нашла это дома и хочет, чтобы оно было у вас."
    show player 239_240 with dissolve
    pause
    show player 447 with dissolve
    show harold 4
    harold "!!!"
    show harold 33 at Position (xpos=1017)
    show player 13
    with dissolve
    harold "Мои старые авиаторы..."
    show harold 32
    show player 14
    player_name "Она подумала, что они должны быть у тебя."
    show player 13
    show harold 35
    harold "Спасибо, Я... Прошло много времени..."
    show harold 34
    show player 14
    player_name "Я думаю, что вы должны их снова носить !"
    show player 13
    show harold 33
    harold "Я подумаю об этом."
    show harold 34
    show player 14
    player_name "Ну, я пожалуй пойду."
    show player 13
    show harold 33
    harold "Эмм... Не мог бы ты сделать что-нибудь быстро для меня, прежде чем уйти?"
    show harold 34
    show player 14
    player_name "Конечно, в чем дело?"
    show player 13
    show harold 33
    harold "Просто скажи {b}Yumi{/b} что нам нужна обновленная информация о переводе заключенного..."
    harold "...Она должна быть в подвале."
    show harold 34
    show player 14
    player_name "Хорошо,Я скажу ей."
    show player 13
    show harold 35
    harold "Спасибо еще раз, парень."
    hide player
    hide harold
    with dissolve
    return

label police_office_mia_convince_harold_pre:
    scene police_c_2 with fade
    show player 14 at left
    show earl 3 at right
    with dissolve
    player_name "Здравствуйте, офицер {b}Earl{/b}!"
    show player 13
    show earl 2 with dissolve
    ear "Здравствуй... Как тебя зовут еще раз"
    show earl 1
    show player 10
    player_name "{b}[firstname]{/b}, Я в классе с вашей дочерью.."
    show player 5
    show earl 4
    ear "О, даааааааа."
    show earl 2
    ear "Что тебе нужно?"
    show earl 3 with dissolve
    show player 12
    player_name "Ну,Я надеялась найти {b}Harold{/b} здесь.Он где-то здесь?"
    show player 13
    show earl 2 with dissolve
    ear "Он только что вышел на патрулирование, но он должен скоро вернуться.."
    ear "Я вря дли закончу свою коробку с пончиками,когда он вернется за стол..."
    ear "...и я ем БЫСТРО!"
    ear "В любом случае... этот парень давно не раскрывал дела.. Я не думаю что он больше на это способен."
    show earl 3 with dissolve
    show player 12
    player_name "Серьезно?"
    show player 5
    show earl 6 with dissolve
    ear "Я думаю, когда меня повысили, вместо него, это выбило его из седла."
    show earl 5
    pause
    show earl 6
    ear "Хэй... У меня закончились пончики!"
    show player 13
    ear "Слушай, парень. Мне нужно быстро съездить и пополнить запасы. Я становлюсь злым, когда мне не хватает сахара в крови."
    ear "И ты не хочешь познакомиться со злым {b}Earl{/b}."
    ear "{b}Harold{/b} скоро вернется. Побудь здесь!"
    hide earl with dissolve
    show player 12
    player_name "Хмм..."
    player_name "( {b}Harold{/b} не очень хорошо справляется на работе,и потерял продвижение по службе... )"
    show player 10
    player_name "( Он получает страдания и дома и на работе. )"
    show player 5
    pause
    show player 13
    show harold 2 at Position (xpos=762) with dissolve
    harold "Ну, привет, {b}[firstname]{/b}."
    harold "Какие у тебя планы на сегодня?"
    show harold 1
    show player 14
    player_name "{b}Mia{/b} хотел, чтобы я попросил тебя присоединиться к ней и {b}Helen{/b} на ужин в выходные."
    show player 13
    show harold 29
    harold "..."
    show harold 30 at right with dissolve
    harold "Чтож... Я очень хотел бы их увидеть..."
    harold "Хотелось бы мне чтобы у меня тоже было на это время, но..."
    show player 5
    hide harold
    show harold 26 at Position (xpos=762)
    with dissolve
    harold "У меня много работы.В последнее время у меня есть много дел."
    harold "Мое самое старое дело начинает выделяться на фоне моего шефа."
    harold "Мне поручили пресловутое дело ночного бандита."
    harold "Я получил накал страстей в последнее время из-за отсутствия результатов о местонахождении пропавших товаров..."
    show harold 25
    return

label police_office_mia_convince_harold_pre_erik_thief:
    show harold 26
    harold "...и {b}Larry{/b} также отказывается говорить местоположения товара..."
    show harold 25
    show player 12
    player_name "Я поговорю с ним. Я знаю его жену."
    player_name "Если я не смогу узнать у него местонахождение, может быть, я смогу попросить {b}Mrs. Johnson{/b} помочь нам."
    return

label police_office_mia_convince_harold_pre_no_erik_thief:
    show player 12
    player_name "Я слышал новости.В последнее время я часто видел вора возле моего дома."
    show harold 29
    player_name "Он всегда крадется к моей соседке, {b}Mrs. Johnson{/b},во двор."
    show player 5
    show harold 3
    harold "Серьезно? Если ты заметишь его снова, позвони мне напрямую."
    show harold 1
    show player 12
    player_name "Конечно! Я не буду спускать глаз с него."
    show player 5
    show harold 6
    harold "Также были сообщения о нем рядом с парком. Если ты заметишь его там, держи меня в курсе."
    show harold 1
    show player 12
    player_name "Хорошо, Я проверю там улики, также."
    return

label police_office_mia_convince_harold_mid:

    show player 13
    show harold 2
    harold "Спасибо, {b}[firstname]{/b}."
    show harold 6
    harold "Мне лучше вернуться к работе. Если я когда-нибудь захочу решить некоторые свои дела и освободиться пораньше от работы."
    show harold 1
    show player 14
    player_name "Поговорим попозже, {b}Harold{/b}."
    hide harold with dissolve
    return

label police_office_mia_convince_harold_mid_erik_thief:
    show player 12
    player_name "( Похоже, мне нужно помочь ему найти, где {b}Larry{/b} спрятал все украденное. )"
    show player 10
    player_name "( Иначе,у него никогда не будет времени поужинать с {b}Mia{/b} и {b}Helen{/b}. )"
    show player 12
    player_name "( Я должен заехать в тюрьму и увидеться с ним.. )"
    player_name "( Может, он скажет мне, где украденные вещи. )"
    return

label police_office_mia_convince_harold_mid_no_erik_thief:
    show player 12
    player_name "( Похоже, мне нужно помочь ему найти украденные товары. )"
    show player 10
    player_name "(В противном случае, он никогда не найдет время чтобы поужинать с {b}Mia{/b} и {b}Helen{/b}. )"
    show player 12
    player_name "( Мне лучше приглядывать за задним двором {b}Mrs. Johnson's{/b} ночью. )"
    player_name "( {b}Harold{/b} также отметил, вор был замечен в парке тоже. )"
    return

label police_office_mia_convince_harold_after:
    show player 5
    pause
    show player 30
    player_name "( {b}Earl{/b} все еще не вернулся. )"
    show player 33
    player_name "( Интересно, сколько пончиков он сжирает каждый день... )"
    hide harold
    hide player
    with dissolve
    return

label police_office_mia_return_goods_pre:
    scene police_c_2 with fade
    show player 453 at right
    show harold 2f at left
    with dissolve
    harold "Привет, {b}[firstname]{/b}."
    show harold 1f
    show player 454
    player_name "Хэй, {b}Harold{/b}!"
    show player 453
    show harold 3f
    harold "Что за большая сумка,у тебя с собой?"
    show harold 1f
    show player 454
    player_name "Это то, что я нашел в парке..."
    player_name "...Думаю, ты захочешь это увидеть."
    show player 453
    show harold 4f
    harold "О, да?"
    show harold 1f
    show player 454
    player_name "Посмотрим!"
    show player 13f
    show harold 47
    with dissolve
    harold "!!!"
    show harold 49 with dissolve
    harold "...Это..."
    harold "...все украденные вещи!!"
    show harold 48
    return

label police_office_mia_return_goods_pre_erik_thief:
    show player 17f
    player_name "Это было прямо там, где вы сказали, что это будет!"
    show player 13f
    show harold 49
    harold "Это было?"
    show harold 48
    show player 14f
    player_name "Вы упомянули, что грабителя часто видели в парке."
    player_name "Я навел кое-какие справки вокруг и нашел его спрятаным за кустами рядом с белым деревом."
    return

label police_office_mia_return_goods_pre_no_erik_thief:
    show player 14f
    player_name "{b}Larry{/b} на самом деле сказал мне, где это было."
    player_name "Он сказал, что спрятал все украденное в парке.."
    return

label police_office_mia_return_goods_after:
    show player 13f
    show harold 49
    harold "Я впечатлен {b}[firstname]{/b}. Ты проделал отличную работу!"
    show harold 48
    show player 17f
    player_name "О, не благодари меня. Я бы не нашел его, если бы ты не собрал улики.."
    show player 14f
    player_name "Если кто-нибудь спросит меня об этом, это был офицер {b}Harold{/b} кто нашел!"
    show player 13f
    show harold 49
    harold "О, ты слишком великодушный."
    show harold 48
    show earl 5 at Position (xpos=500)
    show yumi 11 at Position (xpos=700)
    with dissolve
    yum "Что у тебя там напарник?"
    show yumi 10
    show earl 6
    ear "Похоже на его грязную сумку для белья."
    ear "*Фыркать* Hee-uck-uck-uck"
    show earl 5
    show harold 49
    harold "Не совсем, {b}Earl{/b}. Это все украденные вещи ночного грабителя.!"
    show harold 48
    show earl 6
    ear "Деррррьмммммо!"
    show earl 5
    show yumi 11
    yum "Поздравляю, сэр!"
    show yumi 10
    show earl 6
    ear "Я...Я всегда знал что могу на тебя рассчитывать, {b}Harold{/b}!"
    show earl 5
    show harold 49
    harold "Спасибо ребята. Я действительно ничего такого не сделал-"
    show harold 48
    show player 14f
    player_name "{b}Harold's{/b} просто скромничает!"
    show player 13f
    show earl 6
    ear "Итак, какие там пропавшие вещи?"
    show earl 5
    show harold 49
    harold "Много ценных вещей... Я думаю, тут все, что было украдено здесь."
    hide harold
    show earl 7 at left
    with dissolve
    ear "Вау! Я не думал, что ты на такое способен в последнее время, {b}Harold{/b}!"
    ear "Но ты раскрыл одно из самых громких дел в последние годы!"
    show earl 8
    ear "Ты наверняка получишь продвижение по службе, найдя все украденные предметы! Черт возьми, ты заслуживаешь повышения.!"
    show earl 7
    "*Ворчание* *Ворчание*"
    show earl 8
    ear "Знаешь... Мой живот урчит... Все это волнение сделало меня очень голодным!"
    ear "Мне нужно найти себе пончик.!"
    hide earl
    show harold 48 at left
    with dissolve
    show yumi 11
    yum "Поздравляю еще раз, {b}Harold{/b}."
    show yumi 10
    show harold 49
    harold "Спасибо, {b}Yumi{/b}."
    show harold 50
    hide yumi
    show player 11f
    with dissolve
    harold "!!!"
    show harold 48
    show yumi 12 at Position (xpos=500)
    with dissolve
    yum "..."
    show yumi 13 at Position (xoffset=12) with dissolve
    yum "Ну... мне... эм... лучше вернуться к своим обязанностям в камере."
    hide yumi with dissolve
    show harold 2f at Position (xpos=9) with dissolve
    show player 13f
    harold "Это... считаю прекрасно."
    harold "Я не чувствовал, что это оценится в течение длительного времени..."
    harold "Спасибе тебе, {b}[firstname]{/b}, за то, что помог мне с этим."
    show harold 1f
    show player 14f
    player_name "Это было большое везенье, правда."
    show player 13f
    show harold 2f
    harold "Аххх..."
    harold "Я думаю, теперь я начну проводить больше времени в патрулях.."
    harold "Ты знаешь... на самом деле попытался решить мои другие дела вместо того, чтобы пытаться просто сделать его в течение дня."
    show harold 1f
    show player 14f
    player_name "Молодец {b}Harold{/b}.Я рад что тебе лучше."
    player_name "Я знаю, что всегда чувствую себя хорошо после чего-то в школе."
    show player 17f
    player_name "{b}Mia{/b} и {b}Helen{/b} будут рады услышать, что ты решил это дело тоже!"
    show player 13f
    show harold 25f
    pause
    show harold 2f
    harold "Знаешь что. Я все-таки приду на ужин все-таки."
    harold "Я чувствую, как груз упал с моих плечь теперь, когда ценности людей были найдены."
    harold "Я позвоню им в ближайшее время и составлю планы на ужин... Мне действительно есть, о чем им рассказать!"
    show harold 1f
    show player 14f
    player_name "Я рад, что все получилось в конце концов, {b}Harold{/b}."
    show player 13f
    pause
    show player 36f with dissolve
    player_name "Чтож, Увидимся позже."
    show player 13f with dissolve
    show harold 2f
    harold "Пока, {b}[firstname]{/b}."
    hide harold
    hide player
    with dissolve
    return

label police_harolds_desk:
    call expression game.dialog_select("police_harolds_desk_dialogue")
    $ M_mia.trigger(T_harold_photo_clue)
    $ game.main()

label police_harolds_desk_dialogue:
    scene police_c_2
    show player 109
    show harold_desk at right
    with dissolve
    pause
    show player 108
    player_name "( Здесь ничего особенного. )"
    show player 108f with dissolve
    player_name "( Я надеялся найти кое-какие заметки и кое-что- )"
    player_name "Хмм..."
    player_name "( Это его старая фотография? )"
    call screen harolds_desk
    scene police_office_picture
    player_name "( Это... {b}Helen{/b} и {b}Harold{/b}?! )"
    player_name "( Вау... Они так по-другому... и намного счастливее! )"
    player_name "..."
    player_name "( Где это место? )"
    player_name "( Это похоже на... может быть {b}Рейвен-Хилл{/b}? )"
    player_name "Хмм."
    player_name "( Они, наверное, часто там зависали... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
