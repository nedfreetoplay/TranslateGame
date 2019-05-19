label barn_daisy_pregnancy_anouncement_repeat:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides f_normal at Position (xpos=600)
    show daisy f_normal at Position (xpos=300)
    with dissolve
    player_name "Привет, я получил твое сообщение."
    show player 5
    show diane f_normal_talk
    dia "{b}Привет, {b}[firstname]{/b}."
    dia "Эх ты, возможно, захочешь присесть..."
    show diane f_normal
    player_name "Э?"
    show player 10b
    player_name "Что происходит?"
    show player 5
    show diane f_normal_talk
    dia "{b}Дейзи{/b} опять беременна."
    show diane f_normal
    show player 10b
    player_name "Опять?!"
    player_name "Это-"
    show player 5
    pause
    show player 30
    player_name "Ты уверенна?"
    show player 5
    show diane f_normal_talk
    dia "Ну, бедняжка болела каждое утро в течение последних 3 дней, и она скучала по ее... Эмм..."
    show diane f_normal
    pause
    show diane f_shamed_talk_fardown
    dia "{b}*Ммм*{/b} Я почти уверена."
    show diane f_shamed_fardown
    show player 10b
    player_name "{b}*Уф*{/b} Хорошо..."
    show player 5b
    show diane f_normal_talk
    dia "О, не волнуйся. Все будет хорошо."
    show diane f_laugh
    dia "Ребенок-это благословение!"
    show diane f_normal
    show player 10b
    player_name "Как ты относишься ко всему этому {b}Дейзи{/b}?"
    show player 5b
    show daisy f_normal_talk
    daisy "Я снова стану мамой!"
    show daisy f_normal
    show diane f_laugh
    dia "Хе-хе, ты определенно милашка."
    show diane f_smirk_talk_fardown
    dia "Пойдем, принесем тебе поесть."
    dia "Теперь ты ешь за двоих."
    show diane f_smirk
    hide daisy with dissolve
    pause
    show diane f_smirk_talk
    dia "Выше нос, {b}[firstname]{/b}!"
    show diane f_smirk
    show player 5
    player_name "Эээ?"
    show diane f_smirk_talk
    dia "Ты снова станешь отцом."
    dia "Это хорошие новости."
    show diane f_smirk
    show player 14
    player_name "Да, я знаю."
    show player 13
    show diane f_laugh
    dia "Поздравляю!"
    show diane f_smirk
    show player 14
    player_name "Спасибо, {b}Диана{/b}."
    hide diane with dissolve
    pause
    show player 24
    player_name "( Вот черт. )"
    player_name "( У {b}Дейзи{/b} будет еще ребенок... )"
    player_name "{b}*глоток*{/b} Надеюсь я готов к этому."
    hide player with dissolve
    return

label barn_daisy_pregnancy_seen_in_labor:
    scene expression player.location.background_blur with None
    show player 5 at left
    show diane b_naked a_naked_sides f_normal_talk at Position (xpos=600)
    show daisy a_naked_baby f_down at Position (xpos=300)
    with dissolve
    dia "Вот он!"
    show diane f_normal
    pause
    show diane f_teasing_look
    show daisy f_normal
    dia "Вот твой папа!"
    show diane f_normal
    show player 3 with dissolve
    player_name "{b}*глоток*{/b}"
    show diane f_normal_talk
    dia "Давай, красавчик."
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "Ты должен познакомиться {b}со своим новым сыном{/b}."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}М-моим сыном{/b}?"
    else:
        dia "Ты должен познакомиться {b}со своей новой дочерью{/b}."
        show diane f_smirk_fardown
        show player 10 with dissolve
        player_name "{b}М-моей дочерью{/b}?"
    show player 13
    dia "Ммммммм."
    show player 426
    show daisy f_down
    with dissolve
    pause
    show player 14
    player_name "Вау..."
    if M_daisy.pregnancy.baby_gender == "boy":
        player_name "... Он такой милый!"
    else:
        player_name "... Она такая милая!"
    show player 426
    show diane f_laugh
    dia "Хехе, ага."
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "Прямо как его папочка."
    else:
        dia "Прямо как ее мамочка."
    show diane f_cheese
    show player 14b
    player_name "Как ты себя чувствуешь {b}Дейзи{/b}?"
    show player 1b
    show diane f_smirk_fardown
    show daisy f_sad_talk
    daisy "Уставшей."
    show daisy f_sad
    show diane f_normal_talk
    if M_daisy.pregnancy.baby_gender == "boy":
        dia "Она не спала всю ночь, выталкивая этого маленького парня."
    else:
        dia "Она не спала всю ночь, выталкивая эту девчонку."
    dia "Это отняло у нее много сил."
    show diane f_smirk_fardown
    pause
    show daisy f_down
    show player 10
    player_name "Все прошло хорошо, да?"
    show player 5
    show diane f_normal_talk
    dia "О, да."
    dia "Ты быстро встанешь на ноги, правда, милая?"
    show diane f_smirk_fardown
    show daisy f_down_talk
    daisy "Да!"
    show daisy f_laugh
    daisy "У нас ребенок, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Д-да, я знаю."
    player_name "Не волнуйтесь, я о вас позабочусь."
    show player 1b
    show diane f_laugh
    dia "О, ты такой милый, {b}[firstname]{/b}."
    show diane f_smirk_talk_fardown
    dia "Давай, мы должны дать им отдохнуть."
    dia "Попрощайся с папой!"
    show diane f_normal
    pause
    show player 429
    player_name "Скоро увидимся, хорошо?"
    show player 1b
    show daisy f_normal_talk
    daisy "Хорошо, {b}[firstname]{/b}."
    hide daisy
    hide player
    hide diane
    with dissolve
    return

label barn_daisy_pregnancy_anouncement_first:
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides f_sad at Position (xpos=600)
    show daisy f_sad at Position (xpos=300)
    with dissolve
    player_name "Привет, я получил твое сообщение."
    show player 5
    show diane f_sad_talk
    dia "{b}Привет, {b}[firstname]{/b}."
    dia "Эх ты, возможно, захочешь присесть..."
    show diane f_sad
    player_name "Эээ?"
    show player 10b
    player_name "Что происходит?"
    show player 5
    show diane f_sad_talk
    dia "Я думаю {b}Дейзи{/b} беременна."
    show diane f_sad
    show player 23
    player_name "Что?!"
    player_name "Я не думал,что-"
    player_name "В смысле, ты уверенна?!"
    show player 5
    show diane f_sad_talk
    dia "Ну, бедняжка болела каждое утро в течение последних 3 дней, и она скучала по ее... Эмм..."
    show diane f_sad
    pause
    show diane f_sad_talk
    dia "{b}*ух*{/b} Я почти уверена."
    show diane f_sad
    show player 10
    player_name "Вау, эмм... Хорошо."
    player_name "Я не думал, что она может забеременеть."
    show player 5
    show diane f_sad_talk
    dia "Да, я тоже так думала..."
    show diane f_sad
    show player 10
    player_name "Что мы будем делать?"
    show player 5
    show diane f_normal_talk
    dia "О, не волнуйся. Все будет хорошо."
    show diane f_laugh
    dia "Ребенок - это благословение!"
    show diane f_normal
    show player 10b
    player_name "Как ты относишься ко всему этому {b}Дейзи{/b}?"
    show player 5b
    show daisy f_sad_talk
    daisy "Я-"
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Я не знаю..."
    daisy "Думаешь, я буду хорошей мамой?"
    show daisy f_sad
    show diane f_normal_talk
    dia "Конечно, будешь, милая!"
    dia "Кроме того, {b}[firstname]{/b} и я будем здесь, чтобы помочь тебе на каждом шагу."
    show diane f_normal_talk
    dia "Не так ли, {b}[firstname]{/b}?"
    show diane f_normal
    show player 14
    player_name "Д-да, конечно!"
    show player 13
    show diane f_normal_talk
    dia "На самом деле, почему бы тебе не пойти со мной. У меня есть несколько книг на эту тему, ты можешь посмотреть их."
    show diane f_normal
    show daisy f_sad_talk
    daisy "Хорошо, {b}Диана{/b}."
    hide daisy
    hide diane
    with dissolve
    pause
    show player 24
    player_name "Вот черт."
    player_name "У {b}Дейзи{/b} будет мой ребенок..."
    player_name "{b}*глоток*{/b} Надеюсь, я к этому готов."
    hide player with dissolve
    return

