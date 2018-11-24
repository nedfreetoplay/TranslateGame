label tony_dialogue_pre:
    scene pizza_behind_c
    show xtra 12 zorder 2
    with None
    show maria f_normal zorder 1 at fliplleft
    show tony f_normal_talk zorder 0 at flip, Position (xpos=750)
    show player 1f zorder 3 at right
    with dissolve
    return

label tony_dialogue_deliver_pizzas_first:
    tony "Hey, kid!"
    tony "Ready to work?"
    show tony f_normal at flip, Position (xpos=750)
    show player 14f
    player_name "Sure!"
    show tony f_normal_talk at flip
    show player 1f
    tony "Good! Before we start, make sure you got a {b}bicycle{/b} or something - anything - to get you around faster."
    tony "Then grab those boxes on the counter, and deliver them to the right addresses!"
    tony "Oh! Our customers love their pizzas nice and hot."
    tony "So the faster you work, the more I'll pay ya!"
    show tony f_normal
    show player 14f
    player_name "Sounds good, {b}Tony{/b}!"
    return

label tony_dialogue_deliver_pizzas_repeat:
    tony "The boxes are right there, kid!"
    return

label tony_dialogue_default:
    show tony f_normal_talk at flip, Position (xpos=750)
    show player 10f
    tony "You need to get a bike to deliver pizzas, kiddo!"
    show tony f_normal at flip
    show player 4f
    player_name "( I bet I could buy a bike at {b}Consum'r{/b}... )"
    show player 2f
    player_name "Thanks, {b}Tony{/b}. I'll get a bike and come back!"
    show tony f_normal_talk
    tony "You do, you kid!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
