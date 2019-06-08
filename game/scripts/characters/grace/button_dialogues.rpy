label button_grace_mia_get_tattoo:
    scene tattoo_indoor_c
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Эй, там!"
    grace "У вас здесь встреча?"
    return

label button_grace_generic:
    show player 13 at left
    show grace f_normal_talk at right
    show tattoo_desk at right
    with dissolve
    grace "Эй, там!"
    grace "У вас здесь встреча?"
    return

label button_grace_tattoo:
    show mia 10f
    mia "Я хотела бы сделать тату... Сейчас."
    show mia 7f
    show grace f_normal_talk
    grace "Сейчас? Я вижу..."
    show grace f_suspicious
    grace "Вы уже придумали какой-нибудь рисунок?"
    show grace f_normal
    show mia 30f at Position (xoffset=64) with dissolve
    mia "Мой друг нарисовал это для меня, и Я хотела бы его сделать сегодня!"
    show mia 7f
    show grace f_normal_down_talk a_dressed_hip_paper
    with dissolve
    grace "Хмм..."
    show grace f_normal_talk
    grace "Ты уверена что ты этого хочешь?"
    grace "Татуировки постоянные, так что я должна убиться что мои клиенты знают что они делают!"
    show grace f_normal
    show mia 10f
    mia "Я думала об этом об этом уже долгое время... Да, я и правда хочу это сделать."
    show mia 7f
    show grace f_normal_talk
    grace "Отлично, солнышко. но, это не дешево!"
    show grace f_normal
    show player 14
    player_name "Сколько это стоит?"
    show player 13
    show grace f_normal_down_talk
    grace "Для этого размера... с цветами... примерно {b}$400{/b}."
    show grace f_normal
    show player 22
    show mia 12f
    mia "!!!"
    mia "Черт... Я думаю у меня только {b}$200{/b}..."
    show mia 8f
    show player 11
    player_name "..."
    show player 10
    player_name "Тебе не хватает?"
    show player 5
    show mia 12 with dissolve
    mia "Нет, это все что мне удалось накопить."
    mia "Как думаешь что мне делать?"
    show mia 8
    return

label button_grace_tattoo_help:
    show player 14
    player_name "Я позабочусь об остальном."
    show player 13
    show mia 12
    mia "Реально?!"
    show mia 7
    show player 14
    player_name "Почему нет."
    player_name "Я работал в последнее время так что у меня есть немного денег чтобы потратить..."
    show player 17
    player_name "...И это ради благого дела!"
    show player 13
    show mia 10
    mia "Это очень мило с твоей стороны..."
    mia "...и я обязательно верну тебе деньги!"
    show mia 7
    show player 17
    player_name "Все в порядке, ха ха."
    show player 13
    show grace f_normal_talk
    grace "So?"
    show mia 7f with dissolve
    grace "Готова начать?"
    show grace f_normal
    show mia 10f
    mia "Я готова!"
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve

    scene tattoo_cs01
    show text "Потребовалось некоторое время чтобы {b}Грэйс{/b} закончила работу.\nЯ очень переживал за {b}Мию{/b}...\n...но, казалось что она была в порядке на протяжении всего времени!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide tattoo_cs01
    with dissolve

    scene tattoo_indoor_b
    show mia 7f at Position (xpos=400)
    show player 13 at left
    show grace f_normal_talk at right
    with dissolve
    grace "Все готово!"
    grace "Я надеюсть вам это понравится ребята."
    show grace f_normal
    show mia 10f
    mia "Это потрясающе! И это не было так больно как я думала..."
    show mia 7f
    show grace f_normal_talk
    grace "Удоставерься что ты оставила повязку на ней по крайней мере несколько дней."
    show grace f_normal
    show mia 10f
    mia "Хорошо, спасибо!"
    show mia 7f
    show grace f_normal_talk
    grace "Пока, ребята."
    hide grace with dissolve
    pause(.25)
    hide mia
    show mia 7 at right
    with dissolve
    show player 14
    player_name "Ну как?"
    show player 13
    show mia 12
    mia "Татуировка?"
    show mia 7
    show player 14
    player_name "Да."
    show player 13
    show mia 12
    mia "Все прекрасно... просто немножко покалывает."
    show mia 10
    mia "И я рада что это сделала... Я наконец могу сказать что я сделать то чего я хотела."
    show mia 7
    show player 10
    player_name "Ты не боишся что твоя мама сможет об этом узнать?"
    show player 5
    show mia 9
    mia "Надеюсь что нет, но оно находится в хорошо скрытом месте, ха ха."
    show mia 7
    show player 17
    player_name "Я думаю это круто что ты сделала."
    show player 18
    show mia 10
    mia "Спасибо, {b}[firstname]{/b}.Я счаслива что ты пошел со мной."
    show player 13
    mia "Тем не менее, мне нужно идти.Прежде чем моя мама начала что-то подозревать..."
    show mia 7
    show player 14
    player_name "Хорошо, увидимся в школе!"
    show player 13
    show mia 10
    mia "Пока."
    hide player
    hide mia
    with dissolve
    return