label barn_daisy_caught_breeding_aftermath:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy f_laugh at Position (xpos=300)
    show diane b_naked a_naked_sides f_smirk at Position (xpos=580)
    with dissolve
    daisy "Привет, {b}[firstname]{/b}!"
    show daisy f_normal
    show player 14b
    player_name "Привет, {b}Дейзи{/b}. {b}Диана{/b}."
    show player 1
    show diane f_smirk_talk
    dia "Привет."
    show diane f_smirk
    pause
    show diane a_nudge f_smirk_talk_fardown with dissolve
    dia "{b}*хм*{/b}"
    show diane a_naked_sides f_smirk_fardown with dissolve
    show daisy f_shy_talk
    daisy "Итак, {b}Диана{/b} рассказала мне все о сексе..."
    show daisy f_shy
    show player 11
    player_name "!!!"
    show daisy f_shy_talk
    daisy "... И как это то, что два взрослых человека должны делать только тогда, когда они очень любят друг друга."
    show daisy f_shy
    show player 10b
    player_name "Хо-хорошо?"
    show player 5b
    show diane f_smirk_talk_fardown
    dia "Ииии?"
    show diane f_smirk_fardown
    show daisy f_shy_talk
    daisy "... И что мой учитель лгал и использовал меня, что неправильно..."
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Вот именно."
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "О!"
    show daisy f_shy_talk
    daisy "... И что их не называют ласками или тайниками."
    daisy "У тебя есть пенис, а у меня флугалище!"
    show daisy f_shy
    player_name "..."
    show diane f_smirk_talk_fardown
    dia "ВЛА-галище, милая."
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "Ой, прости!"
    daisy "Влагалище. У меня есть влагалище."
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Очень хорошо, милая."
    show diane f_smirk_fardown with None
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "Итак, можем ли {b}[firstname]{/b} и я заняться сексом сейчас?!"
    show daisy f_normal
    show player 11
    show diane f_surprised
    player_name "!!!" with hpunch
    show diane f_shamed_talk_smile
    dia "{b}*ох*{/b}"
    show player 5
    show diane f_shamed_talk_fardown
    dia "{b}Дейзи{/b}, я сказала тебе, почему {b}[firstname]{/b} и я занимаемся сексом, не так ли?"
    show diane f_shamed_fardown
    show daisy f_normal_talk
    daisy "Да, потому что вы взрослые люди, которые очень любят друг друга..."
    daisy "... И это увеличивает производство молока."
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "Правильно, это для моего бизнеса."
    show diane f_shamed_fardown
    show daisy f_laugh
    daisy "Я тоже часть бизнеса!"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "Я знаю это, но-"
    show diane f_shamed_fardown
    show daisy f_normal_talk
    daisy "... И я взрослая, и я люблю {b}[firstname]{/b}..."
    daisy "... И я тоже хочу секса!"
    show daisy f_normal
    show diane f_shamed_talk_fardown
    dia "{b}*ох*{/b}"
    dia "Ну, тогда это между тобой и {b}[firstname]{/b}."
    show daisy at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show diane f_shamed
    show player 10
    player_name "Эээ?!"
    show player 5
    pause
    show player 10
    player_name "Т-ты серьезно?!"
    show player 5
    show diane f_shamed_talk_smile
    dia "Она права."
    dia "Вы оба взрослые люди и если вы хотите заняться сексом, я не могу остановить тебя."
    dia "Я бы предпочла, чтобы мы держали все это в секрете, вместо того, чтобы вы двое делали это за моей спиной."
    show diane f_shamed
    show player 10
    player_name "Я не-"
    player_name "То есть, Я бы не стал-"
    show player 5
    show diane f_shamed_talk_smile
    dia "Все в порядке, {b}[firstname]{/b}."
    dia "{b}Дейзи{/b} милая девушка, и ты ей очень нравишься."
    dia "Если она тебе нравится, то ничего плохого нет если у вас двоих будет секс."
    dia "Просто пообещай мне, что будешь осторожна."
    show diane f_shamed
    show player 24
    player_name "..."
    show player 5b
    show daisy f_normal_talk
    daisy "Я буду осторожна!"
    show daisy f_normal
    show diane f_laugh
    dia "Хехе, хорошоя девочка {b}Дейзи{/b}."
    show diane f_smirk
    pause
    show diane f_smirk_talk
    dia "Ладно, вам двоим есть о чем поговорить, а мне пора возвращаться к работе."
    dia "Дай мне знать, если тебе что-нибудь понадобится."
    show diane f_smirk with None
    show daisy f_laugh at flip
    show daisy at Position (xpos=750)
    with dissolve
    show diane f_smirk_fardown
    daisy "Спасибо, {b}Диана{/b}!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Пожалуйста, милая."
    hide diane with dissolve
    pause
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "Ты в порядке, {b}[firstname]{/b}?"
    daisy "Ты выглядишь забавно."
    show daisy f_shy
    show player 10b
    player_name "Я не-"
    show player 5b
    pause
    show player 10b
    player_name "Все это так неожиданно."
    show player 5b
    show daisy f_sad_talk
    daisy "Ой."
    daisy "То есть, ты не хочешь заниматься со мной сексом?"
    show daisy f_sad
    show player 10b
    player_name "Я этого не говорю, просто ..... Ты уверена, что это то, чего ты хочешь?"
    show player 5b
    show daisy f_normal_talk
    daisy "О, да!"
    daisy "Ты заботишься обо мне и приносишь пиццу и красивые цветы!"
    daisy "Ты самый лучший человек на свете!"
    daisy "Я лучше займусь сексом с тобой, чем с хозяином..."
    show daisy f_normal
    show player 10b
    player_name "Да, но тебе не нужно ни с кем заниматься сексом, {b}Дейзи{/b}..."
    show player 5b
    show daisy f_normal_talk
    daisy "Я хочу!"
    show daisy f_sexy_talk
    daisy "Думаю, будет забавно засунуть твою ласку в мою норку!"
    show daisy f_sexy
    player_name "..."
    show daisy f_sexy_talk
    daisy "Прости, я имела в виду твой пенис... В моем флугалище."
    show daisy f_sexy
    show player 10b
    player_name "Влагалище."
    show player 5b
    show daisy f_shy_talk
    daisy "О, верно!"
    show daisy f_shy
    pause
    show daisy f_normal_talk
    daisy "Так ты хочешь заняться сексом?!"
    show daisy f_sexy
    return

label barn_daisy_caught_breeding_aftermath_yes:
    show player 14b
    player_name "Хорошо, давай сделаем это."
    show player 1b
    show daisy f_normal_talk
    daisy "{b}*ах*{/b} Правда?!"
    show daisy f_laugh
    daisy "Да!!!"
    show daisy f_normal
    show player 14b
    player_name "Пойдем к одному из доильных аппаратов."
    show player 1b
    show daisy f_laugh
    daisy "Хорошо!"
    hide daisy
    hide player
    with dissolve
    pause
    return

label barn_daisy_caught_breeding_aftermath_no:
    show player 10b
    player_name "{b}Дейзи{/b}, Я не думаю, что это хорошая идея."
    show player 5b
    show daisy f_sad_talk
    daisy "Нет?"
    show daisy f_sad
    show player 10b
    player_name "Мы не должны спешить с этим, не подумав."
    show player 5b
    show daisy f_sad_talk
    daisy "Еще подумать?"
    daisy "Я уже давно думаю о сексе с тобой!"
    show daisy f_sad
    show player 10b
    player_name "Правда?"
    show player 5b
    show daisy f_sad_talk
    daisy "Ух угу."
    show daisy f_sad
    pause
    show player 10b
    player_name "И все же я думаю... Мне нужно время, чтобы все это переварить..."
    show player 5b
    show daisy f_sad_talk
    daisy "О, хорошо."
    show daisy f_sad
    pause
    show daisy f_sad_talk
    daisy "Дай мне знать, когда будешь готов, ладно?"
    show daisy f_sad
    show player 10b
    player_name "Да, хорошо."
    show player 5b
    pause
    show player 10b
    player_name "Спасибо за понимание, {b}Дейзи{/b}."
    show player 5b
    show daisy f_sad_talk
    daisy "Пожалуйста."
    show daisy f_sad
    pause
    show player 10b
    player_name "Я должен-"
    player_name "{b}*хм*{/b} Мне нужно вернуться к работе."
    show player 5b
    show daisy f_sad_talk
    daisy "Хорошо."
    hide player
    hide daisy
    with dissolve
    return

label barn_dialogue_daisy_caught_breeding:
    scene expression player.location.background_blur with None
    show player 12 with dissolve
    player_name "Нет, {b}Диана{/b} хотела побыть наедине с {b}Дейзи{/b} чтобы разобраться во всей этой ситуации с \"лаской\" ..."
    player_name "Я не должен вмешиваться."
    hide player with dissolve
    return

label barn_daisy_dead_flowers:
    scene expression player.location.background_blur with None
    show player 1b at left
    show daisy b_naked_behind_sad f_empty a_empty zorder 1
    with dissolve
    daisy "О нет!!!"
    show player 5b
    player_name "Хмм?"
    daisy "Нет, нет, нет, нет!!"
    show player 10b
    player_name "{b}Дейзи{/b}?"
    show player 5b
    show daisy b_naked a_naked_cover f_sad_talk with dissolve
    daisy "{b}[firstname]{/b}, это ужасно!"
    daisy "{b}*фырк*{/b} Что-то не так!"
    show daisy f_sad
    show player 10b
    player_name "Эээ?"
    show player 5b
    show daisy f_sad_talk
    daisy "Я думаю, они больны!"
    show daisy f_sad
    show player 10b
    player_name "{b}Дейзи{/b}, Я не-"
    player_name "Кто болен?"
    show player 5b
    show daisy f_sad_talk a_naked_vase_wilted at Position (xpos=300) with dissolve
    daisy "Мои цветы!!!"
    show daisy f_sad
    show player 10b
    player_name "Все?!"
    show player 5b
    show daisy f_sad_talk
    daisy "{b}*фырк*{/b} Да..."
    show daisy f_sad
    show player 10b
    player_name "Как это произошло?"
    show player 5b
    show daisy f_sad_talk
    daisy "Я не знаю! {b}*фырк*{/b}"
    daisy "Они были вчера красивыми ..."
    show daisy f_sad
    show player 10b
    player_name "Мне так жаль, {b}Дейзи{/b}..."
    show player 5b
    show diane f_sad_talk b_shirtless a_shirtless_sides at Position (xpos=600) with dissolve
    show player 5
    dia "{b}Дейзи{/b} плачет?!"
    show diane f_sad with None
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "{b}Диана{/b}, что-то не так с моими прекрасными цветами!!"
    show daisy f_sad

    pause
    show diane f_shamed_talk_fardown
    dia "Ауу, милая..."
    dia "Так всегда бывает с цветами..."
    dia "... Им не суждено жить вечно."
    dia "Все будет хорошо."
    show diane f_shamed_fardown
    show daisy f_sad_talk
    daisy "{b}*фырк*{/b} Но... Но..."
    daisy "Как мы их исправим?"
    show daisy f_sad
    show diane f_shamed_talk_fardown
    dia "Боюсь, некоторые вещи нельзя исправить, дорогая..."
    show diane f_shamed_fardown
    show daisy f_sad_talk
    daisy "... Нет..."
    hide daisy
    hide diane
    show daisy b_naked_diane_comfort f_empty a_empty
    show diane b_empty a_empty f_shamed_talk_look
    with dissolve
    dia "Они, они."
    dia "Шшшшш."
    show diane f_shamed_talk_look_closed
    show daisy b_naked_diane_comfort2
    daisy "{b}*фырк*{/b} Что мы будем делать?"
    show daisy b_naked_diane_comfort
    show diane f_shamed_talk_look
    dia "Почему бы нам не добавить их в компостную кучу на заднем дворе?"
    dia "Таким образом, однажды они помогут нам сделать новые цветы."
    show daisy b_naked_diane_comfort2
    show diane f_shamed_talk_look_closed
    daisy "Правда?"
    show daisy b_naked_diane_comfort
    dia "Мммммм."
    show diane f_shamed_talk_look
    dia "Давай, милая. Я тебе покажу."
    show diane f_shamed_talk_look_closed
    show daisy b_naked_diane_comfort2
    daisy "{b}*фырк*{/b} Хорошо."
    hide daisy
    show diane f_shamed b_shirtless a_shirtless_sides at fliplright
    with dissolve
    pause
    hide diane
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "{b}[firstname]{/b}?"
    show diane f_normal
    show player 13
    player_name "Ммм?"
    show diane f_normal_talk
    dia "Почему бы тебе не сбегать в {b}торговый центр{/b} и не купить ей новые цветы?"
    show diane f_normal
    show player 10
    player_name "Сейчас?"
    show player 5
    show diane f_normal_talk
    dia "Да, это будет приятный сюрприз для нее."
    show diane f_normal
    show player 14
    player_name "Хорошо."
    show player 13
    show diane f_normal_talk
    dia "Попробуй достать ей что-нибудь большое и яркое."
    show diane f_laugh
    dia "{b}Подсолнухи{/b} были бы идеальны!"
    show diane f_normal
    show player 14
    player_name "Хорошо, я поищу {b}Подсолнухи{/b}."
    show player 13
    daisy "{b}Диана{/b}?!"
    show diane f_normal_talk at fliplright with dissolve
    dia "Иду, милая!"
    hide diane
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "Спасибо, {b}[firstname]{/b}."
    hide diane with dissolve
    pause
    show player 4 with dissolve
    player_name "( Хм, я думаю, что в новом магазине {b}Cupid{/b} в {b}торговом центре{/b} продают цветы. )"
    player_name "( {b}Я должен начать с него{/b}. )"
    hide player with dissolve
    return

