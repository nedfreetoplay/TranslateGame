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
    show diane at lright
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
    dia "You should get on home, {b}[firstname]{/b}."
    dia "I have some other work to do tonight."
    show diane f_normal
    show player 678
    player_name "Anything I can help with?"
    show player 677
    show diane f_surprised
    dia "Hmm?"
    show diane f_smirk_talk
    dia "Nah, I think not. I appreciate the offer, but this is work I'm better off doing alone..."
    show diane f_smirk
    show player 678
    player_name "O-okay..."
    show player 677
    show diane f_normal_talk
    dia "Thanks again for all your help today, stud!"
    dia "Tell {b}[deb_name]{/b} I said, \"Hi.\""
    show diane f_normal
    show player 678
    player_name "Alright."
    player_name "See ya soon, {b}Diane{/b}."
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
    player_name "[str_warn]Ughhh!!..."
    player_name "[str_warn]...Ghhh..."
    show player 27 with dissolve
    player_name "[str_warn]I... I can't do it..."
    player_name "[str_warn]I'm sorry..."
    show player 3
    show diane f_normal_talk
    dia "Oh..."
    dia "It's... okay. I really did pack it way too full..."
    dia "I'll just take some out and we can do it little by little."
    show player 23
    player_name "No, wait... I can do it!"
    show player 256 with dissolve
    dia "..."
    show player 10 with dissolve
    player_name "I'm just tired today, that's all..."
    player_name "Let me rest and get some {b}strength{/b}. I'll come back and do it another day, I promise."
    show diane f_normal
    show player 3
    dia "..."
    show diane f_laugh
    show player 5
    dia "Oh? Well, if you say so..."
    show diane f_normal_talk
    dia "I'll see you again soon?"
    show player 2
    show diane f_normal
    player_name "Yeah, I'll be back real soon."
    player_name "Thanks, {b}Diane{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_3_task_week:
    scene garden
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides at lright
    with dissolve
    dia "Hey there, stud!"
    dia "You ready to make another delivery?"
    show diane f_normal
    show player 17
    player_name "Oh, so that's the big job you were talking about!"
    show player 13
    show diane f_normal_talk
    dia "Well, of course."
    dia "What did you think it was?"
    show diane f_normal
    show player 29 with dissolve
    player_name "I..."
    player_name "I dunno."
    show player 3
    show diane f_smirk
    dia "Mmhmm."
    show diane f_smirk_talk
    dia "Naughty boy..."
    dia "This is my biggest customer yet, {b}[firstname]{/b}."
    dia "Do a good job and you can help me with my pumping when you get back, deal?"
    show diane f_smirk
    show player 17 with dissolve
    player_name "deal!"
    show player 13
    show diane f_laugh
    dia "Hehe."
    show diane f_smirk
    show player 14
    player_name "So where is the package going this time?"
    show player 13
    show diane f_normal_talk
    dia "Just deliver it to the cafeteria at your school."
    show diane f_normal
    show player 22
    player_name "!!!"
    show player 10
    player_name "My school?"
    show player 11
    show diane f_normal_talk
    dia "That's right!"
    show diane f_normal
    show player 10
    player_name "You mean the students at school will be drinking-"
    show player 11
    show diane f_normal_talk
    dia "You'd better hurry, handsome."
    dia "I told your principal to expect delivery ASAP."
    show diane f_normal
    player_name "..."
    show player 10
    player_name "Okay."
    show player 5
    show diane f_normal_talk
    dia "{b}The package is in the shed.{/b}"
    show diane f_normal
    show player 10
    player_name "Got it."
    return

label dianes_garden_diane_delivery_3_task_weekend:
    scene expression player.location.background_blur
    show diane f_normal_talk
    dia "The {b}Package{/b} has to be dropped off at the {b}School{/b}, so come back during the school week."
    show player 1 at left
    player_name "Okay."
    return

