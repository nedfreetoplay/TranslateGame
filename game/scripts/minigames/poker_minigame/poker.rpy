init python:
    config.use_cpickle = False

    bot_fold_chance = 100
    erik_status = ""
    mrsj_status = ""
    player_status = ""

    class Card:
        def __init__(self, image = "", hand_image = "", number = "", kind = ""):
            self.image = image
            self.hand_image = hand_image
            self.number = number
            self.kind = kind

    def drawing_hand(hand, deck):
        i = 0
        while i < 2:
            random_card = renpy.random.choice(deck)
            hand.append(random_card)
            deck.remove(random_card)
            i += 1

    def reveal_card(deck, table):
        random_card = renpy.random.choice(deck)
        table.append(random_card)
        deck.remove(random_card)

    numbers = "01 02 03 04 05 06 07 08 09 10 11 12 13"
    number = numbers.split()
    kind = ["heart", "diamond", "club", "spade"]

    def allnumbers_count(re_hand, allnumbers):
        for Card in re_hand:
            allnumbers.append(Card.number)

    def allkinds_count(re_hand, allkinds):
        for Card in re_hand:
            allkinds.append(Card.kind)

    def straightflush(re_hand, allfaces):
        hearts = 0
        clubs = 0
        diamonds = 0
        spades = 0
        c_list = []
        for Card in re_hand:
            if Card.kind == "heart":
                hearts += 1
            elif Card.kind == "club":
                clubs += 1
            elif Card.kind == "diamond":
                diamonds += 1
            elif Card.kind == "spade":
                spades += 1
        if hearts >= 5:
            for Card in re_hand:
                if Card.kind == "heart":
                    c_list.append(Card)
        if spades >= 5:
            for Card in re_hand:
                if Card.kind == "spade":
                    c_list.append(Card)
        if clubs >= 5:
            for Card in re_hand:
                if Card.kind == "club":
                    c_list.append(Card)
        if diamonds >= 5:
            for Card in re_hand:
                if Card.kind == "diamond":
                    c_list.append(Card)

        allftypes = set([Card.number for Card in c_list])
        ordered = sorted(allftypes)
        if len(allftypes) >= 5:
            temp_var = []
            a = 0
            while len(temp_var) < 5:
                temp_var.append(ordered[a])
                a += 1
            if " ".join(card for card in temp_var) in numbers:
                return True
            elif len(allftypes) >= 6:
                temp_var = []
                a = 1
                while len(temp_var) < 5:
                    temp_var.append(ordered[a])
                    a += 1
                if " ".join(card for card in temp_var) in numbers:
                    return True
                elif len(allftypes) == 7:
                    temp_var = []
                    a = 2
                    while len(temp_var) < 5:
                        temp_var.append(ordered[a])
                        a += 1
                    if " ".join(card for card in temp_var) in numbers:
                        return True
        return False

    def fourofakind(re_hand, allfaces):
        for Card.number in allfaces:
            if allfaces.count(Card.number) == 4:
                return True
        return False

    def fullhouse(re_hand, allfaces):
        three = False
        pair = False
        for Card.number in allfaces:
            if allfaces.count(Card.number) == 3:
                three = True
        for Card.number in allfaces:
            if allfaces.count(Card.number) == 2:
                pair = True
        if three == True and pair == True:
            return True
        return False

    def flush(re_hand, allsuits):
        hearts = 0
        clubs = 0
        diamonds = 0
        spades = 0
        for Card in re_hand:
            if Card.kind == "heart":
                hearts += 1
            elif Card.kind == "club":
                clubs += 1
            elif Card.kind == "diamond":
                diamonds += 1
            elif Card.kind == "spade":
                spades += 1
        if hearts == 5 or clubs == 5 or diamonds == 5 or spades == 5:
            return True
        return False

    def straight(re_hand, allfaces):

        allftypes = set(allfaces)
        ordered = sorted(allftypes)
        if len(allftypes) >= 5:
            temp_var = []
            a = 0
            while len(temp_var) < 5:
                temp_var.append(ordered[a])
                a += 1
            if " ".join(card for card in temp_var) in numbers:
                return True
            elif len(allftypes) >= 6:
                temp_var = []
                a = 1
                while len(temp_var) < 5:
                    temp_var.append(ordered[a])
                    a += 1
                if " ".join(card for card in temp_var) in numbers:
                    return True
                elif len(allftypes) == 7:
                    temp_var = []
                    a = 2
                    while len(temp_var) < 5:
                        temp_var.append(ordered[a])
                        a += 1
                    if " ".join(card for card in temp_var) in numbers:
                        return True
        return False

    def threeofakind(re_hand, allfaces):

        allftypes = set(allfaces)
        if len(allftypes) <= 2:
            return False
        for Card.number in allftypes:
            if allfaces.count(Card.number) == 3:
                return True

    def twopair(re_hand, allfaces):

        pairs = [Card.number for Card.number in allfaces if allfaces.count(Card.number) == 2]
        if len(pairs) != 4 and len(pairs) != 6:
            return False
        return True

    def onepair(re_hand, allfaces):

        pairs = [Card.number for Card.number in allfaces if allfaces.count(Card.number) == 2]
        if len(pairs) != 2:
            return False
        return True

    class Cloth:
        def __init__(self, image = "", passive_image = ""):
            self.image = image
            self.passive_image = passive_image

    def all_in(poker_item_list, poker_pot):
        while len(poker_item_list) != 0:
            poker_pot.append(poker_item_list[0])
            poker_item_list.remove(poker_item_list[0])

    def poker_call(poker_item_list, poker_pot):
        poker_pot.append(poker_item_list[0])
        poker_item_list.remove(poker_item_list[0])

    def remove_cloth(poker_item_list, poker_pot):
        for Cloth in poker_pot:
            poker_item_list.remove(Cloth)

    Card = Card
    heart_1 = Card(image = "buttons/poker_cards_large_A01.png", hand_image = "buttons/poker_cards_large_AA01.png", number = "01", kind = "heart")
    heart_2 = Card(image = "buttons/poker_cards_large_A02.png", hand_image = "buttons/poker_cards_large_AA02.png", number = "02", kind = "heart")
    heart_3 = Card(image = "buttons/poker_cards_large_A03.png", hand_image = "buttons/poker_cards_large_AA03.png", number = "03", kind = "heart")
    heart_4 = Card(image = "buttons/poker_cards_large_A04.png", hand_image = "buttons/poker_cards_large_AA04.png", number = "04", kind = "heart")
    heart_5 = Card(image = "buttons/poker_cards_large_A05.png", hand_image = "buttons/poker_cards_large_AA05.png", number = "05", kind = "heart")
    heart_6 = Card(image = "buttons/poker_cards_large_A06.png", hand_image = "buttons/poker_cards_large_AA06.png", number = "06", kind = "heart")
    heart_7 = Card(image = "buttons/poker_cards_large_A07.png", hand_image = "buttons/poker_cards_large_AA07.png", number = "07", kind = "heart")
    heart_8 = Card(image = "buttons/poker_cards_large_A08.png", hand_image = "buttons/poker_cards_large_AA08.png", number = "08", kind = "heart")
    heart_9 = Card(image = "buttons/poker_cards_large_A09.png", hand_image = "buttons/poker_cards_large_AA09.png", number = "09", kind = "heart")
    heart_10 = Card(image = "buttons/poker_cards_large_A10.png", hand_image = "buttons/poker_cards_large_AA10.png", number = "10", kind = "heart")
    heart_11 = Card(image = "buttons/poker_cards_large_A11.png", hand_image = "buttons/poker_cards_large_AA11.png", number = "11", kind = "heart")
    heart_12 = Card(image = "buttons/poker_cards_large_A12.png", hand_image = "buttons/poker_cards_large_AA12.png", number = "12", kind = "heart")
    heart_13 = Card(image = "buttons/poker_cards_large_A13.png", hand_image = "buttons/poker_cards_large_AA13.png", number = "13", kind = "heart")
    diamond_1 = Card(image = "buttons/poker_cards_large_B01.png", hand_image = "buttons/poker_cards_large_BB01.png", number = "01", kind = "diamond")
    diamond_2 = Card(image = "buttons/poker_cards_large_B02.png", hand_image = "buttons/poker_cards_large_BB02.png", number = "02", kind = "diamond")
    diamond_3 = Card(image = "buttons/poker_cards_large_B03.png", hand_image = "buttons/poker_cards_large_BB03.png", number = "03", kind = "diamond")
    diamond_4 = Card(image = "buttons/poker_cards_large_B04.png", hand_image = "buttons/poker_cards_large_BB04.png", number = "04", kind = "diamond")
    diamond_5 = Card(image = "buttons/poker_cards_large_B05.png", hand_image = "buttons/poker_cards_large_BB05.png", number = "05", kind = "diamond")
    diamond_6 = Card(image = "buttons/poker_cards_large_B06.png", hand_image = "buttons/poker_cards_large_BB06.png", number = "06", kind = "diamond")
    diamond_7 = Card(image = "buttons/poker_cards_large_B07.png", hand_image = "buttons/poker_cards_large_BB07.png", number = "07", kind = "diamond")
    diamond_8 = Card(image = "buttons/poker_cards_large_B08.png", hand_image = "buttons/poker_cards_large_BB08.png", number = "08", kind = "diamond")
    diamond_9 = Card(image = "buttons/poker_cards_large_B09.png", hand_image = "buttons/poker_cards_large_BB09.png", number = "09", kind = "diamond")
    diamond_10 = Card(image = "buttons/poker_cards_large_B10.png", hand_image = "buttons/poker_cards_large_BB10.png", number = "10", kind = "diamond")
    diamond_11 = Card(image = "buttons/poker_cards_large_B11.png", hand_image = "buttons/poker_cards_large_BB11.png", number = "11", kind = "diamond")
    diamond_12 = Card(image = "buttons/poker_cards_large_B12.png", hand_image = "buttons/poker_cards_large_BB12.png", number = "12", kind = "diamond")
    diamond_13 = Card(image = "buttons/poker_cards_large_B13.png", hand_image = "buttons/poker_cards_large_BB13.png", number = "13", kind = "diamond")
    club_1 = Card(image = "buttons/poker_cards_large_C01.png", hand_image = "buttons/poker_cards_large_CC01.png", number = "01", kind = "club")
    club_2 = Card(image = "buttons/poker_cards_large_C02.png", hand_image = "buttons/poker_cards_large_CC02.png", number = "02", kind = "club")
    club_3 = Card(image = "buttons/poker_cards_large_C03.png", hand_image = "buttons/poker_cards_large_CC03.png", number = "03", kind = "club")
    club_4 = Card(image = "buttons/poker_cards_large_C04.png", hand_image = "buttons/poker_cards_large_CC04.png", number = "04", kind = "club")
    club_5 = Card(image = "buttons/poker_cards_large_C05.png", hand_image = "buttons/poker_cards_large_CC05.png", number = "05", kind = "club")
    club_6 = Card(image = "buttons/poker_cards_large_C06.png", hand_image = "buttons/poker_cards_large_CC06.png", number = "06", kind = "club")
    club_7 = Card(image = "buttons/poker_cards_large_C07.png", hand_image = "buttons/poker_cards_large_CC07.png", number = "07", kind = "club")
    club_8 = Card(image = "buttons/poker_cards_large_C08.png", hand_image = "buttons/poker_cards_large_CC08.png", number = "08", kind = "club")
    club_9 = Card(image = "buttons/poker_cards_large_C09.png", hand_image = "buttons/poker_cards_large_CC09.png", number = "09", kind = "club")
    club_10 = Card(image = "buttons/poker_cards_large_C10.png", hand_image = "buttons/poker_cards_large_CC10.png", number = "10", kind = "club")
    club_11 = Card(image = "buttons/poker_cards_large_C11.png", hand_image = "buttons/poker_cards_large_CC11.png", number = "11", kind = "club")
    club_12 = Card(image = "buttons/poker_cards_large_C12.png", hand_image = "buttons/poker_cards_large_CC12.png", number = "12", kind = "club")
    club_13 = Card(image = "buttons/poker_cards_large_C13.png", hand_image = "buttons/poker_cards_large_CC13.png", number = "13", kind = "club")
    spade_1 = Card(image = "buttons/poker_cards_large_D01.png", hand_image = "buttons/poker_cards_large_DD01.png", number = "01", kind = "spade")
    spade_2 = Card(image = "buttons/poker_cards_large_D02.png", hand_image = "buttons/poker_cards_large_DD02.png", number = "02", kind = "spade")
    spade_3 = Card(image = "buttons/poker_cards_large_D03.png", hand_image = "buttons/poker_cards_large_DD03.png", number = "03", kind = "spade")
    spade_4 = Card(image = "buttons/poker_cards_large_D04.png", hand_image = "buttons/poker_cards_large_DD04.png", number = "04", kind = "spade")
    spade_5 = Card(image = "buttons/poker_cards_large_D05.png", hand_image = "buttons/poker_cards_large_DD05.png", number = "05", kind = "spade")
    spade_6 = Card(image = "buttons/poker_cards_large_D06.png", hand_image = "buttons/poker_cards_large_DD06.png", number = "06", kind = "spade")
    spade_7 = Card(image = "buttons/poker_cards_large_D07.png", hand_image = "buttons/poker_cards_large_DD07.png", number = "07", kind = "spade")
    spade_8 = Card(image = "buttons/poker_cards_large_D08.png", hand_image = "buttons/poker_cards_large_DD08.png", number = "08", kind = "spade")
    spade_9 = Card(image = "buttons/poker_cards_large_D09.png", hand_image = "buttons/poker_cards_large_DD09.png", number = "09", kind = "spade")
    spade_10 = Card(image = "buttons/poker_cards_large_D10.png", hand_image = "buttons/poker_cards_large_DD10.png", number = "10", kind = "spade")
    spade_11 = Card(image = "buttons/poker_cards_large_D11.png", hand_image = "buttons/poker_cards_large_DD11.png", number = "11", kind = "spade")
    spade_12 = Card(image = "buttons/poker_cards_large_D12.png", hand_image = "buttons/poker_cards_large_DD12.png", number = "12", kind = "spade")
    spade_13 = Card(image = "buttons/poker_cards_large_D13.png", hand_image = "buttons/poker_cards_large_DD13.png", number = "13", kind = "spade")

    player_item01 = Cloth(image = "buttons/poker_items_player_01.png", passive_image = "buttons/poker_items_player_01b.png")
    player_item02 = Cloth(image = "buttons/poker_items_player_02.png", passive_image = "buttons/poker_items_player_02b.png")
    player_item03 = Cloth(image = "buttons/poker_items_player_03.png", passive_image = "buttons/poker_items_player_03b.png")
    player_item04 = Cloth(image = "buttons/poker_items_player_04.png", passive_image = "buttons/poker_items_player_04b.png")
    player_item05 = Cloth(image = "buttons/poker_items_player_05.png", passive_image = "buttons/poker_items_player_05b.png")
    player_item06 = Cloth(image = "buttons/poker_items_player_06.png", passive_image = "buttons/poker_items_player_06b.png")
    player_cloth = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]
    player_cloth_active = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]

    erik_item01 = Cloth(image = "buttons/poker_items_erik_01.png", passive_image = "buttons/poker_items_erik_01b.png")
    erik_item02 = Cloth(image = "buttons/poker_items_erik_02.png", passive_image = "buttons/poker_items_erik_02b.png")
    erik_item03 = Cloth(image = "buttons/poker_items_erik_03.png", passive_image = "buttons/poker_items_erik_03b.png")
    erik_item04 = Cloth(image = "buttons/poker_items_erik_04.png", passive_image = "buttons/poker_items_erik_04b.png")
    erik_item05 = Cloth(image = "buttons/poker_items_erik_05.png", passive_image = "buttons/poker_items_erik_05b.png")
    erik_item06 = Cloth(image = "buttons/poker_items_erik_06.png", passive_image = "buttons/poker_items_erik_06b.png")
    erik_cloth = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]
    erik_cloth_active = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]

    mia_item01 = Cloth(image = "buttons/poker_items_mia_01.png", passive_image = "buttons/poker_items_mia_01b.png")
    mia_item02 = Cloth(image = "buttons/poker_items_mia_02.png", passive_image = "buttons/poker_items_mia_02b.png")
    mia_item03 = Cloth(image = "buttons/poker_items_mia_03.png", passive_image = "buttons/poker_items_mia_03b.png")
    mia_item04 = Cloth(image = "buttons/poker_items_mia_04.png", passive_image = "buttons/poker_items_mia_04b.png")
    mia_item05 = Cloth(image = "buttons/poker_items_mia_05.png", passive_image = "buttons/poker_items_mia_05b.png")
    mia_item06 = Cloth(image = "buttons/poker_items_mia_06.png", passive_image = "buttons/poker_items_mia_06b.png")
    mia_cloth = [mia_item01, mia_item02, mia_item03, mia_item04, mia_item05, mia_item06]
    mia_cloth_active = [mia_item01, mia_item02, mia_item03, mia_item04, mia_item05, mia_item06]

    mrsj_item01 = Cloth(image = "buttons/poker_items_mrsj_01.png", passive_image = "buttons/poker_items_mrsj_01b.png")
    mrsj_item02 = Cloth(image = "buttons/poker_items_mrsj_02.png", passive_image = "buttons/poker_items_mrsj_02b.png")
    mrsj_item03 = Cloth(image = "buttons/poker_items_mrsj_03.png", passive_image = "buttons/poker_items_mrsj_03b.png")
    mrsj_item04 = Cloth(image = "buttons/poker_items_mrsj_04.png", passive_image = "buttons/poker_items_mrsj_04b.png")
    mrsj_item05 = Cloth(image = "buttons/poker_items_mrsj_05.png", passive_image = "buttons/poker_items_mrsj_05b.png")
    mrsj_item06 = Cloth(image = "buttons/poker_items_mrsj_06.png", passive_image = "buttons/poker_items_mrsj_06b.png")
    mrsj_cloth = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]
    mrsj_cloth_active = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]

