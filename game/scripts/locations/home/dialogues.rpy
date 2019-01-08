label home_diane_checkup_results:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Спасибо, что пошел со мной, {b}[firstname]{/b}."
    dia "Ты был так великолепен сегодня!"
    show diane f_normal
    show player 14
    player_name "Без проблем."
    player_name "Я просто рад, что у нас хорошие новости."
    show player 13
    show diane f_normal_talk
    dia "Я тоже."
    hide player
    show diane kiss_casual
    with dissolve
    pause
    show player 13 at left
    show diane b_casual a_casual_sides f_normal_talk
    with dissolve
    dia "Мы начнем завтра, хорошо?"
    show diane f_normal
    show player 14
    player_name "Хорошо."
    show player 13
    show diane f_normal_talk
    dia "Тебе лучше пойти спать и хорошенько выспаться."
    show diane f_wink
    pause
    show diane f_smirk_talk
    dia "Много тяжелой работы ждет тебя завтра, жеребец."
    show diane f_smirk
    show player 29 with dissolve
    player_name "{b}*глоток*{/b} Да, хорошо."
    hide player
    hide diane
    with dissolve
    return

label home_front_mom_mrsj_visit:
    scene home_front
    show debbie 164f zorder 2 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Привет, {b}[deb_char_name]{/b}!"
    show debbie 165f
    show mrsj 14
    deb "О, привет, {b}Тэмми{/b}."
    show debbie 164f
    show mrsj 17
    mrsjo "Я хотел остановиться и выразить свои соболезнования в связи с вашей потерей. Я знаю, что он был твоим близким другом..."
    show debbie 165f
    show mrsj 14
    deb "О, спасибо. Это очень... заботливо с твоей стороны."
    show debbie 169f
    show mrsj 19
    mrsjo "Я просто хочу, чтобы ты знала, что мы с {b}Эриком{/b} рядом, если тебе что-нибудь понадобится."
    mrsjo "... Даже если тебе просто нужно поговорить."
    show debbie 168f
    show mrsj 14
    deb "Это очень щедро."
    show debbie 169f
    show mrsj 17
    mrsjo "Я знаю, что это совершенно другая ситуация для тебя, но я могу рассказать тебе, понимаешь?"
    show debbie 168f
    show mrsj 14
    deb "Ты говоришь, о муже?"
    show debbie 169f
    show mrsj 17
    mrsjo "Конечно!"
    show mrsj 20
    mrsjo "Я имею в виду, мой муж бросил меня... Так что это немного другое."
    show mrsj 18
    mrsjo "... Но я была одна долгое время!"
    show debbie 168f
    show mrsj 14
    deb "Одинокой, не так ли?"
    deb "Нелегко быть совсем одной."
    show debbie 169f
    show mrsj 20
    mrsjo "Да, у меня были тяжелые времена..."
    show mrsj 17
    mrsjo "... Но потом я решила сдать свой дом и стала жить с {b}Эриком{/b}"
    mrsjo "Он был таким благословением!"
    show debbie 168f
    show mrsj 14
    deb "О, как так?"
    show debbie 169f
    show mrsj 17
    mrsjo "Он такой милый молодой человек и он нуждается во мне, чтобы я могла заботиться о нем!"
    show debbie 169bf
    mrsjo "Приятно снова быть нужным. Это дает мне чувство цели в жизни, понимаешь?"
    show debbie 169f
    mrsjo "Я готовлю для него и стираю его вещи. Я спрашиваю его о его дне и проявляю привязанность, когда ему это нужно."
    show debbie 168f
    show mrsj 14
    deb "Понятно..."
    show debbie 169f
    show mrsj 18
    mrsjo "Я думаю, это тоже помогает ему выбраться из скорлупы! Так что это взаимовыгодно!"
    show debbie 168f
    show mrsj 14
    deb "Я просто не знаю, как разговаривать с {b}[firstname]{/b}. Я имею в виду, я знаю, что ему нужно руководство, но я не его мать...."
    show debbie 169f
    show mrsj 17
    mrsjo "Хорошо, держись, дорогая. Это не уладится за одну ночь."
    mrsjo "Сосредоточься на нем и на том, что он чувствует. Я так и сделала!"
    mrsjo "Остальное скоро встанет на свои места."
    show debbie 168f
    show mrsj 14
    deb "Надеюсь ты права."
    show debbie 169f
    pause
    show player 1 zorder 1 at Position(xpos=300) with dissolve
    show debbie 165f
    deb "О! Привет, милый!"
    show debbie 164f
    show player 14
    player_name "Привет, {b}[deb_name]{/b}... Здрасьте, {b}Миссис Джонсон{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Привет, {b}[firstname]{/b}."
    mrsjo "{b}[deb_char_name]{/b} только что говорила мне, как она счастлива, что ты переехал жить к ней..."
    show mrsj 14
    show player 14
    player_name "О, правда? Я просто благодарен, что она согласилась принять меня."
    show mrsj 17
    show player 13
    mrsjo "Она хорошая женщина, так что тебе лучше позаботиться о ней!"
    show mrsj 14
    show player 14
    player_name "Хорошо!"
    show player 1
    show mrsj 17
    mrsjo "Хехе, смотри {b}[deb_name]{/b}? Будет все хорошо!"
    mrsjo "Что ж, мне нужно вернуться домой."
    show mrsj 14
    show debbie 165f
    deb "Ты уверена, что не хочешь войти?"
    show debbie 164f
    show mrsj 17
    mrsjo "Нет, Спасибо! Мне нужно вернуться домой и проведать {b}Эрика{/b}. Может, ему что-нибудь нужно..."
    show mrsj 14
    show debbie 165f
    deb "Что ж, спасибо за беседу {b}Тэмми{/b}. Приходите к нам снова!"
    show debbie 164f
    show mrsj 17
    mrsjo "Хорошо! Вы двое заботитесь друг о друге, слышите?"
    hide mrsj
    hide debbie
    hide player
    with dissolve
    return

