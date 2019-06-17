label annies_house_first_time:
    scene expression player.location.background_blur with None
    show player at Position (xpos=400)
    show richard f_angry_talk at flip
    show richard at Position (xpos=150)
    show lucy f_sad at Position (xpos=600)
    rich "No, I wanna know how the chair got broken, {b}Lucy{/b}?!"
    show richard f_angry
    show player f_worried
    show lucy f_thinking
    lucy "I dunno, dear..."
    show lucy f_sad_talk
    lucy "{b}Timmy{/b} says they were playing tag and {b}Molly{/b} tripped and knocked it over."
    show lucy f_sad_down
    show richard f_angry_talk
    rich "So you were letting them run in the house, after I specifically told you not to let them do that."
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "It was just an accident, dear."
    show lucy f_sad
    show richard f_angry_talk
    rich "I don't care, this is unacceptable!"
    rich "We have rules in the house for a reason... If they can't follow them, then they need to stay out!"
    show richard f_angry
    show lucy f_confused_talk
    lucy "Tsk, you're making such a fuss over a silly chair {b}Richard{/b}..."
    lucy "Can't you just repair it?"
    show lucy f_confused
    show richard f_angry_talk
    rich "Yeah, because that's exactly what I wanna do after working my ass off all day..."
    show richard f_angry
    show lucy f_confused_talk
    lucy "There's no rush... Maybe this weekend you could-"
    show lucy f_confused
    show richard f_angry_talk
    rich "I'm working all weekend!!"
    show richard f_angry
    show lucy f_sad_talk
    lucy "Again?!"
    show lucy f_sad
    show richard f_angry_talk
    rich "Yes!"
    show richard f_angry
    show lucy f_sad_talk
    lucy "B-but you don't have to-"
    show lucy f_sad
    show richard f_angry_talk
    rich "I'm trying to build a business, {b}Lucy{/b}."
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "{b}*Sigh*{/b} I know."
    lucy "I just wish you were around more-"
    show lucy f_sad_down
    show richard f_angry_talk
    rich "You knew what you were signing up for when I started this company!"
    show richard f_angry
    lucy "..."
    show richard f_angry_talk
    rich "I, on the other hand, had no idea your stupid daycare was gonna be such a pain in my ass!"
    rich "I should never have agreed to it!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "I'm sorry... I-"
    show lucy f_sad_down
    pause
    show lucy f_sad_talk
    lucy "I'll just buy a new chair, okay?"
    lucy "Then you won't have to-"
    show lucy f_confused_talk
    show richard f_angry_yell a_dressed_frustrated with dissolve
    rich "NO!"
    show lucy f_sad_down
    show richard f_angry_talk
    rich "We can't afford that, {b}Lucy{/b}!"
    show richard f_angry_yell a_dressed_stop with dissolve
    rich "Arrggghh!!!"
    rich "Just-"
    show richard f_angry_talk a_dressed_frustrated with dissolve
    rich "Set the chair aside and I'll get to it when I get to it!"
    show richard f_angry
    show lucy f_sad_talk_down
    lucy "O-okay..."
    show lucy f_sad_down
    show richard f_stern_down a_dressed_watch with dissolve
    rich "I'm late for work!"
    show richard f_angry a_dressed_frustrated at unflip
    show richard at Position (xpos=-200)
    show player f_worried_talk
    player_name "Excuse me, I-"
    show player f_surprised
    show richard f_angry_talk a_dressed_stop with dissolve
    rich "I don't have time, talk to her!"
    hide richard with dissolve
    show player f_skeptical
    player_name "..."
    show player f_worried_talk
    player_name "Are you alright, ma'am?"
    show player f_worried
    show lucy f_sad_talk
    lucy "Hmm?"
    show lucy f_thinking
    lucy "Oh, yeah... I'm fine."
    show lucy f_sad_down
    show player f_worried_talk
    player_name "You sure?"
    show player f_worried
    show lucy f_normal
    lucy "Mmhmm."
    show lucy f_normal_talk
    lucy "What can I help you with?"
    show lucy f_normal
    show player f_worried_talk
    player_name "I'm looking for the daycare."
    show player f_worried
    show lucy f_normal_talk
    lucy "Well, you've found it!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Really?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Are you a father?"
    show lucy f_normal
    show player f_laugh
    player_name "Yes."
    show player f_grin
    show lucy f_normal_talk
    lucy "Aww, I bet your kid is just adorable!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Well, I think so!"
    show player f_normal
    show lucy f_laugh
    lucy "Hehe!"
    show lucy f_normal_talk
    lucy "Why don't you come inside and have a look around?"
    show lucy f_normal
    show player f_normal_talk
    player_name "I'd like that."
    show player f_normal
    show lucy f_normal_talk at flip
    show lucy at Position (xpos=1100)
    with dissolve
    lucy "I'll give you the whole tour."
    scene black with fade
    pause
    $ player.go_to(L_annie_daycare)
    scene expression player.location.background_blur
    show lucy f_normal_talk
    show player
    with fade
    lucy "... And over here is our arts and crafts table."
    show lucy f_normal
    show player f_normal_talk
    player_name "Wow, this is all really impressive..."
    player_name "... And all the kids seem so happy!"
    show player f_normal
    show lucy f_laugh
    lucy "Hehe, thanks!"
    show lucy f_normal
    show player f_normal_talk
    player_name "How many did you say you have right now?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Just eight at the moment."
    show lucy f_normal
    show player f_normal_talk
    player_name "This place is huge for just eight kids!"
    show player f_normal
    show lucy f_normal_talk
    lucy "Yeah, my husband went a little overboard building it."
    lucy "Honestly, I was hoping we'd get more but it's such a small town, you know?"
    lucy "Clients have been tough to come by..."
    show lucy f_normal
    show player f_normal_talk
    player_name "I can understand."
    show player f_normal
    show lucy f_normal_talk
    lucy "If you know anyone with kids, be sure to recommend us."
    show lucy f_normal
    show player f_normal_talk
    player_name "I definitely will."
    player_name "Thank you for the tour, Mrs-?"
    show player f_normal
    show lucy f_normal_talk
    lucy "Oh, you can just call me {b}Lucy{/b}."
    show lucy f_normal
    show player f_normal_talk
    player_name "Alright then, {b}Lucy{/b}."
    player_name "I'm {b}[firstname]{/b}."
    show player f_normal
    show lucy f_normal_talk
    lucy "It's been a pleasure meeting you, {b}[firstname]{/b}."
    lucy "Bring your little one next time!"
    show lucy f_normal
    show player f_normal_talk
    player_name "Will do."
    hide player with dissolve
    return

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
    player_name "Это кажется тебе несправедливым, {b}Люси{/b}..."
    show player 5
    show lucy f_normal_talk a_dressed_wave with dissolve
    lucy "О, все в порядке."
    show lucy a_dressed_sides with dissolve
    lucy "{b}Ричард{/b} никогда по-настоящему не хотел иметь детей."
    lucy "Я знала, во что ввязываюсь, когда убедила его завести {b}Энни{/b}."
    lucy "Я беспокоюсь о том, как это повлияло на нее."
    lucy "Она сделает все, чтобы получить одобрение отца."
    show lucy f_normal
    show player 35
    player_name "Хм, это объясняет некоторые вещи в ее поведении..."
    show player 34
    show lucy f_confused_talk
    lucy "О чем ты?"
    show lucy f_normal
    show player 10
    player_name "О, эээ... Ни о чем мэм'-"
    show player 14
    player_name "{b}*Гммм*{/b} Я имею в виду, ничего {b}Люси{/b}."
    player_name "Мне, наверное, уже пора начинать делать эти игрушки, да?"
    show player 13
    show lucy f_normal_talk
    lucy "Ты прав."
    lucy "Я должна уложить малышей спать."
    show lucy f_normal
    show player 10
    player_name "У {b}Ричарда{/b} есть какие-нибудь инструменты, которыми я могу воспользоваться?"
    show player 13
    show lucy f_laugh a_dressed_cover with dissolve
    lucy "Ха-ха, у {b}Ричарда{/b} есть какие-нибудь инструменты..."
    show lucy f_normal_talk a_dressed_sides with dissolve
    lucy "Иди проверь внутри дома, ты найдешь то, что тебе нужно."
    show lucy f_normal
    show player 14
    player_name "Спасибо."
    hide player
    hide lucy
    with dissolve
    return

