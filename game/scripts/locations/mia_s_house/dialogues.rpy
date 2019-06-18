label mias_house_is_morning:
    scene miahouse
    show player 12 with dissolve
    player_name "( Здесь никого нет... )"
    show player 35
    player_name "( {b}Мия{/b}, наверное, уже ушла в {b}школу{/b}. )"
    hide player 35 with dissolve
    return

label mias_house_mia_concerning_visit:
    scene expression game.timer.image("miahouse{}")
    show harold 21 at right
    show player 10 at left
    with dissolve
    player_name "{b}Гарольд{/b}! А {b}Мия{/b}-"
    show player 11
    player_name "..."
    show harold 23
    harold "Здравствуй..."
    show harold 22
    show player 12
    player_name "Всё хорошо?"
    show player 11
    show harold 23
    harold "Бывало и лучше."
    show harold 22
    show player 10
    player_name "Куда ты?"
    show player 5
    show harold 23
    harold "Я...пока не знаю."
    show harold 22
    show player 10
    player_name "Что?"
    show player 12
    player_name "Ну, а что в коробке?"
    show player 11
    show harold 23
    harold "Я съезжаю, {b}[firstname]{/b}..."
    show harold 22
    show player 22
    player_name "!!!"
    show harold 23
    harold "...прости, что видишь нашу семью такой."
    show harold 21
    harold "До встречи, дружок."
    hide harold with dissolve
    show player 10
    player_name "Вот дела!"
    player_name "Нужно проведать {b}Мию{/b} и узнать, как она..."
    hide player with dissolve
    return

label mias_house_front_door_locked:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Мия{/b} наверняка спит... Лучше придти завтра. )"
    hide player 2 with dissolve
    hide miahouse_night
    return

label night_closed_mia:
    scene miahouse_night
    show player 2 with dissolve
    player_name "( {b}Мия{/b} наверняка спит... Лучше придти завтра. )"
    hide player 2 with dissolve
    $ game.main()

label mia_banned:
    scene expression game.timer.image("miahouse{}")
    show player 12 with dissolve
    player_name "Нужно дать {b}Мие{/b} и её семье время побыть одним..."
    hide player with dissolve
    $ game.main()

label closed_mia:
    scene expression game.timer.image("miahouse{}")
    show player 12 with dissolve
    if game.timer.is_morning() and not game.timer.is_weekend():
        player_name "( Никого нет... )"
        show player 35
        player_name "( {b}Мия{/b} наверное уже ушла в {b}школу{/b}. )"
    else:
        player_name "( {b}Мия{/b} на улице, Мне незачем туда идти. )"
    $ game.main()

label mia_mailbox_pizza_pamphlet:
    scene expression game.timer.image("mia_mailbox{}")
    player_name "( Это наверное реклама. )"
    show expression "objects/object_mailbox_item02_closeup.png" with dissolve
    player_name "( Пиццерия Тони. Давненько я там не был. )"
    player_name "( Лучше положить буклет на место. )"
    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label mia_mailbox_newspaper:
    scene expression game.timer.image("mia_mailbox{}")
    player_name "( Местная газета. Должно быть интересно... )"
    show expression "objects/object_newspaper.png" with dissolve
    player_name "( Вор всё ещё на свободе? Надеемся, что в скором времени его поймают. )"
    player_name "( Лучше положить её на место. )"
    hide expression "objects/object_newspaper.png" with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
