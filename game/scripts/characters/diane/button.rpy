label aunt_button_dialogue:
    scene expression player.location.background_blur with None
    if M_diane.is_state(S_diane_daylight_drinking):
        call expression game.dialog_select("dianes_dialogue_daylight_drinking")
        $ M_diane.trigger(T_diane_drunk)
        $ game.main()

    if M_diane.pregnancy.gave_birth:
        call expression game.dialog_select("dianes_dialogue_gave_birth_intro")

    elif M_diane.between_states(S_diane_start, S_diane_work_on_garden):
        call expression game.dialog_select("dianes_dialogue_intro_d1_d6")

    elif M_diane.between_states(S_diane_get_augmentation, S_diane_milking_help):
        call expression game.dialog_select("dianes_dialogue_intro_d7_d12")

    elif M_diane.between_states(S_diane_debbie_evening_visit, S_diane_couch_crashing):
        call expression game.dialog_select("dianes_dialogue_intro_d12b_d15")

    elif M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and game.timer.is_day():
        call expression game.dialog_select("dianes_dialogue_intro_d16_d18_barn")

    elif M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and game.timer.is_dark():
        call expression game.dialog_select("dianes_dialogue_intro_d16_d18_couch")

    elif M_diane.between_states(S_diane_milk_production_increase, S_diane_end) and game.timer.is_day():
        call expression game.dialog_select("dianes_dialogue_intro_d19_d20_barn")

    elif (M_diane.finished_state(S_diane_milk_production_increase) and game.timer.is_dark() and
          (M_mom.is_state(S_mom_sleepover) or M_jenny.is_state(S_jenny_catch_her_jilling)
          or M_mom.is_state(S_mom_spy))):
        call expression game.dialog_select("dianes_dialogue_intro_kitchen")

    elif M_diane.is_state(S_diane_milk_production_increase) and game.timer.is_dark():
        call expression game.dialog_select("dianes_dialogue_intro_d19_couch")

    elif M_diane.between_states(S_diane_risky_frisky_kinky, S_diane_end) and game.timer.is_dark():
        call expression game.dialog_select("dianes_dialogue_intro_d20_couch")

    if M_diane.pregnancy.gave_birth:
        menu dia_baby_default_dialogue_options:
            "How's he doing?" if M_diane.pregnancy.baby_gender == "boy":
                call expression game.dialog_select("dianes_dialogue_hows_baby_doing_boy")
                jump dia_baby_default_dialogue_options

            "How are they doing?" if M_diane.pregnancy.baby_gender == "twins":
                call expression game.dialog_select("dianes_dialogue_hows_baby_doing_twins")
                jump dia_baby_default_dialogue_options

            "How's she doing?" if M_diane.pregnancy.baby_gender == "girl":
                call expression game.dialog_select("dianes_dialogue_hows_baby_doing_girl")
                jump dia_baby_default_dialogue_options
            "Can I get you anything?":

                call expression game.dialog_select("dianes_dialogue_get_anything_baby")
                jump dia_baby_default_dialogue_options
            "I'll leave you guys be.":

                call expression game.dialog_select("dianes_dialogue_baby_leave")
        $ game.main()

    menu dia_default_dialogue_options:
        "What have you been up to?" if M_diane.between_states(S_diane_start, S_diane_work_on_garden):
            call expression game.dialog_select("dianes_dialogue_what_have_you_been_up_to")
            jump dia_default_dialogue_options

        "How's the garden?" if M_diane.between_states(S_diane_start, S_diane_work_on_garden):
            call expression game.dialog_select("dianes_dialogue_hows_the_garden")
            jump dia_default_dialogue_options

        "About {b}[deb_name]{/b}." if M_diane.between_states(S_diane_start, S_diane_work_on_garden):
            call expression game.dialog_select("dianes_dialogue_about_debname")
            jump dia_default_dialogue_options

        "How's the garden?" if M_diane.between_states(S_diane_get_augmentation, S_diane_milking_help):
            call expression game.dialog_select("dianes_dialogue_hows_the_garden_2")
            jump dia_default_dialogue_options

        "How's business?" if M_diane.pregnancy.number_of_babies>0:
            call expression game.dialog_select("dianes_dialogue_hows_business")
            jump dia_default_dialogue_options

        "About {b}Veronica{/b}" if M_diane.between_states(S_diane_get_augmentation, S_diane_milking_help):
            call expression game.dialog_select("dianes_dialogue_about_veronica")
            jump dia_default_dialogue_options

        "Have you spoken with {b}[deb_name]{/b} recently?" if M_diane.between_states(S_diane_get_augmentation, S_diane_milking_help):
            call expression game.dialog_select("dianes_dialogue_have_you_spoken_with_debname")
            jump dia_default_dialogue_options

        "Feeling better?" if M_diane.between_states(S_diane_debbie_evening_visit, S_diane_couch_crashing):
            call expression game.dialog_select("dianes_dialogue_feeling_better")
            jump dia_default_dialogue_options

        "I really like working for you." if M_diane.between_states(S_diane_debbie_evening_visit, S_diane_return_outfit_package) and L_diane_barn_interior.is_here(M_diane):
            call expression game.dialog_select("dianes_dialogue_like_working_for_you")
            jump dia_default_dialogue_options

        "How's the couch" if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and L_diane_barn_interior.is_here(M_diane):
            call expression game.dialog_select("dianes_dialogue_hows_the_couch")
            jump dia_default_dialogue_options

        "What are you up to?" if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_what_are_you_up_to")
            jump dia_default_dialogue_options

        "Where's {b}[deb_name]{/b}?" if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_wheres_debname")
            jump dia_default_dialogue_options

        "I love that nightgown!" if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_love_that_nightgown")
            jump dia_default_dialogue_options

        "You call {b}Veronica{/b} yet?" if M_diane.between_states(S_diane_milk_production_increase, S_diane_end) and game.timer.is_day():
            call expression game.dialog_select("dianes_dialogue_call_veronica")
            jump dia_default_dialogue_options

        "How's the business going?" if M_diane.between_states(S_diane_milk_production_increase, S_diane_end) and game.timer.is_day():
            call expression game.dialog_select("dianes_dialogue_hows_the_business")
            jump dia_default_dialogue_options

        "What are you up to?" if M_diane.is_state(S_diane_milk_production_increase) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_what_up_to")
            jump dia_default_dialogue_options

        "I was on my way to see {b}[deb_name]{/b}." if M_diane.is_state(S_diane_milk_production_increase) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_on_my_way_debbie")
            $ game.main()

        "Cow Girl." if M_daisy.between_states(S_daisy_awakened_statue, S_daisy_picking_flowers):
            call expression game.dialog_select("dianes_dialogue_cow_girl")
            jump dia_default_dialogue_options

        "{b}Daisy{/b}." if M_daisy.finished_state(S_daisy_picking_flowers):
            call expression game.dialog_select("dianes_dialogue_daisy")
            jump dia_default_dialogue_options

        "Paint." if M_dewitt.is_state([S_dewitt_ask_diane_paint, S_dewitt_shed_get_paint]):
            call expression game.dialog_select("dianes_dialogue_pre_fun_paint")
            $ M_dewitt.trigger(T_dewitt_shed_paint)

        "Breastfeed" if M_diane.finished_state(S_diane_milking_help) and (L_diane_barn_interior.is_here(M_diane) or L_diane_shed.is_here(M_diane)) and M_diane.pregnancy.stage <= 2:
            call expression game.dialog_select("dianes_dialogue_breastfeed")

        "Drink" if M_diane.is_state(S_diane_make_drink) and not game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_make_drink")

        "Tool." if M_diane.is_state(S_diane_fetch_pump):
            if player.has_item("pump"):
                call expression game.dialog_select("dianes_dialogue_diane_got_pump")
                $ M_diane.trigger(T_diane_found_pump)
                $ player.remove_item("pump")
            else:
                call expression game.dialog_select("dianes_dialogue_diane_fetch_pump")

        "Delivery." if M_diane.is_state(S_diane_delivery_1, S_diane_delivery_1_done):
            if M_diane.is_state(S_diane_delivery_1):
                call expression game.dialog_select("dianes_dialogue_delivery_1_reminder")
            else:

                call expression game.dialog_select("dianes_dialogue_delivery_1_done")
                $ M_diane.trigger(T_diane_delivery_finished)

        "Delivery." if M_diane.between_states(S_diane_delivery_3_fetch_goods, S_diane_delivery_3_drop_off_goods):
            call expression game.dialog_select("dianes_dialogue_delivery_3_reminder")

        "Pump." if M_diane.is_state(S_diane_dump_pump):
            call expression game.dialog_select("dianes_dialogue_dump_pump")
            $ game.main()

        "Cow Suit." if not M_diane.get("breed first time") and L_diane_barn_interior.is_here(M_diane):
            call expression game.dialog_select("dianes_dialogue_cow_suit")
            call expression game.dialog_select("diane_outfit_change")
            jump dia_default_dialogue_options

        "Breeding Session." if (not M_diane.get("breed first time") or M_diane.finished_state(S_diane_return_outfit_package)) and M_diane.pregnancy.stage <= 2 and L_diane_barn_interior.is_here(M_diane):
            call expression game.dialog_select("dianes_dialogue_breeding_session")
            jump diane_sex_breed_start

        "How's the baby?" if M_diane.pregnancy and 1<=M_diane.pregnancy.stage<=4:
            call expression game.dialog_select("dianes_dialogue_hows_the_baby_pregnancy_{}".format(M_diane.pregnancy.stage))
            jump dia_default_dialogue_options

        "Taste from the source." if L_diane_shed.is_here(M_diane) and M_diane.finished_state(S_diane_milk_production_increase):
            call expression game.dialog_select("dianes_shed_dianes_dialogue_lets_milk")

        "Ready to pump?" if M_diane.finished_state(S_diane_return_production_book) and L_diane_barn_interior.is_here(M_diane) and M_diane.pregnancy.stage <= 2:
            call expression game.dialog_select("dianes_dialogue_ready_to_pump")
            jump milking_game_pre

        "Milk Sample." if M_daisy.is_state(S_daisy_viewed_statue):
            call expression game.dialog_select("dianes_dialogue_milk_sample")
            $ player.get_item("milk_sample")

        "I should get to work." if M_diane.between_states(S_diane_start, S_diane_work_on_garden):
            call expression game.dialog_select("dianes_dialogue_leave_d1")

        "You should take it easy." if M_diane.between_states(S_diane_get_augmentation, S_diane_milking_help):
            call expression game.dialog_select("dianes_dialogue_take_it_easy")

        "I should get to work." if M_diane.between_states(S_diane_debbie_evening_visit, S_diane_return_outfit_package) and not L_home_livingroom.is_here(M_diane):
            call expression game.dialog_select("dianes_dialogue_leave_d12b")

        "Goodnight." if M_diane.between_states(S_diane_inform_carpenter, S_diane_return_outfit_package) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_goodnight")

        "I should get to work." if M_diane.finished_state(S_diane_milk_production_increase) and game.timer.is_day():
            call expression game.dialog_select("dianes_dialogue_leave_d19_d20_day")

        "Goodnight." if M_diane.is_state(S_diane_milk_production_increase, S_diane_risky_frisky_kinky) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_goodnight_1")

        "Goodnight." if M_diane.finished_state(S_diane_risky_frisky_kinky) and game.timer.is_dark():
            call expression game.dialog_select("dianes_dialogue_goodnight_2")
    $ game.main()

