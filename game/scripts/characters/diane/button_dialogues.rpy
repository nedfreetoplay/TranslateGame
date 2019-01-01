label dianes_dialogue_daisy:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Как поживает {b}Дейзи{/b}?"
    show player 13
    show diane f_normal_talk
    dia "О, Она прекрасно устроилась!"
    dia "Забавно, что фермер нашел волшебную корову, не так ли?"
    dia "Хорошо, что я построила этот сарай..."
    show diane f_normal
    pause
    show diane f_laugh
    dia "Она очень милая девушка."
    show diane f_normal
    show player 14
    player_name "Да, верно."
    show player 13
    show diane f_normal_talk
    dia "Я так рада, что мы нашли ее."
    show diane f_normal
    return

label dianes_dialogue_cow_girl:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides
    with dissolve
    player_name "Есть успехи с нашим новым другом?"
    show player 5
    show diane f_shamed_talk_smile
    dia "{b}*вздыхая*{/b} Эта бедняжка."
    dia "Она все еще наполовину убеждена, что ее хозяин появится и накажет ее за то, что она позволила нам увидеть ее."
    dia "Что бы этот ужасный человек с ней не сделал, она не готова говорить об этом."
    show diane f_shamed
    show player 10
    player_name "Она хотя бы назвала тебе свое имя?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Нет, пока нет."
    dia "Но она приходит в себя."
    dia "Думаю, она скоро будет готова поговорить с тобой."
    show diane f_shamed
    show player 10
    player_name "Хорошо."
    show player 5
    return

label dianes_dialogue_milk_sample:
    scene expression player.location.background_blur with None
    show diane b_naked a_naked_sides
    show player 14 at left
    player_name "Можно мне немного вашего молока?"
    show player 13
    show diane f_smirk_talk
    dia "Хе-хе, чувствуешь жажду, не так ли?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Нет, мне действительно нужен образец."
    show player 13 with dissolve
    show diane f_surprised
    pause
    show diane f_shamed_talk
    dia "О."
    dia "Ох, конечно. Просто дайте мне секунду."
    if M_diane.outfit == "shirtless":
        show diane b_topless
    show diane a_squeeze3 f_down_front
    with dissolve
    pause
    show diane f_normal_talk a_bottle1 with dissolve
    dia "Это сработает?"
    show diane b_naked f_normal a_naked_sides with dissolve
    show player 713
    with dissolve
    player_name "Да, это просто замечательно!"
    player_name "Спасибо, {b}Диана{/b}!"
    show diane f_normal_talk
    hide player with dissolve
    dia "Без проб-"
    show diane f_surprised
    pause
    show diane f_shamed_front
    dia "( Что он собирается делать? )"
    hide diane with dissolve

    return

label dianes_dialogue_hows_baby_doing_boy:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Как у него дела?"
    show player 13
    show diane f_normal_talk
    dia "О, он просто замечательный!"
    dia "Я никогда не хочу его отпустить."
    show diane f_normal
    show player 14
    player_name "В конце концов, тебе придется его отпустить..."
    show player 13
    show diane f_laugh
    dia "Не-а!"
    show diane f_cheese
    show player 17
    player_name "Хехехе."
    show player 13
    return

label dianes_dialogue_hows_baby_doing_girl:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Как у неё дела?"
    show player 13
    show diane f_normal_talk
    dia "О, Она просто замечательная!"
    dia "Я никогда не хочу её отпустить."
    show diane f_normal
    show player 14
    player_name "В конце концов, тебе придется её отпустить..."
    show player 13
    show diane f_laugh
    dia "Не-а!"
    show diane f_cheese
    show player 17
    player_name "Хехехе."
    show player 13
    return

label dianes_dialogue_get_anything_baby:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Могу я вам что-нибудь предложить?"
    show player 13
    show diane f_normal_talk
    dia "Нет, все нормально."
    dia "Спасибо, жеребец."
    show diane f_normal
    show player 14
    player_name "Пожалуйста."
    show player 13
    show diane f_shamed_talk_smile
    dia "Нет уж, спасибо тебе, {b}[firstname]{/b}."
    dia "За всё."
    show diane f_shamed
    show player 14
    player_name "Не за что, {b}Диана{/b}."
    show player 13
    return

label dianes_dialogue_baby_leave:
    show player 14 at left
    show diane b_casual a_casual_baby
    player_name "Я оставлю вас в покое, ребята."
    show player 13
    show diane f_normal_talk
    dia "Хорошо."
    show diane f_laugh
    dia "Скажи, пока, папа."
    show diane f_cheese
    show player 17
    player_name "Хехе."
    show player 36 with dissolve
    player_name "До свидания, малыш."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_gave_birth_intro:
    show player 14 at left
    show diane b_casual a_casual_baby
    with dissolve
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    if M_diane.pregnancy.baby_gender == "boy":
        dia "Шшш, он спит."
    else:
        dia "Шшш, она спит."
    show diane f_normal
    show player 14
    player_name "О, прости."
    show player 13
    return

