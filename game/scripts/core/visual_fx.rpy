image rain:
    "vfx/vfx_rain_01.png"
    0.1
    "vfx/vfx_rain_02.png"
    0.1
    "vfx/vfx_rain_03.png"
    0.1
    repeat


image shower_running = Fixed(
    'backgrounds/location_home_shower_closeup.jpg', 'shower_water')

image shower_steam = AlphaMask(
    'vfx/steam_mask.png', At('vfx/steam.png', shower_thermals))

image shower_water:
    'vfx/shower_vfx_water01.png'
    0.1
    'vfx/shower_vfx_water02.png'
    0.1
    'vfx/shower_vfx_water03.png'
    0.1
    'vfx/shower_vfx_water04.png'
    0.1
    repeat

transform shower_thermals:
    ytile 2
    block:
        ypos 0
        linear 4 ypos -1.
        repeat

transform shower_zoom:
    align (.335, 1.)
    zoom 2.3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
