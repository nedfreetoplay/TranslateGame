label mom_bedroom_screen:
    $ player.go_to(L_home_mombedroom)
    $ game.main()

label mom_bedroom:
    $ player.go_to(L_home_mombedroom)
    if game.timer.is_dark() and M_mom.is_state(S_mom_end) and M_diane.is_state(S_diane_risky_frisky_kinky) and not M_diane.pregnancy and not M_mom.pregnancy:
        call expression game.dialog_select("mom_bedroom_diane_risky_frisky_kinky")
        $ player.go_to(L_home_bedroom)
        $ M_diane.trigger(T_diane_debbie_caught)
        $ game.main()

    if M_diane.is_state(S_diane_end) and M_diane.get("refused 3way"):
        call expression game.dialog_select("mom_bedroom_diane_refused_3way")
        $ player.go_to(L_home_livingroom)
        $ game.main()

    if M_mom.is_state(S_mom_spy) and not game.timer.is_dark():
        call expression game.dialog_select("mom_spy")
        $ M_mom.trigger(T_mom_caught_spying)
        $ persistent.cookie_jar["Debbie"]["unlocked"] = True
        $ persistent.cookie_jar["Debbie"]["gallery"]["01_unlocked"] = True
        $ game.timer.tick()

    elif M_mom.is_state(S_mom_panties_masturbation_again):
        call expression game.dialog_select("moms_bedroom_mom_panties_masturbation_again")

    elif M_mom.is_state(S_mom_sleepover_wakeup):
        call expression game.dialog_select("moms_bedroom_mom_sleepover_makeup")
        $ M_mom.trigger(T_mom_sleepover_morning)
        $ player.go_to(L_home_livingroom)

    elif M_diane.is_state(S_diane_debbie_dinner_outfit):
        call expression game.dialog_select("moms_bedroom_mom_dinner_outfit")
        menu:
            "Ask {b}[deb_name]{/b}.":
                call expression game.dialog_select("moms_bedroom_mom_dinner_outfit_ask")
            "Just leave.":

                $ pass
        $ M_diane.trigger(T_diane_debbie_gave_dinner_outfit_advice)
        jump expression game.dialog_select("home_livingroom_dialogue")

    elif M_mom.is_state(S_mom_midnight_swim_after):
        $ player.go_to(L_home_livingroom)
        call expression game.dialog_select("moms_bedroom_mom_midnight_swim_after")

    elif game.timer.is_dark() and not L_home_mombedroom.is_here(M_diane):
        call expression game.dialog_select("moms_bedroom_night")

    elif not M_mom.is_set("fetch lotion") and not M_mom.is_set("sleep together"):
        call expression game.dialog_select("moms_bedroom_mom_is_set_lotion")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
