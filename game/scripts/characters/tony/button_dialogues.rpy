label tony_dialogue_veggie_pizza_no_money_repeat:
    show player 10f
    player_name "Oh, crap."
    player_name "I don't have enough money on me."
    show player 5f
    show tony f_question
    tony "Well, you can't get no pizza without money."
    tony "What are you thinkin' knucklehead?"
    show tony f_suspicious
    show player 29f with dissolve
    player_name "Heh, sorry."
    show player 5f with dissolve
    show tony f_question
    tony "Just come back when you got some cash on ya, alright?"
    show tony f_suspicious
    show player 10f
    player_name "Will do."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_has_money_repeat:
    show player 14f zorder 3 at right
    player_name "Here ya go."
    show player 41f with dissolve
    pause
    show player 13f
    show tony f_question at unflip
    show tony at Position (xpos=100)
    with dissolve
    tony "'Ey, {b}Maria{/b}!"
    tony "One vegetable with mushrooms and pineapple, to go."
    maria "Yeah, yeah..."
    hide tony with dissolve
    maria "You know, my mother would burn this place to the ground before she'd put pineapple on a pizza..."
    maria "... It just ain't right."
    tony "Yeah well, it's a good thing I married you and not your mother then, aint it?"
    maria "Haha!"
    pause
    show tony a_dressed_pizza f_normal_talk zorder 1 at fliplleft with dissolve
    tony "Here's your pie, kiddo."
    show tony f_normal a_dressed_hips
    show player 719bf
    with dissolve
    player_name "Thanks, {b}Tony{/b}."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_repeat:
    scene pizza_behind_c
    show xtra 12 zorder 2 with None
    show player 14f zorder 3 at right
    show tony f_normal zorder 1 at fliplleft
    player_name "Could I get another {b}veggie pizza{/b}?"
    show player 13f
    show tony f_normal_talk
    tony "Sure thing, kiddo."
    tony "That'll be $20."
    show tony f_normal
    return

label tony_dialogue_nevermind_pizza_order:
    show player 10f zorder 3 at right
    player_name "Uhh, actually... Nevermind."
    player_name "I don't want one afterall."
    show player 5f
    show tony f_normal_talk
    tony "No?"
    tony "Alright, kiddo."
    show tony f_normal
    pause
    show tony f_normal_talk
    tony "Come back if you change your mind."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_no_money_first:
    show player 10f
    player_name "Oh, crap."
    player_name "I don't have enough money on me."
    show player 5f
    show tony f_question
    tony "Well, you can't get no pizza without money."
    tony "What are you thinkin' knucklehead?"
    show tony f_suspicious
    show player 29f with dissolve
    player_name "Heh, sorry."
    show player 13f with dissolve
    show tony f_normal_talk
    tony "Just come back when you got some cash on ya, alright?"
    show tony f_normal
    show player 14f
    player_name "Will do."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_has_money_first:
    show player 14f zorder 3 at right
    player_name "Here ya go."
    show player 41f with dissolve
    pause
    show player 13f
    show tony f_question at unflip
    show tony at Position (xpos=100)
    with dissolve
    tony "'Ey, {b}Maria{/b}!"
    tony "We got a customer 'ere!"
    show tony f_suspicious
    maria "I know you ain't yellin' orders at me now, {b}Tony{/b}!"
    maria "You can turn your fat ass around and ask politely."
    show tony f_normal_talk
    tony "Ah, sheesh."
    tony "Can you believe this woman?"
    show player 9f with dissolve
    tony "Tch, the balls on her..."
    hide tony with dissolve
    tony "Now you look here woman..."
    tony "It should be you up here dealin' with the customers."
    tony "God knows, we'd be bringing in a lot more business if they saw your pretty face 'ere instead of this ugly mug."
    maria "Yeah but they'd never come back after they tasted your cookin'!"
    tony "Oh, now that's just mean!"
    tony "Haha!"
    maria "Haha!"
    maria "Yeah, yeah... Come gimme a kiss and take your pie."
    tony "Ah well, who could refuse that?"
    pause
    tony "Hehehe."
    show tony a_dressed_pizza f_normal_talk zorder 1 at fliplleft with dissolve
    tony "{b}*Ahem*{/b} Uhh, sorry about all that."
    show tony f_normal
    show player 14f with dissolve
    player_name "No problem."
    show player 13f
    show tony f_normal_talk
    tony "Here's your pie."
    show tony a_dressed_hips
    show player 719f
    with dissolve
    tony "Enjoy!"
    show tony f_normal

    show player 720 with dissolve
    player_name "( Oh, this smells really good. )"
    player_name "( I hope {b}Daisy{/b} likes it. )"
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_first:
    show player 14f zorder 3 at right
    player_name "Can I get one with all the vegetables?"
    show player 13f
    show tony f_normal_talk
    tony "Sure thing, kiddo!"
    tony "You want mushrooms and pineapple too?"
    show tony f_normal
    show player 14f
    player_name "Oh, yes please!"
    show player 13f
    show tony f_normal_talk
    tony "That'll be $20."
    show tony f_normal
    return

label tony_dialogue_pizza_order:
    scene pizza_behind_c
    show xtra 12 zorder 2 with None
    show player 14f zorder 3 at right
    show tony f_normal zorder 1 at fliplleft
    player_name "I'll take one large pizza, please."
    show player 13f
    show tony f_normal_talk
    tony "Now we're talkin'!"
    tony "What kinda pie are you lookin' for?"
    show tony f_normal
    return

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
    tony "Привет, парень!"
    tony "Готов к работе?"
    show tony f_normal at flip, Position (xpos=750)
    show player 14f
    player_name "Конечно!"
    show tony f_normal_talk at flip
    show player 1f
    tony "Отлично! Прежде всего, у тебя должен быть {b}велосипед{/b} или что-то, что позволит тебе передвигаться быстрее."
    tony "Просто хватай те коробки и доставляй их на правильные адреса!"
    tony "Ох! Наши покупатели любят горячую пиццу."
    tony "Так что чем быстрее ты работаешь - тем больше получаешь!"
    show tony f_normal
    show player 14f
    player_name "Звучит неплохо, {b}Тони{/b}!"
    return

label tony_dialogue_deliver_pizzas_repeat:
    tony "Коробки прямо тут, парень!"
    return

label tony_dialogue_default:
    show tony f_normal_talk at flip, Position (xpos=750)
    show player 10f
    tony "Тебе нужен велик, чтобы развозить пиццу!"
    show tony f_normal at flip
    show player 4f
    player_name "( Уверен, что смогу купить его в {b}магазине{/b}... )"
    show player 2f
    player_name "Спасибо, {b}Тони{/b}. я скоро вернусь, но уже вместе с ним!"
    show tony f_normal_talk
    tony "Отлично, парень!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
