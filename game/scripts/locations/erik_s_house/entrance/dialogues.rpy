label erikentrance_erik_gf_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14 at left
    show june 2 at Position (xpos=700)
    show erik 1 at right
    with dissolve
    player_name "Ох,привет ребята!"
    show player 1
    show erik 4
    eri "Хэй, {b}[firstname]{/b}!"
    show june 3
    show erik 1
    june "привет!"
    show player 14
    show june 2
    player_name "Я не знал что вы оба уже общаетесь!"
    show player 1
    show erik 4
    eri "Да, мы играли в Ork Bork много..."
    show erik 1
    show june 6
    june "Ха ха. Да, мы совсем пристрастились!"
    show june 2
    show player 14
    player_name "Итак, вы двое хорошо ладите друг с другом, хм?"
    show player 1
    show erik 4
    eri "Да, вообще-то мы должны что то сделать... в моей эээ... комнате."
    show erik 1
    show player 11
    show june 3
    june "Да нам нужно, мммм... посмотреть кое-что?"
    show player 14
    show june 2
    player_name "Ох... Я вижу!"
    show player 17
    player_name "Все в порядке, я тогда зайду в другой раз."
    show player 14
    player_name "увидимся позже ребята!"
    show player 1
    show erik 4
    eri "Позже, приятель."
    hide player
    hide june
    hide erik
    with dissolve
    return

label erikentrance_erik_sex_ed_block:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14
    with dissolve
    player_name "Я должен посмотреть если {b}Эрик{/b} в своей комнате..."
    hide player with dissolve
    return

label erikentrance_mrsj_poker_night_over:
    scene expression game.timer.image("erik_inside{}_b")
    show mrsj 17 at right
    show player 1 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!"
    show player 11
    mrsjo "Можно тебя на пару слов перед тем как вы уйдете с {b}Эриком{/b}?"
    show mrsj 14
    show player 14
    player_name "Конечно, {b}Миссис Джонсон{/b}."
    show mrsj 20
    show player 11
    mrsjo "Я... Я почти ничего не помню с прошлой ночи."
    show mrsj 19
    mrsjo "Что бы не произошло, я хочу извиниться."
    show player 13
    mrsjo "Я слишком много выпила, и я не должна была заниматься этими вещами с вами мальчики."
    show mrsj 19c
    show player 10
    player_name "Ох, все в порядке, {b}Миссис Джонсон{/b}..."
    show mrsj 19
    show player 13
    mrsjo "Ты не обижаешься на меня, верно?"
    show mrsj 19c
    show player 14
    player_name "Конечно нет."
    player_name "Я думаю это было весело!"
    show mrsj 19
    show player 1
    mrsjo "Что насчет {b}Эрика{/b}?"
    mrsjo "Ему тоже было весело?"
    show player 14
    show mrsj 14
    player_name "Я.. я думаю да?"
    show mrsj 17
    show player 1
    mrsjo "Что ж... если вы только мальчики не нашли это слишком странным..."
    show mrsj 19c
    show player 14
    player_name "Ты говорил с ним об этом?"
    show mrsj 19
    show player 11
    mrsjo "Нет! Боже нет."
    show mrsj 20
    mrsjo "Я не хочу что бы было еще более неловко чем сейчас."
    show mrsj 19
    mrsjo "Но... Не можешь  мне сделать одолжение и поговорить с ним об этом?"
    mrsjo "Я просто хочу убедиться что он не злиться на меня из-за этого."
    show mrsj 14
    show player 14
    player_name "Конечно, {b}Миссис Джонсон{/b}. Я поговорю с ним."
    show mrsj 18
    show player 1
    mrsjo "Спасибо, ты такой милый."
    hide player
    hide mrsj
    with dissolve
    return

