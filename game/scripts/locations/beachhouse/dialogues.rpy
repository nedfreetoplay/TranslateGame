label beach_house_entrance_meet_consuela:
    scene expression player.location.background_blur with None
    show player 13 with dissolve
    consuela "♪El chico del apartamento (Мальчик из квартиры) 512♪"
    show player 11
    consuela "♪Él que hace a mi pobre corazón saltar (Он заставляет мое бедное сердце прыгать)♪"
    show player 10
    player_name "Какого черта?"
    show player 5
    consuela "♪Es a quien le hago cartas noche y día (Это тот, кого я пишу ночью и днем)♪"
    consuela "♪Que no puedo entregar (Что я не могу доставить)♪"
    show player 10
    player_name "В моем доме поет странная женщина!"
    show player 5
    consuela "♪El chico del apartamento (Мальчик из квартиры) 512♪"
    consuela "♪Es él quien me hace tartamuda y más (Это он заставляет меня заикаться и многое другое)♪"
    show player 12
    player_name "Похоже, она в спальне..."
    show player 5
    consuela "♪Es en quien yo pienso y sueño noche y día (Это то, о чем я думаю и мечтаю ночь и день)♪"
    consuela "♪Él, solo él (Он, только он)♪"
    show player 12
    player_name "Я лучше пойду и выясню, что она здесь делает."
    hide player with dissolve

    scene expression game.timer.image("backgrounds/location_beach_house_bedroom{}.jpg")
    show player 428 at left
    show consuela b_bending f_empty a_empty zorder 1 at flip
    show consuela at Position (xpos=500)
    with dissolve
    consuela "♪Pero hoy por fin me he decidido de veras (Но сегодня я наконец-то решил по-настоящему)♪"
    consuela "♪Todo mi amor a confesarle (Все, что я люблю признаться вам)♪"
    show player 427
    player_name "Вау."
    consuela "♪Toco su puerta y se me enchina la piel (Я прикасаюсь к ее двери, и кожа меня затыкает)♪"
    show player 426
    player_name "..."
    consuela "♪Y me contesta una güera (И она отвечает на меня)♪"
    show consuela b_lift_back with dissolve
    consuela "♪Y mi corazón se quiebra (И мое сердце обанкротилось)♪"
    show consuela b_dressed a_dressed_lift f_singing with dissolve
    consuela "♪El chico del apartamento (Мальчик из квартиры) 512♪"
    show consuela a_dressed_sing at unflip
    show consuela at Position (xpos=0)
    with dissolve
    consuela "♪Él que hace a mi pobre corazón salt- (Он заставляет мое бедное сердце пры-)♪"
    show consuela f_surprised a_dressed_work3
    consuela "Ой!!" with hpunch
    show consuela f_sad
    show player 22
    player_name "!!!"
    show player 23
    player_name "Прости, я не хотел-"
    show player 11
    show consuela f_sad_talk
    consuela "¿Que estas haciendo aqui? (Что ты здесь делаешь?)"
    show consuela f_sad
    show player 10
    player_name "Эээ..."
    show player 5
    show consuela f_sad_talk
    consuela "¿Eres un ladrón? (Ты вор?)"
    consuela "¡Llamaré a la policía! (Я вызову полицию!)"
    show consuela f_sad
    show player 10
    player_name "Полицию?!"
    player_name "Нет, нет, нет!"
    player_name "Этот дом принадлежит мне!"
    show player 5
    show consuela f_sad_talk
    consuela "¿Qué? (Что?)"
    show consuela f_sad
    show player 12c with dissolve
    player_name "Эээ... Э-Т-О М-О-Й Д-О-М!"
    show player 12b
    show consuela f_sad_talk
    consuela "Твой..."
    consuela "... Дом?"
    show consuela f_sad
    show player 12c
    player_name "Да, мой дом."
    show player 12 with dissolve
    player_name "Я только что купил его."
    show player 5
    pause
    show player 11
    show consuela f_yell
    consuela "¡{b}Камила{/b}!"
    consuela "¡{b}Камила{/b} спускайся сюда прямо сейчас!"
    show consuela f_sad
    show player 10
    player_name "Эээ?"
    show player 5
    show consuela f_angry_talk
    consuela "Ты..."
    consuela "... Стой!"
    show consuela f_angry
    player_name "..."
    show consuela f_yell
    consuela "¡{b}Камила{/b}!"
    show consuela f_angry
    martinez "¡Ya voy! (Иду!)"
    martinez "Por dios, mamá. ¿cuál es tu problema? (Господи, мама. Что случилось?)"
    show martinez f_stinkeye a_dressed_sides zorder 0 at Position (xpos=300) with dissolve
    pause
    show martinez f_angry_talk a_dressed_crossed with dissolve
    martinez "Какого хрена?!"
    show martinez f_normal_talk a_dressed_sides at flip
    show martinez at Position (xpos=750)
    with dissolve
    martinez "¿Qué está haciendo aquí? (Что ты здесь делаешь?)"
    show martinez f_normal
    show consuela f_sad_talk
    consuela "Este chico dice que el es el dueño de la casa. (Этот парень говорит, что он владелец дома.)"
    show consuela f_sad
    show martinez f_suspicious
    martinez "Что?!"
    show martinez f_angry_talk a_dressed_crossed at unflip
    show martinez at Position (xpos=300)
    with dissolve
    martinez "Ты не хозяин этого дома!"
    show martinez f_angry
    show player 12
    player_name "Ну, я - хозяин."
    show player 5
    show martinez f_angry_talk
    martinez "Ты врешь."
    show martinez f_angry
    show player 12
    player_name "Вообще-то, я только что купил его."
    show player 90
    show martinez f_normal_talk at flip
    show martinez at Position (xpos=750)
    with dissolve
    martinez "Dice que acaba de comprar la casa. (Он сказал, что только что купил дом.)"
    show martinez f_normal
    show consuela f_sad_talk
    consuela "¿Qué? (Что?)"
    show consuela f_unsure
    consuela "¿Quieres decir que sus padres lo compraron? (Ты имеешь в виду, что его родители купили его?)"
    show consuela f_sad
    show martinez f_normal_talk
    martinez "No, él dice que lo hizo. (Нет, он сказал, что сам купил.)"
    show martinez f_normal
    show consuela f_sad_talk
    consuela "En verdad? (Правда?)"
    show consuela f_laugh
    consuela "¡Eso es increíble! (Это невероятно!)"
    show consuela f_normal_talk
    consuela "¿Cómo alguien tan joven ganó el dinero para una casa tan grande? (Как и где такой молодой заработал деньги на такой большой дом?)"
    show consuela f_normal
    show martinez f_angry_talk at unflip
    show martinez at Position (xpos=300)
    with dissolve
    martinez "{b}Моя мама{/b} хочет знать, как тебе удалось позволить себе такую квартиру в одиночку?"
    show martinez f_angry
    show player 10
    player_name "Это {b}твоя мама{/b}?"
    show player 11
    show martinez f_angry_talk
    martinez "Да, а что?!"
    show martinez a_dressed_sign with dissolve
    martinez "У тебя с этим проблемы?"
    show martinez f_angry a_dressed_crossed with dissolve
    show player 10
    player_name "Нет..."
    show player 5
    show martinez f_angry_talk
    martinez "Тогда ответь на мой вопрос, Estúpido (глупый)!"
    show martinez f_angry
    show player 12
    player_name "Я много работал и копил свои деньги."
    show player 5
    show martinez f_laugh
    martinez "Ха!"
    show martinez f_angry_talk
    martinez "Где, черт возьми, ты работаешь, что тебе платит достаточно, чтобы купить гребаный огромный домик на пляже!"
    show martinez f_angry
    show player 12
    player_name "Это не твое дело."
    show player 90
    show martinez f_eyeroll
    martinez "Пфффф."
    show martinez f_angry
    show consuela f_normal_talk
    consuela "¿Vas a la escuela con este chico? (Ты ходишь в школу с этим парнем?)"
    show consuela f_normal
    show martinez f_normal_talk a_dressed_sides at flip
    show martinez at Position (xpos=750)
    with dissolve
    martinez "Sí, es un perdedor ... (Да, он неудачник ...)"
    show martinez f_normal
    show consuela f_sad_talk
    consuela "¡¿Perdedor?! (Неудачник?!)"
    consuela "Creo que es un poco lindo. (Я думаю, он немного милый.)"
    show consuela f_sad
    show martinez f_normal_talk
    martinez "Йейк, мама..."
    martinez "¡Eso es asqueroso! (Это отвратительно!)"
    show martinez f_normal at unflip
    show martinez at Position (xpos=300)
    with dissolve
    show consuela f_unsure
    consuela "Я Эх... Простите, мистер?"
    show consuela f_normal
    show player 5
    player_name "Хмм?"
    show player 10
    player_name "О, эмм... {b}[firstname]{/b}."
    player_name "Меня зовут {b}[firstname]{/b}."
    show player 5
    show consuela f_laugh
    consuela "Мистер {b}[firstname]{/b}."
    consuela "Меня зовут {b}Консуэла{/b}."
    show consuela f_normal_talk
    consuela "И это моя глупая дочь, {b}Камила{/b}."
    show consuela f_normal
    show martinez f_eyeroll a_dressed_crossed at flip
    show martinez at Position (xpos=750)
    with dissolve
    martinez "Mamá, no me llames estúpido! (Мама, не называй меня глупой!)"
    show martinez f_normal
    show consuela f_normal_talk
    consuela "Dile que estoy aquí para limpiar la casa. (Скажи ему, что я здесь, чтобы убрать дом.)"
    consuela "No voy a entrar en su camino. (Я не буду мешать ему.)"
    show consuela f_normal
    show martinez a_dressed_sides with dissolve
    martinez "{b}*вздыхая*{/b}"
    show martinez f_eyeroll at unflip
    show martinez at Position (xpos=300)
    with dissolve
    martinez "{b}Моя мама{/b} убирает в доме {b}по четвергам{/b}."
    show martinez f_normal
    show player 10
    player_name "А, почему?"
    show player 5
    show martinez f_angry_talk a_dressed_crossed with dissolve
    martinez "... Потому что ты ей платишь?"
    martinez "Ты что, совсем дурак, что ли?"
    show martinez f_angry
    show player 10
    player_name "Нет."
    player_name "Я просто не знал, что в доме есть горничная."
    show player 5
    show martinez f_angry_talk
    martinez "Теперь знаешь."
    show martinez f_angry
    pause
    show martinez f_normal_talk at flip
    show martinez at Position (xpos=750)
    with dissolve
    martinez "Ya te puedo ir? (Я могу идти?)"
    show martinez f_normal
    show consuela f_normal_talk
    consuela "Sí, pero vete a la casa. (Да, иди домой.)"
    consuela "No puedes estar aquí ahora que la casa tiene un dueño..(Ты не можешь быть здесь сейчас, когда в доме есть владелец..)"
    show consuela f_normal
    show martinez f_eyeroll
    martinez "Пфф, ладно."
    show martinez f_normal_talk
    martinez "Я ухожу."
    show martinez f_normal at unflip
    show martinez at Position (xpos=300)
    with dissolve
    show player 10
    player_name "Подожди секундочку."
    show player 5
    pause
    show player 10
    player_name "Она называла тебя {b}Камилой{/b}?"
    show player 5
    show martinez f_angry_talk
    martinez "Да, и что?"
    show martinez f_angry
    show player 401
    player_name "Красивое имя."
    show player 403
    show martinez f_angry_talk a_dressed_sign with dissolve
    martinez "Ччч, да пошел ты, задница!"
    show martinez f_angry a_dressed_crossed with dissolve
    show player 10
    player_name "Блин, я просто пытаюсь быть милым..."
    show player 13
    show martinez f_angry_talk
    martinez "Да, как стерва."
    hide martinez with dissolve
    show player 13f with dissolve
    pause
    show player 5f
    player_name "( У этой цыпочки серьезные проблемы с гневом... )"
    show player 5 with dissolve
    consuela "..."
    show player 3 with dissolve
    player_name "..."
    pause
    show consuela f_normal_talk
    consuela "{b}*гм*{/b} Debería volver al trabajo. (Я должна вернуться к работе.)"
    show consuela f_normal
    show player 29
    player_name "Простите, я не понимаю."
    show player 3
    show consuela f_unsure
    consuela "Эхх... Теперь я прибираюсь."
    consuela "¿Sí? (Да?)"
    show consuela f_normal
    show player 10
    player_name "О, да."
    player_name "Эээ, т.е. ... Sí!"
    show player 14
    player_name "Спасибо, {b}Консуэла{/b}."
    show player 13
    show consuela f_unsure
    consuela "Пожалуйста, мистер {b}[firstname]{/b}."
    hide player
    hide consuela
    with dissolve
    return

