
image menu_cloud_large:
    subpixel True
    'backgrounds/menu_cloud_large.png'
    block:
        pos (590, 65)
        linear 110.0 xpos -320
        repeat

image menu_cloud_small:
    subpixel True
    'backgrounds/menu_cloud_small.png'
    block:
        pos (600, 175)
        linear 155.0 xpos -170
        pause 30
        repeat



image webcam_loading_circle:
    "buttons/loading_circle.png"
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 1 rotate 360
    repeat


image player 155_156_156b_156:
    Transform("player 155")
    pause .2
    Transform("player 156")
    pause .2
    Transform("player 156b")
    pause .2
    Transform("player 156")
    pause .2
    repeat

image player 157_158_159:
    Transform("player 157")
    pause .2
    Transform("player 158")
    pause .2
    Transform("player 159")
    pause .2
    repeat

image player 239_240:
    Transform("player 239")
    pause .4
    Transform("player 240")
    pause .4
    repeat

image player 239_240f:
    Transform("player 239f")
    pause .4
    Transform("player 240f")
    pause .4
    repeat

image player 694_694b:
    Transform("characters/player/char_player_694.png")
    pause M_player.get('sex speed')
    Transform("characters/player/char_player_694b.png",xoffset=2)
    pause M_player.get('sex speed')
    repeat

image player 496c_496d_496e_496d_496c:
    "characters/player/char_player_496c.png"
    pause M_player.get('sex speed')
    "characters/player/char_player_496d.png"
    pause M_player.get('sex speed')
    "characters/player/char_player_496e.png"
    pause M_player.get('sex speed')
    "characters/player/char_player_496d.png"
    pause M_player.get('sex speed')
    "characters/player/char_player_496c.png"
    pause M_player.get('sex speed')
    repeat

image player_hand 629b_629c:
    Transform("player_hand 629b")
    pause .4
    Transform("player_hand 629c")
    pause .4
    repeat

image player_arms 488c_488d:
    Transform("player_arms 488c")
    pause .4
    Transform("player_arms 488d")
    pause .4
    repeat

image player_arms 488c_488d_488e:
    Transform("player_arms 488c")
    pause .4
    Transform("player_arms 488d")
    pause .4
    Transform("player_arms 488e")
    pause .4
    repeat

image player_arms 488e_488f:
    Transform("player_arms 488e")
    pause .4
    Transform("player_arms 488f")
    pause .4
    repeat

image playersex 134_135_136_137:
    Transform("playersex 134")
    pause M_jenny.get("sex speed")
    Transform("playersex 135")
    pause M_jenny.get("sex speed")
    Transform("playersex 136")
    pause M_jenny.get("sex speed")
    Transform("playersex 137")
    pause M_jenny.get("sex speed")
    repeat

image player 316_317:
    Transform("characters/player/char_player_316.png")
    pause .4
    Transform("characters/player/char_player_317.png")
    pause .4
    repeat

image location_debbiebed 2_3 = Animation("backgrounds/location_home_debbiebed02.jpg", .4, "backgrounds/location_home_debbiebed03.jpg", .4)

image player medmo 155_156_156b:
    "characters/player/char_player_155.png"
    pause M_mom.get("sex speed")*5/6
    "characters/player/char_player_156.png"
    pause M_mom.get("sex speed")*5/6
    "characters/player/char_player_156b.png"
    pause M_mom.get("sex speed")*5/6
    repeat

image player 427d_e:
    Transform("player 427d")
    pause .4
    Transform("player 427e")
    pause .4
    repeat


image debbie_shower 6a_6b_6c:
    Transform("shower06a")
    pause 1.2
    Transform("shower06b")
    pause .8
    Transform("shower06c")
    pause .8
    Transform("shower06b")
    pause .8
    Transform("shower06a")
    pause 1.2
    Transform("shower06c")
    pause .8
    repeat

image debbie_peek_sequence 2_3 = Animation("backgrounds/location_home_debbiepeak_day02.jpg", .4, "backgrounds/location_home_debbiepeak_day03.jpg", .4)

image dream_debbie 1_2 = Animation("backgrounds/location_home_dream_debbie_01.jpg", .4, "backgrounds/location_home_dream_debbie_02.jpg", .4)

image debbie 80_79 = Animation("characters/debbie/char_debbie_80.png", .5, "characters/debbie/char_debbie_79.png", .5)

image debbie 49_50_50b:
    Transform("debbie 49")
    pause .4
    Transform("debbie 50", xoffset = 5)
    pause .4
    Transform("debbie 50b")
    pause .4
    repeat

image debbie 194_195_196:
    Transform("debbie 194")
    pause M_mom.get("sex speed")
    Transform("debbie 195")
    pause M_mom.get("sex speed")
    Transform("debbie 196")
    pause M_mom.get("sex speed")
    repeat

image debbie 194f_195f_196f:
    Transform("debbie 194f")
    pause M_mom.get("sex speed")
    Transform("debbie 195f")
    pause M_mom.get("sex speed")
    Transform("debbie 196f")
    pause M_mom.get("sex speed")
    repeat

image debbie 209_210:
    Transform("debbie 209")
    pause .4
    Transform("debbie 210")
    pause .4
    repeat

image debbie 212b_215b:
    Transform("debbie 212b")
    pause .4
    Transform("debbie 215b")
    pause .4
    repeat

image debbie_arms_car 5_5b_5c_5b:
    Transform("debbie_arms_car 5")
    pause M_mom.get("sex speed")
    Transform("debbie_arms_car 5b")
    pause M_mom.get("sex speed")
    Transform("debbie_arms_car 5c")
    pause M_mom.get("sex speed")
    Transform("debbie_arms_car 5b")
    pause M_mom.get("sex speed")
    repeat