label mrsj_sex_ed:
    scene erik_house_upstairs_night_c01
    show erik 5f at Position (xpos=300)
    show player 13 at left
    show mrsj 14 at right
    with dissolve
    eri "Привет, {b}Миссис Джонсон{/b}!"
    eri "Тебе... нужно что-то от нас?"
    show erik 1f
    show mrsj 19
    mrsjo "Слушайте, мальчики."
    mrsjo "Я знаю что вы двое говорили об этом уже, так что..."
    mrsjo "Я много думала об этом, и так как вы двое отночитесь к этому..."
    show mrsj 49
    mrsjo "Я согласна дать вам два частных... урока по сексуальному обучению."
    show mrsj 50
    show player 23
    player_name "!!!"
    show erik 5f
    eri "М...{b}Миссис Джонсон{/b}, ты уверена?"
    show erik 1f
    show mrsj 49
    show player 18
    mrsjo "Конечно, тыковка!"
    mrsjo "У меня с этим нет проблем, до тех пор пока это останется между нами!!"
    show mrsj 50
    show player 14
    player_name "У... у меня нет проблем с этим, {b}Миссис Джонсон{/b}..."
    show player 11
    show mrsj 52
    mrsjo "Но!!" with hpunch
    mrsjo "Прежде чем мы начнем эти уроки... Мне от вас кое-что нужно."
    show player 5
    show mrsj 14
    show erik 4f
    eri "Что тебе нужно {b}Миссис Джонсон{/b}?"
    show erik 1f
    show mrsj 19
    show player 13
    mrsjo "...Вообще то у меня никогда небыло раньше секса с двумя парнями."
    show mrsj 49
    mrsjo "Мне нужна книга где показывают сексульные позиции более чем с двумя партнерами."
    mrsjo "Я слышала она называется {b}Камасутра{/b} описывает древне-восточние позиции."
    mrsjo "Посмотрите сможете ли вы достать мне эту книгу."
    show mrsj 52
    mrsjo "И еще кое-что..."
    show mrsj 14
    show erik 5f
    eri "Ох, да?"
    show erik 1f
    show mrsj 49
    mrsjo "Чтож, если мы хотим заниматься сексом, я должна быть уверена что я не за беременею!"
    show mrsj 50
    player_name "..."
    show mrsj 49
    mrsjo "Я буду принимать {b}противозачаточные таблетки{/b}..."
    show mrsj 50
    show erik 5f
    eri "Мы не можем использовать презирвативы?"
    show erik 1f
    show mrsj 52
    mrsjo "Даже с презирвативами, всегда есть риск!!"
    show mrsj 49
    mrsjo "И если я использую таблетки, мы можем делать это неопасным..."
    show mrsj 50
    show player 83
    show erik 58f
    player_name "!!!"
    show player 82
    show mrsj 20
    pause
    mrsjo "..."
    show mrsj 18
    mrsjo "Ха ха!"
    show player 81
    player_name "!!!" with hpunch
    show player 78
    show mrsj 49
    mrsjo "Я вижу что вы оба очень взволнованы от идеи начать секс уроки со мной..."
    show mrsj 50
    show erik 56f
    eri "Извини, {b}Миссис Джонсон{/b}."
    show erik 57f
    show mrsj 49
    mrsjo "Все хорошо, тыковка."
    show player 80
    mrsjo "Чем раньше вы можете мне получить то что мне нужно, тем скорее мы сможем начать!"
    show mrsj 50
    show erik 58f
    eri "Хорошо, {b}Миссис Джонсон{/b}!"
    show erik 57f
    show player 83
    player_name "Мы найдем все что тебе нужно, {b}Миссис Джонсон{/b}!"
    hide player
    hide mrsj
    hide erik
    with dissolve
    scene black with fade
    pause
    scene expression game.timer.image("erik_entrance{}_c")
    show erik 4 at right
    show player 13 at left
    with dissolve
    eri "Я не могу поверить {b}Миссис Джонсон{/b} согласна заниматься сексом с нами..."
    show erik 1
    show player 17
    player_name "Я думаю что мы счастливчики..."
    show player 13
    show erik 3
    eri "Я никогда не занимался сексом раньше.."
    show erik 3c
    show player 14
    player_name "Что ж, {b}Миссис Джонсон{/b} планирует научить нас как. И это будет офигенно!"
    show player 13
    show erik 5
    eri "Но где мы достанем эту вещь которую она попрасила?"
    show erik 1
    show player 34
    player_name "Хммм..."
    show player 35
    player_name "Я думаю у меня есть идея."
    show player 13
    show erik 5
    eri "Ох да?"
    show erik 1
    show player 14
    player_name "Я уверен что в {b} больнице есть таблетки про которые Миссис Джонсон{/b} говорила..."
    show player 33
    player_name "И мы всегда можем найти {b}Книгу Камасутры в библиотеке{/b}!"
    show player 13
    show erik 5
    eri "Надеюсь ты прав."
    show erik 1
    show player 14
    player_name "Я вернусь когда я найду что-то..."
    hide player
    hide erik
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ erik.complete_events(erik_sex_ed)
    $ mrsj.add_event(mrsj_sex_ed)
    $ M_erik.place(place = L_erikhouse_erikroom)

    $ game.main()