label start_poker:
    scene expression "backgrounds/location_erik_basement_poker.jpg"
    python:
        bot_fold_chance = 0
        bot_fold = 0

        erik_status = ""
        mrsj_status = ""
        player_status = ""
        player_active = True
        erik_active = True
        mia_active = True
        mrsj_active = True

        player_pot = []
        erik_pot = []
        mia_pot = []
        mrsj_pot = []

        erik_max_loss = 0
        mrsj_max_loss = 0

        first_loser = ""

        erik_out = False
        mrsj_out = False

        round_count = 0

        recount_points = 0

        player_hand = []
        len_r = len(player_hand)
        player_points = 0
        bot_points = 0
        bot02_points = 0
        not_in_deck = []

        bot_hand = []
        bot02_hand = []
        table = []
        deck = [heart_1, heart_2, heart_3, heart_4, heart_5, heart_6, heart_7, heart_8, heart_9, heart_10, heart_11, heart_12, heart_13,
                diamond_1, diamond_2, diamond_3, diamond_4, diamond_5, diamond_6, diamond_7, diamond_8, diamond_9, diamond_10, diamond_11, diamond_12, diamond_13,
                club_1, club_2, club_3, club_4, club_5, club_6, club_7, club_8, club_9, club_10, club_11, club_12, club_13,
                spade_1, spade_2, spade_3, spade_4, spade_5, spade_6, spade_7, spade_8, spade_9, spade_10, spade_11, spade_12, spade_13]

        mia_cloth = [mia_item01, mia_item02, mia_item03, mia_item04, mia_item05, mia_item06]
        mia_cloth_active = [mia_item01, mia_item02, mia_item03, mia_item04, mia_item05, mia_item06]
        mia_cloth_removed = [mia_item01, mia_item02, mia_item03, mia_item04, mia_item05, mia_item06]
        player_cloth = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]
        player_cloth_active = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]
        player_cloth_removed = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]
        erik_cloth = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]
        erik_cloth_active = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]
        erik_cloth_removed = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]
        mrsj_cloth = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]
        mrsj_cloth_active = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]
        mrsj_cloth_removed = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]

    $ drawing_hand(player_hand, deck)
    $ drawing_hand(bot_hand, deck)
    $ drawing_hand(bot02_hand, deck)

    if len(erik_cloth_active) > 0:
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        if erik_item05 in erik_cloth_removed:
            show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    else:
        show erikpoker 8 at Position(xpos=234,ypos=626)
    if poker_bot02 == "mrsj":
        if len(mrsj_cloth_active) > 0:
            show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
            if mrsj_item05 in mrsj_cloth_removed:
                show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
            if mrsj_item06 in mrsj_cloth_removed:
                show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        else:
            show mrsjpoker 6 at Position(xpos=857,ypos=626)
    hide screen unclick_overlay
    call screen poker_screen

