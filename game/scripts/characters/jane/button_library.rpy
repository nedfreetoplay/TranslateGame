label library_desk_dialogue:
    scene librarydesk
    if M_bissette.is_state(S_bissette_find_dictionary):
        call expression game.dialog_select("jane_library_dialogue_bissette_find_dictionary")
        $ M_bissette.trigger(T_bissette_check_library)

    elif M_bissette.is_state(S_bissette_get_dictionary) and player.has_item("french_dictionary"):
        call expression game.dialog_select("jane_library_dialogue_bissette_get_dictionary")
        $ M_bissette.trigger(T_bissette_check_library_shelf)


    elif M_bissette.is_state(S_bissette_return_overdue_books):
        call expression game.dialog_select("jane_library_dialogue_bissette_return_overdue_books")
        $ M_bissette.trigger(T_bissette_return_books)
        $ player.remove_item("oedipuss")
        $ player.remove_item("quick_mafs")
        $ player.remove_item("cholas_tricks")
    else:

        call expression game.dialog_select("jane_library_dialogue_pre")
        menu:
            "Книга по производству молока." if M_diane.is_state(S_diane_increase_milk_production):
                call expression game.dialog_select("jane_library_dialogue_production_ask_librarian")
                $ M_diane.trigger(T_diane_find_production_book)

            "Французская поэзия." if M_bissette.is_state(S_bissette_find_poem_reference_book):
                call expression game.dialog_select("jane_library_dialogue_french_poetry")

            "Французская еда." if M_bissette.between_states(S_bissette_find_food_book, [S_bissette_got_dexters_martinez_books, S_bissette_got_dexters_eriks_books,
                                                                                   S_bissette_got_eriks_dexters_books, S_bissette_got_eriks_martinez_books,
                                                                                   S_bissette_got_martinez_dexters_books, S_bissette_got_martinez_eriks_books
                                                                                  ]):
                if M_bissette.is_state(S_bissette_find_food_book):
                    call expression game.dialog_select("jane_library_dialogue_french_food_find_books")
                    $ M_bissette.trigger(T_bissette_check_library)
                else:

                    call expression game.dialog_select("jane_library_dialogue_french_food_book_holders")

            "Журналы." if M_ross.is_state(S_ross_find_magazines):
                if M_ross.get("talked with jane"):
                    call expression game.dialog_select("jane_library_dialogue_magazines_repeat")
                else:

                    call expression game.dialog_select("jane_library_dialogue_magazines_first")
                    $ M_ross.set("talked with jane", True)

            "Возврат библиотечных книг." if get_returnable_books():
                call expression game.dialog_select("jane_library_dialogue_return_books_pre")
                if M_jane.get("first book returned"):
                    call expression game.dialog_select("jane_library_dialogue_return_books_first")
                    $ M_jane.set("first book returned", False)
                python:
                    for book in get_returnable_books():
                        player.remove_item(book)
                call expression game.dialog_select("jane_library_dialogue_return_books_after")
            "Неважно.":

                call expression game.dialog_select("jane_library_dialogue_leave")

    hide xtra
    hide player
    hide jane
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
