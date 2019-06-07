screen coach_bridgets_office():
    use mods_screens_hook("coach_bridgets_office")

    add game.timer.image("backgrounds/location_school_gym_office_day{}.jpg")

    if M_bissette.get_state() == S_bissette_roxxy_pom_poms and player.has_item("pompoms"):
        add Timer("backgrounds/location_school_gym_office_minigame.jpg", "coach_bridgets_office", "coachs_office_locker_hide_fail", 5)

    imagebutton:
        focus_mask True
        pos (0,261)
        idle game.timer.image("objects/object_locker_11{}.png")
        hover HoverImage(game.timer.image("objects/object_locker_11{}.png"))
        action Hide("coach_bridgets_office"), Jump("coach_locker_dialogue")

    if player.location.is_here(M_bridget):
        imagebutton:
            focus_mask True
            pos (183,386)
            idle "objects/character_coach_02.png"
            hover HoverImage("objects/character_coach_02.png")
            action Hide("coach_bridgets_office"), Jump("coach_button_dialogue")

    imagebutton:
        focus_mask True
        pos (495,497)
        idle game.timer.image("objects/object_table_04{}.png")

        action NullAction()


    if M_bissette.get_state() != S_bissette_roxxy_pom_poms or not player.has_item("pompoms"):
        imagebutton:
            focus_mask True
            align (0.5,0.97)
            idle "boxes/auto_option_generic_02.png"
            hover HoverImage("boxes/auto_option_generic_02.png")
            action Hide("coach_bridgets_office"), Jump("right_hall_dialogue")

screen coachs_locker():
    add "coach_locker"

    if M_bissette.get_state() == S_bissette_roxxy_pom_poms:
        imagebutton:
            focus_mask True
            pos (431,62)
            idle "objects/object_pompom_01.png"
            hover HoverImage("objects/object_pompom_01.png")
            action Hide("coachs_locker"), Jump("coach_locker_pom_poms")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_02.png"
        hover HoverImage("boxes/auto_option_generic_02.png")
        action Hide("coachs_locker"), Jump("coach_office_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
