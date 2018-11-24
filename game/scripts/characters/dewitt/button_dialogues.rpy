label dewitt_dialogue_dewitt_eve_meet_up:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Я должен дать ей немного пространства на время."
    player_name "И я должен встретится с {b}Евой{/b} в {b}парке ночью{/b}."
    return

label dewitt_dialogue_dewitt_science_adhesive:
    scene music_classroom_c
    show player 17 with dissolve
    player_name "{b}Кевин{/b} собирался сделать клей в классе {b}Мисс Окиты{/b}."
    player_name "Я должен увидеть, что у него получится."
    return

label dewitt_dialogue_dewitt_school_sneak_mission_help:
    scene music_classroom_c
    show player 10 with dissolve
    player_name "Может быть, {b}Эрик{/b} поможет мне {b}пробраться в школу ночью{/b}."
    return

label dewitt_dialogue_dewitt_office_night_visit_delay:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Запомни, у меня есть еще один сюрприз для тебя."
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Тебе придется прийти ко мне в офис {b}завтра{/b} после школы, если хочешь..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "Хо-хорошо..."
    player_name "Я буду там."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Ммм, я не могу дождаться!"
    dewitt "Увидимся, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_office_night_visit:
    scene music_classroom_c
    show player 13 at left
    show dewitt 19f at right
    with dissolve
    dewitt "Запомни, у меня есть ещё один сюрприз для тебя."
    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Приходи ко мне в офис после школы, если хочешь..."
    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "Хо-хорошо..."
    player_name "Я буду там."
    show player 13 with dissolve
    show dewitt 19f
    dewitt "Ммм, я не могу дождаться!"
    dewitt "Увидимся, {b}[firstname]{/b}."
    hide dewitt with dissolve
    show player 18
    player_name "..."
    return

label dewitt_dialogue_dewitt_end:
    scene music_classroom_c
    show player 13f at right
    show dewitt 2 at left
    with dissolve
    dewitt "Ещё раз спасибо за все, сахарок!"
    show dewitt 1
    show player 14f
    player_name "С удовольствием, {b}Мисс Девитт{/b}."
    show player 13f
    show dewitt 19 with dissolve
    dewitt "Помни, моя дверь всегда открыта для тебя."
    show dewitt 18
    show player 17f
    player_name "Да, мэм."
    return

label dewitt_dialogue_intro:
    scene music_classroom_c
    show dewitt 1 at left
    show player 2f at right
    player_name "Привет, {b}Мисс Девитт{/b}."
    show dewitt 2
    show player 1f
    dewitt "Привет, {b}[firstname]{/b}!"
    dewitt "Готов кайфовать сегодня с нами?"
    show dewitt 1
    show player 33f
    player_name "Конечно!"
    show dewitt 2
    show player 13f
    dewitt "Ты хочешь о чем-нибудь поговорить?"
    show dewitt 1
    show player 34f
    return

label dewitt_dialogue_dewitt_find_flute:
    show player 10f
    player_name "Где я должен начать искать флейту?"
    show player 5f
    show dewitt 2
    dewitt "Ты {b}проверил лист наладки инструментов в шкафчике класса{/b}?"
    show dewitt 1
    show player 14f
    player_name "Ох, да!"
    player_name "Я поищу там подсказку!"
    show player 13f
    show dewitt 2
    dewitt "Пока, сахарок!"
    return

label dewitt_dialogue_dewitt_make_new_flute:
    show player 10f
    player_name "О флейте-"
    show player 11f
    show dewitt 2
    dewitt "Ты уже нашел флейту?"
    show dewitt 1
    show player 3f at Position (xoffset=-8) with dissolve
    player_name "..."
    show player 10f with dissolve
    player_name "Нет еще."
    show player 5f
    show dewitt 2
    dewitt "Надеюсь, она не потерялась."
    show dewitt 1
    show player 14f
    player_name "Не волнуйтесь! Я в деле!"
    show player 13f
    show dewitt 2
    dewitt "Спасибо, {b}[firstname]{/b}!"
    hide dewitt with dissolve
    show player 4f with dissolve
    player_name "( {b}Эрик{/b}  сказал, что я смогу сам её сделать. )"
    return

label dewitt_dialogue_talent_show_help:
    show player 10f
    player_name "Сколько людей нужно для шоу талантов?"
    show player 5f
    show dewitt 5
    dewitt "Я надеялась, что по крайней мере, {b}ещё два{/b}."
    dewitt "Если меньше, я боюсь, нам придется все отменить."
    show dewitt 4
    show player 14f
    player_name "Хорошо, не волнуйтесь, {b}Мисс Девитт{/b}! Я найду кого-нибудь!"
    show player 13f
    show dewitt 5
    dewitt "Ах спасибо, сахарок!"
    return

label dewitt_dialogue_leave:
    show player 10f
    player_name "Не совсем ..."
    player_name "Просто надеюсь, что смогу наверстать упущенное."
    show dewitt 2
    show player 5f
    dewitt "Ох, сладкий. С тобой все будет в порядке!"
    show player 13f
    dewitt "Выбери инструмент и присаживайся!"
    dewitt "Мы вернем тебя в прежнее русло..."
    show dewitt 1
    show player 14f
    player_name "Спасибо, {b}Мисс Девитт{/b}..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
