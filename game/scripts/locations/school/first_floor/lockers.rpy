label annies_locker_dialogue:
    call locker_check ("right", L_school_locker_annie)
    if not L_school_locker_annie.is_visited:
        call expression game.dialog_select("annie_locker_first_visit")
        $ L_school_locker_annie.visited()
    $ player.go_to(L_school_locker_annie)
    $ player.location.call_screen(False)

label dexters_locker_dialogue:
    call locker_check ("right", L_school_locker_dexter)
    if M_bissette.is_set("dexters book search"):
        call expression game.dialog_select("dexter_locker_first_visit")
        python:
            for image in renpy.get_showing_tags():
                renpy.hide(image)
        call screen dexters_locker
        $ player.get_item("quick_mafs")
        call expression game.dialog_select("dexter_locker_book_found")

        if M_bissette.is_state(S_bissette_jane_return_books):
            call expression game.dialog_select("bissette_book_search_2_books_left")
        elif M_bissette.is_state([S_bissette_got_dexters_book, S_bissette_got_eriks_book, S_bissette_got_martinez_book]):
            call expression game.dialog_select("bissette_book_search_1_book_left")
        else:
            call expression game.dialog_select("bissette_book_search_no_books_left")
        $ M_bissette.trigger(T_bissette_ask_dexter)
        $ game.main()

    elif not L_school_locker_dexter.is_visited:
        call expression game.dialog_select("dexter_locker_first_visit")
        $ L_school_locker_dexter.visited()
    $ player.go_to(L_school_locker_dexter)
    $ player.location.call_screen(False)

label eriks_locker_dialogue:
    call locker_check ("right", L_school_locker_erik)
    if not L_school_locker_erik.is_visited:
        call expression game.dialog_select("erik_locker_first_visit")
        $ L_school_locker_erik.visited()
    $ player.go_to(L_school_locker_erik)
    $ player.location.call_screen(False)

label eves_locker_dialogue:
    call locker_check ("right", L_school_locker_eve)
    if not L_school_locker_eve.is_visited:
        call expression game.dialog_select("eve_locker_first_visit")
        $ L_school_locker_eve.visited()
    $ player.go_to(L_school_locker_eve)
    $ player.location.call_screen(False)

label judiths_locker_dialogue:
    call locker_check ("left", L_school_locker_judith)
    if not L_school_locker_judith.is_visited:
        call expression game.dialog_select("judith_locker_first_visit")
        $ L_school_locker_judith.visited()
    $ player.go_to(L_school_locker_judith)
    $ player.location.call_screen(False)

label kevins_locker_dialogue:
    call locker_check ("right", L_school_locker_kevin)
    if not L_school_locker_kevin.is_visited:
        call expression game.dialog_select("kevin_locker_first_visit")
        $ L_school_locker_kevin.visited()
    $ player.go_to(L_school_locker_kevin)
    $ player.location.call_screen(False)

label mias_locker_dialogue:
    call locker_check ("right", L_school_locker_mia)
    if not L_school_locker_mia.is_visited:
        call expression game.dialog_select("mia_locker_first_visit")
        if M_mia.between_states(S_mia_start, S_mia_need_space):
            call expression game.dialog_select("mia_locker_first_visit_early_route")

        elif M_mia.between_states(S_mia_concerning_visit, S_mia_route_split):
            call expression game.dialog_select("mia_locker_first_visit_helping_parents")

        elif M_helen.get("helen route"):
            call expression game.dialog_select("mia_locker_first_visit_helen_route")
        $ L_school_locker_mia.visited()
    $ player.go_to(L_school_locker_mia)
    $ player.location.call_screen(False)

label rondas_locker_dialogue:
    call locker_check ("right", L_school_locker_ronda)
    if not L_school_locker_ronda.is_visited:
        call expression game.dialog_select("ronda_locker_first_visit")
        $ L_school_locker_ronda.visited()
    $ player.go_to(L_school_locker_ronda)
    $ player.location.call_screen(False)

label roxxys_locker_dialogue:
    call locker_check ("left", L_school_locker_roxxy)
    if not L_school_locker_roxxy.is_visited:
        call expression game.dialog_select("roxxy_locker_first_visit")
        $ L_school_locker_roxxy.visited()
    $ player.go_to(L_school_locker_roxxy)
    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
