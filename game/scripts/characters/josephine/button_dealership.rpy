label josephine_button_dealership_dialogue:
    call expression game.dialog_select("josephine_button_dealership_dialogue_pre")
    if L_dealership.first_visit:
        call expression game.dialog_select("josephine_button_dealership_dialogue_intro")
        $ L_dealership.visited()
    call expression game.dialog_select("josephine_button_dealership_dialogue_after")
    menu josephine_button_dealership_dialogue_options:
        "Buy a vehicle.":
            call expression game.dialog_select("josephine_button_dealership_dialogue_buy_vehicle")
            menu:
                "Scooter. (1500$)" if player.transport_level < 2:
                    if player.has_money(1500):
                        $ player.transport_level = max(player.transport_level, 2)
                        $ player.spend_money(1500)
                    else:

                        call expression game.dialog_select("josephine_button_dealership_dialogue_buy_vehicle_no_money")

                "Small Car. (3000$)" if player.transport_level < 3:
                    if player.has_money(3000):
                        $ player.transport_level = max(player.transport_level, 3)
                        $ player.spend_money(3000)
                    else:

                        call expression game.dialog_select("josephine_button_dealership_dialogue_buy_vehicle_no_money")

                "Sports Car. (10,000$)" if player.transport_level < 4:
                    if player.has_money(10000):
                        $ player.transport_level = max(player.transport_level, 4)
                        $ player.spend_money(10000)
                    else:

                        call expression game.dialog_select("josephine_button_dealership_dialogue_buy_vehicle_no_money")

        "Make an insurance claim" if M_mom.is_state(S_mom_fix_car):
            label josephine_button_dealership_dialogue_insurance_claim_plate_menu:
                call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_pre")
                call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu_dialogue")
                $ selected_plates = ["dtfmom"]
                $ counter = 0
                while (counter < 3):
                    $ random_plate = renpy.random.choice(plates)
                    while (random_plate in selected_plates):
                        $ random_plate = renpy.random.choice(plates)
                    $ selected_plates += [random_plate]
                    $ counter += 1
            menu:
                "INCEZT" if "incezt" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "DTFM0M" if "dtfmom" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_right_plate")
                    menu:
                        "Pay the bill.":
                            if not player.has_money(9000):
                                call expression game.dialog_select("josephine_button_dealership_dialogue_buy_vehicle_no_money")
                            else:

                                call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_pay")
                                $ M_mom.trigger(T_mom_renew_insurance)
                                $ game.timer.tick()
                                if game.timer.is_dark():
                                    $ player.go_to(L_dealership_front)
                        "Convince her.":

                            if player.stats.chr() >= 7:
                                call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_pay_convince")
                                $ M_mom.trigger(T_mom_renew_insurance)
                                $ game.timer.tick()
                                if game.timer.is_dark():
                                    $ player.go_to(L_dealership_front)
                            else:

                                call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_stat_fail")
                        "Give up":

                            call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_give_up")

                "ASSMAN" if "assman" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_proctologist_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "I♥PEN15" if "peni5" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "VIBE R8R" if "viber8r" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "YES 269" if "yes269" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "XESTTUB" if "xesttub" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")

                "2GRL 1CP" if "2grl1cp" in selected_plates:
                    call expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_wrong_plate")
                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")
                "None of these.":

                    jump expression game.dialog_select("josephine_button_dealership_dialogue_insurance_claim_plate_menu")
        "Kim":

            call expression game.dialog_select("josephine_button_dealership_dialogue_kim")
            jump josephine_button_dealership_dialogue_options
        "Nothing":

            $ pass

    hide joe
    hide player
    hide xtra
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
