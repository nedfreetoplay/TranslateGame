label consumr_diane_get_milk_jug_bought:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 173 with dissolve
    player_name "Хорошо, это должно хорошо работать для кувшина, который хотела {b}Диана{/b}."
    label consumr_diane_get_milk_jug_bought.tail:
    show player 172
    pause
    player_name "( Хм, интересно, стоит ли мне поговорить с {b}Дианой{/b} о вещах, которые мне рассказала {b}Вероника{/b}? )"
    player_name "( Я не уверен, что это относится к ее конкретной проблеме, но это не помешает разобраться. )"
    player_name "( {b}Я должен отправиться в библиотеку{/b} и найти одну из тех упомянутых {b}Вероникой{/b} книг о доении. )"
    hide player with dissolve
    $ M_diane.trigger(T_diane_bought_milk_jug)
    $ game.main()

label consumr_diane_get_milk_jug_owned:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 173 with dissolve
    player_name "Hey! I already had one of these!"
    player_name "This should work fine for the jug {b}Diane{/b} wanted."
    jump consumr_diane_get_milk_jug_bought.tail

label consumr_diane_get_milk_jug:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 13 at left
    show vero f_sexy_talk
    with dissolve
    vero "Так, так, так ... Смотри, кто заходит в мой магазин!"
    show vero f_sexy
    show player 14
    player_name "Привет, {b}Вероника{/b}."
    show player 13
    show vero f_normal_talk
    vero "Как дела, {b}[firstname]{/b}?"
    vero "У тебя все еще есть зеленый палец?"
    show vero f_normal
    show player 14
    player_name "Хе-хе, да, наверное."
    show player 13
    show vero f_sexy_talk
    vero "О, я люблю человека, который знает дорогу в саду..."
    show vero f_sexy
    show player 29 with dissolve
    player_name "{b}*глоток*{/b} О, да?"
    show player 3
    show vero f_normal_talk
    vero "Так что привело тебя сюда?"
    show vero f_normal
    show player 14 with dissolve
    player_name "Мне нужен еще один {b}кувшин под молоко для Дианы{/b}."
    show player 13
    show vero f_normal_talk
    vero "Да?"
    vero "Как она вообще себя чувствует?"
    vero "Я пыталась заскочить и навестить ее на днях, но там было много строительных работ."
    show vero f_normal
    show player 14
    player_name "Хех, да. Она снесла свой дом и поставила сарай."
    show player 13
    show vero f_surprised
    vero "!!!"
    show vero f_normal_talk
    vero "Ты не говорил?!"
    vero "Итак, я думаю, она наконец-то расширяется, да?"
    show vero f_normal
    show player 14
    player_name "Да, наверное, так и есть."
    show player 13
    show vero f_normal_talk
    vero "Она вообще упоминала, что нанимала дополнительную помощь?"
    show vero f_normal
    show player 14
    player_name "Хм, немного ..."
    show player 13
    show vero f_normal_talk
    vero "Ну, скажи ей, чтобы она помнила, что ее хорошая подруга {b}Вероника{/b} работает в этом тупике!"
    show vero f_normal
    show player 17
    player_name "Ха-ха, хватит."
    show player 14
    player_name "Я думаю, сейчас она слишком занята, беспокоясь о производстве молока..."
    show player 13
    vero "Хмм?"
    show vero f_normal_talk
    vero "Ее коровы высыхают?"
    show vero f_normal
    show player 10
    player_name "Я эээ..."
    show player 5
    show vero f_normal_talk
    vero "Расскажи мне, {b}[firstname]{/b}."
    vero "Я знаю все, что нужно знать о доении коров."
    show vero f_normal
    show player 10
    player_name "Хех, я не знаю... Я не должен говорить об этом."
    show player 5
    show vero f_normal_talk
    vero "Ой, да ладно!"
    show vero f_normal
    show player 29 with dissolve
    player_name "Ей просто нужна ее эээ... корова."
    player_name "Чтобы ... Вы знаете, производить больше молока."
    show player 3
    show vero f_normal_talk
    vero "Она оплодотворяет их?"
    show vero f_normal
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "О-оплодотворяет?!"
    show player 11
    show vero f_laugh
    vero "Ну, конечно!"
    show vero f_normal_talk
    vero "Коровы будут производить совсем немного молока сами по себе, но если вы действительно хотите получить от них все, что можете, вы должны их подбить."
    show vero f_normal
    show player 29 with dissolve
    player_name "{b}*глоток*{/b} Я не-"
    show player 3
    show vero f_normal_talk
    vero "Это удвоит их производство молока, легко!"
    vero "Потом, когда теленок родится, его можно продать с большой прибылью."
    show vero f_normal
    player_name "..."
    show vero f_normal_talk
    vero "... Или оставь себе, и ты получил себе нового работника!"
    vero "Это отличный источник дополнительного дохода."
    show vero f_normal
    show player 29
    player_name "О, я не думаю, что она захочет-"
    show player 3
    show vero f_normal_talk
    vero "Почему ты покраснел?"
    show vero f_normal
    show player 29
    player_name "Я не-"
    show player 3
    show vero f_laugh
    vero "Хе-хе, что происходит {b}[firstname]{/b}?!"
    show vero f_normal
    show player 12 with dissolve
    player_name "Ничего!"
    show player 10
    player_name "Я просто... Ты уверена?"
    show player 5
    show vero f_normal_talk
    vero "Конечно."
    vero "{b}Иди в библиотеку и посмотри{/b} , если ты мне не веришь, я уверена, что ты найдешь тонны информации о разведении и доении сельскохозяйственных животных."
    show vero f_normal
    show player 14
    player_name "Да, хорошо."
    player_name "Схожу."
    show player 13
    show vero f_laugh
    vero "Хе-хе, ты слишком милый!"
    show vero f_normal_talk
    vero "У нас есть кувшины из нержавеющей стали вон там."
    vero "Дай мне знать, если тебе понадобится помощь."
    show vero f_normal
    show player 14
    player_name "Спасибо, {b}Вероника{/b}."
    show player 13
    show vero f_sexy_talk
    vero "Никаких проблем, жеребец."
    hide player
    hide vero
    with dissolve
    return

