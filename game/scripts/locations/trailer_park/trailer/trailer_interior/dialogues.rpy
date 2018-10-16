label trailer_park_first_visit:
    scene expression game.timer.image("trailer_interior{}")
    show player 10 with dissolve
    player_name "( Вот тут {b}Roxxy{/b} и живет? )"
    player_name "( Здесь же полно всякого мусора... )"
    hide player with dissolve
    return

label trailer_interior_roxxy_get_cheerleader_outfit:
    scene trailer_interior_c
    show roxxy 1f f at Position (xpos=400)
    show player 5 zorder 1 at left
    show crystal 3 at right
    with dissolve
    crys "Какого хрена ты делаешь дома?!"
    crys "Ты же знаешь, что больше не можешь пропускать школу!"
    show crystal 1
    show roxxy 3f
    rox "Угх, расслабься!"
    rox "Мне просто нужно забрать кое-то..."
    show roxxy 1f f
    show crystal 2
    crys "... И, как я вижу, ты привела своего милого бойфренда!"
    show player 13
    show crystal 4 with dissolve
    show roxxy 2f
    rox "... Он не мой бойфренд!"
    show player 5
    show crystal 1 with dissolve
    rox "Я просто не хотела сама идти по городу!"
    show roxxy 1f f
    show crystal 2
    crys "Ну, раз уж он не твой бойфренд - пусть тогда будет моим!"
    show player 22
    crys "Хахахаха!"
    show crystal 1
    show roxxy 3f
    rox "... Угх, заткнись {b}Мам{/b}!"
    hide roxxy with dissolve
    show player 5
    show crystal 3
    crys "... Ну и какие у тебя намерения?"
    show crystal 1
    show player 10
    player_name "... А?"
    show player 5
    show crystal 2
    crys "Ну знаешь, намерения?!"
    crys "Собираетесь развлекаться без всяких обязательств?"
    show crystal 1
    show player 21
    player_name "Что?! Нет, мэ'эм!"
    player_name "Я просто помогаю ей с  уроками."
    show player 5
    show xtra 21 zorder 2 at left
    show crystal 2
    crys "Хаха, да не смущайся ты так!"
    show crystal 3
    crys "Я просто интересуюсь..."
    show crystal 2
    crys "Если собираешься развлекаться с моей дочерью..."
    show player 22
    crys "... Хотя бы найди нормальную работу!"
    crys "Нам здесь ещё один иждивенец не нужен."
    show crystal 1
    hide xtra
    show player 21
    player_name "... Мэм, мы правда просто друзья."
    show xtra 21 zorder 2 at left
    show player 5
    show crystal 3
    crys "Хехе, а ты покраснел..."
    crys "Клянусь, ты милее всех, кого я знала!"
    show crystal 4
    show roxxy 3cf zorder 0 at Position (xpos=400)
    with dissolve
    rox "Ты никуда не перекладывала мою {b}Чирлидерскую униформу{/b}?"
    show roxxy 3df
    show crystal 2 with dissolve
    crys "... Не помню такого."
    show crystal 1
    show roxxy 3f
    rox "Я не могу её найти!"
    show roxxy 3df
    show crystal 2
    crys "И что я должна сделать?"
    show crystal 1
    show roxxy 3f
    rox "Угх, ничего {b}Мам{/b}... Просто сиди на жопе ровно и продолжай бухать."
    rox "... Как ты обычно и делаешь."
    show roxxy 3df
    show crystal 3
    crys "{b}Roxxy{/b}!"
    crys "Я ведь говорила тебе не разговаривать так со мной!"
    crys "Я занимаюсь тут многими делами."
    show roxxy 2bf
    crys "Вот только сегодня утром заходил твой кузин и мы-"
    show crystal 1
    show roxxy 2cf
    show player 11
    rox "Стоп!"
    rox "{b}Clyde{/b} был здесь сегодня утром?!"
    show roxxy 2bf
    show crystal 2
    crys "... Ага."
    show crystal 1
    show roxxy 3f
    rox "Черт!"
    rox "Он опять бухал прямо на своем тракторе??"
    show roxxy 3df
    show crystal 2
    crys "Да откуда я знаю?!"
    show crystal 1
    show roxxy 3cf
    rox "Угх, пошли со мной {b}[firstname]{/b}..."
    hide roxxy
    hide player
    hide xtra
    with dissolve
    show crystal 2
    crys "... Эту девченку нужно отлупить."
    show crystal 4 with dissolve
    pause
    scene black with fade
    return

