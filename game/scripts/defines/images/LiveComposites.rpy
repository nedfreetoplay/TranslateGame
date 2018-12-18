
image school = ConditionSwitch(
    "Game.is_christmas()", "backgrounds/location_school_christmas_day_blur.jpg",
    "Game.is_halloween()", "backgrounds/location_school_halloween_day_blur.jpg",
    "True", "backgrounds/location_school_day_blur.jpg",
    )
image school_night = ConditionSwitch(
    "Game.is_christmas()", "backgrounds/location_school_christmas_night_blur.jpg",
    "Game.is_halloween()", "backgrounds/location_school_halloween_night_blur.jpg",
    "True", "backgrounds/location_school_night_blur.jpg",
    )
image graveyard = ConditionSwitch(
    "Game.is_halloween()", "backgrounds/location_church_graveyard_halloween_day_blur.jpg",
    "True", "backgrounds/location_church_graveyard_day_blur.jpg",
    )
image graveyard_night = ConditionSwitch(
    "Game.is_halloween()", "backgrounds/location_church_graveyard_halloween_night_blur.jpg",
    "True", "backgrounds/location_church_graveyard_night_blur.jpg",
    )
image office = ConditionSwitch(
    "not M_ross.is_set('smith office painting')", "backgrounds/location_school_office_day_blur.jpg",
    "True", "backgrounds/location_school_office_painting_day_blur.jpg",
    )
image office_night = ConditionSwitch(
    "not M_ross.is_set('smith office painting')", "backgrounds/location_school_office_night_blur.jpg",
    "True", "backgrounds/location_school_office_painting_night_blur.jpg",
    )



image weightlifting03 = ConditionSwitch(
    "player.stats.str() >= 7", "backgrounds/location_gym_minigame04c_heavy.jpg",
    "player.stats.str() >= 3", "backgrounds/location_gym_minigame04c_medium.jpg",
    "True", "backgrounds/location_gym_minigame04c.jpg",
    )



image trailer_bedroom = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_day.jpg",
    "True", "backgrounds/location_trailer_bedroom_day.jpg",
    )

image trailer_bedroom_night = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_night.jpg",
    "True", "backgrounds/location_trailer_bedroom_night.jpg",
    )

image trailer_bedroom_blur = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_day_blur.jpg",
    "True", "backgrounds/location_trailer_bedroom_day_blur.jpg",
    )

image trailer_bedroom_night_blur = ConditionSwitch(
    "M_roxxy.finished_state(S_roxxy_get_oil)", "backgrounds/location_trailer_bedroom_trophy_night_blur.jpg",
    "True", "backgrounds/location_trailer_bedroom_night_blur.jpg",
    )



image coach_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_coach_night.jpg", "True", "backgrounds/location_school_locker_coach_day.jpg"),
    (431,62), ConditionSwitch("M_bissette.is_state(S_bissette_roxxy_pom_poms) and not player.has_item('pompoms')", "objects/object_pompom_01.png", "True", Null()),
    )

image eve_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_eve_night.jpg", "True", "backgrounds/location_school_locker_eve_day.jpg"),
    (316,457), ConditionSwitch("M_ross.is_set('talked with chad') and not player.has_picked_up_item('eve_drawing')", "objects/object_drawing_01.png", "True", Null()),
    )

image mia_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_mia_night.jpg", "True", "backgrounds/location_school_locker_mia_day.jpg"),
    )

image ronda_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_ronda_night.jpg", "True", "backgrounds/location_school_locker_ronda_day.jpg"),
    )

image dexter_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_dexter_night.jpg", "True", "backgrounds/location_school_locker_dexter_day.jpg"),
    (725,540), ConditionSwitch("M_bissette.is_set('dexters book search') and not player.has_item('quick_mafs')", ConditionSwitch("game.timer.is_dark()", "objects/object_book_02_night.png", "True", "objects/object_book_02.png"), "True", Null()),
    )

image kevin_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_kevin_night.jpg", "True", "backgrounds/location_school_locker_kevin_day.jpg"),
    )

image annie_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_annie_night.jpg", "True", "backgrounds/location_school_locker_annie_day.jpg"),
    )

image roxxy_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_roxxy_night.jpg", "True", "backgrounds/location_school_locker_roxxy_day.jpg"),
    )

image judith_locker = Composite(
    (1024, 768), 
    (0,0), ConditionSwitch("game.timer.is_dark()", "backgrounds/location_school_locker_judith_night.jpg", "True", "backgrounds/location_school_locker_judith_day.jpg"),
    (394,607), ConditionSwitch("M_okita.is_state(S_okita_picture_taken) and not player.has_item('judith_glasses')", "objects/object_glasses_01.png", "True", Null()),
    (584,406), ConditionSwitch("M_dewitt.is_state(S_dewitt_judith_locker_search) and not player.has_item('broken_flute')", "objects/object_flute_01.png", "True", Null()),
    )



