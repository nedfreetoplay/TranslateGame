label bissette_dialogue_meet_in_office:
    show player 10 at left
    show teacher 1 at right
    with dissolve
    player_name "{b}Мисс Биссетт{/b}, что мне нужно сделать?"
    show player 5
    show teacher 12
    bis "Ох, {b}[firstname]{/b}. Не здесь. {b}Приходи ко мне в мой кабинет после школы{/b}, хорошо?"
    show teacher 13
    show player 14
    player_name "Хорошо, Я встречу вас там."
    return

label bissette_dialogue_check_dictionary:
    show teacher 1 at right
    show player 10 at left
    with dissolve
    player_name "Привет, {b}Мисс Биссетт{/b}. Я нашел словарь в библиотеке, но в нем отсутствует несколько страниц."
    show player 239_240 with dissolve
    pause
    show player 503 with dissolve
    pause
    show player 5
    show teacher 22b
    with dissolve
    bis "Вот это да!"
    bis "Я думаю, это усложнит задачу."
    bis "Французско-английский раздел не поврежден, но вы пропустете много слов..."
    bis "Я боюсь, что некоторые из них могут иметь решающее значение для субъектов, которые мы должны изучить."
    show teacher 21b
    show player 10
    player_name "Фу, я боялся, что.."
    show player 5
    show teacher 21
    bis "Хм, возможно, не всё потеряно. Я уверена, что {b}ваши одноклассники{/b} будет готовы позволить вам копировать недостающие страницы из их словаря."
    bis "Можно использовать {b}ксерокс в компьютерном классе{/b}."
    show teacher 22
    show player 14
    player_name "Хорошая идея!"
    show player 13
    show teacher 2 with dissolve
    bis "{i}Добро пожаловать{/i}, {b}[firstname]{/b}."
    bis "Не забудьте получить английские слова, начинающиеся с буквы 'B' для нашего следующего урока."
    show teacher 1
    show player 14
    player_name "Хорошо, есть время найти другой словарь..."
    show player 13
    show teacher 12
    bis "Задание очень сложное. Я могу сказать, вы желаете специальную награду, очень большую, да?"
    show teacher 13
    show player 10
    player_name "Есть ли идея о том, чей словарь я могу одолжить?"
    show player 13
    show teacher 11
    bis "хмм..."
    show teacher 2
    bis "Возможно {b}Джудит{/b}?"
    bis "Она имеет большой талант во французском языке..."
    show teacher 1
    show player 14
    player_name "Хорошо, Я начну с {b}Джудит{/b}."
    return

label bissette_dialogue_intro:
    show player 1 at left
    show teacher 2 at right
    with dissolve
    bis "Привет, {b}[firstname]{/b}!"
    show player 17 at left
    show teacher 1 at right
    player_name "Привет, {b}Мисс Биссетт{/b}!"
    show player 1 at left
    show teacher 2 at right
    bis "У вас удалось достичь учебную программу?"
    bis "Я действительно надеюсь, что вы это сделайте!"
    bis "Теперь, есть ли что-то, о чем бы вы хотели поговорить?"
    show teacher 1
    return

label bissette_dialogue_food_assignment_intro:
    show player 10
    player_name "Какое мое следующее задание?"
    show player 5
    show teacher 2
    bis "Я хочу, чтобы вы {b}написали несколько абзацев о вашей любимой пищи, {i}на французском{/i}{/b}."
    bis "Тогда мы рассмотрим это вместе, да?"
    show teacher 1
    show player 14
    player_name "Ох, да!"
    return

label bissette_dialogue_food_assignment_prepare_assignment:
    player_name "Я должен снова посетить этого библиотекаря. Может быть, она могла бы найти книгу о {b}французской кухни{/b} для меня."
    player_name "Тогда я могу ввести что-то на моем компьютере."
    player_name "Спасибо, {b}Мисс Биссетт{/b}!"
    return

label bissette_dialogue_food_assignment_do_assignment:
    player_name "Я должен набрать что-то на моем компьютере."
    player_name "Спасибо, {b}Мисс Биссетт{/b}!"
    return

label bissette_dialogue_poem_assignment_intro:
    show player 10
    player_name "Напомните мне, что было задано?"
    show player 5
    show teacher 2
    bis "{i}Что? Вы уже забыли{/i}?"
    bis "{b}Вы должны писать романтические стихотворение {i}на Французском{/i}{/b}!"
    show teacher 1
    show player 14
    player_name "Ох, конечно!"
    player_name "Спасибо, {b}Мисс Биссетт{/b}."
    show player 13
    show teacher 2
    bis "Вернитесь ко мне, как только это будет завершено."
    bis "Не заставляйте меня ждать, {i}мой красивый мужчина{/i}."
    return

label bissette_dialogue_poem_assignment_do_assignment:
    show player 14
    player_name "Я должен набрать что-то на моем компьютере."
    return

label bissette_dialogue_poem_assignment_print_assignment:
    show player 14
    player_name "Я закончил стихотворение, {b}Мисс Биссетт{/b}."
    show player 13
    show teacher 2
    bis "Отлично, дай мне посмотреть!"
    show teacher 1
    show player 10
    player_name "Ох, во первых мне нужно распечатать..."
    show player 5
    show teacher 2
    bis "Хорошо, принтер находится в {b}Компьютерном классе{/b}, помнишь?"
    show teacher 1
    show player 14
    player_name "Ага, сейчас вернусь!"
    return

