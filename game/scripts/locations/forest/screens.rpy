init python:
    def piece_dragged(drags, drop):
        store.movedpiece = int(drags[0].drag_name[6:])
        
        if drags[0].x > 112 and drags[0].x < 212 and drags[0].y > 93 and drags[0].y < 193:
            if ([162,143] in piecelist):
                occupied = store.piecelist.index([162,143])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [162,143]
        
        elif drags[0].x > 332 and drags[0].x < 432 and drags[0].y >= 0 and drags[0].y < 70:
            if ([382,20] in piecelist):
                occupied = store.piecelist.index([382,20])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [382,20]
        
        elif drags[0].x > 550 and drags[0].x < 650 and drags[0].y > 89 and drags[0].y < 189:
            if ([600,139] in piecelist):
                occupied = store.piecelist.index([600,139])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [600,139]
        
        elif drags[0].x > 333 and drags[0].x < 433 and drags[0].y > 213 and drags[0].y < 313:
            if ([383,263] in piecelist):
                occupied = store.piecelist.index([383,263])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [383,263]
        
        elif drags[0].x > 113 and drags[0].x < 213 and drags[0].y > 335 and drags[0].y < 435:
            if ([163,385] in piecelist):
                occupied = store.piecelist.index([163,385])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [163,385]
        
        elif drags[0].x > 553 and drags[0].x < 653 and drags[0].y > 337 and drags[0].y < 437:
            if ([603,387] in piecelist):
                occupied = store.piecelist.index([603,387])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [603,387]
        
        elif drags[0].x > 334 and drags[0].x < 434 and drags[0].y > 466 and drags[0].y < 566:
            if ([384,516] in piecelist):
                occupied = store.piecelist.index([384,516])
                store.piecelist[occupied] = renpy.random.choice([[-60,580],[830,580]])
            
            store.piecelist[movedpiece] = [384,516]
        
        elif drags[0].x < 50 and drags[0].y > 530:
            store.piecelist[movedpiece] = [-60,580]
        
        elif drags[0].x > 780 and drags[0].y > 530:
            store.piecelist[movedpiece] = [830,580]
        
        else:
            store.piecelist[movedpiece] = renpy.random.choice([[-60,580],[830,580]])
        
        return True

screen forest():
    use mods_screens_hook("forest")

    add game.timer.image("backgrounds/location_forest_day{}.jpg")

    if not game.timer.is_dark():
        if M_anna.is_state(S_anna_find_dog):
            if M_anna.get("awesomo lured") and not player.has_item("dog"):
                imagebutton:
                    focus_mask True
                    pos (576,630)
                    idle "objects/character_awesomo_02.png"
                    hover HoverImage("objects/character_awesomo_02.png")
                    action Hide("forest"), Jump("awesomo_dialogue_button")

        if not player.has_picked_up_item("worm"):
            imagebutton:
                focus_mask True
                pos (184,708)
                idle "objects/object_dirt_01.png"
                hover HoverImage("objects/object_dirt_01.png")
                action Hide("forest"), Jump("dirt_pile")

    if M_aqua.is_set("altar search"):
        imagebutton:
            focus_mask True
            pos (314,594)
            idle game.timer.image("objects/object_rocks_01{}.png")
            hover HoverImage(game.timer.image("objects/object_rocks_01{}.png"))
            action Hide("forest"), With(fade), Jump("altar")

    if (M_okita.is_state(S_okita_get_ingredients) or M_aqua.is_state(S_aqua_seasucc_mushroom)) and not player.has_item("mushroom"):
        imagebutton:
            focus_mask True
            pos (844,647)
            idle game.timer.image("objects/object_mushroom_01{}.png")
            hover HoverImage(game.timer.image("objects/object_mushroom_01{}.png"))
            action Hide("forest"), Jump("mushroom")

    imagebutton:
        focus_mask True
        pos (130,469)
        idle game.timer.image("objects/object_waterfall_01{}.png")
        hover HoverImage(game.timer.image("objects/object_waterfall_01{}.png"))
        action Hide("forest"), Jump("waterfall_dialogue")