label beach_house_entrance_mysterious_statue_3:
    scene expression player.location.background_blur with None
    show player 5 at left
    show consuela f_unsure
    with dissolve
    consuela "Ой, простите... Мистер {b}[firstname]{/b}."
    show consuela f_normal
    player_name "Хмм?"
    show player 10
    player_name "О, привет {b}Консуэла{/b}."
    show player 5
    show consuela f_normal_talk a_dressed_statue with dissolve
    consuela "Я нашла."
    show consuela f_normal
    show player 11
    player_name "!!!"
    show player 10
    player_name "Ты нашла это?"
    show player 11
    show consuela f_normal_talk
    consuela "Sí, я нашла."
    show consuela f_normal
    show player 14
    player_name "Это похоже на последний кусочек статуи!"
    player_name "Тот, который принадлежал {b}дедушке Клайда{/b}."
    player_name "Это было в доме?"
    show player 13
    show consuela f_unsure
    consuela "Эээ..."
    consuela "Я нашла... под кроватью."
    consuela "Вы хотите?"
    show consuela f_normal
    show player 14
    player_name "О, да, пожалуйста."
    show consuela a_dressed_hips
    show player 714
    with dissolve
    pause
    show player 714b
    player_name "Спасибо, {b}Консуэла{/b}."
    show player 714
    show consuela f_laugh
    consuela "Пожалуйста, мистер {b}[firstname]{/b}."
    hide consuela with dissolve
    consuela "No dormiría aquí con cosas tan extrañas debajo de la cama ... (Я бы не спала здесь с такими странными вещами под кроватью ...)"
    player_name "( Хмм. )"
    player_name "( Интересно, как он попал под кровать? )"
    pause
    player_name "( Ну, неважно... Теперь у меня есть все три части. )"
    pause
    player_name "( Держу пари, {b}Диана{/b} заинтересовалась бы этой статуей. )"
    player_name "( {b}Я должен показать ее ей в следующий раз, когда буду работать у нее{/b}. )"
    hide player with dissolve
return

label beachhouse_not_bought:
    scene expression player.location.background_blur
    show player 3 at left
    player_name "Эх... ключа то нету..."
    show player 4 at left
    player_name "Хмм... Этот домик продаётся..."
    show player 1 at left with dissolve
    player_name "Можно попытаться накопить из тех денег, которые {b}Тётя Диана{/b} мне платит..."
    with dissolve
    return

label beach_house_first_time:
    scene expression player.location.background_blur
    show player 14
    with dissolve
    player_name "Ух ты! Прекрасный домик!"
    player_name "И так много места!"
    show player 1
    pause
    show player 14
    player_name "Не верю что сейчас он мой!"
    show player 1
    pause
    show player 14
    player_name "Наверное надо начать поиски {b}мебели{/b}."
    player_name "... Тогда тут будет идеально!"
    return

label beachhouse_weekday_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Надо готовиться идти в школу... )"
    hide player with dissolve
    return

label beachhouse_weekend_just_wokeup:
    scene expression L_beachhouse_bedroom.background_blur
    show player 7 with dissolve
    player_name "{b}*Зевает*{/b}"
    show player 8
    window hide
    pause
    show player 9
    player_name "( Надо за выходные что нибудь сделать... )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
