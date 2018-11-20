label park_bushes_erik_father_treasure_started:
    scene expression game.timer.image("park_bushes{}_b")
    show player 4 with dissolve
    player_name "Хмм..."
    show player 12 with dissolve
    player_name "( Выгядит так как буд-то здесь есть тайник. )"
    show player 14
    player_name "( Может {b}отец Эрика{/b} говорил правду. )"
    player_name "( Надо осмотреться. )"
    hide player with dissolve
    return

label park_bushes_mia_stolen_goods:
    scene expression game.timer.image("park_bushes{}_b")
    show player 4 with dissolve
    player_name "Хмм..."
    show player 12 with dissolve
    player_name "( Отличное место чтобы что-то скрыть. )"
    show player 14
    player_name "( Надо осмотреться. )"
    hide player with dissolve
    return

label park_bushes_bag_mia_stolen_goods:
    player_name "Вауу!"
    player_name "( Тут так много вещей! )"
    player_name "( Похоже что какой-то вор прячет сюда ворованные вещи. )"
    player_name "( Должно быть он долгое время собирал эти вещи. )"
    player_name "Хмм..."
    player_name "( Какой-то странный ключ... )"
    return

label park_bushes_bag_erik_father_treasure_started:
    player_name "Вау!"
    player_name "( Здесь столько всего! )"
    player_name "( Должно быть {b}отец Эрика{/b} долгое время собирал эти вещи. )"
    player_name "Хмм..."
    player_name "( Какой-то странный ключ... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
