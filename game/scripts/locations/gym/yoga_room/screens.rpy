screen yoga_room():
    use mods_screens_hook("yoga_room")

    add game.timer.image("backgrounds/location_gym_yoga_day{}.jpg")

    if player.location.is_here(M_mrsj):
        imagebutton:
            focus_mask True
            pos (660,340)
            idle "objects/character_mrsj_01.png"
            hover HoverImage("objects/character_mrsj_01.png")
            action Hide("yoga_room"), Jump("mrsj_yoga_button_dialogue")

    if player.location.is_here(M_anna):
        imagebutton:
            focus_mask True
            pos (660,340)
            idle "objects/character_anna_02.png"
            hover HoverImage("objects/character_anna_02.png")
            action Hide("yoga_room"), Jump("anna_yoga_button_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_05.png"
        hover HoverImage("boxes/auto_option_05.png")
        action Hide("yoga_room"), Jump("training_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
