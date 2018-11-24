label mrsj_triggers_init:
    python:

        T_mrsj_intro = Trigger("intro", "MILF Next Door" )
        T_mrsj_yoga_intro = Trigger("yoga intro", "Who's That Milf There")
        T_mrsj_yoga_help_asked = Trigger("yoga help asked", "Women In Tights? Yes Please Part 1")
        T_mrsj_yoga_helped_annie = Trigger("yoga helped annie", "Women In Tights? Yes Please Part 2")
        T_mrsj_poker_night_asked = Trigger("poker night asked", "Poker 1, 2, Strip Part 1")
        T_mrsj_poker_night_lost = Trigger("poker night lost", "Poker 1, 2, Strip Part 2")
        T_mrsj_sex_ed_prepped = Trigger("sex ed prepped", "Sex Ed For Dummies")
        T_mrsj_threesome = Trigger("threesome", "Sex Ed Just Got Practical")
    return

label mrsj_fsm_init:
    python:

        S_mrsj_start = State("start")
        S_mrsj_yoga_intro = State("yoga intro")
        S_mrsj_yoga_ask_help = State("yoga ask help")
        S_mrsj_yoga_helped_annie = State("yoga helped annie")
        S_mrsj_poker_ask = State("poker ask")
        S_mrsj_poker_lost = State("poker lost")
        S_mrsj_sex_ed_prep = State("sex ed prep")
        S_mrsj_threesome = State("threesome")
        S_mrsj_private_yoga = State("private yoga")



        S_mrsj_start.add(T_mrsj_intro, S_mrsj_yoga_intro)
        S_mrsj_yoga_intro.add(T_mrsj_yoga_help_asked, S_mrsj_yoga_ask_help)
        S_mrsj_yoga_ask_help.add(T_mrsj_yoga_helped_annie, S_mrsj_yoga_helped_annie)
        S_mrsj_yoga_helped_annie.add(T_mrsj_poker_night_asked, S_mrsj_poker_ask)
        S_mrsj_poker_ask.add(T_mrsj_poker_night_lost, S_mrsj_poker_lost)
        S_mrsj_poker_lost.add(T_erik_sex_ed, S_mrsj_sex_ed_prep)
        S_mrsj_sex_ed_prep.add(T_mrsj_sex_ed_prepped, S_mrsj_threesome)
        S_mrsj_poker_lost.add(T_erik_find_gf, S_mrsj_private_yoga)

        M_mrsj.add(S_mrsj_start, S_mrsj_yoga_intro, S_mrsj_yoga_ask_help,
                   S_mrsj_yoga_helped_annie, S_mrsj_poker_ask, S_mrsj_poker_lost,
                   S_mrsj_sex_ed_prep, S_mrsj_threesome, S_mrsj_private_yoga)
    return

label mrsj_machine_init:
    python:
        M_mrsj = Machine("mrsj", default_loc = [[L_erikhouse_entrance, L_yoga_room, L_NULL, L_NULL]],
                         vars = {"sex speed": .3,
                                 "afterpoker fun": False,
                                 },
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
