label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Простите, Сэр?"
    show player 5
    show earl 2
    ear "А?"
    ear "Что вы здесь делаете дети?"
    show earl 3 with dissolve
    show player 10
    player_name "Мы просто пытаемся получить информацию об аресте, который вы сегодня произвели."
    show player 5
    show earl 2 with dissolve
    ear "Хмм, ты дочь {b}Кристи{/b}, не правда ли?"
    show earl 1
    show roxxy 1jf
    rox "..."
    show player 10
    player_name "Да, верно, Сэр."
    player_name "Не могли бы вы рассказать нам, что произошло?"
    show player 5
    show earl 2
    ear "Боюсь, мне запрещено обсуждать эти вопросы с кем-либо, кроме членов её семьи."
    ear "Если вы хотите пойти со мной, мисс. Я расскажу вам, как все это работает."
    show earl 1
    show player 10
    player_name "... Да, хорошо. Я подожду зэесь-"
    show player 11
    show roxxy 2c at Position (xpos=500) with dissolve
    rox "Нет!"
    show roxxy 2cf at Position (xpos=434)
    with dissolve
    rox "... то-есть."
    show roxxy 33f at Position (xpos=400) with dissolve
    rox "Я хочу чтобы он остался."
    show roxxy 32f
    show player 13
    ear "..."
    show earl 2
    ear "Вы уверены."
    show earl 1
    show roxxy 33f
    rox "Да."
    show roxxy 32f
    show earl 2
    ear "Дело ваше."
    ear "Сегодня утром мы получили анонимную наводку о большом запасе наркотиков в вашем доме."
    ear "Поэтому мы поехали туда посмотреть правда ли это."
    ear "Вы знали, что у {b}вашей матери{/b} было более фунта (0.5кг) кристаллического Метамфетамина, спрятанного под диваном?"
    show earl 1
    show roxxy 1if
    show player 23
    player_name "Фунта?!"
    show player 22
    show roxxy 27f at Position (xoffset=67)
    rox "..."
    show earl 2
    ear "Боюсь, что да."
    ear "Это уже уголовная ответственность."
    ear "Мы задержали {b}твою мать{/b} за хранение наркотиков с намерением их продать."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "..."
    show player 10
    player_name "Это плохо."
    show player 5
    show roxxy 1jf with dissolve
    show earl 2
    ear "Да, сынок. Это конечно плохо."
    ear "... Ну, я знаю {b}Кристи{/b} очень давно."
    ear "Когда-то мы вместе ходили в школу."
    ear "Она всегда умела попадать в неприятности..."
    ear "... Но после допроса сегодня утром, я могу сказать вам без сомнения, что она не знает ничего о приготовлении мета."
    ear "Теперь она утверждает, что она сделала все сама и хотела сбыть..."
    ear "... Но я бы поставил хорошие деньги, на то что она просто держала его для кого-то другого!"
    show earl 1
    rox "..."
    show earl 2
    ear "К сожалению, если я не найду доказательств. Она надолго попадет в тюрьму."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "{b}*фырк*{/b}."
    show player 10
    player_name "Хорошо, а что насчет дома моей подруги?"
    show roxxy 1jf with dissolve
    show player 5
    show earl 2
    ear "О, трейлер?"
    ear "... Ну, если {b}Кристи{/b} будет осуждена, его вернут властям штата и продадут."
    show earl 1
    show player 25
    player_name "Шшшииишшшш..."
    show player 12
    player_name "Мы можем что-нибудь сделать, чтобы исправить это?"
    show player 5
    show earl 2
    ear "Нет, если только ты не убедишь {b}Кристи{/b} расказать о том кого она выгораживает..."
    show earl 1
    rox "..."
    show player 11
    player_name "..."
    show player 5
    show earl 2
    ear "Мне очень жаль, что все так вышло, Мисс."
    show earl 1
    rox "{b}*фырк*{/b}"
    show earl 2
    ear "Вы можете {b}спустится вниз к камерам и навести её{/b} если желаете."
    ear "Её уже должны были допросить."
    show earl 1
    show player 14
    player_name "Хорошо, спасибо за информацию, офицер."
    show player 13
    hide earl with dissolve
    pause
    show player 5
    show roxxy 33bf
    rox "... {b}*фырк*{/b} Все это ради рожденным идиотом..."
    show roxxy 1j with dissolve
    show player 10
    player_name "Ладно, пошли поговорим с {b}твоей мамой{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl 2 at right
    show player 11 at left
    with dissolve
    ear "Что ты здесь делаешь?!"
    show earl 3
    ear "Это ещё один из тех дней \"Приведи своих детей на работу\"?"
    show earl 1
    show player 14
    player_name "О, нет, я просто проходил мимо, сэр."
    player_name "Я хотел поговорить с {b}Гарольдом{/b}."
    show earl 2
    show player 1
    ear "Подожди минутку... Ты же ходишь в школу с моей дочерью?"
    show earl 3
    show player 14
    player_name "О, да! Вы отец {b}Ронды{/b}!"
    show earl 2
    show player 1
    ear "Деееерррррьььмоооо!"
    show player 11
    ear "Тебе лучше следить за собой находясь рядом с моей девочкой, или мне придется установить наблюдение за {b}тобой{/b}."
    show earl 4
    ear "Ясно?!"
    show earl 1
    show player 29
    player_name "Ооо... конечно, Сэр!"
    player_name "Я никогда-"
    show earl 2
    show player 13 at left
    ear "Расслабься, я просто прикалываюсь! Иди."
    return

