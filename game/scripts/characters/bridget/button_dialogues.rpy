label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Что ты здесь делаешь?"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Простите, мэм!!!"
    player_name "У меня просто есть вопросы!"
    show player 31
    show bridget f_angry_talk
    bri "Вопросы?!"
    bri "Какие?"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show bridget f_angry_talk at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Лучше тренируй свою задницу в {b}Тренажерном зале{/b}, или я засуну свою ногу в нее!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Да, мэм!!!"
    show player 31
    show bridget f_angry_talk
    bri "Еще есть вопросы?!"
    show bridget a_dressed_crossed f_angry
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "... Хорошо, где я должен тренироваться?"
    show bridget a_dressed_crossed f_angry
    show player 5
    bri "..."
    show player 22
    show bridget f_angry_talk
    bri "Я только что тебе сказала!"
    show bridget a_dressed_crossed f_angry_yell
    bri "В {b}Тренажерном зале{/b}!!!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "Но... Что я должен тренировать?"
    show player 11
    show bridget f_angry_talk
    bri "Ты должен работать над своими {b}силой{/b} и {b}ловкостью{/b}!"
    bri "Ты должен пройти {b}бег 110м с пепятствиями{/b} чтобы квалифицироваться в {b}школе{/b} и попасть в команду на {b}чемпионат штата{/b}!"
    show player 10
    show bridget a_dressed_crossed f_angry
    player_name "Это... Большая нагрузка"
    show player 23
    show bridget f_angry_talk
    bri "...И тебе лучше не подводить меня!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Да, мэм!!!"
    hide bridget
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show bridget a_dressed_crossed f_normal
    player_name "Я... Я забыл."
    show player 11
    show bridget f_angry_talk
    bri "Забыл? Ты самый грустный кусок мяса, что я когда-либо видела!"
    show player 22
    show bridget a_dressed_crossed f_angry_yell
    bri "А теперь выметайся отсюда и приступай к {b}РАБОТЕ{/b}!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Да, мэм!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
