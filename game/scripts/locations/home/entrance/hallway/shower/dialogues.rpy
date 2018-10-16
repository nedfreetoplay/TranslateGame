label shower_mom_sis_check:
    scene shower_cutscene1
    show text "Я бросился наверх, услышав проклятия {b}[jen_name]{/b}.\nСцена при входе была почти смешной. {b}[jen_name]{/b} была взволнована и выглядела как утонувшая крыса.\nОткрытая труба изливала воду повсюду и делала вокруг беспорядок." at Position(xpos=500, ypos=700)
    with dissolve
    $ renpy.pause()
    hide shower_cutscene1
    hide text
    scene shower2
    show player 11 at left
    show jenny 27 at right
    with dissolve
    jen "Ты как раз вовремя появился!"
    show player 10
    show jenny 26
    player_name "Как такое могло произойти?!"
    show player 11
    show jenny 27
    jen "Откуда мне об этом знать? По-твоему, я похож на водопроводчика?! Я всего лишь включил раковину!"
    show player 12
    show jenny 26
    player_name "Что мне прикажешь делать?"
    show player 11
    show jenny 27
    jen "Исправьте это, очевидно! В конце концов, ты здесь единственный мужчина!"
    show jenny 26
    show player 12
    player_name "Отлично! Я думаю, нужно {b}спустится вниз{/b} и посмотреть как выключается {b}водопроводный кран{/b}..."
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene shower2
    show jenny 27 at right
    show player 11 at left
    with dissolve
    jen "Вода все еще распыляется вокруг!"
    jen "Иди в {b}подвал{/b} и закрой водопроводный {b}кран{/b}!"
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_pipe_check:
    scene shower2
    show jenny 29 at Position (xpos=800)
    show player 11 at left
    with dissolve
    jen "Похоже, у тебя получилось. Вода остановилась."
    show player 12
    show jenny 26 at right
    player_name "Да, я выключил водяной клапан. Что дальше?"
    show player 5
    show jenny 27
    jen "О чем ты меня спрашиваешь? Я не знаю, заменить его или что-то?"
    show player 10
    show jenny 26
    player_name "Я никогда не работал над чем-то подобным!"
    show player 5
    show jenny 27
    jen "Ну, теперь ты живешь в доме с девушками, а это значит, что тебе нужно научиться исправлять такие вещи!"
    show player 10
    show jenny 26
    player_name "Окей! Окей! Я думаю, я пойду в {b}CONSUM-R{/b} и посмотрю, как получить {b}трубный ключ{/b}."
    show player 212
    player_name "..."
    show player
    show jenny 28
    $ renpy.pause()
    show jenny 27
    jen "..."
    jen "Ты хорошо все разглядел, маленький извращенец?!"
    show player 23
    show jenny 26
    player_name "Я не-"
    show player 22
    show jenny 41 at Position(xpos=0.9123,ypos=1.0000)
    jen "О, пожалуйста, думаешь, я не могу понять, когда кто-то пялится на мои сиськи?"
    player_name "..."
    jen "Что с тобой происходит?"
    show player 24
    show jenny 30
    player_name "Прсти, {b}[jen_name]{/b}. Я только-"
    show jenny 31
    jen "Ой, заткнись!"
    show player 25
    jen "Если собираешься пялиться, хотя бы будь мужиком!"
    jen "Отрицая это или оправдываясь, ты выглядишь слабаком."
    jen "Никто не хочет, чтобы его проверял бесхребетный маленький слабак!"
    show player 5
    player_name "..."
    show jenny 27 at right
    jen "Если бы ты поднялся сюда, чтобы разобраться с этой ситуацией с трубами раньше, возможно, я была бы в лучшем настроении."
    show jenny 41 at Position(xpos=0.9123,ypos=1.0000)
    jen "... Но с тех пор, как ты решил приятно провести время...."
    jen "Думаю, тебе стоит взять это..."
    show player 22
    show jenny 32
    $ renpy.pause()
    show jenny 33
    $ renpy.pause()
    show player 23
    show jenny 42 at right
    jen "...  чтобы постирать внизу для меня."
    player_name "( !!! )" with hpunch
    show player 21
    player_name "Ко-конечно..."
    show jenny 37
    show player 211
    jen "..."
    show jenny 38
    jen "Перестань пялиться и иди! Я не собираюсь весь день ждать ,пока ты {b}починишь эту трубу{/b}!"
    show player 22
    player_name "( !!! )"
    hide player with dissolve
    show jenny 36
    jen "Хех, я так и знала!"
    jen "У этого маленького неудачника есть кое-что для меня!"
    hide jenny with dissolve
    hide shower2
    return

label shower_mom_fix_pipe_no_wrench:
    scene shower2
    show player 11 at left
    if not game.timer.is_dark():
        show jenny 27 at right
        with dissolve
        jen "Ты наконец-то собираешься починить раковину?"
        jen "Поторопись уже!"
        hide jenny with dissolve
        show player 4
    with dissolve
    player_name "( Мне нужен {b}ключ{/b} ,чтобы починить сломанную трубу. )"
    hide player
    with dissolve
    return

