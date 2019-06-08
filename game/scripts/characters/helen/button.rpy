label helen_button_dialogue:
    if M_helen.is_state(S_helen_master_servant_fun):
        jump expression game.dialog_select("helen_bedroom_sex")

    scene expression game.timer.image("mia_house_helen_c{}")
    if M_mia.is_set("mia route"):
        call expression game.dialog_select("helen_dialogue_mia_route")

    elif M_helen.is_state(S_helen_end):
        call expression game.dialog_select("helen_dialogue_helen_end_intro")
        menu:
            "Очисти своё тело.":
                call expression game.dialog_select("helen_dialogue_helen_end_sex")
                $ M_helen.set("sex speed", .175)
                jump expression game.dialog_select("helen_bedroom_sex_start")
            "В другой раз.":

                call expression game.dialog_select("helen_dialogue_helen_end_leave")

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("helen_dialogue_change_intro")
        menu:
            "{b}Гарольд{/b}." if not M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_harold")

            "{b}Гарольд{/b}." if M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_mia_clues")

            "Корсет." if M_mia.is_state(S_mia_helen_outfit_request):
                call expression game.dialog_select("helen_dialogue_change_corset")

            "Анжелика." if M_mia.is_set('helen angelica training'):
                call expression game.dialog_select("helen_dialogue_change_angelica")

            "Порка." if M_mia.is_state(S_mia_helen_condition):
                call expression game.dialog_select("helen_dialogue_change_whipping")
                $ M_mia.trigger(T_helen_thanks)

            "Ритуал." if M_mia.is_state(S_mia_find_sinners):
                call expression game.dialog_select("helen_dialogue_change_ritual")
                menu:
                    "Я не знаю." if player.stats.chr() < 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_fail")

                    "Древние таинства." if player.stats.chr() >= 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_pass")
                        $ M_mia.trigger(T_helen_secret_sacrement)

    elif M_mia.is_set("helen button"):
        call expression game.dialog_select("helen_dialogue_intro")
        menu helen_dialogue:
            "{b}Гарольд{/b}.":
                call expression game.dialog_select("helen_dialogue_harold")
    else:

        call expression game.dialog_select("helen_dialogue_leave")
    hide player
    hide helen
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
