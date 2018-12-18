label INIT_INVENTORY_ITEMS:
    python hide:
        json_file = renpy.file("scripts/data/items.json")
        store.items = json.load(json_file)
        json_file.close()

    python:
        sea_dogs_saga = ComicItem("game", "PC Game - Sea Dogs Saga", "", "boxes/popup_item_game.png", Transform("game_1"), Transform("game_1b"), 100, "Video Games", False)
        world_of_orcette = ComicItem("game02", "PC Game - World of Orcette", "", "boxes/popup_item_game2.png", Transform("game_2"), Transform("game_2b"), 100, "Video Games", False)
        orcette_outfit = ComicItem("orcette_cosplay", "Cosplay Outfit - Orcette Queen", "", "boxes/popup_cosplay.png", Transform("cosplay_1"), Transform("cosplay_1b"), 300, "Cosplay", False)
        cock_goblin = ComicItem("card01", "Trading Card - The Flying Cock Goblin", "objects/closeup_card01.png", "boxes/popup_item_card1.png", "objects/item_card1.png", HoverImage("objects/item_card1.png"), 50, "Collectible", False)
        cock_crown = ComicItem("card02", "Trading Card - Cock Crown of Thorns", "objects/closeup_card02.png", "boxes/popup_item_card2.png", Transform("card_2"), Transform("card_2b"), 50, "Collectible", False)

        comicstore = ComicStore()
        comicstore.items = [cock_goblin, sea_dogs_saga, world_of_orcette, cock_crown, orcette_outfit]

        red_corset_lingerie = PinkItem("red_corset", "Red Corset", "", "boxes/pink_item_15.png", Transform("sex_17"), Transform("sex_17b"), 300, "Lingerie", False)
        cow_outfit_lingerie = PinkItem("cow_outfit", "Cow Outfit", "", "boxes/pink_item_16.png", Transform("sex_6"), Transform("sex_6b"), 300, "Lingerie", False)

        pinkstore = PinkStore()
        pinkstore.items = [red_corset_lingerie, cow_outfit_lingerie]

        plush1 = CupidItem("plush_1", "Plush - Awesomo", "Plushes")
        plush2 = CupidItem("plush_2", "Plush - Pinguin", "Plushes")
        plush3 = CupidItem("plush_3", "Plush - Kitty", "Plushes")
        plush4 = CupidItem("plush_4", "Plush - Cow", "Plushes")
        plush5 = CupidItem("plush_5", "Plush - Beaver", "Plushes")
        plush6 = CupidItem("plush_6", "Plush - Rabbit", "Plushes")
        plush7 = CupidItem("plush_7", "Plush - Unicorn", "Plushes")
        plush8 = CupidItem("plush_8", "Plush - Orcette", "Plushes")
        plush9 = CupidItem("plush_9", "Plush - Panda", "Plushes")
        plush10 = CupidItem("plush_10", "Plush - Barbarian", "Plushes")
        plush11 = CupidItem("plush_11", "Plush - Pink Beaver", "Plushes")
        plush12 = CupidItem("plush_12", "Plush - Snecko", "Plushes")

        flower1 = CupidItem("flower_1", "Flowers - Lillies", "Flowers")
        flower2 = CupidItem("flower_2", "Flowers - Daisies", "Flowers")
        flower3 = CupidItem("flower_3", "Flowers - Roses", "Flowers")
        flower4 = CupidItem("flower_4", "Flowers - Orchids", "Flowers")
        flower5 = CupidItem("flower_5", "Flowers - Begonias", "Flowers")
        flower6 = CupidItem("flower_6", "Flowers - Tulips", "Flowers")
        flower7 = CupidItem("flower_7", "Flowers - Sunflower", "Flowers")

        cupidstore = CupidStore()
        cupidstore.items = [plush1, plush2, plush3, plush4, plush5, plush6, plush7, plush8, plush9, 
                            plush10, plush11, plush12, flower1, flower2, flower3, flower4, flower5,
                            flower6, flower7]
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
