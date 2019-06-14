label spin_bottle_minigame_kiss_mc_roxxy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=3)
    show player car 2b zorder 1 at Position (xoffset=-3)
    show player_arms car 1 zorder 2 at Position (xoffset=-3)
    with dissolve
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show player_shadow front sitting 1 zorder 0
    show player_arms front sitting 3 at Position (xoffset=3-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    show roxxy_arm front sitting 1 at Position (xoffset=3)
    with dissolve
    rox "Ммм."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    show player front sitting 7 at Position (xoffset=-3)
    show roxxy front sitting 3b at Position (xoffset=3)
    if randomizer() < 33:
        missy "Они так мило смотрятся вместе ,правда {b}Бекка{/b}?"
        becca "..."
    elif randomizer() < 66:
        rox "Он лучше всех целуется..."
        missy "Я вся как желе."
        becca "..."
    else:
        becca "{b}Рокси{/b} отлично владеет языком..."
        missy "Да, но {b}[firstname]{/b} тоже!"
        becca "..."
    show player front sitting 7b at Position (xoffset=-3)
    show roxxy front sitting 3 at Position (xoffset=3)
    pause
    hide player
    hide roxxy
    hide roxxy_arm
    hide player_arms
    hide player_shadow
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_becca:
    if randomizer() > 50:
        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player front sitting 7b
        show player_shadow front sitting 1 zorder 0
        show player_arms front sitting 3
        show becca front sitting 3
        with dissolve
        becca "Ммм."
        player_name "..."
        show player front sitting 7
        show becca front sitting 3b
        pause
        show player front sitting 7b
        show becca front sitting 3
        if randomizer() < 33:
            rox "Да, вот так..."
            rox "Поиграй с ее сосками!"
            missy "Хе-хе, посмотри, как она возбуждена!"
        elif randomizer() < 66:
            missy "Мне жаль, что тебе приходится целовать эту уродливую веснушчатую рыжую девку, {b}[firstname]{/b}..."
            rox "Заткнись, {b}Мисси{/b}..."
        else:
            rox "Это действительно круто!"
        show player front sitting 7
        show becca front sitting 3b
        if randomizer() < 50:
            rox "Давай {b}Бекка{/b}, используй больше языка!"
            becca "..."
        else:
            missy "Блее, {b}Бекка{/b} скучно целуется."
            missy "Подожди, сейчас моя очередь, {b}[firstname]{/b}!"
        show player front sitting 7b
        show becca front sitting 3
    else:

        scene expression "backgrounds/location_beach_fire_kiss.jpg"
        show becca front sitting 1
        show player car 2b zorder 1
        show player_arms car 1 zorder 2
        with dissolve
        pause
        show player_shadow front sitting 1 zorder 0
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
        with dissolve
        if randomizer() < 33:
            becca "Ггхххх!"
        else:
            becca "Ммм."
            player_name "..."
        show player front sitting 7b
        show player_arms front sitting 4d
        show becca front sitting 3
        pause
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
        if randomizer() < 33:
            rox "Да, вот так..."
            rox "Поиграй с ее сосками!"
            missy "Хе-хе, посмотри, как она возбуждена!"
        elif randomizer() < 66:
            missy "Мне жаль, что тебе приходится целовать эту уродливую веснушчатую рыжую девку, {b}[firstname]{/b}..."
            rox "Заткнись, {b}Мисси{/b}..."
        else:
            rox "Это действительно круто!"
        show player front sitting 7b
        show player_arms front sitting 4d
        show becca front sitting 3
        if randomizer() < 50:
            rox "Давай {b}Бекка{/b}, используй больше языка!"
            becca "..."
        else:
            missy "Блее, {b}Бекка{/b} скучно целуется."
            missy "Подожди, сейчас моя очередь, {b}[firstname]{/b}!"
        show player front sitting 7
        show player_arms front sitting 4
        show becca front sitting 3b
    pause
    hide player
    hide player_arms
    hide player_shadow
    hide becca
    with dissolve
    return

label spin_bottle_minigame_kiss_mc_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show missy front sitting 1
    show player car 2b zorder 1 at Position (xoffset=-7)
    show player_arms car 1 zorder 2 at Position (xoffset=-7)
    pause
    show player_shadow front sitting 1 zorder 0
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    show missy_arm front sitting 1 zorder 3
    missy "Ммм."
    player_name "..."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    show player front sitting 7 at Position (xoffset=-7)
    show player_arms front sitting 4 at Position (xoffset=-7)
    show missy front sitting 3b
    if randomizer() < 33:
        rox "Да, потискай сиськи, {b}[firstname]{/b}!"
        becca "Там едва ли что-то есть, что можно помять..."
        rox "Заткнись, {b}Бекка{/b}."
    if randomizer() < 66:
        becca "Боже, как она небрежно целуется!"
        becca "Что, черт возьми, она пытается сделать со своим языком?!"
        rox "Я знаю, правильно?"
        rox "Кто-то должен научить эту девушку французскому..."
    else:
        rox "Притормози, {b}Мисси{/b}!"
        rox "Она чертовски нетерпелива..."
        becca "Да, я думаю, ей просто нужно потрахаться."
    show player front sitting 7b at Position (xoffset=-7)
    show player_arms front sitting 4c
    show missy front sitting 3
    pause
    hide player
    hide player_shadow
    hide player_arms
    hide missy
    hide missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_becca_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show becca front sitting 1f at Position (xoffset=-4)
    show missy front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    show missy_arm front sitting 1 at Position (xoffset=4)
    with dissolve
    pause
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    if randomizer() < 33:
        rox "Разве это не жарко, {b}[firstname]{/b}?"
        player_name "Д-Да..."
    if randomizer() < 66:
        rox "Ммм, давай {b}Мисси{/b}..."
        rox "Ты должна быть напористой с {b}Беккой{/b}!"
        rox "Она любит грубое обращение!"
    else:
        becca "Ммм."
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 33:
        rox "{b}Бекка{/b} делает вид, что ей это не нравится, но посмотрите, как сильно возбудились ее соски!"
        player_name "..."
    if randomizer() < 66:
        player_name "..."
    else:
        rox "О, это звучит так, как будто {b}Мисси{/b} начинает привыкать!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    pause
    show becca front sitting 3bf at Position (xoffset=-4)
    show missy front sitting 3 at Position (xoffset=4)
    if randomizer() < 50:
        player_name "..."
        rox "Это делает тебя твердым, {b}[firstname]{/b}?"
        player_name "Д-Да..."
        rox "Хехехе!"
    show becca front sitting 3f at Position (xoffset=-4)
    show missy front sitting 3b at Position (xoffset=4)
    pause
    hide missy
    hide becca
    hide missy_arm
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_becca:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=5)
    show becca front sitting 1f
    with dissolve
    pause
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    if randomizer() < 33:
        becca "Гггхххх..."
    if randomizer() < 66:
        missy "Хехе, я люблю смотреть, как {b}Рокси{/b} справляется с {b}Беккой{/b}..."
        missy "Потому что обычно она такая заносчивая сука, понимаешь?"
        player_name "Ага."
        missy "... Но посмотри на нее сейчас."
        missy "Стонет, как маленькая шлюшка."
        player_name "..."
    else:
        becca "Ммм."
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    if randomizer() < 50:
        missy "Чёрт!"
        missy "Посмотри как {b}Бекка{/b} извиваеся!"
    else:
        missy "Разве {b}Рокси{/b} не вкусная, {b}Бекка{/b}?"
        becca "Мммммммм..."
        missy "Хехе."
    show roxxy front sitting 3 at Position (xoffset=5)
    show roxxy_arm front sitting 2d
    show becca front sitting 3bf
    if randomizer() < 50:
        player_name "..."
        missy "{b}Рокси{/b} действительно знает, как нажимать на ее кнопки."
    show roxxy front sitting 3b at Position (xoffset=5)
    show roxxy_arm front sitting 2c
    show becca front sitting 3f
    pause
    hide roxxy
    hide roxxy_arm
    hide becca
    with dissolve
    return

