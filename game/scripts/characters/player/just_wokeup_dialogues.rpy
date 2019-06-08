label player_jenny_sleepover_mcbedroom:
    scene expression "backgrounds/location_home_bedroom_cutscene19.jpg" with fade
    pause
    scene expression "backgrounds/location_home_bedroom_cutscene20.jpg" with dissolve
    player_name "!!!"
    scene expression "backgrounds/location_home_bedroom_cutscene21.jpg" with dissolve
    player_name "Ты уходишь?"
    if M_jenny.get("jenny_girlfriend_first_time"):
        $ M_jenny.set('jenny_girlfriend_first_time', False)
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Да, солнце взошло, значит, твое время закончилось."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Ох."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Кроме того, {b}[deb_name]{/b} проснется скоро и я не хочу, чтобы она нашла меня здесь."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Ты хорошо спала?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Вообще-то, да."
        jen "Несмотря на твой безумный громкий храп."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Что?!"
        player_name "Я не храплю!"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Хех, неважно."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Мы можем сделать это снова?"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Конечно, если ты платишь."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Но-"
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Пока, неудачник."
    else:
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg" with dissolve
        jen "Угу, {b}[deb_name]{/b} скоро встанет."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "О, ладно."
        scene expression "backgrounds/location_home_bedroom_cutscene15b.jpg"
        jen "Не забудь зайти в {b}мою комнату{/b} сегодня днем для нашего шоу."
        scene expression "backgrounds/location_home_bedroom_cutscene15.jpg"
        player_name "Хорошо, я так и сделаю."
        scene black with fade
        pause
    return

label player_jenny_sleepover_sisbedroom:
    scene expression player.location.background_blur
    show jenny b_panties a_naked_hips f_upset
    show player b_underwear a_naked_sides f_normal_talk
    player_name "Доброе утро!"
    show player f_normal
    show jenny f_eyeroll
    jen "Да, да..."
    show jenny f_upset_talk
    jen "Проваливай, мне нужно в душ."
    show jenny f_upset
    show player f_skeptical_talk
    player_name "Блин, и все?"
    player_name "Рядом с тобой не очень весело просыпаться..."
    show player f_skeptical
    show jenny f_upset_talk
    jen "Ну, что ты хочешь, чтобы я сделала?!"
    jen "Приготовить тебе завтрак или что?"
    jen "Вернись в реальность."
    show jenny f_upset
    show player f_worried_talk
    player_name "Я бы никогда не попросил тебя сделать это, {b}[jen_name]{/b}..."
    show player f_laugh
    player_name "... Я пробовал твою стряпню, это ужасно."
    show player f_grin
    show jenny f_eyeroll a_naked_crossed with dissolve
    jen "Пошёл ты!"
    show jenny f_upset
    show player f_laugh
    player_name "Хахаах!"
    hide player with dissolve
    show jenny f_gross_talk
    jen "Мудак."
    show jenny f_gross
    return

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
    player_name "Рокси{/b} собиралась встретиться с {b}[jen_name]{/b} для занятий группы поддержки."
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
