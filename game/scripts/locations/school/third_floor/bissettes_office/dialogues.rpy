label bissettes_office_first_visit:
    scene school_office1_b with fade
    show player 10 with dissolve
    player_name "Кабинет {b}Мисс Биссетт{/b} выглядит таким...Французким!"
    show player 14
    player_name "Возможно отднажды мы сможем с ней поехать в путешествие..."
    hide player with dissolve
    return

label bissettes_office_afternoon_visit:
    scene expression game.timer.image("french_office_c{}")
    show player 13 at left
    show teacher 2 at right
    with dissolve
    bis "Bonjour(Добрый день), {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Здрасте, {b}Мисс Биссетт{/b}."
    show player 17
    player_name "Мне нравится ваш кабинет! Это очень... эмм... по Французки."
    show player 13
    show teacher 3
    bis "Merci beaucoup(Большое спасибо) !"
    show teacher 1
    show player 35
    player_name "Так, почему вы хотели меня видеть в вашем кабинете?"
    show player 13
    show teacher 5
    bis "Что ж, {b}[firstname]{/b}, Я беспокоюсь о предстоящем экзамене."
    show teacher 4
    show player 33
    player_name "Хм? Вам не нужно волноваться, {b}Мисс Биссетт{/b}."
    show player 14
    player_name "Я никогда не чувствовал себя настолько подготовленым к тесту чем раньше. Я хорошо с ним справлюсь, обязательно!"
    show player 13
    show teacher 5
    bis "Oui(Да), {b}[firstname]{/b}! Ты безусловно мой лучший ученик и Я очень горжусь тобой!"
    bis "Это за {b}Рокси{/b} я очень беспокоюсь..."
    show teacher 4
    show player 12
    player_name "{b}Рокси{/b}?"
    show player 5
    show teacher 5
    bis "Oui(Да)! Учитывая что она даже не появлялась на экзамене, не существует способа заставить её получить хороую отметку."
    show teacher 4
    show player 10
    player_name "Что случится если она не пройдет тест?"
    show player 5
    show teacher 5
    bis "Ce serait ennuyeux(Это будет досадно)..."
    bis "Если {b}Рокси{/b} не появится на экзамене, это снизит среднегодовое число всех студентов."
    show teacher 15 with dissolve
    bis "Я боюсь {b}Директриса Смит{/b} оторвет мне голову!"
    show teacher 14
    show player 10
    player_name "Вы хотите сказать что она уволит вас?!"
    show player 5
    show teacher 5 with dissolve
    bis "Oui(Да)..."
    show teacher 4
    show player 24
    player_name "..."
    show player 12
    player_name "Что ж я не позволю этому случиться!"
    show player 14
    player_name "Я найду способ убедить {b}Рокси{/b} появиться на экзамене, я обещаю!"
    show player 13
    show teacher 2
    bis "Ох, {b}[firstname]{/b}! Tu es mon heros(Ты мой герой)!"
    show teacher 12
    bis "Если ты это сделаешь для меня, я дам тебе лучшее особое вознаграждение ты можешь себе представить, да?"
    show teacher 13
    show player 29 with dissolve
    player_name "Д-да!"
    show player 13 with dissolve
    show teacher 2
    bis "Très Bien(очень хорошо)!Удачи, {b}[firstname]{/b}!"
    show teacher 1
    show player 14
    player_name "Спасибо, {b}Мисс Биссетт{/b}."
    show player 13
    hide teacher with dissolve
    show player 35
    player_name "Хмм, это будет нелегко..."
    player_name "Это единственая убедительная вещь чтобы {b}Рокси{/b} пришла на экзамен."
    player_name "Но так же она должна его как то пройти..."
    show player 4 with dissolve
    player_name "..."
    show player 12
    player_name "... Я уверен что что-нибудь придумаю."
    hide player with dissolve
    return

