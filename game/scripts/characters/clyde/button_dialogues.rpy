label button_clyde_roxxy_get_evidence_intro:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    with dissolve
    player_name "Нам нужно поговорить об этой ситуации с {b}Кристи{/b}."
    show player 5f
    show clyde 22
    clyde "Я бы предпочел не..."
    show clyde 21
    show player 10f
    player_name "{b}Клайд{/b}, они собираются отправить ее в тюрьму и забрать трейлер.!"
    show player 5f
    show clyde 26
    clyde "Смотри, вот! Вы думаете, что я этого не знаю!"
    clyde "Я чувствую себя плохо, но я ничего не могу сделать, чтобы остановить это!"
    show clyde 25
    show player 12f
    player_name "Вы могли бы превратить себя в..."
    show player 5f
    show clyde 22
    clyde "Да..."
    clyde "Тогда мы оба окажемся за решеткой.!"
    show clyde 21
    show player 10f
    player_name "Нет, если ты скажешь им, что {b}Кристи{/b} понятия не имела, что ты спрятал там наркотики.."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "... И зачем мне это?"
    show clyde 1
    show player 12f
    player_name "... Потому что это правильно!"
    show player 90f
    show clyde 2
    clyde "Пфф."
    clyde "Я не могу отправиться в тюрьму!"
    clyde "Красивый парень, как я, эти животные съедят меня заживо."
    show clyde 1
    return

label button_clyde_roxxy_get_evidence_about_roxxy_pass:
    scene expression player.location.background_blur
    show player 90f at right
    show clyde 1 at left
    clyde "..."
    show player 10f
    player_name "Слушай, мужик. Она взяла вину на себя, потому что она ваша семья."
    player_name "... Но это намного хуже, чем она думает!"
    player_name "Она собирается уйти надолго и {b}Рокси{/b} потеряет свою {b}Маму{/b} и свой дом."
    show player 12f
    player_name "{b}Рокси{/b} не сделала ничего, чтобы заслужить это!"
    show player 5f
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "... Ох, черт! Ты прав."
    clyde "{b}Рокси{/b} не должны страдать из-за меня..."
    clyde "... Но я не собираюсь возвращаться в тюрьму! ... Нет, сэр!"
    show clyde 21
    player_name "..."
    show player 14f
    player_name "Что если отправить свое признание в письме?"
    player_name "Расскажи им о своей хижине и пусть они найдут доказательства."
    player_name "Если вы все сделаете правильно, вы можете быть далеко, прежде чем они начнут искать вас."
    show player 13f
    clyde "..."
    show clyde 22
    clyde "Полагаю, я мог бы вернуться к крику..."
    clyde "Они никогда не найдут меня там."
    clyde "... Я бы скучал по {b}Тете Кристи{/b}, хотя..."
    show clyde 21
    show player 10f
    player_name "Ты спасешь ее из тюрьмы, чувак."
    show player 5f
    show clyde 22
    clyde "Хм, я думаю, у тебя есть хороший план."
    show player 13f
    clyde "Значит, я сделаю это, и она выйдет безнаказанной?"
    show clyde 21
    show player 12f
    player_name "... Мы все равно должны были придумать ей залог."
    show player 5f
    show clyde 22
    clyde "Сколько денег тебе нужно?"
    show clyde 21
    show player 12f
    player_name "$50,000..."
    show player 5f
    show clyde 2
    clyde "... Мда."
    clyde "Ну, я могу это сделать!"
    show clyde 1
    show player 10f
    player_name "Что?!" with hpunch
    player_name "Ты не можешь быть серьезным..."
    player_name "У вас где-то лежит 50 000 долларов?"
    show player 11f
    show clyde 2
    clyde "Не совсем."
    show clyde 4 with dissolve
    clyde "... Но у меня целая куча этого мета."
    clyde "Полагаю, хватит на 100 000 долларов для хорошего покупателя."
    show clyde 3
    show player 10f
    player_name "Это безумие!"
    player_name "Ты правда можешь его продать?"
    show player 5f
    show clyde 4
    clyde "Пфф! Давай, приятель..."
    clyde "Не знаешь, с кем разговариваешь?"
    clyde "Я могу продать эскимо с кетчупом девушке в белых перчатках!"
    show clyde 3
    show player 11f
    player_name "..."
    show player 12f
    player_name "... Кетчуп эскимо?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Да, дружище!"
    show clyde 3 with dissolve
    show player 14f
    player_name "... Когда вы можете это сделать?"
    show player 13f
    show clyde 4
    clyde "Хм, мне придётся позвать мах покупателя."
    clyde "... Но, скорее, я считаю."
    show clyde 3
    show player 14f
    player_name "Я собираюсь рассказать {b}Рокси{/b} хорошие новости!"
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_get_evidence_about_roxxy_fail:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "[chr_warn]Ты трус!"
    show player 90f
    show clyde 26
    clyde "[chr_warn]Эй, разве ты не будешь звать {b}меня{/b} не трусом?!"
    clyde "[chr_warn]Ты понятия не имеешь, каково это-сидеть в тюрьме с кем-то вроде меня!"
    clyde "[chr_warn]Я был там однажды, и будь я проклят, если вернусь!"
    show clyde 25
    show player 15f
    player_name "[chr_warn]Что... {b}ТРУС{/b}!"
    show player 16f
    show clyde 26
    clyde "[chr_warn]Пошел ты!"
    clyde "[chr_warn]Я должен принять это!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_get_evidence_nevermind:
    show player 12f
    player_name "Забудь об этом.!"
    show player 90f
    show clyde 22
    clyde "Да, это именно то, что я планирую сделать!"
    clyde "Я считаю, что это целый беспорядок, забывающий внизу этих пивных банок!"
    hide clyde
    hide player
    with dissolve
    return

