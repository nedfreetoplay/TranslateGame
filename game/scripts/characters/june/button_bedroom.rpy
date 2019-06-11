label june_bedroom_dialogue:
    $ game.timer.tick()
    $ june_hang_out = False
    if June.in_progress(june_cosplay):
        label june_cosplay_replay:
            call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_pre")
        call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro")
        $ anim_toggle = True
        $ animated = False
        $ xray = False
        $ M_june.set("sex speed", .3)
        jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")
    else:

        scene bedroom_sex2
        if June.over(june_cosplay):
            call expression game.dialog_select("june_bedroom_dialogue_sex_pre_cosplay")
        else:

            call expression game.dialog_select("june_bedroom_dialogue_sex_pre_no_cosplay")
        menu:
            "Секс!" if June.over(june_cosplay):
                call expression game.dialog_select("june_bedroom_dialogue_sex_normal_pre")
                call expression game.dialog_select("june_bedroom_dialogue_normal_sex_intro")
                $ anim_toggle = True
                $ animated = False
                $ xray = False
                $ M_june.set("sex speed", .3)
                jump expression game.dialog_select("june_bedroom_dialogue_normal_sex_loop")

            "Косплейный секс!" if June.over(june_cosplay):
                call expression game.dialog_select("june_bedroom_dialogue_sex_cosplay_pre")
                call expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_intro")
                $ anim_toggle = True
                $ animated = False
                $ xray = False
                $ M_june.set("sex speed", .3)
                jump expression game.dialog_select("june_bedroom_dialogue_cosplay_sex_loop")
            "Играть в игры.":

                if June.over(june_cosplay):
                    call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_over")
                else:

                    call expression game.dialog_select("june_bedroom_dialogue_play_games_cosplay_not_over")
                jump expression game.dialog_select("orc_battle_start")
            "Мне нужно поспать.":

                $ tmp_deb_name = deb_name.capitalize()
                call expression game.dialog_select("june_bedroom_dialogue_leave")
                $ del tmp_deb_name
                jump expression game.dialog_select("sleeping")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
