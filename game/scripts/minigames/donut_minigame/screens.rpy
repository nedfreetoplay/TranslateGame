screen donut_minigame():
    add "backgrounds/location_donut_minigame.jpg"
    add FilteredText("Выберите один тип глазури и начинки!", style="style_instructions") align .5, .075

    default topping_name = ""
    default topping_xpos = 0
    default glaze_name = ""
    default glaze_xpos = 0

    imagebutton:
        focus_mask True
        pos (65,151)
        idle "buttons/donut_01.png"
        hover HoverImage("buttons/donut_01.png")
        action SetScreenVariable("topping_name", "chocolate chips"), SetScreenVariable("topping_xpos", 59)

    imagebutton:
        focus_mask True
        pos (295,151)
        idle "buttons/donut_02.png"
        hover HoverImage("buttons/donut_02.png")
        action SetScreenVariable("topping_name", "sprinkles"), SetScreenVariable("topping_xpos", 289)

    imagebutton:
        focus_mask True
        pos (524,151)
        idle "buttons/donut_03.png"
        hover HoverImage("buttons/donut_03.png")
        action SetScreenVariable("topping_name", "vanilla drizzle"), SetScreenVariable("topping_xpos", 518)

    imagebutton:
        focus_mask True
        pos (755,151)
        idle "buttons/donut_04.png"
        hover HoverImage("buttons/donut_04.png")
        action SetScreenVariable("topping_name", "maple drizzle"), SetScreenVariable("topping_xpos", 749)

    if topping_name != "":
        imagebutton:
            focus_mask True
            pos (topping_xpos,145)
            idle "buttons/donut_selection.png"

    imagebutton:
        focus_mask True
        pos (65,430)
        idle "buttons/donut_05.png"
        hover HoverImage("buttons/donut_05.png")
        action SetScreenVariable("glaze_name", "strawberry glazed"), SetScreenVariable("glaze_xpos", 59)

    imagebutton:
        focus_mask True
        pos (295,430)
        idle "buttons/donut_06.png"
        hover HoverImage("buttons/donut_06.png")
        action SetScreenVariable("glaze_name", "chocolate glazed"), SetScreenVariable("glaze_xpos", 289)

    imagebutton:
        focus_mask True
        pos (524,430)
        idle "buttons/donut_07.png"
        hover HoverImage("buttons/donut_07.png")
        action SetScreenVariable("glaze_name", "blueberry glazed"), SetScreenVariable("glaze_xpos", 518)

    imagebutton:
        focus_mask True
        pos (755,430)
        idle "buttons/donut_08.png"
        hover HoverImage("buttons/donut_08.png")
        action SetScreenVariable("glaze_name", "vanilla glazed"), SetScreenVariable("glaze_xpos", 749)

    if glaze_name != "":
        imagebutton:
            focus_mask True
            pos (glaze_xpos,424)
            idle "buttons/donut_selection.png"

    if topping_name != "" and glaze_name != "":
        imagebutton:
            focus_mask True
            pos (409,676)
            idle "buttons/shop_button_50.png"
            hover HoverImage("buttons/shop_button_50.png")
            action Hide("donut_minigame"), If(topping_name == M_harold.get("topping") and glaze_name == M_harold.get("glaze"), Function(player.get_item, "donuts_correct"), Function(player.get_item, "donuts_fail")), Jump("donut_buy_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
