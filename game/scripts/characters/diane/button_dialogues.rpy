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
    player_name "Так чем ты занималась последние несколько лет?"
    show player 13
    show diane f_normal_talk
    dia " О, не так уж и многим на самом деле..."
    show diane f_normal
    show player 14
    player_name "Не многим?!"
    player_name "Я думал, ты там веселишься как сумасшедшая и тебя преследуют богачи?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Ха-ха, боже, нет!"
    dia "Что навело тебя на эту мысль?"
    show diane f_normal a_dressed_shovel with dissolve
    show player 14
    player_name "Ну, {b}[deb_name]{/b} всегда говорит, что ты дикая."
    show player 13
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Ну, возможно, в молодости..."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Честно говоря, после развода я большую часть времени провожу здесь, в этом саду."
    show diane f_normal
    show player 14
    player_name "Ты имеешь в виду, ты больше не выходишь на улицу?"
    show player 13
    show diane f_normal_talk
    dia "Иногда я хожу выпить со своей подругой {b}Вероникой{/b}."
    dia "Ничего особенного."
    show diane f_normal
    show player 14
    player_name "Разве ты не скучаешь по этому?"
    show player 13
    show diane f_normal_talk
    dia "Хмм, иногда."
    dia "Я слишком стара для такой жизни."
    show diane f_smirk_talk
    dia "Кроме того, в этом городе не осталось хороших мужчин."
    show diane f_smirk
    show player 12
    player_name "Правда?!"
    show player 13
    show diane f_laugh
    dia "Хе, поверь мне."
    show diane f_smirk_talk
    dia "В моем возрасте остались только отбросы."
    show diane f_smirk
    show player 10
    player_name "Облом."
    show player 5
    return

label dianes_dialogue_intro_d1_d6:
    show player 13 at left
    show diane f_normal_talk
    with dissolve
    dia "Приветик, {b}[firstname]{/b}!"
    dia "Я так рада, что ты решила прийти и помочь мне."
    show diane f_normal
    show player 14
    player_name "Да, это не проблема {b}Диана{/b}."
    player_name "Спасибо, что платите мне!"
    show player 13
    show diane f_laugh
    dia "Хе-хе, с удовольствием, красавчик."
    show diane f_normal
    return

label dianes_dialogue_intro_d7_d12:
    show player 5 at left
    show diane f_tired_talk b_naked a_magic_dressed_shovel_shirtless_sides
    with dissolve
    dia "Привет, {b}[firstname]{/b}."
    dia "Мой сад выглядит действительно-"
    dia "*зевая*"
    dia "... действительно круто."
    show diane f_tired
    show player 10
    player_name "Ты в порядке, {b}Диана{/b}?"
    show player 5
    show diane f_tired_talk
    dia "Да, я в порядке."
    dia "Только устала."
    show diane f_tired
    return

label dianes_dialogue_intro_d12b_d15:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    dia "Привет, красавчик!"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Тебе что-нибудь нужно?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_barn:
    show player 13 at left
    show diane f_normal_talk b_shirtless a_shirtless_sides
    with dissolve
    dia "Привет, жеребец!"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ты готов к работе?"
    show diane f_normal
    return

label dianes_dialogue_intro_d16_d18_couch:
    show player 13 at left
    show diane f_normal_talk b_nightgown a_nightgown_sides
    with dissolve
    dia "Привет, жеребец!"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ты собираешься спать?"
    show diane f_normal
    show player 14
    player_name "Да, через пару минут."
    show player 13
    return

label dianes_dialogue_intro_d19_d20_barn:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Привет, жеребец!"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ты готов к работе?"
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
    dia "Привет, жеребец!"
    show diane f_smirk
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Ты ищешь меня или {b}[deb_name]{/b}?"
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
    dia "Хмм, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Привет, {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Все в порядке?"
    show diane f_normal
    return

label dianes_dialogue_ready_to_pump:
    show player 14 at left
    if M_diane.between_states(S_diane_barn_news, S_diane_return_outfit_package):
        $ M_diane.outfit = "shirtless"
    show diane f_normal b_naked a_naked_sides
    with dissolve
    player_name "Ты готова к откачке?"
    show player 13
    show diane f_normal_talk
    dia "Абсолютно."
    dia "Дай мне одну секунду, чтобы подготовиться."
    hide diane with dissolve
    show player 14
    player_name "Хорошо."
    return

