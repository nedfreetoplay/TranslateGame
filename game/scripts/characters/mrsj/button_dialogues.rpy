label button_mrsj_greetings:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Привет, {b}Миссис Джонсон{/b}!"
    show player 1
    show mrsj 17
    mrsjo "Привет, {b}[firstname]{/b}!"
    mrsjo "Как твои дела?"
    show player 14
    show mrsj 14
    player_name "У меня всё хорошо, спасибо!"
    show player 1
    show mrsj 17
    mrsjo "Я могу что-нибудь сделать для тебя?"
    show mrsj 14
    return


label button_mrsj_sex_ed_intro:
    scene erik_upstairs_night_c
    show mrsj 42 at right
    show player 11 zorder 2 at left
    show erik 1f zorder 1 at Position(xpos=300)
    with dissolve
    mrsjo "Эй, мальчик..."
    show mrsj 41
    show player 21
    player_name "П-привет, {b}Миссис Джонсон{/b}!"
    show player 13
    show erik 4f
    eri "Ты... Очень симпатичный, {b}Миссис Джонсон{/b}."
    show erik 1f
    show mrsj 40b with fastdissolve
    mrsjo "Ну, ты просто будешь пялиться на меня или хочешь спросить меня кое о чем?"
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
    player_name "Вы... Вы голая, {b}Миссис Джонсон{/b}."
    show player 434
    show mrsj 54
    mrsjo "Мне нравится чувствовать... комфорт в моей комнате..."
    mrsjo "Ты что-то спрашивал у меня?"
    show mrsj 53
    return

label button_mrsj_about_erik:
    show player 14 at left
    show mrsj 14 at right
    player_name "Я хотел поговорить о {b}Эрике{/b}..."
    show player 1
    show mrsj 19
    mrsjo "О, он в порядке?"
    show player 14
    show mrsj 19c
    player_name "Да, он в порядке."
    player_name "Я разговаривала с ним о том, что произошло в ту ночь..."
    show player 11
    show mrsj 19
    mrsjo "Он расстроен?"
    show player 14
    show mrsj 19c
    player_name "Нет, вовсе нет."
    show player 10
    player_name "Он просто не уверен в том, чего он хочет..."
    show player 11
    show mrsj 19
    mrsjo "Как так?"
    show player 10
    show mrsj 19c
    player_name "Я думаю, он откажется от встречи с девушками."
    player_name "Я мог бы попытаться помочь ему получить девушку, но я думаю, что он любит больше вас..."
    show player 13
    show mrsj 19
    mrsjo "Вот это да..."
    show mrsj 20
    mrsjo "Неужели я слишком сильно его приютила?"
    show mrsj 19
    mrsjo "Что, по-твоему, я должна сделать?"
    show mrsj 19c
    return

