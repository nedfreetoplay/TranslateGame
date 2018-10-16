label consumr_quest10_not_completed:
    scene consumr
    show player 4 with dissolve
    player_name "( Здесь должен быть весьма неплохой выбор пестицидов. )"
    show player 10
    player_name "( Я не уверен что именно мне нужно. )"
    player_name "( Возможно, я должен спросить у {b}продавщицы{/b}, как {b}тётя Диана{/b} и предлагала. )"
    hide player with dissolve
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
    player_name "Окита сказала, что {b}Растительное сырьё{/b} подойдет лучше всего для основы сыворотки."
    return

label consumr_okita_get_ingredients_talked_with_veronica:
    show player 10
    player_name "... Но у них есть только {b}Куринный бульон{/b}."
    player_name "Похоже придется обойтись {b}куринным бульоном{/b}."
    show player 2
    player_name "Мне нужно {b}купить{/b} и отнести его Оките."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