label bissette_dialogue_private_tutoring:
    show player 10
    player_name "Как вы думаете, мы могли бы встретиться в вашем офисе сегодня вечером?"
    show player 26
    player_name "Вы знаете, для некоторых... Обучение?"
    show player 13
    show teacher 12
    bis "О, репетиторство. Да!"
    bis "Тогда увидимся сегодня вечером, {i}Да{/i}?"
    show teacher 13
    show player 33
    player_name "{i}Да{/i}!"
    show player 13
    show teacher 12
    bis "{i}Очень хорошо, мой красивый мужчина{/i}!"
    return

label bissette_dialogue_tutoring:
    show player 10
    player_name "Мне было интересно, если вы все еще предлагаете частное репетиторство?"
    show player 5
    show teacher 3
    bis "Ох, {i}Конечно{/i}!"
    show teacher 1
    show player 14
    player_name "Замечательно! Когда вы будете свобод-"
    show player 11
    show teacher 2
    bis "Импрессионнант! Вы первый студент, кто узнал о репетиторстве!"
    show teacher 1
    show player 12
    player_name "Серьезно? Это странно..."
    show player 5
    show teacher 5
    bis "Я начинаю думать, что никто не был заинтересован в специальной награды."
    show teacher 1
    show player 12
    player_name "О да, я уже забыл о специальной награды..."
    show player 5
    show teacher 5
    bis "{i}Какой{/i}!? Вы не желая вознаграждения?!"
    show teacher 4
    show player 29 with dissolve
    player_name "Эмм... нет, Я имею в виду... Специальная награда звучит замечательно, {b}Мисс Биссетт{/b}."
    show player 3
    show teacher 3
    bis "А великолепно!"
    show teacher 2
    bis "Тогда мы будем встречаться после школы, для кого-то на одном уроке, Хорошо?"
    show teacher 1
    show player 10 with dissolve
    player_name "Эм... Да, Я думаю, что будет-"
    show player 11
    show teacher 2
    bis "{i}Три скважины{/i}!"
    bis "Просто не забудьте принести ваш {b}французский словарь {/b}."
    show teacher 1
    show player 24
    player_name "А, чёрт. О том, что... {b}Мисс Биссетт{/b}, Я не могу найти свой {b}Французский словарь{/b}."
    show player 25
    player_name "Его нет в моем рюкзаке, моем доме, или в моем шкафчике..."
    show player 5
    show teacher 5
    bis "Ох, нет, это не хорошо!"
    bis "Возможно, вам следует {b}зайти в библиотеку{/b} и посмотреть, если ли у них?"
    show teacher 2
    bis "Я бы одолжила вам мое, но я боюсь, что я недавно пролила вино на него."
    show teacher 1
    show player 14
    player_name "О да, я забыл о библиотеке!"
    show player 13
    show teacher 2
    bis "Oui, Я сама хожу туда довольно часто."
    show teacher 12
    bis "Я люблю чувствовать хорошие книги в моих руках."
    bis "Обнимались теплым огнем с некоторым крепким вином..."
    bis "{i}Это рай{/i}."
    show teacher 13
    show player 11
    player_name "..."
    show teacher 2
    bis "Ох, глупая я, мечты мои. Просто дайте мне знать, когда у вас будет словарь, Хорошо?"
    show teacher 1
    show player 14
    player_name "Хорошо, {b}Мисс Биссетт{/b}."
    return

label bissette_dialogue_get_dictionary:
    show player 12
    player_name "Напомни мне, что мне нужно получить, прежде чем мы сможем учиться вместе?"
    show player 5
    show teacher 2
    bis "Вам понадобится словарь с французского на русский."
    bis "{b}Проверьте библиотеку{/b}, Хорошо?"
    show teacher 1
    show player 14
    player_name "Ох, конечно!"
    player_name "Спасибо!"
    return

label bissette_dialogue_replace_missing_pages:
    show player 12
    player_name "Что я должен был сделать вновь?"
    show player 5
    show teacher 2
    bis "Скопируйте недостающие страницы из словаря одноклассников."
    show teacher 1
    show player 14
    player_name "Ох, конечно!"
    show player 13
    show teacher 2
    bis "Поговори с {b}Джудит{/b}. У неё очень хороший французский."
    show teacher 1
    show player 14
    player_name "И потом {b}В Компьютерном классе имеется копировальный аппарат{/b}..."
    player_name "Хорошо, еще раз спасибо!"
    return

label bissette_dialogue_chat:
    show player 29 at left
    show teacher 1 at right
    player_name "{b}Мисс Биссетт{/b}, Я просто хотел сказать, что я действительно ценю вашу помощь с домашним заданием!"
    show player 13 at left
    show teacher 3 at right
    bis "С удовольствием! Все, что я хочу, это убедиться, что вы мотивированы выполнять..."
    show teacher 12 at right
    bis "...И я люблю награждать трудолюбивых студентов!"
    show teacher 13 at right
    show player 10 at left
    player_name "Я сделаю все возможное. Я очень хочу поступить в хороший колледж..."
    show teacher 2 at right
    show player 13 at left
    bis "Именно это я и хочу от вас слышать!"
    bis "Я могу рассмотреть ваше {b}домашнее задание{/b} с вами, когда вы принесете его, если хотите!"
    show teacher 1 at right
    show player 17 at left
    player_name "Звучит неплохо, {b}Мисс Биссетт{/b}! Спасибо вам!"
    return

label bissette_dialogue_leave:
    show player 14
    player_name "Нет. Я просто хотел поздороваться."
    show teacher 2
    show player 13
    bis "Что ж, присаживайтесь. Занятие скоро начнется!"
    show teacher 3
    bis "На сегодня у меня запланирован увлекательный урок!"
    show teacher 1
    show player 2
    player_name "Звучит отлично, {b}Мисс Биссетт{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
