label hospital_storage_no_access_card:
    scene hospital_lock
    player_name "Черт, заперто!"
    player_name "Похоже мне нужна {b}Карта доступа{/b} чтобы открыть эту дверь..."
    return

label hospital_storage_cabinet_dialogue:
    $ player.go_to(L_hospital_storagecabinet)
    if mrsj.started(mrsj_sex_ed) and not player.has_item("birth_control_pills"):
        call expression game.dialog_select("hospital_storage_cabinet_mrsj_sex_ed_started")
    $ player.location.call_screen(False)

label hospital_storage_cabinet_mrsj_sex_ed_started:
    scene hospital_cabinet_filled
    player_name "Хмм..."
    player_name "Здесь несколько видов таблеток."
    player_name "Может, эта зелёная коробка?"
    return

label roz_storage_sex:
    $ M_roz.set("fun time", False)
    $ game.timer.tick()
    scene location_hospital_sex with fade
    if M_roz.is_state(S_roz_end):
        call expression game.dialog_select("roz_storage_sex_pre_repeat")
    else:

        call expression game.dialog_select("roz_storage_sex_pre_first")
    call expression game.dialog_select("roz_storage_sex_pre_after")
    $ anim_toggle = True
	$ animated = False
    jump expression game.dialog_select("roz_storage_sex_loop")

label roz_storage_sex_pre_repeat:
    show player 11f at Position(xpos=.7,ypos=1.0)
    pause
    show roz 4 at left with dissolve
    show player 13f
    pause
    show roz 5
    roz "Удивлена увидеть тебя так быстро. Я долженf оставить впечатление."
    show player 14f
    show roz 4
    player_name "Д...даа. Ты была действительно хороша!"
    show player 13f
    show roz 5
    roz "Хех, тебе повезло узнать некоторые хитрости будучи ещё молодым, малыш."
    show roz 8
    pause
    show roz 9
    roz "Нусс...тогда..."
    hide roz
    hide player
    show roz 16 at right with dissolve
    show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
    pause
    show roz 17
    pause
    show roz 18
    pause
    show player 80
    pause
    show roz 19
    roz "Почему бы тебе не достать своего великана чтобы мы могли начать."
    show player 83
    player_name "Да, Мадам!"
    hide player with dissolve
    show roz 18
    show player 480 at Position(xpos=.35,ypos=1.0)
    pause
    show roz 19
    roz "Малыш, ты действительно хорош."
    show roz 18
    show player 482
    pause
    show roz 19
    roz "Только не забудь кончить в меня..."
    show roz 18
    show player 481
    player_name "Д...да, Мадам!"
    show player 483 at Position (xpos=.36,ypos=1.0)
    show roz 19
    roz "Хороший мальчик..."
    return

