label library_dialogue:
    $ player.go_to(L_library)
    if getPlayingSound("<loop 9 to 83>audio/ambience_library.ogg"):
        $ playSound("<loop 9 to 83>audio/ambience_library.ogg", 1.0)

    if M_jane.is_state(S_jane_intro):
        call expression game.dialog_select("library_jane_intro")

    if M_diane.is_state(S_diane_increase_milk_production):
        call expression game.dialog_select("library_diane_production_ask_librarian")

    elif M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("library_bissette_find_poem_reference_book")

    elif M_ross.is_state(S_ross_find_magazines) and not M_ross.get("talked with jane"):
        call expression game.dialog_select("library_ross_find_magazines")
    $ game.main()

label library_bookshelf:
    $ player.go_to(L_library_bookshelf)
    $ player.location.call_screen(ui = False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
