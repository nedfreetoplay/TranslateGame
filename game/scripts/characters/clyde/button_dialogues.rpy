label button_clyde_pink_beaver:
    scene expression player.location.background_blur with None
    show player 14f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "Эй, насчет бобра, которого ты хотел."
    show player 13f
    show clyde 2
    clyde "Да?"
    show clyde 1
    show player 239_240f
    pause
    show player 709f
    player_name "Это он?"
    show player 708f
    show clyde 30
    clyde "!!!"
    show clyde 4 with dissolve
    clyde "Ну, смажь мою попку и назови меня печеньем, ты на самом деле понял!"
    show clyde 3
    show player 709f
    player_name "Я думал, что это может быть."
    show clyde 34
    show player 13f
    with dissolve
    pause
    show clyde 35
    clyde "Как, черт возьми, ты выиграл эту штуку?!"
    show clyde 33 with dissolve
    clyde "Ярмарки не будет еще 2 месяца!"
    show clyde 32
    show player 12f
    player_name "Я купил его в торговом центре, {b}Клайд{/b}."
    show player 5f
    show clyde 2 with dissolve
    clyde "В торговом центре?"
    clyde "А, черт."
    clyde "Я никогда там не был."
    clyde "Куда эта собака убежала сейчас?"
    clyde "Давай, девочка!"
    show clyde 1
    pause
    show player 10f
    player_name "Подожди. Ты никогда не был в торговом центре?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Нет, сэр."
    show clyde 3
    show player 10f
    player_name "Где ты тогда покупаешь продукты?"
    show player 5f
    show clyde 4
    clyde "Пффф, вы горожане и ваши продукты..."
    clyde "Я никому не буду платить за то, что бесплатно прямо здесь, в лесу!"
    show clyde 3
    show player 10f
    player_name "... Ааа?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Я охочусь за едой, приятель."
    show clyde 4 with dissolve
    clyde "Кстати, у меня в хижине есть горшочек тушеной белки."
    clyde "Приходи к нам на ужин!"
    show clyde 3
    show player 12f
    player_name "Йее, нет спасибо."
    show player 5f
    pig "{b}*хрююююю*{/b}"
    show clyde 4
    clyde "Вот ты где!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Где же ты была, моя девочка?!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 38
    with dissolve
    pig "*{b}Хрю{/b}*"
    show clyde 37
    clyde "Посмотри, что {b}[firstname]{/b} принес для тебя!"
    show clyde 38
    pig "{b}*ХРЮЮ ХРЮЮ*{/b}"
    show clyde 37
    clyde "Хехехе, посмотри, как она счастлива!"
    if M_clyde.get("cletus"):
        show clyde_hat down
    show clyde 36
    with dissolve
    clyde "Иди и повеселись сейчас же!"
    if M_clyde.get("cletus"):
        show clyde_hat
    show clyde 3
    with dissolve
    pig "{b}*фырк*{/b}"
    pause
    show clyde 4
    clyde "Теперь это одна счастливая собака."
    clyde "Ладно, парень..."
    show clyde 9 with dissolve
    clyde "Я должен как-то отплатить тебе за это."
    show clyde 3 with dissolve
    show player 12f
    player_name "Не беспокойтесь об этом."
    player_name "Просто считай это подарком."
    show player 5f
    show clyde 4
    clyde "Теперь подожди секунду."
    show clyde 1 with dissolve
    pause
    show clyde 9 with dissolve
    clyde "О!"
    clyde "У меня как раз то, что надо!"
    hide clyde
    hide clyde_hat
    with dissolve
    show player 10f
    player_name "Куда это ты собрался?!"
    show player 5f
    clyde "Подожди здесь!"
    pause
    clyde "Не двигай мышцами!"
    show player 25f
    player_name "О, блин."
    player_name "Правда, хорошо..."
    player_name "Я не-"
    show player 11f
    show clyde 40 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    with dissolve
    clyde "Зацени!"
    show clyde 39
    if player.has_item("mysterious_statue_1"):
        show player 23f
        player_name "!!!"
        show player 30f
        if M_clyde.get("cletus"):
            player_name "{b}Клайд{/b}, Я думал, ты сказал, что ничего не знаешь о статуе своего деда!"
        else:
            player_name "{b}Клетус{/b}, Я думал, ты сказал, что ничего не знаешь о статуе своего деда!"
        show player 90f
        show clyde 40
        clyde "О, точно."
        clyde "Я ведь это и сказал, не так ли?"
        show clyde 39
        pause
        show clyde 11 with dissolve
        clyde "Ну, я просто соврал."
        show clyde 12
        show player 12f
        player_name "Почему?!"
        show player 90f
    else:

        player_name "!!!"
        show player 30f
        player_name "Что это за хрень?"
        show player 5f
        show clyde 40
        clyde "Ну, это принадлежало моему дедушке."
        show clyde 39
        show player 10f
        player_name "Твоему дедушке?!"
        show player 5f
        show clyde 9 with dissolve
        clyde "Точно!"
        clyde "Оле {b}Джебедия Дельмонт{/b} вообще-то!"
        show clyde 3
        pause
        player_name "..."
        show clyde 2 with dissolve
        clyde "Ты никогда не слышал о {b}Джебедия Дельмонте{/b}?"
        show clyde 1
        show player 10f
        player_name "Нет?"
        show player 5f
        show clyde 2
        clyde "{b}*вздыхая*{/b} Боже мой."
        show clyde 4 with dissolve
        clyde "Он славился в этих краях своими коровами и их восхитительным молоком!"
        clyde "Он побеждал во всевозможных конкурсах."
        show clyde 3
        show player 10f
        player_name "Он был молочным фермером?"
        show player 5f
        show clyde 4
        clyde "Ну, он не просто занимался молочной фермой."
        clyde "У него были разные животные."
        show clyde 9 with dissolve
        clyde "Видели бы вы куриные яйца, которые он приносил на ярмарку."
        clyde "Они были размером с футбольный мяч!"
        show clyde 3 with dissolve
        show player 10f
        player_name "Да ну?"
        show player 5f
        show clyde 4
        clyde "Хе, да, чувак!"
        show clyde 3
        pause
        show player 17f
        player_name "Звучит потрясающе!"
        show player 14f
        player_name "Расскажи больше."
        show player 13f
        show clyde 11 with dissolve
        clyde "О, нет. Я эээ-"
        clyde "{b}*ммммм*{/b} Я правда не хочу в это ввязываться..."
        show clyde 12
        show player 10f
        player_name "Хух, почему нет?"
        show player 5f
    show clyde 11
    clyde "Слушай, приятель, мой дедушка не совсем гордость {b}семьи Дельмонт{/b}..."
    clyde "Мы не любим об этом говорить!"
    show clyde 12
    show player 10f
    player_name "Почему?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*вздыхая*{/b} Давайте просто скажем, что Оле' {b}Джебедия{/b} был немного тронутый, хорошо?"
    show clyde 1
    show player 10f
    player_name "Был немного тронутый?"
    show player 5f
    show clyde 2
    clyde "Ну ты понимаешь."
    clyde "У него нехватало несколько винтов."
    show clyde 1
    show player 10f
    player_name "Эээ..."
    show player 5f
    show clyde 9 with dissolve
    clyde "Его колесо поворачивалось, но хомяк был мертв."
    show clyde 3 with dissolve
    show player 10f
    player_name "Я не..."
    show player 5f
    show clyde 4
    clyde "Ему не хватило нескольких карт до полной колоды."
    show clyde 3
    show player 12f
    player_name "О чем ты говоришь?!"
    show player 5f
    show clyde 26 with dissolve
    clyde "Tch, he was nuttier than a porta potty at a peanut festival, alright?!"
    show clyde 25
    show player 12f
    player_name "You mean he was crazy?"
    show player 5f
    show clyde 26
    clyde "That's what I've been tryin' to tell ya..."
    show clyde 25
    show player 10f
    player_name "Oh."
    show player 5f
    show clyde 2
    clyde "Yeah."
    clyde "Mama says he was always a bit eccentric."
    clyde "Folk in the holler used to call him the hillbilly wizard."
    show clyde 1
    show player 10f
    player_name "He was a wizard?"
    show player 5f
    show clyde 2
    clyde "Yeah, but he wasn't a very good one."
    clyde "I remember, he tried turnin' me into a toad one time, cause I had gone and got my head stuck in the stairs."
    show clyde 1
    show player 10f
    player_name "You got your head stuck in the stairs?!"
    show player 5f
    show clyde 2
    clyde "My brother told me there was a leprechaun livin' under the stairs and I wanted to see him."
    show clyde 1
    show player 17f
    player_name "Pfft, hahaha!"
    show player 13f
    show clyde 2
    clyde "Anyways, his spell didn't work."
    show clyde 11 with dissolve
    clyde "So Mama had to grease me up with bacon fat and slide me out."
    show clyde 12
    show player 17f
    player_name "Haha!"
    show player 13f
    show clyde 4
    clyde "Then there was this one time, I was failin' the second grade..."
    clyde "... And grandpappy, he said, \"Don't you worry none little {b}Clyde{/b}. Grandpappy will fix it right up fer ya.\""
    show clyde 3
    pause
    show player 14f
    player_name "Okay, so what happened?"
    show player 13f
    show clyde 2 with dissolve
    clyde "Well, I don't rightly know. They found him in the school house, in the middle of the night, buck naked and covered in chicken blood."
    show clyde 1
    show player 23f
    player_name "Chicken blood?!"
    show player 11f
    show clyde 2
    clyde "Yeah, he said he was performin' some kinda ritual thingy to help me with my schoolin'."
    clyde "Apparently he was a hootin' and a hollerin' and a carryin' on."
    show clyde 1
    show player 10f
    player_name "Yeah, he does sound a little crazy, {b}Clyde{/b}."
    show player 12f
    show clyde 2
    clyde "Yeah, I reckon he was."
    clyde "He was a sweet ole' feller though."
    clyde "It's too bad all dem evil spirits got mad at him."
    show clyde 1
    show player 10f
    player_name "Evil spirits?"
    show player 11f
    show clyde 2
    clyde "Yeah, he told me all about it right after he broke this here statue and hid the pieces."
    clyde "Said they was coming fer him and he wanted her to be safe."
    show clyde 1
    show player 10f
    player_name "Her?"
    show player 5f
    show clyde 40 with dissolve
    clyde "The lady in the statue, of course!"
    clyde "He was real tore up about hiding her away."
    clyde "She was his good luck charm after all."
    show clyde 39
    show player 12f
    player_name "Weird."
    show player 5f
    show clyde 9 with dissolve
    clyde "Then we caught him fornicatin' with the livestock and Mama sent him off to the nut house."
    show clyde 3 with dissolve
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "You mean he-"
    player_name "W-with animals?!"
    show player 37f
    show clyde 11
    with dissolve
    clyde "{b}*Sigh*{/b} Yup, crying like a baby too."
    clyde "Them spirits musta really done a number on him, poor feller."
    show clyde 12
    show player 10f with dissolve
    player_name "So uhh..."
    player_name "... Is your grandpa still living at the nut house then?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ah, nah."
    clyde "About two weeks after Mama sent him there, his room caught on fire and he burnt up in it."
    show clyde 1
    show player 24f
    player_name "Jesus..."
    show clyde 2
    clyde "They not sure how the fire started but I reckon them spirits finally got him."
    show clyde 1
    player_name "I don't even..."
    player_name "..."
    show clyde 30
    clyde "Yeah, it was real sad..."
    show clyde 29
    pause
    show player 11f
    show clyde 2
    clyde "Anyways!"
    show player 5f
    show clyde 40 with dissolve
    clyde "I reckon he wouldn't mind me giving you this piece of the statue."
    clyde "Seein' as you helped me and all."
    clyde "Who knows, maybe it'll bring you luck too."
    show clyde 39
    show player 10f
    player_name "R-right."
    player_name "Thanks, I guess..."
    show player 715f
    show clyde 9
    with dissolve
    clyde "Don't mention it, buddy!"
    show player 5f with dissolve
    clyde "Now if you'll excuse me."
    clyde "I wanna watch my dog give that ole' beaver what fer!"
    hide clyde
    hide clyde_hat
    with dissolve
    clyde "Hehehe."
    show player 239_240f with dissolve
    pause
    show player 715f with dissolve
    player_name "( You know, this actually explains quite a lot about {b}Clyde{/b} and why he is the way he is... )"
    pause
    player_name "( I guess I should keep an eye out for the other pieces of this statue. )"
    hide player with dissolve
    return

