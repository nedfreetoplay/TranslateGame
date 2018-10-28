label yoga_room_mrsj_yoga_help_started:
    if M_anna.is_state(S_anna_start):
        $ M_anna.trigger(T_anna_intro)

    scene yoga_room_night
    if yoga_fail_retry:
        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_pre_repeat")
    else:

        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_pre_first")

    label anna_yoga_lesson:
        call expression game.dialog_select("yoga_room_mrsj_yoga_help_started_intro")
    $ yoga_position = ""
    $ yoga_stage = 1
    $ boner_fail = False
    $ game.timer.tick()
    label yoga_room_class:
        call expression game.dialog_select("yoga_room_class_position_pre")
    menu:
        "Счастливый малыш." if store._in_replay == None or yoga_stage == 2:
            $ yoga_position = "Счастливый малыш"
            if yoga_stage == 2:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_2nd_position_success")
                jump expression game.dialog_select("yoga_room_class")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "Позиция плуг." if store._in_replay == None or yoga_stage == 3:
            $ yoga_position = "Позиция плуг"
            if yoga_stage == 3:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_3rd_position_success")
                call expression game.dialog_select("yoga_room_class_success")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "Нисходящая собака." if store._in_replay == None or yoga_stage == 1:
            $ yoga_position = "Нисходящая собака"
            if yoga_stage == 1:
                $ yoga_stage += 1
                call expression game.dialog_select("yoga_room_class_1st_position_success")
                jump expression game.dialog_select("yoga_room_class")
            else:

                call expression game.dialog_select("yoga_room_class_failure")

        "Конец урока." if store._in_replay == None and mrsj.completed(mrsj_yoga_help):
            call expression game.dialog_select("yoga_room_class_end_lesson")
    $ game.main()

label yoga_room_mrsj_yoga_help_started_pre_repeat:
    show player 385 at left with dissolve
    show anna 2 at right with dissolve
    anna "Готов попробовать еще раз?"
    show anna 1
    show player 386
    player_name "Я думаю я должен запомнить позиции в этот раз."
    show player 385
    anna "Просто скажи мне какие позиции делать и я последую твоему примеру."
    return

label yoga_room_mrsj_yoga_help_started_pre_first:
    show player 380 at left with dissolve
    show anna 12 at right with dissolve
    if not M_anna.is_state(S_anna_start):
        anna "Прошу прощения?"
    else:
        "Прости?"
    show player 385
    if not M_anna.is_state(S_anna_start):
        anna "Ты не видел {b}Тэмми{/b} в последнее время?"
    else:
        "Ты не видел {b}Тэмми{/b} в последнее время?"
    show anna 11
    show player 384
    player_name "На самом деле, она не сможет прийти сегодня вечером."
    show player 386
    player_name "Она послала меня помочь обучить её группу..."
    show player 385
    show anna 12
    if not M_anna.is_state(S_anna_start):
        anna "Ох, она рассказала тебе что надо делать, {b}[firstname]{/b}?"
    else:
        "Ох, она рассказала тебе что надо делать?"
    show anna 11
    show player 386
    player_name "Ну, {b}Миссис Джонсон{/b} дала мне этот список с указаниями."
    show player 381
    player_name "Я посмотрел их немного... Думаю,я справлюсь."
    if not M_anna.is_state(S_anna_start):
        show player 386
        player_name "Она сказала что ты может быть сможешь помочь мне?"
        show player 385
        show anna 2 with dissolve
        anna "Конечно я помогу тебе!"
        anna "И не волнуйся! Просто скажи мне какие позиции делать и я последую твоему примеру."
    else:

        show player 384
        player_name "Ты не видела девушку по имени, {b}Анна{/b}?"
        player_name "{b}Миссис Джонсон{/b} сказала что она сможет помочь мне."
        show player 385
        show anna 3 with dissolve
        anna "Я - {b}Анна{/b}!!"
        show anna 1
        show player 386
        player_name "Ох!!"
        show player 385
        show anna 3
        anna "Я надеялась ты знаешь что ты делаешь. Ха ха!"
        show anna 2
        anna "Я здесь что бы помочь тебе с движениями, не волнуйся."
    return

