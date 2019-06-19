label shower_jenny_pregnant:
    scene expression L_home_shower.background_blur
    show jenny b_towel a_magic_preggo_towel f_gross_down at flip
    show jenny at Position (xpos=500)
    show player f_flirt with dissolve
    pause 1
    show jenny f_gross_down_talk
    jen "{b}*Sigh*{/b} I am never going to forgive him for this shit..."
    show player f_surprised_teeth a_dressed_surprised_up_both with dissolve
    jen "That bastard should be waiting on me twenty-four, seven!"
    show player at Position (xoffset=-100) with dissolve
    jen "Catering to my every need!"
    hide player with dissolve
    jen "Rubbing feet..."
    scene expression L_home_hallway.background_blur
    show player f_worried with dissolve
    player_name "( Yeah, I probably shouldn't go in there right now... )"
    hide player with dissolve
    return

label shower_jenny_peep:
    player_name "( Is she... Masturbating?! )"
    player_name "( Oh, this is awesome! )"
    pause
    player_name "( I wish, I could stand here and keep watching... )"
    pause
    player_name "( I'd better go before she sees me. )"
    return

label shower_jenny_pissed_at_handjob:
    pause
    player_name "( I wonder if she realizes I'm watching her? )"
    pause
    player_name "( Would she even care if I joined her? )"
    player_name "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"
    pause
    player_name "( Nah, she'd might freak out and hit me with something. )"
    player_name "( Not worth it. )"
    return

label shower_jenny_blowjob_intro_repeat:
    player_name "( Heh, and there's my cue... )"
    menu:
        "Enter.":
            call scene_shower_with_vfx
            show jenny f_sexy_talk b_shower a_naked_hips
            show player b_naked a_naked_sides f_normal od_naked_dick3
            with fade
            jen "It's about damn time!"
            jen "I didn't think you were ever going to join me!"
            show jenny f_sexy
            show player f_normal_talk
            player_name "Well, here I am..."
            show jenny f_grin_down a_shower_soap1 with dissolve
            player_name "So, what do you wanna-"
            show player f_surprised
            show jenny a_shower_soap2 with dissolve
            pause
            show jenny a_shower_soap3 with dissolve
            pause
            show jenny f_grin b_shower_soaping a_empty with dissolve
            player_name "..."
            show jenny f_grin_talk
            jen "What were you saying?"
            show jenny f_grin
            show player f_worried_talk
            player_name "Was I saying something?"
            show player f_worried
            show jenny f_laugh
            jen "Hahaha!"
            show jenny f_grin
            menu:
                "Blowjob":

                    show jenny f_grin_talk
                    jen "You wanna have a little fun?"
                    show jenny f_grin b_shower a_naked_hips with dissolve
                    show player f_normal_talk
                    player_name "Yes!"
                    show player f_normal
                    if M_jenny.get("dominance") <= 0:
                        show jenny f_grin_talk
                        jen "Well then, you know what comes next..."
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "Do I have to?"
                        show player f_worried
                        show jenny f_grin_talk
                        jen "C'mon, doggy..."
                        jen "You gotta beg for your treat!"
                        show jenny f_grin
                        show player f_worried_talk
                        player_name "{b}*Sigh*{/b}"
                        jump bj_shower_repeat_sub
                    else:
                        show player f_skeptical_talk
                        player_name "And before you ask, I'm not begging!"
                        show player f_skeptical
                        show jenny f_upset_talk
                        jen "Yeah, yeah."
                        jen "I'm well aware."
                        show jenny f_upset
                        call scene_shower_with_vfx_zoom
                        show jenny_shower_bj_mc
                        show jenny_shower_bj pre_talk
                        with fade
                        jen "Just shut up and enjoy, asshole."
                        jump bj_shower_repeat_dom

                "Sex" if M_jenny.finished_inclusive(S_jenny_end):

                    label jenny_shower_sex_intro_replay:
                    if store._in_replay is not None:
                        $ player.location = L_home_shower
                        call scene_shower_with_vfx
                        show jenny f_grin b_shower_soaping a_empty
                        show player b_naked a_naked_sides f_worried od_naked_dick3
                        with fade
                        pause
                    show jenny f_grin_talk b_shower a_naked_hips with dissolve
                    jen "Hmm, I think I deserve the treat today."
                    show jenny f_grin
                    show player f_worried_talk
                    player_name "What do you mean?"
                    show player f_worried
                    show jenny f_grin_talk
                    jen "I mean, you're going to fuck me."
                    show jenny f_grin
                    show player f_surprised
                    player_name "!!!"
                    show player f_normal_talk
                    player_name "Okay, sure!"
                    show player f_normal
                    show jenny b_shower_back a_shower_back_down f_shower_overshoulder_back_look_normal_talk o_shower_back_soap at Position (align=(0,0)) with dissolve
                    jen "Ah ah ah, not so fast!"
                    show player b_side_naked_forward a_side_naked_react f_side_shock_down od_empty zorder 0
                    show jenny b_shower_butt1 f_shower_butt1_talk a_empty o_empty zorder 1
                    with dissolve
                    jen "You wanna stick it in?"
                    jen "You've gotta beg for it!"
                    show jenny b_shower_butt f_empty with dissolve
                    show player f_side_shy_down_talk
                    player_name "Ugh, this again?!"
                    show player f_side_shy_down
                    show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                    jen "C'mon, loser."
                    jen "Beg your princess!"
                    show jenny b_shower_butt f_empty with dissolve
                    if M_jenny.get("dominance") <= 0:
                        show player f_side_shy_down_talk
                        player_name "{b}*Sigh*{/b}"
                        player_name "Please, {b}Princess [jen_name]{/b}..."
                        show player f_side_shy_down
                        show jenny b_shower_butt1 f_shower_butt1_talk with dissolve
                        jen "Please what?"
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "Please, can I stick it inside you?"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hmm, I think you can do better..."
                        show jenny f_shower_butt1
                        show player f_side_shy_down_talk
                        player_name "PLEASE?!"
                        show player f_side_shy_down
                        show jenny f_shower_butt1_talk
                        jen "Hahahaah!!"
                        jen "Alright, do it!"
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "!!!" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "Wow, you really are excited!"
                        player_name "Y-yeah!"
                    else:
                        pause
                        show jenny_shower_sex 1
                        hide player
                        hide jenny
                        jen "What the-" with hpunch
                        $ animated = True
                        $ anim_toggle = True
                        $ M_jenny.set('sex speed', .12)
                        show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
                        jen "... Oh, Fuuuuuuuuck!"
                        pause
                        jen "I didn't say you could-"
                        player_name "You want me to stop?"
                        jen "NO!"
                        jen "Don't stop!"
                    jump jenny_shower_sex_loop
        "Not Now.":
            player_name "( Hmm, nah... )"
            player_name "( I'm not really in the mood to mess with her today. )"
            pause
            $ renpy.end_replay()
            return

