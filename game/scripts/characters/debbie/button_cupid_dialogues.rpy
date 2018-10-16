label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    deb "Ты что-то нашел, дорогуша?"
    show player 10
    show debbie 164
    player_name "Я все еще продолжаю."
    show player 5
    show debbie 166
    deb "Хехе, хорошо!"
    show debbie 165
    deb "Не смотри так серьезно. Это просто! Просто найди что-нибудь, что бы мне понравилось..."
    show debbie 164
    pause
    hide debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Что-то что понравится {b}[deb_name]{/b}? )"
    player_name "( Может, ожерелье? )"
    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Хорошо, {b}[deb_name]{/b}. Как насчет этого?"
    hide xtra
    show player 1 with dissolve
    show debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show debbie 172
    deb "Ооо, {b}[firstname]{/b}... Это прекрасное {b}ожерелье{/b}."
    show debbie 170
    show player 14
    player_name "Тебе правда нравится?"
    show player 13
    show debbie 171
    deb "Да! У тебя прекрасный вкус, милый."
    show debbie 170
    show player 14
    player_name "Хух, спасибо {b}[deb_name]{/b}!"
    show player 13
    show debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show debbie 175
    pause 2
    show debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show debbie 165
    deb "Ну?"
    show player 14
    show debbie 164
    player_name "... Хмм?"
    show player 13
    show debbie 166
    deb "Как я выгляжу?"
    show player 14
    show debbie 164
    player_name "Ты выглядишь прекрасно, {b}[deb_name]{/b}!"
    show player 13
    show debbie 166
    deb "Ааа... Спасибо, любимый."
    show debbie 164
    deb "Хмм..."
    show debbie 165
    deb "Где это зеркало, когда оно нужно?"
    show debbie 164
    player_name "..."
    show player 14
    player_name "Наверное, в примерочной есть..."
    show player 13
    show debbie 165
    deb "Молодец, милый!"
    deb "Я сейчас вернусь."
    hide debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Хорошо."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
