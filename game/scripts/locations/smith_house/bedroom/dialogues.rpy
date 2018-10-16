label smith_bedroom_sneaking:
    scene expression "backgrounds/location_smith_bedroom_night_blur.jpg"
    show player 14 with dissolve
    player_name "Фух, думаю дома никого нет."
    show player 10
    player_name "{b}Мне нужно здесь осмотреться.{/b}"
    show player 35b
    pause
    show player 35
    player_name "Это что, голова козы над головой?"
    player_name "Такое ощущение, что эти глаза следят за мной..."
    show player 35b
    player_name "..."
    show player 10
    player_name "Уровень стремности только что достиг 110 процентов!"
    player_name "Нужно {b}найти эти тесты и сваливать отсюда{/b}."
    player_name "Эта комната выглядит как лучшее место, где она может их хранить."
    hide player with dissolve
    return

label smith_painting:
    if not player.has_item("smith_painting_key") and game.timer.is_dark():
        call expression game.dialog_select("smith_painting_dialogue")
        $ player.get_item("smith_painting_key")
    $ game.main()

label smith_painting_dialogue:
    scene expression "backgrounds/location_smith_bedroom_frame.jpg"
    show expression "objects/object_key_04.png" at Position (xoffset=-245,yoffset=-320)
    player_name "Хмм, этот ключ может мне пригодиться."
    player_name "{b}Может где-то в этой комнате я и смогу его применить{/b}"
    return

label smith_exams:
    call expression game.dialog_select("smith_exams_dialogue")
    $ player.get_item("smith_exams")
    $ player.remove_item("smith_painting_key")
    $ game.main()

label smith_exams_dialogue:
    scene expression "backgrounds/location_smith_bedroom_night_blur.jpg"
    show player 14 with dissolve
    player_name "Это они!"
    player_name "Не могу поверить, {b}Missy{/b} и {b}Becca{/b} были правы!"
    show player 13
    "Скрип..."
    show player 10
    player_name "... Что это было?!"
    show player 23
    player_name "Здесь кто-то есть!" with hpunch
    player_name "{b}Principal Smith{/b}! Нужно выбираться отсюда!"
    player_name "... Дерьмо! И куда мне теперь?!"
    hide player with dissolve
    return

label smith_window_exit_dialogue:
    if M_roxxy.is_state(S_roxxy_sneak_into_smith) and player.has_item("smith_exams"):
        call expression game.dialog_select("smith_window_exit_roxxy_sneak_into_smith")
        $ game.sleep_lock = False
        $ player.go_to(L_map)
        $ M_roxxy.trigger(T_roxxy_escaped_smith)
        $ game.main()
    jump expression game.dialog_select("smiths_frontyard_dialogue")

label smith_window_exit_roxxy_sneak_into_smith:
    scene expression "backgrounds/location_smith_frontyard_cutscene01.jpg"
    with fade
    show text "Как только я услышал, как кто-то шел из прихожей к спальням\n... Я выпрыгнул в открытое окно и приземлился на крышу снизу!\nМысль о том, что меня могли поймать в спальне {b}Principal Smith{/b}’s до сих пор преследует меня в кошмарах!" at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve
    scene expression "backgrounds/location_smith_frontyard_night_blur.jpg"
    show player 10
    player_name "Фух! Это было опасно!"
    player_name "Завтра я принесу эти тесты {b}Roxxy{/b} в школу!"
    player_name "А сейчас я хочу пойти домой и отдохнуть."
    show player 24
    pause
    show player 25
    player_name "... И сменить эти шорты!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
