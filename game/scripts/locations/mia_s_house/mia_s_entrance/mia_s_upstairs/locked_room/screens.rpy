screen helens_locked_room():
    use mods_screens_hook("helens_locked_room")

    add game.timer.image("backgrounds/location_mia_house_locked_day{}.jpg")

    if M_mia.get_state() == S_mia_locked_room:
        imagebutton:
            focus_mask True
            pos (346,498)
            idle "objects/object_bed_11.png"
            hover HoverImage("objects/object_bed_11.png")
            action Hide("helens_locked_room"), Jump("mia_tied_up")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("helens_locked_room"), Jump("mias_upstairs")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