label dianes_dialogue_hows_the_baby_pregnancy_1:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "О, пока не о чем особо рассказывать."
    dia "Если только ты не хочешь услышать о моей утренней тошноте?"
    show diane f_normal
    show player 10
    player_name "Ну, если ты хочешь поговорить об этом, то можно?"
    show player 13
    show diane f_laugh
    dia "Хаха, о боже, нет!"
    show diane f_normal_talk
    dia "Я ценю, что ты интересуешься."
    dia "Спасибо, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_2:
    show player 13 at left
    show diane b_naked a_naked_sides f_normal_talk
    with dissolve
    dia "О, пока не о чем особо рассказывать."
    dia "Если только ты не хочешь услышать о моей утренней тошноте?"
    show diane f_normal
    show player 10
    player_name "Ну, если ты хочешь поговорить об этом, то можно?"
    show player 13
    show diane f_laugh
    dia "Хаха, о боже, нет!"
    show diane f_normal_talk
    dia "Я ценю, что ты интересуешься."
    dia "Спасибо, {b}[firstname]{/b}."
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_3:
    show player 13 at left
    show diane f_normal_talk b_naked a_naked_sides
    with dissolve
    dia "Хе, у меня сиськи так распухли!"
    dia "Они кажутся тебе больше?"
    show diane f_normal
    show player 26
    player_name "Я не знаю, они были довольно большими с самого начала..."
    show player 18
    show diane f_normal_talk
    dia "О, да ладно!"
    show player 13
    dia "Они определенно стали больше!"
    show diane f_normal
    pause
    show player 14
    player_name "Я просто люблю твою маленькую крошку!"
    show player 13
    if not M_diane.outfit == "nightgown":
        show diane f_laugh a_touch_belly with dissolve
    else:
        show diane f_laugh
    dia "Хехе, я знаю!"
    show diane f_normal_talk
    dia "Разве это не восхитительно?"
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Спасибо за регистрацию со мной, {b}[firstname]{/b}."
    show diane f_normal
    show player 14
    player_name "Конечно."
    player_name "Я не могу дождаться встречи с нашим ребенком, {b}Диана{/b}!"
    show player 13
    show diane f_normal_talk
    dia "Ауу, ты самый милый мужчина на свете!"
    show diane f_normal
    return

label dianes_dialogue_hows_the_baby_pregnancy_4:
    show player 13 at left
    if not M_diane.outfit == "nightgown":
        show diane f_tired_talk b_naked a_touch_belly
    else:
        show diane f_tired_talk b_naked a_naked_sides
    with dissolve
    dia "Фу, я очень устала..."
    show player 5
    dia "Мои ноги убивают меня, я выгляжу как кит, и мои сиськи никогда не перестают течь!"
    show diane f_tired
    show player 10
    player_name "... Ох."
    show player 5
    show diane f_laugh
    dia "Хе-хе, но все в порядке."
    show diane f_normal_talk
    dia "Я очень скоро стану мамой!"
    show diane f_normal
    show player 14
    player_name "Это верно, скоро!"
    show player 13
    show diane f_normal_talk
    dia "Я так рада, {b}[firstname]{/b}!"
    dia "Я не могу дождаться, чтобы подержать нашего ребенка на руках!"
    show diane f_normal
    show player 14
    player_name "Да, я тоже."
    show player 13
    return

label dianes_dialogue_breeding_session:
    show player 13 at left
    show diane b_naked a_naked_sides f_smirk_talk
    with dissolve
    dia "Ты готов приступить к работе?"
    show diane f_smirk
    show player 14
    player_name "Конечно."
    show player 13
    show diane f_smirk_talk
    dia "Слава богу!"
    dia "Я так промокла от одной мысли о том, что твой большой член засунул в меня ребенка..."
    show diane f_smirk
    show player 10
    player_name "Ты..?!"
    hide player
    show diane b_pull_mc_naked f_empty a_empty
    with dissolve
    dia "Ммм, мне это так нужно, {b}[firstname]{/b}!"
    hide diane
    with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed_mc
    show diane_sex_breed pre_talk
    with dissolve
    dia "Вот и все, жеребец."
    dia "Дай его мне."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "Ахх!!"
    return

