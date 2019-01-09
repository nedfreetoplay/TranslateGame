label art_classroom_ross_start:
    scene location_school_art_closeup
    show player 2f at right
    show ross 1 at left
    player_name "Привет, {b}Мисс Росс{/b}."
    show player 1f
    show ross 2
    ross "Ну привет, {b}[firstname]{/b}!"
    show ross 25 with dissolve
    ross "Я слышала о смерти твоего отца..."
    ross "Бедняжка, я молюсь за тебя."
    show ross 24
    show player 2f
    player_name "Ух, спасибо!"
    show player 1f
    show ross 25
    ross "О, это не проблема, сладкий."
    ross "Дай мне знать, если я могу что-то для тебя сделать."
    show player 2f
    show ross 24
    player_name "Ну, вообще-то, вы можете кое-что сделать."
    player_name "Мне нужен способ {b}повысить свою художественную оценку{/b}."
    show player 1f
    show ross 25
    ross "О да, она немного упала во время твоего отсутствия."
    ross "Это действительно очень плохо. Ты был лучшим в классе перед уходом..."
    show player 10f
    show ross 24
    player_name "Разве?!"
    show player 11f
    show ross 11
    ross "Ой, не скромничай, {b}[firstname]{/b}! У тебя такой талант к искусству!"
    show player 2f
    show ross 10
    player_name "Хех, Да, наверно..."
    show player 1f
    show ross 11
    ross "Я уверен, что мы сможем каким-то образом улучшить наш класс."
    show ross 2 with dissolve
    ross "Почему бы нам не поговорить об этом сегодня после занятий?"
    show player 2f
    show ross 1
    player_name "Звучит здорово! Большое спасибо, {b}Мисс Росс{/b}!"
    show player 1f
    show ross 2
    ross "Тогда иди {b}возьми глиняную плиту{/b} и присядь, чтобы мы могли начать предклассовую медитацию."
    show player 10f
    show ross 1
    player_name "Медитацию?"
    show player 11f
    show ross 2
    ross "Ну конечно! Мы должны расслабить наш разум и выровнять наши чакры, если мы хотим, чтобы наше творчество шло правильно!"
    show player 10f
    show ross 1
    player_name "Ух. Да, мэм."
    return

label art_classroom_mia_find_easel:
    scene art_classroom_b
    show player 4 with dissolve
    player_name "Хмм..."
    show player 12 with dissolve
    player_name "Давайте посмотрим, смогу ли я найти {b}мольберт{/b}, который я мог бы использовать, чтобы нарисовать некоторые идеи для татуировки..."
    hide player with dissolve
    return

label easel_dialogue_mia_show_tattoo:
    show player 14 with dissolve
    player_name "( Сначала я должен показать рисунок, который я сделал для {b}Мии{/b}, прежде чем я сделаю еще один. )"
    hide player with dissolve
    return

label easel_dialogue_mia_draw_tattoo_intro:
    scene school_art_tattoos
    player_name "Хмм..."
    player_name "( Что я должен нарисовать для {b}Мии{/b}... )"
    return

label easel_dialogue_mia_draw_tattoo_drawn:
    hide player with dissolve
    scene school_art_cs01
    with fade
    show text "Я и раньше рисовал много картин...\n...Но, делая что-то подобное для {b}Мии{/b} заставило меня очень нервничать!\nНадеюсь, она этого хочет..." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve
    scene art_classroom_b
    show player 381 with dissolve
    player_name "Неплохо!"
    show player 386
    player_name "( Я должен пойти и показать {b}Мии{/b} что получилось. )"
    player_name "( Надеюсь, ей понравится...)"
    hide player with dissolve
    return

