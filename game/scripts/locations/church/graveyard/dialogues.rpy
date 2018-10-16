label right_tombstone:
    scene location_church_graveyard_tombstone01
    if M_aqua.is_state(S_aqua_graveyard_search):
        call expression game.dialog_select("right_tombstone_aqua_graveyard_search")
        $ M_aqua.trigger(T_aqua_tomb_engraving)
    else:

        pause
    $ game.main()

label right_tombstone_aqua_graveyard_search:
    player_name "( Имя на этой надгробной плите - Бен Довер! )"
    player_name "( Должно быть единственная. )"
    player_name "( Но теперь, когда я нашел его, я не знаю, что я должен искать дальше... )"
    player_name "Хмм..."
    player_name "( Может быть, где-то есть {b}подсказка{/b}? )"
    player_name "( Эта гравировка выделяется... )"
    player_name "( Может, мне стоит поискать большой {b}колокол{/b} где-нибудь в городе? )"
    return

label stray_cat:
    scene location_church_graveyard_closeup
    if not M_player.is_set("found cat"):
        $ M_player.set("found cat", True)
        call expression game.dialog_select("stray_cat_first_pre")
        if player.has_item("cat_food"):
            call expression game.dialog_select("feed_cat")
            $ player.remove_item("cat_food")
            jump expression game.dialog_select("stray_cat_take_home")
        call expression game.dialog_select("stray_cat_first_after")

    elif not player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_no_food")

    elif player.has_item("cat_food"):
        call expression game.dialog_select("stray_cat_have_food_pre")
        $ player.remove_item("cat_food")
        menu stray_cat_take_home:
            "Взять домой.":
                call expression game.dialog_select("stray_cat_have_food_take_her_pre")
                call screen cat_name_input
                if cat_name.strip() == "":
                    $ cat_name = "Pussywillow"
                $ cat = Character("[cat_name]", color = "#c87efe")
                call expression game.dialog_select("stray_cat_have_food_take_her_after")
                $ M_player.set("pet cat", True)
            "Оставить.":

                call expression game.dialog_select("stray_cat_have_food_leave_her")

    hide cat
    hide player
    with dissolve
    $ game.main()

label stray_cat_first_pre:
    show player 11 at left with dissolve
    cat "Мяу"
    show player 10
    player_name "Ух, привет?"
    show player 11
    cat "Мяу"
    show player 10
    player_name "Откуда доносится этот звук?"
    cat "Мууууууурррррр!"
    show player 11
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show player 1
    pause
    show player 2
    player_name "Ааа."
    player_name "Ну привет малыш."
    show player 1
    show cat 4
    cat "Мммууурррр"
    show player 2
    show cat 3
    player_name "Что ты здесь делаешь совсем один?"
    player_name "Потерялся?"
    show player 1
    show cat 4
    cat "Мммууурррр"
    show player 2
    show cat 3
    player_name "Бедняжка."
    player_name "Я не вижу ошейника."
    show cat 3
    player_name "Наверно ничей..."
    player_name "Где твой дом, малыш?"
    show player 1
    show cat 4
    cat "Мммууурррр!"
    show player 11
    show cat 3
    pause
    show player 10
    player_name "Ну в чем дело?"
    show player 11
    show cat 4
    cat "Мммууурррр!"
    show player 30
    show cat 3
    player_name "Хмм..."
    show player 2
    player_name "ОХ, Я понял!"
    player_name "Ты - кошечка, правда?!"
    show player 1
    show cat 4
    cat "Мммууурррр"
    show cat 5 with dissolve
    cat "Мммууурррр"
    show player 2
    player_name "Ты выглядишь голодной."
    player_name "Хочешь кушать малышка?"
    show player 1
    show cat 4
    cat "Мяу"
    show player 2
    show cat 3
    return

label stray_cat_first_after:
    player_name "Хехе, хоршо. Может быть я смогу что-нибудь найти для тебя."
    show player 4
    show cat 3
    player_name "(Хмм.)"
    player_name "(Я бы хотел бы дать ей что-нибудь поесть.)"
    player_name "(Возможно в Consum-r продают что-нибудь.)"
    return

