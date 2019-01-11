label pizza_minigame:
    if player.transport_level == 0:
        scene location_pizza_day_blur with None
        show player 35 with dissolve
        player_name "Мне нужно найти {b}велосипед{/b} или что-то такое, потому что я буду слишком медленно идти."
        hide player with dissolve
        jump pizza_interior_dialogue
    $ pizza_earnings = 0
    if player.transport_level > 1:
        menu:
            "На велосипеде.":
                call screen pizza_minigame(1)
            "На скутере." if player.transport_level>1:
                call screen pizza_minigame(2)
            "На маленькой машинке." if player.transport_level>2:
                call screen pizza_minigame(3)
            "На спортивном авто." if player.transport_level>3:
                call screen pizza_minigame(4)
    call screen pizza_minigame(1)

label pizza_delivered_fail:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria f_normal zorder 1 at fliplleft
    show tony f_suspicious zorder 0 at flip, Position (xpos=750)
    show player 5f zorder 3 at right
    with dissolve
    tony "Я получил несколько жалоб от клиентов..."
    tony "Они сказали, что получили пиццу поздно, и что она была холодной."
    show player 10f
    player_name "Прости, Тони. Я должен был неверно прочитать адрес..."
    show player 11f
    show tony f_normal_talk at flip
    tony "Все в порядке, парень. Ты новичок в этом, со временем станет лучше."
    show player 1f
    tony "Вот твоя плата за работу, которую ты сделал, приходи позже, когда мы получим больше заказов."
    show player 17f
    show tony f_normal
    player_name "Спасибо, {b}Тони{/b}!"
    jump pizza_delivered

label pizza_delivered_success:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria f_normal zorder 1 at fliplleft
    show tony f_normal_talk zorder 0 at flip, Position (xpos=750)
    show player 1f zorder 3 at right
    with dissolve
    tony "Я знал, что могу рассчитывать на тебя малыш!"
    show tony f_normal at flip
    show player 14f
    player_name "Я справился?"
    show tony f_normal_talk
    show player 1f
    tony "Ещё как!"
    tony "Вот твоя зарплата, приходи позже, когда мы получим больше заказов!"
    show tony f_normal
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
