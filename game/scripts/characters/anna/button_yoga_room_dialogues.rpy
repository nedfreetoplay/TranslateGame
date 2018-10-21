label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Привет, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Привет, {b}Анна{/b}."
    show player 13
    show anna 2
    anna "В чем дело?"
    show anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "Я ищу {b}Миссис Джонсон{/b}."
    show player 30
    player_name "Ты знаешь, где я могу её найти?"
    show player 5
    show anna 2
    anna "Она обычно преподает в течение дня."
    anna "Сейчас она должна быть дома..."
    show anna 1
    show player 14
    player_name "О. Понятно. Спасибо!"
    show player 13
    show anna 3
    anna "Нет проблем!"
    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Хочешь попрактиковаться со мной в позах йоги?"
    show player 5
    show anna 3
    anna "Ну конечно!!"
    show anna 2
    anna "Мне нравится, когда кто-то может помочь мне постичь эти... сложные позы..."
    show anna 1
    show player 33
    player_name "Да, ты достаточно гибкая, насколько я помню."
    show player 13
    show anna 2
    anna "Хорошо, давай найдем коврик для йоги..."
    hide anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show anna 13
    with dissolve
    anna "Какую позицию мы должны тренировать?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