label shower_mom_fix_pipe_wrench:
    show expression Cutscene("shower_cutscene2", "Как только я вернулся домой, я направился наверх, чтобы починить раковину в ванной.\nЯ заменил сломаную трубу на новую и затянул ее настолько, насколько смог. \nБыло немного странно, что {b}[deb_name]{/b} и {b}[jen_name]{/b} все время наблюдали за мной.\nК счастью для меня, ремонт прошел гладко...") as cutscene with dissolve
    pause
    hide cutscene
    hide text
    scene shower2
    show player 203f at right
    show jenny 11f at Position(xpos=0.3649,ypos=1.0000)
    show debbie 62f at left
    with dissolve
    deb "Вау!!"
    deb "Великолепная работа, {b}[firstname]{/b}!"
    show jenny 9f
    show debbie 61f
    jen "Закончил..."
    show jenny 11f
    show debbie 62f
    deb "Не хами, {b}[jen_name]{/b}. Было мило с его стороны исправить это для нас..."
    show player 2f
    show jenny 11f
    show debbie 61f
    player_name "Хех, никаких проблем."
    player_name "Я был счастлив сделать это."
    player_name "...Кроме того, {b}[jen_name]{/b} права. Исправлять подобные вещи теперь моя обязанность."
    show player 29f
    show jenny 10f
    show debbie 62f
    deb "Однажды ты осчастливишь девушку и будешь хорошем мужем!"
    show player 203f
    show jenny 9f
    show debbie 61f
    jen "Пфффф..."
    jen "Не говори так, он зазнается!"
    show player 16f
    show jenny 12f
    jen "В конце концов, он все еще слабак."
    show player 15f
    show jenny 11f
    show debbie 61f
    player_name "Я не слабак!"
    show player 16f
    show jenny 12f
    jen "Ха, какая разница, слабак!"
    show player 1f
    show jenny 11f
    show debbie 62f
    deb "... Не слушай ее, {b}[firstname]{/b}. Она дразнит тебя только потому, что считает милым."
    show jenny 9f
    show debbie 59f
    jen "... Ага!"
    show player 11f
    jen "... А сейчас вы двое можете выйти? Я весь день ждала, чтобы принять душ!"
    show jenny 10f
    show debbie 60f
    show player 1f
    deb "Пойдем, {b}[firstname]{/b}. Пока Принцесса не заразила нас своим дурным настроением."
    show jenny 9f
    show debbie 59f
    jen "Хех, \"Принцесса\" звучало как оскорбление..."
    hide debbie
    hide jenny
    hide player
    with dissolve
    return

label shower_mom_shower_peek_after:
    scene location_home_hallway_day
    show player 3
    player_name "( Тело {b}[deb_name]{/b} выглядит очень хорошо, но я не хочу подглядывать за ней слишком долго... )"
    player_name "( было бы очень неловко, если бы она меня поймала. )"
    hide player with dissolve
    return

label shower_mom_shower_peek:
    player_name "( !!! )"
    show debbie_shower 6a_6b_6c
    player_name "( {b}[deb_name]{/b} в душе! )"
    player_name "( Вау... )"
    player_name "( У нее такое прекрасное тело! )"
    player_name "( Не могу поверить, что она оставила дверь приоткрытой! "
    player_name "( Я могу видеть абсолютно все! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    player_name "..."
    scene shower06d
    player_name "( Мне лучше уйти, пока она меня не увидела. )"
    scene hallway
    show player 79 with dissolve
    player_name "Вау..."
    player_name "Не могу поверить, что живу с этой прекрасной женщиной!"
    player_name "... Жаль, что она видит меня, как ребенка моего {b}отца{/b}."
    show player 78 with dissolve
    player_name "( !!! )"
    show player 81
    player_name "Я лучше вернусь в свою комнату, пока никто меня не поймал..."
    hide player with dissolve
    return

label shower_mom_walk_in:
    player_name "( Потрясающе! )"
    show debbie_shower 6a_6b_6c
    pause
    player_name "( Интересно, ее грудь такая же мягкая, как ноги? )"
    player_name "( Они смотрятся... прекрасно! )"
    hide debbie_shower 6a_6b_6c
    scene shower06a
    pause
    scene shower06d
    player_name "(Интересно, что случится, если я просто войду туда? )"
    player_name "( Она, вероятно, рассердится, но что, если нет? )"
    show debbie_shower 6a_6b_6c
    player_name "( Я всегда могу притвориться, что не понял, что она в душе.... )"
    return

label shower_mom_walk_in_yes:
    player_name "( Я не могу сопротивляться... Я вхожу! )"
    hide debbie_shower 6a_6b_6c
    scene shower_closeup
    show player 5 at left
    show debbie 35b at right
    with dissolve
    deb "( !!! )"
    show player 29 with dissolve
    player_name "Упс!"
    show player 3
    show debbie 35c
    deb "Милый, что ты здесь делаешь?!!"
    show debbie 35
    deb "Я голая!"
    show debbie 34
    show player 42 at Position (xoffset=38) with dissolve
    player_name "Извени, {b}[deb_name]{/b}! Я не думал, что здесь кто-то есть!"
    deb "..."
    show debbie 35
    deb "...Ничего.."
    deb "Если тебе что-то нужно в ванной, просто постучи."
    deb "Я закончу через несколько минут, ладно?"
    show debbie 34
    show player 37 with dissolve
    player_name "Ладно..."
    show player 3 with dissolve
    show debbie 35
    deb "Теперь дай мне закончить, милый."
    show debbie 33
    deb "И закрой за собой дверь!"
    show debbie 32
    show player 29
    player_name "Закрою!"
    hide player with dissolve
    show debbie 35
    deb "Это из-за-"
    deb "..."
    deb "Поцелуев..."
    deb "Я должна быть более осторожной с ним."
    hide debbie with dissolve
    scene hallway
    show player 24 with dissolve
    player_name "( Тьфу... Это было неловко... )"
    player_name "( Почему я подумал, что это хорошая идея? )"
    pause
    show player 37 at Position (xoffset=41) with dissolve
    player_name "( Надеюсь, она не слишком злится на меня. )"
    hide player with dissolve
    return

