label church_angelicas_room_mia_church_plan:
    scene church_nun_b
    show player 12 with dissolve
    player_name "( Похоже, это то самое место. )"
    show player 30
    player_name "( Тут должно быть что-то, что я могу надеть... )"
    hide player with dissolve
    return

label church_angelicas_room_mia_return_priest_outfit:
    scene church_nun_b
    show player 14f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "Прошло лучше, чем я ожид-"
    show player 14f at Position (xpos=182)
    show players robe f at left
    show ang 2 at right
    with fastdissolve
    ang "Вот ты где!"
    show ang 1
    show player 23 at Position (xpos=180)
    show players robe
    with fastdissolve
    player_name "!!!" with hpunch
    show player 10
    player_name "Ой, простите!"
    player_name "Я не хотел-"
    show player 11
    show ang 2
    ang "Остановись."
    show ang 1
    show player 22
    player_name "..."
    show ang 2
    ang "Я наблюдала за тобой все это время."
    ang "Кража одежды священника... Выдавать себя за нашего священника на исповеди..."
    ang "...И лгать этой бедной женщине."
    show ang 1
    show player 10
    player_name "Это не то, о чем вы думаете!"
    player_name "Я просто пытался помочь ей..."
    show player 11
    show ang 2
    ang "Помочь?"
    ang "Единственный человек, которому ты можешь помочь, это ты сам..."
    ang "...Потому что я подумываю сообщить о тебе властям."
    show ang 1
    show player 22
    player_name "!!!"
    show ang 2
    ang "Разве что... ты сделаешь кое-что для меня."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "Я не понимаю, как я могу пом-"
    show player 11
    show ang 2
    ang "Если ты согласен, приходи ко мне на неделе."
    ang "Я объясню, что мне от тебя нужно..."
    ang "...И не пытайся скрыться от меня, или все узнают, что ты сделал..."
    ang "...Особенно, та дама. Та, с которой я тебя видела!"
    show ang 1
    show player 10
    player_name "Пожалуйста, не говорите ей ничего... Я прийду. Обещаю."
    show player 11
    show ang 2
    ang "Хорошо."
    ang "А теперь верни то, что украл и покинь мои покои..."
    show ang 1
    hide players robe
    show player 444 at left
    with dissolve
    player_name "..."
    hide player
    hide ang
    with dissolve
    return

label church_angelicas_room_mia_church_night_visit:
    scene church_nun_night_c
    show ang 1 at right
    show player 10 at left
    with dissolve
    player_name "Здравствуйте, {b}Сестра Анжелика{/b}..."
    show player 5
    show ang 2
    ang "Я знала, что могу на тебя рассчитывать."
    ang "Ты соблюдаешь наше согласие... И умеешь хранить секреты."
    ang "Вот почему я надеюсь, что ты мне поможешь..."
    show ang 1
    show player 12
    player_name "И так, о чем конкретно мы говорим?"
    show player 5
    show ang 2
    ang "Я совершаю частное таинство ночью... В своих покоях..."
    show player 11
    ang "Его цель - помочь прихожанам нашей церкви бороться со своими пригрешениями..."
    ang "...Я помогаю им очищаться от своих грехов!"
    show ang 1
    show player 10
    player_name "Грешникам?"
    show player 11
    show ang 2
    ang "Вот именно!"
    ang "Но, чтобы продолжать выполнять это таинство, мне нужно найти подходящих кандидатов..."
    ang "...новеньких из наших прихожан!"
    show ang 1
    show player 10
    player_name "Хорошо, что мне нужно делать?"
    show player 11
    show ang 2
    ang "Мне нужно, чтобы ты нашел кого-нибудь!"
    show ang 1
    show player 10
    player_name "Я нужен вам, чтобы найти кого-то?!"
    show player 11
    show ang 2
    ang "Да, грешников."
    show ang 1
    show player 37 with dissolve
    player_name "..."
    show player 38 with dissolve
    player_name "Но, я и правда не знаю никого такого... Я даже не-"
    show player 3 with dissolve
    show ang 2
    ang "Ты ЗНАЕШЬ кое-кого!"
    show ang 1
    show player 12 with dissolve
    player_name "... Но кого?!"
    show player 11
    show ang 2
    ang "Ту даму из исповедальни."
    ang "Её зовут {b}Елена{/b}."
    ang "Она всегда была набожным служителем нашего {b}Господа{/b}."
    ang "Она считает себя очень добродетельной и ниногда не согласится на мой... ритуал."
    ang "Но ей, похоже, было так стыдно после разговора с тобой в исповедальне."
    ang "Ты знаешь её тайные грехи."
    ang "И ты приведёшь её ко мне."
    ang "Я обожаю персонально очищать по-настоящему верных от греха."
    ang "Это одно из самых... удовлетворяющих... переживаний нашей религии."
    show ang 1
    show player 22
    player_name "!!!"
    show player 10
    player_name "Вы хотите, чтобы я привел {b}Елену{/b} сюда?!"
    show player 11
    show ang 2
    ang "Да, ночью, в мои покои."
    show ang 1
    show player 12
    player_name "Как я смогу убедить её прийти сюда?! Я не знаю, как..."
    show player 11
    show ang 2
    ang "Я уверена что ты найдешь способ."
    ang "Мы оба заинтересованы в этом..."
    show ang 1
    show player 24
    player_name "{b}*вздох*{/b}"
    show player 12
    player_name "Хорошо, я попробую... Но вообще, что это за таинство?"
    show player 5
    show ang 2
    ang "Ты узнаешь, когда придет время."
    show ang 1
    show player 10
    player_name "Мне... Мне пора идти. Уже поздно."
    show player 5
    show ang 2
    ang "Конечно! Только не забудь о нашем соглашении."
    hide ang with dissolve
    show player 24
    player_name "..."
    hide player with dissolve
    return

