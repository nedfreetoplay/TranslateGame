label police_office_dialogue:
    $ player.go_to(L_police_office)
    if L_police_office.first_visit and player.location.is_here(M_harold):
        call expression game.dialog_select("police_office_first_visit_pre")
        menu:
            "Где {b}Мия{/b}?":
                call expression game.dialog_select("police_office_first_visit_wheres_mia")
                $ L_police_office.visited()

    elif M_mia.is_set("questioned yumi") and M_mia.is_set("questioned earl"):
        call expression game.dialog_select("police_office_mia_clues_summary")
        $ M_mia.trigger(T_mia_clues_summary)

    elif M_mia.is_state(S_mia_harold_gift):
        call expression game.dialog_select("police_office_mia_harold_gift")
        $ player.remove_item("aviators")

        $ M_mia.trigger(T_harold_glasses)

    elif M_mia.is_state(S_mia_convince_harold):
        call expression game.dialog_select("police_office_mia_convince_harold_pre")
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_convince_harold_pre_erik_thief")
        else:

            call expression game.dialog_select("police_office_mia_convince_harold_pre_no_erik_thief")

        call expression game.dialog_select("police_office_mia_convince_harold_mid")
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_convince_harold_mid_erik_thief")
        else:

            call expression game.dialog_select("police_office_mia_convince_harold_mid_no_erik_thief")

        call expression game.dialog_select("police_office_mia_convince_harold_after")
        $ M_mia.trigger(T_harold_find_goods)

    elif M_mia.is_state(S_mia_return_goods):
        call expression game.dialog_select("police_office_mia_return_goods_pre")
        if erik.over(erik_thief):
            call expression game.dialog_select("police_office_mia_return_goods_pre_erik_thief")
        else:

            call expression game.dialog_select("police_office_mia_return_goods_pre_no_erik_thief")

        call expression game.dialog_select("police_office_mia_return_goods_after")
        $ M_mia.trigger(T_harold_promotion)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
