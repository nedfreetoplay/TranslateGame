screen bedroom:
    if MC_computer_broken:
        add game.timer.image("backgrounds/location_home_bedroom_broken{}.jpg")
    else:
        add game.timer.image("backgrounds/location_home_bedroom{}.jpg")

    imagebutton:
        focus_mask True
        pos (44,352)
        idle game.timer.image("objects/object_telescope_01{}.png")
        hover HoverImage(game.timer.image("objects/object_telescope_01{}.png"))
        action Hide("bedroom"), Function(renpy.call, "home_lock_check", "Telescope", "telescope")

    imagebutton:
        focus_mask True
        pos (225,187)
        idle game.timer.image("objects/object_door_01{}.png")
        hover HoverImage(game.timer.image("objects/object_door_01{}.png"))
        action Hide("bedroom"), Function(renpy.call, "home_lock_check", "Hallway", "hallway_dialogue")

    imagebutton:
        focus_mask True
        pos (445,336)
        if M_mom.get_state() == S_mom_note:
            idle "objects/object_desk_01_note.png"
            hover HoverImage("objects/object_desk_01_note.png")

        elif MC_computer_broken:
            idle game.timer.image("objects/object_desk_broken_01{}.png")
            hover HoverImage(game.timer.image("objects/object_desk_broken_01{}.png"))

        else:
            idle game.timer.image("objects/object_desk_01{}.png")
            hover HoverImage(game.timer.image("objects/object_desk_01{}.png"))
        if M_mom.get_state() == S_mom_note:
            action Hide("bedroom"), Jump("M6_note")

        else:
            action If(
                      MC_computer_broken,
                      Show ("desk01_options"),
                      [Hide("bedroom"), Function(renpy.call, "home_lock_check", "MC Computer", "MC_computer")]
            )

    if player.location.is_here(M_june):
        imagebutton:
            focus_mask True
            pos (670,350)
            idle "images/objects/character_june_02.png"
            hover HoverImage("images/objects/character_june_02.png")
            action Hide("bedroom"), Jump("june_bedroom_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (639,439)
            idle game.timer.image("objects/object_bed_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bed_01{}.png"))
            action If(
                      M_mia.get_state() == S_mia_midnight_help,
                      [Hide("bedroom"), Jump("mia_midnight_text")],
                      Show("bed01_options")
            )

    if not player.has_picked_up_item("cookies"):
        imagebutton:
            focus_mask True
            pos (30,630)
            idle game.timer.image("objects/object_cookies_01{}.png")
            hover HoverImage(game.timer.image("objects/object_cookies_01{}.png"))
            action Function(player.get_item, "cookies"), Hide("bedroom"), Jump("cookies")

    if M_player.is_set("pet cat"):
        imagebutton:
            focus_mask True
            pos (350,670)
            idle game.timer.image("objects/character_cat_01{}.png")
            hover HoverImage(game.timer.image("objects/character_cat_01{}.png"))
            action Hide("bedroom"), Jump("pet_cat")

screen desk01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action [Hide("desk01_options")]

    imagebutton:
        idle "boxes/desk01_option_03.png"
        hover HoverImage("boxes/desk01_option_03.png")
        action If(player.has_item("parts"), [SetVariable("MC_computer_broken", False), (Function(player.remove_item, "parts"), Hide("desk01_options"), Show("popup_repaired01"))], (Hide("desk01_options"), Show("popup_broken")))
        xpos 350
        ypos 600

screen popup_broken:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_broken")

    imagebutton:
        idle "boxes/popup_broken_comp.png"
        action Hide("popup_broken")
        xpos 280
        ypos 360

screen popup_repaired01:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_repaired01")

    imagebutton:
        idle "boxes/popup_broken_comp2.png"
        action Hide("popup_repaired01")
        xpos 280
        ypos 360

screen bed01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bed01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/bed01_option_01.png"
        hover HoverImage("boxes/bed01_option_01.png")
        action If(M_mom.is_state(S_mom_debt_call),
                  [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                  If(game.sleep_lock,
                     [Hide("bed01_options"), Hide("bedroom"), Jump("bed_locked")],
                     [Hide("bed01_options"), Hide("bedroom"), Jump("sleeping")]
                  )
        )

    if player.has_jerk_available() and not game.timer.is_night():
        imagebutton:
            focus_mask True
            align (0.5,0.9)
            idle "boxes/bed01_option_02.png"
            hover HoverImage("boxes/bed01_option_02.png")
            action If(M_mom.is_state(S_mom_debt_call),
                      [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                      If(game.sleep_lock and not M_diane.is_state(S_diane_peeking_masturbate),
                         [Hide("bed01_options"), Hide("bedroom"), Jump("bed_locked")],
                         [Hide("bed01_options"), Hide("bedroom"), Jump("jerking_off_dialogue")]
                      )
            )

screen june_mcbedroom_normal_sex_options:
    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("june_mcbedroom_normal_sex_options"), Jump("june_bedroom_dialogue_normal_sex_cum_inside")

    if M_june.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("june_mcbedroom_normal_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") + 0.1), Jump("june_bedroom_dialogue_normal_sex_loop")

    if M_june.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("june_mcbedroom_normal_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") - 0.1), Jump("june_bedroom_dialogue_normal_sex_loop")

screen june_mcbedroom_cosplay_sex_options:
    imagebutton:
        focus_mask True
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_loop")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_cum_outside")

    imagebutton:
        focus_mask True
        pos (550,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("june_mcbedroom_cosplay_sex_options"), Jump("june_bedroom_dialogue_cosplay_sex_cum_inside")

    if M_june.get("sex speed") < .3:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("june_mcbedroom_cosplay_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") + 0.1), Jump("june_bedroom_dialogue_cosplay_sex_loop")

    if M_june.get("sex speed") > .11:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("june_mcbedroom_cosplay_sex_options"), Function(M_june.set, "sex speed", M_june.get("sex speed") - 0.1), Jump("june_bedroom_dialogue_cosplay_sex_loop")

screen bedroom_debbie_sleepover_options:

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("bedroom_debbie_sleepover_options"), Jump("bedroom_debbie_sleepover_loop")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("bedroom_debbie_sleepover_options"), Jump("bedroom_debbie_sleepover_cum")
        xpos 450
        ypos 700

    imagebutton:
        pos (370,665)
        idle "buttons/diane_stage01_04.png"
        hover HoverImage("buttons/diane_stage01_04.png")
        action Hide("bedroom_debbie_sleepover_options"), Function(M_mom.toggle, "change angle"), SetVariable("animated", False), Jump("bedroom_debbie_sleepover_loop")

    if M_mom.get('sex speed') < .12:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("bedroom_debbie_sleepover_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.03), Jump("bedroom_debbie_sleepover_loop")
            xpos 250
            ypos 735

    if M_mom.get('sex speed') > .061:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("bedroom_debbie_sleepover_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.03), Jump("bedroom_debbie_sleepover_loop")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
