label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Нам нужно поговорить об этой ситуации с {b}Кристи{/b}."
    show player 5f
    show clyde 22
    clyde "Я не хочу..."
    show clyde 21
    show player 10f
    player_name "{b}Клайд{/b}, они хотят отправить её в тюрьму и избавиться от трейлера!"
    show player 5f
    show clyde 26
    clyde "Послушай дорогой! Ты думаешь что я не знаю об этом!"
    clyde "Я сожалею но я ничего не могу я не могу это прекратить!"
    show clyde 25
    show player 12f
    player_name "Ты можешь сдаться..."
    show player 5f
    show clyde 22
    clyde "Да точно..."
    clyde "Тогда мы оба и окажемся за решёткой!"
    show clyde 21
    show player 10f
    player_name "Нет если ты скажешь им что {b}Кристи{/b} не знала что наркотики были спрятаны там."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... И с чего мне бы так делать?"
    show clyde 1
    show player 12f
    player_name "... Потому что это будет правильным решением!"
    show player 90f
    show clyde 2
    clyde "Пффф."
    clyde "Я не хочу попасть в тюрьму!"
    clyde "Красивому парню как я, эти животные сожрут меня заживо."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Смотри чувак. Она взяла вину на себя потому что она твоя семья."
    player_name "... Но это было гораздо хуже чем она думала!"
    player_name "Она может изчезнуть на долгое время и {b}Рокси{/b} потеряет свою {b}Маму{/b} и свой дом."
    show player 12f
    player_name "{b}Рокси{/b} ничего не сделала что бы заслужить такое!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Ох, дерьмо! Ты прав."
    clyde "{b}Роксанна{/b} не должна страдать по моей вине..."
    clyde "... Но Я не вернусь обратно в тюрьму! ... Нет сэр!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "Что если бы ты послал своё признание в письменном виде?"
    player_name "Расскажи им о своей хижине и пусть они придут и найдут доказательства."
    player_name "Если ты все сделаешь правильно, ты можешь быть уже далеко до того,как они начнут тебя искать."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "Наверное я мог бы вернуться в долину..."
    clyde "Они никогда не смогут найти меня там."
    clyde "... Я уверен что точно буду скучать по {b}Тете Кристи{/b} все-таки..."
    show clyde 21
    show player 10f
    player_name "Ты спасешь её из тюрьмы, мужик."
    show player 5f
    show clyde 22
    clyde "Хмм, Я думаю у тебя хороший план."
    show player 13f
    clyde "Итак когда я сделаю это то она будет свободна?"
    show clyde 21
    show player 12f
    player_name "... Мы все ещё должны прийти с деньгами за её залог но для начала неплохо."
    show player 5f
    show clyde 22
    clyde "Сколько денег тебе надо"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Хмх."
    clyde "Что ж я могу это сделать"
    show clyde 1
    show player 10f
    player_name "Что?!" with hpunch
    player_name "Ты же не серьезно..."
    player_name "У тебя есть $50,000 завалявшиеся где-то?"
    show player 11f
    show clyde 2
    clyde "Не совсем."
    show clyde 4 with dissolve
    clyde "... Но у меня есть целая куча метамфитомина."
    clyde "Этого будет достаточно что бы получить $100,000 с хорошего покупателся, Я думаю."
    show clyde 3
    show player 10f
    player_name "Это безумие"
    player_name "Ты реально можешь продать его?"
    show player 5f
    show clyde 4
    clyde "Пффф! Да ладно дружище..."
    clyde "Ты хоть знаешь с кем ты разговариваешь?"
    clyde "Я могу продать замороженый кетчуп как девченка которая носит белые перчатки!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Замороженый кетчуп?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да дружище!"
    show clyde 3 with dissolve
    show player 14f
    player_name "... Когда ты сможешь это сделать?"
    show player 13f
    show clyde 4
    clyde "Хммм, мне нужно будет позвонить моему покупателю."
    clyde "... Но очеьн скоро, я думаю'."
    show clyde 3
    show player 14f
    player_name "Мне надо рассказать {b}Рокси{/b} хорошие новости!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]Ты просто трус!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Эй, тебе не надо называть меня {b}меня{/b} трусо!"
    clyde "[chr_warn]Ты не предстовляешь себе какого это быть в тюрьме для кого то вроде меня!"
    clyde "[chr_warn]Я когда-то был там однажды и будь я проклят если бы я не вернулся назад"
    show clyde 25
    show player 15f
    player_name "[chr_warn]Неважно... {b}ТРУС{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Да пошел ты!"
    clyde "[chr_warn]Я не приму это!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Угх, забей!"
    show player 90f
    show clyde 22
    clyde "Да, это именно то что я собирался сделать'!"
    clyde "Я думаю' что эту больщую кучу забвения' на дне из этих пивных банок!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Когда ты сможешь продать этот Мет"
    show player 5f
    show clyde 2
    clyde "Притормози конец, парень!"
    clyde "Это требуем времени."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Просто иди и скажи моей сладкой {b}кузену{/b} что {b}Клайд{/b} позаботитьтся обо всем!"
    show clyde 1
    show player 14f
    player_name "... Верно."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Ты уже связался со своим покупателем?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Да, приятель!"
    show player 13f
    clyde "Я намериваюсь заключить с ним сделку!"
    show clyde 3
    show player 12f
    player_name "{b}Рокси{/b} сказала что ты не торгавал Метом раньше!"
    show player 90f
    show clyde 26 with dissolve
    clyde "Что?!"
    clyde "Она ничего не знает'!"
    clyde "Я занимался кучей похожих сделорк сдесь!"
    show clyde 25
    show player 12f
    player_name "Ты на самом деле имел дело с покупателями раньше?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Ну, я видел как {b}Тетей Кристи{/b} делала это много раз!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Вздох*{/b} Я пойду с тобой."
    show player 90f with dissolve
    show clyde 2
    clyde "Хм?"
    clyde "Что ты знаешь о продаже наркотиков?!"
    show clyde 1
    show player 12f
    player_name "Ни черта не смыслю в этом."
    player_name "... Но Я точно знаю что ты определенно недостаточно компетенты что бы сделать это в одиночку."
    show player 90f
    show clyde 22
    clyde "Ну, это не... Подожди секунду, что ты имел в виду?!"
    show clyde 1
    show player 12f
    player_name "... Именно."
    show player 90f
    show clyde 2
    clyde "Ччч, Неважно, парень."
    clyde "Пойдешь или не пойдешь. Это не важно для меня!"
    show clyde 26
    clyde "... Но если ты пойдешь то лучше бы тебе {b}встретиться со мной в трейлире вечером {/b}."
    clyde "Ты понял?"
    show clyde 1
    show player 12f
    player_name "Да, я понял."
    player_name "Увидимся {b}сегодня в трейлере Рокси{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Мы все по прежнему хороши что бы продавать мету?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Уверен"
    clyde "Просто будть здесь {b}вечером{/b} если увязался со мной."
    show clyde 3
    show player 12f
    player_name "Да, понял."
    player_name "Увидимся {b}вечером{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Ты готов идти?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Ты одел это?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "Что не так с моей одеждой?"
    show player 5f
    show clyde 2
    clyde "Угх... Я не знаю, парень. Ты выглядишь чертовски подозрительно..."
    clyde "Я уверен что никто не купил бы никаких наркотиков у когда-то как ты."
    show clyde 1
    show player 10f
    player_name "Ну, у меня другой одежды не было..."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Подожди секунду.У меня есть кое что получше для тебя!"
    hide clyde with dissolve
    show player 12f
    player_name "... Это будет интересно."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Давай парень..."
    clyde "Не заставляй нас опоздать!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Я не верю что ты уговорил меня надеть это..."
    player_name "Я чувствую себя глупо!"
    show player 90f
    show clyde 4
    clyde "Шшш, не будь глупцом."
    clyde "Ты похож на настоящего торговца!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Покупатель может придти с секунды на секунду."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Клайд{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Когда ты вернешься в город?!"
    show player 5f
    show clyde 2
    clyde "Эээ, прости приятель."
    clyde "Ты ошибся приятеля..."
    show clyde 1
    show player 10f
    player_name "Хм?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Меня зовут {b}Клетус{/b}!"
    clyde "Рад познакомиться с тобой!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "О чем ты говоришь, {b}Клайд{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Кгхм*{/b} Еше раз..."
    clyde "Мое имя не {b}Клайд{/b}... а {b}Клетус{/b}."
    show clyde 1
    show player 12f
    player_name "... Но ты так похож на кузена {b}Рокси{/b}, {b}Клайда{/b}."
    show player 5f
    show clyde 2
    clyde "Хмм, что ж извини. Я не знаю этого человека {b}Клайда{/b}."
    show clyde 9 with dissolve
    clyde "Тем не менее это звучит так как будто он красивый сукин сын!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Ты что сейчас прикалываешься надо мной?!"
    show player 13f
    show clyde 4
    clyde "Позволь мне спросить..."
    clyde "Этот {b}Clyde{/b} носит шапку?"
    show clyde 3
    show player 10f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Что ж, вот и все!"
    clyde "Как ты можешь видеть... {b}Cletus{/b} никуда не выходит, без своей верной шляпы!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Это так странно."
    show player 12f
    player_name "Мне нужно идти."
    show player 5f
    show clyde 4
    clyde "Ладно. Что ж, рад был с тобой познакомиться, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "Я тебе не говорил своего имени!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Ох, ээээ..."
    clyde "... Ну, я..."
    show clyde 11 with dissolve
    clyde "Эммм... Телепатия!"
    show clyde 12
    show player 10f
    player_name "Хмм?!"
    show player 5f
    show clyde 11
    clyde "Я, {b}Клетус{/b}... Я телепат."
    show clyde 4 with dissolve
    clyde "... И я могу прочесть твои мысли силой вволи!"
    show clyde 3
    show player 10f
    player_name "Мои мысли?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да точно, парень!"
    show clyde 4 with dissolve
    clyde "Так что не говори людям что я здесь"
    clyde "Потому что я знаю..."
    clyde "Особенно,если эти будет полиция."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Я..."
    player_name "... Только..."
    player_name "... Пока."
    hide player with dissolve
    pause
    show clyde 4
    clyde "До скорого, парень!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Я могу тебе помочь с чем-то?"
    show clyde 1
    show player 10f
    player_name "Эммм, нет?"
    show player 5f
    show clyde 22
    clyde "Ох, мужик.Ты один из них от дома к дому, иисус любит людей?"
    show clyde 21
    show player 12f
    player_name "Что?! Нет!"
    show player 5f
    show clyde 26
    clyde "{b}*Задыхаясь*{/b} Ты что коп?!"
    clyde "Ты должен мне сказать, такие правила!"
    show clyde 25
    show player 12f
    player_name "Нет мужик... Мы познакомились только прошлой ночью!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "Я помогал{b}Рокси{/b} с её домашней работой?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Ох, да наверное!"
    clyde "Ты новый парень {b}Рокси{/b}!"
    show clyde 3
    show player 10f
    player_name "Нет, мы только друзья-"
    show player 5f
    show clyde 4
    clyde "Как дела, брат?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "Как дела, брат?!"
    show clyde 3
    show player 14f
    player_name "Ох, привет {b}Клайд{/b}..."
    show player 5f
    show clyde 4
    clyde "Что ты здесь делаешь?!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "И так {b}Клетус{/b}, верно?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Ты прав, парень!"
    show clyde 4 with dissolve
    clyde "Чем я могу тебе помочь?!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Вздох*{/b} все в порядке."
    player_name "Что делаешь?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Много того  что никто не делает'!"
    clyde "Хахаха, знаешь что я имею в виду, брат?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "'Потому что у меня был весь секс... с девушками..."
    clyde "{b}*Кгхм*{/b} человеческими девушками."
    show clyde 12
    show player 12f
    player_name "Да, я понял, {b}Клайд{/b}..."
    show clyde 9 with dissolve
    clyde "Хех, конечно ты!"
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Я никогда не слышал что бы кто не будь так говорил как ты, {b}Clyde{/b}..."
    show player 12f
    player_name "В общем откуда ты?"
    show player 5f
    show clyde 4
    clyde "Это потому что все городские города говорят так же странно!"
    clyde "Там в низу в долине, мы все так разговариваем..."
    show clyde 3
    show player 10f
    player_name "... В долине"
    show player 5f
    show clyde 4
    clyde "Да."
    show clyde 3
    show player 10f
    player_name "Что это?!"
    show player 5f
    show clyde 4
    clyde "Эмм, где я вырос.Ясень пень!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "Это в нескольких округах севернее от сюда."
    clyde "На холмах."
    show clyde 3
    show player 10f
    player_name "Я думал что там севернее одни леса?"
    show player 5f
    show clyde 4
    clyde "Да, довольно много..."
    show clyde 3
    show player 12f
    player_name "Люди живут там?"
    show player 5f
    show clyde 4
    clyde "Psh, моя семья по-прежнему живет здесь."
    clyde "Я думал что я бы переехал сюда {b}Auntie Crystal{/b} через некоторое время."
    clyde "Ощутить городской жизни по настоящему."
    show clyde 3
    show player 10f
    player_name "И как получается?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ээээ, есть свои плюсы и минусы."
    clyde "Я скучаю по родному самогону дома и по всей травке."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Но я там готовил!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "И что ты готовишь?"
    show player 5f
    show clyde 22
    clyde "Э-э-э... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Курицу!"
    show clyde 4 with dissolve
    clyde "Хех, да! Я готовлю жареных цыплят!"
    clyde "Твоему городскому городу этого не хватает..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "Мне нужно идти..."
    show player 5f with dissolve
    show clyde 4
    clyde "Ага, хорошо."
    clyde "Продолдим в следующий раз', братиш!"
    clyde "Wooo!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "Что у тебя там происходит?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Эээ, извини бро."
    clyde "В эту лачугу строго запрещается заходить!"
    show clyde 9 with dissolve
    clyde "Если только у тебя нет женских прелестей?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Хех, что ж запомни это... Если хижина качается', лучше не стучать'!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?!"
    show clyde 3
    show player 401f
    player_name "... Да. несмотря на то что мне бы очень хотелось..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Хороший трактор."
    show player 13f
    show clyde 4
    clyde "Ох, да!"
    clyde "Это здесь {b}Большая Берта{/b}!"
    clyde "Разве она не красавица?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Я сам ее построил из  остатков металлолома."
    clyde "31.2 лошадиных сил, 2500 об/мин, 8.5 галлонов..."
    clyde "... И только посмотри на этот рубиново красный завершение!"
    clyde "Мммм! Она самая сексуальная вещь на четырех колесах!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "На самом деле, неважно."
    player_name "... Может быть в другой раз?"
    show player 5f
    show clyde 4
    clyde "Psh, Черт возьма да, братиш!"
    clyde "Ты знаешь где меня найти."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Давай, {b}Клайд{/b}! Я знаю это ты!"
    show player 16f
    show clyde 4
    clyde "Я не  понимаю о чем ты говоришь..."
    show clyde 3
    show player 15f
    player_name "Это глупо,Я никому не скажу что ты вернулся..."
    show player 16f
    show clyde 4
    clyde "Что ты курил', приятель?"
    show player 428f
    clyde "Мое имя {b}Клетус{/b} и я впервые здесь."
    clyde "навсегда."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "До сих пор написано {b}Clyde{/b} на твоей стене!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Эй!"
    clyde "Не разрушай все стены!"
    clyde "Это обман'!"
    clyde "Мое имя {b}Клетус{/b}!!!"
    show clyde 26
    clyde "Скажи это!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Давай, ты знаешь что хочешь сказать это..."
    show clyde 1
    show player 24f
    player_name "{b}*Вздох*{/b}"
    show player 25f
    player_name "{b}Клетус{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "Вот так!"
    clyde "Это было не так сложно, правда?!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
