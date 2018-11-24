label angelica_triggers_init:
    python:

        T_angelica_house_visit = Trigger("house visit", "Анжелика приходит к вам дом")
        T_angelica_ritual_deal = Trigger("ritual deal", "Анжелика заставляет Вас согласиться на её ритуальную сделку")
        T_angelica_requires_whip = Trigger("requires whip", "Анжелика требует хлыст для её следующего причастия")
        T_angelica_sinful_thoughts = Trigger("sinful thoughts", "Анжелика говорит, что накажет вас, если у вас есть греховные мысли")
        T_angelica_strapon_request = Trigger("strapon request", "Последнее причастие Анжелики требует специального инструмента")
        T_angelicas_final_ritual = Trigger("final ritual", "Последнее причастие Анжелики начинается")
    return

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
