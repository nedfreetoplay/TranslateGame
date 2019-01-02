label tony_dialogue:
    call expression game.dialog_select("tony_dialogue_pre")
    if not M_tony.is_set("deliver") and player.transport_level > 0:
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_first")
        $ M_tony.set("deliver", True)

    elif M_tony.is_set("deliver"):
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_repeat")
    else:
        call expression game.dialog_select("tony_dialogue_default")

    menu menu_tony_button:
        "Заказ Пиццы.":
            call expression game.dialog_select("tony_dialogue_pizza_order")
            menu:
                "Вегетарианская Пицца." if M_daisy.is_state(S_daisy_get_pizza):
                    call expression game.dialog_select("tony_dialogue_veggie_pizza_first")
                    if player.has_money(20):
                        call expression game.dialog_select("tony_dialogue_veggie_pizza_has_money_first")
                        $ player.get_item("veggie_pizza")
                        $ game.main()
                    else:
                        call expression game.dialog_select("tony_dialogue_veggie_pizza_no_money_first")
                        $ game.main()

                "Вегетарианская Пицца." if M_daisy.get("veggie pizza"):
                    call expression game.dialog_select("tony_dialogue_veggie_pizza_repeat")
                    if player.has_money(20):
                        call expression game.dialog_select("tony_dialogue_veggie_pizza_has_money_repeat")
                        $ player.get_item("veggie_pizza")
                        $ game.main()
                    else:
                        call expression game.dialog_select("tony_dialogue_veggie_pizza_no_money_repeat")
                        $ game.main()
                "Не важно.":

                    call expression game.dialog_select("tony_dialogue_nevermind_pizza_order")
                    $ game.main()
    hide player
    hide tony
    hide maria
    with dissolve
    hide xtra
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
