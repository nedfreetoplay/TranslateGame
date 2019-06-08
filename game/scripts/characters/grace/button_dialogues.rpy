label button_grace_mia_get_tattoo:
    scene tattoo_indoor_c
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Эй, там!"
    grace "У вас здесь встреча?"
    return

label button_grace_generic:
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Эй, там!"
    grace "У вас здесь встреча?"
    return

label button_grace_tattoo:
    show mia 10f
    mia "Я хотела бы сделать тату... Сейчас."
    show mia 7f
    show grace f_normal_talk
    grace "Сейчас? Я вижу..."
    show grace f_suspicious
    grace "Вы уже придумали какой-нибудь рисунок?"
    show grace f_normal
    show mia 30f at Position (xoffset=64) with dissolve
    mia "Мой друг нарисовал это для меня, и Я хотела бы его сделать сегодня!"
    show mia 7f
    show grace f_normal_down_talk a_dressed_hip_paper
    with dissolve
    grace "Хмм..."
    show grace f_normal_talk
    grace "Ты уверена что ты этого хочешь?"
    grace "Татуировки постоянные, так что я должна убиться что мои клиенты знают что они делают!"
    show grace f_normal
    show mia 10f
    mia "Я думала об этом об этом уже долгое время... Да, я и правда хочу это сделать."
    show mia 7f
    show grace f_normal_talk
    grace "Отлично, солнышко. но, это не дешево!"
    show grace f_normal
    show player 14
    player_name "Сколько это стоит?"
    show player 13
    show grace f_normal_down_talk
    grace "Для этого размера... с цветами... примерно {b}$400{/b}."
    show grace f_normal
    show player 22
    show mia 12f
    mia "!!!"
    mia "Черт... Я думаю у меня только {b}$200{/b}..."
    show mia 8f
    show player 11
    player_name "..."
    show player 10
    player_name "Тебе не хватает?"
    show player 5
    show mia 12 with dissolve
    mia "Нет, это все что мне удалось накопить."
    mia "Как думаешь что мне делать?"
    show mia 8
    return

