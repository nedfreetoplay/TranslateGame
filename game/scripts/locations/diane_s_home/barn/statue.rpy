label barn_garden_statue_dialogue:
    $ M_daisy.trigger(T_daisy_view_statue)
    if player.has_item("milk_sample"):
        call expression game.dialog_select("barn_statue_has_milk")
        $ M_daisy.trigger(T_daisy_awaken_statue)
    else:
        call expression game.dialog_select("barn_statue_has_not_milk")
    $ game.main()

label barn_statue_has_milk:
    scene expression "backgrounds/location_diane_garden_closeup.jpg"
    show player 712 at left with dissolve
    player_name "( Итак, {b}ведерко с молоком{/b}, да? )"
    pause
    show diane b_shirtless a_shirtless_sides f_shamed_talk_smile at Position (xpos=600) with dissolve
    dia "Что ты делаешь с этим {b}молоком{/b}, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 713
    player_name "У меня есть идея."
    show player 184 with dissolve
    show diane f_shamed_talk_look
    dia "У тебя есть идея?"
    hide player with dissolve
    dia "Ты не собираешься-"
    scene expression "backgrounds/location_diane_garden_cutscene09.jpg"
    show expression FilteredText("Мне пришлось вылить молоко в ведро.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Это было похоже на желание, с которым я не мог бороться.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("Я не уверен, что ожидал такого развития событий...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene expression "backgrounds/location_diane_garden_cutscene10.jpg"
    show expression FilteredText("... Но я никогда не мог предвидеть того, что произошло.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Статуя начала трескаться и из нее начало исходить странное свечение.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("Вскоре стало так светло, что нам с {b}Дианой{/b} пришлось прикрыть глаза!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression player.location.background_blur with None
    show player 428 at left
    show diane b_naked a_naked_sides f_surprised_front at Position (xpos=600)
    with dissolve
    player_name "!!!"
    show diane f_surprised_front_talk
    dia "Что это такое-"
    show diane f_surprised_front
    show player 10b
    player_name "Он светится..."
    show player 428
    pause
    show diane f_surprised_front_talk
    dia "Он такой яркий!"
    show player 718
    show diane f_scream a_shirtless_cover
    with dissolve
    dia "Аааа!"
    player_name "!!!"
    show daisy b_appear_flash a_empty f_empty at Position (xpos=300) with flash
    pause
    show daisy b_appear with dissolve
    pause
    show player 23 with None
    show daisy f_sad_talk_closed b_naked a_naked_up
    show diane f_scared a_shirtless_sides
    with dissolve
    cow "Нет, хозяин!!!"
    show player 428
    cow "Пожалуйста, я буду хорошей девочкой!"
    cow "Я буду, Я-"
    show player 22
    pause
    show player 5b
    show daisy f_sad_talk
    pause
    show daisy f_scared b_naked a_naked_cover
    cow "АААААААААААА!!!" with hpunch
    show daisy f_sad_talk_closed
    cow "Не смотри на меня так!"
    cow "Я не хотела этого делать!!"
    show player 10b
    player_name "Какого черта?"
    show player 5b
    cow "Ты не можешь меня видеть!"
    cow "Пожалуйста, он сделает мне больно, если узнает!"
    show player 11
    show diane f_scared_talk
    dia "Кто сделает тебе больно, милая?"
    show diane f_scared with None
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "Хозяин."
    show player 4 with dissolve
    show diane f_scared_talk
    dia "Кто?"
    show diane f_scared
    show daisy f_sad_talk
    cow "{b}*Ваааааа*{/b}"
    show daisy f_sad
    show player 10
    player_name "Я думаю, она говорит о {b}Джебадиане Делмонте{/b}."
    show player 5
    show diane f_scared_talk
    dia "Кто такой {b}Джебадиан Делмонт{/b}?"
    show diane f_scared
    show player 12
    player_name "Это длинная история..."
    show player 5
    pause
    show player 12
    player_name "Скажем так, это он сделал статую."
    show player 5
    pause
    show diane f_sad_talk
    dia "Ты об этом говоришь, дорогая?"
    show diane f_sad
    show daisy f_sad_talk_closed
    cow "{b}*фырк*{/b} Ух хух."
    show daisy f_sad
    show diane f_sad_talk
    dia "Ой, бедняжка."
    dia "Не волнуйся, он больше никогда тебя не обидит."
    show diane f_sad
    show daisy f_sad_talk
    cow "{b}*фырк*{/b} Он будет..."
    show daisy f_sad
    show diane f_sad_talk
    dia "Нет, я не позволю ему."
    show diane f_sad
    show daisy f_sad_talk a_naked_wiping_tears with dissolve
    cow "Ты обещаешь?"
    show daisy f_shy_sad b_naked_shy a_naked_shy_cover at Position (yoffset=10) with dissolve
    show diane f_shamed_talk_smile
    dia "Я обещаю."
    hide daisy
    hide diane
    show daisy b_naked_diane_comfort a_empty f_empty
    show diane a_empty b_empty f_shamed_talk_look_closed
    with dissolve
    pause
    show diane f_shamed_talk_look
    dia "Ой, ну ну..."
    dia "Все будет в порядке."
    dia "Давай отведем тебя в сарай и укроем, хорошо?"
    show daisy b_naked_diane_comfort2_shirtless
    show diane f_shamed_talk_look_closed
    cow "{b}*фырк*{/b} Хорошо."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 34
    player_name "( Что, черт возьми, только что произошло?! )"
    player_name "( Действительно ли сумасшедший дедушка {b}Клайда{/b} был волшебником?! )"
    pause
    show player 37 with dissolve
    player_name "( {b}Я должен пойти за ними в сарай и узнать больше.{/b} )"
    hide player with dissolve
    return

label barn_statue_has_not_milk:
    scene expression player.location.background_blur with None
    show player 426 with dissolve
    player_name "( Вау, статуя действительно хорошо выглядит в саду Дианы! )"
    pause
    player_name "( Однако в ней что-то не так. )"
    player_name "( Она выглядит так, будто боится... )"
    pause
    show player 4 with dissolve
    player_name "( ... И почему у нее {b}ведерко с молоком{/b}, интересно? )"
    pause
    show player 426 with dissolve
    player_name "( Хмм, странно... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
