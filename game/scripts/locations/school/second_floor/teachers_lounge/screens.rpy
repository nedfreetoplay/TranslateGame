screen teachers_lounge():
    use mods_screens_hook("teachers_lounge")

    add game.timer.image("backgrounds/location_school_lounge_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (61,208)
        idle game.timer.image("objects/object_door_102{}.png")
        hover HoverImage(game.timer.image("objects/object_door_102{}.png"))
        action Hide("teachers_lounge"), Jump("stairs_dialogue")

    imagebutton:
        focus_mask True
        pos (244,457)
        idle game.timer.image("objects/object_microwave_01{}.png")
        hover HoverImage(game.timer.image("objects/object_microwave_01{}.png"))
        action Hide("teachers_lounge"), Jump("microwave_dialogue")

    if M_okita.is_state(S_okita_dose_smith):
        imagebutton:
            focus_mask True
            pos (349,435)
            idle game.timer.image("objects/object_coffee01{}.png")
            hover HoverImage(game.timer.image("objects/object_coffee01{}.png"))
            action Hide("teachers_lounge"), Jump("coffee_pot_dialogue")

    if player.location.is_here(M_dewitt):
        imagebutton:
            focus_mask True
            pos (599,414)
            idle "objects/character_dewitt_03.png"
            hover HoverImage("objects/character_dewitt_03.png")
            action Hide("teachers_lounge"), Jump("dewitt_button_dialogue_lounge")

    elif player.location.is_here(M_smith):
        imagebutton:
            focus_mask True
            pos (620,409)
            idle "objects/character_smith_01.png"
            hover HoverImage("objects/character_smith_01.png")
            action Hide("teachers_lounge"), Jump("smith_lounge_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