label trailer_interior_crystal_sex_offer_pre_first:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 13 at left
    show crystal 2 zorder 1 at right
    with dissolve
    crys "Кто тут у нас... Это ведь новый парень {b}Roxxy{/b}..."
    show crystal 4 with dissolve
    show player 10
    player_name "Эм, парень?"
    show player 5
    show crystal 2 with dissolve
    crys "Хочешь снова засадить моей дочке?"
    show crystal 1
    show player 10
    player_name "... Засадить?"
    show player 12
    player_name "Я не совсем понимаю о чем вы, мэм."
    show player 5
    show crystal 2
    crys "Мэм?"
    show crystal 2b
    crys "Хахахаха!!"
    crys "Меня ещё никто не называл \"Мэм\"..."
    show crystal 2
    crys "Зови меня просто {b}Crystal{/b}."
    show crystal 3 with dissolve
    crys "... А по поводу засаживания..."
    show crystal 3b_3c with dissolve
    pause
    show player 22
    player_name "!!!" with hpunch
    show crystal 4 with dissolve
    show player 29 with dissolve
    player_name "Ох! Я не..."
    show crystal 1 with dissolve
    player_name "В смысле мы не..."
    show player 3
    show crystal 2b
    crys "Хахахаха!"
    show crystal 3 with dissolve
    crys "Конечно же вы да!"
    show crystal 2 with dissolve
    crys "Думаешь, я могла тут чего-то не услышать?!"
    show player 22 with dissolve
    crys "В этом трейлере ты никогда не добьешься хоть какого-нибудь уединения!"
    show crystal 1
    show player 21
    player_name "Хех, да. Наверное вы правы."
    player_name "Извините."
    show player 5
    show crystal 2
    crys "О, тут не за что извиняться."
    crys "{b}Roxxy{/b} должна прислушаться ко мне и перестать трахаться с парнями по одному разу."
    show crystal 1
    show player 10
    player_name "Ага, эмм... Она вообще здесь?"
    show player 5
    show crystal 2
    crys "Боюсь, что нет..."
    show crystal 1
    show player 10
    player_name "... Ох."
    show player 36
    player_name "Ладно, тогда я не буду вам мешать-"
    hide player
    show crystal 17 at left
    with dissolve
    crys "Ну, не нужно так спешить..."
    crys "Я не совру, если скажу, что ты прекрасно заботишься о моей дочери, {b}[firstname]{/b}..."
    show crystal 17b
    player_name "Эм..."
    show player 106 zorder 0 at left
    show crystal 16c at Position (xpos=134)
    with dissolve
    crys "Он ведь помогает тебе избавляться от всего это яда?"
    show crystal 16d
    show player 108f
    player_name "Яда?"
    show player 109f
    show crystal 16c
    crys "Хехе, да..."
    show crystal 18_18b
    show crystal_talking_head zorder 2
    with dissolve
    crys "Для молодых парней крайне важно избавляться от этого."
    hide crystal_talking_head
    show player 106
    player_name "!!!"
    show player 108f
    player_name "Что вы имеете в-"
    show player 109f
    show crystal_talking_head zorder 2
    crys "Шшш, всё в порядке..."
    crys "Я тоже не против помочь."
    hide crystal_talking_head
    show player 10
    player_name "... А {b}Roxxy{/b}?!"
    show player 5
    show crystal_talking_head zorder 2
    crys "Ох, да не волнуйся ты о {b}Roxxy{/b}..."
    crys "Ей не навредит то, о чем она не узнает."
    hide crystal_talking_head
    show player 5
    player_name "..."
    show crystal undress 1 at center with dissolve
    pause
    show crystal undress 2 with dissolve
    show player 428
    crys "Просто позволь {b}Crystal{/b} тебе помочь..."
    show crystal undress 3 with dissolve
    show player 427
    player_name "{b}*Глоть*{/b}"
    show player 428
    show crystal undress 4 with dissolve
    crys "Как только ты это прочувствуешь, уже никогда не захочешь бросить мою девочку!"
    show player 426
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7 at right with dissolve
    crys "... Просто дай {b}Мамочке{/b} этого прекрсного мужского мяса..."
    show crystal undress 7b
    show player 427
    player_name "Ох, я не..."
    show player 426
    show crystal undress 7
    crys "Хехе, не нужно так стесняться."
    show crystal undress 10 with dissolve
    crys "Я мечтаю прокатиться на этом огромном члене уже достаточно долго."
    crys "У меня от этих мыслей там просто водопад!"
    show crystal undress 10b
    player_name "..."
    show crystal undress 10
    crys "А может.."
    crys "... Ты предпочтешь мой черный вход?"
    show crystal undress 9 with dissolve
    show player 427
    player_name "Ха?"
    player_name "Вы это о чем-"
    show player 428
    show crystal undress 11_11b
    player_name "!!!" with hpunch
    crys "Ты можешь использовать меня так, как сам пожелаешь, {b}[firstname]{/b}!"
    show player 429
    player_name "С-серьезно?"
    show player 426
    crys "Мммм!"
    return

