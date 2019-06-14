label eriks_backyard_erik_thief_in_progress:
    scene eriks_backyard_night_b
    show door_thief_night at Position (xpos=882,ypos=655)
    player_name "( Он... пытается проникнуть через заднюю дверь к {b}Миссис Джонсон{/b} ? )"
    player_name "( Должно быть, это тот взломщик, о котором мы постоянно слышим в новостях. )"
    player_name "( Надо посмотреть поближе... )"
    return

label erik_thief_block2:
    scene eriks_backyard_night_b
    show door_thief_night at Position (xpos=882,ypos=655)
    player_name "( Я пока не могу уйти. )"
    player_name "( Что если он попытается вломиться?! )"
    player_name "( Надо убедиться, что ничего плохого не происходит... )"
    $ game.main()

label erik_thief_confront:
    scene eriks_backyard_c
    show larry 1 at Position (xpos=800) with dissolve
    show player 12 at left with dissolve
    player_name "...Ухх!"
    player_name "Извините!"
    show player 16
    show larry 2 at right with dissolve
    thief "!!!" with hpunch
    show player 12
    player_name "Что вы делаете?"
    show player 16
    show larry 3 with dissolve
    thief "Вот дерь-"
    hide larry with dissolve
    show player 15
    player_name "ЭЙ!"
    player_name "А ну стой!!"
    hide player with dissolve

    scene erik_house_cs03 with fade
    show text "Я собрался предотвратить проникновение вора во двор...\n...Но он очень ловко перескачил через забор.\nЯ погнался за ним, и тогда..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    return

