init python:

    T_erik_intro = Trigger("intro", "Брат От Другой Матери")
    T_erik_asked_favor = Trigger("asked favor", "Просить Брата Об Одолжении часть 1")
    T_erik_favor_gave_game = Trigger("favor gave game", "Просить Брата Об Одолжении часть 2")
    T_erik_card_hunt = Trigger("card hunt", "Эрик не может найти свою коробку с карточками")
    T_erik_card_hunt_find_cards = Trigger("card hunt find cards", "Эрик не может найти свою коробку с карточками")
    T_erik_got_crown_card = Trigger("got crown card", "Эрику нужно это кольцо на член, т.е. корону")
    T_erik_order_orcette = Trigger("order orcette", "Разве нам всем не любопытно? часть 1")
    T_erik_received_orcette = Trigger("received orcette", "Разве нам всем не любопытно? часть 2")
    T_erik_bullying_start = Trigger("bullying start", "Потому что слова не болят, а мышцы болят. часть 1")
    T_erik_bullying_got_beaten_up = Trigger("bullying got beaten up", "Потому что слова не болят, а мышцы болят. часть 2")
    T_erik_bullying_bedridden = Trigger("bullying bedridden", "Потому что слова не болят, а мышцы болят. часть 3")
    T_erik_vr_asked = Trigger("vr asked", "Переход 2D на следующий уровень")
    T_erik_vr_buy_headset = Trigger("vr buy headset", "Переход 2D на следующий уровень")
    T_erik_vr_give = Trigger("vr give", "gave the ultimate fapping tool")
    T_erik_breastfeeding_seen_telescope = Trigger("breastfeeding seen telescope", "Ты Все Еще Ребенок? часть 1")
    T_erik_breastfeeding_seen_in_person = Trigger("breastfeeding seen in person", "Ты Все Еще Ребенок? часть 2")
    T_erik_thief_seen_telescope = Trigger("thief seen telescope", "Трусики?! Куда?! часть 1")
    T_erik_thief_catch = Trigger("thief_catch", "Трусики?! Куда?! часть 2")
    T_erik_father_forgive = Trigger("father forgive", "Ларри Просто Хочет, Чтобы Его Простили.")
    T_erik_father_tell_location = Trigger("father tell location", "Ларри сказал тебе заглянуть в кусты в парке.") 
    T_erik_father_got_treasure = Trigger("father got treasure", "Тайник Ларри с сокровищами")
    T_erik_path_split = Trigger("path split", "В Какую Сторону Идти")
    T_erik_sex_ed = Trigger("sex ed", "Причины, Почему Секс воспитание Важно")
    T_erik_find_gf = Trigger("find gf", "Помогите Брату")

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
