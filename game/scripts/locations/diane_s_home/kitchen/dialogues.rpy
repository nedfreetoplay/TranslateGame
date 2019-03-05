label dianes_kitchen_diane_look_in_kitchen:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    player_name "( !!! )" with hpunch
    pause
    dia "Нгххх..."
    player_name "( {b}Диана{/b} ... )"
    player_name "( Она... )"
    player_name "( ... Это что, огурец? )"
    pause
    dia "Ммм, вот так!"
    $ M_diane.set("sex speed",0.3)
    show diane_masturbate 1_2
    player_name "( Это... )"
    dia "Трахни меня сильнее, жеребец!"
    player_name "( Интересно, кого она воображает? )"
    pause
    player_name "( Я должен убраться отсюда, пока она меня не увидела. )"
    pause
    hide diane_masturbate with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["01_unlocked"] = True
    $ renpy.end_replay()
    return

label dianes_kitchen_diane_clean_garden_report:
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 5f with dissolve
    player_name "..."
    show player 10f
    player_name "... Привет?!"
    show player 22f
    dia "ИИИКККК!!!" with hpunch
    player_name "!!!"
    show player 23f
    player_name "Диана?!"
    show player 22f
    dia "{b}[firstname]{/b}! Помоги!!!"
    show player 23f
    player_name "Где ты?!"
    show player 22f
    dia "АААААААА!!!" with hpunch
    show player 23f
    player_name "Похоже, она наверху!"
    hide player with dissolve
    scene black with dissolve
    scene expression "backgrounds/location_diane_bedroom_closeup.jpg"
    show diane b_pole a_empty f_pole_scream
    show player 11 at left
    with dissolve
    dia "ПОМОГИ!!!"
    show player 10
    player_name "{b}Диана{/b}?!"
    player_name "Что случил-"
    show player 11
    dia "M-MM-MM-МЫШЬ!"
    show player 12
    player_name "А, мышка?"
    show player 14
    player_name "Это то, что тебя так напугало?"
    show player 13
    dia "..."
    show player 14
    player_name "Где же она?"
    show player 13
    show diane b_pole_point f_pole_scared_talk_back with dissolve
    dia "Ш-шкаф!"
    show diane f_pole_scared
    show player 10
    player_name "Ты видела мышь в своем шкафу?"
    show diane b_pole with dissolve
    show player 14
    player_name "Я проверю."
    show diane f_pole_scared_talk_back
    show player 108f at right with dissolve
    player_name "Я не-"
    show player 670 with dissolve
    player_name "..."
    "{b}*стук*{/b}"
    show player 22 at left
    player_name "!!!" with hpunch
    show diane f_pole_scream
    dia "ИИИИКККК!!!"
    hide player
    show diane pickup
    player_name "ХРРГГГ!!!" with hpunch
    player_name "..."
    show diane pickup_scared
    dia "Это была та самая мышь?!"
    show diane pickup
    player_name "Я... Я не знаю..."
    show diane pickup_talk
    dia "Ненавижу мышей!"
    show diane pickup_laugh
    player_name "Хехе, ты постоянно имеешь дело с грязью и жуками, но мыши тебя пугают?"
    show diane pickup_talk
    dia "ДА!!!"
    show diane pickup_scared
    dia "Ты видел её?!"
    show diane pickup
    player_name "Эээ... Нет?"
    show diane pickup_talk
    dia "Я видела!"
    show diane pickup
    player_name "... Где?"
    show diane pickup_scared
    dia "ПРЯМО ТУТ!!"
    dia "Видишь хвост?!"
    show diane pickup
    player_name "..."
    player_name "Я думаю, это шнурок от ботинок..."
    show diane pickup_talk
    dia "Что?! НЕТ!!!"
    show diane pickup_scared
    dia "Это мышь!"
    player_name "..."
    show diane pickup
    player_name "Мне трудно рассмотреть, когда ты сжимаешь мою голову..."
    show diane pickup_talk
    dia "Хмм?"
    dia "О, прости, {b}[firstname]{/b}!"
    show diane b_pole a_empty f_pole_scared
    show player 17 at left
    with dissolve
    player_name "Хех, все в порядке."
    show player 14
    player_name "А теперь позволь мне позаботиться об этом шнурке..."
    hide player with dissolve
    show diane f_pole_scared_talk_back
    dia "Говорю тебе, это мышь!"
    show diane f_pole_scream
    dia "Ух, будь осторожен, {b}[firstname]{/b}!!!"
    player_name "..."
    show diane f_pole_scared
    show player 682 at left with dissolve
    player_name "..."
    show player 683
    player_name "{b}*хм*{/b}"
    show player 682
    show diane f_pole_scared
    dia "..."
    show diane f_pole_scared_talk
    dia "Это шнурок от обуви."
    show diane f_pole_scared
    show player 683
    player_name "Хех, я же говорил тебе!"
    show player 682
    show diane b_lingerie a_lingerie_sides f_scared_talk
    with dissolve
    dia "Ты уверен, что там нет мыши?"
    show diane f_scared
    show player 683
    player_name "Конечно."
    show player 13 at left with dissolve
    show diane f_laugh
    dia "Фууу!"
    show diane f_scared_talk
    dia "У меня чуть инфаркт не случился..."
    show diane f_normal
    show player 14
    player_name "Да, я никогда не видел тебя такой взволнованной."
    player_name " Теперь ты в порядке?"
    show player 13
    show diane f_normal_talk
    dia "Да, наверно."
    show diane f_normal
    dia "..."
    show player 17
    player_name "... Не могу поверить, что ты кричала на шнурки!"
    player_name "Хахаха!"
    show diane f_laugh
    dia "О, заткнись!"
    show diane f_normal
    show player 13
    show diane f_surprised_front
    pause
    show diane f_surprised_front_talk a_lingerie_cover with dissolve
    dia "... Я... голая..."
    show diane f_shamed
    show player 10
    player_name "Ну, не совсем голая..."
    show player 5
    show diane f_shamed_talk
    dia "С таким же успехом я могла бы."
    dia "Прости, {b}[firstname]{/b}."
    dia "Мне неловко."
    show diane f_shamed
    show player 10
    player_name "Хмм?"
    player_name "Тут нечего стыдится..."
    show player 14
    player_name "Ты выглядишь потрясающе!"
    show player 13
    show diane a_lingerie_shock f_laugh at Position (yoffset=13) with dissolve
    dia "{b}[firstname]{/b}!!!"
    show diane f_smirk at Position (yoffset=13)
    show player 17
    player_name "Что? Ты делаешь."
    show player 13
    show diane f_smirk_talk a_lingerie_sides with dissolve
    dia "{b}Дебби{/b} закатила бы истерику, если бы узнала, что ты видишь меня такой."
    show diane f_smirk
    show player 14
    player_name "Ну, я не собираюсь ей говорить..."
    show player 13
    dia "..."
    show diane f_normal_talk
    dia "Ты правда думаешь, что я хорошо выгляжу?"
    show diane f_normal
    show player 14
    player_name "Конечно!"
    player_name "Ты прекрасна!"
    show player 13
    dia "..."
    hide player
    show diane lingerie_kiss
    with dissolve
    dia "Ты такой милый!"
    show player 13 at left
    show diane b_lingerie a_lingerie_sides f_smirk_talk
    with dissolve
    dia "Спасибо, красавчик!"
    show diane f_smirk
    player_name "..."
    show diane f_smirk_talk
    dia "Мне нужно закончить одеваться."
    dia "Хочешь пойти со мной и забрать {b}пестицид{/b}?"
    show diane f_smirk
    player_name "Да, хорошо."
    show diane f_laugh
    dia "Великолепно!"
    show diane f_smirk_talk
    dia "Тебе стоит подождать меня внизу."
    dia "Я буду через минуту или две."
    hide player
    hide diane
    with dissolve
    scene expression "backgrounds/location_diane_kitchen_closeup.jpg"
    show player 13f at right
    with dissolve
    player_name "( Ух ты, поверить не могу, что мне пришлось видеть {b}Диану{/b} в таком виде! )"
    player_name "( У нее такое прекрасное тело! )"
    show diane b_casual a_casual_sides f_smirk_talk at flip with dissolve
    dia "Готов ехать, жеребец?"
    show diane f_smirk
    show player 11f
    player_name "!!!"
    show player 14f
    player_name "Да..."
    player_name "Классный наряд!"
    show player 13f
    show diane f_laugh
    dia "Хех, спасибо!"
    show diane f_normal_talk
    dia "Мы должны найти {b}пестицид{/b} который нам нужен в {b}Consum-R{/b}."
    show diane f_normal
    show player 14f
    player_name "Хорошо, поехали."
    hide player
    hide diane
    with dissolve
    return

label dianes_kitchen_diane_mouse_attack_started:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "Блин. Её здесь тоже нет."
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
