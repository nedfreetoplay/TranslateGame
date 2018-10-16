label forest_first_visit:
    scene expression game.timer.image("forest{}_b")
    show player 43 with dissolve
    player_name "Вау!"
    player_name "( Я ни когда не был в лесу раньше... )"
    player_name "( Тут так... спокойно... )"
    return

label forest_anna_missing_pup_started_dark:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( Слишком темно, чтобы искать {b}Авесомо{/b}. )"
    hide player with dissolve
    return

label forest_anna_missing_pup_started_have_cookies:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( Посмотрим, смогу ли я найти эту собаку. )"
    scene forest_closeup
    show player 239 at left
    with dissolve
    player_name "( Теперь... )"
    show player 240
    player_name "( ...Я мог бы его заманить... )"
    show player 245 at Position(xpos=8)
    player_name "( ...с помощью {b}этого{/b}! )"
    show player 246 at left
    pause
    show player 1 with dissolve
    player_name "( Посмотрим, выйдет ли он. )"
    show player 31
    player_name "( Он должен быть где-то здесь... )"
    hide player with dissolve
    return

label forest_anna_missing_pup_started_no_cookies:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( Я должен найти {b}печенье{/b} чтобы заманить {b}Авесомо{/b} . )"
    hide player with dissolve
    return

label forest_okita_get_ingredients:
    scene expression game.timer.image("forest{}_b")
    show player 2 with dissolve
    player_name "Тааак, {b}грибы{/b} должны быть где-то здесь."
    player_name "... Ещё надо найти {b}Жабу{/b} возлеводы, и {b}цветок{/b} в пещере."
    hide player with dissolve
    return

label forest_dewitt_make_new_flute:
    scene expression game.timer.image("forest{}_b")
    show player 32 with dissolve
    player_name "Что-то я не вижу падающих ветвей."
    player_name "Надо посмотреть где-то в другом месте."
    hide player with dissolve
    return

label awesomo_dialogue_intro:
    scene expression game.timer.image("forest{}_b")
    show player 177 with dissolve
    player_name "Привет, малыш..."

    player_name "Что ты здесь делаешь?"
    awesomo "Гаф!"
    player_name "ты заставил всех волноваться из-за тебя!"
    awesomo "Гаф!"
    player_name "Ты забавная собачка..."
    return

label awesomo_dialogue_give_cookie:
    scene expression game.timer.image("forest{}_b")
    player_name "Хочешь печенье?"
    show player 178 at Position(xpos=517)
    player_name "Вот так..."
    show player 179 with hpunch
    player_name "!!!"
    show player 180
    player_name "Боже мой!"
    player_name "Кто то проголодался..."
    show player 181
    player_name "Хмм..."
    show player 182
    player_name "Ты мне нравишься!"
    awesomo "Гаф!"
    return

label awesomo_dialogue_check_name_tag_pre:
    scene expression game.timer.image("forest{}_b")
    show player 177
    player_name "Посмотрим, ты ли это, кого я ищу..."
    show awesomo_tag zorder 2 with dissolve
    player_name "{b}Авесомо{/b}... Ага! Должно быть это, ты!"
    hide awesomo_tag with dissolve
    return

label awesomo_dialogue_check_name_tag_after:
    scene expression game.timer.image("forest{}_b")
    player_name "Давай вернем тебя хозяйке."
    player_name "Она волнуется из-за тебя..."
    awesomo "Гаф!"
    player_name "Ха-ха! Хорошо, тогда пойдем..."
    hide player with dissolve
    return


label dirt_pile:
    if player.has_item("shovel"):
        call expression game.dialog_select("forest_dirt_pile_have_shovel_intro")
        menu:
            "Надо копать лопатой." if player.has_item("shovel"):
                call expression game.dialog_select("forest_dirt_pile_have_shovel_dig")
                call screen forest_worms
            "Оставить это.":

                call expression game.dialog_select("forest_dirt_pile_have_shovel_leave")
    else:

        call expression game.dialog_select("forest_dirt_pile_no_shovel")
    $ game.main()

label forest_dirt_pile_have_shovel_intro:
    scene location_forest_dirt1
    player_name "( В этом пятне грязи есть что-то странное... )"
    player_name "( Кажется, что что-то движется под ним. )"
    player_name "( Может быть, я мог бы выкопать его? )"
    return

label forest_dirt_pile_have_shovel_dig:
    player_name "( Посмотрим, что там... )"
    scene location_forest_dirt2
    pause
    scene location_forest_dirt3
    player_name "{b}Черви{/b}?!"
    player_name "( Говорят из этого делают {b}приманку для рыбалки{/b}. )"
    player_name "( Может быть, я продолжу позже... )"
    return

