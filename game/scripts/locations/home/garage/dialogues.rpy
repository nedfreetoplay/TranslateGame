label home_garage_pick_up_shovel:
    scene expression game.timer.image("backgrounds/location_home_garage{}_blur.jpg")
    show player 244 with dissolve
    player_name "Да, это должно сработать!"
    player_name "Было бы неплохо иметь немного денег для разнообразия..."
    show player 243
    jen "{b}*гм*{/b}"
    player_name "!!!" with hpunch
    show player 243 at left
    show jenny f_upset_talk a_dressed_crossed
    with dissolve
    jen "Что ты делаешь с лопатой?"
    show jenny f_upset
    show player 244
    player_name "... Ааа?"
    player_name "О! Я беру ее в дом {b}Дианы{/b}."
    player_name "Я буду работать ей этим летом."
    show player 243
    show jenny f_upset_talk
    jen "{b}Диана{/b} дала тебе работу?"
    jen "... Она никогда не предлагала мне работу!"
    show jenny f_upset
    show player 14 with dissolve
    player_name "Ну, это физический труд в ее саду."
    player_name "Она, вероятно, просто предположила, что тебе это будет не интересно..."
    show player 13
    show jenny f_eyeroll
    jen "Тьфу, в такую жару?"
    show jenny f_upset_talk
	jen "Да, ни за что. К черту это!"
    show jenny f_upset
    show player 10
    player_name "Что ты делаешь в гараже?"
    player_name "Ты никогда сюда не выходишь..."
    show player 5
    show jenny f_normal_talk a_dressed_hips with dissolve
    jen "Мне нужны батарейки. Разве у нас здесь их нет?"
    show jenny f_normal
    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Да, я тоже так думаю."
    player_name "Посмотри в коробке на нижней полке."
    show player 13
    pause
    show jenny b_bend f_empty a_empty at flip
    show jenny at Position (xpos=800)
	with dissolve
	show player 428
    player_name "!!!"
    pause
    show jenny b_bend_down with dissolve
    pause
	show player 12
    hide jenny
    show jenny a_dressed_hips_battery f_upset_talk b_dressed at unflip
	with dissolve
	player_name "Черт возьми, зачем тебе столько?"
    show player 5
    jen "Не твое дело, неудачник!"
    jen "Просто возьми лопату и проваливай."
    show jenny f_upset
    show player 12
    player_name "Тч, неважно."
    show player 90
    show jenny f_grin_talk
    jen "Получай удовольствие напрягая задницу для {b}Дианы{/b}..."
    show jenny f_laugh
    jen "Хахаха!"
    hide jenny with dissolve
    show player 12
    player_name "... Она такая стерва."
    show player 90
    show screen popup("boxes/popup_item_shovel1.png")
    $ player.get_item("shovel")
    hide player with dissolve
    $ game.main()

label car_dialogue:
    if M_mom.is_state(S_mom_mall_outing):
        call expression game.dialog_select("garage_car_mom_mall_outing")
        jump expression game.dialog_select("mall_dialogue")

    scene expression game.timer.image("home_garage{}")
    if M_mom.is_state(S_mom_check_car):
        $ player.go_to(L_home_car)
        call expression game.dialog_select("garage_car_mom_check_car")
        $ player.location.call_screen(False)
    else:

        if seen_garage_locked:
            call expression game.dialog_select("garage_car_seen")
        else:
            call expression game.dialog_select("garage_car_not_seen")
            $ seen_garage_locked = True
    $ game.main()