label dianes_dialogue_cow_suit:
    show player 14 at left
    show diane f_normal b_naked a_naked_sides
    player_name "Я хотел поговорить с тобой о твоем коровьем наряде..."
    show player 13
    show diane f_normal_talk
    dia "Ох?"
    show diane f_normal
    menu:
        "Надень его." if M_diane.is_naked:
            show player 14 at left
            show diane f_normal
            player_name "Я хочу, чтобы ты носила его, пока я тебя трахаю."
            player_name "Он такой сексуальный!"
            show player 13
            show diane f_laugh
            dia "О, я так счастлива, что ты так думаешь!"
            show diane f_normal_talk
            dia "Я тоже его люблю!"
            show diane f_smirk_talk
            dia "Это просто кажется правильным, понимаешь?"
            dia "Носить его здесь."
            show diane f_smirk
            show player 14
            player_name "Да, конечно."
            hide diane
            with dissolve
            $ M_diane.is_naked = 0
            $ M_diane.outfit = "cow"

        "Можешь его снять?" if not M_diane.is_naked:
            show player 14 at left
            show diane f_normal
            player_name "Я бы предпочел, чтобы ты была полностью голой."
            show player 13
            show diane f_smirk_talk
            dia "Ты бы хотел?!"
            dia "Ммм, ты непослушный мальчик..."
            show diane f_smirk
            pause
            show diane f_smirk_talk
            dia "Я могу снять его, если ты действительно этого хочешь."
            dia "Все, что поможет тебе засунуть ребенка мне в живот."
            hide diane
            with dissolve
            $ M_diane.is_naked = 1
    return

label dianes_dialogue_dump_pump:
    scene garden
    show player 10 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "Что мне нужно делать?"
    show player 13
    show diane f_normal_talk
    dia "Хмм?"
    dia "О, {b}просто зайдите в сарай и вылейте то, что находится в насосе, в кувшин для хранения.{/b}"
    show diane f_normal
    show player 14
    player_name "Верно!"
    player_name "Бегу!"
    hide player
    hide diane with dissolve
    return

label dianes_dialogue_daylight_drinking:
    scene expression "backgrounds/location_diane_garden_close_day_blur.jpg"
    show player 429 zorder 0 at Position (xpos=175,ypos=648)
    show diane_chair up
    show diane b_laying_back_shirtless a_laydown f_laying_smirk_up at Position (ypos=982)
    with dissolve
    player_name "Как ты здесь поживаешь?"
    show player 426
    show diane f_laying_laugh
    dia "Ммм, фантастика!"
    show diane f_laying_smirk_up
    show player 429
    player_name "Принести вам что-нибудь?"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Я бы не отказался от выпивки."
    show diane f_laying_smirk_up
    show player 429
    player_name "Твое желание-мой приказ!"
    player_name "Какой напиток ты хочешь?"
    show player 426
    $ randomdrink = M_diane.get("random drink")
    show diane f_laying_thinking
    dia "Как насчет {b}[randomdrink]{/b}?"
    show diane f_laying_smirk_up
    show player 427
    player_name "{b}[randomdrink]{/b}?!"
    player_name "Я никогда не делал ничего подобного раньше..."
    show player 426
    show diane f_laying_laugh
    dia "Хе-хе, не беспокойся. Я сделаю это."
    show diane f_laying_smirk_up
    show player 429
    player_name "Нет! Я могу с этим разобраться."
    player_name "Просто расслабься в свой выходной!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Ты уверен?"
    show diane f_laying_smirk_up
    show player 429
    player_name "Несомненно!"
    show player 426
    show diane f_laying_smirk_up_talk
    dia "Хорошо. Ну, {b}рецепт находится внутри на блокноте рядом с миксером.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Ясно!"
    player_name "Один {b}[randomdrink]{/b}, сейчас будет!"
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
    player_name "Еще раз, что ты хочешь выпить?"
    show player 426
    show diane f_laying_thinking
    dia "Хмм, {b}[randomdrink]{/b} был бы неплохо."
    show diane f_laying_smirk_up_talk
    dia "{b}Рецепт находится внутри на блокноте рядом с миксером.{/b}"
    show diane f_laying_smirk_up
    show player 429
    player_name "Один {b}[randomdrink]{/b}, сейчас будет!"
    hide player
    hide diane
    hide diane_chair
    with dissolve
    return

