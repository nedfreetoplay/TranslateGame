label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with dissolve
    deb "Привет, милый..."
    deb "Ты меня искал?"
    show debbie 54
    show player 111
    player_name "Да..."
    show player 110
    show debbie 55
    deb "Ты что-то хотел от меня?"
    show debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    deb "Теперь, есть ли что-нибудь ещё, что тебе надо?"
    show debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show debbie 54 at left
    player_name "Могу я получить поцелуй?"
    show player 110
    show debbie 55
    deb "Конечно, милый! Иди сюда."
    scene debbie_bedroom
    show debbie 79
    with fade
    deb "Мммм..."
    show debbie 80_79
    pause 3
    show debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    deb "У тебя стало лучше получаться!"
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Привет, {b}[deb_name]{/b}!"
    player_name "Хочешь принять со мной душ?"
    show player 110
    show debbie 55
    deb "В доме становится довольно жарко..."
    deb "Конечно! Душ - звучит прекрасно."
    deb "Пойдем, милый. Я буду там через минуту."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Прости, что заставила ждать, милый."
    return

label debbie_dialogue_master_room_sex_random_true:
    show debbie 54 at left
    show player 111 at right
    player_name "Мне нравится... Делать это с тобой снова."
    show player 110
    show debbie 55
    deb "Все нормально!"
    deb "Я надеялась, что ты захочешь..."
    show player 111
    show debbie 54
    player_name "Правда?"
    show player 110
    show debbie 58 with dissolve
    deb "Конечно! В конце концов, ты мой мужчина."
    show debbie 57
    player_name "!!!"
    show debbie 58
    deb "Снимай одежду, милый."
    show debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show debbie 103
    deb "Ммм, иди возьми меня, милый!"
    show player 262 at right
    show debbie 102 at left
    player_name "Не нужно говорить мне дважды ..."
    return

label debbie_dialogue_master_room_sex_random_false:
    show debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, хотишь немного повеселиться?"
    show player 110
    show debbie 54
    deb "О?"
    show debbie 56 with dissolve
    deb "Любить... это забавно?"
    show debbie 57
    show player 111
    player_name "Конечно..."
    show player 110
    show debbie 58
    deb "Покажи мне свой член..."
    show debbie 57
    show player 8f with dissolve
    pause
    show debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show debbie 58
    deb "Похоже, что ты готов!"
    show debbie 57
    show player 262
    player_name "Я ждал этого с тех пор, как проснулся сегодня утром."
    show player 263
    show debbie 58
    deb "Я тоже."
    show debbie 102 with dissolve
    pause
    show debbie 103
    deb "Иди и возьми, милый."
    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show debbie 104 at left
    with dissolve
    pause
    hide debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show debbie 54
    show player 111
    player_name "Я хотел спросить, не нужна ли тебе помощь в подвале."
    show player 110
    show debbie 55
    deb "В подвале? Для чего?"
    show player 111
    show debbie 54
    player_name "Может, я смогу помочь тебе со стиркой... Как в прошлый раз?"
    show player 110
    show debbie 55
    deb "А, понятно... Я точно знаю, чего ты хочешь!"
    deb "Дай мне минутку подготовиться."
    deb "Встретимся там внизу..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "Я подумал, что нам стоит посмотреть фильм сегодня вечером. Интересно?"
    show player 110
    show debbie 55
    deb "Ммм, вечер кино, да?"
    deb "Это звучит великолепно, любимый!"
    show player 111
    show debbie 54
    player_name "Потрясающе!"
    player_name "Увидимся вечером в гостиной?"
    show player 110
    show debbie 55
    deb "Я не могу ждать..."
    return

label debbie_dialogue_master_room_leave:
    show debbie 54
    show player 111
    player_name "Ничего, {b}[deb_name]{/b}."
    player_name "Просто хотел поздороваться."
    show player 110
    show debbie 55
    deb "Ох, хорошо..."
    deb "Ну, возвращайся как захочешь... Я буду скучать..."
    deb "Мы можем повеселиться, когда захочешь."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