label church_angelicas_room_mia_church_sacrement:
    scene church_nun_night_c
    show player 5f at right
    show helen 23 at Position (xpos=575)
    show ang 2f at left
    with dissolve
    ang "Спасибо, {b}[firstname]{/b}, за то, что привел нашего замечательного последователя!"
    ang "{b}Елена{/b} посещает нашу церковь уже очень долгое время..."
    ang "...И она рассказала мне всё о её неудачном браке."
    show ang 1f
    show helen 24
    helen "Я... Я просто надеюсь, что это поможет мне разобраться с моими нечестивыми побуждениями..."
    show helen 23
    show ang 2f
    ang "Вот именно, {b}Елена{/b}."
    ang "Я горжусь тем, что ты готова встретиться лицом к лицу со своими демонами."
    ang "Готова ли ты следовать моим указаниям, чтобы обрести свет?"
    show ang 1f
    show helen 24
    helen "Да. Готова..."
    show helen 23
    show ang 2f
    ang "Хорошо! Будут три ступени твоего искупления."
    ang "Первый шаг требует, чтобы ты избавилась от всех земных материй..."
    show player 11f
    ang "...Таких, как {b}твоя одежда{/b}."
    ang "И только тогда мы сможем начать процесс твое очищения от грехов!"
    show ang 1f
    show helen 4 at Position (xoffset=2) with dissolve
    helen "Ты же не ждешь, что я ......здесь разденусь?!"
    show helen 1 at Position (xoffset=2)
    show ang 2f
    ang "Мы {b}Божьи{/b} создания, {b}Елена{/b}... Мы все равны!"
    ang "ты не должна стыдиться того, кто ты есть..."
    show ang 1f
    show helen 25 with dissolve
    helen "..."
    show helen 23
    show ang 2f
    ang "Давай же, {b}Елена{/b}. Избавься от всего этого..."
    show ang 1f
    show helen 27
    pause
    show helen 28
    helen "Если это то, что я должа сделать, тогда я это сделаю..."
    show player 106f
    show helen 21 with dissolve
    pause
    show player 11f
    show helen 22 at Position (xoffset=-13) with dissolve
    pause
    show helen 33 with dissolve
    show player 23f
    player_name "!!!"
    show ang 2f
    show helen 29
    ang "Отлично, {b}Елена{/b}."
    show ang 1f
    show helen 33
    helen "..."
    show ang 2f
    show helen 29
    ang "{b}[firstname]{/b}?"
    show ang 1f
    show helen 31
    show player 21f
    player_name "Эээ... Да?"
    show player 5f
    show ang 2f
    show helen 29
    ang "Теперь ты можешь оставить нас, сегодня мне не нужна твоя помощь"
    ang "Приходи в другой раз, чтобы мы могли продолжить наши занятия..."
    show ang 1f
    show player 10f
    player_name "О, хорошо."
    player_name "Тогда, Спокойной ночи!"
    hide player
    hide helen
    hide ang
    with dissolve
    return

