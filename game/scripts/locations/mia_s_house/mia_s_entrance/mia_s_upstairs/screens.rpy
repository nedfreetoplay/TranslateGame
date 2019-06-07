screen mias_house_upstairs():
    use mods_screens_hook("mias_house_upstairs")

    add game.timer.image("backgrounds/location_mia_house_upstairs_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (444,419)
        idle game.timer.image("objects/object_door_33{}.png")
        hover HoverImage(game.timer.image("objects/object_door_33{}.png"))
        action Hide("mias_house_upstairs"), Jump("mias_bedroom_screen")

    imagebutton:
        focus_mask True
        pos (615,337)
        idle game.timer.image("objects/object_door_92{}.png")
        hover HoverImage(game.timer.image("objects/object_door_92{}.png"))
        action Hide("mias_house_upstairs"), Jump("helens_bedroom")

    imagebutton:
        focus_mask True
        pos (257,238)
        idle game.timer.image("objects/object_door_93{}.png")
        hover HoverImage(game.timer.image("objects/object_door_93{}.png"))
        action Hide("mias_house_upstairs"), If(M_mia.is_set('helens locked room locked'), Jump("helens_locked_room_block"), Jump("helens_locked_room"))

    imagebutton:
        focus_mask True
        pos (758,110)
        idle game.timer.image("objects/object_door_94{}.png")
        hover HoverImage(game.timer.image("objects/object_door_94{}.png"))
        action Hide("mias_house_upstairs"), Jump("harolds_office")

    imagebutton:
        focus_mask True
        pos (0,0)
        idle game.timer.image("objects/object_door_95{}.png")
        hover HoverImage(game.timer.image("objects/object_door_95{}.png"))
        action Hide("mias_house_upstairs"), Jump("mias_entrance")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