label shower_jenny_blowjob_intro_first:
    if store._in_replay is not None:
        $ player.location = L_home_shower
        call scene_shower_with_vfx
        with None
        $ M_jenny.set('rng', randomizer())
        if M_jenny.get('rng') > 50:
            show jenny b_shower_scene_d1 a_empty f_empty
            pause
            show jenny b_shower_scene_d_rub with dissolve
        else:
            show jenny b_shower_scene_e_rub a_empty f_empty
    player_name "( I wonder if she realizes I'm watching her? )"
    pause
    player_name "( Would she even care if I joined her? )"
    player_name "( I mean, after what we've been doing for her camshows, showering together doesn't seem so taboo... )"
    pause
    player_name "( Nah, she'd might freak out and hit me with- )"
    jen "Are you just gonna stand there and watch?"
    player_name "!!!" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower a_naked_hips f_sexy_camera at Position (xoffset=-200) with dissolve
    else:
        show jenny b_shower_back f_shower_overshoulder_back_look_normal a_shower_back_down at Position (align=(0,0)) with dissolve
    player_name "Huh?!"
    player_name "I wasn't-"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Hehe, would you just take your clothes off and get in here already!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "R-really?"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera_talk at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal_talk
    jen "Yes!"
    if M_jenny.get('rng') > 50:
        show jenny f_sexy_camera at Position (xoffset=-200)
    else:
        show jenny f_shower_overshoulder_back_look_normal
    player_name "Okay."
    call scene_shower_with_vfx
    show jenny f_sexy b_shower a_naked_hips
    show player b_naked a_naked_sides f_worried_talk od_naked_dick3
    with fade
    player_name "So, ehh..."
    player_name "Do you need a hand or something?"
    show player f_worried
    show jenny f_grin_talk
    jen "Did you seriously just ask if I needed a hand?"
    show jenny f_grin
    player_name "..."
    show jenny f_laugh
    jen "Pfft, hahahaha!"
    jen "That's so pathetic!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Shut up!"
    show player f_skeptical
    show jenny f_laugh
    jen "Haha!"
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Did you just invite me in to make fun of me?"
    show player f_skeptical
    show jenny f_grin_talk a_shower_soap1 with dissolve
    jen "No."
    jen "I actually was thinking we would mess around a little bit."
    show jenny f_grin_down a_shower_soap2 with dissolve
    pause
    show jenny a_shower_soap3 with dissolve
    show player f_worried_talk
    player_name "{b}*Gulp*{/b} R-really?"
    show player f_worried
    show jenny f_grin_talk a_shower_soap2 o_shower_soap1 with dissolve
    jen "Yeah."
    show jenny f_grin
    pause
    show jenny f_upset_talk a_shower_soap1 with dissolve
    jen "Of course, that was before you fed me that stupid line."
    show jenny f_grin_down a_shower_soap4 with dissolve
    player_name "..."
    show jenny f_grin_talk b_shower_soaping a_empty o_empty with dissolve
    jen "So now, I'm thinking... You'll have to beg for it."
    show jenny f_grin
    show player f_skeptical_talk
    player_name "Huh?"
    show player f_skeptical
    pause
    show jenny f_eyeroll b_shower a_naked_hips with dissolve
    jen "You wanna help me wash, don't you?"
    show jenny f_upset
    show player f_worried_talk
    player_name "Y-yes."
    show player f_worried
    show jenny f_grin_talk
    jen "Then be a good doggy and beg!"
    show jenny f_grin
    show player f_worried_talk
    player_name "You want me to beg?"
    show player f_worried
    show jenny f_grin_talk
    jen "Go on."
    show jenny f_grin
    player_name "..."
    if M_jenny.get("dominance") <= 0:
        show player f_worried_talk
        player_name "P-please?"
        show player f_worried
        show jenny f_grin_talk
        jen "Please what?"
        show jenny f_grin
        show player f_worried_talk
        player_name "Please, let me wash you..."
        show player f_worried
        show jenny f_grin_talk
        jen "Now bark like a dog."
        show jenny f_grin
        show player f_worried_talk
        player_name "Seriously?!"
        show player f_worried
        show jenny f_laugh
        jen "Ah ah ah, I said bark!"
        show jenny f_grin
        player_name "..."
        jump bj_shower_repeat_sub
    else:
        show player f_skeptical_talk
        player_name "No way!"
        show player f_skeptical
        show jenny f_grin_talk
        jen "Yes, way!"
        show jenny f_grin
        player_name "..."
        show jenny f_upset_talk
        jen "C'mon {b}[firstname]{/b}, do it!"
        show jenny f_upset
        show player f_skeptical_talk
        player_name "No!"
        show player f_skeptical
        show jenny f_angry_talk
        jen "Beg or get out!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name "Screw this, I'm outta here."
        show player f_skeptical
        show jenny f_angry_talk
        jen "What?!"
        jen "You're seriously going to walk away from me right now?!"
        show jenny f_angry
        show player f_skeptical_talk
        player_name "You know I hate this humiliation stuff, {b}[jen_name]{/b}!"
        player_name "If that's all you brought me in here for, then just forget it!"
        show player f_skeptical
        show jenny f_angry_pouting
        jen "..."
        show jenny f_angry_talk
        jen "Grr, fine!"
        show jenny f_angry
        call scene_shower_with_vfx_zoom
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_look
        with fade
        player_name "!!!"
        show jenny_shower_bj pre_talk
        jen "You really take the fun out of all this!"
        show jenny_shower_bj pre_look
        player_name "W-what are you doing?!"
        show jenny_shower_bj pre_talk
        jen "What the fuck does it look like I'm doing?!"
        jump bj_shower_repeat_dom