label mrsj_sex_ed_2:
    scene erik_house_upstairs_night_c01
    show erik 4f at Position (xpos=300)
    show player 13 at left
    show mrsj 14 at right
    with dissolve
    eri "Привет, {b}Миссис Джонсон{/b}."
    show erik 1f
    show mrsj 17
    mrsjo "Привет, мальчики!"
    mrsjo "Как там у вас дела?"
    show mrsj 14
    show erik 4f
    eri "Мы нашли несколько вещей которые помогут тебе...с нашими уроками."
    show erik 1f
    show player 239_240 with dissolve
    pause
    show player 425 with dissolve
    player_name "Вот что я нашел, {b}Миссис Джонсон{/b}!"
    show player 13
    show mrsj 63
    with dissolve
    mrsjo "Ох, великолепно!"
    mrsjo "Нужно подготовиться для наши маленьких уроков вместе..."
    mrsjo "Может быть вы двое навестите меня ночью в моей комнате...или, мне лучше называть её, нашей классной комнатой!"
    mrsjo "Ha ha."
    hide player
    hide mrsj
    hide erik
    with dissolve
    scene black with fade
    pause
    scene expression game.timer.image("erik_entrance{}_c")
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Когда мы должны навестить {b}Миссис Джонсон{/b}?"
    show erik 1
    show player 14
    player_name "Я попробую придти так скоро как я смогу..."
    player_name "Но ты можешь делать это с ней каждый раз когда ты захочешь!"
    show player 13
    show erik 4
    eri "Я думаю ты прав..."
    eri "Срасибо что помог мне с этим, {b}[firstname]{/b}."
    hide player
    hide erik
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ player.remove_item("kamasutra")
    $ player.remove_item("birth_control_pills")
    $ mrsj_sex_ed.finish()
    $ M_mrsj.unforce()
    $ M_erik.unforce()
    $ M_erik.set_default_locations([[L_school_scienceclassroom, L_school_cafeteria, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom],
                                    [L_erikhouse_erikroom, L_erikhouse_erikroom, L_erikhouse_mrsjroom, L_erikhouse_mrsjroom]])
    $ game.main()

label erik_breastfeeding:
    scene erik_house_cs01_01b with fade
    show text "Это был первы раз когда я зашел в комнату {b}Миссис Джонсон{/b}.\nЯ знал её и {b}Эрика{/b} с необычными отношениями...\nЯ не ожидал увидить его... кормление грудью..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text
    scene erik_house_cs02 with fade
    show text "Выражение их лиц сказали все...\n...Я не должен был там быть. Все было бы хорошо...\n...Если бы я постучал сперва.\nИнстинктивно, Я закрыл дверь и решил что мне лучше уйти." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene expression game.timer.image("erik_entrance{}_c")
    show player 22 at left with dissolve
    show erik 2 at Position (xpos=750)
    show mrsj 52 at right
    with dissolve
    mrsjo "{b}[firstname]{/b}?!"
    mrsjo "Я... Что ты здесь делаешь?"
    show mrsj 38
    show player 37 with dissolve
    player_name "{b}Эрик{/b}?!"
    show erik 3b with dissolve
    player_name "Я... эм... просто пытался найти тебя."
    show player 24 with dissolve
    show erik 3
    eri "{b}[firstname]{/b}..."
    show erik 2 with dissolve
    show player 25
    player_name "Я услышал голоса и я подумал..."
    show player 11
    show erik 3b
    eri "Я... Я просто хочу пойти в свою комнату прямо сейчас."
    show erik 2
    show mrsj 19b
    mrsjo "Все хорошо Я-"
    hide erik with dissolve
    show mrsj 19c
    show player 22
    mrsjo "..."
    show mrsj 20
    mrsjo "Слушай, что ты сейчас видел кое-что... нормальное!"
    show player 5
    show mrsj 19
    mrsjo "Я просто пыталась вытащить его из своей раковины, {b}[firstname]{/b}."
    show mrsj 19c
    show player 10
    player_name "Все нормально, {b}Миссис Джонсон{/b}."
    player_name "Я не хотел вламываться к вам вот так..."
    show player 5
    pause
    show player 10
    player_name "Можешь просто сказать {b}Эрику{/b} что я извиняюсь?"
    show player 5
    show mrsj 19
    mrsjo "Не волнуйся о нем. Он будет в порядке..."
    mrsjo "Дело в том что... {b}Эрик{/b} похоже не видит или не может говорить со многими девченками, так что я попыталась и..."
    show player 11
    mrsjo "...Я дала ему немного женсокой заботы!"
    mrsjo "Я думала я смогу вытащить его с его компьютера если бы он мог просто... попробовать немного на вкус!"
    show mrsj 19c
    show player 5
    player_name "..."
    show mrsj 19
    mrsjo "Ты можешь просто... ты знаешь. Оставить это между нами?"
    mrsjo "Я не думаю что он бы хотел чтобы другие ребят в школе узнали про это."
    show mrsj 19c
    show player 10
    player_name "Все хорошо, {b}Миссис Джонсон{/b}. Я никому не скажу."
    hide player
    hide mrsj
    with dissolve
    $ player.go_to(L_erikhouse_entrance)
    $ erik.complete_events(erik_breastfeeding)
    $ erik.add_event(erik_breastfeeding_2)
    $ erik_breastfeeding_2.finish()
    $ M_erik.unforce()

    $ game.main()

