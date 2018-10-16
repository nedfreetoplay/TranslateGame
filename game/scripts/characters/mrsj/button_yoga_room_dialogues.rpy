label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Эммм-"
    show player 11 at left
    window hide
    pause
    player_name "..."
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right with hpunch
    mrsjo "Ох!"
    show player 18 at left
    mrsjo "...{b}[firstname]{/b}?"
    show mrsj 14 at right
    show player 17 at left
    player_name "Здавствуйте, {b}Mrs. Johnson{/b}!"
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Что ты здесь делаешь?"
    show mrsj 14 at right
    show player 29 at left
    player_name "Я... увидел тебя с главного {b}спортзала{/b}!"
    player_name "Я просто зашел поздороваться.!"
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Это так мило!"
    show mrsj 17 at right
    mrsjo "Значит ты начал качаться, хм?"
    show mrsj 14 at right
    show player 21 at left
    player_name "Хаха. Да..."
    player_name "...Только начал тренироваться,чтобы быть в хорошей физической форме!"
    show mrsj 19 at right
    show player 11 at left
    mrsjo "И я уверена что ты станешь здоровым и {b}жестким{/b}-"
    mrsjo "..."
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Я имею в виду, {b}сильным{/b}!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Надеюсь,что так..."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "В общем, есть что-нибудь о чем бы ты хотел поговорить?"
    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Привет, {b}Mrs. Johnson{/b}!"
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Привет, {b}[firstname]{/b}!"
    show player 11 at left
    show mrsj 18 at right
    mrsjo "Ты начинаешь выглядеть в форме, молодой мужчина!"
    show player 29 at left
    show mrsj 14 at right
    player_name "О. Спасибо..."
    player_name "Так вы..."
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Есть ли что-нибудь, о чем ты хотел поговорить??"
    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "Как {b}Erik{/b} в последние время?"
    player_name "Я почти его не вижу."
    show mrsj 18 at right
    show player 5 at left
    mrsjo "Ну... Ты же знаешь, какой он!"
    mrsjo "Он просто любит свои видеоигры..."
    show player 10 at left
    show mrsj 14 at right
    player_name "Да, но в последнее время стало еще хуже."
    player_name "Я даже не получаю от него сообщений..."
    show mrsj 19 at right
    show player 5 at left
    mrsjo "..."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Ты знаешь, Я думаю, у него проблемы с адаптацией к одиночной жизни."
    mrsjo "Я беспокоюсь о нем."
    show mrsj 19 at right
    show player 12 at left
    player_name "Я и не знал."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Он не привык быть хозяином дома."
    mrsjo "... И ему так тяжело с девушками.."
    show mrsj 19 at right
    mrsjo "Бедняжка должен быть он совсем одинок."
    show mrsj 14 at right
    show player 21 at left
    player_name "...Да.Думаю я понимаю."
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Хорошо, что у него есть верный друг, как ты, {b}[firstname]{/b}!"
    mrsjo "Ты ему нужен."
    show mrsj 14 at right
    show player 17 at left
    player_name "Ну, мы всегда были друзьями так что..."
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Я скажу ему, чтобы писал тебе чаще!"
    show mrsj 14 at right
    show player 14 at left
    player_name "Все в порядке, я просто хотел убедиться, что он в порядке."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Есть ли что-нибудь еще, о чем ты хотел поговорить?"
    return

label mrsj_button_yoga_room_dialogue_what_was_that:
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_pre")
    if M_anna.is_state(S_anna_start):
        call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_anna_intro")
        $ M_anna.trigger(T_anna_intro)
    call expression game.dialog_select("mrsj_button_yoga_room_dialogue_what_was_that_after")
    return