label trailer_interior_crystal_sex_offer_pre_repeat:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 10 at left
    show crystal 1 at right
    with dissolve
    player_name "По поводу того, что вы говорили ранее..."
    show player 5
    show crystal 2
    crys "Ох, так ты наконец-то решился?"
    show crystal 1
    show player 24
    player_name "..."
    show crystal undress 1 with dissolve
    crys "Ты об этом не пожалеешь."
    show crystal undress 3 with dissolve
    show player 428
    crys "Если я в чем-то хороша - так это в ублажении мужчин..."
    show crystal undress 4 with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7b
    player_name "!!!" with hpunch
    show crystal undress 7
    crys "Хехе!"
    crys "... Ты даже не представляешь, как сильно я этого хочу, {b}[firstname]{/b}!"
    show crystal undress 9 with dissolve
    show player 426
    player_name "..."
    show crystal undress 11_11b with dissolve
    crys "Ммм, может позволишь мне руководить?"
    return

label trailer_interior_crystal_sex_offer_menu:
    menu:
        "Окей...":
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_accept")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "Я не могу..." if not M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_first")
            $ M_crystal.set("crystal sex offer denied", True)

        "Я всё ещё не могу..." if M_crystal.is_set("crystal sex offer denied"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_denied_repeat")
    $ game.main()

label trailer_interior_crystal_sex_offer_accept:
    show player 429
    player_name "О-окей."
    show player 426 zorder 2
    show crystal undress 10 with dissolve
    crys "Вот это дух!"
    crys "Возьми меня как сам того хочешь!"
    show crystal undress 10b
    return

label trailer_interior_crystal_sex_offer_denied_first:
    show player 24
    player_name "Я..."
    show crystal undress 9 with dissolve
    crys "Хаха, давай милый, не заставляй меня умолять об этом..."
    show player 37 with dissolve
    player_name "Не могу..."
    show crystal undress 8 with dissolve
    crys "Хмм?"
    crys "... Что значит, не могу?!"
    crys "Это не сложно! Просто достань этого плохого парня и выбери дырку..."
    show crystal undress 8b
    show player 12 with dissolve
    player_name "Нет, я имею ввиду... Я не могу так поступить с {b}Roxxy{/b}..."
    show player 5
    show crystal undress 8
    crys "Пфф, я же сказала. {b}Roxxy{/b} ничего не узнает!"
    show crystal undress 8b
    show player 10
    player_name "Да, но я-то буду знать..."
    show player 12
    player_name "... И я не хочу быть одним из таких парней."
    show player 5
    show crystal undress 6 with dissolve
    crys "..."
    show crystal undress 5 with dissolve
    pause
    show crystal undress 4 with dissolve
    crys "Ох, знаешь... А ты и правда хороший малый."
    show crystal undress 2 with dissolve
    crys "Я не представляю, как в этом мире {b}Roxxy{/b} смогла наткнуться на тебя..."
    show crystal undress 1 with dissolve
    crys "{b}*Вздох*{/b}"
    show crystal 6 with dissolve
    crys "Как хочешь..."
    crys "... Но предложение всё ещё в силе. Может когда-нибудь передумаешь."
    show crystal 16
    crys "Ммм, я буду ждать."
    show crystal 14
    show player 11
    player_name "..."
    hide crystal with dissolve
    show player 10
    player_name "... Что ж, это было неловко."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_offer_denied_repeat:
    show player 24
    player_name "Я..."
    show player 25
    player_name "Прости, {b}Crystal{/b}. Но я не могу..."
    show crystal undress 9 with dissolve
    crys "..."
    show crystal undress 6 with dissolve
    crys "Я не люблю, когда меня дразнят, {b}[firstname]{/b}!"
    show crystal undress 5 with dissolve
    show player 10
    player_name "... Прости."
    show player 5
    show crystal undress 5 with dissolve
    pause
    show crystal undress 1 with dissolve
    crys "Как хочешь."
    show crystal 6 with dissolve
    crys "Ты знаешь, где меня найти, если вдруг передумаешь."
    hide crystal with dissolve
    player_name "..."
    hide player with dissolve
    return

label trailer_interior_crystal_sex_or_anal_menu:
    menu:
        "Sex.":
            $ M_crystal.set("crystal anal", False)
            if M_roxxy.get("roxxy crystal sex") and not L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_first")

            elif L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_outside")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_sex_repeat")
        "Anal.":

            $ M_crystal.set("crystal anal", True)
            if M_roxxy.get("roxxy crystal sex") and not L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_first")

            elif L_trailer.is_here(M_crystal):
                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_outside")
            else:

                call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_choose_anal_repeat")
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_first:
    show crystal undress 10 with dissolve
    crys "О да, малыш."
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Ммм, дай мне этого монстра!"
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show crystals cum 2 with dissolve
    crys "!!!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_outside:
    show crystal undress 10 with dissolve
    crys "Ладно, малыш."
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Помни, я хочу его как можно глубже..."
    pause
    hide crystal

    scene expression "backgrounds/location_trailer_sex_night.jpg"
    show crystals insert 1
    show trailer_counter_night at right
    with dissolve
    crys "Ммм..."
    show crystals cum 2 with dissolve
    crys "Какой большой парень!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    crys "Вот так..."
    crys "На всю аплитуду..."
    pause
    crys "Mmm..."
    pause
    crys "Аахх!"
    pause
    crys "Заполни меня всю, {b}[firstname]{/b}!"
    return