image debbief 8flip_8bf_8cf_8df_8ef_8ff_8gf:
    im.Flip("characters/debbie/char_debbie_front_08.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08b.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08c.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08d.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08e.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08f.png", horizontal=True)
    pause M_mom.get("sex speed")
    im.Flip("characters/debbie/char_debbie_front_08g.png", horizontal=True)
    pause M_mom.get("sex speed")
    repeat

image debbiefa 3f_3bf:
    im.Flip("characters/debbie/char_debbie_front_arms_03.png", horizontal=True)
    pause M_mom.get("sex speed")
    Transform("debbiefa 3bf", xoffset=-8, yoffset=-3)
    pause M_mom.get("sex speed")
    repeat

image debbiefa 5bf_5cf:
    Transform("debbiefa 5bf", xoffset=-12, yoffset=5)
    pause M_mom.get("sex speed")
    Transform("debbiefa 5cf", xoffset=-12, yoffset=5)
    pause M_mom.get("sex speed")
    repeat

image debbie_car_bj 8_8b_8c_8d_8e_8f_8g:
    Transform("debbie_car_bj 8")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8b")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8c")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8d")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8e")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8f")
    pause M_mom.get('sex speed')
    Transform("debbie_car_bj 8g")
    pause M_mom.get('sex speed')
    repeat

image debbied 4_5:
    "characters/debbie/char_debbie_dream_04.png"
    pause M_mom.get('sex speed')
    "characters/debbie/char_debbie_dream_05.png"
    pause M_mom.get('sex speed')
    repeat

image debbies 7_8 = Animation("characters/debbie/char_debbie_sex_07.png", .4, "characters/debbie/char_debbie_sex_08.png", .4)
image debbies 13_14 = Animation("characters/debbie/char_debbie_sex_13.png", .4, "characters/debbie/char_debbie_sex_14.png", .4)
image debbies 16_17 = Animation("characters/debbie/char_debbie_sex_16.png", .45, "characters/debbie/char_debbie_sex_17.png", .45)
image debbies 37_36 = Animation("characters/debbie/char_debbie_sex_37.png", .45, "characters/debbie/char_debbie_sex_36.png", .45)
image debbies 41_76 = Animation("characters/debbie/char_debbie_sex_41.png", .5, "characters/debbie/char_debbie_sex_76.png", .5)

image debbies 49_50:
    Image("characters/debbie/char_debbie_49.png")
    pause .4
    Image("characters/debbie/char_debbie_50.png", xoffset = 5)
    pause .4
    repeat

image debbies 20h_20i_20j_20k_20l_20m_20n_20o:
    "characters/debbie/char_debbie_sex_20h.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20i.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20j.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20k.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20l.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20m.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20n.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20o.png"
    pause M_mom.get("sex speed")
    repeat

image debbies 20p_20q:
    "characters/debbie/char_debbie_sex_20p.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_20q.png"
    pause M_mom.get("sex speed")
    repeat

image debbies 52_53_52_51 = Animation("characters/debbie/char_debbie_sex_52.png", .4, "characters/debbie/char_debbie_sex_53.png", .4, "characters/debbie/char_debbie_sex_52.png", .4, "characters/debbie/char_debbie_sex_51.png", .4)
image debbies 56_55 = Animation("characters/debbie/char_debbie_sex_56.png", .35, "characters/debbie/char_debbie_sex_55.png", .35)

image debbies 59_60_61:
    Transform("debbies 59")
    pause M_mom.get("sex speed")
    Transform("debbies 60")
    pause M_mom.get("sex speed")
    Transform("debbies 61")
    pause M_mom.get("sex speed")
    repeat

image debbies 65_66_64:
    Transform("debbies 65")
    pause M_mom.get("sex speed")*2/4
    Transform("debbies 66")
    pause M_mom.get("sex speed")
    Transform("debbies 64")
    pause M_mom.get("sex speed")
    repeat

image debbies 68_67 = Animation("debbies 68", .4, "debbies 67", .4)
image debbies 72_71 = Animation("characters/debbie/char_debbie_sex_72.png", .4, "characters/debbie/char_debbie_sex_71.png", .4)
image debbies 73_74 = Animation("characters/debbie/char_debbie_sex_73.png", .4, "characters/debbie/char_debbie_sex_74.png", .4)
image debbies 81_82 = Animation("characters/debbie/char_debbie_sex_81.png", .5, "characters/debbie/char_debbie_sex_82.png", .5)
image debbies 85_86 = Animation("characters/debbie/char_debbie_sex_85.png", .5, "characters/debbie/char_debbie_sex_86.png", .5)

image debbies 88_89:
    Image("characters/debbie/char_debbie_sex_88.png", xoffset = 0)
    pause .5
    Image("characters/debbie/char_debbie_sex_89.png", xoffset = -2)
    pause .5
    repeat

image debbies 93_94:
    Image("characters/debbie/char_debbie_sex_93.png", xoffset = 0)
    pause .4
    Image("characters/debbie/char_debbie_sex_94.png", xoffset = -2)
    pause .4
    repeat

image debbies 97_98:
    Transform("debbies 97")
    pause .4
    Transform("debbies 98", xoffset = -2)
    pause .4
    repeat

image debbies 113_114:
    Image("characters/debbie/char_debbie_sex_113.png", xoffset = 0)
    pause .4
    Image("characters/debbie/char_debbie_sex_114.png", xoffset = 4)
    pause .4
    repeat