label button_grace_tattoo_help:
    show player 14
    player_name "Я позабочусь об остальном."
    show player 13
    show mia 12
    mia "Реально?!"
    show mia 7
    show player 14
    player_name "Почему нет."
    player_name "Я работал в последнее время так что у меня есть немного денег чтобы потратить..."
    show player 17
    player_name "...И это ради благого дела!"
    show player 13
    show mia 10
    mia "Это очень мило с твоей стороны..."
    mia "...и я обязательно верну тебе деньги!"
    show mia 7
    show player 17
    player_name "Все в порядке, ха ха."
    show player 13
    show grace f_normal_talk
    grace "So?"
    show mia 7f with dissolve
    grace "Готова начать?"
    show grace f_normal
    show mia 10f
    mia "Я готова!"
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve

    scene tattoo_cs01
    show text "Потребовалось некоторое время чтобы {b}Грэйс{/b} закончила работу.\nЯ очень переживал за {b}Мию{/b}...\n...но, казалось что она была в порядке на протяжении всего времени!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide tattoo_cs01
    with dissolve

    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    with dissolve
    grace "Все готово!"
    grace "Я надеюсть вам это понравится ребята."
    show grace f_normal
    show mia 10f
    mia "Это потрясающе! И это не было так больно как я думала..."
    show mia 7f
    show grace f_normal_talk
    grace "Удоставерься что ты оставила повязку на ней по крайней мере несколько дней."
    show grace f_normal
    show mia 10f
    mia "Хорошо, спасибо!"
    show mia 7f
    show grace f_normal_talk
    grace "Пока, ребята."
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 7 at right
    with dissolve
    show player 14
    player_name "Ну как?"
    show player 13
    show mia 12
    mia "Татуировка?"
    show mia 7
    show player 14
    player_name "Да."
    show player 13
    show mia 12
    mia "Все прекрасно... просто немножко покалывает."
    show mia 10
    mia "И я рада что это сделала... Я наконец могу сказать что я сделать то чего я хотела."
    show mia 7
    show player 10
    player_name "Ты не боишся что твоя мама сможет об этом узнать?"
    show player 5
    show mia 9
    mia "Надеюсь что нет, но оно находится в хорошо скрытом месте, ха ха."
    show mia 7
    show player 17
    player_name "Я думаю это круто что ты сделала."
    show player 18
    show mia 10
    mia "Спасибо, {b}[firstname]{/b}.Я счаслива что ты пошел со мной."
    show player 13
    mia "Тем не менее, мне нужно идти.Прежде чем моя мама начала что-то подозревать..."
    show mia 7
    show player 14
    player_name "Хорошо, увидимся в школе!"
    show player 13
    show mia 10
    mia "Пока."
    hide player
    hide mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    show player 10
    player_name "Может быть нам вернуться попозже?"
    show player 5
    mia "..."
    show mia 12
    mia "Я думаю мы должны."
    show mia 8
    show player 10
    player_name "Все будет хорошо. Мы всегда сможем вернуться в другой раз."
    show player 5
    show mia 12
    mia "Ты прав."
    show mia 8
    show player 10
    player_name "Очень жаль что ты не смогла сделать свою Татуировку сегодня..."
    show player 5
    show mia 12
    mia "Все нормально. Сейчас мне нужно идти домой."
    show mia 8
    show player 10
    player_name "Хорошо, увидимся позже."
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene location_tattoo_indoor_closeup
    show player 10 zorder 3 at left
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace f_normal zorder 0 at right
    player_name "Могу я тебя спросить?"
    show player 11
    show grace f_normal_talk
    grace "Конечно!"
    show player 10
    show grace f_normal
    player_name "Ну, ты видишь..."
    show player 11
    pause
    show player 10
    player_name "Дело в том..."
    show player 11
    grace "..."
    show player 10
    player_name "... Дело вот в чем..."
    show player 11
    show eve 2f zorder 2 at Position(xpos=0.35, ypos=1.0) with dissolve
    eve "Господи, выкладывай уже, {b}[firstname]{/b}!"
    show eve 1bf with dissolve
    eve "Как дела, Хрюшка Энн?"
    show eve 5f with dissolve
    show grace f_laugh
    grace "Хех, не очень."
    show grace f_normal_talk
    grace "Ты останешься вне проблем, Дрянь?"
    show eve 6bf
    show grace f_normal
    eve "Конечно нет."
    show player 1
    show eve 5f
    show grace f_laugh
    grace "Хехе."
    show eve 2f
    show grace f_normal
    eve "Смотри, {b}[firstname]{/b} здесь нужно немного чернил."
    show eve 5f
    show grace f_normal_talk
    grace "Ох, ты думаешь сделать здесь себе тату, Кобель?"
    show player 11
    show grace f_normal
    player_name "..."
    show eve 1bf with dissolve
    eve "Нет, нет, нет. Ему нажны на самом деле чернилы! Как в бутылках, да Тупица!"
    show eve 6bf
    eve "Извини, она может быть немного заторможенной."
    show eve 5f
    show grace f_suspicious
    grace "Хэй! Я всё слышала!"
    show eve 6f
    show grace f_normal
    eve "Да, Я специально сказала это громко..."
    show eve 5f
    show grace f_laugh
    grace "Хаха, по умничай тут."
    show eve 6f
    show grace f_normal
    eve "Люблю тебя, Сис!"
    show eve 5f
    show grace f_normal_talk
    grace "Да, да. Тебе повезло что ты милашка."
    show player 1
    show grace f_normal
    show eve 1bf with dissolve
    eve "Я, я не милашка?"
    show grace f_normal_talk
    show eve 5f with dissolve
    grace "Итак, сколько чернил тебе нужно, {b}[firstname]{/b}?"
    show player 2
    show grace f_normal
    player_name "Эммм, я не уверен."
    player_name "Ровно столько, чтобы сделать одну картину."
    show player 1
    show grace f_normal_talk
    grace "Ааах, художник, хм?"
    show grace f_laugh
    grace "Иллюстрации, первого парня {b}Иви{/b} привело в дом художника."
    show player 11
    show grace f_normal
    show eve 6bf
    eve "Чч, лучше чем этот байкерский фрик который шлялся здесь в старшей школе."
    show eve 1f
    show grace f_laugh
    grace "Хех, у тебя тут нет оргументов..."
    show grace f_normal_talk
    grace "Одну бутылку каждого цвета будет достаточно?"
    show grace f_suspicious
    grace "Я предпологаю ты знаешь как смешивать?"
    show player 10
    show grace f_normal
    player_name "Смешивать?"
    show player 11
    show eve 2f
    eve "Да, ты знаешь? Голубой и красный создает фиолетовый."
    eve "Желтый и синий создает зеленый."
    show player 2
    show eve 1f
    player_name "Ох да, как цветное колесо, так?"
    show player 1
    show grace f_normal_talk
    grace "Да, точно."
    show grace f_suspicious
    grace "Теперь я думаю единственный вопрос для меня, что ты сделаешь для меня?"
    show grace f_normal
    show player 10
    player_name "Ах, эмм. Я не зняю? Что ты хочешь чтобы я сделал?"
    show grace f_suspicious
    show player 11
    grace "Хмм, ты заметил граффити на стене дома когда ты входил?"
    show player 10
    show grace f_normal
    player_name "... Да, его довольно трудно не заметить."
    show player 11
    show grace f_normal_talk
    grace "Я отдам тебе краски если ты сотрешь его для меня."
    show grace f_normal
    show eve 2f
    eve "Взаправду?"
    show player 2
    show eve 1f
    player_name "Я это сделаю!"
    show player 1
    show eve 6bf
    grace "Пфффф, что за пустая трата времени!"
    show eve 1f
    show player 11
    player_name "..."
    show eve 1bf with dissolve
    eve "Оно снова будет помечено..."
    show eve 1f
    show grace f_angry_talk a_dressed_hips_mad
    with dissolve
    grace "Чтож, это все твои тупые блядские друзья продолжают этим заниматься!"
    grace "Тебе нужно сказать этим маленьким сучкам, Я надеру их чертовы задницы если это повторится снова!"
    show grace f_angry
    show player 10
    player_name "Черт я не знал, что твоя {b}Сестра{/b} была такой большой задницей!"
    show eve 6f
    show player 11
    eve "Хех, ты не предстовляешь."
    show eve 5f
    show grace f_angry_talk
    grace "Я не знаю почему ты общаешься так или иначе общаешься с этой кучкой придурков..."
    show eve 2f
    show grace f_angry
    eve "... Если ты хочешь шантажировать {b}[firstname]{/b} через выполнение этой работы. Ты могла бы по крайней мере сделать для него что то полезное."
    eve "Напримере передвинуть все это тяжелое дерьмо которое ты заказала в подсобку?"
    show eve 6bf
    show grace f_normal a_dressed_hip with dissolve
    eve "Я не хочу надрывать свою вагину чтобы перенести это дерьмо!"
    show eve 5f
    show grace f_suspicious
    grace "Хммм, Я думаю что это не плохая идея."
    show grace f_laugh
    grace "...Особенно если ты заткнешься о своей вагине! Агх!"
    show grace f_normal
    show eve 6bf
    eve "... Сука."
    show eve 5f
    show grace f_laugh
    grace "Хахаха, не притворяйся будьто не любишь насилие."
    show grace f_normal
    show eve 6bf
    eve "Да, да..."
    show eve 2f
    eve "Если ты меня простишь, {b}[firstname]{/b}."
    show player 1
    eve "Я должна пойти предупредить парней что {b}Грэйс{/b} снова обьявила войну."
    show eve 1f
    show grace f_laugh
    grace "Черт побери!"
    show grace f_normal
    show eve 6f
    eve "Увидимся, Сис!"
    hide eve
    with dissolve
    show grace f_normal_talk
    grace "{b}Коробки прямо перед стойкой{/b}. Только {b}перемести их{/b} за мою спину и краска твоя."
    show grace f_normal
    show player 2
    player_name "Звучит Отлично!"
    return

