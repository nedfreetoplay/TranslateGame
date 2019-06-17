label forest_dialogue:
    $ player.go_to(L_forest)
    if L_forest.first_visit:
        call expression game.dialog_select("forest_first_visit")
        $ L_forest.visited()

    if M_anna.is_state(S_anna_find_dog):
        if game.timer.is_dark():
            call expression game.dialog_select("forest_anna_missing_pup_started_dark")

        elif player.has_item("cookies"):
            call expression game.dialog_select("forest_anna_missing_pup_started_have_cookies")
            $ M_anna.set("awesomo lured", True)
            $ player.remove_item("cookies")

        elif not M_anna.get("awesomo lured"):
            call expression game.dialog_select("forest_anna_missing_pup_started_no_cookies")

    if M_okita.is_state(S_okita_get_ingredients) and not player.has_item("mushroom") and not player.has_item("toad"):
        call expression game.dialog_select("forest_okita_get_ingredients")

    if M_dewitt.is_state(S_dewitt_make_new_flute) and not player.has_item("stick"):
        call expression game.dialog_select("forest_dewitt_make_new_flute")
    $ game.main()

label awesomo_dialogue_button:
    scene expression L_forest.background_blur
    call expression game.dialog_select("awesomo_dialogue_intro")
    menu awesomo_dialogue_loop:
        "Дать печеньки.":
            call expression game.dialog_select("awesomo_dialogue_give_cookie")
            jump expression game.dialog_select("awesomo_dialogue_loop")
        "Проверить имя.":

            call expression game.dialog_select("awesomo_dialogue_check_name_tag_pre")
            $ awesomo = Character("Awesomo")
            call expression game.dialog_select("awesomo_dialogue_check_name_tag_after")
            $ player.get_item("dog")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
