label french_classroom_bissette_intro:
    scene french_class_c
    show player 1 at left with dissolve
    show teacher 2 at right with dissolve
    bis "Вот ты где!"
    show player 2 at left
    show teacher 1 at right
    player_name "Здрасте, {b}Miss Bissette{/b}!"
    show player 2 at left
    show teacher 5 at right
    bis "Слушай, {b}[firstname]{/b},  я знаю, что у тебя были кое-какие личные дела, о которых нужно позаботиться, и именно поэтому ты отсутствовал в последнее время..."
    bis "...Но все ли в порядке?"
    show player 24 at left
    show teacher 4 at right
    player_name "Да. Я думаю все в порядке..."

    show player 5
    show teacher 5
    bis "Ты не единственный, кто немного отстает."
    show teacher 4
    show player 10
    player_name "Думаю, это самый сложный класс, который у нас есть."
    show player 5
    show teacher 2
    bis "Если тебе что-нибудь понадобится, дай мне знать."
    show teacher 1
    show player 14
    player_name "Спасибо, {b}Miss Bissette{/b}."
    show player 5
    show teacher 3
    bis "Ой! Это напоминает мне!"
    show teacher 2
    bis "Я внедряю новую систему обучения для тех, кто пытается догнать."
    show teacher 1
    show player 10
    player_name "Да?"
    show player 5
    show teacher 12
    bis "Это будет немного больше... один на один тип обучения..."
    bis "...И я надеюсь, что это активизирует студентов."
    show teacher 13
    show player 14
    player_name "Понятно."
    show player 13
    show teacher 2
    bis "Почему бы тебе не занять свое место и я буду обсуждать его в классе."
    show teacher 1
    show player 14
    player_name "Хорошо."
    hide player
    hide teacher
    scene black
    with fade

    scene french_class_cs9
    with fade
    show text "{b}Miss Bissette{/b}сделала объявление.\nОна планировала наградить ученика, который показал наибольшее улучшение в классе после финального теста.\nОна даже предлагала частные уроки всем, кто был заинтересован." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide french_class_cs9
    scene black
    with fade

    show studyclass02 with dissolve
    show text "Я целый день пыталась наверстать упущенное в учебе..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03
    with dissolve
    show text "...пока не прозвенел звонок." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    scene black
    with fade

    pause 0.5

    show studyclass04 with dissolve
    show text "Я и забыл, что занятия французским вызывают у меня сонливость.\nБыло трудно сосредоточиться на уроке." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass05
    with dissolve
    show text "Но я всегда могу рассчитывать, что мои одноклассники не дадут мне уснуть..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass06
    with dissolve
    show text "В последнее время они надо мной издеваются...\nНаверное, потому что я только что вернулась и теперь я в центре внимания..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass07
    with dissolve
    show text "Не поймите меня неправильно. Я могу стоять на своем..." at Position (xpos= 512, ypos = 700) with dissolve
    pause

    hide text
    show studyclass08
    with hpunch
    show text "...но я думаю, что это просто, как в любой школе.\nНу, хотя бы день закончился и я могу идти домой..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene french_class_c
    show teacher 2
    with dissolve
    bis "О! И прежде чем вы все уйдете."
    bis "Любые студенты, интересующиеся занятиями после школы, {b}приходят поговорить со мной в моем офисе или завтра в классе!{/b}"
    show teacher 3
    bis "До свидания!"
    hide teacher with dissolve
    return

label french_classroom_bissette_tutoring:
    scene french_class_c
    show player 5 with dissolve
    player_name "( Я должен поговорить с {b}Miss Bissette{/b} о персональных занятиях. )"
    player_name "( Мне понадобится помощь, если я хочу сдать французский. )"
    hide player with dissolve
    return

