label erik_dialogue_intro:
    scene location_school_computer_day_blur
    show player 2 at left
    show erik 1 at right
    with dissolve
    return

label erik_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Я помогаю Оките с проектом.."
    show player 1
    show erik 4
    eri "Реально?Круто!"
    eri "Что это за проект такой?"
    show player 2
    show erik 1
    player_name "Эмм,Не думаю, что я должен говорить..."
    show player 1
    show erik 4
    eri "Ох, сверхсекретное исследование?"
    eri "Круто, я могу помочь?"
    show player 2
    show erik 1
    player_name "Вообще-то да,!"
    player_name "Мне нужно найти пару толстых {b}Линз{/b}."
    player_name "У тебя случайно нет запасного комплекта очков, не так ли?"
    show player 1
    show erik 4
    eri "ты шутишь?"
    eri "Ты знаешь, сколько раз {b}Dexter{/b} разбил эту пару?"
    eri "Я всегда держу запасной комплект рядом."
    show player 2
    show erik 1
    player_name "Замечательно!!"
    player_name "Вы позволишь мне их взять?"
    show player 1
    show erik 4
    eri "Конечно!"
    show player 2
    show erik 1
    player_name "Спасибо, мужик!"
    show player 1
    show erik 4
    eri "Без проблем, {b}[firstname]{/b}! Для чего нужны друзья?"
    show player 10
    show erik 1
    player_name "... Ох, подожди!"
    show player 29 with dissolve
    player_name "Я забыл, они должны быть {b}Варифокальные линзы{/b}..."
    show player 3
    show erik 5
    eri "Вари- что?"
    show player 10 with dissolve
    show erik 1
    player_name "Ты дальнозоркий или близорукий?"
    show player 11
    show erik 5
    eri "Близорукий. Почему?"
    show player 10
    show erik 1
    player_name "Черт! Мне нужны линзы от кого-то, кто оба."
    show player 11
    show erik 5
    eri "Ох."
    show player 24
    show erik 1
    player_name "*вздох*"
    show player 10
    player_name "Думаю, мне придется продолжать поиски."
    show player 11
    show erik 5
    eri "Извини, {b}[firstname]{/b}."
    show player 2
    show erik 1
    player_name "Все в порядке, {b}Erik{/b}.Все равно Спасибо."
    show player 1
    show erik 4
    eri "В любое время, мужик."
    return

label erik_dialogue_leave:
    show player 14
    player_name "Ох, ничего!"
    player_name "Просто сказать привет."
    show player 1
    show erik 4
    june "Ах,хорошо тогда..."
    show erik 1
    show player 29 at Position(xoffset=8)
    player_name "Эээ... Увидимся позже!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
