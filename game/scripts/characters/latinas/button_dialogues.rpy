label latinas_dialogue_shower:
    scene location_school_lockershowers_closeup
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    show player 57 zorder 0 at left
    with dissolve
    lopez "Хэй! Что ты здесь делаешь?"
    show lopez f_angry
    show player 58
    player_name "Эмм... Просто пытаюсь принять душ?"
    show lopez f_angry_talk
    show player 59
    lopez "Слушай, парень. Эта наша территория, так что иди погуляй где-то еще!"
    show lopez f_angry
    show martinez f_normal_talk
    martinez "Подожди, {b}Лопес{/b}!"
    martinez "Йоу, Я думаю это тот парень о котором нам говорили!"
    show lopez f_angry_left_talk
    show martinez f_normal
    lopez "Что?! Не может быть..."
    lopez "Ты хочешь сказать что у этого парня {b}Огромный член{/b}?"
    show lopez f_angry
    show martinez f_angry_talk
    martinez "Хорошо, парень! Покажи нам что там у тебя внизу, ты можешь его вытащить!"
    show martinez f_angry
    show player 60
    player_name "Эммм... я думаю что откажусь. Я просто приму душ дома тогда-"
    show martinez b_towelgrab f_empty a_empty
    pause
    show player 61
    show lopez f_surprised_down
    show martinez b_towel a_towel_hold_towel f_smirk_down
    with hpunch
    pause
    player_name "..."
    show player 62
    show martinez f_normal_talk_right
    martinez "Вот - видишь!"
    show martinez f_smirk_down
    show lopez f_normal_down_talk
    lopez "...Вот это ты называла {b}большим{/b}?"
    show lopez f_normal_down
    show martinez f_surprised_right
    martinez "Wha-"
    show player 63
    show martinez f_suspicious
    martinez "Он вялый?!..."
    martinez "...Его нужно немного возбудить..."
    show martinez f_eyeroll
    martinez "...Хмм..."
    show martinez f_normal_talk_right
    martinez "...Это должно сработать!"
    show lopez f_normal with None
    show martinez f_normal_talk_right b_towel a_empty
    show martinez_body_parts a_towel_hold_towel_pull1 zorder 3
    with dissolve
    pause
    show player 64
    show lopez f_surprised_down_down b_toweldown a_towel_surprised
    show martinez f_smirk_down
    show martinez_body_parts a_towel_hold_towel_pull2
    with hpunch
    pause
    show lopez f_angry_left_talk a_toweldown_cover1
    show martinez a_towel_crossed
    hide martinez_body_parts
    with dissolve
    lopez "О мой бог, puta(шлюха)!"
    show lopez f_angry
    show martinez f_normal_talk_right
    martinez "Расслабься, все уже видели его в школе! Хаха!"
    show martinez f_laugh
    martinez "Хаха!"
    show martinez f_smirk_down
    show lopez f_surprised_down
    lopez "Yo, it's not doing anything!"
    show lopez f_normal_down
    show martinez f_eyeroll
    martinez "Maybe he's into guys?"
    show martinez f_angry
    show lopez f_normal_down_talk a_toweldown_pull1 with dissolve
    lopez "Here, I know what will work!"
    show martinez b_empty
    show martinez_body_parts b_towelup zorder 0
    show lopez f_normal_down a_toweldown_pull2
    with dissolve
    pause
    show martinez f_smirk_down2
    show lopez f_surprised_down
    with hpunch
    pause
    show player 65
    show martinez f_smirk_down
    player_name "...Ох... нет..."
    pause
    show player 66 with hpunch
    show martinez f_surprised_down
    pause
    hide martinez_body_parts
    show martinez b_towel
    show lopez f_surprised_right a_toweldown_cover2
    with dissolve
    show player 67
    lopez "Ох, дермо!"
    lopez "{b}Энни{/b} пришла!!"
    show lopez f_sorry
    show martinez f_sad_down a_towel_cover b_towel with dissolve
    show player 68
    show annie 1 zorder 3 at Position (xpos=400)
    ann "..."
    show annie 3
    ann "Что тут вообще происходит??"
    show player 69
    show annie 1
    player_name "Я просто пытался-"
    show player 68
    show annie 3
    ann "Выставить себя неподобающе?"
    show annie 4
    ann "{b}СНОВА{/b}!?"
    show player 69
    show annie 6
    player_name "Нет, это нет-"
    show player 68
    show annie 5
    ann "Я не хочу слышать твои жалкие отговорки!"
    ann "Мне было приказано привести нарушителей в {b}Кабинет{/b}!"
    show annie 7
    ann "Иди со мной, {b}СЕЙЧАС{/b}!!!"
    show annie 8f
    ann "...а вы двое, убирайтесь отсюда пока я вас обеих не задержала!!!"
    hide lopez
    hide martinez
    hide player
    hide annie
    with dissolve
    $ renpy.end_replay()
    return

label latinas_dialogue_leave:
    show player 57 at left
    show martinez b_towel a_towel_crossed f_angry zorder 1 at Position (xpos=250)
    show lopez b_towel a_towel_hips f_angry_talk zorder 2
    with dissolve
    lopez "Хэй! Ты опять здесь чтобы доставить нам неприятности?"
    show player 58 at left
    show lopez f_angry
    player_name "Эмм... Только пытаюсь принять душ?"
    show player 59 at left
    show martinez f_angry_talk
    martinez "Вали отсюда, йо!"
    show martinez f_angry
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
