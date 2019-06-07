screen mias_house_entrance():
    use mods_screens_hook("mias_house_entrance")

    if M_mia.is_set('harold left') and game.timer.is_dark():
        add "backgrounds/location_mia_house_without_night.jpg"

    else:
        add game.timer.image("backgrounds/location_mia_house_day{}.jpg")

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (280,330)
            idle "objects/character_mia_01c.png"
            hover HoverImage("objects/character_mia_01c.png")
            action Hide("mias_house_entrance"), Jump("mia_button_dialogue")

    imagebutton:
        focus_mask True
        pos (531,267)
        idle game.timer.image("objects/object_stairs_05{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_05{}.png"))
        action Hide("mias_house_entrance"), Jump("mias_upstairs")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action Hide("mias_house_entrance"), If(M_mia.get_state() == S_mia_unexpected_visit and game.timer.is_afternoon(), Jump("helen_masturbating_block"), Jump("mias_house_dialogue"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