label roz_storage_sex_pre_first:
    show player 12 at center with dissolve
    player_name "Я помню, {b}Роз{/b} говорила что коробка здесь."
    show player 11 zorder 2
    player_name "Но я её не вижу. Возможно, она её переложила и забыла?"
    show roz 5 zorder 1 at left with dissolve

    roz "Нужна помощь?"
    show player 23f at Position(xpos=.7,ypos=1.0)
    show roz 4
    player_name "Ааааа!"
    show player 22f
    player_name "..."
    show player 10f
    player_name "Уфф, здра-здрасти, {b}Роз{/b}. Вы меня напугали!"
    show player 11f
    show roz 5
    roz "Ахх, не будь таким смешным! Я пришла тебе помочь."
    show player 10f
    show roz 4
    player_name "Ага, хорошо. Эмм, вы говорили что коробка тут, но я её не нахужу."
    show player 11f
    show roz 5
    roz "Не нашёл? Странно."
    roz "Возможно, что я не помню куда положила, но помню, что приносила ее сюда."
    roz "Моя память не настолько хороша как в былые времена."
    show roz 4
    player_name "..."
    show player 10f
    player_name "Ну ничего страшного. Спущусь по лестнице-"
    show player 22f
    show roz 6

    player_name "!!!" with hpunch
    show roz 7
    roz "Куда торопишься?"
    roz "Кажется у нас есть время уединиться в этой комнате..."
    roz "И я думаю, что ты сможешь что-то сделать для меня."
    show player 38f
    show roz 6
    player_name "О, да, конечно. Что ты имела в виду?"
    show player 3f
    show roz 7
    roz "Так, короче, {b}[firstname]{/b}."
    roz "Если ты понимаешь, то у ласточки что перед тобой же долгое время не было удовольствия."
    show player 10f
    show roz 6
    player_name "Эээ, ууудовольствия?"
    show player 11f
    show roz 7
    roz "Ну да."
    show roz 10
    pause


    show roz 8
    pause
    show player 23f
    player_name "!!!" with hpunch
    show player 42f
    player_name "Эй! {b}Роз{/b}, что вы делаете?"
    show roz 9
    roz "Ты что, дурак? А на что это похоже?"
    roz "Снимай одежду, и посмотри что для тебя ТАМ, внизу."
    show player 10f
    show roz 8
    player_name "Подождите, вы что хотите--Н-но я НЕ МОГУ!"
    show player 11f
    show roz 9
    roz "Что? Тебе нужны эти {b}записи{/b} или нет?"
    show player 10f
    show roz 8
    player_name "Нуууу да, нужны, но-"
    show player 11f
    show roz 9
    roz "И чего ты сейчас впустую балтаешь? Ты поможешь мне, я тебе. Договорились?"
    show player 24f
    show roz 8
    player_name "Я...я...ай, ладно, согласен."
    show roz 9
    roz "Вот и славненько!"
    hide roz
    hide player
    show roz 16 at right with dissolve
    show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
    pause
    show roz 17
    pause
    show roz 18
    pause
    show player 78
    pause
    show roz 19
    roz "Да, я хочу получить удовольствие."
    show player 80
    show roz 18
    pause
    show roz 19
    roz "И чего тормозим?"
    show player 83
    player_name "Матерь Божья..."
    hide player with dissolve
    show roz 18
    show player 480 at Position(xpos=.35,ypos=1.0)
    pause
    show roz 19
    roz "Афигеть! Какой монстр!"
    show roz 18
    show player 482
    pause
    show roz 19
    roz "Я думаю это была хорошая мысль!"
    show roz 18
    pause
    show roz 19
    roz "Подходи сюда, и дай тёте {b}Розе{/b} то чего ей не хватало."
    show roz 18
    show player 481
    player_name "Л...ладно!"
    show player 483 at Position (xpos=.36,ypos=1.0)
    show roz 19
    roz "Хороший мальчик..."
    return

label roz_storage_sex_pre_after:
    scene location_hospital_sex
    $ M_roz.set("sex speed", .175)
    show expression AnimatedImage("rozs", [1,2,3,4,5,6,7], M_roz) as rozs at right
    with fade
    roz "Да, малыш, глубже."
    pause
    roz "О, дааааа..."
    pause
    roz "О последствиях не волнуйся."
    roz "Мне уже нечего бояться, поэтому можно полностью насладиться процессом."
    $ M_roz.set("sex speed", .125)
    roz "Да, вот так!"
    pause
    roz "Давай, малыш, сильнее!"
    $ M_roz.set("sex speed", .075)
    return