label shower_jenny_snoop_around_for_laptop:
    scene expression player.location.background_closeup with None
    show player 17 with dissolve
    player_name "( Hmm, this is {b}my chance to sneak into her room and look through her diary{/b}. )"
    player_name "( I should hurry! )"
    hide player with dissolve
    return

label shower_jenny_snoop_around:
    scene expression player.location.background_closeup with None
    show player 13 with dissolve
    player_name "( Hmm, this is {b}my chance to sneak into her room and look for that camera{/b}. )"
    player_name "( I should hurry! )"
    hide player with dissolve
    return

label shower_mom_sis_check:
    scene shower_cutscene1
    show text "Я бросился наверх, услышав проклятия {b}[jen_name]{/b}.\nСцена при входе была почти смешной. {b}[jen_name]{/b} была взволнована и выглядела как мокрая крыса.\nОткрытая труба изливала воду повсюду и делала вокруг беспорядок." at Position(xpos=500, ypos=700)
    with dissolve
    $ renpy.pause()
    hide shower_cutscene1
    hide text
    scene shower2
    show player 11 at left
    show jenny f_upset_talk b_wet a_dressed_hips
    with dissolve
    jen "Ты как раз вовремя появился!"
    show player 10
    show jenny f_upset
    player_name "Как такое могло произойти?!"
    show player 11
    show jenny f_upset_talk
    jen "Откуда мне об этом знать? По-твоему, я похожа на водопроводчика?! Я всего лишь включила раковину!"
    show player 12
    show jenny f_upset
    player_name "Что мне прикажешь делать?"
    show player 11
    show jenny f_upset_talk
    jen "Исправь это, очевидно! В конце концов, ты здесь единственный мужчина!"
    show jenny f_gross
    show player 12
    player_name "Отлично! Я думаю, нужно {b}спустится вниз{/b} и посмотреть как выключается {b}водопроводный кран{/b}..."
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_close_valve:
    scene shower2
    show jenny f_upset_talk b_wet a_dressed_hips
    show player 11 at left
    with dissolve
    jen "Вода все еще бежит!"
    jen "Иди в {b}подвал{/b} и закрой водопроводный {b}кран{/b}!"
    hide player
    hide jenny
    with dissolve
    return

