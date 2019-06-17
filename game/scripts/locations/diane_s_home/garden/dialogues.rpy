label dianes_garden_diane_find_carpenter:
    scene garden
    show player 14 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Привет, {b}Диана{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Привет, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "Ты уже говорила с {b}отцом Энни{/b}?"
    player_name "Ну, знаешь, о строительстве амбара?"
    show player 13
    show diane f_normal_talk
    dia "О, да."
    dia "Я говорила с ним по телефону сегодня утром."
    dia "Он сделает его и за хорошую цену."
    show diane f_normal
    show player 17
    player_name "Отличные новости!"
    show player 14
    player_name "Когда он начнет?"
    show player 13
    show diane f_sad_talk
    dia "В этом-то и проблема."
    show player 5
    dia "Он был очень уклончив по телефону."
    show diane f_sad
    show player 10
    player_name "О?"
    show player 5
    show diane f_sad_talk
    dia "Я сказал ему, что мне нужно, чтобы он был завершен как можно скорее, но ему нужно было сначала выполнить несколько неотложных дел в его доме."
    dia "Я надеялся, что ты сможешь помочь-"
    show diane f_sad
    pause
    show diane f_normal_talk
    dia "О, неважно. Это глупо."
    show diane f_normal
    show player 14
    player_name "Нет, продолжай."
    show player 13
    show diane f_normal_talk
    dia "Что ж... Как ты думаешь, ты мог бы пойти туда и помочь ему?"
    show diane f_normal
    show player 12
    player_name "Правда?"
    show player 5
    show diane f_normal_talk
    dia "Да."
    dia "Просто посмотри, можешь ли ты чем-нибудь помочь ему, понимаешь?"
    dia "Все, что угодно, лишь бы он поскорее приехал сюда и начал строить."
    show diane f_normal
    show player 10
    player_name "Хм, думаю, можно попробовать..."
    show player 5
    show diane f_normal_talk
    dia "Я была бы очень признательна, красавчик."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    hide diane
    show player 29 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Хех, нет проблем!"
    show player 13 with dissolve
    show diane f_normal_talk
    dia "Я буду в сарае, если понадоблюсь."
    hide diane with dissolve
    pause
    show player 12
    player_name "Хм, я полагаю, что я должен направиться в {b}дом Энни{/b} и {b}поговорить с ее отцом.{/b}"
    hide player with dissolve
    return

label garden_diane_drunken_splur_aftermath:
    scene garden
    show player 35 with dissolve
    player_name "Нет смысла сегодня работать в саду..."
    player_name "Я вернусь в другой раз."
    hide player with dissolve
    $ game.main()
    return

label garden_diane_gardening_help:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 684
    player_name "( Фу, сегодня на улице очень жарко... )"
    pause
    show player 685
    player_name "( Надеюсь, {b}Диана{/b} хорошо себя чувствует в сарае. )"
    player_name "( Последние пару лет она держалась на расстоянии... )"
    dia "ООООЙЙЙЙ!!!" with hpunch
    show player 23 with dissolve
    player_name "*глоток* {b}Диана?!{/b}"
    show player 22
    dia "Ой! Ой! Ой!"
    show player 12
    player_name "Бегу!!!"
    hide player with dissolve
    return

label dianes_garden_diane_drunk_like_a_sailor:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_wave f_laying_laugh zorder 2 at Position (ypos=982)
    with dissolve
    dia "Ю-ху, {b}[firstname]{/b}!!!"
    show diane f_laying_smirk_talk
    dia "Можешь подойти на секундочку?"
    show diane f_laying_smirk
    player_name "Иду!"
    show diane a_drink_sip f_laying_drinking with dissolve
    pause
    show diane a_drink f_laying_smirk_up
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    with dissolve
    player_name "Что случилось, {b}Диана{/b}?"
    player_name "Тебе что-то нужно?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Я просто боюсь, что сгорю, сидя здесь на солнце..."
    show diane f_laying_smirk_up_talk a_wave with dissolve
    dia "Как думаешь, ты мог бы мне помочь?"
    show diane f_laying_smirk_up
    show player 435
    player_name "Хочешь, я намажу тебя солнцезащитным кремом?"
    show player 434
    show diane f_laying_laugh a_single_bottle with dissolve
    dia "О да, очень!"
    show diane f_laying_smirk_up
    show player 435
    player_name "{b}*глоток*{/b} Да, хорошо."
    show player 434
    hide diane
    show diane f_laying_sitting_smirk_up_talk b_laying_sitting_topless a_empty zorder 2 at Position (yoffset=92)
    with dissolve
    dia "Дай мне секунду..."
    show diane_chair down
    show diane laying1 zorder 2
    with dissolve
    pause
    show player 426 at Position (xpos=387,ypos=648) with dissolve
    pause
    show player 427
    player_name "Ты хочешь, чтобы солнцезащитный крем был под этими ремнями?"
    show player 426
    dia "Конечно!"
    dia "И если от этого станет легче, просто оттащи их назад..."
    show player 429g
    player_name "!!!"
    hide player
    show diane laying_remove1
    with dissolve
    pause
    show diane laying_remove2 with dissolve
    pause
    show player 429 zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    player_name "Так?"
    show player 426
    dia "There we go."
    dia "Давай, жеребец!"
    player_name "..."
    show player massage 2 with dissolve
    pause
    show player massage 3 with dissolve
    pause
    hide player
    show diane laying_massage_back
    with dissolve
    dia "Ммм, это чудесно!"
    dia "Убедитесь, что ты не пропустил ни сантиметра."
    show player 429b zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    player_name "Ммммммм."
    hide player
    show diane laying_massage_back
    with dissolve
    pause
    pause
    show player massage 3 zorder 0 at Position (xpos=560,ypos=798)
    show diane laying2
    with dissolve
    dia "О, это очень мило..."
    pause
    show player massage 5
    show diane laying3
    with dissolve
    pause
    show diane laying4 with dissolve
    pause
    show player massage 4
    show diane laying5
    with dissolve
    player_name "!!!"
    player_name "( Она действительно хочет, чтобы я втирал туда лосьон? )"
    pause
    show player massage 5
    dia "Не останавливайся, {b}[firstname]{/b}!"
    show player 429h with dissolve
    player_name "Хе, хорошо."
    hide player
    show diane laying_massage_naked_back
    with dissolve
    pause
    pause
    player_name "Вот так..."
    show diane laying_massage_butt with dissolve
    pause
    dia "О, боже..."
    pause
    show player 429h zorder 0 at Position (xpos=560,ypos=798)
    show diane laying5
    with dissolve
    player_name "Я эээ... Думаю я закончил, {b}Диана{/b}."
    show player 429d
    dia "Хмм?"
    dia "Ты уверен, что ничего не пропустил?"
    show player 429g
    player_name "..."
    dia "Хехехе, я просто дразню тебя, красавчик."
    show player 429b
    player_name "Мне нужно вернуться к работе."
    show player 429g
    show diane laying_getup with dissolve
    dia "Я так не думаю!"
    player_name "!!!"
    show diane laying_kick
    show diane_chair up
    with dissolve
    dia "Ты все еще должен сделать с этой стороны!"
    show diane b_laying_back_naked a_laydown f_laying_smirk_up at Position (ypos=982)
    show player 429b at Position (xpos=355,ypos=648)
    with dissolve
    player_name "{b}*глоток*{/b} Правда?"
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Мммммм."
    dia "Ты же не хочешь, чтобы я сгорела?"
    show diane f_laying_smirk_up
    show player 429b
    player_name "Нет..."
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Начни с моей груди."
    show diane f_laying_smirk_up a_cream with dissolve
    show player 429b
    player_name "Ты уверена?"
    show player 429c
    show diane f_laying_smirk_up_talk
    dia "Да!"
    dia "... Давай помогу."
    show diane a_laydown
    show player 429i at Position (xpos=387,ypos=648)
    with dissolve
    dia "Просто положи руку..."
    hide player
    show diane b_laying_grope1 f_laying_smirk_up_talk
    with dissolve
    dia "... Прямо сюда..."
    with dissolve
    show diane b_laying_grope f_laying_explain_close with dissolve
    pause
    show diane f_laying_explain
    dia "Ооооо, это как раз то, что мне нужно {b}[firstname]{/b}!"
    show diane f_laying_explain_close
    pause
    show diane f_laying_explain
    dia "Моя грудь так болит от дойки..."
    show diane f_laying_explain_close
    player_name "Ммммммм."
    pause
    show diane f_laying_explain
    dia "Нннггхх!"
    dia "Осторожнее с моими сосками, они сейчас очень чувствительные..."
    show diane f_laying_explain_close
    pause
    show diane b_laying_back_naked
    show player 81 at Position (xpos=403,ypos=648)
    with dissolve
    player_name "( О нет, только не это! )"
    show player 78
    show diane f_laying_explain
    dia "Хмм?"
    show diane f_laying_smirk_up_talk
    dia "Почему ты остановился-"
    show diane f_laying_surprised_down
    dia "!!!" with hpunch
    show player 426e with dissolve
    player_name "Прости, {b}Диана{/b}!"
    player_name "Я не думал-"
    show diane f_laying_smirk_up_talk
    dia "Шшш!"
    dia "Все хорошо, {b}[firstname]{/b}..."
    dia "Ты просто немного взволнован, помогая мне."
    dia "Это совершенно естественно."
    show diane f_laying_smirk_up
    show player 427b with dissolve
    player_name "Да, но..."
    show player 78 with dissolve
    show diane f_laying_smirk_up_talk
    dia "Могу я отплатить тебе тем же?"
    show diane f_laying_smirk_up
    show player 427b with dissolve
    player_name "Что ты хочешь-"
    show player 427c
    player_name "!!!" with hpunch
    show player 427d_e
    pause
    show diane f_laying_smirk_up_talk
    dia "Тебе приятно, не так ли?"
    show diane f_laying_smirk_up
    player_name "Да..."
    player_name "Очень приятно!"
    show diane f_laying_laugh
    dia "Хехе, видишь?"
    show diane f_laying_smirk_up_talk
    dia "Здесь нечего стесняться"
    show diane f_laying_smirk_up
    pause
    show diane f_laying_smirk_up_talk
    dia "Я не чувствовала ничего подобного ооооооочень давно."
    show diane f_laying_smirk_up
    player_name "..."
    pause
    show diane f_laying_laugh
    dia "Не могу поверить, что у тебя такой большой!"
    show diane f_laying_smirk_up
    player_name "Я..."
    player_name "... Спасибо."
    show diane f_laying_laugh
    dia "Хехехе."
    show diane f_laying_smirk_up
    pause
    player_name "{b}Диана{/b}, Я сейчас..."
    show diane f_laying_smirk_up_talk
    dia "Давай, жеребец."
    show diane f_laying_smirk_up
    pause
    show player 426b
    player_name "ХННГГГГ!!!" with flash
    pause
    player_name "Аааа... Ааааа..."
    player_name "!!!"
    show player 426g
    player_name "О мой бог, {b}Диана{/b}, Прости!"
    player_name "Я не хотел-"
    show player 426h
    show diane f_laying_smirk_up_talk
    dia "Хе-хе, тебе не за что извиняться, {b}[firstname]{/b}!"
    dia "Давай зайдем в дом и приведем тебя в порядок..."
    show diane f_laying_smirk_up
    show player 426g
    player_name "Хорошо."
    hide player
    hide diane
    hide diane_chair
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 139 at left
    show diane b_shirtless f_smirk a_shirtless_sides at lright
    with dissolve
    player_name "..."
    show diane f_smirk_talk
    dia "Ммм, видишь? Только быстро- *ик*"
    dia "Просто быстро почистим и ты как новенький!"
    show diane f_smirk
    show player 140
    player_name "Да..."
    show player 139
    show diane f_smirk_talk
    dia "Кажется, я опять слишком много выпила."
    dia "Мне нужно прилечь."
    dia "Спасибо за мой выходной, {b}[firstname]{/b}!"
    show diane f_laugh
    dia "Это было именно то, что доктор прописал."
    show diane f_smirk
    show player 140
    player_name "Я рад, что тебе понравилось."
    show player 139
    show diane f_laugh
    dia "Хехе, очень!"
    hide player
    show diane kiss_mouth
    with dissolve
    player_name "!!!"
    show player 3 at left
    show diane b_shirtless f_smirk_talk a_shirtless_sides at lright
    with dissolve
    dia "Спокойной ночи, жеребец!"
    hide diane with dissolve
    show player 29
    player_name "Спокойной ночи..."
    $ renpy.end_replay()
    show player 3
    player_name "..."
    player_name "( Не могу поверить, что это случилось! )"
    player_name "( {b}Диана{/b} только... )"
    show player 18 with dissolve
    player_name "( ... )"
    player_name "( ... Вау! )"
    show player 13
    player_name "( Надеюсь, с ней все в порядке. )"
    player_name "( Мне пора домой. )"
    hide player with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["02_unlocked"] = True
    return

label garden_diane_check_up:
    scene garden
    show player 14 with dissolve
    player_name "Я должен найти {b}Диану{/b}."
    show player 35
    player_name "{b}... Может быть она в доме?{/b}"
    hide player with dissolve
    return

label dianes_garden_diane_clear_bug_infested_garden:
    scene garden_dead
    show player 14 at left
    show diane b_casual a_casual_sides
    with dissolve
    player_name "Похоже, я пропустил несколько гнезд..."
    show player 13
    show diane f_normal_talk
    dia "Не волнуйся, {b}пестицид{/b} позаботится о них."
    dia "Давай, начинай распылять, пока я переодеваюсь."
    dia "Когда я вернусь, мы сможем начать пересадку."
    show diane f_normal
    show player 14
    player_name "Звучит хорошо."
    hide player
    hide diane with dissolve
    return

label diane_garden_first_time:
    show expression "backgrounds/location_diane_garden_cutscene05.jpg"
    show expression FilteredText("Я ничего не знал о садоводстве, но было приятно увидеть {b}Диану{/b}.\nВ детстве она мне всегда нравилась.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause    
    hide cutscene
    show expression FilteredText("С ней было просто весело общаться!\nДобросердечная и заботливая.\nОтличное чувство юмора и внимательная.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide cutscene
    show expression FilteredText("Надеюсь, я ее не разочарую...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade

    scene garden
    show player 1 at left
    show diane f_normal_talk at right
    with dissolve
    dia "Ну, что красивый молодой человек..."
    show diane f_laugh
    show player 13
    dia "Ты так вырос, что я едва узнала тебя на похоронах."
    show diane f_normal
    show player 17
    player_name "Хе, привет {b}Diane{/b}."
    show diane f_surprised
    show player 2
    player_name "Ух ты! Ты так похожа на {b}[deb_name]{/b}..."
    show diane f_thinking
    show player 1
    dia "Ох, ладно. Я далеко не так красива, как  {b}[deb_name]{/b}..."
    show diane f_surprised
    show player 33
    player_name "Ну, я думаю, ты выглядишь великолепно, {b}Диана{/b}!"
    show diane a_dressed_blush f_laugh_blush with dissolve
    show player 1
    dia "Разве ты не очаровашка?!"
    show diane f_surprised
    show player 11
    dia "..."
    show diane f_laugh_blush with dissolve
    dia "Ты здесь, чтобы сделать кое-какую работу для меня?"
    show diane f_normal_talk
    show player 1
    dia "Я предполагаю, что {b}[deb_name]{/b} сказала тебе, что я ищу кого-то, кто поможет мне этим летом?"
    show diane f_normal
    show player 2
    player_name "Да, она сказала мне прийти к тебе. Мне определенно нужны деньги на обучение."
    show diane f_normal_talk
    show player 5
    dia "Прекрасно!"
    dia "Я надеялась, что ты начнешь сегодня, но, боюсь, я столкнулась с проблемой..."
    show diane f_shamed_talk_look a_dressed_broken with dissolve
    dia "Моя старая лопата сломалась."
    show diane f_shamed
    show player 10
    player_name "О! Да, выглядит довольно плохо."
    show diane f_shamed_talk_smile
    show player 1
    dia "Возможно, придется подождать, пока я ее заменю..."
    dia "Прости, {b}[firstname]{/b}."
    show diane f_shamed
    show player 2
    player_name "Все хорошо, {b}Диана{/b}."
    show player 2 at left
    show diane f_normal at right with dissolve
    player_name "Есть ли способ продолжить работу без нее?"
    show diane f_normal_talk
    show player 1
    dia "Ну, мы же не можем копать сад без лопаты, не так ли?"
    dia "В следующий раз, когда буду в магазине, куплю новую."
    show diane f_teasing
    show player 11
    dia "Разве что..."
    show player 10
    show diane f_normal
    player_name "Что?"
    show player 11
    show diane f_normal_talk
    dia "... У тебя случайно нет дома лопаты?"
    show player 4
    show diane f_normal
    player_name "Хмм..."
    show player 2
    player_name "У нас есть {b}лопата{/b} в гараже!"
    player_name "Пойду проверю и вернусь, если найду."
    show player 203
    show diane f_laugh
    dia "Было бы здорово!"
    show diane f_normal_talk
    dia "Возвращайся, если найдешь, и мы начнем."
    hide diane
    hide player
    with dissolve
    return

label diane_garden_need_shovel_has_shovel:
    scene garden
    show player 239_240 at left
    show diane a_dressed_sides at lright
    with dissolve
    player_name "Хмм..."
    show player 241 with dissolve
    pause
    show player 242 with dissolve
    pause
    show player 244 with dissolve
    player_name "Вот!"
    show player 243
    show diane f_laugh
    dia "Ох! Прекрасно!"
    show diane f_normal_talk
    dia "Видишь, ты уже очень помог!"
    dia "Хорошо, прежде чем ты начнешь, я покажу тебе, что делать..."
    show diane a_dressed_finger f_explain with dissolve
    show player 11
    with dissolve
    dia "Убедитесь, что остались {b}только{/b} {b}длинные{/b} и {b}твердые{/b} овощи!"
    dia "Убери все остальное... Особенно этих надоедливых крыс и жуков, понятно?"
    show diane a_dressed_shovel f_normal with dissolve
    show player 14
    player_name "Ясно!!"
    show diane f_normal_talk
    show player 1
    dia "Ты должен положить все деньги, которые я плачу тебе в {b}Банк{/b}, когда закончишь!"
    dia "Но это твое решение."
    show diane f_normal
    show player 4
    player_name "Ммм, конечно. Думаю, я смогу это сделать..."
    show diane f_laugh
    show player 1
    dia "Ладно, красавчик, за работу!"
    hide player
    show diane kiss
    with dissolve
    player_name "..."
    hide diane with dissolve
    show expression "boxes/popup_garden.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_garden.png" with dissolve
    return

label diane_garden_need_shovel_no_shovel:
    scene expression player.location.background_blur with None
    show player 2 at left
    show diane f_normal at right
    with dissolve
    player_name "Я все еще не нашел {b}лопату{/b}."
    player_name "Есть ли способ продолжить работу без нее?"
    show diane f_normal_talk
    show player 1
    dia "Ну, мы же не можем копать сад без лопаты, не так ли?"
    dia "В следующий раз, когда буду в магазине, куплю новую."
    show diane f_teasing
    show player 11
    dia "Разве что..."
    show player 10
    show diane f_normal
    player_name "Что?"
    show player 11
    show diane f_normal_talk
    dia "... У тебя случайно нет дома лопаты?"
    show player 4
    show diane f_normal
    player_name "Хмм..."
    show player 2
    player_name "У нас есть {b}лопата{/b} в гараже!"
    player_name "Пойду проверю и вернусь, если найду."
    show player 203
    show diane f_laugh
    dia "Было бы здорово!"
    show diane f_normal_talk
    dia "Возвращайся, если найдешь, и мы начнем."
    hide diane
    hide player
    with dissolve
    return

label diane_garden_delivery_1_task:
    scene garden
    show player 13 at left
    show diane f_normal_talk at lright
    with dissolve
    dia "О, {b}[firstname]{/b}, Я так рада, что ты пришел сегодня!"
    show diane f_normal
    show player 10
    player_name "Еще одна чрезвычайная ситуация в саду?"
    show player 5
    show diane f_laugh
    dia "Хех, не совсем..."
    show diane f_normal_talk
    dia "Я ведь еще не рассказала тебе о своих побочных делах?"
    show diane f_normal
    show player 12
    player_name "Побочный бизнес? Я думал, ты живешь на деньги, которые получила при разводе?"
    show player 5
    show diane f_smirk_talk
    dia "Хех, ну, я делаю по большей части. Мой маленький стартап-это скорее любимый проект, чем реальная попытка заработать деньги..."
    show diane f_smirk
    show player 14
    player_name "Ладно, так в чем дело?"
    show player 13
    show diane f_normal_talk
    dia "Я упаковываю и продаю молоко."
    show diane f_normal
    show player 14
    player_name "Молоко?! Я не знал, что у тебя есть корова! Это потрясающе!"
    show player 13
    dia "..."
    show player 32 with dissolve
    player_name "Где она? Можно ее погладить?"
    show player 31
    show diane f_laugh
    dia "Хахаха!"
    show diane f_smirk_talk
    dia "Прости, красавчик. Моя корова... Что ж... Скажем так, она не любит гостей."
    show diane f_smirk
    show player 10 with dissolve
    player_name "Ааа, хорошо..."
    player_name "Так с чем тебе нужна моя помощь?"
    show player 13
    show diane f_normal_talk
    dia "Ну, из местной пиццерии сделали заказ, и мне нужен кто-то, кто доставит его."
    show diane f_normal
    show player 14
    player_name "Я смогу это сделать!"
    show player 13
    show diane f_normal_talk
    dia "Ты не против?"
    dia "Это было бы огромной помощью."
    show diane f_normal
    show player 14
    player_name "Нет, я совсем не против."
    show player 13
    show diane f_laugh
    dia "О, прекрасно!"
    hide player
    show diane kiss
    with dissolve
    pause
    show player 5 at left
    show xtra 21 at left
    show diane f_normal_talk
    with dissolve
    dia "Я не знаю, что бы я без тебя делала, {b}[firstname]{/b}!"
    show diane f_normal
    hide xtra 21
    show player 21
    player_name "Хех, это не проблема. Я люблю помогать!"
    show player 13
    show diane f_normal_talk
    dia "Давай я принесу тебе пакет..."
    hide diane with dissolve
    pause
    show player 18
    player_name "( Вау, это так круто! )"
    player_name "( {b}Диана{/b} в глубине души похожа на деревенскую девушку. )"
    show player 33
    player_name "( Надеюсь, когда-нибудь она познакомит меня со своей коровой... )"
    show player 13
    show diane f_normal_talk a_dressed_milk_package with dissolve
    dia "Вот."
    show diane f_normal
    show player 427
    player_name "Ух ты, на нем твое лицо и все такое!"
    show player 426
    show diane f_smirk_talk
    dia "Ага."
    show diane f_smirk
    show player 427
    player_name "Хмм, {b}\"Оригинал тетушки Дианы.\"{/b}"
    show player 426
    show diane f_smirk_talk
    dia "Хехехе, тебе нравится?"
    show diane f_smirk
    show player 14
    player_name "Да, звучит неплохо!"
    show player 13
    show diane f_smirk_talk
    dia "Я тоже так думаю."
    show diane f_cheese a_dressed_shovel
    show player 163e
    with dissolve
    player_name "Итак, куда я это везу?"
    show player 163d
    show diane f_normal_talk
    dia "Вниз по дороге в маленький ресторанчик под названием, {b}\"Пицца Тони.\"{/b}"
    show diane f_normal
    show player 163e
    player_name "Я слышал об этом месте!"
    player_name "Мы получаем {b}рекламки{/b} от них в {b}почтовом ящике{/b}."
    show player 163d
    show diane f_normal_talk
    dia "Да, я слышала, они довольно хороши."
    dia "Передай от меня привет {b}Тони{/b}, ладно?"
    dia "Да,и не забудь забрать деньги."
    show diane f_normal
    show player 163e
    player_name "Конечно."
    player_name "Я вернусь как Флэш!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_drunken_splur:
    scene location_diane_garden_close_day_blur with None
    show player 11 at left
    show diane b_shirtless a_shirtless_drink f_drunk_talk at lright
    with dissolve
    dia "Ю-ху! Вот ты где, красавчик!"
    show player 5
    dia "Как у тебя-*ик* сегодня дела?"
    dia "Ты здесь, чтобы дать мне еще одно-*ик*"
    dia "... Еще одно шоу?!"
    show diane a_shirtless_drink_sip with dissolve
    show player 12
    player_name "{b}Диана{/b}? Ты пьяна?"
    show player 11
    show diane a_shirtless_drink with dissolve
    dia "Хехехе, даааааа..."
    dia "Чуть чуть!"
    dia "Здесь так жарко, понимаешь?!"
    dia "Мне просто-*ик*"
    dia "Мне просто нужно немного чего-то чтобы охладить себя..."
    dia "... И я подумала про себя, \"сама,\" {b}*ик*{/b} \"дополнительный бизнес действительно начинает набирать обороты!\""
    dia "Если это не повод для праздника, то я не знаю, что это!"
    show diane a_shirtless_drink_sip with dissolve
    pause
    show diane b_shirtless_pull a_shirtless_drink_pull f_drunk with dissolve
    player_name "!!!"
    show diane f_drunk_talk
    dia "Ты хочешь отпраздновать со мной, {b}[firstname]{/b}?"
    show diane f_drunk
    show player 22
    pause
    show player 10
    player_name "{b}Диана{/b}, твоя одежда... Она... сползла."
    show player 11
    show diane f_drunk_talk
    dia "А? Что..."
    show diane a_shirtless_drink_hand_pull with dissolve
    dia "О!!"
    show diane a_shirtless_reach_pull f_laugh_blush with dissolve
    dia "Хахаха!"
    show player 21
    show diane f_shamed
    player_name "Хе..."
    show player 13
    show diane f_shamed_talk
    dia "Наверное, мне не стоило снимать рубашку, да?"
    dia "Хотя она не поможет, имея эти... Массивные титьки которые вываливаются ото всюду!!"
    show diane f_laugh_blush
    dia "Хаха!"
    show diane b_shirtless a_shirtless_reach f_shamed with dissolve
    pause
    show player 11
    show diane b_shirtless_pull a_shirtless_drink_hand_pull with dissolve
    dia "Упс! Они пытаются сбежать!"
    show diane a_shirtless_reach_pull f_laugh_blush with dissolve
    dia "Хаха!"
    show player 1
    show diane b_shirtless a_shirtless_drink f_drunk_talk at right with fastdissolve
    dia "Вот."
    dia "Я когда-нибудь говорила тебе, как сильно мне не нравится другой житель у {b}[deb_name]{/b}?"
    show player 10
    show diane f_drunk
    player_name "Эээ, нет. Ты говоришь о, {b}[jen_name]{/b}?"
    show player 5
    show diane f_laugh_blush
    dia "Да! *ик* О ней!"
    show diane f_drunk_talk
    dia "Она такая сууууучка!"
    show diane f_drunk
    show player 11
    pause
    show diane f_drunk_talk
    dia "Жаль, что у меня нет таких красивых молодых сисек, как у нее..."
    show diane a_shirtless_drink_sip with dissolve
    pause
    show diane a_shirtless_drink with dissolve
    dia "В чем дело?"
    dia "Тебе не нравятся ее сиськи?"
    show diane f_drunk
    show player 24
    player_name "Я... Эээ..."
    show diane a_shirtless_drink_hand with dissolve
    dia "Ты хочешь сказать, что не заметил их?"
    show diane a_shirtless_drink with dissolve
    show player 10
    player_name "Ну... Я не знаю."
    show diane f_drunk_talk
    show player 11
    dia "Тут."
    show diane b_shirtless_pull a_shirtless_pull f_drunk with fastdissolve
    show player 22
    pause
    show diane f_drunk_talk
    show player 11
    dia "Тебе не кажется, что они выглядят лучше, чем эти старые штуки?"
    show diane f_drunk
    show player 21
    player_name "Нет, я думаю, твоя грудь выглядит великолепно, {b}Диана{/b}."
    show diane f_drunk_talk
    show player 13
    dia "Аааа!"
    dia "Ты так-*ик*"
    dia "... Такой милый!"
    show diane f_drunk
    pause
    show diane a_shirtless_reach_pull f_shamed_talk with dissolve
    show player 11
    dia "Хмм..."
    dia "Я не чувствую себя так хорошо внезапно."
    dia "Думаю, мне нужно... -*ик*"
    dia "Мне нужно немного прилечь..."
    show diane sitting_drunk with dissolve
    show player 427
    player_name "Эй, эй, эй!"
    player_name "{b}Диана{/b}, ты не можешь просто лежать в саду..."
    show player 13
    show diane b_shirtless_pull a_shirtless_reach_pull f_shamed_talk
    with dissolve
    dia "Хмм?"
    show diane f_shamed
    show player 14
    player_name "Давай я помогу тебе подняться в постель!"
    show player 13
    show diane f_drunk_talk
    dia "О, ты бы сделал это ради-*ик*"
    dia "... Сделаешь это для меня?"
    show diane f_drunk
    show player 14
    player_name "Конечно, так..."
    hide player
    show diane hold_talk
    with dissolve
    dia "Ммм, такой услужливый молодой человек..."
    show diane hold_peek
    pause
    show diane hold_talk
    dia "Ты намного милее, чем все остальные никчемные мужчины в этом городе!"
    show diane hold_peek
    player_name "..."
    dia "..."
    show diane hold_talk
    dia "Хехехе, спальня на верхнем этаже, жеребец."
    show diane hold
    player_name "!!!"
    player_name "Точно, прости."
    hide diane with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene07.jpg"
    show expression FilteredText("Я никогда не видел {b}Диану{/b} такой пьяной раньше!\nЯ помог ей подняться по лестнице в ее комнату, изо всех сил стараясь слушать, как она пьяным голосом изливает душу.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("Она все говорила и говорила о своем никчемном бывшем муже и о мужчинах, которых встречала после развода.\nЯ начал подозревать, что в этом пьяном эпизоде было\nнечто большее, чем простое празднование. ") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade
    scene expression "backgrounds/location_diane_bedroom_closeup.jpg"
    show diane hold_tired_talk
    dia "... Он даже не разговаривал со мной о детях, никчемный придурок."
    dia "Какой мужчина не захочет остепениться и завести семью?!"
    show diane hold_tired
    player_name "..."
    show diane hold_tired_talk
    dia "... Теперь он, наверное, играет в азартные игры и трахает дешевых шлюх!"
    show diane hold_tired
    player_name "Хорошо {b}Диана{/b}, вот мы и..."
    player_name "Давай уложим тебя в кроватку, хорошо?"
    show diane hold_talk
    dia "Пффф, хахаха!"
    dia "Ты первый человек, который сказал мне это за дооооооолгое время!"
    show diane hold
    player_name "!!!"
    show diane hold_talk
    dia "Хахаха!"
    dia "Ой, Я только-*ик*"
    dia "Я просто дразню тебя, жеребец..."
    dia "Думаю, дальше я справлюсь."
    show diane b_shirtless_pull a_shirtless_tired f_drunk_talk
    show player 13 at left
    with dissolve
    dia "Почему бы тебе не сходить на кухню и не принести мне стакан воды?"
    show diane f_drunk
    show player 14
    player_name "Да, хорошо."
    show player 13
    show diane f_drunk_talk
    dia "Хороший мальчик."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_mouse_attack_not_known:
    scene garden with None
    show player 1f with dissolve
    pause
    show player 32f at Position(xoffset=-69)
    player_name "Ха. А где {b}Диана{/b}?"
    player_name "Обычно она работает в саду..."
    show player 31 at Position(xoffset=68)
    pause
    show player 30
    player_name "Не похоже, что она в своем сарае."
    show player 12
    player_name "Она должна быть в доме. На улице сегодня очень жарко."
    show player 5
    player_name "..."
    show player 10
    player_name "Может, мне стоит проверить ее, прежде чем я начну работать."
    hide player with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane f_normal_talk
    with dissolve
    dia "А, вот и ты. Слава богу!"
    dia "Я уже начала думать, что ты сегодня не придешь."
    show player 2
    show diane f_normal
    player_name "Привет, {b}Диана{/b}!"
    player_name "Все в порядке?"
    show diane f_normal_talk
    show player 203
    dia "Все в порядке. Ты отлично поработал в моем саду, {b}[firstname]{/b}!"
    dia "На самом деле, ты так хорошо справляешься, что у нас осталась тонна отходов!"
    show diane f_normal
    show player 17
    player_name "Прости. Хаха."
    show diane f_normal_talk
    show player 203
    dia "Не извеняйся, милый!"
    dia "Мне просто нужна помощь, чтобы перенести их."
    dia "Я погрузила все в эту {b}тачку{/b}..."
    dia "... Но боюсь, она слишком тяжелая для моей бедной спины."
    dia "Как ты думаешь, ты мог бы мне помочь?"
    show player 14
    show diane f_normal
    player_name "Конечно!"
    player_name "Для этого я здесь!"
    show player 13
    show diane f_normal_talk
    dia "Только будь осторожен, она очень тяжелая!"
    show player 2
    show diane f_normal
    player_name "Без проблем!"
    player_name "Я позабочусь об этом!"
    return

label dianes_garden_diane_need_shovel_remove_waste_repeat:
    scene expression player.location.background_blur with None
    show player 203 at left
    show diane f_normal_talk
    with dissolve
    dia "Я уже начала думать, что ты сегодня не придешь."
    show player 2
    show diane f_normal
    player_name "Привет, {b}Диана{/b}!"
    player_name "Все в порядке?"
    show diane f_normal_talk
    show player 203
    dia "Все в порядке. Мне просто нужна помощь в перемещении этой {b}тачки{/b}..."
    dia "... Но боюсь, она слишком тяжелая для моей бедной спины."
    dia "Как ты думаешь, ты мог бы мне помочь?"
    show player 14
    show diane f_normal
    player_name "Конечно!"
    player_name "Для этого я здесь!"
    show player 13
    show diane f_normal_talk
    dia "Только будь осторожен, она очень тяжелая!"
    show player 2
    show diane f_normal
    player_name "Без проблем!"
    player_name "Я позабочусь об этом!"
    return

label dianes_garden_diane_need_shovel_remove_waste_pass:
    scene expression player.location.background_blur with None
    show player 255 at left
    show diane f_normal
    with dissolve
    player_name "Поехали."
    player_name "Видишь, я справлюсь!"
    show player 254
    show diane f_laugh_blush
    dia "!!!" with hpunch
    dia "Круто... Ты поднял ее, как будто она пустая!"
    show diane f_smirk
    pause
    show player 254
    show diane f_smirk_talk
    dia "Сильный и красивый..."
    dia "Бьюсь об заклад, тебе приходится отбиваться от этих девчонок в школе палкой, не так ли?!"
    show diane f_smirk
    show player 255
    player_name "Ха, нет... не совсем."
    show player 254
    show diane f_laugh
    dia "Да ладно тебе! Ни на секунду в это не поверю!"
    show diane f_smirk_talk
    dia "В молодости я бы в одно мгновение набросился на тебя!"
    show diane f_smirk
    show player 255
    show xtra 21 at Position (xpos=88) with dissolve
    player_name "Хехе."
    player_name "Я эээ..."
    player_name "... Куда вывалить?"
    show player 254
    show diane f_smirk_talk
    dia "Хмм?"
    show diane f_lookup
    dia "О, точно!"
    show diane f_normal_talk
    dia "Просто следуй за мной, красавчик."
    dia "Я держу компостную яму прямо здесь, за домом."
    show diane f_normal
    show player 255
    hide xtra with dissolve
    player_name "Компостную?"
    player_name "Типа, мусор?"
    show player 254
    show diane f_laugh
    dia "Что? Хехе, нет!"
    show diane f_normal_talk
    dia "Компост - ценный ресурс для садовода, {b}[firstname]{/b}!"
    dia "Все, что органическое вещество разлагается и создает богатое питательными веществами удобрение для почвы."
    show diane f_normal
    show player 255
    player_name "Неужели? Так это помогает растениям расти?"
    show player 254
    show diane f_normal_talk
    dia "Точно!"
    dia "Это то, что делает мои овощи такими..."
    show diane f_smirk_talk
    dia "Большими."
    show diane f_smirk
    show player 255
    player_name "Потрясающе!"
    player_name "Я многому учусь у тебя, {b}Диана{/b}!"
    hide location_diane_garden_day_blur
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene04.jpg"
    show expression FilteredText("Компостная яма за ее домом была так далеко!\n Я еле успевал; тачка выскальзывала у меня из рук.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("И все же было приятно катить тачку для {b}Дианы{/b}.\n... И я много узнал о садоводстве!") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide cutscene
    scene black
    with fade
    scene location_diane_garden_day_blur
    show player 18 at left
    show diane f_laugh_blush at lright
    with dissolve
    dia "Я не могу поверить, что ты сделал это с такой легкостью!"
    show diane f_normal
    show player 17
    player_name "Это было довольно трудно, на самом деле. Ха-ха!"
    show player 203
    show diane f_normal_talk
    dia "Что ж, я очень рада, что ты здесь..."
    dia "Не знаю, что бы я без тебя делала!"
    show diane f_normal
    show player 2
    player_name "Ничего страшного."
    player_name "Мне нравится тренировка!"
    show player 203
    show diane f_teasing
    dia "Держу пари, что ..."
    dia "... ты постоянно тренируешься."
    show diane f_smirk
    show player 11
    player_name "..."
    show player 21
    player_name "Что ты имеешь в виду?"
    show player 13
    show diane f_laugh
    dia "Ну же, в чем твой секрет? Ты такой стройный и подтянутый!"
    show diane f_thinking
    show player 11
    dia "Я стараюсь оставаться активной как можно чаще, но я не могу избавиться от всего этого жира."
    show diane f_normal
    show player 10
    player_name "Жир?! Какой жир?"
    show diane f_surprised
    show player 29 with dissolve
    player_name "Ты отлично выглядишь, {b}Диана{/b}."
    show diane a_dressed_blush f_laugh_blush with dissolve
    show player 13 with dissolve
    dia "Оу. Ты говоришь это сейчас. Но если бы ты увидел меня без одежды, ты бы запел по-другому!"
    show diane f_surprised
    show player 11
    player_name "..."
    show diane a_dressed_shovel f_laugh_blush with dissolve
    dia "Эээ... В любом случае!"
    show diane f_teasing
    dia "... Ты расскажешь мне свой секрет или нет?"
    dia "Ты тренируешься?"
    show diane f_smirk
    show player 21
    player_name "Немного."
    show player 35
    player_name "Я иногда хожу в спортзал."
    show player 13
    show diane f_normal_talk
    dia "Правда?!"
    dia "Это здорово!"
    show diane a_dressed_finger f_explain with dissolve
    dia "Знаешь, есть много хороших преимуществ, чтобы оставаться в форме."
    show diane a_dressed_shovel f_teasing with dissolve
    show player 11
    dia "Женщины любят стройных, сильных и энергичных парней."
    show diane f_smirk
    player_name "..."
    show diane f_smirk_talk
    dia "Давай посмотрим на упаковку из шести банок!"
    show diane f_smirk
    show player 22
    player_name "!!!" with hpunch
    show player 21
    player_name "Ты хочешь увидеть мои..."
    show player 11
    show diane f_smirk_talk
    dia "Твой пресс! Да."
    dia "Покажи этой старушке шоу!"
    show diane f_smirk
    show player 10
    player_name "Хорошо..."
    show diane f_surprised
    show player 249 with dissolve
    show diane a_dressed_blush f_laugh_blush with dissolve
    dia "Ваууууу!"
    show diane a_dressed_shovel f_smirk_talk with dissolve
    dia "Посмотри на это сексуальное тело!"
    show diane f_teasing
    dia "Как ты можешь не нравиться девочкам в школе?"
    show diane f_smirk
    show player 250
    player_name "Ну, я не знаю..."
    show diane f_surprised
    show player 108f with dissolve
    player_name "В школе есть парни намного крупнее меня."
    player_name "Я определенно не из крутых парней..."
    show player 109f
    show diane f_teasing
    dia "Оу, ну и ладно, {b}[firstname]{/b}."
    show diane f_thinking
    show player 13
    dia "Девочки выйдут из этой фазы раньше, чем ты думаешь..."
    show diane f_laugh_blush
    dia "... Дай им немного времени!"
    show diane f_eyes_closed
    show player 17
    player_name "Спасибо, {b}Диана{/b}."
    show diane f_smirk_talk
    show player 203
    dia "Нет проблем, жеребец!"
    show diane f_smirk
    show xtra 21 at left with dissolve
    player_name "..."
    show diane f_normal
    dia "..."
    show diane f_thinking a_dressed_blush with dissolve
    dia "Мальчик, конечно, жарковато здесь, не правда ли?"
    show diane f_normal
    show player 14
    hide xtra with dissolve
    player_name "Хех, да. Я потею, как сумасшедший!"
    show player 13
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Ну, я думаю, я могу придумать какое-то решение..."
    show diane hose with dissolve
    show player 10
    player_name "О?"
    show player 12
    player_name "Что ты-"
    show diane a_dressed_hose f_cheese with dissolve
    show player 11
    player_name "..."
    show player 10
    player_name "Ты не собираешься-"
    show diane a_dressed_hose_shoot
    show player 668
    player_name "!!!" with hpunch
    pause
    player_name "Ого! Как холодно!"
    show player 669f with dissolve
    show diane f_laugh
    dia "О, нет, не надо! Ты так легко не отделаешься!"
    hide player with dissolve
    show diane hose_chase with dissolve
    dia "Хахаха!"
    hide diane with dissolve
    scene expression "backgrounds/location_diane_garden_cutscene06.jpg"
    show expression FilteredText("Мы с {/b}Дианой{/b} боролись с этим шлангом, поливая друг друга и хихикая, как школьники.") as cutscene at Position (xpos= 512, ypos = 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("Мы не сделали много дел в саду в тот день, но у нас было много веселья!") as cutscene at Position (xpos= 512, ypos = 700) with dissolve
    pause
    scene black
    hide cutscene
    with fade
    scene location_diane_garden_night_blur
    show player 677 at left
    show diane b_dressed_wet f_laugh a_dressed_blush at lright
    with dissolve
    dia "Ладно, ладно! Я подчиняюсь!"
    show diane f_normal_talk
    dia "Я не могу за тобой угнаться..."
    show diane f_cheese a_dressed_shovel with dissolve
    show player 678
    player_name "Я выиграл?!"
    show player 677
    show diane f_normal_talk
    dia "Да, да... Ты победил!"
    show diane f_normal
    show player 679 with dissolve
    player_name "Хахаха! Победа!"
    show diane f_laugh
    dia "Хехехе!"
    show player 677 with dissolve
    show diane f_lookup
    pause
    dia "Блин, уже темнеет?"
    show diane f_normal_talk
    dia "Ты должен идти домой, {b}[firstname]{/b}."
    dia "У меня сегодня есть другая работа."
    show diane f_normal
    show player 678
    player_name "Я могу чем-нибудь помочь?"
    show player 677
    show diane f_surprised
    dia "Хмм?"
    show diane f_smirk_talk
    dia "Нет, не думаю. Я ценю твое предложение, но эту работу мне лучше делать одной..."
    show diane f_smirk
    show player 678
    player_name "Хорошо..."
    show player 677
    show diane f_normal_talk
    dia "Еще раз спасибо за помощь, жеребец!"
    dia "Передай {b}[deb_name]{/b}, \"Привет.\""
    show diane f_normal
    show player 678
    player_name "Хорошо."
    player_name "Увидемся, {b}Диана{/b}."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_need_shovel_remove_waste_fail:
    scene location_diane_garden_day_blur
    show player 253 at left with dissolve
    pause
    show player 256 at Position(xpos=0.0322,ypos=1.0000)
    show diane f_normal
    with dissolve
    player_name "[str_warn]Уххххх!!..."
    player_name "[str_warn]...Гххх..."
    show player 27 with dissolve
    player_name "[str_warn]I... Я не могу..."
    player_name "[str_warn]Прости..."
    show player 3
    show diane f_normal_talk
    dia "Ой..."
    dia "Все... хорошо. Я действительно упаковала его слишком полно..."
    dia "Я просто возьму немного, и мы сможем делать это постепенно."
    show player 23
    player_name "Нет, подожди... Я смогу это сделать!"
    show player 256 with dissolve
    dia "..."
    show player 10 with dissolve
    player_name "Я просто устал сегодня, вот и все..."
    player_name "Дай мне отдохнуть и набраться {b}сил{/b}. Я вернусь и сделаю это в другой раз, обещаю."
    show diane f_normal
    show player 3
    dia "..."
    show diane f_laugh
    show player 5
    dia "Да? Ну, как скажешь..."
    show diane f_normal_talk
    dia "Я скоро увижу тебя вновь?"
    show player 2
    show diane f_normal
    player_name "Да, я скоро вернусь."
    player_name "Спасибо, {b}Диана{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_task_week:
    scene garden
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides at lright
    with dissolve
    dia "Привет, жеребец!"
    dia "Вы готовы сделать еще одну доставку?"
    show diane f_normal
    show player 17
    player_name "О, так это большая работа, о которой ты говорила!"
    show player 13
    show diane f_normal_talk
    dia "Ну, конечно."
    dia "Как ты думаешь, что это?"
    show diane f_normal
    show player 29 with dissolve
    player_name "Я..."
    player_name "Я не знаю."
    show player 3
    show diane f_smirk
    dia "Ммммм."
    show diane f_smirk_talk
    dia "Непослушный мальчик..."
    dia "Это мой самый большой клиент, {b}[firstname]{/b}."
    dia "Сделаешь хорошую работу и поможешь мне с прокачкой, когда вернешься, договорились?"
    show diane f_smirk
    show player 17 with dissolve
    player_name "Договорились!"
    show player 13
    show diane f_laugh
    dia "Хехе."
    show diane f_smirk
    show player 14
    player_name "Так куда посылка на этот раз?"
    show player 13
    show diane f_normal_talk
    dia "Просто доставь ее в школьный кафетерий."
    show diane f_normal
    show player 22
    player_name "!!!"
    show player 10
    player_name "В мою школу?"
    show player 11
    show diane f_normal_talk
    dia "Точно!"
    show diane f_normal
    show player 10
    player_name "Ты имеешь в виду, что ученики в школе будут пить-"
    show player 11
    show diane f_normal_talk
    dia "Тебе лучше поторопиться, красавчик."
    dia "Я сказал вашему директору ождать доставки вскоре."
    show diane f_normal
    player_name "..."
    show player 10
    player_name "Хорошо."
    show player 5
    show diane f_normal_talk
    dia "{b}Пакет в сарае.{/b}"
    show diane f_normal
    show player 10
    player_name "Ясно."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_done:
    scene garden
    show player 640e at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Привет, {b}Диана{/b}."
    player_name "Я доставил этот пакет в школу для тебя."
    show player 13
    show diane a_shirtless_money f_shamed_talk_smile
    with dissolve
    dia "Да, я только что говорила по телефону с парнем из кафетерия."
    show diane a_shirtless_sides with dissolve
    dia "Он уже сделал другой заказ."
    dia "Даже больше, чем в прошлый раз."
    show diane f_shamed
    show player 14
    player_name "Это ведь хорошо, правда?"
    show player 13
    show diane f_shamed_talk_smile
    dia "{b}*вздох*{/b} Да, я просто беспокоюсь о том, как удовлетворить спрос."
    dia "Мне нужно найти место для работы получше!"
    dia "Иначе я могу потерять клиентов..."
    show diane f_shamed
    show player 10
    player_name "Я могу чем-нибудь помочь?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Мда, боюсь, что нет."
    dia "Мне остается только надеяться, что освободится где-нибудь сарай."
    show diane f_shamed
    show player 10
    player_name "Жаль, что у вас здесь нет земли. Можно просто построить новый амбар."
    show player 5
    show diane f_normal_talk
    dia "Да, это было бы здорово, не так ли?"
    dia "Я могла бы спроектировать его так, чтобы он идеально подходил моему бизнесу!"
    show diane f_thinking
    dia "... Знаешь что?!"
    dia "Возможно, ты действительно на что-то наткнулся {b}[firstname]{/b}..."
    show player 14
    player_name "Правда?"
    show player 13
    show diane f_normal_talk
    dia "Да!"
    dia "Почему бы тебе не начать работать в саду и не дать мне подумать об этом некоторое время."
    show diane f_normal
    show player 14
    player_name "Конечно!"
    show player 13
    show diane f_smirk_talk
    dia "Приходи ко мне, когда закончишь."
    dia "Мы сможем немного повеселиться."
    show diane f_smirk
    show player 29 with dissolve
    player_name "Хорошо."
    show player 3
    show diane f_laugh
    dia "Хехехе, спасибо, жеребец!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    hide diane with dissolve
    return

label garden_diane_clean_garden:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 10 with dissolve
    player_name "О, боже..."
    player_name "Как это случилось?"
    show player 184 at right with dissolve
    player_name "..."
    show player 672 with dissolve
    player_name "Фу!"
    player_name "Все испорчено...."
    show diane at flip with dissolve
    player_name "Как это произошло-"
    show diane f_sad_talk
    dia "Привет, {b}[firstname]{/b}..."
    show diane f_sad
    show player 22 at Position (xoffset=-131) with dissolve
    player_name "!!!"
    show player 10f with dissolve
    player_name "{b}Диана{/b}, смотри!"
    show player 671f with dissolve
    show diane f_scared
    dia "..."
    show player 672f
    player_name "Что случилось с садом?"
    player_name "Я что-то напортачил?"
    show player 5f with dissolve
    show diane a_dressed_blush f_shamed_talk_smile with dissolve
    dia "О нет, милый..."
    dia "Это все я."
    show diane a_dressed_shovel with dissolve
    dia "В этом году я использовал натуральный пестицид, и он оказался не таким эффективным, как я надеялся."
    show diane f_shamed
    show player 12f
    player_name "Пестицид?"
    show player 5f
    show diane f_shamed_talk_smile
    dia "Да, видишь этих тварей, ползающих по всему саду?"
    show diane f_shamed
    show player 10f
    player_name "Да..."
    show player 5f
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "Это {b}уховертки{/b}."
    show diane f_shamed a_dressed_shovel with dissolve
    player_name "..."
    show player 12f
    player_name "Почему их называют уховертками?"
    show player 5f
    show diane f_laugh
    dia "Хе-хе, это из бабушкиной сказки... Раньше люди верили, что уховертки могут заползти в ухо и отложить яйца в мозгу."
    show diane f_normal
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "Это не так... Я имею в виду, они на самом деле не-"
    show player 5f
    show diane f_laugh a_dressed_blush with dissolve
    dia "Хахаха! Нет, конечно, нет!"
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Они предпочитают влажную богатую почву, вот почему они оказались в нашем саду."
    dia "Бьюсь об заклад, в этой земле сейчас десятки гнезд..."
    show diane f_normal
    show player 12f
    player_name "... Гадость!!!"
    player_name "Так как мы это исправим?"
    show player 5f
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Ну, для начала, мы должны выбросить все эти зараженные культуры и уничтожить столько гнезд, сколько сможем."
    dia "Потом нужно будет возделывать землю и сажать растения."
    dia "Убедившись, что на этот раз мы используем более эффективный пестицид."
    show diane f_normal a_dressed_shovel with dissolve
    show player 14f
    player_name "Хорошо."
    player_name "Давай начнем!"
    show player 13f
    show diane f_normal_talk
    dia "Хе-хе, такой нетерпеливый..."
    dia "Не могу поверить, что тебе так нравится работать в саду!"
    show diane f_normal
    show player 14f
    player_name "Это очень весело!"
    show player 13f
    show diane f_normal_talk
    dia "Хорошо, копай!"
    hide player
    hide diane
    with dissolve
    jump garden_listing
    return

label dianes_garden_diane_bug_infestation:
    scene garden
    show player 10 at left with dissolve
    player_name "{b}Диана{/b}?"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "Это странно."
    player_name "Она обычно ждет меня здесь, чтобы поприветствовать."
    show player 31 with dissolve
    player_name "!!!"
    show player 32
    player_name "О, нет!"
    player_name "Что случилось с садом?!"
    hide player with dissolve
    return

label dianes_garden_diane_check_up_on_garden:
    scene garden
    show player 14 with dissolve
    player_name "Привет, {b}Диана{/b}!"
    player_name "Как-"
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Вау!!!"
    show player 17 with dissolve
    player_name "Сад выглядит великолепно!"
    show player 14
    player_name "Не могу поверить, что все растет так быстро."
    show player 30
    player_name "Хмм..."
    show player 32f with dissolve
    player_name "{b}Диана{/b} опять пропала..."
    player_name "Интересно, где она прячется?"
    hide player with dissolve
    return

label dianes_garden_diane_pump_request:
    scene garden
    show player 5 at left
    show diane f_normal_talk at lright
    with dissolve
    dia "Hey, there he is!"
    show diane f_normal
    show player 29 with dissolve
    player_name "Привет, {b}Диана{/b}."
    show player 3
    show diane f_laugh
    dia "Я так рада, что ты здесь!"
    show diane f_normal_talk
    dia "{b}[deb_name]{/b} рассказала тебе о моем новом клиенте?"
    show diane f_normal
    show player 29
    player_name "Да, она сказала, что ты поймала большую рыбу."
    show player 3
    show diane f_laugh
    dia "Тебе лучше поверить в это!"
    show diane f_normal_talk
    dia "У меня много работы, прежде чем мы сможем сделать доставку."
    dia "Боюсь, у меня нет времени ухаживать за садом..."
    show diane f_normal
    show player 5 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Думаешь, справишься сам?"
    show diane f_explain
    dia "Я увеличу тебе зарплату..."
    show diane f_cheese
    show player 10
    player_name "Да, конечно."
    show player 5
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "В чем дело, красавчик?"
    dia "Ты все еще думаешь о том дне?"
    show diane f_shamed
    show player 12
    player_name "Да, мне очень жаль насчет всего этого-"
    show player 11
    show diane f_laugh a_dressed_finger with dissolve
    dia "Не глупи, красавчик."
    show diane f_normal_talk
    dia "Ты молодой человек!"
    dia "Ты не можешь всегда контролировать эти вещи!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 29 with dissolve
    player_name "Да, наверно..."
    show player 3
    show diane f_normal_talk
    dia "Не думай об этом больше, {b}[firstname]{/b}!"
    show diane f_normal
    show player 13 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Ладно, мне лучше начать."
    dia "Много работы!"
    dia "Я буду в сарае, все подготовлю, если понадоблюсь, хорошо?"
    show diane f_normal
    show player 23
    player_name "{b}*ох*{/b} Корова сейчас там?"
    show player 14
    player_name "Можно погладить?!"
    show player 13
    show diane f_normal_talk
    dia "Ааа?"
    show diane f_lookup
    dia "О, корова... Ухх, нет."
    show diane f_smirk
    dia "..."
    show diane f_smirk_talk
    dia "Я пойду и навещу корову сегодня вечером."
    show diane f_smirk
    show player 12
    player_name "Так что ты сейчас делаешь в сарае?"
    show player 5
    show diane f_surprised_down a_dressed_blush with dissolve
    dia "Я эээ..."
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "... Убираюсь!"
    dia "Да, мне нужно стерилизовать все оборудование и убедиться, что упаковка готова."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 17
    player_name "Ясно."
    show player 14
    player_name "Тебе нужна помощь?"
    show player 13
    show diane f_laugh
    dia "Нет, спасибо, красавчик."
    dia "Ты пока сосредоточься на садоводстве, а я-"
    show diane f_explain a_dressed_finger with dissolve
    dia "!!!"
    show diane f_normal_talk
    dia "Вообще-то, ты можешь кое-что для меня сделать!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Конечно, что угодно."
    show player 13
    show diane f_smirk_talk
    dia "{b}Я оставила один из инструментов на кухонном столе.{/b}"
    dia "Сбегай и принеси его мне?"
    show diane f_smirk
    show player 14
    player_name "Хорошо."
    player_name "Я быстро."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_2_task:
    scene garden
    show diane b_shirtless a_shirtless_tired f_tired_down at lright
    show player 14 at left
    with dissolve
    player_name "Привет, {b}Диана{/b}."
    player_name "Как у тебя-"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Ты в порядке?"
    player_name "Ты выглядишь измученной!"
    show player 5
    show diane f_tired_talk
    dia "О, да. Я в порядке."
    dia "Просто последние несколько дней я почти не спала..."
    dia "Эта последняя доставка убивает меня!"
    show diane f_tired
    show player 10
    player_name "Это не хорошо."
    player_name "Ты уверена, что я не могу помочь тебе подоить корову?"
    show player 12
    player_name "Я бы не возражал."
    show player 5
    show diane f_tired_talk
    dia "Держу пари, что нет!"
    show diane f_laugh
    dia "Хахахаха!"
    show diane f_tired
    show player 11
    player_name "..."
    show diane f_tired_talk
    dia "Прости, я сейчас немного не в себе."
    show player 5
    dia "В этом нет необходимости, жеребец."
    dia "Я закончила заказ вчера вечером."
    show diane f_tired
    show player 12
    player_name "Ааа."
    show player 14
    player_name "Что ж, это хорошо!"
    show player 13
    show diane f_tired_talk
    dia "Не могли бы ты доставить его для меня еще раз?"
    show diane f_tired
    show player 14
    player_name "Я не против!"
    player_name "Я с удовольствием доставлю заказ."
    show player 13
    show diane f_tired_talk
    dia "О, ты мой спаситель, красавчик!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "Вам не придется далеко идти; это для детского сада по соседству."
    show diane f_tired
    show player 10
    player_name "По соседству?"
    player_name "Я думал {b}Энни{/b} живет по соседству..."
    show player 5
    show diane f_tired_down
    dia "Хмм?"
    show player 12
    player_name "Она из моего класса."
    show player 5
    show diane f_tired_talk
    dia "О, это, должно быть, {b}дочь Люси{/b}."
    show diane f_tired
    show player 12
    player_name "{b}Люси{/b}? не знаю, возможно..."
    show player 5
    show diane f_tired_talk
    dia "Ну, если она хоть немного похожа на свою мать, я уверена, что она восхитительна!"
    show diane f_tired
    show player 12
    player_name "... Угу. Я не знаю об этом."
    show player 5
    show diane f_tired_talk
    dia "Передай им от меня привет, ладно?"
    dia "Мне нужно поспать."
    dia "... Просто принеси мне деньги, когда закончишь, хорошо?"
    show diane f_tired
    show player 14
    player_name "Хорошо, {b}Диана.{/b}"
    show player 13
    show diane f_tired_talk
    dia "Спасибо, жеребец."
    show diane f_tired at Position (xpos=450) with dissolve
    show player 10
    player_name "Подожди!!"
    show player 5
    dia "Хмм?"
    show player 12
    player_name "Где доставка?"
    show player 5
    show diane f_tired_down
    dia "..."
    show diane f_laugh
    dia "Ой! Хахахахахахаха!!"
    dia "Да, тебе это, наверное, понадобится, да?"
    show diane f_tired_talk
    dia "Он в сарае."
    dia "Я оставила его открытым для тебя, красавчик."
    show diane f_tired
    show player 17
    player_name "Хорошо."
    show player 13
    show diane f_tired_talk
    dia "Еще раз спасибо, красавчик."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_d9_intro:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_tired f_tired
    with dissolve
    player_name "Привет, {b}Диана{/b}."
    player_name "Чувствуешь себя лучше сегодня?"
    show player 5
    show diane f_tired_talk
    dia "Привет, красавчик."
    dia "Я прекрасно себя чувствую. Спасибо, что спросил."
    show diane f_tired
    show player 10
    player_name "... Ты уверена? Ты все еще выглядишь очень усталой."
    show player 5
    show diane f_tired_talk
    dia "Хе, разве?"
    show diane f_tired
    show player 10
    player_name "Сколько ты вчера спала?"
    show player 5
    show diane f_tired_talk
    dia "Я не уверена."
    dia "Я видела записку, которую ты оставил мне о следующем заказе Люси, и я пыталась начать производство."
    dia "Это утомительно, но мне просто нужно привыкнуть к этому, я думаю..."
    show diane f_tired
    show player 10
    player_name "Что ты имеешь в виду?"
    show player 5
    show diane f_tired_talk
    dia "Ну, мои заказы не замедлятся в ближайшее время."
    dia "На самом деле, они становятся больше."
    show diane f_tired
    show player 10
    player_name "Да, но-"
    show player 5
    show diane f_tired_talk
    dia "У меня даже есть наводка на другого нового клиента."
    dia "Мой самый большой."
    show diane f_tired
    show player 10
    player_name "{b}Диана{/b}..."
    player_name "Сначала ты должна позаботиться о себе..."
    player_name "Ты уверена, что не берешь на себя слишком много, слишком быстро?"
    player_name "Я беспокоюсь за тебя."
    show player 5
    show diane f_tired_talk
    dia "Ааа."
    dia "Я ценю твою заботу, {b}[firstname]{/b}, но тебе не нужно беспокоиться обо мне."
    dia "Этот бизнес был моей мечтой долгое время."
    dia "Потребуется гораздо больше, чем несколько бессонных ночей, чтобы остановить меня."
    show diane f_tired
    show player 10
    player_name "... Хорошо, только..."
    show player 14
    player_name "... Помни, я здесь, чтобы помочь тебе, если понадобится."
    show player 13
    show diane f_tired_talk
    dia "Спасибо, {b}[firstname]{/b}."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "Ну, я должна вернуться."
    dia "Позаботься о моем саде, хорошо?"
    show diane f_tired
    show player 14
    player_name "Конечно."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_shed_light_on:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "( Хмм? )"
    player_name "( {b}Дверь открыта и свет горит!{/b} )"
    player_name "( Она не может еще работать, или может? )"
    hide player with dissolve
    return

label dianes_garden_diane_missing:
    scene garden
    show player 127 with dissolve
    player_name "Где {b}Диана{/b}?"
    show player 12
    player_name "Обычно в это время она на улице..."
    show player 56
    player_name "Она должна быть где-то здесь."
    hide player 56 with dissolve
    return

label dianes_garden_diane_daylight_drinking:
    return

label dianes_garden_diane_ready_for_day_off:
    scene garden
    show player 14 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Привет {b}Диана{/b}!"
    player_name "Готова к выходному?"
    show player 13
    show diane f_normal_talk
    dia "Привет, {b}[firstname]{/b}."
    dia "HХехе, полагаю что да..."
    dia "Мне просто нужно закончить последнюю партию, над которой я работала этим утром и-"
    show diane f_normal
    show player 33
    player_name "Нет, нет, нет..."
    show player 14
    player_name "Ты закончила работать сегодня!"
    show player 13
    show diane f_normal_talk
    dia "... Но я должна убедиться, что все хранится правильно."
    show diane f_normal
    show player 14
    player_name "Просто скажи мне, что делать, и я все улажу."
    show player 17
    player_name "Остальная часть вашего дня - это отдых!"
    show player 13
    show diane f_laugh a_shirtless_shock with dissolve
    dia "Хахаха. Хорошо, хорошо..."
    show diane f_normal_talk a_shirtless_sides with dissolve
    dia "{b}Просто зайдите в сарай и слей то, что в насосе, в кувшин.{/b}"
    show diane f_normal
    show player 14
    player_name "Звучит достаточно просто."
    show player 13
    show diane f_normal_talk
    dia "... Но ты должны убедиться, что закрыл крышку крепко!"
    show diane f_normal
    show player 14
    player_name "Ты просто присядь, а я займусь делами, хорошо?"
    $ M_diane.is_naked = 0
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_return_drink:
    return

label dianes_garden_diane_drunken_shenanigans_apology:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show diane at flip
    show diane at Position (xpos=250)
    show vero f_normal_talk b_casual a_casual_front at Position (xpos=600)
    with dissolve
    vero "Я просто не могу поверить в то, как хорошо выглядит твой сад сейчас!"
    vero "Я помню, когда это было просто грустное маленькое пятно помидоров..."
    show vero f_normal
    show diane f_laugh
    dia "Хаха, спасибо {b}Ви{/b}!"
    show diane f_normal_talk
    dia "Конечно, он прошел долгий путь..."
    show diane f_normal
    show vero f_normal_talk
    vero "Это действительно великолепно, {b}Диана{/b}!"
    vero "Вау!!!"
    show vero bending at flip
    show vero at Position (xoffset=100)
    show diane f_down_front
    with dissolve
    pause
    hide vero
    show vero f_normal_talk b_casual a_cucumber1 at Position (xpos=600)
    show diane f_normal
    with dissolve
    vero "Посмотрите на размер этого!"
    show vero f_normal
    show diane f_normal_talk
    dia "Да, я знаю!"
    show diane f_smirk_talk
    dia "Просто монстр."
    show diane f_smirk
    show vero f_normal_talk a_cucumber2 with dissolve
    vero "Я бы сказала..."
    show vero f_normal
    show diane f_normal_talk
    dia "Хочешь забрать его домой?"
    show diane f_wink
    show vero f_rolleyes a_cucumber1 with dissolve
    vero "Боже мой, мне не следовало говорить тебе об этом..."
    show vero f_sexy
    show diane f_laugh a_dressed_finger with dissolve
    dia "Эй, я не осуждаю."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_down
    vero "..."
    show vero f_sexy_talk_down
    vero "Нет, он слишком большой для меня!"
    show vero f_sexy_down
    show diane f_laugh
    dia "Хаха, да. Для меня тоже."
    show diane f_smirk
    show vero f_surprised_down
    vero "Ахаха, я знала, что ты попробуешь!"
    show vero f_sexy a_casual_front with dissolve
    show diane f_smirk_talk
    dia "Да, да..."
    show diane f_smirk
    show vero f_sexy_talk
    vero "Так в чем твой секрет?"
    vero "Ты же не используешь гормоны на них или что-то в этом роде?"
    show vero f_sexy
    show diane f_normal_talk
    dia "Пфф, конечно нет!"
    dia "Я помню наш разговор об этом."
    show diane f_normal
    show vero f_sexy_talk
    vero "Хорошо."
    show vero f_sexy
    show diane f_normal_talk
    dia "Честно говоря, в этом году я оставила большую часть садоводства своему другу."
    show diane f_normal
    show vero f_normal_talk
    vero "Ты имеешь в виду того милашку, которого ты привела в магазин на днях?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Даже не думай, {b}Ви{/b}!"
    dia "Он хороший парень."
    show diane f_normal
    show vero f_normal_talk
    vero "Да, и что?"
    show vero f_sexy_talk
    vero "Я хорошая девушка..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Хух."
    show diane f_normal
    show vero f_laugh
    vero "Хехехе!"
    show vero f_sexy
    show diane f_normal_talk
    dia "Его опекун убьет меня, если я позволю тебе вцепиться в него когтями."
    show diane f_normal
    show vero f_sexy_talk
    vero "Ой, да ладно."
    show vero f_sexy
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Точно нет, {b}Ви{/b}."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_talk
    vero "Шшш, с тобой не весело."
    show vero f_sexy
    pause
    show vero f_thinking
    vero "... Рррггхх..."
    vero "Иногда я действительно жалею о переезде в этот город."
    vero "Мужчины здесь-отстой!"
    show vero f_normal
    show diane f_normal_talk
    dia "Ты не обязана мне говорить."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Ты же не думаешь вернуться на ферму?"
    show diane f_normal
    show vero f_laugh
    vero "О, черт возьми, нет!"
    show vero f_normal_talk
    vero "Если я вернусь туда с поджатым хвостом, то упрекам не будет конца.!"
    vero "{b}*вздох*{/b}"
    vero "Не могу поверить что работаю в {b}Consum-R{/b} уже 5 лет!"
    vero "Это так угнетает..."
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "О, это напомнило мне!"
    vero "Я хотела спросить, как продвигается новый бизнес?"
    show vero f_normal
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "О, эээ..."
    show diane a_dressed_shovel with dissolve
    dia "Пока все идет хорошо."
    show diane f_normal
    show vero f_normal_talk
    vero "Ты все еще не готова рассказать мне подробности?"
    show vero f_normal
    show diane f_normal_talk
    dia "Ммм, пока нет..."
    show diane f_normal
    show vero f_rolleyes
    vero "Ух, лааадно."
    show vero f_normal_talk
    vero "Только не забывай обо мне, когда начнешь зарабатывать большие деньги!"
    vero "Я быстро учусь и буду усердно работать на тебя, {b}Диана{/b}."
    show vero f_normal
    show diane f_normal_talk
    dia "Хе, я знаю, {b}Ви{/b}..."
    dia "Просто сейчас у меня недостаточно работы, чтобы нанять еще одного работника."
    dia "Обещаю, я позвоню тебе, как только."
    show diane f_normal
    show player 13 at left with dissolve
    show vero f_normal_talk
    vero "Так-то лучше."
    show vero f_normal
    show player 14
    player_name "Здравствуйте дамы."
    show player 13
    show vero f_sexy_talk
    vero "Ух ох, Твой парень здесь..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Ччч, заткнись {b}Ви{/b}!"
    show diane at unflip
    show diane at lcenter
    with dissolve
    dia "Не слушай ее, {b}[firstname]{/b}."
    show diane f_normal
    show vero f_sexy_talk
    vero "Он знает, что я просто шучу..."
    show vero f_normal_talk
    vero "Мы как раз говорили об этом прекрасном саде, над которым ты работал."
    show vero f_normal
    show player 17
    player_name "Выглядит неплохо, да?"
    show player 18
    show vero f_normal_talk
    vero "Выглядит лучше, чем хорошо."
    vero "В чем твой секрет?"
    show vero f_normal
    show player 10
    player_name "Ааа?"
    show player 5
    show vero f_normal_talk
    vero "Ты наверно делаешь что-то особенное, чтобы получить такие результаты."
    show vero f_normal
    show player 35
    player_name "Хмм, да нет."
    show player 14
    player_name "Я просто пашу, сею и поливаю."
    player_name "Как меня учила {b}Диана{/b}."
    show player 13
    show vero f_normal_talk
    vero "И все?"
    show vero f_normal
    show player 14
    player_name "Ага."
    show player 13
    pause
    show player 35
    player_name "О!"
    show player 14
    player_name "Я удобрял его компостом..."
    show player 10
    player_name "... Может, это мой секрет?"
    show player 13
    show diane f_laugh
    dia "Хахаха!"
    show vero f_laugh
    vero "Хехе, может быть..."
    show diane f_normal
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "Ну, мне, наверное, пора идти..."
    show vero f_normal
    hide diane
    show diane f_normal_talk at flip
    show diane at Position (xpos=250)
    with dissolve
    dia "Так рано?"
    show diane f_normal
    show vero f_normal_talk
    vero "Хех, Да. Продукты в {b}Consum-R{/b} сами себя не продадут."
    show vero f_normal
    show diane f_normal_talk
    dia "Ха, полагаю что нет."
    hide vero
    show diane hug_vero_talk at Position (xoffset=200)
    with dissolve
    dia "Заходи в любое время, хорошо?"
    show diane f_normal
    show vero f_normal_talk b_casual a_casual_front at Position (xpos=600)
    vero "Хорошо."
    show vero f_normal
    show player 14
    player_name "Пока {b}Вероника{/b}."
    player_name "Был рад снова тебя видеть."
    show player 13
    show vero f_normal_talk
    vero "Да, ты слишком красив."
    show vero f_sexy
    pause
    show vero f_sexy_talk
    vero "Знаешь что?"
    vero "Пожалуй, я все-таки возьму огурец..."
    show vero bending at Position (xoffset=370)
    show diane f_down_front
    with dissolve
    pause
    show player 426
    vero "Хм, куда же я его дела..."
    show diane f_lookup
    dia "О, боже мой!"
    show diane f_laugh
    dia "Хаха, ты бы уже ушла отсюда!"
    show diane f_normal
    show vero f_sexy_talk b_casual a_cucumber1 at Position (xpos=600) with dissolve
    show player 13
    vero "Хехе, спасибо опять, {b}Диана{/b}!"
    hide vero with dissolve
    player_name "..."
    hide diane
    show diane f_normal_talk
    with dissolve
    dia "Ты готов приступить к работе, {b}жеребец{/b}?"
    show diane f_normal
    show player 10
    player_name "Хмм?"
    show player 14
    player_name "О!"
    player_name "Ага, я готов."
    show player 13
    show diane f_normal_talk
    dia "Приятно слышать это."
    show diane f_shamed_talk_smile
    dia "... Но прежде чем ты начнешь..."
    show diane f_shamed
    show player 14
    player_name "Да?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "Думаю, мне следует извиниться."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 10
    player_name "Извиниться?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Знаешь, на днях..."
    dia "... эээ-"
    dia "{b}*хмм*{/b} Я просто слишком много выпила, и вела себя... эээ, неуместно."
    show diane f_shamed
    player_name "..."
    show diane f_shamed_talk_smile
    dia "Просто прошло много времени с тех пор, как кто-то проявлял ко мне столько внимания, и в последнее время мне было одиноко-"
    dia "Ухх, нет. Черт возьми, это не оправдание... Я-"
    show diane f_sad_talk
    dia "Слушай, я воспользовалась тобой, {b}[firstname]{/b} и мне очень жаль... Я-"
    show diane f_sad
    show player 14
    player_name "Ты не воспользовался мной!"
    show player 13
    show diane f_sad_talk
    dia "Ааа?"
    show diane f_sad
    show player 17
    player_name "Это было потрясающе!"
    player_name "Я надеялся, что мы как-нибудь повторим?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "Ты хочешь повторить?!"
    show diane f_shamed
    show player 26
    player_name "Конечно. Ты красивая женщина, {b}Диана{/b}!"
    show player 13
    show diane f_shamed_talk_smile a_dressed_shovel with dissolve
    dia "Хорошо, но-"
    dia "{b}[deb_name]{/b} доверила мне присматривать за тобой, и это было неправильно с моей стороны-"
    show diane f_shamed
    show player 14
    player_name "Я не ребенок, {b}Диана{/b}. И кроме того, это было весело!"
    show player 13
    show diane f_shamed_talk_smile
    dia "... И {b}[deb_name]{/b} убьет меня, если узнает."
    show diane f_shamed
    show player 14
    player_name "Она не должна узнать."
    show player 13
    dia "..."
    show player 14
    player_name "Я имею в виду, мы просто немного повеселились."
    player_name "Я не вижу в этом ничего плохого."
    show player 13
    show diane f_shamed_talk_smile
    dia "Хмм."
    dia "Разве ты не предпочел бы заниматься этим с девочками своего возраста?"
    show diane f_shamed
    show player 14
    player_name "Ты шутишь?!"
    player_name "Ты в миллион раз сексуальнее, чем девочки в моей школе, {b}Диана{/b}!"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Ой, нет!"
    show player 17
    player_name "Хе, это правда."
    show player 18
    show diane f_smirk a_dressed_shovel with dissolve
    pause
    show diane f_lookup
    dia "Хорошо, Мистер Очарование..."
    show diane f_smirk_talk
    dia "Мы явно не в том настроении, чтобы вести этот разговор."
    dia "Так что давай сосредоточимся на работе, хорошо?"
    show diane f_smirk
    show player 12
    player_name "Серьезно?"
    show player 5
    show diane f_smirk_talk
    dia "Да, серьезно!"
    show diane f_normal_talk
    dia "Я буду в сарае, если тебе что-нибудь понадобится."
    show diane f_normal
    show player 26
    player_name "Ты уверена, что я не могу тебе помочь?"
    show player 13
    show diane f_laugh
    dia "Ха-ха, нет. Мне не нужна помощь..."
    show diane f_smirk_talk
    dia "Хорошая попытка."
    show diane f_smirk
    show player 14
    player_name "Что?!"
    show player 13
    show diane f_smirk_talk
    dia "Просто начни работу в саду."
    show diane f_smirk
    show player 14
    player_name "Хорошо."
    show player 13
    hide diane with dissolve
    pause
    show player 5
    player_name "( Надеюсь, я ее не расстроил... )"
    player_name "{b}( Наверное, мне стоит оставить ее в покое и сосредоточиться на работе в саду. ){/b}"
    hide player with dissolve
    return

label dianes_garden_diane_do_not_disturb:
    scene townmap
    player_name "Я должен посетить {b}Диану{/b} в другой раз..."
    return

label dianes_garden_diane_shed_still_open:
    show player 12 with dissolve
    player_name "Это странно..."
    show player 30
    player_name "Сарай {b}Дианы{/b} {b}еще открыт{/b}..."
    hide player 30 with dissolve
    return

label drink_offered:
    scene garden
    if M_diane.get("aunt_drink_made"):
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "Я должен дать {b}Диане{/b} ее {b}напиток{/b} перед тем как вернуться к работе..."
    $ game.main()

label aunt_masturbate_not_seen:
    show diane_masturbate 1_2
    player_name "!!!"
    player_name "( ... Что она... )"
    window hide
    pause 2
    player_name "( ВАУ... )"
    player_name "( Она играет со своими овощами... )"
    player_name "( Целый огурец! )"
    player_name "( ... )"
    player_name "( ...Я должна уйти, пока меня не поймали. )"
    scene garden
    with dissolve
    show player 113 with dissolve
    player_name "Не могу поверить, что застукал ее за мастурбацией!"
    show player 114
    player_name "... или что она достаточно возбуждена, чтобы сделать это с овощами!"
    show player 113
    player_name "Вот почему она говорила только {b}длинные{/b} и {b}твердые{/b}?"
    show player 109f
    player_name "Хмм..."
    show player 108f
    player_name "Думаю, она была одинока в последнее время..."
    player_name "Я должен вернуться к работе и притвориться, что ничего не видел..."
    hide player 108f with dissolve
    $ renpy.end_replay()
    return

label find_shovel:
    scene expression game.timer.image("garden{}")
    show player 12 with dissolve
    if player.has_item("shovel"):
        player_name "Я должен сказать {b}Диане{/b}, что готов приступить к работе."
    else:
        player_name "Мне нужно найти {b}лопату{/b}, прежде чем я смогу помочь с садом..."
    hide player with dissolve
    $ game.main()


label before_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Хмммм..."
    show player 12
    player_name "Сначала я должен узнать, дома ли {b}Диана{/b}."
    $ game.main()

label after_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Хмммм..."
    show player 12
    player_name "Может, не сейчас."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