label church_angelicas_room_mia_angelicas_order:
    scene church_nun_night_c with fade
    show player 23f at right
    show helen 29 at Position (xpos=575)
    show ang 5f at left
    with dissolve
    player_name "!!!"
    show ang 6f
    ang "В чем дело, {b}[firstname]{/b}?"
    show ang 7f with dissolve
    pause
    show ang 8f
    ang "У тебя же нет никаких греховных мыслей?"
    show player 22f
    ang "Может, тебе следует занять место {b}Елены{/b} -"
    show ang 7f
    show player 10f
    player_name "Нет! Я... Я просто удивлен, что вы не надели свои одеяния!"
    show player 11f
    ang "..."
    show ang 9 with dissolve
    ang "Я показала {b}Елене{/b} ,как {b}Бог{/b} благословляет своих немногих избранных, которые поистине праведны и набожны и изнутри, и снаружи."
    ang "Как видишь... Он наделил меня по-настоящему священным телом..."
    show ang 10
    pause
    show ang 9
    ang "Верно, {b}Елена{/b}?"
    show ang 10
    show helen 34
    helen "...Да, Госпожа... Ваше тело, это святыня нашего {b}Господа{/b}."
    show helen 33
    show ang 8f with dissolve
    ang "Кроме того, для продолжения очищающего таинства мне требуется возложить руки на эту раскаивающуюся, но развращенную грешницу."
    ang "Я предпочитаю не загрязнять свою одежду..."
    show ang 6f with dissolve
    ang "А теперь если это всё, я должна вернуться к инструктажу {b}Елены{/b}."
    show ang 9 with dissolve
    ang "И если я увижу любые греховные желания, появляющиеся в нижних частях твоего тела, я не буду медлить с {b}Божьим{/b} правосудием..."
    show ang 11
    show player 22f
    player_name "!!!"
    show ang 9
    ang "Ты понял?"
    show ang 10
    show player 138f at Position (xoffset=-16) with dissolve
    player_name "Д... Д... Да... {b}Сестра Анжелика{/b}."
    hide player
    hide ang
    hide helen
    with dissolve
    return

label priest_outfit:
    call expression game.dialog_select("priest_outfit_dialogue")

    $ M_mia.trigger(T_mia_priest_outfit)
    $ game.main()

label priest_outfit_dialogue:
    scene church_nun_b
    show player 444f with dissolve
    player_name "..."
    player_name "( Эта штука тяжелая! )"
    show player 106f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "Хмм..."
    show player 33f at Position (xoffset=1)
    player_name "( Похоже, это действительно может сработать. )"
    show player 14f at Position (xoffset=1)
    player_name "( Посмотрим, смогу ли я стать ближе с {b}Еленой{/b}... )"
    hide player
    hide players robe
    with dissolve
    return

label helen_final_sacrament:
    if store._in_replay == None:
        $ player.remove_item("strapon_drawing")
        $ player.remove_item("strapon")
        $ M_mia.trigger(T_angelicas_final_ritual)
    label helen_final_mc:
        call expression game.dialog_select("helen_final_sacrament_pre")

    if store._in_replay == "helen_final_mc":
        jump expression game.dialog_select("helen_mc_replay")

    elif store._in_replay == "helen_final_sacrament":
        jump expression game.dialog_select("helen_ang_replay")
    menu mia_helen_route_spilt:
        "Трахнуть {b}Елену{/b}.":
            label helen_mc_replay:
                call expression game.dialog_select("helen_final_sacrament_fuck_helen_pre")

            label helen_mc_churchsex:
                call expression game.dialog_select("helen_final_sacrament_fuck_helen_after")

            $ anim_toggle = True
            $ xray = False
            jump expression game.dialog_select("helen_final_sacrament_fuck_helen_loop")
        "Смотреть за {b}Сестрой Анжеликой{/b}.":

            label helen_ang_replay:
                call expression game.dialog_select("helen_final_sacrament_watch_angelica")

            $ anim_toggle = True
            $ xray = False
            jump expression game.dialog_select("helen_final_sacrament_watch_angelica_loop")
    $ game.main()

