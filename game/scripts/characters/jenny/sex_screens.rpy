screen jenny_jenny_bed_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_jenny_bed_sex_options"), Jump("jenny_jenny_bed_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_jenny_bed_sex_options"), Jump("jenny_jenny_bed_sex_cum_outside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_jenny_bed_sex_options"), Jump("jenny_jenny_bed_sex_cum_inside")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_jenny_bed_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_jenny_bed_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_jenny_bed_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_jenny_bed_sex_loop")
            xpos 450
            ypos 735

screen jenny_pool_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_pool_sex_options"), Jump("jenny_pool_sex_loop")
        xpos 50
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_pool_sex_options"), Jump("jenny_pool_sex_cum_inside")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_pool_sex_options"), Jump("jenny_pool_sex_cum_outside")
        xpos 450
        ypos 700

    imagebutton:
        focus_mask True
        idle "sexb_changeoutfit_n"
        hover "sexb_changeoutfit_h"
        action Hide("jenny_pool_sex_options"), Function(M_jenny.toggle, "pool_clothes"), SetVariable("animated", False), Jump("jenny_pool_sex_loop")
        xpos 650
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_pool_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_pool_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_pool_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_pool_sex_loop")
            xpos 450
            ypos 735

screen jenny_diningroom_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_diningroom_sex_options"), Jump("jenny_diningroom_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_diningroom_sex_options"), Jump("jenny_diningroom_sex_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_diningroom_sex_options"), Jump("jenny_diningroom_sex_cum_outside")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_diningroom_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_diningroom_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_diningroom_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_diningroom_sex_loop")
            xpos 450
            ypos 735

screen jenny_couch_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_couch_sex_options"), Jump("jenny_couch_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_couch_sex_options"), Jump("jenny_couch_sex_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_couch_sex_options"), Jump("jenny_couch_sex_cum_outside")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_couch_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_couch_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_couch_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_couch_sex_loop")
            xpos 450
            ypos 735

screen jenny_shower_bj_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_shower_bj_options"), Jump("jenny_shower_bj_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("jenny_shower_bj_options"), Jump("jenny_shower_bj_cum")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("jenny_shower_bj_options"), Function(M_jenny.toggle, "jenny_bj_deep"), SetVariable("animated", False), Jump("jenny_shower_bj_loop")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .14 and not M_jenny.get("jenny_bj_deep"):
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_shower_bj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.025), Jump("jenny_shower_bj_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .091 and not M_jenny.get("jenny_bj_deep"):
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_shower_bj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.025), Jump("jenny_shower_bj_loop")
            xpos 450
            ypos 735

screen jenny_shower_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_shower_sex_options"), Jump("jenny_shower_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_shower_sex_options"), Jump("jenny_shower_sex_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_shower_sex_options"), Jump("jenny_shower_sex_cum_outside")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_shower_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_shower_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_shower_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_shower_sex_loop")
            xpos 450
            ypos 735

