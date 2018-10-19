label dianes_kitchen_diane_breeding_bull_started:
    scene location_diane_kitchen_closeup with None
    show player 1 at left
    show diane 88 at right
    with dissolve
    pause
    show diane 89
    dia "Доброе утро, красавчик!"
    show diane 88
    show player 36
    player_name "Доброе утро, {b}Диана{/b}."
    show player 13
    show diane 92
    dia "Так... Я думала о том, что ты сказал ВСЮ ночь."
    dia "Это нелегкое решение, и я не хочу, чтобы это было чем-то, о чем я сожалею."
    show diane 87
    dia "Но, твое предложение звучит так заманчиво, и у него есть несколько преимуществ, так..."
    show diane 89
    dia "Я решила развлечься с твой идеей и быть воспитанной!"
    show player 17
    show diane 88
    player_name "Правда? Я рад, что тебе понравилась моя идея!"
    show player 13
    show diane 90
    dia "Если я собираюсь продвинуться в доильном бизнесе, мне понадобится настоящее, работающее вымя!"
    show diane 87
    dia "Я очень хочу, чтобы все получилось, поэтому я буду придерживаться литературы!"
    show diane 89
    dia "Плюс мысль о том, что {b}тебя будут разводить как сучку в жару{/b}... Это заводит меня больше, чем ты можешь себе представить!"
    show diane 88
    show player 21
    player_name "Правда?"
    show player 13
    show diane 90
    dia "Мне пришлось поменять простыни дважды прошлой ночью!"
    show diane 92
    show player 11
    dia "Но у меня есть небольшая проблема..."
    show diane 89
    dia "Я просто не уверена, что смогу найти, понимаешь... молодого, здорового бычка!"
    dia "Но, все в порядке. Я могу начать работать над деталями."
    show diane 88
    show player 14
    player_name "Рад, что смог помочь! Я счастлив, что ты счастлива!"
    show player 13
    show diane 89
    dia "Спасибо."
    dia "О, И если ты думаешь, что знаешь кого-то, кто подходит мне, ты дашь мне знать?"
    show diane 88
    show player 21
    player_name "Ухх... Хорошо!"
    hide player
    hide diane
    with dissolve
    return

label dianes_kitchen_diane_mouse_attack_started:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "Блин. Ее здесь тоже нет."
    player_name "( Я был абсолютно уверен в этом... )"
    show player 11
    dia "ИИИИИИИИККККККК!"
    show player 23f
    player_name "Что за..."
    player_name "( Это кричит {b}Диана{/b}?! )"
    hide player with dissolve
    return

label dianes_kitchen_diane_drunken_splur_not_known:
    scene dianekitchen1
    player_name "( Здесь никого нет. )"
    player_name "( {b}Диана{/b} снаружи у сада. )"
    return

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( Я не могу просто уйти, {b}Диана{/b} может быть в беде. )"
    hide player with dissolve
    $ game.main()

label dianes_kitchen_diane_kitchen_drink_intro:
    scene dianekitchen
    show player 133 with dissolve
    player_name "( Это должно быть... )"
    show player 135
    player_name "Иииии... там."
    show player 132
    show expression "characters/xtra/char_xtra_01.png" at Position(xpos = 638, ypos = 519)
    player_name "Хммм..."
    show player 133
    player_name "( Может, мне добавить ещё немного? )"
    return

label dianes_kitchen_diane_kitchen_drink_no:
    show player 133
    player_name "Нет. Этого должно быть достаточно..."
    player_name "( {b}Диане{/b} тоже... нравится, когда у нее есть немного выпивки. )"
    show player 134
    player_name "( Этого хватит... )"
    return

label dianes_kitchen_diane_kitchen_drink_yes:
    show player 135
    player_name "Таааааак... {b}эще немножко{/b}!"
    show player 134
    player_name "( Этого хватит... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