label bissettes_office_night_visit:
    scene expression game.timer.image("french_office_sex_c{}")
    show teacher 29 at right
    show player 13 at left
    with dissolve
    bis "Ахх, {b}[firstname]{/b}! Я уже начала думать что ты не придешь!"
    show teacher 28
    show player 10
    player_name "Вы начали без меня?"
    show player 5
    show teacher 29
    bis "*ик* Oui, mon bel homme!(да, мой красивый мужчина)"
    bis "Я только что закончила свою 2 бутылку."
    show teacher 30 with dissolve
    bis "Позволь мне налить- *ик*"
    show teacher 31 with dissolve
    bis "ça me saoûle(это меня опьянило)."
    show teacher 33 with dissolve
    show player 13
    bis "Ты видишь *ик* Франция делает лучшее вино!"
    show teacher 32
    show player 17
    player_name "Хехе, как скажите."
    show player 13
    show teacher 33
    bis "Тсс! это правда!"
    bis "лучшее вино..."
    bis "И лучших любовников..."
    show teacher 32
    show player 11
    player_name "*Глоток*"
    show teacher 33
    bis "Я задолжала тебе особую награду, да?"
    show teacher 32
    show player 26
    player_name "Д-да..."
    show player 13
    show teacher 33
    bis "Ну чтож это ждет тебя, вот здесь..."
    bis "Почему бы тебе не пойти и не развернуть его?"
    show player 523 at Position (xoffset=378)
    show teacher 34
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 35
    with dissolve
    pause
    show player 524 at Position (xoffset=378)
    show teacher 37
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 38
    with dissolve
    pause
    show teacher 39
    bis "Тебе нравится?"
    show teacher 38
    show player 526 at Position (xoffset=360)
    player_name "Да очень."
    show player 527 at Position (xoffset=360)
    player_name "Вы красивая."
    show player 525 at Position (xoffset=360)
    show teacher 39
    bis "Не стесняйся поцелуй их."
    hide player
    show teacher 39b
    with dissolve
    bis "Мммм..."
    bis "Не забудь использовать свой язычок, {b}[firstname]{/b}."
    show teacher 39b_39c_39d
    bis "Ох, mon bel homme(мой красивый мужчина)..."
    bis "Ты заставляешь- *ик*"
    bis "Ты заставляешь меня таять этими поцелуями!"
    pause
    pause
    show player 83c at left
    show teacher 39
    with dissolve
    bis "Я знаю что ты скрываешь что то большое в этих твоих штанах..."
    bis "Я покажу тебе мою. Ты покажы мне свой, да?"
    show teacher 38
    show player 83b
    player_name "Конечно!"
    show player 261bf with dissolve
    pause
    show player 263cf with dissolve
    show teacher 39
    bis "Oh mon Dieu(Боже мой)!Il est magnifique!(Он великолепен)"
    bis "Дай мне его, {b}[firstname]{/b}!"
    show teacher 38
    show player 262bf
    player_name "Ты имеешь в виду... Ты хочешь чтобы я..."
    show player 263cf
    show teacher 39
    bis "S'il te plaît(Пожалуйста)!"
    bis "Твоя награда только начинается."
    show teacher 40 with dissolve
    pause
    show teacher 41 with dissolve
    pause
    show teacher 42 with dissolve
    pause
    show teacher 43 with dissolve
    show player 263bf
    bis "Я не могу описать с каким нетерпением я ждала этого."
    pause
    show teacher 44 with dissolve
    pause
    show teacher 45 with dissolve
    pause
    show player 263cf
    show teacher 46
    bis "Тебе нравится мое Французкое тело, да?"
    show teacher 45
    show player 262bf
    player_name "Да!"
    show player 263cf
    show teacher 46
    bis "Excellent!(превосходно)"
    show teacher 47 at Position (yoffset=-61) with dissolve
    show player 263bf
    pause
    show teacher 48 at Position (yoffset=-61)
    bis "Подойти! Позволь мен рассказать тебе о французком занятии любовью!"
    show teacher 50 with dissolve
    bis "Я гоотова для тебя"
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    bis "Войди в меня, {b}[firstname]{/b}."
    show teachers 52 with dissolve
    bis "Оххх, Il est si grosse(он такой толстый)!"
    bis "Ааааах!"

    $ M_bissette.set("change angle", False)
    $ M_bissette.set("sex speed", .175)
    show teachers 1_2_3_4_5_6_7
    pause
    return