label roz_storage_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
		if not animated:
            show expression AnimatedImage("rozs", [1,2,3,4,5,6,7], M_roz) as rozs at right
            $ animated = True
			pause 5
            call expression game.dialog_select("roz_storage_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "rozs {}".format(pose_list[pose_counter]) as rozs at right
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("roz_storage_hscene_dialog")
        $ animcounter += 1
    call screen roz_storage_sex_options

label roz_storage_hscene_dialog:
    if animcounter == 1:
        roz "Аххх!!!{p=1}{nw}"

    elif animcounter == 3:
        roz "Ох!!!{p=1}{nw}"
        player_name "Уххх...{p=1}{nw}"
    return

label roz_storage_sex_cum:
    call expression game.dialog_select("roz_storage_sex_cum_pre")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roz"]["unlocked"] = True
    $ persistent.cookie_jar["Roz"]["gallery"]["01_unlocked"] = True
    scene location_hospital_sex with fade
    if M_roz.is_state(S_roz_end):
        call expression game.dialog_select("roz_storage_sex_cum_after_repeat")
    else:

        call expression game.dialog_select("roz_storage_sex_cum_after_first")
        $ player.get_item("obituary_records")
        $ M_roz.trigger(T_roz_fuckery)
    $ M_roz.unforce()
    $ game.main()

label roz_storage_sex_cum_pre:
    player_name "Роз, я скоро кончу... Н-немогу дольше."
    roz "Да, малыш, кончай в меня!"
    pause
    roz "Оооо, как хорошо!!!"
    show rozs 8_9 with flash
    player_name "УХХХ!!!"
    roz "AAAAХХХ!!!!"
    pause
    hide rozs
    show player 482 zorder 2 at Position(xpos = .36, ypos = 1.0)
    show roz 18 zorder 1 at right
    show rozs 144 zorder 3 at Position(xpos = .5155, ypos = .895)
    show players 143 zorder 4 at Position(xpos = .435, ypos = .8625)
    pause
    show roz 19
    roz "*хрипло* ... Вауу."
    roz "Дорогуша... *кашель* Это было просто отпадно, {b}[firstname]{/b}!"
    show roz 18
    show player 481
    player_name "Д-да..."
    show player 482
    show roz 19
    roz "Просто дай мне немного времени... перевести дыхание."
    scene black with fade
    return

label roz_storage_sex_cum_after_repeat:
    show player 1f at Position(xpos=.7,ypos=1.0) with dissolve
    show roz 13 at left with dissolve
    pause
    show roz 15
    roz "Ты сегодня был молодцом, малыш."
    roz "Улучшения прям на виду."
    show player 29f
    show roz 14
    player_name "Правда? Хе, Спасибо. Я пологаю..."
    show player 3f
    show roz 15
    roz "С удовольствием, {b}[firstname]{/b}."
    roz "Приходи ещё, и опять сможешь поиметь {b}Роз{/b} . Хорошо?"
    show player 29f
    show roz 14
    player_name "К...конечно."
    hide roz
    hide player
    with dissolve
    return

label roz_storage_sex_cum_after_first:
    show player 5f at Position(xpos=.7,ypos=1.0)
    show roz 4 at left
    pause
    show roz 12
    roz "Вот эти записи."
    show player 12f
    show roz 11
    player_name "Они были у вас всё это время?!"
    show player 462
    show roz 5
    roz "Конечно, я же говорила что знаю где они."
    show roz 4
    player_name "..."
    show roz 5
    roz "Только я не знаю какое имя ты ищешь..."
    roz "Но если его хоронили на {b}нашем кладбище{/b}, то оно будет в этих {b}записях{/b}."
    show roz 13
    pause
    show player 463
    show roz 14
    player_name "...Спасибо."
    show player 462
    show roz 15
    roz "С большим удовольствием, малыш."
    roz "Приходи ко мне ещё, если тебе что-то будет нужно."
    show roz 14
    pause
    show roz 15
    roz "И сможем запустить второй раунд? Хех!"
    show roz 14
    hide roz with dissolve
    pause
    show player 37f
    player_name "( Я... Это просто пиздец... у меня был секс с {b}Роз{/b}. )"
    player_name "( Она старше моей бабушки... )"
    show player 24f
    player_name "( Ну по крайней мере я получил {b}Записи о захоронениях{/b}. )"
    player_name "( Я надеюсь что там будет запись о судостроителе. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