label consumr_okita_get_ingredients:
    call expression game.dialog_select("consumr_okita_get_ingredients_pre")
    if M_okita.get("talked with veronica"):
        call expression game.dialog_select("consumr_okita_get_ingredients_talked_with_veronica")
    return

label consumr_okita_get_ingredients_pre:
    scene location_mall_consumr_day_blur
    show player 2
    with dissolve
    player_name "Окита сказал ,что {b} овощной бульон{/b} будет лучше всего работать в качестве базовой жидкости."
    return

label consumr_okita_get_ingredients_talked_with_veronica:
    show player 10
    player_name "... Но у них есть только {b}куриный бульон{/b}."
    player_name "Думаю, придется обойтись {b}куриным бульоном{/b}."
    show player 2
    player_name "Я должен {b}купить{/b} немного и отнисти к Оките."
    hide player with dissolve
    return

label consumr_diane_get_bug_spray:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show diane b_casual a_casual_sides f_normal_talk at flip
    show diane at Position (xpos=-100)
    show player 13f
    with dissolve
    dia "Хорошо, на том, что нам нужно ,будет {b}зеленая крышка{/b}..."
    show diane f_normal
    show vero f_normal_talk at Position (xpos=600) with dissolve
    vero "{b}Диана{/b}?!"
    show player 13 with dissolve
    vero "Давно не виделись!"
    show vero f_normal
    show diane f_normal_talk
    dia "Привет, {b}Ви{/b}."
    show diane f_normal
    show vero f_normal_talk
    vero "Приятно видеть тебя наконец-то вне дома!"
    vero "Ты пришла за садовыми принадлежностями?"
    show vero f_normal
    show diane f_normal_talk
    dia "Хех, да. Что-то вроде этого..."
    show diane f_normal
    show vero f_normal_talk
    vero "Как жаль, что ты застряла в этом огромном саду одна."
    show vero f_normal
    dia "..."
    show vero f_normal_talk
    vero "Знаешь, я была бы более чем счастлива-"
    show vero f_normal
    show player 14
    player_name "Привет, Я {b}[firstname]{/b}."
    show player 13
    show vero f_normal_talk
    vero "О, привет."
    vero "Я не знала, что вы двое вместе..."
    show vero f_normal
    show diane f_laugh
    dia "О, мы-"
    show diane f_normal
    show vero f_normal_talk
    vero "Я {b}Вероника{/b}."
    show vero f_normal
    show player 14
    player_name "Приятно познакомиться."
    show player 13
    show vero f_normal_talk
    vero "Вау, {b}Диана{/b}!"
    vero "Ты что-то скрываешь от меня."
    show player 11
    vero "Где ты нашла такого красивого молодого человека?!"
    show vero f_normal
    show diane f_normal_talk
    dia "Я не-"
    show diane f_normal
    show player 14
    player_name "Этим летом я помог ей с садом."
    show player 13
    show vero f_sexy_talk
    vero "Ты не говорила..."
    vero "Так когда вы начали встречаться?"
    show vero f_sexy
    show player 23
    player_name "Встречаться?!" with hpunch
    show player 22
    show diane f_surprised
    dia "!!!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "О, Я не..."
    show player 3
    show vero f_sexy_talk
    vero "Хмм?"
    show vero f_sexy
    show diane f_smirk_talk
    dia "{b}[firstname]{/b}, просто мой друг..."
    show diane f_smirk
    show player 13 with dissolve
    show vero f_laugh
    vero "О, прости!"
    show vero f_normal_talk
    vero "Я не хотела делать поспешных выводов, я просто подумала..."
    show vero f_thinking
    vero "..."
    show vero f_laugh
    vero "Хехе, неважно."
    dia "..."
    show vero f_normal_talk
    vero "{b}*гм*{/b} Могу я вам чем-нибудь помочь?"
    show vero f_normal
    show diane f_normal_talk
    dia "Нет, спасибо. Мы точно знаем, что нам нужно."
    show diane f_normal
    show vero f_normal_talk
    vero "Хорошо, я оставлю вас наедине с этим..."
    vero "... Позвони мне как-нибудь!"
    show vero f_sexy_talk
    vero "Я бы хотела услышать больше о том, чем ты занималась этим летом."
    show vero f_sexy
    show diane f_normal_talk
    dia "Хех, да. Хорошо."
    dia "Пока, {b}Ви{/b}."
    show diane f_normal
    hide vero with dissolve
    pause
    show player 10f at right with dissolve
    player_name "Откуда ты ее знаешь?"
    show player 13f
    show diane f_thinking
    dia "О, она часто мне помогала... Знаешь, с инструментами и советами по садоводству."
    show diane f_normal_talk
    dia "Она выросла на ферме, поэтому знает намного больше меня."
    show diane f_normal
    show player 14f
    player_name "Она кажется милой."
    show player 13f
    show diane f_normal_talk
    dia "Да, она действительно хорошая девушка."
    dia "Немного легкомысленная ... Но, конечно, доброжелательная и вежливая."
    show diane f_laugh
    dia "Не могу поверить, что она думала, что мы встречаемся..."
    show diane f_normal
    show player 14f
    player_name "Почему нет?"
    show player 13f
    show diane f_teasing
    dia "Потому что ты такой молодой и красивый, а я такая-"
    show diane f_normal
    show player 14f
    player_name "Не говори что старая. Ты не старая..."
    show player 17f
    player_name "... И ты действительно привлекательная, {b}Диана{/b}!"
    show player 13f
    show diane f_laugh_blush
    dia "Ой, прекрати!"
    show diane f_normal
    show player 14f
    player_name "Я серьезно!"
    show player 13f
    show diane f_smirk_talk
    dia "Хехе, спасибки..."
    show diane f_smirk
    dia "..."
    show diane f_shamed_talk_smile
    dia "{b}*гм*{/b} В любом случае, {b}пестицид{/b} должен быть вон там, на полке."
    show diane a_casual_money with dissolve
    dia "Вот деньги..."
    dia "Ищи балончик с {b}зеленой крышкой.{/b}"
    hide player
    hide diane
    with dissolve
    return

label consumr_diane_buy_bug_spray_brought:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 17 with dissolve
    player_name "Хорошо, теперь давайте вернемся в дом {b}Дианы{/b} и уничтожим этих жуков!"
    label consumr_diane_buy_bug_spray_brought.tail:
    hide player with dissolve
    $ M_diane.trigger(T_diane_find_correct_bug_spray)
    $ game.main()
    
label consumr_diane_buy_bug_spray_owned:
    scene expression "backgrounds/location_mall_consumr_closeup.jpg"
    show player 17 with dissolve
    player_name "Oh, I already had this one!"
    player_name "Better get this back to {b}Diane's{/b} house and eradicate those bugs!"
    jump consumr_diane_buy_bug_spray_brought.tail
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
