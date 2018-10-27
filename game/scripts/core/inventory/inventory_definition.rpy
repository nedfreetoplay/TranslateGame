label INIT_INVENTORY_ITEMS:
    python hide:
        json_file = renpy.file("scripts/data/items.json")
        store.items = json.load(json_file)
        json_file.close()

    python:
        sea_dogs_saga = ComicItem("game", "ПК игра - Sea Dogs Saga", "", "boxes/popup_item_game.png", Transform("game_1"), Transform("game_1b"), 100, "Video Games", False)
        world_of_orcette = ComicItem("game02", "ПК игра - World of Orcette", "", "boxes/popup_item_game2.png", Transform("game_2"), Transform("game_2b"), 100, "Video Games", False)
        orcette_outfit = ComicItem("orcette_cosplay", "Косплей Костюм - Orcette Queen", "", "boxes/popup_cosplay.png", Transform("cosplay_1"), Transform("cosplay_1b"), 300, "Cosplay", False)
        cock_goblin = ComicItem("card01", "Карточка для обмена - The Flying Cock Goblin", "objects/closeup_card01.png", "boxes/popup_item_card1.png", "objects/item_card1.png", HoverImage("objects/item_card1.png"), 50, "Collectible", False)
        cock_crown = ComicItem("card02", "Карточка для обмена - Cock Crown of Thorns", "objects/closeup_card02.png", "boxes/popup_item_card2.png", Transform("card_2"), Transform("card_2b"), 50, "Collectible", False)

        comicstore = ComicStore()
        comicstore.items = [cock_goblin, sea_dogs_saga, world_of_orcette, cock_crown, orcette_outfit]

        red_corset_lingerie = PinkItem("red_corset", "Красный корсет", "", "boxes/pink_item_15.png", Transform("sex_17"), Transform("sex_17b"), 300, "Lingerie", False)
        cow_outfit_lingerie = PinkItem("cow_outfit", "Коровий косплей", "", "boxes/pink_item_16.png", Transform("sex_6"), Transform("sex_6b"), 300, "Lingerie", False)

        pinkstore = PinkStore()
        pinkstore.items = [red_corset_lingerie, cow_outfit_lingerie]
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
