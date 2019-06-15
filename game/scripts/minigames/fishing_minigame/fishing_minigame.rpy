label fishing_night:
    scene expression game.timer.image("pier{}")
    show player 4 at left with dissolve
    player_name "( Слишком поздно идти на рыбалку. )"
    $ game.main()

label no_fish_rod:
    scene expression game.timer.image("pier{}")
    show player 2 with dissolve
    player_name "( Хм... Мне понадобится {b}удочка{/b}, прежде чем я смогу ловить рыбу... )"
    $ game.main()

label before_fishing:
    scene location_pier_minigame06b
    if M_aqua.get_state() == S_aqua_chase:
        menu:
            "Поговорите с девушкой-монстром.":
                show player 474 at Position(xpos=0.715,ypos=.9425)
                player_name "Эй! Аква!"
                show player 475
                pause
                show player 474
                player_name "Я знаю, что ты меня слышишь!"

                show player 475
                show aqua 17b at Position (xpos=0.4175,ypos=1.0) with dissolve
                pause
                show aqua 18b
                aqua "Что ты хочешь на этот раз?"
                show player 474
                show aqua 17b
                player_name "Не прикидывайся идиоткой! Ты знаешь что я хочу вернуть свою приманку!"
                show player 475
                show aqua 18b
                aqua "Блестяшкууу?"
                show player 474
                show aqua 17b
                player_name "Да. Блестяшку. Отдай!"
                show player 475
                show aqua 18b
                aqua "Нет! Ты просто используешь его, чтобы красть рыбок!"
                aqua "Я держу его в безопасности."
                show player 474
                show aqua 17b
                player_name "Грр..."
                show player 475
                show aqua 18b
                aqua "Хочешь Блестяшку - приходи!!!"
                hide aqua with dissolve
                show player 476
                player_name "Блестяшка!"
                player_name "..."
                jump follow_aqua
            "Рыба.":

                $ pass

    if player.has_item("worm") or player.has_item("lure01") or player.has_item("special_lure"):
        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( Терри сказал что-то о правильной приманке для правильной рыбы... )"
        call screen bait_menu

        show player 235 at Position(xpos=0.6062,ypos=0.9455)
        player_name "( Надеюсь, я поймаю что-нибудь хорошее с этой... )"
        show player 236 at Position(xpos=0.4956,ypos=0.9455)
        player_name "..."

        call screen fishing_minigame(bait)
    else:

        show player 234 at Position(xpos=0.6635,ypos=0.9289) with dissolve
        player_name "( Я не могу рыбачить без наживки.. )"
        player_name "( Я должен осмотреть город и посмотреть, что смогу найти. )"
    $ game.main()

label after_fishing(fish_name, chosen_bait):
    scene location_pier_minigame06b
    if fish_name != None:
        play audio randomizer("audio/sfx_reel{}.ogg", 1, 2)
        show player 237 at Position(xpos=0.7173,ypos=0.9455)
        if fish_name == "Seatrout":
            show xtra 4 at Position(xpos=0.5786,ypos=0.4810)
            $ player.get_item("seatrout")
        elif fish_name == "Snapper":
            show xtra 5 at Position(xpos=0.5786,ypos=0.4810)
            $ player.get_item("snapper")
        elif fish_name == "Mackerel":
            show xtra 6 at Position(xpos=0.5786,ypos=0.4810)
            $ player.get_item("mackerel")
        elif fish_name == "Tiger Fish":
            show xtra 29 at Position(xpos=0.56,ypos=0.52)
            player_name "Этот подлый ублюдок устроил настоящую драку.."
            player_name "... и только посмотрите на эти зубы!"
            player_name "Неудивительно, почему Терри хотел его смерти."
            player_name "Не могу дождаться, чтобы показать ему!"
            $ player.get_item("tigger")

        if fish_name != "Tiger Fish":
            player_name "( Да! Я поймал {b}[fish_name]{/b}! )"
        $ fish_caught_count += 1
        $ first_fish = True
    else:
        show player 238 at Position(xpos=0.7173,ypos=0.9455)
        if chosen_bait == "worms":
            show xtra 7 at Position(xpos=0.5786,ypos=0.4479)
        elif chosen_bait == "standard lure":
            show xtra 8 at Position(xpos=0.5796,ypos=0.4645)
        elif chosen_bait == "fancy lure":
            show xtra 9 at Position(xpos=0.5796,ypos=0.4479)
        elif chosen_bait == "golden lure":
            show xtra 10 at Position(xpos=0.5796,ypos=0.4479)
        player_name "!!!" with hpunch
        player_name "( Я ничего не поймал! )"
        player_name "( Возможно, мне нужно лучше {b}прицелиться{/b} или использовать правильную {b}приманку{/b}... )"
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
