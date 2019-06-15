label science_minigame_success:
    scene expression game.timer.image("backgrounds/location_school_office4{}_closeup.jpg")
    show player 2 at Position(xpos=0.25, ypos=1.0)
    show okita 4 at Position(xpos=0.7, ypos=1.0)
    player_name "Кажется, у меня получилось!"
    show player 1
    show okita 5
    okita "Позволь мне посмтреть!"
    show okita 35 at Position(xpos=0.65, ypos=1.0) with dissolve

    okita "..."
    show okita 34
    okita "Выглядит правильно!"
    okita "О, это так захватывающе!"
    show player 2
    show okita 35
    player_name "Спасибо, Я-"

    show okita 36 at Position(xpos=0.7, ypos=1.0) with dissolve
    show player 23
    player_name "( !!! )" with hpunch
    show player 10
    player_name "Вау, вы выглядите... в порядке."
    show okita 37 at Position(xpos=0.65, ypos=1.0) with dissolve
    okita "Хммм!"
    show okita 38
    okita "Это на самом деле очень вкусно!"
    show player 10
    show okita 6 at Position(xpos=0.7, ypos=1.0) with dissolve
    player_name "... Это сделал я..."
    show player 11
    player_name "..."
    show player 10
    player_name "И это все? Мы закончили?"
    show player 11
    show okita 7
    okita "Почти!"
    okita "Осталось сделать еще кое-что."
    show okita 28 with dissolve
    player_name "..."
    show okita 29 at Position(xpos=0.65, ypos=1.0) with dissolve

    okita "Вам просто нужно убедиться, что {b}директриса Смит{/b} примет это."
    show player 10
    show okita 30
    player_name "Что?!"
    player_name "Как я должен это сделать?"
    show player 11
    show okita 29
    okita "Ты что-нибудь придумаешь..."
    show player 535 at Position(xpos=0.3, ypos=1.0)
    show okita 5 at Position(xpos=0.7, ypos=1.0) with dissolve
    with dissolve
    okita "Как и всегда."
    show player 534
    show okita 4
    player_name "Прекрасно..."
    show player 535
    show okita 3
    okita "Просто {b}подсунь это ей в еду или еще куда-нибудь{/b}."
    show player 10 at Position(xpos=0.25, ypos=1.0) with dissolve
    show okita 4
    player_name "Тогда я получу свою пятерку?"
    show player 11
    show okita 5
    okita "Хм, Мы это обсудим."

    hide okita with dissolve
    hide player
    show player 2f
    with dissolve
    player_name "Хорошо, я могу это сделать."

    $ player.remove_item("mushroom")
    $ player.remove_item("toad")
    $ player.remove_item("tissue")
    $ player.remove_item("chicken_stock")
    $ player.remove_item("caveflower")
    $ M_okita.trigger(T_okita_brewed_serum)
    $ game.timer.tick(2)
    $ player.go_to(L_map)
    $ game.main()
    return

label science_minigame_fail:
    scene expression game.timer.image("backgrounds/location_school_office4{}_closeup.jpg")
    show player 11 zorder 0 at left
    show playerl 1 zorder 1 at Position(xpos=0.152, ypos=1.0)
    show playerg 1 zorder 2 at Position(xpos=0.17, ypos=0.3475)
    show okita 11 at right
    okita "Нет, Нет, НЕТ!"
    okita "Как тебе всегда удается все испортить?!"
    show player 10
    show okita 11b
    player_name "Простите, я немного запуталась..."
    show player 11
    show okita 9
    okita "Ухх..."
    show okita 11
    okita "Ну, сегодня у нас нет времени начинать все сначала. Завтра тебе придется повторить попытку."
    show player 10
    show okita 11b
    player_name "Хорошо."
    player_name "Тогда увидимся завтра вечером."
    show player 11
    show okita 11
    okita "Постарайся не подвести меня в следующий раз!"
    $ game.timer.tick(2)
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
