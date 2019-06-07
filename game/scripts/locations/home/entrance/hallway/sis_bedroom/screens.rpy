screen upstairs_bedroom():
    use mods_screens_hook("upstairs_bedroom")

    add game.timer.image("backgrounds/location_home_jennybedroom_day{}.jpg")


    if not L_home_sisbedroom.is_here(M_jenny) or not M_jenny.finished_state(S_jenny_start_camshow_handjob) or M_jenny.pregnancy or game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (82,435)
            idle game.timer.image("objects/object_desk_02{}.png")
            hover HoverImage(game.timer.image("objects/object_desk_02{}.png"))
            action Show("desk02_options")
    elif (player.location.is_here(M_jenny) and game.timer.is_day() and not M_jenny.finished_state(S_jenny_start_camshow_handjob)):
        imagebutton:
            focus_mask True
            pos (82,435)
            idle game.timer.image("objects/object_desk_02{}.png")
            action NullAction()


    if M_jenny.finished_state(S_jenny_pics_afterthought):
        imagebutton:
            focus_mask True
            pos (865,483)
            idle game.timer.image("objects/object_bedtable_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bedtable_01{}.png"))
            action Show("bedtable01_options")
    else:
        imagebutton:
            focus_mask True
            pos (865, 483)
            idle game.timer.image("objects/object_bedtable_01{}.png")
            action NullAction()


    if L_home_sisbedroom.can_leave:
        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/auto_option_01.png"
            hover HoverImage("boxes/auto_option_01.png")
            action Hide("upstairs_bedroom"), Jump("hallway_dialogue")












    if player.location.is_here(M_jenny) and game.timer.is_night():


        imagebutton:
            focus_mask True
            pos (362,416)
            idle game.timer.image("characters/jenny/buttons/object_bed_02{}.png")
            hover HoverImage(game.timer.image("characters/jenny/buttons/object_bed_02{}.png"))
            action Hide("upstairs_bedroom"), Jump("jenny_bed_night_button")

    elif player.location.is_here(M_jenny) or M_jenny.pregnancy.gave_birth:
        if M_jenny.finished_state(S_jenny_start_camshow_handjob) and not M_jenny.pregnancy and game.timer.is_day():
            $ img_i = "characters/jenny/buttons/character_jenny_03.png"
            $ img_h = HoverImage("characters/jenny/buttons/character_jenny_03.png")
            $ img_x = 580
            $ img_y = 420

        elif M_jenny.pregnancy:
            $ img_i = "characters/jenny/buttons/character_jenny_01[M_jenny.pregnancy.to_full_string].png"
            $ img_h = HoverImage("characters/jenny/buttons/character_jenny_01{}.png".format(M_jenny.pregnancy.to_full_string))
            $ img_x = 660
            $ img_y = 320

        elif game.timer.is_evening():
            $ img_i = "characters/jenny/buttons/character_jenny_02_evening.png"
            $ img_h = HoverImage("characters/jenny/buttons/character_jenny_02_evening.png")
            $ img_x = 598
            $ img_y = 390

        else:
            $ img_i = "characters/jenny/buttons/character_jenny_02.png"
            $ img_h = HoverImage("characters/jenny/buttons/character_jenny_02.png")
            $ img_x = 598
            $ img_y = 390

        imagebutton:
            focus_mask True
            pos (img_x, img_y)
            idle img_i
            hover img_h
            action TalkTo(M_jenny)


    elif not L_home_sisbedroom.is_here(M_jenny) and game.timer.is_day():
        imagebutton:
            focus_mask True
            pos (610,520)

            idle "objects/object_diary_item01.png"
            hover HoverImage("objects/object_diary_item01.png")
            action Hide("upstairs_bedroom"), Show("jenny_diary")

screen sisbed_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("sisbed_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bed02_option_01.png"
        hover HoverImage("boxes/bed02_option_01.png")
        action Hide("sisbed_options"), Hide("upstairs_bedroom"), Jump("sneak_in_sis_bed")

screen desk02_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk02_options")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/desk02_option_01.png"
        hover HoverImage("boxes/desk02_option_01.png")
        action Hide("desk02_options"), Hide("upstairs_bedroom"), Jump("upstairs_bedroom_enter_laptop")

screen bedtable01_options():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("desk04_options")
    imagebutton:
        focus_mask True
        pos (350,600)
        idle "boxes/bedtable01_option_01.png"
        hover HoverImage("boxes/bedtable01_option_01.png")
        action (Hide("bedtable01_options"),
                Hide("upstairs_bedroom"),
                Jump("bedside01_dialogue"))

screen bedside01():
    add "backgrounds/location_home_jennytable.jpg"
    if not player.has_picked_up_item("jenny_panties"):
        imagebutton:
            focus_mask True
            pos (382,302)
            idle "objects/object_panties_01.png"
            hover HoverImage("objects/object_panties_01.png")
            action Hide("bedside01"), Jump("sis_panties_dialogue")
    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("bedside01"), Jump("jenny_out_of_bedside_table")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