label french_classroom_bissette_study:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Ладно, я готов начать урок, {b}Miss Bissette{/b}."
    show player 13
    show teacher 3
    bis "Гениально!"
    show teacher 2
    bis "Останься после уроков и мы начнем."
    show teacher 1
    show player 14
    player_name "Конечно."
    hide player
    hide teacher
    with dissolve

    show studyclass02 with dissolve
    show text "Я целый день пыталась наверстать упущенное в учебе..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...пока не прозвенел звонок." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show teacher 7 at right
    show desk 5 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Ты готов к нашему первому уроку?"
    bis "Один."
    bis "Вместе."
    show teacher 9
    show desk 6
    player_name "Ух, да?"
    show desk 5
    show teacher 7
    bis "Ах-ах-ах, парле ву франсэ?"
    show teacher 9
    show desk 6
    player_name "О! Ум, уии?"
    show desk 5
    show teacher 7
    bis "Хорошо!"
    bis "Итак, ты уже посмотрел на задания?"
    show teacher 9
    show desk 6
    player_name "Да, посмотрел."
    show desk 5
    show teacher 7
    bis "Какое создает проблему?"
    show teacher 9
    show desk 6
    player_name "Ну, я не очень хорошо произношу слова."
    show desk 4
    player_name "Так... Как ты произносишь это слово?"
    show desk 3
    show teacher 7f at Position (xpos=300) with dissolve
    bis "Это velo или la bicyclette."
    bis "Это значит велосипед."
    hide teacher
    show desk 8 at Position (xoffset=-29)
    with dissolve
    player_name "!!!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Так, повторяй за мной {b}[firstname]{/b}."
    show desk 10 at Position (xoffset=-27) with dissolve
    bis "Vi-loo"
    show desk 11 at Position (xoffset=-27)
    player_name "...Velow."
    show desk 10 at Position (xoffset=-27)
    bis "No VI-loo."
    show desk 11 at Position (xoffset=-27)
    player_name "Vv...velo"
    show desk 10 at Position (xoffset=-27)
    bis "Почти, тебе просто нужно произнести e сейчас."
    show desk 11 at Position (xoffset=-27)
    player_name "...Velo."
    show desk 10 at Position (xoffset=-27)
    bis "Tres bien, мой красавец!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Ты учишься очень быстро."
    show desk 11 at Position (xoffset=-27) with dissolve
    player_name "Спасибо, {b}Miss Bissette{/b}. Вы хороший учитель!"
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Ах, такой чародей!"
    show desk 8 at Position (xoffset=-29) with dissolve
    bis "Такой воспитанный молодой человек."
    show desk 9 at Position (xoffset=-27) with dissolve
    bis "Теперь перейдем к следующему слову."
    scene black with fade
    pause 1
    scene classroom_night
    show teacher 7 at right
    show desk 1 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Ты так хорошо справился, {b}[firstname]{/b} но уже поздно."
    show teacher 10
    bis "Мы должны закончить на сегодня, да?"
    show teacher 9
    show desk 2
    player_name "Вау, уже так поздно?"
    player_name "Я совсем потерял счет времени."
    show desk 1
    show teacher 7
    bis "Да, время летит быстро, когда тебе так весело!"
    bis "Ты знаешь, {b}[firstname]{/b}. Я так рада, что ты записался на мое репетиторство."
    bis "Это наполняет меня радостью, помогая таким хорошим молодым студентам, как ты, добиться успеха."
    show teacher 10
    bis "Вот почему я стала учительницей французского."
    show teacher 9
    show desk 2
    player_name "Да, мне повезло, что вы мой учитель, {b}Miss Bissette{/b}."
    show desk 1
    show teacher 7
    bis "Ты льстишь..."
    bis "Ты заставляешь меня краснеть."
    bis "Просто продолжай практиковаться, и я думаю, что ты наверстаешь в кратчайшие сроки."
    bis "Кто знает, может быть, ты даже заработаешь эту специальную награду..."
    show teacher 9
    show desk 2
    player_name "Да, мэм."
    show desk 1
    show teacher 7
    bis "Сейчас иди домой, {b}[firstname]{/b}."
    show teacher 10
    bis "Au revoir!"
    show teacher 9
    show desk 2
    player_name "Спокойной ночи, {b}Miss Bissette{/b}."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_smith_report:
    scene french_class_c
    show teacher 4 at right
    show principal 28f at left
    with dissolve
    smi "{b}Miss Bissette{/b}, Я ожидала твой промежуточный отчет на моем столе сегодня утром."
    show principal 29f
    show teacher 15
    with dissolve
    bis "Je suis desole! Это совершенно вылетело у меня из головы!"
    show teacher 4 with dissolve
    show principal 27f at Position (xoffset=70)
    smi "Да, я хочу получить его к концу дня!"
    show principal 28f with dissolve
    smi "...И лучше бы было улучшение по сравнению со средним баллом за прошлый семестр!"
    smi "Город не будет продолжать финансировать нас, если все наши студенты провалят свои занятия!"
    show principal 29f with dissolve
    show teacher 5
    bis "Oui, {b}Directrice Smith{/b}. Я разработала новый метод, чтобы вдохновить студентов."
    bis "Наверняка, это поднимет их интерес к французскому языку."
    show teacher 4
    show principal 27f at Position (xoffset=70)
    smi "Ха! Вы не могли вдохновить собаку лаять..."
    show principal 29f
    show teacher 19
    bis "Mais, Madame... Конечно, вы-"
    show teacher 18
    show principal 27f at Position (xoffset=70)
    smi "Просто принеси мне отчет, или я отправлю твою вонючую задницу обратно во французскую дыру, из которой ты выползла!"
    show principal 28f with dissolve
    smi "Все понятно?!"
    show principal 29f with dissolve
    show teacher 5
    bis "...O-oui, {b}Directrice Smith{/b}."
    hide principal with dissolve
    show teacher 20
    pause
    show teacher 19 at center with dissolve
    bis "Старая злая сука!(франц.)"
    show teacher 18f with dissolve
    pause
    show player 10 at left with dissolve
    player_name "{b}Miss Bissette{/b}?"
    show player 5
    show teacher 5 at right with dissolve
    bis "Oh, mon Dieu!"
    show teacher 1
    show player 11
    player_name "..."
    show teacher 3
    bis "{b}[firstname]{/b}, ты напугал меня!"
    show teacher 1
    show player 10
    player_name "Простите..."
    show player 12
    player_name "Все в порядке?"
    show teacher 4
    player_name "Я слышал крики {b}Principal Smith{/b} в коридоре..."
    show player 5
    show teacher 5
    bis "Oui. Она просто хочет, чтобы вы, студенты, проявляли больше интереса к французкому."
    show teacher 4
    show player 12
    player_name "Ну, она не должна была быть настолько грубой."
    show player 5
    show teacher 3
    bis "О, {b}[firstname]{/b}. Ты всегда такой милый со мной..."
    show teacher 17 zorder 1 with dissolve
    show player 11
    player_name "!!!" with hpunch
    show teacher 16
    bis "Знаешь, я хотела поговорить с тобой о следующем задании для твоих репетиторских занятий."
    show teacher 17
    player_name "*глоток*"
    show player 10
    player_name "Хорошо, что вы имеете в виду?"
    show player 5
    show teacher 16
    bis "Я хочу, чтобы ты {b}написал несколько абзацев о твоей любимой еде, en Francais{/b}."
    bis "Займемся этим вместе, да?"
    show teacher 17
    show player 14
    player_name "Звучит неплохо."
    show player 13
    show teacher 16
    bis "... И если ты все правильно напишешь..."
    bis "Возможно, я дам тебе попробовать мою особую награду, да?"
    show teacher 17
    show player 14
    player_name "Да, Хорошо!"
    show player 13
    show teacher 3 at center with dissolve
    bis "Tres bien! Тогда тебе лучше начать работу."
    bis "Au revoir, {b}[firstname]{/b}!"
    hide teacher with dissolve
    show player 10
    player_name "Интересно, какая может быть награда?"
    show player 5
    player_name "..."
    show player 35 with dissolve
    player_name "...И о какой еде мне писать?"
    show player 14 with dissolve
    player_name "{b}Пора сходить в библиотеку{/b}, я полагаю."
    player_name "Та библиотекарша очень помогла. Может, она сможет найти для меня книгу о {b}французской еде{/b}?"
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_assignment:
    scene french_class_c
    show teacher 1 at right
    show player 14 at left
    with dissolve
    player_name "Я закончил задание!"
    player_name "Я писал о сыре."
    show player 13
    show teacher 2
    bis "О! Тебе нравится французский сыр?"
    show teacher 1
    show player 14
    player_name "Любой нравится..."
    show player 13
    show teacher 2
    bis "Хе-хе, ты знаешь, что хорошо сочетается с сыром, не так ли?"
    show teacher 1
    show player 10
    player_name "...Умм, крекеры?"
    show player 5
    show teacher 3
    bis "Не глупи, французское вино!"
    show teacher 12
    bis "Может быть, когда-нибудь мы могли бы попробовать бутылочку вместе?"
    bis "Но сначала мы должны продолжить практиковать ваш французский."
    bis "Останься сегодня после уроков, и мы будем заниматься одни."
    bis "Только ты и я, да?"
    show teacher 13
    show player 26
    player_name "Да, мэм."
    show player 13
    show xtra 21 at left
    show teacher 2
    bis "О, и перед тем как ты сел, добавь fromage на доску."
    bis "Я попрошу других студентов написать про их предпочтения также хорошо."
    hide player
    hide xtra
    hide teacher
    with dissolve

    scene french_class_cs14
    with fade
    show text "Я чувствовал, что неплохо разбираюсь во французском.\nС каждым днем я понимал все больше и больше.\nЧастные уроки с {b}Miss Bissette{/b} определенно сделали язык более интересным." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    show studyclass02 with dissolve
    show text "Я целый день пыталась наверстать упущенное в учебе..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...пока не прозвенел звонок." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 12 at Position (xpos = 400, ypos = 768)
    with dissolve
    bis "Я очень горжусь твоим последним заданием."
    bis "Ты становишься... бегущим."
    show desk 13
    player_name "Да? Я рад, что вам понравилось. Я очень много над этим работал."
    show desk 12
    bis "Я уверена, что ты работал, mon bel homme."
    bis "Ты готов к следующему уроку репетиторства?"
    show desk 13
    player_name "Да."
    show desk 12
    bis "Тогда давайте повторим еще несколько слов."
    scene black with fade

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Твое произношение становится таким хорошим, {b}[firstname]{/b}."
    bis "Я думаю, ты определенно заслужил это..."
    show desk 19 with dissolve
    bis "...И я так горжусь тобой."
    show desk 20 with dissolve
    bis "Oh, mon Dieu!"
    bis "Все эти новые знания растут..."
    bis "Ce qu'il est enorme ce lapin..."
    show desk 19 with dissolve
    player_name "..."
    show desk 14 with dissolve
    bis "В чем дело, {b}[firstname]{/b}?"
    show desk 15
    player_name "Что, если кто-то..."
    show desk 14
    bis "Aww, Tellement mignon..."
    show desk 17 with dissolve
    bis "Не стоит беспокоиться."
    show desk 18 with dissolve
    bis "Здесь."
    bis "Это должно отвлечь тебя от забот..."
    player_name "*глоток*"
    show desk 24 with dissolve
    player_name "Д-да..."
    show desk 25 with dissolve
    pause
    show desk 26 with dissolve
    bis "Oh, oui! Joue avec mes seins, {b}[firstname]{/b}!"
    show desk 24 with dissolve
    player_name "Вы уверены, что {b}Principal Smith{/b} не придет?"
    show desk 5 at Position (xoffset=-58)
    show teacher 10c at right
    with dissolve
    bis "Oh non! j'ai oublie!"
    bis "Я забыла сдать промежуточный отчет!"
    bis "Прости меня, {b}[firstname]{/b}. Боюсь, мы должны остановиться на сегодня."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Хорошо, {b}Miss Bissette{/b}..."
    show desk 5 at Position (xoffset=-58)
    show teacher 10c
    bis "Мы продолжим в следующий раз, хорошо?"
    bis "Завтра тебя ждет новое задание."
    show teacher 10b
    show desk 6 at Position (xoffset=-58)
    player_name "Конечно, {b}Miss Bissette{/b}."
    show desk 5 at Position (xoffset=-58)
    show teacher 10
    bis "Au revoir, mon petit lapin!"
    show teacher 9
    show desk 6 at Position (xoffset=-58)
    player_name "Au revoir."
    hide desk
    hide teacher
    with dissolve
    return

