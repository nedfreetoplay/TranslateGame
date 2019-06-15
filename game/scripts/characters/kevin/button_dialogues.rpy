label button_kevin_shift_cover_has_favor:
    show kevin 2
    kev "You {b}talk with Erik about covering for me{/b} yet?"
    show kevin 1
    show player 17
    player_name "I did."
    player_name "He's gonna do it."
    show player 13
    show kevin 2b with dissolve
    kev "HELL!"
    kev "YEAH!"
    kev "BRO!"
    show kevin 2c with dissolve
    kev "You are the freaking man!"
    show kevin 6 with dissolve
    kev "Finally I can get back to my two-a-days!"
    show kevin 5
    show player 14
    player_name "Heh, so I guess I'll see you at the gym in the {b}Morning{/b}?"
    show player 13
    show kevin 9b with dissolve
    kev "You know it, bro!"
    hide kevin
    hide player
    with dissolve
    return

label button_kevin_shift_cover_no_favor:
    show kevin 2
    kev "You {b}talk with Erik about covering for me{/b} yet?"
    show kevin 1
    show player 29 with dissolve
    player_name "No, not yet."
    show player 3
    show kevin 2
    kev "Ugh, you gotta hurry, bro!"
    show kevin 2b with dissolve
    kev "My muscles are wasting away in here!"
    show kevin 1 with dissolve
    show player 14 with dissolve
    player_name "Heh, just relax."
    player_name "I'll talk with him."
    show player 13
    return

label button_kevin_cafeteria_duty_repeat:
    show player 14
    player_name "You any closer to getting out of here?"
    show player 13
    show kevin 2
    kev "Hell no."
    kev "I'm gonna be stuck in here all semester, I just know it!"
    show kevin 1
    return

label button_kevin_cafeteria_duty_first:
    show player 14
    player_name "How much longer are you stuck doing this?"
    show player 13
    show kevin 2d with dissolve
    kev "{b}*Sigh*{/b} Until I get my science grade up, bro..."
    kev "Honestly, it could take all semester."
    show kevin 2e
    show player 14
    player_name "Seriously?"
    show player 13
    show kevin 2d
    kev "Yeah."
    show kevin 2e
    show player 14
    player_name "That does suck man."
    player_name "I need you at the gym to spot me."
    show player 13
    show kevin 2 with dissolve
    kev "Ah, don't get me all depressed..."
    kev "You know I wanna be in there helping my bro get ripped!"
    show kevin 1
    pause
    show kevin 4
    kev "Tsk, you know what..."
    show kevin 2
    kev "I wonder if I could sneak outta here?"
    show kevin 1
    show player 5
    player_name "Hmm?"
    show kevin 2
    kev "I mean, if we could {b}find someone to cover for me{/b}..."
    kev "... Like in the mornings."
    kev "It could totally work, bro!"
    show kevin 1
    show player 10
    player_name "What do you mean?"
    show player 5
    show kevin 2
    kev "Well, {b}Mrs. Smith{/b} never comes in here in the morning."
    kev "So as long as the work got done, it wouldn't really matter who was doing it."
    show kevin 1
    show player 14
    player_name "So we just need to {b}find someone to cover for you{/b}?"
    show player 13
    show kevin 2
    kev "Yeah, you got any ideas?"
    show kevin 1
    show player 4
    pause
    show player 14
    player_name "Hmm, I might be able to convice {b}Erik{/b} to do it."
    show player 13
    show kevin 2
    kev "Oh, that would be awesome, bro!"
    show kevin 1
    show player 14
    player_name "I'll {b}ask him{/b} about it."
    show player 13
    show kevin 2
    kev "Hell yeah!"
    show kevin 1
    return

label button_kevin_intro_pre_favor:
    scene expression player.location.background_blur with None
    show player 13 at left
    show kevin 2 at right
    with dissolve
    kev "Sup, bro?!"
    show kevin 1
    show player 14
    player_name "Hey, {b}Kevin{/b}."
    show player 13
    show kevin 2
    kev "You here to scrub some pots?"
    show kevin 1
    show player 17
    player_name "Heh, no way man!"
    show player 13
    show kevin 2
    kev "Ugh, this cafeteria duty sucks dick, bro!"
    show kevin 1
    pause
    show kevin 2
    kev "... And not the cool kind, either."
    show kevin 1
    show player 29 with dissolve
    player_name "Eh, right..."
    show player 5 with dissolve
    return

