label ronda_dialogue_intro:
    scene gym
    show ronda 2 at right
    show player 36 at left
    with dissolve
    player_name "Привет, {b}Ронда{/b}. Как дела?"
    show player 13 with dissolve
    show ronda 3
    ron "У меня всё хорошо. Этот вопрос был тренеровкой?"
    show ronda 2
    show player 11
    player_name "..."
    show player 10
    player_name "Нет-"
    show player 11
    show ronda 4
    ron "Тогда перестань шевелить этими губами и начни двигать эти... ножки!"
    show ronda 2
    show player 34
    player_name "???"
    show ronda 3
    ron "Не важно. Это то, что мой отец всегда говорит..."
    show player 5
    ron "В любом случае, тебе лучше поторопиться потому что испытания быстро приближаются!"
    show ronda 2
    return

label ronda_dialogue_talent_show_help:
    show player 10
    player_name "Я не думаю что тебя заинтересует стать добровольцом в {b}Мисс Девитт{/b} музыкальном шоу талантов?"
    show player 5
    show ronda 3
    ron "Музыкальном таланте? Нет, Мне это неинтересно."
    show ronda 2
    show player 10
    player_name "Ты уверена? Ты не играешь ни на каких инструментах и не поешь вообще?"
    show player 5
    show ronda 3
    ron "Эмм, разве ты не видишь что у меня есть более важные дела на которых я должна сосредоточиться. Как бег и плавание..."
    ron "Тебе надо тоже сосредоточиться на них!"
    ron "Ты никогда не попадешь в команду если ты продолжишь пропускать свои тренеровки!"
    show ronda 2
    show player 30
    player_name "Ты знаешь, в жизни есть вещи поважнее спорта, {b}Ронда{/b}..."
    show player 5
    show ronda 3
    ron "Пффф, да конечно."
    return

label ronda_dialogue_model_help:
    show player 2 at left
    show ronda 2 at right
    player_name "Я работаю на проектом для {b}Мисс Росс{/b} и для этого требуется настоящая топ модель."
    player_name "Тебя это не заинтересует?"
    show player 1
    show ronda 3
    ron "Я занята."
    show player 10
    show ronda 2
    player_name "Занята?"
    player_name "Делать что?"
    show player 11
    show ronda 4
    ron "Серьезно, {b}[firstname]{/b}?!"
    ron "Мне нужно пробежать 6 км и принять ледяной душ до футбольной тренеровки."
    show player 10
    show ronda 1
    player_name "Ухх..."
    show player 11
    show ronda 4
    ron "После, у меня будет только 40 минут чтобы привести себя в порядок до закрытия бассейна."
    show player 10
    show ronda 1
    player_name "Это сум-"
    show player 11
    show ronda 4
    ron "Тогда я вернусь домой что бы согреться и покачать пресс."
    show player 12
    show ronda 1
    player_name "ХОРОШО! Ладно! Я понял..."
    hide ronda
    hide player
    show player 12
    with dissolve
    player_name "Эта девченка ненормальная!"
    return

label ronda_dialogue_leave:
    show player 10
    player_name "Ясно."
    player_name "Увидимся позже."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
