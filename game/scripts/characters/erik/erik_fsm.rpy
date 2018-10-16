label erik_triggers_init:
    python:

        T_erik_intro = Trigger("intro", "Brother From Another Mother")
        T_erik_asked_favor = Trigger("asked favor", "Asking A Brother For A Favor Part 1")
        T_erik_favor_gave_game = Trigger("favor gave game", "Asking A Brother For A Favor Part 2")
        T_erik_card_hunt = Trigger("card hunt", "Erik Can't Find His Fappening Deck")
        T_erik_card_hunt_find_cards = Trigger("card hunt find cards", "Erik Can't Find His Fappening Deck")
        T_erik_got_crown_card = Trigger("got crown card", "Erik Needs That Cock Ring, I Mean Crown")
        T_erik_order_orcette = Trigger("order orcette", "Aren't We All Curious? Part 1")
        T_erik_received_orcette = Trigger("received orcette", "Aren't We All Curious? Part 2")
        T_erik_bullying_start = Trigger("bullying start", "Because Words Don't Hurt But Muscles Do Part 1")
        T_erik_bullying_got_beaten_up = Trigger("bullying got beaten up", "Because Words Don't Hurt But Muscles Do Part 2")
        T_erik_bullying_bedridden = Trigger("bullying bedridden", "Because Words Don't Hurt But Muscles Do Part 3")
        T_erik_vr_asked = Trigger("vr asked", "Taking 2D To The Next Level")
        T_erik_vr_buy_headset = Trigger("vr buy headset", "Taking 2D to the next level")
        T_erik_vr_give = Trigger("vr give", "gave the ultimate fapping tool")
        T_erik_breastfeeding_seen_telescope = Trigger("breastfeeding seen telescope", "Are You Still A Kid? Part 1")
        T_erik_breastfeeding_seen_in_person = Trigger("breastfeeding seen in person", "Are You Still A Kid? Part 2")
        T_erik_thief_seen_telescope = Trigger("thief seen telescope", "PANTIES?! WHERE?! Part 1")
        T_erik_thief_catch = Trigger("thief_catch", "PANTIES?! WHERE?! Part 2")
        T_erik_father_forgive = Trigger("father forgive", "Larry Just Wants To Be Forgiven")
        T_erik_father_tell_location = Trigger("father tell location", "larry told you to look behind the bushes in the park.") 
        T_erik_father_got_treasure = Trigger("father got treasure", "Larry's Secret Treasure Stash")
        T_erik_path_split = Trigger("path split", "Which Way To Go")
        T_erik_sex_ed = Trigger("sex ed", "Reasons Why Sex Ed Is Important")
        T_erik_find_gf = Trigger("find gf", "Help A Brother Out")
    return