label button_grace_tattoo_come_back:
    show player 10
    player_name "Может быть нам вернуться попозже?"
    show player 5
    mia "..."
    show mia 12
    mia "Я думаю мы должны."
    show mia 8
    show player 10
    player_name "Все будет хорошо. Мы всегда сможем вернуться в другой раз."
    show player 5
    show mia 12
    mia "Ты прав."
    show mia 8
    show player 10
    player_name "Очень жаль что ты не смогла сделать свою Татуировку сегодня..."
    show player 5
    show mia 12
    mia "It's fine. I should get home now."
    show mia 8
    show player 10
    player_name "Alright, see you later."
    hide player
    hide mia
    hide grace
    hide tattoo_desk
    with dissolve
    return

label button_grace_paint:
    scene location_tattoo_indoor_closeup
    show player 10 zorder 3 at left
    show xtra 26 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show grace f_normal zorder 0 at right
    player_name "May I ask you something?"
    show player 11
    show grace f_normal_talk
    grace "Sure!"
    show player 10
    show grace f_normal
    player_name "Well, you see..."
    show player 11
    pause
    show player 10
    player_name "The thing is..."
    show player 11
    grace "..."
    show player 10
    player_name "... Here's the thing..."
    show player 11
    show eve 2f zorder 2 at Position(xpos=0.35, ypos=1.0) with dissolve
    eve "Geez, spit it out already, {b}[firstname]{/b}!"
    show eve 1bf with dissolve
    eve "What up, Raggedy Ann?"
    show eve 5f with dissolve
    show grace f_laugh
    grace "Heh, not much."
    show grace f_normal_talk
    grace "You staying outta trouble, Punk?"
    show eve 6bf
    show grace f_normal
    eve "Of course not."
    show player 1
    show eve 5f
    show grace f_laugh
    grace "Hehe."
    show eve 2f
    show grace f_normal
    eve "Look, {b}[firstname]{/b} here needs some ink."
    show eve 5f
    show grace f_normal_talk
    grace "Oh, you thinking of getting a tattoo there, Stud?"
    show player 11
    show grace f_normal
    player_name "..."
    show eve 1bf with dissolve
    eve "No, no, no. He needs actual ink! Like in bottles, ya Dummy!"
    show eve 6bf
    eve "Sorry, she can be a little slow."
    show eve 5f
    show grace f_suspicious
    grace "Hey! I heard that!"
    show eve 6f
    show grace f_normal
    eve "Yeah, I said it loud..."
    show eve 5f
    show grace f_laugh
    grace "Haha, smart ass."
    show eve 6f
    show grace f_normal
    eve "Looove ya, Sis!"
    show eve 5f
    show grace f_normal_talk
    grace "Yeah, yeah. You're lucky you're cute."
    show player 1
    show grace f_normal
    show eve 1bf with dissolve
    eve "I am, aren't I?"
    show grace f_normal_talk
    show eve 5f with dissolve
    grace "So, how much ink do you need, {b}[firstname]{/b}?"
    show player 2
    show grace f_normal
    player_name "Umm, I'm not sure."
    player_name "Just enough to do one painting."
    show player 1
    show grace f_normal_talk
    grace "Ahhh, an artist, huh?"
    show grace f_laugh
    grace "Figures, the first guy {b}Eve{/b} brings home is an artist."
    show player 11
    show grace f_normal
    show eve 6bf
    eve "Tch, better than that biker freak you had hanging around here in high school."
    show eve 1f
    show grace f_laugh
    grace "Heh, you'll get no arguements there..."
    show grace f_normal_talk
    grace "Would one bottle of each primary color be enough?"
    show grace f_suspicious
    grace "I assume you know how to mix?"
    show player 10
    show grace f_normal
    player_name "Mix?"
    show player 11
    show eve 2f
    eve "Yeah, you know? Blue and red make purple."
    eve "Yellow and blue make green."
    show player 2
    show eve 1f
    player_name "Oh yeah, like color wheel stuff, right?"
    show player 1
    show grace f_normal_talk
    grace "Yeah, exactly."
    show grace f_suspicious
    grace "I guess the only question now, is what are you gonna do for me?"
    show grace f_normal
    show player 10
    player_name "Oh, uhh. I dunno? What do you want me to do?"
    show grace f_suspicious
    show player 11
    grace "Hmm, did you happen to notice the graffiti on the side of the building when you came in?"
    show player 10
    show grace f_normal
    player_name "... Yeah, it's pretty hard to miss."
    show player 11
    show grace f_normal_talk
    grace "I'll give you the paints if you can wash it off for me."
    show grace f_normal
    show eve 2f
    eve "For real?"
    show player 2
    show eve 1f
    player_name "I can do that!"
    show player 1
    show eve 6bf
    grace "Pfft, what a waste of time!"
    show eve 1f
    show player 11
    player_name "..."
    show eve 1bf with dissolve
    eve "It's just gonna get tagged again..."
    show eve 1f
    show grace f_angry_talk a_dressed_hips_mad
    with dissolve
    grace "Well, it's your stupid fucking friends that keep doing it!"
    grace "You need to tell those little bitches, I'll whoop their fucking asses if it happens again!"
    show grace f_angry
    show player 10
    player_name "Daaang, I didn't know your {b}Sister{/b} was such a bad ass!"
    show eve 6f
    show player 11
    eve "Heh, you have no idea."
    show eve 5f
    show grace f_angry_talk
    grace "I dunno why you hang out with those douchebags anyways..."
    show eve 2f
    show grace f_angry
    eve "... If you're going to blackmail {b}[firstname]{/b} into doing chores. You could at least have him do something useful."
    eve "Like maybe moving all that heavy shit you ordered into the back room?"
    show eve 6bf
    show grace f_normal a_dressed_hip with dissolve
    eve "I don't wanna bust my vagina carrying that shit!"
    show eve 5f
    show grace f_suspicious
    grace "Hmm, I suppose that's not a bad idea."
    show grace f_laugh
    grace "... Especially if it gets you to shut up about your vagina! Ugh!"
    show grace f_normal
    show eve 6bf
    eve "... Bitch."
    show eve 5f
    show grace f_laugh
    grace "Hahaha, don't pretend like you don't love the abuse."
    show grace f_normal
    show eve 6bf
    eve "Yeah, yeah..."
    show eve 2f
    eve "If you'll excuse me, {b}[firstname]{/b}."
    show player 1
    eve "I'd better go warn the guys that {b}Grace{/b} is on the war path again."
    show eve 1f
    show grace f_laugh
    grace "Damn right!"
    show grace f_normal
    show eve 6f
    eve "See ya, Sis!"
    hide eve
    with dissolve
    show grace f_normal_talk
    grace "The {b}boxes are right in front of the counter{/b}. Just {b}move them{/b} into the back for me and the paint is yours."
    show grace f_normal
    show player 2
    player_name "Sounds good!"
    return

