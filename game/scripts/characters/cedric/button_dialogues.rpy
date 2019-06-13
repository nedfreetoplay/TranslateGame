label button_cedric_about_jenny:
    show player 10
    player_name "You know she's been trying to get ahold of you, right?"
    show player 5
    show cedric f_normal_talk
    ced "Да, верь мне... Я знаю."
    ced "Я не хочу что то делать с этой сумасшедшей сучкой!"
    show cedric f_normal
    show player 12
    player_name "Это немного грубо."
    show player 5
    show cedric f_normal_talk
    ced "Ты знаешь что она вляпалась в порноиндустрию или типо того?"
    show cedric f_normal
    show player 10
    player_name "Д-да, Я знаю."
    show player 5
    show cedric f_normal_talk
    ced "Сейчас она пытается уговорить меня сделать то же самое!"
    show cedric f_normal
    show player 10
    player_name "Ну да?"
    show player 5
    show cedric f_normal_talk
    ced "Я похож на парня, который занимается порно?!"
    show cedric f_normal
    show player 29 with dissolve
    player_name "Эмм, Я не знаю... Слегка?"
    show player 3
    show cedric f_normal_talk
    ced "Да, что ж... Я нет!"
    ced "Ей просто нужно найти кого-то другого, чтобы вонзить в него свои когти."
    ced "Я покончу с ней."
    show cedric f_normal
    show player 5 with dissolve
    player_name "..."
    show player 10
    player_name "Ты хотябы позвонишь и скажешь ей это?"
    show player 5
    show cedric f_normal_talk
    ced "Почему,чтобы она смогла наорать на меня и обозвать?"
    ced "Нет спасибо."
    ced "Ты скажешь ей."
    hide cedric with dissolve
    pause
    show player 37 with dissolve
    player_name "{b}*Вздох*{/b} Дерьмо."
    player_name "( {b}[jen_name]{/b} это не понравится... )"
    player_name "( Я лучше пойду и дам ей знать. )"
    hide player with dissolve
    return

label button_cedric_see_ya:
    show player 14
    player_name "Мне пора идти."
    show player 13
    show cedric f_normal_talk
    ced "Да, конечно."
    ced "Увидимся, приятель."
    show cedric f_normal
    hide player with dissolve
    pause
    show cedric f_normal_talk
    ced "Не пропускай день ног, Хах!"
    hide cedric with dissolve
    return

label button_cedric_can_you_spot_me:
    show player 10
    player_name "Можешь одолжить мне?"
    show player 13
    show cedric f_normal_talk a_dressed_reject with dissolve
    ced "Нет не могу, приятель."
    show player 5
    ced "Ты еще не готов работать с большими мальчиками."
    show cedric f_normal a_dressed_hips with dissolve
    player_name "..."
    show cedric f_normal_talk a_dressed_point with dissolve
    ced "Я не хочу видеть, как ты уроняешь гайку или взорвешь свое уплотнительное кольцо.."
    show cedric f_normal a_dressed_hips with dissolve
    show player 10
    player_name "Ну да, спасибо не за что."
    show player 5
    show cedric f_normal_talk
    ced "Ахх,не надо так нервничать."
    ced "У тебя все получится довольно скоро."
    ced "Смотри сюда!"
    show cedric f_normal a_dressed_flex with dissolve
    show player 13
    pause
    show cedric f_normal_talk
    ced "Я очень хорош, хм?"
    show cedric f_normal
    show player 14
    player_name "Конечно, {b}Cedric{/b}..."
    show player 13
    show cedric f_normal_talk a_dressed_hips with dissolve
    ced "Хех, оо Да!"
    show cedric f_normal
    return

label button_cedric_what_have_you_been_up_to:
    show player 14
    player_name "Чем ты занимался?"
    show player 13
    show cedric f_normal_talk
    ced "Ох, все было отлично!"
    ced "С тех пор, как я наконец избавился от твоей соседки гарпии по комнате, Наконец-то я могу сосредоточиться на тренировках."
    show cedric f_normal
    show player 4
    player_name "Хм."
    show player 14 with dissolve
    player_name "Что ж, это хорошо... наверное."
    show player 13
    show cedric f_normal_talk
    ced "Это очено хорошо, приятель!"
    show cedric a_dressed_point_himself with dissolve
    ced "Хочешь посмотреть, как я поднимаю штангу?"
    ced "Я поднимаю до 205 кг!"
    show cedric f_normal a_dressed_hips with dissolve
    show player 29 with dissolve
    player_name "Э-э-э, может быть в другое время..."
    show player 13 with dissolve
    show cedric f_normal_talk
    ced "Как знаешь."
    show cedric f_normal
    return

label button_cedric_intro_repeat:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show cedric f_normal_talk
    ced "Как дела, дружище?"
    show cedric f_normal
    show player 14
    player_name "Ох, привет {b}Cedric{/b}."
    show player 13
    show cedric f_normal_talk
    ced "Ты здесь чтобы подкачаться?"
    show cedric f_normal
    return

label button_cedric_intro_first:
    scene expression player.location.background_closeup with None
    show cedric f_normal_talk
    show player 13 at left
    ced "Вау, {b}[firstname]{/b}?"
    show cedric f_normal
    show player 14
    player_name "Ох, здарова {b}Cedric{/b}."
    show player 13
    show cedric f_normal_talk
    ced "Я не видел тебя уже давно, юный друг."
    show cedric f_normal
    show player 14
    player_name "Ну да."
    show player 13
    show cedric f_normal_talk a_dressed_point with dissolve
    ced "Ты наконецто решил начать ходить в спортзал и подкачаться?"
    show cedric f_normal a_dressed_hips with dissolve
    show player 29 with dissolve
    player_name "Д-даа, что-то вроде того..."
    show player 13 with dissolve
    show cedric f_normal_talk
    ced "Как {b}[jen_name]{/b}?"
    show cedric f_normal
    show player 12
    player_name "Эммм, я не знаю... Сучка?"
    show player 13
    show cedric f_normal_talk
    ced "Хахахаха, Отлично сказано!"
    show cedric f_normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