label button_clyde_mysterious_statue_1:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 688cf
    player_name "You know anything about this {b}Clyde{/b}?"
    show player 688bf
    show clyde 30
    clyde "{b}*Gasp*{/b} Where in the world did you find that?!"
    show clyde 29
    show player 688cf
    player_name "It was buried under my friends house."
    show player 688bf
    pause
    show player 688cf
    player_name "The name {b}Delmont{/b} is etched in the bottom."
    show player 688bf
    show clyde 2
    clyde "Yeah."
    show clyde 4 with dissolve
    clyde "It's part of my grandpappy's good luck charm."
    show clyde 3
    show player 688cf
    player_name "Grandpappy?"
    player_name "You mean your grandfather?"
    show player 13f with dissolve
    show clyde 4
    clyde "Uh huh, {b}Jebadiah Delmont{/b}."
    clyde "He was real famous in these parts many years ago for the milk his cows produced."
    show clyde 3
    show player 10f
    player_name "Cow milk?"
    show player 5f
    clyde "Mmhmm."
    show clyde 4
    clyde "It was delicious!"
    clyde "Won a bunch of contests with it."
    show clyde 3
    show player 14f
    player_name "That's pretty cool."
    show player 13f
    show clyde 4
    clyde "He had some amazing chicken eggs too."
    clyde "They was big as a football!"
    show clyde 3
    pause
    show player 12f
    player_name "Right..."
    show player 5f
    pause
    show player 10f
    player_name "So uhh..."
    player_name "Do you know where the rest of this statue might be?"
    show player 5f
    show clyde 11 with dissolve
    clyde "Nope!"
    show clyde 12
    pause
    show player 10f
    player_name "Oh, cause I just thought-"
    show player 5f
    show clyde 9 with dissolve
    clyde "Sorry feller, can't help ya!"
    clyde "I dun know squat!"
    show clyde 3 with dissolve
    show player 10f
    player_name "Alright..."
    show player 24f
    player_name "Thanks anyways, I guess."
    show player 5f
    show clyde 1 with dissolve
    return

