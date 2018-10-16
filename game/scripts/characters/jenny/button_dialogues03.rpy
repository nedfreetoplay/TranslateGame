label jenny_dialogue_make_deal_alright_repeat:
    show player 12 at left
    show jenny 82 at Position(xpos=937)
    player_name "Хорошо..."
    show player 41 at Position(xpos=38) with fastdissolve
    pause
    show player 11 at left
    show jenny 80 at Position(xpos=945)
    jen "Подожди: Я посчитаю это первым." with fastdissolve
    show jenny 14
    jen "Хмм..."
    $ player.spend_money(500)
    play audio coins2
    show player 1
    show jenny 12 at Position(xpos=937)
    jen "Все нормально.Все здесь." with fastdissolve
    show jenny 10
    show player 21
    player_name "Итак...точно так же, как прошлый раз?"
    show player 11
    show jenny 7 at right
    jen "Да, НЕ трогать без моего разрешения!"
    show player 21
    show jenny 8
    player_name "Хорошо..."
    show jenny 161 at Position(xpos = 943) with fastdissolve
    pause
    show jenny 162 with fastdissolve
    pause
    show jenny 91 at right with fastdissolve
    show player 1
    jen "Вы можешь потрогать её одной рукой..."
    hide player
    show jenny 92
    with fastdissolve
    pause
    show jenny 94 with fastdissolve
    pause
    show jenny 93_94
    pause 8
    show jenny 95_94
    pause 8
    show jenny 95
    jen "Почему ты так сжимаешь мой сосок?"
    show jenny 94
    jen "Ты не можешь просто потрогать его нормально?"
    show jenny 95
    pause
    show jenny 96
    jen "Хахх..."
    return

label jenny_dialogue_make_deal_continue:
    show jenny 93_94
    pause 8
    show jenny 95_94
    pause 8
    show jenny 95
    pause
    show jenny 96
    jen "Хахх..."
    return

label jenny_dialogue_make_deal_suck_stat_fail:
    show jenny 97 at Position(xpos=1008) with fastdissolve
    pause
    show jenny 98
    jen "[dex_warn]Какого хрена?!" with hpunch
    show jenny 102
    show player 5 at left
    with dissolve
    jen "[dex_warn] Я никогда не говорила что ты можешь их {b}СОСАТЬ{/b}, ты идиотина!"
    show jenny 103
    show player 10
    player_name "Прости!"
    player_name "Я думал, что все в порядке!"
    show jenny 102
    show player 5
    jen "Я сказала тебе, только РУКОЙ!!!"
    jen "Вали из моей комнаты, ты изврщенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_suck_stat_pass:
    show jenny 99 at Position(xpos=1008) with hpunch
    jen "Аххх!!"
    show jenny 100
    jen "Что ты ДЕЛАЕШЬ?!"
    show jenny 99_100_101
    pause 8
    show jenny 101
    return

label jenny_dialogue_make_deal_suck_continue:
    show jenny 99_100_101
    pause 8
    show jenny 101
    return