label barn_front_daisy_pizza_craving:
    scene expression player.location.background_blur with None
    show player 684 with dissolve
    player_name "( Ох, сегодня так чертовски жарко! )"
    pause
    show player 24 with dissolve
    player_name "{b}*вздох*{/b} Мне нужно сделать перерыв на некоторое время..."
    show player 11
    daisy "{b}Диана{/b}!"
    daisy "Щекотно!!!"
    show player 30
    player_name "Хмм?"
    show player 5
    dia "Ну, мы хотим убедиться, что у нас есть все, не так ли?"
    daisy "Да..."
    show player 10
    player_name "Что они там делают?"
    hide player with dissolve
    pause
    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None

    show daisy b_diane_milking a_empty f_laugh with dissolve
    daisy "Хехехе!"
    dia "Ты должна перестать извиваться, милая."
    daisy "Я ничего не могу поделать!"
    show player 10 at left with dissolve
    player_name "Что происходит-"
    show player 11
    pause
    show player 29 with dissolve
    player_name "Вау."
    show player 3
    show daisy f_normal_talk
    daisy "Привет, {b}[firstname]{/b}."
    show daisy f_normal b_naked a_naked_sides at Position (xpos=300)
    show diane b_naked a_naked_sides f_normal_talk at Position (xpos=600)
    with dissolve
    dia "Привет, {b}[firstname]{/b}."
    dia "Я просто дою нашего нового друга."
    show diane f_normal
    show player 14 with dissolve
    player_name "Да, я вижу это."
    player_name "Извините, я оставлю вас наедине."
    show player 13
    show diane f_laugh
    dia "О, чепуха!"
    show diane f_normal_talk
    dia "Ничего такого, чего бы ты не видел раньше."
    show diane f_smirk_talk_fardown
    show daisy f_shy_back
    dia "Ты не против, если {b}[firstname]{/b} останется, милая?"
    show diane f_smirk_fardown
    show daisy f_shy_talk_back
    daisy "Нет, все в порядке."
    show daisy f_shy_talk
    daisy "{b}[firstname]{/b} это мило, правда?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Хех, да. {b}[firstname]{/b} это очень мило."
    show diane f_smirk
    show daisy f_normal
    show player 14
    player_name "Как долго это продолжается?"
    show player 13
    show diane f_smirk_talk
    dia "Ммм, всего пару дней."
    dia "Бедняжка начала вести себя странно, и я не могла понять, в чем проблема."
    dia "Оказывается, ее \"сиськи\" болели."
    show diane f_cheese
    pause
    show diane f_laugh
    dia "Ха-ха, ее слова, не мои."
    show diane f_smirk_fardown
    show daisy f_sad_talk
    daisy "Ну, мастер доил меня ежедневно..."
    daisy "... Но его больше нет рядом."
    show daisy f_sad
    show diane f_smirk_talk_fardown
    dia "Слава богу, что так."
    dia "Тебе гораздо лучше без этого жуткого старика!"
    show diane f_smirk_fardown
    pause
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    daisy "... Да."
    daisy "Мне нравится, когда {b}Диана{/b} делает это лучше."
    show daisy f_normal
    show diane f_laugh
    dia "Хе."
    show diane f_smirk_talk_fardown
    dia "Ну, если ты думаешь, что я хороша в этом, ты должена увидеть {b}[firstname]{/b}!"
    show diane f_smirk_fardown
    show daisy f_shy_talk
    daisy "Правда?!"
    show daisy f_shy
    dia "Мммммм."
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "{b}Диана{/b} говорит, ты ее тоже иногда доишь?"
    show daisy f_shy
    show diane f_smirk
    show player 14b
    player_name "Да, иногда..."
    show player 1b
    show daisy f_normal_talk
    daisy "Я никогда не встречала никого, кого нужно было бы доить, как меня."
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Возможно, {b}[firstname]{/b} может рассказать тебе больше о том, что мы здесь делаем, и отвлечь тебя от щекотки, а?"
    hide diane
    hide daisy
    show daisy b_diane_milking a_empty f_normal_talk
    with dissolve
    daisy "Да, хорошо."
    show daisy f_normal
    show player 10
    player_name "Ух, конечно..."
    show player 14
    player_name "{b}*хм*{/b} Видешь ли, {b}Диана{/b} продает молоко тем, кто в нем нуждается."
    show player 1
    show daisy f_shy_talk
    daisy "Людям оно нкжно?"
    show daisy f_shy
    show player 14
    player_name "Да."
    player_name "Некоторые из ее клиентов пьют его, а другие готовят с ним."
    player_name "Хех, я даже слышал, как некоторые из моих друзей говорят, что они смешивают его в своих протеиновых коктейлях..."
    show player 1
    show daisy f_laugh
    daisy "Вау, у {b}Дианы{/b} наверно вкусное молоко!"
    show daisy f_normal
    show player 14
    player_name "Да, оно действительно вкусное!"
    show player 1
    show daisy f_shy_back
    daisy "{b}Диана{/b}, ты должна продать и мое молоко!"
    show daisy b_naked a_naked_sides f_normal_talk at flip
    show daisy at Position (xpos=750)
    show diane b_naked a_naked_sides f_smirk_fardown at Position (xpos=600)
    with dissolve
    daisy "Хозяин говорил, что оно лучшее во всем мире!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Ты не против, если я продам немного?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Конечно!"
    daisy "Я тоже хочу помогать людям!"
    show daisy f_normal
    show diane f_laugh
    dia "Ха-ха, ты такая хорошая девочка, {b}Дейзи{/b}."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Угу!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Думаю, на сегодня мы закончили..."
    dia "Чувствуешь себя лучше?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Да, намного лучше."
    daisy "Спасибо, {b}Диана{/b}!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Нет проблем, милая."
    show diane f_smirk_fardown
    pause
    show diane f_smirk_talk_fardown
    dia "Тебе не кажется, что сейчас нам стоит тебя покормить?"
    show diane f_smirk_fardown
    show daisy f_laugh
    daisy "{b}*глоток*{/b} Овес?!"
    show daisy f_normal
    show diane f_laugh
    dia "Хех, опять овес?"
    show diane f_smirk_talk_fardown
    dia "{b}*вздох*{/b} Тебе не надоело все время есть овес?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Нет!"
    daisy "Хозяин всегда кормил меня овсом, он вкусный!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Хорошо, но твой старый хозяин больше не контролирует, что ты ешь..."
    dia "Может, попробуешь что-нибудь другое?"
    show diane f_smirk_fardown
    show daisy f_normal_smelling
    daisy "Ммм"
    show daisy f_normal_talk
    daisy "Я не знаю..."
    daisy "Что может быть лучше овса?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Хе-хе, много чего!"
    dia "Ты можешь попробовать еще что-нибудь из моего сада?"
    show diane f_smirk_fardown
    show daisy f_normal_smelling
    daisy "Хмм..."
    show daisy f_normal_talk at unflip
    show daisy at Position (xpos=300)
    with dissolve
    daisy "Что ты любишь есть, {b}[firstname]{/b}?"
    show daisy f_normal
    show diane f_normal
    show player 10b
    player_name "Я?"
    show player 17
    player_name "Чизбургеры!"
    show player 1b
    show diane f_sad_talk
    dia "{b}[firstname]{/b}, ты с ума сошел?!"
    show player 5
    dia "Мы не можем кормить ее чизбургер!!"
    show diane f_sad
    show player 10
    player_name "Хмм, почему?"
    show player 5
    pause
    show player 11
    pause
    show player 29 with dissolve
    player_name "Ой, верно..."
    show diane f_smirk
    player_name "... Потому что это говядина и она-"
    show player 3
    pause
    show player 14b
    player_name "Прости."
    show player 1b
    show daisy f_normal_talk
    daisy "Что такое чизбургер?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Не обращай внимания, дорогая."
    show diane f_normal
    show player 14b
    player_name "Тогда пицца!"
    show player 1b
    show daisy f_shy_talk
    daisy "Пицца?"
    show daisy f_shy
    pause
    show daisy f_laugh
    daisy "Хе-хе, забавное слово!"
    show daisy f_normal
    show diane f_thinking
    dia "Думаю, это может сработать..."
    show diane f_normal_talk
    show player 13
    dia "Хочешь сбегать в {b}пиццерию Тони{/b} и взять пиццу, чтобы она попробовала?"
    show diane f_normal
    show player 14
    player_name "Да, я могу это сделать."
    show player 13
    show daisy f_normal_talk
    daisy "Пицца!"
    show daisy f_laugh
    daisy "Хехехе!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Просто помни, что она травоядная, хорошо?"
    dia "Не знаю, справится ли она с мясом."
    show diane f_normal
    show player 14
    player_name "Понял!"
    player_name "{b}Одна вегетарианская пицца на подходе{/b}!"
    hide player with dissolve
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    show diane f_smirk_fardown
    daisy "ПИЦЦА!!!"
    show daisy f_normal
    show diane f_laugh
    dia "Хехе!"
    hide diane
    hide daisy
    with dissolve
    return

