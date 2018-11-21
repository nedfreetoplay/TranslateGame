label printer_dialogue_bissette_scan_missing_pages:
    show xtra 40
    show player 520 at Position (xpos=375) with dissolve
    player_name "Хорошо, сейчас Мне нужно просто положить эту книгу сюда..."
    player_name "И нажать на...."
    player_name "Эту кнопку!"
    player_name "..."
    player_name "..."
    player_name "ПК Письмо Загрузки? Что черт возьми это значит?"
    player_name "Может мне стоит {b}спросить кого-нибудь{/b} как заставить эту штуку работать."
    hide player with dissolve
    return

label printer_dialogue_bissette_print_poem_assignment:
    show player 518 at left with dissolve
    player_name "Печать!"
    show player 519 with vpunch
    show xtra_paper 39 at Position (xoffset=100) with dissolve
    pause .25
    hide xtra_paper 39 with dissolve
    show player 184 with dissolve
    pause    
    show player 386 with dissolve
    player_name "Хорошо! Теперь у меня в руках Французкая поэма."
    hide player with dissolve
    return

label printer_dialogue_nothing:
    show player 4 at left with dissolve
    player_name "У меня ничего нет чтобы распечатать в данный момент."
    hide player with dissolve
    return

label printer_dialogue:
    scene computer_room_printer_c
    if M_bissette.is_state([S_bissette_scan_missing_pages, S_bissette_fix_printer]):
        call expression game.dialog_select("printer_dialogue_bissette_scan_missing_pages")
        $ M_bissette.trigger(T_bissette_broken_printer)

    elif M_bissette.is_state(S_bissette_print_poem_assignment):
        call expression game.dialog_select("printer_dialogue_bissette_print_poem_assignment")
        $ M_bissette.trigger(T_bissette_print_assignment)
    else:

        call expression game.dialog_select("printer_dialogue_nothing")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