label jenny_dialogue_make_deal_suck_stop:
    show jenny 98 at Position(xpos=1008)
    jen "Что за хуйня?!" with hpunch
    show jenny 102
    show player 5 at left
    with dissolve
    jen "Я никогда не говорила что ты можешь их ПОСОСАТЬ! Ты кретин!!"
    show player 10
    show jenny 103
    player_name "Извини!"
    player_name "Я думал, что все в порядке!"
    show jenny 102
    show player 5
    jen "Мне- мне не понравилось, Понял?!Я просто притворялась!!"
    jen "Я позволил тебе ЗАЙТИ слишком далеко на этот раз..."
    jen "Выметайся из моей комнаты, извращуга!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_stop:
    show jenny 91 at right
    show player 1 at left
    with fastdissolve
    jen "Доволен?"
    show jenny 89
    show player 21
    player_name "Да... Спасибо."
    show player 1
    show jenny 90
    jen "Нет... Спасибо ТЕБЕ, {b}[firstname]{/b}!"
    jen "Заходи в любое время. Если ты хочешь большего... Ты знаешь сделку."
    show player 21
    show jenny 89
    player_name "Хорошо"
    show player 11
    show jenny 91
    jen "А теперь убирайся из моей комнаты, извращенец!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_not_yet:
    show player 12
    show jenny 10
    player_name "Вообще-то, забей."
    player_name "Мне нужно подумать еще немного."
    show player 11
    show jenny 7 at right
    jen "А теперь убирайся из моей комнаты, изврат!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_make_deal_not_enough:
    show player 10
    show jenny 10 at Position(xpos=937)
    player_name "У меня нет так много денег прямо сейчас...."
    show player 11
    show jenny 9
    jen "Ты банкрот?! Это так грустно..."
    show player 14
    show jenny 10
    player_name "Хотя, они скоро у меня появятся."
    show player 5
    show jenny 9
    jen "Агх... Тогда,возвращайся ко мне, когда у тебя будут деньги."
    jen "А теперь выметайся из моей комнаты, изврат!"
    hide player
    hide jenny
    with dissolve
    return

label jenny_dialogue_cam_show_pre:
    show player 2
    show jenny 11 at Position(xpos=937)
    player_name "Я тебе нужен... для следущего {b}Видео шоу{/b}?"
    show player 1
    show jenny 12
    jen "Кто то у нас {b}возбудился{/b}."
    jen "Ты хочешь почувствовать мою мокрую киску обвивающейся вокруг твого члена, ммм?"
    show player 13
    show jenny 11
    player_name "..."
    show player 21
    player_name "Ну, я думаю , если тебе нужна моя помощь..."
    show player 1
    show jenny 19 at right
    jen "Хорошо, подожди здесь, ты маленький извращенец."
    jen "Дай я возьму мои {b}подставки{/b}, и тогда я объясню, что надо делать."
    scene black with fade
    return

label jenny_dialogue_cam_show_pre_inside:
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 1 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Агх... эта штука так напряженна!"
    show player 21
    show jenny 167
    player_name "Я думаю, что это выглядит хорошо..."
    show player 11
    show jenny 166
    jen "Хватит твоей дешевой лести."
    show jenny 167
    player_name "..."
    show jenny 109
    jen "Итак... ты помнишь, что я сказала тебе, что кончать внутрь-плохо?"
    jen "Оказывается, что мои поклонники ЛЮБЯТ {b}Кремовый торт{/b}.Я получила абсолютную ТОННУ новых подписчиков из-за этого."
    show jenny 108
    show player 21
    player_name "Подожди...Что?"
    show player 1
    show jenny 166
    jen "Я говорю, что ты можешь продолжать это делать, ты придурок!Я не против!"
    show player 21
    show jenny 167
    player_name "Охх..."
    show jenny 166
    show player 11
    jen "Сейчас, просто сядь на мою кравать, и ничего не говори, пока я настраиваю видео шоу...."
    jen "Просто расслабься, держи свой красивый и твердый член, и дай мне знать когда ты вот-вот кончишь."
    jen "Понял, идиот?"
    show jenny 109
    jen "Мы должны поддерживать это прикрытие Парня, пока мы на камере."
    show jenny 108
    show player 21
    player_name "Хорошо..."
    return

label jenny_dialogue_cam_show_pre_outside:
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 1 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Агх... эта штука так напряженна!"
    show player 21
    show jenny 167
    player_name "Я думаю, что это выглядит хорошо..."
    show player 11
    show jenny 166
    jen "Хватит твоей дешевой лести."
    show jenny 166
    show player 11
    jen "Сейчас, просто сядь на мою кравать, и ничего не говори, пока я настраиваю видео шоу..."
    jen "Просто расслабься, держи свой красивый и твердый член, и дай мне знать когда ты вот-вот кончишь."
    jen "Понял, кретин?"
    show jenny 109
    jen "они должны думать, что ты мой парень."
    show jenny 108
    show player 21
    player_name "Хорошо..."
    return

