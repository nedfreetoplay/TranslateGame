label trailer_shack_cant_go_in:
    scene expression L_trailer_shack.background_blur
    player_name "Сейчас я не могу туда войти."
    return

label shack_doghouse_roxxy_get_uniform_on_doggo:
    scene expression "backgrounds/location_trailer_shack_closeup_day.jpg"
    show player 109f at left
    show roxxy 3d at right
    with dissolve
    pig "{b}*хрю-хрю*{/b}"
    show player 111f
    player_name "Вот ты где!"
    show player 110f
    pig "{b}*Фырк*{/b}"
    show roxxy 3c
    rox "Фу, отвратительное создание!"
    show roxxy 3d
    show player 111f
    player_name "Ууу, ты такая миленькая... Правда ведь?"
    show player 110f
    pig "{b}*Хрю*{/b}"
    show player 184 with dissolve
    pause
    show player 630 with dissolve
    player_name "Прости, хрюшка."
    player_name "Эту униформу нужно отдать обратно {b}Рокси{/b}..."
    show player 631 with dissolve
    pause
    show player 632 with dissolve
    pig "{b}*Уиииииии*{/b}"
    show player 633 with dissolve
    player_name "Хехе, не переживай."
    player_name "Уверен, {b}Клайд{/b} подыщет тебе новый наряд."
    show player 184 with dissolve
    pause
    show player 634 with dissolve
    pig "{b}*Фырк*{/b}"
    show roxxy 2
    rox "Ага, возможно даже из моего гардероба."
    show player 5
    show roxxy 61
    with dissolve
    player_name "..."
    show roxxy 60
    rox "Ну и бардак!"
    show roxxy 62
    rox "Пойдем ко мне."
    rox "Мне нужно отмыть запах свиньи!"
    hide roxxy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