label spin_bottle_minigame_kiss_roxxy_missy:
    scene expression "backgrounds/location_beach_fire_kiss.jpg"
    show roxxy front sitting 1 at Position (xoffset=2)
    show missy front sitting 1f at Position (xoffset=-2)
    with dissolve
    pause
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    show missy_arm front sitting 1f at Position (xoffset=-2)
    show roxxy_arm front sitting 1 at Position (xoffset=2)
    with dissolve
    if randomizer() < 50:
        missy "Ггхххх!!!"
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Да, ущипни эту шлюшку за соски!"
        becca "Хахаха!"
    else:
        becca "Ммм, этот {b}Goldschwagger{/b} такой вкусный!"
        becca "Ты уверен, что не хочешь, {b}[firstname]{/b}?"
        player_name "Хех, Неа, все в порядке."
        player_name "Только пивка."
        becca "Буууу!!"
    show roxxy front sitting 3b at Position (xoffset=2)
    show missy front sitting 3f at Position (xoffset=-2)
    if randomizer() < 50:
        becca "Ухх, Посмотри на технику {b}Мисси{/b}..."
        becca "... такая небрежная."
        player_name "Может, вам двоим попрактиковаться в течение недели?"
        becca "Мы тренируемся вместе все время, она просто не-"
        becca "!!!"
        becca "Я имею в виду..."
        becca "Мы не..."
        becca "Это просто по пьянке, {b}[firstname]{/b}!"
        player_name "Хех, хорошо."
    show roxxy front sitting 3 at Position (xoffset=2)
    show missy front sitting 3bf at Position (xoffset=-2)
    pause
    hide missy
    hide missy_arm
    hide roxxy_arm
    hide roxxy
    with dissolve
    return

label spin_bottle_minigame_last_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Ммм..."
    show roxxy sitting 3
    rox "Хорошо, последний поворот."
    return

label spin_bottle_minigame_final_spin:
    scene expression "backgrounds/location_beach_fire_dialogue.jpg"
    show roxxy sitting 2 zorder 1 at right
    show becca sitting 1 at Position (xpos=300)
    show player_sitting 3 zorder 0 at Position (xpos=650)
    show missy sitting 1 at left
    show xtra 47 zorder 2 at Position (xpos=400)
    with dissolve
    rox "Ммм..."
    show roxxy sitting 3
    rox "Хорошо, последний поворот."
    rox "Победитель идет в раздевалку с {b}[firstname]{/b}!"
    show roxxy sitting 2
    show becca sitting 2
    show missy sitting 2
    show player_sitting 3b
    pause
    show player_sitting 3
    pause
    show player_sitting 5
    pause
    show player_sitting 11
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