label yoga_room_mrsj_yoga_help_started_intro:
    hide player
    hide anna
    scene black
    with fade
    scene yoga_front
    show anna 14
    show player 411 at left
    with dissolve
    player_name "Хмм..."
    show player 412
    player_name "Хорошо, нам нужно сделать 3 последовательные позиции, в нужном порядке..."
    show player 411
    show anna 13
    anna "Мммм.. Ты готов?"
    show anna 14
    show player 414 with dissolve
    player_name "Думаю,да?"
    show player 413
    show anna 13
    anna "Что ж, Что ж, с какой позы мы начнём?"
    show anna 14
    show player 412 with dissolve
    return

label yoga_room_class_position_pre:
    if yoga_stage == 1:
        call expression game.dialog_select("yoga_room_class_1st_position_pre")

    elif yoga_stage == 2:
        call expression game.dialog_select("yoga_room_class_2nd_position_pre")

    elif yoga_stage == 3:
        $ boner_fail = True
        call expression game.dialog_select("yoga_room_class_3rd_position_pre")
    return

label yoga_room_class_1st_position_pre:
    player_name "Первая позиция это..."
    return

label yoga_room_class_2nd_position_pre:
    player_name "Хорошо, для второй позиции, я думаю нам стоит попробовать..."
    return

label yoga_room_class_3rd_position_pre:
    player_name "Последняя позиция должна делаться вот так..."
    return

label yoga_room_class_failure:
    call expression game.dialog_select("yoga_room_class_failure_dialogue")
    return

label yoga_room_class_failure_dialogue:
    if boner_fail:
        show player 419 at left
        show anna 21
    else:
        show player 418 at left
    with dissolve
    player_name "Ммм... Я думаю {b}[yoga_position]{/b} это следующая позиция."
    player_name "Я не совсем уверен."
    player_name "Я не могу вспомнить..."
    if boner_fail:
        show player 420
    else:
        show player 417
    show anna 13 with dissolve
    if mrsj.started(mrsj_yoga_help):
        anna "Наверно будет лучше если мы просто пропустим занятия класса на сегодня."
    anna "Мы можем попробовать еще раз завтра снова."
    if boner_fail:
        show player 419
    else:
        show player 418
    show anna 14
    player_name "Да..."
    player_name "Извини."
    if boner_fail:
        show player 420
    else:
        show player 417
    show anna 13
    if mrsj.started(mrsj_yoga_help):
        anna "Просто взгляни на заметки {b}Тэмми{/b} и постарайся их запомнить на следующий раз."
    else:
        anna "Просто взгляни на заметки {b}Тэмми{/b} и постарайся их запомнить на следующий раз."
    if boner_fail:
        show player 419
    else:
        show player 418
    show anna 14
    player_name "Хорошо. Я очень постараюсь..."
    hide anna
    hide player
    with dissolve
    scene yoga_room_night
    show player 24 with dissolve
    player_name "Блин... Я не смог этого сделать."
    if mrsj.started(mrsj_yoga_help):
        player_name "Я должен запомнить все движения и попытаться еще раз завтра."
        show player 25
        player_name "Я не могу позволить чтобы {b}Миссис Джонсон{/b} и {b}Анна{/b} вот так разочеровались во мне..."
    else:
        player_name "Я должен запомнить все движения и попытаться еще раз завтра."
    hide player with dissolve
    return

label yoga_room_class_1st_position_success:
    show player 414 with dissolve
    player_name "Нам нужно сделать {b}[yoga_position]{/b}?"
    show player 413
    show anna 15
    anna "Ах да.Я люблю эту позицию!"
    show anna 18 with dissolve
    anna "Почему нет я могла бы лечь на коврик и ты мог бы помочь мне с растяжкой?"
    show anna 17
    show player 416
    player_name "Охх... Хорошо."
    hide player
    show anna 19
    with dissolve
    pause
    pause
    anna "Не стенсняйся применить силу к своим толчкам!"
    show anna 19_20
    pause
    show player 411 at left
    show anna 18
    with dissolve
    anna "Это было отлично!Я уже чувствую себя намного гибче!"
    show anna 17
    show player 412
    return

label yoga_room_class_2nd_position_success:
    player_name "...эта {b}[yoga_position]{/b}?"
    show player 413 with dissolve
    show anna 18
    anna "Разумеется!"
    anna "Эта одна из моих любимых."
    anna "Позволь мне лечь на спину так что ты сможешь давить и растягивать мои ножки..."
    show anna 21 with dissolve
    show player 416
    player_name "!!!"
    hide player
    show anna 23
    with dissolve
    player_name "Давить твои ноги?"
    show anna 24
    anna "Да"
    anna "Просто дави их назад чтобы я могла растянуться..."
    show anna 25 with dissolve
    pause
    pause
    pause
    show anna 27 with dissolve
    anna "Это был прекрасно..."
    show anna 28
    player_name "..."
    anna "Ох!!"
    show anna 26
    player_name "Ха ха! Я думаю мы готовы для последней позиции!"
    return

