screen movie_theatre():
    add L_movie_theatre.background

    if L_movie_theatre.is_here(M_bubbles):
        imagebutton:
            focus_mask True
            pos 396, 299
            idle "objects/character_bubbles_01.png"
            hover HoverImage("objects/character_bubbles_01.png")
            action TalkTo(M_bubbles)

    if L_movie_theatre.can_leave:
        imagebutton:
            focus_mask True
            align 0.5,0.95
            idle "boxes/auto_option_generic_01.png"
            hover HoverImage("boxes/auto_option_generic_01.png")
            action Hide("movie_theatre"), Jump("mall_dialogue")

screen movie_options():
    add "backgrounds/location_mall_movie_options.jpg"

    imagebutton:
        focus_mask True
        pos (30, 146)
        idle "images/buttons/movie_option_01.png"
        hover HoverImage("images/buttons/movie_option_01.png")
        action SelectMovie("foxxy_roxxy")

    imagebutton:
        focus_mask True
        pos (277, 166)
        idle "images/buttons/movie_option_02.png"
        hover HoverImage("images/buttons/movie_option_02.png")
        action SelectMovie("dirty_harold")

    imagebutton:
        focus_mask True
        pos (535, 166)
        idle "images/buttons/movie_option_03.png"
        hover HoverImage("images/buttons/movie_option_03.png")
        action SelectMovie("bitch_perfect")

    imagebutton:
        focus_mask True
        pos (801, 146)
        idle "images/buttons/movie_option_04.png"
        hover HoverImage("images/buttons/movie_option_04.png")
        action SelectMovie("its_a_trap")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