image libraryshelf = Composite(
    (1024, 768), 
    (0,0), "library_shelf", 
    (742,416), "buttons/book_01.png",
    (190,453), ConditionSwitch("M_bissette.get_state() == S_bissette_get_dictionary and not player.has_item(\"french_dictionary\")", "buttons/book_04.png", "True", Null()),
    (234,110), ConditionSwitch("not M_diane.finished_state(S_diane_check_bookshelf)", "buttons/book_02.png", "True", Null()),
    (406,440), ConditionSwitch("mrsj.started(mrsj_sex_ed) and not player.has_item(\"kamasutra\")" , "buttons/book_03.png", "True", Null()),
    (836,108), ConditionSwitch("not player.has_item(\"old_book\")", "buttons/book_05.png", "True", Null()), 
    )


image bedroom = ConditionSwitch(
    "MC_computer_broken", "backgrounds/location_home_bedroom_broken_day_blur.jpg",
    "True", "backgrounds/location_home_bedroom_day_blur.jpg",
    )
image bedroom_night = ConditionSwitch(
    "MC_computer_broken", "backgrounds/location_home_bedroom_broken_night_blur.jpg",
    "True", "backgrounds/location_home_bedroom_night_blur.jpg",
    )


image card_2 = ConditionSwitch(
    "not erik.known(erik_crown_card) or erik.completed(erik_crown_card)", "objects/item_card2.png",
    "erik.started(erik_crown_card)", "objects/item_card2_quest.png",
    "True", Null(),
    )
image card_2b = ConditionSwitch(
    "not erik.known(erik_crown_card) or erik.completed(erik_crown_card)", HoverImage("objects/item_card2.png"),
    "erik.started(erik_crown_card)", HoverImage("objects/item_card2_quest.png"),
    "True", Null(),
    )
image game_1 = ConditionSwitch(
    "not erik.completed(erik_favor) or erik.known(erik_favor_2)", "objects/item_game1.png",
    "erik.completed(erik_favor) and not erik.known(erik_favor_2)", "objects/item_game1_quest.png",
    "True", Null(),
    )
image game_1b = ConditionSwitch(
    "not erik.completed(erik_favor) or erik.known(erik_favor_2)", HoverImage("objects/item_game1.png"),
    "erik.completed(erik_favor) and not erik.known(erik_favor_2)", HoverImage("objects/item_game1_quest.png"),
    "True", Null(),
    )
image game_2 = ConditionSwitch(
    "not erik.known(erik_vr) or erik.completed(erik_vr)", "objects/item_game2.png",
    "erik.started(erik_vr)", "objects/item_game2_quest.png",
    "True", Null(),
    )
image game_2b = ConditionSwitch(
    "not erik.known(erik_vr) or erik.completed(erik_vr)", HoverImage("objects/item_game2.png"),
    "erik.started(erik_vr)", HoverImage("objects/item_game2_quest.png"),
    "True", Null(),
    )
image cosplay_1 = ConditionSwitch(
    "not June.known(june_cosplay) or June.completed(june_cosplay)", "objects/item_cosplay1.png",
    "June.started(june_cosplay)", "objects/item_cosplay1_quest.png",
    "True", Null(),
    )
image cosplay_1b = ConditionSwitch(
    "not June.known(june_cosplay) or June.completed(june_cosplay)", HoverImage("objects/item_cosplay1.png"),
    "June.started(june_cosplay)", HoverImage("objects/item_cosplay1_quest.png"),
    "True", Null(),
    )
image sex_6 = ConditionSwitch(
    "True", "objects/item_sex6.png",
    "False", "objects/item_sex6_quest.png",
    "True", Null(),
    )
image sex_6b = ConditionSwitch(
    "True", HoverImage("objects/item_sex6.png"),
    "False", HoverImage("objects/item_sex6_quest.png"),
    "True", Null(),
    )
image sex_17 = ConditionSwitch(
    "M_mia.get_state != S_mia_helen_outfit_request", "objects/item_sex17.png",
    "M_mia.get_state == S_mia_helen_outfit_request", "objects/item_sex17_quest.png",
    "True", Null(),
    )
image sex_17b = ConditionSwitch(
    "M_mia.get_state != S_mia_helen_outfit_request", HoverImage("objects/item_sex17.png"),
    "M_mia.get_state == S_mia_helen_outfit_request", HoverImage("objects/item_sex17_quest.png"),
    "True", Null(),
    )


image jenny_computer_bg = Composite(
    (1024,768),
    (0,0), "backgrounds/location_computer_jenny_02.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "computer_icon2",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_05.png",
    (215,250), "buttons/computer_icon_06.png",
    (215,360), "buttons/computer_icon_22.png",
    )
image jenny_computer_nude = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_03.png",
    (270,150), "buttons/computer_pic_03.png",
    )
image jenny_computer_family = Composite(
    (1024,768),
    (270,150), "computer_window1",
    (270,150), "buttons/computer_pic_05.png",
    )
image jenny_computer_swimsuit = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_02.png",
    (270,150), "buttons/computer_pic_01.png",
    )
image jenny_computer_igor = Composite(
    (1024,768),
    (270,150), "computer_window1",
    (270,150), "buttons/computer_pic_04.png",
    )
image jenny_computer_summertime = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_08.png",
    )
