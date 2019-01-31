label entrance_diane_gave_birth_dialogue_seen:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 10 at left
    show debbie 1f at Position (xpos=600)
    show diane a_casual_baby b_casual at Position (xpos=625)
    show jenny f_grin at flip
    show jenny at Position (xpos=150)
    with dissolve
    player_name "{b}Диана{/b}?"
    show player 14
    player_name "Вы наконец-то дома?"
    show player 13
    show diane f_normal_talk
    dia "Да, мы вернулись домой."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Разве он не самая драгоценная вещь на свете?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Не знаю, он похож на картофелину..."
        show jenny f_normal
        show debbie 2f
        deb "Нет, это не так!"
        deb "Он такой красивый!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Кто у нас красивый мальчик, а?"
    else:
        deb "Разве она не самая драгоценная вещь на свете?!"
        show debbie 1f
        show jenny f_normal_talk
        jen "Не знаю, она похожа на картофелину..."
        show jenny f_normal
        show debbie 2f
        deb "Нет, это не так!"
        deb "Она прекрасна!"
        show debbie 1f
        pause
        show debbie 2f
        deb "Кто у нас красивая девочка, а?"
    show debbie 1f
    show diane f_laugh
    dia "Хехе!"
    show diane f_normal
    show debbie 2f
    deb "Не могу поверить, что у тебя наконец-то есть ребенок, {b}Диана{/b}."
    deb "Я так счастлива за тебя!"
    show debbie 1f
    show diane f_normal_talk
    dia "Я знаю, я не думала, что когда-нибудь стану мамой."
    show diane f_normal
    show debbie 2f
    show diane f_down_front
    if M_diane.pregnancy.baby_gender == "boy":
        deb "Он такой очаровательный..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Я могу просто слопать его!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Мне действительно нужно уложить его спать."
        dia "У него был напряженный день."
    else:
        deb "Она такая очаровательная..."
        show jenny f_eyeroll
        show debbie 3f
        deb "Я могу просто слопать ее!"
        show debbie 1f
        show jenny f_normal
        pause
        show diane f_normal_talk
        dia "Мне действительно нужно уложить ее спать."
        dia "У нее был напряженный день."
    show diane f_down_front
    show debbie 2f
    deb "Ау, хорошо..."
    deb "Пока пока, малыш."
    show debbie 1f
    pause
    show debbie 1 at right
    show jenny at Position (xpos=200)
    hide diane
    with dissolve
    pause
    show debbie 3
    deb "О, я просто обожаю детей!"
    show debbie 1
    show jenny f_eyeroll
    jen "Уф, неважно."
    show jenny f_upset_talk
    jen "Если эта штука всю ночь будет кричать, Я просто сорвусь!"
    show jenny f_upset
    show debbie 13
    deb "{b}*вздыхая*{/b}, {b}[jen_name]{/b}..."
    deb "Не будь такой, дорогая."
    show debbie 14b
    show jenny f_normal_talk
    jen "Я просто говорю, что мне нужны мои восемь часов для сна или я разозлюсь."
    show jenny f_normal
    show player 12
    player_name "Ты всегда капризничаешь..."
    show player 13 with None
    show jenny f_upset_talk at unflip
    show jenny at Position (xpos=-200)
    with dissolve
    jen "Что ты сказал?!"
    show jenny f_gross
    show player 10
    player_name "Ничего."
    show player 5
    pause
    show jenny f_upset_talk
    jen "Угу."
    show jenny f_upset
    pause
    show jenny f_upset_talk
    jen "Лучше следи за своим языком."
    jen "Я знаю, где ты спишь."
    hide jenny with dissolve
    pause
    show player 12
    player_name "Она как солнечный лучик..."
    show player 13
    show debbie 3
    deb "Хехехе!"
    show debbie 2
    deb "Не обращайте на нее внимания."
    deb "Она тоже любит детей, просто не хочет этого признавать."
    show debbie 1
    show player 12
    player_name "Как скажешь."
    hide player
    hide debbie
    hide diane
    with dissolve
    return

label entrance_diane_peeking:
    scene expression "backgrounds/location_home_entrance_night_blur.jpg"
    show player 34 with dissolve
    pause
    show player 35
    player_name "Хм, сегодня здесь тихо ..."
    show player 10
    player_name "Интересно, что {b}[deb_name]{/b} и {b}Даина{/b} делают."
    show player 14
    player_name "{b}Они обычно в гостиной{/b} смотрят телевизор и болтают."
    player_name "{b}Я должен проверить их.{/b}"
    hide player with dissolve
    return

label entrance_diane_couch_crashing:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh zorder 1 at Position (xpos=625)
    with dissolve
    dia "Дорогая, мы вернулись домой!"
    dia "Хаха!"
    show player 17
    player_name "Хаха!"
    show diane f_normal
    show debbie 2f zorder 0 with dissolve
    deb "Что, черт возьми, происходит-"
    show debbie 3f
    show player 13
    deb "{b}*вздох*{/b} Ты здесь!"
    show debbie 2f
    show diane f_normal_talk
    dia "Я здесь!!"
    show diane f_normal_talk a_casual_bag_point with dissolve
    dia "Мы начинаем с пижамной вечеринки?"
    show diane f_normal a_casual_bag
    show debbie 222f
    with dissolve
    deb "Ааа?"
    pause
    show debbie 3f with dissolve
    deb "О, да ладно."
    show debbie 1f
    show diane f_normal_talk
    dia "Я серьезно, я принесла свою ночную рубашку и все такое!"
    show diane f_normal
    show debbie 2f
    deb "Ты голодная?"
    show debbie 1f
    show diane f_normal_talk
    dia "О, обслуживание номеров и все такое."
    show diane f_smirk_talk
    dia "Ты не говорила мне, что это будет так чудно..."
    show diane f_smirk
    show debbie 2f
    deb "Просто иди сюда, Я помогу тебе распаковать вещи."
    show debbie 1f
    show diane f_laugh
    dia "Да, мэм."
    show diane f_normal_talk
    dia "Ты хочешь присоединиться к нам, {b}[firstname]{/b}?"
    show debbie 1 with dissolve
    show diane f_normal
    show player 55 with dissolve
    player_name "{b}*зевая*{/b}"
    show player 26 with dissolve
    player_name "... Конечно!"
    show player 25
    show debbie 2
    deb "Милый, ты выглядишь уставшей!"
    deb "Почему бы тебе просто не пойти в кровать и позволить нам с {b}Дианой{/b} провести некоторое время вместе."
    show diane f_wink
    show debbie 1f with dissolve
    pause
    show diane f_smirk_talk
    dia "Ммм, время вместе, хух?"
    show diane f_smirk
    show debbie 3f
    deb "О, тише!"
    show diane f_laugh
    dia "Хаха."
    show diane f_normal
    show debbie 1 with dissolve
    show player 26
    player_name "Да, хорошо."
    player_name "Я довольно сильно устал."
    show player 25
    show diane f_smirk_talk
    dia "Думаю, тогда остались только ты и я, красавица."
    show diane f_smirk
    show debbie 3f with dissolve
    deb "Хе-хе, прекрати!"
    show debbie 1f
    show diane f_smirk_talk
    dia "Спокойной ночи, {b}[firstname]{/b}."
    show player 55
    hide debbie
    hide diane
    with dissolve
    pause
    hide player with dissolve
    return

