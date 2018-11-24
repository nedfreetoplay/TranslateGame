label pizza_minigame:
    if player.transport_level == 0:
        scene location_pizza_day_blur with None
        show player 35 with dissolve
        player_name "I need to find a {b}bicycle{/b} or something, I'll be too slow on foot. Anything on wheels should do."
        hide player with dissolve
        jump pizza_interior_dialogue
    $ pizza_earnings = 0
    call screen pizza_minigame

label pizza_delivered_fail:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria f_normal zorder 1 at fliplleft
    show tony f_suspicious zorder 0 at flip, Position (xpos=750)
    show player 5f zorder 3 at right
    with dissolve
    tony "I got some complaint calls from customers..."
    tony "They said they got their pizza late and that it was cold."
    show player 10f
    player_name "Sorry, {b}Tony{/b}. I must of read the address wrong..."
    show player 11f
    show tony f_normal_talk at flip
    tony "It's alright, kid. You're new at this, you'll get better over time."
    show player 1f
    tony "Here's your pay for the work you did, come back later when we got more deliveries."
    show player 17f
    show tony f_normal
    player_name "Thanks, {b}Tony{/b}!"
    jump pizza_delivered

label pizza_delivered_success:
    scene pizza_behind_c with None
    show xtra 12 zorder 2 with None
    show maria f_normal zorder 1 at fliplleft
    show tony f_normal_talk zorder 0 at flip, Position (xpos=750)
    show player 1f zorder 3 at right
    with dissolve
    tony "I knew I could count on you kid!"
    show tony f_normal at flip
    show player 14f
    player_name "I did alright?"
    show tony f_normal_talk
    show player 1f
    tony "You sure did!"
    tony "Here's your pay, come back later when we got more deliveries!"
    show tony f_normal
    show player 17f
    player_name "Thanks, {b}Tony{/b}!"
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
