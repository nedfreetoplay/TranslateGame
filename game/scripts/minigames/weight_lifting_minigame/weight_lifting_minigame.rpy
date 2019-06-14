label weightlifting_dialogue:
    if player.location.is_here(M_kevin):
        scene lifting
        show player 1 at left with dissolve
        show kevin 9 at right with dissolve
        kev "Приветик, приятель!"
        show kevin 8 at right
        show player 14 at left
        player_name "Привет, {b}Кевин{/b}!"
        show kevin 10 at right
        show player 11 at left
        kev "Готов поднять железку, братан?"
        menu:
            "Конечно, бро.":
                show player 17 at left
                show kevin 8 at right
                player_name "Да, бро!"
                show kevin 9 at right
                show player 11 at left
                kev "Начни с лёгкого веса!"
                show kevin 8 at right
                show player 12 at left
                player_name "Какие упражнения мы делаем?"
                show kevin 13 at right
                show player 24 at left
                kev "Возьми эти легкие гантели..."
                show kevin 9 at right
                show player 85 at left
                if player.stats.str() < 3:
                    show player 85 at left
                elif player.stats.str() < 7:
                    show player 307 at left
                else:
                    show player 308 at left
                kev "Мы собираемся сделать несколько {b}плечевых прессов{/b}!!"
                hide player 85 at left
                hide player 307 at left
                hide player 308 at left
                hide kevin 9 at right
                with dissolve
                hide lifting
                jump weightlifting
            "Не могу прямо сейчас.":

                show player 10 at left
                show kevin 8 at right
                player_name "Я сейчас не могу."
                player_name "Я должен сделать кое-что еще..."
                show kevin 9 at right
                show player 1 at left
                kev "Не беспокойся, братан!"
                show kevin 11 at right
                show player 84 at left
                kev "Увидимся в следующий раз, братан!"
                player_name "Пока!"
                hide player 84 at left with dissolve
                hide kevin 11 at right with dissolve
                hide lifting
                jump training_dialogue


            "Пропустить мини-игру (чит)." if game.cheat_mode:
                $ player.stats.increase("str")
                $ game.timer.tick()
                show unlock25 at truecenter with dissolve
                $ renpy.pause()
                jump training_dialogue
    else:
        scene expression game.timer.image("training{}_b")
        show player 3 at left with dissolve
        player_name "( Блин, Кевина здесь нет. )"
        show player 34 at left
        if game.timer.is_weekend():
            player_name "( Возможно, он находится дома... )"
        else:
            player_name "( Держу пари, он тусуется в {b}кафетерии{/b}. )"
        hide player with dissolve
        $ game.main()

label weightlifting:
    $ style.time_bar.left_bar = "buttons/bar_full.png"
    $ style.time_bar.right_bar = "buttons/bar_empty.png"
    call screen weightlifting

label weightlifting_done:
    scene weightlifting03
    $ renpy.checkpoint()
    $ renpy.pause()
    scene lifting
    show player
    show kevin 10 at right
    with fade
    kev "Прямо сейчас, приятель!"
    show kevin 8 with dissolve
    show player f_normal_talk
    player_name "Поразительно. Мои руки и плечи горят..."
    show player f_normal
    show kevin 9
    kev "Продолжай качать, братан, и у тебя будут такие же безумные пушки!!"
    show kevin 8
    show player f_laugh
    player_name "Спасибо, что заметил меня, {b}Кевин{/b}!"
    show player f_normal
    show kevin 9
    kev "Нет проблем, братан! Приходи завтра!"
    show kevin 8
    hide player
    with dissolve
    show unlock25 at truecenter with dissolve
    $ renpy.pause()
    hide unlock25 with dissolve
    $ player.stats.increase("str")
    $ game.timer.tick()
    hide weightlifting03
    jump training_dialogue

label weightlifting_fail:
    scene weightlifting04
    $ renpy.checkpoint()
    $ renpy.pause()
    scene lifting
    show player f_tired
    show kevin 11b at right
    with fade
    kev "Whoa!"
    kev "Все в порядке, приятель?!"
    show kevin 8 with dissolve
    show player f_tired_talk
    player_name "Y-yeah, I think so."
    player_name "Sorry, I don't know what happened..."
    show player f_tired
    show kevin 9
    kev "I can back you down a few pounds..."
    show kevin 8
    show player f_skeptical_talk
    player_name "No, I can do it!"
    show player f_skeptical
    show kevin 9
    kev "You're sure?"
    show kevin 8
    show player f_normal_talk
    player_name "I'm positive!"
    show player f_normal
    show kevin 9
    kev "Heh, right on bro!"
    show kevin 10 with dissolve
    kev "You're gonna be a beefcake in no time with an attitude like that!"
    show kevin 8
    hide player
    with dissolve
    show unlock26 at truecenter with dissolve
    $ renpy.pause()
    hide unlock26 with dissolve
    $ game.timer.tick()
    hide weightlifting04
    jump training_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
