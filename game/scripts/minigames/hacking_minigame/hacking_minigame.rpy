label hacking_minigame_pre:
    if game.timer.is_day():
        show screen sis_computer
        player_name "( Я не могу этого сделать, когда {b}[jen_name]{/b} может прийти в любую минуту! )"
        pause
        call screen sis_computer
    elif not M_jenny.get("hacked pc"):
        show screen hacking_minigame_pre
        player_name "( Да, это то, что я ищу, прямо здесь! )"
        player_name "( Теперь мне просто нужно немного поработать над магией... )"
        hide screen hacking_minigame_pre
        jump hacking_minigame_call
    elif M_player.get("on_jenny_pc"):
        show screen hacking_minigame_win
        pause
        player_name "( Я уже подключил свой {b}компьютер{/b} к ее. Мне не нужно делать это снова. )"
        pause
        hide screen hacking_minigame_win
        call screen sis_computer
    else:
        show screen sis_computer
        player_name "( Я не понимаю, почему я пытаюсь подключить свой компьютер с моего компьютера... )"
        call screen sis_computer

label hacking_minigame_call:
    call screen hacking_minigame

label hacking_minigame_win:
    show screen hacking_minigame_win
    pause
    hide screen hacking_minigame_win
    scene expression player.location.background_closeup with None
    show player 17
    player_name "( Я думаю, что я сделал это! )"
    player_name "( Теперь я смогу просмотреть ее профиль {b}CAMslut{/b} на своем компьютере. )"
    show player 403
    player_name "( Я не могу дождаться, чтобы посмотреть эти видео! )"
    hide player with dissolve
    $ M_jenny.set("hacked pc", True)
    $ game.main()

label hacking_minigame_fail:
    show screen hacking_minigame_fail
    pause
    hide screen hacking_minigame_fail
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( Что... Он не пускает меня! )"
    player_name "( У меня почти получилось. )"
    jen "{b}*фырк*{/b}"
    show player 22
    player_name "( Вот дерьмо! )"
    jen "Это тебе обойдется... {b}*зевок*{/b} четыре сотни... ззззз... )"
    player_name "( Она шевелится! )"
    pause
    player_name "( Я должен валить отсюда! )"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 37 with dissolve
    player_name "( Фу, это было близко! )"
    player_name "( Я просто попробую еще раз {b}завтра вечером{/b}... )"
    player_name "[int_warn]( Если бы я только знал, как обращаться с {b}компьютерами{/b} ... )"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