label helen_final_sacrament_pre:
    scene church_nun_night_c with fade
    show helen whip 1 at left
    show ang 5f at Position (xpos=418)
    show player 12f at right
    with dissolve
    player_name "О, хорошо. Вы, ребята, уже здесь..."
    show player 5f
    show ang 6f
    ang "А где еще мы могли бы быть, {b}[firstname]{/b}?"
    show ang 5f
    show player 34f
    player_name "..."
    show player 35f
    player_name "В церкви, сидя за столом, считать Библию... И надев свою одежду?"
    show player 5f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "Душа {b}Елены{/b} нуждается в большем, чем просто обычное церковное воспинание."
    ang "Ей нужно полностью завершить мой последний ритуал."
    ang "Мы уже завершили предритуальную подготовку..."
    show ang 9 at Position (xoffset=22) with dissolve
    ang "Правда, {b}Елена{/b}?"
    show ang 10 at Position (xoffset=22)
    helen "Да... {b}Сестра Анжелика{/b}..."
    helen "Мое тело... ждет для твоего последнего ритуала."
    helen "Я хочу очиститься..."
    helen "Теперь я понимаю, что мне нужно очиститься... изнутри..."
    show ang 9 at Position (xoffset=22)
    ang "У тебя есть то, что необходимо для проникновения в грешную плоть {b}Елены{/b} ?"
    show ang 10 at Position (xoffset=22)
    show player 239_240f with dissolve
    pause
    show player 457f with dissolve
    player_name "...Это то, что ты хотела, да?"
    show player 458f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "Это... прекрасно."
    ang "Надень на меня."
    show ang 28 at Position (xpos=393) with dissolve
    show player 457f
    player_name "Чего?"
    show player 458f
    show ang 29
    ang "Я что заикалась?"
    show ang 28
    show player 457f
    player_name "Хорошо..."
    hide player
    show ang 30 at right
    with dissolve
    player_name "Хммм..."
    player_name "Думаю, нет простого способа сделать это..."
    hide ang
    show ang 32 at Position (xpos=483)
    with dissolve
    ang "Осторожнее!"
    show ang 31
    pause
    player_name "( ...Ее грудь... )"
    player_name "( ...Такая большая! )"
    show ang 32
    ang "Hey! Mind your fingers down there..."
    ang "I’ve gotten better at using that whip..."
    show ang 31
    player_name "( ... )"
    show ang 33 at Position (xpos=412)
    show player 10f at right
    with dissolve
    player_name "There. It's on."
    show player 5f
    pause
    show ang 34
    ang "А ты знаешь, что у этого страпона есть особая функция?"
    show ang 35 at Position (xoffset=79)
    show player 6f
    pause
    show ang 33
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Что-"
    show player 22f
    show ang 34
    ang "Поторопись и раздевайся."
    show ang 33
    show player 23f
    player_name "Раздевайся?!"
    show player 10f
    player_name "Ты не собираешься использовать это...на-"
    show player 11f
    show ang 34
    ang "Мы все должны пройти последний ритуал очищения."
    show ang 33
    show player 12f
    player_name "Хорошо! Я раздеваюсь!"
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 8bf with dissolve
    pause
    show player 64f
    show ang 37
    pause
    show ang 34
    ang "Ну... Ну..."
    ang "Это может быть интересно..."
    show ang 33
    show player 63f
    pause
    show player 61f at Position (xoffset=-19) with dissolve
    player_name "..."
    show player 68f at Position (xoffset=-19)
    show ang 34f at Position (xpos=475) with dissolve
    ang "{b}Елена{/b}?"
    show ang 33f
    helen "Да, {b}Сестра Анжелика{/b}?"
    show ang 34f
    ang "Иы готова?"
    show ang 33f
    helen "Да."
    helen "Очистите меня, {b}Сестра Анжелика{/b}."
    show ang 34f
    ang "Хорошая девочка."
    ang "Развернись и покажи {b}[firstname]{/b} источник своей похоти..."
    show ang 33f
    show helen whip 3 with dissolve
    pause
    hide helen
    show ang 22f at left
    with dissolve
    pause
    show ang 23f with dissolve
    pause
    show ang 24f with dissolve
    pause
    show ang 25f with dissolve
    pause
    show player 68bf at Position (xoffset=-19)
    player_name "!!!"
    show ang 26f
    ang "Тебе нравится то, что ты видишь, {b}[firstname]{/b}?"
    ang "Её... Мокрую... Послушную... Пизду?"
    show player 65f with dissolve
    pause
    show player 66f with dissolve
    pause
    show player 430bf
    show ang 25bf
    ang "!!!"
    show ang 22_23_24f
    pause
    show ang 26f
    ang "Что такое..."
    show player 430f
    show ang 22_23_24f
    pause
    show ang 26bf
    ang "...Становишься возбужденным?"
    show ang 26f
    ang "Должна сказать, меня впечатлило то, насколько ты был полезен насчет {b}Елены{/b}..."
    show player 67bf
    ang "Ты должен позаботиться о ней..."
    show ang 26bf
    ang "Или, по крайней мере, твоему телу не терпится помочь ей..."
    show ang 22_23_24f
    pause
    show player 430f
    show ang 25f
    helen "Охх..."
    show player 430bf
    player_name "Я... Я не думаю, что она настолько плоха, как вы говорите."
    show player 430f
    show ang 26f
    ang "Приятно слышать..."
    show ang 25f
    pause
    show ang 26f
    ang "Теперь, я уверена, тебе интересно, почему я попросила эту штуку на фотографии."
    ang "Последний шаг моего очищающего таинства требует большего... Жезла правосудия."
    ang "Понимаешь... Чтобы {b}Елене{/b} очиститься и стать единой со своим телом, ей нужно святое семя."
    ang "Его нужно высадить глубоко... Внутри неё!"
    ang "И только тогда сокровенная душа {b}Елены{/b} будет спасена от всех её грехов."
    show ang 22_23_24f
    show player 430bf
    player_name "What do you mean?"
    show player 430f
    show ang 26f
    ang "Я любезно предлагаю тебе выбор, {b}[firstname]{/b}."
    ang "Или ты позволишь мне очистить {b}Елену{/b} и оставить её непорочной, чтобы она смогла вернуться к мужу очищенной..."
    ang "Или..."
    ang "Лучше, ты сам её очистишь..."
    show ang 25f
    show player 67bf
    player_name "..."
    show ang 26f
    ang "Тогда она станет твоей праведной прислужницей, {b}[firstname]{/b}."
    show ang 22_23_24f
    show player 430bf
    player_name "!!!"
    helen "Пожалуйста, трахни меня!!"
    show ang 26f
    ang "{b}Елена{/b} нуждается в одном из нас, чтобы проникнуть в её грешную плоть..."
    ang "...Я оставлю это решение на тебя."
    show ang 25f
    show player 67cf
    player_name "( Если я это сделаю с... {b}Еленой{/b}, тогда родители{b}Мии{/b} опять не будут вместе. )"
    player_name "( И {b}Мия{/b}... {b}Мия{/b} будет очень растроена. )"
    show player 67bf
    show ang 26f
    ang "Так как? Ты поможешь {b}Елене{/b}, или нет?"
    show ang 22_23_24f
    return