label french_classroom_bissette_poem_assignment:
    scene french_class_c
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bis "Bonjour, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Bonjour, {b}Miss Bissette{/b}."
    show player 13
    show teacher 2
    bis "Comment allez-vous?"
    show teacher 1
    show player 14
    player_name "О умм, У меня все хорошо."
    show player 13
    show teacher 3
    bis "Прекрасно!"
    show teacher 2
    bis "Ты так быстро учишь французский!"
    show teacher 1
    show player 14
    player_name "Да, я думаю, ваше репетиторство действительно помогает."
    show player 13
    show teacher 12
    bis "Тогда мы должны продолжить занятия, да?"
    show teacher 13
    show player 14
    player_name "С удовольствием!"
    show player 13
    show teacher 12
    bis "Думаю, тебе понравится следующее задание..."
    show teacher 13
    show player 14
    player_name "О, правда?"
    show player 13
    show teacher 12
    bis "Oui, beaucoup..."
    bis "Вам знаком французский роман?"
    show teacher 13
    show player 10
    player_name "Н-нет, не совсем..."
    show player 11
    show teacher 16 zorder 1 with dissolve
    bis "On apprend alors!"
    bis "Французы-лучшие любовники во всем мире!"
    show teacher 17
    show player 26
    player_name "...Да? Я не знал этого..."
    show player 13
    show teacher 16
    bis "О, да {b}[firstname]{/b}, так и есть!"
    bis "Чтобы тебе понять это... Ты должен {b}написать романтическое стихотворение en Francais!{/b}"
    show teacher 17
    show player 10
    player_name "Э-э, я не знаю, мэм. Я никогда не писал ничего подобного."
    player_name "Я даже не знаю, с чего начать..."
    show player 13
    show teacher 25 with dissolve
    bis "Ridicule!"
    show teacher 26 with dissolve
    bis "Ты прирожденный, я верю в тебя, {b}[firstname]{/b}!"
    show teacher 27 with dissolve
    show player 14
    player_name "Хех. Хорошо, {b}Miss Bissette{/b}."
    show player 13
    show teacher 25 with dissolve
    bis "Tres Bien, mon bel homme!"
    show teacher 26 with dissolve
    bis "Я знаю, ты напишешь что-нибудь, что растопит сердце!"
    show teacher 16 with dissolve
    bis "Возвращайся ко мне, когда закончишь."
    bis "Возможно, ты наконец-то получишь награду, которую так долго искал, да?"
    show teacher 17
    show player 11
    player_name "*глоток*"
    show player 26
    player_name "Да! Хорошо!"
    show player 13
    show teacher 16
    bis "Ca m'excite!"
    show teacher 17
    show player 14
    player_name "Я скоро вернусь, {b}Miss Bissette{/b}."
    show player 13
    show teacher 16
    bis "Au revoir, {b}[firstname]{/b}."
    hide teacher with dissolve
    show player 29 with dissolve
    player_name "Вау!!!"
    player_name "Ладно, думаю {b}мне стоит сходить в библиотеку{/b} и посмотреть, что я смогу найти о французской поэзии и романтике."
    hide player with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_pre:
    scene french_class_c
    show teacher 1 at right
    show player 386 at left
    with dissolve
    player_name "Вот, {b}Miss Bissette{/b}. Я закончил поэму."
    show player 13 with dissolve
    show teacher 23 with dissolve
    bis "Surperbe!"
    bis "Oh, comme c'est beau!"
    bis "Да, это будет замечательно."
    bis "Класс в твоем распоряжении."
    show teacher 24
    show player 10
    player_name "А? Что вы имеете в виду?"
    show player 5
    show teacher 2 with dissolve
    bis "Ну ты прочитаешь ее для класса, да?"
    show teacher 1
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Никогда!"
    show player 11
    show teacher 12
    bis "Quoi? Давай сейчас, {b}[firstname]{/b}."
    bis "Твои слова прекрасны... Было бы неправильно не поделиться такой вещью, да?"
    show teacher 13
    show player 10
    player_name "Абсолютно нет! Мне было бы слишком стыдно!"
    show player 22
    show teacher 2
    bis "Ой, не будь таким застенчивым, {b}[firstname]{/b}."
    show teacher 11
    pause
    show teacher 2
    bis "Я знаю! Я дам тебе партнера, с которым ты будешь читать!"
    bis "Это менее унизительно, да?"
    show teacher 1
    show player 12
    player_name "... Не совсем."
    show player 23
    show teacher 19
    bis "{b}Roxxy{/b}, проснись!"
    show player 22
    show teacher 18
    rox "Хмм?"
    show teacher 19
    bis "Fille paresseuse! Проснись, я сказала!"
    show teacher 18
    rox "Что?!"
    show teacher 19
    bis "Иди сюда!"
    show teacher 20
    pause
    pause
    show roxxy 27f at Position (xpos=500) with dissolve
    show player 24
    show teacher 19
    bis "Поскольку ты не можешь потрудиться написать стихотворение для класса, ты будешь читать его с {b}[firstname]{/b}."
    show teacher 18
    show roxxy 30f
    rox "Нет, я не буду."
    show roxxy 29f
    show player 22
    show teacher 19
    bis "Да, будешь!"
    show teacher 18
    show roxxy 30f
    rox "Мне плевать на это дурацкое задание!"
    show roxxy 29f
    show teacher 19
    bis "Quoi?! Comment oses-tu!"
    bis "Ты пойдешь туда и прочитаешь или я оставлю тебя под стражей до конца срока!"
    bis "Comprenez vous?!"
    show teacher 20
    show roxxy 30f
    rox "Серьезно?!"
    show roxxy 29f
    show teacher 19
    bis "Сейчас же!"
    show teacher 18
    show roxxy 30f
    rox "Грррр, ладно!"
    hide roxxy with dissolve
    show player 10
    player_name "Эээ, {b}Miss Bissette{/b}?"
    show player 5
    show teacher 2
    bis "Да, {b}[firstname]{/b}?"
    show teacher 1
    show player 10
    player_name "Я действительно не хочу этого делать..."
    show player 5
    show teacher 2
    bis "О, но это так прекрасно..."
    show teacher 16 zorder 1 with dissolve
    bis "Сделай это для меня, mon bel homme!"
    show teacher 26 with dissolve
    bis "... Я дам тебе особую награду, если ты сделаешь это..."
    show teacher 27
    show player 25
    player_name "{b}*глоток*{/b}"
    show player 24
    player_name "... Хорошо, я сделаю это."
    show player 5
    show teacher 12 at center
    bis "Tres bien!"
    bis "Я так горжусь тобой!"
    show teacher 1
    hide player with dissolve
    show teacher 2
    bis "Нет нет! En Francais! Теперь давайте начнем!"
    hide teacher with dissolve

    scene french_class_cs11
    with fade
    show text "Мне не хотелось читать стихи перед классом.\n...но участие {b}Roxxy{/b} действительно помогло.\nНикого не волновало, насколько слащаво было стихотворение; не с {b}Roxxy{/b} , спотыкающейся за каждое слово." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve

    scene french_class_cs13
    with fade
    show text "К тому времени, как мы достигли конца,{b}Roxxy{/b} уже не смущалась.\nНаши одноклассники хихикали над ее плохим произношением.\nОна была в ярости! Я никогда не видел ее такой злой..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    with dissolve
    return