label button_clyde_roxxy_selling_meth_ask_roxxy:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 10f at right
    with dissolve
    player_name "Когда ты сможешь продать метамфетамин?"
    show player 5f
    show clyde 2
    clyde "Попридержи коней, приятель!"
    clyde "Такие вещи требуют времени."
    show clyde 1
    player_name "..."
    show clyde 2
    clyde "Вы просто продолжаете рассказывать моему милому {b}кузену{/b}, что {b}Клайд{/b} заботится обо всём!"
    show clyde 1
    show player 14f
    player_name "... Хорошо."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_selling_meth:
    scene expression player.location.background_blur
    show clyde 3 at left
    show player 10f at right
    player_name "Ты связывался с покупателем?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Да, дружище!"
    show player 13f
    clyde "Я готов закрыть эту сделку!" #Исправить перевод
    show clyde 3
    show player 12f
    player_name "{b}Рокси{/b} говорит, Ты никогда раньше не продавал Мет!"
    show player 90f
    show clyde 26 with dissolve
    clyde "Что?!"
    clyde "Она ничего не знает!"
    clyde "У меня было много таких сделок!"
    show clyde 25
    show player 12f
    player_name "Вы действительно имели дело с покупателями раньше?"
    show player 5f
    show clyde 1
    clyde "..."
    show clyde 22
    clyde "Ну, Я смотрел за {b}Тетей Кристи{/b} больше ста раз!"
    show clyde 1
    show player 37f with dissolve
    player_name "..."
    player_name "{b}*Вздыхать*{/b} Я иду с тобой."
    show player 90f with dissolve
    show clyde 2
    clyde "Да?"
    clyde "Что ты знаешь о продаже наркотиков?!"
    show clyde 1
    show player 12f
    player_name "Ничего такого, черт возьми."
    player_name "... Но я знаю тебя, и ты определенно недостаточно компетентен, чтобы сделать это в одиночку."
    show player 90f
    show clyde 22
    clyde "Хорошо, но это не так... Секундочку, что значит компетентен?!"
    show clyde 1
    show player 12f
    player_name "... Именно."
    show player 90f
    show clyde 2
    clyde "Пф, Все, приятель."
    clyde "Приходите или не приходите. Для меня это не имеет значения!"
    show clyde 26
    clyde "... Но если «вы придете», вам лучше {b}встретиться со мной в трейлере сегодня вечером {/b}."
    clyde "Ты понял это?"
    show clyde 1
    show player 12f
    player_name "Да, я понял это."
    player_name "Увидимся {b}сегодня в трейлере Рокси{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Мы все еще продаем этот Мет?"
    show player 90f
    show clyde 4 with dissolve
    clyde "Да, конечно."
    clyde "Просто будь здесь {b}сегодня вечером{/b}, т тогда наш план состоиться."
    show clyde 3
    show player 12f
    player_name "Да, я сделаю это."
    player_name "Увидемся {b}сегодня вечером{/b}."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_roxxy_meeting_buyer_dark:
    scene expression player.location.background_blur
    show clyde 1 at left
    show player 12f at right
    player_name "Ты готов идти?"
    show player 90f
    show clyde 1
    clyde "..."
    show clyde 2
    clyde "Ты носишь ДАТ?"
    show clyde 1
    show player 5f
    player_name "..."
    show player 10f
    player_name "Что не так с тем, что на мне надето?"
    show player 5f
    show clyde 2
    clyde "Ого... Не знаю, приятель. Ты выглядишь ужасно подозрительно..."
    clyde "Я уверен, что ни за что не куплю наркотики у кого-то похожего на тебя."
    show clyde 1
    show player 10f
    player_name "Ну, я не принес никакой другой одежды...."
    show player 5f
    clyde "..."
    show clyde 2
    clyde "Подождите секундочку, подожди. Мне нужно кое-что на тебя надеть!"
    hide clyde with dissolve
    show player 12f
    player_name "... Это должно быть интересно."
    scene black with fade
    pause
    scene park_bench
    show clyde 4 at left
    with dissolve
    clyde "Давай, приятель..."
    clyde "Ты хочешь опоздать!"
    show clyde 3
    show player 12f at right
    show player_outfit bb 638ef at Position (xpos=866)
    with dissolve
    player_name "Не могу поверить, что позволил тебе уговорить меня надеть это...."
    player_name "Я чувствую себя нелепо!"
    show player 90f
    show clyde 4
    clyde "Пф, не будь глупым."
    clyde "Вы выглядите как настоящая дилер!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Покупатель должен быть здесь через секунду."
    hide clyde
    hide player
    hide player_outfit
    with dissolve
    return

