label anna_button_yoga_room_dialogue_pre:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Привет, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Привет, {b}Anna{/b}."
    show player 13
    show anna 2
    anna "Как дела?"
    show anna 1
    return

label anna_button_yoga_room_dialogue_wheres_mrsj:
    show player 14
    player_name "Я ищу {b}Миссис Джонсон{/b}."
    show player 30
    player_name "Вы не знаете, где я могу ее найти?"
    show player 5
    show anna 2
    anna "Обычно она проводит занятия в течение дня."
    anna "Она уже должна быть дома ..."
    show anna 1
    show player 14
    player_name "Ох. Понял. Благодарю!"
    show player 13
    show anna 3
    anna "Не проблема!"
    return

label anna_button_yoga_room_dialogue_yoga:
    show player 10
    player_name "Вы хотите заняться йогой со мной?"
    show player 5
    show anna 3
    anna "Of course!!"
    show anna 2
    anna "Мне нравится, когда кто-то может помочь мне достичь этих ... сложных позиций ..."
    show anna 1
    show player 33
    player_name "Right, you're quite flexible as I remember."
    show player 13
    show anna 2
    anna "Хорошо, давайте найдем коврик для йоги..."
    hide anna
    scene location_gym_yoga_front
    with fade
    show player 413 at left
    show anna 13
    with dissolve
    anna "Какую позицию мы должны практиковать?"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