label shower_mom_walk_in_no:
    player_name "Наверное, мне не стоит."
    player_name "Я не хочу, чтобы она расстраивалась."
    hide debbie_shower 6a_6b_6c
    return

label shower_mom_sex:
    show debbie_shower 6a_6b_6c
    return

label shower_mom_sex_walk_in_pre:
    scene shower_closeup
    with dissolve
    show debbie 35 at right
    show player 1 at left
    deb "О, {b}[firstname]{/b}... Я не ожидала, что ты так просто ворвешься!"
    show debbie 33
    deb "Хотя, теперь, когда ты здесь..."
    show debbie 36
    deb "Хочешь присоединиться ко мне, милый?"
    hide debbie
    hide player
    show debbies 37 with dissolve
    return

label shower_mom_sex_walk_in_after:
    scene shower_closeup
    show debbies 37_36
    pause 4.8
    show debbies 35
    player_name "Я люблю принимать душ с тобой, {b}[deb_name]{/b}"
    show debbies 76 with dissolve
    pause .1
    show debbies 41_76
    pause 4
    show debbies 42
    deb "Могу я помочь тебе опустить его?"
    show debbies 43
    deb "Так..."
    show debbies 44
    deb "Какие планы на сегодня?"
    show debbies 43
    deb "Что-нибудь веселое?"
    show debbies 72_71
    pause 4
    show debbies 45 with dissolve
    deb "Ты весь напряжен. Теперь все зависит от тебя, милый..."
    show debbies 73 with dissolve
    return

label shower_mom_sex_wash:
    player_name "На этот раз я хочу помыть тебя."
    show debbies 50 with dissolve
    deb "Давай, милый."
    show debbies 51
    pause 1
    show debbies 52_53_52_51
    pause 4.8
    show debbies 54
    player_name "Так приятно..."
    return

label shower_mom_sex_wash_handjob:
    show debbies 45 with dissolve
    pause .4
    show debbies 73_74
    pause 4
    show debbies 73
    player_name "{b}[deb_name]{/b}, я кончаю..."
    show debbies 47 at Position(xpos=526,ypos=768)
    player_name "Мммммммм!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=526,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=549,ypos=508)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Ммм, хороший мальчик."
    return

label shower_mom_sex_finger:
    player_name "Я еще не вымыл{b}везде{/b}..."
    show debbies 55 at Position(xpos=688,ypos=768) with dissolve
    pause .35
    show debbies 56_55
    pause 4
    deb "... Я почти добралась, милый..."
    show debbies 56
    deb "Я-Аааааа!!!"
    show debbies 50 at Position(xpos=498,ypos=768) with dissolve
    deb "Откуда ты всегда точно знаешь, где тереть?"
    show debbies 49
    player_name "Не знаю, просто чувствую, наверное?"
    show debbies 50
    return

label shower_mom_sex_blowjob:
    show debbies 111 with dissolve
    deb "Как насчет особого угощения?"
    show debbies 110
    player_name "Да, пожалуйста..."
    show debbies 112 at Position(xpos=512) with dissolve
    pause .3
    show debbies 113_114 at Position(xpos=513)
    pause 5
    show debbies 112 at Position(xpos=512)
    return

label shower_mom_sex_blowjob_loop:
    show debbies 113_114 at Position(xpos=513)
    pause 5
    show debbies 112 at Position(xpos=512)
    return

label shower_mom_sex_blowjob_cum_in_mouth:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "УУУУХХХХ!!!"
    deb "( !!! )"
    show white with dissolve
    hide white with dissolve
    pause
    show debbies 117 at Position(xpos=523) with dissolve
    deb "Ммммм!!!"
    show debbies 118 at Position(xpos=516)
    deb "{b}*глоток*{/b}"
    show debbies 115 at Position(xpos=531)
    deb "... О, так много!"
    show debbies 110 at Position(xpos=512)
    player_name "Прости, {b}[deb_name]{/b}."
    show debbies 111
    deb "Не извеняйся, милый."
    deb "Мне нравится этот вкус!"
    return

label shower_mom_sex_blowjob_cum_on_face:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "МММММММ!!!"
    deb "( !!! )"
    show white with dissolve
    show debbies 115 at Position(xpos=531)
    show playersex 74 at Position(xpos=530,ypos=519)
    hide white with dissolve
    pause
    show playersex 75 at Position(xpos=574,ypos=655)
    deb "Хехе, посмотри на беспорядок, который ты сделал на моем лице!"
    deb "... Я покрыта..."
    player_name "Прости, {b}[deb_name]{/b}."
    deb "Все в порядке!"
    deb "Мы в душе, поэтому его легко очистить!"
    deb "... Просто помогите мне вытащить это из моих волос."
    return

label shower_mom_sex_already_fingered:
    show debbies 49
    player_name "Могу я засунуть его внутрь?"
    show debbies 50
    deb "Милый, я только что пришла... Сейчас это будет слишком чувствительно..."
    deb "Я закончу своей рукой."
    return