label mrsj_room_locked_dialogue:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Ууупс! {b}Миссис Джонсон{/b} должна держать дверь закрытой..."
    hide player with dissolve
    $ game.main()

label mrsj_filled_block:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10
    with dissolve
    player_name "Я должен дать {b}Миссис Джонсон{/b} отдохнуть."
    player_name "Кроме того, я не думаю что я смогу справиться с этими двумя уроками за один день..."
    hide player with dissolve
    $ game.main()

label eriks_house_intro:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 1 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Привет, {b}[firstname]{/b}!"
    show mrsj 14
    show player 36 with dissolve
    player_name "Привет, {b}Миссис Джонсон{/b}."
    show player 13 with dissolve
    show mrsj 17
    mrsjo "Много времени прошло с твоего прошлого визита к нам!"
    show mrsj 14
    show player 10
    player_name "Да, Я был немного занят в последнее время."
    player_name "Догонять в школе и копить деньги за оплату обучения."
    show player 13
    show mrsj 17
    mrsjo "Хорошо это слышать от молодого человека, вроде тебя, ведешь себя так ответсвенно."
    show mrsj 49
    mrsjo "Не забудь оставить что не будь и для себя чтобы цеплять девченок, милый."
    show mrsj 50
    show player 21
    player_name "Да, хорошо..."
    show player 13
    pause
    show mrsj 17
    mrsjo "Что ж, рада снова тебя видеть!"
    show mrsj 18
    mrsjo "Ты наверно здесь чтобы увидеть {b}Эрика{/b}, а не маленькую старуху как я."
    show mrsj 17
    mrsjo "Тут довольно тихо в округе..."
    show mrsj 14
    show player 10
    player_name "Что вы имеете в виду?"
    show player 5
    show mrsj 19
    mrsjo "Ну, у {b}Эрика{/b} немного поситителей и ты кажется его единственный друг."
    show mrsj 17
    show player 13
    mrsjo "Я хочу чтобы ты знал что тебе всегда рады в этом доме. Днем или ночью."
    show mrsj 49
    mrsjo "Ты и {b}Эрик{/b} хорошие детки."
    show mrsj 50
    show player 2
    player_name "Спасибо, {b}Миссис Джонсон{/b}."
    show player 13
    pause
    show player 12
    player_name "Где {b}Эрик{/b} в любом случае?"
    show player 5
    show mrsj 17
    mrsjo "Я думаю я видела его недавно. Он что то делал редкое с внешним видом своей комнаты!"
    mrsjo "Сейчас он в подвале."
    return

