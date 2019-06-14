label mrsjroom_mrsj_private_yoga_intro:
    show player 435 at left
    show mrsj 53 at Position(xpos=734,ypos=650)
    player_name "Могу ли я увидеть ваши частные уроки йоги?"
    show mrsj 54
    show player 434
    mrsjo "Ну, у меня есть несколько специальных позиций, которые я всегда хотела попробовать."
    mrsjo "У меня никогда не было того, с кем можно было бы их сделать... только если ты не хочешь мне помочь?"
    show mrsj 53
    show player 435
    player_name "Конечно, {b}Миссис Джонсон{/b}, Я с удовольствием помогу!"
    show mrsj 54
    show player 434
    mrsjo "Ты думаешь, что у тебя достаточно энергии, чтобы смочь?"
    show mrsj 53
    show player 435
    player_name "Я могу попробовать!"
    show mrsj 54
    show player 434
    mrsjo "Окей. Начни со снятия одежды..."
    show mrsj 53
    show player 8 with fastdissolve
    pause
    show player 8b with fastdissolve
    pause
    show player 431b with fastdissolve
    pause
    show player 431 with vpunch
    show mrsj 54
    mrsjo "Вау!"
    mrsjo "Я не думаю, что я когда-либо видела что-то такое возбужденное в йоге!"
    mrsjo "Почему бы тебе не лечь на кровать и не устроиться поудобнее со мной?"
    scene erik_upstairs_night_c2
    show mrsjsex 33 at topright
    with fade
    mrsjo "Тебе нравится этот вид из окна?"
    show mrsjsex 34
    player_name "Это действительно замечательно..."
    show mrsjsex 33
    mrsjo "Держи глаза на мне, я хочу показать тебе аккуратный маленький трюк."
    show mrsjsex 35 with fastdissolve
    pause 0.05
    show mrsjsex 36 at Position(yoffset=70) with fastdissolve
    pause 0.2
    show mrsjsex 36_37
    player_name "Уоу..."
    pause
    return

label mrsjroom_mrsj_private_yoga_pos1:
    show mrsjsex 37 at Position(yoffset=60)
    pause 0.2
    show mrsjsex 38 with fastdissolve
    pause 0.2
    show mrsjsex 39 at Position(yoffset=87) with fastdissolve
    mrsjo "Давай перейдем к моей следующей позе..."
    mrsjo "... что-то, что поможет мне растянуться?"
    scene erik_upstairs_night_c3
    show mrsjsex 40 at Position(xpos=580,ypos=710)
    with fade
    mrsjo "Эта позиция большое удовольствие..."
    mrsjo "... ты просто подожди, позволь мне поработать..."
    show mrsjsex 40
    mrsjo "Ты такой БОЛЬШОЙ, {b}[firstname]{/b}..."
    show mrsjsex 41 with fastdissolve
    pause 0.5
    show mrsjsex 42 at Position(xoffset=-14) with fastdissolve
    pause 0.5
    show mrsjsex 43 at Position(xoffset=-20) with fastdissolve
    pause 0.5
    show mrsjsex 44 at Position(xoffset=-30) with fastdissolve
    mrsjo "ААА... настолько глубокий..."
    player_name "{b}Миссис Джонсон{/b}, тебе так хорошо..."
    mrsjo "Сейчас я начну двигаться, постараюсь продержаться дольше нескольких минут, {b}[firstname]{/b}."
    show mrsjsex 45 at Position(xoffset=-23)
    pause 0.2
    show mrsjsex 46 at Position(xoffset=-19)
    pause 0.2
    show mrsjsex 42_43_44_45_46
    pause
    mrsjo "Да!! продолжай..."
    pause
    return

label mrsjroom_mrsj_private_yoga_pos2:
    hide screen erimom_private_pos2_sex_options
    show mrsjsex 42_43_44_45_46
    mrsjo "Продолжай, {b}[firstname]{/b}..."
    mrsjo "... кончи в меня!"
    player_name "Ты уверена?"
    mrsjo "Да, мне нужно почувствовать твою энергию!"
    show mrsjsex 47 at Position(xoffset=-34) with vpunch
    mrsjo "АХХ!!!"
    show white zorder 4
    pause 0.3
    hide white with dissolve
    mrsjo "Да..."
    mrsjo "Мне нравится ощущение, когда энергия течет, капает..."
    player_name "Разве во внутрь это не опасно?"
    show mrsjsex 48 at Position(xoffset=-13) with dissolve
    mrsjo "Я на таблетках, тебе не стоит об этом беспокоиться, милый..."
    scene erik_upstairs_night_c2
    show mrsj 56 at right
    show player 426 at left
    with fade
    mrsjo "Ты... Ты молодец, {b}[firstname]{/b}."
    show player 429
    show mrsj 55
    player_name "Ты в порядке, {b}Миссис Джонсон{/b}?"
    show player 426
    show mrsj 56
    mrsjo "Я в порядке, просто немного устала..."
    mrsjo "Надеюсь, завтра я не буду слишком болеть, чтобы заниматься йогой."
    show player 427
    show mrsj 55
    player_name "Надеюсь... {b}Эрик{/b} не против, что мы проводим время вместе?"
    show player 428
    show mrsj 56
    mrsjo "О, он не думает об этом прямо сейчас..."
    show player 426
    mrsjo "Он слишком занят, проводя время со своей новой подругой."
    mrsjo "Думаю, ты многому научишься, если будешь приходить на мои уроки..."
    mrsjo "... но я думаю, мне нужно немного вздремнуть."
    mrsjo "Не стесняйся возвращаться, я буду ждать тебя здесь по вечерам."
    show player 429
    show mrsj 55
    player_name "Конечно, {b}Миссис Джонсон.{/b}!"
    return

