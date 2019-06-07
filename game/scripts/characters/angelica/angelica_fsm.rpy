init python:

    T_angelica_house_visit = Trigger("house visit", "Angelica pays your house a visit")
    T_angelica_ritual_deal = Trigger("ritual deal", "Angelica makes you agree to her ritual deal")
    T_angelica_requires_whip = Trigger("requires whip", "Angelica requires a whip for her next sacrement")
    T_angelica_sinful_thoughts = Trigger("sinful thoughts", "Angelica says she will punish you if you have sinful thoughts")
    T_angelica_strapon_request = Trigger("strapon request", "Angelica's final sacrament requires a special tool")
    T_angelicas_final_ritual = Trigger("final ritual", "Angelica's final sacrament shall now begin")

label angelica_fsm_init:
    python:
        S_angelica_start = State("angelica start")

        M_angelica.add(S_angelica_start) 
    return

label angelica_machine_init:
    python:
        M_angelica = Machine("angelica", default_loc=[[L_church, L_church, L_church_angelica, L_church_angelica], 
                            [L_NULL, L_church, L_church_angelica, L_church_angelica]],
                            vars={'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