label shower_mom_sex_fuck_pre:
    show debbies 49 with dissolve
    if randomizer() <= 33:
        player_name "{b}[deb_name]{/b}..."
        player_name "Могу я засунуть его внутрь тебя?"
        show debbies 50
        deb "Конечно, милый..."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        deb "О, я ждала этого весь день..."
    elif randomizer() <= 66:
        player_name "{b}[deb_name]{/b}, Я хочу сделать это с тобой."
        show debbies 50
        deb "О, милый..."
        deb "Ты ненасытен."
        deb "Держи мою ногу и дай мне этот большой член!"
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    else:
        player_name "{b}[deb_name]{/b}, я хочу тебя."
        show debbies 50
        deb "Я надеялся, что ты это скажешь."
        deb "Дай мне свой красивый член."
        show debbies 57 at Position(xpos=688,ypos=768) with dissolve
        pause
    show debbies 58 with dissolve
    deb "Аааах!"
    show debbies 59 with dissolve
    pause
    return

label mom_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("debbies", [59,60,61], M_mom) as debbies at Position(xpos = 688,ypos = 768)
            pause 5
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [59,60,61]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = 688,ypos = 768)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,2,3]:
                call expression game.dialog_select("debbie_shower_hscene_dialog")
        $ animcounter += 1
    call screen shower_mom_sex_options

label debbie_shower_hscene_dialog:
    if randomizer() <= 33:
        if animcounter == 1:
            deb "Аххххх!!!{p=1}{nw}"
            deb "Дай мне это, милый!{p=2}{nw}"
        elif animcounter == 3:
            deb "Кончи для меня!{p=2}{nw}"
    elif randomizer() <= 66:
        if animcounter == 1:
            deb "Ооооо!!{p=1}{nw}"
        elif animcounter == 2:
            deb "Милый! Глубже!{p=2}{nw}"
        elif animcounter == 3:
            player_name "{b}[deb_name]{/b}, я люблю тебя!{p=2}{nw}"
            deb "Я тебя тоже люблю!{p=2}{nw}"
    else:
        if animcounter == 2:
            player_name "Мне нравится, как твои сиськи подпрыгивают.{p=2}{nw}"
            deb "Да,а мне нравится твой огромный член!{p=2}{nw}"
        elif animcounter == 3:
            deb "Ааааа!!{p=1}{nw}"
            deb "Да, это то самое место!{p=2}{nw}"
    return

label mom_shower_sex_cum:
    call expression game.dialog_select("mom_shower_sex_cum_pre")
    $ cum = True
    call expression game.dialog_select("mom_shower_sex_cum_after")
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["07_unlocked"] = True
    jump expression game.dialog_select("mom_shower_end")

label mom_shower_sex_cum_pre:
    if randomizer() <= 33:
        player_name "Уххххх!"
    elif randomizer() <= 66:
        deb "Дай мне это, милый!"
        deb "Кончи глубоко в меня!"
    else:
        deb "АААААХХХХХ!"
    return

label mom_shower_sex_cum_after:
    show debbies 60
    show white zorder 4 with dissolve
    hide white with dissolve
    pause
    if randomizer() <= 50:
        player_name "Это было приятно..."

    show playersex 53 zorder 3 at Position(xpos=663,ypos=632)
    show debbies 57
    with dissolve
    if randomizer() <= 50:
        deb "Ты выпустил так много..."
        deb "Такой бардак."
        deb "Хорошо, что мы в душе..."
    else:
        deb "Охх!"
        deb "Боже, как мне нравится твой член!"
        player_name "Хехе, я почти уверен, что он чувствует то же самое ..."
        deb "Ха Ха Ха!"
        deb "Держи меня секундочку. Мои ноги немного шатаются после всего этого!"
    return

label mom_shower_end_dialogue:
    hide playersex
    hide debbies
    show debbies 34 at Position(xpos=498,ypos=768)
    with dissolve
    if randomizer() <= 50:
        deb "Это было весело, но мне действительно нужно было спуститься вниз и начать готовить обед."
        deb "Мы сделаем это снова, хорошо?"
        deb "Убедись, что{b}[jen_name]{/b} не увидит, как ты выходишь из ванной, хорошо?"
    else:
        deb "Надеюсь {b}[jen_name]{/b} не слышала нас..."
        show debbies 35
        player_name "Я сомневаюсь в этом. Душ шумит..."
        show debbies 34
        deb "... Да, наверное, я слишком сильно волнуюсь."
        deb "Я должна спуститься вниз и начать готовить обед..."
        deb "Принешь мне полотенце?"
        show debbies 35
        player_name "Конечно, {b}[deb_name]{/b}!"
    hide debbie_shower
    hide debbie
    hide debbies
    hide player
    with dissolve
    return

label mom_shower_end:
    call expression game.dialog_select("mom_shower_end_dialogue")
    $ renpy.end_replay()
    $ game.timer.tick()
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_mom_sex_leave:
    player_name "Наверное, мне не стоит."
    player_name "Я не хочу, чтобы она расстраивалась."
    return

label shower_sis_sex_pre:
    scene shower3 with None
    player_name "( {b}[jen_name]{/b} в душе... )"
    player_name "( ... и она меня еще не заметила? )"
    player_name "( Может быть, я... )"
    return

label shower_sis_sex_peep_after_cuddle:
    scene shower05a
    player_name "( ...Она снова оставила дверь открытой ... )"
    scene shower05b
    player_name "( ...Как будто она хочет, чтобы я смотрел? )"
    scene shower05c
    player_name "( У нее действительно отличное тело. )"
    scene shower05b
    scene shower05a
    player_name "..."
    show shower 05d_05e
    player_name "( ...Она- )"
    player_name "( Вау... )"
    player_name "( ...Я должен... )"
    player_name "( ...уйти, пока она не заметила... )"
    hide shower 05d_05e
    hide shower05a
    return