label next_round:
    scene expression "backgrounds/location_erik_basement_poker.jpg"
    python:
        bot_fold_chance = 0
        bot_fold = 0

        player_active = True
        erik_active = True
        mia_active = True
        mrsj_active = True

        player_pot = []
        erik_pot = []
        mia_pot = []
        mrsj_pot = []

        round_count = 0

        recount_points = 0

        player_hand = []
        len_r = len(player_hand)
        player_points = 0
        bot_points = 0
        bot02_points = 0
        not_in_deck = []

        bot_hand = []
        bot02_hand = []
        table = []
        deck = [heart_1, heart_2, heart_3, heart_4, heart_5, heart_6, heart_7, heart_8, heart_9, heart_10, heart_11, heart_12, heart_13,
                diamond_1, diamond_2, diamond_3, diamond_4, diamond_5, diamond_6, diamond_7, diamond_8, diamond_9, diamond_10, diamond_11, diamond_12, diamond_13,
                club_1, club_2, club_3, club_4, club_5, club_6, club_7, club_8, club_9, club_10, club_11, club_12, club_13,
                spade_1, spade_2, spade_3, spade_4, spade_5, spade_6, spade_7, spade_8, spade_9, spade_10, spade_11, spade_12, spade_13]

        player_cloth = [player_item01, player_item02, player_item03, player_item04, player_item05, player_item06]
        player_cloth_active = player_cloth_removed[:]
        erik_cloth = [erik_item01, erik_item02, erik_item03, erik_item04, erik_item05, erik_item06]
        erik_cloth_active = erik_cloth_removed[:]
        mrsj_cloth = [mrsj_item01, mrsj_item02, mrsj_item03, mrsj_item04, mrsj_item05, mrsj_item06]
        mrsj_cloth_active = mrsj_cloth_removed[:]

        erik_status = ""
        mrsj_status = ""
        player_status = ""

    $ drawing_hand(player_hand, deck)
    $ drawing_hand(bot_hand, deck)
    $ drawing_hand(bot02_hand, deck)

    if len(erik_cloth_active) > 0:
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        if erik_item05 in erik_cloth_removed:
            show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
    else:
        show erikpoker 8 at Position(xpos=234,ypos=626)
    if poker_bot02 == "mrsj":
        if len(mrsj_cloth_active) > 0:
            show mrsjpoker 2 zorder 1 at Position(xpos=857,ypos=626)
            if mrsj_item05 in mrsj_cloth_removed:
                show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
            if mrsj_item06 in mrsj_cloth_removed:
                show mrsjpokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        else:
            show mrsjpoker 6 at Position(xpos=857,ypos=626)
    hide screen unclick_overlay
    call screen poker_screen

