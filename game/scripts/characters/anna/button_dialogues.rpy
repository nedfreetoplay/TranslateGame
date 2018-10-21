label anna_dialogue_anna_dog_hunt:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Привет {b}[firstname]{/b}, ты не видел {b}маленькую собачку{/b} без поводка??"
    show anna 4
    show player 10
    player_name "Вроде нет..."
    show anna 5
    show player 11
    anna "Я потеряла его."
    anna "Я бегала по тропинке в {b}лесу{/b}, и когда я оглянулась, то он пропал!!"
    show anna 4
    show player 10
    player_name "Ты искала его возле тропинки?"
    show anna 5
    show player 11
    anna "Конечно! Я смотрела везде!"
    anna "Но я не могу самостоятельно прочесать тропу и {b}лес{/b}..."
    show anna 4
    show player 10
    player_name "Как он выглядит?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Ах да, точно. Это {b}мопс{/b}, приблизительно вот такого размера!"
    show anna 5 at right
    anna "Его кличка {b}Awesomo{/b}."
    anna "Он немного толстоват, так что он не мог убежать далеко."
    anna "Пожалуйста! Ты мне поможешь найти его?"
    show anna 4
    return

label anna_dialogue_anna_dog_hunt_yes:
    show player 14
    player_name "Разумеется. Я поищу его."
    player_name "Есть то, что я должен знать о нем?"
    player_name "Что-то, что поможет мне найти его?"
    show player 1
    show anna 5
    anna "Ну... Он очень любит кушать {b}печеньки{/b}."
    anna "Если у тебя есть несколько, то я уверена что он их сможет унюхать и прибежать..."
    show anna 11
    show player 14
    player_name "Окей! Я приду к тебе, если найду его!"
    show anna 12
    show player 1
    anna "Огромное спасибо!"
    return

label anna_dialogue_anna_dog_hunt_no:
    show player 10
    player_name "Я хотел бы помочь, но у меня есть дела по важнее..."
    show player 11
    show anna 5
    anna "Ой, извини что побеспокоила тебя...."
    return

label anna_dialogue_anna_find_dog_have_dog:
    scene location_park_closeup
    show player 247 at left with dissolve
    show anna 4 at right with dissolve
    player_name "Угадай, кого я нашел?"
    show anna 5 with vpunch
    anna "!!!"
    show anna 12
    anna "{b}Awesomo{/b}!!!"
    show player 1
    show anna 9
    with dissolve
    anna "Где ты его нашел?!"
    show anna 8
    show player 14
    player_name "Он ушел далеко в лес по тропинке..."
    player_name "Вы были правы! Трюк с печеньками сработал."
    show anna 10
    show player 1
    anna "Спасибо тебе {b}большое{/b}!"
    show anna 9
    anna "Я обязательно с Вами расплачусь."
    show anna 7
    anna "Я должна отвезти его домой. Он наверное очень сильно проголодался."
    show anna 10
    anna "Увидимся позже!"
    return

label anna_dialogue_anna_find_dog_do_not_have_dog:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Вы уже нашли его??"
    show anna 4
    show player 10
    player_name "Пока нет..."
    player_name "Вы можете мне описать его, еще раз? И повторите, где его можно поискать?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Он вот такого размера и он {b}мопс{/b}!"
    show anna 5 at right
    anna "Потерялся он вдоль тропинки в {b}лес{/b}..."
    anna "...и он обожает {b}печенюшки{/b}!"
    anna "Может быть, вы могли бы использовать {b}печенюшки{/b} чтобы выманить его."
    show anna 11
    show player 14
    player_name "Хорошо! Пойду поищу его!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
