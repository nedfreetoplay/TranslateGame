label ronda_pool_dialogue_pre_cassie_fun:
    show ronda b_swim a_swim_sides f_normal at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "..."
    show ronda f_normal_talk
    ron "Что ты вообще здесь делаешь?"
    show ronda f_normal
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Просто делаю некоторые упражнения!"
    player_name "Я подумал что надо с чего-то начать, и это поможет подготоваиться к отборочным соревнованиям!"
    show ronda f_normal_talk
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Слушай: Я не смогу помочь тебе, не говоря уже о том что бы зайти в воду одновременно с тобой... Так что забудь об этом, хорошо?"
    show ronda f_normal
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "Ничего страшного!"
    player_name "Я сам справлюсь..."
    show ronda f_rolleyes
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Угх... неважно."
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda b_swim a_swim_sides f_upset_talk at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "Здесь надо заплатить Кэйсси за небольшой визит?"
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ухх... Я пришел сюда только поплавать?"
    show ronda f_upset_talk
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Можешь перестать притворяться..."
    ron "...Ты здесь не для тренировки, как и я."
    show ronda f_upset
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ухх... окей?"
    show ronda f_upset_angry
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Угх... ты просто жалок."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