label entrance_diane_debbie_drop_off_request:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 13 at left
    show debbie 221 at right
    with dissolve
    deb "Подожди, {b}[firstname]{/b}."
    show debbie 220
    show player 14
    player_name "Привет, {b}[deb_name]{/b}."
    player_name "Что случилось?"
    show player 13
    show debbie 221
    deb "Ты сегодня работал у {b}Дианы{/b}?"
    show debbie 220
    show player 14
    player_name "Да, я уже был там."
    show player 13
    show debbie 221
    deb "С ней все в порядке?"
    show debbie 220
    show player 5
    player_name "Хмм?"
    show player 10
    player_name "Да, наверное..."
    show player 5
    show debbie 221
    deb "... Потому что я только что говорила с ней по телефону, и она кажется измученной."
    show debbie 220
    show player 10
    player_name "Ну, она очень усердно работает над своим новым бизнесом."
    player_name "Я сказал ей притормозить, но ты же знаешь, как она страстно к этому относится."
    show player 5
    show debbie 221
    deb "Да, у нее есть склонность бросаться на работу и игнорировать свои потребности."
    deb "Это меня беспокоит."
    deb "Мог бы ты вернуться туда?"
    show debbie 220
    show player 10
    player_name "Сегодня вечером?"
    show player 5
    show debbie 221
    deb "Да, я хочу, чтобы ты взял пирог, который я сегодня испекла, и убедился, что она его съест!"
    deb "Она, наверное, ничего не ела весь день."
    show debbie 220
    show player 14
    player_name "Да, я могу это сделать."
    show player 13
    show debbie 221
    deb "Я была бы очень признательна."
    show debbie 2
    show player 673
    with dissolve
    deb "Скажи ей, что ей тоже лучше поспать восемь часов, иначе я приду к ней в гости!"
    show debbie 1
    show player 674
    player_name "Хех, хорошо."
    hide debbie
    hide player
    with dissolve
    return

label entrance_erik_bullying:
    scene expression L_home_entrance.background
    show mrsj 19c at right with dissolve
    show player 10 at left with dissolve
    player_name "Все хорошо, {b}Миссис Джонсон{/b}?"
    show player 5
    show mrsj 19
    mrsjo "Извени что беспокою тебя утром."
    show mrsj 52
    mrsjo "Просто...это насчет {b}Эрика{/b}."
    mrsjo "У {b}Эрика{/b} были проблемы в последнее время в школе?"
    show mrsj 19c
    show player 12
    player_name "Эээ?"
    show player 35
    player_name "Насколько мне известно, нет."
    show player 10
    player_name "Он обычно хорошо учится в школе..."
    show player 5
    show mrsj 20
    mrsjo "Нет. Я не говорю об уроках."
    show mrsj 52
    mrsjo "Другие дети в школе доставляли {b}Эрикe{/b} много хлопот?"
    mrsjo "Он попросил остаться дома вместо того, чтобы идти на занятия."
    show mrsj 20
    mrsjo "Я... Я даже видела, как он пришел домой на прошлой неделе с синяками."
    show mrsj 19c
    show player 23
    player_name "!!!" with hpunch
    show player 12
    player_name "{b}Эрик{/b} ведет себя в школе довольно тихо."
    player_name "Я никогда не видел, чтобы он участвовал в каких-то плохих делах."
    show player 5
    show mrsj 19
    mrsjo "Может быть, если бы близкий друг спросил его, он был бы готов поговорить..."
    show mrsj 19c
    show player 10
    player_name "Вы хотите, чтобы я спросил его?"
    show player 5
    show mrsj 19
    mrsjo "Я просто хочу, лучшего для него, а ты его единственный друг."
    show mrsj 19c
    show player 12
    player_name "Хорошо. Пойду спрошу у него."
    hide mrsj
    hide player
    with dissolve
    return