label button_kevin_used_panties_repeat:
    show player 10
    player_name "I can't believe this guy has me stealing {b}used panties{/b}..."
    show player 5
    show kevin magic 2
    kev "It's not that big a deal, bro!"
    kev "Just swipe a pair from home."
    show kevin magic 1
    show player 37 with dissolve
    player_name "Yeah, yeah."
    player_name "I'll {b}check around my house{/b} and see if I can find a pair of {b}[deb_name]'s{/b} or {b}[jen_name]'s{/b}."
    show player 13 with dissolve
    return

label button_kevin_used_panties_first:
    show player 10 at left
    show kevin magic 1 at right
    player_name "So I met that new {b}Muay Thai{/b} trainer you were going on about."
    show player 5
    show kevin magic 2
    kev "Right on, bro!"
    kev "He's pretty awesome, right?!"
    show kevin magic 1
    show player 12
    player_name "He's a total crackpot!"
    show player 5
    show kevin magic 2
    kev "Huh?"
    show kevin magic 1
    show player 12
    player_name "Yeah, he said he won't teach me unless I bring him {b}used panties{/b}!"
    show player 5
    show kevin magic 2
    kev "Oh, that..."
    show kevin magic 3 with dissolve
    kev "Umm."
    show kevin magic 4
    show player 10
    player_name "Wait a second..."
    show player 14
    player_name "You brought him a pair, didn't you?!"
    show player 13
    show kevin magic 3
    kev "Eh, yeeeeah."
    show kevin magic 4
    show player 14
    player_name "Dude, seriously?"
    show player 13
    show kevin magic 2 with dissolve
    kev "Well, I heard all this awesome stuff about him and I was curious..."
    kev "Once you get past the panties thing, he's like totally legit!"
    show kevin magic 1
    show player 11
    player_name "..."
    show kevin magic 2
    kev "I'm serious!"
    kev "He really knows his shit, bro."
    show kevin magic 1
    show player 14
    player_name "Where did you get a pair of {b}used panties{/b}?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Oh, eh... I kinda... Snatched a pair of {b}my mom's{/b}, outta the dirty clothes basket."
    show kevin magic 4
    show player 12
    player_name "Dude..."
    show player 5
    show kevin magic 2 with dissolve
    kev "What?!"
    kev "It's not THAT weird."
    kev "I just took one pair and it's not like I was taking them for me."
    kev "I gave them to {b}Master Somrak{/b}."
    show kevin magic 1
    show player 14
    player_name "It's pretty weird {b}Kevin{/b}."
    show player 13
    show kevin magic 2
    kev "Nah, bro."
    kev "You're getting hung up on trivial stuff..."
    kev "You've got a couple girls at your house don't you?"
    show kevin magic 1
    show player 10
    player_name "Yeah but-"
    show player 11
    show kevin magic 2
    kev "Well, there ya go! Just snag one pair and you're in!"
    kev "It's really not a big deal, bro."
    show kevin magic 1
    show player 35
    player_name "Hmm, I dunno..."
    show player 34
    show kevin magic 2
    kev "Just do it, {b}[firstname]{/b}."
    kev "{b}Master Somrak's{/b} teachings will change your life, I'm telling ya!"
    show kevin magic 1
    show player 33
    player_name "I guess I could take one pair..."
    show player 13
    show kevin magic 2
    kev "See, there ya go!"
    show kevin magic 1
    show player 14
    player_name "I'll {b}check around my house{/b} and see if I can find a pair of {b}[deb_name]'s{/b} or {b}[jen_name]'s{/b} panties."
    show player 13
    return

