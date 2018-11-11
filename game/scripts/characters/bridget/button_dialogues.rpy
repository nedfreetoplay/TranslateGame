label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Что ты здесь делаешь?"
    show player 32
    show coach 7
    player_name "Простите, мэм!!!"
    player_name "У меня просто есть вопросы!"
    show player 31
    show coach 3
    bri "Вопросы?!"
    bri "Какие?"
    show coach 7
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Лучше тренируй свою задницу в {b}Тренажерном зале{/b}, или я засуну свою ногу в нее!!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    show player 31
    show coach 3
    bri "Еще есть вопросы?!"
    show coach 7
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show coach 1
    player_name "... Хорошо, где я должен тренироваться?"
    show coach 7
    show player 5
    bri "..."
    show player 22
    show coach 3
    bri "Я только что тебе сказала!"
    show coach 4
    bri "В {b}Тренажерном зале{/b}!!!"
    show player 10
    show coach 7
    player_name "Но... Что я должен тренировать?"
    show player 11
    show coach 3
    bri "Ты должен работать над своими {b}силой{/b} и {b}ловкостью{/b}!"
    bri "Ты должен пройти {b}бег 110м с пепятствиями{/b} чтобы квалифицироваться в {b}школе{/b} и попасть в команду на {b}чемпионат штата{/b}!"
    show player 10
    show coach 7
    player_name "Это... Большая нагрузка."
    show player 23
    show coach 3
    bri "...И тебе лучше не подводить меня!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    hide coach
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show coach 1
    player_name "Я... Я забыл."
    show player 11
    show coach 3
    bri "Забыл? Ты самый грустный кусок мяса, что я когда-либо видела!"
    show player 22
    show coach 4
    bri "А теперь выметайся отсюда и приступай к {b}РАБОТЕ{/b}!!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