label dianes_dialogue_diane_fetch_pump:
    show player 10 at left
    show diane f_normal
    with dissolve
    player_name "Что тебе нужно, чтобы я снова сделал?"
    show player 5
    show diane f_normal_talk
    dia "Просто принесите мне {b}инструмент{/b}, который я оставила на {b}кухонном столе.{/b}"
    show diane f_normal
    show player 14
    player_name "Хорошо!"
    player_name "Щас принесу!"
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
    player_name "Это то, что тебе нужно?"
    show player 13
    show diane a_dressed_pump f_normal_talk
    with dissolve
    dia "Ага!"
    show diane f_normal
    show player 10
    player_name "Что это за штука?"
    show player 13
    show diane f_normal_talk
    dia "Ты никогда раньше не видел молокоотсос?"
    show diane f_normal
    show player 10
    player_name "... Нет?"
    show player 12
    player_name "Это насос?"
    show player 5
    dia "Мммммм."
    show player 10
    player_name "Как он работает?"
    show player 5
    show diane f_explain
    dia "Хе-хе, хорошо, вы кладете этот конец поверх соска, а затем нажимаете рычаг, и он высасывает молоко в этот контейнер."
    show diane f_normal
    show player 14
    player_name "Вау!"
    show player 10
    player_name "... И корове это не повредит?"
    show player 13
    show diane f_laugh a_dressed_blush with dissolve
    dia "Хахаха!"
    dia "Нет, красавчик."
    show diane f_normal_talk a_dressed_shovel with dissolve
    dia "Это действительно здорово!"
    show diane f_shamed_talk_smile
    dia "Ну, знаешь, для эээ ... .. Коровы."
    show diane f_shamed
    show player 14
    player_name "Могу я как-нибудь попробовать подоить корову?"
    show player 13
    show diane f_laugh
    dia "Ха-ха, Не думаю, что это хорошая идея, красавчик."
    show diane f_smirk_talk a_dressed_finger with dissolve
    dia "Пока ты просто работаешь в саду, хорошо?"
    show diane f_smirk a_dressed_shovel with dissolve
    show player 14
    player_name "... Хорошо."
    show player 13
    show diane f_smirk_talk
    dia "Если понадоблюсь, я буду здесь."
    dia "Просто постучи сначала, понял?"
    show diane f_smirk
    show player 14
    player_name "Да, я понял."
    show player 13
    show diane f_laugh
    dia "Хехе, спасибо, жеребец."
    hide player
    hide diane
    with dissolve
    return


