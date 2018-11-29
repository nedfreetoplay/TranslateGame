label dianes_front_yard_dialogue:
    $ player.go_to(L_diane_yard)
    if M_diane.is_state(S_diane_seen_cucumber):
        call expression game.dialog_select("dianes_front_seen_cucumber")
        $ M_diane.trigger(T_diane_cucumber_aftermath)
    $ game.main()

label dianes_front_yard_night_locked:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "{b}Diane{/b} is probably asleep..."
    hide player with dissolve
    return

label dianes_front_seen_cucumber:
    scene expression "backgrounds/location_diane_front_day_blur.jpg"
    show player 83b with dissolve
    player_name "Wow!!!"
    player_name "I had no idea {b}Diane{/b} was so..."
    player_name "I mean... She's masturbating in her kitchen!"
    player_name "... With a cucumber!"
    show player 78 at Position (xoffset=50) with dissolve
    player_name "!!!"
    show player 79 with dissolve
    player_name "I should uhh... Probably..."
    player_name "... I can't let {b}Diane{/b} see me like this!"
    player_name "{b}Best get started with the garden.{/b} That'll get my mind off it."
    hide player with dissolve
    return

label locked_shed_dialogue:
    if M_diane.finished_state(S_diane_fetch_pump):
        scene garden
        show player 10 at left with dissolve
        player_name "{b}Diane{/b}?"
        show player 5
        dia "Just a second!"
        player_name "..."
        show diane b_shirtless a_shirtless_sides f_normal
        show player 11
        player_name "!!!"
        show diane f_normal_talk
        dia "What's the matter, handsome?"
        show diane f_normal
        show player 10
        player_name "Where's your shirt?"
        show player 5
        show diane f_surprised_front a_shirtless_shock with dissolve
        dia "Hmm?"
        show diane f_thinking_back a_shirtless_sides with dissolve
        dia "Oh, I took it off because... Well..."
        dia "... It's really hot in there."
        show diane f_normal
        show player 14
        player_name "Yeah, I bet!"
        show player 13
        show diane f_normal_talk
        dia "Did you need something?"
        show diane f_normal
        menu diane_shed_locked_menu:
            "Need any help in there?":
                show player 10 at left
                show diane f_normal
                with dissolve
                player_name "Do you need any help in there?"
                show player 13
                show diane f_laugh
                dia "Hehe, no I've got everything handled."
                show diane f_smirk_talk
                dia "Thanks for the offer though, stud."
                show diane f_normal
                jump diane_shed_locked_menu
            "Nothing.":

                show player 14 at left
                show diane f_normal
                with dissolve
                player_name "I was just checking on you."
                player_name "It's so quiet in there..."
                show player 13
                show diane f_laugh
                dia "Heh, yeah. I'm just focused."
                dia "Ugh, it's like an oven in there!"
                show diane f_normal
                show player 14
                player_name "You know, you can leave the door open if you want..."
                player_name "That would help with the heat."
                show player 13
                show diane f_thinking_back
                dia "Oh, umm..."
                dia "No that's alright."
                show diane f_laugh
                dia "I work better in private."
                show diane f_normal
                show player 14
                player_name "Hmm, okay."
                player_name "I guess I'll leave you too it."
                show player 13
                show diane f_normal_talk
                dia "Thanks, {b}[firstname]{/b}."
                hide player
                hide diane
                with dissolve
                $ game.main()
    else:

        if M_diane.get("seen_shed_locked"):
            call expression game.dialog_select("dianes_shed_seen_shed_locked")
        else:

            call expression game.dialog_select("dianes_shed_not_seen_shed_locked")
            $ M_diane.set("seen_shed_locked", True)
    $ game.main()

label night_closed_garden:
    if M_diane.is_state(S_diane_get_bug_spray, S_diane_clear_bug_infested_garden):
        scene garden_dead_night
    else:
        scene garden_night
    show player 10 with dissolve
    if not M_diane.get("breed first time") and not game.timer.is_night():
        player_name "{b}Diane{/b} said she would be in the {b}barn{/b}."
    else:
        player_name "{b}Diane{/b} is probably asleep... I don't think I can work on the garden right now."
    hide player 2 with dissolve
    return