label earl_police_office_dialogue_pre:
    show earl 2 at right
    show player 1 at left
    with dissolve
    ear "Привет, что случилось?"
    show earl 3
    return

label earl_police_office_dialogue_donuts:
    show earl 1
    show player 14
    player_name "Это может показаться глупым вопросом, но какие пончики нравятся {b}Гарольду{/b}?"
    show player 1
    show earl 2
    ear "Ха!"
    ear "{b}Гарольд{/b} ест только пончики, если они в {b}[harold_glaze]{/b}..."
    show earl 3
    ear "... Но я не знаю, что ещё он на них посыпает."
    show player 14
    show earl 1
    player_name "Понятно."
    show player 11
    show earl 2
    ear "Почему ты спрашиваешь?"
    show player 17
    show earl 1
    player_name "О, просто так."
    show player 11
    show earl 4
    ear "Подожди, разве ты не должен быть в школе? Что ты здесь делаешь-"
    show player 14
    show earl 3
    player_name "Аааа..."
    show player 17
    player_name "Спасибо, пока!"
    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Вы не знаете где может быть {b}Гарольд{/b}?"
    player_name "Мне нужно эээээ... вернуть ему кое-что!"
    show player 11
    show earl 2
    ear "Я не знаю куда он делся, но я видел его вчера в офисе..."
    ear "...Он был в ужасном состоянии, это уж точно!"
    ear "На секунду мне показалось, что он уходит..."
    ear "...но я сказал ему взять отгул."
    show earl 1
    show player 12
    player_name "Он не упоминал, где будет во время дежурства?"
    show player 5
    show earl 2
    ear "Я не хотел задавать слишком много вопросов, понимаешь?"
    ear "Некоторым ребятам иногда нужно побыть одним..."
    show earl 1
    show player 14
    player_name "Хорошо, спасибо."
    return

label earl_police_office_dialogue_roxxys_mom:
    show earl 1
    show player 12
    player_name "Где мы можем поговорить с {b}мамой моего друга{/b}?"
    show player 5
    show earl 2
    ear "Она {b}внизу в камере{/b}."
    ear "Офицер {b}Юми{/b} внизу, она даст вам немного личного пространства, чтобы поговорить."
    show earl 1
    show player 14
    player_name "Хорошо, спасибо."
    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Просто проходил мимо, сэр."
    show earl 2
    show player 1
    ear "Хорошо."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