label kevin_dialogue_ross_find_magazines:
    show player 2 at left
    show kevin 29b at right
    with dissolve
    player_name "Привет, {b}Кевин{/b}!"
    show player 1
    show kevin 30
    kev "Как дела, {b}[firstname]{/b}?"
    show player 2
    show kevin 29b
    player_name "Не очень. Что ты читаешь?"
    show player 1
    show kevin 30b
    kev "Ох, просто некоторые журналы, которые я взял, в спортзале."
    show player 2
    show kevin 29b
    player_name "Круто, ты ищешь новую работу или типо того?"
    show player 1
    show kevin 30
    kev "Нет, почему?"
    show player 11
    show kevin 29
    player_name "..."
    show kevin 31 with dissolve
    kev "Иди посмотри на этого красавчика, {b}[firstname]{/b}!"
    show player 10
    show kevin 31b
    player_name "... Красавчика?"
    show player 11
    player_name "..."
    show player 10
    player_name "Ох, точно... Ты думаешь, я могу взять один из этих журналов?"
    show player 11
    show kevin 30 with dissolve
    kev "Хех, Я не знал что ты был знатаком мужских форм..."
    show player 10
    show kevin 29
    player_name "Вообще-то я уже в Колледже."
    show player 11
    show kevin 30b
    kev "Ох, точно. Колледж."
    show kevin 31 with dissolve
    kev "Я понял тебя Бро! Ни слова больше!"
    kev "Бери все что тебе нужно! Вот этот займет меня на некоторое время."
    show player 2
    show kevin 31b
    player_name "Крутяк! Спасибо, эмм, Бро..."
    show player 1
    show kevin 31c
    kev "Чееерт возьми, он блестит..."
    show player 10
    player_name "..."
    return

label kevin_dialogue_ross_ask_model:
    show player 2 at left
    show kevin 1 at right
    player_name "Я работаю надо проектом для {b}Мисс Росс{/b} и для этого требуется живая модель."
    player_name "Тебя не заинтересует?"
    show kevin 2
    show player 1
    kev "Позирование. Я просто должен стоять там?"
    show player 2
    show kevin 1
    player_name "Да, тебе просто нужно будет стоять там."
    show player 10
    player_name "Голым."
    show kevin 3
    show player 11
    kev "Голым!?"
    kev "Ох, мужик. Я не знаю, Бро."
    kev "Это только ты там будешь рисовать?"
    show player 10
    show kevin 1
    player_name "Ну, {b}Мия{/b} и я - оба будем рисовать."
    player_name "{b}Мисс Росс{/b} тоже там будет."
    show player 11
    show kevin 4
    kev "Агх, пасс..."
    show kevin 3
    kev "Я не хочу чтобы девочки видели меня голым, Бро. Это немного стремно."
    show kevin 1
    player_name "..."
    show player 10
    player_name "Х-хорошо."
    return

label kevin_dialogue_intro:
    show kevin 23 at right
    show player 14 at left
    with dissolve
    player_name "Привет, {b}Кевин{/b}!"
    show player 13
    show kevin 9b
    kev "Привет, {b}[firstname]{/b}."
    show kevin 23
    show player 14
    player_name "Как дела?"
    show player 13
    show kevin 9b
    kev "Не очень. Вчера у меня был ягодичный день."
    kev "Моя задница болит!"
    kev "Хотя потрогай какая она тугая!"
    show kevin 23
    show player 10
    player_name "Эмммм... Нет спасибо чувак."
    show player 13
    show kevin 9b
    kev "Ты многое потерял!"
    return

label kevin_dialogue_erik_favor_2_completed:
    kev "Лучше увидимся в спортзале чуть позже!"
    show kevin 23
    show player 14
    player_name "Может быть..."
    show player 13
    show kevin 9b
    return

