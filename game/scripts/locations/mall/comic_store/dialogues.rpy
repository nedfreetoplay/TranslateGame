label comic_store_june_cosplay_started:
    scene comic_b
    show player 14 with dissolve
    player_name "Похоже у них есть некоторые костюмы висящие на стене."
    player_name "Я должен на них взглянуть..."
    player_name "... Возможно у них есть эти части оркского косплея."
    hide player with dissolve
    return

label comic_store_erik_vr_started_have_all:
    show player 14 with dissolve
    player_name "( Я думаю это все что {b}Эрик{/b} хотел. )"
    player_name "( Давайте вернумся к нему... )"
    hide player with dissolve
    return

label comic_store_erik_vr_started_do_not_have_all:
    show player 35 with dissolve
    player_name "( У них должны быть вещи, которые хотел {b}Эрик{/b}, где-то здесь. )"
    show player 12 with dissolve
    player_name "( Может быть на тех полках на прилавке? )"
    hide player with dissolve
    return

label comic_store_first_visit:
    scene comic_b
    show player 1 at left
    show lilly f_laugh at right
    with dissolve
    lilly "Привет!"
    show lilly f_normal_talk
    lilly "Первый раз посещаете {b}Cosmic Cumics{/b}?"
    show lilly f_normal
    show player 29
    player_name "Эммм... Да! Я не знал что это место существовало..."
    show lilly f_normal_talk
    show player 1
    lilly "Да мы только недавно открылись!"
    show lilly f_normal
    show player 2
    player_name "Ох, круто!"
    player_name "Вы ребята вы продаете видео-игры тоже?"
    show lilly f_laugh
    show player 1
    lilly "Конечно."
    show lilly f_normal_talk
    lilly "Мы продаем разнообразные продукты начиная от {b}видео-игр{/b},{b}комиксов{/b}, {b}фигурок{/b}, {b}плакатов{/b} и {b}коллекционных предметов{/b}!"
    show lilly f_normal
    show player 2
    player_name "Ох. и так... задротские вещи..."
    show lilly f_laugh
    show player 1
    lilly "Ага!"
    lilly "Осмотрись, и дай мне знать если тебе понадобится помощь с чем-нибудь!"
    hide lilly
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