label erikentrance_erik_thief_2_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 14 at left
    show erik 1 zorder 1 at right
    with dissolve
    player_name "Хэй, {b}Эрик{/b}."
    show erik 4
    show player 1
    eri "Хэй, ты кого нибудь нашел?"
    show erik 1
    show player 10
    player_name "Не очень много, все либо очень заняты или не хотят приходить."
    show erik 5
    show player 11
    eri "Даже {b}Мия{/b}?"
    show erik 1
    show player 10
    player_name "Я думаю она занята своей домашкой."
    show erik 3
    show player 5
    eri "Авв чувак, кто еще будет играть с нами в карты?"
    show player 1
    show erik 1b at Position(xpos=870)
    show mrsj 17b zorder 2 at right
    with dissolve
    mrsjo "Что случилось, тыковка?"
    show erik 4b
    show mrsj 14b
    eri "Ох, ничего, {b}Миссис Джонсон{/b}."
    show erik 1b
    show mrsj 18
    mrsjo "Ох, Да ладно! Я слышала что вы ребята говорили об приглошении друзей."
    show erik 5b
    show mrsj 14b
    eri "Что ж, мы никого не можем найти что бы поиграть в покер с нами."
    show erik 1b
    show mrsj 17
    mrsjo "Оох, это звучит грустно!"
    show erik 5b
    show mrsj 14b
    eri "Было бы более весело если бы у нас были другие игроки..."
    show erik 1b
    show player 11
    show mrsj 17
    mrsjo "Что насчет меня?"
    show player 13
    show mrsj 18
    mrsjo "Я бы хотела сыграть..."
    show player 1
    show erik 4b
    show mrsj 14b
    eri "Серьезно?"
    show erik 1b
    show mrsj 17
    mrsjo "Да! Это не справедливо, что пара хороших ребят как вы не могу найти кого то чтобы поиграть..."
    mrsjo "Знаешь что, если вам понадобиться другой игрок, дай мне знать, Я всегда готова для хорошей игры в покера ночью!"
    show erik 1
    show player 14
    show mrsj 14
    player_name "Это звучит круто!"
    show player 17
    player_name "Спасибо, {b}Миссис Джонсон{/b}."
    show player 1
    show erik 1 at right
    hide mrsj
    with dissolve
    pause
    show player 14
    player_name "Чувак!! Я не могу поверить {b}Миссис Джонсон{/b} будет играть с нами."
    show erik 4
    show player 1
    eri "Чтож, Я думаю мы кого то нашли..."
    hide player
    hide erik
    with dissolve
    return

label erikentrance_erik_thief_over:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 19 at right
    show player 13 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!"
    mrsjo "Я просто хотела сказать большое спасибо за, ты знаешь, что защитил нас."
    show mrsj 20
    mrsjo "Это довольно стыдно что ты увидел моего бывшего мужа вот так..."
    show mrsj 19c
    show player 33
    player_name "Я просто хотел убедиться что он не ворвется в твой дом."
    show player 13
    show mrsj 17
    mrsjo "Я счастлива иметь такого прекрасного соседа..."
    show mrsj 14
    show player 17
    player_name "Ох, спасибо!"
    show player 13
    show mrsj 49
    mrsjo "Я должна... вознаградить тебя чем то особенным, за то что ты сделал для нас..."
    show mrsj 50
    show player 4 with dissolve
    player_name "..."
    show player 29 with dissolve
    player_name "Эмм, Вам не нужно, {b}Миссис Джонсон{/b}!"
    show player 13 with dissolve
    show mrsj 49
    mrsjo "Ох, нет. Я настаиваю!"
    mrsjo "Я что не будь придумаю и я уверена что тебе это понравится..."
    show mrsj 50
    show player 17
    player_name "Ха ха, хорошо."
    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_mrsj_yoga_2_over:
    scene expression game.timer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "( Здесь тихо, кто не будь есть дома? )"
    player_name "( Может быть {b}Эрик{/b} в своей комнате. )"
    show player 17
    player_name "( Я надеюсь он не спит... или занят чем то другим. )"
    hide player with dissolve
    return

