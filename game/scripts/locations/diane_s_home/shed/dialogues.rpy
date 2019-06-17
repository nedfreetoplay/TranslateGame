label dianes_shed_diane_delivery_2_fetch_goods:
    scene shed
    show player 14 with dissolve
    player_name "Вау!!!"
    player_name "Посмотри на все эти молочные бидоны!"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Неужели {b}Диана{/b} действительно заполнила все это сама?!"
    player_name "Это займет целую вечность, особенно если она будет тащить их к корове одну за другой..."
    show player 4 with dissolve
    player_name "Хмм."
    show player 33 with dissolve
    player_name "Думаю, это объясняет, почему она проводит здесь так много времени."
    show player 13
    player_name "..."
    show player 14
    player_name "Я должен {b}начать с доставки.{/b}"
    hide player with dissolve
    return

label dianes_shed_diane_fetch_pump:
    show player 35 at left with dissolve
    player_name "Вау..."
    show player 34
    player_name "...Какой странный сарай."
    player_name "Что со всеми этими контейнерами?.. А что это за цепи?!"
    show player 43
    player_name "В любом случае, давайте попробуем {b}найти этот насос{/b}..."
    hide player 43 with dissolve
    return

label dianes_shed_milking_help:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    $ M_diane.is_naked = 1
    show player 10 at left
    show diane b_topless_blank a_topless_pump1 f_surprised_front at lright
    with dissolve
    player_name "{b}Диана{/b}?!"
    player_name "Что здесь происходит?"
    player_name "Ты в порядке?"
    show player 5
    show diane f_sad_talk
    dia "Ахххх, нет!"
    dia "Я снова забиваюсь, а насос застрял!"
    show diane f_sad
    show player 10
    player_name "Забиваешься?"
    show player 5
    dia "..."
    show player 10
    player_name "Подожди, эта штука прилипла к твоей груди?"
    show player 5
    show diane f_surprised_down a_topless_pump_stuck with dissolve
    pause
    show diane f_scream
    dia "{b}*ииитттххх*{/b} Ах, это действительно больно!"
    show diane a_topless_pump1 f_tired_down with dissolve
    show player 10
    player_name "Позвольте мне помочь!"
    show player 5
    show diane f_sad_talk
    dia "Нет."
    dia "Я сама."
    show diane f_surprised_down a_topless_pump_stuck with dissolve
    pause
    show diane a_topless_pump1 f_scream with dissolve
    dia "Аааааххх!"
    show diane f_tired_down
    show player 10
    player_name "Да ладно, тебе больно. Просто дай мне взглянуть."
    show player 5
    show diane f_sad_talk
    dia "Хорошо."
    show diane f_surprised_front
    show player 670b at Position (xoffset=100)
    with dissolve
    pause
    show diane f_surprised_down
    dia "Просто будь осторожен."
    show diane f_surprised_front
    player_name "Хорошо, обещаю."
    pause
    player_name "Хмм."
    show player 670c zorder 1 at Position (xoffset=46)
    show diane f_surprised_down a_topless_pump_stuck
    with dissolve
    pause
    player_name "Готово!"
    show player 13
    show diane a_topless_ouch f_surprised_front_talk
    with dissolve
    dia "О, слава богу..."
    show diane f_surprised_front
    player_name "Ты в порядке?"
    show diane f_surprised_front_talk
    dia "Фу, мне намного лучше теперь, когда ты снял с меня этот дурацкий насос."
    show diane b_topless a_naked_sides f_smirk_talk with dissolve
    dia "Спасибо, {b}[firstname]{/b}."
    show diane f_smirk
    show player 429
    player_name "Пожалуйста."
    show player 426
    pause
    show player 14
    player_name "... Ты что-то говорила о засоре?"
    show player 13
    dia "Хмм?"
    show diane f_sad_talk
    dia "О, да."
    dia "Такое иногда случается. У женщин может забиться проток в молочных железах."
    show diane f_sad
    show player 10
    player_name "Больно?"
    show player 5
    show diane f_laugh
    dia "... Ну, это определенно не хорошо!"
    show diane f_smirk
    show player 10
    player_name "Прости..."
    player_name "Как это исправить?"
    show player 5
    show diane f_smirk_talk a_topless_ouch with dissolve
    dia "Обычно я просто надеваю горячий компресс и массирую их."
    show diane f_smirk a_naked_sides with dissolve
    show player 12
    player_name "Значит, массаж может их прочистить?"
    show player 5
    show diane f_smirk_talk
    dia "Да, если ты знаешь, что делаешь."
    show diane f_smirk
    show player 429
    player_name "Можно попробовать?"
    show player 426
    show diane f_surprised
    dia "..."
    show diane f_shamed_talk_smile
    dia "Не уверена, что это хорошая идея."
    show diane f_shamed
    show player 10
    player_name "Мне не нравится видеть твою боль, {b}Диана{/b}."
    player_name "Пожалуйста, позволь мне помочь."
    show player 5
    show diane f_smirk
    dia "..."
    show diane f_explain
    dia "Да, хорошо..."
    show diane a_topless_ouch f_smirk_talk
    show player 426
    with dissolve
    dia "Просто нажми сюда большим пальцем и веди вниз к моему соску."
    show diane f_smirk
    show player 17
    player_name "Хорошо!"
    hide player
    show diane b_topless_blank2 a_topless_waiting f_down_front
    with dissolve
    pause
    show diane b_topless_blank2 a_topless_squeeze1 with dissolve
    player_name "Так?"
    show diane f_shamed_talk_look
    dia "Да. Теперь сожми и потяни."
    show diane a_topless_squeeze f_explain_close with dissolve
    pause
    show diane f_explain
    dia "Даааа. Вот так..."
    show diane f_explain_close
    pause
    show diane f_explain
    dia "Ммм, как хорошо."
    dia "Не помню, когда у меня не болела грудь..."
    show diane f_explain_close
    player_name "Это нехорошо, {b}Диана{/b}."
    show diane f_laugh
    dia "Да, я знаю."
    show diane f_explain
    dia "Мне нужно лучшее оборудование."
    show diane f_lip_bite
    pause
    player_name "Это помогает?"
    show diane f_explain
    dia "Аааа, наверняка..."
    dia "Твои руки восхитительны, {b}[firstname]{/b}!"
    show diane f_down_front
    pause
    show diane f_explain
    dia "Ты очень хорош в этом!"
    show diane f_lip_bite
    pause
    player_name "Как я узнаю, что все исправлено?"
    show diane f_laugh a_topless_squeeze_milk
    dia "Аааххх!" with hpunch
    show diane f_down_front
    pause
    show diane a_topless_squeeze1 with dissolve
    player_name "Хехе, ох."
    show diane a_topless_squeeze_milk with dissolve
    player_name "Думаю, именно так..."
    show diane f_laugh
    dia "Ааааахх... Ааааахх..."
    dia "Фу, спасибо..."
    show player 83b at left
    show diane b_topless a_naked_sides f_smirk
    with dissolve
    player_name "Хехе, пожалуйста."
    player_name "Я просто рад, что хоть раз смог помочь."
    show player 83c
    show diane f_smirk_talk
    dia "У тебя лучшие руки что я видела в своей жизни-"
    show diane f_surprised_down
    dia "!!!"
    pause
    show player 83
    player_name "... ты никогда?"
    show player 82
    show diane f_smirk
    dia "Хмм?"
    show player 83
    player_name "Ты говорила что-то о моих руках."
    show player 82
    show diane f_teasing_look
    dia "Разве?"
    dia "Я совершенно забыла, что говорила...."
    show diane f_smirk
    show player 83b
    player_name "Хе, прости."
    show player 83c
    show diane f_smirk_talk
    dia "Нет, все в порядке {b}[firstname]{/b}..."
    show diane f_teasing_look
    dia "... Я только-"
    show player 78
    show diane b_jerk_pre a_empty f_jerk_down_front at Position (xoffset=-110)
    player_name "!!!" with hpunch
    hide player
    show diane b_jerk2 at Position (xpos=402)
    with dissolve
    player_name "{b}Диана{/b}?"
    player_name "Я думал, ты не хочешь-"
    show diane f_jerk_teasing_look
    dia "Я знаю."
    dia "Честно говоря, я не знаю, чего хочу..."
    show diane b_jerk f_jerk_down_front
    player_name "Это очень приятно."
    pause
    show diane f_jerk_smirk_up_talk
    dia "Обещай, что не скажешь {b}[deb_name]{/b}?"
    show diane f_jerk_smirk_up
    player_name "О, обещаю!"
    pause
    show diane b_jerk2 f_jerk_smirk_up_talk
    dia "Хочешь еще раз попробовать мое молоко?"
    show diane f_jerk_down_front
    player_name "Хмм?"
    player_name "Умм, да... Хорошо, конечно."
    pause
    show diane b_topless a_naked_sides f_smirk at lright
    show player 10 at left
    with dissolve
    player_name "Мне принести насос?"
    show player 5
    show diane f_smirk_talk
    dia "Нет."
    dia "Я подумал, может, ты захочешь..."
    dia "... Ты знаешь, попробовать прямо из-за крана?"
    show diane f_smirk
    pause
    show player 10
    player_name "Ты имеешь в виду-"
    show player 29 with dissolve
    player_name "Д-Да, определенно!"
    show player 3
    show diane f_smirk_talk a_topless_invite with dissolve
    dia "Садись сюда."
    show diane f_smirk
    show player 29
    player_name "На твои колени?"
    show player 3
    dia "Мммммммм."
    show diane f_smirk_talk
    dia "Не стесняйся."
    show player 29
    player_name "Хорошо."
    hide player
    hide diane
    with dissolve
    
    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding1 a_empty f_hay_feeding_explain
    with dissolve
    dia "Давай, красавчик."
    show diane b_hay_feeding f_hay_feeding_lip_bite
    dia "Ммм."
    pause
    show diane f_hay_feeding_explain
    dia "Боже мой, как хорошо!"
    show diane f_hay_feeding_explain_close
    pause
    show diane f_hay_feeding_explain
    dia "Как на вкус?"
    show diane f_hay_feeding_lip_bite
    player_name "Восхитительно!"
    show diane f_hay_feeding_laugh
    dia "Хехе."
    show diane a_hay_feeding_arm f_hay_feeding_shamed_talk_look with dissolve
    dia "У тебя такой классный член, {b}[firstname]{/b}."
    dia "Я упоминала об этом раньше?"
    show diane f_hay_feeding_smirk_down
    player_name "Хе, да. Кажется, ты уже упоминала об этом."
    show diane f_hay_feeding_laugh
    dia "Хаха!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane f_hay_feeding_explain
    dia "Ммм, О да... Продолжай делать это языком."
    dia "Твой рот восхитителен на моем соске!"
    show diane f_hay_feeding_lip_bite
    pause
    show diane b_hay_feeding1 a_empty with dissolve
    dia "Нннгггг!"
    show diane f_hay_feeding_shamed_talk_look
    dia "Ладно, нам лучше остановиться, пока ты не выпил меня досуха, жеребец."
    show diane f_hay_feeding_smirk_down
    player_name "Ауууу."
    show diane f_hay_feeding_explain
    dia "Я знаю..."
    hide diane with dissolve
    $ M_diane.outfit.is_naked = 1
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_topless a_naked_sides f_smirk_talk
    with dissolve
    dia "Мы повторим это в другой раз, хорошо?"
    show diane f_smirk
    show player 14
    player_name "Да, хорошо."
    show player 13
    show diane f_smirk_talk
    dia "Но ты не можешь быть жадным."
    show diane f_laugh
    dia "У меня бизнес!"
    show diane f_smirk
    show player 17
    player_name "Хех, Я знаю."
    show player 13
    show diane f_smirk_talk
    dia "Теперь верни свою милую задницу к работе!"
    show diane f_smirk
    show player 14
    player_name "Да, мэм!"
    hide player
    hide diane
    with dissolve
    return

