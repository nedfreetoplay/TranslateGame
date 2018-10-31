label photo_booth_roxxy_take_picture:
    scene expression "backgrounds/location_mall_upstairs_booth.jpg"
    show roxxy_booth 1 at right
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "Ты когда-нибудь пользовалась этой вещью раньше?"
    show player 13
    show roxxy 2
    rox "Нет..."
    show roxxy 1
    rox "..."
    show roxxy 1h
    rox "Как я выгляжу?"
    show roxxy 1g
    show player 29 with dissolve
    player_name "... Ты великолепна."
    show player 13 with dissolve
    show roxxy 1b
    rox "Да?"
    show roxxy 1
    show player 14
    player_name "Да!"
    show player 26
    player_name "Ты всегда красиво выглядишь.!"
    show player 13
    show roxxy 4
    rox "..."
    rox "Ой, заткнись!"
    show roxxy 1h
    rox "Я не всегда так выгляжу..."
    show roxxy 1g
    show player 26
    player_name "Да так и есть."
    show player 13
    show roxxy 1h
    rox "Неважно."
    show roxxy 1g
    show player 5
    player_name "..."
    rox "..."
    show roxxy 1h
    rox "Хорошо, я собираюсь войти.."
    hide roxxy_booth
    show roxxy booth 2
    with dissolve
    show player 14
    player_name "... Хорошо."
    show player 13
    hide roxxy
    show roxxy_booth 1 at right with dissolve
    pause
    show player 5
    player_name "..."
    show player 10
    player_name "Ты уверена, что знаешь, как все работает?"
    show player 5
    rox "Это не высшая математика,!"
    rox "Ты просто кладешь деньги и нажимаешь кнопку."
    show player 14
    player_name "Хех, хорошо."
    show player 13
    show roxxy_booth 1 with flash
    pause
    show player 9 with dissolve
    show roxxy_booth 1 with flash
    pause
    show roxxy_booth 1 with flash
    pause
    player_name "..."
    show player 10 with dissolve
    player_name "... Ты закончила?"
    player_name "Ты получила все, что тебе было нужно?"
    show player 5
    rox "Мне нужна еще одна картинка."
    show player 10
    player_name "... Хорошо."
    show player 11
    hide roxxy_booth
    show roxxy booth 2 at right
    with dissolve
    rox "Иди сюда!"
    hide player
    show roxxy booth 3
    player_name "!!!" with hpunch
    show roxxy booth 4
    pause
    scene expression "backgrounds/location_mall_upstairs_booth_inside.jpg"
    show roxxy booth 5 at right with dissolve
    rox "Скажи сыыр, {b}[firstname]{/b}!"
    show roxxy booth 6 with dissolve
    player_name "Стой, стой, стой!!!"
    show roxxy booth 7 with dissolve
    rox "!!!" with hpunch
    show roxxy booth 7 with flash
    rox "Какого хрена, {b}[firstname]{/b}!!"
    scene black with fade
    scene expression "backgrounds/location_mall_upstairs_booth.jpg"
    show roxxy_booth 1 at right
    show roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "... Извини."
    player_name "Я подскользнулся!"
    show player 5
    show roxxy 2
    rox "... Да,точно."
    rox "Я просто пыталась дать тебе небольшую награду..."
    show roxxy 68 with dissolve
    pause
    hide player
    hide roxxy
    show roxxy_picture 1
    with dissolve
    rox "..."
    pause
    hide roxxy_picture
    show roxxy 69 at right
    show player 5 at left
    with dissolve
    rox "Хахаха!"
    show player 13
    show roxxy 72
    rox "Я думаю, ты получил большую награду, чем я предполагала..."
    show roxxy 1g
    show player 645
    with dissolve
    player_name "!!!"
    show player 646
    player_name "... Эмм, спасибо, я думаю?"
    show player 645
    show roxxy 1h
    rox "Ох, Давай..."
    rox "Ты только что сделал фотку уткнувшись в мои сиськи.."
    rox "Чего больше ботаник как ты мог просить?"
    show roxxy 1g
    show player 4 with dissolve
    player_name "..."
    show roxxy 2
    rox "Только не причини себе боль дроча на него..."
    show roxxy 1g
    show player 10 with dissolve
    player_name "Я не собираюсь... Я имею в виду Я не-"
    show player 5
    show roxxy 2
    rox "Неважно,извращенец!"
    show roxxy 3c
    rox "Не кому больше этого не показывай!"
    rox "Если {b}Декстер{/b} узнает об этом он убьет нас обоих!"
    show roxxy 1
    show player 14
    player_name "Да,да... Я не буду."
    show player 645 with dissolve
    show roxxy 1g
    rox "..."
    show roxxy 68 with dissolve
    pause
    show roxxy 72 with dissolve
    rox "Здесь."
    show roxxy 1b with dissolve
    rox "Думаешь что одна из этих подойдет для меня?"
    show roxxy 1
    show player 646
    player_name "Думаю,да..."
    show player 13 with dissolve
    show roxxy 1b
    rox "Хорошо."
    rox "Позвони мне, когда документы будут готовы."
    show roxxy 1
    show player 14
    player_name "Да, Хорошо."
    show player 13
    hide roxxy with dissolve
    player_name "( ... )"
    show player 5
    player_name "( Что ж, это было странно. )"
    player_name "( Я провалился лицом в сиськи {b}Рокси{/b} и она даже не разозлилась... )"
    player_name "( Я должен принести {b}Это фото к Капитану Терри{/b} на {b}причал{/b}. )"
    hide player with dissolve
    return

label photo_booth_generic_dialogue:
    scene expression player.location.background
    show player 2
    player_name "Хмм,Мне не нужно фотографироваться прямо сейчас..."
    hide player
    return

label photo_booth_first_visit:
    scene expression player.location.background
    show player 2
    player_name "Эй, Я никогда не замечал эту фото-будку здесь раньше..."
    player_name "... Он должен быть новым!"
    show player 17
    player_name "Круто!"
    hide player
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