label dianes_garden_diane_delivery_3_done:
    scene garden
    show player 640e at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "I delivered that package to my school for you."
    show player 13
    show diane a_shirtless_money f_shamed_talk_smile
    with dissolve
    dia "Yeah, I just got off the phone with the cafeteria guy."
    show diane a_shirtless_sides with dissolve
    dia "He's already placed another order."
    dia "Even bigger than the last."
    show diane f_shamed
    show player 14
    player_name "That's a good thing, right?"
    show player 13
    show diane f_shamed_talk_smile
    dia "{b}*Sigh*{/b} Yeah, I'm just worried about meeting the demand is all."
    dia "I need to find a better work place soon!"
    dia "Otherwise, I might lose customers..."
    show diane f_shamed
    show player 10
    player_name "Anything I can do to help?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Hmm, I'm afraid not."
    dia "I just have to hope a vacant barn becomes available."
    show diane f_shamed
    show player 10
    player_name "It's a shame you don't have more land here. You could just build a new barn."
    show player 5
    show diane f_normal_talk
    dia "Yeah, that would be nice wouldn't it?"
    dia "I could design it to fit my business perfectly!"
    show diane f_thinking
    dia "... You know what?!"
    dia "You might actually be on to something {b}[firstname]{/b}..."
    show player 14
    player_name "Really?"
    show player 13
    show diane f_normal_talk
    dia "Yeah!"
    dia "Why don't you get started on the gardening and let me think on this for awhile."
    show diane f_normal
    show player 14
    player_name "Sure thing!"
    show player 13
    show diane f_smirk_talk
    dia "Come and see me when you're done."
    dia "We can have some fun."
    show diane f_smirk
    show player 29 with dissolve
    player_name "O-okay."
    show player 3
    show diane f_laugh
    dia "Hehehe, thanks stud!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    hide diane with dissolve
    return

label garden_diane_clean_garden:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 10 with dissolve
    player_name "Oh, man..."
    player_name "How did this happen?"
    show player 184 at right with dissolve
    player_name "..."
    show player 672 with dissolve
    player_name "Yuck!"
    player_name "Everything is ruined..."
    show diane at flip with dissolve
    player_name "How did this happen-"
    show diane f_sad_talk
    dia "Hi, {b}[firstname]{/b}..."
    show diane f_sad
    show player 22 at Position (xoffset=-131) with dissolve
    player_name "!!!"
    show player 10f with dissolve
    player_name "{b}Diane{/b}, look!"
    show player 671f with dissolve
    show diane f_scared
    dia "..."
    show player 672f
    player_name "What happened to the garden?"
    player_name "Did I screw something up?"
    show player 5f with dissolve
    show diane a_dressed_blush f_shamed_talk_smile with dissolve
    dia "Oh no, handsome..."
    dia "This is all my fault."
    show diane a_dressed_shovel with dissolve
    dia "I went with an all natural pesticide this year and it wasn't as effective as I was hoping."
    show diane f_shamed
    show player 12f
    player_name "Pesticide?"
    show player 5f
    show diane f_shamed_talk_smile
    dia "Yeah, you see those critters crawling all over the garden?"
    show diane f_shamed
    show player 10f
    player_name "Yeah..."
    show player 5f
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "Those are {b}earwigs{/b}."
    show diane f_shamed a_dressed_shovel with dissolve
    player_name "..."
    show player 12f
    player_name "Why do they call them earwigs?"
    show player 5f
    show diane f_laugh
    dia "Hehe, it's from an old wives tale... People used to believe earwigs would crawl into your ear and lay eggs in your brains."
    show diane f_normal
    show player 11f
    player_name "!!!"
    show player 10f
    player_name "That's not... I mean, they don't really-"
    show player 5f
    show diane f_laugh a_dressed_blush with dissolve
    dia "Hahaha! No, of course not!"
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "They prefer moist rich soil, which is why they ended up in our garden here."
    dia "I betcha there are dozens of nests in that soil right now..."
    show diane f_normal
    show player 12f
    player_name "... Gross!!!"
    player_name "So how do we fix it?"
    show player 5f
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Hmm, well for starters, we're gonna have to throw out all these infested crops and destroy as many nests as we can."
    dia "Then we'll need to till the soil and replant."
    dia "Making sure we use a more effective pesticide this time."
    show diane f_normal a_dressed_shovel with dissolve
    show player 14f
    player_name "Alright."
    player_name "Let's get started!"
    show player 13f
    show diane f_normal_talk
    dia "Hehe, so eager..."
    dia "I can't believe you're enjoying gardening so much!"
    show diane f_normal
    show player 14f
    player_name "It's a lot of fun!"
    show player 13f
    show diane f_normal_talk
    dia "Alright, well dig in!"
    hide player
    hide diane
    with dissolve
    jump garden_listing
    return