label erik_fsm_init:
    python:

        S_erik_start = State("start", "Erik's start state")
        S_erik_ask_favor = State("ask favor", "Asking a brother for a favor")
        S_erik_favor_give_game = State("favor give game", "Completing the favor")
        S_erik_card_hunt = State("card hunt", "default")
        S_erik_card_hunt_found_cards = State("card hunt found cards", "default")
        S_erik_card_hunt_get_crown_card = State("card hunt get crown card", "default")
        S_erik_orcette_ask = State("orcette ask", "default")
        S_erik_orcette_give = State("orcette give", "default")
        S_erik_bullying_start = State("bullying start", "default")
        S_erik_confront_dexter = State("confront dexter", "default")
        S_erik_hospital_bedridden = State("hospital bedridden", "default")
        S_erik_vr_ask = State("vr ask", "default")
        S_erik_vr_bought = State("vr bought", "default")
        S_erik_vr_given = State("vr given", "default")
        S_erik_breastfeeding_telescope_spy = State("breastfeeding telescope spy", "default")
        S_erik_breastfeeding_caught_in_act = State("breastfeeding caught in act", "default")
        S_erik_thief_telescope_spy = State("thief telescope spy", "default")
        S_erik_thief_caught_thief = State("thief caught thief", "default")
        S_erik_forgive_father = State("forgive father", "default")
        S_erik_forgive_father_get_treasure_location = State("forgive father get treasure location", "default")
        S_erik_forgive_father_found_treasure = State("forgive father found treasure", "default")
        S_erik_path_split = State("path split", "default")
        S_erik_find_girlfriend = State("find girlfriend", "default")
        S_erik_sexual_education = State("sexual education", "default")


        S_erik_start.add(T_erik_intro, S_erik_ask_favor)
        S_erik_ask_favor.add(T_erik_asked_favor, S_erik_favor_give_game)
        S_erik_favor_give_game.add(T_erik_favor_gave_game, S_erik_card_hunt)
        S_erik_card_hunt.add(T_erik_card_hunt, S_erik_card_hunt_found_cards)
        S_erik_card_hunt_found_cards.add(T_erik_card_hunt_find_cards, S_erik_card_hunt_get_crown_card)
        S_erik_card_hunt_get_crown_card.add(T_erik_got_crown_card, S_erik_orcette_ask)
        S_erik_orcette_ask.add(T_erik_order_orcette, S_erik_orcette_give)
        S_erik_orcette_give.add(T_erik_received_orcette, S_erik_bullying_start)
        S_erik_bullying_start.add(T_erik_bullying_start, S_erik_confront_dexter)
        S_erik_confront_dexter.add(T_erik_bullying_got_beaten_up, S_erik_hospital_bedridden)
        S_erik_hospital_bedridden.add(T_erik_bullying_bedridden, S_erik_vr_ask)
        S_erik_vr_ask.add(T_erik_vr_asked, S_erik_vr_bought)
        S_erik_vr_bought.add(T_erik_vr_give, S_erik_vr_given)
        S_erik_vr_given.add(T_erik_breastfeeding_seen_telescope, S_erik_breastfeeding_telescope_spy)
        S_erik_breastfeeding_telescope_spy.add(T_erik_breastfeeding_seen_in_person, S_erik_breastfeeding_caught_in_act)
        S_erik_breastfeeding_caught_in_act.add(T_erik_thief_seen_telescope, S_erik_thief_telescope_spy)
        S_erik_thief_telescope_spy.add(T_erik_thief_catch, S_erik_thief_caught_thief)
        S_erik_thief_caught_thief.add(T_erik_father_forgive, S_erik_forgive_father)
        S_erik_forgive_father.add(T_erik_father_tell_location, S_erik_forgive_father_get_treasure_location)
        S_erik_forgive_father_get_treasure_location.add(T_erik_father_got_treasure, S_erik_forgive_father_found_treasure)
        S_erik_forgive_father_found_treasure.add(T_erik_path_split, S_erik_path_split)

        S_erik_path_split.add(T_erik_find_gf, S_erik_find_girlfriend)
        S_erik_path_split.add(T_erik_sex_ed, S_erik_sexual_education)


        M_erik.add(S_erik_start, S_erik_ask_favor, S_erik_favor_give_game, S_erik_card_hunt,
                    S_erik_card_hunt_found_cards, S_erik_card_hunt_get_crown_card, S_erik_orcette_ask,
                    S_erik_orcette_give, S_erik_bullying_start, S_erik_confront_dexter, S_erik_hospital_bedridden,
                    S_erik_vr_ask, S_erik_vr_bought, S_erik_vr_given, S_erik_breastfeeding_telescope_spy,
                    S_erik_breastfeeding_caught_in_act, S_erik_thief_telescope_spy, S_erik_thief_caught_thief,
                    S_erik_forgive_father, S_erik_forgive_father_get_treasure_location, S_erik_forgive_father_found_treasure,
                    S_erik_path_split, S_erik_find_girlfriend, S_erik_sexual_education)
    return

label erik_machine_init:
    python:
        M_erik = Machine("erik", default_loc = [[L_school_scienceclassroom, L_school_cafeteria, L_erikhouse_erikroom, L_erikhouse_erikroom], 
                                                [L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_erikroom]
                                                ],
                         vars = {"sex speed": .3,
                                 "webcam help": False,
                                 "seen basement": False,
                                 "bullying delay": 999999,
                                 "received orcette": False,
                                }
                        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