label forest_dirt_pile_have_shovel_leave:
    player_name "( Хотяяя... )"
    player_name "( Возможно я должен оставить их в покое... )"
    return

label forest_dirt_pile_no_shovel:
    scene location_forest_dirt1
    player_name "( Есть кое-что странное в этой куче земли... )"
    player_name "( Такое ощущение будто что то двигается под ней. )"
    player_name "( Мне нужно найти {b}лопату{/b} чтобы выкопать это. )"
    return

label mushroom:
    call expression game.dialog_select("forest_mushroom_intro")
    if M_okita.is_state(S_okita_get_ingredients):
        call expression game.dialog_select("forest_mushroom_okita_get_ingredients")

    if M_aqua.is_state(S_aqua_seasucc_mushroom):
        call expression game.dialog_select("forest_mushroom_aqua_seasucc_mushroom")

    call expression game.dialog_select("forest_mushroom_take_mushroom")
    $ player.get_item("mushroom")
    $ game.main()

label forest_mushroom_intro:
    scene expression game.timer.image("forest{}_b")
    show player 498 with dissolve
    return

label forest_mushroom_okita_get_ingredients:
    player_name "Что ж, это определенно...Член."
    return

label forest_mushroom_aqua_seasucc_mushroom:
    player_name "Эти грибы похожи на те о которых {b}Аква{/b} рассказывала."
    player_name "Надо собрать, и отнести их {b}МореСоку{/b}..."
    return

label forest_mushroom_take_mushroom:
    show expression "boxes/popup_item_mushroom1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_mushroom1.png" with dissolve
    return

label altar:
    if M_aqua.is_set("altar pass"):
        scene expression game.timer.image("location_forest_puzzle_day{}")
        pause
        $ game.main()

    call expression game.dialog_select("altar_intro_pre")
    if not game.timer.is_dark():
        call expression game.dialog_select("altar_intro_day")
    else:

        call expression game.dialog_select("altar_intro_night")
        $ game.timer.tick()
        label altar_puzzle:
            call screen altar_puzzle
            if piecelist[9] == [162,143] and piecelist[18] == [382,20] and piecelist[16] == [600,139] and piecelist[14] == [383,263] and piecelist[10] == [163,385] and piecelist[12] == [603,387] and piecelist[20] == [384,516]:
                call screen altar_puzzle_finish
            jump expression game.dialog_select("altar_puzzle")
    $ game.main()

label altar_intro_pre:
    scene expression game.timer.image("forest_altar{}")
    with fade
    show text "Странное каменое строение стоит в середине леса." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Это выглядит старинным!Полностью покрытым мхом..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    if not game.timer.is_dark():
        show text "...а вот и {b}солнечный свет{/b} светит прямо на него." at Position (xpos= 512, ypos= 700) with dissolve
    else:
        show text "...а вот и {b}солнечный свет{/b} светит прямо на него." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Это должно быть то что я ищу." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    return

label altar_intro_day:
    scene location_forest_puzzle_day
    player_name "Хмм..."
    player_name "Это похоже на алтарь, как на цкрковном колоколе"
    player_name "...Но что то не так. Я в тупике."
    player_name "Так, какие были ключи?"
    player_name "Каменный алтарь, среди деревьев, и {b}луна{/b} освещает его."
    player_name "Над этим надо подумать."
    return

label altar_intro_night:
    scene location_forest_puzzle_night_closed
    player_name "Что то странное."
    player_name "Кажется это лунный свет светит на алтарь."
    player_name "Эти символы должны быть важными, и похоже, я могу их перемещать, чтобы сложить картинку..."
    player_name "Похоже на головоломку."
    return

label altar_puzzle_finish:
    call expression game.dialog_select("altar_puzzle_finish_dialogue")
    $ player.get_item("treasure_map")
    $ M_aqua.trigger(T_aqua_altar_puzzle_solve)
    $ game.main()

label altar_puzzle_finish_dialogue:
    scene expression "location_forest_puzzle_night"
    show expression "objects/object_map_01.png" at Position(xalign = 0.473, yalign = 0.44)
    with None
    show popup_item_map1 at truecenter with dissolve
    pause
    hide popup_item_map1 with dissolve
    return

label altar_puzzle_leave:
    scene expression game.timer.image("forest{}_b")
    show player 12 with dissolve
    player_name "Эх... Может есть что то, что подскажет как решить эту загадку."
    if not player.has_item("scroll"):
        player_name "Я мог бы ещё раз {b}взглянуть на церковный колокол{/b}, не пропустил ли я что- нибудь."
    else:
        player_name "Возможно, {b}свиток который я нашел в дереве{/b} содержит детали этой головоломки."
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
