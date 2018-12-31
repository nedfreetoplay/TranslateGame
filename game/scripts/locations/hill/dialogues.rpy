label hill_first_visit:
    scene expression game.timer.image("hill{}_b")
    show player 32 with dissolve
    player_name "Вау! Вот это вид!"
    show player 14 at Position(xpos = 444)
    player_name "( Идеальное место, чтобы привести девушку на свидание... )"
    show player 4 at Position(xpos = 450)
    player_name "( ...Если бы у меня только была машина! )"
    hide player with dissolve
    return

label hill_mia_find_harold:
    scene expression game.timer.image("hill{}")
    show harold_car_02 at Position (xpos=575,ypos=550)
    show player 31 with dissolve
    player_name "..."
    show player 32
    player_name "( Я вижу полицейскую машину. )"
    player_name "( Может это {b}Гарольд{/b}? )"
    hide player with dissolve
    return

label hill_tree:
    scene expression game.timer.image("location_lair_hill_tree{}")
    if not player.has_item("scroll"):
        jump expression game.dialog_select("hill_tree_no_scroll")
    else:
        pause
	$ game.main()

label hill_tree_no_scroll:
    if not game.timer.is_dark():
        show expression "objects/object_scroll_01.png" at Position(xalign = 0.45, yalign = 0.65)
    else:
        show expression "objects/object_scroll_01_night.png" at Position(xalign = 0.45, yalign = 0.65)
    player_name "Что это такое? Какой-то старый свиток?"
    player_name "Интересно, как долго он там был."
    call screen hill_tree
    
label hill_tree_get_scroll:
    $ player.get_item("scroll")
    show popup_item_scroll1 at truecenter with dissolve
    pause
    hide popup_item_scroll1 with dissolve
	$ game.main()
	
	label hill_dewitt_stick:
    call expression game.dialog_select("hill_dewitt_stick_dialogue")
    $ player.get_item("stick")
    $ game.main()

label hill_dewitt_stick_dialogue:
    scene expression game.timer.image("hill{}_b")
    show player 14 with dissolve
    player_name "Это дерево подойдет идеально!"
    player_name "Я должен работать над созданием флейты в моем гараже."
    hide player with dissolve
    return

label hill_harolds_car:
    call expression game.dialog_select("hill_harolds_car_dialogue")
    $ M_mia.trigger(T_harold_found)
    $ game.main()

label hill_harolds_car_dialogue:
    scene hill_c
    show harold 28 at right
    show player 10 at left
    with dissolve
    player_name "{b}Гарольд{/b}?!"
    show player 11
    show harold 19
    harold "Привет... Что ты {b}*ик*{/b} делаешь здесь... Разве ты не должен быть в постели?"
    show harold 18
    show player 12
    player_name "Эхх... Сейчас полдень, сэр."
    show player 11
    show harold 20
    harold "О, точно. Это верно."
    show harold 19
    harold "Невожно, но..."
    show harold 18
    show player 10
    player_name "Вы в порядке, сэр?"
    show player 5
    show harold 19
    harold "Я думаю, что я {b}*ик*{/b} живой..."
    harold "...Моя жена, кажется, прекрасно {b}*ик*{/b} справляется без меня... Так почему я не должен этого делать?!"
    show harold 20
    harold "Я могу о себе позаботиться {b}*ик*{/b}... Мне не нужна ничья помощь..."
    show harold 19
    harold "Подожди... Что ты опять спрашиваешь???"
    show harold 18
    show player 11
    player_name "?!?"
    show player 12
    player_name "Ну, {b}Мия{/b} и {b}Хелен{/b} не видели вас несколько дней... Они просто беспокоятся о вас..."
    player_name "...И я сказал, что постараюсь выяснить, все ли с вами в порядке."
    player_name "Даже ваши коллеги на работе волнуются."
    show player 10
    player_name "Я думаю, что многие люди в вашей жизни заботятся о вас!"
    show player 5
    show harold 19
    harold "Они?!"
    harold "Я {b}*ик*{/b}, эээ... Стой, как ты меня нашел?!"
    show harold 18
    show player 12
    player_name "Я поспрашивал на вашей работе..."
    player_name "...И я увидел старую фотографию вас и {b}Хелен{/b} на вашем столе."
    player_name "Когда вы двое проводили здесь время."
    show player 5
    show harold 27
    harold "..."
    show harold 28
    harold "*вздыхая*"
    show harold 20
    harold "Я чувствую, что все было {b}*ик*{/b}... намного проще, когда-то..."
    harold "Я был счастлив... и чувствовал себя самим собой, не притворяясь тем, кем я не являюсь, понимаешь?"
    harold "Я даже себя больше не узнаю..."
    show harold 18
    show player 10
    player_name "Почему нельзя все вернуть?"
    show player 5
    show harold 19
    harold "Что {b}*ик*{/b}... ты имеешь в виду?"
    show harold 18
    show player 10
    player_name "Ты перестал быть собой... Может в этом и проблема!"
    show player 5
    show harold 28
    harold "..."
    show harold 20
    harold "Может ты прав..."
    show harold 19
    harold "...Но {b}Хелен{/b} тоже не такая, какой была раньше."
    show harold 18
    show player 14
    player_name "Я думаю, она тоже может измениться!"
    player_name "Дайте ей хоть один шанс..."
    show player 13
    show harold 19
    harold "Должен сказать, вы проделали большую детективную работу, разыскивая меня..."
    harold "...И я ценю, что ты заботишься о моей семье."
    show harold 18
    show player 10
    player_name "Я просто хочу, чтобы вы снова были счастливы."
    show player 5
    show harold 27
    harold "..."
    show harold 20
    harold "Я должен {b}*ик*{/b} вернуться в участок и протрезветь..."
    harold "...Потом я позвоню домой."
    show harold 19
    harold "Увидимся позже, малыш!"
    show harold 18
    show player 36 with dissolve
    player_name "Будьте осторожнее, {b}Гарольд{/b}!"
    show player 13
    hide harold
    with dissolve
    pause
    show player 12
    player_name "(Ну, это было... интересно...)"
    player_name "( Я должна сказать {b}Мие{/b} что нашла его, и он в порядке... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