label entrance_erik_bullying_3:
    scene expression L_home_entrance.background
    show mrsj 19c at Position (xpos=700)
    show debbie 13 at right
    with dissolve
    show player 5 at left with dissolve
    deb "Милый!! Ты в порядке?!"
    show debbie 14b
    show player 10
    player_name "Я в норме, {b}[deb_name]{/b}. Медсестра сказала, что у меня было небольшое сотрясение мозга."
    show player 11
    show debbie 13
    deb "Сотрясение!"
    show debbie 14b
    show player 10
    player_name "Все отлично. Я буду в порядке, {b}[deb_name]{/b}."
    show player 5
    show debbie 13
    deb "Твоя глупая школа даже не позвонила, чтобы сообщить, что ты в больнице!"
    deb "Я узнала об этом от {b}Тэмми{/b}!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}, все в порядке. Я в порядке! Успокойся."
    show player 11
    show debbie 13
    deb "Извини ... Я так волновался за тебя!"
    deb "Твой {b}отец{/b} просил присматривать за тобой!"
    show debbie 14b
    show mrsj 19
    mrsjo "Я так рада, что ты в порядке, {b}[firstname]{/b}."
    mrsjo "Я пришел сюда, чтобы рассказать {b}[deb_name]{/b} вскоре как {b}Эрик{/b} позвонил мне."
    mrsjo "Ты сделал хорошее дело, защищая {b}Эрика{/b}."
    show mrsj 38
    show debbie 13
    deb "Да, это было очень храбро с твоей стороны заступиться за своего друга в школе."
    deb "Но, пожалуйста, будь осторожен!"
    show debbie 14b
    show player 24
    player_name "Я понял {b}[deb_name]{/b}..."
    show player 25
    player_name "Я обещаю, что постараюсь держаться подальше от неприятностей."
    show player 24
    show debbie 13
    deb "Иди сюда."
    hide player
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at right
    show debbie 4
    with dissolve
    deb "Я так рада, что ты в безопасности."
    deb "{b}Твой отец{/b} закатит бы истерику, если узнал, что я позволил этому случиться."
    player_name "Все хорошо, {b}[deb_name]{/b}."
    hide debbie
    hide mrsj
    with dissolve
    show mrsj 14 at Position (xpos=700)
    show debbie 1 at right
    show player 13 at left
    with dissolve
    show mrsj 17
    mrsjo "Спасибо еще раз, {b}[firstname]{/b}."
    mrsjo "Ты всегда можешь приходить к нам."
    show mrsj 14
    show player 14
    player_name " Все нормально. Просто помогаю другу."
    show player 13
    show mrsj 17
    mrsjo "Спасибо."
    show mrsj 14
    show player 36 with dissolve
    player_name "Спокойной ночи, {b}Миссис Джонсон{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Спокойной ночи."
    hide mrsj with dissolve
    show debbie 2
    deb "А теперь поспеши в постель и отдохни."
    hide player
    hide debbie
    with dissolve
    return

label entrance_mia_angelicas_impatience:
    scene expression L_home_entrance.background
    show debbie 1f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3
    with dissolve
    deb "А вот и он!"
    show debbie 1
    show player 22
    player_name "!!!" with hpunch
    show debbie 2
    deb "Я так рад слышать, что {b}[firstname]{/b} недавно посетил нашу местную церковь..."
    deb "... И предложили волонтерскую работу с духовенством!"
    show debbie 1
    show player 24
    player_name "Ааа..."
    show debbie 2
    deb "Ну! Оставлю вас двоих, у меня есть дела на кухне!"
    show debbie 2f with dissolve
    deb "Было приятно познакомиться, {b}Сестра Анжелика{/b}!"
    hide debbie with dissolve
    show player 12
    player_name "Волонтерская работа?"
    player_name "И почему вы здесь?!"
    show player 11
    show ang 2
    ang "Я думала, мы договорились?"
    show ang 1
    show player 24
    player_name "..."
    show ang 2
    ang "Ты думаешь, что я просто позволю тебе ускользнуть от меня?!"
    show ang 1
    show player 10
    player_name "Нет, я только... Что вам нужно от меня?"
    show player 11
    show ang 2
    ang "Дверь церкви ночью останется незапертой."
    ang "Приходите ко мне в гости в мою палату, и я объясню, что мне нужно от тебя..."
    ang "...И не пытайся скрыть от меня, иначе-"
    show ang 1
    show player 12
    player_name "Хорошо, хорошо!"
    player_name "Только ничего не говори моей {b}хозяйке{/b}..."
    show player 11
    show ang 2
    ang "Это зависит от тебя..."
    hide ang with dissolve
    show player 12
    player_name "Теперь мне нужно увидеться с ней в церкви? Ночью?!"
    show player 10
    player_name "Это странно..."
    hide player with dissolve
    return

label entrance_mia_angelicas_home_visit:
    scene expression L_home_entrance.background with fade
    show debbie 2f at Position (xpos=500)
    show ang 1 at right
    with dissolve
    pause.5
    show player 5 at left
    show debbie 3f
    with dissolve
    deb "Всегда приятно слышать, что {b}[firstname]{/b} активно сотрудничает с церковью."
    deb "Вы двое, должно быть, хорошо друг друга узнали."
    show debbie 1f
    show ang 2
    ang "Да, {b}[firstname]{/b} был очень полезен, вызывая угрюмых грешников."
    ang "{b}Бог{/b} непременно вспомнит о своих плодах любви к ближним."
    show ang 1
    show debbie 3f
    deb "Это же здорово!"
    deb "Я знаю, что мы все можем быть непослушными время от времени..."
    show debbie 2f
    deb "Что ж, мне лучше поторопиться. Стирка сама себя не постирает."
    hide debbie with dissolve
    show ang 3
    player_name "..."
    show player 30
    player_name "Что сейчас?"
    player_name "Я привел к вам {b}Хелен{/b}. Разве этого недостаточно?"
    show player 5
    show ang 4
    ang "О, нет, дорогой ребенок. {b}У Бога{/b} есть много вещей для вас."
    ang "{b}Хелен{/b} далеко не очищенна. Ее упрямство раздражает."
    show ang 3
    show player 26
    player_name "Расскажи мне об этом."
    show player 5
    show ang 2
    ang "Самые кающиеся христиане нуждаются в особой заботе."
    ang "Их нужно сбросить с пьедестала, чтобы мы могли его восстановить."
    ang "Думаю, для нее потребуется еще два ритуала..."
    ang "Вот почему я пришела повидаться с тобой."
    ang "Я нуждаюсь в инструменте, используемом на протяжении многих библейских времен."
    show ang 1
    show player 11
    player_name "..."
    show player 12
    player_name "Что вам нужно?"
    show player 5
    show ang 2
    ang "Я намерена подорвать {b}Хелен{/b} с помощью бичевания."
    show ang 1
    show player 12
    player_name "Что?"
    show player 5
    show ang 4
    ang "Принеси мне {b}плетку{/b}."
    show ang 3
    show player 23
    player_name "{b}Плетку{/b}!?"
    show player 11
    show ang 4
    ang "Я бы предпочла плетку которой подвергся наш {b}Спаситель{/b}."
    ang "Но я боюсь, что ее будет трудно найти."
    ang "{b}Стандартной кожаной плетки{/b} хватит."
    show ang 2
    ang "Принеси ее мне в мои покои."
    show ang 1
    show player 10
    player_name "Это не кажется мне правильным-"
    show player 11
    show ang 2
    ang "Ты забыл, где твое место? Не заставляй меня напоминать тебе и всем остальным о твоих грехах!"
    show ang 1
    show player 15
    player_name "Но вы хотите выпороть {b}Хелен{/b}!"
    show player 16
    show ang 2
    ang "Ты заключил со мной сделку. Не сомневайтесь в моих... церковных методах."
    show ang 1
    show player 12
    player_name "Это просто не правильно."
    show player 5
    show ang 4
    ang "И кто ты такой, чтобы отличать хорошее от плохого?"
    show ang 3
    show player 24
    player_name "..."
    show player 12
    player_name "Хорошо. Где я вообще должен достать {b}плетку{/b}?"
    show player 17
    player_name "Есть ли список дистрибьюторов на задней странице Библии?"
    show player 5
    show ang 1
    ang "..."
    show ang 2
    ang "Я уверена, что кто-то из твоих друзей знает о грязных похотливых местах, которые продают такие вещи."
    ang "Не заставляй меня ждать."
    hide ang with dissolve
    show player 37 with dissolve
    player_name "Мне не следовало ходить в церковь."
    pause
    show player 38 with dissolve
    player_name "Куда пойти чтобы добыть {b}плетку{/b}?"
    player_name "Может в {b}магазине Pink в торговом центре{/b} торгуют чем-то похожим."
    show player 37 with dissolve
    player_name "..."
    hide player with dissolve
    return