label diane_bedroom_dialogue:
    if M_diane.is_state(S_diane_bring_cold_towel):
        call expression game.dialog_select("diane_bedroom_bring_cold_towel")
        $ M_diane.trigger(T_diane_nip_slip_n_dip)

    elif M_diane.is_state(S_diane_drunken_splur_aftermath):
        call expression game.dialog_select("diane_bedroom_drunken_splur_aftermath")
    $ game.main()

label diane_outfit_change:
    show player 26 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    dia "Is that better?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Y-yeah."
    show player 13 with dissolve
    return

label diane_debbie_3way_dialogue:
    if M_diane.is_state(S_diane_get_dirty_with_debbie):
        call expression game.dialog_select("mom_bedroom_diane_debbie_threeway_intro")
        $ animated = True
        jump diane_debbie_sex_start
    $ animated = True
    $ M_diane.set("sex speed", 0.09)
    scene expression "backgrounds/location_home_debbiesidebed_dialogue_sheet.jpg"
    show diane f_sit_bed_smirk b_nightgown_sit a_empty at Position (xpos=650,ypos=800)
    show debbie b_nightgown_bed a_empty f_bed_sit_sexy_talk at flip
    show debbie at Position (xpos=-250)
    show playerf 5b at Position (xpos=200,ypos=850)
    show playerfa 1 at Position (xpos=180,ypos=640)
    with dissolve
    deb "There he is!"
    show debbie f_bed_sit_sexy
    show diane f_sit_bed_smirk_talk
    dia "Finally!"
    show diane f_sit_bed_smirk
    show debbie f_bed_sit_sexy_talk
    deb "We were worried you might not come tonight."
    show debbie f_bed_sit_sexy
    show diane f_sit_bed_smirk_talk
    dia "I was about to start without you!"
    show diane f_sit_bed_smirk
    show debbie f_bed_sit_sexy_talk
    deb "Hehe, oh stop it!"
    show debbie f_bed_sit_sexy
    show diane f_sit_bed_smirk_talk
    dia "I'm serious!"
    dia "You gonna join us, {b}[firstname]{/b}?"
    show diane f_sit_bed_smirk
    menu:
        "Yes.":
            show diane f_sit_bed_smirk b_nightgown_sit a_empty at Position (xpos=650,ypos=800)
            show debbie b_nightgown_bed a_empty f_bed_sit_sexy at flip
            show debbie at Position (xpos=-250)
            show playerf 5 at Position (xpos=200,ypos=850)
            show playerfa 1 at Position (xpos=180,ypos=640)
            player_name "Definitely!"
            show playerf 5b
            show debbie f_bed_sit_sexy_talk
            deb "Oh, I'm so happy!"
            show debbie f_bed_sit_sexy b_bed_nightgown_undress
            show diane b_nightgown_undress f_sit_bed_undress_down_front
            with dissolve
            pause
            show diane b_nightgown_undress2 f_sit_bed_undress2_down_front
            show debbie b_bed_undress2 f_bed_sit_undress2_sexy
            with dissolve
            pause
            show diane b_naked_sit f_sit_bed_smirk
            show debbie b_naked_bed f_bed_sit_sexy
            with dissolve
            pause
            show diane f_sit_bed_smirk_talk
            dia "Well, what are you waiting for?!"
            show diane f_sit_bed_smirk
            show debbie f_bed_sit_sexy_talk
            deb "Get those pants off!"
            show debbie f_bed_sit_sexy
            show playerf 5
            player_name "Okay!"
            hide playerf
            hide playerfa
            hide debbie
            hide diane
            with dissolve

            scene expression "backgrounds/location_home_debbiebed_sex.jpg"
            show diane_debbie_sex_bed diane_talk
            dia "Mmm, I love being in here with you guys."
            dia "It's like the best sex ever!"
            show diane_debbie_sex_bed debbie_talk
            deb "Heh, it really is!"
            show diane_debbie_sex_bed player_talk
            player_name "Yeah!"
            show diane_debbie_sex_bed debbie_talk
            deb "So sweetie, who do you wanna start with tonight?"
            menu:
                "{b}Diane{/b}.":
                    $ M_diane.set("change partner",False)
                "{b}[deb_name]{/b}.":

                    $ M_diane.set("change partner",True)
            jump diane_debbie_pre_sex_loop
        "No.":

            show diane f_sit_bed_smirk b_nightgown_sit a_empty at Position (xpos=650,ypos=800)
            show debbie b_nightgown_bed a_empty f_bed_sit_sexy at flip
            show debbie at Position (xpos=-250)
            show playerf 5 at Position (xpos=200,ypos=850)
            show playerfa 1 at Position (xpos=180,ypos=640)
            player_name "Eh, actually..."
            player_name "I have something else I need to take care of."
            show playerf 5b
            show debbie f_bed_sit_sexy_talk
            deb "Aww, are you sure?"
            show debbie f_bed_sit_sexy
            show playerf 5
            player_name "Yeah, sorry."
            show playerf 5b
            show debbie f_bed_sit_sexy_talk
            deb "That's alright, sweetie."
            show debbie f_bed_sit_sexy
            show diane f_sit_bed_smirk_talk
            dia "Your loss, stud."
            dia "Looks like we're on our own tonight!"
            hide debbie
            show diane b_nightgown_sit_kissing_debbie f_empty at Position (xoffset=100)
            with dissolve
            show playerf 3
            player_name "!!!"
            player_name "( Ah, man... )"
            hide playerf
            hide playerfa
            with dissolve
            $ M_diane.set("refused 3way", True)
            $ player.go_to(L_home_livingroom)
    $ game.main()

