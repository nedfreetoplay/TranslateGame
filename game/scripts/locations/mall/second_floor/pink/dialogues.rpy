label pink_first_visit:
    scene pink
    show player 23 with dissolve
    player_name "( Вау! )"
    show player 21
    player_name "( Это... Здесь много странных вещей. )"
    show player 29
    player_name "( Хммм... Может быть, это пригодится в один прекрасный день... )"
    hide player 29 with dissolve
    return

label pink_mia_helen_outfit_request:
    scene pink
    show player 12 with dissolve
    player_name "Я должен осмотреть эту стойку одежды..."
    player_name "...У них должен быть выбор нижнего белья."
    hide player with dissolve
    return

label pink_mia_angelicas_whip:
    scene pink with fade
    show player 12 with dissolve
    player_name "Здесь должно быть что-то похожее на {b}Хлыст{/b}..."
    hide player with dissolve
    return

label ivy_paizuri:
    call expression game.dialog_select("ivy_paizuri_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_paizuri_first")
        $ M_ivy.set("first visit", False)
    else:

        call expression game.dialog_select("ivy_paizuri_repeat")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = False
    $ xray_needed = False
    jump expression game.dialog_select("ivy_paizuri_loop")

label ivy_paizuri_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Я попробую основное."
    ivy "Тестирование воды, хм?"
    show player 29
    player_name "Я эмм..."
    show ivy 3
    ivy "Хех, Я просто дразню!"
    show ivy 12
    ivy "Следуй за мной."
    scene massage_room_closeup with fade
    show player 1 at left
    show ivy 2 at right
    with dissolve
    return

label ivy_paizuri_first:
    show player 43
    player_name "{b}*Свист*{/b} Крутая комната."
    show player 1
    show ivy 3 with dissolve
    ivy "{b}*Хихиканье*{/b} Будет еще круче когда мы только начнем."
    show ivy 2
    ivy "Сейчас, раздевайся и ложись на кравать. Ты можешь положить свои вещи на стол."
    ivy "Я дам тебе пару минут чтобы подготовиться."
    ivy "Нужно убедиться что никто нам не помешает..."
    hide ivy with dissolve
    show player 18
    player_name "( Фух! Это было гораздо менее неловко чем я мог ожидать! )"
    scene massage_room_closeup with fade
    show player 175 at left
    with dissolve
    player_name "( Я не ожидал что это будет так просто, хотя... )"
    show player 57
    player_name "( Действительно ли я готов к этому? )"
    player_name "( ...Я не могу остановиться. )"
    show player 175
    player_name "( Нужно просто наслаждаться этим. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    with dissolve
    ivy "{b}*Хихиканье*{/b} Почему ты все еще так одет?"
    ivy "Нам не нужны полотенца для этого вида массажа."
    player_name "Ох. Извини..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "Вот! Так намного лучше не так ли?"
    player_name "Да, так и есть."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "Как, черт возьми, ты прячешь эту штуку?"
    ivy "В любом случае: моё имя Айви."
    ivy "Сейчас, моя очередь подготовиться..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Нравится что ты видишь?"
    player_name "Да..."
    ivy "{b}*Смех*{/b} Что ж, твоему другу тоже похоже Нравится."
    ivy "Я думаю, мне придется позаботиться об этом..."
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 7 with dissolve
    ivy "Прежде чем мы начнем, я должна тебе кое-что сказать..."
    ivy "Этот комната звукоизолирована..."
    player_name "( Ох? )"
    ivy "...Так что тебе не надо ничего сдерживать."
    ivy "А сейчас, просто расслабься..."
    return

label ivy_paizuri_repeat:
    show player 1
    ivy "Ты знаешь правила. Я вернусь через минуту."
    hide ivy with dissolve
    pause 0.5
    hide player with dissolve
    scene massage_room with fade
    show playersex 19 zorder 1
    with dissolve
    pause 2
    show ivy 18 at Position (xpos=870,ypos=655) with dissolve
    ivy "Хорошо! Можем начинать!"
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Давай сделаем это!"
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 6
    return

label ivy_paizuri_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("ivysex", [6,5], M_ivy) as ivysex zorder 2
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [6,5]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_paizuri_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_paizuri_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["01_unlocked"] = True
    $ game.main()