label trailer_interior_crystal_sex_or_anal_choose_sex_repeat:
    show crystal undress 10
    crys "Давай же!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12
    with dissolve
    crys "Mmm, мне не нужен этот петтинг, {b}[firstname]{/b}..."
    crys "Дай мне его полностью!"
    player_name "Д-да, мэм..."
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    pause
    show crystals cum 2
    crys "О боже!" with hpunch
    crys "Этот член неповторим!"
    crys "Фух!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_first:
    show crystal undress 10 with dissolve
    crys "Mmm!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    crys "Вставь этого монстра мне в зад!"
    hide player
    show crystal undress 12b
    with dissolve
    pause
    hide crystal

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1 at left
    show trailer_counter at right
    with dissolve
    player_name "Готова?"
    crys "Давай уже!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "NGGHHH!!!"
    pause
    player_name "Вы трясетесь..."
    crys "..."
    player_name "Мэм?"
    crys "Заткнись и продолжай!"
    player_name "O-окей!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_outside:
    show crystal undress 10 with dissolve
    crys "Ох, я надеялась, что ты это скажешь!"
    show crystal undress 10b
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12b
    with dissolve
    crys "Ммм, да, во так..."
    hide crystal

    scene expression "backgrounds/location_trailer_sex_night.jpg"
    show crystals insert 1 at left
    show trailer_counter_night at right
    with dissolve
    crys "Давай, порадуй мамочку!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "Fuuuuuuu-"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    pause
    crys "Боже мой!"
    player_name "Шшш!!"
    player_name "Вы должны быть потише, или {b}Roxxy{/b} нас услышит!"
    pause
    crys "{b}*Скулит*{/b}"
    pause
    crys "Оохх, так глубоко!"
    crys "Ахх, еби меня в зад, {b}[firstname]{/b}!"
    player_name "Шшш!!"
    return

label trailer_interior_crystal_sex_or_anal_choose_anal_repeat:
    crys "Ох, я надеялась, что ты это скажешь!"
    show player 429
    player_name "Правда?"
    show player 426
    crys "А то!"
    crys "Не пойми меня неправильно."
    crys "Мне нравится обычный секс..."
    crys "... Но самые мощные оргазмы я получаю лишь тогда, когда меня имеют в жопу!"
    crys "Так всегда было."
    show player 427
    player_name "... Серьезно?"
    show player 426
    crys "Mmmmm!"
    show crystal undress 10 with dissolve
    crys "Давай, просто засунь его туда и сам увидишь."
    show crystal undress 10b
    show player 429
    player_name "O-oкей..."
    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show player crystal 13 with dissolve
    pause
    hide player
    show crystal undress 12b
    with dissolve
    crys "Вот оно..."

    scene expression "backgrounds/location_trailer_sex.jpg"
    show crystals insert 1
    show trailer_counter at right
    with dissolve
    crys "Не бойся прилагать усилия!"
    crys "Я смогу полностью его принять!"
    show crystals cum 2
    crys "!!!" with hpunch
    crys "Ооох, Боже мой!"
    $ M_crystal.set("sex speed", .175)
    show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
    with dissolve
    crys "NNGGGHHH!!!"
    crys "Господи, как же глубоко!"
    pause
    crys "Такое чувство, что ты сломаешь мне позвоночник!"
    player_name "Мне перестать?!"
    crys "GGRRRAAAHHH!!!"
    player_name "{b}Crystal{/b}!"
    crys "КАК ЖЕ ХОРОШО!!!"
    crys "Давай же, еби меня сильнее!"
    pause
    $ M_crystal.set("sex speed", .125)
    crys "{b}*Жадно глотает воздух*{/b}"
    pause
    crys "АААААААХХХХ!!!"
    crys "Не останавливайся!"
    pause
    crys "НЕ ОСТАНАВЛИВАЙСЯ!!!"
    pause
    crys "NGGHHH!!!" with hpunch
    return

label trailer_interior_crystal_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("crystals", [1,2,3,4,5,6,7,8], M_crystal) as crystals
            pause 5
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "crystals {}".format(pose_list[pose_counter]) as crystals
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("crystal_trailer_interior_hscene_dialog")
        $ animcounter += 1
    if not M_roxxy.get("roxxy crystal sex") and store._in_replay == None:
        $ M_roxxy.trigger(T_roxxy_crystal_sex)
    call screen crystal_sex_options