label barn_front_daisy_picking_flowers:
    scene expression player.location.background_blur with None
    show player 14 at left
    $ M_diane.outfit = "shirtless"
    show diane b_naked a_naked_sides
    with dissolve
    player_name "Привет {b}Диана{/b}."
    show player 13
    show diane f_normal_talk
    dia "Привет, жеребец."
    dia "Как ты сегодня?"
    show diane f_normal
    show player 14
    player_name "Я в порядке."
    player_name "Что ты делаешь в саду?"
    player_name "Разве ты не должна быть внутри с нашим новым другом?"
    show player 13
    show diane f_normal_talk
    dia "Вообще-то, это была ее идея."
    show diane f_normal
    show player 5
    player_name "Эээ?"
    show diane f_normal_talk
    dia "Посмотри сам."
    show diane f_normal
    show player 5f with dissolve
    pause
    scene expression "backgrounds/location_diane_garden_cutscene11.jpg" with fade
    player_name "Вау, посмотри на нее..."
    player_name "... Она улыбается!"
    dia "Я знаю, разве это не мило?!"
    dia "Ты бы видел, какой робкой она была, когда попросила разрешения выйти из амбара."
    dia "Это разбило мне сердце."
    player_name "Могу себе представить."
    player_name "Почему она голая?"
    dia "Я дала ей кое-какую одежду, но она сказала, что не любит ее носить."
    dia "Я не хотела ее принуждать."
    scene expression player.location.background_blur with None
    show player 10 at left
    show diane b_naked a_naked_sides at Position (xpos=600)
    with dissolve
    player_name "Итак..."
    player_name "Что ты собираешься с ней делать?"
    show player 5
    dia "Хмм?"
    show player 10
    player_name "Разве мы не должны позвонить кому-нибудь или куда-нибудь?"
    show player 5
    show diane f_normal_talk
    dia "Хе-хе, кого бы мы могли позвать для чего-то подобного?"
    show diane f_normal
    show player 10
    player_name "Не знаю? Контроль за животными?"
    show player 5
    show diane f_normal_talk
    dia "Нет, пусть она сама решает, что делать."
    dia "Сейчас, наверное, лучше, если она останется здесь, в сарае."
    dia "Кто знает, что случится, если ее кто-нибудь увидит."
    show diane f_normal
    show player 10
    player_name "Д-да, думаю, в этом есть смысл."
    show player 5
    cow "{b}Диана{/b}!"
    cow "{b}Диана{/b} ты видела все эти цветы?!"
    show daisy a_naked_bouquet f_down_talk at Position (xpos=300) with dissolve
    show player 1b
    cow "Они такие крас-"
    show daisy f_scared
    pause
    show daisy f_sad_talk
    show player 5b
    cow "Ик!"
    show daisy f_sad
    show diane f_shamed_talk_smile
    dia "Шшш, все в порядке милая."
    dia "Помнишь, о чем мы говорили?"
    dia "Это {b}[firstname]{/b} и он приятный мужчина."
    dia "Он не причинит тебе вреда."
    show diane f_shamed
    cow "..."
    show daisy f_shy_back
    show diane f_shamed_talk_smile
    dia "Ты не причинишь ей боль, {b}[firstname]{/b}?"
    show diane f_shamed
    show player 29 with dissolve
    show daisy f_sad
    player_name "Низачто."
    show player 4
    cow "..."
    show player 14b with dissolve
    player_name "Мне нравятся твои цветы."
    show player 1b
    show daisy f_sad_talk
    cow "Правда?"
    show daisy f_sad
    show diane f_normal
    show player 14b
    player_name "Да, они очень красивые."
    show player 1b
    pause
    show daisy f_sad_talk
    cow "{b}Диана{/b} говорит, что это ты меня разбудил."
    show daisy f_sad
    show player 14b
    player_name "О, ммм... Да, наверное, так и было."
    show player 1b
    show daisy f_sad_talk_closed
    cow "Спасибо тебе за это."
    show daisy f_shy
    show player 17
    player_name "Хех, ты не должна благодарить меня."
    show player 14b
    player_name "Я просто рад, что ты сейчас здесь."
    show player 1b
    show daisy f_shy_talk
    cow "Я тоже."
    show daisy f_normal_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "М-могу я оставить их себе, {b}Диана{/b}?"
    show daisy f_normal
    show diane f_normal_talk
    show player 13
    dia "Ты хочешь оставить цветы?"
    show diane f_normal
    show daisy f_shy_talk
    cow "Если ты не против?"
    show daisy f_shy
    show diane f_laugh
    dia "Ну конечно, все в порядке, милая!"
    show diane f_normal_talk
    dia "Давай поставим их в воду, чтобы им было что пить, хорошо?"
    show diane f_normal
    show daisy f_laugh
    cow "Да, хорошо!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Идите за мной, оба."
    hide diane with dissolve
    show player 1b
    pause
    show daisy f_shy at unflip
    show daisy at Position (xpos=300)
    with dissolve
    show player 18
    pause
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=750)
    with dissolve
    cow "Подожди меня!"
    hide daisy with dissolve
    show player 11
    pause
    show player 5
    player_name "( Ну, по крайней мере, она больше не дрожит от страха. )"
    player_name "( Это шаг в правильном направлении. )"
    $ player.go_to(L_diane_barn_interior)
    scene expression player.location.background_blur with None
    show player 1 at left
    show diane b_naked a_naked_sides f_smirk_fardown at Position (xpos=600)
    show daisy a_naked_bouquet f_shy_talk at flip
    show daisy at Position (xpos=250)
    with dissolve
    cow "Так они пьют воду?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Мммммм, они нуждаются в воде, чтобы произвести еду для себя."
    show diane f_smirk_fardown
    show daisy f_shy_talk
    cow "... Но где же рот на цветке?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Хе-хе, нет, дорогая."
    dia "Они пьют воду корнями."
    dia "Она течет прямо вверх по стеблю и в лепестки."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "Правда?!"
    show daisy f_normal
    show diane f_smirk_talk_fardown a_shirtless_vase1 with dissolve
    dia "Давай я тебе покажу."
    show diane f_smirk_fardown
    pause
    show daisy a_naked_sides
    show diane f_laugh a_shirtless_vase2
    with dissolve
    dia "Вот так, видишь?"
    show diane f_smirk_talk_fardown a_shirtless_sides
    show daisy a_naked_vase
    with dissolve
    dia "Теперь ты проверяй их в течение дня, и ты увидишь, что уровень воды падает, когда они пьют."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "Хорошо, {b}Диана{/b}."
    show daisy f_normal
    show diane f_smirk
    show player 14b
    player_name "Ты должна убедиться, что они также получают солнечный свет."
    show player 1b
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    cow "Солнечный свет?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Он прав."
    show daisy at flip
    show daisy at Position (xpos=250)
    with dissolve
    dia "Цветам тоже нужен солнечный свет, иначе они завянут и умрут."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "Хорошо."
    cow "Ты покажешь мне, как ловить солнечный свет?"
    show daisy f_normal
    show player 17
    player_name "Хаха!"
    show player 1b
    show diane f_laugh
    show daisy f_sad
    dia "Ты не должна его ловить, милая."
    show diane f_smirk_talk_fardown
    dia "Все, что тебе нужно сделать, это поместить их в место, где они могут видеть солнце в течение нескольких часов в день."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    cow "О, я могу это сделать!"
    show daisy f_shy_talk at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    cow "Спасибо, {b}[firstname]{/b}!"
    show daisy f_shy
    show diane f_smirk
    show player 14b
    player_name "Пожалуйста, ээ..."
    player_name "Как мне тебя называть?"
    show player 1b
    cow "Хмм?"
    show player 14b
    player_name "У тебя есть имя?"
    show player 1b
    show daisy f_sad_talk_closed
    cow "Умм..."
    show daisy f_shy_talk
    cow "{b}Диана{/b} зовет меня милая?"
    show daisy f_shy
    show diane f_normal_talk
    dia "Хе-хе, это скорее ласкательное слово, чем настоящее имя, дорогая."
    show diane f_normal
    show daisy f_shy_talk
    cow "О, Я эмм..."
    show daisy f_shy
    show player 10b
    player_name "Разве... Эээ, хозяин, не дал тебе имя?"
    show player 433
    show daisy f_shy_talk
    cow "Он называл меня малышкой..."
    cow "... или иногда..."
    show daisy f_sad_talk_closed
    cow "непослушная девочка."
    show daisy f_sad
    show diane f_laugh
    dia "Ну, это не годится!"
    show diane f_normal
    show player 10b
    player_name "Верно."
    show player 5b
    show daisy f_shy
    pause
    show player 14b
    player_name "Ты должна выбрать себе имя."
    show player 1b
    show daisy f_shy_talk
    cow "Я могу выбрать?"
    show daisy f_shy
    show diane f_normal_talk
    dia "Это хорошая идея, {b}[firstname]{/b}!"
    show diane f_normal
    show daisy f_shy_talk
    cow "Но, Я не знаю никаких имен..."
    show daisy f_shy
    show player 14b
    player_name "Все в порядке, мы тебе поможем!"
    show player 1b
    show daisy f_shy_talk
    cow "Хорошо."
    show daisy f_shy
    show diane f_normal_talk
    dia "Дороти!"
    show diane f_normal
    show daisy f_scared
    cow "Ммм..."
    show player 10
    player_name "Бесси?"
    show player 5
    show diane f_shamed_talk_smile
    show daisy f_shy_back
    dia "Йее, нет."
    show diane f_normal_talk
    dia "Как насчет Молли?"
    show diane f_normal
    show daisy f_shy
    cow "Ммм..."
    show player 17
    player_name "Кларабель!"
    show player 13
    show daisy f_down
    show diane f_laugh
    dia "Ха, почему ты продолжаешь говорить коровьи имена?"
    show diane f_normal
    show player 14
    player_name "Эээ, потому что она {b}девушка - корова{/b}?"
    show player 13
    show diane f_smirk_talk
    dia "Да, но она определенно больше девушка, чем корова!"
    show diane f_smirk
    show player 14
    player_name "Да ладно, я же не пытаюсь назвать ее Лютиком или как-то так..."
    show player 1b
    show daisy f_down_talk
    cow "Как это называется?"
    show daisy f_down
    show diane f_normal
    dia "Хмм?"
    show daisy f_shy_talk a_naked_flower with dissolve
    cow "Цветок, как он называется?"
    show daisy f_shy
    show diane f_smirk_talk_fardown
    dia "Этот цветок называется {b}маргаритка{/b}."
    show diane f_smirk_fardown
    show daisy f_down_talk
    cow "{b}Дейзи{/b}..."
    show daisy f_laugh
    cow "Мне нравится!"
    show daisy f_normal_talk
    cow "Могу я быть {b}Дейзи{/b}?"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Хехе, конечно милая."
    show diane f_smirk_fardown
    show player 17
    player_name "Красивое имя, и оно тебе идет!"
    show player 1b
    show daisy f_normal_talk
    cow "Идет?"
    show daisy f_normal
    show diane f_normal_talk
    dia "Я согласна."
    show diane f_smirk_fardown
    show daisy f_laugh at flip
    show daisy at Position (xpos=250)
    with dissolve
    cow "Хорошо!"
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Значит, решено."
    dia "Твое имя будет {b}Дейзи{/b}."
    show diane f_smirk_fardown
    show daisy f_laugh at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    daisy "Мое имя {b}Дейзи{/b}."
    show daisy f_normal
    show player 14b
    player_name "Приятно познакомиться, {b}Дейзи{/b}!"
    show player 1b
    show daisy f_laugh
    daisy "Хехе!"
    show daisy f_normal_talk a_naked_sides with dissolve
    daisy "Приятно познакомиться, {b}[firstname]{/b}!"
    show daisy f_normal
    show diane f_normal_talk
    dia "Мое сердце может просто растаять прямо сейчас."
    show diane f_smirk_fardown
    show daisy f_sad_talk at flip
    show daisy at Position (xpos=250)
    with dissolve
    daisy "{b}*вздох*{/b} Оно может это сделать?!"
    show daisy f_sad
    show player 17
    player_name "Пфф, хахаха!"
    show player 1b
    show diane f_smirk_talk_fardown
    dia "Хех, нет дорогая."
    show daisy f_normal
    dia "Это просто выражение такое."
    dia "Это значит, что я действительно счастлива."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "О."
    show daisy f_laugh a_naked_up with dissolve
    daisy "Тогда мое сердце тоже растает!"
    show daisy f_normal a_naked_sides with dissolve
    show player 17
    show diane f_laugh
    dia "Хахаха!"
    player_name "Хахаха!"
    show player 1b
    pause
    show diane f_smirk_talk_fardown
    dia "Хорошо, тогда..."
    show diane f_smirk_talk
    dia "{b}[firstname]{/b} и мне действительно нужно кое-что сделать до того, как закончится дневной свет."
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "О."
    show daisy f_normal
    show diane f_smirk_talk_fardown
    dia "Позаботься пока о своих цветах и дай нам знать, если тебе что-нибудь понадобится, хорошо?"
    show diane f_smirk_fardown
    show daisy f_normal_talk
    daisy "Да."
    show daisy f_normal
    show diane f_normal_talk
    dia "Хорошо, пойдем {b}[firstname]{/b}."
    hide diane with dissolve
    show player 14b
    player_name "Пока, {b}Дейзи{/b}."
    show player 1b
    show daisy f_laugh at unflip
    show daisy at Position (xpos=-200)
    with dissolve
    daisy "Пока!"
    hide player
    hide daisy
    with dissolve
    return

