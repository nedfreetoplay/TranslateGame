label helen_dialogue_mia_route:
    show helen 50 at right
    show player 14 at left
    with dissolve
    player_name "Добрый день, {b}Хелен{/b}."
    show player 13
    show helen 51
    helen "Здравствуй, {b}[firstname]{/b}."
    show helen 50
    show player 14
    player_name "Как идут дела в последнее время?"
    show player 13
    show helen 51
    helen "Куда лучше."
    helen "С осознанием того, что я очищена, жить куда легче."
    helen "Церковь очень помогла мне восстановить отношения с {b}Гарольдом{/b}."
    show helen 24
    helen "Но... никто не должен знать, как это происходило."
    show helen 50
    show player 21
    player_name "Хех... Да, я понимаю."
    show player 29
    show xtra 21 at left
    with dissolve
    player_name "It's a bit of a blur, for me..."
    show player 13
    hide xtra 21
    with dissolve
    show helen 51
    helen "Ещё раз спасибо за твою помощь. Наша семья глубоко ценит то, что ты сделал... и от чего отказался."
    helen "Тебе пора. Наверное, ты хочешь пообщаться с {b}Мией{/b}."
    show helen 50
    show player 14
    player_name "Да."
    show player 36 with dissolve
    player_name "До встречи!"
    return

label helen_dialogue_helen_end_intro:
    show player 13 at left
    show helen 63 at right
    with dissolve
    helen "Здравствуйте, {b}[firstname]{/b}."
    show helen 62
    show player 14
    player_name "Привет, {b}Хелен{/b}."
    show player 13
    show helen 63
    helen "Вы пришли очистить мое греховное тело?"
    show helen 62
    return

label helen_dialogue_helen_end_leave:
    show player 10
    player_name "Спасибо, {b}Хелен{/b}..."
    player_name "Но, в другой раз."
    show player 12
    player_name "У меня... есть неотложные дела."
    show player 5
    show helen 48
    helen "Оу..."
    helen "Я так надеялась обслужить вас..."
    helen "Не забывайте обо мне, приходите почаще."
    show helen 47
    show player 12
    player_name "Конечно... Я дам тебе знать, {b}Хелен{/b}."
    return

label helen_dialogue_helen_end_sex:
    show player 26
    player_name "Да."
    show player 13
    show helen 63
    helen "Слава {b}Богу{/b}!"
    helen "Я молилась о том, чтобы вы поскорее вернулись."
    helen "Снимайте одежду и дайте мне вкусить божественного света."
    helen "Затем лягте на спину и позвольте благодати {b}Господа{/b} воссиять на мне."
    hide helen
    scene mia_house_helen_window1
    show player helen_sex 59
    with fade
    pause
    scene mia_house_helen_window2
    show player helen_sex 59
    pause
    scene mia_house_helen_window3
    show player helen_sex 59
    show helen 54 with dissolve
    return

label helen_dialogue_change_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Хелен{/b}!"
    show player 5
    helen "..."
    show helen 3
    helen "Привет, {b}[firstname]{/b}."
    show helen 1
    show player 12
    player_name "Выглядишь куда лучше!"
    show player 5
    show helen 2
    helen "Я пытаюсь... открыться... в том числе и тебе."
    show helen 1
    show player 14
    player_name "Это здорово."
    show player 13
    show helen 2
    helen "Что тебе нужно?"
    show helen 1
    return

label helen_dialogue_change_harold:
    show player 10
    player_name "Ты говорила с {b}Гарольдом{/b}?"
    show player 11
    show helen 4
    helen "Нет..."
    show helen 3
    helen "...На все воля {b}Божья{/b}."
    show helen 1
    show player 12
    player_name "Что?"
    show player 5
    show helen 4
    helen "Тебе пора идти..."
    return

label helen_dialogue_change_mia_clues:
    show player 10
    player_name " Как мне найти {b}Гарольда{/b}?"
    show player 5
    show helen 24 with dissolve
    helen "Начни с опроса его коллег в {b}полицейском участке{/b}..."
    helen "...и поищи {b}зацепки{/b} на его рабочем месте."
    show helen 23
    show player 12
    player_name "Я опрошу всех, кого смогу..."
    show player 5
    show helen 24
    helen "Спасибо..."
    return

label helen_dialogue_change_corset:
    show player 10
    player_name "Еще раз, какое бельё тебе нужно?"
    show player 5
    show helen 28
    helen "Я давно хотела купить корсет... и {b}Гарольд{/b} говорил, что мне идет красный цвет."
    show helen 23
    show player 12
    player_name "Итак, {b}красный корсет{/b}?"
    show player 5
    show helen 24
    helen "Если найдешь такой, принеси его мне."
    show helen 23
    show player 10
    player_name "Я попробую..."
    show player 5
    show helen 28
    helen "Спасибо, {b}[firstname]{/b}."
    return

label helen_dialogue_change_angelica:
    show player 10
    player_name "Как проходят обряды?"
    player_name "У вас есть прогресс с {b}Сестрой Анжеликой{/b}?"
    show player 5
    show helen 27
    helen "..."
    show helen 24
    helen "Я... Я думаю, все хорошо..."
    show helen 28
    helen "...{b}Сестра Анжелика{/b} более... совершенна и образована, нежели я."
    show helen 23
    show player 10
    player_name "Понял..."
    player_name "Ну, дайте знать, если понадоблюсь!"
    return