label entrance_mia_angelicas_final_home_visit:
    scene expression L_home_entrance.background with fade
    show player 11 at left
    show ang 2 at right
    with dissolve
    ang "Самое время спуститься вниз."
    ang "Ты мне снова понадобился."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Я не уверен, что хочу продолжать помогать после того, что вы сделали с {b}Хелен{/b}, Я-"
    show player 5
    show ang 4
    ang "О, не будь таким наивным!"
    ang "Несмотря на ее нежелание, мы оба знаем, что ей понравилось."
    show ang 3
    show player 11
    player_name "..."
    show ang 2
    ang "Я пришла сюда не спорить с грешником."
    show ang 39 with dissolve
    ang "Если ты действительно хочешь помочь {b}Хелен{/b} ты поможешь мне получить это..."
    show ang 38
    pause
    show ang 3
    show player 459 at Position (xoffset=1)
    with dissolve
    player_name "..."
    hide player
    hide ang
    show note_01_c
    with dissolve
    pause
    hide note_01_c
    show player 1 at left
    show ang 3 at right
    show player 460 at Position (xoffset=1)
    with dissolve
    player_name "Что...ЭТО?"
    show player 461 at Position (xoffset=1)
    show ang 4
    ang "Это главный элемент для последнего этапа очистки {b}Хелен{/b} ..."
    ang "...И твое последнее задание."
    show ang 3
    show player 460 at Position (xoffset=1)
    player_name "Но как это будет использоваться для очистки {b}Хелен{/b}?"
    show player 11 with dissolve
    show ang 2
    ang "Не задавай мне вопросов!"
    ang "Грешники должны просто принять слова, сказанные избраниками {b}Бога{/b}."
    ang "А теперь принеси мне предмет с фотографии и встретимся в моем кабинете."
    show ang 1
    show player 5
    player_name "..."
    show player 12
    player_name "Хорошо..."
    show player 5
    show ang 2
    ang "Хорошо. Поторопись."
    hide ang with dissolve
    show player 5
    player_name "..."
    show player 10
    player_name "{b}Хелен{/b}  кажется, даже не понимает, что {b}Сестра Анжелика{/b} превращает её..."
    player_name "...в секс-рабыню!"
    show player 12
    player_name "Я должен поговорить с {b}Гарольд{/b} перед тем как помочь {b}Сестре Анжелике{/b}."
    player_name "Может, он поможет мне понять, что делать."
    show unlock55 at truecenter with dissolve
    $ player.get_item("strapon_drawing")
    pause
    hide unlock55 with dissolve
    hide player with dissolve
    return

label entrance_mom_overheard:
    scene expression game.timer.image("home_entrance{}")
    show player 34 with dissolve
    player_name "...{b}*отдаленный голос*{/b}..."
    show player 35
    player_name "( Это {b}[deb_name]{/b} по телефону? )"
    show player 12
    player_name "( ...Похоже, она сумасшедшая. Она кричит?)"
    show player 10
    player_name "( Пойду посмотрю, все ли с ней в порядке. )"
    hide player with dissolve
    return

label entrance_mom_lawn_help:
    scene expression L_home_entrance.background
    show player 1 at left
    show debbie 2 at right
    with dissolve
    if game.timer.is_morning():
        deb "Доброе утро, милый."
    else:
        deb "Привет, милый."
    show debbie 1
    show player 2
    if game.timer.is_morning():
        player_name "Доброе утро, {b}[deb_name]{/b}."
    else:
        player_name "Привет, {b}[deb_name]{/b}."
    show player 1
    show debbie 2
    if game.timer.is_morning():
        deb "Готов к школе?"
    else:
        deb "Счастлив вернуться в школу?"
    show debbie 1
    show player 10
    player_name "Да, наверное. У меня столько домашней работы, чтобы догнать."
    show player 1
    show debbie 3
    deb "О, я уверена, что все будет хорошо."
    show debbie 2
    deb "Хорошо вернуться в обычную рутину."
    show debbie 1
    show player 14
    player_name "Наверное."
    player_name "Что ты сегодня делаешь?"
    show player 13
    show debbie 13
    deb "Я?"
    deb "По дому в основном. Это заставляет меня быть очень занятой."
    deb "Нелегко заботиться об этом большом месте в одиночку."
    show debbie 14b
    show player 5
    pause
    show player 2
    player_name "Я могу помочь, понимаешь?"
    show player 1
    show debbie 13
    deb "Хочешь помочь по хозяйству?"
    show debbie 1
    show player 29 with dissolve
    player_name "Конечно! Я имею в виду, я чувствую, что я должен внести свой вклад..."
    show player 1 with dissolve
    show debbie 2
    deb "Это отлично, {b}[firstname]{/b}!"
    show debbie 1
    deb "Хмм..."
    show debbie 2
    deb "Ну, газон не косили уже несколько недель..."
    deb "Можешь покосить его!"
    deb "{b}Косилка{/b} должна быть в {b}гараже{/b}."
    show debbie 1
    show player 14
    player_name "Хорошо. Пойду посмотрю."
    show player 13
    show debbie 2
    deb "Спасибо, {b}[firstname]{/b}."
    deb "Будь осторожен!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_clothes_dirty:
    scene expression L_home_entrance.background
    show player 11 zorder 1 at left
    show xtra 15 zorder 2 at Position(xpos=170,ypos=754)
    show jenny 9 at right
    with dissolve
    jen "Ого, что это за запах?!"
    show player 14
    show jenny 10
    player_name "... Я кажется. Я был снаружи, косил газон-"
    show player 11
    show jenny 9
    jen "Это отвратительно! Ты везде в траве, неряха!"
    show player 12
    show jenny 10
    player_name "Извини. Я просто пыталась помочь {b}[deb_name]{/b}."
    show player 11
    show jenny 9
    jen "Итак, что ты собираешься делать здесь?"
    jen "Тебе нравится {b}[deb_name]{/b} или что-то еще?"
    show player 10
    show jenny 10
    player_name "Нет! Я только-"
    show player 11
    show jenny 9
    jen "Пфф, не прикидывайся идиотом! Я вижу, что ты задумал!"
    hide jenny with dissolve
    pause
    show player 12
    player_name "Что у нее за проблема?"
    show player 10
    player_name "Ну что ж, я должен отнести эту одежду {b}вниз, в стирку{/b}."
    hide player with dissolve
    return