label button_clyde_cletus_introduce:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "{b}Клайд{/b}?!"
    show player 5f
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 10f
    player_name "Когда ты вернулся в город?!"
    show player 5f
    show clyde 2
    clyde "Эх, прости приятель."
    clyde "Ты ошибся приятель..."
    show clyde 1
    show player 10f
    player_name "Что?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Меня зовут {b}Клетус{/b}!"
    clyde "Приятно познакомиться.!"
    show clyde 3
    player_name "..."
    show player 12f
    player_name "О чем ты говоришь , {b}Клайд{/b}?"
    show player 5f
    show clyde 2 with dissolve
    clyde "{b}*Гхм*{/b} Снова..."
    clyde "Меня зовут не {b}Clyde{/b}... а {b}Клетус{/b}."
    show clyde 1
    show player 12f
    player_name "... Но вы так похожи на кузина {b}Рокси{/b}, {b}Клайда{/b}."
    show player 5f
    show clyde 2
    clyde "Хм, ну извините. Я не знаю ни какого {b}Клайда{/b}."
    show clyde 9 with dissolve
    clyde "Он уверен, что звучит как красивая сука сына, хотя!"
    show clyde 3 with dissolve
    player_name "..."
    show player 17f
    player_name "Ты сейчас шутишь надо мной?!"
    show player 13f
    show clyde 4
    clyde "Позвольте спросить у вас..."
    clyde "Этот {b}Клайд{/b} носит шляпу?"
    show clyde 3
    show player 10f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Ну, тогда проехали!"
    clyde "Как вы можете видеть... Клетус никогда никуда не уходит без своей верной шляпы!"
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Это странно."
    show player 12f
    player_name "Я пойду."
    show player 5f
    show clyde 4
    clyde "Хорошо. Ну, было приятно встретиться, {b}[firstname]{/b}!"
    show clyde 3
    player_name "..."
    show player 92f
    player_name "Я не сказал тебе своего имени!"
    show player 91f
    show clyde 22
    clyde "!!!" with hpunch
    clyde "Ох, чёрт..."
    clyde "... Ну, Я..."
    show clyde 11 with dissolve
    clyde "Эмм... Телепатия!"
    show clyde 12
    show player 10f
    player_name "Что?!"
    show player 5f
    show clyde 11
    clyde "Я, {b}Клетус{/b}... Я телепат."
    show clyde 4 with dissolve
    clyde "... И я не могу читать твои мысли своими пулями разума!"
    show clyde 3
    show player 10f
    player_name "Пули разума?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Ты прав, приятель!"
    show clyde 4 with dissolve
    clyde "Так что не говори людям, что я здесь."
    clyde "Я знаю..."
    clyde "Особенно, если эти люди-пух."
    show clyde 3
    player_name "..."
    show player 25f
    player_name "Я..."
    player_name "... Просто..."
    player_name "... Пойду."
    hide player with dissolve
    pause
    show clyde 4
    clyde "Пока, приятель.!"
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_intro_0:
    show clyde 2 at left
    show player 5f at right
    with dissolve
    clyde "Могу я вам чем-нибудь помочь?"
    show clyde 1
    show player 10f
    player_name "Ухх, нет?"
    show player 5f
    show clyde 22
    clyde "О чувак. Ты один из демократов, Иисус любит тебя??"
    show clyde 21
    show player 12f
    player_name "Что?! Нет!"
    show player 5f
    show clyde 26
    clyde "{b}*Вздох*{/b} Ты полицейский?!"
    clyde "Вы должны сказать мне сейчас, это закон!"
    show clyde 25
    show player 12f
    player_name "Ничейный... Мы познакомились прошлой ночью!"
    show player 5f
    clyde "..."
    show player 10f
    player_name "Я помогал {b}Рокси{/b} с домашним заданием?"
    show player 5f
    show clyde 4 with dissolve
    clyde "Черт, да!"
    clyde "Ты новый парень {b}Рокси{/b}!"
    show clyde 3
    show player 10f
    player_name "Нет, вы просто др-"
    show player 5f
    show clyde 4
    clyde "Как ты поживаешь, братишка?!"
    show clyde 3
    player_name "..."
    return