label shower_sis_sex_peep_before_cuddle:
    scene shower3
    player_name "Черт! {b}[jen_name]{/b} в душе..."
    scene shower4 with hpunch
    player_name "( Дерьмо!! Она заметила меня! )"
    scene shower2
    show jenny 3 at right
    show player 6 at left
    with dissolve
    jen "Что с тобой не так??!"
    jen "Разве ты не видишь, что я здесь?"
    show jenny 2 at Position(xpos=962) with fastdissolve
    player_name "Дверь была не заперта!"
    show player 3 with fastdissolve
    jen "Постучи сначала в следующий раз, извращенец!"
    show player 29
    player_name "Прости! Я думал, здесь никого нет..."
    hide jenny
    hide player
    with dissolve
    hide shower2
    return

label shower_sis_sex_go_inside:
    scene shower2b
    show player 11 at Position(xpos=261)
    with fade
    player_name "( Не могу поверить, что собираюсь сделать это... )"
    show player 4 at Position(xpos=267)
    player_name "( Будет ли она кричать на меня в этот раз, или она позволит мне остаться? )"
    player_name "( Она оставила дверь открытой, как бы приглашая меня... )"
    show player 13 at Position(xpos=261)
    player_name "( Я знаю... )"
    show player 249 at left with fastdissolve
    player_name "( Я могу просто притвориться, что не видел ее! )"
    show player 261f at Position(xpos=137) with fastdissolve
    player_name "( Хорошо,  вхожу... )"
    return

label shower_sis_sex_leave:
    player_name "( Нет, слишком рискованно... )"
    return

label shower_sis_sex_intro:
    $ game.timer.tick()
    if sis_shower_intro_first:
        call expression game.dialog_select("shower_sis_sex_intro_first")
        $ sis_shower_intro_first = False
    else:

        call expression game.dialog_select("shower_sis_sex_intro_repeat")
    if not store._in_replay == None:
        jump expression game.dialog_select("sis_shower_jump_1")

    elif sister.known(sis_shower_cuddle02) and not sister.known(sis_hallway01):
        $ sis_shower_cuddle02.finish()
        $ sister.add_event(sis_hallway01)
    menu:
        "Ой, Прости!":
            call expression game.dialog_select("shower_sis_sex_intro_sorry")
        "Помочь?":

            if sis_shower_intro_first:
                call expression game.dialog_select("shower_sis_sex_intro_help_fail")
            else:

                label sis_shower_jump_1:
                    call expression game.dialog_select("shower_sis_sex_intro_help_pass")
            $ M_jenny.set("seen MCs penis", True)
            call expression game.dialog_select("sis_shower_sex")
    hide jenny
    hide player
    with dissolve
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label shower_sis_sex_intro_first:
    scene shower_closeup
    show player 342 at Position(xpos=160)
    show jenny 163 at Position(xpos=791)
    with fade
    pause
    show jenny 163b with fastdissolve
    pause
    show jenny 106 with fastdissolve
    jen "Так так..."
    jen "Мне было интересно, когда ты последуешь за мной."
    show jenny 105
    return

label shower_sis_sex_intro_repeat:
    scene shower_closeup
    show player 342 at Position(xpos=160)
    show jenny 163 at Position(xpos=791)
    with fade
    pause
    show jenny 163b with fastdissolve
    jen "А?"
    show jenny 104
    jen "{b}[firstname]{/b}?!" with hpunch
    jen "Какого хрена?!"
    jen "Разве ты не видишь, что я здесь?!!"
    show jenny 105
    return

label shower_sis_sex_intro_sorry:
    show jenny 105
    show player 343
    player_name "Ой!"
    player_name "Извени! Я не заметил тебя..."
    show jenny 106
    show player 342
    jen "Разве я не говорила тебе стучаться?! Идиот!"
    show player 343
    show jenny 105
    player_name "Я знаю но-"
    show jenny 104
    show player 342
    jen "Зткнись и {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    return

label shower_sis_sex_intro_help_fail:
    show jenny 105
    show player 343
    player_name "Я подумал, может тебе снова нужна помощь..."
    show jenny 107
    show player 342
    jen "Помощь? Ха!!"
    show jenny 106
    jen "Больше чем я помогаю себе, пока извращеный идиот смотрит..."
    jen "Ты действительно не можешь перестать шпионить за мной, не так ли?"
    show jenny 105
    player_name "..."
    return

label shower_sis_sex_intro_help_pass:
    show jenny 105
    show player 343
    player_name "Я знаю..."
    player_name "Мне было интересно, если... ну ты знаешь... тебе нужна помощь?"
    show jenny 104
    show player 342
    jen "Помощь??"
    show jenny 106
    jen "О! Ха-ха!"
    show jenny 105
    show player 343
    player_name "Что смешного?"
    show player 342
    show jenny 106
    jen "Ух... ты {b}жалок{/b}."
    jen "Я знаю, ты просто хочешь увидеть меня голой!"
    show jenny 105
    player_name "..."
    return