image debbies 126_126b_126c_126d_126e_126f_126g_126h_126i_126j:
    Transform("debbies 126")
    pause M_mom.get('sex speed')
    Transform("debbies 126b")
    pause M_mom.get('sex speed')
    Transform("debbies 126c")
    pause M_mom.get('sex speed')
    Transform("debbies 126d")
    pause M_mom.get('sex speed')
    Transform("debbies 126e")
    pause M_mom.get('sex speed')
    Transform("debbies 126f")
    pause M_mom.get('sex speed')
    Transform("debbies 126g")
    pause M_mom.get('sex speed')
    Transform("debbies 126h")
    pause M_mom.get('sex speed')
    Transform("debbies 126i")
    pause M_mom.get('sex speed')
    Transform("debbies 126j")
    pause M_mom.get('sex speed')
    repeat










image debbies 133_134:
    "characters/debbie/char_debbie_sex_133.png"
    pause M_mom.get("sex speed")
    Image("characters/debbie/char_debbie_sex_134.png", xoffset = 9)
    pause M_mom.get("sex speed")
    repeat

image debbies 146_147:
    "characters/debbie/char_debbie_sex_146.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_147.png"
    pause M_mom.get("sex speed")
    repeat

image debbies 151_152_153_154_155_156_157:
    "characters/debbie/char_debbie_sex_151.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_152.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_153.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_154.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_155.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_156.png"
    pause M_mom.get("sex speed")
    "characters/debbie/char_debbie_sex_157.png"
    pause M_mom.get("sex speed")
    repeat

image debbies 170_171_172_173_174_175_176_177:
    Transform("debbies 170")
    pause M_mom.get('sex speed')/3
    Transform("debbies 171")
    pause M_mom.get('sex speed')/3
    Transform("debbies 172")
    pause M_mom.get('sex speed')/3
    Transform("debbies 173")
    pause M_mom.get('sex speed')/3
    Transform("debbies 174")
    pause M_mom.get('sex speed')/3
    Transform("debbies 175")
    pause M_mom.get('sex speed')/3
    Transform("debbies 176")
    pause M_mom.get('sex speed')/3
    Transform("debbies 177")
    pause M_mom.get('sex speed')/3
    repeat

image debbie_robe 194b_195b_196b:
    Transform("debbie_robe 194b")
    pause M_mom.get("sex speed")
    Transform("debbie_robe 195b")
    pause M_mom.get("sex speed")
    Transform("debbie_robe 196b")
    pause M_mom.get("sex speed")
    repeat

image debbie_robe 194bf_195bf_196bf:
    Transform("debbie_robe 194bf")
    pause M_mom.get("sex speed")
    Transform("debbie_robe 195bf")
    pause M_mom.get("sex speed")
    Transform("debbie_robe 196bf")
    pause M_mom.get("sex speed")
    repeat


image jenny 69_68:
    Transform("jenny 69")
    pause .4
    Transform("jenny 68")
    pause .4
    repeat
image jenny 74_83:
    Transform("jenny 74")
    pause sis_sybian_speed
    Transform("jenny 83", xoffset = 2)
    pause sis_sybian_speed
    repeat
image jenny 93_94:
    Transform("jenny 93")
    pause .6
    Transform("jenny 94")
    pause .6
    repeat
image jenny 95_94:
    Transform("jenny 95")
    pause .6
    Transform("jenny 94")
    pause .6
    repeat
image jenny 99_100_101:
    Transform("jenny 99")
    pause .4
    Transform("jenny 100")
    pause .4
    Transform("jenny 101")
    pause .4
    repeat
image jenny 117_118_119_116:
    Transform("jenny 117")
    pause .4
    Transform("jenny 118", xoffset = 6)
    pause .4
    Transform("jenny 119", xoffset = 8)
    pause .4
    Transform("jenny 116", xoffset = 4)
    pause .4
    repeat
image jenny 124_125_126_123:
    Transform("jenny 124")
    pause .4
    Transform("jenny 125")
    pause .4
    Transform("jenny 126")
    pause .4
    Transform("jenny 123")
    pause .4
    repeat
image jenny 145_146_147_148:
    Transform("jenny 145")
    pause .4
    Transform("jenny 146")
    pause .4
    Transform("jenny 147")
    pause .4
    Transform("jenny 148")
    pause .4
    repeat
image jennysex 2_3_1_4:
    Transform("jennysex 2")
    pause .4
    Transform("jennysex 3")
    pause .4
    Transform("jennysex 1")
    pause .4
    Transform("jennysex 4")
    pause .4
    repeat
image jennysex 23_24_25_22:
    Transform("jennysex 23")
    pause .4
    Transform("jennysex 24")
    pause .4
    Transform("jennysex 25")
    pause .4
    Transform("jennysex 22")
    pause .4
    repeat
image jennysex 28_29_30_31:
    Transform("jennysex 28")
    pause .4
    Transform("jennysex 29")
    pause .4
    Transform("jennysex 30")
    pause .4
    Transform("jennysex 31")
    pause .4
    repeat
image jennysex 36_37_38_35:
    Transform("jennysex 36", xoffset = -8)
    pause .4
    Transform("jennysex 37", xoffset = 45)
    pause .4
    Transform("jennysex 38", xoffset = 51)
    pause .4
    Transform("jennysex 35")
    pause .4
    repeat
image jennysex 49_84:
    Transform("jennysex 49")
    pause .4
    Transform("jennysex 84")
    pause .4
    repeat
image jennysex 54_55:
    Transform("jennysex 54")
    pause .6
    Transform("jennysex 55")
    pause .6
    repeat
image jennysex 60_59:
    Transform("jennysex 60")
    pause .6
    Transform("jennysex 59")
    pause .6
    repeat
