label check_pregnancies:
    call _check_all_pregnancies
    return

label _check_all_pregnancies:
    python hide:
        preggos = pregnant_machines()
        store.pregnant_machines_read = []
        if len(preggos) > 0:
            for preggo in preggos:
                if not game.new_message:
                    if preggo.pregnancy.stage == 1:
                        preggo.pregnancy.text_announcement_seen = True
                    if preggo.pregnancy.stage == 5:
                        preggo.pregnancy.text_labor_seen = True
                if preggo.pregnancy.text_announcement_seen and preggo.pregnancy.stage == 1 and not preggo.pregnancy.announced_pregnancy:
                    renpy.call("{}_pregnant_announcement_2".format(preggo._name))
                elif not preggo.pregnancy.text_announcement_seen and preggo.pregnancy.stage == 1 and not preggo.pregnancy.announced_pregnancy:
                    renpy.call("{}_pregnant_announcement_1".format(preggo._name))
                    preggo.pregnancy.text_announcement_seen = True
                elif preggo.pregnancy.text_labor_seen and preggo.pregnancy.stage == 5 and not preggo.pregnancy.seen_in_labor:
                    renpy.call("call_pregnant_labor_2", preggo._name)
                elif not preggo.pregnancy.text_labor_seen and preggo.pregnancy.stage == 5 and not preggo.pregnancy.seen_in_labor:
                    renpy.call("{}_pregnant_labor_1".format(preggo._name))
                    preggo.pregnancy.text_labor_seen = True
    return

label call_pregnant_labor_2(name):
    call expression "{}_pregnant_labor_2".format(name)
    $ L_hospital.unlock()
    $ L_annie_front.unlock()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
