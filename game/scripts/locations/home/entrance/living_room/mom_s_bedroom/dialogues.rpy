label mom_bedroom_diane_refused_3way:
    scene expression "backgrounds/location_home_livingroom_night_blur.jpg"
    show player 14 with dissolve
    player_name "Если я пойду туда сейчас, они ни за что не позволят мне уйти."
    player_name "Я должен оставить их в покое."
    hide player with dissolve
    return

label mom_bedroom_diane_debbie_threeway_intro:
    scene expression "backgrounds/location_home_debbiesidebed_dialogue_sheet.jpg"
    show diane f_sit_bed_smirk b_nightgown_sit a_empty at Position (xpos=650,ypos=800)
    show debbie b_nightgown_bed a_empty f_bed_sit_sexy at flip
    show debbie at Position (xpos=-250)
    show playerf 5 at Position (xpos=200,ypos=850)
    show playerfa 1 zorder 3 at Position (xpos=180,ypos=640)
    with dissolve
    player_name "{b}[deb_name]{/b}, {b}Диана{/b}, что происходит?"
    show playerf 5b
    dia "..."
    show debbie f_bed_sit_sexy_talk
    deb "Мы с {b}Дианой{/b} поговорили и ну..."
    deb "... Я люблю тебя, милый."
    show debbie f_bed_sit_sexy
    show playerf 5
    player_name "Я тоже тебя люблю, {b}[deb_name]{/b}!"
    player_name "Но я не поним-"
    show playerf 5b
    show debbie f_bed_sit_sexy_talk
    deb "... И я люблю {b}Диану{/b}."
    deb "Она была моей лучшей подругой, сколько я себя помню."
    show debbie f_bed_sit_sexy
    show diane f_sit_bed_smirk_talk
    dia "Больше чем подруга, {b}[deb_name]{/b}."
    hide debbie
    show diane b_nightgown_sit_kissing_debbie f_empty at Position (xoffset=100)
    with dissolve
    show playerf 3 zorder 2
    player_name "!!!"
    pause
    show diane f_sit_bed_smirk b_nightgown_sit a_empty zorder 0 at Position (xpos=650,ypos=800)
    show debbie b_nightgown_bed a_empty f_bed_sit_sexy_talk zorder 1 at flip
    show debbie at Position (xpos=-250)
    with dissolve
    deb "Больше, чем друзья."
    deb "Мне надоело беспокоиться о нашей ситуации."
    deb "Здесь так много любви между нами тремя..."
    deb "... И я думаю, мы должны это отпраздновать."
    deb "Тебе так не кажется?"
    show debbie f_bed_sit_sexy
    show diane f_sit_bed_smirk_talk
    dia "Конечно!"
    show diane f_sit_bed_smirk
    show playerf 5
    player_name "Я не уверен что понял-"
    show playerf 5b
    pause
    show diane b_nightgown_undress f_sit_bed_undress_down_front with dissolve
    pause
    show diane b_nightgown_undress2 f_sit_bed_undress2_down_front with dissolve
    show playerf 3
    player_name "!!!"
    show diane b_naked_sit f_sit_bed_smirk with dissolve
    pause
    show playerf 5
    player_name "Ты эээ-"
    show playerf 5b
    show debbie b_bed_nightgown_undress with dissolve
    pause
    show debbie b_bed_undress2 f_bed_sit_undress2_sexy with dissolve
    show diane f_sit_bed_smirk_talk
    dia "Давай, жеребец."
    show debbie b_naked_bed f_bed_sit_sexy with dissolve
    dia "Неси сюда этот красивый член!"
    show diane f_sit_bed_smirk
    show playerf 5
    player_name "Хорошо..."
    hide debbie
    show diane b_naked_sit_kissing_debbie f_empty
    with dissolve
    pause
    hide playerf
    hide playerfa
    hide diane
    with dissolve
    scene expression "backgrounds/location_home_debbiebed_sex.jpg"
    show diane_debbie_sex_bed player_talk with dissolve
    player_name "О, боже!"
    player_name "Это действительно происходит?!"
    show diane_debbie_sex_bed diane_talk
    dia "Хехе!"
    show diane_debbie_sex_bed debbie_talk
    deb "Да милый, это действительно происходит."
    show diane_debbie_sex_bed player_talk
    player_name "Я не-"
    player_name "Я имею в виду, я не знаю, с чего начать..."
    show diane_debbie_sex_bed diane_talk
    dia "Ты должна быть первой, {b}[deb_name]{/b}!"
    dia "Это была твоя идея."
    show diane_debbie_sex_bed player_talk
    player_name "Хорошо, сначала {b}[deb_name]{/b}."
    show diane_debbie_sex_bed debbie_talk
    deb "Забирайся на меня, {b}Диана{/b}."
    show diane_debbie_sex_bed diane_talk
    dia "Хехе, хорошо."
    $ M_diane.set("change partner", True)
    show diane_debbie_sex_bed insert with dissolve
    player_name "Теперь, {b}[deb_name]{/b}!"
    show diane_debbie_sex_bed 7
    deb "О, милый!" with hpunch
    player_name "О, ааааа!"
    player_name "Ты такая мокрая!"
    dia "Она любит публику, не так ли {b}[deb_name]{/b}?!"
    deb "Да..."
    dia "Хехехе!"
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
    deb "Аааааа!"
    dia "Это так чертовски круто!"
    pause
    dia "Ммм, мне нравится смотреть, как тебя трахают, {b}[deb_name]{/b}!"
    deb "Ага, я знаю."
    player_name "Вы делали это раньше?!"
    dia "Со времен колледжа, нет."
    deb "... И никогда с кем-то у кого такой б-"
    deb "ОЛЬШООООЙ!!"
    deb "О, боже!"
    dia "Хахаха!"
    pause
    dia "Вау,не могу поверить, что он входит весь..."
    dia "У меня так не получается!"
    pause
    deb "Как приятно!"
    deb "Я щас кончу!"
    dia "О, ты слышал её {b}[firstname]{/b}!"
    dia "Поднажми!"
    $ M_diane.set('sex speed', 0.06)
    pause
    deb "Я кончаю-"
    deb "ДА!!"
    deb "ААААААААА!!!" with flash
    $ M_diane.set('sex speed', 0.2)
    show expression AnimatedImage("diane_debbie_sex_bed", [1,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
    dia "Ух ты, она так дрожит!"
    show diane_debbie_sex_bed insert with dissolve
    pause
    deb "Ахххх... Ахххх..."
    deb "О боже..."
    deb "Ладно, мне нужна секундочка."
    deb "Теперь черед {b}Дианы{/b}, {b}[firstname]{/b}!"
    dia "О, да, пожалуйста!"
    player_name "Хорошо."
    $ M_diane.set("change partner", False)
    show diane_debbie_sex_bed insert with dissolve
    player_name "Теперь, {b}Диана{/b}."
    show diane_debbie_sex_bed 7
    dia "О, черт!" with hpunch
    dia "Ммм, такой большой, {b}[firstname]{/b}!"
    deb "Ахх... Разве это не чудесно?"
    dia "Да-"
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
    dia "Ахх!!"
    pause
    deb "Ух ты, смотри, какие большие штуки!"
    dia "Ты о-"
    dia "О, черт!"
    dia "Ты говоришь о моих сиськах?!"
    deb "Хехе, да."
    deb "Они определенно больше моих."
    dia "Ну, да."
    dia "Они полны молока."
    deb "Точно."
    dia "Надеюсь, я не оболью тебя."
    deb "Я бы не возражала."
    pause
    dia "Ааа, он так глубоко!"
    dia "Я не могу этого вынести!"
    deb "Конечно, можешь, я же смогла."
    dia "Ааа, блядь!"
    pause
    deb "Давай милый, еби ее сильнее!"
    $ M_diane.set('sex speed', 0.06)
    dia "АААААХХХХ!!!"
    pause
    dia "Я близко!"
    player_name "Я тоже!"
    deb "Это замечательно, милый."
    deb "Ты можешь кончить с {b}Дианой{/b}."
    dia "Ты уверенна?!"
    dia "Он должен кончить с тобой."
    dia "Все это было твоей идеей!"
    deb "Пусть {b}[firstname]{/b} выбирает."
    return

label mom_bedroom_diane_risky_frisky_kinky:
    scene expression "backgrounds/location_home_livingroom_closeup_night.jpg"
    if M_diane.is_naked:
        $ M_diane.set("previous outfit", "naked")
    else:
        $ M_diane.set("previous outfit", "cow")
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "nightgown"
    show diane f_smirk_talk b_naked a_naked_sides
    show player 13f at Position (xpos=400)
    with dissolve
    dia "Куда-то собрался?"
    show diane f_smirk
    show player 22
    player_name "!!!"
    show player 29 at left with dissolve
    player_name "{b}Диана{/b}!!"
    player_name "Эээ, прости..."
    player_name "Я думал, ты спишь."
    show player 3
    pause
    show diane f_smirk_talk
    dia "Знаешь, это нелегко."
    show diane f_smirk
    show player 5 with dissolve
    player_name "Хмм?"
    show diane f_smirk_talk
    dia "Лежу здесь, одна, пока ты в одной комнате трахаешься с моей подругой."
    show diane f_smirk
    show player 10
    player_name "Я не..."
    player_name "То есть, мы не-"
    show player 5
    show diane f_laugh
    dia "Хаха, тебе не нужно лгать, {b}[firstname]{/b}."
    show diane f_smirk_talk
    dia "Я слышу, как вы там стонете."
    show diane f_smirk
    show player 3 with dissolve
    player_name "..."
    show diane f_normal_talk
    dia "Не пойми меня неправильно, но это действительно круто."
    show diane f_smirk
    show player 10 with dissolve
    player_name "Т-ты не думаешь, что это неправильно?"
    show player 5
    show diane f_laugh
    dia "Ну, учитывая то, что ты и я делаем, это сделало бы меня довольно большим лицемером, если бы я это сделала!"
    show diane f_smirk
    show player 14
    player_name "Хе, да."
    show player 13
    show diane f_smirk_talk
    dia "Я просто говорю, что по эту сторону двери становится одиноко..."
    show diane f_smirk
    show player 14
    player_name "Прости."
    show player 13
    show diane f_smirk_talk
    dia "Я подумала, может быть... Прежде чем ты войдешь туда... Мы могли бы..."
    show diane f_smirk
    player_name "..."
    show diane f_smirk_talk
    dia "... Немножко пошалить?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Правда?"
    show player 13 with dissolve
    show diane f_cheese
    dia "Мммммммм."
    show diane f_smirk_talk
    dia "Думаешь, справишься с нами обоими, жеребец?"
    show diane f_smirk
    show player 14
    player_name "Ну, я не знаю {b}Диана{/b}..."
    show player 13
    show diane f_smirk_talk
    dia "Да ладно, ну пожалуйста?"
    show diane f_smirk
    show player 13f at Position (xpos=300) with dissolve
    player_name "..."
    show player 14 at left with dissolve
    player_name "Хорошо, но мы должны сделать это быстро."
    show player 13
    show diane f_smirk_talk
    dia "Ой, не волнуйся..."
    show diane f_down_front b_nightgown_remove1 a_empty with dissolve
    pause
    show diane b_nightgown_remove2 with dissolve
    show player 426
    pause
    $ M_diane.is_naked = 1
    show diane b_naked a_naked_sides f_laugh
    dia "Я могу быть быстрой!"
    hide player
    show diane kiss_naked at Position (xoffset=-150)
    with dissolve
    pause
    show diane b_pull_mc_naked f_empty a_empty at flip with dissolve
    dia "А теперь давай снимем эти штанишки!"
    pause
    scene black with fade
    hide diane
    dia "Хехехе!"
    scene expression "backgrounds/location_home_debbiesidebed_dialogue.jpg"
    show debbie b_bed_nightgown_sleep f_empty a_empty
    with dissolve
    dia "Хехехе!"
    deb "!!!"
    deb "( Приятно, что {b}Диана{/b} здесь. )"
    deb "( Я не понимала, как сильно скучала по ее компании все эти годы... )"
    dia "Аааахх!"
    show debbie b_bed_nightgown_wake with dissolve
    deb "( Что это...? )"
    dia "Ммм."
    deb "( Это {b}Диана{/b} стонет! )"
    pause
    deb "( О боже мой... )"
    deb "( Она смотрит порно?! )"
    deb "( Я сказала ей вести себя хорошо, пока она здесь. )"
    pause
    show debbie b_bed_nightgown_sleep with dissolve
    pause
    dia "О, я так нуждалась в этом!"
    dia "Аааах!"
    deb "( Бедняжка... )"
    deb "( Думаю, ей так же одиноко, как и мне. )"
    pause
    deb "( Интересно, придет ли {b}[firstname]{/b} ко мне сегодня вечером? )"
    deb "( Ммм, надеюсь... )"
    pause
    dia "Ааах, я кончаю!"
    deb "( Она действительно собирается сделать это там! )"
    pause
    show debbie b_bed_nightgown_getup f_bed_getup_lip_bite with dissolve
    deb "( Я лучше пойду и скажу ей, чтобы она не шумела. )"
    scene expression "backgrounds/location_home_debbiesidebed_dialogue_sheet.jpg"
    hide debbie
    with dissolve
    deb "( Я не хочу, чтобы кто-то из детей проснулся и обнаружил ее мастурбирующей в нашей гостиной... )"
    pause
    scene expression "backgrounds/location_home_livingroom_couch_cutscene01.jpg"
    deb "!!!" with hpunch
    dia "Я кончаю!!"
    dia "О, да!!!"
    player_name "Шшш, ты разбудишь {b}[deb_name]{/b}..."
    deb "... {b}[firstname]{/b}?"
    scene expression "backgrounds/location_home_livingroom_couch_cutscene02.jpg"
    player_name "!!!" with hpunch
    player_name "{b}[deb_name]{/b}?!!"
    dia "О, черт!"
    scene expression "backgrounds/location_home_livingroom_night_blur.jpg"
    show debbie b_nightgown a_nightgown_hip f_angry_talk zorder 1 at flip
    show player 8cf zorder 1 at Position (xpos=700)
    show diane b_naked a_naked_shy f_sad zorder 2 at Position (xpos=600)
    deb "Что, черт побери, вы делаете?!"
    show debbie f_angry
    show player 5f with dissolve
    show diane f_sad_talk
    dia "Подожди секундочку, {b}[deb_name]{/b}..."
    dia "Это не так плохо, как кажется."
    show diane f_sad
    show debbie f_angry_talk
    deb "Не так плохо, как кажется?!"
    deb "Ты издеваешься?!"
    deb "Ты сказал мне, что не стоит беспокоиться о {b}Диане{/b}!"
    show debbie f_angry
    show diane f_sad_talk
    dia "Просто успокойся."
    show diane f_sad
    show debbie f_angry_talk
    deb "Я знала, что ты это сделаешь!"
    deb "Я так и знала!"
    show debbie f_angry
    show diane f_sad_talk
    dia "Пожалуйста, позволь мне объяснить..."
    show diane f_sad
    show debbie f_angry_talk
    deb "Я не должена была посылать его работать на тебя этим летом!"
    show debbie f_angry
    jen "Какого черта здесь происходит?!"
    show jenny f_normal_talk a_dressed_hips zorder 0 at Position (xpos=275) with dissolve
    jen "Почему вы кричите-"
    show jenny a_dressed_up_surprised f_surprised at flip
    show jenny at Position (xpos=700)
    with dissolve
    pause
    jen "О, боже мой..."
    jen "Вы двое трахались?!"
    show diane f_sad_talk
    dia "{b}[jen_name]{/b} не вмешивайся..."
    show diane f_sad
    show jenny f_happy_talk a_dressed_hips with dissolve
    jen "Ха-ха-ха, вы трахались друг с другом, не так ли?!"
    jen "Я так и знала!"
    show jenny at unflip
    show jenny at Position (xpos=275)
    with dissolve
    jen "Я же говорила, что-то происходит!"
    show jenny f_happy
    deb "..."
    show diane f_annoyed_talk
    dia "Заткнись, {b}[jen_name]{/b}."
    show diane f_annoyed
    show jenny f_upset_talk
    jen "Йии, они делали это на нашем диване!"
    jen "Я смотрю тут телевизор!"
    show jenny f_gross
    show debbie f_angry_talk
    deb "{b}[jen_name]{/b}, ЗАТКНИСЬ!"
    show debbie f_angry
    show jenny f_surprised
    jen "!!!"
    show jenny f_upset_talk a_dressed_crossed with dissolve
    jen "Блин, я не знаю, почему ты кричишь на меня..."
    show jenny f_normal_talk
    jen "Это не я трахалась с {b}[firstname]{/b} в гостиной!"
    show jenny f_grin
    show debbie f_angry_talk
    deb "Черт побери, {b}[jen_name]{/b}!"
    show debbie f_sad_talk
    deb "Просто..."
    deb "{b}*Вздыхая*{/b} Ты можешь просто вернуться наверх и позволить мне разобраться с этим, пожалуйста?"
    show debbie f_sad
    pause
    show jenny f_eyeroll
    jen "Пффф, хорошо."
    hide jenny with dissolve
    pause
    show diane f_sad_talk
    dia "Послушай {b}[deb_name]{/b}, Я и не пытаюсь..."
    show diane f_sad
    show debbie f_angry_talk
    deb "Помолчи!"
    deb "Не могу поверить, что ты это сделала, {b}Диана{/b}!"
    deb "Он всего лишь ребенок, и я должна защищать его от подобных вещей!"
    deb "Ты не можешь просто использовать его как какой-то инструмент, чтобы воплотить свои странные фантазии!"
    show debbie f_angry
    show diane f_annoyed_talk
    dia "Защитить его, да?!"
    dia "Это то, что ты говоришь себе, когда он трахает тебя до потери сознания?!"
    show diane f_annoyed
    show debbie f_angry_talk
    deb "!!!" with hpunch
    deb "Я не..."
    show debbie f_angry
    show diane f_annoyed_talk
    dia "Что?"
    dia "Думаешь, я не знаю?!"
    dia "Я в соседней комнате от тебя, а ты визжишь как Банши!"
    show diane f_annoyed
    show player 10f
    player_name "{b}Диана{/b}, не-"
    show player 11f
    show diane f_annoyed_talk
    dia "НЕТ!"
    dia "Если она хочет, чтобы все так и было, я не буду сдерживаться."
    show diane a_naked_point with dissolve
    dia "Ты лицемерка, {b}[deb_name]{/b}!"
    dia "Мы говорили о тебе и твоих желаниях все лето."
    dia "ТВОИ углубляющиеся отношения с {b}[firstname]{/b}, ТВОЕ желание идти дальше, и как удивительно ТЫ себя при этом чувствовала."
    dia "Я никогда не видел ТЕБЯ счастливее, чем в последние несколько недель..."
    dia "... И теперь ты собираешься разозлиться на меня из-за того, что я хочу только крошечный кусочек этого?"
    show diane f_annoyed a_naked_hips_both with dissolve
    show debbie f_angry_talk
    deb "Это другое дело!"
    show debbie f_angry
    show diane f_annoyed_talk
    dia "Чем же это отличается?!"
    show diane f_annoyed
    show debbie f_angry_talk
    deb "... Потому что я люблю его, ясно?!"
    show debbie f_angry
    show diane f_annoyed_talk
    dia "А ты думаешь, что я нет?!"
    show diane f_annoyed
    show debbie f_angry_talk
    deb "О боже..."
    show debbie f_angry
    show diane f_annoyed_talk
    dia "Как я могу не любить {b}[firstname]{/b}?!"
    dia "Он самый замечательный человек, которого я когда-либо встречала."
    show diane f_annoyed
    show debbie f_sad_talk a_nightgown_sides with dissolve
    deb "Что мы-"
    show debbie f_sad
    pause
    show debbie a_nightgown_hand_mouth f_sad_talk with dissolve
    deb "Что я наделала?!"
    hide debbie with dissolve
    show player 10f at center with dissolve
    player_name "{b}[deb_name]{/b}, подожди!"
    show player 5f
    show diane f_sad_talk a_naked_sides with dissolve
    dia "Пусть идет."
    show diane f_sad
    show player 10f
    player_name "Но-"
    show player 5 at left with dissolve
    show diane f_sad_talk
    dia "Иди спать, {b}[firstname]{/b}."
    show diane f_sad
    show player 10
    player_name "Ах?!"
    player_name "Я не-"
    show player 5
    show diane f_sad_talk b_nightgown_remove2 a_empty with dissolve
    dia "Я справлюсь с этим..."
    show diane b_nightgown_remove1 with dissolve
    dia "Просто иди наверх."
    hide diane with dissolve
    pause
    show player 24
    player_name "( О, боже... )"
    player_name "( Надеюсь, я не испортил все с {b}[deb_name]{/b}. )"
    hide player with dissolve
    pause
    scene expression "backgrounds/location_home_debbiesidebed_dialogue_sheet.jpg"
    show debbie b_bed_nightgown_straight_crying f_empty a_empty
    show diane f_sit_bed_shamed_talk_look_closed b_nightgown_sit a_empty at Position (ypos=800)
    with dissolve
    pause
    show diane f_sit_bed_shamed_talk_look
    dia "Не делай этого, {b}[deb_name]{/b}..."
    dia "Все будет хорошо."
    show diane f_sit_bed_shamed_talk_look_closed
    deb "Как ты можешь так говорить?!"
    deb "Ты хоть понимаешь, что мы делаем неправильно?"
    show diane f_sit_bed_shamed_talk_look
    dia "Ты не сделала ничего плохого, {b}[deb_name]{/b}."
    dia "Ты просто следуешь зову сердца."
    dia "Он действительно любит тебя, понимаешь?"
    show diane f_sit_bed_shamed_talk_look_closed
    deb "{b}*сопя*{/b} Я знаю..."
    show diane f_sit_bed_shamed_talk_look
    dia "Это я облажалась."
    show debbie b_bed_nightgown_straight f_bed_sit_sad
    show diane f_sit_bed_sad
    with dissolve
    pause
    show diane f_sit_bed_sad_talk
    dia "Я только..."
    show diane f_sit_bed_scream
    dia "Я никогда не хотела причинить тебе боль, {b}[deb_name]{/b}."
    dia "Это просто... {b}[firstname]{/b} великолепен..."
    dia "Такой очаровательный и милый, ответственный и готов помочь во всем..."
    dia "Я знаю, это прозвучит глупо, но с ним я снова чувствую себя подростком!"
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sad_talk
    deb "Это не глупо."
    deb "Он действует на меня точно так же."
    show debbie f_bed_sit_sad
    show diane f_sit_bed_shamed_talk_look
    dia "Но это не оправдание..."
    dia "У вас с {b}[firstname]{/b} все прекрасно..."
    dia "... А я просто ревнивая, одинокая сучка..."
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sad_talk
    deb "Не говори так."
    show debbie f_bed_sit_sad
    show diane f_sit_bed_sad_talk
    dia "Нет, так и есть."
    show diane f_sit_bed_sad
    pause
    show diane f_sit_bed_shamed_talk_look
    dia "Я просто была так одинока, так долго."
    show diane f_sit_bed_shamed_talk_look_closed
    show debbie f_bed_sit_sad_talk
    deb "Я знаю..."
    show debbie f_bed_sit_sad
    show diane f_sit_bed_shamed_talk_look
    dia "Хорошо, что кто-то снова обо мне заботится."
    show diane f_sit_bed_sad_talk
    dia "{b}*сопя*{/b} Пожалуйста, прости меня!"
    hide debbie
    show diane b_nightgown_sit_hug1 f_empty at Position (yoffset=-25)
    with dissolve
    deb "Шшш, все хорошо."
    deb "Я прощаю тебя."
    deb "Ни один мужчина не может встать между нами!"
    pause
    show debbie b_bed_nightgown_straight f_bed_sit_sorry a_empty
    show diane f_sit_bed_shamed_talk_smile b_nightgown_sit a_empty
    with dissolve
    dia "Спасибо."
    show diane f_sit_bed_sad_talk
    dia "Но, что нам теперь делать?"
    dia "Мне начать собирать вещи?"
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sorry_talk
    deb "Что?!"
    deb "Нет!"
    deb "Ты никуда не пойдешь!"
    show debbie f_bed_sit_sorry
    show diane f_sit_bed_sad_talk
    dia "Но-"
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sorry_talk
    deb "Ты права, {b}Диана{/b}."
    deb "Я - лицемер."
    show debbie f_bed_sit_sorry
    show diane f_sit_bed_sad_talk
    dia "Н-Нет, я не должна была так говорить-"
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sorry_talk
    deb "Все в порядке."
    show debbie f_bed_sit_sorry
    pause
    show debbie f_bed_sit_sorry_talk
    deb "Я знаю все об одиночестве, {b}Диана{/b}."
    deb "Как это может быть удручающе и что это может заставить вас делать."
    deb "Я не позволю тебе вернуться к этому."
    show debbie f_bed_sit_sorry
    show diane f_sit_bed_sad_talk
    dia "Ты уверена?"
    show diane f_sit_bed_sad
    show debbie f_bed_sit_sorry_talk
    deb "Да."
    deb "Твое место здесь, с нами."
    show debbie f_bed_sit_sorry
    show diane f_sit_bed_shamed_talk_smile
    dia "{b}*сопя*{/b} Я люблю тебя!"
    hide debbie
    show diane b_nightgown_sit_hug1 f_empty at Position (yoffset=-25)
    with dissolve
    deb "Я тоже люблю тебя."
    scene black with fade
    pause
    scene expression game.timer.image("bedroom{}")
    show player 24 with dissolve
    player_name "( Бедная {b}[deb_name]{/b}... )"
    player_name "{b}*вздыхая*{/b}"
    player_name "( Мне не следовало заниматься сексом с {b}Дианой{/b} в доме. )"
    player_name "( Я просто хотел, чтобы меня поймали. )"
    pause
    player_name "( Теперь {b}Диане{/b}, вероятно, придется съехать... )"
    deb "Милый?"
    show player 10f with dissolve
    player_name "{b}[deb_name]{/b}?!"
    show player 5f at right
    show debbie b_nightgown a_nightgown_sides f_sad at flip
    with dissolve
    show player 10f
    player_name "О боже, мне очень жаль!"
    player_name "Это я во всем виноват!"
    show player 5f
    show debbie f_sorry_talk
    deb "Шшш, успокойся."
    show debbie f_sorry
    show player 10f
    player_name "Пожалуста, не выгоняй {b}Диану{/b}!"
    show player 5f
    show debbie f_sorry_talk
    deb "Успокойся, милый."
    deb "{b}Диана{/b} никуда не уезжает."
    show debbie f_sorry
    show player 30f
    player_name "Фуу, хорошо."
    show player 10f
    player_name "Я так волновался, что ты прогон-"
    show player 5f
    show debbie f_sorry_talk
    deb "Шшшш."
    deb "Пойдем со мной, {b}[firstname]{/b}."
    deb "Я хочу тебе кое-что показать."
    show debbie f_sorry
    player_name "Хмм?"
    show debbie f_sorry_talk
    deb "Пойдем."
    hide debbie with dissolve
    pause
    show player 10f
    player_name "Хорошо..."
    hide player with dissolve
    return

label moms_bedroom_night:
    scene debbie_peek_sequence_1_night
    player_name "( {b}[deb_name]{/b} спит. )"
    player_name "( Мне не следует шуметь. )"
    return

label mom_spy:
    show debbie_peek_sequence 2_3 zorder 3
    player_name "ЧТО-!!"
    player_name "{b}[deb_name]{/b}?!?"
    player_name "( ...Она голая на своей кровати... )"
    player_name "( ...И возбуждает себя...стонет. )"
    deb "О... Да..."
    deb "Вот так, милый..."
    deb "Ммм..."
    deb "Да... {b}[firstname]{/b}..."
    deb "Не останавливайся!"
    player_name "( !!! )"
    deb "Ох бог!"
    deb "Я уже близко, милый!"
    deb "Трахни меня сильнее! Мне нужно кончить сильнее!"
    deb "Ahh!"

    deb "ДААА!!!" with hpunch
    $ player.go_to(L_home_livingroom)
    scene home_livingroom_c
    show player 107 at left
    with fade
    player_name "( Это... Я чувствую... )"
    player_name "( ... Это круто! )"
    show jenny 10 at right with dissolve
    jen "..."
    show jenny 9 at right
    jen "Что ты тут делаешь?!"
    show player 23 at left with hpunch
    show jenny 10 at right
    player_name "( !!! )"
    show player 29 at left
    player_name "Эрр, ничего! Я просто-"
    show player 11 at left
    show jenny 9 at right
    jen "Шпионишь за {b}[deb_name]{/b}?"
    show player 5 at left
    show jenny 10 at right
    jen "Что она меняет или что-то еще?"
    show player 10 at left
    player_name "... Нет."
    show player 5 at left
    show jenny 12 at right
    jen "Хорошо, что тогда?"
    show jenny 16 at left
    show player 22f at right
    with dissolve
    jen "Отойди!"
    jen "..."
    show player 5f at right
    jen "Ух ты!! Она действительно делает это там!"
    show jenny 17f at left
    jen "... И говорит твое имя!"
    show player 80f at right with dissolve
    jen "Что за черт?!"
    show player 81f at right with hpunch
    player_name "( !!! )"
    show jenny 12f at left
    show player 78f at right
    jen "Боже правый! У тебя там сырокопченая колбаса или что?"
    show player 80f at right
    jen "Надеюсь, ты не шпионишь за мной каждый раз, когда я плохо себя чувствую..."
    show player 82f at right
    jen "... потому что это было бы очень глупо, {b}[firstname]{/b}!"
    jen "Что ты можешь сказать в свое оправдание?"
    show player 83f at right
    show jenny 11f at left
    player_name "Пожалуйста, не говори {b}[deb_name]{/b} что я смотрел за ней..."
    show player 82f at right
    show jenny 19f at left
    jen "Хех, Ну... Может быть и не скажу..."
    show player 83f at right
    show jenny 18f at left
    player_name "Что ты имеешь в виду?"
    show jenny 19f at left
    show player 80f at right
    jen "Ты должен согласиться делать то, что я говорю, когда я говорю."
    show player 83f at right
    show jenny 18f at left
    player_name "А, как это?"
    show player 82f at right
    show jenny 19f at left
    jen "Пока не знаю. Тебе придется подождать и посмотреть..."
    show jenny 18f at left
    player_name "..."
    show jenny 12f at left
    jen "Похоже, она уже слишком близко... Наслаждайся остатком шоу, извращенец!"
    hide player
    hide jenny
    with dissolve
    $ renpy.end_replay()
    return

label moms_bedroom_mom_panties_masturbation_again:
    scene location_home_debbiebedroom_day_blur
    show player 1 with dissolve
    player_name "( Хорошо, Я внутри! )"
    player_name "( Теперь мне просто {b}нужно взять пару ее трусиков{/b} перед тем, как лечь к ней в постель. )"
    player_name "( О, как приятно... Я близко! )"
    hide player with dissolve
    return

label moms_bedroom_mom_sleepover_makeup:
    scene debbie_bedroom
    show player 264 at left with dissolve
    player_name "{b}*зевает*{/b}"
    show player 266 with dissolve
    player_name "Не могу поверить, что я спал в кровати {b}[deb_name]{/b} прошлой ночью..."
    show player 267
    pause
    show player 268
    player_name "Я лучше пойду, пока она не заметила мой утренний лес."
    show player 267
    deb "{b}*зевает*{/b}"
    player_name "( !!! )"
    show player 261 with dissolve
    pause
    show player 8f with dissolve
    pause
    show debbie 2 at right with dissolve
    show player 22 with dissolve
    deb "Я спала, как полено!"
    show debbie 1
    show player 21
    player_name "Да, я тоже..."
    show xtra 21 at left
    show player 5
    show debbie 3
    deb "Это был лучший сон за долгое время!"
    show debbie 2
    deb "Было приятно снова видеть кого-то здесь со мной."
    deb "Я не осознавала, как сильно скучаю по этому чувству."
    show debbie 1
    show player 21
    player_name "Да, это было приятное чувство."
    show player 5
    show debbie 3
    deb "Хех, ты такой симпатичный!"
    show debbie 2
    deb "Вам лучше подняться наверх до того, как {b}[jen_name]{/b} проснется."
    show debbie 1
    show player 21
    player_name "Да, я как раз собирался уходить."
    show player 5
    show debbie 2
    deb "Только не шуми, милый."
    deb "Мы же не хотим, чтобы она узнала, что у меня к тебе особое отношение!"
    show debbie 3
    deb "Хаха."
    show debbie 1
    show player 21
    player_name "Я буду очень осторожен."
    player_name "Не стесняйся приходить сюда снова спать, если тебе нужно."
    show player 13
    show debbie 2
    deb "Увидимся, милый."
    deb "... И помни. Ты всегда можешь спать здесь."
    hide xtra
    hide player
    hide debbie
    with dissolve
    return

label moms_bedroom_mom_dinner_outfit:
    scene debbie_bedroom with None
    show debbie 144 at left
    show player 11f at right
    with dissolve
    deb "Итак, что ты думаешь?"
    show debbie 145
    show player 14f
    player_name "Отлично выглядишь, {b}[deb_name]{/b}!"
    show debbie 146
    show player 13f
    deb "Правда? Как насчет с другой стороны?"
    show debbie 147 with fastdissolve
    show player 212f
    pause
    show player 21f
    player_name "Еще лучше!"
    show player 1f
    deb "Правда?"
    deb "Довольно туго..."
    show player 14f
    player_name "Ничего подобного! Твоя попка выглядит шикарно, {b}[deb_name]{/b}!"
    show player 212f
    pause
    show player 11f
    deb "О, Так ты пялишься на мою задницу, да?"
    show player 21f
    player_name "... Может быть... Чуть чуть."
    show player 1f
    show debbie 148 with fastdissolve
    deb "Хех, ну по крайней мере ты честен!"
    deb "Я рада что тебе нравится..."
    show debbie 149
    show player 29f
    player_name "Хехе, да..."
    hide debbie
    hide player
    with dissolve
    scene home_livingroom_b
    show player 35
    with dissolve
    player_name "Мне лучше не буду забывать, что сегодня на ужин {b}рыба{/b}. Что за рыбу она просила принести?"
    show player 34
    return

label moms_bedroom_mom_dinner_outfit_ask:
    scene debbie_bedroom
    show debbie 159 at left
    with fade
    pause
    show debbie 160 with fastdissolve
    pause
    show debbie 161b
    show player 14f at right with fastdissolve
    player_name "Привет {b}[deb_name]{/b}, что было-"
    show player 428f
    player_name "( !!! )" with hpunch
    show debbie 161
    deb "Милый! Я все еще переодеваюсь!"
    show player 29f
    show debbie 152
    with fastdissolve
    player_name "О, И... Извени!"
    show debbie 153
    show player 3f at Position (xoffset=-8)
    deb "Все нормально."
    deb "Ничего такого, чего бы ты раньше не видел."
    show debbie 152
    show player 29f
    player_name "Ухх... Ну, скажи как называется та {b}рыба{/b}? Которую любит {b}Диана{/b}?"
    show debbie 153
    show player 3f at Position (xoffset=-8)
    deb "{b}Морская форель{/b}, милый."
    show debbie 152
    show player 14f with dissolve
    player_name "Понял! Я обязательно ее принесу!"
    show debbie 154
    show player 11f
    deb "Подожди!"
    show debbie 155
    show player 10f
    player_name "Хмм?"
    show debbie 156 with fastdissolve
    show player 11f
    deb "Тебе нравится мое новое белье?"
    show debbie 157
    show player 429f
    player_name "Уххх..."
    show player 21f
    player_name "Оно сексуальное, {b}[deb_name]{/b}."
    show debbie 158
    show player 13f
    deb "Хе-хе, ты такой милый!"
    deb "Иди сюда!"
    show debbie 162 at Position(xpos=102)
    hide player
    with fastdissolve
    pause
    show debbie 163
    player_name "( !!! )" with hpunch
    show debbie 155 at left
    show player 21f at right
    with fastdissolve
    player_name "Спасибо, {b}[deb_name]{/b}!"
    player_name "Я лучше пойду."
    show debbie 154
    show player 13f
    deb "Да. Увидимся вечером, милый."
    scene home_livingroom_b
    show player 21
    with fade
    player_name "( {b}Вау{/b}! )"
    player_name "( {b}[deb_name]{/b} горяча! )"
    hide player with dissolve
    return

label moms_bedroom_mom_midnight_swim_after:
    scene home_livingroom_night_b
    show player 25f with dissolve
    player_name "Я должен оставить ее в покое..."
    show player 24f
    player_name "Она выглядела очень расстроенной..."
    hide player with dissolve
    return

label moms_bedroom_mom_is_set_lotion:
    scene debbie_peek_sequence_1
    player_name "( {b}[deb_name]{/b} нет в комнате. )"
    player_name "( Она наверно на кухне или еще где-то... )"
    return


label mom_drawer:
    python:
        for image in renpy.get_showing_tags():
            renpy.hide(image)
    call screen moms_drawer

label mom_drawer_panties:
    call expression game.dialog_select("mom_drawer_panties_dialogue")
    $ M_mom.trigger(T_mom_steal_panties)
    $ M_mom.set("panties taken", True)

    $ game.main()

label mom_drawer_panties_dialogue:
    scene debbie_bedroom
    show player 490
    player_name "( Ничего себе, они такие мягкие. )"
    show player 489
    pause
    show player 491
    pause
    show player 490
    player_name "( ... Хмм, Пахнет свежим постельным бельем. )"
    show player 489
    player_name "( ... )"
    show player 490
    player_name "( Бьюсь об заклад, ее кровать пахнет как она... )"
    player_name "( Может быть, я мог бы немного полежать на ней? )"
    player_name "( Она никогда не узнает. )"
    hide player
    with dissolve
    return

label mombedroom_mom_movie_afterthoughts_two:
    scene expression player.location.background_blur
    show player 5 with dissolve
    player_name "Наверное, мне не стоит настаивать на сегодняшнем вечере."
    player_name "Сегодня я буду спать в своей комнате."
    hide player with dissolve
    return

label mom_bed_panties_masturbation_first:
    player_name "( Эти трусики такие сексуальные... )"
    show location_debbiebed 2_3
    pause 5
    scene location_debbiebed04
    deb "( !!! )" with hpunch
    scene location_debbiebed05
    deb "Ой мой..."
    player_name "{b}[deb_name]{/b}?!"
    scene debbie_bedroom_closeup
    show debbie 16 at right
    show player 152 at left
    with dissolve
    deb "Прости, я не хотел-"
    show debbie 17
    show player 150
    deb "... Я имела в виду, я ожидала-"
    deb "Я..."
    show debbie 16
    deb "Я должна уйти!"
    show debbie 15
    show player 149
    player_name "Но-"
    show debbie 16
    show player 150
    deb "Нет, все хорошо... Только..."
    show debbie 17
    show player 154
    deb "... Извени меня!"
    player_name "..."
    scene home_livingroom_b
    show debbie 16
    with dissolve
    deb "( Я не могу поверить в то, что я только что видела! )"
    deb "( Он действительно это делал?! )"
    show debbie 20
    deb "( ... В МОЕЙ комнате?! )"
    show debbie 17
    deb "( Зачем ему делать это в моей комнате?! )"
    show debbie 16
    deb "( Конечно, он не может быть увлечен мною, не так ли?! )"
    show debbie 19
    deb "..."
    show debbie 18
    deb "( Наверное, это нормально... )"
    deb "( Он молодой человек и его гормоны заставляют его делать сумасшедшие вещи! )"
    deb "( Это должно быть именно так! Он просто запутался после всего, что случилось недавно... )"
    show debbie 17
    deb "( ... Мне нужно поговорить с ним об этом? )"
    show debbie 16
    deb "( Полагаю, я должна хотя бы попросить его сделать что-то подобное в его собственной комнате... И только не с моим  {b}нижним бельем{/b}! )"
    scene debbie_bedroom_closeup
    show player 151 at left
    with dissolve
    player_name "( Вот дерьмо. Это плохо! )"
    player_name "( Я {b}СИЛЬНО{/b} облажался... )"
    player_name "( Зачем я вообще это сделал! )"
    show player 153
    player_name "...Ух..."
    player_name "( Я глупец... )"
    show player 151
    player_name "( ... Между нами все было так хорошо, а теперь это все испортит! )"
    scene home_livingroom_b
    show debbie 13 at right with dissolve
    show player 5 at left with dissolve
    deb "Привет, милый!"
    show debbie 14
    show player 21
    player_name "..."
    show debbie 13
    show player 24
    deb "Слушай, я просто хочу, чтобы ты знал, что я не злюсь..."
    deb "Мастурбация-это совершенно нормально..."
    deb "Я знаю, что ты прошел через многое в последнее время; потерял своего {b}отца{/b} и переехал сюда к нам..."
    show player 5
    show debbie 14
    player_name "..."
    show debbie 13
    deb "Ты должно быть напряжен и более чем смущен..."
    deb "... Но тебе не следует делать это в моей комнате! ... И уж точно не с моим бельем!"
    show debbie 14
    show player 24
    player_name "Я знаю, прошу прощения. Я не знаю, что на меня нашло!"
    show debbie 13
    show player 5
    deb "Все хорошо, милый..."
    show player 11
    deb "Нам просто нужно найти тебе хорошую девушку или типа того..."
    deb "... {b}Может дать интернет порно{/b} попробовать до тех пор?"
    show debbie 14
    show player 21
    player_name "{b}[deb_name]{/b}!! Пожалуйста, прекрати, это все так неловко!"
    show debbie 13
    show player 13
    deb "... Прости. Я только пытаюсь помочь."
    deb "Не надо так смущаться. На самом деле, это не имеет большого значения... Все мастурбируют. Это совершенно нормально!"
    deb "Я все еще думаю, что ты отличный парень! Это просто тяжелое время для тебя..."
    show debbie 14
    show player 21
    player_name "Я не ребенок..."
    show debbie 13
    show player 13
    deb "Ты прав, мне очень жаль. Ты не ребенок. Просто пообещай больше не делать этого в моей комнате."
    show player 21
    show debbie 14
    player_name "Обещаю..."
    return

label mom_bed_panties_masturbation_repeat:
    player_name "( Они такие мягкие против моей кожи... )"
    show location_debbiebed 2_3
    pause 5
    scene location_debbiebed04
    deb "!!!" with hpunch
    scene location_debbiebed05
    deb "Опять!"
    player_name "{b}[deb_name]{/b}!!"
    scene debbie_bedroom_closeup
    show player 150 zorder 1 at left
    show debbie 16 at right with dissolve
    deb "Милый!"
    show debbie 25b at Position(xpos = 810, ypos = 768) with dissolve
    deb "Ты испортишь все мои красивые трусики!"
    show debbie 26 zorder 0 at Position(xpos = 610) with dissolve
    show player 151
    player_name "Прости, я просто..... Кажется, я не могу остановиться."
    show player 150
    show debbie 25
    deb "Все в порядке. Ты мужчина и у тебя есть желания..."
    deb "Хочешь, я покажу тебе еще одно маленькое шоу, чтобы ускорить процесс?"
    show debbie 26
    show player 154
    player_name "( !!! )"
    show player 149
    player_name "Правда?"
    player_name "Да!"
    show player 150 zorder 0
    show debbie 25b zorder 1 at Position(xpos = 810) with dissolve
    deb "Хорошо, милый."
    show debbie 19 at right with dissolve
    pause
    show debbie 21 with dissolve
    pause
    show debbie 22b with dissolve
    pause
    show debbie 23d with dissolve
    pause
    show debbie 23e
    deb "Как я выгляжу?"
    show debbie 23d
    show player 149
    player_name "Красивая..."
    show player 150
    show debbie 24b
    show player 155_156_156b_156 with dissolve
    pause
    pause
    player_name "О, {b}[deb_name]{/b}! Ты сексуальна!"
    show player 157_158_159 with flash
    show debbie 24c
    deb "( !!! ){p=1.5}{nw}"
    show player 161 with dissolve
    show debbie 24b
    deb "Это позволит сделать все здесь!"
    show debbie 23d
    show player 160
    player_name "Ты лучшая {b}[deb_name]{/b}..."
    show player 161
    show debbie 23e
    deb "Лучше бы я позволила тебе сделать это!"
    deb "А теперь иди сюда и обними меня."
    show debbie 23d
    hide player
    show debbie 28
    with dissolve
    deb "Люблю тебя."
    show debbie 29
    player_name "Я тоже тебя люблю."
    return

label mom_bed_panties_masturbation_pre:
    scene location_debbiebed01
    player_name "( Они такие мягкие против моей кожи... )"
    show location_debbiebed 2_3
    player_name "( Это как раз то, что мне было нужно... )"
    pause 5
    scene location_debbiebed04
    deb "( !!! )" with hpunch
    scene location_debbiebed05
    deb "Ой мой..."
    player_name "{b}[deb_name]{/b}!!"
    scene debbie_bedroom_closeup
    show player 152 at left with dissolve
    show debbie 16 at right with dissolve
    deb "{b}Опять{/b}??!"
    show debbie 20
    pause
    deb "..."
    show player 150 zorder 1
    show debbie 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
    pause 1
    show debbie 25 at Position(xpos =0.58, ypos = 768) with dissolve
    deb "Милый, мы уже разговаривали об этом."
    return

label mom_bed_panties_masturbation_sorry:
    show debbie 26
    show player 151
    player_name "Извени, {b}[deb_name]{/b}..."
    player_name "Я не знаю, что на меня нашло!"
    player_name "...Это больше не повторится, обещаю!"
    show debbie 27
    show player 152
    deb "О, милый..."
    show debbie 25
    deb "...Просто, пожалуйста, попробуй сделать это в другом месте."
    deb "Ты можешь сделать это для меня?"
    show debbie 26
    show player 151
    player_name "Да, мэм..."
    return

label mom_bed_panties_masturbation_cant_help_it:
    show debbie 26
    show player 151
    player_name "Извени, {b}[deb_name]{/b}... Но только {b}так приятно{/b}..."
    show debbie 27
    show player 152
    deb "Я знаю, милый... Но это неправильно, что ты делаешь это в моей постели... И вместе с моей одеждой!"
    show debbie 25
    deb "Почему ты не можешь найти другой способ, чтобы освободить свою... {b}Энергию{/b}?"
    deb "А что насчет девочек в твоей школе, они тебе не нравятся?"
    return

label mom_bed_panties_masturbation_im_trying:
    show debbie 26
    show player 151
    player_name "Я пытаюсь, {b}[deb_name]{/b}..."
    player_name "...Иногда нелегко знакомиться с девушками..."
    show player 152
    deb "..."
    show debbie 25
    deb "Ты пробовал приглашать их на свидания?"
    show debbie 26
    show player 149
    player_name "Что?"
    player_name "Я не могу просто... сделай это вот так..."
    show debbie 25
    show player 152
    deb "Ну, тебе придется приложить усилия, милый!"
    show debbie 26
    show player 151
    player_name "{b}*вздыхая*{/b} Я попробую, {b}[deb_name]{/b}."
    show debbie 25
    show player 152
    deb "Как долго будешь пытаться..."
    show debbie 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
    deb "Иди сюда..."
    hide player
    show debbie 28
    with dissolve
    player_name "..."
    deb "Мы пройдем через это..."
    show debbie 29
    player_name "Да..."
    return

label mom_bed_panties_masturbation_not_really:
    show debbie 26
    show player 151
    player_name "Не знаю..."
    player_name "...Наверное, я просто не нашел того, кто мне нравится."
    deb "..."
    show debbie 25
    show player 152
    deb "Как насчет соседской девушки?"
    show debbie 27
    show player 150
    deb "Как ее зовут?"
    show debbie 26
    show player 151
    player_name "{b}Мия{/b}..."
    show debbie 25
    show player 152
    deb "Да! Что насчет {b}Мии{/b}? Она симпатичная!"
    show debbie 26
    show player 151
    player_name "Да, наверное..."
    show debbie 25
    show player 152
    deb "Ну, тебе придется приложить усилия, милый!"
    show debbie 26
    show player 151
    player_name "Я попробую, {b}[deb_name]{/b}."
    show debbie 25
    show player 152
    deb "Как долго будешь пытаться..."
    show debbie 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
    deb "Иди сюда..."
    hide player
    show debbie 28
    with dissolve
    player_name "..."
    deb "Мы пройдем через это..."
    show debbie 29
    player_name "Да..."
    return

label mom_bed_panties_masturbation_i_like_you:
    show debbie 30
    show player 149
    if M_mom.is_state(S_mom_panties_masturbation_again):
        player_name "Ты мне нравишься..."
    else:
        player_name "Но я не могу выбросить тебя из головы..."
    show player 152
    deb "..."
    if M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 25
        show player 150
        deb "Это не так... Ты просто запутался."
        show debbie 30
        show player 149
        player_name "Нет, я действительно так думаю! {b}[deb_name]{/b}, я думаю только о тебе."
        show player 151
        player_name "Девочки моего возраста просто не могут соперничать с тобой!"
        show player 152
        deb "..."
        show debbie 25
        deb "Я..."
        show debbie 26
        deb "Это очень мило с твоей стороны, {b}[firstname]{/b} но мы не можем сделать это!"
        show player 150
        show debbie 25
        deb "{b}*вздыхая*{/b} Это все моя вина..."
        deb "... Все эти поцелуи..."
        show debbie 27
        deb "О боже, и еще в машине!"
        show debbie 27
        deb "..."
        deb "Я просто ужасный человек..."
        show debbie 26
        show player 149
        player_name "Ты не виновата, {b}[deb_name]{/b}..."
        show debbie 30
        show player 151
        player_name "Это я! Я просто не хочу никого другого!"
        player_name "... Может, со мной что-то не так..."
        show debbie 25b zorder 0 at Position(xpos=0.675, ypos= 1.0) with dissolve
        pause.4
        show debbie 15 at Position(xpos=0.8, ypos=1.0) with dissolve
        show player 150
        player_name "..."
        show debbie 17
        deb "{b}*вздыхая*{/b}"
        show debbie 18
        deb "Милый, с тобой все в порядке."
        deb "Ты просто запуталась... Вот и все."
    if not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 17 at Position(xpos=0.8, ypos=1.0) with dissolve
    deb "... Может, тебе просто нужно выкинуть это из головы?"
    show debbie 15
    if M_mom.is_state(S_mom_panties_masturbation_again):
        show player 149
        player_name "Что ты имеешь в виду?"
        show debbie 18
        deb "Я собираюсь сделать это, но {b}только один раз, хорошо{/b}?"
        show debbie 17
        deb "И ты должен пообещать мне, что будешь больше стараться разговаривать с девочками в школе!"
        show debbie 19
        show player 149
        player_name "Что ты собираешься делать?"
    show player 154
    show debbie 21
    window hide
    pause
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 22b
    else:
        show debbie 22
    window hide
    pause
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 23b with hpunch
    else:
        show debbie 23 with hpunch
    window hide
    pause
    player_name "( !!! )"
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 23e
    else:
        show debbie 31
    deb "Давай, {b}[firstname]{/b}. Закончи то, что начал..."
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 23b
    else:
        show debbie 23
    show player 149
    player_name "...Ты хочешь сказать, все в порядке?!!"
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 23e
    else:
        show debbie 31
    show player 150
    if M_mom.is_state(S_mom_panties_masturbation_again):
        deb "Все хорошо, {b}только один раз{/b}!"
    else:
        deb "Просто {b}сделай это{/b}. Все в порядке..."
        show debbie 23b
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show player 149
        player_name "{b}[deb_name]{/b}..."
        player_name "...Ты не носишь трусики?"
        show player 150
        show debbie 23c
        pause
        show debbie 23e
        deb "Что такое?"
        deb "О! Мои трусики?"
        deb "Наверное, я просто.....забыла!"
        show debbie 23d
        player_name "..."
        show debbie 23e
        deb "Это поможет?"
        show debbie 23d
        show player 149
        player_name "Мне нравится."
    else:

        show debbie 23
        show player 155 with dissolve
        player_name "Хорошо..."
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show player 155_156_156b_156
    else:
        show player medmo 155_156_156b
    pause
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 24d
    else:
        show debbie 24
    player_name "О, {b}[deb_name]{/b}..."
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 24b
    else:
        show debbie 24f
    deb "О мой..."
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 24d
    else:
        show debbie 24
    pause
    player_name "{b}[deb_name]{/b}!!! Я кончаю-"
    deb "..."
    show player 157 with flash
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 24c
    else:
        show debbie 24e
    player_name "Хнннн!!"
    pause .4
    show player 158
    pause .4
    show player 159
    pause 1
    show player 157
    pause .4
    show player 158
    pause .4
    show player 159
    pause 1
    show player 157
    pause .4
    show player 158
    pause .4
    show player 159
    pause .2
    show player 160 with dissolve
    player_name "Хух, хуууух, хууууух..."
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 24b
    else:
        show debbie 24f
    deb "Ничего себе, так много!"
    player_name "..."
    show player 161
    if M_mom.is_set("no panties") and not M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 22b
    else:
        show debbie 22
    window hide
    pause
    show debbie 21
    window hide
    pause
    if M_mom.is_state(S_mom_panties_masturbation_again):
        show debbie 16
        deb "Ты должен сделать усилие, чтобы встретить других девушек сейчас...{b}обещал{/b}?"
        show debbie 15
        show player 160
        player_name "Да..."
        show debbie 17
        show player 161
        deb "Это было просто {b}один раз{/b}... Чтобы избавиться от..."
    show debbie 17
    deb "Иди сюда..."
    hide player
    show debbie 28 with dissolve
    pause
    show debbie 29
    player_name "..."
    show debbie 28
    deb "Мы пройдем через это..."
    show debbie 29
    player_name "Да..."
    return

label mom_bed_sleep_together_pre_sex_available:
    show player 109 at right
    show debbie 83 at left
    with dissolve
    deb "..."
    show debbie 81
    deb "{b}[firstname]{/b}?"
    deb "Все в порядке?"
    show player 111
    player_name "Привет, {b}[deb_name]{/b}."
    show player 108
    player_name "У меня просто проблемы со сном..."
    player_name "Все, о чем я могу думать, это чтобы быть внутри тебя."
    show player 109
    show debbie 81
    deb "Это нормально."
    deb "У тебя слишком много энергии, которую нужно...сбросить."
    deb "Заходи, я точно знаю, что делать."
    show debbie 82
    show player 108
    player_name "Ты уверена?"
    show debbie 81
    show player 110
    deb "О, да... мне тоже это нужно."
    scene debbie_cuddle
    show debbies 77
    with fade

    player_name "Спасибо, {b}[deb_name]{/b}."
    show debbies_bed_overlay zorder 3 at Position(xpos=438)
    show debbies 79 zorder 2 at Position(xpos=365)
    with dissolve
    player_name "Я просто не мог уснуть... Я был так возбужден, думая о тебе..."
    player_name "...И я хотел снова быть в тебе."
    show debbies 80
    deb "Это совершенно нормально, милый."
    return

label mom_bed_sleep_together_pre:
    show player 109 at right
    show debbie 83 at left
    with dissolve
    deb "..."
    show debbie 81
    deb "{b}[firstname]{/b}?"
    deb "Все хорошо?"
    show debbie 82
    show player 111
    player_name "Да, {b}[deb_name]{/b}."
    show player 108
    player_name "Я не могу уснуть..."
    show player 109
    show debbie 81
    deb "О..."
    deb "Ничего страшного, милый."
    deb "Я понимаю, через что тебе приходится пройти..."
    show debbie 83
    deb "... И со всем, что случилось..."
    show debbie 82
    show player 108
    player_name "Можно я сегодня с тобой посплю?"
    show player 109
    show debbie 83
    deb "{b}*вздыхая*{/b}"
    show debbie 81
    show player 110
    deb "Да, все должно быть в порядке. Если ты проснешься рано и вернешься в свою комнату до того, как {b}[jen_name]{/b} проснется."
    show debbie 82
    show player 111
    player_name "Я смогу это сделать."
    scene debbie_cuddle
    with fade
    show debbies 77
    with fade
    player_name "Спасибо, {b}[deb_name]{/b}."
    show debbies_bed_overlay zorder 3 at Position(xpos=438)
    show debbies 79 zorder 2 at Position(xpos=365)
    with dissolve
    player_name "Мне нравится быть рядом с тобой..."
    player_name "... Здесь, в твоей кровати."
    show debbies 80
    deb "Я знаю, милый. Мне тоже нравится."
    show debbies 79
    player_name "Правда?"
    return

label mom_bed_sleep_together_cuddle_sex_available:
    show debbies 79
    player_name "Мы можем обняться?"
    show debbies 80
    deb "Конечно."
    show debbies 83 with dissolve
    player_name "Ты пахнешь очень приятно, {b}[deb_name]{/b}..."
    show debbies 84
    deb "Спасибо, милый."
    show debbies 81_82 with dissolve
    pause 4
    show debbies 81
    return

label mom_bed_sleep_together_cuddle:
    show debbies 79
    player_name "Мы можем обняться? Немного?"
    show debbies 80
    deb "Конечно, милый."
    show debbies 81_82 with dissolve
    deb "( !!! )"
    deb "( Он... ласкает мои бедра... )"
    deb "( Неужели это слишком? )"
    deb "( Это приятно, но я должна остановить его? )"
    show debbies 83
    player_name "Ты очень хорошо пахнешь, {b}[deb_name]{/b}..."
    show debbies 82
    deb "( ... )"
    show debbies 84
    deb "Спасибо, {b}[firstname]{/b}."
    show debbies 82
    return

label mom_bed_sleep_together_cuddle_keep_going:
    show debbies 81_82
    pause 4
    show debbies 81
    return

label mom_bed_sleep_together_kiss_sex_available:
    show debbies 83
    player_name "Мы можем поцеловаться?"
    show debbies 84
    deb "Тебе даже не нужно спрашивать, милый."
    deb "Иди сюда..."
    show debbies 85_86 with dissolve
    pause 4
    show debbies 81 with dissolve
    return

label mom_bed_sleep_together_kiss:
    show debbies 83
    player_name "{b}[deb_name]{/b}..."
    show debbies 84
    deb "Да?"
    show debbies 83
    player_name "Можно тебя поцеловать?"
    show debbies 84
    deb "Ты хочешь меня поцеловать?"
    deb "... Сейчас?"
    show debbies 83
    player_name "Да, пожалуйста."
    show debbies 81
    deb "..."
    show debbies 83
    player_name "Я не знаю, почему... Я просто очень хочу поцеловать тебя прямо сейчас."
    show debbies 84
    deb "... Это мило, {b}[firstname]{/b}."
    show debbies 83
    player_name "Значит, все в порядке?"
    player_name "... поцеловать тебя, совсем чуть-чуть?"
    show debbies 84
    deb "Я..."
    deb "Я полагаю, мы можем поцеловаться, но только немного!"
    show debbies 83
    player_name "Да."
    show debbies 85_86 with hpunch
    deb "( !!! )"
    deb "( Я чувствую его язык! )"
    deb "( Почему он так хорош в этом?! )"
    deb "Ммм..."
    deb "( О, мой... )"
    deb "( Его руки на моей груди... )"
    deb "Ммм..."
    deb "( ... Это меня так возбуждает! )"
    show debbies 83 with dissolve
    player_name "... Как это было?"
    show debbies 84
    deb "..."
    deb "{b}*глоток*{/b} Это было действительно хорошо, {b}[firstname]{/b}."
    show debbies 83
    player_name "Ты в порядке, {b}[deb_name]{/b}?"
    show debbies 84
    deb "... Да, все нормально, милый. Здесь просто очень жарко."
    show debbies 81 with dissolve
    return

label mom_bed_sleep_together_kiss_keep_going:
    show debbies 85_86 with dissolve
    pause 4
    show debbies 81 with dissolve
    return

label mom_bed_sleep_together_breastfeed_sex_available:
    show debbies 83
    player_name "Могу я... пососать грудь?"
    show debbies 87 with dissolve
    deb "Только... будь нежным."
    show debbies 88_89 at Position(xpos=329) with dissolve
    pause 4
    show debbies 89 at Position(xpos=327)
    return

label mom_bed_sleep_together_breastfeed:
    show debbies 83
    player_name "Могу ли я ... Поцеловать тебя сюда?"
    show debbies 84
    deb "Хмм?"
    show debbies 83
    player_name "В шею... И твою грудь..."
    show debbies 84
    deb "О, я не знаю..."
    show debbies 83
    player_name "Только немного, я обещаю."
    show debbies 84
    deb "..."
    show debbies 87 with dissolve
    deb "... нежнее."
    show debbies 88_89 at Position(xpos=329) with dissolve
    deb "( Ах! Он сосет мой сосок! )"
    deb "( ... Ох бог! )"
    deb "( Аххх...!! )" with hpunch
    deb "( Как приятно! )"
    deb "( ... )"
    deb "( Он так крепко держится! )"
    deb "( ... Хочется, чтобы он продолжал!! )"
    show debbies 88 at Position(xpos=329)
    return

label mom_bed_sleep_together_breastfeed_keep_going:
    show debbies 88_89 at Position(xpos=329) with dissolve
    pause 4
    show debbies 88 at Position(xpos=329)
    return

label mom_bed_sleep_together_rub_sex_available:
    show debbies 90 at Position(xpos=327) with dissolve
    deb "Да, милый."
    show debbies 91 with dissolve
    deb "Достань его и положи мне между ног..."
    show debbies 92 with dissolve
    pause
    show debbies 93_94 at Position(xpos=329) with dissolve
    deb "Ты такой красивый и сильный."
    deb "Я это чувствую..."
    deb "Продолжай двигать бедрами, милый."
    deb "Как приятно..."
    deb "Ахххх.."
    pause
    show debbies 93_94 at Position(xpos=329)
    pause 4
    show debbies 94 at Position(xpos=327)
    return

label mom_bed_sleep_together_rub:
    show debbies 90 at Position(xpos=327) with dissolve
    deb "( Что он... )"
    show debbies 91 with dissolve
    deb "..."
    show debbies 92 with dissolve
    deb "( Он только что его вытащил?! )"
    deb "( О мой бог! )"
    deb "( Я должна остановить его, но... )"
    deb "( ... )"
    show debbies 93_94 at Position(xpos=329) with hpunch
    deb "( Аххх...! )"
    deb "Мммм!"
    deb "( Я близко! )"
    deb "( Он собирается заставить меня кончить! )"
    deb "( ОХ БОГ!!! )"
    deb "( Я кончаю... )"
    deb "( Я КОНЧАЮ!! )"
    deb "ААААХХХХ!"
    show debbies 93 at Position(xpos=329)
    return

label mom_bed_sleep_together_rub_keep_going:
    show debbies 93_94 at Position(xpos=329) with dissolve
    pause 4
    show debbies 93 at Position(xpos=329)
    return

label mom_bed_sleep_together_stop:
    show debbies 79 with dissolve
    return

label mom_bed_sleep_together_fuck:
    show debbies 95 with dissolve
    if randomizer() <= 50:
        deb "Позволь мне помочь, милый..."
        deb "...А теперь вставь его в меня... поглубже."
        show debbies 96 with dissolve
        deb "Вот так... Да, милый..."
    else:
        deb "Я не могу терпеть все эти приставания."
        deb "Я хочу, чтобы ты закопал в меня этот большой член."
        deb "Не двигайся медленно..."
        deb "Ты достаточно меня дразнил."
        show debbies 96 with dissolve
        pause
    show debbies 98 at Position(xpos=327) with dissolve
    if randomizer() <= 50:
        deb "АХХ!"
    else:
        deb "Охх..."
    show screen xray_scr
    pause
    if anim_toggle:
        hide screen xray_scr
        show debbies 97_98 at Position(xpos=329)
        deb "О, да!{p=1}{nw}"
        deb "Да, милый...{p=1}{nw}"
        deb "Продолжай...{p=1}{nw}"
        deb "Глубже... Быстрее!!{p=1}{nw}"
    else:

        hide screen xray_scr
        show debbies 97 at Position(xpos=329)
        deb "О, да!"
        show debbies 98 at Position(xpos=327)
        deb "Да, милый..."
        show debbies 97 at Position(xpos=329)
        deb "Продолжай..."
        show debbies 98 at Position(xpos=327)
        deb "Глубже... Быстрее!!"
        show debbies 97 at Position(xpos=329)
    show debbies 97 at Position(xpos=329)
    return

label mom_bed_sleep_together_fuck_keep_going:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not renpy.showing("debbies 97_98"):
                show debbies 97_98 as debbies at Position(xpos = 329)
            pause 4
        else:

            $ pose_counter = 0
            $ pose_list = [97,98]
            $ xpos_list = [329,327]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at Position(xpos = xpos_list[pose_counter])
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
        $ animcounter += 1
    return

label mom_bed_sleep_together_fuck_cum:
    deb "ААХХХ!!!"
    show white zorder 4
    show debbies 99 at Position(xpos=327) with vpunch
    hide white with dissolve
    if randomizer() <= 50:
        deb "ДА малыш..."
        $ xray = False
        show debbies 98 at Position(xpos=327) with dissolve
        deb "{b}*пыхтит*{/b}"
        deb "Оставайся внутри меня еще немного..."
        deb "Мне нравится чувствовать твою сперму внутри себя."
        show debbies 100 with fade
        deb "Ее так много..."
        player_name "Это... плохо?"
        deb "Нет, милый. Это чудесно!"
    else:
        $ xray = False
        show debbies 98 at Position(xpos=327) with dissolve
        deb "Ох, малыш..."
        show debbies 100 with fade
        deb "Я не думала, что ты остановишься..."
        deb "Это было здорово..."

    show debbies 80 at Position(xpos=329) with fade
    if randomizer() <= 50:
        deb "Пожалуйста, останься со мной на ночь."
    else:
        deb "Ты сегодня здесь спишь?"
    show debbies 79
    return

label mom_bed_sleep_together_fuck_cum_stay:
    player_name "Хорошо, {b}[deb_name]{/b}."
    show debbies 80
    deb "Молодец."
    hide debbies
    hide debbies_bed_overlay
    scene black
    with fade
    return

label mom_bed_sleep_together_fuck_cum_leave:
    player_name "Я не могу. Может завтра."
    show debbies 80
    deb "Ох... Хорошо, не стесняйтесь."
    scene black
    hide debbies
    hide debbies_bed_overlay
    with fade
    pause
    scene debbie_bedroom_closeup
    show player 111 at right
    show debbie 82 at left
    with dissolve
    player_name "Спокойной ночи, {b}[deb_name]{/b}."
    show player 110
    show debbie 81
    deb "Спокойной ночи, милый."
    deb "Я люблю тебя."
    show debbie 82
    show player 111
    player_name "Я тоже люблю тебя, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    return

label mom_bed_sleep_together_sleep:
    show debbies 79 with dissolve
    player_name "Спокойной ночи, {b}[deb_name]{/b}..."
    show debbies 80 with dissolve
    deb "Спокойной ночи, {b}[firstname]{/b}..."
    hide debbies
    hide debbies_bed_overlay
    return

label mom_bed_night:
    scene debbie_bedroom_night
    show player 106 with dissolve
    player_name "( Мне пробраться в ее кровать? )"
    show player 34
    player_name "Хмм..."
    player_name "( Я не должен беспокоить ее, когда она спит... )"
    hide player with dissolve
    return

label mom_bed_day:
    scene debbie_bedroom
    show player 1 with dissolve
    player_name "( Мне было так хорошо, дрочить в ее постели. )"
    player_name "( ... Просто полностью быть окутаным ее запахом. )"
    show player 5
    player_name "( Но я пообещал ей, что больше так не буду. )"
    player_name "( Я должен изо всех сил стараться сдержать это обещание. )"
    hide player with dissolve
    return

label mom_sleeping:
    call expression game.dialog_select("mom_sleeping_pre")
    $ Sleep()
    if M_player.is_set("just wokeup"):
        call expression game.dialog_select("player_just_wokeup")
    jump expression game.dialog_select("mom_bedroom")

label mom_sleeping_pre:
    scene location_home_debbiebedroom_night_sleep with fade
    show unlock11 at truecenter with dissolve
    pause
    hide unlock11 with dissolve
    scene black with fade
    hide location_home_debbiebedroom_night_sleep with fade
    return

label mom_sleeping_sex_available_random:
    scene debbie_bedroom
    show player 7 with dissolve
    player_name "{b}*зевая*{/b}"
    show player 101 with dissolve
    player_name "Похоже {b}[deb_name]{/b} только что встала."
    show player 8 with dissolve
    pause
    show player 14 with dissolve
    player_name "Мне лучше улизнуть отсюда, так чтобы {b}[jen_name]{/b} не увидела меня."
    hide debbie
    hide player
    with dissolve
    return

label mom_sleeping_sex_available:
    scene debbie_bedroom_closeup2
    show debbie 83 at left
    show player 7 at right
    with dissolve
    player_name "{b}*зевая*{/b}"
    show player 8 with dissolve
    show debbie 81
    deb "Доброе утро, {b}[firstname]{/b}."
    show debbie 82
    show player 22 with hpunch
    player_name "!!!"
    show player 108 with dissolve
    player_name "Доброе утро! Я тебя разбудил?"
    show player 109
    show debbie 82
    deb "Нет, милый."
    deb "Я тоже наслаждался тобой рядом."
    show debbie 81
    show player 111
    player_name "Да, было приятно спать с тобой. В твоей кровати подушки мягче."
    show player 110
    show debbie 81
    deb "Точно."
    deb "Наверное, мне тоже лучше встать."
    deb "Еще раз спасибо, что спал со мной."
    show debbie 82
    show player 111
    player_name "Незачто. Люблю тебя, {b}[deb_name]{/b}."
    show player 110
    show debbie 81
    deb "Я тоже тебя люблю, милый."
    hide debbie
    hide player
    with dissolve
    return

label mom_room_laundry_dialogue:
    scene debbie_bedroom
    show player 276 with dissolve
    player_name "Я должен отнести это в {b}подвал{/b}."
    hide player with dissolve
    return

label mom_room_laundry:
    call expression game.dialog_select("mom_room_laundry_dialogue")
    $ M_mom.trigger(T_mom_got_laundry)
    $ game.main()

label mom_sex_replay:
    $ M_mom.set("sex available", True)
    scene debbie_bedroom_closeup2
    $ rnd = randomizer()
    if rnd < 50:
        jump expression game.dialog_select("sex_mom_bed_intro_3")

    elif rnd < 75:
        jump expression game.dialog_select("sex_mom_bed_intro_2")
    jump expression game.dialog_select("sex_mom_bed_intro_1")

label mom_sex:
    $ M_mom.set("sex speed", .4)
    $ M_mom.set("change angle", False)
    $ mom_sex_position = "missionary"
    $ cum = False
    $ anim_toggle = True
    $ animated = False
    $ xray = False
    $ first_time_cowgirl = True
    $ first_time_suck_tits = True
    call expression game.dialog_select("mom_sex_pre")
    jump expression game.dialog_select("mom_sex_loop")

label mom_sex_pre:
    show debbies 106 at left
    with fade
    deb "Начинай медленно и аккуратно, милый."
    show debbies 103 with dissolve
    pause
    show debbies 104 with dissolve
    deb "Ахх..."
    show debbies 104 at left
    return

label mom_sex_loop_pre:
    if mom_sex_position in ["missionary", "suck tits"]:
        if not renpy.showing("debbie_bedroom_closeup_sex"):
            scene debbie_bedroom_closeup_sex

        if mom_sex_position == "missionary":
            show debbies 106 at left

        if mom_sex_position == "suck tits":
            if first_time_suck_tits and randomizer() <= 50:
                call expression game.dialog_select("mom_sex_loop_pre_suck_tits")
                $ first_time_suck_tits = False

    elif mom_sex_position == "cowgirl":
        if not renpy.showing("bedroom_sex_05") and M_mom.is_set("change angle"):
            scene bedroom_sex_05
            show debbies 170

        elif not renpy.showing("debbie_bedroom_closeup_sex"):
            scene debbie_bedroom_closeup_sex
            show debbies 62 at left
        else:

            show debbies 62 at left

        if first_time_cowgirl:
            call expression game.dialog_select("mom_sex_loop_pre_cowgirl")
            $ first_time_cowgirl = False
    jump expression game.dialog_select("mom_sex_loop")

label mom_sex_loop_pre_suck_tits:
    show debbies 67 at left with dissolve
    player_name "Могу я поцеловать твою грудь?"
    show debbies 68
    deb "Быть нежными."
    deb "Они чувствительные."
    return

label mom_sex_loop_pre_cowgirl:
    with dissolve
    if randomizer() <= 50:
        deb "Ляг на спину и дай мне повернуться."
    else:
        deb "Тебе просто нравится смотреть, как мои сиськи подпрыгивают, не так ли, мой непослушный мальчик?"
    return

label mom_sex_loop:
    show screen xray_scr
    pause
    hide screen xray_scr
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if mom_sex_position == "missionary":
                    show expression AnimatedImage("debbies", [103,104,105,104], M_mom) as debbies at left

                elif mom_sex_position == "suck tits":
                    if not renpy.showing("debbies 68_67"):
                        show debbies 68_67 as debbies at left

                elif mom_sex_position == "cowgirl":
                    if M_mom.is_set("change angle"):
                        show expression AnimatedImage("debbies", [170,171,172,173,174,175,176,177], M_mom) as debbies
                    else:

                        show expression AnimatedImage("debbies", [65,66,64], M_mom) as debbies at left
                $ animated = True
            pause 5
            call expression game.dialog_select("debbie_bed_hscene_dialog")
            pause 3
        else:

            $ M_mom.set("sex poses", [])
            $ pose_counter = 0
            if mom_sex_position == "missionary":
                $ pose_list = [103,104,105,104]

            elif mom_sex_position == "suck tits":
                $ pose_list = [68,67]

            elif mom_sex_position == "cowgirl":
                if M_mom.is_set("change angle"):
                    $ pose_list = [170,171,172,173,174,175,176,177]
                else:

                    $ pose_list = [65,66,64]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies at left
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("debbie_bed_hscene_dialog")
        $ animcounter += 1
    call screen mom_sex_options

label debbie_bed_hscene_dialog:
    if mom_sex_position == "missionary":
        if randomizer() <= 33:
            if animcounter == 1:
                deb "Аххххх!!!{p=1}{nw}"

            elif animcounter == 3:
                deb "О, милый!!!{p=1}{nw}"
                player_name "Уххх...{p=1}{nw}"

        elif randomizer() <= 66:
            if animcounter == 1:
                deb "О...{p=1}{nw}"

            elif animcounter == 2:
                deb "Дай мне это, милый.{p=2}{nw}"
                player_name "Вот так?{p=2}{nw}"
                deb "Даааааа....{p=1}{nw}"

            elif animcounter == 3:
                deb "Ахх!{p=1}{nw}"
        else:

            if animcounter == 2:
                deb "Быстрее, милый!{p=2}{nw}"
                deb "Я почти!{p=2}{nw}"
                player_name "О, {b}[deb_name]{/b}! Я чувствую, как ты сжимаешь его!{p=2}{nw}"

            elif animcounter == 3:
                deb "Ахх!!!{p=1}{nw}"

    elif mom_sex_position == "suck tits":
        if randomizer() <= 33:
            if animcounter == 2:
                deb "Да, милый....{p=1}{nw}"
                deb "Продолжай сосать их.{p=1}{nw}"

        elif randomizer() <= 66:
            if animcounter == 1:
                deb "Мммм...{p=1}{nw}"

            elif animcounter == 2:
                deb "О!{p=1}{nw}"
                deb "Аккуратно, милый!{p=1}{nw}"
        else:
            if animcounter == 3:
                deb "О, малыш...{p=1}{nw}"
                deb "Тебе нравится сосать мои сиськи?{p=2}{nw}"
                player_name "Ммммммм..{p=1}{nw}"

    elif mom_sex_position == "cowgirl":
        if randomizer() <= 50:
            if animcounter == 1:
                deb "Ахххх!!!{p=1}{nw}"

            elif animcounter == 3:
                deb "О, милый!!!{p=1}{nw}"
                player_name "Ухххх...{p=1}{nw}"
        else:

            if animcounter == 2:
                deb "Тебе нравится так?{p=2}{nw}"
                player_name "Да...{p=1}{nw}"
                deb "Мне тоже...{p=2}{nw}"
                deb "Я чувствую тебя глубоко внутри меня.{p=2}{nw}"

            elif animcounter == 3:
                deb "Аххх!!!{p=1}{nw}"
                deb "О, малыш...{p=1}{nw}"
    return

label mom_sex_cum_inside:
    if mom_sex_position == "missionary":
        if randomizer() <= 50:
            call expression game.dialog_select("mom_sex_cum_inside_missionary_pre_random")
            $ cum = True
            call expression game.dialog_select("mom_sex_cum_inside_missionary_after_cum_random")
            $ xray = False
            call expression game.dialog_select("mom_sex_cum_inside_missionary_after_xray_random")
        else:

            call expression game.dialog_select("mom_sex_cum_inside_missionary_pre")
            $ cum = True
            call expression game.dialog_select("mom_sex_cum_inside_missionary_after_cum")
            $ xray = False
            call expression game.dialog_select("mom_sex_cum_inside_missionary_after_xray")
    else:

        if not renpy.showing("debbie_bedroom_closeup_sex"):
            scene debbie_bedroom_closeup_sex

        call expression game.dialog_select("mom_sex_cum_inside_cowgirl_pre")
        $ cum = True
        call expression game.dialog_select("mom_sex_cum_inside_cowgirl_after_cum")
    jump expression game.dialog_select("mom_bed_after_sex")

label mom_sex_cum_inside_missionary_pre_random:
    show debbies 103 at left
    player_name "{b}[deb_name]{/b}, я кончаю..."
    deb "Давай, милый!"
    show debbies 105 with hpunch
    player_name "{b}[deb_name]{/b}!!!"
    show white with dissolve
    return

label mom_sex_cum_inside_missionary_pre:
    show debbies 105 at left with hpunch
    player_name "О, {b}[deb_name]{/b}!"
    show white with dissolve
    return

label mom_sex_cum_inside_missionary_after_cum_random:
    hide white with dissolve
    deb "Аххх!!!"
    deb "Да!"
    deb "Оставаться внутри меня..."
    show debbies 106 with fade
    return

label mom_sex_cum_inside_missionary_after_cum:
    hide white with dissolve
    deb "Ахх!!!"
    deb "О, милый..."
    deb "Это было напряженно..."
    player_name "Это было приятно."
    deb "Да..."
    deb "О, милый. Ты молодец."
    show debbies 106 with fade
    return

label mom_sex_cum_inside_missionary_after_xray_random:
    deb "Так много спермы..."
    return

label mom_sex_cum_inside_missionary_after_xray:
    deb "Ты все еще такой напряженный..."
    deb "Держу пари, ты можешь еще!"
    return

label mom_sex_cum_inside_cowgirl_pre:
    scene debbie_bedroom_closeup_sex
    show debbies 69 at left with vpunch
    player_name "{b}[deb_name]{/b}!!!"
    deb "Ахх!!!"
    show white with dissolve
    return

label mom_sex_cum_inside_cowgirl_after_cum:
    hide white with dissolve
    pause
    deb "О..."
    show debbies 70 with dissolve
    deb "Ты должен предупредить меня, когда собираешься это сделать, милый."
    player_name "Извени, {b}[deb_name]{/b}."
    player_name "Я ничего не мог с собой поделать..."
    player_name "это было слишком хорошо..."
    deb "Все нормально. Давай приведем тебя в порядок..."
    return

label mom_sex_cum_outside:
    if mom_sex_position == "missionary":
        if randomizer() <= 50:
            call expression game.dialog_select("mom_sex_cum_outside_missionary_pre_random")
            $ xray = False
            call expression game.dialog_select("mom_sex_cum_outside_missionary_after_xray_random")
        else:

            call expression game.dialog_select("mom_sex_cum_outside_missionary_pre")
            $ xray = False
            call expression game.dialog_select("mom_sex_cum_outside_missionary_after_xray")
    else:

        if not renpy.showing("debbie_bedroom_closeup_sex"):
            scene debbie_bedroom_closeup_sex

        if randomizer() <= 50:
            call expression game.dialog_select("mom_sex_cum_outside_cowgirl_random")
        else:

            call expression game.dialog_select("mom_sex_cum_outside_cowgirl")
    jump expression game.dialog_select("mom_bed_after_sex")

label mom_sex_cum_outside_missionary_pre_random:
    show debbies 103
    player_name "{b}[deb_name]{/b}, Я кончаю..."
    deb "Давай, милый!"
    return

label mom_sex_cum_outside_missionary_pre:
    show debbies 103
    player_name "{b}[deb_name]{/b}, могу я кончить на тебя сверху?"
    deb "Да, милый!"
    return

label mom_sex_cum_outside_missionary_after_xray_random:
    show debbies 107 with dissolve
    show white with dissolve
    show playersex 70 at Position(xpos=568, ypos=348)
    hide white with dissolve
    pause
    show playersex 71 at Position(xpos=612, ypos=450)
    pause
    hide playersex
    show debbies 108
    deb "О!!!"
    deb "Вау!"
    deb "Хех, посмотри на меня! Я вся забрызгана!"
    player_name "Да... Наверное, я немного увлеклась."
    return

label mom_sex_cum_outside_missionary_after_xray:
    show debbies 107 with dissolve
    show white with dissolve
    show playersex 70 at Position(xpos=568, ypos=348)
    hide white with dissolve
    pause
    show playersex 71 at Position(xpos=612, ypos=450)
    pause
    hide playersex
    show debbies 108
    deb "О!"
    deb "Я не думала, что это будет так много!"
    deb "Мне придется поменять простыни!"
    player_name "Извени..."
    deb "Не стоит. Все замечательно!"
    return

label mom_sex_cum_outside_cowgirl_random:
    show debbies 64 at left
    player_name "{b}[deb_name]{/b}, я кончаю..."
    show debbies 109 with dissolve
    show white with dissolve
    show playersex 72 at Position(xpos=478, ypos=418)
    hide white with dissolve
    pause
    show playersex 73 at Position(xpos=524, ypos=478) with dissolve
    deb "Спасибо за предупреждение, милый."
    deb "Давайте приведем себя в порядок..."
    return

label mom_sex_cum_outside_cowgirl:
    show debbies 64 at left
    player_name "{b}[deb_name]{/b}! Я..."
    show debbies 109 with dissolve
    show white with dissolve
    show playersex 72 at Position(xpos=478, ypos=418)
    hide white with dissolve
    pause
    show playersex 73 at Position(xpos=524, ypos=478) with dissolve
    deb "!!!"
    player_name "Вау, как много..."
    deb "Ха ха ха..."
    deb "Она везде!."
    deb "Я вся пропитана!"
    return

label mom_bed_after_sex:
    call expression game.dialog_select("mom_bed_after_sex_pre")
    if randomizer() <= M_mom.get("mom concerned"):
        if M_mom.get("mom concerned") > 0:
            $ M_mom.set("mom concerned", M_mom.get("mom concerned") - 20)

        if M_mom.get("mom concerned") < 0:
            $ M_mom.set("mom concerned", 0)

        call expression game.dialog_select("mom_bed_after_sex_random")
    call expression game.dialog_select("mom_bed_after_sex_after")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["11_unlocked"] = True

    $ game.timer.tick()
    $ mom_dialogue_advance = True
    $ game.main()

label mom_bed_after_sex_pre:
    scene debbie_bedroom
    show player 227 at Position(xpos=200)
    show debbie 73 at Position(xpos=650)
    with fade
    deb "Милый..."
    return

label mom_bed_after_sex_random:
    deb "Я хочу, чтобы ты сказал мне, если ты больше не хочешь этого делать, хорошо?"
    show player 228
    show debbie 76
    player_name "Нет, все хорошо, {b}[deb_name]{/b}."
    player_name "Мне всегда хочется сделать это с тобой."
    show player 227
    show debbie 77
    deb "Правда?"
    show player 228
    player_name "Да, это все, о чем я думаю, когда вижу тебя..."
    show player 227
    show debbie 75
    deb "Ты всегда такой милый..."
    return

label mom_bed_after_sex_after:
    deb "Поцелуй меня."
    hide player
    show debbie 80
    with dissolve
    pause
    show debbie 79 with dissolve
    pause
    show debbie 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show debbie 78
    with dissolve
    player_name "Я люблю тебя, {b}[deb_name]{/b}!"
    show player 227
    show debbie 75
    deb "Я тоже тебя люблю, милый..."
    hide debbie
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
