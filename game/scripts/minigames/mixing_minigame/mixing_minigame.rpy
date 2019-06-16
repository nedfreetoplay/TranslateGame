label shaking_minigame_win:
    show player 135 with dissolve
    player_name "Надеюсь, я все сделал правильно!"
    player_name "Я не хочу разочаровывать {b}Диану{/b}."
    hide player with dissolve
    scene black with fade
    scene expression L_diane_garden.background_blur
    show player 137 zorder 0 at Position (xpos=222,ypos=648)
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_laydown f_laying_explain_close zorder 2 at Position (ypos=982)
    with dissolve
    pause
    show diane f_laying_smirk_up_talk
    with dissolve
    dia "Ммм, это выглядит вкусно !!"
    show player 426 at Position (xpos=175,ypos=648)
    show diane a_drink_sip f_laying_drinking
    with dissolve
    pause
    show diane a_drink f_laying_laugh with dissolve
    dia "Спасибо, {b}[firstname]{/b}!!!"
    show diane f_laying_smirk_up
    show player 429
    player_name "С удовольствием!"
    player_name "А теперь расслабься, пока я работаю в твоем саду."
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Хе-хе, да, сэр!"
    $ M_diane.trigger(T_diane_made_drink)
    $ player.go_to(L_diane_garden)
    $ M_diane.trigger(T_diane_gave_drink)
    $ game.main()

label shaking_minigame_fail:
    show player 135 with dissolve
    player_name "Надеюсь, я все сделал правильно!"
    player_name "Я не хочу разочаровывать {b}Диану{/b}."
    hide player with dissolve
    scene black with fade
    scene expression L_diane_garden.background_blur
    show player 137 zorder 0 at Position (xpos=222,ypos=648)
    show diane_chair up zorder 1
    show diane b_laying_back_shirtless a_laydown f_laying_shamed zorder 2 at Position (ypos=982)
    with dissolve
    pause
    show diane f_laying_shamed_talk
    dia "Это не то, что я заказывала..."
    show diane f_laying_shamed
    show player 136
    player_name "Не то?"
    player_name "Упс!"
    show player 137
    show diane f_laying_smirk_up_talk
    dia "Хочешь, я тебе покажу?"
    show diane f_laying_smirk_up
    show player 136
    player_name "Нет!"
    player_name "Я сделаю все правильно. Одну секунду..."
    $ player.go_to(L_diane_garden)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