label sis_shower_sex:
    call expression game.dialog_select("sis_shower_sex_pre")
    if not store._in_replay == None:
        call expression game.dialog_select("sis_shower_jump_2")
    menu:
        "Уйти.":
            call expression game.dialog_select("sis_shower_sex_leave")

        "Умолять." if not sister.known(sis_shower_cuddle03):
            call expression game.dialog_select("sis_shower_sex_first_beg_fail")

        "Умолять." if sister.known(sis_shower_cuddle03):
            if not sister.known(sis_couch03):
                $ sister.add_event(sis_couch03)
            $ sis_shower_cuddle03.finish()
            label sis_shower_jump_2:
                call expression game.dialog_select("sis_shower_sex_first_beg_pass")
            if not store._in_replay == None:
                call expression game.dialog_select("sis_shower_jump_3")
            menu:
                "Уйти.":
                    call expression game.dialog_select("sis_shower_sex_leave")

                "Умолять." if not sister.known(sis_shower_cuddle04):
                    call expression game.dialog_select("sis_shower_sex_second_beg_fail")

                "Умолять." if sister.known(sis_shower_cuddle04):
                    if not sister.known(sis_final):
                        $ sister.add_event(sis_final)
                    $ sis_shower_cuddle04.finish()
                    label sis_shower_jump_3:
                        call expression game.dialog_select("sis_shower_sex_second_beg_pass")
                    if not store._in_replay == None:
                        call expression game.dialog_select("sis_shower_jump_4")
                    menu:
                        "Вставить." if not sister.known(sis_shower_cuddle05) or player.stats.dex() < 7:
                            call expression game.dialog_select("sis_shower_sex_put_it_in_fail")

                        "Вставить." if sister.known(sis_shower_cuddle05) and player.stats.dex() >= 7:
                            $ sis_shower_cuddle05.finish()
                            label sis_shower_jump_4:
                                $ M_jenny.set("sex speed", .4)
                                $ anim_toggle = False
                                $ xray = False
                            call expression game.dialog_select("sis_shower_sex_put_it_in_pass")
                            jump expression game.dialog_select("sis_shower_sex_loop")
    hide jenny
    hide player
    with dissolve
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_pre:
    show jenny 107
    show player 342
    jen "Хорошо, я позволю тебе остаться..."
    show jenny 106
    jen "... но, ты помогаешь только {b}смотря{/b} своими {b}глазами{/b}."
    show jenny 104
    jen "Понятно?!"
    show jenny 105
    show player 343
    player_name "Да, {b}[jen_name]{/b}..."
    show player 342
    show jenny 109 at right
    jen "Хорошо."
    jen "Сейчас..."
    show jenny 110 with fastdissolve
    jen "Мне нравится моя грудь, красивая и мыльная..."
    show jenny 111
    jen "Поэтому я люблю использовать мнооооого мыла!"
    show jenny 112 with fastdissolve
    pause
    show jenny 113 with fastdissolve
    pause
    show jenny 115 with fastdissolve
    jen "Тебе нравится видеть весь этот... {b}крем{/b} на мне?"
    jen "Это заставляет тебя думать о чем-то {b}другом{/b}?"
    show jenny 114
    show player 343
    player_name "Я... Я не знаю..."
    show player 342
    jen "Хммм..."
    show jenny 115
    show player 344
    jen "Давай намылим их немного!"
    show jenny 116 at Position(xpos=984) with fastdissolve
    pause
    show jenny 117_118_119_116 at Position(xpos=980)
    pause 8
    show player 345 at left
    show jenny 122 at Position(xpos=980)
    player_name "Ого..."
    show jenny 120b
    show player 346 with fastdissolve
    pause 0.05
    show player 347 with vpunch
    pause
    show jenny 120
    jen "Ну, это было легко!"
    show player 348 at Position(xpos=60)
    show jenny 109 at Position(xpos=1024)
    jen "Раз тебе это нравится, может, мы сможем вымыть {b}еще одну{/b} часть моего тела..."
    show jenny 108
    show player 349
    player_name "Хорошо..."
    show jenny 109
    show player 348
    jen "Во-первых, я хочу услышать, как ты {b}умоляешь{/b} об этом."
    show jenny 167
    show player 349
    player_name "Что ты имеешь в виду?"
    show jenny 166
    show player 348
    jen "Что из этого тебе не понятно?"
    show jenny 164
    jen "... Я не буду этого делать, пока ты не будешь {b}умолять{/b}меня!"
    show jenny 167
    show player 349
    player_name "Умолять... для чего именно?"
    show jenny 109
    show player 348
    jen "Я хочу, чтобы ты {b}умолял{/b} показать мою киску."
    show jenny 108
    return

label sis_shower_sex_leave:
    show player 349
    show jenny 167
    player_name "Думаю, я просто уйду отсюда..."
    show player 348
    jen "???"
    show jenny 166
    jen "Ты не будешь этого делать?"
    show player 349
    show jenny 165
    player_name "Нет, извени."
    show player 354
    show jenny 164
    jen "Думаешь, ты {b}слишком хорош{/b} для этого?!"
    show player 349
    show jenny 165
    player_name "Это не похоже-"
    show player 354
    show jenny 164
    jen "Заткнись и {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    return

label sis_shower_sex_first_beg_fail:
    show player 349
    show jenny 108
    player_name "Можешь... показать мне свою киску?"
    show player 348
    show jenny 109
    jen "Я не слышу {b}пожалуйста{/b}."
    show player 349
    show jenny 167
    player_name "Пожалуйста, покажи мне свою киску, {b}[jen_name]{/b}?"
    show player 348
    show jenny 166
    jen "Знаешь что..."
    jen "Я не думаю, что ты заслуживаешь этого, даже если просил."
    jen "Ты все равно слишком жалок."
    show player 349
    show jenny 167
    player_name "Но я думал, тебе нужна помощь-"
    show player 348
    show jenny 166
    jen "Может позже... если ты будешь относиться ко мне немного лучше..."
    show jenny 164
    show player 354
    jen "Сейчас, {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    return