label french_classroom_bissette_hand_in_poem_assignment_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, твой французкий прекрасен!"
    show teacher 1
    show player 14
    player_name "Спасибо, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... И {b}Roxxy{/b}..."
    bis "... Что ж, ты пыталась."
    show teacher 18
    rox "Грррр..."
    show teacher 2
    bis "Очень хорошо, вот и все на сегодня."
    bis "Не забудте сделать домашнюю работу, и я увижу вас завтра, хорошо?!"
    hide teacher
    with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, прости за-"
    show player 11f
    show roxxy 3f with dissolve
    rox "Я НЕНАВИЖУ ЕЕ!!!"
    show roxxy 29f
    show player 10f
    player_name "... {b}Roxxy{/b}, серьезно! Ты должна успокоиться..."
    show player 11f
    show roxxy 31f
    rox "УСПОКОИТСЯ?!"
    rox "Я не собираюсь успокаиваться!"
    show roxxy 30f
    show player 24f
    rox "Эта сука с болтливым ртом получает какое-то больное удовольствие от того, что смущает меня!"
    rox "Французская шлюха!"
    rox "Ей повезло, что я не надрала ей задницу прямо здесь и сейчас!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "Что это за вопли такие!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "Я не могу поверить, что вы заставили меня сделать это!"
    rox "Вы знаете, как мне неловко?!"
    show roxxy 29f
    show teacher 12
    bis "Ба, не будь таким ребенком..."
    bis "{b}[firstname]{/b} написал прекрасную поэму!"
    show teacher 19
    bis "Ты должна извиниться перед ним за свое неуклюжее произношение."
    show teacher 13
    show roxxy 31f
    rox "Что?! Он не тот, кого ты подставила и выглядела нелепо!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "Это не моя вина, что ты позоришь себя своим бедным французским!"
    bis "Ты тот, кто отказывается от учебы!"
    show teacher 18
    show roxxy 30f
    rox "Гррр!!!"
    rox "Я никогда этого не забуду!"
    hide roxxy with dissolve
    show teacher 19
    bis "Хорошо! Помни об этом, как о причине более серьезно относиться к учебе!"
    show teacher 18
    show player 25
    player_name "Вау, я никогда не видел ее такой злой раньше..."
    show player 5
    show teacher 12
    bis "Ты должен поговорить с ней, {b}[firstname]{/b}."
    bis "Научи ее контролировать свой характер..."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "... Но сначала мы начнем твое обучение, да?"
    show teacher 13
    show player 14
    player_name "Да! Хорошо!"
    show player 13
    show teacher 12
    bis "Tres Bien! Подойди и сядь рядом со мной!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_poem_assignment_no_roxxy_sex:
    scene french_class_c
    show player 13 at Position (xpos=500)
    show roxxy 29f at left
    show teacher 2 at right
    with dissolve
    bis "Tres Bien!"
    bis "{b}[firstname]{/b}, твой французский идеален!"
    show teacher 1
    show player 14
    player_name "Спасибо, {b}Miss Bissette{/b}."
    show player 13
    show teacher 19
    bis "... И {b}Roxxy{/b}..."
    bis "... Что ж, ты пыталась."
    show teacher 18
    rox "Гррр..."
    show teacher 2
    bis "Очень хорошо, вот и все на сегодня."
    bis "Не забудте сделать домашнюю работу, и я увижу вас завтра, хорошо?!"
    hide teacher with dissolve
    show player 25f with dissolve
    player_name "...{b}Roxxy{/b}, прости за-"
    show player 11f
    show roxxy 3f with dissolve
    rox "Заткнись!"
    show roxxy 29f
    show player 10f
    player_name "...Я просто пытаюсь извени-"
    show player 11f
    show roxxy 31f
    rox "Я СКАЗАЛА ЗАКРОЙ СВОЙ РОТ!"
    rox "Не могу поверить, что она заставила меня читать эту сопливую чушь перед всем классом!"
    show roxxy 30f
    show player 24f
    rox "Тьфу, и с тобой для всего класса!"
    rox "Отвратительно!"
    rox "Тебе повезло, что я не надрала тебе задницу прямо здесь и сейчас!"
    show roxxy 29f
    show teacher 19 at right with dissolve
    bis "Que se passe-t-il!?"
    bis "Что это за вопли такие!?"
    show teacher 18
    show player 22
    show roxxy 30f
    rox "Я не могу поверить, что вы заставили меня сделать это!"
    rox "Вы знаете, как мне неловко?!"
    show roxxy 29f
    show teacher 12
    bis "Ба, не будь таким ребенком..."
    bis "{b}[firstname]{/b} написал прекрасную поэму!"
    show teacher 19
    bis "Ты должна извиниться перед ним за свое неуклюжее произношение."
    show teacher 13
    show roxxy 31f
    rox "Извиниться?! Перед ним?! Ты сошла с ума, черт возьми!"
    show roxxy 3f
    show teacher 19
    bis "Shush toi!!"
    bis "Мы не виноваты, что ты позоришь себя своим бедным французским!"
    bis "Ты тот, кто отказывается от учебы!"
    show teacher 18
    show roxxy 30f
    rox "Грррр!!!"
    rox "Я никогда этого не забуду!"
    hide roxxy with dissolve
    show teacher 19
    bis "Хорошо! Помните об этом, как о причине более серьезно относиться к учебе!"
    show teacher 18
    show player 25
    player_name "Вау, я никогда не видел ее такой злой раньше..."
    show player 5
    show teacher 12
    bis "Не беспокойся о ней, {b}[firstname]{/b}."
    bis "Она справится с этим."
    show teacher 13
    show player 34
    player_name "..."
    show player 5
    show teacher 12
    bis "Теперь, я думаю, пришло время начать обучение, да?"
    show teacher 13
    show player 14
    player_name "Да! Хорошо!"
    show player 13
    show teacher 12
    bis "Tres Bien! Подойди и сядь рядом со мной!"
    scene black with fade
    return