label recount:
    show screen unclick_overlay
    $ re_player_hand = player_hand + table
    $ re_bot_hand = bot_hand + table
    $ re_bot02_hand = bot02_hand + table

    if player_status != "fold":
        $ allnumbers = []
        $ allkinds = []
        $ allnumbers_count(re_player_hand, allnumbers)
        $ allkinds_count (re_player_hand, allkinds)
        if straightflush(re_player_hand, allnumbers):
            $ player_points += 100
        elif fourofakind(re_player_hand, allnumbers):
            $ player_points += 90
        elif fullhouse(re_player_hand, allnumbers):
            $ player_points += 80
        elif flush(re_player_hand, allkinds):
            $ player_points += 70
        elif straight(re_player_hand, allnumbers):
            $ player_points += 60
        elif threeofakind(re_player_hand, allnumbers):
            $ player_points += 50
        elif onepair(re_player_hand, allnumbers):
            $ player_points += 30
        elif twopair(re_player_hand, allnumbers):
            $ player_points += 40

    if erik_status != "fold":
        $ allnumbers_bot = []
        $ allkinds_bot = []
        $ allnumbers_count(re_bot_hand, allnumbers_bot)
        $ allkinds_count (re_bot_hand, allkinds_bot)
        if straightflush(re_bot_hand, allnumbers_bot):
            $ bot_points += 100
        elif fourofakind(re_bot_hand, allnumbers_bot):
            $ bot_points += 90
        elif fullhouse(re_bot_hand, allnumbers_bot):
            $ bot_points += 80
        elif flush(re_bot_hand, allkinds_bot):
            $ bot_points += 70
        elif straight(re_bot_hand, allnumbers_bot):
            $ bot_points += 60
        elif threeofakind(re_bot_hand, allnumbers_bot):
            $ bot_points += 50
        elif onepair(re_bot_hand, allnumbers_bot):
            $ bot_points += 30
        elif twopair(re_bot_hand, allnumbers_bot):
            $ bot_points += 40

    if mrsj_status != "fold":
        $ allnumbers_bot02 = []
        $ allkinds_bot02 = []
        $ allnumbers_count(re_bot02_hand, allnumbers_bot02)
        $ allkinds_count (re_bot02_hand, allkinds_bot02)
        if straightflush(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 100
        elif fourofakind(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 90
        elif fullhouse(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 80
        elif flush(re_bot02_hand, allkinds_bot02):
            $ bot02_points += 70
        elif straight(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 60
        elif threeofakind(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 50
        elif onepair(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 30
        elif twopair(re_bot02_hand, allnumbers_bot02):
            $ bot02_points += 40

    if player_points > bot_points and player_points > bot02_points:
        player_name "Я выиграл!"
        $ player_status = "win"
        jump cloth_remove
    elif bot_points > player_points and bot_points > bot02_points and len(erik_cloth_active) > 0:
        eri "Да! Я выиграл."
        $ erik_status = "win"
        jump cloth_remove
    elif bot02_points > bot_points and bot02_points > player_points and len(mrsj_cloth_active) > 0:
        mrsjo "Я выиграла!"
        $ mrsj_status = "win"
        jump cloth_remove
    else:
        player_name "Никто не выигрывает, ура!"
    hide screen unclick_overlay
    jump end_dialogue

label all_in:
    show screen poker_screen
    show screen unclick_overlay
    $ all_in(player_cloth_active, player_pot)
    player_name "Я алл-ин, ребята!"
    $ player_status = "allin"

    if erik_status != "fold":
        $ re_bot_hand = bot_hand + table
        $ allnumbers_bot = []
        $ allkinds_bot = []
        $ allnumbers_count(re_bot_hand, allnumbers_bot)
        $ allkinds_count (re_bot_hand, allkinds_bot)
        if fourofakind(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 100
        elif threeofakind(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 90
        elif onepair(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 70
        elif twopair(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 80
        else:
            $ bot_fold_chance += 70


        $ bot_fold = renpy.random.randint(0,100)
        if bot_fold > bot_fold_chance and round_count != 0:
            Character("Erik") "Черт, я пас!"
            $ erik_status = "fold"
        else:
            Character("Erik") "Он блефует, я алл-ин, тоже!"
            $ all_in(erik_cloth_active, erik_pot)
            $ erik_status = "allin"
        $ bot_fold_chance = 0

    if erik_status == "fold" and mrsj_status == "fold" and player_status != "fold":
        player_name "Ура, я победил!"
        jump end_dialogue
    elif erik_status != "fold" and mrsj_status == "fold" and player_status == "fold":
        Character("Erik") "Да, я наконец-то выиграл!"
        jump end_dialogue
    elif mrsj_status != "fold" and erik_status == "fold" and player_status == "fold":
        poker_sayer02 "Не могу поверить, что выиграла!"
        jump end_dialogue

    if mrsj_status != "fold":
        $ re_bot02_hand = bot02_hand + table
        $ allnumbers_bot02 = []
        $ allkinds_bot02 = []
        $ allnumbers_count(re_bot02_hand, allnumbers_bot02)
        $ allkinds_count (re_bot02_hand, allkinds_bot02)
        if fourofakind(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 100
        elif threeofakind(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 90
        elif onepair(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 70
        elif twopair(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 80
        else:
            $ bot_fold_chance += 70

        $ bot_fold = renpy.random.randint(0,100)
        if bot_fold > bot_fold_chance and round_count != 0:
            poker_sayer02 "Я пассую."
            $ mrsj_status = "fold"
        else:
            poker_sayer02 "Блеф! Я алл-ин."
            $ all_in(mrsj_cloth_active, mrsj_pot)
            $ mrsj_status = "allin"
        $ bot_fold_chance = 0

    while len(table) < 5:
        $ reveal_card(deck, table)
    player_name "Покажи свои карты!"
    jump recount

label fold:
    show screen poker_screen
    show screen unclick_overlay
    $ player_status = "fold"
    $ remove_cloth(player_cloth_removed, player_pot)
    if len(player_cloth_removed) == 5:
        player_name "Ладно."
    elif len(player_cloth_removed) == 4:
        player_name "Вот, держи."
    elif len(player_cloth_removed) == 3:
        player_name "Снова..."
    elif len(player_cloth_removed) == 2:
        player_name "Еще один."
    elif len(player_cloth_removed) == 1:
        player_name "Уххх..."
        show mrsjpoker 2 at Position(xpos=857,ypos=626)
        mrsjo "Ты в порядке, {b}[firstname]{/b}?"
        show mrsjpoker 10 at Position(xpos=856,ypos=627)
        show erikpoker 12
        eri "Ты выглядишь не очень хорошо...."
        show erikpoker 1
        player_name "Всё нормально, спасибо..."
    elif len(player_cloth_removed) == 0:
        if len(erik_cloth_active) > 0 and len(mrsj_cloth_active) > 0:
            player_name "У меня голова кругом идет... Я только что проиграл?!"
            show erikpoker 12
            eri "Да."
            show erikpoker 1
            player_name "Да, хорошая {b}*ик*{/b} игра."
        else:
            jump end_dialogue
    $ player_active = False
    jump poker_call

label poker_call:
    show screen poker_screen
    show screen unclick_overlay
    if player_status != "fold":
        if len(player_cloth_active) > 0:
            $ poker_call(player_cloth_active, player_pot)
            player_name "Я пропущу."
            $ player_status = "call"

    if erik_status != "fold":
        $ re_bot_hand = bot_hand + table
        $ allnumbers_bot = []
        $ allkinds_bot = []
        $ allnumbers_count(re_bot_hand, allnumbers_bot)
        $ allkinds_count (re_bot_hand, allkinds_bot)
        if fourofakind(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 100
        elif threeofakind(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 90
        elif onepair(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 70
        elif twopair(re_bot_hand, allnumbers_bot):
            $ bot_fold_chance += 80
        else:
            $ bot_fold_chance += 70

        if len(erik_cloth_active) == 0:
            if first_loser == "":
                $ first_loser = "Erik"
            $ bot_fold_chance = 0

        $ bot_fold = renpy.random.randint(0,100)
        if bot_fold > bot_fold_chance and round_count != 0:
            $ erik_status = "fold"
            if player_status == "fold":
                if len(player_pot) == 0:
                    $ erik_max_loss = 0
                elif len(player_pot) == 1:
                    $ erik_max_loss = 1
                elif len(player_pot) == 2:
                    $ erik_max_loss = 2
                elif len(player_pot) == 3:
                    $ erik_max_loss = 3
                elif len(player_pot) == 4:
                    $ erik_max_loss = 4
                elif len(player_pot) == 5:
                    $ erik_max_loss = 5
                elif len(player_pot) == 6:
                    $ erik_max_loss = 6
                if len(erik_pot) > erik_max_loss:
                    $ counter = 0
                    $ max_ = len(erik_pot) - erik_max_loss
                    while (counter < max_):
                        $ erik_pot.remove(renpy.random.choice(erik_pot))
                        $ counter += 1
            $ remove_cloth(erik_cloth_removed, erik_pot)
            if len(erik_cloth_active) > 0 or erik_out == False:
                if len(erik_cloth_removed) == 5:
                    show erikpoker 12
                    show erikpokerc
                    show mrsjpoker 1 at Position(xpos=857,ypos=626)
                    eri "Круто."
                    show erikpokerc 10 at Position(xpos=144,ypos=592)
                    show erikpoker 3 at Position(xpos=172,ypos=624)
                    pause
                    show erikpokerc 9 at Position(xpos=144,ypos=592)
                    show erikpoker 1 at Position(xpos=153,ypos=626)
                    show mrsjpoker 10 at Position(xpos=856,ypos=627)
                elif len(erik_cloth_removed) == 4:
                    show mrsjpoker 1 at Position(xpos=857,ypos=626)
                    show erikpoker 12 at Position(xpos=153,ypos=626)
                    eri "Хорошо..."
                    show erikpokerc 10 at Position(xpos=144,ypos=592)
                    show erikpoker 3 at Position(xpos=172,ypos=624)
                    pause
                    show erikpokerc 9 at Position(xpos=144,ypos=592)
                    show erikpoker 1 at Position(xpos=153,ypos=626)
                    show mrsjpoker 10 at Position(xpos=856,ypos=627)
                elif len(erik_cloth_removed) == 3:
                    show mrsjpoker 1 at Position(xpos=857,ypos=626)
                    show erikpoker 2 at Position(xpos=153,ypos=626)
                    eri "Хех, пей до дна!"
                    show erikpokerc 10 at Position(xpos=144,ypos=592)
                    show erikpoker 3 at Position(xpos=172,ypos=624)
                    pause
                    show erikpokerc 9 at Position(xpos=144,ypos=592)
                    show erikpoker 1 at Position(xpos=153,ypos=626)
                    show mrsjpoker 10 at Position(xpos=856,ypos=627)
                elif len(erik_cloth_removed) == 2:
                    show mrsjpoker 1 at Position(xpos=857,ypos=626)
                    show erikpoker 2 at Position(xpos=153,ypos=626)
                    eri "Братан, грубая игра..."
                    show erikpokerc 10 at Position(xpos=144,ypos=592)
                    show erikpoker 3 at Position(xpos=172,ypos=624)
                    pause
                    show erikpokerc 9 at Position(xpos=144,ypos=592)
                    show erikpoker 1 at Position(xpos=153,ypos=626)
                    pause
                    show erikpoker 12
                    eri "УФ! Кажется, я начинаю это чувствовать."
                    show erikpoker 13
                    show mrsjpoker 10 at Position(xpos=856,ypos=627)
                elif len(erik_cloth_removed) == 1:
                    call expression game.dialog_select("poker_erik_1_cloth_left")
                elif len(erik_cloth_removed) == 0:
                    show mrsjpoker 1 at Position(xpos=857,ypos=626)
                    show erikpoker 5 at Position(xpos=153,ypos=626)
                    eri "Хорошо сыграно..."
                    hide erikpokerc with dissolve
                    show erikpoker 3 at Position(xpos=172,ypos=624)
                    pause
                    show erikpoker 13 at Position(xpos=153,ypos=626)
                    pause
                    show erikpoker 6 with dissolve
                    pause
                    show erikpoker 7
                    eri "Я ничего не вижу, ребята..."
                    eri "Я..."
                    eri "Я... Не очень хорошо себя чувствую..."
                    pause
                    show erikpoker 8 at Position(xpos=234,ypos=626) with vpunch
                    pause
                    $ erik_out = True

            $ erik_active = False
        else:
            if len(erik_cloth_active) > 0:
                Character("Erik") "Пропущу..."
                $ erik_status = "call"
                $ poker_call(erik_cloth_active, erik_pot)
        $ bot_fold_chance = 0

    if erik_status == "fold" and mrsj_status == "fold" and player_status != "fold":
        player_name "Да! Я выиграл!"
        jump end_dialogue
    elif erik_status != "fold" and mrsj_status == "fold" and player_status == "fold":
        Character("Erik") "Да! Я наконец-то выиграл!"
        jump end_dialogue
    elif mrsj_status != "fold" and erik_status == "fold" and player_status == "fold":
        poker_sayer02 "Не могу поверить, что выиграла!"
        jump end_dialogue
    elif len(table) == 5:
        player_name "Покажи свои карты!"
        jump recount

    if mrsj_status != "fold":
        $ re_bot02_hand = bot02_hand + table
        $ allnumbers_bot02 = []
        $ allkinds_bot02 = []
        $ allnumbers_count(re_bot02_hand, allnumbers_bot02)
        $ allkinds_count (re_bot02_hand, allkinds_bot02)
        if fourofakind(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 100
        elif threeofakind(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 90
        elif onepair(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 70
        elif twopair(re_bot02_hand, allnumbers_bot02):
            $ bot_fold_chance += 80
        else:
            $ bot_fold_chance += 70

        if len(mrsj_cloth_active) == 0:
            if first_loser == "":
                $ first_loser = "Mrs J"
            $ bot_fold_chance = 0

        $ bot_fold = renpy.random.randint(0,100)
        if bot_fold > bot_fold_chance and round_count != 0:
            $ mrsj_status = "fold"
            if player_status == "fold":
                if len(player_pot) == 0:
                    $ mrsj_max_loss = 0
                elif len(player_pot) == 1:
                    $ mrsj_max_loss = 1
                elif len(player_pot) == 2:
                    $ mrsj_max_loss = 2
                elif len(player_pot) == 3:
                    $ mrsj_max_loss = 3
                elif len(player_pot) == 4:
                    $ mrsj_max_loss = 4
                elif len(player_pot) == 5:
                    $ mrsj_max_loss = 5
                elif len(player_pot) == 6:
                    $ mrsj_max_loss = 6
                if len(mrsj_pot) > mrsj_max_loss:
                    $ counter = 0
                    $ max_ = len(mrsj_pot) - mrsj_max_loss
                    while (counter < max_):
                        $ mrsj_pot.remove(renpy.random.choice(mrsj_pot))
                        $ counter += 1
            $ remove_cloth(mrsj_cloth_removed, mrsj_pot)
            if len(mrsj_cloth_removed) == 5:
                show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
                show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
                show erikpoker 11 at Position(xpos=153,ypos=626)
                show mrsjpoker 2 at Position(xpos=857,ypos=626)
                mrsjo "Вот так-то!"
                show mrsjpoker 3 at Position(xpos=836,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 4:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Боже, я и забыл, как это волнующе!"
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 3:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Интересно, хватит ли нам на всех..."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 2:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Мальчики, Вам нравится?"
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Итак, когда вы, мальчики, приведете сюда девушку?"
                show mrsjpoker 1
                show erikpoker 2
                eri "Мы работаем над этим, {b}Миссис Джонсон{/b}."
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 11
                player_name "Да, это сложнее, чем кажется."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 9 at Position(xpos=857,ypos=627)
                mrsjo "О, я знаю, некоторые девушки в вашем возрасте просто порочны."
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Продолжайте пытаться, я уверен, вы оба найдете хорошего партнера."
                show erikpoker 1
                show mrsjpoker 1
            elif len(mrsj_cloth_removed) == 1:
                hide screen unclick_overlay
                hide screen poker_screen
                show erik_cutscene zorder 6 with fade
                show text "Я не ожидал {b}Миссис Джонсон{/b} что было так весело играть с нами. \nСначала у нее все было хорошо, но каждый раз, когда она проигрывала, она пила больше и раздевалась... \nУ нее быстро заканчивалась одежда! \n" zorder 7 at Position (xpos= 512, ypos = 700) with dissolve
                pause
                hide erik_cutscene
                hide text
                with fade
                show screen unclick_overlay
                show screen poker_screen

            elif len(mrsj_cloth_removed) == 0:
                show erikpoker 11
                show mrsjpoker 5 at Position(xpos=858,ypos=626)
                mrsjo "Тогда спускайтесь в люк..."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 11 at Position(xpos=857,ypos=627)
                pause
                hide mrsjpokerc1 with dissolve
                hide mrsjpokerc2 with dissolve
                pause
                hide screen unclick_overlay
                hide screen poker_screen
                show mrsjpoker 6 at Position(xpos=857,ypos=626) with dissolve
                mrsjo "Поразительно... Я не была так пьяна в течение долгого времени!"
                mrsjo "Хорошо сыграно, мальчики..."
                jump mrsj_lost
            $ mrsj_active = False
        else:
            if len(mrsj_cloth_active) > 0:
                poker_sayer02 "Я звоню."
                $ poker_call(mrsj_cloth_active, mrsj_pot)
                $ mrsj_status = "call"
        $ bot_fold_chance = 0

    if erik_status == "fold" and mrsj_status == "fold" and player_status != "fold":
        player_name "Ура, я выиграл!"
        jump end_dialogue
    elif erik_status != "fold" and mrsj_status == "fold" and player_status == "fold":
        Character("Erik") "Да, я наконец-то победил!"
        jump end_dialogue
    elif mrsj_status != "fold" and erik_status == "fold" and player_status == "fold":
        poker_sayer02 "Не могу поверить, что выиграла!"
        jump end_dialogue
    else:
        player_name "Игра продолжается."
    $ reveal_card(deck, table)
    if len(table) == 5:
        player_name "Покажи свои карты!"
        jump recount
    $ round_count += 1
    if player_status == "fold":
        jump poker_call
    hide screen unclick_overlay
    hide screen poker_screen
    call screen poker_screen

label end_dialogue:
    if first_loser == "Erik":
        jump erik_lost
    elif first_loser == "Mrs J":
        jump mrsj_lost
    elif len(player_cloth_active) == 0:
        if first_loser == "":
            jump player_lost
        else:
            if first_loser == "Erik":
                jump erik_lost
            elif first_loser == "Mrs J":
                jump mrsj_lost
    player_name "Следующий раунд."
    jump next_round

label cloth_remove:
    label cloth_remove_player:
        if player_status != "win" and player_active == True:
            $ remove_cloth(player_cloth_removed, player_pot)
            if len(player_cloth_removed) == 5:
                player_name "Хорошо, ваше здоровье!"
            elif len(player_cloth_removed) == 4:
                player_name "Вот."
            elif len(player_cloth_removed) == 3:
                player_name "Опять..."
            elif len(player_cloth_removed) == 2:
                player_name "Еще одну."
            elif len(player_cloth_removed) == 1:
                player_name "Уууууггг..."
                show mrsjpoker 2 at Position(xpos=857,ypos=626)
                mrsjo "Ты в порядке, {b}[firstname]{/b}?"
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
                show erikpoker 12
                eri "Да, ты выглядишь не очень...."
                show erikpoker 1
                player_name "Со мной все будет хорошо, Спасибо."
            elif len(player_cloth_removed) == 0:
                player_name "У меня голова кругом идет... Я только что проиграл?!"
                show erikpoker 12
                eri "Да."
                show erikpoker 1
                player_name "Ух, хорошая {b}*ик*{/b} игра."
                jump player_lost
            $ player_active = False
            jump end_dialogue

    label cloth_remove_erik:
        if erik_status != "win" and erik_active == True:
            if player_status == "fold":
                if len(player_pot) == 0:
                    $ erik_max_loss = 0
                elif len(player_pot) == 1:
                    $ erik_max_loss = 1
                elif len(player_pot) == 2:
                    $ erik_max_loss = 2
                elif len(player_pot) == 3:
                    $ erik_max_loss = 3
                elif len(player_pot) == 4:
                    $ erik_max_loss = 4
                elif len(player_pot) == 5:
                    $ erik_max_loss = 5
                elif len(player_pot) == 6:
                    $ erik_max_loss = 6
                if len(erik_pot) > erik_max_loss:
                    $ counter = 0
                    $ max_ = len(erik_pot) - erik_max_loss
                    while (counter < max_):
                        $ erik_pot.remove(renpy.random.choice(erik_pot))
                        $ counter += 1
            $ remove_cloth(erik_cloth_removed, erik_pot)
            if len(erik_cloth_removed) == 5:
                show erikpoker 12
                show erikpokerc
                show mrsjpoker 1 at Position(xpos=857,ypos=626)
                eri "Круто."
                show erikpokerc 10 at Position(xpos=144,ypos=592)
                show erikpoker 3 at Position(xpos=172,ypos=624)
                pause
                show erikpokerc 9 at Position(xpos=144,ypos=592)
                show erikpoker 1 at Position(xpos=153,ypos=626)
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
            elif len(erik_cloth_removed) == 4:
                show mrsjpoker 1 at Position(xpos=857,ypos=626)
                show erikpoker 12 at Position(xpos=153,ypos=626)
                eri "Хорошо..."
                show erikpokerc 10 at Position(xpos=144,ypos=592)
                show erikpoker 3 at Position(xpos=172,ypos=624)
                pause
                show erikpokerc 9 at Position(xpos=144,ypos=592)
                show erikpoker 1 at Position(xpos=153,ypos=626)
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
            elif len(erik_cloth_removed) == 3:
                show mrsjpoker 1 at Position(xpos=857,ypos=626)
                show erikpoker 2 at Position(xpos=153,ypos=626)
                eri "Хех, пей до дна!"
                show erikpokerc 10 at Position(xpos=144,ypos=592)
                show erikpoker 3 at Position(xpos=172,ypos=624)
                pause
                show erikpokerc 9 at Position(xpos=144,ypos=592)
                show erikpoker 1 at Position(xpos=153,ypos=626)
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
            elif len(erik_cloth_removed) == 2:
                show mrsjpoker 1 at Position(xpos=857,ypos=626)
                show erikpoker 2 at Position(xpos=153,ypos=626)
                eri "Чувак, тяжелая игра."
                show erikpokerc 10 at Position(xpos=144,ypos=592)
                show erikpoker 3 at Position(xpos=172,ypos=624)
                pause
                show erikpokerc 9 at Position(xpos=144,ypos=592)
                show erikpoker 1 at Position(xpos=153,ypos=626)
                pause
                show erikpoker 12
                eri "УФ! Думаю, я начинаю чувствовать это сейчас."
                show erikpoker 13
                show mrsjpoker 10 at Position(xpos=856,ypos=627)
            elif len(erik_cloth_removed) == 1:
                call expression game.dialog_select("poker_erik_0_cloth_left")
            elif len(erik_cloth_removed) == 0:
                show mrsjpoker 1 at Position(xpos=857,ypos=626)
                show erikpoker 5 at Position(xpos=153,ypos=626)
                eri "Хорошо сыграно..."
                hide erikpokerc with dissolve
                show erikpoker 3 at Position(xpos=172,ypos=624)
                pause
                show erikpoker 13 at Position(xpos=153,ypos=626)
                pause
                show erikpoker 6 with dissolve
                pause
                show erikpoker 7
                eri "Я ничего не вижу, ребята...."
                eri "Я..."
                eri "И... Не очень хорошо себя чувствую..."
                pause
                show erikpoker 8 at Position(xpos=234,ypos=626) with vpunch
                pause
                $ erik_out = True
                jump erik_lost
            $ erik_active = False
            jump end_dialogue

    label cloth_remove_mrsj:
        if mrsj_status != "win" and mrsj_active == True:
            if player_status == "fold":
                if len(player_pot) == 0:
                    $ mrsj_max_loss = 0
                elif len(player_pot) == 1:
                    $ mrsj_max_loss = 1
                elif len(player_pot) == 2:
                    $ mrsj_max_loss = 2
                elif len(player_pot) == 3:
                    $ mrsj_max_loss = 3
                elif len(player_pot) == 4:
                    $ mrsj_max_loss = 4
                elif len(player_pot) == 5:
                    $ mrsj_max_loss = 5
                elif len(player_pot) == 6:
                    $ mrsj_max_loss = 6
                if len(mrsj_pot) > mrsj_max_loss:
                    $ counter = 0
                    $ max_ = len(mrsj_pot) - mrsj_max_loss
                    while (counter < max_):
                        $ mrsj_pot.remove(renpy.random.choice(mrsj_pot))
                        $ counter += 1
            $ remove_cloth(mrsj_cloth_removed, mrsj_pot)
            if len(mrsj_cloth_removed) == 5:
                show mrsjpokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
                show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
                show erikpoker 11 at Position(xpos=153,ypos=626)
                show mrsjpoker 2 at Position(xpos=857,ypos=626)
                mrsjo "Вот так-то!"
                show mrsjpoker 3 at Position(xpos=836,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 4:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Боже, я и забыл, как это волнующе!"
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 3:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Интересно, хватит ли нам на всех..."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 1
            elif len(mrsj_cloth_removed) == 2:
                show erikpoker 11
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Мальчики, Вам нравится?"
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Итак, когда вы, мальчики, приведете сюда девушку?"
                show mrsjpoker 1
                show erikpoker 2
                eri "Мы работаем над этим, {b}Миссис Джонсон{/b}."
                show mrsjpoker 10 at Position(xpos=857,ypos=627)
                show erikpoker 11
                player_name "Да, это сложнее, чем кажется."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 9 at Position(xpos=857,ypos=627)
                mrsjo "О, я знаю, некоторые девушки в вашем возрасте просто порочны."
                show mrsjpoker 2 at Position(xpos=858,ypos=626)
                mrsjo "Продолжайте пытаться, я уверена, вы оба найдете хорошего партнера."
                show erikpoker 1
                show mrsjpoker 1
            elif len(mrsj_cloth_removed) == 1:
                hide screen unclick_overlay
                hide screen poker_screen
                show erik_cutscene zorder 6 with fade
                show text "Я не ожидал что {b}Миссис Джонсон{/b} так весело играть с нами. \nСначала у нее все было хорошо, но каждый раз, когда она проигрывала, она пила больше и раздевалась... \nУ нее быстро заканчивалась одежда! \n" zorder 7 at Position (xpos= 512, ypos = 700) with dissolve
                pause
                hide erik_cutscene
                hide text
                with fade
                show screen unclick_overlay
                show screen poker_screen

            elif len(mrsj_cloth_removed) == 0:
                show erikpoker 11
                show mrsjpoker 5 at Position(xpos=858,ypos=626)
                mrsjo "Тогда спускайтесь в люк..."
                show mrsjpoker 3 at Position(xpos=837,ypos=626)
                pause
                show mrsjpoker 11 at Position(xpos=857,ypos=627)
                pause
                hide mrsjpokerc1 with dissolve
                hide mrsjpokerc2 with dissolve
                pause
                hide screen unclick_overlay
                hide screen poker_screen
                show mrsjpoker 6 at Position(xpos=857,ypos=626) with dissolve
                mrsjo "Поразительно... Я не была так пьян в течение долгого времени!"
                mrsjo "Хорошо сыграно, мальчики..."
                jump mrsj_lost
            $ mrsj_active = False
            jump end_dialogue

    label player_lost:
        $ player.go_to(L_erikhouse)
        $ poker_bot02 = ""
        $ poker_sayer02 = ""
        $ M_mrsj.unforce()
        $ M_erik.unforce()
        $ game.timer.tick()
        hide erikpoker
        hide erikpokerc
        hide mrsjpoker
        hide mrsjpokerc1
        hide mrsjpokerc2
        hide screen unclick_overlay
        hide screen poker_screen
        scene erik_basement
        show player 193 at left
        show erik 1 at Position(xpos=756,ypos=768)
        show mrsj 18 at Position(xpos=876,ypos=768)
        with fade

        mrsjo "Хахаха."
        show mrsj 17
        mrsjo "Кто-то слишком много выпил!!"
        show mrsj 14
        show erik 4
        eri "Ты в порядке, {b}[firstname]{/b}?"
        show erik 1
        show player 192
        player_name "Да, всё заебись..."
        player_name "Мне просто нужно найти свою одежду..."
        show player 193
        show mrsj 18
        mrsjo "Я принесу её для тебя."
        show mrsj 14
        show player 194 at Position(xpos=-25,ypos=768)
        player_name "Спасибо вам {b}Миссис Джонсон{/b}. Вы очень, очень добры."
        show player 192 at left
        player_name "Думаю, мне стоит пойти домой..."
        show player 193
        show erik 4
        eri "Нужна помощь, чтобы добраться домой?"
        show erik 1
        show player 192
        player_name "Нет, со мной все будет в порядке..."
        show player 193
        show erik 4
        eri "Спасибо, что зашел ко мне."
        eri "Доброй ночи!"
        show player 192
        player_name "И тебее..."
        hide erik
        hide player
        hide mrsj
        $ game.main()

    label erik_lost:
        $ player.go_to(L_erikhouse)
        $ poker_bot02 = ""
        $ poker_sayer02 = ""
        $ M_mrsj.unforce()
        $ M_erik.unforce()
        $ game.timer.tick()
        hide erikpoker
        hide erikpokerc
        hide mrsjpoker
        hide mrsjpokerc1
        hide mrsjpokerc2
        hide screen unclick_overlay
        hide screen poker_screen
        scene erik_basement
        show player 10f at Position(xpos=756,ypos=768)
        show erik 23 at left
        show mrsj 14 at Position(xpos=876,ypos=768)
        with fade

        player_name "Всё хорошо {b}Эрик{/b}??"
        show player 11f
        show erik 24
        eri "Да... Дай мне секунду, чтобы одеться..."
        pause
        show erik 25
        pause 0.5
        show player 22f
        show erik 26 with vpunch
        pause 0.05
        hide erik
        player_name "!!!"
        show player 109
        show mrsj 20
        mrsjo "О, боже..."
        mrsjo "Он не привык к выпивке!"
        show mrsj 14
        show player 108
        player_name "С ним все будет в порядке?"
        show mrsj 17
        show player 109
        mrsjo "Не волнуйтесь! Я позабочусь о своем мальчике..."
        show mrsj 14
        show player 10f
        player_name "Окей. Тогда мне, наверное, пора идти."
        show player 17f
        player_name "Спасибо за игру! Было весело."
        show mrsj 18
        mrsjo "Дааа!"
        hide erik
        hide player
        hide mrsj
        $ game.main()

    label mrsj_lost:
        $ player.go_to(L_erikhouse)
        $ poker_bot02 = ""
        $ poker_sayer02 = ""
        $ game.timer.tick()
        hide erikpoker
        hide erikpokerc
        hide mrsjpoker
        hide mrsjpokerc1
        hide mrsjpokerc2
        hide screen unclick_overlay
        hide screen poker_screen
        scene erik_basement with fade
        if mrsj.completed(mrsj_poker_night_2):
            show player 1f at Position(xpos=756)
            show erik 1 at Position(xpos=876)
            show mrsj 29f at left
            with fade
            pause
            mrsjo "Вооу!"
            show mrsj 28f
            mrsjo "Это было весело!"
            show mrsj 27f at Position(xoffset=-1)
            pause
            show mrsj 28f
            mrsjo "Хорошо, ты меня раскусила!"
            show player 11f
            mrsjo "Увидимся в моей комнате, мальчики."
            show player 21f
            show mrsj 27f at Position(xoffset=-1)
            player_name "Подожди, ты хочешь сделать это снова?"
            show erik 5
            show player 1f
            eri "Да, ты уверена насчет этого, {b}Миссис Джонсон{/b}?"
            show mrsj 33 at center
            hide player
            hide erik
            with fastdissolve
            mrsjo "Да ладно, ты живешь только один раз!"
            show mrsj 34
            mrsjo "С таким же успехом можно повеселиться, да?"
        else:

            show player 1f at Position(xpos=756)
            show erik 1 at Position(xpos=876)
            show mrsj 29f at left
            with fade
            pause
            mrsjo "Вооу!"
            show mrsj 28f
            mrsjo "Это было весело!!"
            show mrsj 27f at Position(xpos=-1)
            pause
            player_name "..."
            show mrsj 28f at Position(xpos=0)
            mrsjo "Хорошо, ты меня раскусила!!"
            show erik 5
            show mrsj 27f at Position(xpos=-1)
            eri "*ик* Ты совершенно голая, {b}Миссис Джонсон{/b}."
            show erik 1
            show mrsj 28f at Position(xpos=0)
            mrsjo "Ну, разве не в этом смысл вашей маленькой игры, мальчики?"
            show player 21f
            show mrsj 27f at Position(xpos=-1)
            player_name "Вы... действительно милая, {b}Миссис Джонсон{/b}!"
            show player 1f
            show mrsj 28f at Position(xpos=0)
            mrsjo "Серьёзно?"
            show mrsj 31 with fastdissolve
            pause
            mrsjo "Мне кажется, я выгляжу Толстой..."
            show player 11f
            show mrsj 30f with fastdissolve
            mrsjo "Но, по крайней мере, мои сиськи все еще красивые и упругие!"
            show mrsj 33 at center
            hide player
            hide erik
            with fastdissolve
            mrsjo "Хи-хи, у меня есть идея..."
            mrsjo "Как насчет того, чтобы устроиться поудобнее на диване в другой комнате..."
            show mrsj 34
            mrsjo "... и вы двое решите, хотите ли присоединиться ко мне."
            show mrsj 33
            mrsjo "Увидимся на месте!"
            show unlock45 at truecenter with dissolve
            pause
            hide unlock45 with dissolve
        hide mrsj
        show player 13 at left
        show erik 1 at right
        with fastdissolve
        pause
        show player 21

        player_name "Так... что нам теперь делать?"
        show erik 3
        show player 1
        eri "{b}*ик*{/b} Я не знаю!"
        show erik 3b
        eri "Что ты думаешь, {b}*ик*{/b} мы должны это сделать?"
        show erik 1
        show player 4
        menu:
            "Иди к ней.":
                show player 14 at left
                show erik 1 at right
                player_name "Я думаю {b}Миссис Джонсон{/b} хочет повеселиться с нами."
                show erik 4
                show player 1
                eri "Ты думаешь?"
                show erik 1
                show player 14
                player_name "Дааа!"
                player_name "Мы должны увидеть, чего она хочет..."
                show erik 4
                show player 1
                eri "Ладно, *ик* пойдем навестим её."
                hide erik
                hide player
                with dissolve
                $ M_mrsj.set("afterpoker fun", True)

                $ M_mrsj.place(place = L_erikhouse_basement_backroom)
                $ M_erik.place(place = L_erikhouse_basement_backroom)
                $ player.go_to(L_erikhouse_basement)

            "Идти домой." if mrsj.over(mrsj_poker_night):
                show player 10 at left
                player_name "Вообще-то, я думаю, мне стоит пойти домой... Я не очень хорошо себя чувствую."
                show player 5
                show erik 4
                eri "Да... Я думаю *ик*, мы все слишком много выпили..."
                show player 10
                show erik 1
                player_name "Скажите {b}Миссис Джонсон{/b}, Извините."
                show player 5
                show erik 4
                eri "Я *ик* буду."
                eri "Увидимся завтра?"
                show player 10
                show erik 1
                player_name "Да, пока, {b}Эрик{/b}."
                $ M_mrsj.unforce()
                $ M_erik.unforce()
                jump bedroom_dialogue
        $ game.main()

label poker_erik_1_cloth_left:
    show mrsjpoker 1 at Position(xpos=857,ypos=626)
    show erikpoker 5
    eri "Да, определенно чувствую..."
    show erikpoker 4
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsjo "Тыковка, ты в порядке?"
    show erikpoker 14
    show mrsjpoker 1 at Position(xpos=857,ypos=626)
    eri "Я справлюсь, {b}Миссис Джонсон{/b}. Спасибо."
    show erikpokerc 10 at Position(xpos=144,ypos=592)
    show erikpoker 3 at Position(xpos=172,ypos=624)
    pause
    show erikpokerc 9 at Position(xpos=144,ypos=592)
    show erikpoker 13 at Position(xpos=153,ypos=626)
    pause
    hide erikpokerc with dissolve
    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    return

label poker_erik_0_cloth_left:
    show mrsjpoker 1 at Position(xpos=857,ypos=626)
    show erikpoker 5
    eri "Да, определенно чувствую..."
    show erikpoker 4
    show mrsjpoker 9 at Position(xpos=856,ypos=627)
    mrsjo "Тыковка, ты в порядке?"
    show erikpoker 14
    show mrsjpoker 1 at Position(xpos=857,ypos=626)
    eri "Я справлюсь, {b}Миссис Джонсон{/b}, спасибо."
    show erikpokerc 10 at Position(xpos=144,ypos=592)
    show erikpoker 3 at Position(xpos=172,ypos=624)
    pause
    show erikpokerc 9 at Position(xpos=144,ypos=592)
    show erikpoker 13 at Position(xpos=153,ypos=626)
    pause
    hide erikpokerc with dissolve
    show mrsjpoker 10 at Position(xpos=856,ypos=627)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
