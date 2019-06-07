screen cellphone():
    imagebutton:
        idle "backgrounds/menu_ground.png"
        pos 0,0
        action Hide("cellphone"), Jump("cellphone_exit")

    imagebutton:
        idle "cellphone/cellphone.png"
        pos 300,80
        action NullAction()

    add CellPhone() pos 300,80

    imagebutton:
        focus_mask True
        pos (397, 126)
        idle "cellphone/cellphone_wifi.png"
        if config.developer or renpy.variant("mobile"):
            action Show("debug_menu", current_screen="general")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
