label mias_house_dialogue:
    $ player.go_to(L_miahouse)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_morning() and not game.timer.is_weekend():
        call expression game.dialog_select("mias_house_is_morning")

    elif M_mia.get_state() == S_mia_concerning_visit and game.timer.is_afternoon():
        call expression game.dialog_select("mias_house_mia_concerning_visit")

        $ M_mia.trigger(T_harold_leaves)

    elif game.timer.is_evening() and M_mia.is_set('front door locked'):
        call expression game.dialog_select("mias_house_front_door_locked")
    $ game.main()

label mias_mailbox_dialogue:
    if game.mail["mia"] == "m_pizza_pamphlet":
        call expression game.dialog_select("mia_mailbox_pizza_pamphlet")
        $ L_pizzeria_exterior.unlock()
        $ L_dealership_front.unlock()
    elif game.mail["mia"] == "m_newspaper":
        call expression game.dialog_select("mia_mailbox_newspaper")
    call screen mias_mailbox
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
