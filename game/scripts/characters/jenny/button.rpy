label jenny_button_dialogue:
    if player.location == L_home_diningroom:
        $ M_jenny.set('sit', 1)
    else:
        $ M_jenny.set('sit', 0)
    scene expression player.location.background_closeup
    if M_jenny.is_state(S_jenny_talked_to_cedric) and game.timer.is_day():
        call expression game.dialog_select("jenny_button_talked_to_cedric")
        $ M_jenny.trigger(T_jenny_cedric_didnt_call)
        $ game.timer.tick()
        $ game.main()
    elif M_jenny.is_state(S_jenny_go_to_her_room) and L_home_sisbedroom.is_here(M_jenny):
        if M_jenny.get("dominance") > 0:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_no_money")
        else:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_no_money")
        $ game.main()
    elif M_jenny.is_state(S_jenny_have_breakfast_2) and L_home_diningroom.is_here(M_jenny):
        call expression game.dialog_select("dining_room_jenny_have_breakfast_2")
        menu:
            "You're hot. {color=7ff7}[[Submissive]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_youre_hot")
                $ M_jenny.decrement("dominance")
            "No. {color=f77b}[[Dominant]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_no")
                $ M_jenny.increment("dominance")
        $ M_jenny.trigger(T_jenny_had_breakfast_2)
        $ game.main()
    elif M_jenny.is_state(S_jenny_get_a_mask, S_jenny_buy_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_get_mask")
        $ game.main()
    elif M_jenny.is_state(S_jenny_bought_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_bought_mask")
        $ M_jenny.trigger(T_jenny_delivered_mask)
        $ game.main()
    elif M_jenny.is_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("button_jenny_start_camshow_handjob")
    elif M_jenny.is_state(S_jenny_pool_talk) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("button_jenny_pool_talk")
        $ M_jenny.trigger(T_jenny_stalked)
        $ player.go_to(L_home)
        $ game.main()
    elif M_jenny.is_state(S_jenny_ask_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_ask_movie_date")
        $ M_jenny.trigger(T_jenny_movie_date)
        $ game.main()
    elif M_jenny.is_state(S_jenny_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_movie_date")
        $ game.main()
    elif M_jenny.pregnancy.stage >= 1:
        if M_jenny.pregnancy.stage <= 1:
            call expression game.dialog_select("jenny_button_pregnancy_stage_1")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_button_pregnancy_stage_2")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage in (3, 4):
            call expression game.dialog_select("jenny_button_pregnancy_stage_3")
            jump jenny_pregnancy_menu
        else:
            call expression game.dialog_select("jenny_button_pregnancy_holding_baby")
            jump jenny_pregnancy_baby_menu
    else:
        if L_home_diningroom.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_diningroom_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_diningroom_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_diningroom_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_diningroom_j21")
        elif L_home_backyard.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_backyard_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_backyard_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_backyard_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_backyard_j21")
        elif L_home_sisbedroom.is_here(M_jenny):
            if game.timer.is_afternoon():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_j21")
            elif game.timer.is_evening():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j21")
    menu sis_bedroom_menu:
        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Pay" if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Don't Pay":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")

        "I have a surprise for you!" if M_jenny.is_state(S_jenny_diary_clue) and player.has_item("\w+_necklace", regex=True) and game.timer.is_tick(1, 2):
            call expression game.dialog_select("button_jenny_have_a_surprise_necklace")
            menu:
                "Yes.":
                    call expression game.dialog_select("button_jenny_have_a_surprise_yes")
                "No, I want the real thing!":
                    call expression game.dialog_select("button_jenny_have_a_surprise_no")
            $ M_jenny.trigger(T_jenny_give_necklace)
            jump sis_bedroom_menu

        "Make a deal." if M_jenny.finished_state(S_jenny_go_to_her_room):
            if L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny):
                call expression game.dialog_select("jenny_dialogue_make_a_deal_breakfast")
            else:
                call expression game.dialog_select("jenny_dialogue_make_a_deal")
            $ game.main()

        "Toy." if M_jenny.is_state(S_jenny_get_a_toy, S_jenny_go_to_pink, S_jenny_bring_toy_back) and L_home_sisbedroom.is_here(M_jenny):
            if M_jenny.is_state(S_jenny_bring_toy_back):
                call expression game.dialog_select("button_jenny_has_toy_electroclit")
                if M_jenny.get("dominance") <= 0:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_submissive")
                else:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_dominant")
                $ M_jenny.trigger(T_jenny_brought_back_toy)
                $ game.timer.tick()
                $ game.main()
            else:
                call expression game.dialog_select("button_jenny_get_toy_electroclit")
                jump sis_bedroom_menu

        "{b}Cedric{/b}." if M_jenny.is_state(S_jenny_talk_to_cedric) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("button_jenny_talk_to_cedric")

        "Camshow." if M_jenny.is_state(S_jenny_come_back_camshow) and not M_jenny.pregnancy and game.timer.is_day():
            call expression game.dialog_select("button_jenny_come_back_camshow")

        "Camshow." if M_jenny.finished_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny) and not M_jenny.pregnancy and game.timer.is_day():
            $ M_jenny.set('teasin_before_sex', False)
            call expression game.dialog_select("button_jenny_camshow")
            menu jenny_camshow_options:
                "Handjob.":
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_hj")
                    else:
                        call expression game.dialog_select("jenny_hj_intro_repeat")

                "Oral." if M_jenny.finished_state(S_jenny_start_camshow_blowjob):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_bj")
                    else:
                        call expression game.dialog_select("jenny_bj_intro_repeat")

                "Cunnilingus." if M_jenny.finished_state(S_jenny_give_cunni):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_cunni")
                    else:
                        call expression game.dialog_select("jenny_cunni_intro_repeat")

                "Sex." if M_jenny.finished_state(S_jenny_cheerleader_sex):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_sex")
                    else:
                        call expression game.dialog_select("jenny_sex_intro_repeat")

        "Just Curious." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_curious")
            jump sis_bedroom_menu

        "You and that phone." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_you_and_phone")
            jump sis_bedroom_menu

        "Just saying hi." if L_home_sisbedroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_saying_hi")
            jump sis_bedroom_menu

        "Not swimming?" if L_home_backyard.is_here(M_jenny) and M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("button_jenny_not_swimming")
            jump sis_bedroom_menu

        "Finally warming up to me?" if game.timer.is_morning() and M_jenny.finished_state(S_jenny_catch_her_jilling):
            call expression game.dialog_select("jenny_button_warming_up")
            jump sis_bedroom_menu

        "What are you writing?" if game.timer.is_evening() and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing_2")
                jump sis_bedroom_menu

        "Are you really staying?" if M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy.had_baby:
            call expression game.dialog_select("jenny_button_really_staying")
            jump sis_bedroom_menu

        "You wanna watch porn together?" if M_jenny.finished_state(S_jenny_catch_her_jilling) and game.timer.is_afternoon():
            call expression game.dialog_select("button_jenny_wanna_watch_porn")
            $ M_jenny.set("force_couch_sex", True)

        "Wanna fool around?" if game.timer.is_day() and L_home_diningroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            $ player.go_to(L_home_diningroom)
            if M_jenny.get("first_sex_dining"):
                call expression game.dialog_select("button_jenny_fool_around_diningroom_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_diningroom_repeat")
            jump jenny_dining_room_sex_intro

        "Wanna fool around?" if game.timer.is_day() and L_home_backyard.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            if M_jenny.get("first_sex_pool"):
                $ M_jenny.set("first_sex_pool", False)
                call expression game.dialog_select("button_jenny_fool_around_pool_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_pool_repeat")

        "Wanna fool around?" if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy and game.timer.is_afternoon():
            call expression game.dialog_select("jenny_button_fool_around")
            menu:
                "Okay.":
                    $ M_jenny.set('teasin_before_sex', True)
                    jump jenny_camshow_options
                "Not Today.":
                    call expression game.dialog_select("jenny_button_fool_around_not_today")
                    $ player.go_to(L_home_hallway)
                    $ game.main()

        "Wanna fool around?" if game.timer.is_evening() and M_jenny.finished_inclusive(S_jenny_end):
            call expression game.dialog_select("jenny_button_fool_around_evening")
            jump sis_bedroom_menu

        "Come to my room tonight." if M_jenny.finished_state(S_jenny_night_time_sex) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_button_come_to_my_room")
            $ M_jenny.set("forced_sneak_in_chance", 60)
            jump sis_bedroom_menu

        "Girlfriend experience." if M_jenny.finished_inclusive(S_jenny_necklace_rebutal):
            if game.timer.is_day():
                call expression game.dialog_select("jenny_button_gf_experience_day")
                jump sis_bedroom_menu
            elif game.timer.is_evening():
                call expression game.dialog_select("jenny_button_gf_experience_evening")
                menu:
                    "Yes.":
                        jump expression game.dialog_select("jenny_button_gf_experience_yes")
                    "Nevermind.":
                        call expression game.dialog_select("jenny_button_gf_experience_nevermind")
                        jump sis_bedroom_menu

        "Nothing." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing_2")

        "Nevermind." if (L_home_sisbedroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if game.timer.is_day():
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_2")
            else:
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind_evening_2")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_evening")

        "I should go." if (L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_morning")

        "Nah, I'm busy." if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_bedroom")

    hide player
    hide jenny
    $ game.main()

label jenny_hospital_bed_dialogue:
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    scene expression game.timer.image("hospital_bed{}") with None
    show jenny a_gown_bed_baby b_gown_bed f_gurney_happy_down at Position (align=(0,0))
    show player f_normal_talk with dissolve
    player_name "Hey, how are you feeling?"
    show player f_normal
    show jenny f_gurney_happy_talk_down
    jen "Aww, {b}[firstname]{/b}..."
    if M_jenny.pregnancy.baby_gender == "twins":
        jen "Aren't they beautiful?"
        jen "I can't stop staring at them..."
    elif M_jenny.pregnancy.baby_gender == "boy":
        jen "Isn't he beautiful?"
        jen "I can't stop staring at him..."
    else:
        jen "Isn't she beautiful?"
        jen "I can't stop staring at her..."
    show jenny f_gurney_happy_down
    show player f_normal_talk
    player_name "Hehe, it's so weird hearing you talk like this..."
    show player f_normal
    show jenny f_gurney_upset_talk
    jen "Oh, shut up!"
    show jenny f_gurney_upset
    show player f_laugh
    player_name "There's the {b}[jen_name]{/b} I know and love."
    show player f_normal
    show jenny f_gurney_eyeroll
    jen "... Dick."
    show jenny f_gurney_happy_down
    menu:
        "I just wanted to check on you.":
            show player f_normal_talk
            player_name "I just wanted to check on you."
            show player f_normal
            show jenny f_gurney_happy_talk_down
            jen "Well, we're fine."
            show jenny f_gurney_eyeroll
            jen "I mean, I'm exhausted and the food here fucking sucks but..."
            show jenny f_gurney_happy_talk_down
            jen "... Otherwise, we're fine."
            show jenny f_gurney_happy_down
            show player f_normal_talk
            player_name "Heh, you'll be coming home soon."
            if M_jenny.pregnancy.baby_gender == "twins":
                player_name "You want me to take them for awhile so you can sleep?"
            elif M_jenny.pregnancy.baby_gender == "boy":
                player_name "You want me to take him for awhile so you can sleep?"
            else:
                player_name "You want me to take her for awhile so you can sleep?"
            show player f_normal
            show jenny f_gurney_happy
            jen "Hmm?"
            show jenny f_gurney_happy_talk_down
            if M_jenny.pregnancy.baby_gender == "twins":
                jen "No, I've got them!"
            elif M_jenny.pregnancy.baby_gender == "boy":
                jen "No, I've got him!"
            else:
                jen "No, I've got her!"
            show jenny f_gurney_happy_down
            show player f_normal_talk
            player_name "You sure?"
            show player f_normal
            show jenny f_gurney_upset_talk
            if M_jenny.pregnancy.baby_gender == "twins":
                jen "I said, I've got them, {b}[firstname]{/b}!"
            elif M_jenny.pregnancy.baby_gender == "boy":
                jen "I said, I've got him, {b}[firstname]{/b}!"
            else:
                jen "I said, I've got her, {b}[firstname]{/b}!"
            show jenny f_gurney_happy_down
            show player f_worried_talk
            player_name "O-okay."
            hide player with dissolve
    $ game.main()

label jenny_pregnancy_menu:
    menu:
        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Pay" if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Don't Pay":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")
        "You doing okay?" if game.timer.is_morning() and M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_1")
            jump jenny_pregnancy_menu
        "Are you still mad?" if M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_are_you_still_mad")
            jump jenny_pregnancy_menu
        "You doing okay?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_2")
            jump jenny_pregnancy_menu
        "Can I get you something?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something")
            jump jenny_pregnancy_menu
        "About {b}[deb_name]{/b}..." if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_about_debbie")
            jump jenny_pregnancy_menu
        "Can I get you something?" if game.timer.is_afternoon() and M_jenny.pregnancy.stage == 4:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something_3")
            jump jenny_pregnancy_menu
        "{b}[deb_name]{/b} is driving you crazy?" if M_jenny.pregnancy.stage in (3,4):
            call expression game.dialog_select("jenny_pregnancy_debbie_driving_crazy")
            jump jenny_pregnancy_menu
        "I'll leave you be.":
            call expression game.dialog_select("jenny_pregnancy_leave")
            $ game.main()

label jenny_pregnancy_baby_menu:
    menu:
        "You guys need anything?":
            call expression game.dialog_select("jenny_pregnancy_baby_need_anything")
            jump jenny_pregnancy_baby_menu
        "Looking forward to Daycare.":
            call expression game.dialog_select("jenny_pregnancy_baby_looking_forward_daycare")
            jump jenny_pregnancy_baby_menu
        "I'll leave you be.":
            call expression game.dialog_select("jenny_pregnancy_baby_leave")
            $ game.main()

label jenny_button_gf_experience_yes:
    if not player.has_money(500) and M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_first")
        jump sis_bedroom_menu
    elif not player.has_money(200) and not M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_repeat")
        jump sis_bedroom_menu
    else:
        if M_jenny.get("jenny_girlfriend_first_time"):
            $ player.spend_money(500)
        else:
            $ player.spend_money(200)
        $ M_jenny.set("girlfriend_in_progress", True)
        call expression game.dialog_select("jenny_button_gf_experience_start")
        menu:
            "Stay in.":
                call expression game.dialog_select("jenny_button_gf_experience_stay_in")
                $ game.timer.tick()
                $ player.go_to(L_home_livingroom)
                $ game.main()

label jenny_button_girlfriend_experience_bedroom:
    scene expression "backgrounds/location_home_bedroom_sex01d.jpg"
    show player b_sit a_sit_lap f_sit_flirt_talk o_sit_boner at Position (align=(0,0))
    show jenny b_visit_sit_naked a_visit_sit_naked_down f_visit_sexy_up
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        player_name "W-whoa."
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Took you long enough..."
        show jenny f_visit_sexy_up
        player_name "..."
        show jenny f_visit_sexy_talk_up
        jen "You like?"
        show jenny f_visit_sexy_up
        show player f_sit_flirt_talk
        player_name "I like!"
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Hehe, good!"
        show jenny a_visit_sit_naked_push f_visit_sexy_up
        show player b_sit_falling a_empty f_empty
        with dissolve
        pause
        show jenny f_visit_sexy_talk a_visit_sit_naked_down
        show player b_sit_laying o_visit_laying_boner
        with dissolve
        jen "Now lay back and let me take care of you."

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jen "Mmm, I'm real glad my new boyfriend has such a nice cock!"
        player_name "You like it?"
        show jenny_mc_room_sex 1 with dissolve
        jen "Fuuuuck!"
        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jen "Heh, I wouldn't be dating you if I didn't..."
        player_name "Wow, you're really wet tonight!"
        jen "I know..."
        pause
        jen "Mmm, I've been thinking about your cock all night!"
        player_name "Even while we were watching your show?"
        jen "Yeah, I've seen it all before..."
        player_name "Oh, right."
        pause
        jen "I'm going to sleep real well after this!"
        player_name "Yeah, me too!"
    else:
        player_name "You know, I could really get used to seeing you naked on my bed in the evenings..."
        show player f_sit_flirt
        show jenny f_visit_sexy_talk_up
        jen "Yeah, I bet you could."
        show jenny a_visit_sit_naked_push f_visit_sexy_up
        show player b_sit_falling a_empty f_empty
        with dissolve
        pause
        show jenny f_visit_sexy_talk a_visit_sit_naked_down
        show player b_sit_laying o_visit_laying_boner
        with dissolve
        jen "Now lay back and let me take care of you."
        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jen "Mmm, I love this cock!"
        player_name "I think it loves you too."
        jen "Hah!"
        show jenny_mc_room_sex 1 with dissolve
        jen "Fuuuuck!"
        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jen "It's so deep, {b}[firstname]{/b}!"
        player_name "Yeah.."
        pause
        player_name "I love watching your boobs bounce from this position!"
        jen "Ahh!"
    jump jenny_mc_room_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
