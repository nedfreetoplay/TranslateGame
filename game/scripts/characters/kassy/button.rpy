label kass_dialogue:
    scene location_mall_cupid_blur
    if kassy_first_visit:
        $ kassy_first_visit = False
        call expression game.dialog_select("kassy_first_visit")
    else:

        call expression game.dialog_select("kassy_repeat")

    hide kassy
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
