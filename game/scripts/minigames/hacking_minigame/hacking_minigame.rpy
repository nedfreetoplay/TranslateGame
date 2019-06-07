label hacking_minigame_pre:
    if game.timer.is_day():
        show screen sis_computer
        player_name "( I can't do that when {b}[jen_name]{/b} can come in any minute! )"
        pause
        call screen sis_computer
    elif not M_jenny.get("hacked pc"):
        show screen hacking_minigame_pre
        player_name "( Yeah, this is what I'm looking for, right here! )"
        player_name "( Now I just need to work a little magic... )"
        hide screen hacking_minigame_pre
        jump hacking_minigame_call
    elif M_player.get("on_jenny_pc"):
        show screen hacking_minigame_win
        pause
        player_name "( I already connected my {b}computer{/b} to hers. I don't need to do it again )"
        pause
        hide screen hacking_minigame_win
        call screen sis_computer
    else:
        show screen sis_computer
        player_name "( I don't see why I'd try to connect my computer from my computer... )"
        call screen sis_computer

label hacking_minigame_call:
    call screen hacking_minigame

label hacking_minigame_win:
    show screen hacking_minigame_win
    pause
    hide screen hacking_minigame_win
    scene expression player.location.background_closeup with None
    show player 17
    player_name "( I think I did it! )"
    player_name "( Now I should be able to view her {b}CAMslut{/b} profile on my computer. )"
    show player 403
    player_name "( I can't wait to check out those videos! )"
    hide player with dissolve
    $ M_jenny.set("hacked pc", True)
    $ game.main()

label hacking_minigame_fail:
    show screen hacking_minigame_fail
    pause
    hide screen hacking_minigame_fail
    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( What the... It locked me out! )"
    player_name "( I almost had it too. )"
    jen "{b}*Snort*{/b}"
    show player 22
    player_name "( Oh, crap! )"
    jen "Mmm, that'll cost you... {b}*Yawn*{/b} four-hundred... Zzz... )"
    player_name "( She's stirring! )"
    pause
    player_name "( I gotta get out of here! )"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_closeup with None
    show player 37 with dissolve
    player_name "( Phew, that was close! )"
    player_name "( I'll just have to try again {b}tomorrow night{/b}... )"
    player_name "[int_warn]( If only I knew my way around {b}computers{/b} a bit more... )"
    hide player with dissolve
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
