label pizza_exterior_dialogue:
    $ player.go_to(L_pizzeria_exterior)
    if L_pizzeria_exterior.first_visit:
        call expression game.dialog_select("pizza_exterior_first_visit")
        $ L_pizzeria_exterior.visited()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
