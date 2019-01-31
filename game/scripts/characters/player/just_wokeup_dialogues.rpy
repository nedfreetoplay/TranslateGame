label bedroom_sis_webcam_show:

    show player 4 with dissolve
    player_name "Хмм..."
    player_name "( Интересно, что {b}[jen_name]{/b} делает прямо сейчас. )"
    show player 1
    player_name "( Может быть, я мог бы подключиться к её {b}веб-камере{/b} со моего компьютера... )"
    hide player with dissolve
    return

label bedroom_bissette_roxxy_jenny_mentoring:
    show player 12 with dissolve
    player_name "{b}Рокси{/b} собиралась встретиться с {b}[jen_name]{/b} для занятий группы поддержки."
    show player 10
    player_name "{b}Я должен отправиться домой{/b} и убедиться, что {b}[jen_name]{/b} не налетит на неё."
    hide player with dissolve
    return

label bedroom_dewitt_make_replacement_guitar:
    if game.timer.is_dark():
        show player 14 with dissolve
        player_name "Думаю, у меня есть всё, что нужно, чтобы сделать мою фальшивую гитару."
        show player 4
        player_name "Мне нужно не забыть собрать её завтра в гараже."
        hide player with dissolve
    else:
        show player 14 with dissolve
        player_name "Думаю, у меня есть всё, что нужно, чтобы сделать мою фальшивую гитару."
        player_name "Я должен вернуться в свой гараж, чтобы начать работать над этим."
        hide player with dissolve
    return

label bedroom_sis_telescope_1:

    show player 4 with dissolve
    player_name "( Интересно, что сейчас делает {b}Эрик{/b}. )"
    player_name "( Я должен использовать мой {b}телескоп{/b} и посмотреть, что он задумал... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_2:

    show player 4 with dissolve
    player_name "( Интересно, что сейчас делает {b}Мия{/b}. )"
    player_name "( Я должен использовать мой {b}телескоп{/b} и посмотреть, что она задумала... )"
    hide player with dissolve
    return

label bedroom_sis_telescope_3:

    show player 4 with dissolve
    player_name "( Интересно, что сейчас делает {b}Миссис Джонсон{/b}. )"
    player_name "( Я должен использовать мой {b}телескоп{/b} и посмотреть, что она задумала... )"
    hide player with dissolve
    return

label bedroom_master_somrak_training:

    show player 4 with dissolve
    player_name "( Интересно, {b}мастер Сомрак{/b} готов снова тренировать меня. )"
    hide player with dissolve
    return

label bedroom_roxxy_spin_bottle:
    show player 17 with dissolve
    player_name "{b}Рокси{/b} и девочки хотели, чтобы я сходил на пляж сегодня днём."
    player_name "Мне надо туда!"
    return

label bedroom_roxxy_spin_bottle_no_goldschwagger:
    show player 4 with dissolve
    player_name "( Мне же ещё нужно поговорить с {b}Капитаном Терри{/b} о {b}GoldSchwagger{/b} для {b}Бекки{/b}. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