label button_grace_you_look_familiar:
    show player 10
    player_name "Ты знаешь... Я думаю..."
    show player 12
    player_name "Эммм."
    show player 34
    show grace f_suspicious
    grace "Всё в порядке?"
    show grace f_normal
    show player 30
    player_name "Извини, но ты выглядишь... знакомой."
    show player 5
    show grace f_suspicious
    grace "Хм?"
    show grace f_normal_talk
    grace "Хмм... Наверно ты говоришь о моей сестре?"
    show grace f_normal
    show player 12
    player_name "Сестры?"
    show player 11
    show grace f_suspicious
    grace "Моя маленькая сестра? {b}Ева{/b}?"
    show grace f_normal
    show player 38 with dissolve
    player_name "Ох! Конечно!"
    show player 14 with dissolve
    player_name "Я теперь вижу связь."
    show player 13
    show grace f_laugh
    grace "Ха Ха."
    show grace f_normal_talk
    grace "В любом случае, Я могу что то для тебя сделать?"
    return

label button_grace_nothing:
    show player 14
    player_name "Я просто осматриваюсь."
    show player 13
    show grace f_normal_talk
    grace "Круто! Осмотрись."
    grace "Я делаю все стили и проекты, продемонстрированные в моем магазине!"
    grace "Просто дай мне знать если тыбе чего то захочется, и мы сможем договориться о встрече!"
    show grace f_normal
    show player 14
    player_name "Хорошо, Спасибо!"
    show player 13
    show grace f_normal_talk
    grace "Увидимся."
    hide grace
    hide mia
    hide player
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
