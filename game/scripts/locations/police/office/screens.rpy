screen police_office():
    use mods_screens_hook("police_office")

    add "backgrounds/location_police_office.jpg"

    imagebutton:
        focus_mask True
        pos (669,425)
        idle "objects/character_harold_01_empty.png"
        if M_mia.get_state() == S_mia_search_desk:
            hover HoverImage("objects/character_harold_01_empty.png")
            action Hide("police_office"), Jump("police_harolds_desk")

    if player.location.is_here(M_harold):
        imagebutton:
            focus_mask True
            pos (670,384)
            idle "objects/character_harold_01.png"
            hover HoverImage("objects/character_harold_01.png")
            action Hide("police_office"), Jump("police_harold_dialogue")

    if player.location.is_here(M_earl):
        imagebutton:
            focus_mask True
            pos (280,350)
            idle "objects/character_earl_01.png"
            hover HoverImage("objects/character_earl_01.png")
            action Hide("police_office"), Jump("police_earl_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_13.png"
        hover HoverImage("boxes/auto_option_13.png")
        action Hide("police_office"), Jump("police_lobby_dialogue")

screen harolds_desk():

    imagebutton:
        focus_mask True
        pos (896,628)
        idle PulseHoverImage("objects/object_picture_02.png", delay = 0.5)
        hover HoverImage("objects/object_picture_02.png")
        action Hide("harolds_desk"), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