label entrance_mom_debt_collectors:
    scene henchman_cs1 2 with fade
    show text "Я ожидал увидеть {b}Эрика{/b}, но вместо него там стоял странный мужчина...\nОн был весь в черном, с таким взглядом, что даже тренер Бриджит не могла бы с ним соперничать." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene henchman_cs1 1
    show player 2 at left
    show henchman2 1 at right
    with dissolve
    player_name "Привет?"
    show henchman2 2
    show player 1
    henchman2 "Где владелец дома?"
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "А кто спрашивает?"
    show player 11
    show henchman2 3
    henchman2 "Это не твое дело, парень."
    show henchman2 1
    show player 12
    player_name "Ну, она сейчас немного занята, почему бы вам не зайти в другой раз?"
    show henchman2 2
    show player 11
    henchman2 "Не нужно, просто передай ей это сообщения."
    show henchman2 3
    henchman2 "У неё осталось мало времени, лучше бы поскорее заплатить или..."
    henchman2 "Мой босс не любит ждать."
    show henchman2 1
    show player 11
    player_name "..."
    show player 12
    player_name "Или что?"
    show player 11
    show henchman2 3
    henchman2 "Просто передай ей это, парень."
    henchman2 "Мы скоро вернемся..."
    show henchman2 1
    player_name "..."
    $ playMusic()
    hide henchman2
    with dissolve
    scene expression L_home_entrance.background
    show player 10 at left
    with fade
    player_name "( Что {b}это{/b} было вообще... )"
    show player 5
    show debbie 62 at right with dissolve
    deb "Кто-то приходил, милый?"
    show player 10
    show debbie 61
    player_name "Да, какой-то странный мужик в черном костюме..."
    show player 5
    show debbie 59
    deb "!!!"
    show player 11
    show debbie 60
    deb "... Чего он хотел?"
    show debbie 59
    show player 10
    player_name "Он сказал, что тебе нужно заплатить, и что он скоро вернется, но нормально ничего не объяснил."
    show player 11
    show debbie 60
    deb "Это должно быть..."
    deb "Но я ведь уже всё-"
    show debbie 59
    deb "..."
    show player 10
    player_name "Что такое?"
    show player 11
    show debbie 60
    deb "Ничего, милый."
    show player 1
    show debbie 62
    deb "Наверное, он просто ошиблись домом."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_pipe_help:
    scene expression L_home_entrance.background
    show player 11 at left
    show debbie 13 at right
    with dissolve
    deb "Милый! Как хорошо, что ты тут!"
    show debbie 14b
    show player 10
    player_name "{b}[deb_name]{/b}?"
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} и мне нужна твоя помощь."
    show debbie 14b
    show player 12
    player_name "Ха?"
    show player 5
    show debbie 13
    deb "Наверху прорвало труду, и вода сейчас просто повсюду!"
    deb "Твоя сестра сейчас пытается с этим разобраться."
    deb "Не мог бы ты помочь ей?"
    show debbie 14b
    show player 10
    player_name "Я? Эмм..."
    show player 5
    show debbie 13
    deb "Я не могу сейчас вызвать ремонтников. После того, что произошло..."
    show debbie 14b
    show player 10
    player_name "Ох, верно..."
    show player 14
    player_name "Я тогда схожу посмотрю."
    show player 13
    show debbie 2
    deb "Спасибо, милый! Скажешь, если тебе что-то понадобится."
    show debbie 1
    show player 14
    player_name "Конечно."
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_movie_night:
    scene location_home_entrance_night_blur
    show player 1 at left
    show debbie 62 at right
    deb "О, привет, милый!"
    deb "Уже собираешься спать?"
    show player 2
    show debbie 61
    player_name "Не, просто думаю, чем бы заняться..."
    show player 14
    player_name "А ты чего делаешь?"
    show player 1
    show debbie 62
    deb "Думала глянуть какой-нибудь фильм."
    show player 2
    show debbie 61
    player_name "Отлично."
    show player 1
    deb "..."
    show debbie 63
    deb "Может присоединишься?"
    show player 10
    show debbie 61
    player_name "Серьезно?"
    show player 11
    show debbie 62
    deb "А почему нет? Сейчас ещё не поздно, да и я люблю смотреть что-нибудь в компании!"
    show player 2
    show debbie 61
    player_name "Д-да, окей. Звучит неплохо, {b}[deb_name]{/b}."
    show player 1
    show debbie 62
    deb "Отлично!"
    deb "Тогда я пойду всё приготовлю, а ты приходи, как будешь готов, окей?"
    show player 2
    show debbie 61
    player_name "Окей!"
    hide debbie
    hide player
    with dissolve
    return

