label helen_button_dialogue:
    if M_helen.is_state(S_helen_master_servant_fun):
        jump expression game.dialog_select("helen_bedroom_sex")

    scene expression game.timer.image("mia_house_helen_c{}")
    if M_mia.is_set("mia route"):
        call expression game.dialog_select("helen_dialogue_mia_route")

    elif M_helen.is_state(S_helen_end):
        call expression game.dialog_select("helen_dialogue_helen_end_intro")
        menu:
            "Purify your body.":
                call expression game.dialog_select("helen_dialogue_helen_end_sex")
                $ M_helen.set("sex speed", .175)
                jump expression game.dialog_select("helen_bedroom_sex_start")
            "Another time.":

                call expression game.dialog_select("helen_dialogue_helen_end_leave")

    elif M_mia.is_set("helen dialogue change"):
        call expression game.dialog_select("helen_dialogue_change_intro")
        menu:
            "{b}Harold{/b}." if not M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_harold")

            "{b}Harold{/b}." if M_mia.is_state(S_mia_clues):
                call expression game.dialog_select("helen_dialogue_change_mia_clues")

            "Corset." if M_mia.is_state(S_mia_helen_outfit_request):
                call expression game.dialog_select("helen_dialogue_change_corset")

            "Angelica." if M_mia.is_set('helen angelica training'):
                call expression game.dialog_select("helen_dialogue_change_angelica")

            "Whipping." if M_mia.is_state(S_mia_helen_condition):
                call expression game.dialog_select("helen_dialogue_change_whipping")
                $ M_mia.trigger(T_helen_thanks)

            "Ritual." if M_mia.is_state(S_mia_find_sinners):
                call expression game.dialog_select("helen_dialogue_change_ritual")
                menu:
                    "I don't know." if player.stats.chr() < 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_fail")

                    "Ancient sacrament." if player.stats.chr() >= 5:
                        call expression game.dialog_select("helen_dialogue_change_ritual_stat_pass")
                        $ M_mia.trigger(T_helen_secret_sacrement)

    elif M_mia.is_set("helen button"):
        call expression game.dialog_select("helen_dialogue_intro")
        menu helen_dialogue:
            "{b}Harold{/b}.":
                call expression game.dialog_select("helen_dialogue_harold")
    else:

        call expression game.dialog_select("helen_dialogue_leave")
    hide player
    hide helen
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
