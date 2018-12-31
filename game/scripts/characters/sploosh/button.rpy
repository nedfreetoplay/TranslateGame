label sploosh_button_dialogue:
    scene expression game.timer.image("backgrounds/location_pier_boxes{}.jpg")
    show player 10 at left with dissolve
    show sploosh 1 at right
    player_name "Здравствуйте?"
    Sploosh "ХХХХррррррр..."
    show player 4
    player_name "(Хммм... Он, должно быть, спит.)"
    menu:
        "Разбудить Адмирала Сплуш.":
            show player 10
            player_name "Эмм... Извините?"
            show sploosh 2
            show player 11
            python:
                if store.sploosh["amount"] != 0:
                    choices = store.sploosh["dialogues"]
                    choices.append(["There are currently {} dialogues written by our patrons!".format(store.sploosh["amount"]), "Так говорит команда разработчиков..."])
                    rng = random.randint(0, store.sploosh["amount"])
                    dialogues = choices[rng]
                    
                    
                    for dialogue in dialogues:
                        d = re.sub("\\\\n", "\\n", dialogue)
                        Sploosh(d)
                else:
                    renpy.show("player 23")
                    Sploosh("Я Король всего мира!!!")
            show player 23
            player_name "!!!" with hpunch
            show sploosh 1
            Sploosh "ХХХХррррррр..."
            show player 1
            player_name "Что за странный пират..."
            hide player with dissolve
        "Оставить.":
            player_name "Лучше не беспокоить его..."
            Sploosh "ХХХХррррррр..."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