image jennysex 62_64:
    Transform("jennysex 62")
    pause .4
    Transform("jennysex 63", xoffset = 2)
    pause .4
    repeat
image jennysex 78_79:
    Transform("jennysex 78")
    pause .4
    Transform("jennysex 79", xoffset = 7)
    pause .4
    repeat
image jennysex 79_78:
    Transform("jennysex 79")
    pause .4
    Transform("jennysex 78", xoffset = -7)
    pause .4
    repeat
image jennysex 42_43_44_41:
    Transform("jennysex 42", xoffset = 2)
    pause .4
    Transform("jennysex 43", xoffset = 3)
    pause .4
    Transform("jennysex 44", xoffset = 2)
    pause .4
    Transform("jennysex 41")
    pause .4
    repeat
image jennysex 92_93_94_95:
    Transform("jennysex 92")
    pause .4
    Transform("jennysex 93", xoffset = 23)
    pause .4
    Transform("jennysex 94", xoffset = 2)
    pause .4
    Transform("jennysex 95")
    pause .4
    repeat

image jennysex 98_99_100_101:
    Transform("jennysex 98")
    pause M_jenny.get("sex speed")
    Transform("jennysex 99", xoffset = 7)
    pause M_jenny.get("sex speed")
    Transform("jennysex 100", xoffset = -14)
    pause M_jenny.get("sex speed")
    Transform("jennysex 101", xoffset = -35)
    pause M_jenny.get("sex speed")
    repeat

image jennysex 102_103:
    Transform("white")
    pause .1
    Transform("jennysex 102")
    pause .6
    Transform("jennysex 103", xoffset = -5)
    pause .4
    repeat
image jennysex 114b_115b:
    Transform("jennysex 114b")
    pause .6
    Transform("jennysex 115b")
    pause .6
    repeat

image jennysex 117_118_119_120_121:
    Transform("jennysex 117")
    pause M_jenny.get("sex speed")
    Transform("jennysex 118", xoffset = 2)
    pause M_jenny.get("sex speed")
    Transform("jennysex 119", xoffset = 23)
    pause M_jenny.get("sex speed")
    Transform("jennysex 120", xoffset = 29)
    pause M_jenny.get("sex speed")
    Transform("jennysex 121", xoffset = 14)
    pause M_jenny.get("sex speed")
    repeat

image jennysex 123_124_125_126_127:
    Transform("jennysex 123")
    pause M_jenny.get("sex speed")
    Transform("jennysex 124")
    pause M_jenny.get("sex speed")
    Transform("jennysex 125")
    pause M_jenny.get("sex speed")
    Transform("jennysex 126")
    pause M_jenny.get("sex speed")
    Transform("jennysex 127")
    pause M_jenny.get("sex speed")
    repeat

image jennysex 129b_128:
    Transform("jennysex 129b")
    pause .6
    Transform("white")
    pause .1
    Transform("jennysex 128")
    pause .4
    repeat
image jennysex 139_140_141_142 = Animation("characters/jenny/char_jenny_sex_139.png", .4, "characters/jenny/char_jenny_sex_140.png", .4, "characters/jenny/char_jenny_sex_141.png", .3, "characters/jenny/char_jenny_sex_142.png", .2)
image jennysex 139b_140b_141b_142b = Animation("characters/jenny/char_jenny_sex_139b.png", .4, "characters/jenny/char_jenny_sex_140b.png", .4, "characters/jenny/char_jenny_sex_141b.png", .3, "characters/jenny/char_jenny_sex_142b.png", .2)


image diane_masturbate 1_2:
    "backgrounds/location_diane_kitchen_vegies01.jpg"
    pause M_diane.get("sex speed")
    "backgrounds/location_diane_kitchen_vegies01b.jpg",
    pause M_diane.get("sex speed")
    repeat


image ivysex 4_3:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_19.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_19.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_04.png", xoffset = 242, yoffset = 169)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_03.png", xoffset = 242, yoffset = 169)
        pause M_ivy.get("sex speed")
        repeat
image ivysex 6_5:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_19.png", xoffset = -2, yoffset = 439)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_19.png", xoffset = -2, yoffset = 439)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_06.png", xoffset = 249, yoffset = 85)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_05.png", xoffset = 249, yoffset = 63)
        pause M_ivy.get("sex speed")
        repeat
image ivysex 10_11:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_20.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_21.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_10.png", xoffset = 148, yoffset = 61)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_11.png", xoffset = 148, yoffset = 92)
        pause M_ivy.get("sex speed")
        repeat
image ivysex 18_19:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_18.png", xoffset = 246, yoffset = 104)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_19.png", xoffset = 244, yoffset = 78)
        pause M_ivy.get("sex speed")
        repeat
image ivysex_xray 36_37:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_20.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_21.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_10.png", xoffset = 148, yoffset = 61)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_11.png", xoffset = 148, yoffset = 92)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/player/char_player_sex_36.png", xoffset = 428, yoffset = 331)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_37.png", xoffset = 422, yoffset = 370)
        pause M_ivy.get("sex speed")
        repeat
image ivysex_xray 39_40:
    contains:
        subpixel True
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_22.png", xoffset = -3, yoffset = 443)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        subpixel True
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_29.png", xoffset = 486, yoffset = 436)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/ivy/char_ivy_sex_18.png", xoffset = 246, yoffset = 104)
        pause M_ivy.get("sex speed")
        Image("characters/ivy/char_ivy_sex_19.png", xoffset = 244, yoffset = 78)
        pause M_ivy.get("sex speed")
        repeat
    contains:
        Image("characters/player/char_player_sex_39.png", xoffset = 410, yoffset = 329)
        pause M_ivy.get("sex speed")
        Image("characters/player/char_player_sex_40.png", xoffset = 419, yoffset = 393)
        pause M_ivy.get("sex speed")
        repeat