label barn_daisy_awakened_statue:
    scene expression player.location.background_blur with None
    $ M_diane.outfit = "shirtless"
    show diane b_naked f_shamed_talk_fardown a_shirtless_blanket at Position (xpos=600)
    show daisy b_naked_shy a_naked_shy_front f_shy_sad at flip
    show daisy at Position (xpos=200,yoffset=10)
    with dissolve
    dia "Держи, милая."
    hide diane
    hide daisy
    show daisy b_naked_blanket_cover1 a_empty f_blanket_shy_back zorder 0 at Position (yoffset=10)
    show diane f_down_front b_empty a_empty zorder 1
    with dissolve
    pause
    show daisy b_naked_blanket_cover2 f_blanket_shy_talk_back at Position (yoffset=10)
    cow "Ухх, спасибо."
    show daisy b_naked_shy a_naked_shy_blanket f_shy_sad zorder 2 at flip
    show daisy at Position (xpos=700,yoffset=10)
    show diane b_naked a_naked_sides f_shamed_talk_fardown at Position (xpos=600)
    with dissolve
    dia "Пожалуйста."
    show diane f_shamed_fardown
    show player 5 at left with dissolve
    pause
    show diane f_shamed_talk_fardown
    dia "А теперь расскажи мне, как ты оказалась в моем саду, дорогая."
    show diane f_shamed_fardown
    show player 5b
    show daisy f_shy_sad_talk at Position (yoffset=10)
    cow "Я-"
    cow "Я не уверена."
    cow "Хозяин чем-то встревожился и сказал, что мне пора спать."
    show daisy f_shy_sad at Position (yoffset=10)
    pause
    show daisy f_shy_sad_talk at Position (yoffset=10)
    cow "Я умоляла его не делать этого!"
    cow "Ненавижу, когда он заставляет меня спать."
    show daisy f_shy_sad at Position (yoffset=10)
    show diane f_shamed_talk_fardown
    dia "Я не уверена, что понимаю..."
    show diane f_shamed
    show player 10
    player_name "Он превратил ее в статую."
    show player 5b
    show daisy b_jump_scared a_empty f_empty
    cow "ИИИИИК!" with hpunch
    show diane b_empty a_empty f_thinking_back zorder 1 at Position (xpos=414)
    show daisy b_naked_cower f_cower_sad a_empty at unflip
    show daisy zorder 0 at Position (xpos=600,yoffset=26)
    with dissolve
    pause
    show diane f_shamed_talk
    dia "Что?"
    show diane f_shamed
    show player 10
    player_name "{b}Джебадия Делмонт{/b} был, предположительно, каким-то деревенским волшебником."
    player_name "Я думаю, он держал ее в секрете, превратив в статую."
    player_name "Таким образом, что никто бы ее не увидел."
    show player 5
    show diane f_smirk_talk
    dia "Деревенским волшебником?!"
    dia "Это глупо!"
    show diane f_smirk
    show player 10
    player_name "Я знаю, но-"
    show player 5
    show diane f_laugh
    dia "Хахаха, ты не можешь быть серьезным!"
    show diane f_smirk
    show player 12
    player_name "Я тоже не поверил, но..... Я имею в виду..."
    show diane f_thinking
    show player 469 with dissolve
    player_name "Как еще ты объяснишь ее?"
    show player 5b with dissolve
    show daisy f_cower_sad_talk at Position (yoffset=26)
    cow "Пожалуйста, я не хотела-!"
    show daisy b_naked_shy a_naked_shy_cover f_shy_sad at Position (yoffset=10)
    show diane b_naked a_naked_sides f_shamed_talk_fardown at flip
    show diane at Position (xpos=750)
    with dissolve
    show player 5
    dia "Ауу, милая..."
    dia "Никто тебя не обидит, ясно?"
    dia "{b}[firstname]{/b} это самый милый парень, которого ты когда-либо встречала."
    show diane f_shamed_fardown
    pause
    show diane f_shamed_talk_smile at unflip
    show diane at Position (xpos=300)
    with dissolve
    dia "Я думаю, она немного боится тебя, {b}[firstname]{/b}..."
    show diane f_shamed
    pause
    show diane f_shamed_talk_smile
    dia "Почему бы тебе не поехать домой и не дать мне немного времени, чтобы успокоить ее, хорошо?"
    show diane f_shamed
    show player 10
    player_name "Ухх, да. Хорошо."
    player_name "If you're sure you'll be alright?"
    show player 5
    show diane f_shamed_talk_smile
    dia "Со мной все будет в порядке."
    dia "Иди, {b}мы можем поговорить об этом позже{/b}, ладно?"
    show diane f_shamed
    hide player with dissolve
    return