label erik_thief_dex_pass:
    scene erik_house_cs05 with fade
    show text "...Я его догнал и мы схватились...\n...И после непродолжиельной борьбы я его победил..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene eriks_backyard_c
    show larry 4 at left
    with dissolve
    player_name "Эй!"
    show larry 5
    pause
    show larry 4
    player_name "Что ты хотел сделать?!"
    player_name "Хватит дергаться!"
    player_name "Ты ни куда не пойдешь."
    show larry 7
    show erik 52 at Position (xpos=750)
    show mrsj 52 at right
    mrsjo "Что за шум на заднем дворе?"
    mrsjo "Кто там?"
    show mrsj 38
    show erik 53
    eri "{b}[firstname]{/b}?"
    show erik 52
    show larry 6
    player_name "Простите, {b}Миссис Джонсон{/b}. Я не хотел вас разбудить..."
    show larry 4
    player_name "...Но я поймал этого парня, он пытался проникнуть в ваш дом!"
    show larry 7
    show erik 51
    show mrsj 19
    mrsjo "!!!"
    show mrsj 52
    mrsjo "Что? Что случилось?"
    show mrsj 38
    show erik 52
    show larry 6
    player_name "Я услышал какой-то шум и увидел, как этот парень пробирается на задний двор."
    player_name "Я вышел на улицу, посмотреть, куда он пошел, и увидел как он пытается к вам вломиться!"
    show larry 4
    player_name "Он попытался сбежать, но я смог догнать его..."
    show larry 7
    show mrsj 19
    mrsjo "Ох, боже!"
    show mrsj 38
    show larry 5
    mrsjo "Давай-ка посмотрим, кто скрывается за этой маской..."
    hide mrsj
    hide larry
    show larry 8 at left
    with dissolve
    pause
    show larry 9
    show mrsj 61 at right
    with dissolve
    show erik 51
    mrsjo "!!!" with hpunch
    show erik 53
    eri "{b}Мистер Джонсон{/b}?!"
    show erik 3b
    player_name "!!!"
    show mrsj 51 with dissolve
    show larry 10
    larry "Простите..."
    show larry 11
    show mrsj 52
    mrsjo "{b}Ларри{/b}! Боже, что ты делаешь в городе? Я думала ты живешь в другом штате?"
    show mrsj 51
    show erik 52
    show larry 10
    larry "Я... Я знаю... Просто..."
    larry "...Несколько лет назад моя группировка распалась."
    larry "У меня были проблемы с деньгами и... Мне пришлось вернуться."
    show larry 9
    show mrsj 52
    mrsjo "Ты уже несколько лет, как вернулся?!"
    show mrsj 51
    show larry 11
    larry "..."
    show mrsj 52
    mrsjo "Объяснись, {b}Ларри{/b}!"
    show mrsj 51
    show larry 10
    larry "У... У меня не хватило смелости увидеть тебя после того, как я бросил тебя..."
    show larry 9
    show mrsj 19
    mrsjo "И ты решил, что не плохо бы начать воровать?"
    show mrsj 19c
    show larry 11
    larry "..."
    show larry 10
    larry "Я не могу найти роботу!"
    larry "И... меня все здесь знают."
    larry "Я не хотел, чтобы кто-нибудь узнал..."
    show larry 11
    show mrsj 52
    mrsjo "Зачем тогда вообще возвращаться?"
    show mrsj 51
    show erik 51
    show larry 10
    larry "Я... Я скучал по тебе, {b}Тэмми{/b}..."
    larry "Я заглядывал ночью в течение последних двух месяцев, надеясь увидеться с тобой..."
    show larry 9
    show erik 52
    show mrsj 52
    mrsjo "Тебе нужно было думать об этом, прежде чем бросать нас!!"
    mrsjo "Знаешь что? Ты совсем не изменился."
    mrsjo "Ты всё еще думаешь только о себе!!"
    show mrsj 51
    show erik 53
    eri "{b}Миссис Джонсон{/b}... Что теперь делать?"
    show larry 11
    show erik 51
    show mrsj 52
    mrsjo "Вызывай полицию."
    mrsjo "Пусть они позаботятся о нем."
    hide mrsj
    hide erik
    hide larry
    with dissolve
    scene black with fade

    scene erik_house_night_cops
    pause
    show player 5f at Position (xpos=650)
    show erik 52 at Position (xpos=775)
    show mrsj 51 at right
    show harold 3f at left
    show larry 13 at Position (xpos=275)
    with dissolve
    harold "Хорошо, что ты позвонил!"
    harold "Мы два года пытались его поймать..."
    show harold 1f
    show mrsj 52
    show larry 12
    mrsjo "Я... Я никогда не думала, что увижу его снова..."
    mrsjo "...Он всегда создавал проблемы!"
    mrsjo "Я очень рада, что все закончилось, и он исчез из нашей жизни навсегда!"
    show mrsj 51
    show larry 12b
    show erik 51
    show player 11f
    larry "{b}Тэмми{/b}!"
    show erik 52
    larry "Я рад, что у тебя все хорошо..."
    larry "...Я скучал по тебе!!"
    show larry 12
    show erik 50
    show player 5f
    eri "..."
    show larry 13
    show harold 3f
    harold "Давай уже, {b}Ларри{/b}. Отведем тебя в участок."
    hide harold
    hide larry
    with dissolve
    show player 11f
    show erik 2
    show mrsj 61
    with dissolve
    pause
    hide player
    hide erik
    hide mrsj
    with dissolve
    $ erik.complete_events(erik_thief)
    show unlock44 at truecenter with dissolve
    pause
    hide unlock44 with dissolve
    pause .4
    return

label erik_thief_dex_fail:
    scene erik_house_cs04 with fade
    show text "...Он подбежал к забору и перепрыгнул его в один миг!!\nЯ не был достаточно ловким чтобы поймать его..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene eriks_backyard_c with None
    show player 25 with dissolve
    player_name "[dex_warn]Черт..."
    player_name "[dex_warn]Я не могу поверить что он так высоко прыгнул, и я позволил ему уйти!"
    player_name "[dex_warn]Я должен быть в лучшей форме если я хочу поймать его."
    show player 24
    player_name "[dex_warn]Угх."
    player_name "[dex_warn]Я должен вернуться в кровать..."
    hide player with dissolve
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
