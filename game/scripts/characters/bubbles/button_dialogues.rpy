label bubbles_button_intro:
    scene movie_lobby with None
    show bubbles f_normal_talk o_desk at flip
    show player at flip
    with dissolve
    bub "Добро пожаловать в {b}Кинотеатр Saga{/b}, меня зовут {b}Бабл{/b}."
    bub "Чем могу помочь?"
    show bubbles f_normal
    return

label bubbles_movie_select_pre:
    show player f_normal_talk
    player_name "Я бы хотел посмотреть фильм."
    show player f_normal
    show bubbles f_normal_talk
    bub "Конечно."
    bub "Билет стоит {b}50 долларов{/b} и все, что вам нужно сделать, это выбрать тот, который вы хотите посмотреть..."
    show bubbles f_normal
    show player f_normal_talk
    player_name "Клево!"
    show player f_normal
    return

label bubbles_button_nevermind:
    show player f_normal_talk
    player_name "Я просто осматриваюсь, спасибо."
    show player f_normal
    show bubbles f_normal_talk
    bub "Хорошо."
    bub "Просто дай мне знать, если захочешь что-нибудь посмотреть."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