label ivy_paizuri_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 5
        ivy "Держу пари что это не так Хорошо когда ты используешь свою руку..."
        if not anim_toggle:
            show ivysex 6
        player_name "( И рядом не было! )"
        if not anim_toggle:
            show ivysex 5
        player_name "Быстрее..."
        if not anim_toggle:
            show ivysex 6

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 5
        ivy "Ты-{b}*Пыхтишь*{/b}-уже близко?"
        if not anim_toggle:
            show ivysex 6
        player_name "Да..."
        ivy "Тогда давайте включим высокую передачу!"
        player_name "Аааах-собираюсь..."

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 5
        player_name "...Собираюсь...КОНЧИТЬ!"
        show ivysex 7
        ivy "Сделай это!"
        show white zorder 4 with dissolve
        hide white with dissolve
        show expression "characters/player/char_player_sex_25.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_26.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_27.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        show expression "characters/player/char_player_sex_28.png" as playersex_cum zorder 3
        with Dissolve(0.3)
        ivy "Вау.... тут так много..."
        ivy "Тебе понравилось?"
        player_name "Да... ты в этом хороша."
        ivy "{b}*Хихиканье*{/b} Я знаю."
        ivy "Такой беспорядок но..."
        ivy "Давай приведем себя в порядок."
    return

label ivy_blowjob:
    call expression game.dialog_select("ivy_blowjob_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_blowjob_first")
        $ M_ivy.set("first visit", False)
    else:

        call expression game.dialog_select("ivy_blowjob_repeat")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = False
    $ xray_needed = False
    jump expression game.dialog_select("ivy_blowjob_loop")

label ivy_blowjob_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Да. Я бы хотел классику,пожалуйста."
    ivy "Ох? смотришь на мои губы?"
    show player 29
    player_name "Я Ээээ..."
    show ivy 3
    ivy "Расслабься, Я просто дурачусь!"
    show ivy 12
    ivy "Иди за мной."
    scene massage_room_closeup with fade
    show player 1 at left
    show ivy 3 at right
    with dissolve
    ivy "Хорошо, Я просто удостоверюсь что никто нам не помешает."
    return

label ivy_blowjob_first:
    show player 43
    player_name "{b}*Свист*{/b} Крутая комната."
    show player 1
    ivy "{b}*Хихиканье*{/b} Будет еще круче когда мы начнем."
    show ivy 2
    ivy "Сейчас, раздевайся и ложись на кравать. Ты можешь положить свои вещи на стол."
    ivy "Я дам тебе пару минут чтобы подготовиться."
    ivy "Нужно убедиться что никто нам не помешает..."
    hide ivy with dissolve
    show player 18
    player_name "( Фух! Это было гораздо менее неловко чем я мог ожидать! )"
    show player 175 with dissolve
    player_name "( Я не ожидал что это будет так просто, хотя... )"
    show player 57
    player_name "(  Действительно ли я готов к этому? )"
    player_name "( ...Нет, Я не могу повернуть назад. )"
    show player 175
    player_name "( Можно просто наслаждаться этим. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    with dissolve
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    ivy "{b}*Хихиканье*{/b} Почему ты все еще так одет?"
    ivy "Нам не нужны полотенца для этого вида массажа."
    player_name "Ой, Извини..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "Вот! Так намного лучше, не так ли?"
    player_name "Да, так и есть."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "Как, черт возьми, ты прячешь эту штуку?"
    ivy "В любом случае: моё имя Айви."
    ivy "Сейчас, моя очередь подготовиться..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Нравится что ты видишь?"
    player_name "Да..."
    ivy "{b}*Хихиканье*{/b} Что ж, твоему другу тоже похоже Нравиться."
    ivy "Я думаю, мне придется позаботиться об этом..."
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 2 with dissolve
    ivy "Прежде чем мы начнем, я должна тебе кое-что сказать."
    ivy "Этот комната звукоизолирована..."
    player_name "( Оу? )"
    ivy "...Так что тебе не надо сдерживаться."
    ivy "Ох,и дай мне знать когда ты будешь близок, Хорошо?"
    player_name "Конечно."
    ivy "А сейчас, просто ляг и расслабься..."
    return

