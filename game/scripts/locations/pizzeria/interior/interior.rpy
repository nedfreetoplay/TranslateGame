label pizza_interior_dialogue:
    $ player.go_to(L_pizzeria_interior)

    if M_diane.is_state(S_diane_delivery_1):
        call expression game.dialog_select("pizza_interior_diane_delivery_1")
        $ M_diane.trigger(T_diane_make_delivery)
        $ M_tony.trigger(T_tony_intro)
    elif M_tony.is_state(S_tony_start):
        call expression game.dialog_select("pizza_interior_pizza_count_0")
        $ M_tony.trigger(T_tony_intro)


    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
