transform credit_scroll:
    xalign 0.0 yalign 0.0
    linear 20.0 yalign 1.



transform flip:
    xzoom -1

transform unflip:
    xzoom 1

transform lright:
    unflip
    xcenter .5

transform lcenter:
    unflip
    xcenter .25

transform lleft:
    unflip
    xcenter 0

transform fliplright:
    flip
    xcenter 1.0

transform fliplleft:
    flip
    xcenter .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
