label hallway_jenny_start:
    scene hallway
    show player 1 at left
    show jenny 10 at right
    with dissolve
    jen "Разве ты не должен быть в школе?"
    show player 2
    player_name "Разве у тебя не должно быть работы?"
    show jenny 6
    show player 1
    jen "!!!"
    show jenny 9
    jen "Ты же не хочешь играть со мной в эту игру, умник."
    show jenny 6
    show player 14
    player_name "Эй, ты первая начала!"
    show player 34
    player_name "..."
    show jenny 10
    jen "Что это?"
    player_name "{b}*нюх*{/b}"
    show player 35
    player_name "Что-то вкусно пахнет."
    show jenny 9
    show player 11
    jen "Ах, Да. Это, наверное, завтрак, который ждет тебя {b}внизу{/b}, тупица."
    show jenny 12
    jen "Не могу поверить, что она до сих пор готовит тебе завтрак каждый день. Прошло больше месяца с тех пор, как умер {b}твой отец{/b}."
    show player 2
    show jenny 11
    player_name "Да, она хорошая женщина."
    hide player with dissolve
    pause 0.5
    show jenny 10
    jen "Ах, да. Слишком милая, если спросите меня."
    hide jenny
    with dissolve
    return

label hallway_mom_sis_boobs_afterthoughts:
    scene hallway
    show player 26 with dissolve
    player_name "Вау..."
    player_name "Я не могу поверить, что {b}[jen_name]{/b} оголила грудь передо мной..."
    if M_jenny.finished_state(S_jenny_shower_peep_bed_cuddle):
        player_name "Я никогда раньше не видел их так близко..."
    else:
        player_name "Я никогда раньше их не видел."
    player_name "Ее грудь такая красивая..."
    hide player with dissolve
    return

label hallway_sis_hallway_1_started:
    scene hallway
    show jenny 7 at right
    show player 11 at left
    with dissolve
    jen "Эй!"
    show jenny 8
    show player 12
    player_name "Чего тебе надо?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Ты лазил в моем компьютере?"
    show jenny 6
    show player 12
    player_name "Ох... Нет?"
    show jenny 9
    show player 11
    jen "Не {b}лги{/b} мне."
    jen "Я знаю, что ты рылась в моих вещах..."
    show jenny 10
    show player 12
    player_name "Чего?"
    player_name "Я никогда не был в твоей комнате!"
    show jenny 9
    show player 11
    jen "Откуда ты знаешь мой пароль?"
    show jenny 6
    show player 11
    player_name "..."
    show jenny 9
    show player 5
    jen "Что-то ты искал?"
    show jenny 10
    show player 10
    player_name "Ничего! Я сказал тебе-"
    show jenny 9
    show player 11
    jen "Ты пытался найти мои {b}личные{/b} фотографии?"
    jen "Так что ты мог бы {b}использовать{/b} их?"
    show jenny 6
    show player 10
    player_name "Нет! Я же сказал-"
    show jenny 9
    show player 11
    jen "Неважно."
    jen "Если ты снова будешь рыться в моих вещах, я расскажу все {b}[deb_name]{/b}."
    show jenny 7 at right
    show player 5
    jen "ПОНЯТНО?!" with vpunch
    show jenny 8
    show player 10
    player_name "Да..."
    hide player
    hide jenny
    with dissolve
    return

