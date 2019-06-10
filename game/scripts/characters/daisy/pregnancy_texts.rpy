label daisy_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Хмм?"
    player_name "У меня сообщение от {b}Дианы{/b}!"
    hide player with dissolve
    return

label daisy_pregnant_announcement_2:
    if not player.location == L_map:
        scene expression player.location.background_blur with None
        show player 10 with dissolve
    player_name "Интересно, что происходит?"
    player_name "{b}Я должен заскочить в амбар {b}Дианы{/b} и посмотреть, в чем дело.{/b}."
    hide player with dissolve
    return

label daisy_pregnant_labor_1:
    scene expression player.location.background_blur
    show player f_normal_talk with dissolve
    player_name "Похоже, я получил сообщение."
    hide player with dissolve
    return

label daisy_pregnant_labor_2:
    scene expression player.location.background_blur with None
    show player 14 with dissolve
    player_name "Ребенок здесь!"
    show player 10
    player_name "Черт побери!"
    show player 5
    pause
    show player 14
    player_name "Я лучше пойду в {b}сарай{/b}, проверю, как они там."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
