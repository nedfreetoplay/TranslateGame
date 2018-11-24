label annie_button_home_intro:
    show player 10 at left
    show annie 6 at right
    with dissolve
    player_name "Привет, {b}Энни{/b}."
    show player 5
    show annie 5
    ann "{b}[firstname]{/b}?!"
    show annie 4
    ann "Что ты делаешь в моем доме?"
    show annie 6
    show player 12
    player_name "Вообще-то, это хороший вопрос..."
    show player 5
    show annie 5
    ann "Разве у тебя нет домашней работы, которую ты должен делать?!"
    show annie 6
    show player 10
    player_name "Я эмм... Да, типа того..."
    show player 5
    pause
    show annie 5
    ann "Ну, хватит меня беспокоить, иди и сделай это!"
    show annie 6
    return

label annie_button_home_menu_alright_sheesh:
    show player 10 at left
    show annie 6 at right
    player_name "Хорошо, хорошо!"
    player_name "Тебе действительно нужно удалить эту палку."
    show player 5
    show annie 5
    ann "О чем ты вообще говоришь?"
    show annie 6
    show player 14
    player_name "Знаешь, тот, что у тебя в заднице."
    show player 13
    show annie 8
    ann "Ты хотите задержание?!" # Do you want detention?!
    ann "Я напишу тебе, здесь и сейчас!"
    show annie 1
    show player 12
    player_name "Мы даже не в школе, {b}Энни{/b}!"
    show player 5
    show annie 17 with dissolve
    ann "Вот и все, я получу свой блокнот.-"
    show annie 6 with dissolve
    show player 10
    player_name "Ладно, хватит!"
    player_name "Я ухожу, черт возьми!"
    hide player
    hide annie
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