label button_mrsj_route_sex_ed:
    show player 14 at left
    show mrsj 19c at right
    player_name "Я думаю, что лучше, если ты дашь ему то внимание, которое ему нужно..."
    show mrsj 19
    show player 1
    mrsjo "Ты правда так считаешь?"
    show mrsj 19c
    show player 14
    player_name "Ну, я не думаю, что он хочет видеть других девушек..."
    player_name "... И ты ему очень нравишься!"
    show mrsj 19
    show player 1
    mrsjo "Он всегда был близок ко мне..."
    show mrsj 19c
    show player 14
    player_name "У нас было такое прекрасное время в ту ночь!"
    player_name "Я никогда не видела {b}Эрика{/b} таким счастливым."
    show mrsj 19
    show player 11
    mrsjo "Как думаешь ... вы, ребята, хотели бы больше такого ... внимания?"
    show mrsj 19c
    show player 21
    player_name "Я... Думаю, да!"
    show mrsj 20
    show player 13
    mrsjo "Если ни одна из девушек из школы не даст ему того внимания, которое ему нужно..."
    show mrsj 19
    mrsjo "...Может быть, я должна быть одна?"
    show mrsj 14
    show player 14
    player_name "Я думаю, ему это понравится."
    show mrsj 49
    show player 11
    mrsjo "Что делать, если я дам вам, ребята некоторые... личное половое воспитание?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "Это только для образовательных целей, конечно..."
    show mrsj 50
    show player 29
    player_name "Ох, я эмм... Я бы не возражал!"
    show mrsj 49
    show player 13
    mrsjo "Я должна сначала подумать, но."
    show mrsj 50
    show player 14
    player_name "Конечно, {b}Миссис Джонсон{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_route_gf:
    show player 14 at left
    show mrsj 19c
    player_name "Я думаю, мы должны попытаться найти ему девушку."
    show player 1
    show mrsj 19
    mrsjo "Ты правда так считаешь?"
    show player 14
    show mrsj 19c
    player_name "Ну, я думаю, он был бы счастливее..."
    player_name "... и это построит его уверенность!"
    show player 1
    show mrsj 20
    mrsjo "Ему нужно больше выходить..."
    show player 10
    show mrsj 19c
    player_name "Не поверь мне, у нас было очень весело в ту ночь..."
    show player 14
    player_name "... но я думаю, что {b}Эрику{/b} нужно найти девушку."
    show player 13
    show mrsj 20
    mrsjo "Ты прав..."
    show player 11
    show mrsj 19
    mrsjo "Но как насчет... меня?"
    show player 10
    show mrsj 19c
    player_name "Что вы имеете в виду?"
    show player 11
    show mrsj 19
    mrsjo "Ну..."
    mrsjo "Если {b}Эрик{/b} найдёт себе девушку... Что я буду делать?"
    show mrsj 20
    mrsjo "Я не буду никому уделять мое внимание..."
    show player 21
    show mrsj 19c
    player_name "О, я уверен, что вы найдете кого-то {b}Миссис Джонсон{/b}!"
    show mrsj 14
    player_name "Вы очень... привлекательная, и любящая!"
    show player 13
    show mrsj 17
    mrsjo "Ахх, очень мило, что ты сказал."
    show mrsj 50
    mrsjo "Хмм..."
    show mrsj 49
    show player 1
    mrsjo "У меня другая идея!"
    mrsjo "Что, если бы я взяла это внимание..."
    show player 11
    mrsjo "... и дал его {b}тебе{/b}?"
    show mrsj 50
    player_name "!!!" with vpunch
    show mrsj 49
    mrsjo "Что не так?"
    mrsjo "Только если ты захочешь, это то, что я хотела сказать..."
    show player 21
    show mrsj 50
    player_name "Я-я бы не возражал!"
    player_name "Но, только до тех пор, как {b}Эрику{/b} хорошо с этим."
    show player 1
    show mrsj 49
    mrsjo "Просто спроси его!"
    mrsjo "Я уверена, что он будет в порядке с этим..."
    show player 13
    mrsjo "... особенно, если он слишком занят игрой с другой девушкой! Ха-ха."
    show player 29
    show mrsj 50
    player_name "Полагаю, да, ха-ха."
    show player 14
    player_name "Я попытаюсь найти кого-нибудь для него..."
    show player 13
    show mrsj 49
    mrsjo "Вернись и дай мне знать, что происходит."
    show player 17
    show mrsj 50
    player_name "Конечно, {b}Миссис Джонсон{/b}!"
    show mrsj 14
    show player 1
    return