label sis_shower_sex_first_beg_pass:
    show player 349
    show jenny 108
    player_name "Можешь... показать мне свою киску?"
    show jenny 109
    show player 348
    jen "Я не слышу {b}пожалуйста{/b}."
    show jenny 108
    show player 349
    player_name "Пожалуйста, покажи мне свою киску, {b}[jen_name]{/b}?"
    show player 348
    show jenny 109
    jen "Хорошо..."
    show jenny 127
    show player 344b
    with fastdissolve
    jen "Давай помоем эту часть моего тела... прямо здесь..."
    show jenny 124_125_126_123
    pause 8
    jen "Ммм..."
    show jenny 127
    jen "Знаешь что?"
    jen "Я не могу туда добраться... Мне нужна помощь..."
    show player 349 at Position(xpos=60)
    show jenny 123
    player_name "...Моя помощь?"
    show player 348
    show jenny 109 at Position(xpos=1024) with fastdissolve
    jen "Не совсем..."
    jen "Во-первых, положи немного мыла на него..."
    show jenny 167
    show player 349
    player_name "На него?"
    show player 348
    show jenny 166
    jen "На {b}член{/b}, идиот!"
    show jenny 111 with fastdissolve
    jen "Вот, возьми!"
    show jenny 108
    show player 356
    with fastdissolve
    pause
    show player 350 with fastdissolve
    pause
    show player 348 with fastdissolve
    show jenny 109
    jen "Теперь ты знаешь, что делать..."
    show jenny 108
    show player 349
    player_name "Я не знаю..."
    show jenny 109
    show player 348
    jen "Я хочу услышать, как ты {b}умоляешь{/b} меня, но на этот раз {b}ПО-НАСТОЯЩЕМУ{/b} ..."
    show jenny 108
    return

label sis_shower_sex_second_beg_fail:
    show player 349
    show jenny 167
    player_name "Могу я... помочь тебе, пожалуйста, {b}[jen_name]{/b}?"
    show jenny 164
    show player 354
    jen "НЕПРАВИЛЬНО!!" with hpunch
    show jenny 109
    show player 348
    jen "Я хочу чтобы ты называл меня {b}принцессой{/b}..."
    show jenny 167
    show player 349
    player_name "Могу ли я помочь вам, {b}принцесса{/b}?"
    show player 348
    show jenny 166
    jen "Знаешь что?"
    jen "Я не думаю, что ты заслуживаешь этого, даже если просил."
    jen "Ты все равно слишком жалок."
    show player 349
    show jenny 167
    player_name "Но я думал, тебе нужна помощь-"
    show player 348
    show jenny 166
    jen "Может позже... если ты будешь относиться ко мне немного лучше..."
    show jenny 164
    show player 354
    jen "Сейчас, {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    return

label sis_shower_sex_second_beg_pass:
    show jenny 167
    show player 349
    player_name "Могу я... помочь тебе, пожалуйста, {b}[jen_name]{/b}?"
    show player 354
    show jenny 164
    jen "НЕПРАВИЛЬНО!!" with hpunch
    show jenny 109
    show player 348
    jen "Я хочу чтобы ты называл меня {b}принцессой{/b}..."
    show jenny 108
    show player 349
    player_name "Могу ли я, пожалуйста, помочь вам,  {b}принцесса{/b}?"
    show player 354
    show jenny 164
    jen "ГРОМЧЕ!!" with hpunch
    show player 355
    show jenny 108
    player_name "Могу..."
    player_name "{b}Могу ли я, пожалуйста, помочь вам, принцесса{/b}?!!" with hpunch
    show player 348
    show jenny 109
    jen "Так то лучше!"
    jen "Конечно."
    jen "Я позволяю тебе помочь мне..."
    show jenny 166
    jen "... не, {b}ТРОГАЙ{/b} меня своими руками!!"
    hide player
    hide jenny
    show jennysex 96
    with fastdissolve
    jen "Понятно?!"
    show jennysex 95 at Position(xpos=511)
    player_name "Да, {b}[jen_name]{/b}..."
    show jennysex 92_93_94_95 at Position(xpos=511)
    pause 8
    show jennysex 96 at Position(xpos=512)
    jen "Тебе нравится, маленький извращенец?"
    show jennysex 93 at Position(xpos=534)
    pause
    show jennysex 94 at Position(xpos=513)
    pause
    show jennysex 95 at Position(xpos=511)
    return

label sis_shower_sex_put_it_in_fail:
    hide jennysex
    show jenny 129 zorder 1 at Position(xpos=443)
    show player 351 zorder 2 at Position(xpos=260)
    jen "[dex_warn]Не так быстро, извращенец!!" with hpunch
    jen "[dex_warn]Что ты пытаешься сделать?!"
    show jenny 128
    player_name "!!!"
    show jenny 130
    jen "Я же сказала тебе {b}БЕЗ РУК{/b}??"
    show player 351b
    show jenny 131
    player_name "Извините ... Я не удержался ..."
    show jenny 132
    show player 351
    jen "Тебе повезло, что я позволила тебе зайти так далеко!"
    show jenny 131
    show player 351b
    player_name "М..."
    player_name "Мне жаль!!"
    show jenny 130
    show player 351
    jen "Заткнись и {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    return