label french_classroom_bissette_hand_in_assignment_intro_continue:
    show studyclass02 with dissolve
    show text "Я целый день пытался наверстать упущенное в учебе..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    show studyclass03 with dissolve
    show text "...пока не прозвенел звонок." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text with dissolve

    scene classroom_night
    show desk 16 at Position (xpos = 400, ypos = 768)
    bis "Твой прогресс во французком впечатляет, {b}[firstname]{/b}."
    bis "Думаю, на большом экзамене у тебя все получится."
    show desk 15
    player_name "Надеюсь на это! Мне очень нужно сдать этот предмет."
    show desk 19 with dissolve
    bis "Aww, mon bel homme..."
    show desk 20
    bis "Не стоит так беспокоиться..."
    player_name "*глоток*"
    show desk 16 with dissolve
    bis "Знаешь, я припоминаю, что обещала тебе особую награду за сегодняшнее чтение, да?"
    show desk 15
    player_name "Д-да..."
    show desk 16
    bis "Знаешь, твоя поэма была прекрасна."
    bis "Французский язык был создан для поэзии. Ты так не думаешь?"
    show desk 15
    player_name "Д-да, мэм."
    show desk 16
    bis "Мне очень понравилась часть, которую ты написала о поцелуе."
    show desk 15
    player_name "О... эта часть?"
    show desk 16
    bis "Знаете ли ты французский поцелуй особым образом?"
    show desk 15
    player_name "Ммм ... А? Я имею в виду, что они делают?"
    show desk 16
    bis "Oui, они называют это французским поцелуем и все..."
    show desk 15
    player_name "О да, я слышал об этом."
    show desk 16
    bis "Ты пробовал французский поцелуй раньше?"
    return

label french_classroom_bissette_hand_in_poem_assignment_have_kissed:
    scene classroom_night
    show desk 15
    player_name "Д-да, немного больше."
    show desk 16
    bis "Да просто?"
    show desk 15
    bis "Ты должен показать мне, что ты знаешь!"
    player_name "Правда?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "{b}[firstname]{/b}!"
    bis "Я нахожусь под большим впечатлением!"
    bis "Где ты научился так целоваться?"
    show desk 29
    player_name "Ох, ох... вы знаете... Здесь и там..."
    show desk 30
    bis "Хе-хе, хорошо. Храни свои секреты. Просто целуй меня как можно дольше!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_havent_kissed:
    scene classroom_night
    show desk 15 at Position (xpos=400)
    player_name "Н-нет..."
    show desk 16
    bis "Oh, Je dois t'apprendre!"
    show desk 15
    player_name "...Ты хочешь научить меня?"
    show desk 16
    bis "Oui."
    show desk 27 at Position (xpos=342) with dissolve
    pause
    show desk 28 with dissolve
    pause
    show desk 31_32 with dissolve
    pause
    pause
    show desk 30
    bis "Tres Bien, {b}[firstname]{/b}..."
    bis "Ты тоже естественный в этом."
    show desk 29
    player_name "Д-да, спасибо!"
    show desk 31_32 with dissolve
    pause
    pause
    return

label french_classroom_bissette_hand_in_poem_assignment_continue:
    scene classroom_night
    bis "Мммм..."
    bis "Mon bel homme..."
    bis "Ты заставляешь меня волноваться..."
    player_name "*глоток*"
    bis "Возможно, нам стоит взять это-"
    show desk 33 with hpunch
    "*Bzzt*"
    smi "{b}Miss Bissette{/b}!"
    "*Bzzt*"
    "*Bzzt*"
    smi "Где ты? Ты забыла о нашей встрече?!"
    smi "Не заставляй меня спускаться и тащить свою тощую задницу в мой кабинет!"
    smi "ИДИТЕ ЮДА НЕМЕДЛЕННО!"
    "*Bzzt*"
    show desk 30
    bis "Sacrebleu! Чего она хочет сейчас?!"
    bis "*гммм* Извени, {b}[firstname]{/b}. Кажется, мы должны прерваться еще раз."
    show desk 29
    player_name "Все хорошо, {b}Miss Bissette{/b}. Я понимаю."
    show desk 31_32 with dissolve
    pause
    show desk 30
    bis "Mmm, Ta {b}bouche{/b} est magique!"
    show desk 29
    player_name "А?"
    show desk 30
    bis "Твой {b}рот{/b} волшебный!"
    show desk 29
    player_name "Оооо, {b}bouche{/b}  значит {b}рот{/b}?"
    show desk 30
    bis "Oui."
    show desk 27 with dissolve
    pause
    show teacher 10 at right
    show desk 5
    with dissolve
    bis "Я хочу, чтобы ты {b}пришел ко мне в офис завтра после занятий{/b}."
    bis "Есть еще кое-что, с чем мне нужно тебе помощь перед экзаменом."
    show teacher 9
    show desk 6
    player_name "Конечно."
    player_name "Увидемся завтра, {b}Miss Bissette{/b}."
    show desk 5
    show teacher 10
    bis "Au revoir, mon bel homme."
    hide teacher with dissolve
    player_name "..."
    show desk 34
    player_name "Уфф, это было потрясающе!"
    hide desk with dissolve
    return