label mrsj_button_yoga_room_dialogue_what_was_that_pre:
    show mrsj 14 at right
    show player 14 at left
    player_name "Что это была за {b}поза йоги{/b} которую вы делали раньше?"
    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsjo "О, Я покажу тебе!"
    show mrsj 12 at right
    show player 11 at left
    mrsjo "Вы начинаете вот так!"
    show mrsj 11 at right
    window hide
    pause
    show player 21 at left
    show mrsj 10 at right
    window hide
    pause
    mrsjo "До самого конца на своих коленях!"
    window hide
    pause
    show player 21 at left
    player_name "Эмммм..."
    player_name "...Да..."
    show player 11 at left
    mrsjo "Это назывется {b}Кошачья корова{/b}!"
    show mrsj 11 at right
    window hide
    pause
    show mrsj 12 at right
    window hide
    pause
    show mrsj 13 at right
    show player 18 at left
    mrsjo "Неплохо, правда?"
    return

label mrsj_button_yoga_room_dialogue_what_was_that_anna_intro:
    show anna 12f at Position (xpos=600)
    show mrsj 13 at right
    show player 13
    with dissolve
    anna "Приветик, {b}Tammy{/b}."
    show anna 5f
    anna "Не говори мне, что ты начал без меня."
    show anna 4f
    show mrsj 18
    mrsjo "Конечно нет! Я просто болтаю с другом моего жильца, {b}Erik{/b}!"
    show anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsjo "{b}Anna{/b}, это {b}[firstname]{/b}. {b}[firstname]{/b}, это моя подруга, {b}Anna{/b}."
    show mrsj 14
    show player 36 with dissolve
    player_name "Привет!"
    show player 13 with dissolve
    show mrsj 14b
    show anna 12
    anna "Ты друг {b}Erik{/b}?"
    show anna 11
    show player 14
    show mrsj 14
    player_name "Да. Мы дружим уже много лет."
    show player 12
    player_name "Ты тоже здесь тренер?"
    show player 5
    show anna 2 with dissolve
    show mrsj 14b
    anna "О, нет. Я просто ученица."
    show anna 1
    show player 13
    show mrsj 17
    mrsjo "{b}Anna{/b} одеа из моих лучших. Она могла бы обучать тут сама если бы захотела!"
    show mrsj 14b
    show anna 3
    anna "О, Я так не думаю!Ха ха!"
    show anna 2
    anna "Она отличный учитель, а я всего лишь новичок."
    show anna 1
    show mrsj 17
    mrsjo "{b}Anna{/b}, просто скромничает."
    show mrsj 17b
    mrsjo "Она может быть новичком, но она очень талантлива... и чрезвычайно гибкая."
    show mrsj 14b
    show anna 3
    anna "Ха ха."
    show anna 2
    anna "Мне пора идти и готовиться к следующему уроку."
    show anna 3
    anna "До свидания, {b}Tammy{/b}!"
    show anna 1
    show mrsj 17b
    mrsjo "Скоро увидимся."
    show mrsj 14b
    show anna 2
    anna "Было приятно познакомиться с тобой, {b}[firstname]{/b}."
    show anna 1
    show player 14
    show mrsj 14
    player_name "Пока!"
    hide anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Есть что-нибудь еще о чем ты бы хотел поговорить?"
    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Я должен сказать, {b}Mrs. Johnson{/b},вы очень фигуристая!"
    player_name "Вы много тренируетесь?"
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ой... Ты такой хороший!"
    show mrsj 17 at right
    mrsjo "Ну, Я прихожу сюда так часто, как могу, и стараюсь пользоваться тренажерным залом..."
    mrsjo "...Я так же бегаю трусцой! И я занимаюсь йогой в своей комнате ночью тоже..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Что ж, у тебя получается!"
    show player 13 at left
    mrsjo "Ты думаешь?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Моя {b}задница{/b} по-прежнему немного большая..."
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...И мои {b}сиськи{/b} не такие какие они были прежде..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*Глоток*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Есть что-нибудь еще о чем ты бы хотел поговорить?"
    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "Мне нужно вернуться к своим тренеровкам!"
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Хорошо,тогда!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Пока, {b}Mrs. Johnson{/b}!"
    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
