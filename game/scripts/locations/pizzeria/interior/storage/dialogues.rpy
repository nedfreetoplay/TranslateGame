label pizzeria_storage_diane_delivery_1_place_goods:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 163d at left
    show maria f_normal_talk at flip, Position (xpos=750)
    with dissolve
    maria "Он находится прямо здесь."
    maria "У нас есть холодильная установка. Ничего особенного, но это-"
    show maria falling at unflip, lright with dissolve
    show player 163j
    maria "!!!"
    hide maria with dissolve
    maria "ААААХХХХХ!!!"
    show expression "backgrounds/location_pizza_cutscene01.jpg"
    show expression FilteredText("{b}Мария{/b} споткнулась о мешок с мукой и начала падать.\nОтчаянно хватаясь за полку, она упала...") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression "backgrounds/location_pizza_cutscene02.jpg"
    show expression FilteredText("К сожалению, все, что ей удалось сделать, это опрокинуть пару банок измельченных помидоров,\nпрежде чем упасть на пол.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    show expression FilteredText("Я застыл, как олень в свете фар, когда она лежала с обнаженной нижней половиной...") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 106 zorder 1 at left
    show maria knees zorder 1
    with dissolve
    maria "Тч, Ай..."
    show player 108f
    player_name "С вами все в порядке, мэм?"
    show player 114
    show maria knees_closed
    tony "МАРИЯ?!"
    show tony f_suspicious zorder 0 at flip, Position (xpos=600) with dissolve
    show player 5
    tony "Ты в порядке?!"
    tony "Какого черта происходит в-"
    show tony f_question at flip
    tony "!!!"
    tony "Господи, {b}Мария{/b}, ты выставлена на обозрение всему миру!"
    show maria knees_talk with dissolve
    maria "Ай, заткнись {b}Тони{/b}!"
    maria "Я же не специально это сделала!"
    show maria a_dressed_gross o_sauce f_surprised_down at Position (xpos=580) with dissolve
    maria "Это ты все время оставляешь муку, чтобы я споткнулась!"
    maria "Я не знаю, почему ты не можешь просто положить вещи туда, где они должны быть?!"
    show maria f_shy a_dressed_back with dissolve
    show tony f_suspicious at flip
    tony "Я забыл, хорошо?!"
    tony "Почему бы тебе не перестать бить меня по яйцам и не извиниться перед парнем?"
    tony "Ты, вероятно, напугала его до полусмерти, сверкая своими непослушными булочками перед ним!"
    show tony f_normal_talk at flip
    tony "Хахаха!"
    show tony f_normal at flip
    show maria f_shy_talk
    maria "О, пожалуйста."
    maria "Дети его возраста постоянно видят это в интернете."
    show maria f_sexy_talk
    maria "Он, наверное, думает, что это его счастливый день!"
    show maria f_sexy
    show player 10
    player_name "Я не был... Я...я не хотел этого делать..."
    show player 5
    show maria f_normal_talk
    maria "Хаха!"
    maria "Вот видишь. Он не беспокоит никого."
    show maria f_sexy_talk
    maria "Знаешь, он такой милый, когда волнуется."
    maria "Возможно, он как раз тот, кто займет должность, которую ты рекламировал."
    show maria f_sexy
    show tony f_question at unflip
    show tony f_question at Position (xpos=400)
    with dissolve
    tony "Хмм, да."
    tony "Now that you mention it, he does kinda look like a young me..."
    show tony f_normal
    show player 11
    player_name "..."
    show tony f_normal_talk
    tony "У тебя есть велосипед, малыш?"
    show tony f_normal
    return

label pizzeria_storage_diane_delivery_1_place_goods_no_bike:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 10 zorder 1 at left
    show tony f_normal zorder 0 at Position (xpos=400)
    show maria f_sexy o_sauce zorder 1 at Position (xpos=580)
    player_name "Нет, боюсь, что нет."
    show player 5
    show tony f_normal_talk
    tony "А, черт."
    tony "Вот что я тебе скажу..."
    tony "Купи себе велосипед и возвращайся ко мне."
    tony "Я сделаю вам предложение, от которого вы не сможете отказаться, ферштейн?"
    show tony f_normal
    show player 29 with dissolve
    player_name "Да, хорошо..."
    show player 3
    show tony f_normal_talk
    tony "Вот хороший мальчик."
    tony Вот деньги на молоко."
    show tony a_dressed_money with dissolve
    tony "Ты приходи к нам поскорее, слышишь?"
    show tony f_normal a_dressed_hips
    show player 640e
    with dissolve
    player_name "Спасибо, {b}Тони{/b}!"
    show player 640d
    show maria f_sexy_talk
    maria "Прощай, красавчик."
    show maria f_sexy
    show player 21 with dissolve
    player_name "Пока, {b}Мария{/b}."
    hide player
    hide maria
    hide tony
    with dissolve
    return


label pizzeria_storage_diane_delivery_1_place_goods_bike:
    scene expression "backgrounds/location_pizza_storage_day_blur.jpg"
    show player 17 zorder 1 at left
    show tony f_normal zorder 0 at Position (xpos=400)
    show maria f_sexy o_sauce zorder 1 at Position (xpos=580)
    player_name "Да, у меня есть."
    show player 13
    show tony f_question
    tony "Правда?!"
    show tony f_normal_talk
    tony "Теперь есть ребенок, у которого есть свои приоритеты!"
    tony "Вот что я тебе скажу..."
    tony "Если ты когда-нибудь будешь искать работу, приходи ко мне."
    tony "Я сделаю вам предложение, от которого вы не сможете отказаться, ферштейн?"
    show tony f_normal
    show player 29 with dissolve
    player_name "Да, хорошо..."
    show player 3
    show tony f_normal_talk
    tony "Это хорошо, парень."
    tony "Вот деньги на молоко."
    show tony a_dressed_money with dissolve
    tony "Ты приходи к нам поскорее, слышишь?"
    show tony f_normal a_dressed_hips
    show player 640e
    with dissolve
    player_name "Спасибо, {b}Тони{/b}!"
    show player 640d
    show maria f_normal_talk
    maria "Пока, {b}[firstname]{/b}."
    show maria f_normal
    show player 21 with dissolve
    player_name "Пока, {b}Мария{/b}."
    hide player
    hide tony
    hide maria
    with dissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
