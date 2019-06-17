label tired_training_dialogue:
    scene expression game.timer.image("training{}_b")
    show player 5 with dissolve
    player_name "( Я устал, Я должен пойти домой и поспать. )"
    hide player with dissolve
    return

label cant_solo_lift:
    if game.timer.is_day():
        scene expression game.timer.image("training{}_b")
        show player 11 at left with dissolve
        player_name "( Сам я не справлюсь. )"
        player_name "( Нужно, чтобы кто-то меня подстраховал! )"
        hide player with dissolve
    else:
        call expression game.dialog_select("tired_training_dialogue")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
