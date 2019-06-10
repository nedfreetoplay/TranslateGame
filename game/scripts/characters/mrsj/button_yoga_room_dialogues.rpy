label mrsj_button_yoga_room_dialogue_pre_first:
    show player 1 at left
    show mrsj 10 at right
    with dissolve
    player_name "Ммм-"
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
    player_name "Привет, {b}Миссис Джонсон{/b}!"
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Что Вы здесь делаете?"
    show mrsj 14 at right
    show player 29 at left
    player_name "Я... видел вас из главного {b}Тренажерного зала{/b}!"
    player_name "Я просто пришел, чтобы сказать вам привет!"
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Это так мило!"
    show mrsj 17 at right
    mrsjo "Итак, вы сейчас работаете, да?"
    show mrsj 14 at right
    show player 21 at left
    player_name "Хаха. Да..."
    player_name "...Просто начал тренироваться, чтобы набрать форму!"
    show mrsj 19 at right
    show player 11 at left
    mrsjo "Я уверена, у вас получиться стать сильным и {b}мощьным{/b}-"
    mrsjo "..."
    show player 13 at left
    show mrsj 18 at right
    mrsjo "Я имею в виду, {b}Крепким{/b}!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Надеюсь..."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Во всяком случае, есть ли что-нибудь, о чем вы хотели поговорить?"
    return

label mrsj_button_yoga_room_dialogue_pre_repeat:
    show player 14 at left
    show mrsj 14 at right
    with dissolve
    player_name "Привет, {b}Миссис Джонсон{/b}!"
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Привет, {b}[firstname]{/b}!"
    show player 11 at left
    show mrsj 18 at right
    mrsjo "Вы начинаете выглядеть здоровым, молодой человек!"
    show player 29 at left
    show mrsj 14 at right
    player_name "Ох. Спасибо..."
    player_name "Как вы..."
    show player 1 at left
    show mrsj 17 at right
    mrsjo "Есть что-нибудь, о чём вы хотели бы поговорить?"
    return