image jenny_computer_webcam = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_06.png",
    (719,495), "buttons/computer_button_04.png",
    )
image jenny_computer_toylist = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_04.png",
    )
image jenny_computer_livecrush = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_05.png",
    )
image jenny_computer_email = Composite(
    (1024,768),
    (135,150), "buttons/computer_window_11.png",
    (235,251), "buttons/computer_email_01.png",
    (235,291), "buttons/computer_email_02.png",
    (235,331), "buttons/computer_email_03_read.png",
    (235,371), "buttons/computer_email_04_read.png",
    (235,411), "buttons/computer_email_05_read.png",
    (235,451), "buttons/computer_email_06_read.png",
    )
image player_computer_bg_day = Composite(
    (1024,768),
    (0,0), "backgrounds/location_computer_player_02.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "computer_icon2",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_13.png",
    (215,250), "buttons/computer_icon_14.png",
    (215,360), "buttons/computer_icon_23.png",
    )
image player_computer_bg_night = Composite(
    (1024,768),
    (0,0), "backgrounds/location_computer_player_02_night.jpg",
    (105,603), "buttons/computer_button_02.png",
    (105,140), "buttons/computer_icon_01.png",
    (105,250), "computer_icon2",
    (105,360), "buttons/computer_icon_03.png",
    (105,470), "buttons/computer_icon_04.png",
    (215,140), "buttons/computer_icon_13.png",
    (215,250), "buttons/computer_icon_14.png",
    (215,360), "buttons/computer_icon_23.png",
    )
image player_computer_webscreen_connected = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_09.png",
    (370,380), "buttons/computer_icon_20.png",
    (500,380), "buttons/computer_icon_21.png",
    (623,380), "buttons/computer_icon_21.png",
    )
image player_computer_webscreen_disconnected = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_09.png",
    (304,302), "buttons/computer_window_10.png",
    )
image player_computer_webscreen_connecting = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_09b.png",
    (490,350), Transform("webcam_loading_circle"),
    )
image player_computer_egay_search = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_12.png",
    )
image player_computer_egay_purchased = Composite(
    (1024,768),
    (270,150), "buttons/computer_window_15.png",
    )

image player_computer_bg = ConditionSwitch(
    "not game.timer.is_dark()", "player_computer_bg_day",
    "game.timer.is_dark()", "player_computer_bg_night",
    "True", Null(),
    )





image player_computer_webscreen = ConditionSwitch(
    "connected == True", "player_computer_webscreen_connected",
    "connected == False", "player_computer_webscreen_disconnected",
    "True", Null(),
    )


image pink_channel_login = Composite(
    (1024,768),
    (0,0), "backgrounds/location_home_tv.jpg",
    (86,107), "buttons/tv_channel_08.png", 
    )


image hospital_cabinet_filled = Composite(
    (1024,768),
    (0,0), "backgrounds/location_hospital_cabinet.jpg",
    (98,173), "objects/object_pharmacy_01.png",
    (486,207), "objects/object_pharmacy_02.png",
    (770,226), "objects/object_pharmacy_03.png",
    (148,469), "objects/object_pharmacy_04.png",
    (331,502), "objects/object_pharmacy_05.png",
    (596,466), "objects/object_pharmacy_06.png",
    (732,457), "objects/object_pharmacy_07.png",
    )


image ivysex_10x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_10.png",
    (0,0), "characters/player/char_player_sex_36.png", 
    )
image ivysex_11x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_11.png",
    (0,0), "characters/player/char_player_sex_37.png", 
    )
image ivysex_11xc = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_11.png",
    (0,0), "characters/player/char_player_sex_38.png", 
    )
image ivysex_18x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_18.png",
    (0,0), "characters/player/char_player_sex_39.png", 
    )
image ivysex_19x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_19.png",
    (0,0), "characters/player/char_player_sex_40.png", 
    )
image ivysex_19xc = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_19.png",
    (0,0), "characters/player/char_player_sex_41.png", 
    )
image ivysex_20x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_20.png",
    (0,0), "characters/player/char_player_sex_40c.png", 
    )
image ivysex_21x = Composite(
    (1024,768),
    (0,0), "characters/ivy/char_ivy_sex_21.png",
    (0,0), "characters/player/char_player_sex_40b.png", 
    )

image ivysex 10 = ConditionSwitch( 
    "xray == True", "ivysex_10x",
    "xray == False", "characters/ivy/char_ivy_sex_10.png",
    "True", Null(),
    )
image ivysex 11 = ConditionSwitch( 
    "xray == True and ivy_cum_inside == False", "ivysex_11x",
    "xray == True and ivy_cum_inside == True", "ivysex_11xc",
    "xray == False", "characters/ivy/char_ivy_sex_11.png",
    "True", Null(),
    )
image ivysex 18 = ConditionSwitch( 
    "xray == True", "ivysex_18x",
    "xray == False", "characters/ivy/char_ivy_sex_18.png",
    "True", Null(),
    )