screen forest_worms():
    imagebutton:
        focus_mask True
        pos (313,269)
        idle "objects/object_worms_01.png"
        hover HoverImage("objects/object_worms_01.png")
        action Function(player.get_item, "worm"), Show('popup', None, "boxes/popup_item_worm1.png"), Hide("forest_worms"), Function(player.location.call_screen, new_context = True)

screen altar_puzzle_finish():
    add game.timer.image("location_forest_puzzle_day{}")

    imagebutton:
        focus_mask True
        align (0.473,0.44)
        idle "objects/object_map_01.png"
        hover HoverImage("objects/object_map_01.png")
        action Hide("altar_puzzle_finish"), Jump("altar_puzzle_finish")

screen altar_puzzle():
    add "backgrounds/location_forest_puzzle_night_closed.jpg"

    imagebutton:
        focus_mask True
        align (0.96,0.08)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("altar_puzzle"), Jump("altar_puzzle_leave")

    draggroup:

        drag:
            drag_name "Middle Groove"

            draggable False
            xpos 150 ypos 130

        drag:
            drag_name "Piece 01"
            child "buttons/puzzle_piece_01.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]

        drag:
            drag_name "Piece 02"
            child "buttons/puzzle_piece_02.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]

        drag:
            drag_name "Piece 03"
            child "buttons/puzzle_piece_03.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]

        drag:
            drag_name "Piece 04"
            child "buttons/puzzle_piece_04.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]

        drag:
            drag_name "Piece 05"
            child "buttons/puzzle_piece_05.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]

        drag:
            drag_name "Piece 06"
            child "buttons/puzzle_piece_06.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]

        drag:
            drag_name "Piece 07"
            child "buttons/puzzle_piece_07.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[7][0] ypos piecelist[7][1]

        drag:
            drag_name "Piece 08"
            child "buttons/puzzle_piece_08.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[8][0] ypos piecelist[8][1]

        drag:
            drag_name "Piece 09"
            child "buttons/puzzle_piece_09.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[9][0] ypos piecelist[9][1]

        drag:
            drag_name "Piece 10"
            child "buttons/puzzle_piece_10.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[10][0] ypos piecelist[10][1]

        drag:
            drag_name "Piece 11"
            child "buttons/puzzle_piece_11.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[11][0] ypos piecelist[11][1]

        drag:
            drag_name "Piece 12"
            child "buttons/puzzle_piece_12.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[12][0] ypos piecelist[12][1]

        drag:
            drag_name "Piece 13"
            child "buttons/puzzle_piece_13.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[13][0] ypos piecelist[13][1]

        drag:
            drag_name "Piece 14"
            child "buttons/puzzle_piece_14.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[14][0] ypos piecelist[14][1]

        drag:
            drag_name "Piece 15"
            child "buttons/puzzle_piece_15.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[15][0] ypos piecelist[15][1]

        drag:
            drag_name "Piece 16"
            child "buttons/puzzle_piece_16.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[16][0] ypos piecelist[16][1]

        drag:
            drag_name "Piece 17"
            child "buttons/puzzle_piece_17.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[17][0] ypos piecelist[17][1]

        drag:
            drag_name "Piece 18"
            child "buttons/puzzle_piece_18.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[18][0] ypos piecelist[18][1]

        drag:
            drag_name "Piece 19"
            child "buttons/puzzle_piece_19.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[19][0] ypos piecelist[19][1]

        drag:
            drag_name "Piece 20"
            child "buttons/puzzle_piece_20.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[20][0] ypos piecelist[20][1]

        drag:
            drag_name "Piece 21"
            child "buttons/puzzle_piece_21.png"
            droppable False
            dragged piece_dragged
            xpos piecelist[21][0] ypos piecelist[21][1]

        drag:
            drag_name "Piece 22"
            child "buttons/puzzle_piece_22.png"
            droppable True
            dragged piece_dragged
            xpos piecelist[22][0] ypos piecelist[22][1]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
