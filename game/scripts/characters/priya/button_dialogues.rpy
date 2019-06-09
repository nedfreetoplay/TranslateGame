label priya_button_intro:
    scene expression "backgrounds/location_hospital_lab_blur.jpg"
    show player 5 at left
    show priya f_angry a_dressed_point
    with dissolve
    priya "Опять ты?!"
    priya "Что ты здесь делаешь?!"
    show priya f_stern a_dressed_crossed with dissolve
    pause
    show priya f_angry
    priya "У тебя есть какие-то результаты?"
    show priya f_stern
    return

label priya_button_menu_no:
    show priya f_stern a_dressed_crossed
    show player 24 at left
    player_name "Нет, извени."
    player_name "Я только-"
    show player 5
    show priya f_angry a_dressed_point with dissolve
    priya "Это запретная зона!"
    priya "Ты не можешь просто приходить и уходить, когда захочешь..."
    show priya f_stern a_dressed_crossed with dissolve
    show player 10
    player_name "Прости, {b}Прия{/b}."
    show player 24
    player_name "Я-"
    player_name "Я пойду..."
    show player 5
    show priya f_facepalm_talk a_dressed_facepalm with dissolve
    priya "{b}*вздыхая*{/b}"
    priya "Нет, прошу прощения...прости."
    show priya f_hopeful_talk a_dressed_sides with dissolve
    priya "Я не хотела кричать на тебя."
    show priya f_normal_talk
    priya "Это просто... Тебе опасно здесь находиться."
    priya "Так что, пожалуйста, не возвращайся, если не хочешь что-то сообщить."
    show priya f_normal
    show player 10
    player_name "Хорошо."
    hide player
    hide priya
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
