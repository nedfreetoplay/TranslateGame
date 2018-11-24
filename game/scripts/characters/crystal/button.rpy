label roxmom_dialogue:
    scene expression game.timer.image("trailer_interior_c{}")
    if M_crystal.is_state(S_crystal_start):
        $ M_crystal.trigger(T_crystal_intro)

    if M_roxxy.is_state(S_roxxy_picnic_done):
        call expression game.dialog_select("button_crystal_roxxy_go_to_picnic")
    else:
        if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call expression game.dialog_select("button_crystal_rox8_11_evening")
            else:
                call expression game.dialog_select("button_crystal_rox8_11_day")
        elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            if game.timer.is_dark():
                call expression game.dialog_select("button_crystal_final_evening")
            else:
                call expression game.dialog_select("button_crystal_final_day")
        else:
            call expression game.dialog_select("button_crystal_preamble")
    show crystal 1
    menu roxmom_dialogue_repeat:
        "Где {b}Рокси{/b}?" if not game.timer.is_dark():
            if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_rox8_rox11")
            elif M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
                call expression game.dialog_select("button_crystal_roxxy_final")
            else:
                call expression game.dialog_select("button_crystal_roxxy")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Так вы мама {b}Рокси{/b}?" if not game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxys_mom")

        "А {b}Рокси{/b} занята?" if game.timer.is_dark() and M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_roxxy_busy")

        "Да, она действительно здесь?" if game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_she_here")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Вы счастливы быть дома?" if not game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_happy_home")
            jump expression game.dialog_select("roxmom_dialogue_repeat")
        "{b}Отец Рокси{/b}.":

            call expression game.dialog_select("button_crystal_roxxys_dad")
            jump expression game.dialog_select("roxmom_dialogue_repeat")

        "Предлагать." if M_crystal.is_set("crystal sex offer") and not M_roxxy.get("roxxy crystal sex"):
            call expression game.dialog_select("trailer_interior_crystal_sex_offer_pre_repeat")
            jump expression game.dialog_select("trailer_interior_crystal_sex_offer_menu")

        "Халтура." if M_roxxy.get("roxxy crystal sex") and L_trailer.is_here(M_crystal):
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_pre")
            jump expression game.dialog_select("trailer_interior_crystal_sex_repeat_outside_offer_menu")

        "Халтура." if M_roxxy.get("roxxy crystal sex") and L_trailer_interior.is_here(M_crystal):
            label crystal_hscene_replay:
                if not store._in_replay == None:
                    scene expression game.timer.image("trailer_interior_c{}")
                    show player 11 at left
                    show crystal 2 at right
                    with dissolve
            call expression game.dialog_select("trailer_interior_crystal_sex_repeat_inside")
            call expression game.dialog_select("trailer_interior_crystal_sex_or_anal_menu")
            $ anim_toggle = True
            jump expression game.dialog_select("trailer_interior_crystal_sex_loop")

        "Извините за беспокойство." if M_roxxy.between_states(S_roxxy_assignment_delay, S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_sorry_to_bother")

        "Я должен идти." if game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_should_go_evening")

        "Я должен идти." if not game.timer.is_dark() and M_roxxy.finished_state(S_roxxy_hows_it_going_delay):
            call expression game.dialog_select("button_crystal_should_go_day")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