label jenny_dialogue_cam_show_pre_after:
    scene jenny_webcam2
    show jenny 151 zorder 2 at Position(xpos=407,ypos=748)
    show jenny_cheer1 zorder 3 at Position(xpos=439,ypos=724)
    show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
    show xtra 20 zorder 4 at left
    with fade
    jen "Отлично, Мы в прямом эфире!"
    show jenny 155
    jen "Прииивет ребята!"
    show jenny 151
    jen "Извините, что заставила вас ждать! Я должна была сходить за своим парнем!"
    jen "Он был очень плохим мальчиком, и теперь я должен преподать ему урок!"
    jen "Давайте начинать,что ли?"
    hide jenny
    hide jenny_cheer1
    show jennysex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
    show playersex 116b
    with fastdissolve
    jen "Просто нудо сделать несколько вещей..."
    hide jennysex
    show jennysex 104 zorder 1 at Position(xpos=122,ypos=540)
    show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
    with fastdissolve
    jen "Позвольте мне сначала снять эту юбку..."
    show jennysex 105 at Position(xpos=144,ypos=544) with fastdissolve
    pause
    show jennysex 106 at Position(xpos=170,ypos=542) with fastdissolve
    jen "Теперь, давайте используем их, чтобы убедиться, что он никуда не сбежим, в то время как я буду ебать его до потери сознания..."
    show jennysex 106b
    show playersex 120
    player_name "Ты же на самом деле не собираешься-"
    show jennysex 107 zorder 2 at Position(xpos=300,ypos=542)
    show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
    with fastdissolve
    pause
    show playersex 125
    show jennysex 109 at Position(xpos=357,ypos=620)
    with fastdissolve
    jen "Что вы скажете ребята? Должны ли мы узнать, что скрывается под его шортами?"
    show jennysex 108
    player_name "..."
    show jennysex 111 at Position(xpos=375,ypos=634) with fastdissolve
    jen "Ой, вау..."
    show jennysex 112 at Position(xpos=374,ypos=674)
    show playersex 127
    jen "Вы посмотрите на этот хороший, толстый, длинный член..." with vpunch
    show jennysex 113 with fastdissolve
    jen "Давайте сделаем это красиво и усердно."
    show jennysex 115b with fastdissolve
    pause
    show jennysex 114b_115b
    pause 8
    show jennysex 114
    jen "Интересно, поместится ли он в меня..."
    show jennysex 115b
    player_name "!!!"
    show playersex 126
    player_name "Подожди... Ты принимаешь таблетки, верно?"
    show jennysex 110b at Position(xpos=423,ypos=674)
    show playersex 127b
    jen "Шшшшш!!!" with hpunch
    jen "Тебе не нужно беспокоиться об этом!!"
    jen "Просто делай то, что делал в прошлый раз, и все будет хорошо!"
    show jennysex 114 at Position(xpos=374,ypos=674)
    show playersex 127
    with fastdissolve
    jen "Извините за это, ребята!"
    show jennysex 115
    jen "Мой парень просто... стесняется."
    show jennysex 114
    jen "Теперь, давайте дадим вам то, чего вы все так долго ждали..."
    show jennysex 116 at right with dissolve
    pause
    show jennysex 119b at Position(xpos = 939, ypos = 674) with fastdissolve
    jen "О, ДААА!!"
    show jennysex 117b with fastdissolve
    jen "Он так... {b}глубоко{/b}!!"
    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
    pause 8
    show jennysex 117b
    jen "Его член намного лучше, чем любая из моих игрушек..."
    show jennysex 118b
    jen "Он действительно растягивает меня..."
    show jennysex 119
    pause
    show jennysex 120
    pause
    show jennysex 121
    pause
    return