label button_mrsj_sex_ed_prep:
    show mrsj 14 at right
    show player 10 at left
    player_name "Как мы можем помочь вам подготовиться к половому воспитанию снова?"
    show player 5
    show mrsj 17
    mrsjo "Мне нужна хорошая Учебная книга, {b}Кама Сутра{/b}."
    mrsjo "И некоторые {b}противозачаточные таблетки{/b}!"
    show mrsj 49
    mrsjo "Вы никогда не можете быть слишком осторожны..."
    show mrsj 50
    show player 14
    player_name "Хорошо."
    player_name "Я постараюсь найти их..."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_erik_got_gf:
    show player 14
    player_name "Я думаю, что смог представить {b}Эрика{/b} девочке в школе!"
    show player 1
    show mrsj 17
    mrsjo "Правда?!"
    show player 14
    show mrsj 14
    player_name "Да!"
    player_name "Они имеют так много общего, они были бы идеальными друг для друга!"
    show mrsj 17
    show player 17
    player_name "Я думаю, что это сработает наверняка!"
    show player 1
    show mrsj 18
    mrsjo "Потрясающе!!"
    show mrsj 17
    mrsjo "Я не могу поверить, что ты был так хорошо с {b}Эриком{/b}."
    show mrsj 49
    mrsjo "Я думаю, что пришло время для меня, чтобы дать тебе небольшую награду..."
    show player 21
    show mrsj 50
    player_name "Эмм... Награда?"
    show player 11
    show mrsj 49
    mrsjo "Как насчет того, что я дам тебе некоторые... {b}частные{/b} уроки йоги..."
    mrsjo "Вид, который ты не получишь в спортзале."
    show mrsj 50
    show player 21
    player_name "Это было бы потрясающе, {b}Миссис Джонсоны{/b}!"
    show player 13
    show mrsj 49
    mrsjo "Просто приходи навестить меня ночью в моей комнате... Убедитесь, что ты хорошо отдохнул!"
    show player 11
    mrsjo "Для него может... довольно утомительно."
    show player 21
    show mrsj 50
    player_name "Да, {b}Миссис Джонсон{/b}."
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
    player_name "Я не думаю, что это будет работать с {b}Джуной{/b}..."
    show player 11
    show mrsj 19
    mrsjo "Девушка из школы?"
    show player 10
    show mrsj 19c
    player_name "Да."
    show player 5
    show mrsj 19
    mrsjo "Это такой позор..."
    mrsjo "Что случилось?"
    show player 10
    show mrsj 19c
    player_name "Она просто не интересуется, и..."
    show mrsj 51
    player_name "... она, возможно, приедет к моему дому позже, чтобы повиснуть со мной."
    show player 5
    show mrsj 52
    mrsjo "Вот это да..."
    mrsjo "{b}Эрик{/b} в порядке?"
    show player 10
    show mrsj 51
    player_name "Я не уверен ... возможно нет?"
    show player 5
    show mrsj 52
    mrsjo "Я должна сказать ... Я немного разочарован в тебе, {b}[firstname]{/b}."
    show mrsj 51
    player_name "..."
    show mrsj 52
    mrsjo "Ты знала, что {b}Эрик{/b} любил ее..."
    mrsjo "... Я думала, он твой друг!"
    show player 10
    show mrsj 51
    player_name "Простите, {b}Миссис Джонсон{/b}."
    player_name "Сейчас я пойду домой."
    hide mrsj
    hide player
    return

label button_mrsj_erik_introduce_june:
    show player 14
    player_name "В школе есть такая девушка, которой нравится {b}Эрик{/b}."
    show player 1
    show mrsj 17
    mrsjo "Серьёзно?"
    show mrsj 18
    mrsjo "Потрясающе!"
    show mrsj 17
    mrsjo "Ты ее знаешь? Что она любит?!"
    show mrsj 14
    show player 14
    player_name "Нет, я еще не говорил с ней."
    player_name "Я думаю, она из другого класса."
    show mrsj 17
    show player 1
    mrsjo "О, я понимаю."
    show player 11
    mrsjo "{b}Эрик{/b} говорит с ней?"
    show mrsj 14
    show player 10
    player_name "Я так не думаю... Он говорит, что слишком застенчив."
    player_name "Я сказал ему, что узнаю больше о ней и дам ему знать, кто она такая."
    show mrsj 18
    show player 13
    mrsjo "Это так мило с твоей стороны!"
    show mrsj 17
    mrsjo "Ему очень повезло, что ты была другом..."
    show mrsj 14
    show player 14
    player_name "О, я уверена, что он сделает то же самое для меня!"
    show mrsj 49
    show player 1
    mrsjo "Скажите, что, дайте мне знать, как все это происходит..."
    show player 11
    mrsjo "Если ты найдёшь {b}Эрику{/b} подругу, то тебя ждет специальная награда..."
    show mrsj 50
    player_name "..."
    show player 21
    player_name "Несомненно, {b}Миссис Джонсон{/b}!"
    show player 1
    show mrsj 14
    return