label annies_house_livingroom_diane_delivery_2:
    scene expression "backgrounds/location_annie_frontyard_day_blur.jpg"
    show richard a_dressed_phone_talk f_phone_talk
    show player 13 at left
    with dissolve
    rich "Нет, абсолютно нет!"
    rich "Ну, мне все равно, если тебе это не нравится..."
    show player 5
    show richard f_phone
    pause
    show richard f_phone_talk
    rich "Нет..."
    rich "Дело в том, что это регулирование OSHA."
    rich "Нет, я все делаю строго по правилам!"
    rich "Я говорил тебе об этом, когда ты меня нанимал."
    show richard f_normal
    rich "..."
    show richard f_phone_talk
    rich "Нет, больше денег не заставит его исчезнуть."
    rich "Правила есть правила."
    rich "Слушай, мне нужно, чтобы ты подождал секунду."
    show richard f_normal_talk a_dressed_phone with dissolve
    rich "Я могу помочь?"
    show richard f_normal
    show player 12
    player_name "Эээ, наверно..."
    show player 239_240 with dissolve
    pause
    show player 163c with dissolve
    player_name "Я должен доставить это-"
    show player 163g
    show richard f_normal_talk
    rich "О, ты молочник..."
    rich "Фу, хорошо. Иди за мной."
    show richard a_dressed_phone_talk f_phone_talk at fliplright
    with dissolve
    rich "Итак, на чем мы остановились?"
    rich "Ах да, руководство OSHA статья 7..."
    hide richard with dissolve
    player_name "..."
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show richard a_dressed_phone f_normal_talk at flip, Position (xcenter=0.75)
    show player 163b at left
    with dissolve
    rich "{b}Люси{/b}!"
    rich "Молочник здесь!"
    show richard f_normal at flip, Position (xcenter=0.75)
    lucy "О, иду!"
    show richard a_dressed_phone f_normal_talk at unflip
    show richard at lcenter
    with dissolve
    rich "Его заказала моя жена."
    rich "Она с тобой разберется."
    show richard a_dressed_phone_talk f_phone at flip, Position (xcenter=0.75) with dissolve
    show player 163c
    player_name "Х-хорошо."
    show player 163b
    show lucy f_normal_talk at Position (xpos=650) with dissolve
    lucy "Фу, эти дети изматывают меня!"
    show lucy f_normal
    show richard f_phone_talk at flip
    rich "Угу..."
    show richard f_phone at flip
    show lucy f_normal_talk
    lucy "{b}Ричард{/b}, не могли бы вы, мм... Помочь донести это до дома?"
    show lucy f_normal
    show richard f_angry_talk at flip
    rich "Не сейчас, {b}Люси{/b}! Разве ты не видишь, что я разговариваю по телефону с клиентом?!"
    show richard f_phone_talk at flip
    rich "Ой, извини... Секундочку."
    show richard a_dressed_phone f_angry_talk at flip with dissolve
    rich "Этот детский сад был твоей глупой идеей, и ты должна справиться с этим самостоятельно!"
    show lucy f_sad
    rich "... И убедитесь, что ты пересчитала деньги на этот раз, прежде чем передать их!"
    rich "С деньгами итак достаточно туго, не надо бросать их на ветер!"
    show richard f_angry at flip
    show lucy f_sad_talk
    show player 163g
    lucy "Да, милый..."
    show lucy f_sad_down
    hide richard with dissolve
    rich "Извини, снова об этом..."
    lucy "..."
    show player 163c
    player_name "Я помогу Вам, мэм."
    show player 163b
    show lucy f_sad_talk
    lucy "В этом нет необходимости. Я уверена, что у вас много-"
    show lucy f_sad
    show player 163c
    player_name "Я настаиваю."
    show player 163b
    show lucy f_normal
    lucy "..."
    show lucy f_normal_talk
    lucy "Ну, разве ты не прелесть!"
    lucy "Позвольте мне позвать дочь, чтобы присмотреть за детьми."
    show lucy f_normal
    show player 163c
    player_name "Да, хорошо."
    show player 163b
    hide lucy with dissolve
    player_name "..."
    lucy "{b}Энни{/b}, милая?"
    lucy "Не могла ли ты помочь мне на секунду?"
    ann "Ух, Я как раз выходила за дверь, {b}Мам{/b}..."
    lucy "Ты мне нужна всего на пару минут."
    ann "Аххх!!!"
    show annie 7 at Position (xpos=600)
    show lucy f_normal at Position (xpos=650)
    with dissolve
    ann "Лучше бы мне не опаздывать!"
    ann "{b}Миссис Смит{/b} терпеть не может-"
    show annie 1
    ann "..."
    show annie 4
    ann "Что он здесь делает?"
    show annie 6
    lucy "Хмм?"
    show lucy f_confused_talk
    lucy "Вы двое знаете друг друга?"
    show lucy f_confused
    show player 163c
    player_name "Мы учимся в одном классе в школе."
    show player 163b
    show lucy f_laugh
    lucy "Ну, разве это не прекрасно?"
    show lucy f_normal
    show annie 5
    ann "Едва..."
    show annie 6
     if not L_annie_front.first_visit:
        show lucy f_normal_talk
        lucy "He's brought us more of that wonderful milk the children like so much."
        show lucy f_normal
        show annie 3
        ann "You work for a milk company?"
        show annie 1
        show player 163c
        player_name "Well, my friend {b}Diane{/b} owns the company."
        player_name "I just help her out as much as possible."
        show player 163b
    else:
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
    lucy "О, боже."
    show lucy f_normal_talk
    lucy "Надеюсь, ты дружишь с ним, {b}Энни{/b}?"
    lucy "Он мне нравится!"
    show lucy f_normal
    show annie 3
    ann "Он преступник!"
    show annie 1
    show player 163g
    show lucy f_normal_talk
    lucy "О, не называй его так!"
    show lucy f_normal
    show annie 4
    ann "... Вот кто он такой!"
    show annie 1
    show lucy f_normal_talk
    lucy "{b}[firstname]{/b}, предлагал перетащить все это молоко внутрь для меня."
    lucy "Присмотришь за детьми, пока я ему помогу?"
    show player 163b
    show lucy f_normal
    show annie 4f with dissolve
    ann "Нет! Ни за что!"
    ann "Ты же знаешь, я НЕНАВИЖУ детей!"
    show annie 1f
    show lucy f_normal_talk
    lucy "Пожалууууууууйста?"
    lucy "Это займет всего минуту."
    show lucy f_normal
    show annie 6f
    ann "..."
    show annie 5f
    ann "Почему {b}папа{/b} не может это сделать?!"
    show annie 6f
    show lucy f_normal_talk
    lucy "Он разговаривает по телефону с клиентом."
    show lucy f_normal
    show annie 5f
    ann "... Этот идиот все еще жалуется на правила OSHA?!"
    ann "Это не похоже на то, что {b}папа{/b} написал правила, он просто соблюдает их, как любой приличный человек..."
    show annie 6f
    show lucy f_confused_talk
    lucy "Я не-"
    show lucy f_confused
    lucy "..."
    show lucy f_confused_talk
    lucy "Что такое OSHA?"
    show lucy f_confused
    show annie 7f
    ann "Эххррр!! Неважно..."
    show annie 4f
    ann "Просто поторопись!"
    hide annie
    show lucy hug_annie
    with dissolve
    lucy "Спасибо, дорогая!"
    lucy "Иди за мной, {b}[firstname]{/b}!"
    show annie 6f at Position (xpos=600)
    hide lucy
    with dissolve
    show player 163c
    player_name "Да, мэм."
    hide player with dissolve
    ann "..."
    show annie 4f
    ann "Эй! Хватит бегать!!"
    hide annie with dissolve
    ann "Эй, не клади это себе в рот!!!"
    scene expression "backgrounds/location_annie_livingroom_day_blur.jpg"
    show lucy bend
    show player 426 at left
    with dissolve
    lucy "Хорошо, все выглядит неплохо."
    lucy "Я не знаю, что вы все кладете в это молоко, но дети просто не могут насытиться!"
    player_name "Мммммм."
    lucy "Все это исчезнет через пару недель."
    lucy "В следующий раз мне нужно будет заказать намного больше."
    lucy "Если {b}Ричард{/b} мне позволит."
    player_name "..."
    lucy "Это не будет проблемой, не так ли?"
    player_name "..."
    show lucy f_confused_talk at Position (xpos=650)
    lucy "{b}[firstname]{/b}?"
    show lucy f_confused
    show player 11
    player_name "!!!"
    show player 29 with dissolve
    player_name "Простите, это было в последний раз?"
    show player 3
    show lucy f_normal_talk
    lucy "Я сказала, что в следующий раз мне нужно будет заказать больше, если вы не против?"
    show lucy f_normal
    show player 29
    player_name "... Да, я тоже так думаю."
    show player 17 with dissolve
    player_name "Я поговорю об этом с {b}Дианой{/b}."
    show player 13
    show lucy f_laugh
    lucy "Замечательно!"
    show lucy f_normal_talk
    lucy "Что касается вашей оплаты..."
    show lucy f_normal_down a_dressed_cleavage with dissolve
    show player 11
    player_name "!!!"
    show lucy a_dressed_money with dissolve
    lucy "Это должно покрыть все расходы."
    show lucy f_normal a_dressed_sides
    show player 638b at Position (xoffset=-19)
    with dissolve
    player_name "..."
    show player 638 at Position (xoffset=-21)
    player_name "Ох, это слишком много."
    show player 13
    show lucy a_dressed_money f_normal_down with dissolve
    lucy "..."
    show player 14
    player_name "Это на пятьдесят долларов больше стоимости..."
    show player 13
    show lucy f_confused_talk
    lucy "!!!"
    show lucy f_laugh
    lucy "Упс!"
    show lucy f_normal_talk
    lucy "Хе-хе, у меня так много денег..."
    show lucy f_laugh a_dressed_cleavage with dissolve
    lucy "... А ты просто милашка!"
    hide player
    show lucy hug_mc
    with dissolve
    lucy "Спасибо за честность, {b}[firstname]{/b}!"
    player_name "!!!"
    pause
    show player 29 at left
    show lucy f_normal
    with dissolve
    player_name "Хех. Н-никаких проблем, мэм."
    player_name "Я не хочу, чтобы твой муж снова на тебя разозлился."
    show player 3
    show lucy f_confused
    lucy "Хмм?"
    show lucy f_laugh a_dressed_wave with dissolve
    lucy "О! Нет..."
    show player 13 with dissolve
    lucy "Он просто так занят {b}своими плотницкими делами{/b} и все такое!"
    lucy "У него нет времени на меня и мои проблемы."
    show lucy f_normal a_dressed_sides with dissolve
    player_name "..."
    show player 10
    player_name "Он {b}плотник{/b}?"
    show player 5
    lucy "Мммммм."
    show lucy f_sad_talk
    lucy "Он занимается этим более 20 лет."
    lucy "Бедняжка, работает до мозга костей."
    show lucy f_sad
    show player 12
    player_name "Ну, он должен найти время."
    show player 14
    player_name "Вы такая милая леди!"
    show player 13
    show lucy f_normal_talk
    lucy "Ой, ну спасибо, {b}[firstname]{/b}!"
    lucy "Ты тоже милый!"
    show lucy f_normal
    ann "НЕ БРОСАЙТЕ ВЕЩИ!!!" with hpunch
    show player 11
    player_name "!!!"
    show lucy f_confused
    ann "ААААААА!!"
    show lucy f_confused_talk
    lucy "Ой..."
    show player 13
    lucy "Звучит так,будто дети берут верх над {b}Энни{/b}."
    lucy "Я лучше пойду спасу ее!"
    hide lucy with dissolve
    player_name "..."
    show player 17
    player_name "( О, я должен это проверить! )"
    hide player with dissolve
    scene expression "backgrounds/location_annie_daycare_day_blur.jpg"
    show annie 25 at right
    show player 11 at Position (xpos=400)
    show lucy f_confused at fliplleft
    with dissolve
    ann "Я СКАЗАЛА ВАМ ПЕРЕСТАТЬ БЕГАТЬ!!!"
    show annie 24
    pause
    show annie 25
    ann "Наконец-то!"
    ann "Почему ты так долго?!"
    show annie 24
    show lucy f_confused_talk
    lucy "Мне очень жаль, дорогая. Я-"
    show lucy f_confused
    show annie 25
    ann "Посмотри на меня, я теперь катастрофа!"
    ann "Мне снова придется принимать душ!"
    show annie 24
    show lucy f_sad_down
    lucy "..."
    show annie 25
    ann "Спасибо большое {b}Мам{/b}!"
    show annie 26 with dissolve
    pause
    hide annie with dissolve
    pause
    show player 10f at right with dissolve
    player_name "Ничего себе, это было..."
    player_name "... Вы в порядке, мэм?"
    show player 5f
    show lucy f_sad
    lucy "Хмм?"
    show lucy f_sad_talk
    lucy "О, все хорошо."
    show lucy f_sad
    lucy "..."
    show lucy f_sad_talk
    lucy "Еще раз спасибо за помощь сегодня, {b}[firstname]{/b}."
    show lucy f_sad
    show player 14f
    player_name "Это не было проблемой, мэм."
    player_name "Увидимся в следующий раз."
    show player 13f
    hide lucy with dissolve
    pause
    show player 5f
    player_name "( Бедная женщина... )"
    pause
    show player 18f
    player_name "( Ну, я должен вернуть эти деньги {b}Диане{/b} и сказать ей, что в следующий раз детскому саду понадобится больше. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
