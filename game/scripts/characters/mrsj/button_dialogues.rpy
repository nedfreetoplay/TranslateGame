label button_mrsj_greetings:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Здравствуйте, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Привет, {b}[firstname]{/b}!"
    mrsjo "Как у тебя дела?"
    show player 14
    show mrsj 14
    player_name "Все хорошо, спасибо!"
    show player 1
    show mrsj 17
    mrsjo "Я могу тебе чем-нибудь помочь?"
    show mrsj 14
    return


label button_mrsj_sex_ed_intro:
    scene erik_upstairs_night_c
    show mrsj 42 at right
    show player 11 zorder 2 at left
    show erik 1f zorder 1 at Position(xpos=300)
    with dissolve
    mrsjo "Привет,мальчики..."
    show mrsj 41
    show player 21
    player_name "П-привет, {b}Mrs. Johnson{/b}!"
    show player 13
    show erik 4f
    eri "Ты... очень красивая, {b}Mrs. Johnson{/b}."
    show erik 1f
    show mrsj 40b with fastdissolve
    mrsjo "Что ж, ты так и будешь пялиться на меня или хочешь спросить меня о чем-то?"
    show mrsj 39
    return

label button_mrsj_private_yoga_intro:
    scene erik_upstairs_night_c2
    show mrsj 54 at Position(xpos=734,ypos=650)
    show player 433 zorder 2 at left
    with dissolve
    mrsjo "Привет, {b}[firstname]{/b}..."
    show mrsj 53
    player_name "!!!"
    show mrsj 54
    mrsjo "Что-то не так?"
    show player 435
    show mrsj 53
    player_name "Вы.. вы голая, {b}Mrs. Johnson{/b}."
    show player 434
    show mrsj 54
    mrsjo "Мне нравится чувствовать... себя комфортно в своей комнате..."
    mrsjo "Разве ты не собирался спросить меня о чем-то?"
    show mrsj 53
    return

label button_mrsj_about_erik:
    show player 14 at left
    show mrsj 14 at right
    player_name "Я хотел поговорить о {b}Erik{/b}..."
    show player 1
    show mrsj 19
    mrsjo "О, он в порядке?"
    show player 14
    show mrsj 19c
    player_name "Да, он в порядке."
    player_name "Я поговорил с ним о том, что произошло прошлой ночью..."
    show player 11
    show mrsj 19
    mrsjo "Он расстроен?"
    show player 14
    show mrsj 19c
    player_name "Нет, вовсе нет."
    show player 10
    player_name "Он просто не уверен, чего хочет...."
    show player 11
    show mrsj 19
    mrsjo "В каком смысле?"
    show player 10
    show mrsj 19c
    player_name "Думаю, он бросил встречаться с девушками."
    player_name "Я мог бы попытаться помочь ему найти девушку, но  я думаю, что ты ему нравишься больше...."
    show player 13
    show mrsj 19
    mrsjo "Ох, мой..."
    show mrsj 20
    mrsjo "Я действительно слишком сильно его приютила?"
    show mrsj 19
    mrsjo "Как ты думаешь, что я должна делать?"
    show mrsj 19c
    return