label art_classroom_ross_molding_clay_cutscene:
    scene location_school_art_cutscene03
    with fade
    show text "Было приятно вернуться в художественный класс." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "У меня всегда были способности к этому." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    scene location_school_art_cutscene04
    with fade
    show text "К сожалению, то же самое нельзя сказать о моих друзьях..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    scene location_school_art_closeup
    show player 547f at right
    show ross 27 zorder 1 at left
    with dissolve
    ross "Боже, какой милый маленький жираф, {b}[firstname]{/b}!"
    show player 548f
    show ross 26
    player_name "Вы так думаете?"
    show player 547f
    show ross 27
    ross "Просто Прелесть!"
    show ross 13 with dissolve
    ross "Это, безусловно, очень талантливо. Не так ли?"
    show player 10f with dissolve
    show ross 12
    player_name "Хух?"
    show player 11f
    show ross 13
    ross "Я просто хочу сказать, что он такой длинный и толстый..."
    show player 2f
    show ross 12
    player_name "... О, вы имеете в виду шею!"
    show player 1f
    show ross 11
    ross "Хе-хе, да, это тоже. Он очень хорошо сделан!"
    show ross 10
    player_name "..."
    show ross 11
    ross "Так что мы будем делать с твоими низкими оценками?"
    show ross 13
    ross "Я могу придумать больше, чем несколько применений для этих талантливых рук..."
    show player 11f
    show ross 12
    player_name "..."
    show ross 13
    ross "Может, нам стоит начать после школы-"
    show ross 12
    smi "{b}Росс{/b}!!!" with hpunch
    show ross 24
    show player 22f
    smi "Где ты, ты Утка!?"
    show player 11 zorder 0 at Position(xpos=0.45, ypos=1.0)
    show principal 2 at Position(xpos=0.75, ypos=1.0)
    with dissolve
    smi "Тебе лучше не делать голую медитацию опять-"
    show principal 3b at Position(xpos=0.8, ypos=1.0) with dissolve
    pause
    show principal 27 at Position(xpos=0.75, ypos=1.0) with dissolve

    smi "О, вот ты где!"
    show ross 23
    show principal 26
    ross "Извините, я сейчас занимаюсь со студентом..."
    show ross 22
    show principal 27
    smi "Пуф-Ф. Ему просто придется подождать."
    smi "Мне нужно поговорить с тобой обо всем, что ты заказала."
    show ross 25
    show principal 26
    ross "Вы имеете в виду художественные принадлежности?"
    show ross 24
    show principal 27
    smi "Я не знаю! Что бы это ни было, этого не будет!"
    show ross 25b
    show principal 26
    ross "Но..."
    show ross 24
    show principal 27
    smi "Слушай, это просто не в бюджете {b}Барбара{/b}."
    smi "Тебе придется обходиться без этого."
    show ross 25
    show principal 26
    ross "{b}Директриса Смит{/b}, нам нужны эти принадлежности! Наше оборудование разгромлено!"
    show ross 24
    show principal 27
    smi "Я не могу дать тебе то, чего у меня нет, не так ли?"
    show principal 26
    ross "..."
    show principal 28 at Position(xpos=0.7, ypos=1.0) with dissolve
    smi "Просто будьте благодарны, что у вас все еще есть какой-то {b}бюджет{/b}."
    smi "Вы хоть представляете, как трудно продать то, хиппи-дерьмо, которое вы рисуете на досках?"
    show ross 25b
    show principal 26 at Position(xpos=0.75, ypos=1.0) with dissolve
    ross "... Но искусство важно для роста личности!"
    show ross 24
    show principal 27
    smi "Да, конечно..."
    smi "Ответ НЕТ, {b}Барбара{/b}!"
    smi "Тебе просто придется пережить это."
    hide principal
    with dissolve
    pause
    hide player
    show player 11f zorder 1 at right
    show ross 23
    with dissolve

    ross "Аррр!"
    ross "С каждым годом становится все хуже и хуже!"
    show ross 22
    pause
    show mia 12b zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve

    mia "Все в порядке, {b}Мисс Росс{/b}?"
    show ross 11
    show mia 8b
    ross "О, привет, {b}Мия{/b}."
    show ross 10
    show mia 12b
    mia "Я слышала, как {b}Директриса Смит{/b} кричала на тебя..."
    show mia 8b
    show player 10f
    player_name "Да, это определенно звучит не очень хорошо."
    show player 11f
    show ross 25
    ross "Просто так мало бюджета на искусство."
    show ross 25b
    ross "Он становится все меньше и меньше с каждым годом."
    show ross 25
    ross "Боюсь, у меня скоро не будет работы..."
    show ross 24
    show mia 12b
    mia "Серьезно?"
    mia "Они не могут просто взять и закрыть класс рисования, да?"
    show ross 25
    show mia 8b
    ross "Я не могу пойти против {b}Директриса Смит{/b}.  Она не уважает то, чему я учу."
    show ross 25b
    ross "Если бы я только могла найти способ немного увеличить финансирование..."
    show ross 24
    show player 10f
    player_name "Нмм, а сколько нужно денег?"
    show ross 25
    show player 11f
    ross "Я точно не знаю."
    show ross 24
    pause
    show mia 12b
    mia "Тысяча долларов поможет?"
    show mia 8b
    show ross 25
    ross "А? Да, этого было бы достаточно, чтобы заказать новое оборудование, пополнить запасы на полках и, возможно, даже нанять настоящих моделей для рисования."
    ross "... Но где мы возьмем такие деньги?"
    show ross 24
    show mia 62 at Position(xpos=0.585, ypos=1.0) with dissolve

    mia "Вы можете принять участие в {b}конкурсе искусств мэра{/b}!"
    show mia 63
    show ross 11
    ross "{b}Мэр{/b} проводит художественный конкурс?"
    show mia 62
    show ross 10
    mia "Да, взгляните."
    show flyer 1 zorder 3 with dissolve
    show mia 63
    pause
    hide flyer with dissolve

    show player 10f
    player_name "Награда за первое место 1000 долларов, хух?"
    show player 2f
    player_name "{b}Мисс Росс{/b}, вы должны участвовать!"
    show player 1f
    show ross 27 with dissolve
    ross "О небеса, нет! У меня не было бы шанса выиграть что-то подобное..."
    show ross 26
    show mia 7 at Position(xpos=0.65, ypos=1.0) with dissolve
    ross "..."
    show ross 27
    ross "... но {b}[firstname]{/b} может."
    show ross 26
    show player 10f
    player_name "Что?!"
    player_name "Нет! Я недостаточно талантлив для такого."
    show ross 11 with dissolve
    show player 11f
    ross "Ерунда! Ты самый талантливый студент, который у меня был за долгое время!"
    ross "С моей помощью, я думаю получится!"
    show ross 10
    show mia 9
    mia "Хе-хе, это так здорово!"
    show mia 10b
    mia "Ты сможешь, {b}[firstname]{/b}!"
    show mia 7
    show ross 11
    ross "Видишь, {b}Мия{/b} верит в тебя! Надо попробовать!"
    show player 10f
    show ross 10
    player_name "Я не..."
    show player 11f
    show ross 27 with dissolve
    ross "Что если я пообещаю повысить твои оценки?"
    show player 10f
    show ross 26
    player_name "Ты хочешь повысить мои оценки?"
    show player 11f
    show ross 27
    ross "Все, что тебе нужно сделать, это много практиковаться в течение нескольких недель и приготовить что-то к конкурсу."
    ross "Ты сделаешь это а я поставлю 5+!"
    show player 10f
    show ross 26
    player_name "5+?!"
    player_name "Только за участие?"
    show player 11f
    show ross 27
    ross "Вот именно. Ну что договорились?!"
    show ross 26
    pause
    show player 2f
    player_name ".Да, хорошо. Договорились!"
    show player 1f
    show mia 9
    mia "Ура!"
    show mia 7

    hide player
    show ross 21 at Position(xpos=0.15, ypos=1.0) with dissolve
    ross "Я знала, что ты меня не подведешь, {b}[firstname]{/b}!"
    ross "Возвращайся сюда {b}завтра после занятий{/b} и мы начнем!"
    show ross 11 at left
    show player 11f at right
    with dissolve
    ross "Хорошо, {b}[firstname]{/b}?"
    show ross 10
    show player 10f
    player_name "Хорошо, {b}Мисс Росс{/b}. До завтра."

    $ game.timer.tick()
    $ M_ross.trigger(T_ross_molded_clay)
    $ game.main()