label helen_final_sacrament_fuck_helen_pre:
    show player 430bf
    player_name "Я...я... да, я сделаю это."
    show player 430f
    show ang 26f
    ang "Отлично. Твои деяния не останутся незамеченными в глазах {b}Господа{/b}, {b}[firstname]{/b}..."
    ang "...Или моих."
    ang "Давайте же начнем последний ритуал."
    hide ang
    hide player
    with dissolve
    return

label helen_final_sacrament_fuck_helen_after:
    scene church_nun_night_hs_1
    show helens 4_4b
    with fade
    ang "Только кончик, {b}[firstname]{/b}."
    ang "Я хочу, чтобы ты вошел медленно."
    if not M_helen.is_state(S_helen_start):
        ang "Первый раз всегда такой... особый."
    show helens 5 with dissolve
    helen "Охххх, {b}[firstname]{/b}!"
    $ M_helen.set("sex speed", .175)
    show expression AnimatedImage("helens", [6,7,8,9,10], M_helen) as helens with dissolve
    helen "Ахххх... Будь нежным...."
    player_name "Там так...мокро!"
    player_name "Святое де-"
    ang "Ах ах ах. Мы находимся в месте поклонения."
    ang "Хорошо. Теперь войди глубже и не спускай своё семя, пока я не скажу."
    ang "Не забывай, что у меня есть мой кнут..."
    pause
    $ M_helen.set("sex speed", .125)
    ang "Глубже! Быстрее, {b}[firstname]{/b}! Заставь её понять, какая она грешная женщина!"
    ang "{b}Елене{/b} нужно осознать, что теперь она никогда не сможет быть действительно свободна от своего греха!"
    $ M_helen.set("sex speed", .075)
    pause
    return