label hallway_sis_hallway_2_started:
    scene hallway
    show jenny 7 at right
    show player 11 at left
    with dissolve
    jen "Стоять!"
    show jenny 8
    show player 12
    player_name "Что тебе нужно?"
    show jenny 9 at Position(xpos=937)
    show player 11
    jen "Куда ты направляешся?"
    show jenny 10
    show player 10
    player_name "Хух?"
    show jenny 9
    show player 11
    jen "Взможно к {b}[deb_name]{/b} в ее комнату?"
    show jenny 6
    show player 29
    player_name "Что?"
    show jenny 9
    show player 11 at left
    jen "В последнее время ты часто подлизываетесь к {b}[deb_name]{/b}."
    jen "Честно говоря, мне все равно: ты всегда был ее любимчиком."
    show jenny 6
    show player 10
    player_name "... Я не понимаю."
    show jenny 9
    show player 11
    jen "Можешь притворяться сколько хочешь..."
    jen "... но я вижу маленькую игру, в которую ты играешь."
    show jenny 10
    show player 14
    player_name "Ну, {b}[deb_name]{/b} нужна была помощь по дому, так что я-"
    show jenny 9
    show player 11
    jen "О, прекращай!"
    jen "Слушай, мне все равно, что ты и {b}[deb_name]{/b} делаете втайне."
    show player 16
    jen "Мы оба знаем, что ты - извращенец."
    show player 11

    jen "Важно то, что мне нужно, чтобы ты сосредоточился!"
    jen "Я не могу позволить тебе отвлекаться на {b}[deb_name]{/b}."
    jen "Мне нужен свежий контент для моих {b}стримов{/b}..."
    jen "... так что лучше принеси мне {b}реквизит{/b}."
    show jenny 11
    show player 12
    player_name "Расслабся. Я принесу, хорошо?"
    show jenny 12
    show player 13
    jen "Отлично."
    hide player
    hide jenny
    with dissolve
    return

label hallway_sis_final_started:
    scene hallway
    show player 11 with dissolve
    player_name "..."
    player_name "( Какие-то голоса доносятся из комнаты {b}[jen_name]{/b} ... )"
    show player 4
    player_name "( Похоже на то что... она с кем-то разговаривает? Но с кем... )"
    show player 1
    player_name "( Может быть, я смогу подкрасться к ее двери и узнать... )"
    hide player with dissolve
    return

label hallway_sis_final_over:
    scene hallway
    show player 11 at left
    show jenny 9 at right
    show jenny 9 at Position(xpos=937)
    with dissolve
    jen "Пссс, эй!!"
    show player 10
    show jenny 9b
    player_name "А?"
    player_name "Что ты делаешь?"
    show player 11
    show jenny 9
    jen "Быстро в мою комнату. Сейчас же!"
    show player 10
    show jenny 10
    player_name "Но, почему?"
    show player 11
    show jenny 9
    jen "Без вопросов. Быстро,  придурок!"
    scene jennybedroom
    show player 12 at left
    show jenny 82 at right
    show jenny 82 at Position(xpos=937)
    with fade
    player_name "Что здесь происходит?"
    show player 11
    show jenny 12
    jen "Мне нужна услуга."
    show player 12
    show jenny 82
    player_name "Позволь мне угадать, больше секс игрушек?"
    show player 16
    show jenny 9
    jen "Нет, ты идиот!"
    show player 12
    show jenny 10
    player_name "Я тебе не слуга, понимаешь?"
    show player 16
    show jenny 7 at right
    jen "Просто ЗАТКНИСЬ уже и дай мне объяснить!!" with hpunch
    show player 11
    show jenny 19
    jen "Мы оба получим от этого то, что хотим..."
    jen "Я обещаю."
    show player 12
    show jenny 18
    player_name "... Ладно?"
    show player 11
    show jenny 12 at Position(xpos=937)
    jen "Хорошо. Мне нужно, чтобы ты кое-что нашел для меня. Это довольно специфично, так что придется поискать."
    show player 10
    show jenny 11
    player_name "Что именно?"
    show player 11
    show jenny 12
    jen "Во первых, найди {b}костюм болельщицы{/b}."
    jen "Потом {b}наручники{/b}."
    show player 10
    show jenny 10
    player_name "Да, редкие вещи... Где мне их поискать?"
    show player 11
    show jenny 7 at right
    jen "Я НЕ ЗНАЮ!"
    show jenny 9 at Position(xpos=937)
    jen "Это твоя часть сделки! Мне все равно, где ты их возьмешь, главное, чтобы они были у тебя!"
    show player 12
    show jenny 9b
    player_name "Что я получу взамен?"
    player_name "Мне больше не нужны трусы..."
    show player 11
    show jenny 12
    jen "Не беспокойтесь об этом! Я дам тебе кое-что получше трусиков!"
    show player 12
    show jenny 10
    player_name "Ты даже не скажешь мне, что это такое?"
    show player 11
    show jenny 7 at right
    jen "Я сказала, {b}НЕ БЕСПОКОЙСЯ{/b}!!"
    show jenny 9 at Position(xpos=937)
    jen "Это больше, чем ты заслуживаешь, и тебе это определенно понравится, так что просто ИДИ И ПРИНЕСИ!"
    show player 10
    show jenny 9b
    player_name "{b}*вздох*{/b}"
    show jenny 82
    player_name "Хорошо. Посмотрим, что я смогу найти..."
    show player 1
    show jenny 12
    jen "Отлично."
    show player 11
    show jenny 7 at right
    jen "А сейчас {b}ПРОВАЛИВАЙ{/b}!!" with hpunch
    hide player
    hide jenny
    return

