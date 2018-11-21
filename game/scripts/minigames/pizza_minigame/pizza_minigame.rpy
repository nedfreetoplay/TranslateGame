label pizza_minigame:
    if player.transport_level == 0:
        scene location_pizza_day_blur with None
        show player 35 with dissolve
        player_name "Мне нужно найти {b}велосипед{/b} или что-то такое, потому что я буду слишком медленно идти."
        hide player with dissolve
        jump pizza_interior_dialogue
    $ pizza_earnings = 0
    $ tips = False
    $ end_while_pizza_minigame = False
    if game.cheat_mode:
        $ tips = True
    else:
        $ tips = False
    scene location_pizza_day_blur with None
    while not end_while_pizza_minigame:
        menu:
            "Замедление времени: {color=#FFD700}ВКЛЮЧЕНО{/color}" if tips:
                $ tips = False

            "Замедление времени: ВЫКЛЮЧЕНО" if not tips:
                $ tips = True

            "Начать доставку.":
                $ end_while_pizza_minigame = True

    call screen pizza_minigame

label pizza_delivered_fail:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria 1 zorder 1 at left
    show tony 4 zorder 1 at Position(xpos=400)
    show player 5f zorder 3 at right
    with dissolve
    tony "Я получил несколько жалоб от клиентов..."
    tony "Они сказали, что получили пиццу поздно, и что она была холодной."
    show tony 1
    show player 10f
    player_name "Прости, Тони. Я должен был неверно прочитать адрес..."
    show player 11f
    show tony 2
    tony "Все в порядке, парень. Ты новичок в этом, со временем станет лучше."
    show player 1f
    tony "Вот твоя плата за работу, которую ты сделал, приходи позже, когда мы получим больше заказов."
    show player 17f
    show tony 1
    player_name "Спасибо, {b}Тони{/b}!"
    jump pizza_delivered

label pizza_delivered_success:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria 1 zorder 1 at left
    show tony 2 zorder 1 at Position(xpos=400)
    show player 1f zorder 3 at right
    with dissolve
    tony "Я знал, что могу рассчитывать на тебя малыш!"
    show tony 1
    show player 14f
    player_name "Я справился?"
    show tony 2
    show player 1f
    tony "Ещё как!"
    tony "Вот твоя зарплата, приходи позже, когда мы получим больше заказов!"
    show tony 1
    show player 17f
    player_name "Спасибо, {b}Тони{/b}!"
    jump pizza_delivered


label pizza_delivered:
    show unlock35 zorder 3 at truecenter
    show text "{size=30}{b}[pizza_earnings]{/b}{/size}" zorder 4 at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ player.get_money(pizza_earnings)
    $ renpy.pause()
    hide text "{b}[pizza_earnings]{/b}"
    hide unlock35
    with dissolve
    hide player
    hide tony
    hide maria
    with dissolve
    hide xtra
    hide location_pizza_day_blur
    $ del pizza_earnings
    $ game.timer.tick()
    if game.timer.is_dark():
        call expression game.dialog_select("map_dialogue")
    else:
        jump pizza_interior_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