label diane_hospital_bed_dialogue:
    scene expression game.timer.image("hospital_bed{}") with None
    show diane f_gurney_normal_talk a_gown_bed_baby b_gown_bed at Position (xpos=578,ypos=850)
    show player 13
    with dissolve
    dia "Hey, handsome."
    dia "You come by to check on us again?"
    show diane f_gurney_normal
    menu:
        "Yup.":
            show diane f_gurney_normal a_gown_bed_baby b_gown_bed at Position (xpos=578,ypos=850)
            show player 14
            if M_diane.pregnancy.baby_gender == "boy":
                player_name "How's he doing?"
                show player 426
                show diane f_gurney_teasing_look
                dia "He's sleeping."
                show diane f_gurney_down_front
                show player 429
                player_name "He's so cute!"
            elif M_diane.pregnancy.baby_gender == "twins":
                player_name "How are they doing?"
                show player 426
                show diane f_gurney_teasing_look
                dia "They're sleeping."
                show diane f_gurney_down_front
                show player 429
                player_name "They're so cute!"
            else:
                player_name "How's she doing?"
                show player 426
                show diane f_gurney_teasing_look
                dia "She's sleeping."
                show diane f_gurney_down_front
                show player 429
                player_name "She's so cute!"
            show player 426
            show diane f_gurney_laugh
            dia "Hehe."
            show diane f_gurney_down_front
            pause
            show player 14
            player_name "I guess, I should leave you guys to rest."
            show player 13
            show diane f_gurney_normal_talk
            dia "We'll be home soon."
            show diane f_gurney_normal
            show player 14
            player_name "Okay."
            show player 429
            if M_diane.pregnancy.baby_gender == "twins":
                player_name "I'll see you soon, little ones."
            else:
                player_name "I'll see you soon, little one."
            hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