label shower_mom_pipe_check:
    scene shower2
    show jenny b_wet a_dressed_hips f_upset_talk
    show player 11 at left
    with dissolve
    jen "Похоже, у тебя получилось. Вода остановилась."
    show player 12
    show jenny f_upset
    player_name "Да, я закрыл водопроводный кран. Что дальше?"
    show player 5
    show jenny f_upset_talk
    jen "О чем ты меня спрашиваешь? Я не знаю, заменить его или что-то?"
    show player 10
    show jenny f_upset
    player_name "Я никогда не работал над чем-то подобным!"
    show player 5
    show jenny f_upset_talk
    jen "Ну, теперь ты живешь в доме с девушками, а это значит, что тебе нужно научиться исправлять такие вещи!"
    show player 10
    show jenny f_gross
    player_name "Окей! Окей! Я думаю, я пойду в {b}CONSUM-R{/b} и посмотрю, как получить {b}трубный ключ{/b}."
    show player 212
    player_name "..."
    show player
    show jenny f_normal_low
    pause
    show jenny f_angry
    jen "..."
    show jenny f_angry_talk
    jen "Ты хорошо все разглядел, маленький извращенец?!"
    show player 23
    show jenny f_angry
    player_name "Я не-"
    show player 22
    show jenny f_angry_talk
    jen "О, пожалуйста, думаешь, я не могу понять, когда кто-то пялится на мои сиськи?"
    show jenny f_angry
    player_name "..."
    show jenny f_angry_talk
    jen "Что с тобой происходит?"
    show jenny f_angry
    show player 24
    player_name "Прости, {b}[jen_name]{/b}. Я только-"
    show jenny f_angry_talk
    jen "Ой, заткнись!"
    show player 25
    jen "Если собираешься пялиться, хотя бы будь мужиком!"
    jen "Отрицая это или оправдываясь, ты выглядишь слабаком."
    jen "Никто не хочет, чтобы его проверял бесхребетный маленький слабак!"
    show jenny f_angry
    show player 5
    player_name "..."
    show jenny f_upset_talk at right
    jen "Если бы ты поднялся сюда, чтобы разобраться с этой ситуацией с трубами раньше, возможно, я была бы в лучшем настроении."
    jen "... Но с тех пор, как ты решил приятно провести время...."
    show jenny f_grin_talk
    jen "Думаю, тебе стоит взять это..."
    show player 22
    show jenny f_grin_down a_empty b_pull1_wet with dissolve
    pause
    show jenny b_pull2 f_empty with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    pause
    show player 23
    show jenny b_panties f_upset_talk a_panties_shirt with dissolve
    jen "...  чтобы постирать внизу для меня."
    show jenny f_upset
    player_name "( !!! )" with hpunch
    show player 21
    player_name "Ко-конечно..."
    show jenny a_naked_hips f_angry
    show player 211
    with dissolve
    jen "..."
    show jenny f_angry_talk
    jen "Перестань пялиться и иди! Я не собираюсь весь день ждать ,пока ты {b}починишь эту трубу{/b}!"
    show jenny f_angry
    show player 22 with dissolve
    player_name "( !!! )"
    hide player with dissolve
    pause
    show jenny f_grin_talk
    jen "Хех, я так и знала!"
    jen "У этого маленького неудачника есть кое-что для меня!"
    hide jenny with dissolve
    hide shower2
    return

