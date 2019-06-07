screen cafeteria():
    use mods_screens_hook("cafeteria")

    add game.timer.image("backgrounds/location_school_cafeteria{}.jpg")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/door07_option_01.png"
        hover HoverImage("boxes/door07_option_01.png")
        action Hide("cafeteria"), Jump("stairs_dialogue")

    if player.location.is_here(M_erik):
        imagebutton:
            focus_mask True
            pos (599,424)
            idle "objects/character_erik_04.png"
            hover HoverImage("objects/character_erik_04.png")
            action Hide("cafeteria"), Jump("erik_button_dialogue")

    if player.location.is_here(M_kevin):
        if M_ross.is_state(S_ross_find_magazines):
            imagebutton:
                focus_mask True
                pos (852,391)
                idle "objects/character_kevin_02.png"
                hover HoverImage("objects/character_kevin_02.png")
                action Hide("cafeteria"), Jump("kevin_button_dialogue")

        elif not erik.completed(erik_favor_2):
            imagebutton:
                focus_mask True
                pos (852,391)
                idle "objects/character_kevin_01.png"
                hover HoverImage("objects/character_kevin_01.png")
                action Hide("cafeteria"), Jump("kevin_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (852,391)
                idle "objects/character_kevin_04.png"
                hover HoverImage("objects/character_kevin_04.png")
                action Hide("cafeteria"), Jump("kevin_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