label button_clyde_mysterious_statue_2:
    scene expression player.location.background_blur with None
    show player 239_240f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    pause
    show player 715bf with dissolve
    player_name "Any idea where I can find more of this statue?"
    show player 715cf
    show clyde 2
    clyde "Erm, not really."
    clyde "Knowin' grandpappy, that last piece will probably {b}find you{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "What do you mean?"
    show player 5f
    show clyde 2
    clyde "Yeah, I reckon I'd prolly jus' {b}find a nice comfy place to relax{/b}..."
    clyde "... {b}somewheres near the beach, maybe{/b}."
    show clyde 1
    pause
    show clyde 2
    clyde "I betcha' {b}that head will pop up all on it's own{/b}."
    show clyde 1
    show player 10f with dissolve
    player_name "Ehh, right..."
    player_name "Well, thanks. I guess..."
    show player 5f
    show clyde 9 with dissolve
    clyde "No problem, buddy."
    show clyde 1 with dissolve
    return


label button_clyde_your_dog:
    scene expression player.location.background_blur with None
    show player 10f at right
    show clyde 1 at left
    if M_clyde.get("cletus"):
        show clyde_hat at left
    player_name "So, about your dog..."
    show player 5f
    show clyde 4 with dissolve
    clyde "Ah yeah, she's a good girl ain't she?"
    show clyde 3
    show player 10f
    player_name "Okay, sure."
    show player 12f
    player_name "You realize she isn't a dog though, right?"
    show player 5f
    show clyde 4
    clyde "Best dog I ever had!"
    show clyde 3
    show player 24f
    player_name "{b}*Sigh*{/b}"
    show player 5f
    show clyde 4
    clyde "That's why I'm practicin' so hard, to win her one of dem {b}stuffed beavers{/b} at the fair."
    show clyde 3
    show player 12f
    player_name "Yeah, you mentioned that."
    show player 10f
    player_name "Why don't you just buy her one?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Psh, now you'se talkin' crazy..."
    clyde "What, you think {b}Pink beavers{/b} jus' be growin' on trees or somethin'?"
    show clyde 3 with dissolve
    show player 10f
    player_name "Does the color really matter?"
    show player 5f
    show clyde 4
    clyde "Heck ya it matters!"
    clyde "{b}Pink beavers{/b} is the best beavers."
    show clyde 9 with dissolve
    clyde "Ever'body knows dat!"
    show clyde 3 with dissolve
    show player 402f
    player_name "... Right."
    show player 10f
    player_name "Okay, well good luck with all that I guess..."
    show player 5f
    show clyde 4
    clyde "\"Luck\" is my middle name, brother."
    show clyde 3
    pause
    show clyde 2 with dissolve
    clyde "Actually it's Cornelius."
    show clyde 1
    show player 12f
    player_name "Huh?"
    show player 5f
    show clyde 2
    if M_clyde.get("cletus"):
        clyde "{b}Cletus Cornelius Delmont{/b}."
    else:
        clyde "{b}Clyde Cornelius Delmont{/b}."
    show clyde 1
    show player 10f
    player_name "You're middle name is Cornelius?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Yeah buddy."
    clyde "Like that prospector fella on the flyin' Reindeer show."
    show clyde 4
    clyde "You seen dat one?!"
    show clyde 3
    show player 10f
    player_name "I don't think so..."
    show player 5f
    show clyde 4
    clyde "Maaan, das a great one!"
    show clyde 3
    show player 10f
    player_name "You're a weird guy, {b}Clyde{/b}."
    show player 5f
    show clyde 4
    clyde "Uh huh!"
    show clyde 1 with dissolve
    return