label crystal_trailer_interior_hscene_dialog:
    $ random_count = randomizer()
    if animcounter == 0:
        if not M_roxxy.get("roxxy crystal sex"):
            crys "О ГОСПОДИ!{p=1}{nw}"
            crys "Это точно самый большой из всех, что у меня были!{p=2}{nw}"
            pause
            crys "Ты как будто разрываешь меня на части!{p=2}{nw}"
            player_name "Мне остановиться?{p=2}{nw}"
            crys "Ну уж нет!{p=1}{nw}"
            crys "Еби меня жестче!{p=1}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "Раааар!!{p=1}{nw}"
                    crys "Это так прекрасно!{p=1}{nw}"
                else:

                    crys "Mmm, да, это оно!{p=1}{nw}"
                    crys "Выплесни весь этот яд!{p=2}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crys "О да...{p=1}{nw}"
                    pause
                    crys "Это то, что {b}мамочке{/b} было нужно сегодня!{p=2}{nw}"
                    player_name "Всё хорошо?{p=1}{nw}"
                    crys "Просто прекрасно.{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    player_name "Не могу поверить, что тебе так нравится анал...{p=2}{nw}"
                    crys "Ох, малыш, я его просто обожаю!{p=2}{nw}"
                    crys "Я даже не могу передать все эти чувства.{p=2}{nw}"
                    player_name "...{p=1}{nw}"
                    crys "... И если ты немного сменишь угол, то достанешь прямо в-{p=2}{nw}"
                    crys "AAAХХХ!!{p=1}{nw}"
                    pause
                    crys "Ох, это именно тот угол!{p=2}{nw}"
                    crys "Не смей останавливаться!{p=1}{nw}"
                else:

                    crys "Это так приятно, {b}[firstname]{/b}!{p=2}{nw}"
                    player_name "О да.{p=1}{nw}"

    elif animcounter == 1:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "Давай же, {b}[firstname]{/b}! Глубже!{p=1}{nw}"
                    player_name "Да, мэм.{p=1}{nw}"
                    if M_crystal.get("sex speed") > .076:
                        $ M_crystal.set("sex speed", M_crystal.get("sex speed") - 0.05)
                else:

                    crys "Дай {b}мамочке{/b} ещё!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    crys "Mmm, вот так {b}[firstname]{/b}!{p=1}{nw}"
                    crys "Продожай вбивать его так же глубоко!{p=2}{nw}"
                else:

                    crys "Скажи мне, {b}[firstname]{/b}?{p=1}{nw}"
                    player_name "Хмм?{p=1}{nw}"
                    crys "Моя дочь, более узкая?{p=2}{nw}"
                    player_name "Да, она намного уже...{p=2}{nw}"
                    pause
                    crys "Хмм, значит она не может взять его так глубоко?{p=2}{nw}"
                    player_name "Нет, она не может!{p=1}{nw}"
                    crys "Хехехе, значит опыт чего-то да стоит-{p=2}{nw}"
                    $ M_crystal.set("sex speed", .075)
                    crys "О Боже!!!{p=1}{nw}" with hpunch
                    pause
                    crys "AAAAAAХХХХ!!!{p=1}{nw}"
            else:

                if M_crystal.is_set("crystal anal"):
                    crys "ГРААХХ!!!{p=1}{nw}"
                else:

                    crys "Aaх!{p=1}{nw}"
        else:

            crys "Еби мемня жестче!{p=2}{nw}"

    elif animcounter == 2:
        if not M_roxxy.get("roxxy crystal sex"):
            crys "Aaaх!!{p=1}{nw}"
            crys "И ты тыкал этим монстром в мою дочь?!{p=2}{nw}"
            player_name "Д-да, мэм...{p=1}{nw}"
            pause
            player_name "Думаю, что она не сможет принять его так глубоко!{p=2}{nw}"
            crys "Надеюсь, что нет!{p=1}{nw}"
            crys "Бедная девочка пока не готова для такого проникновения!{p=2}{nw}"

        elif M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if M_crystal.is_set("crystal anal"):
                    crys "О боже!{p=1}{nw}"
                    crys "AAaххх!!{p=1}{nw}"
                else:

                    crys "Aaахх!!{p=1}{nw}"
                    crys "Сильнее!!{p=1}{nw}"

            elif random_count > 33 and random_count <= 66:
                if M_crystal.is_set("crystal anal"):
                    player_name "Тут так узко!{p=1}{nw}"
                    crys "Mmm, не останавливайся!{p=1}{nw}"
            else:

                crys "Твой член и правда особенный, {b}[firstname]{/b}!{p=2}{nw}"
                player_name "Хехе, спасибо!{p=1}{nw}"

    elif animcounter == 3:
        if M_roxxy.get("roxxy crystal sex"):
            if random_count <= 33:
                if not M_crystal.is_set("crystal anal"):
                    crys "Nngghhh!{p=1}{nw}"

            elif random_count > 66:
                if not M_crystal.is_set("crystal anal"):
                    crys "Я скоро-{p=1}{nw}"
                    crys "NGGHHH!!!{p=1}{nw}"
        else:

            if random_count > 50:
                crys "Aaah!!{p=1}{nw}"
                crys "Уже близко!{p=1}{nw}"
    return

