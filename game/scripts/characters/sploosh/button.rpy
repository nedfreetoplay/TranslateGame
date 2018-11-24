label sploosh_button_dialogue:
    scene expression game.timer.image("backgrounds/location_pier_boxes{}.jpg")
    show player 10 at left with dissolve
    show sploosh 1 at right
    player_name "Hello?"
    Sploosh "ZZZzzzz..."
    show player 4
    player_name "(Hmm... He must be sleeping)"
    menu:
        "Wake up Admiral Sploosh":
            show player 10
            player_name "Erm... Excuse me?"
            show sploosh 2
            show player 11
            python:
                if store.sploosh["amount"] != 0:
                    choices = store.sploosh["dialogues"]
                    choices.append(["There are currently {} dialogues written by our patrons!".format(store.sploosh["amount"]), "So sayeth the dev team..."])
                    rng = random.randint(0, store.sploosh["amount"])
                    dialogues = choices[rng]
                    
                    
                    for dialogue in dialogues:
                        d = re.sub("\\\\n", "\\n", dialogue)
                        Sploosh(d)
                else:
                    renpy.show("player 23")
                    Sploosh("I'm the king of the world!!!")
            show player 23
            player_name "!!!" with hpunch
            show sploosh 1
            Sploosh "ZZZzzzz..."
            show player 1
            player_name "What a strange pirate..."
            hide player with dissolve
        "Leave":
            player_name "I'd better not disturb him..."
            Sploosh "ZZZzzzz..."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