label sis_shower_sex_put_it_in_pass:
    show jennysex 98
    jen "Аааа!!!" with hpunch
    show jennysex 97
    jen "Что ты ДЕЛАЕШЬ?!!"
    show jennysex 101 at Position(xpos=476)
    player_name "Я хочу тебя, {b}[jen_name]{/b}!!!"
    return

label sis_shower_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("jennysex", [98,99,100,101], M_jenny) as jennysex at Position(xpos = 511)
            pause 5
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_shower_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [98,99,100,101]
            $ xpos_list = [511,518,497,476]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jennysex {}".format(pose_list[pose_counter]) as jennysex at Position(xpos = xpos_list[pose_counter])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("jenny_shower_hscene_dialog")
        $ animcounter += 1
    jen "Не смей кончать в меня...{p=2}{nw}"
    if not anim_toggle:
        show jennysex 97 at Position(xpos=511)
    jen "... Я клянусь Я {b}УБЬЮ ТЕБЯ{/b}!!{p=2}{nw}"
    call screen sis_shower_sex_options

label jenny_shower_hscene_dialog:
    if animcounter == 1:
        jen "Аааааа!!!{p=1}{nw}"

    elif animcounter == 3:
        jen "О!!!{p=1}{nw}"
        player_name "Ууух...{p=1}{nw}"
    return

label sis_shower_sex_cum_1:
    if anim_toggle:
        call expression game.dialog_select("sis_shower_sex_cum_1_pre_animation")
    else:
        call expression game.dialog_select("sis_shower_sex_cum_1_pre_manual")
    $ xray = False
    call expression game.dialog_select("sis_shower_sex_cum_1_after")
    $ playSound()
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_cum_1_pre_animation:
    show jennysex 98_99_100_101
    pause 5
    hide jennysex
    return

label sis_shower_sex_cum_1_pre_manual:
    show jennysex 101 at Position(xpos=476)
    pause
    show jennysex 98 at Position(xpos=511)
    pause
    show jennysex 99 at Position(xpos=518)
    pause
    show jennysex 100 at Position(xpos=497)
    pause
    show jennysex 101 at Position(xpos=476)
    pause
    hide jennysex
    return

label sis_shower_sex_cum_1_after:
    show jenny 130 zorder 1 at Position(xpos=443)
    show player 351 zorder 2 at Position(xpos=260)
    jen "[str_warn]Какого {b}ХРЕНА{/b}??" with hpunch
    jen "[str_warn]Ты собирался кончить {b}В{/b} меня!?"
    show jenny 131
    show player 351b
    player_name "Нет..."
    show jenny 130
    show player 351
    jen "Что с тобой?!"
    jen "Ты же знаешь что я могу {b}ЗАБЕРЕМЕНЕТЬ{/b}, правда??! ТЫ ИДИОТ!"
    show jenny 131
    show player 351b
    player_name "М..."
    player_name "Мне жаль!!"
    show jenny 130
    show player 351
    jen "Да, точно! Мы закончили! {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    hide jenny
    hide player
    with dissolve
    return

label sis_shower_sex_cum_2:
    if anim_toggle:
        call expression game.dialog_select("sis_shower_sex_cum_2_animation")
    else:
        call expression game.dialog_select("sis_shower_sex_cum_2_manual")
    call expression game.dialog_select("sis_shower_sex_cum_2_pre")
    $ xray = False
    call expression game.dialog_select("sis_shower_sex_cum_2_after")
    $ playSound()
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    jump expression game.dialog_select("hallway_dialogue")

label sis_shower_sex_cum_2_animation:
    show jennysex 98_99_100_101
    pause 5
    return

label sis_shower_sex_cum_2_manual:
    show jennysex 101 at Position(xpos=476)
    pause
    show jennysex 98 at Position(xpos=511)
    pause
    show jennysex 99 at Position(xpos=518)
    pause
    show jennysex 100 at Position(xpos=497)
    pause
    show jennysex 101 at Position(xpos=476)
    pause
    return

label sis_shower_sex_cum_2_pre:
    show white
    show jennysex 102 at Position(xpos=516)
    jen "{b}Аааах!!!!{/b}" with hpunch
    hide white with dissolve
    pause
    show jennysex 103 at Position(xpos=511) with fastdissolve
    pause
    show jennysex 102_103 at Position(xpos = 516)
    pause 2.5
    show jennysex 103 at Position(xpos=511)
    return

label sis_shower_sex_cum_2_after:
    jen "{b}*тяжело дыша*{/b}"
    jen "Боже мой..."
    hide jennysex
    show jenny 134 zorder 1 at Position(xpos=600)
    show player 353 zorder 2 at Position(xpos=260)
    with dissolve
    jen "Какого хрена?!?!"
    jen "Я чувствую его!!!"
    show player 352
    jen "Ты продолжаешь стрелять спермой глубоко во внутрь!!"
    show jenny 133
    show player 349 at Position(xpos=254)
    player_name "Это был рефлекс!"
    player_name "Я... Я не смог остановиться..."
    show jenny 134
    show player 348
    jen "Ты не понимаешь, ты идиот?!"
    jen "Если ты продолжишь кончать в меня каждый раз, я могу {b}ЗАБЕРЕМЕНЕТЬ{/b}!!"
    show jenny 133
    show player 349
    player_name "Пр..."
    player_name "Прости меня!!"
    show jenny 134
    show player 353 at Position(xpos=260)
    jen "За-Заткнись и {b}ВЫМЕТАЙСЯ{/b}!!" with hpunch
    hide jenny
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