screen jenny_hj_options():
    if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("jenny_hj_options"), Jump("jenny_hj_loop")
            xpos 150
            ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_02.png"
            hover HoverImage("buttons/judith_stage02_02.png")
            action Hide("jenny_hj_options"), Jump("jenny_hj_cum")
            xpos 350
            ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/jenny_mask_on_off.png"
            hover HoverImage("buttons/jenny_mask_on_off.png")
            action Hide("jenny_hj_options"), Function(M_jenny.toggle, "cam show mask"), Jump("jenny_hj_loop")
            xpos 550
            ypos 700

    else:
        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("jenny_hj_options"), Jump("jenny_hj_loop")
            xpos 250
            ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_02.png"
            hover HoverImage("buttons/judith_stage02_02.png")
            action Hide("jenny_hj_options"), Jump("jenny_hj_cum")
            xpos 450
            ypos 700

    if M_jenny.get('sex speed') < .1:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_hj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.025), Jump("jenny_hj_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .051:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_hj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.025), Jump("jenny_hj_loop")
            xpos 450
            ypos 735

screen jenny_bj_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_bj_options"), Jump("jenny_bj_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_bj_options"), Jump("jenny_bj_cum")

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_bj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_bj_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_bj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_bj_loop")
            xpos 450
            ypos 735

screen jenny_couch_fj_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_couch_fj_options"), Jump("jenny_couch_fj_loop")
        if not M_jenny.get("couch_sex_first") or M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            xpos 150
            ypos 700
        else:
            xpos 250
            ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_02.png"
        hover HoverImage("buttons/judith_stage02_02.png")
        action Hide("jenny_couch_fj_options"), Jump("jenny_couch_fj_cum")
        if not M_jenny.get("couch_sex_first") or M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            xpos 350
            ypos 700
        else:
            xpos 450
            ypos 700

    if not M_jenny.get("couch_sex_first") or M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_07.png"
            hover HoverImage("buttons/diane_stage01_07.png")
            action Hide("jenny_couch_fj_options"), Jump("jenny_couch_sex")
            xpos 550
            ypos 700

    if M_jenny.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_couch_fj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.075), Jump("jenny_couch_fj_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .151:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_couch_fj_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.075), Jump("jenny_couch_fj_loop")
            xpos 450
            ypos 735

screen jenny_lick_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_lick_options"), Jump("jenny_lick_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("jenny_lick_options"), Jump("jenny_lick_cum")
        xpos 450
        ypos 700

    if M_jenny.get('sex speed') < .2:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_lick_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.025), Jump("jenny_lick_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .151:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_lick_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.025), Jump("jenny_lick_loop")
            xpos 450
            ypos 735

screen jenny_cheer_sex_options_tied():
    if M_jenny.get("dominance") <= 0 and not _in_replay and not M_jenny.finished_inclusive(S_jenny_end):
        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_loop_tied")
            xpos 150
            ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_cum_inside_tied")
            xpos 350
            ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_03.png"
            hover HoverImage("buttons/diane_stage01_03.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_cum_outside_tied")
            xpos 550
            ypos 700
    else:
        imagebutton:
            focus_mask True
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_loop_tied")
            if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
                xpos 0
                ypos 700
            else:
                xpos 50
                ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_cum_inside_tied")
            if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
                xpos 200
                ypos 700
            else:
                xpos 250
                ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/diane_stage01_03.png"
            hover HoverImage("buttons/diane_stage01_03.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_cum_outside_tied")
            if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
                xpos 400
                ypos 700
            else:
                xpos 450
                ypos 700

        imagebutton:
            focus_mask True
            idle "buttons/jenny_break_01.png"
            hover HoverImage("buttons/jenny_break_01.png")
            action Hide("jenny_cheer_sex_options_tied"), Jump("jenny_cheer_sex_break_free")
            if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
                xpos 600
                ypos 700
            else:
                xpos 650
                ypos 700

        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            imagebutton:
                focus_mask True
                idle "buttons/jenny_mask_on_off.png"
                hover HoverImage("buttons/jenny_mask_on_off.png")
                action Hide("jenny_cheer_sex_options_tied"), Function(M_jenny.toggle, "cam show mask"), SetVariable("animated", False), Jump("jenny_cheer_sex_loop_tied")
                xpos 800
                ypos 700

    if M_jenny.get('sex speed') < .09:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_cheer_sex_options_tied"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_cheer_sex_loop_tied")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .031:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_cheer_sex_options_tied"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_cheer_sex_loop_tied")
            xpos 450
            ypos 735

screen jenny_cheer_sex_options_free():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_cheer_sex_options_free"), Jump("jenny_cheer_sex_loop_free")
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            xpos 50
            ypos 700
        else:
            xpos 150
            ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_cheer_sex_options_free"), Jump("jenny_cheer_sex_cum_inside_free")
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            xpos 250
            ypos 700
        else:
            xpos 350
            ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_cheer_sex_options_free"), Jump("jenny_cheer_sex_cum_outside_free")
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
            xpos 450
            ypos 700
        else:
            xpos 550
            ypos 700

    if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay is not None:
        imagebutton:
            focus_mask True
            idle "buttons/jenny_mask_on_off.png"
            hover HoverImage("buttons/jenny_mask_on_off.png")
            action Hide("jenny_cheer_sex_options_free"), Function(M_jenny.toggle, "cam show mask"), SetVariable("animated", False), Jump("jenny_cheer_sex_loop_free")
            xpos 650
            ypos 700

    if M_jenny.get('sex speed') < .08:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_cheer_sex_options_free"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.01), Jump("jenny_cheer_sex_loop_free")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_cheer_sex_options_free"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.01), Jump("jenny_cheer_sex_loop_free")
            xpos 450
            ypos 735

screen jenny_mc_room_sex_options():
    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("jenny_mc_room_sex_options"), Jump("jenny_mc_room_sex_loop")
        xpos 150
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("jenny_mc_room_sex_options"), Jump("jenny_mc_room_sex_cum_inside")
        xpos 350
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("jenny_mc_room_sex_options"), Jump("jenny_mc_room_sex_cum_outside")
        xpos 550
        ypos 700

    if M_jenny.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("jenny_mc_room_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") + 0.03), Jump("jenny_mc_room_sex_loop")
            xpos 250
            ypos 735

    if M_jenny.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("jenny_mc_room_sex_options"), Function(M_jenny.set, "sex speed", M_jenny.get("sex speed") - 0.03), Jump("jenny_mc_room_sex_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