label dianes_garden_diane_bug_infestation:
    scene garden
    show player 10 at left with dissolve
    player_name "{b}Diane{/b}?"
    show player 4 with dissolve
    player_name "..."
    show player 12 with dissolve
    player_name "That's weird."
    player_name "She's usually waiting here to greet me."
    show player 31 with dissolve
    player_name "!!!"
    show player 32
    player_name "Oh, no!"
    player_name "What's wrong with the garden?!"
    hide player with dissolve
    return

label dianes_garden_diane_check_up_on_garden:
    scene garden
    show player 14 with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "How's the-"
    show player 32 at Position (xoffset=68) with dissolve
    player_name "Wow!!!"
    show player 17 with dissolve
    player_name "The garden looks great!"
    show player 14
    player_name "I can't believe everything is growing back so quickly."
    show player 30
    player_name "Hmm..."
    show player 32f with dissolve
    player_name "{b}Diane{/b} is missing again..."
    player_name "I wonder where she's hiding?"
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
    player_name "Hi, {b}Diane{/b}."
    show player 3
    show diane f_laugh
    dia "I'm so glad you're here!"
    show diane f_normal_talk
    dia "Did {b}[deb_name]{/b} tell you about my new client?"
    show diane f_normal
    show player 29
    player_name "Yeah, she said you landed a big one."
    show player 3
    show diane f_laugh
    dia "You better believe it!"
    show diane f_normal_talk
    dia "I've got a lot of work to do before we can make the delivery."
    dia "I'm afraid I won't really have time to tend the garden..."
    show diane f_normal
    show player 5 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Think you can handle it by yourself?"
    show diane f_explain
    dia "I'll give you a bump in pay..."
    show diane f_cheese
    show player 10
    player_name "Yeah, that's fine."
    show player 5
    show diane f_normal
    dia "..."
    show diane f_shamed_talk_smile
    dia "What's the matter, handsome?"
    dia "You still thinking about the other day?"
    show diane f_shamed
    show player 12
    player_name "Yeah, I'm really sorry about the whole-"
    show player 11
    show diane f_laugh a_dressed_finger with dissolve
    dia "Oh, don't be silly, handsome."
    show diane f_normal_talk
    dia "You're a young man!"
    dia "You can't always control those things!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 29 with dissolve
    player_name "Yeah, I guess..."
    show player 3
    show diane f_normal_talk
    dia "Don't give it another thought, {b}[firstname]{/b}!"
    show diane f_normal
    show player 13 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Alright, well I'd best get started."
    dia "Lots of work to do!"
    dia "I'll be in the shed getting everything ready if you need me, okay?"
    show diane f_normal
    show player 23
    player_name "{b}*Gasp*{/b} Is the cow in there now?"
    show player 14
    player_name "Can I pet it?!"
    show player 13
    show diane f_normal_talk
    dia "Huh?"
    show diane f_lookup
    dia "Oh, the cow... Uhh, no."
    show diane f_smirk
    dia "..."
    show diane f_smirk_talk
    dia "I'll go and visit the cow later tonight."
    show diane f_smirk
    show player 12
    player_name "So, what are you doing in the shed now?"
    show player 5
    show diane f_surprised_down a_dressed_blush with dissolve
    dia "I uhh..."
    show diane f_shamed_talk_smile a_dressed_finger with dissolve
    dia "... Cleaning!"
    dia "Yeah, I have to get all the equipment sterilized and make sure all the packaging is ready."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 17
    player_name "I see."
    show player 14
    player_name "Do you need any help?"
    show player 13
    show diane f_laugh
    dia "No thanks, handsome."
    dia "You just focus on the gardening for now and I'll-"
    show diane f_explain a_dressed_finger with dissolve
    dia "!!!"
    show diane f_normal_talk
    dia "Actually, there is something you can do for me!"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Sure, anything."
    show player 13
    show diane f_smirk_talk
    dia "{b}I left one of my tools on the kitchen counter.{/b}"
    dia "Could you run and fetch it for me?"
    show diane f_smirk
    show player 14
    player_name "Of course."
    player_name "I'll be right back."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_diane_delivery_2_task:
    scene garden
    show diane b_shirtless a_shirtless_tired f_tired_down at lright
    show player 14 at left
    with dissolve
    player_name "Hello, {b}Diane{/b}."
    player_name "How are you-"
    show player 11
    player_name "!!!"
    show player 10
    player_name "Are you okay?"
    player_name "You look exhausted!"
    show player 5
    show diane f_tired_talk
    dia "Oh, yeah. I'm alright."
    dia "I just haven't gotten much sleep these past few days..."
    dia "This latest delivery is killing me!"
    show diane f_tired
    show player 10
    player_name "That's not good."
    player_name "Are you sure I can't help you milk the cow?"
    show player 12
    player_name "I really wouldn't mind."
    show player 5
    show diane f_tired_talk
    dia "I bet you wouldn't!"
    show diane f_laugh
    dia "Hahahaha!"
    show diane f_tired
    show player 11
    player_name "..."
    show diane f_tired_talk
    dia "Sorry, I'm a little loopy right now."
    show player 5
    dia "There's no need, stud."
    dia "I finished the order last night."
    show diane f_tired
    show player 12
    player_name "Oh."
    show player 14
    player_name "Well, that's good!"
    show player 13
    show diane f_tired_talk
    dia "You wouldn't mind delivering it for me again, would you?"
    show diane f_tired
    show player 14
    player_name "Of course not!"
    player_name "I'd love to deliver it for you."
    show player 13
    show diane f_tired_talk
    dia "Oh, you're a lifesaver, handsome!"
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "You won't have far to go; It's for the daycare next door."
    show diane f_tired
    show player 10
    player_name "Next door?"
    player_name "I think {b}Anne{/b} lives next door..."
    show player 5
    show diane f_tired_down
    dia "Hmm?"
    show player 12
    player_name "She's a girl from my class."
    show player 5
    show diane f_tired_talk
    dia "Oh, that must be {b}Lucy's daughter{/b}."
    show diane f_tired
    show player 12
    player_name "{b}Lucy{/b}? I dunno, maybe..."
    show player 5
    show diane f_tired_talk
    dia "Well, if she's anything like her mother, I'm sure she's delightful!"
    show diane f_tired
    show player 12
    player_name "... Yeah. I dunno about that."
    show player 5
    show diane f_tired_talk
    dia "Give them my regards, will you?"
    dia "I've gotta get some sleep."
    dia "... Just bring me the money when you're finished, okay?"
    show diane f_tired
    show player 14
    player_name "Sure thing, {b}Diane.{/b}"
    show player 13
    show diane f_tired_talk
    dia "Thanks, stud."
    show diane f_tired at Position (xpos=450) with dissolve
    show player 10
    player_name "Wait!!"
    show player 5
    dia "Hmm?"
    show player 12
    player_name "Where's the delivery?"
    show player 5
    show diane f_tired_down
    dia "..."
    show diane f_laugh
    dia "Oh! Hahahahaha!!"
    dia "Yeah, you'll probably need that, huh?"
    show diane f_tired_talk
    dia "It's in the shed."
    dia "I left it unlocked for you, handsome."
    show diane f_tired
    show player 17
    player_name "Okay, I'm on it."
    show player 13
    show diane f_tired_talk
    dia "Thanks again, handsome."
    hide diane
    hide player
    with dissolve
    return