label dianes_dialogue_delivery_1_reminder:
    scene garden
    show player 10 at left
    show diane
    with dissolve
    player_name "Куда я должен снова доставить это молоко?"
    show player 5
    show diane f_normal_talk
    dia "Тебе нужно доставить этот заказ {b}Тони{/b} в {b}пиццерию Тони{/b}."
    show diane f_normal
    show player 14
    player_name "О да, я знаю это место!"
    player_name "Хорошо, я вернусь в мгновение ока."
    show player 13
    show diane f_normal_talk
    dia "Спасибо, {b}[firstname]{/b}!"
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_delivery_1_done:
    scene garden
    show diane f_normal
    show player 640e at left
    with dissolve
    player_name "Я выполнил доставку."
    show player 13
    show diane f_normal_talk a_dressed_money
    with dissolve
    dia "О, спасибо большое {b}[firstname]{/b}!"
    show diane a_dressed_shovel with dissolve
    dia "{b}Тони{/b} что-нибудь сказал?"
    show diane f_normal
    show player 14
    player_name "Ага, он сказал, что молоко действительно подняло их пиццу на совершенно новый уровень!"
    show player 13
    show diane f_normal_talk
    dia "{b}*вздох*{/b}"
    dia "Так ему понравилось ?!"
    show diane f_normal
    show player 14
    player_name "Хех, я бы так сказал."
    show player 17
    player_name "Он хочет утроить свой следующий заказ!"
    show player 13
    show diane f_sad_talk
    dia "Утроить?!"
    show diane f_surprised_front
    dia "Хмм..."
    show player 12
    player_name "Это проблема?"
    show player 5
    show diane f_shamed_front_talk
    dia "Хух? О... Ну, я не уверена."
    dia "Я не знаю, смогу ли я справиться-"
    show diane f_surprised
    pause
    show diane f_smirk_talk
    dia "Я имею в виду, моя коровка..."
    dia "... Не знаю, справится ли она с таким спросом."
    show diane f_smirk
    show player 12
    player_name "Похоже, тебе нужно расширить сарай и получить больше скота."
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_thinking_back
    dia "Я определенно еще не готова к этому."
    dia "Мне просто придется надавить на нее сильнее и начать накапливать запасы..."
    show diane f_normal
    show player 14
    player_name "Могу я чем-нибудь помочь?"
    show player 13
    show diane f_normal_talk
    dia "Хех, нет, все в порядке."
    dia "Ты мне уже очень помог."
    show diane f_normal
    player_name "..."
    show diane f_normal_talk
    dia "Почему бы тебе не вернуться к работе в саду?"
    show diane f_normal
    show player 14
    player_name "Да, хорошо..."
    show player 13f with dissolve
    show diane f_teasing
    dia "О!"
    show diane f_normal
    show player 13 with dissolve
    show diane f_normal_talk
    dia "... Чуть не забыла."
    show diane a_dressed_money with dissolve
    dia "Это твое."
    show diane f_normal a_dressed_shovel
    show player 640c
    with dissolve
    player_name "А? Это вся оплата с момента доставки!"
    show player 640b
    show diane f_normal_talk
    dia "Хе-хе, я же говорила, {b}[firstname]{/b}. Это не попытка заработать деньги для меня."
    show diane f_smirk_talk
    dia "По крайней мере, не сейчас."
    show diane f_smirk
    player_name "..."
    show diane f_normal_talk
    dia "Возьми их и вложи в свое обучение."
    show diane f_normal
    show player 14 with dissolve
    player_name "Спасибо, {b}Диана{/b}!"
    show player 13
    show diane f_laugh
    dia "Пожалуйста, милый!"
    hide player
    show diane kiss
    with dissolve
    pause
    hide diane with dissolve
    return

label dianes_dialogue_leave_d1:
    show player 14 at left
    show diane f_normal
    player_name "Наверное, мне стоит начать с сада."
    show player 13
    show diane f_normal_talk
    dia "Хорошо."
    dia "Спасибо еще раз за помощь!"
    show diane f_normal
    show player 14
    player_name "Без проблем."
    hide player
    hide diane
    with dissolve
    return

label dianes_dialogue_leave:
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

label dianes_dialogue_delivery_3_reminder:
    show player 10 at left
    show diane b_naked a_naked_sides at lright
    with dissolve
    player_name "Что я должен был сделать, еще раз?"
    show player 13
    show diane f_normal_talk
    dia "{b}Возьми пакет молока из моего сарая и отнеси его в кафетерий своей школы.{b}"
    show diane f_normal
    show player 14
    player_name "Ах, да."
    player_name "Бегу!"
    hide player
    hide diane
    with dissolve
    return
















































































































































































































































































label dianes_dialogue_pre_fun_paint:
    show player 10
    player_name "{b}[deb_name]{/b} сказала, что дала старую краску из гаража."
    player_name "Она еще у тебя?"
    show player 5
    if L_diane_garden.is_here(M_diane):
        show diane f_laugh
    else:
        show diane b_naked a_naked_sides f_laugh
    dia "Ну, конечно!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 13
    if L_diane_garden.is_here(M_diane):
        show diane f_normal_talk
    else:
        show diane b_naked a_naked_sides f_normal_talk
    dia "Там должно быть немного осталось в сарае."
    dia "Забирай!"
    if L_diane_garden.is_here(M_diane):
        show diane f_normal
    else:
        show diane b_naked a_naked_sides f_normal
    show player 14
    player_name "Спасибо!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
