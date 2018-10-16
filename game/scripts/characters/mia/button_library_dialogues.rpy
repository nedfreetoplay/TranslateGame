label mia_library_dialogue_bissette_find_poem_reference_book:
    show player 14 at left
    show mia 7 at right
    with dissolve
    player_name "Привет, {b}Mia{/b}! Что ты делаешь?"
    show player 13
    show mia 10
    mia "Ох, приветик, {b}[firstname]{/b}! Я только собиралась подготовиться к предстоящему тесту по химии."
    show mia 7
    show player 12
    player_name "Я думал что твоя мама не позволяет тебе что то делать после школы?"
    show player 13
    show mia 12
    mia "Она обычно не разрешает но..."
    show mia 10
    mia "Я сказала ей что{b}Miss Okita{/b} может написать мне рекоминдацию в колледж если я впечатлю её постаравшись хорошо на нашем следующем тесте."
    show mia 7
    player_name "А она и вправду это сделает?"
    show mia 10
    mia "Вряд ли но попытка не пытка, правда?"
    mia "И я вообще то смогу провести время с {b}Judith{/b} на улице!"
    show mia 7
    show player 14
    player_name "Да Пожалуй."
    show player 13
    show mia 10
    mia "Что ты здесь делаешь?"
    show mia 7
    show player 14
    player_name "{b}Miss Bissette{/b} дала мне задание. Я думал может я смогу найти здесь немного вдохновления."
    show player 13
    show mia 10
    mia "Ох да? Какое задание?"
    show mia 7
    show player 10
    player_name "Ну это немного неловко..."
    show player 5
    show mia 9
    mia "хехе, серьезно?! Что ж, тогда ты должен мне рассказать!"
    show mia 7
    show player 10
    player_name "*Вздох* Я должен написать романтическую поэму на французком."
    show player 5
    show mia 10
    mia "Это не неловко!"
    show mia 7
    show player 12
    player_name "Нет?"
    show player 5
    show mia 10
    mia "Нет!Мы должны это сделать!"
    show mia 12
    mia "Что ж, все кроме {b}Roxxy{/b}... Она никогда не делала свою домашку."
    show mia 7
    show player 14
    player_name "Я не знал.А твоя поэма о чем?"
    show player 13
    show mia 12
    mia "Ох, Я..."
    show mia 56 with dissolve
    mia "...Ты знаешь, то и это, хехе..."
    show mia 55
    show player 14
    player_name "Ага! Видишь, это неловко!"
    show player 13
    show mia 10 with dissolve
    mia "Да, Я думаю немного."
    show mia 7
    show player 10
    player_name "Я даже не знаю с чего начать писать эту штуку!"
    player_name "Возможно мне стоить поискать книгу по {b}Французкой романтике{/b}..."
    show player 13
    show mia 10
    mia "Ты знаешь, {b}Judith{/b} и я нашли одну неплохую."
    show mia 7
    show player 10
    player_name "Ох серьезно?"
    show player 13
    show mia 10
    mia "Да, и там все хорошо прорисовано..."
    show mia 7
    show player 12
    player_name "Ты помнишь как она называется?"
    show player 13
    show mia 12
    mia "Хмм, нет, не совсем."
    show mia 10
    mia "У {b}Judith{/b} она была в последний раз. Она пользовалась ей {b}в кладовке{/b} там,я думаю."
    show mia 7
    show player 10
    player_name "Хм, ты думаешь она уже вышла от туда?"
    show player 13
    show mia 10
    mia "Может быть."
    show mia 7
    show player 14
    player_name "Я думаю мне надо пойти посмотреть тогда. Спасибо за помощь, {b}Mia{/b}!"
    show player 13
    show mia 10
    mia "Без проблем! Удачи, {b}[firstname]{/b}!"
    show mia 7
    show player 14
    player_name "Тебе тоже!"
    return

label mia_library_dialogue_bissette_mia_book_feedback:
    show mia 10 at right
    show player 13 at left
    with dissolve
    mia "Есть успехи в поисках?"
    show mia 7
    show player 10
    player_name "Да, я нашел её..."
    show player 14
    player_name "Ты не шутила она и в правдуу очень хорошо нарисована!"
    show player 13
    show mia 56 with dissolve
    mia "...Да."
    show mia 55
    show player 10
    player_name "Интересно что {b}Judith{/b} делала с ней что до сих пор не вернула её сама"
    show player 5
    show mia 56
    mia "Хех, Д-дааа, Я не знаю..."
    mia "...Мне на самом деле нужно возвращаться к учебе."
    show mia 55
    show player 14
    player_name "Ах да!Извини!"
    player_name "Спасибо еще раз, {b}Mia{/b}."
    show player 13
    show mia 56
    mia "Без проблем, {b}[firstname]{/b}."
    hide mia with dissolve
    show player 14
    player_name "Отлично, лучше возьму её к себе домой к {b}моему компьютеру{/b} и начну писать поэму для {b}Miss Bissette{/b}."
    return

label mia_library_dialogue_do_not_disturb:
    show player 10 with dissolve
    player_name "Нет, Я должен дать ей спокойно учиться..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