image cassie 26_27:
    "characters/cassie/char_cassie_26.png"
    pause .4
    Image("characters/cassie/char_cassie_27.png", xoffset = 7)
    pause .4
    repeat

image cassie 26_28:
    "characters/cassie/char_cassie_26.png"
    pause .4
    Image("characters/cassie/char_cassie_28.png", xoffset = 12)
    pause .4
    repeat


image judith 25_23 = Animation("characters/judith/char_judith_25.png", .4, "characters/judith/char_judith_23.png", .4)
image judith 31_32 = Animation("characters/judith/char_judith_31.png", .4, "characters/judith/char_judith_32.png", .4)
image judith 36_37_38 = Animation("characters/judith/char_judith_36.png", .4, "characters/judith/char_judith_37.png", .4, "characters/judith/char_judith_38.png", .4)

image judith 72c_72d:
    "characters/judith/char_judith_72c.png"
    pause 0.5
    "characters/judith/char_judith_72d.png"
    pause 0.5
    repeat


image windowmianight03a_b = Animation("backgrounds/location_telescope_mia_night03a.jpg", .4, "backgrounds/location_telescope_mia_night03b.jpg", .4)
image windowerikday04a_b = Animation("backgrounds/location_telescope_erik_day04a.jpg", .4, "backgrounds/location_telescope_erik_day04b.jpg", .4)
image windowerikday05a_b = Animation("backgrounds/location_telescope_erik_day05a.jpg", .4, "backgrounds/location_telescope_erik_day05b.jpg", .4)


image library 1_2 = Animation("characters/library/char_library_01.png", .4, "characters/library/char_library_02.png", .4)


image anna 19_20 = Animation("characters/anna/char_anna_19.png", .8, "characters/anna/char_anna_20.png", 1.6)
image anna_slow 31_32 = Animation("characters/anna/char_anna_31.png", .8, "characters/anna/char_anna_32.png", .8)
image anna_fast 31_32 = Animation("characters/anna/char_anna_31.png", .4, "characters/anna/char_anna_32.png", .4)


image erik_house_cs01_01b = Animation("backgrounds/location_erik_house_cutscene01.jpg", .4, "backgrounds/location_erik_house_cutscene01b.jpg", .6)


image dexter 25_26:
    "characters/dexter/char_dexter_25.png"
    pause 0.25
    Image("characters/dexter/char_dexter_26.png", xoffset = -1)
    pause 0.25
    repeat




image mrsjsex 8_9:
    "characters/mrsj/char_mrsj_sex_08.png"
    pause 0.6
    "characters/mrsj/char_mrsj_sex_09.png"
    pause 0.4
    repeat
image mrsjsex 12_13_14_13:
    "characters/mrsj/char_mrsj_sex_12.png"
    pause 0.6
    "characters/mrsj/char_mrsj_sex_13.png"
    pause 0.4
    "characters/mrsj/char_mrsj_sex_14.png"
    pause 0.5
    "characters/mrsj/char_mrsj_sex_13.png"
    pause 0.4
    repeat
image mrsjsex 13_14_13_12:
    "characters/mrsj/char_mrsj_sex_13.png"
    pause 0.4
    "characters/mrsj/char_mrsj_sex_14.png"
    pause 0.5
    "characters/mrsj/char_mrsj_sex_13.png"
    pause 0.4
    "characters/mrsj/char_mrsj_sex_12.png"
    pause 0.6
    repeat
image mrsjsex 12b_13b_14b:
    "characters/mrsj/char_mrsj_sex_12b.png"
    pause 0.6
    "characters/mrsj/char_mrsj_sex_13b.png"
    pause 0.4
    "characters/mrsj/char_mrsj_sex_14b.png"
    pause 0.5
    "characters/mrsj/char_mrsj_sex_13b.png"
    pause 0.4
    repeat
image mrsjsex 15_16_17:
    "characters/mrsj/char_mrsj_sex_15.png"
    pause 0.6
    "characters/mrsj/char_mrsj_sex_16.png"
    pause 0.4
    "characters/mrsj/char_mrsj_sex_17.png"
    pause 0.5
    repeat
image mrsjsex 21_22_23_24_25:
    "characters/mrsj/char_mrsj_sex_21.png"
    pause M_mrsj.get("sex speed")*2/3
    "characters/mrsj/char_mrsj_sex_22.png"
    pause M_mrsj.get("sex speed")
    "characters/mrsj/char_mrsj_sex_23.png"
    pause M_mrsj.get("sex speed")
    "characters/mrsj/char_mrsj_sex_24.png"
    pause M_mrsj.get("sex speed")*2.5/3
    "characters/mrsj/char_mrsj_sex_25.png"
    pause M_mrsj.get("sex speed")*2/3
    repeat
image mrsjsex 28_29_30:
    Transform("characters/mrsj/char_mrsj_sex_28.png", yoffset=42)
    pause M_mrsj.get("sex speed")*2/3
    Transform("characters/mrsj/char_mrsj_sex_29.png", yoffset=36)
    pause M_mrsj.get("sex speed")
    Transform("characters/mrsj/char_mrsj_sex_30.png", xoffset=-4, yoffset=41)
    pause M_mrsj.get("sex speed")
    repeat
image mrsjsex 36_37:
    Transform("characters/mrsj/char_mrsj_sex_36.png", yoffset=70)
    pause M_mrsj.get("sex speed")
    Transform("characters/mrsj/char_mrsj_sex_37.png", yoffset=60)
    pause M_mrsj.get("sex speed")
    repeat