label helen_dialogue_change_whipping:
    show player 10
    player_name "Все в порядке? Я до сих пор не могу поверить, что {b}Сестра Анжелика{/b} отхлестала вас."
    show player 5
    show helen 25
    helen "..."
    show helen 28
    helen "Все ещё немного больно, но..."
    show helen 24
    helen "...Я грешница, {b}[firstname]{/b}. Я... Я это заслужила."
    show helen 28
    helen "Если таким образом освобождаются от греховных пут, я должнна пройти через это."
    show helen 27
    show player 37 with dissolve
    player_name "..."
    show player 10 with dissolve
    player_name "Это хорошо, наверное."
    player_name "Если понадобится помощь - зовите меня."
    player_name "Я всегда к вашим услугам."
    show player 5
    show helen 24
    helen "Thanks, {b}[firstname]{/b}. Ты и так во многом помогаешь."
    helen "{b}Сестра Анжелика{/b} помогает мне осознать, что во всех жизненных неудачах виной лишь моя греховность."
    helen "Я должна пройти через это, и, может быть я стану такой же доброй и полезной людям... как ты."
    show helen 27
    show player 37 with dissolve
    player_name "{b}Хелен{/b}..."
    show helen 23
    show player 10 with dissolve
    player_name "Я не считаю вас плохой."
    show player 5
    show helen 28
    helen "Спасибо, {b}[firstname]{/b}."
    return

label helen_dialogue_change_ritual:
    show player 10
    player_name "Знаете... Я начал чаще посещать церковь..."
    show player 5
    show helen 2
    helen "...правда?"
    show helen 1
    show player 14
    player_name "Да!"
    show player 10
    player_name "Я стараюсь узнать больше... ну знаете... о {b}Боге{/b} и всём таком!"
    show player 5
    show helen 2
    helen "Хмм... Серьезно?"
    show helen 1
    show player 12
    player_name "А вы знаете, что... ночью совершают особое таинство?"
    show player 5
    show helen 4
    helen "Ночное богослужение?"
    show helen 1
    show player 10
    player_name "Да! Это вроде... ритуала."
    show player 5
    show helen 4
    helen "Я никогда не слышала ни о чем подобном, хотя посещаю церковь уже 20 лет."
    show helen 2
    helen "Почему же я никогда не слышала об этом... таинстве?"
    show helen 1
    return

label helen_dialogue_change_ritual_stat_fail:
    show player 10
    player_name "[chr_warn]Ну я это, эммм... Я и не знаю, как это объяснить..."
    show player 5
    show helen 4
    helen "[chr_warn]Похоже ты смеёшься надо мной..."
    show helen 1
    show player 24
    player_name "[chr_warn]..."
    show player 25
    player_name "[chr_warn]Ну я узнал про это совсем недавно, так что не знаю до конца что да как."
    show player 24
    show helen 4
    helen "[chr_warn]Я совсем не поняла твой посыл..."
    show helen 2
    helen "[chr_warn]...но удачи тебе в твоих начинаниях, и дай знать если разузнаешь про это подробнее."
    show helen 1
    show player 25
    player_name "[chr_warn]Оу... Ладно."
    return

label helen_dialogue_change_ritual_stat_pass:
    show player 12
    player_name "Я узнал от {b}Сестры Анжелики{/b}!"
    player_name "Она попросила меня распостранить информацию и найти... эмм... несколько благочестивых прихожан!"
    show player 14
    player_name "Я знаю, что вы очень набожны..."
    show player 33
    player_name "И вы уже 20 лет посещаете церковь. Я даже удивлен, что вы никогда не слышали о ночных таинствах. Может я-"
    show helen 4
    helen "Постой."
    show helen 1
    show player 13
    player_name "..."
    show helen 4
    helen "Ты сам-то там бывал?"
    show helen 1
    show player 14
    player_name "Скажем так... Мне нравится помогать при храме!"
    show player 13
    show helen 2
    helen "Хочу сказать, что я приятно удивлена твоим интересом к церковной жизни..."
    show helen 4
    helen "...но я не совсем понимаю, для чего нужны эти богослужения."
    show helen 1
    show player 14
    player_name "{b}Сестра Анжелика{/b} говорит, что это прекрасная возможность искупить грехи покаянием..."
    show player 13
    show helen 3
    helen "Хмм..."
    show helen 2
    helen "Мне нужно придти ночью?"
    show helen 1
    show player 14
    player_name "Да, мэм! Оно проходит... в монашеской келье!"
    show player 13
    show helen 3
    helen "Ладно, ты меня убедил."
    show helen 2
    helen "Я навещу {b}Сестру Анжелику{/b} ночью и увижу как проходят такие богослужения..."
    show helen 1
    show player 14
    player_name "Прекрасно!"
    return

label helen_dialogue_intro:
    show helen 1 at right
    show player 10 at left
    with dissolve
    player_name "Добрый день, {b}Хелен{/b}!"
    show player 5
    show helen 4
    helen "Опять ты."
    helen "Что тебе нужно?!"
    show helen 1
    return

label helen_dialogue_harold:
    show player 10
    player_name "Ты поговорила с {b}Гарольдом{/b}?"
    show player 11
    show helen 5
    helen "Это не твое дело."
    show helen 4
    helen "К тому же, здесь ничего не поделаешь..."
    show helen 3
    helen "...ибо на все воля {b}Божья{/b}!"
    show helen 1
    show player 12
    player_name "Что?"
    show player 5
    show helen 4
    helen "Тебе пора идти..."
    return

label helen_dialogue_leave:
    show player 5 at left
    show helen 2 at right
    with dissolve
    helen "!!!"
    show helen 4
    helen "Что ты здесь делаешь?!"
    show player 22
    helen "Это моя комната! Выметайся!!"
    show helen 6
    show player 10
    player_name "Простите!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
