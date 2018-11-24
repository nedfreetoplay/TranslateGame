screen popup_cookiejar_character_locked:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_cookiejar_character_locked")

    key "K_SPACE" action Hide("popup_cookiejar_character_locked")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_cookie_jar_01.png"
        action Hide("popup_cookiejar_character_locked")

screen popup_cookiejar_scene_locked:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_cookiejar_scene_locked")

    key "K_SPACE" action Hide("popup_cookiejar_scene_locked")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_cookie_jar_02.png"
        action Hide("popup_cookiejar_scene_locked")

screen popup_cookie_jar_reset:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("popup_cookie_jar_reset")

    key "K_SPACE" action Hide("popup_cookie_jar_reset")

    imagebutton:
        focus_mask True
        align (0.5,0.5)
        idle "boxes/popup_cookie_jar_reset.png"
        action Hide("popup_cookie_jar_reset")

    imagebutton:
        focus_mask True
        pos 330,420
        idle "buttons/menu_no.png"
        hover HoverImage("buttons/menu_no.png")
        action Hide("popup_cookie_jar_reset")

    imagebutton:
        focus_mask True
        pos 590,420
        idle "buttons/menu_yes.png"
        hover HoverImage("buttons/menu_yes.png")
        action Function(lock_all_scenes), Hide("popup_cookie_jar_reset")



screen cookie_jar() tag menu:
    imagemap:
        ground "backgrounds/menu_cookie_jar_01.jpg"
        hover HoverImage("backgrounds/menu_cookie_jar_01.jpg")

        hotspot (301,111,170,45) action [Hide("cookie_jar"), Show("main_menu")]
        hotspot (544,111,170,45) action [Show("popup_cookie_jar_reset")]

    default cookie_page = 1
    default cookies_per_page = 28
    default current_cookie = 0
    default start_cookie = 0
    default total_cookies = cookie_page * cookies_per_page
    default cookies = persistent.cookie_jar

    for cookie in cookies:
        $ current_cookie = int(cookies[cookie]["order"]) - 1

        if current_cookie <= total_cookies:
            $ start_xpos = 120
            $ start_ypos = 180
            $ row_ypos = math.trunc(current_cookie / 7)
            $ row_xpos = current_cookie - (row_ypos * 7)
            $ row_ypos -= math.trunc(start_cookie / 7)
            $ start_xpos += 115 * row_xpos
            $ start_ypos += 115 * row_ypos

            imagebutton:
                focus_mask True
                pos (start_xpos,start_ypos)
                if cookies[cookie]["unlocked"]:
                    idle cookies[cookie]["idle"]
                    hover HoverImage(cookies[cookie]["idle"])
                    action Hide("cookie_jar"), ShowMenu("cookie_jar_gallery", cookies[cookie])

                else:
                    idle cookies[cookie]["locked_idle"]
                    hover HoverImage(cookies[cookie]["locked_idle"])
                    action Show("popup_cookiejar_character_locked")

screen cookie_jar_gallery(cookie) tag cookie_jar:
    imagemap:
        ground "backgrounds/menu_cookie_jar_02.jpg"
        hover HoverImage("backgrounds/menu_cookie_jar_02.jpg")

        hotspot (428,111,170,45) action ShowMenu("cookie_jar"), Hide("cookie_jar_gallery")

    default gallery_page = 1
    default galleries_per_page = 20
    default current_gallery = 0
    default start_gallery = 0
    default total_galleries = gallery_page * galleries_per_page
    default galleries = cookie["gallery"]

    for gallery in galleries:
        $ current_gallery = int(gallery[:2]) - 1

        if current_gallery <= total_galleries:
            $ start_xpos = 26
            $ start_ypos = 225
            $ row_ypos = math.trunc(current_gallery / 5)
            $ row_xpos = current_gallery - (row_ypos * 5)
            $ row_ypos -= math.trunc(start_gallery / 5)
            $ start_xpos += 200 * row_xpos
            $ start_ypos += 175 * row_ypos

            imagebutton:
                focus_mask True
                pos (start_xpos,start_ypos)
                if galleries[gallery]:
                    idle cookie["gallery_image"] + gallery[:2] + ".png"
                    hover HoverImage(cookie["gallery_image"] + gallery[:2] + ".png")
                    action With(fade), Function(renpy.call, "replay_INITS", cookie["gallery_labels"][gallery[:2] + "_label"], cookie)

                else:
                    idle "buttons/cookie_jar_box_locked.png"
                    hover HoverImage("buttons/cookie_jar_box_locked.png")
                    action Show("popup_cookiejar_scene_locked")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