image ivysex 19 = ConditionSwitch( 
    "xray == True and ivy_cum_inside == False", "ivysex_19x",
    "xray == True and ivy_cum_inside == True", "ivysex_19xc",
    "xray == False", "characters/ivy/char_ivy_sex_19.png",
    "True", Null(),
    )
image ivysex 20 = ConditionSwitch( 
    "xray == True", "ivysex_20x",
    "xray == False", "characters/ivy/char_ivy_sex_20.png",
    "True", Null(),
    )
image ivysex 21 = ConditionSwitch( 
    "xray == True", "ivysex_21x",
    "xray == False", "characters/ivy/char_ivy_sex_21.png",
    "True", Null(),
    )



image debbies_59x = Composite(
    (711,752),
    (0,0), "characters/debbie/char_debbie_sex_59.png",
    (267,487), "characters/player/char_player_sex_54.png", 
    )
image debbies_60x = Composite(
    (700,751),
    (0,0), "characters/debbie/char_debbie_sex_60.png",
    (262,475), "characters/player/char_player_sex_55.png",  
    )
image debbies_60xc = Composite(
    (700,751),
    (0,0), "characters/debbie/char_debbie_sex_60.png",
    (262,475), "characters/player/char_player_sex_64.png",  
    )
image debbies_61x = Composite(
    (695,751),
    (0,0), "characters/debbie/char_debbie_sex_61.png",
    (276,464), "characters/player/char_player_sex_56.png", 
    )
image debbies_64x = Composite(
    (952,698),
    (0,0), "characters/debbie/char_debbie_sex_64.png",
    (0,0), "characters/player/char_player_sex_57.png", 
    )
image debbies_65x = Composite(
    (952,698),
    (0,0), "characters/debbie/char_debbie_sex_65.png",
    (0,0), "characters/player/char_player_sex_58.png", 
    )
image debbies_66x = Composite(
    (952,698),
    (0,0), "characters/debbie/char_debbie_sex_66.png",
    (0,0), "characters/player/char_player_sex_59.png", 
    )
image debbies_67x = Composite(
    (1024,698),
    (0,0), "characters/debbie/char_debbie_sex_67.png",
    (0,0), "characters/player/char_player_sex_59.png", 
    )
image debbies_68x = Composite(
    (1024,698),
    (0,0), "characters/debbie/char_debbie_sex_68.png",
    (0,0), "characters/player/char_player_sex_59.png", 
    )
image debbies_69x = Composite(
    (947,761),
    (0,0), "characters/debbie/char_debbie_sex_69.png",
    (0,63), "characters/player/char_player_sex_57.png", 
    )
image debbies_69xc = Composite(
    (947,761),
    (0,0), "characters/debbie/char_debbie_sex_69.png",
    (268,352), "characters/player/char_player_sex_60.png", 
    )
image debbies_97x = Composite(
    (655,744),
    (0,0), "characters/debbie/char_debbie_sex_97.png",
    (160,305), "characters/player/char_player_sex_61.png", 
    )
image debbies_98x = Composite(
    (651,744),
    (0,0), "characters/debbie/char_debbie_sex_98.png",
    (160,305), "characters/player/char_player_sex_62.png", 
    )
image debbies_99x = Composite(
    (647,727),
    (0,0), "characters/debbie/char_debbie_sex_99.png",
    (158,286), "characters/player/char_player_sex_63.png", 
    )
image debbies_103x = Composite(
    (901,509),
    (0,7), "characters/debbie/char_debbie_sex_103.png",
    (367,247), "characters/player/char_player_sex_65.png",
    )
image debbies_104x = Composite(
    (902,509),
    (0,0), "characters/debbie/char_debbie_sex_104.png",
    (414,231), "characters/player/char_player_sex_66.png",
    )
image debbies_105x = Composite(
    (903,509),
    (0,0), "characters/debbie/char_debbie_sex_105.png",
    (434,237), "characters/player/char_player_sex_67.png",
    )
image debbies_105xc = Composite(
    (903,509),
    (0,0), "characters/debbie/char_debbie_sex_105.png",
    (414,231), "characters/player/char_player_sex_68.png",
    )
image debbies_106c = Composite(
    (905,627),
    (0,0), "characters/debbie/char_debbie_sex_106.png",
    (374,307), "characters/player/char_player_sex_69.png",
    )















image debbies_129x = Composite(
    (536,626),
    (0,0), "characters/debbie/char_debbie_sex_129.png",
    (185,321), "characters/player/char_player_sex_79.png", 
    )

image debbies 59 = ConditionSwitch(
    "xray == True", "debbies_59x",
    "xray == False", "characters/debbie/char_debbie_sex_59.png",
    "True", Null(),
    )
image debbies 60 = ConditionSwitch(
    "xray == True and cum == True", "debbies_60xc",
    "xray == True", "debbies_60x",
    "xray == False", "characters/debbie/char_debbie_sex_60.png",
    "True", Null(),
    )
image debbies 61 = ConditionSwitch(
    "xray == True", "debbies_61x",
    "xray == False", "characters/debbie/char_debbie_sex_61.png",
    "True", Null(),
    )
image debbies 64 = ConditionSwitch( 
    "xray == True", "debbies_64x",
    "xray == False", "characters/debbie/char_debbie_sex_64.png",
    "True", Null(),
    )
