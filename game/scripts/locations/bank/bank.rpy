label bank_dialogue:
    $ player.go_to(L_bank)
    if not L_bank.is_visited:
        call expression game.dialog_select("bank_first_time")
        $ L_bank.visited()
    $ game.main()

label bank_teller_dialogue:
    call expression game.dialog_select("bank_liu_start")
    menu:
        "Check my account.":
            call expression game.dialog_select("bank_liu_account_info")
            menu:
                "More information.":
                    call expression game.dialog_select("bank_liu_more_info")
                "Thanks, I have to go.":

                    call expression game.dialog_select("bank_liu_gtg")
        "Chat.":

            call expression game.dialog_select("bank_liu_chat")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
