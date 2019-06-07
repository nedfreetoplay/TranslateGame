screen fancy_menu():
    add 'backgrounds/menu_menu.jpg'
    add 'menu_cloud_large' id 'cloud_large'
    add 'menu_cloud_small' id 'cloud_small'
    add SnowBlossom(Animation('buttons/leaf01.png', 0.15,
                              'buttons/leaf02.png', 0.15)) id 'leaves'
    add 'backgrounds/menu_menu_overlay.png'

    fixed:
        transclude
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
