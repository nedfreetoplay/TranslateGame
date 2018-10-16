label church_first_visit:
    scene church_b
    show player 11 with dissolve
    player_name "( В церкви пусто. )"
    player_name "( Похоже, я пропустил службу. )"
    hide player 11
    return

label church_mia_church_plan:
    scene church_full02_b
    show player 32 at Position (xoffset=68) with dissolve
    player_name "( {b}Хелен{/b} сидит в первых рядах. )"
    show player 12 with dissolve
    player_name "( Должен быть способ поговорить с ней... )"
    player_name "(...Но сначала мне нужно переодеться. )"
    player_name "( Посмотрим, смогу ли я найти одно их этих {b}одеяний священника{/b} где-то в церкви... )"
    hide player with dissolve
    return

label church_mia_convince_helen:
    scene church_cs01
    with fade
    show text "Служба продолжается.\n{b}Хелен{/b} встала и направившись к исповеди...\n...зашла внутрь." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene church_cs02
    with fade
    show text "Священник на какое-то время вышел.\nТеперь отличный момент пообщаться с ней...\n...И поменять её мнение о {b}Гарольде{/b}." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text with dissolve

    scene church_full03_b
    show player 30 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "Мне нужно {b}зайти в исповедальню{/b} с {b}правой стороны{/b}..."
    hide player
    hide players robe
    with dissolve
    return

label church_mia_return_priest_outfit:
    scene church_full02_b
    show player 33 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "Прекрасно!"
    show player 106 at Position (xoffset=-1)
    player_name "..."
    show player 14 at Position (xoffset=-1)
    player_name "( Я должен вернуть этот наряд туда, где нашел его... )"
    player_name "( ...пока никто не заметил.... )"
    hide player
    hide players robe
    with dissolve
    return

label church_mia_nun_thoughts:
    scene church_b
    show player 10 with dissolve
    player_name "( Черт... Это было страшно! )"
    player_name "( Теперь я должен кое-что сделать для этой монахини... )"
    player_name "( ...надеюсь, что она никому не расскажет о том, что я сделал. )"
    hide player with dissolve
    return

label church_mia_church_night_visit:
    scene church_night_b
    show player 10 with dissolve
    player_name "( По ночам здесь так тихо. )"
    player_name "( Я не уверен, что людям позволено приходить сюда так поздно. )"
    show player 12
    player_name "( Теперь, схожу к {b}сестре Анжелике{/b} и посмотрю, чего она хочет... )"
    hide player with dissolve
    return

label confessional_left:
    if M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("confessional_left_mia_return_priest_outfit")

    elif M_mia.is_state(S_mia_priest_act):
        call expression game.dialog_select("confessional_left_mia_priest_act")
    else:

        call expression game.dialog_select("confessional_left_empty")
    $ game.main()

label confessional_left_mia_return_priest_outfit:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( Мне нужно вернуть это одеяние, пока меня не увидели. )"
    hide player
    hide players robe
    with dissolve
    return

label confessional_left_mia_priest_act:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( Я не могу войти с этой стороны )"
    player_name "( Я должен использовать дверь с {b}правой стороны{/b} исповедальни... )"
    hide player
    hide players robe
    with dissolve
    return

label confessional_left_empty:
    scene church_confession
    show player 283 at Position(xpos=280)
    with dissolve
    player_name "Благослови меня отец, ибо я согрешил."
    show player 278
    player_name "..."
    show player 284
    player_name "......"
    show player 280
    player_name "Отец?"
    player_name "( Здесь никого нет? )"
    show player 10
    player_name "( Полагаю, в это время здесь нет священника... )"
    hide player
    hide church_confession
    return

label confessional_right:
    if M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("confessional_right_mia_return_priest_outfit")

    elif M_mia.is_state(S_mia_priest_act):
        call expression game.dialog_select("confessional_right_mia_priest_act_pre")
        menu:
            "Молиться?" if player.stats.chr() < 3:
                call expression game.dialog_select("confessional_right_mia_priest_act_pray")

                $ M_mia.trigger(T_helen_convince_fail)

            "Change." if player.stats.chr() >= 3:
                call expression game.dialog_select("confessional_right_mia_priest_act_change")
                $ M_mia.trigger(T_helen_convince_change)
                jump expression game.dialog_select("church_dialogue")
    else:

        call expression game.dialog_select("confessional_right_empty")
    $ game.main()

label confessional_right_mia_return_priest_outfit:
    scene church_full02_b
    show player 10 at Position (xoffset=-1)
    show players robe
    with dissolve
    player_name "( Мне нужно вернуть это одеяние, пока меня не увидели.)"
    hide player
    hide players robe
    with dissolve
    return

label confessional_right_mia_priest_act_pre:
    scene church_confession
    show player 5f at Position (xpos=795)
    show players robe f at Position (xpos=794)
    show helen 16 at Position (xpos=300)
    with dissolve
    helen "Прости мою семью, {b}Отец{/b}, ибо они согрешили. Прошло 7 дней с моей последней исповеди."
    show helen 15
    helen "..."
    show helen 13
    helen "{b}Отец{/b}? Вы здесь?"
    show helen 12
    show player 23f
    player_name "*кашлеет*"
    show player 10f
    player_name "Да... Я эээ... Я слушаю..."
    show player 5f
    show helen 16
    helen "О, {b}Господь{/b}, я прошу твоего прощения за все грехи моей семьи..."
    helen "...За моего мужа, разрушающего наш брак... И за распутное поведение моей дочери..."
    helen "Я изо всех сил старалась заставить их увидеть их поступки."
    helen "Я говорила им много раз, что они отправятся в ад, если не изменятся."
    helen "...Но, похоже они свернули со святого пути и поддались тьме."
    show helen 14
    helen "Что мне делать, {b}Отец{/b}?"
    show helen 15
    return

