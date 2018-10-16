label sis_button_dialogue:
    if sis_panties_trade:
        if not sis_panties_bought:
            call expression game.dialog_select("jenny_dialogue_panties_trade_pre")
            if player.has_money(100):
                menu:
                    "Here's $100.":
                        $ player.spend_money(100)
                        $ player.get_item("panties")
                        $ sis_panty01.finish()
                        $ completed_quests.append(quest07)
                        $ sis_panties_bought = True
                        call expression game.dialog_select("jenny_dialogue_panties_trade_buy")
                    "I don't need it.":

                        call expression game.dialog_select("jenny_dialogue_panties_trade_do_not_buy")
            else:

                menu:
                    "I don't have enough.":
                        call expression game.dialog_select("jenny_dialogue_panties_trade_cant_buy")
            jump expression game.dialog_select("hallway_dialogue")
        else:

            call expression game.dialog_select("jenny_dialogue_pre")
            menu sis_bedroom_menu:
                "Talk.":
                    if not sister.over(sis_shower_cuddle02):
                        call expression game.dialog_select("jennybedroom_talk_after_cuddle")
                    else:
                        call expression game.dialog_select("jenny_dialogue_talk_before_cuddle")

                "I love you." if sister.over(sis_final2):
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

                "{b}[deb_name]{/b} needs you." if sis_panties_bought and not sis_diary_unlocked and sister.over(sis_shower_cuddle01) and sister.completed(sis_panty02):
                    call expression game.dialog_select("sis_bedroom_sis_mom_needs_you")
                    $ diary_scene = True
                    $ sis_diary_unlocked = True
                    $ M_jenny.place(place = L_NULL)
                    $ M_jenny.force(tod = [0,1])

                "Trade for panties." if not sister.completed(sis_panty04):
                    call expression game.dialog_select("jenny_dialogue_trade_panties")

                "Make a deal." if sister.over(sis_breakfast):
                    call expression game.dialog_select("jenny_dialogue_make_deal")
                    jump expression game.dialog_select("hallway_dialogue")

                "Cam show." if sister.known(sis_final2):
                    $ sis_cheerleader_sex2_menu = False
                    if sister.completed(sis_final2):
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
                        $ sis_final2.finish()
                        $ sister.add_event(sis_shower_cuddle05)
                        label sis_cheerleader_replay:
                            call expression game.dialog_select("jenny_dialogue_cam_show_have_items")
                        $ anim_toggle = False
                        $ xray = False
                        jump expression game.dialog_select("sis_cheerleader_fuck_looprep")

                "Need toys?" if sister.over(sis_shower_cuddle05) and not sister.completed(sis_webcam04):
                    if not sister.known(sis_webcam04):
                        call expression game.dialog_select("jenny_dialogue_need_toys")
                        $ sister.add_event(sis_webcam04)

                    elif not player.has_item("badmonster"):
                        call expression game.dialog_select("jenny_dialogue_need_toys_do_not_have_toys")

                    elif player.has_item("badmonster"):
                        call expression game.dialog_select("jenny_dialogue_need_toys_have_toys")
                        $ player.remove_item("badmonster")
                        $ sis_webcam04.finish()

                "Watch TV tonight." if sister.over(sis_final2) and not sis_watch_tv_tonight:
                    call expression game.dialog_select("jenny_dialogue_watch_tv_tonight")
                    $ sis_watch_tv_tonight = True
                    jump expression game.dialog_select("sis_bedroom_menu")

                "Watch the neighbors." if sister.over(sis_final2):
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