label button_clyde_intro_1:
    show clyde 4 at left
    show player 5f at right
    with dissolve
    clyde "Что случилось, брат?!"
    show clyde 3
    show player 14f
    player_name "Ох, привет {b}Клайд{/b}..."
    show player 5f
    show clyde 4
    clyde "Что ты здесь делаешь??!"
    show clyde 3
    return

label button_cletus_intro:
    show player 12f at right
    show clyde 3 at left
    show clyde_hat at left
    with dissolve
    player_name "Так {b}Клетус{/b}, правда?"
    show player 5f
    show clyde 9 with dissolve
    clyde "Ты прав, приятель!"
    show clyde 4 with dissolve
    clyde "Что я могу сделать для тебя?!"
    show clyde 3
    return

label button_clyde_how_are_you:
    show player 37f with dissolve
    player_name "{b}*Вздох*{/b} У меня все в порядке."
    player_name "Как дела?"
    show player 5f with dissolve
    show clyde 9 with dissolve
    clyde "Более того, кто не я!" #Исправить перевод
    clyde "Ха-ха, знаю, что я имею в виду, брат?!"
    show clyde 3 with dissolve
    show player 24f
    player_name "..."
    show clyde 11 with dissolve
    clyde "Потому что у меня есть секс... С дамами..."
    clyde "{b}*Гм*{/b} Человеческие дамы."
    show clyde 12
    show player 12f
    player_name "Да, Я понимаю, {b}Клайд{/b}..."
    show clyde 9 with dissolve
    clyde "Хех, да я делаю!" #Исправить перевод
    show clyde 3 with dissolve
    return

label button_clyde_where_are_you_from:
    show player 10f
    player_name "Я никогда не слышал, чтобы кто-то говорил так, как ты, {b}Клайд{/b}..."
    show player 12f
    player_name "Откуда ты вообще взялся?"
    show player 5f
    show clyde 4
    clyde "Потому что все вы, городские, говорите странно!"
    clyde "Внизу, в крике, мы все разговариваем как дис..."
    show clyde 3
    show player 10f
    player_name "... вскрик?"
    show player 5f
    show clyde 4
    clyde "Да."
    show clyde 3
    show player 10f
    player_name "Это как?!"
    show player 5f
    show clyde 4
    clyde "Там, где я вырос. Да!"
    show clyde 3
    show player 11f
    player_name "..."
    show clyde 4
    clyde "Это всего лишь несколько округов к северу отсюда."
    clyde "В горах."
    show clyde 3
    show player 10f
    player_name "Я думал, что на севере сплошные леса."
    show player 5f
    show clyde 4
    clyde "Да, очень дерзко живём..."
    show clyde 3
    show player 12f
    player_name "Там живут люди?"
    show player 5f
    show clyde 4
    clyde "Да, большая часть моей семьи все еще живет там."
    clyde "Я думал, что перееду сюда с {b}Тетушкой Кристи{/b}, чтобы произнести заклинание."
    clyde "Дайте городской жизни справедливую встряску."
    show clyde 3
    show player 10f
    player_name "Как это работает?"
    show player 5f
    show clyde 2 with dissolve
    clyde "У него есть взлеты и падения."
    clyde "Я скучаю по самогону из дома и всей траве."
    show clyde 1
    player_name "..."
    show clyde 4 with dissolve
    clyde "... Но я и тут готовлю убойные блюда!"
    show clyde 22 with dissolve
    clyde "!!!"
    show clyde 21
    show player 12f
    player_name "Что ты готовишь?"
    show player 5f
    show clyde 22
    clyde "Эхх... "
    show clyde 21
    clyde "..."
    show clyde 22
    clyde "Цыпленка!"
    show clyde 4 with dissolve
    clyde "Хех, да! Я готовлю кучу жареных куриц!"
    clyde "Вы, городские, просто не можете насытиться..."
    show clyde 3
    show player 4f with dissolve
    player_name "..."
    clyde "..."
    show player 5f with dissolve
    return