label dianes_garden_diane_d9_intro:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_tired f_tired
    with dissolve
    player_name "Hey, {b}Diane{/b}."
    player_name "Feeling better today?"
    show player 5
    show diane f_tired_talk
    dia "Hey, handsome."
    dia "I feel fine. Thanks for asking."
    show diane f_tired
    show player 10
    player_name "... You sure? You still look really tired."
    show player 5
    show diane f_tired_talk
    dia "Heh, do I?"
    show diane f_tired
    show player 10
    player_name "How much sleep did you get yesterday?"
    show player 5
    show diane f_tired_talk
    dia "I'm not sure."
    dia "I saw that note you left me about {b}Lucy's{/b} next order and I've been trying to get a head start on production."
    dia "It's strenuous but I'm just going to have to get used to it, I guess..."
    show diane f_tired
    show player 10
    player_name "What do you mean?"
    show player 5
    show diane f_tired_talk
    dia "Well, my orders aren't slowing down anytime soon."
    dia "As a matter of fact, they're getting bigger."
    show diane f_tired
    show player 10
    player_name "Yeah, but-"
    show player 5
    show diane f_tired_talk
    dia "I've even got a line on another new client."
    dia "My biggest yet."
    show diane f_tired
    show player 10
    player_name "{b}Diane{/b}..."
    player_name "You have to take care of yourself first..."
    player_name "Are you sure you aren't taking on too much, too quickly?"
    player_name "I worry about you."
    show player 5
    show diane f_tired_talk
    dia "Aww."
    dia "I appreciate your concern, {b}[firstname]{/b}, but you don't need to worry about me."
    dia "This business has been a dream of mine for a long time."
    dia "It'll take a lot more than a few sleepless nights to stop me from seeing it through."
    show diane f_tired
    show player 10
    player_name "... Alright, just..."
    show player 14
    player_name "... Remember I'm here to help if you need it."
    show player 13
    show diane f_tired_talk
    dia "Thanks, {b}[firstname]{/b}."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_tired f_tired_talk
    with dissolve
    dia "Well, I should get back to it."
    dia "Take good care of my garden, won't you?"
    show diane f_tired
    show player 14
    player_name "Of course."
    hide player
    hide diane
    with dissolve
    return