label mrsj_button_yoga_room_dialogue_hows_erik:
    show player 10 at left
    show mrsj 14 at right
    player_name "Как {b}Эрик{/b} в эти дни?"
    player_name "Я едва его вижу."
    show mrsj 18 at right
    show player 5 at left
    mrsjo "Ну... Ты же знаешь, как он!"
    mrsjo "Он просто любит свои видео игры..."
    show player 10 at left
    show mrsj 14 at right
    player_name "Да, но в последнее время это стало ещё хуже."
    player_name "Я даже не получаю текстовых сообщений от него..."
    show mrsj 19 at right
    show player 5 at left
    mrsjo "..."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Знаешь, я думаю, у него проблемы с адаптацией к жизни."
    mrsjo "Я волнуюсь за него."
    show mrsj 19 at right
    show player 12 at left
    player_name "Понятия не имел."
    show mrsj 20 at right
    show player 11 at left
    mrsjo "Он не привык быть человеком дома."
    mrsjo "... И у него такое трудное время с девушками."
    show mrsj 19 at right
    mrsjo "Бедняжка возможно одинок."
    show mrsj 14 at right
    show player 21 at left
    player_name "...Да уж.  Я думаю, что понял."
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Это хорошо, что у него есть верный друг, как ты, {b}[firstname]{/b}!"
    mrsjo "Он нуждается в тебе."
    show mrsj 14 at right
    show player 17 at left
    player_name "Ну, мы всегда были такими друзьями..."
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Я расскажу ему, чтобы он писал тебе чаще!"
    show mrsj 14 at right
    show player 14 at left
    player_name "Все в порядке, я просто хотел убедиться, что с ним все в порядке."
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Есть ли что-нибудь ещё, о чем вы хотели поговорить?"
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
    player_name "Какой была {b}поза из йоги{/b}, которую вы делали раньше?"
    show mrsj 13 at right
    show player 13 at left
    show player 1 at left
    mrsjo "О, я покажу тебе!"
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
    mrsjo "Весь путь вниз до колен!"
    window hide
    pause
    show player 21 at left
    player_name "Уххх..."
    player_name "...Да..."
    show player 11 at left
    mrsjo "Это называется {b}Кошка Корова{/b}!"
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
    anna "Привет, {b}Тэмми{/b}."
    show anna 5f
    anna "Не говори мне, что ты начала без меня."
    show anna 4f
    show mrsj 18
    mrsjo "Конечно, нет! Я просто общаюсь с другом моего арендатора, {b}Эрика{/b}!"
    show anna 11 at Position (xpos=700) with dissolve
    show mrsj 17b
    mrsjo "{b}Анна{/b}, это {b}[firstname]{/b}. {b}[firstname]{/b}, Это моя подруга, {b}Анна{/b}."
    show mrsj 14
    show player 36 with dissolve
    player_name "Привет!"
    show player 13 with dissolve
    show mrsj 14b
    show anna 12
    anna "Ты друг {b}Эрика{/b}?"
    show anna 11
    show player 14
    show mrsj 14
    player_name "Да. Мы были друзьями в течение длительного времени."
    show player 12
    player_name "Вы тоже тренер?"
    show player 5
    show anna 2 with dissolve
    show mrsj 14b
    anna "О, нет. Я просто студентка."
    show anna 1
    show player 13
    show mrsj 17
    mrsjo "{b}Анна{/b} - одна из моих лучших. Она могла бы научить здесь, если бы хотела!"
    show mrsj 14b
    show anna 3
    anna "О, я так не думаю! Ха-ха!"
    show anna 2
    anna "Она великий учитель, и я просто новичок."
    show anna 1
    show mrsj 17
    mrsjo "{b}Анна{/b}, просто скромная."
    show mrsj 17b
    mrsjo "Она может быть и новичок, но она очень талантлива... и чрезвычайно гибкая."
    show mrsj 14b
    show anna 3
    anna "Ха-ха."
    show anna 2
    anna "Я должна идти сейчас и готовиться к следующему уроку."
    show anna 3
    anna "До свидания, {b}Тэмми{/b}!"
    show anna 1
    show mrsj 17b
    mrsjo "Скоро увидимся."
    show mrsj 14b
    show anna 2
    anna "Было приятно встретиться с вами, {b}[firstname]{/b}."
    show anna 1
    show player 14
    show mrsj 14
    player_name "Пока!"
    hide anna with dissolve
    return

label mrsj_button_yoga_room_dialogue_what_was_that_after:
    show mrsj 17 at right
    show player 1 at left
    mrsjo "Есть еще что-нибудь, о чём вы хотели бы поговорить?"
    return

label mrsj_button_yoga_room_dialogue_youre_so_fit:
    show mrsj 14 at right
    show player 29 at left
    player_name "Я должен сказать: {b}Миссис Джонсон{/b}, вы действительно в форме!"
    player_name "Вы много тренируетесь?"
    show mrsj 18 at right
    show player 13 at left
    mrsjo "Ой ... Ты такой милый!"
    show mrsj 17 at right
    mrsjo "Ну, я стараюсь ходить в спортзал так часто, как могу..."
    mrsjo "...Я бегаю!  И я занимаюсь йогой в своей комнате ночью..."
    show mrsj 19 at right
    show player 21 at left
    player_name "Ну, это работает!"
    show player 13 at left
    mrsjo "Ты думаешь?"
    show mrsj 15 at right
    show player 11 at left
    mrsjo "Моя {b}попа{/b} все ещё выглядит немного большой..."
    show mrsj 16 at right
    show player 23 at left
    mrsjo "...И мои {b}сиськи{/b} не выглядят подтянутыми..."
    player_name "..."
    show player 28 at left
    show mrsj 19 at right
    player_name "*Глоток*"
    show player 1 at left
    show mrsj 18 at right
    mrsjo "Есть ещё что-нибудь, о чём вы хотели поговорить?"
    return

label mrsj_button_yoga_room_dialogue_have_to_train:
    show mrsj 14 at right
    show player 14 at left
    player_name "Я должен вернуться к моей подготовки!"
    show mrsj 18 at right
    show player 1 at left
    mrsjo "Ладно, тогда!"
    show mrsj 14 at right
    show player 17 at left
    player_name "Пока, {b}Миссис Джонсон{/b}!"
    hide player 17 at left with dissolve
    hide mrsj 14 at right with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