image debbies 65 = ConditionSwitch( 
    "xray == True", "debbies_65x",
    "xray == False", "characters/debbie/char_debbie_sex_65.png",
    "True", Null(),
    )
image debbies 66 = ConditionSwitch( 
    "xray == True", "debbies_66x",
    "xray == False", "characters/debbie/char_debbie_sex_66.png",
    "True", Null(),
    )
image debbies 67 = ConditionSwitch( 
    "xray == True", "debbies_67x",
    "xray == False", "characters/debbie/char_debbie_sex_67.png",
    "True", Null(),
    )
image debbies 68 = ConditionSwitch( 
    "xray == True", "debbies_68x",
    "xray == False", "characters/debbie/char_debbie_sex_68.png",
    "True", Null(),
    )
image debbies 69 = ConditionSwitch( 
    "xray == True and cum == True", "debbies_69xc",
    "xray == True", "debbies_69x",
    "xray == False", "characters/debbie/char_debbie_sex_69.png",
    "True", Null(),
    )
image debbies 97 = ConditionSwitch( 
    "xray == True", "debbies_97x",
    "xray == False", "characters/debbie/char_debbie_sex_97.png",
    "True", Null(),
    )
image debbies 98 = ConditionSwitch(
    "xray == True", "debbies_98x",
    "xray == False", "characters/debbie/char_debbie_sex_98.png",
    "True", Null(),
    )
image debbies 99 = ConditionSwitch(
    "xray == True", "debbies_99x",
    "xray == False", "characters/debbie/char_debbie_sex_99.png",
    "True", Null(),
    )
image debbies 103 = ConditionSwitch( 
    "xray == True", "debbies_103x",
    "xray == False", "characters/debbie/char_debbie_sex_103.png",
    "True", Null(),
    )
image debbies 104 = ConditionSwitch( 
    "xray == True", "debbies_104x",
    "xray == False", "characters/debbie/char_debbie_sex_104.png",
    "True", Null(),
    )
image debbies 105 = ConditionSwitch( 
    "xray == True and cum == True", "debbies_105xc",
    "xray == True", "debbies_105x",
    "xray == False", "characters/debbie/char_debbie_sex_105.png",
    "True", Null(),
    )
image debbies 106 = ConditionSwitch( 
    "cum == True", "debbies_106c",
    "cum == False", "characters/debbie/char_debbie_sex_106.png",
    "True", Null(),
    )















image debbies 129 = ConditionSwitch(
    "xray == True", "debbies_129x",
    "xray == False", "characters/debbie/char_debbie_sex_129.png",
    "True", Null(),
    )


image dianesex_26x = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_26.png",
    (0,0), "characters/player/char_player_sex_06.png", 
    )
image dianesex_27x = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_27.png",
    (0,0), "characters/player/char_player_sex_07.png", 
    )
image dianesex_28x = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_28.png",
    (0,0), "characters/player/char_player_sex_08.png", 
    )
image dianesex_28xr = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_28.png",
    (0,0), "characters/player/char_player_sex_10.png", 
    )
image dianesex_30x = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_30.png",
    (0,0), "characters/player/char_player_sex_06.png", 
    )
image dianesex_31x = Composite(
    (945,768),
    (0,0), "characters/diane/char_diane_sex_31.png",
    (0,0), "characters/player/char_player_sex_09.png", 
    )
image dianesex_36o = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_36.png",
    (0,0), "characters/diane/char_diane_sex_37.png", 
    )
image dianesex_38o = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_38.png",
    (0,0), "characters/diane/char_diane_sex_39.png", 
    )
image dianesex_38x = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_38.png",
    (0,0), "characters/player/char_player_sex_42.png", 
    )
image dianesex_38ox = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_38.png",
    (0,0), "characters/diane/char_diane_sex_39.png", 
    (0,0), "characters/player/char_player_sex_42.png", 
    )
image dianesex_40o = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_40.png",
    (0,0), "characters/diane/char_diane_sex_41.png", 
    )
image dianesex_40x = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_40.png",
    (0,0), "characters/player/char_player_sex_43.png", 
    )
image dianesex_40ox = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_40.png",
    (0,0), "characters/diane/char_diane_sex_41.png", 
    (0,0), "characters/player/char_player_sex_43.png", 
    )
image dianesex_42o = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_42.png",
    (0,0), "characters/diane/char_diane_sex_43.png", 
    )
image dianesex_44o = Composite(
    (1024,768),
    (0,0), "characters/diane/char_diane_sex_44.png",
    (0,0), "characters/diane/char_diane_sex_45.png", 
    )
image dianesex_46o = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_46.png",
    (0,0), "characters/diane/char_diane_sex_47.png", 
    )
image dianesex_48o = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_48.png",
    (0,0), "characters/diane/char_diane_sex_49.png", 
    )
image dianes_57x = Composite(
    (711,752),
    (0,0), "characters/diane/char_diane_sex_57.png",
    (267,487), "characters/player/char_player_sex_54.png", 
    )
