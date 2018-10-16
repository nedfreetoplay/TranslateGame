label tony_dialogue_pre:
    scene pizza_behind_c
    show xtra 12 zorder 2
    with None
    show maria 1 zorder 1 at left
    show tony 2 zorder 1 at Position(xpos=400)
    show player 1f zorder 3 at right
    with dissolve
    return

label tony_dialogue_deliver_pizzas_first:
    tony "Хей, парень!"
    tony "Готов к работе?"
    show tony 1
    show player 14f
    player_name "Конечно!"
    show tony 2
    show player 1f
    tony "Отлично! Прежде всего, у тебя должен быть {b}велосипед{/b} или что-то, что позволит тебе передвигаться быстрее."
    tony "Просто хватай те коробки и доставляй их на правильные адреса!"
    tony "Ох! Наши покупатели любят горячую пиццу."
    tony "Так что чем быстрее ты работаешь - тем больше получаешь!"
    show tony 1
    show player 14f
    player_name "Звучит неплохо, {b}Tony{/b}!"
    return

label tony_dialogue_deliver_pizzas_repeat:
    tony "Коробки прямо тут, парень!"
    return

label tony_dialogue_default:
    show tony 1f at right
    show player 10 at left
    tony "Тебе нужен велик, чтобы развозить пиццу!"
    show player 4
    player_name "( Уверен, что смогу купить его в {b}Consum'r{/b}... )"
    show player 2
    player_name "Окей, Tony, я скоро вернусь, но уже вместе с ним!"
    show tony 2f
    tony "Отлично, парень!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