label dianes_dialogue_intro_kitchen:
    scene expression player.location.background_blur
    show player 14 at left
    if M_diane.is_naked:
        $ M_diane.set("previous outfit", "naked")
    else:
        $ M_diane.set("previous outfit", "cow")
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "nightgown"
    show diane b_naked a_nightgown_water
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Привет, {b}[firstname]{/b}."
    show diane f_normal
    show player 10
    player_name "Ты в порядке?"
    show player 5
    dia "Хмм?"
    show diane f_normal_talk
    dia "Да, Я в порядке."
    show player 13
    dia "Мне просто хотелось пить, поэтому я пришла сюда за стаканом воды."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Сейчас я просто размышляю..."
    show diane f_normal
    show player 14
    player_name "О чем?"
    show player 13
    show diane f_laugh
    dia "Хе-хе, я не знаю, о работе, наверно..."
    show diane f_normal
    show player 14
    player_name "Хорошо."
    show player 13
    return

label dianes_dialogue_hows_business:
    show player 14 at left
    show diane b_naked a_naked_sides
    player_name "Тебе было легче следить за всеми вашими заказами сейчас?"
    show player 13
    show diane f_laugh
    dia "О боже, да!"
    show diane f_normal_talk
    dia "Я думаю, что мой запас молока более чем удвоился с момента рождения!"
    dia "Сейчас производство идет очень гладко."
    if M_diane.pregnancy.number_of_babies == 1:
        dia "Я просто должна быть уверена, что оставлю немного молока для малыша."
        show diane f_laugh
        dia "Наш ребенок так голоден!"
    else:
        dia "Я просто должна быть уверена, что оставлю немного молока для малышей."
        show diane f_laugh
        dia "Наши дети так голодны!"
    show diane f_normal
    show player 17
    player_name "Хаха."
    show player 14
    player_name "Ну, твое молоко такое вкусное... Я не могу их винить!"
    show player 13
    return

label dianes_dialogue_goodnight_1:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Я как раз собирался спать."
    player_name "Тебе что-нибудь нужно?"
    show player 13
    dia "Хмм?"
    show diane f_normal_talk
    dia "О, я в порядке, жеребец."
    dia "Спасибо что спросил."
    show diane f_normal
    show player 14
    player_name "Хорошо, спокойной ночи."
    show player 13
    show diane f_normal_talk
    dia "Спокойной ночи."
    hide player
    hide diane
    with dissolve
    if M_diane.get("previous outfit") == "naked":
        $ M_diane.is_naked = 1
    else:
        $ M_diane.outfit = "cow"
    return

label dianes_dialogue_goodnight_2:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Да, все в порядке."
    player_name "Извините, что разбудил."
    show player 13
    show diane f_normal_talk
    dia "Все нормально."
    show diane f_normal
    show player 14
    player_name "Спокойной ночи."
    show player 13
    show diane f_normal_talk
    dia "Спокойной ночи, жеребец."
    hide player
    hide diane
    with dissolve
    if M_diane.get("previous outfit") == "naked":
        $ M_diane.is_naked = 1
    else:
        $ M_diane.outfit = "cow"
    return

label dianes_dialogue_what_up_to:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Что ты собираешься делать?"
    show player 13
    show diane f_normal_talk
    dia " Я просто сижу здесь и скучаю."
    dia "Телевизор поздно ночью-отстой."
    show diane f_normal
    show player 14
    player_name "Хех, это верно!"
    show player 13
    show diane f_smirk_talk
    dia "Ты хочешь сделать что-то интересное?"
    show diane f_smirk
    show player 10
    player_name "Что ты имеешь в виду?"
    show player 13
    show diane f_smirk_talk
    dia "Ммм, я могу придумать несколько вещей..."
    show diane f_smirk
    return