image dianesex_50o = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_50.png",
    (0,0), "characters/diane/char_diane_sex_51.png", 
    )
image dianesex_50x = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_50.png",
    (0,0), "characters/player/char_player_sex_46.png", 
    )
image dianesex_50ox = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_50.png",
    (0,0), "characters/diane/char_diane_sex_51.png", 
    (0,0), "characters/player/char_player_sex_46.png", 
    )
image dianesex_52o = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_52.png",
    (0,0), "characters/diane/char_diane_sex_53.png", 
    )
image dianesex_52x = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_52.png",
    (0,0), "characters/player/char_player_sex_47.png", 
    )
image dianesex_52ox = Composite(
    (869,768),
    (0,0), "characters/diane/char_diane_sex_52.png",
    (0,0), "characters/diane/char_diane_sex_53.png", 
    (0,0), "characters/player/char_player_sex_47.png", 
    )

image dianesex 26 = ConditionSwitch( 
    "xray == True", "dianesex_26x",
    "xray == False", "characters/diane/char_diane_sex_26.png",
    "True", Null(),
    )
image dianesex 27 = ConditionSwitch( 
    "xray == True", "dianesex_27x",
    "xray == False", "characters/diane/char_diane_sex_27.png",
    "True", Null(),
    )

image dianesex 30 = ConditionSwitch( 
    "xray == True", "dianesex_30x",
    "xray == False", "characters/diane/char_diane_sex_30.png",
    "True", Null(),
    )
image dianesex 31 = ConditionSwitch( 
    "xray == True", "dianesex_31x",
    "xray == False", "characters/diane/char_diane_sex_31.png",
    "True", Null(),
    )


image jennysex 77x = Composite(
    (484,737),
    (0,0), "characters/jenny/char_jenny_sex_77.png",
    (145,305), "characters/jenny/char_jenny_sex_78x.png"
    )
image jennysex 78x = Composite(
    (484,737),
    (0,0), "characters/jenny/char_jenny_sex_78.png",
    (145,305), "characters/jenny/char_jenny_sex_78x.png"
    )
image jennysex 79x = Composite(
    (470,740),
    (0,0), "characters/jenny/char_jenny_sex_79.png",
    (131,308), "characters/jenny/char_jenny_sex_79x.png"
    )
image jennysex 79bx = Composite(
    (470,740),
    (0,0), "characters/jenny/char_jenny_sex_79b.png",
    (131,308), "characters/jenny/char_jenny_sex_79x.png"
    )
image jennysex 80ac = Composite(
    (498,760),
    (0,0), "characters/jenny/char_jenny_sex_80.png",
    (145,324), "characters/player/char_player_sex_105.png"
    )
image jennysex 80bc = Composite(
    (498,760),
    (0,0), "characters/jenny/char_jenny_sex_80.png",
    (145,324), "characters/player/char_player_sex_106.png"
    )
image jennysex 80cc = Composite(
    (498,760),
    (0,0), "characters/jenny/char_jenny_sex_80.png",
    (145,324), "characters/player/char_player_sex_107.png"
    )
image jennysex 97x = Composite(
    (644,563),
    (0,0), "characters/jenny/char_jenny_sex_97.png",
    (20,279), "characters/player/char_player_sex_110.png"
    )
image jennysex 98x = Composite(
    (644,563),
    (0,0), "characters/jenny/char_jenny_sex_98.png",
    (20,279), "characters/player/char_player_sex_110.png"
    )
image jennysex 99x = Composite(
    (630,589),
    (0,0), "characters/jenny/char_jenny_sex_99.png",
    (6,305), "characters/player/char_player_sex_111.png"
    )
image jennysex 100x = Composite(
    (673,582),
    (0,0), "characters/jenny/char_jenny_sex_100.png",
    (49,298), "characters/player/char_player_sex_112.png"
    )
image jennysex 101x = Composite(
    (715,551),
    (0,0), "characters/jenny/char_jenny_sex_101.png",
    (91,267), "characters/player/char_player_sex_113.png"
    )
image jennysex 102x = Composite(
    (635,561),
    (0,0), "characters/jenny/char_jenny_sex_102.png",
    (11,277), "characters/player/char_player_sex_114.png" 
    )
image jennysex 102bx = Composite(
    (635,561),
    (0,0), "characters/jenny/char_jenny_sex_102b.png",
    (11,277), "characters/player/char_player_sex_114.png" 
    )
image jennysex 103x = Composite(
    (644,561),
    (0,0), "characters/jenny/char_jenny_sex_103.png",
    (20,277), "characters/player/char_player_sex_115.png"
    )
image jennysex 117x = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_117.png",
    (0,0), "characters/jenny/char_jenny_sex_117x.png"
    )
image jennysex 117bx = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_117b.png",
    (0,0), "characters/jenny/char_jenny_sex_117x.png"
    )
image jennysex 118x = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_118.png",
    (0,0), "characters/jenny/char_jenny_sex_118x.png"
    )
image jennysex 118bx = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_118b.png",
    (0,0), "characters/jenny/char_jenny_sex_118x.png"
    )