label shower_mom_fix_pipe_no_wrench:
    scene shower2
    show player 11 at left
    if not game.timer.is_dark():
        show jenny f_upset_talk b_panties a_naked_hips
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
    scene expression "backgrounds/location_home_bathroom_cutscene02.jpg"
    show expression FilteredText("shower_cutscene2", "Как только я вернулся домой, я направился наверх, чтобы починить раковину в ванной.\nЯ заменил сломаную трубу на новую и затянул ее настолько, насколько смог. \nБыло немного странно, что {b}[deb_name]{/b} и {b}[jen_name]{/b} все время наблюдали за мной.\nК счастью для меня, ремонт прошел гладко...")  as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    
    scene shower2
    show player 203f at right
    show jenny f_upset a_dressed_crossed at flip
    show jenny at Position (xpos=200)
    show debbie 62f at left
    with dissolve
    deb "Вау!!"
    deb "Великолепная работа, {b}[firstname]{/b}!"
    show jenny f_upset_talk
    show debbie 61f
    jen "Закончил..."
    show jenny f_upset
    show debbie 62f
    deb "Не хами, {b}[jen_name]{/b}. Было мило с его стороны исправить это для нас..."
    show player 2f
    show debbie 61f
    player_name "Хех, никаких проблем."
    player_name "Я был счастлив сделать это."
    player_name "...Кроме того, {b}[jen_name]{/b} права. Исправлять подобные вещи теперь моя обязанность."
    show player 29f
    show jenny f_gross
    show debbie 62f
    deb "Однажды ты осчастливишь девушку и будешь хорошем мужем!"
    show player 203f
    show debbie 61f
    jen "Пфффф..."
    show jenny f_upset_talk
    jen "Не говори так, он зазнается!"
    show player 16f
    show jenny f_grin_talk
    jen "В конце концов, он все еще слабак."
    show player 15f
    show jenny f_grin
    show debbie 61f
    player_name "Я не слабак!"
    show player 16f
    show jenny f_grin_talk
    jen "Ха, какая разница, слабак!"
    show player 1f
    show jenny f_grin
    show debbie 62f
    deb "... Не слушай ее, {b}[firstname]{/b}. Она дразнит тебя только потому, что считает милым."
    show jenny f_angry_talk
    show debbie 59f
    jen "... Ага!"
    show player 11f
    show jenny f_eyeroll
    jen "... А сейчас вы двое можете выйти? Я весь день ждала, чтобы принять душ!"
    show jenny f_upset
    show debbie 60f
    show player 1f
    deb "Пойдем, {b}[firstname]{/b}. Пока Принцесса не заразила нас своим дурным настроением."
    show jenny f_grin_talk
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
    deb "...Ничего..."
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
    call scene_shower_with_vfx
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
    call scene_shower_with_vfx
    show debbies 37_36 at Position (xpos=474)
    pause 4.8
    show debbies 35
    player_name "Я люблю принимать душ с тобой, {b}[deb_name]{/b}"
    show debbies 76 with dissolve
    pause .1
    show debbies 41_76
    pause 4
    show debbies 42 at Position (xoffset=38)
    deb "Могу я помочь тебе опустить его?"
    show debbies 43 at Position (xoffset=38)
    deb "Так..."
    show debbies 44 at Position (xoffset=38)
    deb "Какие планы на сегодня?"
    show debbies 43 at Position (xoffset=38)
    deb "Что-нибудь веселое?"
    show debbies 72_71 at Position (xoffset=38)
    pause 4
    show debbies 45 at Position (xoffset=38) with dissolve
    deb "Ты весь напряжен. Теперь все зависит от тебя, милый..."
    show debbies 73 at Position (xoffset=38) with dissolve
    return

