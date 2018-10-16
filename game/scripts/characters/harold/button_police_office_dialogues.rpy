label harold_police_office_dialogue_mia_route:
    show harold 1 at right
    show player 14 at left
    with dissolve
    player_name "Хэй, {b}Harold{/b}!"
    show player 13
    show harold 2
    harold "Вот мой мужик!"
    show harold 1
    show player 14
    player_name "Как идут дела в последнее время?"
    show player 13
    show harold 2
    harold "Никогда не было лучше! Наша семья самая счастливая на свете!"
    harold "{b}Helen{/b} очень изменилась. Очень... изменилась."
    harold "Горячие вещи в спа-"
    show harold 4
    harold "В любом случае, ты знаешь, что я имею в виду."
    show harold 1
    show player 21
    player_name "Хех хех... Да, я полагаю..."
    show player 13
    show harold 2
    harold "Я должен вернуться к работе."
    harold "Не стесняйтесь заходить в дом в любое время, сынок!"
    show harold 1
    show player 14
    player_name "Спасибо, {b}Harold{/b}!"
    player_name "Увидимся позже."
    return

label harold_police_office_dialogue_helen_route_split:
    show player 22f at right
    show harold 51 at left
    with dissolve
    pause
    show harold 52
    show yum 12f at Position (xpos=395)
    with dissolve
    yum "!!!"
    show player 5f
    yum "О! Я не видела тебя тут...."
    show yum 14f at Position (xpos=382) with dissolve
    show harold 53
    harold "Не волнуйся, {b}Yumi{/b}, это просто дружок моей дочери."
    show harold 52
    show player 10f
    player_name "Привет..."
    show player 5f
    show yum 13f
    yum "Привет... Ох! Я забыла, что у меня есть кое-что... нужно уладить в моем офисе."
    hide yum
    show harold 54
    with dissolve
    harold "..."
    show harold 55
    harold "Прости, что тебе пришлось это увидеть, сынок."
    harold "{b}Yumi{/b} мой новый напарник..."
    harold "Я бы попробовал научить ее паре вещей..."
    show harold 54
    show player 11f
    player_name "..."
    show player 10f
    player_name "Так ты и {b}Helen{/b}..."
    show player 5f
    show harold 55
    harold "Слушай этот корабль уплыл, парень.. {b}Helen{/b} по всей видимости согласилась с нашим расставанием."
    harold "Я решил, что мне тоже лучше двигаться дальше."
    harold "Сказать тебе правду."
    harold "Я никогда не был счастливее, и я начал встречаться с кем-то другим."
    show harold 54
    show player 12f
    player_name "Интересно,кто..."
    show player 10f
    player_name "По крайней мере, ты счастлив..."
    show player 5f
    pause
    show player 10f
    player_name "Но как {b}Mia{/b} справилась с этим? С ней все будет в порядке?"
    show player 5f
    show harold 55
    harold "Я не отказываюсь от {b}Mia{/b}."
    harold "Я навещаю ее каждый день. Она моя сильная маленькая девочка.."
    harold "Она всегда была там после того,чтобы померить {b}Helen{/b} и меня."
    harold "Все будет хорошо."
    show harold 54
    show player 12f
    player_name "Хорошо."
    show player 5f
    show harold 55
    harold "Ты хороший парень, {b}[firstname]{/b}.Еще раз спасибо за заботу о моей дочери."
    harold "Я ценю, что ты и она пытаетесь вернуть меня с {b}Helen{/b}..."
    harold "Просто некоторые вещи просто не работают..."
    show harold 54
    show player 21f
    player_name "Хех хех..."
    player_name "Пожалуйста."
    show player 5f
    show harold 55
    harold "Не бойсяь навещать меня, если тебе понадобится помощь."
    show harold 54
    show player 36f with dissolve
    player_name "Хорошо.До свидания, {b}Harold{/b}."
    return