image mrsjsex 42_43_44_45_46:
    Transform("characters/mrsj/char_mrsj_sex_42.png", xoffset=-14)
    pause M_mrsj.get("sex speed")
    Transform("characters/mrsj/char_mrsj_sex_43.png", xoffset=-20)
    pause M_mrsj.get("sex speed")*2/3
    Transform("characters/mrsj/char_mrsj_sex_44.png", xoffset=-30)
    pause M_mrsj.get("sex speed")*2.5/3
    Transform("characters/mrsj/char_mrsj_sex_45.png", xoffset=-23)
    pause M_mrsj.get("sex speed")*2/3
    Transform("characters/mrsj/char_mrsj_sex_46.png", xoffset=-19)
    pause M_mrsj.get("sex speed")*2/3
    repeat


image junesex 4b_5b_6b_7b_8b:
    "characters/june/char_june_sex_04b.png"
    pause M_june.get("sex speed")*2/3
    "characters/june/char_june_sex_05b.png"
    pause M_june.get("sex speed")*2.5/3
    "characters/june/char_june_sex_06b.png"
    pause M_june.get("sex speed")*2.5/3
    "characters/june/char_june_sex_07b.png"
    pause M_june.get("sex speed")*2/3
    "characters/june/char_june_sex_08b.png"
    pause M_june.get("sex speed")
    repeat
image junesex 4_5_6_7_8:
    "characters/june/char_june_sex_04.png"
    pause M_june.get("sex speed")*2/3
    "characters/june/char_june_sex_05.png"
    pause M_june.get("sex speed")*2.5/3
    "characters/june/char_june_sex_06.png"
    pause M_june.get("sex speed")*2.5/3
    "characters/june/char_june_sex_07.png"
    pause M_june.get("sex speed")*2/3
    "characters/june/char_june_sex_08.png"
    pause M_june.get("sex speed")
    repeat


image telescope_mia_masturbate:
    Transform("backgrounds/location_telescope_mia_day03a.jpg")
    pause .4
    Transform("backgrounds/location_telescope_mia_day03b.jpg")
    pause .4
    repeat

image mias 7_8:
    Transform("mias 7")
    pause M_mia.get("sex speed")
    Transform("mias 8")
    pause M_mia.get("sex speed")
    repeat

image mias 7_8_9_10_11:
    Transform("mias 7")
    pause M_mia.get("sex speed")
    Transform("mias 8")
    pause M_mia.get("sex speed")
    Transform("mias 9")
    pause M_mia.get("sex speed")
    Transform("mias 10")
    pause M_mia.get("sex speed")
    Transform("mias 11")
    pause M_mia.get("sex speed")
    repeat

image mias 7b_8b_9b_10b_11b:
    Transform("mias 7b")
    pause M_mia.get("sex speed")
    Transform("mias 8b")
    pause M_mia.get("sex speed")
    Transform("mias 9b")
    pause M_mia.get("sex speed")
    Transform("mias 10b")
    pause M_mia.get("sex speed")
    Transform("mias 11b")
    pause M_mia.get("sex speed")
    repeat

image mias 12_13:
    Transform("mias 12")
    pause .4
    Transform("mias 13")
    pause .2
    repeat

image mias 12b_13b:
    Transform("mias 12b")
    pause .4
    Transform("mias 13b")
    pause .2
    repeat


image helens 1_2 = Animation("characters/helen/char_helen_sex_02.png", .25, "characters/helen/char_helen_sex_01.png", .2)
image helens 4_4b = Animation("characters/helen/char_helen_sex_04.png", .4, "characters/helen/char_helen_sex_04b.png", .2)
image helens 6_7_8_9_10:
    Transform("characters/helen/char_helen_sex_06.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_07.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_08.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_09.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_10.png")
    pause M_helen.get("sex speed")
    repeat
image helens 11_11b = Animation("characters/helen/char_helen_sex_11.png", .2, "characters/helen/char_helen_sex_11b.png", 1)
image helens 15_16_17_18_19:
    Transform("characters/helen/char_helen_sex_15.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_16.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_17.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_18.png")
    pause M_helen.get("sex speed")
    Transform("characters/helen/char_helen_sex_19.png")
    pause M_helen.get("sex speed")
    repeat
image helens 23_24_25_26_27:
    Transform("helens 23")
    pause M_helen.get("sex speed")
    Transform("helens 24")
    pause M_helen.get("sex speed")
    Transform("helens 25")
    pause M_helen.get("sex speed")
    Transform("helens 26")
    pause M_helen.get("sex speed")
    Transform("helens 27")
    pause M_helen.get("sex speed")
    repeat
image h_corset 23_24_25_26_27:
    Transform("h_corset 23b")
    pause M_helen.get("sex speed")
    Transform("h_corset 24b")
    pause M_helen.get("sex speed")
    Transform("h_corset 25b")
    pause M_helen.get("sex speed")
    Transform("h_corset 26b")
    pause M_helen.get("sex speed")
    Transform("h_corset 27b")
    pause M_helen.get("sex speed")
    repeat


image rozs 1_2_3_4_5_6_7:
    Transform("characters/roz/char_roz_sex_01.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_02.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_03.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_04.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_05.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_06.png")
    pause M_roz.get("sex speed")
    Transform("characters/roz/char_roz_sex_07.png")
    pause M_roz.get("sex speed")
    repeat

image rozs 8_9 = Animation("characters/roz/char_roz_sex_08.png", .2, "characters/roz/char_roz_sex_09.png", 1)


