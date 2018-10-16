label map_june_mc_help_started:
    scene outside_school_b
    show player 10 with dissolve
    player_name "Наверное, мне стоит сказать {b}Эрику{/b}, что с {b}Джун{/b} у него ничего не выйдет..."
    player_name "... и что я буду проводить с ней время."
    player_name "Он будет очень расстроен."
    hide player with dissolve
    return

label map_june_erik_help_started:
    scene outside_school_b
    show player 17 with dissolve
    player_name "Я должна сообщить {b}Эрику{/b} хорошие новости!"
    player_name "Он будет в восторге от этого!"
    show player 14
    player_name "{b}Джун{/b} кажется идеальной девушкой для него!"
    hide player with dissolve
    return

label map_erik_intro_in_progress:
    scene expression game.timer.image("outside_school{}")
    show erik 4 at right with dissolve
    eri "Привет, {b}[firstname]{/b}!"
    show player 10 at left with dissolve
    show erik 1
    player_name "О... Привет..."
    show erik 4
    eri "Как прошел твой первый день в школе?"
    show player 37
    show erik 1
    player_name "Тьфу... Я даже не хочу об этом говорить."
    show erik 5
    eri "Ясно..."
    show player 5
    eri "Чем ты сейчас займешься?"
    show erik 1
    show player 26
    player_name "Ну, Я бещал {b}[deb_name]{/b} что схожу к ее подруге {b}Диане{/b}."
    player_name "Она обещала {b}платить{/b} мне деньги за некоторую {b}работу{/b}."
    show erik 3
    show player 13
    eri "Чувак... Жаль у меня нет работы..."
    show erik 4
    eri "Работы, где я мог бы просто сидеть за компьютером и играть в игры весь день..."
    show erik 1
    show player 14
    player_name "О! Блин компьтер... Кажется, мой {b}сломалась{/b}?"
    show player 35
    player_name "Я думаю, что мне нужно заменить некоторые части в нем, или что-то..."
    show player 12
    player_name "Ты знаешь какие-нибудь хорошие магазины, где я мог бы их купить?"
    show erik 4
    show player 1
    eri "Хммм... Я хожу в {b}CONSUM-R{/b} в {b}торговом центре{/b}."
    eri "Они продают много вещей по разумной цене."
    show erik 1
    show player 14
    player_name "Хорошо, пойду проверю!"
    show erik 7
    show player 36
    eri "Увидемся позже!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
