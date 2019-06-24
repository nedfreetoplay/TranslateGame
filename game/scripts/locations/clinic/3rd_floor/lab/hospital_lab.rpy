label hospital_lab_dialogue:
    $ player.go_to(L_hospital_lab)
    if M_priya.is_state(S_priya_look_in_lab):
        call expression game.dialog_select("hospital_lab_priya_look_in_lab")
    $ game.main()

label hospital_laboratory_take_pills_dialogue:
    scene expression "backgrounds/location_hospital_lab_blur.jpg"
    show player 706 at left with dissolve
    player_name "( Хм, так это в виде таблеток? )"
    player_name "( Странно. )"
    player_name "( Я ожидал какой-нибудь крем... )"
    player_name "( ... Или что-то в шприце. )"
    player_name "( Так намного проще! )"
    priya "Кто ты такой?!"
    show player 23
    player_name "!!!" with hpunch
    show priya f_stern a_dressed_crossed with dissolve
    player_name "Я эээ..."
    show player 22
    show priya f_angry
    priya "Как вы попали сю-"
    show priya a_dressed_point with dissolve
    priya "{b}*вздыхая*{/b} Ты крадешь мои лекарства!"
    show priya f_stern a_dressed_crossed with dissolve
    show player 23
    player_name "Нет,Я не-"
    show player 22
    show priya f_angry a_dressed_point with dissolve
    priya "Я вызываю охрану!"
    show priya f_stern a_dressed_sides at flip
    show priya at Position (xoffset=650)
    show player 40 with dissolve
    player_name "Подождите, пожалуйста!"
    pause
    hide priya
    show priya f_stern a_dressed_crossed
    with dissolve
    show player 10 with dissolve
    player_name "Я не собирался их красть, я просто искал!"
    show player 5
    show priya f_angry
    priya "Да, точно!"
    show priya f_stern
    show player 10
    player_name "Я серьезно!"
    player_name "Искал, здесь."
    show player 239_240 with dissolve
    pause
    show player 705f with dissolve
    player_name "Видишь, ничего страшного не случилось."
    show player 704f
    show priya f_angry a_dressed_point with dissolve
    priya "Это запретная зона!"
    priya "Как ты вообще сюда попал?!"
    show priya f_stern a_dressed_crossed with dissolve
    show player 24 with dissolve
    player_name "{b}*вздыхая*{/b} Это длинная история. Пожалуйста, не заставляй меня вспоминать об этом снова."
    show player 10
    player_name "Может быть, вы сможете мне помочь?"
    player_name "Я ищу парня по имени, {b}Доктор Сингх{/b}?"
    show player 5
    pause
    show priya f_rolleyes
    priya "Ну, ты нашел \"его\"."
    show priya f_stern
    show player 12
    player_name "А?"
    show player 10
    player_name "... Ты хочешь сказать-"
    show player 37 with dissolve
    show priya f_angry
    priya "Я {b}Доктор Сингх{/b}."
    show priya f_stern
    show player 30
    player_name "Н-но ты же женщина... Верно?"
    show player 5
    show priya f_angry
    priya "Ни хрена себе, Шерлок."
    show priya f_stern
    show player 10
    player_name "Извините, я не-"
    show player 401
    player_name "У меня сложилось впечатление, что ты мужчина."
    show player 403
    priya "..."
    show priya f_angry
    priya "Не могли бы вы поторопиться и рассказать мне, что все это значит?!"
    show priya f_stern
    show player 10
    player_name "Верно, простите!"
    show player 4 with dissolve
    player_name "Эээ."
    show player 10 with dissolve
    player_name "Я слышал что вы разрабатываете таблетки {b}Pregnax{/b}..."
    show player 5
    show priya f_angry
    priya "Ой, от кого же ты слышал это?!"
    show priya f_stern
    show player 10
    player_name "Я... Я обещал, что не скажу..."
    show player 18
    show priya f_angry
    priya "Это была та медсестра на втором этаже, не так ли?!"
    priya "Эта женщина не может держать рот закрытым даже в течение двух секунд."
    show priya f_stern
    show player 11
    player_name "..."
    show priya f_rolleyes
    priya "Продолжай."
    show priya f_stern
    show player 10
    player_name "Видишь ли, мой др-"
    player_name "{b}*гм*{/b} Моя девушка пытается забеременеть и ее шансы не очень хорошие."
    player_name "Я хочу сделать все возможное, чтобы увеличить ее шансы."
    show player 5
    show priya f_angry
    priya "Так вот почему ты вломился в мою лабораторию?"
    show priya f_stern
    show player 29 with dissolve
    player_name "Да."
    show player 26 with dissolve
    player_name "Который опять же, не должен был ничего украсть!"
    show player 38 with dissolve
    player_name "Я просто хотел поговорить с вами о процессе таблеток {b}Pregnax{/b}."
    show player 5 with dissolve
    show priya f_angry
    priya "Процесс на полной мощности."
    show priya f_stern
    show player 24
    player_name "Да, я тоже слышал об этом."
    pause
    player_name "Ты ничего не можешь сделать?"
    show priya f_facepalm a_dressed_facepalm with dissolve
    priya "..."
    show priya f_facepalm_talk
    priya "Хорошо, я признаю это. Я впечатлен вашей решимостью."
    priya "Наверное, было нелегко подняться сюда."
    show priya a_dressed_sides f_normal_talk with dissolve
    priya "... И мне не безразлично положение твоей девушки."
    show priya f_normal
    show player 11
    pause
    show priya f_normal_talk
    priya "Как тебя зовут?"
    show priya f_normal
    show player 10
    player_name "{b}[firstname]{/b}."
    show player 5
    show priya f_normal_talk
    priya "Сколько тебе лет, {b}[firstname]{/b}?"
    show priya f_normal
    show player 10
    player_name "Мне восемнадцать."
    show player 5
    show priya f_normal_talk
    priya "Ты очень молод."
    priya "Все остальные подопытные на десять-тридцать лет старше тебя."
    show priya f_normal
    show player 30
    player_name "Это хорошо или плохо?"
    show player 5
    show priya f_thinking a_dressed_thinking with dissolve
    pause
    show priya f_suspicious_talk
    priya "Это... интригующе."
    show priya f_normal_talk
    priya "... А твоей девушке сколько лет?"
    show priya f_normal
    show player 35
    player_name "Я не совсем уверен в этом..."
    show player 34
    show priya f_suspicious_talk
    priya "Ты пытаешься завести ребенка с этой женщиной и даже не знаешь ее возраста?"
    show priya f_normal
    show player 35
    player_name "Нет, Я эээ..."
    player_name "Я имею в виду, ей уже за тридцать, я думаю."
    show player 34
    show priya f_normal_talk
    priya "О, теперь это интересно..."
    priya "Она твой единственный сексуальный партнер?"
    show priya f_normal
    show player 17
    player_name "... Нет."
    show player 18
    show priya f_rolleyes a_dressed_crossed with dissolve
    priya "Ччч."
    show priya f_thinking a_dressed_thinking with dissolve
    pause
    show priya f_normal_talk a_dressed_crossed with dissolve
    priya "Вы готовы подвергнуть себя нескольким испытаниям?"
    show priya f_normal
    show player 10
    player_name "Ох, конечно."
    show player 5
    show priya f_normal_talk
    priya "Все это строго неофициально, заметьте."
    show priya f_normal
    show player 10
    player_name "Меня это вполне устраивает."
    show player 5
    show priya f_normal_talk
    priya "Я не благотворительный человек по своей природе, {b}[firstname]{/b}."
    show priya a_dressed_point with dissolve
    priya "Тем не менее, ваши уникальные обстоятельства, безусловно, окажутся полезными для моего исследования."
    show priya f_thinking a_dressed_thinking with dissolve
    priya "..."
    show priya f_normal_talk a_dressed_point with dissolve
    priya "Сейчас я дам тебе одну бутылочку."
    priya "Возможно, больше, в будущем."
    show priya f_normal a_dressed_crossed with dissolve
    show player 14
    player_name "Это было бы замечательно!"
    show player 13
    show priya f_normal_talk
    priya "... Но только если вы согласитесь вернуться сюда для тестирования."
    show priya f_normal
    show player 14
    player_name "Нет проблем!"
    show player 13
    show priya f_normal_talk a_dressed_point with dissolve
    priya "... И я хочу полный отчет о каждом приеме таблеток."
    priya "Каждую деталь."
    show priya f_normal a_dressed_crossed with dissolve
    show player 10
    player_name "Каждую деталь?"
    show player 5
    show priya f_normal_talk
    priya "Если в какой-то момент я не удовлетворюсь качеством вашей информации или результатами тестирования, сделка заканчивается."
    show priya f_normal
    show player 14
    player_name "Хорошо."
    show player 13
    show priya f_normal_talk
    priya "Есть еще кое-что, что вы должны понять, {b}[firstname]{/b}."
    priya "Мы все еще очень рано в испытании с {b}Pregnax{/b}."
    priya "{b}Вы должны быть осторожны в его использовании{/b}."
    priya "{b}Вполне могут быть побочные эффекты,{/b} о которых мы еще не знаем."
    priya "Хотя, теоретически это должно быть относительно безопасно."
    show priya f_normal
    show player 37 with dissolve
    player_name "{b}глоток{/b} Я... Я понял."
    pause
    show player 13 with dissolve
    show priya f_normal
    priya "Хммм."
    show priya f_normal_talk
    priya "Возвращайся ко мне, если закончатся таблетки."
    priya "Я свяжусь с вами по поводу этих... тестов."
    show priya f_normal
    show player 14
    player_name "Я буду с нетерпением ждать ответа от вас."
    player_name "Спасибо, {b}Доктор Сингх{/b}!"
    show player 13
    show priya f_normal_talk
    priya "Я {b}Прия{/b}."
    show priya f_normal
    show player 30
    player_name "Хмм?"
    show player 5
    show priya f_normal_talk
    priya "Меня зовут {b}Прия{/b}."
    priya "{b}Прия Сингх{/b}."
    show priya f_normal
    show player 30
    player_name "{b}Прия{/b}."
    show player 33
    player_name "Это очень красивое имя!"
    show player 18
    show priya f_rolleyes
    priya "Да, да..."
    show priya f_normal_talk
    priya "Go on, Casanova."
    show priya a_dressed_point with dissolve
    priya "Убирайся из моей лаборатории."
    show priya f_normal
    hide player with dissolve
    pause
    show priya f_facepalm_talk a_dressed_facepalm
    priya "Грр, о чем ты думаешь {b}Прия{/b}?!"
    priya "Ты совсем с ума сошла!"
    show priya f_facepalm
    pause
    show priya f_normal a_dressed_sides with dissolve
    priya "..."
    show priya f_facepalm_talk
    priya "Пожалуйста, пусть он принесет мне хорошие новости..."
    hide priya with dissolve

    scene expression "backgrounds/location_hospital_third_blur.jpg"
    show player 705 with dissolve
    player_name "( Хм, В инструкции сказано, что мне нужно {b}принять одну таблетку до начала сексуальной активности{/b}. )"
    player_name "( {b}Влияние будут продолжаться 24 часа.{/b} )"
    player_name "( {b}Также предупреждающий ярлык, \"Не использует это лекарство если у вашего партнера в настоящее время менструация или менопауза.\"{/b} )"
    hide player with dissolve
    $ player.get_item("fertility_pills")
    $ player.get_item("birth_control_pills")
    $ M_priya.trigger(T_priya_start_testing)
    $ player.go_to(L_hospital_floor3)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