label hallway_mom_sleepover_offer:
    scene hallway_night
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Привет, милый."
    show player 17
    show debbie 1
    player_name "Привет, {b}[deb_name]{/b}."
    show debbie 2
    show player 1
    deb "Как спалось?"
    show player 10
    show debbie 14
    player_name "Я не сплю так легко, как раньше, до того, как умер {b}отец{/b}. Хотя со мной все в порядке."
    show player 5
    show debbie 13
    deb "Ты думаешь обо всем, что происходило в последнее время?"
    show debbie 14b
    show player 10
    player_name "Да, наверное... Немного."
    show player 5
    show debbie 13
    deb "Я не хочу, чтобы ты волновался, милый."
    deb "Все будет хорошо, я обещаю."
    show debbie 14
    show player 10
    player_name "Как насчет тебя? Хорошо спишь?"
    show player 5
    show debbie 13
    deb "Не очень."
    show debbie 14
    pause
    show debbie 13
    deb "... Но я уже привыкла. У меня были проблемы со сном, когда мой муж ушел от меня много лет назад."
    show player 11
    deb "Я понимаю, через что ты проходишь."
    show debbie 14b
    show player 12
    player_name "Правда?"
    show player 5
    show debbie 13
    deb "Да. Я тоже скучаю по твоему {b}отцу{/b}."
    show debbie 14
    pause
    show debbie 2
    deb "Мы были друзьями очень долгое время."
    show debbie 1
    show player 13
    pause
    hide player
    show debbie 4 at center
    with dissolve
    pause
    show player 13 at left
    show debbie 2 at right
    with dissolve
    deb "По крайней мере, теперь у меня есть ты ..."
    show debbie 1
    pause
    show debbie 2
    deb "Если у тебя снова будут проблемы со сном, приходи ко мне, хорошо?"
    show debbie 1
    show player 10
    player_name "В твою спальню?"
    show player 5
    show debbie 3
    deb "Конечно!"
    show debbie 2
    deb "Возможно, компания поможет нам заснуть?"
    show debbie 1
    show player 10
    player_name "Ты не возражаешь, если я буду спать в твоей кровати?"
    show player 11
    pause
    show debbie 13
    deb "Думаю, это пойдет нам на пользу..."
    show player 13
    deb "... После всего, что случилось."
    show debbie 14
    show player 14
    player_name "...Хорошо. Конечно, {b}[deb_name]{/b}."
    hide player
    hide debbie
    with dissolve
    show unlock34 at truecenter with dissolve
    pause
    hide unlock34 with dissolve
    return

label hallway_mom_movie_night_two:
    scene hallway_night
    show player 1 at left
    show debbie 62 at right
    deb "Привет, милый!"
    show player 2
    show debbie 61
    player_name "Привет {b}[deb_name]{/b}, в чем дело?"
    show player 1
    show debbie 62
    deb "Я думал о просмотре кинофильма."
    deb "Хочешь присоединиться ко мне?"
    show player 2
    show debbie 61
    player_name "Конечно, с удовольствием!"
    show player 1
    show debbie 62
    deb "Замечательно, тогда я пойду располагаться! Приходите ко мне в {b}гостиную{/b}, когда будешь готов."
    show player 2
    show debbie 61
    player_name "Звучит неплохо! Я сейчас спущусь."
    hide debbie
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