image seasucc 8_8b_8c_8d_8e_8f_8g_8h_8i:
    Transform("seasucc 8")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8b")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8c")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8d")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8e")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8f")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8g")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8h")
    pause M_aqua.get('sex speed')
    Transform("seasucc 8i")
    pause M_aqua.get('sex speed')
    repeat



image teachers 1_2_3_4_5_6_7:
    Transform("teachers 1")
    pause M_bissette.get('sex speed')
    Transform("teachers 2")
    pause M_bissette.get('sex speed')
    Transform("teachers 3")
    pause M_bissette.get('sex speed')
    Transform("teachers 4")
    pause M_bissette.get('sex speed')
    Transform("teachers 5")
    pause M_bissette.get('sex speed')
    Transform("teachers 6")
    pause M_bissette.get('sex speed')
    Transform("teachers 7")
    pause M_bissette.get('sex speed')
    repeat

image teacher 39b_39c_39d:
    Transform("teacher 39b")
    pause 0.3
    Transform("teacher 39c")
    pause 0.3
    Transform("teacher 39d")
    pause 0.4
    repeat

image teachers 52_53:
    Transform("teachers 52")
    pause 0.2
    Transform("teachers 53")
    pause 0.4
    repeat

image teachers_chair 4_to_13:
    Transform("teachers_chair 4")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 5")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 6")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 7")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 8")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 9")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 10")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 11")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 12")
    pause M_bissette.get('sex speed')
    Transform("teachers_chair 13")
    pause M_bissette.get('sex speed')
    repeat

image teachers_chair 14_15:
    Transform("teachers_chair 14")
    pause .4
    Transform("teachers_chair 15")
    pause .4
    repeat


image okitap 7_8:
    "characters/okita/char_okita_52.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_53.png"
    pause M_okita.get('sex speed')
    repeat

image okita 72_73:
    "characters/okita/char_okita_72.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_73.png"
    pause M_okita.get('sex speed')
    repeat

image okitas 1_2_3_4_5_6_7_8_9_10:
    "characters/okita/char_okita_sex_01.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_02.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_03.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_04.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_05.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_06.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_07.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_08.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_09.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_10.png"
    pause M_okita.get('sex speed')
    repeat

image okitas 1b_2b_3b_4b_5b_6b_7b_8b_9b_10b:
    "characters/okita/char_okita_sex_01b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_02b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_03b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_04b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_05b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_06b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_07b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_08b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_09b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_10b.png"
    pause M_okita.get('sex speed')
    repeat

image okitas 11_12:
    "characters/okita/char_okita_sex_11.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_12.png"
    pause M_okita.get('sex speed')
    repeat

image okitas 11b_12b:
    "characters/okita/char_okita_sex_11b.png"
    pause M_okita.get('sex speed')
    "characters/okita/char_okita_sex_12b.png"
    pause M_okita.get('sex speed')
    repeat


image rossg 5_6:
    Image("characters/ross/char_ross_group_05.png", xoffset = -1)
    pause 0.65
    Image("characters/ross/char_ross_group_06.png", xoffset = -1)
    pause 0.65
    repeat

image rossg 7_8:
    Image("characters/ross/char_ross_group_07.png", xoffset = -1)
    pause 0.65
    Image("characters/ross/char_ross_group_08.png", xoffset = -1)
    pause 0.65
    repeat

image rossp 3_4_5_4:
    Image("characters/ross/char_ross_paint_03.png", xoffset = 5)
    pause 0.75
    "characters/ross/char_ross_paint_04.png"
    pause 0.75
    "characters/ross/char_ross_paint_05.png"
    pause 0.75
    "characters/ross/char_ross_paint_04.png"
    pause 0.75
    repeat

image rossp 11_12:
    "characters/ross/char_ross_paint_11.png"
    pause 0.75
    "characters/ross/char_ross_paint_12.png"
    pause 0.75
    repeat

image rosss 2_3_4_5_6_7_8_9_10_11:
    "characters/ross/char_ross_sex_02.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_03.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_04.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_05.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_06.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_07.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_08.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_09.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_10.png"
    pause M_ross.get('sex speed')
    "characters/ross/char_ross_sex_11.png"
    pause M_ross.get('sex speed')
    repeat

image rosss 12_13:
    "characters/ross/char_ross_sex_12.png"
    pause 0.25
    "characters/ross/char_ross_sex_13.png"
    pause 1
    repeat


image desk 31_32:
    Transform("desk 31")
    pause .8
    Transform("desk 32")
    pause .4
    repeat


image ang 22_23_24f = Animation(im.Flip("characters/angelica/char_angelica_22.png", horizontal=True), .3, im.Flip("characters/angelica/char_angelica_23.png", horizontal=True), .3, im.Flip("characters/angelica/char_angelica_24.png", horizontal=True), .3)


image rump_n_cunt 01_02_03_04:
    "characters/mayor/char_mayor_sex_01.png"
    pause 0.2
    "characters/mayor/char_mayor_sex_02.png"
    pause 0.25
    "characters/mayor/char_mayor_sex_03.png"
    pause 0.25
    "characters/mayor/char_mayor_sex_04.png"
    pause 0.2
    repeat


image dewitt_twerk 1b_to_10b:
    Transform("dewitt_twerk 1b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 2b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 3b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 4b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 5b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 6b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 7b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 8b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 9b")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 10b")
    pause M_dewitt.get('sex speed')
    repeat

image dewitt undies twerk 1c_to_10c:
    Transform("dewitt_twerk 1c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 2c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 3c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 4c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 5c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 6c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 7c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 8c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 9c")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 10c")
    pause M_dewitt.get('sex speed')
    repeat


