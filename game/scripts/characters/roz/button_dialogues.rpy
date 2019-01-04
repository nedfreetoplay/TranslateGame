label roz_dialogue_3rd_floor_priya:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "Я хотел спросить вас о {b}третьем этаже{/b}."
    show player 5f
    show roz 2
    roz "Это запрещено."
    show roz 1
    show player 12f
    player_name "Да, я знаю..."
    player_name "... Но я надеялся, может, вы скажете мне, у кого есть доступ?"
    show player 5f
    show roz 2
    roz "Нет, это запрещено."
    show roz 1
    show player 12f
    player_name "... Но мне просто нужно-"
    show player 5f
    show roz 2
    roz "Запрещено."
    show roz 1
    show player 35f
    player_name "Не могли бы вы вызвать одного из врачей, работающих там?"
    player_name "Мне нужно поговорить с {b}доктором Сингх{/b}."
    show player 90f
    show roz 2
    roz "Я могла бы."
    show roz 1
    pause
    player_name "..."
    show player 10f
    player_name "Не могли бы вы?"
    show player 5f
    show roz 2
    roz "Нет."
    show roz 1
    show player 15f
    player_name "Слушайте, мне действительно нужно поговорить с ним."
    player_name "Это очень важно!"
    show player 16f
    show roz 2
    roz "О, я не понимала, насколько это важно..."
    show roz 1
    pause
    show player 10f
    player_name "Так вы сделаете это?"
    show player 5f
    show roz 2
    roz "... Нет."
    show roz 1
    show player 15f
    player_name "Почему?!"
    show player 16f
    show roz 2
    roz "Это запрещено."
    show roz 1
    show player 37f with dissolve
    player_name "{b}*вздыхая*{/b}"
    show player 38f with dissolve
    player_name "Что я могу сделать, чтобы изменить ваше мнение?"
    show player 90f with dissolve
    show roz 2
    roz "Запреще-"
    show roz 1
    pause
    show roz 2
    roz "О."
    roz "Хм, сомневаюсь в этом."
    show roz 1
    pause
    show player 25f
    player_name "Я сделаю все что угодно!"
    show player 24f
    show roz 2
    roz "Все что угодно?"
    show roz 1
    show player 25f
    player_name "Буквально. Что угодно."
    show player 24f
    roz "Хмм."
    show roz 2
    roz "Ты умеешь обращаться с камерами?"
    show roz 1
    show player 12f
    player_name "С камерами?"
    player_name "Да, наверно."
    show player 5f
    show roz 2
    roz "Я купила эту новенькую в магазине, и эта чертова штука не работает."
    show roz 1
    show player 14f
    player_name "Я, вероятно, мог бы посмотреть!"
    show player 13f
    roz "Хмм."
    show roz 2
    roz "Тогда иди за мной."
    hide roz with dissolve
    pause
    show player 4f
    player_name "( Вау, она отвезет меня на {b}третий этаж{/b} только для того, чтобы починить камеру? )"
    player_name "( Как насчет этого, у меня наконец-то появился перерыв. )"
    hide player with dissolve
    return

label roz_dialogue_3rd_floor:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 10f at right
    player_name "Я хотел спросить вас о {b}третьем этаже{/b}."
    show player 5f
    show roz 2
    roz " Это запрещено."
    show roz 1
    show player 12f
    player_name "Да, я знаю..."
    player_name "... Но я надеялся, может, вы скажете мне, у кого есть доступ?"
    show player 5f
    show roz 2
    roz "Нет, это запрещено."
    show roz 1
    show player 12f
    player_name "... Но мне просто нужно-"
    show player 5f
    show roz 2
    roz "Запрещено."
    return


label roz_dialogue_intro:
    scene hospital_desk
    show roz 1 at left
    if Game.is_christmas():
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Привет!"
    show player 13f
    show roz 2
    roz "Да?"
    roz "Чем я могу помочь вам?"
    show roz 1
    return

label roz_dialogue_1st_floor:
    show player 12f
    player_name "Что я могу найти на 1-м этаже?"
    show player 5f
    roz "..."
    show roz 2
    roz "Это Вестибюль."
    show roz 1
    show player 10f
    player_name "Ох... есть ли что-нибудь ещё?"
    show player 5f
    show roz 3 with dissolve
    roz "Ты видишь что-нибудь ещё?"
    show roz 1 with dissolve
    show player 24f
    player_name "Я не думаю..."
    show player 25f
    show roz 2
    roz "Что-нибудь ещё,что я могу сделать?"
    show roz 1
    show player 13f
    return

label roz_dialogue_2nd_floor:
    show player 12f
    player_name "Что я могу найти на 2-м этаже?"
    show player 5f
    show roz 2
    roz "У нас есть больничные палаты, и склад на 2-м этаже."
    show roz 1
    show player 12f
    player_name "Ох.Я вижу."
    show player 5f
    show roz 2
    roz "Что-нибудь ещё,что я могу сделать?"
    show roz 1
    show player 13f
    return

