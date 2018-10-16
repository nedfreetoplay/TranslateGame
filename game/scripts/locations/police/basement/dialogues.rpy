label police_basement_roxxy_ask_earl_release:
    scene police_lobby_b
    show player 12 with dissolve
    player_name "Нужно найти полицейского, чтобы узнать где мама {b}Рокси{/b}."
    hide player with dissolve
    return

label police_basement_first_visit:
    scene police_basement_b
    pause .4
    scene police_c_3
    show player 1
    with dissolve
    player_name "( Это должно быть тот самый \"обезьянник\" о котором говорят люди... )"
    hide player with dissolve
    return

label police_basement_mia_clues_summary:
    scene police_basement_b
    show player 35 with dissolve
    player_name "( Окей, Гарольд сейчас катается на машине по городу... )"
    player_name "( ...И он пьян. )"
    show player 12
    player_name "Хмм..."
    player_name "( Мне нужно больше {b}улик{/b}. )"
    player_name "( Стоит проверить его {b}стол{/b}... )"
    hide player with dissolve
    return

label police_basement_mia_inmate_status:
    scene police_basement_empty_b
    show player 4 at Position (xoffset=6) with dissolve
    player_name "Хмм..."
    show player 12 with dissolve
    player_name "( Я нигде не вижу {b}Юми{/b}, может быть мне- )"
    "*крик*" with hpunch
    show player 11
    player_name "..."
    show player 10
    player_name "( Может быть мне проверить камеры?! )"
    hide player with dissolve
    return

label police_basement_mia_harold_backup:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( Мне нужно как можно быстрее найти {b}Гарольда{/b}! )"
    hide player with dissolve
    return

label inmate_transfer_block:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( Я слышу крики! )"
    player_name "( Я должен проверить, что происходит возле камер! )"
    hide player with dissolve
    $ game.main()

label police_cell_mia_inmate_status:
    scene police_cell_inside_fight1
    yum "Стой, стой!!!!"
    scene police_cell_inside_fight2
    crys "Гррр!!"
    scene police_cell_inside_fight1
    yum "...Давай!! Приведи подмогу!!"
    player_name "!!!"
    scene police_cell_inside_fight2
    player_name "Я позову {b}Гарольда{/b}!"
    scene police_cell_inside_fight1
    yum "Давай! Скорее!"
    return

label police_cell_mia_harold_backup:
    scene police_basement_empty_b
    show player 10 with dissolve
    player_name "( Нужно как можно скорее найти {b}Гарольда{/b}! )"
    hide player with dissolve
    return

label police_cell_mia_harold_to_the_rescue:
    scene police_cell_inside_cs1
    with fade
    show text "{b}Гарольд{/b} и я помчались на подмогу.\nКогда {b}Гарольд{/b} вбежал в камеру, он на секунду застыл...\n...Но он нашел в себе силы и бросился на помощь {b}Юми{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause

    scene police_cell_inside_cs2
    with fade
    show text "Кнутри камеры была {b}Кристал{/b}...\n...Мама {b}Рокси{/b}, широко известная своими проблемами с алгоголем.\nПосле того, как выпьет, она не прочь подраться..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause

    scene police_cell_inside_cs3
    with fade
    show text "{b}Гарольд{/b} поначалу не справлялся...\n...Но вскоре пришел в форму.\nХочу заметить, что он даже получил некоторое удовольствие от потасовки." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide police_cell_inside_cs1
    hide police_cell_inside_cs2
    hide police_cell_inside_cs3

    scene police_cell_c_02 with fade
    show harold 39 at Position (xpos=158)
    show yumi 5 at Position (xpos=855)
    harold "И чтобы НИ ЗВУКА!!"
    show harold 38
    show yumi 7
    yum "..."
    show harold 37
    harold "Ты в порядке?"
    show harold 36
    show yumi 6
    yum "Да, я просто... я никогда тебя таким не видела."
    show yumi 5
    show harold 37
    harold "Оу, ну просто, понимаешь... Некоторые люди могут вывести меня из себя..."
    show harold 36
    show yumi 6
    yum "Нет, в смысле... Ты со всем этим справился."
    yum "Это очень здорово! Я никогда не видела эту сторону тебя."
    show yumi 5
    show harold 37
    harold "Ну, знаешь, я немного скучал. По потасовкам."
    show harold 36
    show yumi 6
    yum "Спасибо, что прикрыл..."
    show yumi 5
    show harold 37
    harold "Да ладно тебе. Я сделаю всё для моего напарника!"
    show harold 36
    show yumi 6
    yum "Гхх! Мне нужно быть осторожней..."
    yum "...это было глупо, любой с этим согласится..."
    show yumi 5
    show harold 37
    harold "Ну, {b}Юми{/b}..."
    harold "Я бы на твоем месте не волновался..."
    show harold 42 at Position (xoffset=32) with dissolve
    pause
    show harold 43 at Position (xpos=195) with dissolve
    pause
    scene police_cell_inside_zoom
    pause
    scene police_cell_inside_splash with flash
    pause
    scene police_cell_c_02
    show harold 41 at Position (xpos=158)
    show yumi 7 at Position (xpos=855)
    with fade
    harold "...потому что я обо всём позабочусь."
    harold "А теперь пойдем отсюда!"
    hide harold
    hide yumi
    with dissolve
    scene black with fade
    pause
    scene police_basement_empty_b
    show player 10f at right
    show harold 40 at left
    show yumi 5f at Position (xpos=550)
    with dissolve
    player_name "...{b}Гарольд{/b}?"
    show player 11f
    show harold 41
    harold "Эй, паренек."
    show harold 40
    show player 10f
    player_name "Ты в порядке? Твоя футболка порвана."
    show player 11f
    show harold 41
    harold "Всё в порядке, просто царапина."
    show harold 40
    show player 12f
    player_name "Похоже вашему напрнику нехило досталось..."
    show player 11f
    show yumi 6f
    yum "Ага... Даже не хочу знать, что с моей причёской."
    show yumi 5 with dissolve
    show harold 41
    harold "Если честно, мне нравится твои волосы сейчас. Ходи пока так."
    show player 13f
    show harold 40
    show yumi 7
    yum "..."
    show harold 41
    harold "Как насчёт поездки?"
    show harold 40
    show yumi 8
    yum "В смысле, прямо сейчас?!"
    show yumi 9
    show harold 41
    harold "Ну да, погода отличная... и я бы выпил чего-нибудь."
    show harold 40
    show yumi 8
    yum "Хаха. Хорошо. Если ты настаиваешь."
    show yumi 9
    show harold 41
    harold "Иди в машину, я скоро буду."
    show harold 40
    hide yumi with dissolve
    show player 14f
    player_name "Вам наверное пора."
    show player 13f
    show harold 41
    harold "Постой..."
    show harold 40
    show player 11f
    player_name "..."
    show harold 41
    harold "Спасибо за твою...помощь."
    show harold 40
    show player 14f
    player_name "Оу, я... Да пустяки, сэр."
    show player 13f
    show harold 41
    harold "Увидимся, паренек!"
    hide harold
    hide player
    with dissolve
    return

label police_cell_empty:
    scene police_cell
    show xtra 13 zorder 1 at left
    show player 10f zorder 2
    with dissolve
    player_name "( Не хотел бы я оказаться здесь. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
