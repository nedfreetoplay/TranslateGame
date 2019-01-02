label tony_dialogue_veggie_pizza_no_money_repeat:
    show player 10f
    player_name "О, черт."
    player_name "У меня с собой недостаточно денег."
    show player 5f
    show tony f_question
    tony "Ну, ты не можешь получить пиццу без денег."
    tony "О чем ты думал, тупица?"
    show tony f_suspicious
    show player 29f with dissolve
    player_name "Хех, прости."
    show player 5f with dissolve
    show tony f_question
    tony "Просто приходи, когда получишь достаточно денег, хорошо?"
    show tony f_suspicious
    show player 10f
    player_name "Хорошо."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_has_money_repeat:
    show player 14f zorder 3 at right
    player_name "Вот, держи."
    show player 41f with dissolve
    pause
    show player 13f
    show tony f_question at unflip
    show tony at Position (xpos=100)
    with dissolve
    tony "Йоу, {b}Мария{/b}!"
    tony "Одну овощную с грибами и ананасом, на вынос."
    maria "Да, да..."
    hide tony with dissolve
    maria "Знаешь, моя мать сожгла бы это место дотла, прежде чем положить ананас в пиццу..."
    maria "... Это просто не правильно."
    tony "Хорошо, что я женился на тебе, а не на твоей матери, не так ли?"
    maria "Хаха!"
    pause
    show tony a_dressed_pizza f_normal_talk zorder 1 at fliplleft with dissolve
    tony "Вот твой пирог, малыш."
    show tony f_normal a_dressed_hips
    show player 719bf
    with dissolve
    player_name "Спасибо, {b}Тони{/b}."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_repeat:
    scene pizza_behind_c
    show xtra 12 zorder 2 with None
    show player 14f zorder 3 at right
    show tony f_normal zorder 1 at fliplleft
    player_name "Могу ли я получить еще одну {b}вегетарианскую пиццу{/b}?"
    show player 13f
    show tony f_normal_talk
    tony "Конечно, малыш."
    tony "Она стоит $20."
    show tony f_normal
    return

label tony_dialogue_nevermind_pizza_order:
    show player 10f zorder 3 at right
    player_name "Э-э, вообще-то ... не важно."
    player_name "Я не хочу, чтобы в конце концов."
    show player 5f
    show tony f_normal_talk
    tony "Нет?"
    tony "Хорошо, малыш."
    show tony f_normal
    pause
    show tony f_normal_talk
    tony "Возвращайся, если передумаешь."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_no_money_first:
    show player 10f
    player_name "О, черт."
    player_name "У меня с собой недостаточно денег."
    show player 5f
    show tony f_question
    tony "Ну, ты не можешь получить пиццу без денег."
    tony "О чем ты думал, тупица?"
    show tony f_suspicious
    show player 29f with dissolve
    player_name "Хех, прости."
    show player 13f with dissolve
    show tony f_normal_talk
    tony "Просто приходи, когда получишь достаточно денег, хорошо?"
    show tony f_normal
    show player 14f
    player_name "Хорошо."
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_has_money_first:
    show player 14f zorder 3 at right
    player_name "Вот и я."
    show player 41f with dissolve
    pause
    show player 13f
    show tony f_question at unflip
    show tony at Position (xpos=100)
    with dissolve
    tony "Йоу, {b}Мария{/b}!"
    tony "У нас тут клиент!"
    show tony f_suspicious
    maria "Я знаю, что ты сейчас не кричишь на меня, {b}Тони{/b}!"
    maria "Можешь развернуться и вежливо спросить."
    show tony f_normal_talk
    tony "О, черт."
    tony "Вы можете поверить этой женщине?"
    show player 9f with dissolve
    tony "Тчч, шары у нее..."
    hide tony with dissolve
    tony "Послушай женщина..."
    tony "Это ты должна разбираться с клиентами."
    tony "Бог свидетель, если бы они увидели твое милое личико, а не эту уродливую рожу, у нас было бы гораздо больше заказов."
    maria "Да, но они никогда не вернутся после того, как отведают твоей стряпни!"
    tony "Ой, это так грубо!"
    tony "Хаха!"
    maria "Хаха!"
    maria "Да, конечно... Поцелуй меня и возьми свой пирог."
    tony "Ну что ж, кто откажется от этого?"
    pause
    tony "Хехехе."
    show tony a_dressed_pizza f_normal_talk zorder 1 at fliplleft with dissolve
    tony "{b}*гмм*{/b} Ох, прости за все это."
    show tony f_normal
    show player 14f with dissolve
    player_name "Нет проблем."
    show player 13f
    show tony f_normal_talk
    tony "Вот твой пирог."
    show tony a_dressed_hips
    show player 719f
    with dissolve
    tony "Наслаждайся!"
    show tony f_normal

    show player 720 with dissolve
    player_name "( О, действительно вкусно пахнет. )"
    player_name "( Надеюсь {b}Дейзи{/b} понравится. )"
    hide player with dissolve
    return

label tony_dialogue_veggie_pizza_first:
    show player 14f zorder 3 at right
    player_name "Можно мне одну со всеми овощами?"
    show player 13f
    show tony f_normal_talk
    tony "Конечно, малыш!"
    tony "Ты тоже хочешь грибов и ананасов?"
    show tony f_normal
    show player 14f
    player_name "О, да пожалуйста!"
    show player 13f
    show tony f_normal_talk
    tony "Будет стоить $20."
    show tony f_normal
    return

label tony_dialogue_pizza_order:
    scene pizza_behind_c
    show xtra 12 zorder 2 with None
    show player 14f zorder 3 at right
    show tony f_normal zorder 1 at fliplleft
    player_name "Я возьму одну большую пиццу, пожалуйста."
    show player 13f
    show tony f_normal_talk
    tony "Теперь мы говорим!"
    tony "Какой пирог ты ищешь?"
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
