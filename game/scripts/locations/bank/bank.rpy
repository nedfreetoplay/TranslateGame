label bank_dialogue:
    $ player.go_to(L_bank)
    if not L_bank.is_visited:
        call expression game.dialog_select("bank_first_time")
        $ L_bank.visited()
    $ game.main()

label bank_teller_dialogue:
    call expression game.dialog_select("bank_liu_start")
    menu:
        "Прверить свой счёт.":
            call expression game.dialog_select("bank_liu_account_info")
            menu:
                "Подробная информация.":
                    call expression game.dialog_select("bank_liu_more_info")
                "Спасибо, мне нужно идти.":

                    call expression game.dialog_select("bank_liu_gtg")
        "Поговорить.":

            call expression game.dialog_select("bank_liu_chat")
    $ game.main()
# Translation group: https://vk.com/summertimesagarus