label button_grace_you_look_familiar:
    show player 10
    player_name "You know... I think..."
    show player 12
    player_name "Uhh."
    show player 34
    show grace f_suspicious
    grace "Is everything okay?"
    show grace f_normal
    show player 30
    player_name "Sorry, but you look... familiar."
    show player 5
    show grace f_suspicious
    grace "Huh?"
    show grace f_normal_talk
    grace "Hmm... Maybe you're thinking of my sister?"
    show grace f_normal
    show player 12
    player_name "Sister?"
    show player 11
    show grace f_suspicious
    grace "My little sister? {b}Eve{/b}?"
    show grace f_normal
    show player 38 with dissolve
    player_name "Oh! Of course!"
    show player 14 with dissolve
    player_name "I can see the connection, now."
    show player 13
    show grace f_laugh
    grace "Ha ha."
    show grace f_normal_talk
    grace "Anyway, is there anything I can do for you?"
    return

label button_grace_nothing:
    show player 14
    player_name "I'm just looking around."
    show player 13
    show grace f_normal_talk
    grace "Cool! Have a look."
    grace "I do all styles and designs showcased in my shop!"
    grace "Just let me know if you ever think about getting something, and we can make an appointment!"
    show grace f_normal
    show player 14
    player_name "Okay, thanks!"
    show player 13
    show grace f_normal_talk
    grace "See ya."
    hide grace
    hide mia
    hide player
    hide tattoo_desk
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