label harold_police_office_dialogue_mia_harold_backup:
    show harold 1 at Position (xpos=762)
    show player 23 at left
    with dissolve
    player_name "{b}Harold{/b}!!"
    show player 22
    show harold 6
    harold "Что происходит??Ты нашел {b}Yumi{/b}?"
    show harold 1
    show player 38 with dissolve
    player_name "Да! Но она нуждается в твоей помощи,сейчас!!"
    show player 3 with dissolve
    show harold 3
    harold "Что?!"
    show harold 1
    show player 10 with dissolve
    player_name "В камере! {b}Yumi{/b}... Она борется с заключенным!!"
    show player 5
    show harold 29
    harold "!!!"
    show harold 30 at right with dissolve
    harold "Я... Я должен вызвать подкрепление.. Возможно, я должен сказать {b}Earl{/b} первому-"
    show player 12
    player_name "{b}Harold{/b}!Нет времени!"
    hide harold
    show harold 25 at Position (xpos=762)
    with dissolve
    player_name "Вы должны взять ситуацию под контроль."
    show player 11
    show harold 26
    harold "Но я должен сказать {b}Earl{/b} сначала..."
    harold "...Я давно не имел дела с заключенными и-"
    show harold 25
    show player 15
    player_name "{b}Yumi{/b}'ваш партнер и нуждается в вашей помощи!"
    player_name "Ты должен идти!СЕЙЧАС!!!"
    show player 16
    show harold 24
    harold "..."
    show harold 6
    harold "Ты прав. Я должен принять меры."
    harold "Let's go."
    return

label harold_police_office_dialogue_mia_harolds_thoughts:
    show harold 1 at right
    show player 36 at left
    with dissolve
    player_name "Привет, {b}Harold{/b}."
    show player 13 with dissolve
    show harold 2
    harold "Привет еще раз,парень."
    show harold 1
    show player 14
    player_name "Решил заглянуть и узнать, как прошел ужин {b}Mia{/b} и {b}Helen{/b}."
    show player 13
    show harold 6
    harold "О... Эмм..Это было хорошо, я думаю. да была действительно хорошей."
    show harold 1
    show player 10
    player_name "Как вы думаете, дела ...стали лучше между {b}Helen{/b}...и тобой?"
    show player 5
    show harold 4
    harold "..."
    show harold 6
    harold "Я знаю {b}Mia{/b} пытается сделать чтобы {b}Helen{/b} и я были снова вместе."
    harold "Ты её помогаешь тоже.Ты хороший парень."
    show harold 1
    harold "..."
    show harold 6
    harold "Я предполагаю, что дела между {b}Helen{/b} и мной лучше чем тогда, когда Вы видели нас Орущими друг на друга."
    show harold 4
    pause
    harold "Я... просто не знаю хотя..."
    show harold 1
    pause
    show player 10
    player_name "Почему ты не знаешь?"
    show player 5
    show harold 26
    harold "О,сынок."
    harold "Мы можем быть в хороших отношениях сейчас, но мы могли бы рвать друг другу глотки снова."
    harold "Впервые, Я думаю, что мог бы быть более счастливым в одиночестве."
    harold "Мой брак лучше оставить позади."
    harold "Возможно... если {b}Helen{/b} действительно изменился навсегда."
    harold "Возможно, нам удастся снова быть вместе."
    show harold 1
    show player 14
    player_name "Я... Я понимаю."
    show player 13
    show harold 6
    harold "Мне лучше вернуться к работе.У меня только что был очередной прорыв в деле."
    show harold 2
    harold "Увидимся позже, {b}[firstname]{/b}."
    show harold 1
    show player 14
    player_name "Пока, {b}Harold{/b}."
    show player 13
    hide harold with dissolve  
    pause
    show player 14
    player_name "( Звучит так, будто {b}Harold's{/b} сказал мне, что есть шанс, что он вернется к {b}Helen{/b}. )"
    show player 35
    player_name "( Может быть {b}Сестра Angelica{/b}'s тренировки фактически помогут ей и {b}Harold{/b}. )"
    show player 10
    player_name "( Но... он определенно кажется счастливым сейчас без {b}Helen{/b}... )"
    player_name "( {b}Mia{/b} будет в отчаянии, если он не вернется к {b}Helen{/b}. )"
    show player 5
    player_name "..."
    show player 12
    player_name "( Думаю, на данный момент это не зависит от меня... )"
    player_name "( Может так же закончить помогать {b}Sister Angelica{/b}. )"
    show player 35
    player_name "( Что она хочет опять? )"
    hide player with dissolve
    return

