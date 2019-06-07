label cupid_dialogue:
    $ player.go_to(L_cupid)
    if M_mom.is_state(S_mom_cupid_store):
        call expression game.dialog_select("cupid_mom_cupid_store")
        $ M_mom.trigger(T_mom_cupid_arrival)
    if M_daisy.is_state(S_daisy_get_new_flowers):
        call expression game.dialog_select("cupid_daisy_get_new_flowers")
    $ game.main()

label cupid_jewelery_display:
    scene expression player.location.background_blur
    if M_mom.is_state(S_mom_show_necklace, S_mom_dressing_room):
        jump mom_cupid_outing_block
    elif M_mom.is_state(S_mom_choose_gift):
        call expression game.dialog_select("necklace_display_mom_choose_gift")
        $ M_mom.trigger(T_mom_pick_necklace)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
