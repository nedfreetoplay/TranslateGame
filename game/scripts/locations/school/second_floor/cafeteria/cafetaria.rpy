label cafeteria_dialogue:
    $ player.go_to(L_school_cafeteria)
    call pa_announcement
    if M_diane.is_state(S_diane_delivery_3_drop_off_goods):
        call expression game.dialog_select("cafeteria_diane_delivery_3_drop_off_goods")
        $ player.remove_item("milk_carton")
        $ M_diane.trigger(T_diane_delivery_3_finished)


    elif not erik.known(erik_favor) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_not_known")
        $ erik.add_event(erik_favor)

    elif erik.known(erik_favor) and not erik.completed(erik_favor_2) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_known")

    elif player.location.is_here(M_erik) and erik.completed(erik_favor_2):
        call expression game.dialog_select("cafeteria_erik_favor_2_completed")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