label bissettes_office_night_visit_repeat:
    $ persistent.cookie_jar["Bissette"]["gallery"]["02_unlocked"] = True
    scene expression game.timer.image("french_office_sex_c{}")
    show teacher 29 at right
    show player 13 at left
    with dissolve
    bis "И так, нехочешь немного вина или перейдем к занятию любовью?"
    show teacher 28
    show player 26
    player_name "Занятием любовью, Пожалуйста."
    show player 13
    show teacher 31 with dissolve
    bis "Dieu merci(Господи спасибо)!"
    show teacher 33 with dissolve
    bis "Хехе!"
    bis "Я с нетерпением ждала этого целый день!"
    bis "Подойди, mon bel homme(Мой красивый мужчина)!Возьми меня силой!"
    show teacher 32
    show player 14
    player_name "Avec plaisir(С удовольствием)!"
    show player 523 at Position (xoffset=378)
    show teacher 34
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 35
    with dissolve
    pause
    show player 524 at Position (xoffset=378)
    show teacher 37
    with dissolve
    pause
    show player 525 at Position (xoffset=360)
    show teacher 38
    with dissolve
    pause
    show player 527 at Position (xoffset=360)
    player_name "Ты прекрасна."
    show player 525 at Position (xoffset=360)
    show teacher 39
    bis "Не стесняйся поцелуй их."
    hide player
    show teacher 39b
    with dissolve
    bis "Мммм..."
    bis "Не забудь использовать свой язычок, {b}[firstname]{/b}."
    show teacher 39b_39c_39d
    bis "Ох, mon bel homme(Мой красивый мужчина)..."
    bis "Ты заставляешь- *ик*"
    bis "Ты заставляешь таять этими поцелуями!"
    pause
    show player 83c at left
    show teacher 39
    with dissolve
    bis "Я знаю что ты скрываешь что-то большое в этих твоих штанах..."
    bis "Я покажу тебе мою. Ты покажи мне свой, да?"
    show teacher 38
    show player 83b
    player_name "Конечно!"
    show player 261bf with dissolve
    pause
    show player 263cf with dissolve
    show teacher 39
    bis "Oh mon Dieu(О мой бог)! C'est beau(Это красиво)..."
    bis "Дай мне его, {b}[firstname]{/b}!"
    show teacher 40 with dissolve
    pause
    show teacher 41 with dissolve
    pause
    show teacher 42 with dissolve
    pause
    show teacher 43 with dissolve
    show player 263bf
    pause
    show teacher 44 with dissolve
    pause
    show teacher 45 with dissolve
    pause
    show player 263cf
    show teacher 46
    bis "Тебе нравится мое Французкое тело, да?"
    show teacher 45
    show player 262bf
    player_name "Да!"
    show player 263cf
    show teacher 46
    bis "Excellent!(превосходно)"
    show teacher 47 at Position (yoffset=-61) with dissolve
    show player 263bf
    pause
    show teacher 48 at Position (yoffset=-61)
    bis "Ah, ma chatte toute serrée a envie de ta grosse bite bien juteuse.(Ах моя очень узкая киска хочет твоего большого очень сочного члена)"
    show teacher 47 at Position (yoffset=-61)
    show player 262bf
    player_name "Что?"
    show player 263cf
    show teacher 50 with dissolve
    bis "Я ждала тебя."
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    bis "Войди в меня, {b}[firstname]{/b}."
    show teachers 52 with dissolve
    bis "Ohh, elle est si grosse (Oxx, он уже такой большой)!"
    bis "Ааааа!"

    $ M_bissette.set("change angle", False)
    $ M_bissette.set("sex speed", .175)
    show teachers 1_2_3_4_5_6_7
    pause
    return