label shower_mom_sex_wash:
    player_name "На этот раз я хочу помыть тебя."
    show debbies 50 with dissolve
    deb "Давай, милый."
    show debbies 51
    pause 1
    show debbies 52_53_52_51
    pause
    show debbies 54
    player_name "Так приятно..."
    return

label shower_mom_sex_wash_handjob:
    show debbies 45 with dissolve
    pause .4
    show debbies 73_74
    pause
    show debbies 73
    player_name "{b}[deb_name]{/b}, я кончаю..."
    show debbies 47 at Position(xpos=526,ypos=768)
    player_name "Мммммммм!!!"
    show white zorder 4 with dissolve
    show debbies 47 at Position(xpos=526,ypos=768)
    show playersex 33 zorder 3 at Position(xpos=610,ypos=880)
    hide white with dissolve
    pause
    show debbies 48
    hide playersex
    with dissolve
    deb "Ммм, хороший мальчик."
    return

label shower_mom_sex_finger:
    player_name "Я еще не вымыл {b}везде{/b}..."
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
    show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
    $ animated = True
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [113,114], M_mom) as debbies at Position(xpos=513) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [113,114]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos=513) with dissolve
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_shower_blowjob_hscene_dialog")
        $ animcounter += 1
    call screen debbie_shower_blowjob_options

label debbie_shower_blowjob_hscene_dialog:
    if animcounter == 1 and randomizer() < 25:
        player_name "О, боже!{p=1}{nw}"
    if animcounter == 4 and randomizer() < 25:
        player_name "Я не могу-{p=1}{nw}"
    return

label debbie_shower_blowjob_cum_in:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "ХННГГГГ!!!"
    deb "( !!! )"
    show white with dissolve
    hide white with dissolve
    pause
    show debbies 117 at Position(xpos=523) with dissolve
    deb "ХММММПХ!!!"
    show debbies 118 at Position(xpos=516)
    deb "{b}*глоток*{/b}"
    show debbies 115 at Position(xpos=531)
    deb "... О, так много!"
    show debbies 110 at Position(xpos=512)
    player_name "Прости, {b}[deb_name]{/b}."
    show debbies 111
    deb "Нет, не извиняйся, милый."
    deb "I love the taste!"
    return

label debbie_shower_blowjob_cum_out:
    show debbies 113 at Position(xpos=513)
    pause .3
    show debbies 116 at Position(xpos=517)
    player_name "ХННГГГГ!!!"
    deb "( !!! )"
    show white with dissolve
    show debbies 115 at Position(xpos=531)
    show playersex 74 at Position(xpos=530,ypos=519)
    hide white with dissolve
    pause
    show playersex 75 at Position(xpos=574,ypos=655)
    deb "Хехехе, посмотри, что ты наделал с моим лицом!"
    deb "... я вся забрызгана..."
    player_name "Прости, {b}[deb_name]{/b}."
    deb "Все в порядке!"
    deb "Мы в душе, так что это легко очистить!"
    deb "... Просто помоги мне избавиться от этого в моих волосах."
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
            if not animated:
                show expression AnimatedImage("debbies", [59,60,61], M_mom) as debbies at Position(xpos = 688,ypos = 768)
                $ animated = True
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
    show debbies 34 at Position(xpos=474,ypos=768)
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