label entrance_mom_hang_out:
    scene location_home_entrance_day_blur
    show player 1 at left with dissolve
    show debbie 165 at right with dissolve
    deb "Привет, мой милый!"
    show player 2
    show debbie 164
    player_name "Привет, {b}[deb_name]{/b}!"
    player_name "Отлично выглядишь! Ты куда-то собираешься?"
    show player 1
    show debbie 165
    deb "Ох, мне нужно сходить в {b}Торговый центр{/b} и купить несколько вещей."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Может хочешь со мной?"
    show player 11
    show debbie 164
    player_name "Хмм?"
    show player 10
    player_name "Оу, я не знаю, я собирался-"
    show player 11
    show debbie 165
    deb "Оу, да ладно! Тебе нужно хотя бы чуть-чуть подышать свежим воздухом."
    show debbie 164
    player_name "..."
    show debbie 165
    deb "... К тому же, я не хочу идти одна..."
    deb "Составишь мне компанию?"
    show debbie 164
    return

label entrance_mom_hang_out_yes:
    show player 2
    player_name "Хех, ладно, {b}[deb_name]{/b}! Я пойду с тобой."
    show player 1
    show debbie 166
    deb "Прекрасно"
    show debbie 165
    deb "Жду тебя в машине, милый!"
    return

label entrance_mom_hang_out_no:
    show player 10
    player_name "Прости {b}[deb_name]{/b}, у меня были планы на сегодня..."
    show player 11
    show debbie 168
    deb "Оу."
    show debbie 169
    deb "..."
    show debbie 168
    deb "Ладно, милый... Только будь аккуратен и вернись к ужину."
    show player 2
    show debbie 169
    player_name "Конечно."
    return

label entrance_mom_spy:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Ха?"
    player_name "Что это за шум?"
    show player 11
    pause
    show player 10
    player_name "Может быть это просто телевизор."
    hide player with dissolve
    return

label entrance_mom_kissing_practice:
    scene expression L_home_entrance.background
    show player 4 with dissolve
    player_name "Интересно, {b}[deb_name]{/b} даст мне снова её поцеловать, если я попрошу?"
    player_name "Нужно {b}поговорить с ней{/b} об этом..."
    hide player with dissolve
    return

label entrance_mom_car_broken:
    scene expression L_home_entrance.background
    show debbie 3 at right
    show player 1 at left
    with dissolve
    deb "Доброе утро, милый."
    show debbie 1
    show player 14
    player_name "Утра, {b}[deb_name]{/b}."
    show player 13
    show debbie 2
    deb "Ты хорошо спал сегодня?"
    show debbie 1
    show player 10
    player_name "... Даа... типа."
    player_name "Мне снилось много странных вещей."
    show player 11
    show debbie 2
    deb "Да? И что же это за странные вещи?"
    show debbie 1
    show player 10
    player_name "Ох, Эмм..."
    player_name "Ну, это немного смущает."
    show player 11
    show debbie 2
    deb "... Пошлые сны?"
    show debbie 1
    show player 10
    player_name "Эх... Да."
    show player 11
    show debbie 2
    deb "Ну тут нечего смущаться, милый!"
    show debbie 3
    deb "Ты ведь как раз в том возрасте."
    show debbie 1
    pause
    show debbie 2
    deb "Ну и кому так повезло?"
    show player 10
    show debbie 1
    player_name "Повезло?"
    player_name "Эмм, я не очень хочу об этом говорить..."
    show player 11
    show debbie 3
    deb "Хехе, оу? Я просто думала, может я её знаю?"
    show player 11
    player_name "..."
    show debbie 3
    deb "Ну ладно. У всех свои секрет!"
    show debbie 2
    deb "Ну пока ты тут, мне нужна твоя помощь. Есть минутка?"
    show debbie 14
    show player 10
    player_name "Ух... Ага. Что нужно сделать?"
    show player 1
    show debbie 13
    deb "Можешь посмотреть, почему машина не заводится?"
    show debbie 1
    show player 10
    player_name "Может она заведется в следующий раз?"
    show player 1
    show debbie 13
    deb "Может быть, но сейчас-то она не заводится!"
    show debbie 1
    show player 2
    player_name "Ты ведь не забыла снова выключить фары и не посадила аккумулятор?"
    show debbie 2
    show player 1
    deb "Ха, нет... То есть, ну... Я не думаю, что я сделала это. Ну так ты проверишь?"
    show debbie 1
    show player 14
    player_name "Нет!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_mom_panties_masturbation_again:
    scene expression L_home_entrance.background
    show player 1
    player_name "( Не могу поверить, что {b}[deb_name]{/b} терлась об мой член! )"
    player_name "( ... ещё пара секунд и я кончу. )"
    player_name "( Ахх, я так сильно её хочу. Это просто пытка! )"
    show player 11
    player_name "( .... )"
    player_name "( Хмм, я обещал не дрочить в её комнате... )"
    show player 13
    player_name "( Просто в тот раз было так приятно! )"
    player_name "( ... )"
    player_name "( А может, если я сделаю все быстро и тихо, то смогу незаметно взять её трусики и кончить... )"
    player_name "( Вроде она {b}сейчас знаята{/b}, а значит я успею подрочить в её кровати. )"
    player_name "( Я думаю, оно того стоит... Мне нужна разрядка... Чтобы очистить свой разум! )"
    hide player with dissolve
    return

label entrance_mom_diane_visit:
    scene expression L_home_entrance.background
    show player 34 with dissolve
    player_name "...{b}*приглушенный голос*{/b}..."
    show player 35
    player_name "( Хмм, вроде {b}[deb_name]{/b} сейчас говорит с кем-то на кухне... )"
    show player 12
    player_name "( Интересно с кем? )"
    show player 10
    player_name "( Нужно пойти проверить... )"
    hide player with dissolve
    return

label entrance_mom_vacuum:
    scene location_home_entrance_fight
    show debbie 94 at right with dissolve
    pause
    show debbie 95
    pause
    show debbie 94
    pause
    show debbie 95
    pause
    show debbie 94
    show player 1 at left with dissolve
    pause
    show debbie 95
    pause
    show debbie 97 with dissolve
    deb "Ох!!!"
    deb "Ты меня напугал..."
    show debbie 98
    show player 17
    player_name "Прости меня, {b}[deb_name]{/b}."
    show player 14
    player_name "Я не хотел!"
    show debbie 97
    show player 1
    deb "Прости за этот шум."
    deb "Просто я хотела пропылесосить."
    deb "... Ох, это просто уничтожает мою спину!"
    show debbie 98
    return