label erikentrance_mrsj_yoga_2_started:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 17 at left
    with dissolve
    mrsjo "{b}[firstname]{/b}!!"
    mrsjo "Как прошел твой первый раз интруктируя класс йоги?"
    show mrsj 14
    show player 14
    player_name "Я думаю все прошло хорошо?"
    show player 13
    show mrsj 17
    mrsjo "{b}Анна{/b} была там что бы помочь тебе?"
    show mrsj 14
    show player 14
    player_name "Да, она была."
    player_name "Она очень хороша в йоге..."
    show player 17
    player_name "...и гибкая!"
    show player 13
    show mrsj 18
    mrsjo "Ха ха ха!"
    show mrsj 49
    mrsjo "{b}Анна{/b} может встать в любую позицию в которую я ей посажу."
    mrsjo "Когда то она у меня была искривленая как крендель с солью."
    show mrsj 50
    show player 12
    player_name "Серьезно?"
    show player 11
    show mrsj 49
    mrsjo "Ох да. Она очень хороша в тесных... условиях."
    mrsjo "И немного детского масла не причинит также боли..."
    show mrsj 50
    show player 13
    player_name "..."
    show mrsj 19
    mrsjo "Эммм... В любом случае, как ты думаешь ты бы сделал это снова?"
    show mrsj 14
    show player 14
    player_name "Что ж, она пригласила меня поззаниматься больше йогой с ней в спортзале ночью."
    show player 13
    show mrsj 18
    mrsjo "Ты должен пойти!"
    show mrsj 49
    mrsjo "{b}Анна{/b} может научить тебя многим вещам..."
    show mrsj 50
    show player 17
    player_name "Я уверен, ха ха."
    show player 13
    show mrsj 19
    mrsjo "Спасибо что помог мне. Ещё раз."
    show mrsj 17
    mrsjo "И не думай что я забыла как много ты сделал для {b}Эрика{/b} и меня."
    show mrsj 49
    mrsjo "Я должна тебе... много."
    show mrsj 50
    show player 33
    player_name "Не волнуйтесь об этом. Это не трудно."
    hide player
    hide mrsj
    with dissolve
    return

label erikentrance_erik_vr_over:
    scene expression game.timer.image("erik_entrance{}_c")
    show mrsj 17 at right
    show player 13 at left
    with dissolve
    mrsjo "Ох, хорошо!"
    show mrsj 19
    mrsjo "{b}[firstname]{/b}, Я не хочу тебя беспокоить, но ты свободен сегодня ночью?"
    show mrsj 19c
    show player 10
    player_name "Хм?"
    show player 11
    show mrsj 19
    mrsjo "Мне нужно что бы кто-то пошел и преподал моей группе по йоге сегодня ньчью. У меня другая встреча мне нужно там присутствовать."
    show mrsj 14
    show player 12
    player_name "Я?!"
    show player 5
    show mrsj 49
    mrsjo "Ты не мог бы помочь вашей... любимой соседке??"
    show mrsj 50
    show player 38 with dissolve
    player_name "Эммм... Я... думаю я могу попробовать?"
    show player 29 with dissolve
    player_name "Но я мало что знаю о йоге..."
    show player 11 at left with dissolve
    show mrsj 17
    mrsjo "Это класс для начинающих!"
    mrsjo "Ты отлично справишся!"
    show mrsj 57 with dissolve
    mrsjo "Вот список движений йоги чтобы сделать это перед классом."
    show mrsj 58
    pause
    show mrsj 14
    show player 386
    with dissolve
    player_name "Спасибо."
    show player 380
    pause
    show player 384
    player_name "Эмм... Эти движения выглядят довольно сложно..."
    show player 385
    show mrsj 17
    mrsjo "Моя подруга {b}Анна{/b} будет там чтобы тебе помочб во время урока."
    show mrsj 18
    mrsjo "Она моя маленькая нетерпеливая бобриха. Всегда готова помочь и порадовать."
    show mrsj 14
    show player 386
    player_name "Ох. хорошо... Я постараюсь из-за всех сил."
    show player 385
    show mrsj 49
    mrsjo "Ты такой милаха. Я постараюсь однажды тебе отплатить!"
    show mrsj 17
    mrsjo "Мне пора идти, так что изучи эти движения!"
    mrsjo "Пока!"
    show mrsj 14
    show player 386
    player_name "Пока, {b}Миссис Джонсон{/b}."
    show player 385
    hide mrsj with dissolve
    return