label mrsjroom_mrsj_3some_intro:
    show mrsj 39 at right
    show player 21 at left
    show erik 1f zorder 1 at Position(xpos=300)
    player_name "{b}Эрик{/b} и я хотели спросить, не могли бы вы научить нас кое-чему?"
    show player 13
    show erik 4f
    eri "Да, мы хотели бы попробовать... позаниматься сексом."
    show mrsj 40
    show erik 1f
    mrsjo "Я надеялась, что вы двое придете ко мне на пару уроков."
    show mrsj 39
    show player 21
    player_name "Серьёзно?"
    show player 13
    show erik 4f
    eri "Что вы хотите, чтобы мы сделали, {b}Миссис Джонсон{/b}?"
    show mrsj 40b
    show erik 1f
    mrsjo "Ну, я читала эту замечательную книгу, которую ты мне принес..."
    show mrsj 40
    mrsjo "... и я думаю что нашла правильные вещи для вас!"
    mrsjo "Как насчет того, чтобы показать вам пару поз?"
    show mrsj 39
    show player 21
    player_name "Се-сексуальные позиции?"
    show player 13
    show mrsj 40
    mrsjo "Почему бы тебе не снять одежду и присоединиться ко мне в постели?"
    mrsjo "Ты можете следовать моим инструкциям..."
    show erik 55f at Position(xoffset=-8)
    show player 8 at Position(xoffset=-27)
    with fastdissolve
    mrsjo "... и позволь мне сделать все остальное."
    scene erik_upstairs_night_c3
    show mrsjsex 20 at topright
    with fade
    mrsjo "Давайте начнем с этого!"
    mrsjo "Я буду на тебе, Тыковка, пока будет держать рот на замке {b}[firstname]{/b}..."
    mrsjo "... старайтесь не кончать слишком быстро!"
    mrsjo "Я хочу попробовать несколько позиций."
    eri "Окей, {b}Миссис Джонсон{/b}..."
    show mrsjsex 21_22_23_24_25 with fastdissolve
    pause
    eri "{b}Миссис Джонсон{/b}..."
    eri "Это такое приятное чувство... внутри вас..."
    return

label mrsjroom_mrsj_3some_pos1:
    show mrsjsex 26
    mrsjo "Как насчет того, чтобы попробовать что-то другое..."
    mrsjo "... Я хочу, чтобы вы, ребята, взяли меня на спине."
    show mrsjsex 27 at Position(xanchor=0,xpos=200,ypos=100) with fade
    mrsjo "Да, {b}[firstname]{/b}, просто так..."
    mrsjo "... Я хочу чувствовать вас обоих одновременно."
    show mrsjsex 28 at Position(yoffset=42) with fastdissolve
    mrsjo "Ах... Да!"
    show mrsjsex 28_29_30
    mrsjo "Быстрее!!"
    return

label mrsjroom_mrsj_3some_pos2:
    hide screen mrsj_3some_pos2_sex_options
    show mrsjsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
    pause
    show mrsjsex 31 at Position(xoffset=60,yoffset=42) with hpunch
    mrsjo "АХХХ!!!"
    show white zorder 4
    pause 0.3
    hide white with dissolve
    pause
    show mrsjsex 32 with fastdissolve
    mrsjo "Вы сделали настоящий беспорядок со всей этой спермой!"
    player_name "Я вошел внутрь... Это нормально?"
    mrsjo "Хорошо, что я начала принимать таблетки..."
    player_name "Простите, {b}Миссис Джонсон{/b}."
    mrsjo "Все в порядке, дорогой. Я люблю чувство когда сперма капает из моего..."
    mrsjo "... Думаю, нам стоит сделать перерыв."
    scene erik_upstairs_night_c2
    show mrsj 56 at right
    show player 426 zorder 2 at left
    show erik 59f zorder 1 at Position(xpos=300)
    with fade
    mrsjo "Боже мой..."
    show erik 60f
    show mrsj 55
    eri "Ты в порядке, {b}Миссис Джонсон{/b}?"
    show erik 59f
    show mrsj 56
    mrsjo "Просто немного устала, Тыковка..."
    mrsjo "... но вы оба отлично справились."
    mrsjo "Думаю, мне нужно вздремнуть после всего этого!"
    mrsjo "Мальчики, вы можете вернуться в другой день..."
    show mrsj 55
    show erik 60f
    eri "Давай, мы должны уйти и дать {b}миссис Джонсон{/b} отдохнуть."
    show erik 59f
    scene expression "backgrounds/location_erik_house_inside_night_blur.jpg"
    show erik 4 at right
    show player 1 at left
    with fade
    eri "Это было потрясающе!!"
    show erik 1
    show player 17
    player_name "Да, {b}Миссис Джонсон{/b} великолепна..."
    show erik 4
    show player 1
    eri "Никогда не думал, что будет так хорошо..."
    show erik 1
    show player 14
    player_name "Думаю, ей тоже очень понравилось!"
    show erik 4
    show player 1
    eri "Тебе нужно зайти еще раз, чтобы нам было веселее..."
    show erik 1
    show player 14
    player_name "Я постараюсь прийти в ближайшее время, обещаю!"
    show erik 4
    show player 1
    eri "Я пойду поиграю в игры на компе в своей комнате, поговорим позже."
    show erik 1
    show player 14
    player_name "Круто, тогда увидимся позже!"
    hide erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