image jennysex 119x = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_119.png",
    (0,0), "characters/jenny/char_jenny_sex_119x.png"
    )
image jennysex 119bx = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_119b.png",
    (0,0), "characters/jenny/char_jenny_sex_119x.png"
    )
image jennysex 120x = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_120.png",
    (0,0), "characters/jenny/char_jenny_sex_120x.png"
    )
image jennysex 120bx = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_120b.png",
    (0,0), "characters/jenny/char_jenny_sex_120x.png"
    )
image jennysex 121x = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_121.png",
    (0,0), "characters/jenny/char_jenny_sex_121x.png"
    )
image jennysex 121bx = Composite(
    (672,579),
    (0,0), "characters/jenny/char_jenny_sex_121b.png",
    (0,0), "characters/jenny/char_jenny_sex_121x.png"
    )
image jennysex 122x = Composite(
    (939,667),
    (0,0), "characters/jenny/char_jenny_sex_122.png",
    (184,-6), "characters/jenny/char_jenny_sex_117x.png"
    )
image jennysex 123x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_123.png",
    (0,0), "characters/jenny/char_jenny_sex_123x.png"
    )
image jennysex 124x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_124.png",
    (0,0), "characters/jenny/char_jenny_sex_124x.png"
    )
image jennysex 125x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_125.png",
    (0,0), "characters/jenny/char_jenny_sex_125x.png"
    )
image jennysex 126x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_126.png",
    (0,0), "characters/jenny/char_jenny_sex_126x.png"
    )
image jennysex 127x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_127.png",
    (0,0), "characters/jenny/char_jenny_sex_127x.png"
    )
image jennysex 128x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_128.png",
    (0,0), "characters/jenny/char_jenny_sex_128x.png"
    )
image jennysex 129x = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_129.png",
    (0,0), "characters/jenny/char_jenny_sex_129x1.png"
    )
image jennysex 129bx = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_129.png",
    (0,0), "characters/jenny/char_jenny_sex_129x3.png"
    )
image jennysex 129cx = Composite(
    (928,743),
    (0,0), "characters/jenny/char_jenny_sex_129c.png",
    (0,0), "characters/jenny/char_jenny_sex_129x2.png"
    )
image jennysex 134 = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_134.png",
    (36,80), "characters/jenny/char_jenny_sex_136.png"
    )
image jennysex 134b = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_134.png",
    (58,37), "characters/jenny/char_jenny_sex_134b.png",
    (36,80), "characters/jenny/char_jenny_sex_136.png"
    )
image jennysex 134c = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_134.png",
    (58,37), "characters/jenny/char_jenny_sex_134b.png",
    (36,137), "characters/jenny/char_jenny_sex_136b.png"
    )
image jennysex 135 = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_135.png",
    (36,80), "characters/jenny/char_jenny_sex_136.png"
    )
image jennysex 135b = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_135.png",
    (58,37), "characters/jenny/char_jenny_sex_135b.png",
    (36,80), "characters/jenny/char_jenny_sex_136.png"
    )
image jennysex 135c = Composite(
    (887,653),
    (0,0), "characters/jenny/char_jenny_sex_135.png",
    (58,37), "characters/jenny/char_jenny_sex_135b.png",
    (36,137), "characters/jenny/char_jenny_sex_136b.png"
    )
image jennysex 137b = Composite(
    (1024,627),
    (0,0), "characters/jenny/char_jenny_sex_137.png",
    (79,280), "characters/jenny/char_jenny_sex_137b.png"
    )

image jennysex 77 = ConditionSwitch(
    "xray == True", "jennysex 77x",
    "xray == False", "characters/jenny/char_jenny_sex_77.png",
    "True",Null(),
    )
image jennysex 78 = ConditionSwitch(
    "xray == True", "jennysex 78x",
    "xray == False", "characters/jenny/char_jenny_sex_78.png",
    "True",Null(),
    )
image jennysex 79 = ConditionSwitch(
    "xray == True", "jennysex 79x",
    "xray == False", "characters/jenny/char_jenny_sex_79.png",
    "True",Null(),
    )
image jennysex 79b = ConditionSwitch(
    "xray == True", "jennysex 79bx",
    "xray == False", "characters/jenny/char_jenny_sex_79b.png",
    "True",Null(),
    )
image jennysex 80a = ConditionSwitch(
    "xray == True", "jennysex 80ac",
    "xray == False", "jennysex 80",
    "True",Null(),
    )
image jennysex 80b = ConditionSwitch(
    "xray == True", "jennysex 80bc",
    "xray == False", "jennysex 80",
    "True",Null(),
    )
image jennysex 80c = ConditionSwitch(
    "xray == True", "jennysex 80cc",
    "xray == False", "jennysex 80",
    "True",Null(),
    )
image jennysex 97 = ConditionSwitch(
    "xray == True", "jennysex 97x",
    "xray == False", "characters/jenny/char_jenny_sex_97.png",
    "True",Null(),
    )
image jennysex 98 = ConditionSwitch(
    "xray == True", "jennysex 98x",
    "xray == False", "characters/jenny/char_jenny_sex_98.png",
    "True",Null(),
    )