label barn_player_completed_mysterious_statue:
    scene expression player.location.background_blur with None
    show diane b_naked a_naked_sides f_normal_talk
    show player 13 at left
    with dissolve
    dia "Привет, {b}[firstname]{/b}."
    dia "Готов приступить к работе?"
    show diane f_normal
    show player 14
    player_name "Вообще-то, я хотел тебе кое-что показать."
    show player 13
    show diane f_normal_talk
    dia "О?"
    show diane f_normal
    show player 14
    player_name "Помнишь разбитую статую, которую {b}Ричард{/b} нашел под твоим домом?"
    show player 13
    show diane f_normal_talk
    dia "Да, с этими жуткими ногами, да?"
    show diane f_normal
    show player 17
    player_name "Хех, да..."
    show player 14
    player_name "Ну, думаю, я нашел все кусочки."
    show player 13
    show diane f_normal_talk
    dia "Правда?"
    show diane f_normal
    show player 14
    player_name "Проверь."
    show player 239_240 with dissolve
    pause
    show player 717 with dissolve
    show diane f_smirk_talk_fardown
    dia "О, вау!"
    dia "Это женщина!"
    show diane f_smirk_fardown
    show player 717b
    player_name "Да, с очень странными ногами..."
    player_name "... И рогами."
    show player 717
    show diane f_smirk_talk_fardown
    dia "О, посмотри на ее милые маленькие ушки!"
    dia "Она напоминает мне тех глупых козлоногов из старых мифов!"
    dia "Знаешь, те, что с флейтами?"
    show diane f_smirk_fardown
    show player 717b
    player_name "Сатиры."
    show player 717
    show diane f_laugh
    dia "Их так называли?"
    show diane f_normal
    player_name "Ммммм."
    show diane f_normal_talk
    dia "Она классная!"
    show diane f_smirk_fardown
    pause
    show diane f_smirk_talk_fardown
    dia "Интересно, почему она держит ведро?"
    show diane f_smirk_fardown
    show player 717b
    player_name "Я думаю это {b}ведро для молока{/b}."
    show player 717
    show diane f_normal_talk
    dia "Почему ты так решил?"
    show diane f_normal
    show player 717b
    player_name "Не знаю, просто предчувствие..."
    show player 717
    show diane f_normal_talk
    dia "Значит, она как маленькая доярка?"
    show diane f_normal
    show player 717b
    player_name "Хехе, точно."
    player_name "{b}Девушка-корова{/b}, доярка."
    show player 717
    show diane f_laugh
    dia "Боже мой, как мне это нравится!"
    show diane f_normal
    show player 717b
    player_name "Хе-хе, я так и думал."
    show player 717c
    pause
    show player 717b
    player_name "Почему бы тебе не оставить ее?"
    show player 717
    show diane f_smirk_talk_fardown
    dia "Правда?"
    show diane f_smirk_fardown
    show player 717b
    player_name "Да."
    player_name "У меня дома его негде поставить."
    show player 717
    show diane f_thinking
    dia "Хмм."
    show diane f_normal_talk
    dia "В моем саду он будет смотреться великолепно, не правда ли?"
    show diane f_normal
    show player 717b
    player_name "Определенно!"
    show player 13
    show diane a_statue_full f_down_front
    with dissolve
    pause
    show diane f_reading_intrigued
    dia "Не могу поверить, что эта штука оказалась таким красивым созданием!"
    pause
    show diane f_laugh
    dia "Спасибо, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "Без проблем!"
    show player 13
    show diane f_normal_talk
    dia "Я собираюсь пойти и найти место для нее {b}в саду{/b}, прямо сейчас!"
    hide diane with dissolve
    pause
    show player 18
    player_name "( Что ж, это определенно сделало {b}Диану{/b} счастливой. )"
    show player 4 with dissolve
    player_name "( Интересно, дед Клайда сделал ее? )"
    player_name "( ... И почему? )"
    pause
    show player 34 with dissolve
    player_name "( Хм, может быть, {b}мне стоит поближе взглянуть на эту статую{/b} как-нибудь... )"
    hide player with dissolve
    return

label barn_diane_pregnancy_anouncement:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 13 at left
    show diane b_naked a_naked_sides f_laugh
    with dissolve
    dia "{b}[firstname]{/b}!!"
    show player 10
    show diane f_cheese
    player_name "Что за срочность?!"
    show player 5
    show diane f_laugh
    dia "Мы сделали это!"
    dia "Я беременна!"
    show diane f_cheese
    show player 14
    player_name "Ты беременна!"
    player_name "Ты уверенна?!"
    show player 13
    show diane f_laugh
    dia "Я уверена!"
    dia "Ты станешь папочкой!"
    show diane f_cheese
    show player 14
    player_name "Я стану-"
    show player 18
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Ты в порядке?"
    show diane f_normal
    show player 14
    player_name "Эээ?"
    player_name "Да!"
    player_name "Это хорошая новость, {b}Диана{/b}!"
    player_name "Я очень рад!"
    hide player
    show diane kiss_naked
    with dissolve
    pause
    show player 13 at left
    show diane b_naked a_naked_sides f_laugh
    with dissolve
    dia "Ммм, я тоже!"
    dia "О, это так волнующе!"
    show diane f_normal_talk
    dia "Никогда не думал, что у меня будет такая возможность!"
    show diane f_normal
    pause
    show diane f_laugh
    dia "О, спасибо {b}[firstname]{/b}!"
    dia "Спасибо, спасибо, спасибо!!!"
    hide player
    show diane kiss_naked
    with dissolve
    pause
    show player 14 at left
    show diane b_naked a_naked_sides f_cheese
    with dissolve
    player_name "Хе, пожалуйста..."
    show player 13
    show diane f_normal
    pause
    show player 14
    player_name "Так что же мне..."
    player_name "{b}*гм*{/b} Я могу что-нибудь для тебя сделать?"
    show player 13




    show diane f_normal_talk
    dia "Хмм?"
    dia "О, нет!"
    dia "Просто продолжай делать все, что ты делаешь."
    dia "Продолжай быть замечательным, {b}[firstname]{/b}!"
    show diane f_normal
    show player 14
    player_name "Это я точно могу!"
    show player 13
    show diane f_laugh
    dia "Хехе!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_return_outfit_package:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 14 at left
    show diane b_shirtless a_shirtless_sides
    with dissolve
    player_name "Привет {b}Диана{/b}, я вернулся!"
    show player 13
    show diane f_normal_talk
    dia "Вот и ты."
    dia "Я уже начала волноваться, что ты заблудился!"
    show diane f_normal
    show player 14
    player_name "Хе, да... Я бегал опять к {b}Веронике{/b} ..."
    show player 13
    show diane f_laugh
    dia "Опять?!"
    show diane f_normal_talk
    dia "Эта девушка преследует тебя или что?"
    show diane f_normal
    show player 10
    player_name "Н-Нет, я так не думаю."
    player_name "Она была в магазине {b}Pink{/b}..."
    show player 13
    show diane f_smirk_talk
    dia "О, она покупала что-то неприличное?"
    show diane f_smirk
    show player 14
    player_name "Вообще-то, она была в задней комнате."
    player_name "Сказала, что выпускает пар."
    show player 13
    show diane f_shamed_talk_smile
    dia "О, боже..."
    dia "Бедняжка, должно быть, очень переживает."
    show diane f_shamed
    show player 14
    player_name "Да, я думаю так и есть."
    player_name "Она хочет, чтобы ты ей позвонила."
    show player 13
    show diane f_normal_talk
    dia "Да, хорошо."
    show diane f_normal
    pause
    show diane f_normal_talk
    dia "Ты забрал посылку, которую я заказала?"
    show diane f_normal
    show player 17
    player_name "Да!"
    show player 239_240 with dissolve
    pause
    show player 170 with dissolve
    player_name "Что в ней?"
    show player 13
    show diane f_laugh a_shirtless_box
    with dissolve
    dia "Хе-хе, ты узнаешь..."
    show diane f_smirk_talk
    dia "Это так здорово!"
    show diane f_smirk
    show player 29 with dissolve
    player_name "Мы правда будем заниматься сексом, {b}Диана{/b}?"
    show player 3
    show diane f_smirk_talk
    dia "О, тебе лучше поверить в это!"
    dia "Мне просто нужно все подготовить."
    dia "Не могли бы ты выйти на минутку?"
    show diane f_smirk
    show player 29
    player_name "Да, конечно."
    hide player with dissolve
    scene expression "backgrounds/location_barn_garden_day_blur.jpg"
    show player 18 with dissolve
    player_name "( Я не могу поверить, что это действительно произойдет! )"
    player_name "( У меня будет секс с {b}Дианой{/b}... )"
    show player 13
    dia "Хорошо, {b}[firstname]{/b}!"
    dia "Я готова!"
    show player 14
    player_name "Вхожу!"
    show player 33
    player_name "( Фу. Ладно, {b}[firstname]{/b}! Вот оно! )"
    hide player with dissolve
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 10f with dissolve
    player_name "{b}Диана{/b}?"
    show player 13f
    $ M_diane.is_naked = 0
    $ M_diane.outfit = "cow"
    show diane f_smirk_talk b_naked a_naked_sides
    dia "Я здесь."
    show diane f_smirk
    show player 11 at left
    player_name "!!!" with hpunch
    show player 23
    player_name "..."
    show diane f_smirk_talk
    dia "Ну, как тебе?"
    show player 428
    show diane a_naked_cow_check f_smirk_down with dissolve
    pause
    show player 426
    show diane a_naked_sides with dissolve
    show player 429
    player_name "Ты выглядишь..."
    show player 29 with dissolve
    show diane f_cheese
    player_name "Вау!"
    show player 3
    show diane f_smirk_talk
    dia "Это слишком?"
    show diane f_smirk
    show player 12 with dissolve
    player_name "НЕТ!"
    show player 26
    player_name "Это очень, очень сексуально!"
    show player 426
    show diane f_smirk_talk
    dia "ТЫ так думаешь?!"
    show diane f_smirk
    show player 26
    player_name "Да!"
    show player 426
    show diane f_smirk_talk
    dia "О, хорошо!"
    dia "Я боялась, что ты сочтешь это глупостью..."
    show diane f_smirk
    show player 29 with dissolve
    player_name "Итак, как ты хочешь-"
    hide player
    show diane kiss_naked at Position (xoffset=-172)
    with dissolve
    player_name "!!!"
    pause
    show diane b_pull_mc_naked f_empty a_empty with dissolve
    dia "Ммм, Я не могу ждать ни секунды!"
    dia "Мы воспользуемся доильной станцией."
    dia "Это прекрасно!"
    pause 
    hide diane with dissolve
    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed pre_talk
    show diane_sex_breed_mc
    with dissolve
    dia "Дай мне это, жеребец!"
    dia "Я хочу, чтобы ты наполнил меня, как животное!"
    player_name "Хорошо..."
    hide diane_sex_breed_mc
    show diane_sex_breed insert_and_pullout
    with dissolve
    pause
    show diane_sex_breed creampie_pullout with dissolve
    pause 1
    show diane_sex_breed creampie
    dia "О, бог мой!" with hpunch
    return

