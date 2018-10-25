label ronda_pool_dialogue_pre_cassie_fun:
    show ronda 5 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "..."
    show ronda 6
    ron "Что ты вообще здесь делаешь?"
    show ronda 5
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Просто делаю некоторые упражнения!"
    player_name "Я подумал что надо с чего-то начать, и это поможет подготоваиться к отборочным соревнованиям!"
    show ronda 6
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Слушай: Я не смогу помочь тебе, не говоря уже о том что бы зайти в воду одновременно с тобой... Так что забудь об этом, хорошо?"
    show ronda 5
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "Ничего страшного!"
    player_name "Я сам справлюсь..."
    show ronda 7
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Угх... неважно."
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda 8 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "Здесь надо заплатить Кэйсси за небольшой визит?"
    show ronda 10
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ухх... Я пришел сюда только поплавать?"
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Можешь перестать притворяться..."
    ron "...Ты здесь не для тренировки, как и я."
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ухх... окей?"
    show ronda 9
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Угх... ты просто жалок."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