label yoga_room_class_3rd_position_success:
    player_name "...эта {b}[yoga_position]{/b}?"
    show anna 27
    anna "Идеально!"
    show player 420 at left
    show anna 29
    with dissolve
    pause
    show anna 30
    anna "Все что тебе нужно сделать это  давить на ... тазовую область против моей задницы."
    show anna 29
    show player 421
    player_name "Мммм... Хорошо..."
    hide player
    show anna 31
    with dissolve
    pause
    show anna 32
    anna "Ахх, да!"
    hide anna
    show anna_slow 31_32
    pause
    anna "Еще чуть-чуть !!"
    hide anna_slow 31_32
    show anna_fast 31_32
    pause
    hide anna_fast 31_32
    return

label yoga_room_class_success:
    call expression game.dialog_select("yoga_room_class_success_pre")
    if store._in_replay == None:
        if mrsj.completed(mrsj_yoga_help):
            $ game.main()
        $ M_mrsj.unforce()
        $ mrsj_yoga_help.finish()
        $ mrsj.add_event(mrsj_yoga_help_2)

    call expression game.dialog_select("yoga_room_class_success_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Anna"]["unlocked"] = True
    $ persistent.cookie_jar["Anna"]["gallery"]["01_unlocked"] = True
    show unlock43 at truecenter with dissolve
    pause
    hide unlock43 with dissolve
    $ A_yoga_apprentice.unlock()
    return

label yoga_room_class_success_pre:
    show player 420 at left
    show anna 22
    with dissolve
    anna "Это было... прекрасно!"
    show anna 21
    show player 419
    player_name "Я... прости за..."
    show player 420
    show anna 15 with dissolve
    anna "Ох! Ха ха!"
    show anna 13
    anna "Все нормально!"
    anna "Это всегда происходит с парнями которые приходят в наш класс!"
    show anna 16
    anna "И я не была против дополнительной... давки..."
    return

label yoga_room_class_success_after:
    scene yoga_room_night
    show player 82 at left
    show anna 2 at right
    with dissolve
    anna "Я впечатлена!"
    anna "Ты проделал отличную работу..."
    show anna 3
    anna "...И мне очень понравилось быть твоей помощницей!"
    show anna 1
    show player 83
    player_name "Я просто пытался помочь {b}Миссис Джонсон{/b}."
    show player 79 with dissolve
    player_name "Это было и в правду довольно весело."
    show player 82 at left with dissolve
    show anna 2
    anna "Будем надеяться, что ты скоро придешь снова для обучения класса... с моей помощью?"
    anna "То есть... если ты захочешь..."
    show anna 1
    show player 79 with dissolve
    player_name "Это может быть весело!"
    show player 82 at left with dissolve
    show anna 2
    anna "Просто убедись что ты пришёл ночью."
    anna "Это когда {b}Тэмми{/b} уходит и мне нужна помощь..."
    show anna 1
    show player 83
    player_name "Эмм... Конечно."
    hide player
    hide anna
    with dissolve
    return

label yoga_room_class_end_lesson:
    scene yoga_room_night
    if boner_fail:
        show player 82 at left
        show player 79
    else:
        show player 14 at left
    show anna 1 at right
    with dissolve
    player_name "Это было весело!"
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 3
    anna "Да!"
    show anna 2
    anna "Ты уверена что ты хорошо провел время. Я впечатлена!"
    show anna 1
    if boner_fail:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Спасибо!"
    player_name "Я просто пытался помочь."
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 2
    anna "Я была бы не против позаниматься еще раз с тобой..."
    anna "...Если ты захочешь."
    show anna 1
    if boner_fail:
        show player 79 with dissolve
    else:
        show player 14
    player_name "Конечно!"
    if boner_fail:
        show player 82 at left with dissolve
    else:
        show player 13
    show anna 2
    anna "Круто! Увидимся в следующий раз..."
    hide player
    hide anna
    with dissolve
    return

label yoga_room_strangers_only:
    scene expression game.timer.image("yoga_room{}")
    show player 12
    with dissolve
    player_name "( Здесь никого нет из моих знакомых... )"
    show player 35
    player_name "( Возможно,я должен придти в другой раз... )"
    hide player 35 with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