label trailer_interior_crystal_sex_cum:
    if L_trailer.is_here(M_crystal):
        if M_crystal.is_set("crystal anal"):
            call expression game.dialog_select("trailer_interior_crystal_sex_outside_cum_anal")
        else:

            call expression game.dialog_select("trailer_interior_crystal_sex_outside_cum")

    elif M_roxxy.get("roxxy crystal sex"):
        if M_crystal.is_set("crystal anal"):
            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat_anal")
        else:

            call expression game.dialog_select("trailer_interior_crystal_sex_cum_repeat")

    elif M_crystal.is_set("crystal anal"):
        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first_anal")
        $ M_roxxy.set("roxxy crystal sex", 0)
    else:

        call expression game.dialog_select("trailer_interior_crystal_sex_cum_first")
        $ M_roxxy.set("roxxy crystal sex", 0)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Crystal"]["unlocked"] = True
    $ persistent.cookie_jar["Crystal"]["gallery"]["01_unlocked"] = True
    $ M_roxxy.trigger(T_roxxy_crystal_sex)
    $ game.timer.tick()
    $ game.main()

label trailer_interior_crystal_sex_outside_cum_anal:
    player_name "Я скоро кончу!"
    crys "Я тоже!"
    pause
    crys "ЕБИ МЕНЯ!!!"
    crys "NGGHHH!!!"
    player_name "Шшш-"
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    crys "{b}*Скулит*{/b}"
    pause
    hide crystals
    hide crystals_anal_cum
    with dissolve

    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal 13b
    with dissolve
    player_name "Дерьмо..."
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show player 8 with dissolve
    rox "{b}Мама{/b}? Что ты там делаешь?!"
    show player 23
    player_name "!!!" with hpunch
    show crystal undress 10
    crys "Ха... Хаа..."
    show player 22
    crys "Ничего я не делаю!"
    crys "Просто ударилась мизинцем!"
    show crystal undress 10b
    rox "Ладно, просто будь тише! Я говорю по телефону!"
    show crystal undress 10
    crys "Хаа... Тебе нужно идти."
    show crystal undress 10b
    show player 29 with dissolve
    player_name "Д-да..."
    hide player with dissolve
    crys "..."
    hide crystal_anal_cum
    show crystal undress 11_11b
    with dissolve
    crys "Mмм, боже мой!"
    pause
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_outside_cum:
    player_name "Вот оно!"
    crys "Шшш, тише..."
    pause
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3 with dissolve
    crys "Mмм..."
    crys "Хехе, так ведь намного лучше, {b}[firstname]{/b}?"
    player_name "Фух, ага..."
    hide crystals with dissolve
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal 13b
    with dissolve
    crys "Ладно, тебе нужно идти..."
    crys "Моя дочь, скорее всего, ждет тебя."
    show crystal undress 10b
    player_name "Да, наверное..."
    hide crystal_pussy_cum
    show crystal undress 6
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show crystal undress 5
    show player 8
    with dissolve
    pause
    show crystal undress 2
    show player 26
    with dissolve
    player_name "Спасибо, {b}Crystal{/b}."
    show player 13
    show crystal undress 1 with dissolve
    crys "Обращайся, малыш."
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_cum_repeat_anal:
    player_name "Твоя задница такая узкая!"
    player_name "Больше не могу держаться..."
    crys "Ещё чуть-чуть!"
    pause
    crys "Ох, блять. Я сейчас кончу!"
    player_name "Я тоже!!"
    show crystals cum 2_2b
    crys "AAAХХХ!!!"
    player_name "HNNGGG!!!" with flash
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    player_name "Воу, это было прекрасно!"
    hide crystals
    hide crystals_anal_cum
    with dissolve

    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "{b}*Скулит*{/b}"
    hide crystal_anal_cum
    show crystal undress 11
    with dissolve
    player_name "..."
    player_name "Вы в порядке, мэм?"
    crys "А-ага... Просто-"
    show crystal undress 11b with dissolve
    crys "Тсч!"
    crys "..."
    show crystal undress 9 with dissolve
    crys "Судороги, хах..."
    show crystal undress 7 with dissolve
    crys "Принесешь мне чего-нибудь прохладительного из холодильника?"
    show crystal undress 7b
    player_name "Конечно!"
    hide player
    hide player_slick_boner
    with dissolve
    pause
    show crystal undress 7
    crys "Боже мой, этот парень просто что-то!"
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_repeat:
    player_name "Я уже почти!"
    crys "Выплесни всё, малыш!"
    crys "Тебе это нужно!"
    show crystals cum 2_2b
    player_name "HNNGGHHH!!!" with flash
    crys "Aххх!!"
    pause
    show crystals retract 3 with dissolve
    pause
    crys "Фух! Именно это мне и было нужно!"
    hide crystals with dissolve

    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "Чувствуешь себя лучше?"
    hide crystal_pussy_cum
    show crystal undress 6
    hide player_slick_boner
    show player 261f at left
    with dissolve
    pause
    show crystal undress 5
    show player 8
    with dissolve
    player_name "Да, намного лучше."
    show player 111f
    show crystal undress 4
    with dissolve
    crys "Хороший мальчик!"
    show crystal undress 2 with dissolve
    show player 13
    crys "А теперь иди, я буду ждать, когда тебе в следующий раз нужна будет разрядка..."
    show crystal undress 1 with dissolve
    crys "Окей?"
    show crystal 4 with dissolve
    show player 14
    player_name "Конечно, {b}Crystal{/b}."
    show player 13
    show crystal 2b with dissolve
    crys "Хехехе!"
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_cum_first_anal:
    player_name "Я больше не могу держаться!"
    crys "..."
    pause
    player_name "{b}Crystal{/b}?!"
    crys "..."
    pause
    player_name "{b}CRYSTAL{/b}!?!"
    player_name "Я скоро-"
    pause
    show crystals cum 2_2b
    player_name "HNNGGG!!!" with flash
    crys "NGGHHHAAAAAAAAAHHHH!!!" with hpunch
    pause
    show crystals retract 3
    show crystals_anal_cum
    with dissolve
    pause
    hide crystals
    hide crystals_anal_cum
    with dissolve
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10b at right
    show crystal_anal_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    player_name "Вы в порядке, мэм?"
    crys "..."
    player_name "Мэ'эм?!"
    show crystal undress 10
    crys "... Mммхммм."
    show crystal undress 10b
    player_name "Фух, я даже занервничал на секунду."
    show crystal undress 10
    crys "Просто мне нужна минутка, чтобы перевести дух."
    crys "Боже, это было охрененно!"
    show crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show crystal undress 10
    crys "Я, наверное, неделю нормально ходить не смогу!"
    show crystal undress 10b
    show player 427
    player_name "Простите."
    show player 426
    show crystal undress 10
    crys "Фух! Не нужно извиняться!"
    crys "Не помню, когда я в последний раз так кончала!"
    hide crystal_anal_cum
    show crystal undress 11b
    with dissolve
    crys "Почувствуй, как я трясусь'!"
    show player 429
    player_name "Ххе, я полагаю, я был хорош?"
    show player 426
    show crystal undress 11 with dissolve
    crys "Ты был намного лучше, чем просто хорош!"
    show crystal undress 9 with dissolve
    pause
    show crystal undress 7 with dissolve
    crys "Вау! Да я даже встать сейчас не могу..."
    crys "Ты уже вставлял эту штуку в зад моей дочери?"
    show crystal undress 7b
    show player 429
    player_name "... Нет, мэм."
    show player 426
    show crystal undress 7
    crys "Хорошо!"
    crys "Эта бедная девочка не готова принять это монстра!"
    crys "Пока что."
    show crystal undress 7b
    player_name "..."
    show crystal undress 7
    crys "Принесешь мне пару банок чего-нибудь прохладительного из холодильника???"
    show crystal undress 7b
    show player 427
    player_name "Именно пару?"
    show player 426
    show crystal undress 7
    crys "Ага."
    crys "Одну мне, и одну моему заднему проходу!"
    crys "Ты неплохо его потрепал!"
    show crystal undress 7b
    show player 429
    player_name "Хаха, ладно."
    hide player with dissolve
    pause
    show crystal undress 7
    crys "Боже мой, моей дочке лучше бы хорошо к нему относиться..."
    crys "Если она его упустит - я точно от неё откажусь!"
    hide crystal with dissolve
    return

