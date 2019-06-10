label micoe_dialogue_blowjob:
    scene expression "backgrounds/location_hospital_room_blur.jpg"
    show player 10 at left
    show micoe at flip
    with dissolve
    player_name "Помнишь, когда ты мне помогла ... Хм, достав мой образец для тестирования."
    show player 5
    show micoe f_sexy_talk
    micoe "Ты имеешь в виду, когда я сосала твой член в ванной?"
    show micoe f_sexy
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Да."
    show player 3
    show micoe f_laugh
    micoe "Хе-хе, я думаю, что мы перестали стесняться, {b}[firstname]{/b}."
    show micoe f_sexy_talk
    micoe "Ты здесь, чтобы дать мне еще раз попробовать?"
    show micoe f_sexy
    show player 17 with dissolve
    player_name "Ага."
    hide player
    show micoe b_pulling f_empty a_empty
    with dissolve
    micoe "Давай, малыш."
    scene expression "backgrounds/location_hospital_bathroom.jpg"
    show player 13f at right
    show micoe f_sexy_talk
    with dissolve
    micoe "Чего ты ждешь?"
    micoe "Доставай свой член!"
    show micoe f_sexy
    show player 14f
    player_name "Хорошо."
    show player 261b with dissolve
    pause
    show player 263b at Position (xoffset=-150)
    show micoe knees
    with dissolve
    pause
    show micoe knees_talk
    micoe "Ммм, я высосу этот прекрасный член в любое время, когда ты захочешь, {b}[firstname]{/b}!"
    $ M_micoe.set('sex speed', .12)
    $ anim_toggle = True
    $ animated = True
    scene expression "backgrounds/location_hospital_bathroom_closeup.jpg"
    show expression AnimatedImage("micoe_bj", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], M_micoe) as micoe_bj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    micoe "{b}*чмок*{/b}"
    player_name "О, боже..."
    player_name "Это потрясающе, {b}Мико{/b}."
    micoe "Мммммммм!"
    return

label micoe_dialogue_goodbye:
    show player 14 at left
    show micoe f_normal at flip
    player_name "Просто поздороваться."
    show player 13
    show micoe f_sad_talk
    micoe "О, ну, это разочаровывает..."
    show micoe f_sexy_talk
    micoe "Я подумала, что ты здесь, чтобы немного повеселиться."
    show micoe f_sexy
    show player 14
    player_name "Прости."
    show player 13
    pause
    show player 14
    player_name "Увидимся позже, хорошо?"
    show player 13
    show micoe f_normal_talk
    micoe "Хорошо, милашка."
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_intro:
    scene expression player.location.background_blur with None
    show player 13 at left
    show micoe f_normal_talk at flip
    micoe "Эй, милашка."
    micoe "Что привело тебя ко мне?"
    show micoe f_normal
    return

