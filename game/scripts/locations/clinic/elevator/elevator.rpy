label elevator_dialogue:
    $ player.go_to(L_hospital_elevator)
    if M_priya.is_state(S_priya_roz_camera_check):
        call expression game.dialog_select("elevator_priya_check_pregnax")
        $ player.go_to(L_hospital_floor3)
        $ M_priya.trigger(T_priya_helped_roz_with_camera)
        $ game.main()
    $ player.location.call_screen(False)

label elevator_priya_check_pregnax:
    scene expression "backgrounds/location_hospital_elevator_interior.jpg"
    show roz 21 at left
    show player 13f at right
    with dissolve
    roz "Ну вот."
    show roz 20
    pause
    show roz 7
    show player 696 at Position (xoffset=-9)
    with dissolve
    roz "Он должен сделать снимок, когда я нажимаю кнопку, но ничего не происходит."
    roz "Глупая штука сломалась!"
    show roz 6
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "Хмм."
    player_name "О, вот мы и приехали!"
    show player 701 at Position (xoffset=-36) with dissolve
    pause
    show player 700 at Position (xoffset=-2) with dissolve
    player_name "Вам просто нужно открыть панель здесь, чтобы включить камеру."
    player_name "Я думаю, что должен-"
    show player 702
    player_name "!!!" with flash
    show player 703 at Position (xoffset=-36) with dissolve
    player_name "И!"
    player_name "Да, это определенно работает..."
    pause
    show roz 23 with vpunch
    show player 10f with dissolve
    player_name "Ты только что остановила лифт?"
    show player 5f
    show roz 7 with dissolve
    roz "Я просто хочу убедиться, что нас не побеспокоят."
    show roz 6
    show player 12f
    player_name "Ааа?"
    player_name "Зачем-"
    show roz 10 with dissolve
    pause
    show roz 8
    show player 6f
    player_name "!!!" with hpunch
    player_name "Ах, что ты делаешь?!?!"
    show roz 9
    roz "Готовлюсь к съемке крупным планом."
    show roz 8
    player_name "Да, я не знаю, что это значит..."
    show roz 9
    roz "Ну, теперь, когда у тебя все получилось, я хочу, чтобы ты сфотографировал меня."
    roz "Для ребят из приюта."
    show roz 8
    show player 113f with dissolve
    player_name "Почему я?!"
    show player 114f
    show roz 9
    roz "Хочешь пойти на третий этаж, малыш?"
    show roz 8
    show player 113f
    player_name "Да..."
    show player 114f
    show roz 9
    roz "Тогда я предлагаю тебе прекратить болтать и начать щелкать."
    show roz 8
    show player 24f
    player_name "..."
    show roz 9
    roz "Ты почеши мне спину, если хочешь, я почешу тебе."
    show roz 8
    show player 37f with dissolve
    player_name "Тьфу, черт."
    show player 24f with dissolve
    show roz 9
    roz "Убедись, что получается отлично!"

    if Game.is_halloween():
        scene expression "backgrounds/location_hospital_cutscene01_halloween.jpg"
    else:
        scene expression "backgrounds/location_hospital_cutscene01.jpg"
    show expression FilteredText("... А я-то думал, что все будет просто.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Как я постоянно попадаю в такие ситуации?!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show expression FilteredText("Надеюсь, эти таблетки того стоят.") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_hospital_elevator_interior.jpg"
    show roz 22 at left
    show player 24f at right
    with dissolve
    roz "О, да!"
    roz "Это сведет ребят с ума!"
    show roz 20 with dissolve
    show player 10f
    player_name "Мы закончили?"
    show player 5f
    roz "Хмм?"
    show player 10f
    player_name "Мне действительно нужно поговорить с {b}Доктором Сингх{/b}."
    show player 5f
    show roz 23 with dissolve
    roz "Ох, точно."
    show roz 7
    roz "У вас, детишек, совсем нет терпения!" with vpunch
    show roz 6
    player_name "..."
    show roz 7
    roz "... И не говори никому, что это я привел тебя сюда!"
    show roz 6
    show player 10f
    player_name "Угу. Я никому не расскажу ни о чем... из этого."
    show player 5f
    show roz 7
    roz "Хорошо."
    roz "А теперь проваливай!"
    hide player with dissolve
    scene expression "backgrounds/location_hospital_third_blur.jpg"
    show player 24 with dissolve
    player_name "( Фу, ну и денек выдался! )"
    player_name "( По крайней мере, я поднялся на {b}третий этаж.{/b}. )"
    player_name "( Я должен {b}осмотреться{/b} и посмотреть, смогу ли я найти этого {b}Доктора Сингх{/b}. )"
    player_name "( Может, мне удастся найти отбеливатель для глаз, пока я здесь... )"
    hide player with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Roz"]["unlocked"] = True
    $ persistent.cookie_jar["Roz"]["gallery"]["02_unlocked"] = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