label confessional_right_mia_priest_act_pray:
    show player 10f
    player_name "[chr_warn]Возможно тебе нужно... эээ... молиться?"
    show player 22f
    show helen 12
    helen "[chr_warn]..."
    show helen 13
    helen "[chr_warn]Молиться?"
    show helen 12
    show player 10f
    player_name "[chr_warn]Верно!"
    show player 22f
    show helen 13
    helen "[chr_warn]Я не совсем понимаю, как это поможет моей семье, {b}Отец{/b}."
    helen "[chr_warn]Что-то должно произойти! Что-то должно измениться, чтобы они осознали свое греховное и мерзкое поведение."
    show helen 12
    show player 21f
    player_name "[chr_warn]ЭЭЭ... Пути {b}Господни{/b} неисповедимы!"
    show player 22f
    helen "[chr_warn]..."
    show helen 14
    helen "[chr_warn]Хорошо... Я сделаю что смогу, {b}Отец{/b}."
    show helen 16
    helen "[chr_warn]Пожалуйста, попросите {b}Господа{/b} простить их, и не могли бы вы тоже помолиться за них?"
    show helen 15
    show player 10f
    player_name "[chr_warn]Конечно! Для меня это не трудно!"
    show player 5f
    show helen 12
    helen "[chr_warn]..."
    show helen 14
    helen "[chr_warn]И что, дорогой {b}Отец{/b}, ты хочешь, чтобы твой верный слуга сделала в качестве покаяния от моей семьи?"
    show helen 12
    show player 10f
    player_name "[chr_warn]Эээ... Эммм... Двух молитв будет достаточно?"
    show player 5f
    helen "[chr_warn]..."
    show helen 13
    helen "[chr_warn]Спасибо..."
    hide helen with dissolve
    show player 24f
    player_name "[chr_warn]Черт, я слишком нервничаю..."
    player_name "[chr_warn]... Мне нужно попробовать ещё раз, с большей уверенностью."
    hide players robe
    show player 444f
    with dissolve
    pause
    hide player with dissolve
    return

label confessional_right_mia_priest_act_change:
    show player 12f
    player_name "Возможно, что {b}ты{/b} та, кому нужно измениться, чтобы они вернулись на путь истинный..."
    show player 5f
    show helen 14
    helen "Я?! ...Но я все делаю правильно. Я..."
    show helen 12
    show player 12f
    player_name "Да, ты проделала хорошую работу, указав на их недостатки, но как насчет твоих собственных?"
    player_name "Я ещё не слышал о твоих проступках. Ты же не можешь быть идеальной?"
    show player 5f
    show helen 15
    helen "..."
    show helen 14
    helen "*sigh*"
    show helen 16
    helen "Возможно вы правы, {b}Отец{/b}."
    helen "Я... возможно... зашла слишком далеко..."
    show helen 14
    helen "Просто они, кажется, не понимают своей опасности... как я..."
    helen "Я сделаю это, потому что я люблю их..."
    show helen 15
    show player 10f
    player_name "Ты всё ещё можешь получить искупление!"
    show player 5f
    show helen 14
    helen "Искупление? Но что мне делать?"
    show helen 15
    show player 12f
    player_name "Возможно, ты могла бы быть более терпимой со своим мужем..."
    player_name "...И дать своей дочери немного свободы!"
    show player 10f
    player_name "Они же не должны быть задушены {b}Божьими{/b} заповедями. Вместо этого покажи им, как сильно ты их любишь, как {b}Бог{/b} любит всех своих созданий."
    player_name "Ты не можешь контролировать всех... Но ты можешь изменить себя."
    show player 5f
    show helen 14
    helen "Вы правы... Я сделаю все что смогу, {b}Отец{/b}."
    show helen 15
    show player 14f
    player_name "Теперь иди и прояви снисходительность и прощение, как {b}Господь{/b} прощает тебя."
    show player 13f
    show helen 16
    helen "Спасибо за понимание... и прощение..."
    show helen 15
    show player 17f
    player_name "Нет проблем!"
    show helen 12
    helen "..."
    show player 21f
    player_name "Эээ... Эмм... благословенного тебе дня."
    show player 13f
    show helen 16
    helen "Что мне делать в наказание, {b}Father{/b}?"
    show helen 15
    show player 12f
    player_name "Достаточно двух молитв в качестве Ёпт... Эээ.. Епитимьи."
    show player 22f
    show helen 12
    pause
    show helen 16
    show player 13f
    helen "Спасибо..."
    hide helen
    hide player
    hide players robe
    with dissolve
    return

label confessional_right_empty:
    scene church_confession
    show player 43f at Position(xpos=760)
    with dissolve
    player_name "( Круто! )"
    player_name "( Я никогда не был на этой стороне исповедальни. )"
    show player 4f
    player_name "Хмм..."
    show player 14f
    player_name "( Выглядит так же как с обратной стороны. )"
    player_name "( Пора убираться от сюда... )"
    hide player
    hide church_confession
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