image jennysex 99 = ConditionSwitch(
    "xray == True", "jennysex 99x",
    "xray == False", "characters/jenny/char_jenny_sex_99.png",
    "True",Null(),
    )
image jennysex 100 = ConditionSwitch(
    "xray == True", "jennysex 100x",
    "xray == False", "characters/jenny/char_jenny_sex_100.png",
    "True",Null(),
    )
image jennysex 101 = ConditionSwitch(
    "xray == True", "jennysex 101x",
    "xray == False", "characters/jenny/char_jenny_sex_101.png",
    "True",Null(),
    )
image jennysex 102 = ConditionSwitch(
    "xray == True", "jennysex 102x",
    "xray == False", "characters/jenny/char_jenny_sex_102.png",
    "True",Null(),
    )
image jennysex 102b = ConditionSwitch(
    "xray == True", "jennysex 102bx",
    "xray == False", "characters/jenny/char_jenny_sex_102.png",
    "True",Null(),
    )
image jennysex 103 = ConditionSwitch(
    "xray == True", "jennysex 103x",
    "xray == False", "characters/jenny/char_jenny_sex_103.png",
    "True",Null(),
    )
image jennysex 117 = ConditionSwitch(
    "xray == True", "jennysex 117x",
    "xray == False", "characters/jenny/char_jenny_sex_117.png",
    "True",Null(),
    )
image jennysex 117b = ConditionSwitch(
    "xray == True", "jennysex 117bx",
    "xray == False", "characters/jenny/char_jenny_sex_117b.png",
    "True",Null(),
    )
image jennysex 118 = ConditionSwitch(
    "xray == True", "jennysex 118x",
    "xray == False", "characters/jenny/char_jenny_sex_118.png",
    "True",Null(),
    )
image jennysex 118b = ConditionSwitch(
    "xray == True", "jennysex 118bx",
    "xray == False", "characters/jenny/char_jenny_sex_118b.png",
    "True",Null(),
    )
image jennysex 119 = ConditionSwitch(
    "xray == True", "jennysex 119x",
    "xray == False", "characters/jenny/char_jenny_sex_119.png",
    "True",Null(),
    )
image jennysex 119b = ConditionSwitch(
    "xray == True", "jennysex 119bx",
    "xray == False", "characters/jenny/char_jenny_sex_119b.png",
    "True",Null(),
    )
image jennysex 120 = ConditionSwitch(
    "xray == True", "jennysex 120x",
    "xray == False", "characters/jenny/char_jenny_sex_120.png",
    "True",Null(),
    )
image jennysex 120b = ConditionSwitch(
    "xray == True", "jennysex 120bx",
    "xray == False", "characters/jenny/char_jenny_sex_120b.png",
    "True",Null(),
    )
image jennysex 121 = ConditionSwitch(
    "xray == True", "jennysex 121x",
    "xray == False", "characters/jenny/char_jenny_sex_121.png",
    "True",Null(),
    )
image jennysex 121b = ConditionSwitch(
    "xray == True", "jennysex 121bx",
    "xray == False", "characters/jenny/char_jenny_sex_121b.png",
    "True",Null(),
    )
image jennysex 122 = ConditionSwitch(
    "xray == True", "jennysex 122x",
    "xray == False", "characters/jenny/char_jenny_sex_122.png",
    "True",Null(),
    )
image jennysex 123 = ConditionSwitch(
    "xray == True", "jennysex 123x",
    "xray == False", "characters/jenny/char_jenny_sex_123.png",
    "True",Null(),
    )
image jennysex 124 = ConditionSwitch(
    "xray == True", "jennysex 124x",
    "xray == False", "characters/jenny/char_jenny_sex_124.png",
    "True",Null(),
    )
image jennysex 125 = ConditionSwitch(
    "xray == True", "jennysex 125x",
    "xray == False", "characters/jenny/char_jenny_sex_125.png",
    "True",Null(),
    )
image jennysex 126 = ConditionSwitch(
    "xray == True", "jennysex 126x",
    "xray == False", "characters/jenny/char_jenny_sex_126.png",
    "True",Null(),
    )
image jennysex 127 = ConditionSwitch(
    "xray == True", "jennysex 127x",
    "xray == False", "characters/jenny/char_jenny_sex_127.png",
    "True",Null(),
    )
image jennysex 128 = ConditionSwitch(
    "xray == True", "jennysex 128x",
    "xray == False", "characters/jenny/char_jenny_sex_128.png",
    "True",Null(),
    )
image jennysex 129 = ConditionSwitch(
    "xray == True", "jennysex 129x",
    "xray == False", "characters/jenny/char_jenny_sex_129.png",
    "True",Null(),
    )
image jennysex 129b = ConditionSwitch(
    "xray == True", "jennysex 129bx",
    "xray == False", "characters/jenny/char_jenny_sex_129.png",
    "True",Null(),
    )
image jennysex 129c = ConditionSwitch(
    "xray == True", "jennysex 129cx",
    "xray == False", "characters/jenny/char_jenny_sex_129c.png",
    "True",Null(),
    )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