label harold_police_office_dialogue_roxxy_ask_earl_release:
    scene police_c_2
    show harold 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Привет, эмм..."
    player_name "{b}Мать моего друга{/b} была взята под стражу сегодня утром, и нам нужно выяснить, что происходит."
    show player 5
    show harold 2
    harold "Хммм?"
    show harold 2
    harold "О, ты должно быть о {b}Crystal's{/b} дочке!"
    show harold 1
    show roxxy 33f
    rox "... Да."
    show roxxy 32f
    show harold 2
    harold "Черт, Ты похожа не неё как две капли воды в молодости!"
    show harold 1
    rox "..."
    show player 10
    player_name "Эмм, скажите нам почему вы её держите?"
    show player 5
    show harold 2
    harold "Извините, детки."
    harold "Хранение наркотиков это серьёзная задержка и выходит за рамки моих полномочий."
    harold "Вам придется поговорить с шефом, если хотите подробностей.."
    show harold 1
    show player 10
    player_name "... Oх."
    player_name "Хорошо,спасибо."
    show player 5
    hide harold with dissolve
    pause
    show roxxy 2c at center
    show roxxy 2c at Position (xoffset=-33)
    with dissolve
    rox "О Боже... Должно быть, они нашли {b}Clyde's{/b} весь тайник!"
    show roxxy 2b at Position (xoffset=-33)
    show player 12
    player_name "В любом случае сколько метамфетамина у твоего кузена?!"
    show player 5
    show roxxy 1j with dissolve
    rox "..."
    show roxxy 1l
    rox "Я... Эмм..."
    rox "... Я не уверена."
    show roxxy 1j
    show player 12
    player_name "Ну, я думаю, нам лучше пойти поговорить {b}шефом{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label harold_police_office_dialogue_pre:
    show player 1 at left
    show harold 2 at right
    with dissolve
    harold "О, привет, это снова ты.Нужно что-нибудь?"
    show harold 1
    show player 14
    player_name "Привет, У меня просто было несколько вопросов."
    show player 1
    return

label harold_police_office_dialogue_wheres_mia:
    show player 14
    player_name "Мне просто интересно: вы знаете, где {b}Mia{/b}?"
    show player 11
    show harold 2
    harold "Извини, Я не могу тебе сейчас помочь.; мы заняты новым делом..."
    harold "Но, она должна быть в школе или дома."
    show harold 1
    show player 14
    player_name "Хорошо. Спасибо,Сэр!"
    return

label harold_police_office_dialogue_the_chief:
    show player 12
    player_name "Кто {b}шеф{/b}?"
    show player 5
    show harold 2
    harold "О, ты хочешь {b}Earl{/b}."
    show player 13
    harold "Он вон там, на другой стороне офиса."
    show harold 1
    show player 14
    player_name "Понял,спасибо!"
    return

label harold_police_office_dialogue_larry:
    show player 10
    player_name "Что тебе нужно, чтобы я спросил {b}Larry{/b}?"
    show player 5
    show harold 6
    harold "{b}Larry{/b} отказывается говорить о расположение товара."
    show harold 1
    show player 33
    player_name "О Да!"
    show player 12
    player_name "Я поговорю с ним.Я знаю его жену."
    player_name "Если я не смогу узнать его местонахождение, может быть, я смогу попросить {b}Mrs. Johnson{/b} помочь нам."
    show player 5
    show harold 2
    harold "Спасибо, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_thief:
    show player 10
    player_name "Что мне нужно было сделать, если я снова увижу вора?"
    show player 5
    show harold 6
    harold "Если ты заметишь его, позвони мне напрямую."
    show harold 1
    show player 12
    player_name "Конечно! Я буду присматривать за ним.."
    player_name "Он всегда крадется к моей соседке, {b}Mrs. Johnson's{/b}, во двор ночью."
    show player 5
    show harold 6
    harold "Также были сообщения о нем рядом с парком. Если вы заметишь его там, держи меня в курсе"
    show harold 1
    show player 12
    player_name "Хорошо, Я также поищу еще улики."
    show player 5
    show harold 2
    harold "Спасибо, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_donuts:
    show player 14
    player_name "Какие ... пончики, эмм... вам нравятся?"
    show player 11
    show harold 3
    harold "Прошу прощения?"
    show player 14
    show harold 1
    player_name "Просто интересно!"
    show player 11
    show harold 2
    harold "Слушай,У меня нет времени сейчас болтать, Я завален работой..."
    harold "... Почему бы тебе не бежать в школу, хорошо?"
    show player 10
    show harold 1
    player_name "Но-"
    show player 5
    show harold 2
    harold "Мне нужно идти, извини.."
    return