label french_classroom_bissette_smith_final_report:
    scene french_class_c
    show teacher 1 at right
    show principal 27f at left
    show principal 27f at Position (xoffset=70)
    with dissolve
    smi "Я не знаю, как вам это удалось, но Средний балл растет."
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "Я говорила вам, что могу вдохновить их!"
    show teacher 1
    show principal 27f at Position (xoffset=70)
    smi "Да, хорошо. Не думайте, что это повод, чтобы начать расслабляться!"
    show principal 26f at Position (xoffset=70)
    show teacher 2
    bis "Не волнуйтесь, мои ученики дают мне 110%%!"
    show player 14 at Position (xpos=500)
    player_name "Доброе утро, {b}Miss Bissette{/b}."
    show player 113
    player_name "...и {b}Principal Smith{/b}."
    show player 13
    show teacher 12
    bis "Bonjour, {b}[firstname]{/b}."
    show teacher 13
    show player 114
    show principal 29f
    smi "Пффф."
    hide player with dissolve
    show principal 26f at Position (xoffset=70)
    show teacher 12
    bis "... Некоторые дают мне даже больше, чем 110%%!"
    show teacher 13
    show principal 29f
    smi "..."
    show principal 28f with dissolve
    smi "Просто помни, что я положила на тебя глаз!"
    hide principal
    hide teacher
    with dissolve
    return

label europe_map_dialogue:
    scene expression "backgrounds/location_school_french_map.jpg"
    player_name "..."
    player_name "Похоже на правду..."
    player_name "{b}Miss Bissette{/b} до сих пор не заметила, что кто-то заменил ее карту Европы."
    pause
    $ A_europe.unlock()
    $ game.main()

label french_class_roxxy_lolipop_intro:
    scene french_class_c
    show roxxy 6f at Position (xpos=500)
    show teacher 19 at right
    with dissolve
    bis "Я надеюсь, что у вас есть что-то для меня сегодня!"
    bis "Вы не можете продолжать занятия с пустыми руками {b}Roxanne{/b}!"
    show teacher 18
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "Ухх, Все зовут меня {b}Roxxy{/b}..."
    rox "Не {b}Roxanne{/b}!"
    show roxxy 6f with dissolve
    show teacher 5
    bis "Почему так?"
    bis "Тебя зовут {b}Roxanne{/b}..."
    bis "Об этом говорится в школьных записях!"
    show teacher 4
    show roxxy 7f
    rox "{b}*вздыхает*{/b}"
    show roxxy 5f
    rox "Слушайте, я сделаю домашнее задание для вас сегодня, хорошо?!"
    show roxxy 10f at Position (xoffset=9) with dissolve
    rox "... Хватит меня доставать, пожалуйста!"
    show roxxy 6f with dissolve
    show teacher 18
    bis "Хмм?"
    show teacher 19
    bis "Я не буду..."
    show teacher 18
    show roxxy 7f
    rox "..."
    show teacher 19
    bis "Просто подготовь домашнее задание к уроку, хорошо?"
    show teacher 18
    show roxxy 11f at Position (xoffset=9) with dissolve
    rox "Я сказала, что получу его!"
    show roxxy 9f at Position (xoffset=9)
    show teacher 19
    bis "... Putain, mais quelle branleuse..."
    hide teacher with dissolve
    pause
    show player 13 at left
    show roxxy 10f at Position (xoffset=9)
    rox "Гррр, глупая каша во рту..."

    show roxxy 7 at Position (xpos=600) with dissolve
    rox "!!!"
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "Ты опять!"
    show roxxy 3b with dissolve
    show player 11
    player_name "..."
    show roxxy 3c
    rox "Почему кажется, что ты всегда рядом?!"
    show roxxy 3d
    show player 10
    player_name "Не знаю."
    player_name "Это не совсем большая школа..."
    show player 5
    show roxxy 2
    rox "Ну, я начинаю уставать от твоей тупой-"
    show roxxy 1
    rox "..."
    show roxxy 1h
    rox "... Подожди."
    rox "Ты сделал {b}домашнее задание по французкому{/b} на сегодня?"
    show roxxy 1g
    show player 12
    player_name "... Да."
    show player 5
    rox "..."
    show roxxy 47 with dissolve
    rox "{b}*мммм*{/b}"
    show roxxy 48
    rox "Я сказала тупой?"
    rox "Потому что я хотел сказать..."
    rox "... Красавец!"
    rox "Да, так!"
    show roxxy 47
    show player 11
    player_name "..."
    show roxxy 48
    rox "Ты занимался?"
    show roxxy 47
    show player 12
    player_name "Почему ты так странно себя ведешь?"
    show player 5
    rox "..."
    show player 12
    player_name "... А, понятно."
    player_name "Тебе нужно мое {b}домашнее задание по французкому{/b}."
    show player 90
    show roxxy 50b with dissolve
    pause
    show roxxy 50 with dissolve
    rox "Ну, если ты предлогаешь..."
    show roxxy 49
    player_name "Ххпппп..."
    show player 30
    player_name "... И что я получу?"
    show player 90
    show roxxy 50
    rox "Ухх, Привилегия помогать самой красивой девушке в школе?"
    show roxxy 49
    player_name "..."
    show player 30
    player_name "Ты действительно думаешь, что ты самая красивая девушка в школе?"
    show player 17
    player_name "Ха!"
    show roxxy 31
    rox "{b}*вздох*{/b} Прости?!" with hpunch
    rox "... Я самая-"
    show roxxy 3d
    show player 12
    player_name "Ты что?!"
    show player 90
    show roxxy 29
    rox "..."
    show roxxy 3
    rox "Рррр, ты поможешь мне или нет?!"
    show roxxy 29
    show player 35
    player_name "Полагаю, я могу позволить тебе скопировать мою работу."
    show player 34
    show roxxy 4
    return