label diane_house_lock_check(location):
    if location.locked:
        if game.timer.is_dark():
            if location is L_diane_home:
                call expression game.dialog_select("dianes_front_yard_night_locked")
            else:
                call expression game.dialog_select("night_closed_garden")
        else:

            if location is L_diane_kitchen:
                call expression game.dialog_select("dianekitchen_locked")

            elif location is L_diane_home:
                call expression game.dialog_select("dianelobby_locked")

            elif location is L_diane_shed:
                if M_dewitt.is_state(S_dewitt_shed_get_paint):
                    $ game.main(location = location)
                else:
                    jump locked_shed_dialogue

    elif M_diane.is_state(S_diane_check_up_on_garden) and location is L_diane_home:
        call expression game.dialog_select("diane_check_up_on_garden")

    elif M_diane.is_state(S_diane_look_in_kitchen) and player.location is L_diane_garden and location is L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_locked")

    elif M_diane.is_state(S_diane_seen_cucumber) and location is L_diane_kitchen:
        call expression game.dialog_select("dianes_kitchen_busy_masturbating")

    elif M_diane.is_state(S_diane_work_on_garden) and (location is L_diane_home or location is L_diane_kitchen):
        call expression game.dialog_select("diane_attend_to_garden")

    elif M_diane.is_state(S_diane_delivery_2_task, S_diane_delivery_2_fetch_goods, S_diane_delivery_2) and (location is L_diane_home or location is L_diane_kitchen):
        call expression game.dialog_select("diane_tired_from_delivery_upkeep")

    elif M_diane.is_state(S_diane_debbie_drop_off) and location is L_diane_home and game.timer.is_dark():
        call expression game.dialog_select("diane_debbie_drop_off")

    elif M_diane.is_state(S_diane_check_shed_light) and not location is L_diane_shed:
        call expression game.dialog_select("diane_shed_light_on")

    elif M_diane.is_state(S_diane_drunken_garden_work):
        call expression game.dialog_select("diane_day_off_gardening")

    elif M_diane.is_state(S_diane_milking_help) and not (location is L_diane_garden or location is L_diane_shed):
        call expression game.dialog_select("diane_milk_jug_pain")

    elif game.timer.is_dark() and (location is L_diane_home or location is L_diane_kitchen):
        if location is L_diane_home:
            call expression game.dialog_select("dianes_front_yard_night_locked")
        else:
            call expression game.dialog_select("night_closed_garden")
    else:

        if location is L_diane_shed:
            play audio "audio/sfx_door_heavy.ogg"

        elif (not ((player.location is L_diane_kitchen and location is L_diane_home) or
              (player.location is L_diane_home and location is L_diane_kitchen) or
              (player.location is L_diane_yard and location is L_diane_garden) or
              (player.location is L_diane_garden and location is L_diane_yard))):
            play audio sfxDoor()
        $ location.call()
    $ game.main()

label dianes_kitchen_locked:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "Hmm?"
    player_name "It's locked."
    player_name "{b}Diane{/b} never locks this door during the day..."
    show player 34
    player_name "..."
    show player 35
    player_name "I should go try the {b}front door{/b}."
    hide player with dissolve
    return

label dianes_kitchen_busy_masturbating:
    $ M_diane.set("sex speed",0.4)
    show diane_masturbate 1_2
    dia "Ngghhh..."
    dia "Don't stop, stud!"
    pause
    player_name "( I should get out of here before she sees me. )"
    pause
    return

label diane_check_up_on_garden:
    scene expression player.location.background_blur
    show player 30 with dissolve
    player_name "I should {b}check up on the garden.{/b}"
    hide player with dissolve
    return

label diane_attend_to_garden:
    scene expression player.location.background_blur
    show player 79 with dissolve
    player_name "I should {b}get started on the garden.{/b}"
    hide player with dissolve
    return

label diane_tired_from_delivery_upkeep:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "I should let her rest..."
    show player 17
    player_name "... Besides, I have a delivery to make!"
    show player 14
    player_name "I should get the package out of {b}Diane's shed{/b} and {b}deliver it next door.{/b}"
    hide player with dissolve
    return

label diane_debbie_drop_off:
    scene expression player.location.background_blur
    show player 13 with dissolve
    player_name "( ... )"
    pause
    show player 5
    player_name "( Hmm, why isn't she answering the door? )"
    player_name "( Surely she's not still working... )"
    player_name "( ... )"
    player_name "( {b}I'd better check the shed.{/b} )"
    hide player with dissolve
    return

label diane_shed_light_on:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "I need to find {b}Diane{/b}."
    hide player with dissolve
    return

label diane_day_off_gardening:
    scene expression player.location.background_blur
    show player 14 with dissolve
    player_name "{b}I should get started on the garden.{/b}"
    hide player with dissolve
    return

label diane_milk_jug_pain:
    scene expression player.location.background_blur
    show player 10 with dissolve
    player_name "Something is wrong with {b}Diane{/b}!"
    player_name "{b}I've gotta check on her in the shed immediately!{b}"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
