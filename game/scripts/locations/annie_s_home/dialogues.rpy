label annie_front_diane_build_toys:
    show expression "backgrounds/location_annie_cutscene02.jpg"
    show expression FilteredText("Я рад, что {b}мой отец{/b} научил меня пользоваться этой штукой перед смертью.\nБыло бы неловко, если бы я не смог помочь {b}Диане{/b} и {b}Люси{/b}.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Делать игрушки - это весело!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    show expression "backgrounds/location_annie_cutscene03.jpg"
    show expression FilteredText("Они получились действительно... Ох... Уникальными!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("По крайней мере, они в безопасности.\nЭто ведь самое главное, правда?") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 184 at Position (xpos=350)
    with dissolve
    player_name "Я просто поставлю игрушку здесь..."
    show player 429 at left with dissolve
    player_name "Надеюсь, они понравятся детям..."
    show player 426
    show lucy f_normal_talk with dissolve
    lucy "Ты все здесь закончил?!"
    show lucy f_normal
    show player 11 with dissolve
    player_name "!!!"
    show player 29 with dissolve
    player_name "О, эээ... П-привет, {b}Люси{/b}."
    player_name "Думаю, да."
    show player 3
    show lucy f_normal_talk
    lucy "Хорошо, давай посмотрим."
    show lucy f_normal_down2

    player_name "..."
    show lucy f_laugh
    lucy "О, они восхитительны {b}[firstname]{/b}!"
    show lucy f_normal
    show player 10 with dissolve
    player_name "...Ты не думаешь, что они уродливые?"
    show player 5
    show lucy f_normal_talk_down
    lucy "Вовсе нет!"
    lucy "Я думаю, они идеальны!"
    lucy "Детям они понравятся!"
    show lucy f_normal
    show player 17
    player_name "Хех, круто!"
    show player 13
    show lucy f_normal_talk
    lucy "Ты такая творческая личность!"
    show lucy f_normal_talk a_dressed_cleavage with dissolve
    lucy "Сколько я тебе должна?"
    show lucy f_normal_down
    show player 10
    player_name "Хух?!"
    show player 14
    player_name "Н-нет, нет!"
    player_name "Вы мне ничего не должны за это, {b}Люси{/b}!"
    show player 13
    show lucy f_normal_talk a_dressed_money with dissolve
    lucy "О, перестань."
    lucy "Вы заслуживаете что-то за такую прекрасную работу!"
    show lucy f_normal
    show player 14
    player_name "Хе-хе, нет, действительно, я ничего не хочу..."
    show player 13
    show lucy f_normal_talk a_dressed_hips with dissolve
    lucy "Хмм."
    show lucy f_smirk_talk
    lucy "Ну, как насчет..."
    hide player
    show lucy kiss_mc
    with dissolve
    lucy "Поцелуй!"
    show player 29 at left
    hide lucy
    show lucy f_smirk
    with dissolve
    pause
    show player 13 at left
    show xtra 21 at left
    with dissolve
    show lucy f_smirk_talk
    lucy "Подойдет?"
    show lucy f_smirk
    show player 21
    hide xtra
    player_name "Ну, д-да!"
    player_name "С-спасибо, {b}Люси{/b}!"
    show player 18
    show lucy f_laugh
    lucy "С удовольствием, {b}[firstname]{/b}!"
    show lucy f_bigsmile
    pause
    show player 13
    player_name "..."
    show lucy f_normal_talk
    lucy "Что ж, мне лучше вернуться к детям..."
    lucy "Ты хочешь присоединиться?"
    show lucy f_normal
    show player 14
    player_name "Ох, ох... Нет, я должен пойти проверить сарай {b}Дианы{/b} и посмотреть, как там {b}Ричард{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "Ааа, ну... хорошо."
    lucy "Возвращайся ко мне поскорее, ладно?"
    show lucy f_normal
    show player 17
    player_name "Хе-хе, хорошо!"
    show player 13
    show lucy f_normal_talk a_dressed_wave with dissolve
    lucy "Пока, {b}[firstname]{/b}."
    hide lucy with dissolve
    pause
    show player 17
    player_name "Вау!"
    show player 14
    player_name "Мама {b}Энни{/b} такая милая!"
    show player 12
    player_name "Что в мире пошло не так с {b}Энни{/b}!"
    show player 4 with dissolve
    pause
    show player 14 with dissolve
    player_name "Ну что ж, мне лучше вернуться к {b}Диане{/b}."
    hide player with dissolve
    return


label annies_house_diane_help_annie:
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show player 5 at left
    show annie 3 at right
    with dissolve
    ann "{b}[firstname]{/b}!"
    show annie 6
    show player 12
    player_name "Привет, {b}Энни{/b}."
    show player 5
    show annie 5
    ann "Что ты делаешь в моем доме?!"
    show annie 6
    show player 14
    player_name "Я готовлю пару игрушек для детского сада твоей мамы."
    show player 10
    player_name "Не могли бы вы показать мне, {b}где ваш отец хранит свои инструменты{/b}?"
    show player 5
    show annie 5
    ann "Почему {b}папа{/b} их не строит?"
    show annie 6
    show player 10
    player_name "Хмм?"
    player_name "Ох, эээ... Моей знакомой нужно было, чтобы {b}твой отец{/b} как можно скорее начал работу над ее сараем, поэтому я предложил помочь с игрушками."
    show player 5
    show annie 3
    ann "Как будто {b}моему отцу{/b} нужна помощь от такого придурка, как ты..."
    show annie 1
    show player 12
    player_name "... Ну, я думаю, что я не настолько глуп, раз он позволяет мне строить их, самому!"
    show player 90
    show annie 3
    ann "Да, точно."
    ann "{b}Моя мама{/b} уговорила его на это?"
    show annie 1
    show player 12
    player_name "Да, типа того."
    show player 5
    show annie 3
    ann "Конечно, она это сделала..."
    ann "Типичная {b}мама{/b}, не ценит мастерство."
    show annie 1
    show player 90
    player_name "..."
    ann "Кто вообще строит амбар в черте города?!"
    show annie 5
    ann "Тебе повезло, что дела идут медленно, иначе {b}мой отец{/b} никогда бы не взялся за эту работу."
    show annie 6
    show player 12
    player_name "Да, неважно {b}Энни{/b}..."
    player_name "Ты мне поможешь или нет?"
    show player 90
    show annie 5
    ann "Нет, не помогу."
    ann "Я должна присматривать за правонарушителями, задержанными этим вечером для {b}миссис Смит{/b}, а потом она хочет, чтобы я ей приготовила ванну-"
    show annie 28
    ann "!!!"
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "Ты только что сказала, что собираешься приготовить ванну для {b}миссис Смит{/b}."
    show player 11
    show annie 5
    ann "... Нет."
    show annie 6
    show player 10
    player_name "Что, ты сейчас готовишь ей ванну?!"
    show player 5
    show annie 8
    ann "НЕТ!!"
    ann "Я не- {b}*вздох*{/b} Суть в том, что я ухожу."
    show annie 5
    ann "Постарайся не сжечь мой дом, придурок."
    show annie 6
    player_name "..."
    hide annie with dissolve
    pause
    show player 17
    player_name "Убедись что ты промоешь все ее укромные уголки и трещины!"
    show player 13
    ann "ЗАТКНИСЬ!!!"
    show player 14
    player_name "Почему бы тебе не сделать ей педикюр, пока ты там?!"
    show player 12
    player_name "Блин, какой чудак..."
    show player 4 with dissolve
    pause
    show player 10 with dissolve
    player_name "Хорошо, мне просто нужен {b}молоток и ручная пила{/b} чтобы построить наездника и качели."
    player_name "{b}Люси{/b} сказала, что они должны быть где-то здесь..."
    hide player with dissolve
    return

label annie_front_diane_ask_help_annie:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show player 13 at left
    show richard at flip
    show richard at Position (xpos=275)
    show lucy f_sad_talk at Position (xpos=650)
    with dissolve
    lucy "Я просто не понимаю, почему ты не можешь сделать это позже?"
    show lucy f_sad
    show player 5
    show richard f_normal_talk
    rich "Это следующий пункт в моем списке, вот почему!"
    show richard f_normal
    show lucy f_sad_talk
    lucy "Да, но ты же знаешь, что я не могу приводить сюда детей, пока у тебя здесь все эти опасные инструменты..."
    show lucy f_sad
    show richard f_normal_talk
    rich "И что?!"
    rich "Они могут играть внутри, не так ли?!"
    show richard f_normal
    show lucy f_sad_talk
    lucy "{b}Ричард{/b}, сегодня такой прекрасный день..."
    lucy "Дети хотят наслаждаться этим..."
    lucy "Ты не можешь просто пойти и начать работу в сарае для {b}Дианы{/b}?"
    show lucy f_sad
    show richard f_normal_talk
    rich "Нет!"
    rich "Ты знаешь, что я обрабатываю свои задания в том порядке, в котором я их получаю, {b}Люси{/b}."
    rich "В противном случае вещи перемешиваются и, прежде чем вы это узнаете, наступает хаос!"
    show richard f_normal
    show lucy f_confused_talk
    lucy "Почему ты не можешь просто переместить этот пункт вниз по списку ниже работы в сарае!"
    lucy "Я не вижу ничего плохого в том-"
    show lucy f_sad
    show player 11
    show richard f_angry_yell
    rich "ЖЕНЩИНА, ХАОС!" with hpunch
    rich "АБСОЛЮТНЫЙ И ПОЛНЫЙ ХАОС!!!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "{b}*вздох*{/b}"
    show lucy f_confused_talk
    lucy "О, {b}[firstname]{/b}!"
    lucy "Что ты здесь делаешь?"
    show lucy f_confused
    show richard f_normal_talk at unflip
    show richard at Position (xpos=-275)
    with dissolve
    rich "Хмм, молочник?"
    show richard f_normal_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "Ради всего святого, вы уже заказали больше?!"
    show richard f_normal
    show lucy f_confused_talk
    lucy "Мне так не кажется..."
    show lucy f_confused
    show richard f_normal_talk
    rich "Клянусь, эти сопляки выпьют меня совсем!"
    show richard f_normal
    show lucy f_thinking
    lucy "... может Я сделаю другой заказ?"
    show lucy f_confused
    show richard at unflip
    show richard at Position (xpos=-275)
    with dissolve
    show player 10
    player_name "Я здесь не для доставки, мэм."
    show player 5
    show lucy f_laugh
    lucy "О, слава богу!"
    show lucy f_normal_talk
    lucy "Я думала, что снова совершила ошибку."
    show lucy f_normal
    show richard f_normal_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "Ну, день еще только начинается. Достаточно времени, чтобы что-то испортить."
    show richard f_normal
    show lucy f_sad_down
    show player 90
    pause
    show player 12
    player_name "Вообще - то, я зашел узнать, могу ли я чем-нибудь помочь {b}Ричарду{/b}?"
    show player 5
    show lucy f_confused
    show richard f_normal_talk at unflip
    show richard at Position (xpos=-275)
    with dissolve
    rich "Хмм?"
    rich "Помочь мне с чем?"
    show richard f_normal
    show player 10
    player_name "Ну, {b}Диана{/b} сказала, что у тебя есть несколько дел в доме, прежде чем ты начнешь работать в ее сарае."
    show player 29 with dissolve
    player_name "Я думал, я мог бы помочь?"
    show player 3
    show lucy f_normal_talk
    lucy "О, это замечательная идея!"
    show lucy f_normal
    show richard f_confused_talk
    rich "Хух?!"
    rich "Ну, держись теперь."
    rich "Я не могу начать платить за-"
    show richard f_confused
    show player 12 with dissolve
    player_name "Я буду работать бесплатно!"
    show player 5
    show richard f_confused_talk
    rich "Бесплатно?!"
    show richard f_confused
    show lucy f_normal_talk
    lucy "Такой милый мальчик..."
    show lucy f_normal
    show player 10
    player_name "До тех пор, пока это не приведет вас к {b}Диане{/b} как можно быстрее."
    show player 5
    show richard f_confused_talk
    rich "Хмм, Не знаю..."
    rich "Я хотел бы убедиться, что работа, которую я делаю, имеет высокое качество-"
    show richard f_confused
    show lucy f_normal_talk
    lucy "О, дерьмо собачье!"
    lucy "Это просто пара игрушек для малышей. Я уверена, что {b}[firstname]{/b} более чем способен создавать игрушки."
    show lucy f_normal
    show player 29 with dissolve
    player_name "Д-Да, это не должно быть проблемой."
    show player 5 with dissolve
    show lucy f_normal_talk
    lucy "Вот, видишь!"
    lucy "Вычеркни этот пункт из списка и перейди к заданию от {b}Дианы{/b}!"
    show lucy f_normal
    show richard f_confused_talk
    rich "Я..."
    show richard f_confused
    pause
    show richard f_confused_talk at flip
    show richard at Position (xpos=275)
    with dissolve
    rich "Полагаю, я могу начать работу на амбаре, пока мальчик качается на..."
    show richard f_normal_talk
    rich "... Однако ничего не вычеркнуто из списка до завершения!"
    rich "Я вернусь, чтобы проверить эти игрушки позже!"
    show richard f_normal
    show lucy f_normal_talk
    lucy "Звучит справедливо."
    show lucy a_dressed_shoo f_laugh with dissolve
    lucy "А теперь Кыш!"
    show lucy f_normal a_dressed_hips with dissolve
    show richard f_normal_talk
    rich "Ччч, держись!"
    rich "Мне нужно собрать инструменты..."
    hide richard with dissolve
    show lucy f_normal_talk
    lucy "Давай, давай, давай!"
    show player 13
    lucy "Слава богу, ты пришел."
    show lucy f_laugh
    lucy "Он сводит меня с ума!"
    show lucy f_normal
    show player 14
    player_name "Хех, да?"
    show player 13
    show lucy f_normal_talk
    lucy "Ты же не собираешься настаивать на том, чтобы начать прямо сейчас?"
    show lucy f_normal
    show player 10
    player_name "Хмм?"
    show player 14
    player_name "О, н-нет... Начну когда будет лучше для вас, мэм."
    show player 13
    show lucy f_normal_talk
    lucy "{b}Люси{/b}, {b}[firstname]{/b}."
    show lucy f_normal
    show player 10
    player_name "А?"
    show player 5
    show lucy f_normal_talk
    lucy "Зови меня {b}Люси{/b}."
    show lucy f_normal
    show player 14
    player_name "Х-хорошо, {b}Люси{/b}."
    show player 13
    show lucy f_normal_talk
    lucy "Я собираюсь выпустить детей поиграть, пока погода такая хорошая."
    lucy "Они действительно могут быть кучей, когда они заперты внутри весь день."
    lucy "Вы можете начать с игрушек, которые пришли в негодность."
    show lucy f_laugh
    lucy "Звучит хорошо?"
    show lucy f_normal
    show player 14
    player_name "Да."
    show player 13
    show lucy f_normal_talk
    lucy "Тебе нравятся маленькие дети?"
    show lucy f_normal
    show player 10
    player_name "О, да, наверное..."
    show player 5
    show lucy f_normal_talk
    lucy "Хехе, тебе лучше быть уверенным, если ты собираешься остаться."
    show expression "backgrounds/location_annie_cutscene01.jpg"
    show expression FilteredText("{b}Люси{/b} не пошутила!\nМалыши выливались из яслей, как рой саранчи.\nКричали, вопили и швыряли игрушки...\nЭто было ужасно!") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    show expression FilteredText("Все это время {b}Люси{/b} едва могла сдерживать свое счастье.\nЕй действительно нравилось ухаживать за ними и видеть, как ее улыбка сделала мой день!") as cutscene at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene black
    hide cutscene
    with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show player 12 at left
    show lucy b_messy
    with dissolve
    player_name "Срань господня..."
    show player 5
    show lucy f_laugh
    lucy "Хе-хе, я знаю."
    lucy "Разве они не замечательные?!"
    show lucy f_normal
    show player 12
    player_name "А?"
    show player 29 with dissolve
    player_name "В смысле, да... Хех, замечательно!"
    show player 3
    show lucy f_normal_talk
    lucy "Ты действительно справляешься с ними, {b}[firstname]{/b}."
    show lucy f_normal
    show player 12 with dissolve
    player_name "О, я не знаю насчет этого..."
    show player 5
    show lucy f_laugh
    lucy "Я серьезно!"
    show lucy f_normal_talk
    lucy "Приятно видеть молодого человека, который так хорошо ладит с детьми."
    lucy "Похоже, что все отцы, которых я встречаю в детском саду, не могут дождаться, чтобы избавиться от своих детей."
    show lucy f_normal
    show player 10
    player_name "Правда?"
    player_name "Это просто печально..."
    player_name "А как насчет {b}Ричарда{/b}?"
    player_name "Кажется, {b}Энни{/b} идеализирует его..."
    show player 5
    show lucy f_normal_talk
    lucy "Хе-хе, ну, скажем так, он взял подход 'руки прочь' к воспитанию {b}Энни{/b}."
    lucy "Его основным направлением всегда был бизнес."
    show lucy f_normal
    show player 10
    player_name "That seems really unfair to you {b}Lucy{/b}..."
    show player 5
    show lucy f_normal_talk a_dressed_wave with dissolve
    lucy "Oh, it's fine."
    show lucy a_dressed_sides with dissolve
    lucy "{b}Richard{/b} never really wanted kids."
    lucy "I knew what I was getting into when I convinced him to have {b}Annie{/b}."
    lucy "I worry about how it affected her though."
    lucy "She'll do anything to gain her father's approval."
    show lucy f_normal
    show player 35
    player_name "Hmm, that does explain some things about her behavior..."
    show player 34
    show lucy f_confused_talk
    lucy "What's that dear?"
    show lucy f_normal
    show player 10
    player_name "Oh, uhh... Nothing ma'-"
    show player 14
    player_name "{b}*Ahem*{/b} I mean, nothing {b}Lucy{/b}."
    player_name "I should probably get started on those toys soon, huh?"
    show player 13
    show lucy f_normal_talk
    lucy "You're right."
    lucy "I should get the little ones inside for nap time."
    show lucy f_normal
    show player 10
    player_name "Does {b}Richard{/b} have any tools I can use?"
    show player 13
    show lucy f_laugh a_dressed_cover with dissolve
    lucy "Haha, does {b}Richard{/b} have any tools..."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "Go check inside the house, you'll find what you need in no time."
    show lucy f_normal
    show player 14
    player_name "Thanks."
    hide player
    hide lucy
    with dissolve
    return

label annies_house_livingroom_diane_delivery_2:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show richard a_dressed_phone_talk f_phone_talk
    show player 13 at left
    with dissolve
    rich "No, absolutely not!"
    rich "Well, I don't care if you don't like it..."
    show player 5
    show richard f_phone
    pause
    show richard f_phone_talk
    rich "No..."
    rich "The fact of the matter is that it's OSHA regulation."
    rich "No, I do things strictly by the book!"
    rich "I told you as much when you hired me."
    show richard f_normal
    rich "..."
    show richard f_phone_talk
    rich "No, more money won't make it go away."
    rich "Rules are rules."
    rich "Look, I need you to hold on for a second."
    show richard f_normal_talk a_dressed_phone with dissolve
    rich "Can I help you?"
    show richard f_normal
    show player 12
    player_name "Uhh, maybe..."
    show player 10
    player_name "Do you live here?"
    show player 5
    show richard f_normal_talk
    rich "Yes?"
    show richard f_normal
    show player 239_240 with dissolve
    pause
    show player 163c with dissolve
    player_name "I'm supposed to deliver this-"
    show player 163g
    show richard f_normal_talk
    rich "Oh, you're the milk guy..."
    rich "Ugh, alright. Follow me."
    show richard a_dressed_phone_talk f_phone_talk at fliplright
    with dissolve
    rich "Now, where were we?"
    rich "Oh right, OSHA guidelines article 7..."
    hide richard with dissolve
    player_name "..."
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show richard a_dressed_phone f_normal_talk at flip, Position (xcenter=0.75)
    show player 163b at left
    with dissolve
    rich "{b}Lucy{/b}!"
    rich "The milk man's here!"
    show richard f_normal at flip, Position (xcenter=0.75)
    lucy "Oh, coming!"
    show richard a_dressed_phone f_normal_talk at unflip
    show richard at lcenter
    with dissolve
    rich "My wife's the one who ordered it."
    rich "She'll sort you out."
    show richard a_dressed_phone_talk f_phone at flip, Position (xcenter=0.75) with dissolve
    show player 163c
    player_name "O-okay."
    show player 163b
    show lucy f_normal_talk at Position (xpos=650) with dissolve
    lucy "Phew, these kids are wearing me out!"
    show lucy f_normal
    show richard f_phone_talk at flip
    rich "Uh huh..."
    show richard f_phone at flip
    show lucy f_normal_talk
    lucy "{b}Richard{/b}, could you, umm... Help carry these over to the house?"
    show lucy f_normal
    show richard f_angry_talk at flip
    rich "Not now, {b}Lucy{/b}! Can't you see I'm on the phone with a client?!"
    show richard f_phone_talk at flip
    rich "Oh, sorry... One second."
    show richard a_dressed_phone f_angry_talk at flip with dissolve
    rich "This daycare was your dumb idea and you should handle it your own damn self!"
    show lucy f_sad
    rich "... And make sure you count the money this time before handing it over!"
    rich "Money is tight enough around here without you throwing more down the drain!"
    show richard f_angry at flip
    show lucy f_sad_talk
    show player 163g
    lucy "Yes, dear..."
    show lucy f_sad_down
    hide richard with dissolve
    rich "Sorry, about that again..."
    lucy "..."
    show player 163c
    player_name "I'll help you, ma'am."
    show player 163b
    show lucy f_sad_talk
    lucy "Oh, that's not necessary. I'm sure you have lots of-"
    show lucy f_sad
    show player 163c
    player_name "I insist."
    show player 163b
    show lucy f_normal
    lucy "..."
    show lucy f_normal_talk
    lucy "Well, aren't you sweet!"
    lucy "Let me call my daughter over to watch the kids for a second."
    show lucy f_normal
    show player 163c
    player_name "Yeah, okay."
    show player 163b
    hide lucy with dissolve
    player_name "..."
    lucy "{b}Annie{/b}, sweetie?"
    lucy "Could you come help me for a second?"
    ann "Ugh, I was just walking out the door, {b}Mom{/b}..."
    lucy "I only need you for a couple minutes."
    ann "Ughhh!!!"
    show annie 7 at Position (xpos=600)
    show lucy f_normal at Position (xpos=650)
    with dissolve
    ann "This had better not make me late!"
    ann "{b}Mrs. Smith{/b} doesn't tolerate-"
    show annie 1
    ann "..."
    show annie 4
    ann "What is he doing here?"
    show annie 6
    lucy "Hmm?"
    show lucy f_confused_talk
    lucy "Do you two know each other?"
    show lucy f_confused
    show player 163c
    player_name "Heh, we're in the same class at school."
    show player 163b
    show lucy f_laugh
    lucy "Well, isn't that nice?"
    show lucy f_normal
    show annie 5
    ann "Hardly..."
    show annie 6
    show lucy f_normal_talk
    lucy "This nice young man-"
    lucy "Sorry, I didn't catch your name?"
    show lucy f_normal
    show player 163c
    player_name "{b}[firstname]{/b}."
    show player 163b
    show lucy f_normal_talk
    lucy "Hi, {b}[firstname]{/b}. I'm {b}Lucy{/b}."
    show lucy f_normal
    show player 163c
    player_name "Nice to meet you, ma'am."
    show player 163b
    show lucy f_laugh
    lucy "Oh, goodness."
    show lucy f_normal_talk
    lucy "I hope you're friends with this one, {b}Annie{/b}?"
    lucy "I like him!"
    show lucy f_normal
    show annie 3
    ann "He's a delinquent!"
    show annie 1
    show player 163g
    show lucy f_normal_talk
    lucy "Oh, don't call him that!"
    show lucy f_normal
    show annie 4
    ann "... That's what he is!"
    show annie 1
    show lucy f_normal_talk
    lucy "{b}[firstname]{/b}, offered to haul all this milk inside for me."
    lucy "Would you watch the kids, while I help him?"
    show player 163b
    show lucy f_normal
    show annie 4f with dissolve
    ann "No way! Absolutely not!"
    ann "You know I HATE kids!"
    show annie 1f
    show lucy f_normal_talk
    lucy "Pleeeeeeeeease?"
    lucy "It'll just take a moment."
    show lucy f_normal
    show annie 6f
    ann "..."
    show annie 5f
    ann "Why can't {b}Dad{/b} do it?!"
    show annie 6f
    show lucy f_normal_talk
    lucy "Oh, he's on the phone arguing with a client."
    show lucy f_normal
    show annie 5f
    ann "... Is that moron still complaining about the OSHA regulations?!"
    ann "It's not like {b}Dad{/b} wrote the rules, he just abides by them like any decent person would..."
    show annie 6f
    show lucy f_confused_talk
    lucy "I don't-"
    show lucy f_confused
    lucy "..."
    show lucy f_confused_talk
    lucy "What's an OSHA?"
    show lucy f_confused
    show annie 7f
    ann "Errghh!! Nevermind..."
    show annie 4f
    ann "Just hurry up!"
    hide annie
    show lucy hug_annie
    with dissolve
    lucy "Thank you, sweetie!"
    lucy "Follow me, {b}[firstname]{/b}!"
    show annie 6f at Position (xpos=600)
    hide lucy
    with dissolve
    show player 163c
    player_name "Yes, ma'am."
    hide player with dissolve
    ann "..."
    show annie 4f
    ann "Hey! Stop running!!"
    hide annie with dissolve
    ann "Eugh, don't put that in your mouth!!!"
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show lucy bend
    show player 426 at left
    with dissolve
    lucy "Alright, everything looks good."
    lucy "I dunno what you all are putting in this milk but the kids just can't get enough!"
    player_name "Mmmhmm."
    lucy "This will all be gone in a couple weeks."
    lucy "I'll need to order a lot more next time."
    lucy "Assuming {b}Richard{/b} lets me."
    player_name "..."
    lucy "That wouldn't be a problem would it?"
    player_name "..."
    show lucy f_confused_talk at Position (xpos=650)
    lucy "{b}[firstname]{/b}?"
    show lucy f_confused
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "I'm sorry, what was that last bit?"
    show player 3
    show lucy f_normal_talk
    lucy "I said I'll need to order more next time, if that's alright?"
    show lucy f_normal
    show player 29
    player_name "... Yeah, I think so."
    show player 17 with dissolve
    player_name "I'll speak with {b}Diane{/b} about it."
    show player 13
    show lucy f_laugh
    lucy "Wonderful!"
    show lucy f_normal_talk
    lucy "As for your payment..."
    show lucy f_normal_down a_dressed_cleavage with dissolve
    show player 11
    player_name "!!!"
    show lucy a_dressed_money with dissolve
    lucy "That should cover it."
    show lucy f_normal a_dressed_sides
    show player 638b at Position (xoffset=-19)
    with dissolve
    player_name "..."
    show player 638 at Position (xoffset=-21)
    player_name "Uhh, this is too much."
    show player 13
    show lucy a_dressed_money f_normal_down with dissolve
    lucy "..."
    show player 14
    player_name "That's fifty dollars more than the price..."
    show player 13
    show lucy f_confused_talk
    lucy "!!!"
    show lucy f_laugh
    lucy "Whoopsie!"
    show lucy f_normal_talk
    lucy "Hehe, I'm such a clutz with money..."
    show lucy f_laugh a_dressed_cleavage with dissolve
    lucy "... And you're a sweetheart!"
    hide player
    show lucy hug_mc
    with dissolve
    lucy "Thank you for being honest, {b}[firstname]{/b}!"
    player_name "!!!"
    pause
    show player 29 at left
    show lucy f_normal
    with dissolve
    player_name "Heh. N-no problem, ma'am."
    player_name "I wouldn't want your husband to get angry at you again."
    show player 3
    show lucy f_confused
    lucy "Hmm?"
    show lucy f_laugh a_dressed_wave with dissolve
    lucy "Oh! No..."
    show player 13 with dissolve
    lucy "He's just so busy with {b}his carpentry business{/b} and all!"
    lucy "He doesn't have time for me and my problems."
    show lucy f_normal a_dressed_sides with dissolve
    player_name "..."
    show player 10
    player_name "He's a {b}carpenter{/b}?"
    show player 5
    lucy "Mmmhmm."
    show lucy f_sad_talk
    lucy "He's been doing it for over 20 years."
    lucy "Poor dear, works himself to the bone."
    show lucy f_sad
    show player 12
    player_name "Well, he should make time."
    show player 14
    player_name "You're such a nice lady!"
    show player 13
    show lucy f_normal_talk
    lucy "Aww, well thank you, {b}[firstname]{/b}!"
    lucy "You're nice too!"
    show lucy f_normal
    ann "DON'T THROW THINGS!!!" with hpunch
    show player 11
    player_name "!!!"
    show lucy f_confused
    ann "AAAHHH!!"
    show lucy f_confused_talk
    lucy "Uh oh..."
    show player 13
    lucy "It sounds like the kids are getting the better of {b}Annie{/b} in there."
    lucy "I'd better go rescue her!"
    hide lucy with dissolve
    player_name "..."
    show player 17
    player_name "( Oh, I have to check this out! )"
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show annie 25 at right
    show player 11 at Position (xpos=400)
    show lucy f_confused at fliplleft
    with dissolve
    ann "I TOLD YOU TO STOP RUNNING!!!"
    show annie 24
    pause
    show annie 25
    ann "Ugh, finally!"
    ann "What took you so long?!"
    show annie 24
    show lucy f_confused_talk
    lucy "I'm sorry, sweetie. I-"
    show lucy f_confused
    show annie 25
    ann "Look at me, I'm a disaster now!"
    ann "I'm going to have to shower again!"
    show annie 24
    show lucy f_sad_down
    lucy "..."
    show annie 25
    ann "Thanks a lot {b}Mom{/b}!"
    show annie 26 with dissolve
    pause
    hide annie with dissolve
    pause
    show player 10f at right with dissolve
    player_name "Wow, that was..."
    player_name "... You alright, ma'am?"
    show player 5f
    show lucy f_sad
    lucy "Hmm?"
    show lucy f_sad_talk
    lucy "Oh, It's fine."
    show lucy f_sad
    lucy "..."
    show lucy f_sad_talk
    lucy "Thanks again, for your help today, {b}[firstname]{/b}."
    show lucy f_sad
    show player 14f
    player_name "It was no problem, ma'am."
    player_name "I'll see you next time."
    show player 13f
    hide lucy with dissolve
    pause
    show player 5f
    player_name "( That poor woman... )"
    pause
    show player 18f
    player_name "( Welp, I should get this money back to {b}Diane{/b} and tell her that the daycare will be needing more next time. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
