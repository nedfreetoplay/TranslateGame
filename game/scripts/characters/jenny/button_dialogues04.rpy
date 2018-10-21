label sis_cheerleader_break_free_pass_animation:
    player_name "( Эй, эти наручники не кажутся такими крепкими... )"
    player_name "( Хорошо, начинаем... )"
    return

label sis_cheerleader_break_free_pass_manual:
    show jennysex 117 at Position(xpos = 939, ypos = 674)
    player_name "( Эй, эти наручники не кажутся такими крепкими... )"
    show jennysex 118
    player_name "( Хорошо, начинаем... )"
    return

label sis_cheerleader_break_free_pass_after:
    show jennysex 119b at Position(xpos = 939, ypos = 674)
    jen "Эй, Что ты-"
    show jennysex 122 at Position(xpos = 1022, ypos = 768)
    hide playersex
    jen "!!!" with hpunch
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "Ахх!!" with vpunch
    show jennysex 124
    jen "Что ты... ДЕЛАЕШЬ?!"
    show jennysex 125
    pause
    show jennysex 126
    pause
    show jennysex 127
    pause
    show jennysex 123
    jen "Ты... делаешь это слишком... быстро!"
    show jennysex 124
    pause
    show jennysex 125
    pause
    show jennysex 126
    jen "Это... ИЗУМИТЕЛЬНО!!"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_unhappy:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_manual")
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_after")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_unhappy_after_no_xray")
    call expression game.dialog_select("sis_cheerleader_fuck_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ sis_final_cum = "Inside"
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_inside_unhappy_animation:
    jen "( Боже мой, я чувствую, как он напрягается... )"
    jen "( ... Он собирается кончить {b}внутрь меня{/b}?! )"
    pause
    jen "( Черт, я не могу от него избавиться!!! )"
    return

label sis_cheerleader_fuck_cum_inside_unhappy_manual:
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "( Боже мой, я чувствую, как он напрягается... )"
    show jennysex 124
    jen "( ... Он собирается кончить {b}внутрь меня{/b}?! )"
    show jennysex 125
    pause
    show jennysex 126
    jen "( Черт, я не могу от него избавиться!!! )"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_unhappy_after:
    show jennysex 129
    jen "ААХХХХХ!!!!" with vpunch
    show white zorder 5
    show jennysex 129c
    hide white with dissolve
    pause
    show jennysex 128 with fastdissolve
    jen "О, боже..."
    show jennysex 129b_128
    pause 2.9
    show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
    show jennysex 131 zorder 2 at Position(xpos=985,ypos=674)
    with dissolve
    return

label sis_cheerleader_fuck_cum_inside_unhappy_after_no_xray:
    jen "Что за... {b}ЧЕРТ{/b}?!"
    jen "Черт, я же говорил тебе {b}НЕ{/b} кончать в меня, {b}ИДИОТ{/b}!!!" with hpunch
    return

label sis_cheerleader_fuck_cum_inside_happy:
    if anim_toggle:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_animation")
    else:
        call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_manual")
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_after")
    $ xray = False
    call expression game.dialog_select("sis_cheerleader_fuck_cum_inside_happy_after_no_xray")
    call expression game.dialog_select("sis_cheerleader_fuck_after_repeat")
    jump expression game.dialog_select("hallway_dialogue")

label sis_cheerleader_fuck_cum_inside_happy_animation:
    jen "( Боже мой, я чувствую, как он напрягается... )"
    jen "( ... Он собирается кончить {b}внутрь меня{/b}?! )"
    pause
    jen "( Черт, я не могу от него избавиться!!! )"
    return

label sis_cheerleader_fuck_cum_inside_happy_manual:
    show jennysex 123 at Position(xpos = 986, ypos = 768)
    jen "( Боже мой, я чувствую, как он напрягается... )"
    show jennysex 124
    jen "( ... Он собирается кончить {b}внутрь меня{/b}?! )"
    show jennysex 125
    pause
    show jennysex 126
    jen "( Черт, я не могу от него избавиться!!! )"
    show jennysex 127
    pause
    return

label sis_cheerleader_fuck_cum_inside_happy_after:
    show jennysex 129
    jen "ААХХХХХ!!!!" with vpunch
    show white zorder 5
    show jennysex 129c
    hide white with dissolve
    jen "ДДАААА, ГЛУБЖЕ!!"
    show jennysex 128 with fastdissolve
    pause
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    jen "Продолжай кончать!"
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    jen "Я хочу больше..."
    show white zorder 5
    show jennysex 129b
    hide white with fastdissolve
    pause
    show jennysex 128 with fastdissolve
    pause
    show playersex 128 zorder 1 at Position(xpos=540,ypos=768)
    show jennysex 132 zorder 2 at Position(xpos=985,ypos=674)
    with dissolve
    return

label sis_cheerleader_fuck_cum_inside_happy_after_no_xray:
    jen "Посмотри на всю сперму что капает из моей киски..."
    jen "...Я могла бы {b}залететь{/b}, в таком случае..."
    return

label sis_cheerleader_fuck_after_repeat:
    scene jennybedroom
    show jenny 109 at right
    show player 13 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Молодец!"
    show jenny 108
    show player 21
    player_name "Все нормально?"
    show player 13
    show jenny 109
    jen "Да, им понравилось наше {b}маленькое представление{/b}."
    jen "Я... должна отдать тебе должное."
    jen "Я не ожидала, что ты так хорошо справишься."
    jen "Ты был крут."
    show jenny 108
    show player 14
    player_name "Правда?"
    show jenny 109
    show player 13
    jen "Ты мне еще понадобишься для других шоу."
    show player 21
    show jenny 167
    player_name "Спасибо, Мне было прият-"
    show jenny 164
    show player 11
    jen "ПРЕКРАТИ!!" with hpunch
    show jenny 165
    jen "..."
    show jenny 166
    jen "{b}*вздох*{/b}"
    show jenny 109
    jen "Да, мне тоже, наверное..."
    show player 13
    show jenny 108
    jen "..."
    show jenny 166
    show player 11
    jen "Но, не начинай придумывать! Я делаю это, потому что это приносит мне кучу денег..."
    jen "О, и сделай одолжение: постарайся не проводить слишком много времени с {b}[deb_name]{/b}..."
    jen "Я знаю, что вы двое задумали, мне нужно, чтобы ты был {b}свежим{/b} и {b}отдохнувшим{/b}."
    jen "Мои подписчики теперь ожидают такого рода стримы {b}регулярно{/b}."
    show jenny 164
    jen "Итак НИКАКОЙ дрочки, и НИКАКОГО секса!!"
    show jenny 165
    show player 12
    player_name "Хорошо! Хорошо! Я понял..."
    show jenny 109
    show player 13
    jen "Хорошо."
    show jenny 164
    show player 11
    jen "Хорошо, а теперь {b}ВАЛИ ИЗ МОЕЙ КОМНАТЫ{/b}!!" with hpunch
    hide player
    hide jenny
    hide jenny_cheer2
    return

label jenny_dialogue_cam_show_no_items:
    show player 1
    show jenny 12 at Position(xpos=937)
    jen "И?"
    jen "У тебя есть все, о чем я тебя просила?"
    show player 2
    show jenny 11
    player_name "Пока нет..."
    show player 22
    show jenny 7 at right
    jen "Тогда найди их и {b}убирайся отсюда{/b}!!"
    return

label jenny_dialogue_cam_show_have_items:
    scene jennybedroom
    show player 1 at left
    show jenny 12 at right
    show jenny 12 at Position(xpos=937)
    jen "Итак..."
    jen "У тебя есть все, о чем я тебя просила?"
    show jenny 82
    show player 21
    player_name "Да, да..."
    show player 239_240
    pause
    show player 285 with fastdissolve
    player_name "Вот."
    show player 1
    show jenny 158 at right
    with fastdissolve
    jen "Прекрасно."
    show jenny 12 at Position(xpos=937)
    show player 11
    jen "Возможно, ты не так глуп, как я думала, в конце концов."
    show jenny 10
    show player 12
    player_name "Теперь я могу идти?"
    show jenny 7 at right
    show player 11
    jen "Подожди!!"
    show jenny 9 at Position(xpos=937)
    jen "Мы еще ничего не закончили."
    show jenny 12
    jen "Разве ты не хочешь знать, что я должена сделать?"
    show jenny 10
    show player 12
    player_name "Ну... Дай угадаю: еще одно оскорбление или типа того..."
    show jenny 9
    show player 16
    jen "{b}*вздох*{/b}."
    show player 11
    jen "Я надеялся найти кого-то другого... но тебе придется это сделать."
    show jenny 9b
    player_name "..."
    show jenny 19 at right
    jen "Мне нужно, чтобы ты трахнул меня."
    show jenny 18
    player_name "!!!" with vpunch
    show player 10
    player_name "Что? Я не-"
    show jenny 7
    show player 11
    jen "ДАЖЕ НЕ ДУМАЙ!"
    show jenny 9 at Position(xpos=937)
    jen "Я делаю это только потому, что мне нужно продвинуть мой канал!"
    show jenny 10
    show player 10
    player_name "Я не думаю, что хочу-"
    show jenny 7 at right
    show player 11
    jen "Ты жалуешься?!!" with hpunch
    show jenny 8
    player_name "!!!"
    show player 10
    player_name "Нет! Просто иногда мне кажется, что ты просто используешь меня ради денег..."
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "О, пожалуйста! Хватит притворяться."
    jen "Я знаю, тебе нравится наша маленькая игра..."
    jen "И теперь ты наконец-то сделаешь то, что так долго хотел..."
    show jenny 12
    jen "Тебе придется трахнуть меня."
    jen "Не надо мне врать! Я знаю, что ты мечтал об этом моменте долгое время."
    jen "Так что это твой шанс, извращенец."
    show jenny 82
    show player 4
    player_name "..."
    show player 14
    player_name "Хорошо! Я в деле!"
    player_name "Но, что я должен делать в шоу?"
    show jenny 12
    show player 1
    jen "Дай мне сначала одеться в этот наряд."
    jen "Тогда я объясню, что мы будем делать..."
    show jenny 9
    show player 11
    jen "...и тебе лучше делать то, что я говорю! Понял?!"
    show jenny 82
    show player 21
    player_name "Да, {b}[jen_name]{/b}..."
    scene black with fade
    scene jennybedroom
    show jenny 166 zorder 1 at right
    show player 11 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Ты правда не мог найти мне более подходящий наряд?!"
    show jenny 167
    show player 10
    player_name "Ну, он твой еще со школы... Я подумал, что он все равно подойдет тебе."
    show jenny 164
    show player 11
    jen "Да, это было пять лет назад, придурок!"
    jen "Разве ты не видишь, что мои сиськи стали БОЛЬШЕ?!"
    show jenny 167
    show player 10
    player_name "Прости..."
    show jenny 166
    show player 11
    jen "О, забудь! Просто сиди на моей кровати и ничего не говори, пока я готовлюсь к шоу..."
    jen "Просто сиди, и проследи что твой член хороший и жесткий, и дайте мне знать, когда ты собираешься кончить."
    jen "Ясно, идиот?"
    show jenny 108
    show player 21
    player_name "Хорошо..."
    scene jenny_webcam2
    show jenny 151 zorder 2 at Position(xpos=407,ypos=748)
    show jenny_cheer1 zorder 3 at Position(xpos=439,ypos=724)
    show playersex 116 zorder 1 at Position(xpos=690,ypos=630)
    show xtra 20 zorder 4 at left
    with fade
    jen "Хорошо, мы в эфире!"
    show jenny 155
    jen "Привеет парни!"
    show jenny 151
    jen "Извините за задержку! Я знаю, вы все терпеливо ждали встречи со мной..."
    jen "... но у меня есть кое-что особенное в меню для вас сегодня!"
    jen "Я грязная маленькая школьная шлюха, одетая только в мой костюм болельщицы, без трусиков..."
    jen "У меня также есть мой возбужденный парень, который ждет, чтобы трахнуть меня своим огромным членом..."

    jen "Ну что Давайте приступим?"
    hide jenny
    hide jenny_cheer1
    show jennysex 133 zorder 2 at Position(xanchor=0,xpos=0,ypos=650)
    show playersex 116b
    with fastdissolve
    jen "Просто нужно кое-что сделать..."
    hide jennysex
    show jennysex 104 zorder 1 at Position(xpos=122,ypos=540)
    show playersex 119 zorder 2 at Position(xpos=455,ypos=768)
    with fastdissolve
    jen "Сначала я сниму эту юбку..."
    show jennysex 105 at Position(xpos=144,ypos=544) with fastdissolve
    pause
    show jennysex 106 at Position(xpos=170,ypos=542) with fastdissolve
    jen "Теперь давай используем это, чтобы убедиться, что он никуда не уйдет, пока я выебу его мозги..."
    show jennysex 106b
    show playersex 120
    player_name "Ты на самом деле не собираешься-"
    show jennysex 107 zorder 2 at Position(xpos=300,ypos=542)
    show playersex 122 zorder 1 at Position(xpos=554,ypos=768)
    with fastdissolve
    pause
    show playersex 125
    show jennysex 109 at Position(xpos=357,ypos=620)
    with fastdissolve
    jen "Что скажете, ребята? Должны ли мы выяснить, что скрывается под его шортами?"
    show jennysex 108
    player_name "..."
    show jennysex 111 at Position(xpos=375,ypos=634) with fastdissolve
    jen "Ой, вау..."
    show jennysex 112 at Position(xpos=374,ypos=674)
    show playersex 127
    jen "Посмотрите на этот красивый, толстый, длинный член..." with vpunch
    show jennysex 113 with fastdissolve
    jen "Давай сделаем эго красивым и твердым."
    show jennysex 115b with fastdissolve
    pause
    show jennysex 114b_115b
    pause 8
    show jennysex 114
    jen "Интересно, поместится ли он внутри меня..."
    show jennysex 115b
    player_name "!!!"
    show playersex 126
    player_name "Мы займемся сексом прямо сейчас?"
    player_name "Разве мы не должны использовать презерв-"
    show jennysex 110b at Position(xpos=423,ypos=674)
    show playersex 127b
    jen "Шшшшшш!!!" with hpunch
    jen "Мои фанаты хотят увидеть грубый секс, ясно??!"
    jen "Итак я хочу убедится что ты кончишь снаружи, ясно!?"
    show jennysex 114 at Position(xpos=374,ypos=674)
    show playersex 127
    with fastdissolve
    jen "Извините за это, ребята!"
    show jennysex 115
    jen "Мой парень просто... застенчивый."
    show jennysex 114
    jen "Теперь давайте дадим вам то, чего вы все так долго ждали..."
    show jennysex 116 at right with dissolve
    pause
    show jennysex 119b at Position(xpos = 939, ypos = 674) with fastdissolve
    jen "Ох, ДАААА!!"
    show jennysex 117b with fastdissolve
    jen "Так... {b}глубоко{/b}!!"
    $ M_jenny.set("sex speed", .3)
    show expression AnimatedImage("jennysex", [117,118,119,120,121], M_jenny) as jennysex at Position(xpos = 939, ypos = 674)
    pause 8
    show jennysex 117b
    jen "Я люблю скакать на члене моего парня!"
    show jennysex 118b
    jen "Он едва помещается в мою тугую киску...."
    show jennysex 119
    pause
    show jennysex 120
    pause
    show jennysex 121
    pause
    return

label sis_cheerleader_fuck_after_initial:
    scene jennybedroom
    show jenny 109 at right
    show player 13 at left
    show jenny_cheer2 zorder 2 at Position(xpos=797,ypos=757)
    with fade
    jen "Молодец!"
    show jenny 108
    show player 21
    player_name "Все нормально?"
    show player 13
    show jenny 109
    jen "Я так думаю: моим подписчикам нравится новый контент."
    jen "Я должна сказать, однако..."
    jen "Я не ожидала, что такой маленький извращенец, как ты, сможет так выступить."
    jen "Думаю, ты неплохо справился."
    show jenny 108
    show player 14
    player_name "Правда?"
    show jenny 109
    show player 13
    jen "Может, я смогу снова использовать тебя для других шоу..."
    show player 21
    show jenny 167
    player_name "Спасибо, мне понравилось-"
    show jenny 164
    show player 11
    jen "Нет, прекрати это!!" with hpunch
    show jenny 166
    jen "Это было {b}строго деловое предложение{/b}, ничего больше!"
    jen "Не начинай придумывать. Я делаю это, чтобы заработать хорошие деньги..."
    jen "О, и сделай одолжение, постарайся не проводить слишком много времени с {b}[deb_name]{/b}..."
    jen "Я знаю, что вы двое задумали, но ты нужен мне {b}свежим{/b} и {b}отдохнувшим{/b}."
    jen "Мои подписчики ожидают больше шоу на этой неделе."
    show jenny 164
    jen "Так что никаких дрочек и никакого секса!!"
    show jenny 165
    show player 12
    player_name "Хорошо! Хорошо! Я понял..."
    show jenny 109
    show player 13
    jen "Хорошо!"
    show jenny 164
    show player 11
    jen "Теперь, {b}ВАЛИ ИЗ МОЕЙ КОМНАТЫ{/b}!!" with hpunch
    hide player
    hide jenny
    hide jenny_cheer2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