label button_mrsj_route_sex_ed:
    show player 14 at left
    show mrsj 19c at right
    player_name "Думаю, будет лучше, если ты уделишь ему внимание, которое ему нужно..."
    show mrsj 19
    show player 1
    mrsjo "Ты действительно так думаешь?"
    show mrsj 19c
    show player 14
    player_name "Ну, я не думаю, что он хочет встречаться с другими девушками..."
    player_name "... И он действительно любит тебя!"
    show mrsj 19
    show player 1
    mrsjo "Он всегда был очень близок ко мне..."
    show mrsj 19c
    show player 14
    player_name "Мы отлично провели время прошлой ночью!"
    player_name "Я никогда не видел {b}Erik{/b} настолько счасливым."
    show mrsj 19
    show player 11
    mrsjo "Ты думаешь...вы,мальчики, хотели бы больше такого...внимания?"
    show mrsj 19c
    show player 21
    player_name "Я...я думаю да!"
    show mrsj 20
    show player 13
    mrsjo "Если ни одна из девочек из школы не будет уделять ему внимание, в котором он нуждается..."
    show mrsj 19
    mrsjo "...Может быть, я должна быть той единственной?"
    show mrsj 14
    show player 14
    player_name "Я думаю, ему бы это понравилось."
    show mrsj 49
    show player 11
    mrsjo "Что если я дам вам ребята немного...личного сексуального воспитания?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "Это только в образовательных целей, конечно..."
    show mrsj 50
    show player 29
    player_name "Ох, Я эмм... Я был бы вообще не против!"
    show mrsj 49
    show player 13
    mrsjo "Но тем не менее сначала я должна все обдумать."
    show mrsj 50
    show player 14
    player_name "Конечно, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_route_gf:
    show player 14 at left
    show mrsj 19c
    player_name "Я думаю, мы должны попытаться найти ему девушку."
    show player 1
    show mrsj 19
    mrsjo "Ты правда так думаешь?"
    show player 14
    show mrsj 19c
    player_name "Ну,я думаю, он был бы счастливее..."
    player_name "... и это повысило бы его самооценку!"
    show player 1
    show mrsj 20
    mrsjo "Ему действительно надо больше выходить на улицу..."
    show player 10
    show mrsj 19c
    player_name "Не поймите меня неправильно, мы хорошо повеселились прошлой ночью...."
    show player 14
    player_name "... но я думаю что {b}Erik{/b} нужно знакомиться с другими девченками."
    show player 13
    show mrsj 20
    mrsjo "Ты прав..."
    show player 11
    show mrsj 19
    mrsjo "Но что насчет... меня?"
    show player 10
    show mrsj 19c
    player_name "Что Вы имеете в виду?"
    show player 11
    show mrsj 19
    mrsjo "Ну..."
    mrsjo "Если {b}Erik{/b} найдет себе девушку... Что я буду делать?"
    show mrsj 20
    mrsjo "У меня никого нет, чтобы отдавать свое внимание..."
    show player 21
    show mrsj 19c
    player_name "О, Я уверен, что вы найдете кого-то {b}Mrs. Johnson{/b}!"
    show mrsj 14
    player_name "Вы очень... красивая, и любящая!"
    show player 13
    show mrsj 17
    mrsjo "Ой, Очень приятно это слышать от тебя."
    show mrsj 50
    mrsjo "Хмм..."
    show mrsj 49
    show player 1
    mrsjo "У меня другая идея!"
    mrsjo "Что если возьму это внимание..."
    show player 11
    mrsjo "... и отдам его {b}тебе{/b}?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "Что-то не так?"
    mrsjo "Только если ты хочешь,вот что я хотела сказать..."
    show player 21
    show mrsj 50
    player_name "Я-я совсем не против!"
    player_name "Но,только при условии что {b}Erik{/b} будет не против."
    show player 1
    show mrsj 49
    mrsjo "Просто спросите его!"
    mrsjo "Я уверена, что он будет не против..."
    show player 13
    mrsjo "... особенно если он будет слишком занят,играя с другой девушкой! Ха ха."
    show player 29
    show mrsj 50
    player_name "Наверное, да, Ха-ха."
    show player 14
    player_name "Я постараюсь найти ему кого-нибудь..."
    show player 13
    show mrsj 49
    mrsjo "Верниcь и дай мне знать, что произойдет."
    show player 17
    show mrsj 50
    player_name "Конечно, {b}Mrs. Johnson{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_sex_ed_prep:
    show mrsj 14 at right
    show player 10 at left
    player_name "Как мы можем вам помочь подготовиться к нашемиу сексуальному обучению еще раз?"
    show player 5
    show mrsj 17
    mrsjo "Мне нужна хорошая учебная книга, например {b}Камасутра{/b}."
    mrsjo "И некоторые {b}противозачаточные таблетки{/b}!"
    show mrsj 49
    mrsjo "Осторожность не бывает излишней..."
    show mrsj 50
    show player 14
    player_name "Хорошо."
    player_name "Я постараюсь найти её..."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_got_gf:
    show player 14
    player_name "Думаю, мне удалось познакомить {b}Erik{/b}с девченкой из школы!"
    show player 1
    show mrsj 17
    mrsjo "Серьезно?!"
    show player 14
    show mrsj 14
    player_name "Да!"
    player_name "У них так много общего, они идеально подходят друг другу!"
    show mrsj 17
    show player 17
    player_name "Я думаю, что это сработает наверняка!"
    show player 1
    show mrsj 18
    mrsjo "Это замечательно!!"
    show mrsj 17
    mrsjo "Не могу поверить, что ты был так добр к {b}Erik{/b}."
    show mrsj 49
    mrsjo "Думаю, пришло мне время дать тебе небольшую награду..."
    show player 21
    show mrsj 50
    player_name "Мм... Награду?"
    show player 11
    show mrsj 49
    mrsjo "Как насчет того чтобы я дала тебе немного... {b}Частных{/b} уроков йоги..."
    mrsjo "Таких, которых не увидишь в спортзале."
    show mrsj 50
    show player 21
    player_name "Это было бы потрясающе, {b}Mrs. Johnson{/b}!"
    show player 13
    show mrsj 49
    mrsjo "Просто приходи ко мне ночью в мою комнату... убедитесь, что ты хорошо отдохнул!"
    show player 11
    mrsjo "Это может быть... довольно изматывающе."
    show player 21
    show mrsj 50
    player_name "Д-да, {b}Mrs. Johnson{/b}."
    show player 13
    show mrsj 49
    mrsjo "Увидимся позже, я буду ждать!"
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_stole_gf:
    show mrsj 19c at right
    show player 10 at left
    player_name "Я не думаю, что из этого что-нибудь получится с {b}June{/b}..."
    show player 11
    show mrsj 19
    mrsjo "С девочки из школы?"
    show player 10
    show mrsj 19c
    player_name "Да."
    show player 5
    show mrsj 19
    mrsjo "Такая жалость..."
    mrsjo "Что случилось?"
    show player 10
    show mrsj 19c
    player_name "Она просто не заинтересована, и..."
    show mrsj 51
    player_name "... возможно она прийдет ко мне домой попозже, чтобы потусоваться со мной."
    show player 5
    show mrsj 52
    mrsjo "Ох мой..."
    mrsjo "{b}Erik{/b} не против этого?"
    show player 10
    show mrsj 51
    player_name "Я не уверен... наверное нет?"
    show player 5
    show mrsj 52
    mrsjo "Я должна сказать... Я немного разочарована в тебе, {b}[firstname]{/b}."
    show mrsj 51
    player_name "..."
    show mrsj 52
    mrsjo "Ты знаешь что она нравится{b}Erik{/b}..."
    mrsjo "... Я думала, он твой друг.!"
    show player 10
    show mrsj 51
    player_name "Простите меня, {b}Mrs. Johnson{/b}."
    player_name "Я сейчас пойду домой."
    hide mrsj
    hide player
    return