label leave_art_classroom:
    if not M_ross.is_state(S_ross_grab_clay):
        jump left_hall_dialogue
    else:

        scene location_school_art_closeup
        show player 2 with dissolve
        player_name "{b}Мисс Росс{/b} хочет, чтобы я взял глиняную плиту и занял свое место."
        $ game.main()

label player_ross_magazines_3_left:
    show player 14 with dissolve
    player_name "Я нашел одну стопку журналов!"
    player_name "Если я смогу найти еще две стопки, у меня будет достаточно, чтобы сделать коллаж."
    hide player with dissolve
    $ player.get_item("magazines1")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_2_left:
    show player 14 with dissolve
    player_name "Теперь мне нужно найти еще одну стопку журналов для {b}Мисс Росс{/b}."
    hide player with dissolve
    $ player.remove_item("magazines1")
    $ player.get_item("magazines2")
    $ M_ross.trigger(T_ross_found_magazines)
    return

label player_ross_magazines_1_left:
    show player 14 with dissolve
    player_name "Вот и все! У меня хватает журналов, чтобы начать работать над художественным коллажем {b}Мисс Росс{/b}!"
    hide player with dissolve
    $ player.remove_item("magazines2")
    $ player.get_item("magazines")
    $ M_ross.trigger(T_ross_found_magazines)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