label ivy_blowjob_repeat:
    ivy "Ты знаешь правила.Я вернусь через минуту."
    hide ivy with dissolve
    pause 0.5
    hide player
    scene massage_room
    show playersex 19 zorder 1
    with dissolve
    pause 2
    show ivy 18 at Position (xpos=870,ypos=655) with dissolve
    ivy "Хорошо! Можем начинать!"
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    ivy "Давай сделаем это!"
    hide ivy
    show ivysex 1 zorder 2
    with dissolve
    show ivysex 2
    return

label ivy_blowjob_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("ivysex", [4,3], M_ivy) as ivysex zorder 2
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [4,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_blowjob_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_blowjob_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["02_unlocked"] = True
    $ game.main()

label ivy_blowjob_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 3
        player_name "( Блин, если ее рот вызывает такие хорошие ощущения, настоящий секс должен быть безумным... )"
        if not anim_toggle:
            show ivysex 4
        player_name "Аааах... Быстрее..."

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 3
        player_name "( Дерьмо, Я уже близко... )"
        if not anim_toggle:
            show ivysex 4
        player_name "Быстрее."

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 3 zorder 2
        player_name "( Нужно её предупредить... )"
        if not anim_toggle:
            show ivysex 4
        player_name "Я вот вот-"
        show ivysex 3
        player_name "ДЕРЬМО!"
        show white zorder 4 with dissolve
        hide white
        show ivysex 24
        with dissolve
        show ivysex 25 with dissolve
        player_name "Я Эммм..."
        show ivysex 26
        ivy "{b}*Кашель*{/b} {b}*Кажель*{/b}"
        ivy "Что случилось со всем этим \"ты не мог мне дать знать\" раньше?"
        player_name "Эмм, я сожалею об этом..."
        ivy "Ты знаешь, обычно я беру дополнительную плату за глотание."
        player_name "Я..."
        player_name "( Дерьмо, может быть мне не стоило этого делать. )"
        show ivysex 1
        ivy "{b}*Хихиканье*{/b} Ох парень, ты бы видел вырожение своего лица!"
        ivy "Не волнуйся об этом, ты хорошо потренировался! Это за счет заведения."
        player_name "*нервный смех* Спасибо."
        player_name "Еще раз, извини за это..."
        ivy "Серьезно,все хорошо... Ты знаешь, Мои обычные клиенты обычно не выпускают там много {b}тепла{/b}."
        player_name "Ох, эм, спасибо, Я думаю."
        ivy "Теперь, давай приведем себя в порядок."
    return

label ivy_reverse_cowgirl:
    call expression game.dialog_select("ivy_reverse_cowgirl_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_reverse_cowgirl_first")
        $ M_ivy.set("first visit", False)
    call expression game.dialog_select("ivy_reverse_cowgirl_after")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = False
    $ ivy_cum_inside = False
    $ xray_needed = True
    jump expression game.dialog_select("ivy_reverse_cowgirl_loop")

label ivy_reverse_cowgirl_pre:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Да, Я попробую премиум, пожалуйста."
    ivy "Ох-ох, довольно смело для твоего возраста!"
    show player 29
    player_name "Я эмм..."
    show ivy 3
    ivy "{b}*Хихиканье*{/b} Мне нравятся нетерпиливые мужчины!"
    show ivy 2
    ivy "Иди за мной."
    scene massage_room_closeup with fade
    show ivy 2 at right
    show player 43 at left
    with dissolve
    ivy "Хорошо, Я просто удостоверюсь что нам никто не помешает."
    return

label ivy_reverse_cowgirl_first:
    player_name "{b}*Свист*{/b} Крутая комната."
    show player 1
    show ivy 3 at right
    ivy "{b}*Хихиканье*{/b} Это будет еще круче, как только мы начнем."
    show ivy 2
    ivy "Сейчас, раздевайся и ложись на кровать. Ты можешь положить свою одежды на стол."
    ivy "Я дам тебе пару минут чтобы подготовиться."
    ivy "Нужно убедиться, что никто не помешает."
    hide ivy 2 with dissolve
    show player 18
    player_name "( Уф, это было менее неловко, чем я ожидал! )"
    show player 175 with dissolve
    player_name "( Я не ожидал, что это будет так просто ... )"
    show player 57
    player_name "( Действительно ли я готов к этому? )"
    player_name "( ...Нет, Я не могу повернуть назад сейчас. )"
    show player 175
    player_name "(Нужно просто наслаждаться этим.. )"
    hide player with dissolve
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    with dissolve
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
    ivy "{b}*Хихиканье*{/b} Почему ты все еще так одет?"
    ivy "Нам не нужны полотенце для этого вида массажа."
    player_name "Ох, извини..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "Вот так! Намного лучше, не так ли?"
    player_name "Да, так и есть."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "Как, черт возьми, ты прятал эту штуку?"
    ivy "В любом случае: меня зовут Айви."
    ivy "Теперь, моя очередь подготовиться..."
    return

label ivy_reverse_cowgirl_after:
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "Для этого нам понадобится презерватив."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Ой, блин..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "О не волнуйся! ты даже не заметишь что он там. Верь мне."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "И для заключительной части..."
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 15 zorder 2
    with dissolve
    pause
    show ivysex 16 with dissolve
    pause
    show ivysex 17 with dissolve
    ivy "{b}*Хихиканье*{/b} Интересно подойдет ли он."
    ivy "Ты готов почувствать себя раю?"
    player_name "{b}*глоток*{/b} Да."
    ivy "Поехали..."
    show playersex 22
    show ivysex 18 with dissolve
    show ivysex 19 with dissolve
    player_name "Хааах-"
    show ivysex 20
    ivy "Ты там в порядке?"
    player_name "Да, продолжай..."
    return

label ivy_reverse_cowgirl_loop:
    show screen sex_xray_anim_buttons
    pause
    hide screen sex_xray_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("ivysex", [18,19], M_ivy) as ivysex zorder 2
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [18,19]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_reverse_cowgirl_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_rcowgirl_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["03_unlocked"] = True
    $ game.main()

label ivy_reverse_cowgirl_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show ivysex 19
        player_name "( Святое дерьмо, это потрясающее чувство! )"
        if not anim_toggle:
            show ivysex 18
        player_name "Ты можешь делать быстрее... Я думаю я смогу с этим справиться..."
        if not anim_toggle:
            show ivysex 19
        ivy "Хорошо. Ты сам напросился!"

    elif animcounter == 2:
        if not anim_toggle:
            show ivysex 19
        player_name "( Нужно продержаться еще немного... )"
        if not anim_toggle:
            show ivysex 18
        ivy "Хаах-Я должна сказать..."
        if not anim_toggle:
            show ivysex 19
        ivy "...ты можешь быть просто подростком..."
        if not anim_toggle:
            show ivysex 18
        ivy "...но ты-ааъ-позоришь некоторых моих клиентов!"
        if not anim_toggle:
            show ivysex 19
        player_name "( Это единственый способ повысить свое эго. )"
        if not anim_toggle:
            show ivysex 18
        player_name "( Интересно как она отреогирует... )"
        if not anim_toggle:
            show ivysex 19

    elif animcounter == 3:
        if not anim_toggle:
            show ivysex 19
        player_name "( Дерьмо, Я на пределе! )"
        if not anim_toggle:
            show ivysex 18
        player_name "( Она слишком хороша в этом! )"
        if not anim_toggle:
            show ivysex 19
        player_name "Я собираюсь кончить!"
        if not anim_toggle:
            show ivysex 18
        ivy "Хах- Давай!"

        call screen ivy_rcowgirl_cum_options

        if ivy_cum_inside:
            show playersex 22
            show ivysex 19 zorder 2
        else:
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 19
            show ivysex 22 zorder 2
            show expression "characters/player/char_player_sex_25.png" as playersex_cum zorder 3
        show white zorder 3 with hpunch
        hide white
        with dissolve
        ivy "Хааа..."
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_51.png" as playersex_cum zorder 3
        ivy "Хаах... Ты продержался довольно долго... для подростка."

        hide expression "characters/player/char_player_sex_29.png"
        if ivy_cum_inside:
            show playersex 19
            show ivysex 22 zorder 2
            show expression "characters/player/char_player_sex_35.png" zorder 3
        player_name "Спасибо. Ты потрясающая..."
        hide expression "characters/player/char_player_sex_35.png"
        show playersex 19
        show ivysex 15 zorder 2
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_52.png" as playersex_cum zorder 3
        else:
            show expression "characters/player/char_player_sex_31.png" zorder 3
        pause
        ivy "Давай приведем себя в порядок..."
    return

label ivy_slap_ass:
    show playersex 23
    show ivysex 20
    pause 0.2
    show ivysex 21
    show playersex 24 with vpunch
    pause 0.2
    ivy "{b}*Хихиканье*{/b} Становишся еще более наглее?"
    ivy "Значит, быстрее!"
    hide expression "characters/player/char_player_sex_40b.png"
    show playersex 22
    show ivysex 20
    jump expression game.dialog_select("ivy_reverse_cowgirl_loop")

label ivy_cowgirl:
    call expression game.dialog_select("ivy_cowgirl_pre")
    if M_ivy.get("first visit"):
        call expression game.dialog_select("ivy_cowgirl_first")
        $ M_ivy.set("first visit", False)
    call expression game.dialog_select("ivy_cowgirl_after")
    $ M_ivy.set("sex speed", 0.8)
    $ animcounter = 0
    $ anim_toggle = False
    $ ivy_cum_inside = False
    $ xray_needed = True
    jump expression game.dialog_select("ivy_cowgirl_loop")

label ivy_cowgirl_pre:
    scene pink
    show ivy 5 at right
    show player 174 at left
    with dissolve
    player_name "Да, Я уже поти в конечном этоге, пожалуйста."
    ivy "{b}*Хихиканье*{/b} Ты хочешь увидеть все это, не так ли?"
    show player 29
    player_name "Я эмм..."
    show ivy 3
    ivy "Я люблю нетерпеливых мужчин."
    show ivy 2
    ivy "Следуй за мной."
    scene massage_room_closeup with fade
    show ivy 2 at right
    show player 43 at left
    with dissolve
    ivy "Хорошо, я просто удостоверюсь, что никто не сможет нас прервать."
    return

label ivy_cowgirl_first:
    player_name "{b}*Свист*{/b} Крутая комната."
    show player 1
    show ivy 3
    ivy "{b}*Хихиканье*{/b} Будет еще круче, как только мы начнем."
    show ivy 2
    ivy "Сейчас, раздевайся и ложись на кровать. Ты можешь положить свои одежды на стол."
    ivy "Я дам тебе несколько минут на подготовку."
    hide ivy 2
    scene blank with dissolve
    scene massage_room_closeup
    show player 175 at left
    with dissolve
    player_name "( Уф, это было менее неловко, чем я ожидал! )"
    player_name "( Я не ожидал, что это будет так просто, хотя. )"
    player_name "( Может быть, я еще не готов к чему-то подобному... )"
    player_name "( ...Нет. Я не могу повернуть сейчас назад. )"
    player_name "( Я мог бы также наслаждаться этим. )"
    scene massage_room
    hide player
    show playersex 19
    show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
    show ivy 18 zorder 3 at Position (xpos=870,ypos=655)
    with dissolve
    ivy "{b}*Хихиканье*{/b} Почему ты все еще так одет?"
    ivy "Нам не нужны полотенца для этого вида массажа."
    player_name "Ох, прости..."
    show ivy 14 at Position (xpos=780,ypos=655) with dissolve
    pause 0.5
    hide expression "characters/ivy/char_ivy_13.png"
    show ivy 15 at Position (xpos=804,ypos=655) with vpunch
    ivy "Вот так! Намного лучше, не так ли?"
    player_name "Да,так и есть."
    show ivy 16 at Position (xpos=870,ypos=658)
    pause 1
    show ivy 17 at Position (xpos=870,ypos=655)
    pause 1
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "Как, черт возьми, ты прятал эту штуку?"
    ivy "В любом случае: мое имя Айви."
    ivy "Теперь, моя очередь подготовиться..."
    return

label ivy_cowgirl_after:
    scene massage_room
    hide player
    show playersex 19
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "Для этого нам понадобится презерватив.."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Ахх мэн..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "О, не волнуйся, ты даже не заметишь, что он там. Поверь мне."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "И для финальной части..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 8 zorder 2
    with dissolve
    pause
    show ivysex 9 with dissolve
    pause
    show playersex 20
    show ivysex 10 with dissolve
    ivy "{b}*Хихиканье*{/b} Интересно, поместится ли он..."
    ivy "Вы готов почувствовать себя в раю?"
    player_name "{b}*Глоток*{/b} Да."
    ivy "Поехали..."
    show playersex 21
    show ivysex 11
    player_name "Хааах-"
    show playersex 20
    show ivysex 10
    ivy "Ты в порядке?"
    player_name "Да, продолжай..."
    return

label ivy_cowgirl_loop:
    show screen sex_xray_anim_buttons
    pause
    hide screen sex_xray_anim_buttons
    while animcounter < 4:
        if anim_toggle:
            show expression AnimatedImage("playersex", [20,21], M_ivy) as playersex
            show expression AnimatedImage("ivysex", [10,11], M_ivy) as ivysex zorder 2
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [10,11]
            $ player_pose_list = [20,21]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "playersex {}".format(player_pose_list[pose_counter]) as playersex
                show expression "ivysex {}".format(pose_list[pose_counter]) as ivysex zorder 2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        call expression game.dialog_select("ivy_cowgirl_hscene_dialog")
        $ animcounter += 1
        if animcounter < 3:
            call screen ivy_cowgirl_options
    $ renpy.end_replay()
    $ persistent.cookie_jar["Ivy"]["unlocked"] = True
    $ persistent.cookie_jar["Ivy"]["gallery"]["04_unlocked"] = True
    $ game.main()

label ivy_cowgirl_hscene_dialog:
    if animcounter == 1:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Святое дерьмо, это потрясающее чувство! )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "Ты можешь быстрее... Думаю, что я смогу справиться с этим..."
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        ivy "Хорошо. Ты сам напросился.!"

    elif animcounter == 2:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Нужно продержаться еще немного.... )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "Хаах-Я должна сказать..."
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        ivy "...ты можешь быть просто подростком..."
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "...но ты-аах-позоришь некоторых моих клиентов!"
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Это один из способов повысить мое эго. )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "( Интересно, как она отреагирует... )"

    elif animcounter == 3:
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "( Дерьмо, Я на пределе! )"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        player_name "( Она слишком хороша в этом ! )"
        if not anim_toggle:
            show playersex 20
            show ivysex 10
        player_name "Я собираюсь кончить!"
        if not anim_toggle:
            show playersex 21
            show ivysex 11
        ivy "Хаах- Давай!"

        call screen ivy_cowgirl_cum_options

        if ivy_cum_inside:
            show playersex 21
            show ivysex 11 zorder 2
        else:
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 20
            show ivysex 13 zorder 2
            show expression "characters/player/char_player_sex_32.png" as playersex_cum zorder 3
        show white zorder 3 with hpunch
        hide white
        with dissolve
        ivy "Хаа..."
        if not ivy_cum_inside:
            show expression "characters/player/char_player_sex_33.png" as playersex_cum zorder 3
        ivy "Хаах... Ты продержался довольно долго... для подростка."
        if not ivy_cum_inside:
            show ivysex 14 zorder 2
            show expression "characters/player/char_player_sex_34.png" as playersex_cum zorder 3
        player_name "Спасибо... Ты потрясающая..."
        hide playersex_cum
        hide expression "characters/player/char_player_sex_29.png"
        show playersex 19
        show ivysex 9 zorder 3
        if ivy_cum_inside:
            show expression "characters/player/char_player_sex_30.png" zorder 2
            with dissolve
        pause
        hide expression "characters/player/char_player_sex_30.png"
        show ivysex 8 zorder 3
        if ivy_cum_inside:
            show expression "characters/player/char_player_sex_31.png" zorder 2
            with dissolve
        pause
        ivy "Давай приведем себя в порядок..."
    return

label ivy_no_money:
    show player 13 at left
    show ivy 4 at right
    with dissolve
    player_name "( Черт, я не могу себе этого позволить. )"
    player_name "С другой стороны, может быть, в другой раз."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