image dewitt clothed twerk 1_to_10:
    Transform("dewitt_twerk 1")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 2")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 3")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 4")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 5")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 6")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 7")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 8")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 9")
    pause M_dewitt.get('sex speed')
    Transform("dewitt_twerk 10")
    pause M_dewitt.get('sex speed')
    repeat

image dewitts_bj 1_to_12:
    Transform("dewitts_bj 1")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 2")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 3")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 4")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 5")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 6")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 7")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 8")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 9")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 10")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 11")
    pause M_dewitt.get('sex speed')
    Transform("dewitts_bj 12")
    pause M_dewitt.get('sex speed')
    repeat

image dewitts 5_to_14:
    Transform("dewitts 5")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 6")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 7")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 8")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 9")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 10")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 11")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 12")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 13")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 14")
    pause M_dewitt.get('sex speed')
    repeat

image dewitts 15_16:
    Transform("dewitts 15")
    pause M_dewitt.get('sex speed')
    Transform("dewitts 16")
    pause M_dewitt.get('sex speed')
    repeat


image roxxy foot 6_7:
    Transform("roxxy foot 6")
    pause .75
    Transform("roxxy foot 7")
    pause .75
    repeat

image roxxy foot 8_9:
    Transform("roxxy foot 8")
    pause .6
    Transform("roxxy foot 9")
    pause .6
    repeat

image roxxy foot 8b_9b:
    Transform("roxxy foot 8b")
    pause .4
    Transform("roxxy foot 9b")
    pause .4
    repeat

image roxxy locker 8_9:
    Transform("roxxy locker 8")
    pause M_roxxy.get('sex speed')
    Transform("roxxy locker 9")
    pause M_roxxy.get('sex speed')
    repeat

image roxxy massage 4_5:
    Transform("roxxy massage 4")
    pause .4
    Transform("roxxy massage 5")
    pause .4
    repeat

image roxxy massage 6_7:
    Transform("roxxy massage 6")
    pause .4
    Transform("roxxy massage 7")
    pause .4
    repeat

image roxxy massage 8_9:
    Transform("roxxy massage 8")
    pause .4
    Transform("roxxy massage 9")
    pause .4
    repeat

image roxxy massage 9_10:
    Transform("roxxy massage 9")
    pause .4
    Transform("roxxy massage 10")
    pause .2
    repeat

image roxxys_locker 1_to_10:
    Transform("roxxys_locker 1")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 2")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 3")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 4")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 5")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 6")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 7")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 8")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 9")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_locker 10")
    pause M_roxxy.get('sex speed')
    repeat

image player locker 15_15b:
    Transform("player locker 15")
    pause .4
    Transform("player locker 15b")
    pause .4
    repeat

image roxxys_bed 1_to_8:
    Transform("roxxys_bed 1")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 2")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 3")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 4")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 5")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 6")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 7")
    pause M_roxxy.get('sex speed')
    Transform("roxxys_bed 8")
    pause M_roxxy.get('sex speed')
    repeat

image roxxys_bed 10_10b:
    Transform("roxxys_bed 10")
    pause .4
    Transform("roxxys_bed 10b")
    pause .4
    repeat

image roxxy 100d_100e:
    Transform("roxxy 100d")
    pause .4
    Transform("roxxy 100e")
    pause .4
    repeat

image roxxy 100b_100c:
    Transform("roxxy 100b")
    pause .4
    Transform("roxxy 100c")
    pause .4
    repeat


image crystals 1_to_8:
    Transform("crystals 1")
    pause M_crystal.get('sex speed')
    Transform("crystals 2")
    pause M_crystal.get('sex speed')
    Transform("crystals 3")
    pause M_crystal.get('sex speed')
    Transform("crystals 4")
    pause M_crystal.get('sex speed')
    Transform("crystals 5")
    pause M_crystal.get('sex speed')
    Transform("crystals 6")
    pause M_crystal.get('sex speed')
    Transform("crystals 7")
    pause M_crystal.get('sex speed')
    Transform("crystals 8")
    pause M_crystal.get('sex speed')
    repeat

image crystal 3b_3c:
    Transform("crystal 3b")
    pause .2
    Transform("crystal 3c")
    pause .2
    repeat

image crystals cum 2_2b:
    Transform("crystals cum 2")
    pause .4
    Transform("crystals cum 2b")
    pause .2
    repeat

image crystal 18_18b:
    Transform("crystal 18")
    pause .4
    Transform("crystal 18b")
    pause .4
    repeat

image crystal undress 11_11b:
    Transform("crystal undress 11")
    pause .4
    Transform("crystal undress 11b")
    pause .4
    repeat

image missy naked 9_10:
    Transform("missy naked 9")
    pause .4
    Transform("missy naked 10")
    pause .4
    repeat

image roxxys_beach 14_15:
    Transform("roxxys_beach 14")
    pause .4
    Transform("roxxys_beach 15")
    pause .2
    repeat

image missys_beach 14_15:
    Transform("missys_beach 14")
    pause .4
    Transform("missys_beach 15")
    pause .2
    repeat

image beccas_beach 14_15:
    Transform("beccas_beach 14")
    pause .4
    Transform("beccas_beach 15")
    pause .2
    repeat

image roxxys_solo 3_4:
    Transform("roxxys_solo 3")
    pause .4
    Transform("roxxys_solo 4")
    pause .2
    repeat

image missys_solo 3_4:
    Transform("missys_solo 3")
    pause .4
    Transform("missys_solo 4")
    pause .2
    repeat

image beccas_solo 3_4:
    Transform("beccas_solo 3")
    pause .4
    Transform("beccas_solo 4")
    pause .2
    repeat

image principal 22_23f:
    Transform("principal 22f")
    pause .4
    Transform("principal 23f")
    pause .4
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