label barn_diane_outfit_package:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 29 at left
    show diane b_shirtless a_shirtless_sides f_smirk
    with dissolve
    player_name "Привет, {b}Диана{/b}."
    show player 3
    show diane f_smirk_talk
    dia "Привет, красавчик."
    dia "Похоже, тебе не терпится начать!"
    show diane f_smirk
    show player 29
    player_name "Хе, да."
    show player 3
    show diane f_smirk_talk
    dia "Ммм, мне тоже..."
    dia "... Но есть одна последняя вещь, я хочу, чтобы ты сделал для меня."
    show diane f_smirk
    show player 14 with dissolve
    player_name "Все что угодно!"
    show player 13
    show diane f_smirk_talk
    dia "Мне нужно, чтобы ты сходил и забрал для меня специальный пакет в торговом центре."
    show diane f_smirk
    show player 14
    player_name "Я могу это сделать!"
    show player 14f with dissolve
    player_name "Я вернусь быстрее, чем ты-"
    show diane f_laugh
    show player 11 with dissolve
    dia "Подожди секунду!"
    show player 13
    show diane f_smirk_talk
    dia "Я даже не сказала тебе, в каком магазине эта посылка!"
    show diane f_smirk
    show player 14
    player_name "Прости."
    show player 13
    show diane f_laugh
    dia "Ха-ха, все в порядке."
    show diane f_smirk_talk
    dia "Тебе нужно будет поискать {b}на втором этаже{/b} магазин под названием, {b}\"Pink.\"{/b}"
    show diane f_smirk
    show player 17
    player_name "{b}\"Pink\"{/b}, ясно!"
    show player 13
    show diane f_smirk_talk
    dia "Скажи даме на стойке регистрации, что вы пришли забрать посылку на имя {b}Диана{/b}."
    show diane f_normal_talk
    dia "... И не заглядывай внутрь!"
    show diane f_normal
    show player 14
    player_name "Хорошо."
    show player 13
    show diane f_normal_talk
    dia "Очень важно, чтобы ты не заглядывал внутрь упаковки, {b}[firstname]{/b}!"
    show diane f_smirk_talk
    dia "Я не хочу портить сюрприз."
    show diane f_smirk
    show player 14
    player_name "Обещаю, я не буду смотреть"
    show player 13
    show diane f_smirk_talk
    dia "Хороший мальчик."
    hide player
    show diane kiss_shirtless
    with dissolve
    pause
    show player 13 at left
    show diane b_shirtless a_shirtless_sides f_smirk_talk
    with dissolve
    dia "Поспеши, жеребец."
    show diane f_smirk
    show player 14
    player_name "Да, мэм!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_barn_checkup:
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 14 at left
    show diane b_casual a_casual_sides
    with dissolve
    player_name "Hey, {b}Diane{/b}!"
    player_name "I'm ready to-"
    show player 11
    pause
    show player 14
    player_name "Where's your overalls?"
    show player 13
    show diane f_normal_talk
    dia "Hey, {b}[firstname]{/b}."
    dia "I was just about to walk out the door."
    show diane f_normal
    show player 10
    player_name "Oh?"
    player_name "Where are you going?"
    show player 5
    show diane f_normal_talk
    dia "I made an appointment to see a doctor this morning."
    dia "If we're gonna... You know."
    show diane f_wink
    pause
    show diane f_normal_talk
    dia "I wanna get checked out and make sure everything's in tip top shape."
    show diane f_normal
    show player 14
    player_name "Ah, I see."
    player_name "Well, can I come with you?"
    show player 13
    show diane f_normal_talk
    dia "You wanna come with me to see the doctor?"
    show diane f_normal
    show player 17
    player_name "Sure!"
    show player 13
    show diane f_normal_talk
    dia "Alright."
    dia "I would definitely appreciate the company."
    show diane f_laugh
    dia "Doctors kinda freak me out."
    show diane f_normal
    show player 14
    player_name "Hehe, really?"
    show player 13
    show diane f_normal_talk
    dia "Yeah."
    dia "All that poking and prodding, you know?"
    show diane f_normal
    show player 14
    player_name "Hah, yeah. I know what you mean."
    show player 13
    show diane f_normal_talk
    dia "Well come on then, stud."
    dia "Let's get moving!"
    show diane f_normal
    show player 14
    player_name "Y-yes, ma'am!"
    hide player
    hide diane
    with dissolve
    return

label barn_diane_return_production_book:
    scene expression player.location.background_blur
    show diane b_shirtless a_shirtless_sides f_normal_talk
    show player 13 at left
    with dissolve
    dia "Finally, you're back!"
    dia "I was starting to think you got lost or something."
    show diane f_normal
    show player 14
    player_name "Yeah, sorry."
    player_name "I stopped off at the library."
    show player 13
    show diane f_normal_talk
    dia "Oh?"
    show diane f_normal
    show player 14
    player_name "Yeah, I ran into {b}Veronica{/b} at {b}Consum-R{/b} and we started talking."
    player_name "She says hi by the way."
    show player 13
    show diane f_laugh
    dia "Oh, I love her! She's such a sweetie!"
    show diane f_normal
    show player 14
    player_name "I asked her about increasing milk production."
    show player 11
    show diane f_sad_talk
    dia "WHAT?!" with hpunch
    show diane f_scared
    pause
    show diane f_sad_talk
    dia "You didn't tell her I'm milking myself did you?!"
    show diane f_sad
    show player 10
    player_name "N-no, of course not."
    show player 5
    show diane f_lookup
    dia "Phew! I was really worried there for a sec!"
    show diane f_normal
    show player 10
    player_name "There's no need to worry."
    player_name "She was asking how the business was going and she was very pushy..."
    player_name "She wants to work for you, you know?"
    show player 5
    show diane f_normal_talk
    dia "Yeah, I know."
    show diane f_normal
    show player 10
    player_name "She seems pretty knowledgeable."
    show player 5
    show diane f_normal_talk
    dia "She is!"
    dia "Her parents owned a huge dairy farm out west and she grew up working it."
    show diane f_normal
    show player 12
    player_name "So when I said you were looking to increase milk production, she assumed I meant cows."
    show player 13
    show diane f_normal_talk
    dia "Oh, good."
    dia "I'm not ready to tell her yet."
    show diane f_normal
    show player 14
    player_name "Anyways, she sent me down a path to find this."
    show player 239_240 with dissolve
    pause
    show player 369 with dissolve
    player_name "I hope it helps..."
    show player 13
    show diane a_shirtless_book_cover f_reading_intrigued
    with dissolve
    dia "Hmm, \"Breeder's Guide?\""
    show diane f_normal
    show player 14
    player_name "Yeah, it turns out, there's a fairly easy answer to your milk production problems..."
    show player 13
    show diane a_shirtless_book f_down_front with dissolve
    pause
    show diane f_surprised_down
    dia "!!!" with hpunch
    dia "I..."
    show diane f_reading_intrigued
    dia "This is-"
    dia "I mean... I can't-"
    show diane f_laugh
    dia "Hahaha!"
    show diane f_normal_talk
    dia "Could you imagine me pregnant?"
    show diane f_normal
    show player 14
    player_name "Sure, why not?"
    show player 13
    show diane f_thinking
    dia "..."
    show diane f_laugh
    dia "Nobody would want to have a baby with me!"
    show diane f_normal
    show player 14
    player_name "I don't know about that..."
    player_name "You're beautiful, and smart, and driven, and so much fun to be around!"
    player_name "I bet, there are tons of guys out there who would be thrilled to have a baby with you, {b}Diane{/b}."
    show player 13
    show diane f_shamed_talk_smile
    dia "... Yeah, right."
    show diane f_shamed
    show player 14
    player_name "I mean, I would."
    show player 13
    show diane f_laugh
    dia "Haha, now you're just being ridiculous..."
    show diane f_shamed
    show player 12
    player_name "Hmm?"
    show player 14
    player_name "I'm serious."
    show player 13
    show diane f_shamed_talk_smile
    dia "Look, I know we have a little fun sometimes but we can't do that!"
    show diane f_shamed
    show player 10
    player_name "Why not?"
    show player 5
    show diane f_shamed_talk_smile
    dia "It isn't right!"
    show diane f_shamed_talk_smile_back
    dia "... And what would {b}[deb_name]{/b} say?!"
    dia "She'd probably never talk to me again!"
    show diane f_shamed
    show player 14
    player_name "Oh, she wouldn't do that."
    player_name "You're like, her favorite person in the entire world, {b}Diane{/b}."
    show player 13
    show diane f_shamed_talk_smile
    dia "You really think it's a good idea for you and I to have a baby?!"
    show diane f_shamed
    show player 14
    player_name "Well, I dunno... Maybe?"
    show player 13
    show diane f_shamed_talk_smile_back
    dia "Tch, I don't think you've really thought this through..."
    show diane f_shamed
    show player 12
    player_name "I just want to help you, {b}Diane{/b}!"
    show player 5
    show diane f_shamed_talk_smile
    dia "Oh, stop it!"
    show diane f_shamed
    player_name "..."
    show diane f_shamed_talk_smile
    dia "I appreciate what you're saying {b}[firstname]{/b} but it's just out of the question, alright?"
    show diane f_shamed
    show player 24
    player_name "{b}*Sigh*{/b} If you say so..."
    show diane f_shamed_talk_smile
    dia "Now, why don't you go tend to the garden while I finish up in here."
    show diane f_shamed
    show player 25
    player_name "Alright."
    hide player with dissolve
    pause
    show diane f_down_front
    pause
    dia "( Oh my... )"
    dia "( Just imagine being bred like a animal! )"
    dia "( Mmm, it's so hot! )"
    show diane f_reading_blushing
    dia "( I can't believe {b}[firstname]{/b} really wants to do that with me! )"
    show diane f_reading_lip_bite
    dia "( ... Maybe... )"
    pause
    show diane a_shirtless_book_close f_explain_close with dissolve
    dia "( No! Stop it, {b}Diane{/b}! )"
    dia "( Get those naughty thoughts out of your head right now! )"
    show diane a_shirtless_book_throw with dissolve
    dia "( Even I'm not perverted enough to do something like that! )"
    show diane a_shirtless_sides with dissolve
    pause
    show diane f_smirk_talk
    dia "Phew, I need some air..."
    hide diane with dissolve
    return


