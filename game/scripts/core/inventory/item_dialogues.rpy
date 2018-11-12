label obituary_records(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Хмм..."
    player_name "Похоже, единственное имя, связанное с лодочником это..."
    player_name "...Бен Довер?"
    player_name "Теперь мне просто нужно посетить кладбище и найти его надгробный камень."
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label keycode_note_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Это {b}код от замка офиса Мисс Окита{/b}. {b}6219{/b}."
    return


label scroll(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Хмм..."
    player_name "На нем странный рисунок."
    player_name "Похож на полумесяц..."
    player_name "{b}Он должно быть пригодится для чего-то...{/b}"
    return

label treasure_map(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Это круто! Настоящая карта сокровищ!"
    player_name "Хмм..."
    player_name "Похоже на рисунок {b}побережья...{/b}"
    player_name "...И это похоже на наш местный пляж?!"
    player_name "... и здесь, на {b}маленьком острове{/b} есть крестик..."
    player_name "Интересно, что там?"
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label weird_coin(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Хух?"
    player_name "Похоже на очень старую монету."
    player_name "Просто посмотрите на эти нечетные {b}символы{/b}!"
    player_name "Мне следует оставить ее себе. Может, она чего-то стоит?"
    return

label old_book(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Эта книга выглядит так, будто была бы полезна что-то расшифровать."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Хех. Может быть {b}скрытое пиратское сокровище{/b} кто-то небрежно бросил."
        player_name "Но это {b}только мечты{/b}."
    else:
        player_name "Я думаю, что на {b}монете пирата{/b} было четыре цифры."
        player_name "Я должен взглянуть на нее еще раз."
    return

label golden_compass(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Вау!!"
    player_name "Я не могу в это поверить! Я нашел сокровище!."
    player_name "Это должно быть компас, о котором говорил Терри."
    return

label tigger(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Уфф, Этот подлый ублюдок неплохо сопротивлялся."
    player_name "... и только посмотрите на эти зубы!"
    player_name "Неудивительно, что Терри хотел его смерти."
    player_name "Не могу дождаться, чтобы показать ему!"
    return


label condom:
    scene expression game.timer.image("jennybedroom{}")
    show expression "objects/closeup_condom.png" with dissolve
    player_name "{b}Презерватив{/b}?!"
    player_name "{b}[jen_name]{/b} должно быть, прячет их в своей комнате..."
    player_name "Она, наверное, не заметит, если я возьму один..."
    hide expression "objects/closeup_condom.png" with dissolve
    show expression "boxes/popup_condom.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_condom.png" with dissolve
    $ game.main()

label attic_key:
    $ suffix = ""
    if (M_mom.get_state() == S_mom_diane_visit and game.timer.is_evening()) or (M_mom.get_state() == S_mom_diane_dinner and game.timer.is_evening()):
        $ suffix = "_evening"
    elif game.timer.is_dark():
        $ suffix = "_night"
    scene expression "home_entrance{}".format(suffix)
    show expression "objects/closeup_key.png" with dissolve
    player_name "( Я никогда не видел этот ключ раньше. )"
    player_name "( Он довольно маленький... )"
    hide expression "objects/closeup_key.png" with dissolve
    show expression "boxes/popup_key.png" at truecenter with dissolve
    $ renpy.pause()
    $ player.get_item("attic_key")
    hide expression "boxes/popup_key.png" with dissolve
    jump home_entrance

label ring:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( Это похоже на дорогое кольцо! )"
    player_name "( Что оно там делало? )"
    hide expression "objects/closeup_ring.png" with dissolve
    show expression "boxes/popup_ring.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_ring.png" with dissolve
    jump attic_dialogue

label cheerleader_outfit:
    scene expression game.timer.image("attic{}")




    show expression "boxes/popup_item_outfit1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_outfit1.png" with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "Это старая {b}папина{/b} {b}удочка{/b}!!"
    player_name "( Я помню, когда я был маленьким, мы ходили с ней рыбачить на {b}пирс{/b}. )"
    player_name "{b}*вздыхая*{/b}"
    player_name "Я скучаю по тебе {b}Папа{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    show expression "boxes/popup_item_rod1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_rod1.png" with dissolve
    if L_pier.locked:
        $ L_pier.unlock()
    jump attic_dialogue

label backpack_pickup_dialogue:
    scene location_park_day_blur
    show player 608
    with dissolve
    pause
    show player 608b
    player_name "Это определенно рюкзак {b}Евы{/b}."
    player_name "Хмм, Я не вижу ее {b}блокнота для рисования{/b}."
    show player 610 with dissolve
    player_name "Я должен {b}спросить ее об этом, когда я верну рюкзак{/b}."
    show expression "boxes/popup_item_backpack1.png" at truecenter with dissolve
    pause
    hide expression "boxes/popup_item_backpack1.png"
    $ player.get_item("eve_backpack")
    jump park_dialogue

label roxxy_homework_pickup_dialogue:
    scene mc_locker
    player_name "Ах, вот она!"
    player_name "Теперь мне просто нужно {b}отнести ее Рокси.{/b}."
    show expression 'boxes/popup_item_homework5.png' at truecenter with dissolve
    pause
    hide expression 'boxes/popup_item_homework5.png'
    $ player.get_item("roxxy_homework")
    $ player.go_to(L_school_hall)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