label trailer_interior_crystal_sex_cum_first:
    player_name "Да, я уже на пределе!"
    crys "Давай же!"
    crys "Наполни меня полностью'!"
    player_name "Nngghh!"
    pause
    crys "Вот так!"
    crys "О черт! Вот оно!"
    show crystals cum 2_2b
    player_name "HNNGGG!!" with flash
    crys "AAAhhhh!!!"
    pause
    show crystals retract 3 with dissolve
    crys "Хаа... Хааа..."
    crys "О боже!"
    crys "Хаа..."
    hide crystals with dissolve
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show crystal undress 10 at right
    show crystal_pussy_cum undress
    show player crystal 13 at left
    show player_slick_boner crystal
    with dissolve
    crys "Я никогда тебя не отпущу."
    show crystal undress 10b
    hide player_slick_boner
    show player 261f at left
    with dissolve
    player_name "..."
    show player 8 with dissolve
    show crystal undress 10
    crys "Если моя дочь не сможет тебя удовлетворить..."
    show player 110f with dissolve
    crys "... Просто прийди к старушке Crystal!"
    crys "Понял?!"
    show crystal undress 10b
    show player 111f
    player_name "Да, мэ'эм."
    show player 110f
    hide crystal_pussy_cum
    show crystal undress 5
    with dissolve
    crys "Фух!"
    show crystal undress 2 with dissolve
    show player 13
    pause
    show crystal undress 1 with dissolve
    crys "Ладно, после такой ебли мне необходимо пиво!"
    show crystal 6 with dissolve
    crys "Хочешь баночку?"
    show crystal 5
    show player 14
    player_name "Нет, спасибр..."
    player_name "Я, наверное, должен идти."
    show player 13
    show crystal 6
    crys "... Как хочешь."
    crys "Только возвращайся скорее, малыш."
    hide player
    hide crystal
    with dissolve
    return