label dianes_garden_shed_light_on:
    scene expression player.location.background_blur
    show player 4 with dissolve
    player_name "( Hmm? )"
    player_name "( {b}The door is open and the light is on!{/b} )"
    player_name "( She can't seriously still be working, can she? )"
    hide player with dissolve
    return

label dianes_garden_diane_missing:
    scene garden
    show player 127 with dissolve
    player_name "Where's {b}Diane{/b}?"
    show player 12
    player_name "She's usually outside around this time..."
    show player 56
    player_name "She must be somewhere."
    hide player 56 with dissolve
    return

label dianes_garden_diane_daylight_drinking:
    return

label dianes_garden_diane_ready_for_day_off:
    scene garden
    show player 14 at left
    show diane b_shirtless a_shirtless_sides at lright
    with dissolve
    player_name "Hey {b}Diane{/b}!"
    player_name "You ready for your day off?"
    show player 13
    show diane f_normal_talk
    dia "Hi, {b}[firstname]{/b}."
    dia "Hehe, yeah I guess..."
    dia "I just need to finish up this last batch I was working on this morning and-"
    show diane f_normal
    show player 33
    player_name "No, no, no..."
    show player 14
    player_name "You're done working today!"
    show player 13
    show diane f_normal_talk
    dia "... But I have to make sure everything is stored away correctly."
    show diane f_normal
    show player 14
    player_name "Just tell me what to do and I'll handle it."
    show player 17
    player_name "The rest of your day is all about relaxation!"
    show player 13
    show diane f_laugh a_shirtless_shock with dissolve
    dia "Hahaha. Okay, okay..."
    show diane f_normal_talk a_shirtless_sides with dissolve
    dia "{b}Just head into the shed and dump what's in the pump into a storage jug.{/b}"
    show diane f_normal
    show player 14
    player_name "That sounds easy enough."
    show player 13
    show diane f_normal_talk
    dia "... But you have to make sure you get the cap on tight!"
    show diane f_normal
    show player 14
    player_name "You just take a seat and I'll handle it, okay?"
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
    vero "I just can't get over how good your garden is looking nowadays!"
    vero "I remember when it was just a sad little patch of tomatoes..."
    show vero f_normal
    show diane f_laugh
    dia "Haha, thanks {b}Vee{/b}!"
    show diane f_normal_talk
    dia "It certainly has come a long way..."
    show diane f_normal
    show vero f_normal_talk
    vero "It's really gorgeous, {b}Diane{/b}!"
    vero "Wow!!!"
    show vero bending at flip
    show vero at Position (xoffset=100)
    show diane f_down_front
    with dissolve
    pause
    hide vero
    show vero f_normal_talk b_casual a_cucumber1 at Position (xpos=600)
    show diane f_normal
    with dissolve
    vero "Look at the size of this one!"
    show vero f_normal
    show diane f_normal_talk
    dia "Yeah, I know!"
    show diane f_smirk_talk
    dia "He's a monster."
    show diane f_smirk
    show vero f_normal_talk a_cucumber2 with dissolve
    vero "I'll say..."
    show vero f_normal
    show diane f_normal_talk
    dia "You wanna take him home with you?"
    show diane f_wink
    show vero f_rolleyes a_cucumber1 with dissolve
    vero "Oh my gosh, I should never have told you about that..."
    show vero f_sexy
    show diane f_laugh a_dressed_finger with dissolve
    dia "Hey, I'm not one to judge."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_down
    vero "..."
    show vero f_sexy_talk_down
    vero "No, it's way too big for me!"
    show vero f_sexy_down
    show diane f_laugh
    dia "Haha, yeah. Me too."
    show diane f_smirk
    show vero f_surprised_down
    vero "Ahaha, I knew you'd try it!"
    show vero f_sexy a_casual_front with dissolve
    show diane f_smirk_talk
    dia "Yeah, yeah..."
    show diane f_smirk
    show vero f_sexy_talk
    vero "So what's your secret?"
    vero "You aren't using hormones on them or anything are you?"
    show vero f_sexy
    show diane f_normal_talk
    dia "Psh, of course not!"
    dia "I remember our discussion about that."
    show diane f_normal
    show vero f_sexy_talk
    vero "Good."
    show vero f_sexy
    show diane f_normal_talk
    dia "To be honest, I've left most of the gardening to my friend this year."
    show diane f_normal
    show vero f_normal_talk
    vero "Oh, you mean that cute one you brought into the store the other day?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Don't get any ideas, {b}Vee{/b}!"
    dia "He's a good kid."
    show diane f_normal
    show vero f_normal_talk
    vero "Yeah, so?"
    show vero f_sexy_talk
    vero "I'm a nice girl..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Uh huh."
    show diane f_normal
    show vero f_laugh
    vero "Hehehe!"
    show vero f_sexy
    show diane f_normal_talk
    dia "His guardian would kill me if I let you get your claws on him."
    show diane f_normal
    show vero f_sexy_talk
    vero "Aww, c'mon."
    show vero f_sexy
    show diane f_normal_talk a_dressed_finger with dissolve
    dia "Absolutely not, {b}Vee{/b}."
    show diane f_normal a_dressed_shovel with dissolve
    show vero f_sexy_talk
    vero "Tsk, you're no fun."
    show vero f_sexy
    pause
    show vero f_thinking
    vero "... Arrghh..."
    vero "Sometimes I really regret moving to this town."
    vero "The men here suck!"
    show vero f_normal
    show diane f_normal_talk
    dia "You don't have to tell me."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "You're not thinking about moving back to the farm are you?"
    show diane f_normal
    show vero f_laugh
    vero "Oh, heck no!"
    show vero f_normal_talk
    vero "If I went back there with my tail between my legs, I'd never hear the end of it.!"
    vero "{b}*Sigh*{/b}"
    vero "I can't believe I've been working at {b}Consum-R{/b} for five years!"
    vero "It's so depressing..."
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "Oh, that reminds me!"
    vero "I wanted to ask you how the new business is going?"
    show vero f_normal
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "Oh, uhh..."
    show diane a_dressed_shovel with dissolve
    dia "It's going well, so far."
    show diane f_normal
    show vero f_normal_talk
    vero "You're still not ready to give me the details?"
    show vero f_normal
    show diane f_normal_talk
    dia "Mmm, not quite yet..."
    show diane f_normal
    show vero f_rolleyes
    vero "Ugh, fiiiine."
    show vero f_normal_talk
    vero "Just don't forget about me when you start making the big bucks!"
    vero "I'm a quick learner and I'll work hard for you {b}Diane{/b}."
    show vero f_normal
    show diane f_normal_talk
    dia "Heh, I know that {b}Vee{/b}..."
    dia "I just don't have enough work to warrant hiring an extra hand at the moment."
    dia "I promise, I'll call you as soon as I do."
    show diane f_normal
    show player 13 at left with dissolve
    show vero f_normal_talk
    vero "You had better."
    show vero f_normal
    show player 14
    player_name "Hello ladies."
    show player 13
    show vero f_sexy_talk
    vero "Uh oh, your boyfriend is here..."
    show vero f_sexy
    show diane f_normal_talk
    dia "Tch, shuddup {b}Vee{/b}!"
    show diane at unflip
    show diane at lcenter
    with dissolve
    dia "Ignore her, {b}[firstname]{/b}."
    show diane f_normal
    show vero f_sexy_talk
    vero "Oh, he knows I'm only teasing..."
    show vero f_normal_talk
    vero "We were just talking about this beautiful garden you've been working on."
    show vero f_normal
    show player 17
    player_name "It looks pretty good, huh?"
    show player 18
    show vero f_normal_talk
    vero "It looks better than good."
    vero "What's your secret?"
    show vero f_normal
    show player 10
    player_name "Huh?"
    show player 5
    show vero f_normal_talk
    vero "You've gotta be doing something special to get results like this."
    show vero f_normal
    show player 35
    player_name "Hmm, not really."
    show player 14
    player_name "I just till it, sow it, and water it."
    player_name "Like {b}Diane{/b} taught me."
    show player 13
    show vero f_normal_talk
    vero "That's it?"
    show vero f_normal
    show player 14
    player_name "Yup."
    show player 13
    pause
    show player 35
    player_name "Oh!"
    show player 14
    player_name "I have been fertilizing it with compost..."
    show player 10
    player_name "... Maybe that's my secret?"
    show player 13
    show diane f_laugh
    dia "Hahaha!"
    show vero f_laugh
    vero "Hehe, maybe..."
    show diane f_normal
    show vero f_normal
    pause
    show vero f_normal_talk
    vero "Well, I should probably get going..."
    show vero f_normal
    hide diane
    show diane f_normal_talk at flip
    show diane at Position (xpos=250)
    with dissolve
    dia "So soon?"
    show diane f_normal
    show vero f_normal_talk
    vero "Heh, Yeah. Those groceries at {b}Consum-R{/b} aren't going to sell themselves you know?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Hah, I suppose not."
    hide vero
    show diane hug_vero_talk at Position (xoffset=200)
    with dissolve
    dia "Swing by anytime, alright?"
    show diane f_normal
    show vero f_normal_talk b_casual a_casual_front at Position (xpos=600)
    vero "Will do."
    show vero f_normal
    show player 14
    player_name "Bye {b}Veronica{/b}."
    player_name "Nice seeing you again."
    show player 13
    show vero f_normal_talk
    vero "Yeah, you too handsome."
    show vero f_sexy
    pause
    show vero f_sexy_talk
    vero "You know what?"
    vero "I think I'll take that cucumber afterall..."
    show vero bending at Position (xoffset=370)
    show diane f_down_front
    with dissolve
    pause
    show player 426
    vero "Hmm, now where did I put it..."
    show diane f_lookup
    dia "Oh, good grief!"
    show diane f_laugh
    dia "Haha, would you get out of here already!"
    show diane f_normal
    show vero f_sexy_talk b_casual a_cucumber1 at Position (xpos=600) with dissolve
    show player 13
    vero "Hehe, thanks again, {b}Diane{/b}!"
    hide vero with dissolve
    player_name "..."
    hide diane
    show diane f_normal_talk
    with dissolve
    dia "You ready to get to work, {b}stud{/b}?"
    show diane f_normal
    show player 10
    player_name "Hmm?"
    show player 14
    player_name "Oh!"
    player_name "Yup, I'm ready."
    show player 13
    show diane f_normal_talk
    dia "Glad to hear it."
    show diane f_shamed_talk_smile
    dia "... But uhh, before you get started..."
    show diane f_shamed
    show player 14
    player_name "Yeah?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "I think I should apologize."
    show diane f_shamed a_dressed_shovel with dissolve
    show player 10
    player_name "Apologize?"
    show player 5
    show diane f_shamed_talk_smile
    dia "You know, the other day..."
    dia "... With the uhh-"
    dia "{b}*Ahem*{/b} I just had too much to drink and things got a little... Umm, inappropriate."
    show diane f_shamed
    player_name "..."
    show diane f_shamed_talk_smile
    dia "It's just been a long while since anyone has shown me that kind of attention and I've been lonely a lot recently and-"
    dia "Ugh, no. Damnit, that's no excuse... I-"
    show diane f_sad_talk
    dia "Look, I took advantage of you, {b}[firstname]{/b} and I'm really sorry... I-"
    show diane f_sad
    show player 14
    player_name "You didn't take advantage of me!"
    show player 13
    show diane f_sad_talk
    dia "Huh?"
    show diane f_sad
    show player 17
    player_name "It was awesome!"
    player_name "I was kinda hoping we could do it again sometime?"
    show player 13
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "You wanna do it again?!"
    show diane f_shamed
    show player 26
    player_name "Of course. You're a beautiful woman, {b}Diane{/b}!"
    show player 13
    show diane f_shamed_talk_smile a_dressed_shovel with dissolve
    dia "O-okay, but-"
    dia "{b}[deb_name]{/b} trusted me to look after you and it wasn't right of me to-"
    show diane f_shamed
    show player 14
    player_name "I'm not a child, {b}Diane{/b}. And besides, it was fun!"
    show player 13
    show diane f_shamed_talk_smile
    dia "... And {b}[deb_name]{/b} would kill me if she found out."
    show diane f_shamed
    show player 14
    player_name "She doesn't have to know."
    show player 13
    dia "..."
    show player 14
    player_name "I mean, we're just having a little fun."
    player_name "I don't see the harm in it."
    show player 13
    show diane f_shamed_talk_smile
    dia "Hmm."
    dia "Wouldn't you rather do that stuff with girls your own age?"
    show diane f_shamed
    show player 14
    player_name "Are you kidding?!"
    player_name "You're like a million times hotter than the girls at my school, {b}Diane{/b}!"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Oh, I am not!"
    show player 17
    player_name "Heh, it's true."
    show player 18
    show diane f_smirk a_dressed_shovel with dissolve
    pause
    show diane f_lookup
    dia "Alright, Mr. Charmer..."
    show diane f_smirk_talk
    dia "We're clearly not in the right mindset to have this conversation."
    dia "So, let's just focus on work, shall we?"
    show diane f_smirk
    show player 12
    player_name "Seriously?"
    show player 5
    show diane f_smirk_talk
    dia "Yes, seriously!"
    show diane f_normal_talk
    dia "I'll be in the shed if you need something."
    show diane f_normal
    show player 26
    player_name "You sure I can't give you a hand?"
    show player 13
    show diane f_laugh
    dia "Haha, no. I don't need a hand..."
    show diane f_smirk_talk
    dia "Nice try."
    show diane f_smirk
    show player 14
    player_name "What?!"
    show player 13
    show diane f_smirk_talk
    dia "Just get started on your garden work."
    show diane f_smirk
    show player 14
    player_name "Alright."
    show player 13
    hide diane with dissolve
    pause
    show player 5
    player_name "( Hmm, I hope I didn't upset her... )"
    player_name "{b}( I should probably leave her be for now and just focus on my work in the garden. ){/b}"
    hide player with dissolve
    return