label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Нам нужно поговорить об этой ситуации с {b}Кристалл{/b}."
    show player 5f
    show clyde 22
    clyde "Я бы предпочел не..."
    show clyde 21
    show player 10f
    player_name "{b}Клайд{/b}, они собираются отправить ее в тюрьму и забрать трейлер!"
    show player 5f
    show clyde 26
    clyde "Послушай дорогой! Ты думаешь что я не знаю об этом!"
    clyde "Я сожалею, но я ничего не могу, я не могу это прекратить!"
    show clyde 25
    show player 12f
    player_name "Ты можешь сдаться..."
    show player 5f
    show clyde 22
    clyde "Да точно..."
    clyde "Тогда мы оба и окажемся за решёткой!"
    show clyde 21
    show player 10f
    player_name "Нет, если ты скажешь им, что {b}Кристалл{/b} понятия не имела, что ты спрятал там наркотики."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... И зачем мне это?"
    show clyde 1
    show player 12f
    player_name "... Потому что это будет правильным решением!"
    show player 90f
    show clyde 2
    clyde "Пффф."
    clyde "Я не хочу попасть в тюрьму!"
    clyde "Красивому парню как я, эти животные сожрут меня заживо."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Смотри чувак. Она взяла вину на себя, потому что она твоя семья."
    player_name "... Но это было гораздо хуже чем она думала!"
    player_name "Она может изчезнуть на долгое время и {b}Рокси{/b} потеряет свою {b}Маму{/b} и свой дом."
    show player 12f
    player_name "{b}Рокси{/b} не сделала ничего, чтобы заслужить это!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Ох, дерьмо! Ты прав."
    clyde "{b}Роксанна{/b} не должна страдать по моей вине..."
    clyde "... Но Я не вернусь обратно в тюрьму! ... Нет, сэр!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "Что если бы ты послал своё признание в письменном виде?"
    player_name "Расскажи им о своей хижине и пусть они придут и найдут доказательства."
    player_name "Если ты все сделаешь правильно, ты можешь быть уже далеко до того,как они начнут тебя искать."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "Наверное, я мог бы вернуться в долину..."
    clyde "Они никогда не смогут найти меня там."
    clyde "... Я уверен что точно буду скучать по {b}Тете Кристалл{/b} все-таки..."
    show clyde 21
    show player 10f
    player_name "Ты спасешь её из тюрьмы, мужик."
    show player 5f
    show clyde 22
    clyde "Хмм, Я думаю у тебя хороший план."
    show player 13f
    clyde "Значит, я сделаю это, и она выйдет безнаказанной?"
    show clyde 21
    show player 12f
    player_name "... Мы все ещё должны прийти с деньгами за её залог, но для начала неплохо."
    show player 5f
    show clyde 22
    clyde "Сколько денег тебе нужно?"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Мда."
    clyde "Ну, я могу это сделать!"
    show clyde 1
    show player 10f
    player_name "Что?!" with hpunch
    player_name "Ты же не серьезно..."
    player_name "У тебя есть $50,000 завалявшиеся где-то?"
    show player 11f
    show clyde 2
    clyde "Не совсем."
    show clyde 4 with dissolve
    clyde "... Но у меня есть целая куча метамфитомина."
    clyde "Этого будет достаточно что бы получить $100,000 с хорошего покупателя, Я думаю."
    show clyde 3
    show player 10f
    player_name "Это безумие."
    player_name "Ты реально можешь продать его?"
    show player 5f
    show clyde 4
    clyde "Пффф! Да ладно дружище..."
    clyde "Ты хоть знаешь с кем ты разговариваешь?"
    clyde "Я могу продать эскимо с кетчупом девушке в белых перчатках!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Замороженый кетчуп?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да, дружище!"
    show clyde 3 with dissolve
    show player 14f
    player_name "... Когда ты сможешь это сделать?"
    show player 13f
    show clyde 4
    clyde "Хммм, мне нужно будет позвонить моему покупателю."
    clyde "... Но очень скоро, я думаю."
    show clyde 3
    show player 14f
    player_name "Мне надо рассказать {b}Рокси{/b} хорошие новости!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]Ты просто трус!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Эй, тебе не надо называть меня {b}меня{/b} трусом!"
    clyde "[chr_warn]Ты не предстовляешь себе какого это быть в тюрьме для кого то вроде меня!"
    clyde "[chr_warn]Я когда-то был там однажды и будь я проклят если бы я не вернулся назад."
    show clyde 25
    show player 15f
    player_name "[chr_warn]Неважно... {b}ТРУС{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Да пошел ты!"
    clyde "[chr_warn]Я не приму это!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Угх, забей!"
    show player 90f
    show clyde 22
    clyde "Да, это именно то, что я планирую сделать!"
    clyde "Я так кумекаю, шо энто пивко к концу банки и так всю память начисто отшибет!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Когда ты сможешь продать этот Мет?"
    show player 5f
    show clyde 2
    clyde "Притормози конец, парень!"
    clyde "Это требуем времени."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Просто иди и скажи моей сладкой {b}кузине{/b}, что {b}Клайд{/b} позаботитьтся обо всем!"
    show clyde 1
    show player 14f
    player_name "... Верно."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Ты уже связался со своим покупателем?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Да, приятель!"
    show player 13f
    clyde "Я намериваюсь заключить с ним сделку!"
    show clyde 3
    show player 12f
    player_name "{b}Рокси{/b} сказала, что ты не торгавал Метом раньше!"
    show player 90f
    show clyde 26 with dissolve
    clyde "Что?!"
    clyde "Она ничего не знает!"
    clyde "У меня было много таких сделок!"
    show clyde 25
    show player 12f
    player_name "Ты на самом деле имел дело с покупателями раньше?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Ну, я видел как {b}Тетя Кристалл{/b} делала это много раз!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Вздох*{/b} Я пойду с тобой."
    show player 90f with dissolve
    show clyde 2
    clyde "Хм?"
    clyde "Что ты знаешь о продаже наркотиков?!"
    show clyde 1
    show player 12f
    player_name "Ни черта не смыслю в этом."
    player_name "... Но Я точно знаю, что ты определенно недостаточно компетентен, чтобы сделать это в одиночку."
    show player 90f
    show clyde 22
    clyde "Ну, это не... Подожди секунду, что ты имел в виду?!"
    show clyde 1
    show player 12f
    player_name "... Именно."
    show player 90f
    show clyde 2
    clyde "Ччч, Неважно, парень."
    clyde "Пойдешь или не пойдешь. Это не важно для меня!"
    show clyde 26
    clyde "... Но если ты пойдешь то лучше бы тебе {b}встретиться со мной в трейлире вечером{/b}."
    clyde "Ты понял?"
    show clyde 1
    show player 12f
    player_name "Да, я понял."
    player_name "Увидимся {b}сегодня в трейлере Рокси{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Мы все по прежнему хороши что бы продавать мет?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Уверен"
    clyde "Просто будть здесь {b}вечером{/b}, если увязался со мной."
    show clyde 3
    show player 12f
    player_name "Да, понял."
    player_name "Увидимся {b}вечером{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Ты готов идти?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Ты одел это?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "Что не так с моей одеждой?"
    show player 5f
    show clyde 2
    clyde "Ого... Не знаю, приятель. Ты выглядишь ужасно подозрительно..."
    clyde "Я уверен, что ни за что не куплю наркотики у кого-то похожего на тебя."
    show clyde 1
    show player 10f
    player_name "Ну, у меня другой одежды не было..."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Подожди секунду. У меня есть кое что получше для тебя!"
    hide clyde with dissolve
    show player 12f
    player_name "... Это будет интересно."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Давай парень..."
    clyde "Не заставляй нас опоздать!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Я не верю что ты уговорил меня надеть это..."
    player_name "Я чувствую себя глупо!"
    show player 90f
    show clyde 4
    clyde "Шшш, не будь глупцом."
    clyde "Ты похож на настоящего торговца!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Покупатель может придти с секунды на секунду."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Клайд{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Когда ты вернешься в город?!"
    show player 5f
    show clyde 2
    clyde "Эээ, прости приятель."
    clyde "Ты ошибся приятеля..."
    show clyde 1
    show player 10f
    player_name "Хм?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Меня зовут {b}Клетус{/b}!"
    clyde "Рад познакомиться с тобой!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "О чем ты говоришь, {b}Клайд{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Кгхм*{/b} Ешё раз..."
    clyde "Мое имя не {b}Клайд{/b}... а {b}Клетус{/b}."
    show clyde 1
    show player 12f
    player_name "... Но ты так похож на кузена {b}Рокси{/b}, {b}Клайда{/b}."
    show player 5f
    show clyde 2
    clyde "Хмм, что ж извини. Я не знаю этого человека {b}Клайда{/b}."
    show clyde 9 with dissolve
    clyde "Тем не менее это звучит так как будто он красивый сукин сын!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Ты что сейчас прикалываешься надо мной?!"
    show player 13f
    show clyde 4
    clyde "Позвольте спросить у вас..."
    clyde "Этот {b}Клайд{/b} носит шляпу?"
    show clyde 3
    show player 10f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Ну, тогда проехали!"
    clyde "Как вы можете видеть... Клетус никогда никуда не уходит без своей верной шляпы!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Это так странно."
    show player 12f
    player_name "Мне нужно идти."
    show player 5f
    show clyde 4
    clyde "Ладно. Что ж, рад был с тобой познакомиться, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "Я тебе не говорил своего имени!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Ох, ээээ..."
    clyde "... Ну, я..."
    show clyde 11 with dissolve
    clyde "Эммм... Телепатия!"
    show clyde 12
    show player 10f
    player_name "Хмм?!"
    show player 5f
    show clyde 11
    clyde "Я, {b}Клетус{/b}... Я телепат."
    show clyde 4 with dissolve
    clyde "... И я могу прочесть твои мысли силой вввволи!"
    show clyde 3
    show player 10f
    player_name "Мои мысли?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да точно, парень!"
    show clyde 4 with dissolve
    clyde "Так что не говори людям, что я здесь."
    clyde "Потому что я знаю..."
    clyde "Особенно, если эти будет полиция."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Я..."
    player_name "... Только..."
    player_name "... Пока."
    hide player with dissolve
    pause
    show clyde 4
    clyde "До скорого, парень!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Я могу тебе помочь?"
    show clyde 1
    show player 10f
    player_name "Эммм, нет?"
    show player 5f
    show clyde 22
    clyde "О чувак. Ты один из демократов, Иисус любит тебя??"
    show clyde 21
    show player 12f
    player_name "Что?! Нет!"
    show player 5f
    show clyde 26
    clyde "{b}*Задыхаясь*{/b} Ты что коп?!"
    clyde "Ты должен мне сказать, такие правила!"
    show clyde 25
    show player 12f
    player_name "Нет мужик... Мы познакомились только прошлой ночью!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "Я помогал {b}Рокси{/b} с домашним заданием?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Ох, да наверное!"
    clyde "Ты новый парень {b}Рокси{/b}!"
    show clyde 3
    show player 10f
    player_name "Нет, мы только друзья-"
    show player 5f
    show clyde 4
    clyde "Как дела, брат?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "Как дела, брат?!"
    show clyde 3
    show player 14f
    player_name "Ох, привет {b}Клайд{/b}..."
    show player 5f
    show clyde 4
    clyde "Что ты здесь делаешь?!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "И так {b}Клетус{/b}, верно?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Ты прав, парень!"
    show clyde 4 with dissolve
    clyde "Чем я могу тебе помочь?!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Вздох*{/b} У меня все в порядке."
    player_name "Как дела?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Много того, что никто не делает!"
    clyde "Хахаха, знаешь что я имею в виду, брат?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "'Потому что у меня был весь секс... с девушками..."
    clyde "{b}*Кгхм*{/b} человеческими девушками."
    show clyde 12
    show player 12f
    player_name "Да, я понял, {b}Клайд{/b}..."
    show clyde 9 with dissolve
    clyde "Хех, конечно ты!"
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Я никогда не слышал, чтобы кто-то говорил так, как ты, {b}Клайд{/b}..."
    show player 12f
    player_name "В общем откуда ты?"
    show player 5f
    show clyde 4
    clyde "Потому что все вы, городские, говорите странно!"
    clyde "Там в низу в долине, мы все так разговариваем..."
    show clyde 3
    show player 10f
    player_name "... В долине?"
    show player 5f
    show clyde 4
    clyde "Да."
    show clyde 3
    show player 10f
    player_name "Что это?!"
    show player 5f
    show clyde 4
    clyde "Эмм, где я вырос. Ясень пень!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "Это в нескольких округах севернее от сюда."
    clyde "На холмах."
    show clyde 3
    show player 10f
    player_name "Я думал, что на севере сплошные леса."
    show player 5f
    show clyde 4
    clyde "Да, довольно много..."
    show clyde 3
    show player 12f
    player_name "Люди живут там?"
    show player 5f
    show clyde 4
    clyde "Да, большая часть моей семьи все еще живет там."
    clyde "Я думал, что перееду сюда с {b}Тетушкой Кристалл{/b}, чтобы произнести заклинание."
    clyde "Дайте городской жизни справедливую встряску."
    show clyde 3
    show player 10f
    player_name "И как получается?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Ээээ, есть свои плюсы и минусы."
    clyde "Я скучаю по родному самогону дома и по всей травке."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Но я и тут готовлю убойные блюда!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "И что ты готовишь?"
    show player 5f
    show clyde 22
    clyde "Э-э-э... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Курицу!"
    show clyde 4 with dissolve
    clyde "Хех, да! Я готовлю жареных цыплят!"
    clyde "Вы, городские, просто не можете насытиться..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "Мне нужно идти..."
    show player 5f with dissolve
    show clyde 4
    clyde "Ага, хорошо."
    clyde "Продолжим в следующий раз, братишка!"
    clyde "Ууу!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "Что у тебя там происходит?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Эээ, извини бро."
    clyde "В эту лачугу строго запрещается заходить!"
    show clyde 9 with dissolve
    clyde "Если только у тебя нет женских прелестей?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Хех, что ж запомни это... Если хижина качается, лучше не стучать!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?!"
    show clyde 3
    show player 401f
    player_name "... Да. несмотря на то что мне бы очень хотелось..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Хороший трактор."
    show player 13f
    show clyde 4
    clyde "Ох, да!"
    clyde "Это {b}Большая Берта{/b}!"
    clyde "Разве она не красавица?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Я сам её построил из остатков металлолома."
    clyde "31.2 лошадиных сил, 2500 об/мин, 8.5 галлонов..."
    clyde "... И только посмотри на этот рубиново красный завершение!"
    clyde "Мммм! Она самая сексуальная вещь на четырех колесах!"
    show clyde 9 with dissolve
    clyde "Понимаешь о чем я?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "На самом деле, неважно."
    player_name "... Может быть в другой раз?"
    show player 5f
    show clyde 4
    clyde "Пф, Черт возьми да, братишка!"
    clyde "Ты знаешь где меня найти."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Давай, {b}Клайд{/b}! Я знаю это ты!"
    show player 16f
    show clyde 4
    clyde "Я не понимаю о чем ты говоришь..."
    show clyde 3
    show player 15f
    player_name "Это глупо, я никому не скажу, что ты вернулся..."
    show player 16f
    show clyde 4
    clyde "Что ты там куришь, приятель?"
    show player 428f
    clyde "Меня зовут {b}Клетус{/b}, и я здесь впервые."
    clyde "Навсегда."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "Он по-прежнему пишет {b}Клайд{/b} над вашим текстовым полем!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Эй!"
    clyde "Не ломай все стены!"
    clyde "Это обман!"
    clyde "Моё имя {b}Клетус{/b}!!!"
    show clyde 26
    clyde "Скажи это!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Давай, ты знаешь что хочешь сказать это..."
    show clyde 1
    show player 24f
    player_name "{b}*Вздох*{/b}"
    show player 25f
    player_name "{b}Клетус{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "Вот так!"
    clyde "Это было не так сложно, правда?!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