label french_class_roxxy_lolipop_just_once:
    show player 12
    player_name "... Но не думай, что я буду отдавать тебе свою работу все время."
    player_name "Мне может быть немного жаль тебя, но это не значит, что я позволю тебе ходить вокруг меня."
    show player 90
    show roxxy 2
    rox "Чччч, ТЕБЕ жалко МЕНЯ?!?!"
    show roxxy 1
    show player 10
    player_name "Ну, ты на грани исключения из школы..."
    show player 5
    show roxxy 3c
    rox "Пошел ты, {b}[firstname]{/b}..."
    show roxxy 3d
    show player 11
    player_name "..."
    show player 10
    player_name "Тебе нужна домашняя работа или нет?"
    show player 5
    show roxxy 3
    rox "... Да."
    show roxxy 3d
    show player 14
    player_name "... Скажи, \"Пожалуйста.\""
    show player 13
    show roxxy 3c
    rox "!!!"
    show roxxy 3b
    rox "..."
    show player 12
    player_name "Знаешь что... забудь!"
    show player 90
    show roxxy 3
    rox "Нет, подожди!"
    show roxxy 3b
    rox "..."
    show roxxy 3c
    rox "... Пожалуйста."
    show roxxy 3d
    show player 12
    player_name "Пожалуйста, что?"
    show player 90
    show roxxy 3
    rox "{b}*вздыхает*{/b}"
    show roxxy 3c
    rox "Пожалуйста, могу я скопировать твое домашнее задание?"
    show roxxy 3b
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "Да, хорошо."
    player_name "Я пойду и {b}заберу ее из своего шкафчика{/b}."
    player_name "Сейчас вернусь."
    hide player with dissolve
    rox "..."
    show roxxy 3
    rox "Придурок..."
    hide roxxy with dissolve
    return

label french_class_roxxy_lolipop_for_lolipop:
    show player 14
    player_name "Если ты дашь мне свой леденец..."
    show player 13
    show roxxy 3c
    rox "What?"
    show roxxy 3d
    show player 14
    player_name "Тот леденец, который ты сосала."
    show player 12
    player_name "Дай его мне."
    show player 90
    show roxxy 10 at Position (xoffset=-9) with dissolve
    rox "..."
    show roxxy 11 at Position (xoffset=-9)
    rox "Ты сезьезно?"
    show roxxy 10 at Position (xoffset=-9)
    show player 17
    player_name "Ага."
    show player 13
    show roxxy 13 at Position (xoffset=-55) with dissolve
    rox "Ухх, Это действительно странно, но ладно..."
    show roxxy 12 at Position (xoffset=-55)
    show player 90
    player_name "..."
    show player 92
    player_name "Он недостаточно влажный."
    show player 90
    show roxxy 13 at Position (xoffset=-55)
    rox "!!!"
    rox "Ты отвратителен!"
    show roxxy 12 at Position (xoffset=-55)
    show player 92
    player_name "Эй, ты хочешь домашнюю работу или нет?"
    show player 90
    rox "..."
    show roxxy 13 at Position (xoffset=-55)
    rox "Ладно!"
    show roxxy 7 with dissolve
    pause
    show roxxy 8 at Position (xoffset=-2) with dissolve
    pause
    show roxxy 12 at Position (xoffset=-55) with dissolve
    rox "Вот, держи, извращенец!"
    show player 97
    show roxxy 3b
    with dissolve
    player_name "Спасибки!"
    show player 93 with dissolve
    show player 94
    player_name "Я пойду и {b}заберу ее из своего шкафчика{/b}."
    player_name "Сейчас вернусь."
    hide player with dissolve
    show roxxy 14
    rox "..."
    show roxxy 3c
    rox "Чудак..."
    hide roxxy with dissolve
    return

label frenchclassroom_roxxy_dexter_alcohol_fight:
    scene french_class_c
    show player 4 at left
    with dissolve
    player_name "( Хмм? )"
    show player 5 with dissolve
    player_name "( {b}Roxxy{/b} пропускает уроки сегодня? )"
    player_name "( Это не хорошо, {b}Miss Bissette{/b} возможно, ее выгонит... )"
    show eve 2 at right with dissolve
    eve "{b}[firstname]{/b}!"
    show eve 5
    show player 14
    player_name "Привет, {b}Eve{/b}."
    player_name "Что случилось?"
    show player 13
    show eve 2
    eve "{b}Roxxy{/b} и {b}Dexter{/b} опять ругаются на {b}баскетбольной площадке{/b}!"
    show player 11
    eve "Пойдем, мы не можем это пропустить!"
    show eve 5
    show player 10
    player_name "Опять?!"
    player_name "Хорошо, пошли."
    hide player
    hide eve
    with dissolve
    return