label sis_cheerleader_fuck_looprep:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not sis_cheerleader_sex2_menu:
                show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
            else:

                show expression AnimatedImage("jennysex", [123,124,125,126,127], M_jenny) as jennysex at Position(xpos = 986, ypos = 768)
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_cheerleader_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if not sis_cheerleader_sex2_menu:
                $ pose_list = [117,118,119,120,121]
                $ xpos_list = [939]
                $ ypos_list = [674]
            else:

                $ pose_list = [123,124,125,126,127]
                $ xpos_list = [986]
                $ ypos_list = [768]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex at Position(xpos = xpos_list[0],ypos = ypos_list[0])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_cheerleader_hscene_dialog")
        $ animcounter += 1
    call screen sis_cheerleader_sex_options

label jenny_cheerleader_hscene_dialog:
    if animcounter == 1:
        jen "Ахххх!!!{p=1}{nw}"

    elif animcounter == 3:
        jen "Ох!!!{p=1}{nw}"
        player_name "Ммммм...{p=1}{nw}"
    return

label sis_cheerleader_fuck_cum_outside:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_manual")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_outside_after")
    if store._in_replay == None and sister.completed(sis_final2):
        call expression game.dialog_select("sis_cheerleader_fuck_after_repeat")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_after_initial")
    $ renpy.end_replay()
    $ sis_final_cum = "Outside"
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_outside_animation:
    jen "( Я чувствую его член... )"
    jen "( ... он пульсирует, как сумасшедший... )"
    jen "( ... он вот-вот кончит?! )"
    pause
    show jennysex 130b
    with vpunch
    return

label sis_cheerleader_fuck_cum_outside_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    jen "( Я чувствую его член... )"
    show jennysex 118
    jen "( ... он пульсирует, как сумасшедший... )"
    show jennysex 119
    jen "( ... он скоро кончит?! )"
    show jennysex 120
    pause
    show jennysex 130b at Position(xpos=939,ypos=674)
    with vpunch
    return

label sis_cheerleader_fuck_cum_outside_after:
    jen "Ахх!!"
    show jennysex 130
    show white zorder 5
    show playersexc 129 zorder 4 at Position(xpos=560,ypos=377)
    hide white with dissolve
    pause
    show playersexc 130 at Position(xpos=609,ypos=423) with fastdissolve
    pause
    show jennysex 130b
    jen "Вау..."
    jen "Ребята вы видите мою зияющую киску?"
    jen "И вся эта горячая сперма бежит по моей спине..."
    jen "Я надеюсь что вам это понравилось ребята!"
    return

label sis_cheerleader_break_free_fail:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_break_free_fail_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_break_free_fail_manual")
    call screen sis_cheerleader_sex_options

label sis_cheerleader_break_free_fail_animation:
    player_name "[str_warn]( Эй, эти наручники не кажутся такими прочными... )"
    player_name "[str_warn]( Да брось... )"
    player_name "[str_warn]( Черт побери, я не могу освободиться. )"
    player_name "[str_warn]( Я недостаточно силен... )"
    return

label sis_cheerleader_break_free_fail_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    player_name "[str_warn]( Эй, эти наручники не кажутся такими прочными... )"
    show jennysex 118
    player_name "[str_warn]( Да ладно... )"
    show jennysex 119
    player_name "[str_warn](Черт побери, я не могу освободиться. )"
    show jennysex 120
    player_name "[str_warn]( Я недостаточно силен... )"
    show jennysex 121
    return

label sis_cheerleader_break_free_pass:
    $ sis_cheerleader_sex2_menu = True
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_break_free_pass_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_break_free_pass_manual")
    call expression game.dialog_select("sis_cheerleader_break_free_pass_after")
    jump expression game.dialog_select("sis_cheerleader_fuck_looprep")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
