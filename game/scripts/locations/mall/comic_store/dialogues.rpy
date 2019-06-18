label comic_store_bought_cyclone_mask:
    scene expression player.location.background_closeup with None
    show player 736 with dissolve
    player_name "( Yeah, this should work great for {b}[jen_name]'s camshows{/b}. )"
    player_name "( I should {b}meet her in her room{/b} and see what she thinks. )"
    hide player with dissolve
    return

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
    show lily f_laugh at right
    with dissolve
    lily "Привет!"
    show lily f_normal_talk
    lily "Первый раз посещаете {b}Cosmic Cumics{/b}?"
    show lily f_normal
    show player 29
    player_name "Эммм... Да! Я не знал что это место существовало..."
    show lily f_normal_talk
    show player 1
    lily "Да мы только недавно открылись!"
    show lily f_normal
    show player 2
    player_name "Ох, круто!"
    player_name "Вы ребята вы продаете видео-игры тоже?"
    show lily f_laugh
    show player 1
    lily "Конечно."
    show lily f_normal_talk
    lily "Мы продаем разнообразные продукты начиная от {b}видео-игр{/b},{b}комиксов{/b}, {b}фигурок{/b}, {b}плакатов{/b} и {b}коллекционных предметов{/b}!"
    show lily f_normal
    show player 2
    player_name "Ох. и так... задротские вещи..."
    show lily f_laugh
    show player 1
    lily "Ага!"
    lily "Осмотрись, и дай мне знать если тебе понадобится помощь с чем-нибудь!"
    hide lily
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
