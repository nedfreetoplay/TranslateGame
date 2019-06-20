label courtyard_roxxy_intense_gymercise:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg") with dissolve
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    with dissolve
    bri "Посмотрите-ка, что кошка притащила."
    bri "Как проходят твои тренировки?"
    show jersey 10
    show bridget a_dressed_crossed f_normal
    player_name "Ум... Я пытался ходить в спортзал!"
    show jersey 11
    show bridget a_dressed_crossed f_angry_talk
    bri "Пытался, да?"
    bri "Посмотрим, сколько отжиманий ты сможешь сделать."
    show bridget a_dressed_crossed f_normal_talk
    bri "Может быть, ты превзошел свой личный рекорд... Повтори еще раз, два раза!?"
    show bridget a_dressed_crossed f_angry_yell
    show jersey 22
    bri "Теперь упал и сделал двадцать!" with hpunch
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254)
    show jersey 29
    with fastdissolve
    pause 0.5
    show jersey 30
    pause 0.5
    show jersey 29
    bri "Один!"
    show jersey 30
    pause 0.5
    show jersey 29
    bri "Два!"
    show jersey 30
    pause 0.7
    show jersey 29
    bri "Три!"
    show jersey 30
    pause 0.9
    show jersey 29
    bri "Четыре!"
    show jersey 27
    show bridget a_dressed_crossed f_normal_talk b_dressed
    with fastdissolve
    bri "Поздравляю, {b}[firstname]{/b}! Ты превратился из никчемного в жалкого!"
    show bridget a_dressed_crossed f_angry_talk
    bri "Продолжай тренироваться, личинка!"
    show bridget a_dressed_crossed f_normal
    show jersey 28
    player_name "Да... {b}тренер Бриджет{/b}..."
    show bridget a_dressed_crossed f_angry_talk
    show jersey 27
    bri "А теперь убирайся с глаз моих!"
    bri "И тебе лучше показать прогресс в следующий раз!"
    show bridget a_dressed_crossed f_normal
    player_name "Простите, {b}тренер Бриджет{/b}!"
    hide bridget
    hide jersey
    with dissolve
    return

label courtyard_bridget_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}_blur.jpg")
    show jersey 13 at left with dissolve
    show bridget a_dressed_crossed f_normal_talk at right with dissolve
    bri "Смотрите, кто пришел!"
    show bridget a_dressed_crossed f_normal at right
    show jersey 17 at left
    player_name "Здрасьте, {b}тренер Бриджет{/b}!"
    show jersey 18 at left
    player_name "Я знаю, что пропустил несколько тренировок, но уверяю вас, что буду готов к Региональным Легкоатлетическим Соревно-"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 22 at left
    bri "Заткнись, слизняк!" with hpunch
    bri "Ты отстаешь на месяц от всех остальных,{b}[firstname]{/b},  и я не позволю тебе утащить команду с твоим отсутствием обязательств!"
    bri "Если ты не сможете получить квалификационные баллы, ты {b}можешь забыть о своих зачетах и окончании в этом году.{/b}"
    show bridget a_dressed_crossed f_angry at right
    show jersey 10 at left
    player_name "Не беспокойтесь, мэм! Уверен, с отборочными проблем не будет!"
    show bridget a_dressed_crossed f_angry_talk at right
    show jersey 11 at left
    bri "...Ты уверен?"
    bri "Почему бы тебе не показать нам свои \"элитные спортивные навыки\" сделав {b}20 отжиманий{/b} прямо сейчас, ты, жалкий маленький болван?!"
    show bridget a_dressed_whistle f_angry_yell at right
    show jersey 10 at left
    player_name "Но-"
    show jersey 23 at left
    bri "{b}*СВИСТОК*{/b}"
    show bridget b_bend a_empty f_bend_angry_talk_down at Position (yoffset=254) with dissolve
    show jersey 29 at left
    player_name "Грр..."
    show jersey 30 at left
    bri "Один..."
    show jersey 29 at left
    player_name "Гррр..."
    show jersey 30 at left
    bri "Два..."
    show jersey 29 at left
    player_name "...Я...Я не могу..."
    show jersey 30 at left
    bri "Три-"
    bri "... ... ..."
    show bridget a_dressed_crossed f_angry_talk b_dressed with dissolve
    bri "Что?!! Это все, на что ты способен??"
    show jersey 27 at left
    bri "Ты даже не можешь сделать 3 жалких отжимания?!"
    show bridget a_dressed_crossed f_angry at right
    player_name "Я..."
    player_name "Я... простите... мэм..."
    show bridget a_dressed_crossed f_angry_talk at right
    bri "Лучше тащи свою задницу в {b}местный спортзал{/b} сейчас же, и начинай заниматься, если хочешь пройти этот класс..."
    show bridget a_dressed_crossed f_angry_yell at right
    bri "... или иди в {b}класс Мисс Биссетт{/b}, где тяжелая работа и хорошие оценки не имеют значения!"
    bri "Сейчас, {b}ИДИ ПРОЧЬ С ГЛАЗ МОИХ!!!{/b}"
    hide bridget 7 with dissolve
    show ronda b_jersey a_jersey_sides f_normal_talk at right with dissolve
    ron "Ты никогда не пройдешь квалификацию..."
    ron "Зачем ты вообще ходишь на эти занятия?"
    show ronda f_normal at right
    show jersey 28 at left
    player_name "Я все еще могу это сделать..."
    player_name "...И ты знаешь, что именно...Я подумал, может, ты мне поможешь -"
    show ronda f_upset_angry at right
    show jersey 27 at left
    ron "Стоять!"
    show ronda f_upset_talk
    ron "Если каким-то чудом тебе удасться {b}пройти испытания{/b}... тогда приходи поговорить со мной. В противном случае, перестань тратить мое время."
    show ronda f_normal at right
    show jersey 28 at left
    player_name "Хорошо!"
    player_name "Но когда я это сделаю, тебе придется показать мне некоторые свои трюки!"
    show ronda f_normal_talk at right
    ron "Я буду в {b}бассейне{/b} следующие две недели тренироваться на дистанции 200 метров..."
    ron "Если ты будешь в команде, приходи ко мне."
    show ronda f_normal at right
    show jersey 20 at left
    player_name "Договорились!!"
    show ronda f_rolleyes at right
    show jersey 19 at left
    ron "Тьфу... Патетический..."
    hide gym
    hide ronda
    hide jersey
    with dissolve
    return

label courtyard_bridget_training:
    scene gym
    show player 11 at left with dissolve
    show bridget a_dressed_crossed f_angry_talk at right with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Тебе лучше тренироваться в {b}тренажерном зале{/b}, или я засуну свою ногу тебе в задницу!!"
    show player 32
    show bridget a_dressed_crossed f_angry
    player_name "Да, мэм!!!"
    hide bridget
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