label entrance_mom_vacuum_yes:
    show debbie 98 at right
    show player 14 at left
    player_name "Эй, {b}[deb_name]{/b}, давай я помогу."
    show player 1
    show debbie 96
    deb "..."
    show debbie 97
    deb "Ты хочешь пропылесосить?"
    show debbie 96
    show player 14
    player_name "Да, я закончу тут за тебя."
    player_name "А ты дай своей спине отдохнуть..."
    show player 10
    player_name "Не нужно так убиваться, если я тут и могу помочь."
    show debbie 97
    show player 11
    deb "Нет, всё в порядке, ты не должен-"
    show debbie 98
    show player 10
    player_name "Я знаю, что я не обязан помогать, {b}[deb_name]{/b}."
    player_name "Но я хочу."
    show debbie 97
    show player 1
    deb "Ну, если ты настаиваешь..."
    show player 257
    show debbie 100
    with dissolve
    deb "Это было бы очень мило с твоей стороны."
    show player 259
    show debbie 99
    player_name "Без проблем!"
    hide player
    hide debbie
    with dissolve
    scene expression "backgrounds/location_home_cutscene02.jpg"
    show expression FilteredText("Я чувствовал себя плохо, {b}[deb_name]{/b} испытывала затруднения при болях в спине.\nСамое малое, что я мог сделать, это помочь ей, даже если я сделаю это в последний раз.\nЛестница была худшей частью! Неудивительно, что её спина причиняет ей боль...\nПо крайней мере, {b}[deb_name]{/b} была со мной, пока я работал.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label entrance_mom_vacuum_no:
    show debbie 96 at right
    show player 10 at left
    player_name "Может закончишь уборку в другой раз?"
    player_name "Я тут пытаюсь заниматься, а этот шум отвлекает."
    show debbie 97
    show player 11
    deb "Прости меня, милый!"
    deb "Я не знала, что ты сейчас занимаешься."
    show debbie 96
    show player 14
    player_name "Все хорошо, {b}[deb_name]{/b}."
    show debbie 97
    show player 1
    deb "Как раз дам своей спине отдохнуть..."
    show debbie 96
    show player 17
    player_name "Спасибо!"
    hide player
    hide debbie
    with dissolve
    return

label entrance_sis_couch_1:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( Что это за звук? )"
    player_name "( Как будто телевизор работает. )"
    show player 4 at Position(xpos=518)
    player_name "( Но кто может смотреть его так поздно? )"
    hide player with dissolve
    return

label entrance_sis_couch_2:
    scene expression L_home_entrance.background
    show player 26 with dissolve
    player_name "( Это порно, что смотрит {b}[jen_name]{/b}, такое горячее! Я бы даже хотел к ней присоединиться... )"
    show player 33
    player_name "Хмм... Может {b}в следующий раз{/b}."
    hide player with dissolve
    return

label entrance_sis_couch_3:
    scene expression L_home_entrance.background
    show player 11 with dissolve
    player_name "( Что это за звук? )"
    hide player with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Милый, кто-то звонит в дверь! Можешь открыть?"
    show debbie 1
    show player 14
    player_name "Конечно, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Привет, {b}Рокси{/b}! Ты пришла к {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Пф. А что, ты думаешь, что я пришла тебя увидеть или что-то вроде того?!"
    show roxxy 1
    show player 21
    player_name "... Нет."
    show player 5
    show roxxy 2
    rox "Отлично, потому что это-"
    show roxxy 1
    show jenny 9f at left with dissolve
    jen "*Кхм*"
    jen "Это та девушка, которой я должна помочь?"
    show jenny 12f
    jen "Ну знаешь, та, которую ты пытаешься завалить?"
    show jenny 11f
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 3
    rox "ИЗВИНИ, ЧТО!?"
    show roxxy 14
    show player 113
    player_name "н-НЕТ!!"
    show player 10
    player_name "{b}Рокси{/b}, Я клянусь, я никогда-"
    show player 11
    show roxxy 2
    rox "Как будто у тебя есть шанс... Разве что в своих мечтах!"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny 12f
    jen "Оу, бедный маленький извращенец."
    jen "Я полагаю, что твоя рука застряла в банке с лосьоном."
    show jenny 11f
    show roxxy 4
    rox "Ха! Да, и мне даже жаль этот лосьон..."
    show roxxy 1
    show jenny 12f
    jen "Хахаха! А ты мне нравишься! {b}Рокси{/b}, не так ли?"
    show jenny 11f
    show roxxy 1b
    rox "Ага, а ты, значит, {b}[jen_name]{/b}?"
    show roxxy 1
    show jenny 12f
    jen "Это так."
    jen "Давай, {b}Рокси{/b}. Мы можем укрыться от этого задрота в моей комнате."
    show jenny 11f
    show roxxy 1b
    rox "Прекрасно."
    show roxxy 2
    rox "Ещё увидимся, задрот!"
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "У меня плохое предчувствие."
    hide player
    hide debbie
    with dissolve

    scene location_home_entrance_cutscene04
    with fade
    show text "Эти двое так быстро спелись...\nЯ полагаю, что у {b}[jen_name]{/b} и {b}Рокси{/b} много общего." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Они обе были капитанами чирлидерш, они популярны, красивы,\nа так же они обе постоянно совершенствуют это искусство быть сукой..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    show text "Я надеюсь, что не пожалею об этом..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    with dissolve

    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Кто это был?"
    show debbie 14
    show player 10
    player_name "Просто девочка из моей школы. {b}[jen_name]{/b} согласилась помочь ей с чирлидерскими штуками."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} кому-то помогает?"
    show debbie 3
    deb "Это что-то новенькое."
    show debbie 1
    show player 12
    player_name "Да, это потому что я заплатил ей..."
    show player 90
    show debbie 13
    deb "Оу."
    deb "Милый, ты не должен позволять {b}[jen_name]{/b} так себя пользовать..."
    show debbie 14
    show player 12
    player_name "Да, я знаю."
    show player 90
    player_name "..."
    show debbie 13
    deb "О чем ты думаешь?"
    show debbie 14
    show player 12
    player_name "Я просто никогда не видел, чтобы {b}[jen_name]{/b} так легко находила с кем-то общий язык..."
    show player 10
    player_name "Это меня даже пугает, если честно."
    show player 5
    show debbie 2
    deb "Ну, я думаю, что это неплохо, если она нашла новую подругу."
    deb "Я немного переживаю из-за того, что она сидит у себя там каждый день..."
    show debbie 13
    deb "Я думаю, что ей очень одиноко."
    show debbie 14
    show player 10
    player_name "Я бы поспорил с этим."
    show player 5
    player_name "..."
    show player 11
    jen "Хахаха!!"
    show player 10
    player_name "...{b}Может стоит их там проверить{/b}?"
    show player 5
    show debbie 2
    deb "Может."
    show debbie 13
    deb "...Только будь осторожен, милый."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_mentoring_sex:
    scene expression L_home_entrance.background
    show player 13 at Position (xpos=300)
    show debbie 2 at right
    with dissolve
    deb "Милый, кто-то звонит в дверь! Можешь открыть??"
    show debbie 1
    show player 14
    player_name "Конечно, {b}[deb_name]{/b}!"
    show player 10
    show roxxy 1 at Position (xpos=600) with dissolve
    player_name "Привет, {b}Рокси{/b}! Ты пришла к {b}[jen_name]{/b}?"
    show player 5
    show roxxy 2
    rox "Да, предложение ведь ещё в силе?"
    show roxxy 1
    show player 21
    player_name "Конечно."
    show player 5
    show roxxy 2
    rox "Прекрасно, я так взволнована-"
    show roxxy 1
    show jenny 9f at left with dissolve
    jen "*Кхм*"
    jen "Это та девушка, которой я должна помочь?"
    show jenny 12f
    jen "Ну знаешь, та, которую ты пытаешься завалить?"
    show jenny 11f
    hide xtra
    show player 11
    with dissolve
    show debbie 14
    player_name "!!!" with hpunch
    show roxxy 4
    rox "... Хахаха!"
    show roxxy 14
    show player 113
    player_name "Я не-"
    show player 10
    player_name "{b}Рокси{/b}, Клянусь, я никогда-"
    show player 11
    show roxxy 1h
    rox "И что именно ты рассказал, {b}[firstname]{/b}?"
    show roxxy 1
    show player 37 at Position (xoffset=41) with dissolve
    show jenny 12f
    jen "Секунду..."
    jen "Имеешь ввиду, что ты... И он?!"
    show jenny 11f
    show roxxy 4
    rox "Эм даа?!"
    rox "До тех пор, пока он хорошо обо мне заботится..."
    rox "... И пока он не растолстеет или не облысеет!"
    show roxxy 1
    show jenny 12f
    jen "Хахаха! А ты мне нравишься! {b}Рокси{/b}, не так ли?"
    show jenny 11f
    show roxxy 1b
    rox "Ага, а ты, значит, {b}[jen_name]{/b}??"
    show roxxy 1
    show jenny 12f
    jen "Верно."
    jen "Давай, {b}Рокси{/b}. Сделаем это у меня в комнате."
    show jenny 11f
    show roxxy 1b
    rox "Окей."
    show roxxy 2
    rox "Ещё раз спасибо, {b}[firstname]{/b}."
    hide roxxy
    hide jenny
    show player 25
    with dissolve
    player_name "..."
    show player 24
    player_name "У меня плохое предчувствие."
    hide player
    hide debbie
    with dissolve
    scene expression L_home_entrance.background
    show player 24 at Position (xpos=300)
    show debbie 13 at right
    with dissolve
    deb "Так вы с ней встречаетесь?"
    show debbie 14
    show player 10
    player_name "Хех, да. {b}[jen_name]{/b} согласилась помочь ей с чирлидерскими штуками."
    show player 5
    show debbie 13
    deb "{b}[jen_name]{/b} помогает кому-то?"
    show debbie 3
    deb "Это что-то новенькое..."
    show debbie 1
    show player 12
    player_name "Да, просто я заплатил ей..."
    show player 90
    show debbie 13
    deb "Ох."
    deb "Милый, ты не должен позволять {b}[jen_name]{/b} так себя пользовать..."
    show debbie 14
    show player 12
    player_name "Да, я знаю."
    show player 90
    player_name "..."
    show debbie 13
    deb "О чем ты думаешь?"
    show debbie 14
    show player 12
    player_name "Я просто никогда не видел, чтобы {b}[jen_name]{/b} так легко находила с кем-то общий язык..."
    show player 10
    player_name "Это меня даже немного пугает."
    show player 5
    show debbie 2
    deb "Ну, я думаю, что это неплохо, если она нашла новую подругу."
    deb "Я немного переживаю из-за того, что она сидит у себя там каждый день..."
    show debbie 13
    deb "Я думаю, что ей очень одиноко."
    show debbie 14
    show player 10
    player_name "Я бы поспорил"
    show player 5
    player_name "..."
    show player 11
    jen "Хахаха!!"
    show player 10
    player_name "...{b}Может стоит их там проверить{/b}?"
    show player 5
    show debbie 2
    deb "Может"
    show debbie 13
    deb "...Только будь аккуратен, милый."
    hide player
    hide debbie
    with dissolve
    return

label entrance_bissette_roxxy_jenny_spying:
    scene expression L_home_entrance.background
    show player 10 with dissolve
    player_name "Я должен пойти проверить как там {b}Рокси{/b} и {b}[jen_name]{/b}..."
    hide player with dissolve
    return

label entrance_diane_debbie_evening_visit_overhear:
    scene expression "backgrounds/location_home_entrance_evening_blur.jpg"
    show player 34 with dissolve
    player_name "( Хмм? )"
    player_name "( Это {b}Диана{/b}? )"
    player_name "( {b}[deb_name]{/b} должно быть, пригласила ее. )"
    player_name "( {b}Интересно, о чем они говорят?{/b} )"
    hide player with dissolve
    return