label frenchclassroom_roxxy_ask_exam_copy:
    scene french_class_c
    show roxxy 32 at right
    show teacher 2f at left
    with dissolve
    bis "Хорошо, что твои оценки наконец улучшаются, {b}Roxxy{/b}."
    bis "... Но я должна напомнить тебе о предстоящих экзаменах."
    bis "Они составят огромную часть вашей общей оценки."
    bis "Если ты не пройдешь их, боюсь, нам придется снова отстранить тебя от группы поддержки..."
    show teacher 3f
    bis "Возможно, навсегда."
    show teacher 1f
    show roxxy 2b with dissolve
    rox "!!!"
    show teacher 2f
    bis "Ты должна учиться усерднее, да?"
    bis "Экзамен будет охватывать весь материал, который мы изучили в этом году."
    show teacher 3f
    bis "В том числе части которые ты пропустила."
    show teacher 1f
    show roxxy 2c
    rox "... Но-"
    rox "Я не..."
    show roxxy 3b
    show teacher 3f
    bis "Ах Ах Ах!"
    bis "Ты зря теряешь время споря, {b}Roxxy{/b}."
    show teacher 12f
    bis "Лучше потратить время на учебу, да?"
    hide teacher with dissolve
    show roxxy 1o with dissolve
    pause
    show player 14 at left with dissolve
    player_name "Привет Rox-"
    show player 11
    player_name "..."
    show player 10
    player_name "Все в порядке?"
    player_name "Ты выглядишь грустной."
    show player 5
    show roxxy 3 with dissolve
    rox "Из-за этой болтовни меня снова вышвырнут из команды!"
    show roxxy 3d
    show player 12
    player_name "Ты о чем?"
    show player 5
    show roxxy 3
    rox "{b}Miss Bissette{/b}!"
    rox "Если я не сдам ее экзамен, они снова меня отстранят от группы поддержки."
    show roxxy 3d
    show player 12
    player_name "... Я думал, твои оценки улучшаются?"
    show player 5
    show roxxy 2
    rox "Да, но мне нужно знать, что мы проходили ранее в этом году."
    show roxxy 3c
    rox "Что, черт побери, мне делать, {b}[firstname]{/b}?"
    rox "Черлидинг - единственная часть школы, которая мне нравится."
    show roxxy 3d
    show player 10
    player_name "{b}Roxxy{/b}..."
    show player 5
    show roxxy 3
    rox "Я не могу тратить все свое время на обучение...."
    rox "... Не со всем, что происходит дома в последнее время."
    show roxxy 32 with dissolve
    player_name "..."
    show roxxy 33
    rox "Что мне делать, {b}[firstname]{/b}?!"
    show roxxy 32
    show player 10
    player_name "Я не знаю."
    show player 5
    show roxxy 33b
    pause
    show roxxy 32
    show player 4 with dissolve
    player_name "Хмм..."
    show player 35 with dissolve
    player_name "... Эй, подожди-ка секундочку!"
    player_name "Разве твои друзья не говорили, что {b}Principal Smith{/b} хранит копии экзаменов у себя дома?"
    show player 13 with dissolve
    show roxxy 33
    rox "Хмм?"
    show roxxy 32
    show player 14
    player_name "{b}Becca{/b} и {b}Missy{/b}!"
    player_name "Они говорили об этом в раздевалке на днях..."
    show player 13
    show roxxy 33
    rox "Где?"
    rox "... Я игнорирую половину того, что говорят эти тупые шлюхи."
    show roxxy 32
    show player 29 with dissolve
    player_name "Хех, я почти уверен, что это то, о чем они говорили."
    show player 13 with dissolve
    show roxxy 1l
    rox "... Но ты же не думаешь, что..."
    rox "Я имею в виду, ты думаешь это правда?"
    show roxxy 1k
    show player 10
    player_name "Хмм, не знаю."
    player_name "{b}Principal Smith{/b} помешана на контроле всего."
    show player 14
    player_name "Возможно, она хранит копии у себя дома."
    show player 13
    show roxxy 1g with dissolve
    rox "..."
    show roxxy 1h
    rox "Ладно, думаю, тебе придется вломиться и найти их для меня..."
    show roxxy 1g
    show player 23
    player_name "Что?! Мне?!"
    show player 22
    show roxxy 2
    rox "Ну, да!"
    show roxxy 1
    show player 12
    player_name "Никогда!"
    player_name "Это твои оценки! Ты и иди!"
    show player 90
    show roxxy 2c
    rox "Ты заставишь меня это сделать?!"
    show roxxy 2
    rox "Я думала, ты настоящий мужчина..."
    show roxxy 1
    show player 5
    player_name "..."
    show roxxy 2
    rox "Настоящий мужчина не заставит девушку делать такие опасные вещи!"
    show roxxy 1
    show player 10
    player_name "Ну, да но..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    show player 433
    rox "Ну, {b}[firstname]{/b}. Пожалуйста..."
    show roxxy 47 at Position (xoffset=-34)
    player_name "..."
    show roxxy 48 at Position (xoffset=-34)
    rox "Не хочешь еще раз побыть моим рыцарем в сияющих доспехах?!"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "Я..."
    show player 434
    show roxxy 50c at Position (xoffset=-34) with dissolve
    rox "Просто подумай о том, что скажут {b}Becca{/b} и {b}Missy{/b} когда я скажу им, какой ты храбрый."
    rox "Я могу рассказать им все об этом в следующий раз, когда мы все вместе будем на пляже!"
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Помнишь пляж, {b}[firstname]{/b}?"
    rox "... Помнишь нашу маленькую игру в бутылочку?"
    show roxxy 49 at Position (xoffset=-23)
    show player 427 with dissolve
    player_name "{b}*глоток*{/b} Д-да..."
    show player 434
    show roxxy 48 at Position (xoffset=-34)
    rox "Ты мне поможешь, не так ли?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427 with dissolve
    player_name "Ну уххх..."
    show player 434
    show roxxy 4 with dissolve
    rox "Хехехе! Я знала, что ты сделаешь это!"
    rox "Спасибо, {b}[firstname]{/b}!"
    show roxxy 1
    show player 24
    player_name "{b}*вздыхая*{/b}"
    show player 10
    player_name "Думаю, мы должны {b}отправиться к ней домой сегодня вечером{/b}."
    show player 5
    show roxxy 2c
    rox "А?!"
    show roxxy 2
    rox "Нет, это ужасная идея!"
    show roxxy 1
    show player 12
    player_name "Почему это ужасная идея?"
    player_name "Она будет в школе."
    show player 90
    show roxxy 2
    rox "Нельзя вламываться в чужой дом средь бела дня!"
    rox "Соседи обязательно вызовут полицию!"
    show roxxy 1
    show player 10
    player_name "Да, но..."
    show player 5
    show roxxy 1b
    rox "Ты должен проникнуть {b}ночью{/b}!"
    rox "{b}Principal Smith{/b} обычно здесь задерживается допоздна, так что у тебя должно быть достаточно времени."
    show roxxy 1
    show player 30
    player_name "Секундочку..."
    player_name "Ты идешь со мной, так?"
    show player 90
    show roxxy 50 at Position (xoffset=-23) with dissolve
    rox "Пффф, это тело не предназначено для бега, {b}[firstname]{/b}..."
    show player 433
    rox "Я только буду задерживать тебя."
    show roxxy 49 at Position (xoffset=-23)
    show player 434
    player_name "..."
    show roxxy 48 at Position (xoffset=-34) with dissolve
    rox "Кроме того, такой сильный мужчина, как ты..."
    rox "You don't need any help, do you?"
    show roxxy 47 at Position (xoffset=-34)
    show player 427
    player_name "... Нуххх."
    show player 434
    show roxxy 2 with dissolve
    rox "Хе-хе, рада это слышать!"
    show roxxy 1
    show player 24
    player_name "{b}*вздыхая*{/b}"
    show player 10
    player_name "Хорошо, тогда, думаю, я {b}вломлюсь в дом Principal Smith сегодня вечером{/b}."
    show player 25
    player_name "... Один."
    show player 5
    show roxxy 1b
    rox "Ты смошешь, {b}[firstname]{/b}!"
    show roxxy 2
    rox "{b}Только не забудь про экзамены{/b}!"
    show roxxy 1
    show player 12
    player_name "Да, не забуду."
    show player 90
    show roxxy 4
    rox "Удачи!"
    hide roxxy
    hide player
    with dissolve
    pause
    show player 37 with dissolve
    player_name "..."
    player_name "Ух ты, я правда только что согласился вломиться в дом {b}Principal Smith{/b}?!"
    show player 10 with dissolve
    player_name "Как это {b}Roxxy{/b} смогла меня уболтать?!"
    show player 4 with dissolve
    player_name "Помню, я подумал, что это плохая идея, а потом ..."
    show player 11 with dissolve
    pause
    show player 10
    player_name "Титьки."
    show player 11
    pause
    show player 24
    player_name "Она хитрая..."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