label button_mrsj_breastfeeding:
    show mrsj 38 at right
    show player 12 at left
    player_name "Так как долго вы...кормили грудью {b}Эрика{/b}?"
    show player 5
    show mrsj 52
    mrsjo "Ох..."
    mrsjo "Послушай, это не то, что ты можешь подумать."
    mrsjo "Я просто всегда воспитывала его вот так."
    show mrsj 38
    show player 11
    mrsjo "..."
    show mrsj 52
    mrsjo "Ты знаешь, что он не получает должного внимания от девочек в школе."
    mrsjo "Я так переживала за него!"
    mrsjo "Я просто хотела дать {b}Эрику{/b} испытать и посмотреть, что такое женщины!"
    show mrsj 20
    mrsjo "Но, может быть, я...Я закончила?"
    show mrsj 19c
    show player 5
    player_name "..."
    show player 12
    player_name "Это здорово, что вы так заботитесь и уделяете ему внимание!"
    show mrsj 14
    show player 10
    player_name "Я думаю, ему очень повезло..."
    show player 11
    show mrsj 18
    mrsjo "О, ха-ха!"
    show mrsj 17
    mrsjo "Что ж, благодарю тебя..."
    mrsjo "Я думаю, что хорошим молодым людям, как ты, нужно все, что ты можешь..."
    show mrsj 14
    show player 13
    player_name "..."
    show mrsj 49
    mrsjo "Я имею в виду, спасибо за понимание, {b}[firstname]{/b}."
    show mrsj 52
    mrsjo "Просто...не забудь оставить это между нами, ладно?"
    show mrsj 14
    show player 14
    player_name "Да, {b}Миссис Джонсон{/b}."
    hide player
    hide mrsj
    with dissolve
    return

label button_mrsj_yoga_help_repeat:
    show player 10
    player_name "Зачем вам помогать?"
    show player 5
    show mrsj 19
    mrsjo "Мне нужно, чтобы кто-то пошел и {b}научил моему классу йоги сегодня вечером{/b}."
    show mrsj 49
    mrsjo "Как вы думаете, вы могли бы помочь своей... любимой соседке??"
    show mrsj 50
    show player 14
    player_name "Конечно!"
    show player 13
    show mrsj 17
    mrsjo "Помни, что мы будем {b}изучать ту йогу, что фигурирует в этом списке{/b}, который я дала!"
    return

label button_mrsj_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Я должен сказать: {b}Миссис Джонсон{/b}, вы действительно в форме!"
    player_name "Вы много тренируетесь?"
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ой ... Ты такой милый!"
    show mrsj 17 at right
    mrsjo "Ну, я стараюсь ходить в спортзал так часто, как могу..."
    mrsjo "...Я бегаю!  И я занимаюсь йогой в своей комнате ночью..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Ну, это работает!"
    show player 13 at left
    mrsjo "Ты думаешь?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Моя {b}попа{/b} все ещё выглядит немного большой..."
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...И мои {b}сиськи{/b} не похожи на используемые..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*Глоток*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Есть ещё что-нибудь, о чём вы хотели поговорить?"
    return

label button_mrsj_invite_poker:
    player_name "Мне было интересно, хотите ли вы присоединиться к {b}Эрику{/b} и ко мне сыграть в покер?"
    show player 1
    show mrsj 17
    mrsjo "Прямо сейчас?"
    show player 14
    show mrsj 14
    player_name "Да... Я имею в виду, вам не обязательно!"
    player_name "{b}Эрик{/b} и я просто ищем третьего игрока..."
    show player 1
    show mrsj 17
    mrsjo "Он ждет внизу?"
    show player 14
    show mrsj 14
    player_name "Да, мы бы хотели поиграть сейчас, если вы свободны?"
    show player 1
    mrsjo "Хмм..."
    show mrsj 17
    mrsjo "Думаю, я могла бы сыграть в одну игру или две."
    show mrsj 18
    show player 13
    mrsjo "Хорошо, я встречу вас внизу!"
    show player 18
    show mrsj 14
    player_name "Замечательно! Спасибо, {b}Миссис Джонсон{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