label home_front_mom_mow_lawn:
    show expression "backgrounds/location_home_grass_cutscene_01.jpg"
    show expression FilteredText("Это намного сложнее, чем я ожидал. Я должен был уделять больше внимания тому, как {b}отец{/b} это делал.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_02.jpg"
    show expression FilteredText("Выглядит не так уж и плохо. Надеюсь, {b}[deb_name]{/b} думает так же.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_grass_cutscene_03.jpg"
    show expression FilteredText("Интересно, как долго она там стоит? Я был так сосредоточен, что не заметил, как она вышла.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    pause 0.5

    scene home_front
    show player 2 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show debbie 1 at right
    with dissolve
    player_name "{b}[deb_name]{/b},Я закончил с газоном."
    show player 203
    show debbie 2
    deb "Я вижу. Выглядит отлично, милый!"
    show debbie 3
    deb "Ты проделал замечательную работу!"
    show debbie 2
    deb "Я горжусь тобой."
    show player 2
    show debbie 1
    player_name "Я просто делал это так, как {b}отец{/b}."
    show player 11
    show debbie 2
    deb "Ну, я уверена, он бы тоже гордился тобой."
    deb "Он всегда старался изо всех сил помочь мне."
    show player 21
    show debbie 1
    player_name "Я тоже, {b}[deb_name]{/b}. Я чувствую, что он этого хочет."
    show player 2
    player_name "Может, теперь пойдем в дом?"
    show debbie 1
    deb "Конечно!"
    scene home_front with None
    show xtra 15 zorder 2 at Position(xpos=520,ypos=754)
    show player 10 zorder 1
    with dissolve
    player_name "{b}*отдышка*{/b}"
    show player 14
    player_name "Вау, это была большая работа!"
    show player 24
    player_name "Мне нужно снять эту вонючую одежду и принять душ сейчас же...."
    show player 4 at Position(xoffset=5)
    player_name "Я должен {b}спуститься вниз, чтобы положить эту одежду в стирку{/b}."
    hide player with dissolve
    return

label home_front_mom_car_fixed:
    scene expression game.timer.image("home_front_mechanic{}_b")
    show jai 2 at left
    show debbie 1 at right
    with dissolve
    jaing "Все должно быть как новенькое, мэм."
    show jai 1
    show debbie 3
    deb "Правда? Это было быстро!"
    show debbie 1
    show jai 2
    jaing "Еще бы!"
    jaing "Я всегда упорно работаю, когда вовлечена красивая женщина!"
    jaing "Просто позвони мне, если будут проблемы."
    jaing "Мне нравится делать маленькие женские модные мультяшки. Понимаешь, о чем я говорю?"
    show jai 1
    show debbie 3
    deb "О, прекрати. Ты такой смешной!"
    deb "Ha Ha Ha."
    show jai 2
    jaing "Гек Гек Гек."
    show jai 1
    show debbie 1
    show player 14 zorder 1
    player_name "Привет, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Вот и он!"
    show debbie 1
    show player 10f with dissolve
    player_name "Ремонт двигателя закончен?"
    show player 5f
    show jai 2
    jaing "Ну, мне пришлось заменить всю эту чертову штуку, но да. Я закончил."
    jaing "Просто еще один день из жизни {b}Цзян{/b} из Car Whisperer. Не нужно меня благодарить."
    show player 11f
    jaing "Гек Гек."
    jaing "Я лучше отправлюсь в путь!"
    show player 5f
    jaing "Просто загляну к тебе под капот, чтобы убедиться, что я не оставил в ней свой инструмент. Понимаешь, о чем я говорю?"
    show jai 1
    show debbie 2
    deb "{b}*гм*{/b} Да, хорошо. Еще раз спасибо!"
    show debbie 1
    show jai 2
    jaing "Никаких проблем, мэм."
    hide jai with dissolve
    show player 13 with dissolve
    show debbie 2
    deb "Хочешь прокатится?"
    show debbie 1
    show player 14
    player_name "Конечно!"
    show player 12
    player_name "Надеюсь, он не пытается нас надуть."
    show player 5
    show debbie 14
    deb "( Он пытался ввернуть все в порядок... )"
    hide player
    hide debbie
    with dissolve
    return

label home_front_mom_car_fixed_check_car:
    scene car_interior
    show debbie car 2b at right
    show player car 1b
    show player_arms car 1
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    deb "Посмотрим..."
    show player car 2b
    show debbie car 1
    hide debbie_arms_car
    with dissolve
    deb "Хмм..."
    show debbie car 2b
    show debbie_arms_car 1
    with dissolve
    deb "Работает!"
    show debbie car 3
    show player car 2
    player_name "Здорово!"
    show player car 1
    show debbie car 2
    player_name "Звучит неплохо."
    show player car 2b
    show debbie car 3b
    deb "Как ты заставил прийти их так быстро?"
    show debbie car 3
    show player car 2
    player_name "Ничего особенного {b}[deb_name]{/b}."
    show player car 5
    player_name "Думаю, я могу быть довольно убедительным..."
    player_name "Я рад видеть, что ты снова улыбаешься..."
    show player car 6
    pause
    show player car 5b
    show debbie car 3b
    show debbie_arms_car 2 with dissolve
    deb "Ааа..."
    deb "Спасибо, милый."
    scene car_interior kiss
    hide player car
    hide debbie_arms_car
    hide player_arms car
    show debbie car 6 at right
    show xtra 30 at right
    with dissolve
    pause
    show player_boner car 1 with dissolve
    pause
    scene car_interior
    show player car 3b
    show player_arms car 2
    show debbie car 3 at right
    show debbie_arms_car 2
    show xtra 30 at right
    show player_boner car 1
    with dissolve
    pause
    show debbie car 4c
    show debbie_arms_car 4 with dissolve
    deb "( !!! )"
    show debbie car 5b
    deb "О!"
    show debbie car 4c
    show player car 4c
    player_name "Извени, {b}[deb_name]{/b}..."
    show player car 3
    show debbie car 5b
    deb "Все хорошо, милый."
    deb "Кажется, у тебя часто получается так , когда я рядом."
    show debbie car 4b
    show debbie_arms_car 2 with dissolve
    deb "Я не уверена должна ли я беспокоится о пользе?"
    show debbie car 3
    show player car 4c
    show player_arms car 1 with dissolve
    player_name "Я знаю... Я действительно стараюсь не делать этого, но ты очень красивая."
    show player car 3
    show debbie car 4
    deb "..."
    show debbie car 5b
    deb "О, милый..."
    hide player_boner car
    show debbie_arms_car 5b at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    deb "Полагаю, это не так уж плохо."
    show debbie car 5
    show player car 4c
    player_name "{b}[deb_name]{/b}?"
    show player car 3
    show debbie car 3b
    deb "Шшш."
    show debbie car 5b
    show debbie_arms_car 5 with dissolve
    deb "Для юношей твоего возраста нормально возбуждаться при первой же возможности."
    show debbie car 5
    show player car 3b
    player_name "{b}*глоток*{/b}"
    show player car 3
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    pause 1.2
    show debbie_arms_car 5 with dissolve
    show debbie car 5b
    deb "Я действительно хотел бы помочь тебе с этим, милый."
    deb "... Но думаю это не правильно."
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558) with dissolve
    show debbie car 3b
    deb "Тебе нужно найти кого-то своего возраста..."
    deb "Кого-то кто станет твоей девушкой. Разве это не здорово?"
    show debbie car 3
    show debbie_arms_car 5c with dissolve
    show player car 5
    player_name "Д-да, хорошо..."
    show player car 5b
    show debbie car 3b
    deb "Договорились."
    show debbie_arms_car 5 with dissolve
    deb "Ты хочешь, чтобы я продолжала?"
    show debbie car 3
    return

label home_front_mom_car_fixed_check_car_little_longer:
    show player car 5
    player_name "Можешь... Можешь продолжить?"
    show player car 2
    player_name "Очень приятно!"
    show player car 2b
    show debbie car 3b
    deb "Хорошо, {b}[firstname]{/b} но я не собираюсь завершать, даже не надейся..."
    show debbie car 3
    return

label mom_car_jerk_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                $ animated = True
        else:

            $ pose_counter = 0
            $ pose_list = [5,"5b","5c","5b"]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1

        if animcounter == 1 or M_mom.get("jerk count") == 1:
            show debbie car 3
        else:
            show debbie car 4
            show player car 4b
        pause 2

        if animcounter == 3 and M_mom.get("jerk count") >= 1:
            show player car 4c
            pause 1
        $ animcounter += 1

    $ M_mom.set("jerk count", M_mom.get("jerk count") + 1)

    if M_mom.get("jerk count") == 2:
        jump expression game.dialog_select("home_front_mom_car_fixed_check_car_finished")
    call screen car_mom_jerk_options

label home_front_mom_car_fixed_check_car_finished:
    if M_mom.get("jerk count") == 2:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_too_much")
    else:
        call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_not_enough")
    call expression game.dialog_select("home_front_mom_car_fixed_check_car_finished_after")
    $ M_mom.trigger(T_mom_car_fun)
    $ game.timer.tick()
    $ game.main()

label home_front_mom_car_fixed_check_car_finished_too_much:
    show player car 3
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "Я... Я не думаю, что я должна продолжать делать это..."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "Но, {b}[deb_name]{/b}-"
    show player car 3
    return

label home_front_mom_car_fixed_check_car_finished_not_enough:
    show player car 4c
    player_name "Думаю, нам стоит остановиться?"
    show player car 4b
    show debbie car 5
    deb "..."
    show player_boner car 1
    hide debbie_arms_car
    show debbie_arms_car 4
    with dissolve
    show debbie car 5b
    deb "Это хорошая идея, Милый."
    show debbie car 5
    show debbie_arms_car 1 with dissolve
    show player car 5
    player_name "... Да."
    show player car 5b
    return

label home_front_mom_car_fixed_check_car_finished_after:
    show debbie car 5b
    deb "Если ты чувствуешь, себя тяжело, ты должен пойти в свою комнату и позаботиться об этом."
    show debbie car 3b
    deb "...Да, милый?"
    show debbie car 3
    show player car 4c
    player_name "... Да, мэм."
    scene black with fade
    hide debbie
    hide debbie_arms_car
    hide xtra
    hide player
    hide player_arms car
    hide player_boner car
    return

label home_front_mom_bad_guys_revisit:
    scene home_front_car
    $ playMusic("<loop 73.5>audio/music_villain.ogg", 1.0)
    show player 11f at right with dissolve
    player_name "!!!"
    player_name "( Снова эта машина! )"
    player_name "( ... с этим подонком, который угрожал {b}[deb_name]{/b}! )"
    hide player
    $ playSound()
    show expression "backgrounds/location_home_entrance_cutscene01.jpg"
	show expression FilteredText("Когда я смотрел в окно, я заметил парня, который доставлял все угрозы.\nПохоже, на этот раз он привел подкрепление.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene02.jpg"
    show expression FilteredText("Я не слышал, что они говорили, но {b}[deb_name]{/b} выглядела испуганной.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    play audio smack
    hide cutscene
    show expression "backgrounds/location_home_entrance_cutscene03.jpg"
    show expression FilteredText("... Затем один из головорезов повалил её на пол!") as cutscene at Position (xpos= 512, ypos= 700)
    with hpunch
    pause
    hide cutscene
    show expression FilteredText("henchman_cs2 3", "Я никак не мог просто стоять и смотреть...\nЯ {b}должен{/b} что-то сделать!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    
	scene home_entrance_fight
    show debbie 40 at Position(xpos=156,ypos=768)
    show henchman2 1 at right
    with dissolve
    python:
        tmp = deb_name.upper()
    player_name "{b}[tmp]{/b}!!"
    show player 205 at Position(xpos=350,ypos=768) with dissolve
    player_name "Что, черт возьми, тут происходит?!"
    show player 204
    deb "{b}[firstname]{/b}, оставь..."
    show player 205
    player_name "Какой мужчина ударит беззащитную женщину?!"
    show player 204
    show henchman2 2
    henchman2 "Не будь глупым, парень. Это тебя не касается."
    show player 205
    show henchman2 1
    player_name "Отвали! Если ты еще раз тронешь ее я-"
    show player 204
    show henchman2 3
    henchman2 "Ха! И что ты сделаешь?!"
    show henchman2 1
    player_name "..."
    show player 205
    player_name "Я вызову полицию и будете иметь дело с-"
    show player 204
    show henchman2 3
    hide debbie with dissolve
    henchman2 "Я так не думаю."
    show henchman2 1
    hide player
    show henchman1 7 at Position(xpos=350,ypos=768) with hpunch
    player_name "Хей! Отпусти меня!"
    show henchman1 8
    hide henchman2
    show henchman2 3 at right
    henchman2 "Ха-ха-ха, полегче, убийца..."
    henchman2 "Твой {b}отец{/b} задолжал нам {b}МНОГО{/b} бабла..."
    henchman2 "{b}Долг{/b} теперь принадлежит вам обоим!"
    show henchman2 2
    henchman2 "... И ты заплатишь. В противном случае..."
    show henchman1 9
    show henchman2 5
    with hpunch
    deb "{b}[firstname]{/b}!!!"
    show henchman2 3
    show henchman1 10 at Position(xpos=340,ypos=768)
    henchman2 "Что касается властей..."
    show henchman2 2
    henchman2 "... Я бы оставил их в покое, если Вы не хотите, чтобы это стало {b}НАСТОЯЩЕЙ{/b} проблеммой!"
    henchman2 "Если вы дорожите своими жизнями, вы {b}принесите деньги{/b} на {b}склад{/b} как вам сказали!"
    show henchman2 4
    henchman2 "Вы же не хотите, чтобы мы возвращались сюда! {b}Все понятно{/b}, дамочка?!"
    show player 184
    show henchman1 6f at left
    show henchman2 2
    with vpunch
    henchman2 "Ладно, пошли из этой помойки."
    $ playMusic()
    hide henchman1
    hide henchman2
    with dissolve
    pause
    hide player
    show debbie 41 at left
    with dissolve
    deb "Полегче, милый. Я держу тебя."
    show debbie 44 at left
    show jenny 39 at right
    with dissolve
    jen "Что тут, черт возьми, происходит?"
    jen "Я слышала крики и-"
    show jenny 40 at Position(xpos=0.885, ypos=1.0) with dissolve
    jen "( !!! )"
    jen "Господи, с ним все в порядке?!"
    show debbie 43
    show jenny 43 at Position(xpos=1.0, ypos=1.0) with dissolve
    deb "С ним все будет в порядке. Просто успокойся..."
    deb "Они ушли."
    show debbie 44
    show jenny 39
    jen "Мы должны позвонить кому-нибудь!"
    show jenny 43
    show debbie 43
    deb "Нет! Мы не можем этого сделать!"
    show debbie 44
    show jenny 39
    jen "Что?! {b}[deb_name]{/b} эти люди вломился сюда и напал на вас!"
    jen "Мы не можем позволить им-"
    show jenny 43
    show debbie 45
    deb "Я сказала {b}НЕТ{/b}, {b}[jen_name]{/b}!"
    show debbie 43
    deb "... Только..."
    deb "Возвращайся в свою комнату и позволь мне разобраться с этим. Ладно?"
    show debbie 44
    show jenny 39
    jen "Я... Хорошо..."
    hide jenny
    with dissolve
    show debbie 41
    deb "Все будет хорошо, милый."
    show debbie 42
    player_name "Прости. Я не смог остановить их, {b}[deb_name]{/b}..."
    show debbie 41
    deb "Не надо извиняться. Это было очень смело с твоей стороны попробовать!"
    deb "Ты пытался защитить нас."
    show debbie 42
    player_name "Что нам делать?"
    show debbie 41
    deb "Не беспокойся об этом сейчас, главное мы в безопасности."
    show debbie 42
    deb "..."
    show debbie 41
    deb "Как у тебя с лицом?"
    show debbie 42
    player_name "У меня болит нос..."
    player_name "... И у меня везде кровь."
    show debbie 41
    deb "Пойдем, приведем тебя в порядок."
    hide debbie with dissolve
    scene shower2
    show debbie 39f at left
    show player 209f
    with dissolve
    deb "Похоже, кровотечение остановилось..."
    show debbie 63f
    deb "Ты должен принять душ, милый."
    deb "Это поможет с опухолью."
    show player 210
    deb "Я принесу тебе чистую одежду."
    show debbie 38f
    hide debbie
    hide player
    scene hallway
    show debbie 38
    with fade
    deb "( ... )"
    deb "( Я чувствую, что должна быть там с ним... Убедиться, что он в порядке. )"
    deb "( Может, будет лучше, если я оставлю его в покое... )"
    deb "( Я просто оставлю его одежду за дверью. )"
    pause
    show debbie 125 with fastdissolve
    deb "( Бедный ребенок. )"
    deb "( Не могу поверить, что он противостоял этим людям... из-за меня. )"
    deb "( Это было самое смелое, что я когда-либо видела! )"
    deb "( Хмм... )"
    deb "( ... Может, мне стоит зайти и проведать его. )"
    deb "( Просто чтобы убедиться, что ему не нужна моя помощь. )"
    scene shower_closeup
    show debbies 26 zorder 2
    with fade
    player_name "Блин... Так вот что значит получить по морде...."
    show debbies 27 with dissolve
    pause
    show debbies_b zorder 1 at Position(xpos=350,ypos=768) with dissolve
    pause
    hide debbies_b
    show debbies 28 at Position(xpos=487,ypos=768)
    with dissolve
    pause
    show debbies 29 at Position(xpos=492,ypos=768)
    player_name "... Мой нос должен быть таким мягким?"
    show debbies 31 at Position(xpos=484,ypos=768) with vpunch
    player_name "{b}[deb_name]{/b}??"
    player_name "Почему ты-"
    show debbies 30
    deb "Шшш, Все хорошо, милый."
    deb "Позволь помочь тебе..."
    show debbies 34
    deb "Ты заслужил это, после того, что ты сделал там."
    show debbies 37_36
    pause 4
    show debbies 34
    deb "Как лицо?"
    show debbies 35
    player_name "Лучше."
    show debbies 34
    deb "Я рада слышать это."
    deb "Я не хочу, чтобы что-то случилось с моим храбрым человечком..."
    show debbies 36
    show debbies 76 with dissolve
    show debbies 41_76
    pause
    show debbies 42 with hpunch
    with dissolve
    deb "Вот, милый, позволь мне помочь тебе."
    show debbies 72
    player_name "... Ты уверена?"
    show debbies 43
    deb "Я уверена, милый. Позволь мне позаботиться о тебе..."
    show debbies 44
    deb "Ты был таким храбрым там. Стоя перед этими людьми защищая нас."
    show debbies 45 with dissolve
    deb "Я горжусь тобой..."
    show debbies 74
    player_name "... Ох, это очень хорошо, {b}[deb_name]{/b}!"
    show debbies 73_74
    pause 4
    show debbies 73
    player_name "{b}[deb_name]{/b}, я кончаю..."
    show debbies 46
    deb "Хорошо, милый, давай!"
    show debbies 47 at Position(xpos=498,ypos=768)
    player_name "!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=498,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Воу, так много..."
    show debbies 44 at Position(xpos=484,ypos=768) with dissolve
    deb "Хороший мальчик..."
    show debbies 34 at Position(xpos=447,ypos=768) with dissolve
    deb "Теперь тебе лучше?"
    show debbies 35 at Position(xpos=447,ypos=768)
    player_name "Оооо, ты понятия не имеешь как лучше..."
    player_name "... Спасибо, {b}[deb_name]{/b}!"
    show debbies 34
    deb "А теперь приведем тебя в порядок."
    scene shower2
    with fade
    show player 261f at left with dissolve
    show debbie 35b with dissolve
    pause
    show player 8 with dissolve
    show debbie 35c with dissolve
    pause
    show player 21 with dissolve
    show debbie 34 with dissolve
    with dissolve
    player_name "{b}[deb_name]{/b}, это было только один раз?"
    show player 1
    show debbie 34
    deb "..."
    show debbie 35
    deb "О, милый... я не знаю."
    show debbie 34
    deb "..."
    show debbie 35
    deb "Я полагаю, мы можем сделать это снова."
    show debbie 36
    deb "Но ты не должен {b}никому{/b} говорить и мы не можем заходить слишком далеко!"
    show debbie 34
    deb "..."
    show debbie 36
    deb "... И мы {b}АБСОЛЮТНО НЕ МОЖЕМ{/b} позволить {b}[jen_name]{/b} узнать об этом!"
    deb "Ты {b}понял{/b}?"
    show debbie 34
    show player 21
    player_name "Я понял, {b}[deb_name]{/b}."
    show debbie 35
    show player 1
    deb "Хорошо..."
    deb "Я должна прибраться внизу..."
    show debbie 36
    deb "Я хочу, чтобы ты подождал пару минут, прежде чем выйти из ванной."
    deb "В противном случае {b}[jen_name]{/b} может что-то заподозрить. Хорошо?"
    show debbie 32
    show player 28
    player_name "Хорошо, {b}[deb_name]{/b}."
    show debbie 33
    show player 1
    deb "Молодчинка."
    hide debbie with dissolve
    pause
    show player 21f at Position(xpos=0.4, ypos=1.0) with dissolve
    player_name "... Вау!"
    player_name "И Это стоило всего одного удара!"
    hide player
    with dissolve
    show popup_debbieshower at truecenter with dissolve
    pause
    hide popup_debbieshower with dissolve
    return

label player_mailbox:
    $ player.go_to(L_home_mailbox)
    $ player.location.call_screen(False)

label player_mailbox_dialogue:
    $ player.go_to(L_home_mailbox)
    scene expression game.timer.image("player_mailbox{}")

    if erik.completed(erik_orcette) and not player.has_item("orcette") and not erik.known(erik_orcette_2) and orcette_mail_lock:
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_pre")
        menu:
            player_name "Пакет адресован мне. Это должна быть {b}игрушка Эрика{/b}."
            "Не открывать.":
                pause
            "Открыть.":


                call expression game.dialog_select("player_mailbox_erik_orcette_completed_open")

        $ player.get_item("orcette")
        $ game.mail["player"] = ""
        call expression game.dialog_select("player_mailbox_erik_orcette_completed_after")

    elif game.mail["player"] == "m_pizza_pamphlet":
        call expression game.dialog_select("player_mailbox_pizza_pamphlet")
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()

    elif game.mail["player"] == "m_newspaper":
        call expression game.dialog_select("player_mailbox_newspaper")
    $ player.location.call_screen(False)

label player_mailbox_erik_orcette_completed_pre:
    player_name "( Мило! Похоже, я первый, кому пришла почта! )"
    return

label player_mailbox_erik_orcette_completed_open:
    show mailbox_item04_c at truecenter
    with dissolve
    pause
    player_name "( Так вот чего он так долго ждал... )"
    player_name "( {b}Орцетте{/b}. )"
    player_name "( Я лучше положу это обратно в коробку. )"
    return

label player_mailbox_erik_orcette_completed_after:
    show unlock38 at truecenter with dissolve
    pause
    hide unlock38
    hide mailbox_item04_c
    with dissolve
    player_name "( Пора отнести это {b}Эрику{/b} пока кто-нибудь не поймал меня с этой штукой. )"
    return

label player_mailbox_pizza_pamphlet:
    player_name "( Это, вероятно, спам.)"
    show expression "objects/object_mailbox_item02_closeup.png" with dissolve
    player_name "( Пицца Тони? Я давно там не был. )"
    player_name "( Я лучше положу это обратно. )"
    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label player_mailbox_newspaper:
    player_name "( Местные новости. Это должно быть интересно... )"
    show expression "objects/object_newspaper.png" with dissolve
    player_name "( Вор все еще на свободе? Можно подумать, они бы уже его поймали... )"
    player_name "( Я лучше положу это обратно. )"
    hide expression "objects/object_newspaper.png" with dissolve
    return

label bad_guys_driveby:
    $ player.go_to(L_home)
    call expression game.dialog_select("bad_guys_driveby_dialogue")
    $ M_mom.trigger(T_mom_bad_guys_watching)
    $ game.main()

label bad_guys_driveby_dialogue:
    scene location_home_driveby_cutscene1
    with fade
    show text "Почему эта машина едет так медленно?" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Секундочку..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_home_driveby_cutscene2
    with fade
    show text "Это тот странный человек, который угрожал мне на днях!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "В чем его проблема..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene location_home_front_day_blur
    show player 11
    player_name "..."
    show player 10
    player_name "Я знаю, что {b}[deb_name]{/b} сказала не беспокоиться об этом..."
    player_name "... Но этот парень действительно пугает меня!"
    show player 11
    player_name "..."
    hide player with dissolve
    return

label home_roxxy_studying_at_mcs:
    scene expression L_home_entrance.background
    show player 13 at left
    show roxxy 1f f at Position (xpos=400)
    show debbie 2 at right
    with dissolve
    deb "Привет, милый!"
    deb "Как дела в шко-"
    show debbie 13
    deb "... О."
    deb "Кто это?"
    show debbie 14
    show player 14
    player_name "{b}[deb_name]{/b}, это {b}Рокси{/b}."
    player_name "Я помогаю ей по французкому языку."
    show player 13
    show debbie 3
    deb "Ну, это хорошо!"
    show debbie 2
    deb "Я рада с вами познакомиться, {b}Рокси{/b}."
    show debbie 1
    show roxxy 1bf
    rox "... Спасибки."
    rox "Я тоже рада с вами познакомиться."
    show roxxy 1f f
    show debbie 2
    deb "Я как раз заканчивала приготовлять ужин."
    deb "Хотите, я принесу вам пару тарелок?"
    show debbie 1
    show player 14
    player_name "Да, это было бы здорово!"
    show player 13
    show roxxy 1bf
    rox "О, я не хочу навязываться..."
    show roxxy 1f f
    show debbie 3
    deb "Пш, совсем нет, дорогая!"
    show debbie 2
    deb "Дети, поднимайтесь и веселитесь!"
    deb "Я принесу вам ужин, как только он будет готов."
    show debbie 1
    show player 14
    player_name "Спасибо, {b}[deb_name]{/b}!"
    hide player
    hide roxxy
    hide debbie
    with dissolve
    scene expression game.timer.image("bedroom{}")
    show player 13 at left
    show roxxy 2 at right
    with dissolve
    rox "Твоя хозяйка очень милая..."
    show roxxy 1
    show player 33
    player_name "Ага, я счастливчик."
    show player 13
    show roxxy 30
    rox "Итак, это твоя комната?"
    show roxxy 1
    show player 10
    player_name "Ага..."
    show player 5
    show roxxy 2
    rox "Ну, симпатичная конура..."
    rox "... Но я думаю, что здесь тоже хорошо."
    show roxxy 1
    show player 14
    player_name "Ха, это был комплимент?"
    show player 13
    show roxxy 2
    rox "Нет. Не глупи."
    show roxxy 1
    show player 10
    player_name "Хорошо, прости."
    player_name "Где будем заниматься?"
    show player 5
    show roxxy 1b
    rox "Кровать выглядит удобной."
    show roxxy 1
    show player 10
    player_name "... Ты хочешь заниматься на кровати?"
    show player 11
    show roxxy 2
    rox "А почему бы нет?"
    show roxxy 1
    show player 29 with dissolve
    player_name "Ладно."
    hide player
    hide roxxy
    with dissolve
    scene expression "backgrounds/location_home_bedroom_bed_dialogue.jpg"
    show player bed 1 at right
    show roxxy 36b at left
    show roxxy_outfit at left
    with dissolve
    rox "Ну..."
    show roxxy 35b
    rox "..."
    show roxxy 35e
    rox "У тебя здесь часто бывают девушки?"
    show roxxy 35d
    show player bed 3
    player_name "Хах?"
    player_name "... Нет, не совсем."
    show player bed 2
    show roxxy 35e
    rox "Это первый раз, когда у тебя на кровати девушка?"
    show roxxy 35d
    player_name "..."
    show player bed 3
    player_name "... Нет?"
    show player bed 2
    show roxxy 35e
    rox "Ты же не девственник?"
    show roxxy 35d
    show player bed 6
    player_name "!!!" with hpunch
    show player bed 3
    player_name "Что?!"
    player_name "Это не так... В смысле, мне не очень комфортно..."
    show player bed 2
    player_name "..."
    show player bed 5
    player_name "А ты?"
    show player bed 4
    show roxxy 35c
    rox "Пфф!"
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Ха-ха, как будто я тебе скажу! Я просто смеюсь!"
    show roxxy 35e at left
    rox "Я говорила тебе, учеба - моя не сильная сторона."
    show roxxy 35d
    show player bed 5
    player_name "Ой, да ладно. Ты даже не пробовала."
    player_name "Я думаю, ты умнее, чем считаешь, {b}Рокси{/b}."
    show player bed 4
    show roxxy 38b
    rox "..."
    show roxxy 36 at Position (xoffset=120, yoffset=-100)
    rox "Ччч, без разницы..."
    show roxxy 35b
    show player bed 5
    player_name "Я серьезно!"
    show player bed 4
    rox "..."
    show roxxy 35c
    rox "У тебя когда-нибудь была девушка?"
    show roxxy 35b
    show player bed 6
    player_name "!!!" with hpunch
    player_name "..."
    show player bed 3
    player_name "Почему ты спрашиваешь меня об этом?"
    show player bed 2
    show roxxy 37 at Position (xoffset=120, yoffset=-100)
    rox "Хаха, скатища..."
    show roxxy 35b
    show player bed 5
    player_name "Смотри, я покажу тебе трюк чтобы сделать обучение более интересным..."
    show player bed 4
    show roxxy 40 at Position (xoffset=120, yoffset=-100)
    rox "Пфф, ага."
    show roxxy 35b
    show player bed 5
    player_name "Смотри!"
    hide player
    hide roxxy
    hide roxxy_outfit
    with dissolve
    scene expression "backgrounds/location_home_bedroom_cutscene10.jpg"
    with fade
    show text "Я провел часы, пытаясь уговорить {b}Рокси{/b} учиться.\nВ основном она просто наблюдала за моей работой и задавала неудобные вопросы о моем опыте с девушками.\n... Но в конце концов мне удалось научить ее тому, что ей нужно знать." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression L_home_entrance.background
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "Так что, я думаю, нам, возможно, придется сделать это снова когда-нибудь, да?"
    show player 5
    show roxxy 2
    rox "Будем надеяться, что нет!"
    show roxxy 1
    show player 12
    player_name "Ой, да ладно... Это было не так уж и плохо!"
    show player 5
    rox "..."
    show roxxy 1b
    rox "... Нет, все было не так уж плохо."
    rox "Только..."
    show roxxy 1
    rox "..."
    show roxxy 1b
    rox "Спасибо ... За то, что было все круто..."
    show roxxy 1
    show player 13
    player_name "..."
    rox "..."
    show roxxy 2
    rox "... Почему ты так смотришь на меня?"
    show roxxy 1
    show player 29 with dissolve
    player_name "П-прости... Это просто... Я не привык к тому, что ты такая милая..."
    show player 3
    show roxxy 2
    rox "... Ну не привыкайте к этому!"
    rox "Ты все еще придурок, и я буду относиться к тебе так и в школе!"
    show roxxy 28 with dissolve
    rox "... но."
    show roxxy 27
    rox "..."
    hide player
    show roxxy 59 at left with dissolve
    player_name "!!!" with hpunch
    show player 11 at left
    show roxxy 1e at right
    with dissolve
    player_name "..."
    show player 10
    player_name "Что это было?"
    show player 11
    show roxxy 1b
    rox "... Просто небольшая благодарность."
    show player 13
    rox "Ничего более!"
    show roxxy 2
    rox "Не думай, что это что-то значит!"
    show roxxy 1
    player_name "..."
    show player 29 with dissolve
    player_name "... Ладно."
    player_name "Я провожу тебя домой."
    show player 3
    show roxxy 1b
    rox "Нет, со мной все будет хорошо."
    rox "Пока, ботан!"
    hide roxxy with dissolve
    pause
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "Свиньи должны куда-то лететь..."
    hide player with dissolve
    return

label home_front_roxxy_cookies_and_milk:
    scene expression L_home_entrance.background
    show player 5 at Position (xpos=400)
    show roxxy 32f at left
    show debbie 13 at right
    with dissolve
    deb "{b}[firstname]{/b}?"
    deb "Что ты делаешь дома так рано?"
    show debbie 14
    show player 10
    player_name "Привет, {b}[deb_name]{/b}."
    player_name "У моего друга сегодня очень тяжелый день."
    show player 5
    show debbie 13
    deb "О!"
    show debbie 2
    deb "Привет опять, дорогая..."
    show debbie 1
    show player 10
    player_name "Я привел ее сюда, чтобы поговорить."
    player_name "... И я предложил ей обед."
    player_name "Надеюсь, все в порядке?"
    show player 5
    show debbie 3
    deb "Конечно, все в порядке!"
    show debbie 2
    deb "... Тебя зовут {b}Рокси{/b}, да?"
    show debbie 1
    show roxxy 33f
    rox "Да, мэм."
    rox "Извините за неудобства ..."
    show roxxy 32f
    show debbie 3
    deb "Это не проблема, дорогая!"
    show debbie 2
    deb "Почему бы вам не отправиться наверх, а я что-нибудь приготовлю для вас."
    show debbie 1
    show player 14
    player_name "Спасибо, {b}[deb_name]{/b}."
    scene black with fade
    pause

    scene expression game.timer.image("backgrounds/location_home_bedroom_day{}.jpg")
    show player 5 at left
    show roxxy 1l
    with dissolve
    rox "Твоя {b}Хозяйка{/b} когда-нибудь носила одежду?"
    show roxxy 1k
    show player 10
    player_name "А?"
    player_name "Что ты имеешь в виду?"
    show player 5
    show roxxy 1i
    rox "..."
    show roxxy 1l
    rox "... Неважно."
    show roxxy 30 at Position (xoffset=-33) with dissolve
    rox "Фу, это катастрофа..."
    rox "Что, черт возьми, я собираюсь делать!"
    show roxxy 29 at Position (xoffset=-33)
    show player 10
    player_name "Успокойся, {b}Рокси{/b}."
    player_name "Нет смысла волноваться, пока мы не выясним все детали."
    show player 5
    show roxxy 3c at Position (xoffset=-33)
    rox "Что ты имеешь в виду?"
    show roxxy 3d at Position (xoffset=-33)
    show player 10
    player_name "Все, что мы знаем, это то, что {b}твоя мама{/b} была арестована за хранение и что полиция ведет расследование."
    player_name "Возможно, еще есть способ исправить ситуацию."
    show player 5
    show roxxy 1k with dissolve
    rox "..."
    show roxxy 1l
    rox "Ты правда так думаешь?"
    show roxxy 1k
    show player 10
    player_name "... Возможно."
    player_name "Мы должны сходить в {b}полицейский участок{/b} и выяснить, что именно происходит."
    show player 5
    show roxxy 27
    rox "..."
    show roxxy 1l
    rox "Ты прав..."
    show roxxy 1k
    rox "..."
    show player 10
    player_name "А пока просто дыши и расслабься."
    player_name "Я уверен, мы сможем найти способ исправить все."
    show player 5
    show roxxy 1l
    rox "... Почему ты так добр ко мне?"
    show roxxy 1k
    show player 10
    player_name "Хух?"
    player_name "Я..."
    show player 5
    show debbie 218 at right with dissolve
    deb "Я принесла перекусить!"
    show roxxy 1kf at Position (xpos=400) with dissolve
    show player 13
    show debbie 217
    deb "Немного свежего молока и печенки..."
    deb "Это идеальная вещь, чтобы ты чувствовала себя лучше после тяжелого дня, {b}Рокси{/b}!"
    show debbie 219 with dissolve
    show roxxy 27f at Position (xoffset=33)
    show player 428
    pause
    show roxxy 1bf with dissolve
    rox "{b}*фырк*{/b} О, вау!"
    show debbie 1 with dissolve
    show player 11
    rox "Выглядит прекрасно, мэм!"
    show roxxy 1f f
    show debbie 3
    deb "О, ну спасибо тебе, дорогая."
    show roxxy 32f at Position (xoffset=-34)
    show player 13
    with dissolve
    deb "Рецепт был в моей семье на протяжении нескольких поколений!"
    show debbie 14b
    show roxxy 27f at Position (xoffset=33)
    deb "..."
    show debbie 13
    deb "У тебя тушь потекла, дорогая..."
    show player 5
    show debbie 14b
    show roxxy 33f at Position (xoffset=-34)
    rox "{b}*фырк*{/b} О, простите..."
    show roxxy 33bf with dissolve
    pause
    show debbie 13
    deb "Тут нечего извеняться!"
    show roxxy 32f at Position (xoffset=-34)
    deb "Вы, ребятки, просто ешьте и дайте мне знать, если я могу еще что-нибудь сделать для вас."
    deb "Я просто ненавижу видеть такую красавицу, как ты, расстроенной..."
    show debbie 14
    show player 13
    show roxxy 33f at Position (xoffset=-34)
    rox "... Спасибо, мэм."
    show roxxy 32f at Position (xoffset=-34)
    show debbie 2
    deb "Пожалуйста, зови меня {b}[deb_name]{/b}, дорогуша."
    hide debbie with dissolve
    rox "..."
    show roxxy 33 at center with dissolve
    rox "Спасибо за все {b}[firstname]{/b}..."
    show roxxy 32
    show player 14
    player_name "В любое время!"
    show player 13
    show roxxy 33b
    rox "{b}*фырк*{/b}."
    show roxxy 32
    show player 10
    player_name "Давайте поедим, а затем мы отправимся в {b}полицейский участок{/b} и разберемся."
    show player 13
    show roxxy 33
    rox "... Да, давай."
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
