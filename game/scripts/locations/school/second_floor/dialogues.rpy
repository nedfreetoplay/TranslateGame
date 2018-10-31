label second_floor_first_visit:
    scene stairs
    show player 4 with dissolve
    player_name "Хммм..."
    player_name "(Не так много людей собираются в кафетерии. )"
    show player 12
    player_name "( Сейчас не обеденный перерыв. )"
    hide player with dissolve
    return

label second_floor_okita_dose_smith:
    scene expression game.timer.image("backgrounds/location_school_second{}_blur.jpg")
    show player 35
    player_name "Хмм, Я думаю {b}Директриса Смит{/b} пошла в {b}Учительскую{/b} чтобы {b}попить кофе{/b} в дневное время."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