label dianes_dialogue_on_my_way_debbie:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Я как раз собирался повидать {b}[deb_name]{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ааа, хорошо."
    dia "Она в своей комнате."
    show diane f_normal
    show player 14
    player_name "Я поговорю с тобой позже, ладно?"
    show player 13
    show diane f_normal_talk
    dia "Хорошо."
    show diane f_normal
    hide player with dissolve
    pause
    show diane f_smirk_talk
    dia "Вы вдвоем повеселитесь."
    show diane f_laugh
    dia "Хехехе."
    hide diane with dissolve
    return

label dianes_dialogue_leave_d19_d20_day:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Я должен проверить сад."
    show player 13
    show diane f_normal_talk
    dia "Хорошо."
    dia "Только не забывай, что мне тоже нужна твоя помощь!"
    show diane f_normal
    show player 14
    player_name "Не забуду."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_business:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Бизнес процветает!"
    dia "Я едва успеваю за всеми заказами!"
    show diane f_normal
    show player 14
    player_name "Это ведь хорошо, правда?"
    show player 13
    show diane f_normal_talk
    dia "Это очень хорошо."
    show diane f_laugh
    dia "Скоро мне придется нанимать больше сисек."
    show diane f_cheese
    return

label dianes_dialogue_call_veronica:
    show player 10 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Ты уже говорила с {b}Вероникой{/b}?"
    show player 13
    show diane f_sad_talk
    dia "Нет, еще не говорила."
    show diane f_normal_talk
    dia "Я поговорю."
    show diane f_normal
    show player 14
    player_name "Она действительно хотела бы работать на тебя."
    show player 13
    show diane f_laugh
    dia "Да, посмотрим."
    show diane f_cheese
    return

label dianes_dialogue_what_are_you_up_to:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Что ты делаешь?"
    show player 13
    show diane f_normal_talk
    dia "О, просто смотрю телевизор и потягиваю вкуснейшее вино {b}[deb_name]{/b}."
    dia "Так приятно снова иметь соседей."
    show diane f_normal
    show player 14
    player_name "Разве?"
    show player 13
    show diane f_normal_talk
    dia "Конечно!"
    dia "Мне было так одиноко там, в большом доме, одной."
    show diane f_normal
    show player 14
    player_name "Да, могу себе представить."
    show player 13
    show diane f_normal_talk
    dia "Теперь я снова чувствую себя частью семьи."
    show diane f_normal
    show player 14
    player_name "Ты всегда была частью нашей семьи, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ооо, спасибо, милый."
    show diane f_normal
    return

label dianes_dialogue_wheres_debname:
    show player 10 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Разве она обычно не сидит здесь с тобой?"
    show player 13
    show diane f_normal_talk
    dia "Сегодня она рано легла спать..."
    dia "... Сказала, что устала."
    show diane f_normal
    show player 14
    player_name "О, понятно."
    show player 13
    show diane f_normal_talk
    dia "Ты все еще можешь навестить ее, если хочешь, я уверена, она не будет возражать."
    show diane f_normal
    show player 14
    player_name "Д-да, возможно..."
    show player 13
    return

label dianes_dialogue_love_that_nightgown:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Это выглядит потрясающе на вас!"
    show player 13
    show diane f_laugh a_nightgown_hip with dissolve
    dia "Хехе, спасибо!"
    show diane f_reading_intrigued
    dia "Я беспокоилась, что это может быть немного неприлично, но учитывая, что {b}[deb_name]{/b} и {b}[jen_name]{/b} находяться рядом..."
    show diane f_normal
    show player 14
    player_name "Хех, д-да."
    show player 426
    pause
    show diane f_smirk_talk
    dia "Хе-хе, ты еще со мной красавчик?"
    show diane f_smirk
    player_name "Хмм?"
    show player 29 with dissolve
    player_name "О, прости!"
    show player 3
    show diane f_smirk_talk
    dia "Ха-ха, все в порядке."
    dia "Можешь посмотреть."
    show diane f_smirk
    show player 426 with dissolve
    pause
    pause
    show player 403
    show diane a_nightgown_sides with dissolve
    return

label dianes_dialogue_goodnight:
    show player 14 at left
    show diane f_normal b_nightgown a_nightgown_sides
    player_name "Мне, наверное, пора спать."
    show player 13
    show diane f_normal_talk
    dia "Да, мне тоже."
    show diane f_normal
    show player 14
    player_name "Спокойной ночи, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Спокойной ночи, красавчик."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_hows_the_couch:
    show player 14 at left
    show diane f_normal b_shirtless a_shirtless_sides
    player_name "Ты хорошо спишь?"
    show player 13
    show diane f_normal_talk
    dia "О, все в порядке."
    dia "Немного бугристый, но я справлюсь."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Хочешь услышать что-то странное?"
    show diane f_normal
    show player 14
    player_name "Конечно."
    show player 13
    show diane f_normal_talk
    dia "{b}[jen_name]{/b} все время спускается посреди ночи и пыхтит, когда находит меня лежащей там."
    dia "Затем, когда я спрашиваю ее, что ей нужно, она закатывает глаза и уходит, бормоча что-то о трате денег."
    dia "Есть идеи, что это значит?"
    show diane f_normal
    show player 29 with dissolve
    player_name "Я эээ-"
    show player 3
    show diane f_normal_talk
    dia "Что ей могло понадобиться в гостиной посреди ночи?"
    show diane f_normal
    pause
    show player 10 with dissolve
    player_name "Понятия не имею."
    show player 5
    show diane f_thinking
    dia "{b}*вздыхая*{/b} Возможно, это ее способ залезть мне под кожу."
    show diane f_normal
    show player 14
    player_name "Хех да, наверное..."
    show player 13
    show diane f_annoyed_talk
    dia "Она такая стерва."
    show diane f_cheese
    return

label dianes_dialogue_feeling_better:
    show player 14 at left
    show diane f_normal
    player_name "Как ты себя чувствуешь?"
    show player 13
    show diane f_laugh
    dia "О, намного лучше теперь, когда ты помогаешь мне качать!"
    show diane f_smirk_talk
    dia "Спасибо тебе за это, {b}[firstname]{/b}."
    show diane f_smirk
    show player 14
    player_name "Пожалуйста."
    player_name "Просто постарайся побольше отдыхать, хорошо?"
    show player 13
    show diane f_laugh
    dia "Ха-ха, хорошо, папа!"
    show diane f_cheese
    show player 17
    player_name "Хаха!"
    show player 13
    show diane f_smirk
    return

label dianes_dialogue_like_working_for_you:
    show player 14 at left
    show diane f_normal
    player_name "Знаешь, мне очень нравится эта работа, {b}Диана{/b}."
    show player 13
    show diane f_laugh
    dia "Держу пари, что это так!"
    if M_diane.outfit == "dressed":
        show diane f_smirk_talk a_dressed_finger with dissolve
    else:
        show diane f_smirk_talk
    dia "Какой молодой человек не наслаждался бы грудью весь день?"
    if M_diane.outfit == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    show player 14
    player_name "Это не то, что я-"
    player_name "Я имею в виду... Эта часть довольно замечательная."
    show player 401
    player_name "У тебя классные сиськи."
    show player 403
    show diane f_smirk_talk
    dia "Угу."
    show diane f_smirk
    show player 14
    player_name "... Но дело не только в этом!"
    player_name "Приятно заботиться о тебе."
    player_name "Мне это нравится."
    show player 13
    if M_diane.outfit == "dressed":
        show diane f_smirk_talk a_dressed_blush with dissolve
    else:
        show diane f_smirk_talk
    dia "Ааа."
    dia "Мне это тоже нравится, {b}[firstname]{/b}."
    if M_diane.outfit == "dressed":
        show diane f_smirk a_dressed_shovel with dissolve
    else:
        show diane f_smirk
    pause
    show diane f_smirk_talk
    dia "Только не говори {b}[deb_name]{/b}!"
    show diane f_smirk
    show player 14
    player_name "Не волнуйся, я не буду."
    show player 403
    return

label dianes_dialogue_leave_d12b:
    show player 14 at left
    show diane f_normal
    player_name "Мне лучше вернуться."
    show player 13
    show diane f_normal_talk
    dia "Хорошо."
    dia "Если тебе что-нибудь понадобится, ты знаешь, где меня найти."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_have_you_spoken_with_debname:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Ты говорила с {b}[deb_name]{/b} в последнее время?"
    show player 13
    show diane f_tired_talk
    dia "О, все время!"
    dia "Мы снова вернулись к ежедневным телефонным звонкам."
    show diane f_tired
    show player 14
    player_name "Это хорошо."
    show player 13
    show diane f_tired_talk
    dia "Это было замечательно!"
    dia "Я так по ней скучала!"
    show diane f_tired
    show player 14
    player_name "Ну, она тоже по тебе скучала."
    player_name "Мы все это сделали, правда."
    show player 13
    show diane f_tired_talk
    dia "Ааа."
    hide player
    if M_diane.outfit == "dressed":
        show diane kiss
    else:
        show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    return

label dianes_dialogue_about_veronica:
    show player 12 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Так как ты познакомилась с той девушкой, {b}Вероникой{/b}?"
    show player 13
    show diane f_tired_talk
    dia "Ты имеешь в виду {b}Ви{/b}?"
    dia "О, я люблю эту девушку!"
    dia "Мы познакомились в садоводческой секции магазина {b}Consum-R{/b}, пару лет назад."
    dia "Она только что переехала сюда из деревни и никого не знала."
    show diane f_tired
    show player 14
    player_name "Бьюсь об заклад, это было тяжело."
    show player 13
    show diane f_tired_talk
    dia "О, это определенно было так."
    dia "Она была петерянной!"
    dia "Я предложил показать бедняжке город в обмен на совет по садоводству, и мы вроде как поладили."
    show diane f_tired
    show player 14
    player_name "Это было мило."
    show player 13
    show diane f_tired_talk
    dia "Да, наверное."
    dia "Честно говоря, мне тоже нужен был друг."
    dia "Из-за того, что {b}[deb_name]{/b} так занята {b}твоим отцом{/b} и все такое."
    show diane f_tired
    show player 5
    player_name "..."
    pause
    show diane f_tired_talk
    dia "О, прости меня, красавчик!"
    dia "Я не хотела, чтобы это прозвучало плохо."
    show diane f_tired
    show player 10
    player_name "Да, я знаю, что это не так."
    show player 5
    show diane f_tired_talk
    dia "Твой {b}отец{/b} был хорошим человеком, он мне всегда нравился."
    show diane f_tired
    show player 10
    player_name "Спасибо."
    show player 5
    return

label dianes_dialogue_hows_the_garden_2:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Так я действительно справляюсь с садом?"
    show player 13
    show diane f_tired_talk
    dia "Ты справляешься лучше, чем хорошо!"
    dia "Я никогда не видела, чтобы мой сад выглядел так хорошо!"
    dia "У меня могут быть лучшие огурцы во всей стране!"
    show diane f_tired
    show player 14
    player_name "Ха, Не знаю насчет этого..."
    player_name "Я рад, что все так хорошо получилось."
    show player 13
    return

label dianes_dialogue_take_it_easy:
    show player 14 at left
    show diane f_tired b_naked a_magic_dressed_shovel_shirtless_sides
    player_name "Ладно, думаю, мне пора возвращаться к работе."
    show player 10
    player_name "Успокойся, хорошо?"
    player_name "Я беспокоюсь, что ты слишком много работаешь."
    show player 5
    show diane f_tired_talk
    dia "Пф, ты говоришь как {b}[deb_name]{/b}..."
    dia "Я в порядке."
    show diane f_tired
    show player 10
    player_name "Ладно..."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_about_debname:
    show player 14 at left
    show diane f_normal
    player_name "Я рад, что ты снова проводишь время с {b}[deb_name]{/b}."
    player_name "Я знаю, что она скучает по вашей компании."
    show player 13
    show diane f_normal_talk a_dressed_blush with dissolve
    dia "Аууу и я скучала!"
    show diane a_dressed_shovel with dissolve
    dia "В молодости мы были неразлучны, понимаешь?"
    show diane f_normal
    show player 14
    player_name "Да, я слышал эти истории."
    show player 13
    show diane f_laugh
    dia "Ха!"
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Надеюсь, она не рассказала тебе все истории!"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 10
    player_name "Ааа?"
    show player 13
    show diane f_laugh
    dia "Хе-хе, неважно."
    show diane f_normal
    show player 14
    player_name "Я до сих пор не могу понять, насколько вы похожи..."
    show player 13
    show diane f_normal_talk
    dia "Да, мы привыкли получать это все время."
    dia "В колледже нас называли близнецами."
    show diane f_normal
    show player 14
    player_name "Я это вижу."
    show player 13
    show diane f_normal_talk
    dia "Я была дикой, а она была хорошенькой!"
    show diane f_normal
    show player 29 with dissolve
    player_name "Я думаю, вы обе хорошенькие, {b}Диана{/b}."
    show player 3
    show diane f_shamed_talk_smile a_dressed_blush with dissolve
    dia "Ауу, спасибо, милый."
    show diane f_normal a_dressed_shovel with dissolve
    show player 13 with dissolve
    return

label dianes_dialogue_hows_the_garden:
    show player 14 at left
    show diane f_normal
    player_name "Как поживает твой сад?"
    show player 13
    show diane f_sad_talk
    dia "Он определенно видел лучшие дни..."
    dia "В последнее время я была так занята другой работой, что боюсь, мой сад просто не получает внимания, которого он заслуживает."
    show diane f_normal_talk
    dia "Вот почему я была так взволнована, когда {b}[deb_name]{/b} сказала, что ты можешь помочь мне этим летом."
    show diane f_normal
    show player 14
    player_name "Я с радостью помогу, {b}Диана{/b}!"
    show player 13
    return

label dianes_dialogue_what_have_you_been_up_to:
    show player 14 at left
    show diane f_normal
    player_name "So what have you been doing with yourself these past few years?"
    show player 13
    show diane f_normal_talk
    dia "Oh, not much really..."
    show diane f_normal
    show player 14
    player_name "Not much?!"
    player_name "I thought you were out there partying like crazy and getting chased by rich men?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Haha, goodness no!"
    dia "Whatever gave you that idea?"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Well, {b}[deb_name]{/b} always says you're the wild one."
    show player 13
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Well, perhaps in my younger days..."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Honestly, since the divorce, I spend most of my time right here in this garden."
    show diane f_normal
    show player 14
    player_name "You mean, you don't go out at all anymore?"
    show player 13
    show diane f_normal_talk
    dia "Occasionally I'll go out for a drink with my friend {b}Veronica{/b}."
    dia "Nothing too exciting."
    show diane f_normal
    show player 14
    player_name "Don't you miss it?"
    show player 13
    show diane f_normal_talk
    dia "Hmm, sometimes."
    dia "I'm too old for that kind of life now."
    show diane f_smirk_talk
    dia "Besides, there's no good men left in this town."
    show diane f_smirk
    show player 12
    player_name "Really?!"
    show player 13
    show diane f_laugh
    dia "Heh, trust me."
    show diane f_smirk_talk
    dia "At my age, the only thing left is the dregs."
    show diane f_smirk
    show player 10
    player_name "Bummer."
    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane f_normal_talk
    with dissolve
    dia "Hey there, {b}[firstname]{/b}!"
    dia "I'm so glad you decided to come and help me."
    show diane f_normal
    show player 14
    player_name "Yeah, it's no problem {b}Diane{/b}."
    player_name "Thanks for paying me!"
    show player 13
    show diane f_laugh
    dia "Hehe, my pleasure handsome."
    show diane f_normal
    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired_talk b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    dia "Hey, {b}[firstname]{/b}."
    dia "My garden is looking really-"
    dia "*Yawn*"
    dia "... Really nice."
    show diane f_tired
    show player 10
    player_name "You alright, {b}Diane{/b}?"
    show player 5
    show diane f_tired_talk
    dia "Yeah, I'm okay."
    dia "Just tired."
    show diane f_tired
    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Hey there, handsome!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You need something?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You ready to work?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You heading to bed?"
    show diane f_normal
    show player 14
    player_name "Yeah, in a couple minutes."
    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You ready to work?"
    show diane f_normal
    return

label dianes_dialogue_intro_d19_couch:
    show player 13 at left
    if M_diane.is_naked:
        $ M_diane.set("previous outfit", "naked")
    else:
        $ M_diane.set("previous outfit", "cow")
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "nightgown"
    show diane f_smirk_talk b_naked a_naked_sides
    with dissolve
    dia "Hey there, stud!"
    show diane f_smirk
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "You looking for me or {b}[deb_name]{/b}?"
    show diane f_normal
    return

label dianes_dialogue_intro_d20_couch:
    show player 13 at left
    if M_diane.is_naked:
        $ M_diane.set("previous outfit", "naked")
    else:
        $ M_diane.set("previous outfit", "cow")
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "nightgown"
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Hmm, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Hey, {b}Diane{/b}."
    show player 13
    show diane f_normal_talk
    dia "Everything alright?"
    show diane f_normal
    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left
    if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package):
        $ M_diane.outfit = "shirtless"
    show diane f_normal b_naked a_naked_sides
    with dissolve
    player_name "You ready to pump?"
    show player 13
    show diane f_normal_talk
    dia "Absolutely."
    dia "Just give me one second to get set up."
    hide diane with dissolve
    show player 14
    player_name "O-okay."
    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, there's not much to report yet."
    dia "Unless you're interested in hearing about my morning sickness?"
    show diane f_normal
    show player 10
    player_name "Well, if you want to talk about it we can?"
    show player 13
    show diane f_laugh
    dia "Haha, oh goodness no!"
    show diane f_normal_talk
    dia "I appreciate you asking though."
    dia "Thanks, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "Oh, there's not much to report yet."
    dia "Unless you're interested in hearing about my morning sickness?"
    show diane f_normal
    show player 10
    player_name "Well, if you want to talk about it we can?"
    show player 13
    show diane f_laugh
    dia "Haha, oh goodness no!"
    show diane f_normal_talk
    dia "I appreciate you asking though."
    dia "Thanks, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Heh, my tits are so swollen!"
    dia "Do they look bigger to you?"
    show diane f_normal
    show player 26
    player_name "I dunno, they were pretty big to begin with..."
    show player 18
    show diane f_normal_talk
    dia "Oh, c'mon!"
    show player 13
    dia "They're definitely bigger!"
    show diane f_normal
    pause
    show player 14
    player_name "I just love your little baby bump!"
    show player 13
    if not M_diane.outfit == "nightgown":
        show diane f_laugh a_touch_belly with dissolve
    else:
        show diane f_laugh
    dia "Hehe, I know!"
    show diane f_normal_talk
    dia "Isn't it adorable?"
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Thanks for checking in with me, {b}[firstname]{/b}."
    show diane f_normal
    show player 14
    player_name "Of course."
    player_name "I can't wait to meet our baby, {b}Diane{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Aww, you're the sweetest man in the world!"
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    if not M_diane.outfit == "nightgown":
        show diane f_tired_talk b_naked a_touch_belly
    else:
        show diane f_tired_talk b_naked a_naked_sides
    with dissolve
    dia "Ugh, I'm exhausted..."
    show player 5
    dia "My feet are killing me, I look like a whale, and my tits never stop leaking!"
    show diane f_tired
    show player 10
    player_name "... Oh."
    show player 5
    show diane f_laugh
    dia "Hehe, but it's okay."
    show diane f_normal_talk
    dia "I'm gonna be a mommy very soon!"
    show diane f_normal
    show player 14
    player_name "That's right, you are!"
    show player 13
    show diane f_normal_talk
    dia "I'm so excited, {b}[firstname]{/b}!"
    dia "I can't wait to hold our child in my arms!"
    show diane f_normal
    show player 14
    player_name "Yeah, me too."
    show player 13
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    dia "You ready to get started?"
    show diane f_smirk
    show player 14
    player_name "S-sure."
    show player 13
    show diane f_smirk_talk
    dia "Thank goodness!"
    dia "I'm getting so wet just thinking about that big dick of your's putting a baby inside me..."
    show diane f_smirk
    show player 10
    player_name "You are?!"
    hide player
    show diane b_pull_mc_naked f_empty a_empty
    with dissolve
    dia "Mmm, I need it so bad, {b}[firstname]{/b}!"
    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed_mc
    show diane_sex_breed pre_talk
    with dissolve
    dia "That's it, stud."
    dia "Give it to me."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Ahh!!"
    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "I wanted to talk to you about your cow outfit..."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    menu:
        "Put it back on." if M_diane.is_naked:
            show player 14 at left
            show diane f_normal
            player_name "I want you to wear it while I breed you."
            player_name "It's so sexy!"
            show player 13
            show diane f_laugh
            dia "Oh, I'm so happy you think so!"
            show diane f_normal_talk
            dia "I love it too!"
            show diane f_smirk_talk
            dia "It just feels right, you know?"
            dia "Wearing it in here."
            show diane f_smirk
            show player 14
            player_name "Yeah, totally."
            hide diane
            with dissolve
            $ M_diane.is_naked = 0
            $ M_diane.outfit = "cow"

        "Could you remove it?" if not M_diane.is_naked:
            show player 14 at left
            show diane f_normal
            player_name "I'd rather have you completely naked."
            show player 13
            show diane f_smirk_talk
            dia "You would?!"
            dia "Mmm, you naughty boy..."
            show diane f_smirk
            pause
            show diane f_smirk_talk
            dia "I can take it off, if that's what you really want."
            dia "Whatever helps you put a baby in my belly."
            hide diane
            with dissolve
            $ M_diane.is_naked = 1
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "What did I need to do again?"
    show player 13
    show diane f_normal_talk
    dia "Hmm?"
    dia "Oh, {b}just head into the shed and dump what's in the pump into a storage jug.{/b}"
    show diane f_normal
    show player 14
    player_name "Right!"
    player_name "I'm on it!"
    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "How are you doing over here?"
    show player 426
    show diane f_laying_laugh
    dia "Mmm, fantastic!"
    show diane f_laying_smirk_up
    show player 429
    player_name "Can I get you anything?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "I wouldn't say no to a drink."
    show diane f_laying_smirk_up
    show player 429
    player_name "Your wish is my command!"
    player_name "What kind of drink do you want?"
    show player 426
    $ randomdrink = M_diane.get("random drink")
    show diane f_laying_thinking
    dia "How about a {b}[randomdrink]{/b}?"
    show diane f_laying_smirk_up
    show player 427
    player_name "{b}[randomdrink]{/b}?!"
    player_name "I've never made anything like that before..."
    show player 426
    show diane f_laying_laugh
    dia "Hehe, no worries. I'll do it."
    show diane f_laying_smirk_up
    show player 429
    player_name "No! I can figure it out."
    player_name "You just relax on your day off!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "You're sure?"
    show diane f_laying_smirk_up
    show player 429
    player_name "Positive!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Okay. Well, {b}the recipe is inside on a note pad next to the mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Got it!"
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_make_drink:
    $ randomdrink = M_diane.get("random drink")
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 427 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "What drink did you want again?"
    show player 426
    show diane f_laying_thinking
    dia "Hmm, a {b}[randomdrink]{/b} would be nice."
    show diane f_laying_smirk_up_talk
    dia "{b}The recipe is inside on a note pad next to the mixer.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "One {b}[randomdrink]{/b}, coming right up!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "What did you need me to do again?"
    show player 5
    show diane f_normal_talk
    dia "Just fetch me the {b}tool{/b} I left on the {b}kitchen counter.{/b}"
    show diane f_normal
    show player 14
    player_name "Oh, right!"
    player_name "I'll be right back!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_diane_got_pump:
    scene garden
    show player 239_240 at left
    show diane at lright
    with dissolve
    pause
    show player 103 at Position (xoffset=38) with dissolve
    player_name "Is this what you needed?"
    show player 13
    show diane a_dressed_pump f_normal_talk
    with dissolve
    dia "Yup!"
    show diane f_normal
    show player 10
    player_name "What is this thing anyways?"
    show player 13
    show diane f_normal_talk
    dia "You've never seen a breast pump before?"
    show diane f_normal
    show player 10
    player_name "... No?"
    show player 12
    player_name "It's a pump?"
    show player 5
    dia "Mmmhmm."
    show player 10
    player_name "How does it work?"
    show player 5
    show diane f_explain
    dia "Hehe, well you put this end over the nipple and then press the lever here and it sucks the milk out of the teet and into this container."
    show diane f_normal
    show player 14
    player_name "Whoa!"
    show player 10
    player_name "... And it doesn't hurt the cow?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Hahaha!"
    dia "No, handsome."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "It feels really good!"
    show diane f_shamed_talk_smile
    dia "You know, for the uhh... Cow."
    show diane f_shamed
    show player 14
    player_name "Can I try milking the cow sometime?"
    show player 13
    show diane f_laugh
    dia "Haha, I don't think that's a good idea, handsome."
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "For now you just work on the garden, okay?"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 14
    player_name "... Okay."
    show player 13
    show diane f_smirk_talk
    dia "If you need me, I'll be in here."
    dia "Just knock first, got it?."
    show diane f_smirk
    show player 14
    player_name "Yeah, I've got it."
    show player 13
    show diane f_laugh
    dia "Hehe, thanks stud."
    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Where am I supposed to deliver this milk again?"
    show player 5
    show diane f_normal_talk
    dia "You need to take that order to {b}Tony{/b} down at {b}Tony's Pizzeria{/b}."
    show diane f_normal
    show player 14
    player_name "Oh yeah, I know that place!"
    player_name "Alright, I'll be back in a flash."
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane f_normal
    show player 640e at left
    with dissolve
    player_name "I made your delivery for you."
    show player 13
    show diane f_normal_talk a_dressed_money
    with dissolve
    dia "Oh, thank you so much {b}[firstname]{/b}!"
    show diane a_dressed_shovel with dissolve
    dia "Did {b}Tony{/b} say anything?"
    show diane f_normal
    show player 14
    player_name "Uh huh, he said the milk had really taken their pizzas to a whole new level!"
    show player 13
    show diane f_normal_talk
    dia "{b}*Gasp*{/b}"
    dia "So he liked it?!"
    show diane f_normal
    show player 14
    player_name "Heh, I'd say so."
    show player 17
    player_name "He wants to triple his next order!"
    show player 13
    show diane f_sad_talk
    dia "Triple?!"
    show diane f_surprised_front
    dia "Hmm..."
    show player 12
    player_name "Is that a problem?"
    show player 5
    show diane f_shamed_front_talk
    dia "Huh? Oh... Well, I'm not sure."
    dia "I've don't know if I can handle-"
    show diane f_surprised
    pause
    show diane f_smirk_talk
    dia "I mean, my cow..."
    dia "... I don't know if she can handle that much demand."
    show diane f_smirk
    show player 12
    player_name "Sounds like you might need to expand and get more cattle."
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_thinking_back
    dia "I'm defintely not ready for that yet."
    dia "I'll just have to push her harder and start stockpiling..."
    show diane f_normal
    show player 14
    player_name "Can I do anything to help?"
    show player 13
    show diane f_normal_talk
    dia "Heh, no that's alright."
    dia "You've helped me plenty already."
    show diane f_normal
    player_name "..."
    show diane f_normal_talk
    dia "Why don't you get back to your garden work?"
    show diane f_normal
    show player 14
    player_name "Yeah, okay..."
    show player 13f with dissolve
    show diane f_teasing
    dia "Oh!"
    show diane f_normal
    show player 13 with dissolve
    show diane f_normal_talk
    dia "... I almost forgot."
    show diane a_dressed_money with dissolve
    dia "This is yours."
    show diane f_normal a_dressed_shovel
    show player 640c
    with dissolve
    player_name "Huh? This is the entire payment from the delivery!"
    show player 640b
    show diane f_normal_talk
    dia "Hehe, I told you, {b}[firstname]{/b}. This isn't a money making endeavor for me."
    show diane f_smirk_talk
    dia "At least not for the moment."
    show diane f_smirk
    player_name "..."
    show diane f_normal_talk
    dia "You take it and put it towards your tuition."
    show diane f_normal
    show player 14 with dissolve
    player_name "Thanks, {b}Diane{/b}!"
    show player 13
    show diane f_laugh
    dia "You're welcome, handsome!"
    hide player
    show diane kiss
    with dissolve
    pause
    hide diane with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "I should probably get started on the garden."
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "Thanks again for helping!"
    show diane f_normal
    show player 14
    player_name "No problem."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_leave:
    show player 14 at left
    show diane f_normal
    player_name "I'd better get back to it."
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "If you need anything, you know where to find me."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_naked_sides at lright
    with dissolve
    player_name "What was I supposed to do again?"
    show player 13
    show diane f_normal_talk
    dia "{b}Take the package of milk from my shed and deliver it to the cafeteria at your school.{b}"
    show diane f_normal
    show player 14
    player_name "Oh, right."
    player_name "I'm on it!"
    hide player
    hide diane
    with dissolve
    return
















































































































































































































































































label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} said she gave the old paint in the garage."
    player_name "You still have it right?"
    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_naked_sides f_laugh
    dia "Well, sure I do!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 13
    if L_diane_garden.is_here(M_diane):
        show diane f_normal_talk
    else:
        show diane b_naked a_naked_sides f_normal_talk
    dia "There should be some left in the shed."
    dia "Help yourself!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 14
    player_name "Thanks!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
