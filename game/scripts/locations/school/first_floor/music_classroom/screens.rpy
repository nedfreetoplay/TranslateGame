screen music_classroom():
    use mods_screens_hook("music_classroom")

    add game.timer.image("backgrounds/location_school_music_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (406,295)
        idle game.timer.image("objects/object_door_61{}.png")
        hover HoverImage(game.timer.image("objects/object_door_61{}.png"))
        action Hide("music_classroom"), Play("audio", sfxDoor()), Jump("school_dialogue")

    if M_dewitt.is_state(S_dewitt_find_flute):
        imagebutton:
            focus_mask True
            pos (531,260)
            idle "objects/object_cabinet_03.png"
            hover HoverImage("objects/object_cabinet_03.png")
            action Hide("music_classroom"), Jump("music_classroom_music_sheet")

    if player.location.is_here(M_dewitt):
        imagebutton:
            focus_mask True
            pos (178,343)
            idle "objects/character_dewitt_01.png"
            hover HoverImage("objects/character_dewitt_01.png")
            action Hide("music_classroom"), Jump("dewitt_button_dialogue")

    if player.location.is_here(M_annie):
        imagebutton:
            focus_mask True
            pos (814, 441)
            idle "objects/character_annie_02.png"
            hover HoverImage("objects/character_annie_02.png")
            action Hide("music_classroom"), Jump("annie_button_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