label stray_cat_no_food:
    show player 1 at left
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Мяу"
    show player 2
    show cat 3
    player_name "Ааа... До сих пор голодна?"
    show player 1
    show cat 4
    cat "Мурмяю"
    show player 2
    show cat 5
    player_name "Ты просто симпатяшка!"
    player_name "Я попробую найти тебе еду, хорошо?"
    show player 1
    show cat 4
    cat "Мрррррр"
    show player 2
    show cat 5
    player_name "Подожди!"
    return

label stray_cat_have_food_pre:
    show player 1 at left with dissolve
    show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
    pause
    show cat 4
    cat "Мяу"
    show player 2
    show cat 3
    player_name "Привет."
    show player 1
    show cat 4
    cat "Мяу"
    show player 2
    show cat 3
    label feed_cat:
        player_name "Угадай, что у меня есть для тебя?"
        show player 239_240
        pause
        hide player with dissolve
        show cplayer 1 at left with dissolve
        show cat 4
        cat "Ммррррр"
        show cplayer 2
        show cat 3
        player_name "Вот именно! Я принес тебе что-то вкусненькое!"
        show cat 4
        cat "Мяу"
        hide cat with dissolve
        show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
        pause



        hide cat with dissolve
        show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
        player_name "!!!" with hpunch
        hide cplayer with dissolve
        hide cat with dissolve
        show cat 8 at left with dissolve
        pause
        show cat 9
        cat "Пррррр"
        show cat 10
        player_name "Хехе, точно."
        player_name "Ням ням для киски!"
        show cat 9
        cat "Мурмяу"
        show cat 8

        scene black with fade
        scene location_church_graveyard_closeup with fade

        show cat 17 at left
        player_name "Вау, ты действительно голодна, не так ли?"
        show cat 18
        cat "Мууууууур!"
        show cat 17
        player_name "..."
        player_name "Ха, я рад, что тебе понравилось..."
        hide cplayer with dissolve
        show player 2 at left
        show cat 3 at Position(xpos=0.57, ypos=0.77)
        with dissolve
        player_name "Теперь стало лучше, не так ли, девочка?"
        show player 1
        show cat 4
        cat "Мрррр"
        show player 2
        show cat 5
        player_name "Ты такая милая."
        show player 4
        player_name "( Хмм... )"
        player_name "( Может, мне стоит забрать тебя домой. )"
        player_name "( Не думаю, что {b}[deb_name]{/b} будет против... )"
    return

label stray_cat_have_food_take_her_pre:
    show player 2
    player_name "Что ты сказала девочка?"
    player_name "Хочешь пойти домой ко мне?"
    show player 1
    show cat 4
    cat "Мрррр!"
    hide cat with dissolve
    show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
    pause
    hide cat with dissolve
    show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
    player_name "!!!" with hpunch
    hide player
    hide cat
    with dissolve
    show cat 13 at left with dissolve
    pause
    show cat 16
    pause
    show cat 14
    player_name "Хехе, ааа..."
    show cat 15
    pause
    show cat 14
    player_name "Буду считать, что это 'да'!"
    show cat 12
    cat "Мррррр"
    show cat 14
    player_name "Тебе понадобится имя, если ты поедешь домой со мной..."
    return

label stray_cat_have_food_take_her_after:
    player_name "Как насчет... [cat]?"
    player_name "Тебе нравится?"
    show cat 12
    cat "Мяу"
    show cat 14
    player_name "Хехе, хорошо. Тогда [cat]!"
    show cat 15
    cat "Мрррр"
    show cat 16
    pause
    show cat 14
    player_name "Хорошо [cat], Давай пойдем домой!"
    show popup_cat at truecenter with dissolve
    pause
    hide popup_cat with dissolve
    return

label stray_cat_have_food_leave_her:
    show player 10 at left
    show cat 5
    player_name "Хмм, извени малышка."
    player_name "Я не думаю, что {b}[deb_name]{/b} будет рада, если я приведу тебя домой."
    show player 11
    show cat 4
    cat "Мяу"
    show player 10
    show cat 5
    player_name "По крайней мере, я принес тебе поесть..."
    show player 11
    show cat 4
    cat "Мррррр"
    show player 10
    show cat 5
    player_name "Ты хорошая девочка."
    player_name "Оставайся в безопасности, хорошо?"
    show player 11
    show cat 4
    cat "Мяу"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