label trailer_interior_crystal_sex_repeat_inside:
    scene expression "backgrounds/location_trailer_closeup_day.jpg"
    show player 14 zorder 2 at left
    show crystal 1 at right
    with dissolve
    player_name "Хочешь немного повеселиться, пока я здесь?"
    show player 13
    show crystal 2
    crys "Ох, знаешь же, что хочу!"
    show crystal undress 1 with dissolve
    crys "Я же сказала, что буду хорошо о тебе заботиться."
    show crystal undress 2 with dissolve
    pause
    show crystal undress 4 with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    show player 426
    pause
    show crystal undress 7 with dissolve
    crys "А теперь..."
    show crystal undress 10 with dissolve
    crys "Ты хочешь мою киску?"
    show crystal undress 9 with dissolve
    crys "Или..."
    show crystal undress 11_11b with dissolve
    crys "Мой зад?"
    return

label trailer_interior_crystal_sex_repeat_outside_offer_pre:
    scene expression "backgrounds/location_trailer_closeup01_evening.jpg"
    show player 13 at left
    show crystal 6 at right
    with dissolve
    crys "Эй, что насчет быстрого перепихона?"
    show crystal 5
    show player 10
    player_name "Что?!" with hpunch
    player_name "... Но ведь {b}Roxxy{/b} прямо здесь!"
    show player 5
    show crystal 16b with dissolve
    crys "Ох, она скорее всего говорит по телефону или что-то ещё!"
    crys "Если мы не будем шуметь, - ничего плохого не произойдет."
    show crystal 5 with dissolve
    player_name "..."
    show player 10
    player_name "Ну не знаю..."
    show player 5
    show crystal 9
    crys "Ох, давай же, малыш!"
    show crystal 15
    crys "Разве ты не хочешь быстрой разрядке?"
    crys "{b}Мамочке{/b} нужен твой прекрасный член, ОЧЕНЬ нужен!"
    show crystal 14
    show player 12
    player_name "А соседи?"
    show player 5
    show crystal 11
    crys "Ха?"
    show crystal 6
    crys "Оу, да кого вообще ебет, что они подумают?!"
    show crystal 1 at left
    show crystal 18_18b at Position (xpos=134)
    show crystal_talking_head
    with dissolve
    crys "К тому же тут достаточно темно, они ничего и не увидят."
    hide crystal_talking_head
    show player 114
    player_name "..."
    show player 5
    return

label trailer_interior_crystal_sex_repeat_outside_offer_menu:
    menu:
        "О-окей.":
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_accept")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")
        "Ни за что!":

            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_denied")
    $ game.main()

label trailer_interior_crystal_sex_repeat_outside_offer_accept:
    show player 14
    player_name "Ладно, но только быстро!"
    show player 13
    show crystal undress 1 at center with dissolve
    crys "Хороший мальчик!"
    show crystal undress 3 with dissolve
    crys "Ну так..."
    show player 426 zorder 2
    show crystal undress 4 at right with dissolve
    pause
    show crystal undress 5 with dissolve
    pause
    show crystal undress 6 with dissolve
    pause
    show crystal undress 7 with dissolve
    pause
    show crystal undress 10 with dissolve
    crys "Ты в настроении для?"
    crys "Киски?"
    show crystal undress 9 with dissolve
    crys "Или..."
    show crystal undress 11_11b with dissolve
    crys "Анала?"
    return

label trailer_interior_crystal_sex_repeat_outside_offer_denied:
    show player 12
    player_name "Мы не можем делать это!"
    player_name "Когда {b}Roxxy{/b} прямо тут!"
    show player 5
    show crystal 11 at center with dissolve
    crys "Тц, ладно."
    show crystal 6
    crys "Ну тогда я просто удовлетворю себя сама..."
    show crystal 5
    show player 11
    player_name "..."
    show crystal 6
    crys "Развлекись там с моей дочкой, {b}[firstname]{/b}."
    hide player
    hide crystal
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