label garage_car_mom_mall_outing:
    scene expression "backgrounds/location_car_cutscene01.jpg"
    show expression FilteredText("И так мы запрыгнули в машину и направились в торговый центр.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("Я обнаружил, что время прошло быстро, пока я был с {b}[deb_name]{/b}...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    show expression FilteredText("... Ее приятная компания и заразительная улыбка поднимали мне настроение.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    scene black
    with fade
    return

label garage_car_mom_check_car:
    show player 4 with dissolve
    player_name "( Она права. Машина не заводиться. )"
    show player 5
    player_name "( Я лучше проверю двигатель. )"
    if game.timer.is_dark():
        player_name "( Здесь определенно темно. )"
    return

label garage_car_seen:
    show player 34 at left with dissolve
    player_name "Хмм..."
    show player 35
    player_name "Я не должен испальзовать {b}[deb_name]{/b} машину."
    hide player 35 with dissolve
    return

label garage_car_not_seen:
    show player 2 at left with dissolve
    player_name "Машина {b}[deb_name]{/b} ... жаль, что у меня нет причины чтобы взять ее..."
    hide player 2 at left with dissolve
    return

label engine_broken:
    call expression game.dialog_select("engine_broken_dialogue")
    $ M_mom.trigger(T_mom_check_engine)
    jump expression game.dialog_select("home_garage")

label engine_broken_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 23 with dissolve
    player_name "( !!! )"
    show player 22
    player_name "( Какого черта?! Похоже, кто-то поработал молотком! )"
    pause
    show player 16
    player_name "( Интересно, это как-то связано с теми парнями в костюмах? )"
    player_name "( Подонки! )"
    show player 11
    player_name "( Я никак не могу это исправить. Нам нужен совершенно новый двигатель. )"
    player_name "( Я, наверное, должен сказать {b}[deb_name]{/b} об этом. Она расстроится! )"
    return

label lawnmower_dialogue:
    $ player.go_to(L_home_garage)
    if M_mom.is_state(S_mom_fill_mower) and not player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_no_gas")
        else:
            call expression game.dialog_select("garage_mom_fill_mower_night")

    elif M_mom.is_state(S_mom_fill_mower) and player.has_item("gas_can"):
        if not game.timer.is_dark():
            call expression game.dialog_select("garage_mom_fill_mower_success")

            $ player.remove_item("gas_can")
            $ M_mom.trigger(T_mom_filled_mower)
            jump expression game.dialog_select("home_front")
        else:

            call expression game.dialog_select("garage_mom_fill_mower_night")
    else:
        call expression game.dialog_select("garage_lawnmower_not_needed")
    $ game.main()

label garage_mom_fill_mower_night:
    scene expression game.timer.image("home_garage{}")
    show player 35f with dissolve
    player_name "( Зачем мне использовать газонокосилку ночью? Я должен вернуться днем... )"
    hide player 35 with dissolve
    return

label garage_mom_fill_mower_no_gas:
    scene home_garage_closeup
    show player 428f at right
    player_name "( Я много лет не пользовался газонокосилкой... вспомнить бы, как ей пользоваться? )"
    player_name "( {b}Отец{/b} тянул за шнур и она начинала работать. Попробуем. )"
    scene home_garage_closeup
    show player 197
    with dissolve
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    scene home_garage
    show player 35f
    with dissolve
    player_name "( Должно быть, бензин кончился. Она едва заработала, так что я хотя бы знаю, как включить. )"
    show player 2f
    player_name "( Без топлива не заработает. Я должен купить немного в {b}CONSUM-R{/b}. )"
    return

label garage_mom_fill_mower_success:
    scene home_garage_closeup
    show player 202 at Position (xpos=521) with dissolve
    player_name "( У меня наконец-то есть бензин для газонокосилки. )"
    show player 201 at Position (xpos=509)
    player_name "( Этого должно хваить. )"
    show player 196 at Position (xpos=521)
    player_name "Надеюсь, это сработает. Я не знаю, что еще делать после этого..."
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 197 at center
    pause
    show player 200 at Position (xpos=566)
    pause
    show player 199 at center
    player_name "Хм... у меня ничего не получается. Я попробую потянуть немного сильнее..."
    show player 200 at Position (xpos=566)
    pause
    show player 198 at center
    player_name "Заработала!"
    return

label garage_lawnmower_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 35 with dissolve
    player_name "( Зачем мне использовать газонокосилку? Трава выглядит хорошо... )"
    hide player 35 with dissolve
    return

label garage_use_workbench_night:
    scene expression player.location.background_blur
    show player 3 with dissolve
    player_name "( Damn! I can't see a thing! )"
    show player 4 with dissolve
    player_name "( And the light fixture is broken! )"
    player_name "( I should come back and work on this during the {b}day{/b}... )"
    hide player with dissolve
    return

label garage_dewitt_drill:
    call expression game.dialog_select("garage_dewitt_drill_dialogue")
    $ player.get_item("drill")
    $ game.main()

label garage_dewitt_drill_dialogue:
    scene expression game.timer.image("home_garage{}")
    show player 14 with dissolve
    player_name "Перед вами старая дрель!"
    player_name "Батареи также заряжены."
    show player 12
    player_name "Теперь мне просто нужно найти {b}упавшую ветку с дерева{/b}."
    hide player with dissolve
    return

label garage_dewitt_make_new_flute:
    scene home_garage_cs1
    with fade
    show text "Странно, но было приятно строить эту флейту вручную.\nЯ на самом деле очень рад играть в эту вещь сейчас!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 566 with dissolve
    player_name "Там!"
    player_name "Не все так плохо!"
    show player 567
    pause
    show player 566
    player_name "Посмотрим, что будет, когда я возьму ее в рот и подую..."
    show player 567d with dissolve
    pause
    show player 566 with dissolve
    player_name "Эй, эта штука звучит неплохо!"
    player_name "Бьюсь об заклад, {b}Мисс Девитт{/b} офигеет, когда увидит, что я сделал флейту с нуля!"
    hide player with dissolve
    return

label garage_dewitt_find_paint:
    scene expression game.timer.image("home_garage{}")
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Я не вижу здесь краску..."
    pause
    show player 10 with dissolve
    player_name "Может быть {b}[deb_name]{/b} знает где она."
    hide player with dissolve
    return

label garage_dewitt_make_replacement_guitar:
    scene home_garage_cs2
    with fade
    show text "Знаешь, я действительно начинаю понимать всю эту деревообработку.\nВозможно, мне стоит стать плотником." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene expression game.timer.image("home_garage{}")
    show player 575 with dissolve
    player_name "Фу! С другой стороны, возможно, я не так талантлив, как думал."
    player_name "Я надеюсь, что это достаточно хорошо, чтобы обмануть {b}Миссис Джонсон{/b}."
    hide player with dissolve
    return

label garage_build_easels:
    scene location_home_garage_cutscene03
    with fade
    show text "Да, я думаю, это выглядит правильно." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Надеюсь {b}Мисс Росс{/b} понравится!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Я действительно не хочу ее расстраивать..." at Position (xpos=512, ypos=700) with dissolve
    pause
    hide text
    with dissolve
    return

label garage_workbench_not_needed:
    scene expression game.timer.image("home_garage{}")
    show player 12 with dissolve
    player_name "( У меня нет причин использовать это прямо сейчас. )"
    hide player with dissolve
    return

label debbie_car_sex_pre:
    scene car_interior
    show player car 2d
    show player_arms car 1
    show debbie car 4 at right
    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
    show xtra 30 at right
    with dissolve
    return

label debbie_car_sex_pre_first_time:
    pause
    show debbie car 4b
    deb "Знаешь, я действительно не ожидала, что ты приведешь меня в машину."
    show debbie car 5g
    deb "Сначала я была настроена скептически, но теперь, когда мы сидим здесь..."
    show player car 3
    deb "... Это меня возбуждает."
    deb "Представьте, если бы мы были где-то припаркованы?"
    deb "Ммм..."
    deb "Я промокаю от одной мысли об этом!"
    show debbie car 5f
    show player car 4g
    player_name "Я бы попробовал что-то подобное..."
    show player car 5
    player_name "... Тебе не будет стыдно?"
    show player car 5b
    show debbie car 5c
    show debbie_arms_car 5 at Position(xalign = 0.357, yalign = 0.558)

    deb "..."
    show debbie car 5g
    deb "Хех, я не знаю... Я, наверное, была бы подавленой, если бы нас поймали!."
    deb "... хотя..."
    deb "... Это то, что делает его таким захватывающим, ты понимаешь?!"
    deb "Ну, по крайней мере, это меня возбуждает..."
    deb "Я промокаю от одной мысли об этом!"
    show debbie car 5f
    show player car 4h
    player_name "..."
    show player car 5
    player_name "Ты, да?"
    show player car 5b
    show debbie car 3b
    deb "Хехе, да..."
    deb "Так что мы будем делать с этим большим, твердым членом?"
    show debbie car 3
    show player car 2d
    return

label debbie_car_sex_pre_repeat:
    show debbie car 4b
    show debbie_arms_car 5c at Position(xalign = 0.357, yalign = 0.558)
    deb "Мне нравится чувствовать, как этот здоровяк напрягается в моей руке."
    show debbie car 4
    pause
    show player car 4b
    show debbie car 3b
    show debbie_arms_car 5 with dissolve
    deb "Молоденькие члены быстро твердеют."
    show debbie car 4
    pause
    show player car 2d
    show debbie car 5b with dissolve
    deb "Выглядит так... Вкусно!"
    show debbie car 3b
    deb "Хочешь, чтобы я взяла в рот?"
    show debbie car 3
    return

label debbie_car_sex_jerk_off:
    show player car 2c
    player_name "Просто продолжай делать то, что делаешь!"
    show player car 2d
    show debbie car 3b
    deb "Хорошо, милый."
    show debbie car 4
    return

label debbie_car_sex_bj:
    show player car 2c
    player_name "Ты... Используешь свой рот?"
    show player car 2d
    show debbie car 3b
    deb "Точно!"
    scene car_interior bj
    show player car 4c
    show player_arms car 1
    show debbie_car_bj 11 at right
    show xtra 30 zorder 2 at right
    with dissolve
    pause
    show debbie_car_bj 12 with dissolve
    pause
    show debbie_car_bj 7
    show player_boner car 3
    with dissolve
    pause
    hide player_boner
    show debbie_car_bj 8 zorder 1 at Position(xalign = 0.93, yalign = 1.0)
    with dissolve
    pause
    show player car 4c
    return

label debbie_car_sex_leave:
    show player car 5
    player_name "Я думаю, что сейчас хорошо."
    player_name "Это было хорошо."
    show player car 5b
    show debbie car 5g
    deb "Правда?"
    deb "Но ты еще не кончил?"
    show debbie car 5f
    show player car 2
    player_name "Ничего страшного."
    show player car 5b
    show debbie car 5g
    deb "Я сделала что-то не так?"
    show debbie car 5f
    show player car 2c
    player_name "Было хорошо {b}[deb_name]{/b}! Не волнуйся."
    player_name "Мне нужно идти, вот и все."
    show player car 5b
    deb "..."
    show debbie car 5g
    deb "Хорошо..."
    return

label debbie_car_sex:
    $ M_mom.set("sex speed", .175)
    $ animated = False
    call expression game.dialog_select("debbie_car_sex_pre")
    if not M_mom.is_set("car sex"):
        call expression game.dialog_select("debbie_car_sex_pre_first_time")
        $ M_mom.set("car sex", True)
    else:

        call expression game.dialog_select("debbie_car_sex_pre_repeat")
    menu:
        "Подрочи мне.":
            $ M_mom.set("car jerk", True)
            call expression game.dialog_select("debbie_car_sex_jerk_off")
            jump expression game.dialog_select("car_mom_sex_loop")
        "Отсос.":

            $ M_mom.set("car jerk", False)
            call expression game.dialog_select("debbie_car_sex_bj")
            jump expression game.dialog_select("car_mom_sex_loop")

        "Уйти." if store._in_replay == None:
            call expression game.dialog_select("debbie_car_sex_leave")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_mom.is_set("car jerk"):
                    show expression AnimatedImage("debbie_arms_car", [5,"5b","5c","5b"], M_mom) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression AnimatedImage("debbie_car_bj", [8,"8b","8c","8d","8e","8f","8g"], M_mom) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_mom.is_set("car jerk"):
                $ pose_list = [5,"5b","5c","5b"]
            else:
                $ pose_list = [8,"8b","8c","8d","8e","8f","8g"]
            $ poses_done = []
            while poses_done != pose_list:
                if M_mom.is_set("car jerk"):
                    show expression "debbie_arms_car {}".format(pose_list[pose_counter]) as debbie_arms_car at Position(xalign = 0.357, yalign = 0.558)
                else:
                    show expression "debbie_car_bj {}".format(pose_list[pose_counter]) as debbie_car_bj zorder 1 at Position(xalign = 0.93, yalign = 1.0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("car_mom_hscene_dialog")
        $ animcounter += 1
    call screen car_mom_sex_options

label car_mom_hscene_dialog:
    if M_mom.is_set("car jerk"):
        if animcounter == 3:
            if randomizer() <= 50:
                show debbie car 4b
                show player car 5b
                deb "Не могу поверить, что у тебя такой большой член!{p=2}{nw}"
                deb "Мне нравится он на ощупь.{p=2}{nw}"
                show debbie car 4
            else:

                show debbie car 5b
                show player car 5b
                deb "Я просто люблю твой большой член!?{p=2}{nw}"
                deb "Кончи для меня, {b}[firstname]{/b}!{p=2}{nw}"
                show player car 4b
                pause 1
                show debbie car 4
                show player car 4c
                player_name "Хорошо...{p=2}{nw}"
                show player car 4h
    else:
        if animcounter == 1:
            deb "Мммм...{p=1}{nw}"

        elif animcounter == 3:
            player_name "О...{p=1}{nw}"
            show player car 4d
            player_name "Сейчас, {b}[deb_name]{/b}.{p=2}{nw}"
            show player car 4c
    return

label car_mom_faster_dialogue:
    show player car 4c
    player_name "Быстрее, {b}[deb_name]{/b}."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_slower_dialogue:
    show player car 4c
    player_name "Помедленее..."
    show player car 4h
    jump expression game.dialog_select("car_mom_sex_loop")

label car_mom_sex_cum:
    if M_mom.is_set("car jerk"):
        call expression game.dialog_select("car_mom_jerk_cum")
    else:
        call expression game.dialog_select("car_mom_bj_cum")
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["05_unlocked"] = True
    $ player.go_to(L_home_garage)
    $ game.timer.tick()
    $ game.main()

label car_mom_jerk_cum:
    show player car 4c
    pause
    show player car 4d
    show player_arms car 2
    show debbie_arms_car 5d at Position(xalign = 0.357, yalign = 0.558)
    with dissolve
    player_name "( !!! )"
    show debbie car 4b
    deb "Воооууу!!!"
    show debbie car 5b
    deb "О, милый!"
    show player car 2b
    show player_arms car 1 with dissolve
    deb "Я всегда забываю, насколько велики твои заряды!!"
    show debbie car 4b
    deb "По крайней мере, у нас ничего не было в  машине..."
    show debbie car 3
    show player car 2c
    player_name "Было круто..."
    scene car_interior kiss
    show debbie car 6 at right
    show player_boner car 1b
    show xtra 30 at right
    with dissolve
    pause
    scene car_interior
    show player car 2c
    show player_arms car 1
    show player_boner car 1b
    show debbie car 3 at right
    show debbie_arms_car 1
    show xtra 30 at right
    with dissolve
    player_name "Спасибо, {b}[deb_name]{/b}."
    show player car 2d
    show debbie car 3b
    deb "Незачто, милый."
    show debbie car 4b
    deb "Давай вернемся назад, прежде чем {b}[jen_name]{/b} начнет задаваться вопросом, куда мы пропали."
    show debbie car 3b
    deb "Я не хочу, чтобы она узнала, что мы здесь делаем!"
    return

label car_mom_bj_cum:
    show player_arms car 2
    show player car 4d
    player_name "{b}[deb_name]{/b}, я на подходе..."
    player_name "( !!! )"
    show debbie_car_bj 9
    show player_arms car 2
    with flash
    deb "Мммммм!!"
    scene car_interior
    show player car 4d
    show player_arms car 1
    show player_boner car 2
    show debbie_car_bj 10 at right
    show xtra 30 at right
    with dissolve
    pause
    show player car 2d
    deb "{b}*глоток*{/b}"
    deb "... {b}*глоток*{/b}"
    show debbie car 2 at right
    hide debbie_arms_car
    hide debbie_car_bj
    show debbie_arms_car 1
    hide xtra
    show xtra 30 at right
    with dissolve
    pause
    show debbie car 3b
    deb "Вау! Так много!"
    deb "Фу... Я думаю, у меня не будет аппетита за ужином."
    show debbie car 3
    show player car 2c
    player_name "Это было круто! У тебя это хорошо получается!"
    show player car 2d
    show debbie car 3b
    deb "Хехе, ну я рада, что тебе понравилось, {b}[firstname]{/b}. Потому что я люблю сосать твой член!"
    show debbie car 3b
    deb "Давай вернемся назад, прежде чем {b}[jen_name]{/b} начнет задаваться вопросом, куда мы пропали."
    show debbie car 3
    show player car 5
    player_name "Хорошо."
    player_name "Просто дай мне сначала привести себя в порядок..."
    show player car 3
    show debbie car 3b
    deb "Увидимся в доме, милый!"
    show player car 5b
    show debbie car 4b
    deb "Не задерживайся слишком долго..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