label helen_final_sacrament_fuck_helen_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("helens", [6,7,8,9,10], M_helen) as helens
            pause 2
            call expression game.dialog_select("helen_final_sacrament_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("helen_final_sacrament_hscene_dialog")
        $ animcounter += 1
    ang "Давай! {b}[firstname]{/b}, кончай для меня!"
    ang "Кончи глубоко в {b}Елену{/b}!"
    call screen final_sacrament_fuck_helen_options

label helen_final_sacrament_hscene_dialog:
    if animcounter == 1:
        player_name "Оххх!!!{p=1}{nw}"

    elif animcounter == 2:
        helen "Ахххх!!!{p=1}{nw}"

    elif animcounter == 4:
        helen "{b}[firstname]{/b}!!!{p=1}{nw}"
    return

label helen_final_sacrament_fuck_helen_cum:
    call expression game.dialog_select("helen_final_sacrament_fuck_helen_cum_pre")
    if not M_helen.is_state(S_helen_start):
        jump expression game.dialog_select("sacrament_complete")

    call expression game.dialog_select("helen_final_sacrament_fuck_helen_cum_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Angelica"]["unlocked"] = True
    $ persistent.cookie_jar["Angelica"]["gallery"]["03_unlocked"] = True
    $ M_helen.trigger(T_helen_route)
    $ M_helen.set("helen route", True)
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label helen_final_sacrament_fuck_helen_cum_pre:
    show helens 11_11b with flash
    player_name "УХХХ!!"
    helen "AХХХХ!!!!"
    show helens 11b with fastdissolve
    helen "Я... Я чуствую себя... Очищенной..."
    show helens 12 with dissolve
    helen "Оххх...так...много..."
    scene black with fade
    pause 1
    return

label helen_final_sacrament_fuck_helen_cum_after:


    scene church_nun_night_c with fade
    show helen whip 2 at left
    show ang 34 at Position (xpos=412)
    show player 5f at right
    with dissolve
    ang "Благословляю тебя, {b}[firstname]{/b}!"
    ang "Тело {b}Елены{/b} снова очищено от её грехов..."
    ang "...И ты только что сделал её своей праведной прислужницей!"
    show ang 33
    show player 10f
    player_name "Что... это значит?"
    show player 5f
    show ang 34
    ang "Ты только что связал желания {b}Елены{/b} с собой."
    ang "Теперь она будет подчиняться твоим командам..."
    show player 11f
    ang "Ты занял место ее мужа в их супружеской постели."
    ang "{b}Елена{/b} теперь потребует ежедневного служения твоего святого семени."
    ang "Чтобы вы сохранили друг друга чистыми и верными."
    show ang 33
    show player 12f
    player_name "Что?!"
    show player 22f
    show ang 34
    ang "Не так ли, {b}Елена{/b}?"
    show ang 33
    helen "Д...да... Теперь я должна служить, {b}[firstname]{/b}."
    helen "Я... приму его святое семя... как покорная и послушная жена."
    show ang 34
    ang "Хорошо, {b}Елена{/b}."
    ang "На этом завершается наше святое таинство. Теперь вы двое можете уйти с миром."
    ang "Я буду продолжать предлагать различные ритуалы причастия в ночное время."
    ang "Приходи если хочешь... участвовать."
    show ang 33
    show player 12f
    player_name "Это замечательно и все такое..."
    show player 10f
    player_name "...Но мне лучше вернуться домой."
    hide player
    hide helen
    hide ang
    with dissolve
    return

label helen_final_sacrament_watch_angelica:
    show player 67cf
    player_name "Я..."
    player_name "Я не могу этого сделать."
    player_name "{b}Елене{/b} нужен её муж, а {b}Мии{/b} нужны её радители."
    show player 67bf
    show ang 26f
    ang "Хорошо, я думаю, я должна быть той, кто спасет {b}Елену{/b}."
    ang "Отойди, {b}[firstname]{/b}."
    show ang 23f
    pause
    show ang 22f
    show player 430f
    player_name "..."
    helen "Спасибо, {b}Сестра Анжелика{/b}..."
    hide ang
    hide player
    with dissolve

    scene church_nun_night_hs_2 with fade
    show helens 13 with dissolve
    ang "{b}Елена{/b}, я с нетерпением ждал этого момента."
    ang "Вы всегда представляли себя самым набожным и благочестивым членом {b}Божьей{/b} паствы."
    ang "Я всегда хотела проникнуть в душу грязного грешника... и не использовать {b}Слово Божье{/b}."
    helen "Ох?"
    ang "Ты больше, чем кто-либо другой..."
    ang "Ты хуже..."
    ang "Ты настоящая шлюха, {b}Елена{/b}."
    ang "Прими мой жезл правосудия!"
    show helens 14 with dissolve
    helen "Оххх!!!"
    ang "Глубже, шлюха!"
    ang "Прими весь!"
    $ M_helen.set("sex speed", .175)
    show expression AnimatedImage("helens", [15,16,17,18,19], M_helen) as helens with dissolve
    helen "Оххх!!!"
    helen "Быстрее! {b}Сестра Анжелика{/b}! Быстрее!"
    $ M_helen.set("sex speed", .125)
    return

label helen_final_sacrament_watch_angelica_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("helens", [15,16,17,18,19], M_helen) as helens
            pause 2
            call expression game.dialog_select("angelica_final_sacrament_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [15,16,17,18,19]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "helens {}".format(pose_list[pose_counter]) as helens
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("angelica_final_sacrament_hscene_dialog")
        $ animcounter += 1
    helen "I'm sooo close!"
    call screen final_sacrament_watch_angelica_options

label angelica_final_sacrament_hscene_dialog:
    if animcounter == 1:
        player_name "Оххх!!!{p=1}{nw}"

    elif animcounter == 2:
        helen "Ахххх!!!{p=1}{nw}"

    elif animcounter == 4:
        helen "{b}Сестра{/b}!!!{p=1}{nw}"
    return

label helen_final_sacrament_watch_angelica_cum:
    call expression game.dialog_select("helen_final_sacrament_watch_angelica_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Angelica"]["unlocked"] = True
    $ persistent.cookie_jar["Angelica"]["gallery"]["02_unlocked"] = True
    $ M_mia.trigger(T_mia_route)
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label helen_final_sacrament_watch_angelica_cum_pre:
    show helens 14 with fastdissolve
    ang "Теперь отпустите свои грехи!"
    ang "Кончи для меня, {b}Елена{/b}!"
    show helens 20 with flash
    helen "ОХХХХХ!!!!!"
    helen "ОХХХХХХХХХХ!!!!"
    show helens 21 with dissolve
    ang "Хорошая шлюшка..."
    scene black with fade
    pause 1



    scene church_nun_night_c with fade
    show helen whip 2 at left
    show ang 34 at Position (xpos=412)
    show player 5f at right
    with dissolve
    ang "{b}Елена{/b} теперь очищена."
    ang "Благодаря моим тренировкам, она стала более покорной."
    ang "{b}Божье{/b} требование всех святых жен к своим мужьям."
    show ang 33

    helen "Спасибо, {b}Сестра Анжелика{/b}."
    show player 11f
    show ang 34
    ang "Что касается тебя {b}[firstname]{/b}, должна сказать, я немного разочарована тобой."
    show player 24f
    ang "{b}Бог{/b} призвал вас на помощь, а вы отвернулись..."
    ang "...Когда ты должен был поделиться своими семенами с {b}Еленой{/b}!"
    show player 5f
    ang "Но, возможно, это и есть вера."
    ang "Спасибо тебе за помощь."
    ang "Я освобождаю тебя от обязанностей и не нуждаюсь больше в твоих услугах."
    show ang 33
    show player 12f
    player_name "Я рад, что наша сделка закончилась."
    show player 10f
    player_name "Я искренне надеюсь, что {b}Елена{/b} будет чувствовать себя лучше после всего этого."
    hide player
    hide helen
    hide ang
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