label bissettes_office_chair_sex_intro:
    scene expression game.timer.image("bissette_office_sex_chair_c{}")
    show teachers_chair 1 at Position(xalign = 0.564)
    with dissolve
    bis "Давай попробуем на стуле, нам должно быть более удобно."
    show teachers_chair 2 with dissolve
    player_name "Вам лучше знать. Вы учитель!"
    show teachers_chair 3 with dissolve
    bis "Oh, mon bel homme(Ох мой прекрасный мужчина)..."
    show teachers_chair 16 with dissolve
    pause
    show teachers_chair 4 with vpunch
    bis "Аааааах!"
    jump expression game.dialog_select("bissettes_office_sex_loop")

label bissettes_office_sex_intro:
    scene expression game.timer.image("french_office_sex_c{}")
    show player 263cf at left
    show teacher 50 at right
    with dissolve
    if randomizer() <= 50:
        bis "Хочешь занять этим на столе, да?"
    else:
        bis "За столом?"
    hide player
    hide teacher
    show teachers 51 at right
    with dissolve
    pause
    show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right with dissolve
    bis "Ohh, elle est si grosse!(Oxx, он уже такой большой)"
    bis "Ааааах!"
    jump expression game.dialog_select("bissettes_office_sex_loop")

label bissettes_office_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if M_bissette.is_set("change angle"):
                show expression AnimatedImage("teachers_chair", [4,5,6,7,8,9,10,11,12,13], M_bissette) as teachers_chair at Position(xalign = 0.564)
            else:
                show expression AnimatedImage("teachers", [1,2,3,4,5,6,7], M_bissette) as teachers at right
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("bissette_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_bissette.is_set("change angle"):
                $ pose_list = [4,5,6,7,8,9,10,11,12,13]
            else:
                $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                if M_bissette.is_set("change angle"):
                    show expression "teachers_chair {}".format(pose_list[pose_counter]) as teachers_chair at Position(xalign = 0.564)
                else:
                    show expression "teachers {}".format(pose_list[pose_counter]) as teachers at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("bissette_hscene_dialog")
        $ animcounter += 1
    call screen bissettes_office_sex_options

label bissette_hscene_dialog:
    if animcounter == 1:
        bis "Охххх!!!{p=1}{nw}"

    elif animcounter == 3:
        if not M_bissette.is_state(S_bissette_wine_sampling):
            bis "Сильнее! Еби меня сильнее!{p=2}{nw}"
            bis "Oh, Oui(Ох, да)!{p=2}{nw}"
            bis "(Я скоро кончу), {b}[firstname]{/b}!{p=2}{nw}"
            player_name "Я тоже!{p=2}{nw}"
            bis "Не останавливайся!{p=2}{nw}"
            bis "Не-{p=1}{nw}"

        elif M_bissette.is_state(S_bissette_wine_sampling):
            $ initial_sex_diag = False
            bis "C'est incroyable(это невероятно)!{p=2}{nw}"
            bis "Я ошибалась!{p=2}{nw}"
            bis "Не один француз никогда не трахал меня так!{p=2}{nw}"
            bis "Аааааааахх!!Не останавливайся!{p=2}{nw}"
    return

label bissettes_office_sex_cum_chair_angle:
    bis "АААААААХХХХ!!!!"
    player_name "Хннггггг!!!"
    show teachers_chair 14_15 at Position(xalign = 0.564) with flash
    pause
    show teachers_chair 16 with dissolve
    pause
    show teachers_chair 17 with dissolve
    pause
    show teachers_chair 18 with dissolve
    bis "Хаах.. Хаах..."
    show teachers_chair 1 with dissolve
    bis "{b}[firstname]{/b}..."
    bis "Это было великолепно!"
    show teachers_chair 2
    player_name "Хаах... Да."
    show teachers_chair 1
    bis "Мы обязаны это сделать снова, Да?"
    show teachers_chair 2
    player_name "Абсолютно!"
    show teachers_chair 1
    bis "Tres Bien(Очень хорошо), mon bel homme!(мой красивый мужчина)"
    bis "И так,присядь."
    bis "Я приготовлю тебе несколько кусочков сыра которые подойдут к вину..."
    show teachers_chair 2
    return

label bissettes_office_sex_cum_desk_angle:
    bis "АААААААХХХХ!!!!"
    player_name "Хннггг!!!"
    show teachers 52_53 at right with flash
    pause
    show teachers 54 with dissolve
    bis "Хаах.. Хаах..."
    show teachers 55 with dissolve
    bis "{b}[firstname]{/b}..."
    bis "Это было великолепно!"
    show teachers 56
    player_name "Хаах... Да."
    show teachers 55
    bis "Мы обязаны это сделать снова, Да?"
    show teachers 56
    player_name "Абсолютно!"
    show teachers 55
    bis "Tres Bien(Очень хорошо), mon bel homme(мой красивый мужчина)!"
    bis "Итак, присядь."
    bis "Я приготовлю тебе несколько кусочков сыра которые подойдут к вину..."
    show teachers 56
    player_name "Хорошо..."
    return

label bissettes_office_sex_cum_first:
    bis "Ты вернешся вновь еще на одну ночь?"
    show teacher 45
    show player 26
    player_name "Еще бы!"
    show player
    show teacher 46
    bis "Дождаться не могу!"
    show teacher 45
    show player 36 with dissolve
    player_name "Скоро увидимся, {b}Мисс Биссетт{/b}!"
    show player 426 with dissolve
    show teacher 46
    bis "Au revoir(До свидания), {b}[firstname]{/b}!"
    hide player
    hide teacher
    with dissolve
    $ renpy.end_replay()
    return

label bissettes_office_sex_cum_repeat:
    show player 13 at left
    show teacher 46 at right
    with dissolve
    bis "Это было прекрасно."
    show teacher 45
    show player 26
    player_name "Да,это так."
    show player 13
    show teacher 46
    bis "Хочешь еше одну сессию завра?"
    show teacher 45
    show player 14
    player_name "Может быть, Я дам вам знать."
    show player 13
    show teacher 46
    bis "Очень хорошо. Au revoir(До свидания), {b}[firstname]{/b}!"
    show teacher 45
    show player 36 with dissolve
    player_name "Au revoir(До свидания), {b}Мисс Биссетт{/b}!"
    hide player
    hide teacher
    with dissolve
    $ renpy.end_replay()
    return

label bissettes_office_sex_cum_scene_change:
    scene black
    hide teachers
    hide teachers_chair
    with fade

    pause

    scene expression game.timer.image("french_office_sex_c{}") with fade
    show player 13 at left
    show teacher 46 at right
    with dissolve
    return

label bissettes_office_sex_cum:
    if M_bissette.get("change angle"):
        call expression game.dialog_select("bissettes_office_sex_cum_chair_angle")
    else:
        call expression game.dialog_select("bissettes_office_sex_cum_desk_angle")

    call expression game.dialog_select("bissettes_office_sex_cum_scene_change")

    if M_bissette.is_state(S_bissette_wine_sampling):
        call expression game.dialog_select("bissettes_office_sex_cum_first")
    else:
        call expression game.dialog_select("bissettes_office_sex_cum_repeat")
    $ M_bissette.trigger(T_bissette_sexy_time)
    $ M_bissette.set("night visit", False)
    $ game.timer.tick()
    $ player.go_to(L_school_floor3)
    $ game.main()

label bissette_office_night_lock:
    scene expression game.timer.image("school_hall_third_floor{}_b")
    show player 55 at Position (xoffset=12) with dissolve
    pause
    show player 56 with dissolve
    player_name "Мне нужно идти домой и немного отдохнуть."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