label kevin_dialogue_dewitt_kevin_give_guitar:
    show player 14
    player_name "Я нашел для тебя гитару!"
    show player 13
    show kevin 24
    kev "Серьезно?"
    show kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "Что ты думаешь?"
    show player 13 with dissolve
    show kevin 16f with dissolve
    kev "Черт возьми!Где ты достал эту штуку?"
    kev "Эта вешь лучше подделки!"
    show kevin 14f
    show player 10
    player_name "Эта?"
    show player 5
    show kevin 15f
    kev "Эмм, да, Бро!"
    kev "Я надеюсь ты ее не украл или типо того."
    show kevin 14f
    show player 14
    player_name "Вообще-то я её одолжил, у моего друга. Так что будь остороже с ней, хорошо?"
    hide player
    show kevin 27 at left
    with dissolve
    kev "Без проблем!"
    kev "Я буду относиться к этой красоте с уважением, которого она так заслуживает!"
    show kevin 28
    player_name "Круто, так что ты будешь играть на ней на шоу талантов."
    show kevin 27
    kev "Я должен!"
    show kevin 28
    player_name "Потрясно! Увидимся тогда скоро в кабинете {b}Мисс Девитт{/b} чтобы потренироваться!"
    show kevin 27
    kev "Звучит неплохо,Бро!"
    show player 13 at left
    show kevin 16 at right
    with dissolve
    kev "Я буду называть тебя... Дэвин"
    kev "Ты бы хотела это красивая?"
    show player 11
    hide kevin with dissolve
    player_name "..."
    return

label kevin_dialogue_talent_show_help:
    show player 10
    player_name "Я помогаю {b}Мисс Девитт{/b} найти добровольцев для шоу талантов."
    player_name "Разве ты раньше не играл на гитаре?"
    show player 5
    show kevin magic 2
    kev "Да, я играл."
    show kevin magic 1
    show player 10
    player_name "Что случилось?"
    show player 5
    show kevin magic 2
    kev "Ох, моя бывшая вроде как разбила её когда я порвал с ним."
    show kevin magic 1
    show player 12
    player_name "С ним?"
    show player 11
    show kevin magic 3 with dissolve
    kev "Я сказал с ним? Извини, я имел в виду с ней."
    kev "... Да, ОНА разбила её на кусочки."
    show kevin magic 1 with dissolve
    show player 14
    player_name "Хм, ты западаешь на сумашедших девченок, хм?"
    show player 13
    show kevin magic 3 with dissolve
    kev "Хех, Ты знаешь! Сумашедшие дувченки, Я на пути к ним! Полностью..."
    show kevin magic 1 with dissolve
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin magic 2
    kev "Да, Я был бы не против."
    kev "Все же где же я достану гитару? Они очень дорогие!"
    show kevin magic 1
    show player 35
    player_name "Хмм, возможно я смогу найти одну для тебя..."
    show player 34
    player_name "( У {b}Эрика{/b} в подвале много гитар. Возможно я смогу одолжить одну? )"
    show player 14
    player_name "Я вернусь!"
    show player 13
    show kevin magic 2
    kev "Хорошо."
    return

label kevin_dialogue_talent_show_replace_guitar:
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin magic 2
    kev "Да, Я бы не отказался."
    kev "Все же где же я достану гитару? Они очень дорогие!"
    show kevin magic 1
    show player 34
    player_name "( Я должен поменять мою само-сделанную гитару с той что в подвале у {b}Эрика{/b}! )"
    show player 14
    player_name "Я приду!"
    show player 13
    show kevin magic 2
    kev "Ладно."
    return

label kevin_dialogue_talent_show:
    show player 14
    player_name "Итак если бы у тебя была гитара, ты бы сыграл на шоу талантов?"
    show player 13
    show kevin magic 2
    kev "Да, Я бы не отказался."
    kev "Все же,где же я достану гитару? Они очень дорогие!"
    show kevin magic 1
    show player 35
    player_name "Хмм, возможно я смогу найти одну для тебя..."
    show player 34
    player_name "( У {b}Эрика{/b} в подвале много гитар. Возможно я смогу одолжить одну? )"
    show player 14
    player_name "Я вернусь!"
    show player 13
    show kevin magic 2
    kev "Хорошо."
    return

label kevin_dialogue_dewitt_science_adhesive:
    show player 10
    player_name "Что нам нужно для этого {b}клея{/b} ещё раз?"
    show player 13
    show kevin 2
    kev "Просто встреться со мной в {b}Научной лаборатории после уроков{/b}."
    kev "Я позабочусь об остальном."
    show kevin 1
    show player 14
    player_name "Круто! Спасибо, {b}Кевин{/b}!"
    return

label kevin_dialogue_leave:
    show player 14
    player_name "Anyways, I gotta go."
    player_name "Keep your spirits up, man."
    show player 13
    show kevin 2
    kev "Yeah, alright bro."
    kev "See ya around."
    hide kevin
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
