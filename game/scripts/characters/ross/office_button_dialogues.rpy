label button_ross_office_generic_pre_hscene:
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg")
    show ross 11 at left
    show player 1f at right
    with dissolve
    ross "Ну привет, {b}[firstname]{/b}."
    ross "Мило с твоей стороны что ты решил навестить меня!"
    show ross 10
    show player 2f
    player_name "Здравствуйте, {b}Мисс Росс{/b}."
    show ross 11
    show player 1f
    ross "Чем я могу тебе помочь?"
    return

label button_ross_office_generic_post_hscene:
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg")
    show ross 10 at left
    show player 2f at right
    with dissolve
    player_name "Привет, {b}Мисс Росс{/b}!"
    show player 1f
    show ross 27 with dissolve
    ross "{b}[firstname]{/b}! Я так рада тебя видеть!"
    show ross 13 with dissolve
    ross "... Я надеюсь, что ты здесь за еще одним частным уроком?"
    return

label ross_dialogue_office_private_lessons:
    show ross 12
    show player 2f
    player_name "Да, мне бы это понравилось!"
    show ross 13
    show player 1f
    ross "Мммм, поторопись и запри дверь!"
    show ross 12
    show player 2f
    player_name "Х-хорошо..."
    return

label ross_dialogue_office_leave:
    scene expression game.timer.image("backgrounds/location_school_office3_closeup{}.jpg")
    show ross 10 at left
    show player 2f at right
    player_name "O, мне ничего не нужно."
    player_name "Простите что беспокою вас."
    show ross 11
    show player 1f
    ross "Не за что извинятся, {b}[firstname]{/b}!"
    ross "Помогать талантливым молодым художникам моя специальность!"
    show ross 10
    show player 2f
    player_name "Хех, хорошо."
    player_name "Мне нужно идти..."
    show ross 11
    show player 1f
    ross "Ой, понятно."
    ross "Пока, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
