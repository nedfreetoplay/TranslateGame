label orc_battle_start:
    call screen orc_battle

label orc_battle_finish:
    $ player.go_to(L_home_bedroom)
    scene expression "backgrounds/location_erik_minigame07c.jpg" with dissolve
    $ renpy.pause(0.7, hard=True)
    scene expression "backgrounds/location_erik_minigame07d.jpg" with dissolve
    $ renpy.pause(1, hard=True)
    scene expression Animation("backgrounds/location_erik_minigame07e.jpg", 0.5, "backgrounds/location_erik_minigame07f.jpg", 0.5) with fade
    pause
    $ game.timer.tick()
    if not June.known(june_cosplay):
        scene bedroom_sex2
        if June.over(june_mc_help_2):
            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Ухх..."
            show june_sitting 12
            show player_sitting 5
            june "Похоже, у нас опять тот же конец."
            show player_sitting 3
            june "Прости..."
            show june_sitting 13
            show player_sitting 4
            player_name "Нет, все в порядке!"
            show june_sitting 12
            show player_sitting 5
            june "Ты все ещё думаешь, что это странно?"
            show june_sitting 13
        else:

            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Ухх..."
            show june_sitting 12
            show player_sitting 5
            june "Я... Я не знала, что так закончится игра, клянусь!"
            show june_sitting 13
            show player_sitting 4
            player_name "Это было... неожиданно?"
            show june_sitting 12
            show player_sitting 3
            june "Это так унизительно..."
            show june_sitting 13
            show player_sitting 4
            player_name "Нет, все в порядке!"
            show june_sitting 12
            show player_sitting 5
            june "Тебе это не показалось странным?"
            show june_sitting 13
            $ june_mc_help_2.finish()
        menu:
            "Это отвратительно.":
                show june_sitting 13 at Position(xpos=300,ypos=787)
                show player_sitting 4 at right
                player_name "Не знаю... Это мерзко?"
                show player_sitting 5
                june "..."
                show player_sitting 6
                player_name "Но, как бы то ни было, все в порядке."
                show player_sitting 1
                show june_sitting 12
                june "Извини... Если бы я только знала..."
                june "Ты все ещё хочешь поиграть со мной в эту игру?"
                show player_sitting 2
                show june_sitting 13
                player_name "Да, это весело!"
                show player_sitting 1
                show june_sitting 12
                june "Спасибо... В любом случае, мне действительно пора идти, уже поздно."
                show player_sitting 2
                show june_sitting 11
                player_name "Окей!"
                player_name "Спокойной ночи!"
                show player_sitting 1
                show june_sitting 10
                june "И тебе, {b}[firstname]{/b}."
            "Она горячая!":

                show player_sitting 2 at right
                show june_sitting 11 at Position(xpos=300,ypos=787)
                player_name "Нет, вообще-то это даже забавно... "
                player_name "... и жарко."
                show june_sitting 10
                show player_sitting 1
                june "Правда? Ты так думаешь?"
                show june_sitting 11
                show player_sitting 2
                player_name "Да, я думаю, орки могут быть довольно сексуальными!"
                show player_sitting 1
                june "..."
                show june_sitting 10
                june "Я... люблю орков..."
                show player_sitting 5
                june "На самом деле, я планировал замутить косплей в ближайшее время..."
                show player_sitting 2
                show june_sitting 11
                player_name "Костюм орка? Для чего?"
                show player_sitting 1
                show june_sitting 10
                june "Я планировал пойти на комический съезд в костюме орка...."
                show june_sitting 12
                june "... но есть проблема."
                june "Я не думаю, что смогу найти все части костюма вовремя."
                show player_sitting 2
                show june_sitting 11
                player_name "Звучит круто!"
                show player_sitting 1
                show june_sitting 10
                june "Ты так думаешь?"
                show player_sitting 2
                show june_sitting 11
                player_name "Чего тебе не хватает?"
                show player_sitting 1
                show june_sitting 10
                june "У меня есть краска для тела... Но мне нужны фальшивые уши, зубы и..... пояс."
                show player_sitting 2
                show june_sitting 11
                player_name "Держу пари, я могу найти их для тебя!"
                show player_sitting 1
                show june_sitting 10
                june "На самом деле? Ты сделаешь это для меня??"
                show player_sitting 2
                show june_sitting 11
                player_name "Я могу попробовать!"
                show player_sitting 6
                player_name "Я думаю, ты будешь выглядеть потрясающе, как орк!"
                show player_sitting 1
                june "..."
                show player_sitting 3
                show june_sitting 10
                june "Это действительно мило. Спасибо, {b}[firstname]{/b}."
                show player_sitting 2
                show june_sitting 11
                player_name "Ну, мне, наверное, пора идти спать..."
                show player_sitting 1
                show june_sitting 10
                june "Да, я тоже должна вернуться домой..."
                june "Спасибо за приглашение! Было весело."
                show player_sitting 6
                show june_sitting 11
                player_name "Да, это действительно было круто."
                show player_sitting 1
                show june_sitting 10
                june "Дай мне знать, если найдешь эти части костюма!"
                june "Увидимся завтра?"
                show player_sitting 2
                show june_sitting 11
                player_name "Конечно!"
                player_name "Давай, я провожу тебя до выхода."
                scene bedroom_night
                show player 35
                with fade
                player_name "Хм... Интересно, где я мог найти {b}части костюма{/b}."
                player_name "Может, мне стоит сходить проверить {b}почту{/b}?"
                show player 55 at Position(xoffset=12)
                player_name "*Зевок*"
                show player 56
                player_name "Я пойду завтра, мне нужно немного поспать..."
                hide player with dissolve
                $ June.add_event(june_cosplay)
                jump sleeping
    else:

        scene bedroom_sex2
        show june_sitting 2 at Position(xpos=300,ypos=787)
        show player_sitting 1 at right
        with fade
        june "Наконец-то! Я пыталась победить его в течение нескольких дней..."
        show june_sitting 3
        june "У тебя хорошо получается."
        show june_sitting 4
        show player_sitting 6
        player_name "Да, я думаю, что игра действительно увлекательная!"
        show june_sitting 1
        show player_sitting 2
        player_name "Эй, а сколько сейчас времени?"
        show june_sitting 5
        show player_sitting 5
        june "Черт, уже за полночь...."
        show june_sitting 6
        show player_sitting 4
        player_name "Мы пробыли здесь дольше, чем я думал..."
        player_name "Похоже, мы потеряли счет времени."
        show june_sitting 5
        show player_sitting 1
        june "Мне пора домой, мои родители, наверное, очень волнуются."
        show june_sitting 3
        june "Спасибо за вечер, {b}[firstname]{/b}."
        show june_sitting 4
        show player_sitting 2
        player_name "Увидимся в школе?"
        show player_sitting 1
        show june_sitting 3
        june "Конечно!"
    $ game.main()

label orc_battle_fail:
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    scene bedroom_sex2
    show june_sitting 4 at Position(xpos=300,ypos=787)
    show player_sitting 4 at right
    with fade
    player_name "Упссс..."
    show player_sitting 3
    show june_sitting 3
    june "Думаю, нам нужно немного попрактиковаться."
    show player_sitting 4
    show june_sitting 4
    player_name "Ха-ха, прости."
    show player_sitting 3
    show june_sitting 3
    june "Все в порядке, я уверен, что мы победим его в конце концов!"
    show player_sitting 6
    show june_sitting 4
    player_name "Надеюсь на это! Иначе я ужасный товарищ по команде..."
    show player_sitting 1
    show june_sitting 3
    june "В любом случае, мне пора, уже довольно поздно.."
    june "Дайте мне знать, если вы хотите играть завтра снова!"
    show player_sitting 2
    show june_sitting 4
    player_name "Окей!"
    player_name "Спокойной ночи!"
    show player_sitting 1
    show june_sitting 3
    june "И тебе, {b}[firstname]{/b}."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
