label kim_button_dialogue_intro:
    show player 13 at left
    show kim 2 at right
    with dissolve
    kim "Привет!"
    kim "Что я могу сделать для вас что бы вы смогли получить ваш новый автомобиль сегодня?"
    show kim 1
    show player 10
    player_name "Ох, эммм..."
    show player 4 with dissolve
    return

label kim_button_dialogue_button:
    show player 14 with dissolve
    player_name "Мне нравятся ваш значок."
    player_name "Ты поклоник {b}Мэра Рампа{/b}?"
    show player 13
    show kim 2
    kim "Ох, {b}Мэр Рамп{/b} номер 1, лучший мэр."
    kim "Он и {b}Ким{/b} хорошие друзья!"
    show kim 3
    show player 10
    player_name "Ты дружишь с {b}Мэром Рампом{/b}?"
    show player 13
    show kim 2
    kim "Да, Я помогаю ему с его политикой взамен на финансирование."
    show kim 6 with dissolve
    kim "Тогда я взойду на мой трон!"
    show kim 3 with dissolve
    show player 10
    player_name "... Трон?"
    show player 5
    show kim 2
    kim "Да!"
    kim "Когда я стану главой этого автосалона, Я построю мощьную империю."
    show kim 5 with dissolve
    kim "Уах ха ха ха!"
    show player 12
    player_name "Ну, удачи со всем этим..."
    show player 5
    show kim 2 with dissolve
    kim "Она мне не нужна.."
    hide kim with dissolve
    show player 10
    player_name "Хммм, почему же наш {b}Мэр{/b} общается с этим парнем?"
    show player 12
    player_name "... Странно."
    hide player with dissolve
    return

label kim_button_dialogue_browsing:
    show player 14 with dissolve
    player_name "Я только пришел сюда что бы посмотреть."
    show player 13
    show kim 2
    kim "Хмммм, посмотреть, мм?"
    kim "Очень хорошо."
    kim "... Но если ты захочешь что то купить, Ты должен поговорить со мной и не с кем другим!"
    kim "Ты понял?!"
    show kim 1
    show player 10
    player_name "Ухх, да..."
    player_name "Само собой."
    show player 5
    show kim 2
    kim "Хорошо."
    kim "Я буду следить за тобой!"
    hide kim
    hide player
    with dissolve
    return

label kim_button_dialogue_sign:
    show player 14 with dissolve
    player_name "Это ты на значке?"
    show player 13
    show kim 5 with dissolve
    kim "Ох, ты заметил знак, мм?!"
    kim "Да, {b}Ким{/b} номер 1, лучший продавец машин!"
    kim "Вскоре, это место будет принадлежать мне."
    show kim 4
    show player 12
    player_name "Ох да?"
    show player 13
    show kim 6 with dissolve
    kim "Ох да... Я покарю это автосалон!"
    kim "Я распростряню его, по всему миру!"
    show player 11
    kim "Когда нибудь, Я покарю весь мир со своими автосалонами !!"
    show kim 3
    show player 3
    with dissolve
    player_name "..."
    show kim 5 with dissolve
    kim "Уах ха ха ха!"
    kim "Я буду автосолным БОГОМ!!!"
    show kim 4
    show player 10 with dissolve
    player_name "... Хорошо."
    player_name "Ну, Я пойду осмотрюсь..."
    show player 5
    show kim 2 with dissolve
    kim "Да, иди салага."
    kim "Найдешь меня если захочешь что то купить."
    hide kim with dissolve
    show player 12
    player_name "Какой странный парень."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
