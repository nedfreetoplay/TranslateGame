label diane_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Хмм?"
    player_name "{b}Я получил сообщение от {b}Дианы{/b}!"
    hide player with dissolve
    return

label diane_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur
        show player 12 with dissolve
    player_name "Интересно, что происходит?"
    player_name "{b}Я должен заскочить в сарай {b}Дианы{/b} и посмотреть, что случилось{/b}."
    hide player with dissolve
    return

label diane_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Похоже, я получил сообщение."
    hide player with dissolve
    return

label diane_pregnant_labor_2:
    scene expression player.location.background_blur
    show player 23 with dissolve
    player_name "Ребенок приближается!"
    player_name "Срань господня!"
    show player 22
    pause
    show player 23
    player_name "Я лучше пойду {b}в клинику{/b}, чтобы проверить их!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
