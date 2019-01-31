label eve_classroom_dialogue_eve_intro:
    scene classroom
    show evedesk 1 at left
    with fade
    eve "Вау...Я думала, что ты  мертв!"
    show evedesk 2
    player_name "Что?... Что ты имеешь в виду?"
    show evedesk 1
    eve "Не знаю... Ты пропал на месяц, и люди начали выдумывать слухи о том, что твоя семья была убита или что-то вроде того..."
    show evedesk 3
    player_name "Ухх... Ничего подобного!"
    show evedesk 4
    eve "Я так и думала. Люди просто любят поговорить, а эта школа - просто шутка."
    eve "Я рада, что наш последний год почти закончился..."
    show evedesk 5
    player_name "Да, я знаю, что ты имеешь в виду."
    show evedesk 6
    eve "Тебе стоит как-нибудь потусоваться с нами в {b}парке{/b}... Без всех этих идиотов из школы и расслабляешся, понимаешь?"
    show evedesk 5
    eve "Приходи {b}ночью{/b}... в это время мы тусим там."
    player_name "Эхх... Думаю, я могу прийти как-нибудь ночью."
    show evedesk 6
    eve "Зависит только от тебя. Если захочешь - приходи!"
    show evedesk 4
    eve "О, ты слышал объявление {b}Мисс Биссетт{/b} о специальном вознаграждении?"
    show evedesk 1
    eve "Или ты проспал эту часть?"
    show evedesk 3
    player_name "Эй! Я проснулся... для этого."
    show evedesk 4
    eve "Интересно, какая будет награда."
    eve "Она не очень много об этом говорила. Наверное, что-то глупое."
    eve "Я уже делаю довольно хорошо, так что даже не стоит пытаться."
    show evedesk 2
    player_name "Почему?"
    show evedesk 6
    eve "Как улучшение от 4 до 5 даст мого возможностей?"
    eve "У тебя больше шансов выиграть..."
    show evedesk 5
    player_name "У меня?"
    show evedesk 1
    eve "Ну, да... ты движешься в правильном направлении, не так ли?"
    eve " У тебя есть много возможностей для улучшения."
    show evedesk 6
    eve "Плюс, {b}Мисс Биссетт{/b} мальчики нравятся больше."
    eve "Тебе стоит серьезно подумать об этом."
    hide evedesk with dissolve
    return

label eve_classroom_dialogue_intro:
    show evedesk 4 at left with dissolve
    eve "Привет, {b}[firstname]{/b}."
    show evedesk 5
    player_name "Привет, {b}Ева{/b}."
    show evedesk 4
    eve "Что случилось?"
    return

label eve_classroom_dialogue_talent_show_help:
    show evedesk 5
    player_name "Ты играешь на каких-нибудь инструментах?"
    show evedesk 4
    eve "Нет, я не играю. Я всегда хотел учиться, но у меня просто не было времени, понимаешь?"
    show evedesk 5
    player_name "Хорошо, а как насчет пения?"
    show evedesk 1
    eve "Ох, умм..."
    show evedesk 4
    eve "Да, мне нравится петь, наверное. Не знаю, насколько я хороша."
    show evedesk 5
    player_name "Я уверен в тебе! Ты должна участвовать в шоу талантов со мной!"
    show evedesk 3
    player_name "Нам действительно не хватает добровольцев."
    show evedesk 1
    eve "... Да, Я не знаю."
    eve "Ты хочешь, чтобы я пела перед всей школой? Звучит довольно неловко."
    eve "... И я не пела некоторое время. С тех пор, как сломалась моя караоке-машина."
    eve "Я давно не практиковалась."
    show evedesk 5
    player_name "Хмм..."
    player_name "Знаешь, у моего друга {b}Эрика{/b} есть {b}караоке-машина{/b} в подвале."
    show evedesk 4
    eve "О, правда?"
    show evedesk 5
    player_name "Точно! Приходи как-нибудь и потренируйся!"
    show evedesk 4
    eve "Ты хочешь, чтобы я спела для тебя и твоего друга?"
    show evedesk 5
    player_name "Нет, мы можем петь все вместе! Давай, сделаем это сегодня вечером, будет весело!"
    eve "..."
    show evedesk 4
    eve "Ладно, думаю, я могу зайти ненадолго."
    show evedesk 5
    player_name "Превосходно! {b}встретимся у Эрика дома{/b} ночью."
    return

label eve_classroom_dialogue_adehsive:
    show evedesk 5
    player_name "Какой план?"
    show evedesk 4
    eve "Ты должен встретиться с {b}Кевин{/b} в {b}научной лаборатории после занятий{/b}."
    eve "Помнишь?"
    show evedesk 5
    player_name "Ох, да точно. Спасибо, {b}Ева{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show evedesk 5
    player_name "Ты собираешься записаться на репетиторство к {b}Мисс Биссетт{/b}?"
    show evedesk 4
    eve "Я уже делаю довольно хорошо, так что даже не стоит пытаться."
    show evedesk 2
    player_name "Почему нет?"
    show evedesk 6
    eve "Как переход от 4 к 5 считается значительным улучшением?"
    eve "У тебя больше шансов выиграть..."
    show evedesk 5
    player_name "Я?"
    show evedesk 1
    eve "Ну, конечно... ты аутсайдер сейчас, не так ли?"
    eve " У тебя есть много возможностей для улучшения."
    show evedesk 6
    eve "Плюс, {b}Мисс Биссетт{/b} благоволит парням."
    eve "Тебе стоит серьезно подумать об этом."
    return

label eve_classroom_dialogue_hang_out:
    show evedesk 5
    player_name "Где, говоришь, ты проводишь время?"
    show evedesk 4
    eve "Мои друзья и {b}Я тусуемся в парке{/b}."
    eve "Просто убедитесь, что ты {b}пришел ночью{/b}... в это время мы всегда тусуемся там."
    show evedesk 5
    player_name "Хорошо. Я могу заскочить на одну ночь."
    show evedesk 6
    eve "Это зависит только от тебя. Делай как знаешь!"
    return

label eve_classroom_dialogue_leave:
    show evedesk 5
    player_name "Ничего, просто хотел поздороваться."
    show evedesk 4
    eve "О. Тогда поговорим позже."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