label barn_building_inform_carpenter:
    scene expression player.location.background_blur with None
    show player 13 at left
    show diane b_casual a_casual_bag f_laugh at lright
    with dissolve
    dia "{b}[firstname]{/b}, there you are!"
    show diane f_normal_talk
    dia "I was just about to head to your house."
    show diane f_normal
    show player 14
    player_name "Wow, he's already started building!"
    show player 13
    show diane f_laugh
    dia "Yup!"
    dia "Isn't it exciting!"
    show diane f_cheese
    show player 14
    player_name "Yeah, it really is."
    player_name "Did he give you a time frame for when he expects to complete it?"
    show player 13
    show diane f_normal_talk
    dia "Hmm, not exactly but he'll call when it's ready."
    hide player
    show diane b_casual_bag_hug a_empty f_laugh at Position (xoffset=-414)
    with dissolve
    dia "C'mon, roomie."
    dia "We gotta get home before {b}Debbie{/b} starts worrying."
    show player 14 at left
    show diane b_casual a_casual_bag f_normal at lright
    with dissolve
    player_name "Heh, yes ma'am."
    hide player
    hide diane
    with dissolve
    return

label barn_diane_check_barn_out:
    scene expression L_diane_barn_interior.background_blur
    show diane b_shirtless a_shirtless_sides at flip
    show diane at Position (xpos=100)
    show richard f_normal_talk
    show player 13 at left
    with dissolve
    rich "Hey, you got here quick."
    show richard f_normal
    show player 17
    player_name "Heh, I could barely keep up with her."
    show player 13
    show diane f_laugh
    dia "I'm excited!"
    show diane f_cheese
    show richard f_confused_talk
    rich "Hah, I guess you're ready for the tour then?"
    show richard f_confused
    show diane f_normal_talk
    dia "Yes, please!"
    show diane f_normal
    show richard f_normal_talk
    rich "Alright then, follow me."
    hide richard
    hide diane
    hide player
    with dissolve
    scene expression L_diane_barn.background with fade
    rich "I did everything exactly to your specifications."
    rich "All the doors are thick and sturdy with custom built locking mechanisms, so you shouldn't have to worry about anyone breaking in."
    dia "Niiice!"
    scene expression L_diane_barn_garden.background with fade
    rich "I made sure to keep the grunts out of your garden so everything there should be more or less the way you left it."
    rich "... And the hay guys had some excess they didn't use, so I told them to stack it under the awning out back."
    dia "That's perfect!"
    scene expression L_diane_barn_interior.background with fade
    player_name "Whoa!"
    dia "Hehe!"
    rich "Again, everything was done to your specifications."
    rich "You've got plenty of extra storage space on the second floor and room to expand, should you ever decide to."
    dia "It's so beautiful!"
    player_name "What are those machines for?!"
    scene expression "backgrounds/location_barn_day_blur.jpg"
    show diane b_shirtless a_shirtless_sides at flip
    show diane at Position (xpos=100)
    show richard f_confused_talk
    show player 13 at left
    with dissolve
    rich "Yeah, about those..."
    rich "A couple fellas showed up with them about three days ago, saying you ordered them."
    rich "All the paperwork checked out and they did all the installation."
    rich "I still don't have any idea what they do..."
    show richard f_confused
    show diane f_laugh
    dia "Hehe, those are, uhh... It's a secret of the trade!"
    show diane f_normal
    rich "Hmmph."
    show richard f_normal_talk
    rich "Fair enough."
    show richard f_normal
    pause
    show richard f_normal_talk
    rich "Welp, I think that about covers it."
    show richard f_normal
    show diane f_normal_talk
    dia "Thanks so much, {b}Richard{/b}."
    dia "This all looks even better than I imagined it."
    show diane f_normal
    show richard f_normal_talk
    rich "Well, I'd appreciate it if you could recommend me to anyone you know who's needing work done."
    show richard f_normal
    show diane f_normal_talk
    dia "I certainly will!"
    show diane f_normal
    show richard f_normal_talk
    rich "Alright, then I'll leave you to it."
    rich "Oh, wait!"
    rich "I nearly forgot."
    show richard f_normal
    dia "Hmm?"
    show richard f_normal_talk a_dressed_statue with dissolve
    show diane f_down_front
    show player 433
    rich "The hay delivery guys found this half buried in the corner the other day."
    show richard f_confused_talk
    rich "It's the damnedest thing..."
    show player 434
    rich "I dunno how I missed it when I was working on the foundation."
    show diane a_shirtless_statue
    show richard a_dressed_hips
    with dissolve
    rich "You know anything about it?"
    show richard f_normal
    show diane f_normal_talk
    dia "I've never seen it before..."
    dia "... Looks like some sort of statue or something."
    show diane f_normal
    show richard f_normal_talk
    rich "Yeah, that's what I was thinking."
    show richard f_normal
    show player 14
    player_name "Can I see it?"
    show diane f_down_front a_shirtless_sides at unflip
    show diane at Position (xpos=-300)
    show player 688
    with dissolve
    player_name "( Hmm, it looks like the lower half a nude woman. )"
    player_name "( What's with the tail though? )"
    show player 689
    player_name "( There's something written on the bottom of it. )"
    show expression "objects/closeup_statue_01.png"
    hide player
    hide diane
    hide richard
    with dissolve
    dia "What's that written on the bottom?"
    player_name "{b}\"Delmont.\"{/b}"
    player_name "Hmm, {b}Delmont{/b}..."
    player_name "It sounds familiar."
    hide expression "objects/closeup_statue_01.png"
    show diane b_shirtless a_shirtless_sides f_normal_talk at Position (xpos=200)
    show richard
    show player 689 at left
    with dissolve
    dia "Maybe it's a name?"
    show diane f_normal
    show richard f_confused_talk
    rich "... Or a surname?"
    show richard f_normal
    show player 12 with dissolve
    player_name "You mind if I hang on to it?"
    show player 5
    show diane f_normal_talk
    dia "Knock yourself out."
    show diane f_normal
    show player 13
    show richard f_normal_talk
    rich "Well..."
    show diane at flip
    show diane at Position (xpos=600)
    rich "Give me a call if you need anything else."
    show richard f_normal
    show diane f_normal_talk
    dia "Thanks again, {b}Richard{/b}."
    show diane f_normal
    hide richard with dissolve
    pause
    show diane f_normal_talk
    dia "Say hi to {b}Lucy{/b} for me!"
    show diane f_normal
    pause
    show diane f_laugh at unflip, lright with dissolve
    dia "Oh, this is wonderful!"
    show diane f_normal_talk
    dia "Isn't it wonderful, {b}[firstname]{/b}?!"
    show diane f_normal
    show player 14
    player_name "Heh, it does look really nice."
    player_name "So what are those machines for?!"
    show player 13
    show diane f_normal_talk
    dia "Oh, right."
    dia "Those are milking machines."
    show diane f_normal
    show player 10
    player_name "They are?"
    show player 13
    show diane f_normal_talk
    dia "You lay in them and attach the milkers to your breasts."
    dia "I had them custom built for comfort, since I have to spend so many hours milking."
    show diane f_normal
    show player 14
    player_name "I see."
    show player 13
    show diane f_smirk_talk
    dia "Gravity should make your job a lot easier with me in that position..."
    show diane f_smirk
    show player 11
    player_name "!!!" with hpunch
    show player 10
    player_name "My job?!"
    show player 11
    show diane f_laugh
    dia "Of course!"
    show diane f_smirk_talk
    dia "You're the one who keeps asking if you can help..."
    dia "... And with those magic hands of yours, I figured, who better?"
    show diane f_smirk
    show player 10
    player_name "So I'm going to be milking you?"
    show player 11
    show diane f_smirk_talk
    dia "Is that a problem?"
    show diane f_smirk
    show player 29 with dissolve
    player_name "N-no!"
    show player 3
    pause
    show player 10 with dissolve
    player_name "How come there are three of them though?"
    show player 5
    show diane f_laugh
    dia "Heh, well I'll have to expand and bring more ladies in eventually, right?"
    show diane f_normal
    show player 10
    player_name "M-more, ladies?"
    player_name "You mean, I'm gonna be milking more ladies?"
    show player 11
    show diane f_normal_talk
    dia "Maybe."
    show diane f_smirk_talk
    dia "That's between you and them."
    show diane f_smirk
    show player 29 with dissolve
    player_name "I uhh... Wha-"
    player_name "{b}*Ahem*{/b} W-who do you have in mind?"
    show player 3
    show diane f_laugh
    dia "Hahaha, calm down handsome."
    show diane f_normal_talk
    dia "I don't have anyone in mind right now..."
    dia "It could be a long while before I find the right fit for a job like that."
    show diane f_normal
    show player 14 with dissolve
    player_name "Heh, right. That makes sense."
    show player 13
    show diane f_normal_talk
    dia "In the meantime, I'll have to see about {b}finding a way to increase my production{/b}..."
    show diane f_normal
    show player 10
    player_name "What do you mean?"
    show player 5
    show diane f_normal_talk
    dia "Well, I'm nearing my limit on how much breast milk I can produce in a day."
    dia "There's gotta be something I can do to increase the flow..."
    show diane f_normal
    show player 10
    player_name "Increase the flow?"
    player_name "... Maybe you should speak with a doctor?"
    show player 5
    show diane f_normal_talk
    dia "Yeah, that might be a good idea."
    dia "Don't worry, {b}[firstname]{/b}, I'll figure something out."
    show diane f_normal
    show player 14
    player_name "N-no, I'll help too!"
    show player 13
    show diane f_laugh
    dia "Haha, there's something else I need you to do."
    show diane f_normal
    show player 14
    player_name "Anything!"
    show player 13
    show diane f_normal_talk
    dia "I don't think I ordered enough {b}storage containers for the milk{/b}."
    dia "Would you run over to {b}Consum-R{/b} and {b}buy me one more?{/b}"
    show diane f_normal
    show player 14
    player_name "Sure thing."
    show player 13
    show diane f_normal_talk
    dia "Thanks, {b}[firstname]{/b}."
    hide player
    hide diane
    with dissolve

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
