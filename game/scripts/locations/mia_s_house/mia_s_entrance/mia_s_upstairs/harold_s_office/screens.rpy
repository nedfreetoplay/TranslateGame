screen harolds_house_office():
    use mods_screens_hook("harolds_house_office")

    add game.timer.image("backgrounds/location_mia_house_office_day{}.jpg")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("harolds_house_office"), Jump("mias_upstairs")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