label micoe_dialogue_increase_chance_of_conception:
    show micoe at flip
    show player 10 at left
    with dissolve
    player_name "Могу ли я сделать что-нибудь еще, чтобы помочь моим друз-"
    player_name "{b}*хмм*{/b} Я имею в виду, помочь моей девушке зачать ребенка?"
    show player 5
    show micoe f_normal_talk
    micoe "Хм, она об этом беспокоится?"
    show micoe f_normal
    show player 10
    player_name "Эхх, не совсем ..."
    player_name "Я просто хочу убедиться, что делаю все возможное, чтобы помочь ей."
    show player 5
    show micoe f_laugh
    micoe "Оу, ты такой милый!"
    show player 13
    show micoe f_normal_talk
    micoe "Ну, у вас двоих было много секса?"
    show micoe f_normal
    show player 29 with dissolve
    player_name "Да."
    show player 13 with dissolve
    show micoe f_normal_talk
    micoe "... И какую позицию ты используешь?"
    show micoe f_normal
    show player 10
    player_name "... Позицию?"
    show player 5
    show micoe f_sexy_talk
    micoe "Да, в каком положении ты занимаешься сексом?"
    show micoe f_sexy
    show player 10
    player_name "Э-э, я не знаю."
    show player 14
    player_name "Я думаю, я обычно позади нее ..."
    show player 13
    show micoe f_sexy_talk
    micoe "Собачий стиль?"
    show micoe f_sexy
    show player 5
    player_name "..."
    show micoe f_laugh
    micoe "Хе-хе, ты такой милый!"
    show micoe f_normal_talk
    micoe "Собачий стиль должен хорошо работать для зачатия."
    show player 13
    micoe "Многие врачи рекомендуют его, потому что он обеспечивает самое глубокое проникновение."
    show micoe f_wink
    pause
    show micoe f_sexy_talk
    micoe "Хотя, с тем, что вы упаковываете, глубокое проникновение не будет проблемой."
    show micoe f_sexy
    show player 29 with dissolve
    player_name "Хе, да..."
    show player 13 with dissolve
    show micoe f_normal_talk
    micoe "Вы можете попробовать миссионерскую позицию."
    show micoe f_normal
    show player 10
    player_name "Это как?"
    show player 13
    show micoe f_normal_talk
    micoe "Это когда женщина лежит на спине, а ты сверху."
    micoe "В этом положении сила тяжести поможет перенести сперму к шейке матки."
    show micoe f_normal
    show player 17
    player_name "О, я понимаю! Нормальный стиль."
    show player 18
    show micoe f_sad
    pause
    show player 14
    player_name "В этом есть смысл."
    show player 13
    pause
    show player 14
    player_name "Что-нибудь еще?"
    show player 13
    show micoe f_normal
    micoe "Хмм."
    show micoe f_normal_talk
    micoe "Наврятли."
    micoe "К сожалению, самым большим препятствием в вашей ситуации является возраст вашей девушки."
    show micoe f_normal
    show player 10
    player_name "Да."
    show player 5
    pause
    show player 10
    player_name "Ты уверена, что я больше ничем не могу помочь?"
    show player 5
    show micoe f_normal_talk
    micoe "Ну..."
    show micoe f_look_back
    pause
    show micoe f_normal_talk
    micoe "Есть только одна вещь... Но я действительно не должна говорить об этом."
    show micoe f_normal
    show player 12
    player_name "Эээ?"
    player_name "Да ландо, скажи?"
    show player 5
    pause
    show player 14
    player_name "Если есть шанс, что это поможет, я действительно должен знать!"
    player_name "{b}Диана{/b} действительно хочет забеременеть."
    show player 13
    pause
    show player 18
    player_name "Пожалуйста?"
    show micoe f_laugh
    micoe "Нгх, ты просто такой милый!"
    show player 13
    show micoe f_normal_talk
    micoe "Хорошо, я скажу вам ... Но я вам ничего не говорила!"
    micoe "Ясно?"
    show micoe f_normal
    show player 14
    player_name "Да, я понял!"
    show player 13
    show micoe f_normal_talk
    micoe "Существует новый препарат, который показал многообещающие результаты, когда речь заходит о повышении уровня зачатия."
    micoe "Оно называется {b}Pregnax{/b}."
    show micoe f_normal
    show player 14
    player_name "Звучит отлично!"
    show player 12
    player_name "В чем загвоздка?"
    show player 5
    show micoe f_normal_talk
    micoe "Загвоздка в том, что они все еще на стадии тестирования."
    show micoe f_normal
    pause
    show player 14
    player_name "Все в порядке, я не против помочь протестировать их."
    show player 13
    show micoe f_laugh
    micoe "Хехе, ты должен поговорить с {b}Доктором Сингх{/b} про это."
    show micoe f_normal
    show player 10
    player_name "{b}Доктор Сингх{/b}?"
    show player 5
    show micoe f_normal_talk
    micoe "Да, {b}Сингх{/b} - это новый доктор в модных штанах, которого они доставили откуда-то из-за границы."
    micoe "Работает на {b}3-ем этаже{/b}."
    micoe "Исследует {b}Pregnax{/b} уже несколько лет."
    show micoe f_normal
    show player 14
    player_name "Хорошо, я пойду и поговорю с ней!"
    show player 13
    show micoe f_sad_talk
    micoe "Хех, я бы хотела, чтобы все было так просто."
    micoe "К сожалению, {b}третий этаж{/b} является запретной зоной."
    micoe "аже у меня нет доступа к нему."
    show micoe f_normal
    show player 12
    player_name "Так, и как мне получить доступ?"
    show player 5
    show micoe f_normal_talk
    micoe "Я не смогу тебе помочь с этим, милашка."
    micoe "Не многие люди в клинике имеют право подняться на {b}третий этаж{/b}."
    show micoe f_normal
    show player 24
    player_name "Черт."
    pause
    show player 10
    player_name "Хорошо, спасибо за информацию {b}Мико{/b}."
    show player 5
    show micoe f_laugh
    micoe "Нет проблем, милашка!"
    show micoe f_sexy_talk
    micoe "Не стесняйся приходить ко мне, если у тебя есть еще вопросы ..."
    show player 13
    show micoe f_wink
    pause
    show micoe f_sexy_talk
    micoe "... Или тебе захочется немного поразвлечься!"
    show micoe f_sexy
    show player 29 with dissolve
    player_name "Да, хорошо."
    show player 3
    show micoe f_sexy_talk
    micoe "Ммм, так восхитительно ..."
    hide player
    hide micoe
    with dissolve
    return

label micoe_dialogue_pregnax:
    scene expression "backgrounds/location_hospital_room.jpg"
    show player 10 at left
    show micoe f_normal at flip
    with dissolve
    player_name "Где я могу найти этот препарат от бесплодия?"
    show player 5
    show micoe f_sad_talk a_dressed_shh at Position (xoffset=-175) with dissolve
    micoe "Шшш!"
    micoe "Не так громко!"
    show micoe f_normal a_dressed_front with dissolve
    show player 10
    player_name "О, прости."
    show player 5
    show micoe f_normal_talk
    micoe "Они находятся на {b}3-ем этаже{/b}."
    show micoe f_normal
    show player 14
    player_name "{b}3-ий этаж{/b}, понятно!"
    show player 13
    show micoe f_normal_talk
    micoe "Подожди, ты не можешь просто ворваться туда."
    micoe "Тебе нужно {b}найти кого-то, у кого есть доступ{/b}, чтобы проводить тебя туда."
    show micoe f_normal
    show player 10
    player_name "Хм, кого я могу спросить?"
    show player 5
    show micoe f_normal_talk
    micoe "Прости, милашка, я не могу помочь тебе с этим."
    micoe "Просто запомни, ты ничего не слышал от меня!"
    show micoe f_normal
    show player 14
    player_name "Не волнуйся, я никому не скажу."
    show player 18
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
