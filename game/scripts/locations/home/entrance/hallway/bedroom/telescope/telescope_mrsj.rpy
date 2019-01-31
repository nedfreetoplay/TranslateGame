label erikmom_bedroom:
    if M_jenny.is_state(S_jenny_telescope_spying_tier_3):
        call expression game.dialog_select("telescope_mrsj_sister_spying")
        $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
        $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["02_unlocked"] = True
        $ M_jenny.trigger(T_jenny_spied_on_neighbour_tier_3)
        jump expression game.dialog_select("bedroom_dialogue")
    else:

        call expression game.dialog_select(game.telescope.mrsj)

    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label telescope_mrsj_sister_spying:
    show windowmrsjday 3a
    player_name "( Вау! Она полностью обнажена!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "( Это прыгающий мячик?.. с фаллоимитатором на нем?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Почему она не закрыла шторы? )"
    show windowmrsjday 3c-d
    player_name "( Как будто она хочет, чтобы ее увидели... )"
    player_name "( Я думаю, она знает... )"
    player_name "( Она смотрит прямо на меня. )"
    hide windowmrsjday
    hide screen telescope
    show telescope_caught 1
    with dissolve

    jen "( Хм... Интересно, что он задумал. )"
    show telescope_caught 3 with dissolve
    pause
    show telescope_caught 5
    jen "( Попался! )"
    scene location_home_bedroom_telescope_window
    show player 357 at Position(xpos=456,ypos=758)
    with dissolve
    pause
    show jenny 136 at Position(xpos=725,ypos=0,xanchor=0,yanchor=0) with fastdissolve
    pause
    show jenny 135
    jen "Боже, какой же ты извращенец!!"
    show jenny 136
    show player 358 at Position(xpos=448)
    player_name "!!!" with vpunch
    show player 360 at Position(ypos=768)
    player_name "Как ты-"
    show player 361
    show jenny 135
    jen "Я знала, что ты будешь здесь."
    jen "Ты не можешь насытиться этим телескопом..."
    jen "Посмотрим, что ты нашел на этот раз."
    show player 360 at Position(ypos=768)
    show jenny 136
    player_name "Постой-"
    show player 361
    show jenny 138
    jen "Подвинся."
    show player 361 at left
    show jenny 142 at Position(xpos=284,ypos=231)
    with fastdissolve
    jen "Так, посмотрим..."
    show jenny 140 at Position(ypos=229)
    pause
    show windowmrsjday 3c-d with dissolve
    jen "{b}Миссис Джонсон{/b}?!!"
    jen "Ну, блин..."
    jen "Она озорная, не так ли?"
    scene location_home_bedroom_telescope_window
    show player 361 at left
    show jenny 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
    with dissolve
    pause
    show jenny 142 at Position(xpos=284,ypos=231,xanchor=0,yanchor=0)
    jen "Она всегда делает такие вещи перед своим окном?"
    show jenny 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
    jen "Как будто она хочет, чтобы ее увидели..."
    show player 360
    player_name "...Наверное?"
    show player 361
    jen "Это горячо... То, как она перемалывает этот мяч..."
    show jenny 145_146_147_148 at Position(xpos=286,ypos=229,xanchor=0,yanchor=0) with fastdissolve
    pause
    show player 364
    player_name "!!!"
    show player 361
    jen "Мне нравится, как ее задница отскакивает от него."
    show player 362
    jen "Жаль, что я не сижу на этом шаре..."
    show jenny 144 at Position(ypos=231)
    show player 361
    jen "В чем дело?"
    jen "Я не могу наслаждаться жизнью?"
    show player 360
    show jenny 143
    player_name "Я этого не говорил...."
    show player 361
    show jenny 144
    jen "Что тебе больше нравится?"
    jen "Смотреть на {b}Миссис Джонсон{/b}... или смотреть на {b}меня{/b}?"
    show player 360
    show jenny 143
    player_name "Я не знаю..."
    show jenny 139 at right with fastdissolve
    show player 361
    jen "Упсс!"
    jen "Ты только посмотри на это..."
    jen "Я вся {b}мокрая{/b}!"
    jen "Я должна оставить это на потом... Может, ОБМЕНЯЕМ их на что-нибудь..."
    hide jenny with dissolve
    pause
    show player 362
    pause
    $ renpy.end_replay()
    return

label telescope_mrsj_morning_1:
    scene windowmrsjmorning01
    player_name "( ...это {b}домохозяйка Эрика{/b}?! )"
    scene windowmrsjmorning01b
    player_name "( Ух ты! Она одевается... )"
    scene windowmrsjmorning01c
    player_name "( Нет! Еще чуть чуть! )"
    scene windowmrsjmorning01d
    player_name "( Черт! Шоу окончено... )"
    return

label telescope_mrsj_morning_2:
    scene windowmrsjday02
    player_name "( Ее жалюзи закрыты. Ее, наверное, нет дома. )"
    return

label telescope_mrsj_afternoon_1:
    scene windowmrsjday01
    player_name "( Ее нет дома. )"
    return

label telescope_mrsj_afternoon_2:
    show windowmrsjday 3a
    player_name "( Вау... Она совершенно голая!! )"
    show windowmrsjday 3b with fastdissolve
    player_name "(Это прыгающий мячик?.. с фаллоимитатором на нем?! )"
    show windowmrsjday 3c with fastdissolve
    player_name "( Почему она не закрыла шторы? )"
    show windowmrsjday 3c-d
    player_name "( Как будто она хочет, чтобы ее увидели... )"
    player_name "( Я думаю, она знает... )"
    player_name "( Она смотрит прямо на меня. )"
    return

label telescope_mrsj_afternoon_3:
    scene windowmrsjday02
    player_name "( Ее жалюзи закрыты. Ее, наверное, нет дома. )"
    return

label telescope_mrsj_night_1:
    scene windowmrsjnight03
    player_name "( ...Она занимается йогой? )"
    player_name "( ...На кровати? )"
    scene windowmrsjnight04
    player_name "..."
    player_name "( {b}Домохозяйка Эрика{/b} в хорошей форме... )"
    player_name "( ...у нее прекрасное тело... )"
    return

label telescope_mrsj_night_2:
    scene windowmrsjnight01
    player_name "( Ее нет в комнате.... )"
    return

label telescope_mrsj_night_3:
    scene windowmrsjnight02
    player_name "( Она должно быть уже спит. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
