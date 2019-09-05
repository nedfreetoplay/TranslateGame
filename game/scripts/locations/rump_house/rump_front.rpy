label mayor_rumps_frontyard_dialogue:
    $ game.main()

label mayor_rumps_house_locked:
    scene expression player.location.background_closeup with None
    show player f_worried
    show rump_guard 1 at right
    with dissolve
    guard "..."
    show player f_worried_talk
    player_name "Эээ, здрасьте?"
    show player f_worried
    show rump_guard 2
    guard "Что тебе нужно, пацан?"
    show rump_guard 1
    show player f_worried_talk
    player_name "Это дом {b}Мэра Рампа{/b}, верно?"
    show player f_worried
    show rump_guard 2
    guard "Так точно."
    guard "У тебя назначена встреча?"
    show rump_guard 1
    show player f_worried_talk
    player_name "Нет..."
    show player f_worried
    show rump_guard 2
    guard "Тогда двигай дальше, пожалуйста. Здесь не место для гуляния."
    show rump_guard 1
    show player f_worried_talk
    player_name "Я только-"
    show player f_worried
    show rump_guard 2
    guard "Двигай отсюда!"
    show rump_guard 1
    show player f_surprised_teeth
    player_name "!!!"
    hide rump_guard
    show player 4 at center
    with dissolve
    player_name "( Как, черт возьми, мне добится {b}встречи{/b} с {b}мэром{/b}? )"
    show popup_unfinished at truecenter
    pause
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