label dianes_garden_diane_do_not_disturb:
    scene townmap
    player_name "I should visit {b}Diane{/b} another time..."
    return

label dianes_garden_diane_shed_still_open:
    show player 12 with dissolve
    player_name "That's strange..."
    show player 30
    player_name "{b}Diane's{/b} shed is {b}still open{/b}..."
    hide player 30 with dissolve
    return

label drink_offered:
    scene garden
    if M_diane.get("aunt_drink_made"):
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "I should give {b}Diane{/b} her {b}drink{/b} before I get back to work..."
    $ game.main()

label aunt_masturbate_not_seen:
    show diane_masturbate 1_2
    player_name "!!!"
    player_name "( ... What is she... )"
    window hide
    pause 2
    player_name "( WOW... )"
    player_name "( She's playing with her vegetables... )"
    player_name "( A whole cucumber! )"
    player_name "( ... )"
    player_name "( ...I should leave before I get caught. )"
    scene garden
    with dissolve
    show player 113 with dissolve
    player_name "I can't believe I caught her masturbating!"
    show player 114
    player_name "... or that she's horny enough to do it with veggies!"
    show player 113
    player_name "Is that why she only wants {b}long{/b} and {b}hard{/b} ones?"
    show player 109f
    player_name "Hmm..."
    show player 108f
    player_name "I guess she has been lonely lately..."
    player_name "I should get back to work and pretend I didn't see anything..."
    hide player 108f with dissolve
    $ renpy.end_replay()
    return

label find_shovel:
    scene expression game.timer.image("garden{}")
    show player 12 with dissolve
    if player.has_item("shovel"):
        player_name "I should let {b}Diane{/b} know that I'm ready to start working."
    else:
        player_name "I need to find a {b}shovel{/b} before I can help with the garden..."
    hide player with dissolve
    $ game.main()


label before_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "I should find out if {b}Diane{/b} is home first."
    $ game.main()

label after_masturbation:
    scene expression game.timer.image("garden{}")
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Maybe not right now."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