label harold_police_office_dialogue_donuts_wrong:
    show player 437 at left with fastdissolve
    player_name "Я эмм,Вам кое-что принес."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Это для вас!"
    show harold 8
    show player 1
    with fastdissolve
    harold "Ты принесла мне коробку с ... пончиками?!"
    show player 14
    show harold 7
    player_name "Да! Я подумал,может ты захочешь перекусить ими на работе..."
    show player 1
    show harold 9
    harold "О..."
    harold "Я не большой любитель токого вида,если быть честным."
    show player 11
    show harold 10
    player_name "..."
    show harold 11
    harold "Но я err... Спасибо тебе за эту идею!"
    harold "Я уверен что {b}Earl{/b} будет более чем счастлив получить их..."
    show player 10
    show harold 10
    player_name "Хорошо."

    show player 5
    hide harold with dissolve
    pause
    show player 10
    player_name "( Черт! )"
    player_name "( Я должно быть купил не тот вид. )"
    player_name "( Я должен убедиться что получил правильные ингредиенты... )"
    return

label harold_police_office_dialogue_donuts_correct:
    show player 437 at left with fastdissolve
    player_name "Я эмм, Вам кое-что принес."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Это для вас!"
    show harold 8
    show player 1
    with fastdissolve
    harold "Ты принесла мне коробку с ... пончиками?!"
    show player 14
    show harold 7
    player_name "Да! Я подумал,может ты захочешь перекусить ими на работе..."
    show player 1
    show harold 9
    harold "Дай мне посмотреть..."
    harold "Матерь... [harold_glaze]... с... [harold_topping]?!"
    show player 14
    show harold 7
    player_name "Я подумал ты эти захочешь!"
    show player 1
    show harold 8
    harold "Это мои любимые... Как ты..."
    show player 17
    show harold 44
    player_name "Я счастливчик, пожалуй."
    show player 1
    show harold 45
    harold "*Ням ням*"
    show harold 46
    harold "Ну, парень, ты молодец."
    show player 17
    show harold 45
    player_name "Рад, что вам нравится!"
    show player 1
    harold "..."
    show player 11
    show harold 46
    harold "Подожди, пока ты не ушел..."
    show player 1
    harold "Я знаю, что тебе и {b}Mia{/b} нравится... проводить время, и тому подобное."
    harold "Ты кажешься хорошим паренем, sтак что я поговорю со своей женой и посмотрю, сможет ли она отстать немного."
    show player 14
    show harold 45
    player_name "Вы имеете в виду, Я могу навестить ее сейчас"
    show player 1
    show harold 46
    harold "Не так быстро!"
    harold "Я этого не говорил.... но... Ты, наверное, мог бы проникнуть, как раньше, а я постараюсь отвлечь свою жену, хорошо?"
    show player 14
    show harold 45
    player_name "Серьезно?"
    show player 1
    show harold 46
    harold "Я сказал, что попробую, я ничего не могу тебе обещать."
    show player 14
    show harold 45
    player_name "Спасибо, {b}Harold{/b}."
    show player 1
    show harold 46
    harold "Хорошо, теперь убирайтесь отсюда, покамой босс не увидео нас с этими пончиками!"
    show player 17
    show harold 45
    player_name "Ха ха."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