label roz_dialogue_schedule:
    show player 12f
    player_name "Есть кто то в приёмной?"
    show player 5f
    show roz 2
    roz "Да."
    roz "Я всегда здесь."
    show roz 1
    show player 12f
    player_name "Вы никогда не покидаете своё рабочее место?"
    show player 5f
    show roz 2
    roz "Почему ты спрашиваешь?"
    show roz 1
    show player 10f
    player_name "Эмм... Просто интересно?"
    show player 5f
    show roz 2
    roz "Я покидаю своё рабочее место только в экстренных случаях."
    show player 11f
    roz "Если я не получаю {b}телефоный звонок{/b}, я не покидаю своего рабочего места."
    show roz 1 with dissolve
    show player 14f
    player_name "Ох. Я вижу."
    show player 13f
    show roz 2
    roz "Что-нибудь ещё, что я могу сделать?"
    show roz 1
    return

label roz_dialogue_ancestory:
    show player 14f
    show roz 1
    player_name "Роза! Мне нужно вас спросить кое о чём."
    show player 11f
    show roz 2
    roz "Хмм, да?"
    show roz 1
    show player 10f
    player_name "Я пытаюсь найти могилу кого-то кто умер в этом городе, много лет назад."
    show player 29f
    player_name "Я думаю он был Лодочником."
    player_name "У вас есть какие-то идеи как лучше отыскать его?"
    show player 3f
    show roz 2
    roz "Возможно есть одна или две."
    show roz 1
    roz "..."
    show player 11f
    player_name "..."
    show player 12f
    player_name "Не могли бы вы сказать мне?"
    show player 11f
    show roz 2
    roz "... Возможно я могла бы."
    show roz 1
    roz "..."
    show player 16f
    player_name "..."
    show player 30f
    player_name "*Ахх* Расскажите мне пожалуйста?"
    show player 16f
    show roz 2
    roz "Как его зовут?"
    show player 29f
    show roz 1
    player_name "... В этом и проблема. Я не знаю его имени."
    show player 11f
    show roz 2
    roz "Хмм..."
    roz "Ясно это все усложняет, не так ли?"
    show player 25f
    show roz 1
    player_name "... Да."

    show player 24f
    show roz 2
    roz "Хмм..."
    roz "Возможно ты сможешь отсыскать его в старых {b}Записях Патологоанатома{/b}."
    show player 11f
    roz "Я припоминаю несколько человек и их профессии указаны здесь."
    show player 10f
    show roz 1
    player_name "Серьёзно?! Это звучит многообещающе!"
    show player 11f
    show roz 2
    roz "Проблема в том, что это доставит большую мароку. Придется покапаться в старых делах."
    show player 29f
    show roz 1
    player_name "Ох?"
    show player 3f
    show roz 2
    roz "Может и ты сможешь сделать что-то что бы я не тратила своего времени?"
    show player 29f
    show roz 1
    player_name "К-конечно!"
    show player 2f
    player_name "Позвольте мне взглянуть на те записи и я сделаю все что вы захотите!"
    show player 1f
    show roz 2
    roz "Хмм... Что угодно?"
    show player 2f
    show roz 1
    player_name "Что угодно!"
    show player 1f
    roz "..."
    show roz 2
    roz "Хорошо. Я тебе скажу что. Возьми это ключи от {b}2-го этажа склада{/b}."
    roz "Ты его найдешь в уродливой коробке, лежащей на полке, она там как бельмо на глазу, ты не сможешь пропустить его."
    show player 2f
    show roz 1
    player_name "Уродливая коробка, понял."
    show player 1f
    show roz 2
    roz "Иди принеси мне эту коробку. Я просмотрю эти записи."
    show player 2f
    show roz 1
    player_name "Это звучит достаточно просто! Я вернусь в мгновение ока!"
    hide player with dissolve

    show roz 2
    roz "Хех, конечно ты будешь, Мальчик. Конечно ты будешь."
    return

label roz_dialogue_go_on_break:
    show player 14f
    show roz 1
    player_name "Я подумал может вы захотите... Знаете, взять перерыв?"
    show player 13f
    show roz 2
    roz "Ахх..."
    roz "Немогу устоять, ах Малыш."
    show roz 1
    player_name "..."
    show roz 2
    roz "Не волнуйся, сообщение получено."
    roz "Направляйся на склад и Я буду с минуты на минуту..."
    roz "...один момент, нужно привести себя в порядок."
    show roz 1
    player_name "..."
    show player 14f
    player_name "К-конечно, Я буду ждать наверху."
    show player 13f
    hide player with dissolve
    show roz 2
    roz "Хороший мальчик..."
    return

label roz_dialogue_nothing:
    show player 14f
    player_name "Нет, Я думаю это все!"
    show player 13f
    show roz 2
    roz "Пока."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