label button_mrsj_erik_introduce_june:
    show player 14
    player_name "В школе есть девушка, которая я думаю {b}Erik{/b} нравится."
    show player 1
    show mrsj 17
    mrsjo "Серьезно?"
    show mrsj 18
    mrsjo "Это прекрасно!"
    show mrsj 17
    mrsjo "Ты её знаешь? Какая она?!"
    show mrsj 14
    show player 14
    player_name "Нет, Я с ней еще не разговаривал."
    player_name "Я думаю,что она из другого класса."
    show mrsj 17
    show player 1
    mrsjo "Ох, я вижу."
    show player 11
    mrsjo "{b}Erik{/b} говорил с ней?"
    show mrsj 14
    show player 10
    player_name "Врят ли... Он говорит что он слишком стесняется."
    player_name "Я сказал ему, что узнаю о ней больше и дам ему знать,что её нравится."
    show mrsj 18
    show player 13
    mrsjo "Это так мило с твоей стороны!!"
    show mrsj 17
    mrsjo "Ему очень повезло, что ты как друг..."
    show mrsj 14
    show player 14
    player_name "Ох, Я уверен, что он сделал бы то же самое для меня!"
    show mrsj 49
    show player 1
    mrsjo "Знаешь что, расскажешь, как все пройдет..."
    show player 11
    mrsjo "Если ты можешь найти {b}Erik{/b} девушку, тебя ждет особое вознограждение..."
    show mrsj 50
    player_name "..."
    show player 21
    player_name "Конечно, {b}Mrs. Johnson{/b}!"
    show player 1
    show mrsj 14
    return