label button_clyde_see_ya:
    show player 36f with dissolve
    player_name "Мне пора идти..."
    show player 5f with dissolve
    show clyde 4
    clyde "Да, ладно."
    clyde "Продолжай зажигать, брат!"
    clyde "Ууу!!"
    show clyde 3
    show player 30f
    player_name "..."
    hide player
    hide clyde
    with dissolve
    return

label button_clyde_whats_going_on:
    show player 12f
    player_name "Что у тебя там происходит?"
    show player 5f
    show clyde 2 with dissolve
    clyde "Эхх, прости брат."
    clyde "В лачугу строго вход воспрещен!"
    show clyde 9 with dissolve
    clyde "Если только у тебя нет женских частей?!"
    show clyde 3 with dissolve
    show player 30f
    player_name "... Нет."
    show player 5f
    show clyde 4
    clyde "Эх, хорошо запомни это... Если хижина качается, лучше не стучаться!"
    show clyde 9 with dissolve
    clyde "Понимаешь, о чем я говорю?!"
    show clyde 3
    show player 401f
    player_name "... Да. Мне жаль, что я не..."
    show player 403f
    return

label button_clyde_nice_tractor:
    show player 14f
    player_name "Хороший трактор."
    show player 13f
    show clyde 4
    clyde "О, да!"
    clyde "Да, это {b}Большая Берта{/b}!"
    clyde "Разве она не красавица?!"
    show clyde 3
    player_name "..."
    show clyde 4
    clyde "Я сам вырастил ее из объедков."
    clyde "31,2 лошадиных сил, 2500 об/мин, емкость 8,5 галлонов..."
    clyde "... И только посмотрите на эту рубиново-красную отделку!"
    clyde "Ммм! Она самая сексуальная штучка на четырех колесах!"
    show clyde 9 with dissolve
    clyde "Знаешь, что я имею в виду?"
    show clyde 3 with dissolve
    show player 5f
    player_name "..."
    return

label button_clyde_nevermind:
    show player 10f
    player_name "Вообще-то, забудь."
    player_name "... Может быть, в другой раз?"
    show player 5f
    show clyde 4
    clyde "Пф, Черт возьми, да, брат!"
    clyde "Ты знаешь, где меня найти."
    hide player
    hide clyde
    hide clyde_hat
    with dissolve
    return

label button_clyde_know_youre_clyde:
    show player 15f
    player_name "Нуже, {b}Клайд{/b}! Я знаю, что это ты!"
    show player 16f
    show clyde 4
    clyde "Я не знаю, о чем ты говоришь..."
    show clyde 3
    show player 15f
    player_name "Это глупо, я никому не скажу, что ты вернулся..."
    show player 16f
    show clyde 4
    clyde "Что ты там куришь, приятель?"
    show player 428f
    clyde "Меня зовут {b}Клетус{/b}, и я здесь впервые."
    clyde "Навсегда."
    show clyde 3
    show player 403f
    player_name "..."
    show player 402f with dissolve
    player_name "Он по-прежнему пишет {b}Клайд{/b} над вашим текстовым полем!"
    show player 403f
    show clyde 2 with dissolve
    clyde "Эй!"
    clyde "Не ломай четвертую стену!"
    clyde "Это жульничество!"
    clyde "Моё имя {b}Клетус{/b}!!!"
    show clyde 26
    clyde "Скажи это!"
    show clyde 25
    show player 90f
    player_name "..."
    show clyde 2
    clyde "Да ладно, я знаю что ты хочешь сказать..."
    show clyde 1
    show player 24f
    player_name "{b}*Вздыхая*{/b}"
    show player 25f
    player_name "{b}Клетус{/b}."
    show player 24f
    show clyde 4 with dissolve
    clyde "Вот так!"
    clyde "Ну это же было не так сложно, не так ли?!"
    show clyde 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