label shower_jenny_shower_spy_repeat:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, it's so steamy... )"
    player_name "( I can't quite make out- )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( Hello, {b}[jen_name]{/b}... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Oh, here we go. )"
        player_name "( I hope I haven't missed the show! )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Hehe, it's {b}[jen_name]{/b} again! )"
    else:
        player_name "( Whoa!! )"
        player_name "( It's {b}[jen_name]{/b}! )"
    pause

    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( I can't believe how much has happened between us! )"
        player_name "( A few weeks ago she would have freaked out about this but now... )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        pause
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( She should take her webcam in there with her, she'd probably make a fortune... )"
        pause
    else:
        player_name "( Oh man, she would be so pissed if she knew I was spying on her! )"
        pause

    if M_jenny.get('rng') > 75:
        show jenny b_shower_scene_a3
    elif 75 > M_jenny.get('rng') > 50:
        show jenny b_shower_scene_b3
    elif 50 > M_jenny.get('rng') > 25:
        show jenny b_shower_scene_c3
    else:
        show jenny b_shower_scene_e3
    with dissolve

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        player_name "( I can just walk in there and join her, whenever I want! )"
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( C'mon {b}[jen_name]{/b}, you know you want to... )"
    elif M_jenny.finished_state(S_jenny_talked_to_cedric):
        player_name "( Mmm, I could watch her scrub that body all- )"
    else:
        player_name "( It's a shame she's such a bitch all the time... )"
        player_name "( With a body like that, she could probably get any guy she wants. )"
        pause
        player_name "( I should get out of here before she catches me. )"
        pause
        scene black with fade
        jump jenny_shower_peep_end

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d1
    else:
        show jenny b_shower_scene_e_rub

    if M_jenny.finished_state(S_jenny_perv_on_tammy) and not M_jenny.get("first_shower_time"):
        pause
    elif M_jenny.finished_state(S_jenny_pissed_at_handjob) or store._in_replay is not None:
        player_name "( Bingo! )"
    else:
        player_name "( !!! )" with hpunch

    if M_jenny.get('rng') > 50:
        show jenny b_shower_scene_d_rub with dissolve
    return

label shower_jenny_shower_spy:
    call scene_shower_with_vfx_peep
    $ M_jenny.set('rng', randomizer())
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1_blurred f_empty a_empty
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1_blurred f_empty a_empty
    else:
        show jenny b_shower_scene_c1_blurred f_empty a_empty
    with dissolve
    pause
    player_name "( Hmm, it's so steamy... )"
    player_name "( I can't quite make out- )"
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a1
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b1
    else:
        show jenny b_shower_scene_c1
    show bathroom_door_left at Position (xoffset=-50)
    show bathroom_door_right at Position (xoffset=50)
    with dissolve
    player_name "( Whoa!! )"
    player_name "( It's {b}[jen_name]{/b}! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a2
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b2
    else:
        show jenny b_shower_scene_c2
    with dissolve
    player_name "( Oh man, she would be so pissed if she knew I was spying on her! )"
    pause
    if M_jenny.get('rng') > 66:
        show jenny b_shower_scene_a3
    elif 66 > M_jenny.get('rng') > 33:
        show jenny b_shower_scene_b3
    else:
        show jenny b_shower_scene_c3
    with dissolve
    player_name "( Just look at that body though! )"
    player_name "( She's like a perfect- )"
    show jenny b_shower_caught_front_surprised
    player_name "( !!! )" with hpunch
    jen "What the fuck, {b}[firstname]{/b}!!!"
    player_name "( Uh oh... )"

    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 6 at left
    show jenny b_towel a_towel_hit f_angry_talk at Position (xpos=350)
    with dissolve
    jen "You!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ack!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "Little!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ow!!"
    show jenny f_angry_talk a_towel_hit with dissolve
    jen "PERVERT!!!"
    show jenny f_angry a_towel_hit2 with dissolve
    player_name "Ouch!!"
    show player 12
    show jenny a_towel_hit
    with dissolve
    player_name "Stop hitting me!!!"
    show player 90
    hide jenny
    show jenny b_towel f_angry_talk a_towel_hips with dissolve
    jen "What the hell is the matter with you?!"
    show jenny f_angry
    show player 12
    player_name "Nothing, I just saw the door cracked and I-"
    show player 24
    show jenny f_angry_talk
    jen "... And you what?!"
    jen "Thought it was alright to peep on people in the shower?!"
    show jenny f_angry
    show player 25
    player_name "It's not like that..."
    show jenny f_gross
    pause
    show player 24
    pause
    player_name "Well, okay. It's a little like that but..."
    show jenny f_angry_talk
    jen "It's exactly like that, you pathetic little-"
    show jenny f_angry
    show player 10
    player_name "I'm sorry, alright?!"
    show player 5
    pause
    show jenny f_angry_talk
    jen "{b}*Sigh*{/b} Just get outta here or I'm telling {b}[deb_name]{/b}!"
    show jenny f_angry
    show player 23
    player_name "No, no, please don't tell {b}[deb_name]{/b}!"
    player_name "I'm leaving right now!"
    hide player with fastdissolve
    pause
    show jenny f_gross
    jen "( Grr, he's such a freaking loser! )"
    jen "( I just wanna wring his stupid neck! )"
    hide jenny with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