label button_mrsj_breastfeeding:
    show mrsj 38 at right
    show player 12 at left
    player_name "Итак как долго вы...вскармливаете грудью {b}Erik{/b}?"
    show player 5
    show mrsj 52
    mrsjo "Ох..."
    mrsjo "Слушай, это не то что ты мог подумать."
    mrsjo "Я просто всегда его так поощряла."
    show mrsj 38
    show player 11
    mrsjo "..."
    show mrsj 52
    mrsjo "Ты знаешь, что он не получает много внимания от девочек в школе."
    mrsjo "Мне было так жаль его!"
    mrsjo "Я просто хотела чтобы {b}Erik{/b} испытал и увидел как устроены все женщины!"
    show mrsj 20
    mrsjo "Но, возможно, я...я переборшила с этим?"
    show mrsj 19c
    show player 5
    player_name "..."
    show player 12
    player_name "Это так замечательно, что вы так заботитесь и уделяете ему внимание!"
    show mrsj 14
    show player 10
    player_name "Я думаю,что ему очень повезло..."
    show player 11
    show mrsj 18
    mrsjo "Ох,Ха ха!"
    show mrsj 17
    mrsjo "Что ж, спасибо..."
    mrsjo "Я думаю, что такой хорошей молодой парень, как ты нуждается во всем внимании которое ему нужно..."
    show mrsj 14
    show player 13
    player_name "..."
    show mrsj 49
    mrsjo "Я имею в виду, спасибо за понимание, {b}[firstname]{/b}."
    show mrsj 52
    mrsjo "Просто...запомни что мы должны сохранить это только между нами, хорошо?"
    show mrsj 14
    show player 14
    player_name "Да, {b}Mrs. Johnson{/b}."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_yoga_help_repeat:
    show player 10
    player_name "С чем вам нужна была моя помощь?"
    show player 5
    show mrsj 19
    mrsjo "Мне нужно, чтобы кто-то кто пошел бы и {b}провел мой урок йоги сегодня вечером{/b}."
    show mrsj 49
    mrsjo "Как ты думаете, ты смог бы помочь твоей... любимой соседке??"
    show mrsj 50
    show player 14
    player_name "Конечно!"
    show player 13
    show mrsj 17
    mrsjo "Не забудь {b}изучите жти движения йоги из этого списка{/b} которые я дала!"
    return

label button_mrsj_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Я хочу сказать, {b}Mrs. Johnson{/b}, вы в очень хорошей форме!"
    player_name "Вы очень много тренируетесь?"
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ой... Ты такой милый!"
    show mrsj 17 at right
    mrsjo "Ну, я стараюсь использовать тренажерный зал так часто, как я могу..."
    mrsjo "...Я так же занимаюсь пробежкой! И я ночью занимаюсь йогой в моей комнате..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Ну, это работает!"
    show player 13 at left
    mrsjo "Ты думаешь?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Моя {b}задница{/b} по-проежнему является слишком большой..."
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...И мои {b}сиськи{/b} не похоже не те какие были раньше..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*Глоток*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Есть ли что-нибудь еще, о чем ты хочешь поговорить?"
    return

label button_mrsj_invite_poker:
    player_name "Я хотел спросить, не хотите ли вы присоединиться к {b}Erik{/b} и мне к покеру?"
    show player 1
    show mrsj 17
    mrsjo "Сейчас?"
    show player 14
    show mrsj 14
    player_name "Да... Я имею в виду вы не обязаны!"
    player_name "{b}Erik{/b} и я просто ищем третьего игрока..."
    show player 1
    show mrsj 17
    mrsjo "Он ждет внизу ?"
    show player 14
    show mrsj 14
    player_name "Да, мы хотели бы сыграть сейчас, если вы свободны?"
    show player 1
    mrsjo "Хммм..."
    show mrsj 17
    mrsjo "Я думаю, я могла бы сыграть одну игру или две."
    show mrsj 18
    show player 13
    mrsjo "Хорошо,встретимся тогда с вами там внизу!"
    show player 18
    show mrsj 14
    player_name "Круто! Спасибо, {b}Mrs. Johnson{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