label erikentrance_erik_orcette_completed:
    scene expression game.timer.image("erik_entrance{}_c")
    show player 375 at left
    show mrsj 17 at right
    with dissolve
    mrsjo "Привет, {b}[firstname]{/b}!"
    mrsjo "Ты ищешь {b}Эрика{/b}?"
    show mrsj 14
    show player 377
    player_name "!!!"
    show player 376
    player_name "П... привет, {b}Миссис Джонсон{/b}."
    show player 378
    mrsjo "..."
    show mrsj 17
    mrsjo "Итак, чем вы двое планируете заниматься..."
    show mrsj 14
    show player 376
    player_name "Ох, ничем!"
    show player 377
    show mrsj 49
    mrsjo "Вообщем что у тебя там в руках?"
    mrsjo "Что то новенькое для тебя и {b}Эрика{/b} Вы будете играть, мм?"
    show mrsj 50
    player_name "!!!"
    show player 379
    player_name "эм.... Да что то в этом роде."
    show player 377
    show mrsj 17
    mrsjo "Я просто люблю сюрпризы! Что это? Это должно быть какая то новенькая игра."
    mrsjo "Это все чем {b}Эрик{/b} занимается в последнее время..."
    show mrsj 14
    show player 379
    player_name "Да... эм... Это не.. Ну..."
    show player 377
    show mrsj 17
    mrsjo "Дай мне посмотреть!"
    show player 23 with dissolve
    show mrsj 43 with dissolve
    player_name "Подожди!"
    show player 22
    mrsjo "!!!"
    show mrsj 44
    mrsjo "Что... это?"
    show mrsj 46
    show player 10
    player_name "Это..."
    show player 11
    show mrsj 43
    mrsjo "Эта одна из этих фальшивых секс вещей которые рекламируют онлайн?"
    show mrsj 46
    show player 10
    player_name "Ох..."
    show player 24
    show mrsj 44
    mrsjo "Это {b}Эрик{/b} тебя надоумил?"
    mrsjo "Я видела эту молнию на экране его компьютера когда я вошла в его комнату один раз."
    show mrsj 46
    show player 25
    player_name "Нет. нет. Это... эм... Мое."
    show player 24
    player_name "Я... эм... собирался... только показать ему?"
    show mrsj 45
    mrsjo "Ха ха."
    mrsjo "мальчики и их игрушки!"
    show mrsj 46
    player_name "..."
    show player 25
    show mrsj 44
    mrsjo "Ох дорогой... Все в порядке!"
    mrsjo "Молодой мужчина проявляет интерес к интимной стороне жизни в этом нет ничего плохого!"
    mrsjo "Может быть увидев твою новую игрушку мотивирует его чтобы... выбратся из его комнаты?"
    mrsjo "В реальной жизни...еще лучше, молодой мужчина."
    show mrsj 46
    show player 22
    player_name "{b}*Глоток*{/b}"
    show mrsj 44
    mrsjo "{b}Эрик{/b} наверху, сладкий."
    mrsjo "Ох, и проследи что бы использовал смазку с этой штукой."
    mrsjo "Ты же не хочешь получить ожоги от трения на твоих...частях."
    hide mrsj with dissolve
    show player 377 with dissolve
    pause
    show player 376
    player_name "( Вау.. Я думал что она будет чувствовать отвращение во мне из-за этого... )"
    player_name "( Но она отнеслась довольно спокойно к этому? )"
    player_name "( {b}Эрику{/b} очень повезло что он оказался здесь... )"
    return

label erikentrance_mrsj_intro_started_day:
    mrsjo "В любом случае, Мне наверное пора идти."
    show player 13
    mrsjo "Я должна провести уроки йоги во второй половине дня в спортзале."
    mrsjo "У меня будут несколько новых учеников и мне лучше поспешить чтобы я не опоздала!"
    show mrsj 14
    show player 14
    player_name "Хорошо, повеселись!"
    show player 13
    show mrsj 17
    mrsjo "Ты тоже! Скажи {b}Эрику{/b}, что я вернусь к ужину и что бы он не ел слишко много сладостей."
    show mrsj 49
    mrsjo "Я хочу чтобы он был хорошим и жаждуещим меня сегодня вечером!"
    return

label erikentrance_mrsj_intro_started_night:
    show mrsj 18
    mrsjo "Что ж, становится немного поздно для меня."
    show mrsj 17
    show player 13
    mrsjo "Я пошла спать, ток что развлекайтесь. Но запомните не делйте слишком громко если будете играть в компьютерные игры."
    show mrsj 14
    show player 14
    player_name "Сделаем. Доброй ночи {b}Миссис Джонсон{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
