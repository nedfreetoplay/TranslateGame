label sis_button_dialogue:
    call expression game.dialog_select("jenny_dialogue_pre")
    menu sis_bedroom_menu:
        "Talk.":
            if not M_jenny.finished_state(S_jenny_shower_peep_bed_cuddle_tier_2):
                call expression game.dialog_select("jennybedroom_talk_after_cuddle")
            else:
                call expression game.dialog_select("jenny_dialogue_talk_before_cuddle")

        "I love you." if M_jenny.finished_state(S_jenny_cam_show):
            if sis_confession_first:
                call expression game.dialog_select("jenny_dialogue_confess_first")
                $ sis_confession_first = False
            else:

                call expression game.dialog_select("jenny_dialogue_confess_repeat")
            jump expression game.dialog_select("hallway_dialogue")

        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Pay" if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Don't Pay":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")

        "{b}[deb_name]{/b} needs you." if M_jenny.is_state(S_jenny_debbie_needs_jenny):
            call expression game.dialog_select("sis_bedroom_sis_mom_needs_you")
            $ M_jenny.trigger(T_jenny_tricked)

        "Trade for panties." if not M_jenny.finished_state(S_jenny_panty_deal_tier_4):
            call expression game.dialog_select("jenny_dialogue_trade_panties")

        "Make a deal." if M_jenny.finished_state(S_jenny_breakfast):
            call expression game.dialog_select("jenny_dialogue_make_deal")
            jump expression game.dialog_select("hallway_dialogue")

        "Cam show." if M_jenny.between_states(S_jenny_cam_show, S_jenny_end):
            $ sis_cheerleader_sex2_menu = False
            if not M_jenny.is_state(S_jenny_cam_show):
                $ game.timer.tick()
                $ anim_toggle = False
                $ xray = False
                call expression game.dialog_select("jenny_dialogue_cam_show_pre")
                if sis_final_cum == "Inside" and sis_final_cum_inside_first:
                    call expression game.dialog_select("jenny_dialogue_cam_show_pre_inside")
                    $ sis_final_cum_inside_first = False

                elif sis_final_cum == "Outside":
                    call expression game.dialog_select("jenny_dialogue_cam_show_pre_outside")
                call expression game.dialog_select("jenny_dialogue_cam_show_pre_after")
                jump expression game.dialog_select("sis_cheerleader_fuck_looprep")

            elif not player.has_item("handcuffs") or not player.has_item("cheerleader_outfit"):
                call expression game.dialog_select("jenny_dialogue_cam_show_no_items")
                jump expression game.dialog_select("hallway_dialogue")

            elif player.has_item("handcuffs") and player.has_item("cheerleader_outfit"):
                $ game.timer.tick()
                $ player.remove_item("handcuffs")
                $ player.remove_item("cheerleader_outfit")
                $ M_jenny.trigger(T_jenny_stream_ready)
                label sis_cheerleader_replay:
                    call expression game.dialog_select("jenny_dialogue_cam_show_have_items")
                $ anim_toggle = False
                $ xray = False
                jump expression game.dialog_select("sis_cheerleader_fuck_looprep")

        "Need toys?" if M_jenny.is_state(S_jenny_help_stream_tier_4, S_jenny_prepare_stream_tier_4):
            if M_jenny.is_state(S_jenny_help_stream_tier_4):
                call expression game.dialog_select("jenny_dialogue_need_toys")
                $ M_jenny.trigger(T_jenny_need_toys)

            elif not player.has_item("badmonster"):
                call expression game.dialog_select("jenny_dialogue_need_toys_do_not_have_toys")

            elif player.has_item("badmonster"):
                call expression game.dialog_select("jenny_dialogue_need_toys_have_toys")
                $ player.remove_item("badmonster")
                $ M_jenny.trigger(T_jenny_brought_toys)

        "Watch TV tonight." if M_jenny.finished_state(S_jenny_cam_show) and not sis_watch_tv_tonight:
            call expression game.dialog_select("jenny_dialogue_watch_tv_tonight")
            $ sis_watch_tv_tonight = True
            jump expression game.dialog_select("sis_bedroom_menu")

        "Watch the neighbors." if M_jenny.finished_state(S_jenny_cam_show):
            $ game.timer.tick()
            call expression game.dialog_select("jenny_dialogue_watch_neighbours")
            call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue01")
            label neighbors_spy_replay:
                call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue02")
            $ persistent.cookie_jar["Mrs Johnson"]["unlocked"] = True
            $ persistent.cookie_jar["Mrs Johnson"]["gallery"]["03_unlocked"] = True
            call expression game.dialog_select("jenny_dialogue_watch_neighbours_continue03")
            $ anim_toggle = False
            $ xray = False
            call expression game.dialog_select("jenny_dialogue_watch_neighbours_menu")
            jump expression game.dialog_select("bedroom_dialogue")
    hide player
    hide jenny
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