label dianes_shed_diane_check_shed_light:
    scene expression "backgrounds/location_diane_shed_closeup.jpg"
    show diane b_topless_blank a_topless_pump f_tired
    dia "..."
    show diane f_tired_talk
    dia "{b}*зевая*{/b}"
    show diane f_tired_down
    pause
    player_name "{b}Диана{/b}??"
    show player 10 at left with dissolve
    player_name "Ты здесь?"
    show player 14
    player_name "Я принес тебе-"
    show player 23
    player_name "{b}*вздох*{/b}"
    show diane f_sad_talk
    dia "{b}[firstname]{/b}!!!" with hpunch
    show diane f_surprised
    show player 428
    player_name "!!!"
    show diane f_sad_talk
    dia "Что ты-"
    show diane b_topless a_topless_covering f_surprised with dissolve
    show player 10
    player_name "... вот..."
    player_name "Ты..."
    show player 11
    show diane f_scared
    dia "..."
    show player 12
    player_name "Почему ты используешь молокоотсос коровы на себе?"
    show player 5
    show diane f_sad_talk
    dia "Прости, я не хотела, чтобы ты это ... Подожди, что?!"
    show diane f_sad
    dia "..."
    show diane f_sad_talk
    dia "{b}[firstname]{/b}, это не для коров."
    show diane f_sad
    show player 10
    player_name "... Здесь нет коровы?"
    player_name "Но тогда, откуда все это молоко-"
    show player 11
    pause
    show player 37 with dissolve
    player_name "... О."
    show player 38 with dissolve
    player_name "ОООО!!!"
    player_name "Ты хочешь сказать, все это было-"
    show player 3 with dissolve
    show diane f_sad_talk
    dia "Это грудное молоко."
    dia "Это МОЁ грудное молоко."
    show diane f_sad
    show player 11 with dissolve
    player_name "!!!"
    show player 17
    player_name "Это так здорово!"
    show player 18
    show diane f_shamed_talk_smile
    dia "... Здорово?"
    show diane f_shamed
    show player 14
    player_name "Да!!"
    player_name "Я понятия не имел, что люди могут столько сделать!"
    show player 13
    show diane f_shamed_talk_look
    dia "Ухх..."
    show diane f_shamed
    show player 22
    player_name "{b}*глоток*{/b}"
    show player 14
    player_name "Я только что понял!"
    player_name "... {b}Тонни{/b} делает пиццу с молоком из твоих сисек!!"
    show player 17
    player_name "Это так круто!"
    show player 13
    show diane f_shamed_talk_smile
    dia "Хе-хе, я действительно не думала, что ты так хорошо это воспримешь..."
    dia "Тебя это не беспокоит?"
    show diane f_shamed
    show player 12
    player_name "Нет, с чего бы?"
    show player 13
    dia "..."
    show player 14
    player_name "Можно попробовать?"
    show player 13
    show diane f_surprised_front_talk
    dia "Ты хочешь попробовать?!"
    show diane f_shamed_talk_smile
    dia "Правда?"
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "Умм, конечно. Надеюсь..."
    show diane f_shamed a_topless_milk_cover with dissolve
    pause
    show diane a_topless_covering
    show player 104
    with dissolve
    pause
    show player 105 with dissolve
    pause
    show player 34 with dissolve
    player_name "Хмм."
    show diane f_shamed_talk_smile
    dia "Ну как?"
    show diane f_shamed
    show player 33
    player_name "Сливочное!"
    show player 34
    pause
    show player 33
    player_name "... И оно вроде как... Сладкое."
    show player 34
    pause
    show player 14
    player_name "Мне нравится!"
    show player 13
    show diane f_shamed_talk_smile
    dia "Да?"
    show diane f_shamed
    show player 14
    player_name "Да."
    player_name "Не могу поверить, что ты сама все это сделала!"
    show player 13
    show diane f_laugh
    dia "Хех, да. Это было нелегко."
    show diane f_shamed_talk_smile
    dia "Я дою себя круглосуточно уже несколько недель..."
    show diane f_shamed
    show player 14
    player_name "О, да!"
    player_name "{b}[deb_name]{/b} послала тебе это."
    show player 239_240 with dissolve
    pause
    show player 674 with dissolve
    player_name "Она беспокоится, что ты мало ешь."
    show player 673
    show diane f_shamed_talk_smile
    dia "О, это яблоко?"
    show diane f_shamed
    player_name "Мммммм."
    show diane f_shamed_talk_smile
    dia "Выглядит аппетитно!"
    show diane f_tired_talk
    dia "И она права, я не ела весь день."
    show diane f_tired
    show player 675
    player_name "Это нехорошо, {b}Диана{/b}..."
    player_name "Ты должна позаботиться о себе!"
    show player 676
    show diane f_tired_talk
    dia "{b}*вздыхая*{/b} Я знаю, я слишком сильно давлю себя."
    show diane f_tired
    show player 674
    player_name "Как насчет того, что в следующий раз, когда я приду, ты возьмешь выходной?"
    show player 673
    show diane f_sad_talk
    dia "Целый день?"
    show diane f_tired_talk
    dia "Не знаю..."
    show diane f_tired
    show player 674
    player_name "Да ладно тебе!"
    player_name "Я позабочусь о саде и дам тебе все, что нужно."
    player_name "Ты можешь просто лечь и расслабиться."
    player_name "Разве это не здорово?"
    show player 673
    dia "Хмм."
    show diane f_shamed_talk_smile
    dia "Это действительно здорово..."
    show diane f_shamed
    show player 674
    player_name "Тогда это свидание!"
    show player 673
    show diane f_surprised
    dia "!!!"
    show diane f_shamed_talk_smile
    dia "Ты такой милый, {b}[firstname]{/b}."
    show diane f_shamed
    show player 674
    player_name "Это не проблема."
    show player 673
    show diane f_shamed_talk_smile
    dia "Ты ведь никому не расскажешь?"
    show diane f_shamed
    show player 676
    player_name "Хмм?"
    show diane f_shamed_talk_smile
    dia "Знаешь, насчет молока..."
    show diane f_shamed
    show player 674
    player_name "О, нет. Я никому не скажу."
    show player 673
    show diane f_shamed_talk_smile
    dia "Спасибо, красавчик!"
    show diane f_shamed
    show player 674
    player_name "Сейчас, давай пойдем во внутрь и попробуем пирог {b}[deb_name]{/b}!"
    show diane f_lookup
    dia "Уф!"
    show diane f_shamed_talk_smile
    dia "Я так волновалась, что ты подумаешь, что это мерзко..."
    dia "... Или что я ужасный человек."
    show diane f_shamed
    show player 674
    player_name "Нет же!"
    show player 673
    show diane f_shamed_talk_smile
    dia "Первоначально я использовала коров, но мое грудное молоко было таким хитом..."
    show diane f_shamed
    show player 674
    player_name "Да, очень вкусно!"
    player_name "Я не удивлен, что им оно так нравится."
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_front_night_blur.jpg"
    show player 13
    player_name "( Вау, она клевала носом все время, пока ела. )"
    player_name "( Мне едва удалось затащить ее в постель. )"
    player_name "( Трудно поверить, что все это молоко из {b}Дианы{/b}. )"
    show player 18
    player_name "( Это так круто! )"
    show player 13
    player_name "( Но она работает до изнеможения! )"
    player_name "( ... Может быть, я могу помочь ей наладить нормальную жизнь? )"
    player_name "( А пока я просто должен убедиться, что ее выходной действительно особенный и что она хорошо отдохнет. )"
    hide player with dissolve
    return

label dianes_shed_seen_shed_locked:
    scene garden
    show player 34 with dissolve
    player_name "Хмм..."
    show player 35
    player_name "Дверь заперта."
    hide player 35 with dissolve
    return

label dianes_shed_not_seen_shed_locked:
    scene garden
    show player 35 with dissolve
    player_name "Хм.. Сарай заперт. Интересно, что там?"
    hide player
    hide diane
    with dissolve
    return

label dianes_shed_dewitt_paint:
    scene location_diane_shed01_night_closeup
    show player 588
    with dissolve
    player_name "Наконец-то нашел краску!"
    player_name "Если я принесу это и немного {b}досок{/b} на {b}верстак{/b} в {b}гараж{/b}, я смогу сделать фальшивую гитару, без проблем."
    hide player with dissolve
    $ M_dewitt.trigger(T_dewitt_shed_find_paint)
    if not player.has_item("paint"):
        $ player.get_item("paint")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
