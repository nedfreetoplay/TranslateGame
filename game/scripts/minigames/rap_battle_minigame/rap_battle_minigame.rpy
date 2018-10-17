default temp_list = []
default chico_random = 0
default chad_random = 0
default tyrone_random = 0
init python:
    class Rap:
        def __init__(self, line, rhymes, answer):
            self.line = line
            self.rhymes = rhymes
            self.answer = answer

screen rapbattle:
    add "backgrounds/location_park_minigame05b.jpg"
    add "buttons/rap_ui_mc.png" pos 400,250
    text temp_list[player_point].line size 22 pos 520,280
    $ rap_index = 0
    $ a = 570
    for Rap in temp_list[player_point].rhymes:
        $ b = 380 + rap_index*60
        textbutton temp_list[player_point].rhymes[rap_index] style style.button["rapbattle"] text_style style.text["rapbattle_text"] pos a,b action If(temp_list[player_point].rhymes[rap_index] == temp_list[player_point].answer, Jump("end_phase"), [Hide("rapbattle"), Jump("rapbattle_lose")])
        $ rap_index += 1
    timer 0.02 repeat True action If(time_count > 0, SetVariable("time_count", time_count - 0.01), [Hide("rapbattle"), Jump("rapbattle_lose")])
    bar value time_count range timer_range pos 260,685 xmaximum 513 ymaximum 33 style "time_bar"

label rapbattle_listing:
    if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap.ogg"):
        $ playMusic("<loop 108.292 to 180.658>audio/music_rap.ogg")

    $ chico1 = Rap(line = "Чико, почему ты такая стерва? \nТвоей разбитой губе понадобится ____.", rhymes = ["швы", "заплатки", "поцелуй"], answer = "швы")
    $ chico2 = Rap(line = "Ты уверен, что тебя зовут не Рик?\nПотому что сейчас ты ведешь себя ____.", rhymes = ["хуй", "писюн", "задница"], answer = "хуй")
    $ chico_list = [chico1, chico2]
    $ chico3 = Rap(line = "Ты хочешь команду? Я дам тебе три.\nУ тебя не будет других богов \nпередо ____.", rhymes = ["мной", "Као", "Иисусом"], answer = "мной")
    $ chico4 = Rap(line = "Преклонитесь передо мной и уважайте мой ход.\nя даю команды сейчас,\nэто моё ____.", rhymes = ["шоу", "рэп", "жизнь"], answer = "шоу")
    $ chico_list2 = [chico3, chico4]
    $ chico5 = Rap(line = "Кроме Евы, все что я вижу здесь, только позера. \nТы сделал ход, \nно я буду ____.", rhymes = ["близко", "лучше", "Иисус"], answer = "близко")
    $ chico6 = Rap(line = "И правда мужик? Один из твоих родственников?\nЯ мог бы вытянуть лучшие рэпы в \n мусорном ____.", rhymes = ["сумка", "грузовик", "ведре"], answer = "ведре")
    $ chico_list3 = [chico5, chico6]
    $ chico7 = Rap(line = "Эй йоу, Чико, ты действительно хочешь рэпа? \nты читаешь так, будто у тебя перья на ____.", rhymes = ["твоей кепке", "твоих волосах", "твоей заднице"], answer = "твоей кепке")
    $ chico8 = Rap(line = "Йоу, твои рифмы такие ненормальные; \nВсе что тебе нужно это ____.", rhymes = ["новый сникерс", "закадровый смех", "мамкины спагетти"], answer = "закадровый смех")
    $ chico_list4 = [chico7, chico8]

    $ chad_time = 6.0
    $ chad1 = Rap(line = "Очень приятно познакомиться с тобой Чад и я \nрад что я сделал, потому что твое чтение было \nслабым, а ты сложен как ____.", rhymes = ["ребенок", "женщина", "слон"], answer = "ребенок")
    $ chad2 = Rap(line = "Я могу быть в твоем классе,но ты будешь \nучиться у меня. Я починю твое мастерство,\nи я это даже сделаю  ____.", rhymes = ["бесплатно", "массаж", "все"], answer = "бесплатно")
    $ chad3 = Rap(line = "Ты ничему не можешь меня научить,ты не освоил ни хрена. \nТы можешь получить\nэто место сейчас,я думаю пришло время тебе ____.", rhymes = ["присесть", "убираться", "отъебаться"], answer = "присесть")
    $ chad4 = Rap(line = "Твоя проза слаба,и твой \nсклад ума не стоит упомиминания, Твоё \nчтение неудачника, и это принесет тебе ____.", rhymes = ["арест", "аутизм", "овации"], answer = "арест")
    $ chad_list = [chad1, chad2, chad3, chad4]
    $ chad5 = Rap(line = "Этот снова уставший рэп? Хорошо Чад, \nдавай сделаем это диким, тебе нравится эта школа \nтварь, мм? Чтож, давай тогда, ____.", rhymes = ["ребенок", "чувак", "лузер"], answer = "ребенок")
    $ chad6 = Rap(line = "Я здесь не затем, чтобы впечатлять тебя, но поверь,\nя оставлю впечатление,ты не будешь\nв стостоянии ходить после того,как я закончу с этим ____.", rhymes = ["сеансом", "дерьмом", "линией"], answer = "сеансом")
    $ chad7 = Rap(line = "Ты симпатичный парень, так что да, давай поговорим о тебе, \nи о том, как я уничтожу тебя и эту пидорскую____.", rhymes = ["прическу", "стиль", "рожу"], answer = "прическу")
    $ chad8 = Rap(line = "Ты хочешь плюнуть на естественную науку о жаре\n конвекции? Я зажарил тебя \n, и это дало твоим мальчикам ____.", rhymes = ["эрекцию", "аутизм", "мурашки по коже"], answer = "эрекцию")
    $ chad_list2 = [chad5, chad6, chad7, chad8]
    $ chad9 = Rap(line = "Давай не будем говорить о твоей такой тонкой коже\n я все в твоем районе, \nи ты знаешь, что это мой ____.", rhymes = ["биз", "женшина", "слон"], answer = "биз")
    $ chad10 = Rap(line = "Да, я ношу сандалии, потому что кроссовки тают, \nмой огонь горячее твоего,когда я снимаю свой ____.", rhymes = ["ремень", "штаны", "парик"], answer = "ремень")
    $ chad11 = Rap(line = "Мне насрать на твое остроумие, у меня острый\nкак клинок, когда я покончу с твоей задницей, \nя зайду в торговый центр и ____.", rhymes = ["перепихнусь", "напьюсь", "выброшусь"], answer = "перепихнусь")
    $ chad12 = Rap(line = "Так что это было весело в твоем классе, жаль что \n твой рэп был плохим, я выпустился с этой \n школы, это конец, До свидания ____.", rhymes = ["Чад", "все", "жены"], answer = "Чад")
    $ chad_list3 = [chad9, chad10, chad11, chad12]

    $ tyrone_time = 6.0
    $ tyrone1 = Rap(line = "Не говори о моей семье, я тебя нахуй порежу. \nУ меня есть в доме меч, острый, как ____.", rhymes = ["гинсу", "джутсу", "Винду"], answer = "гинсу")
    $ tyrone2 = Rap(line = "Но ничто так не остро, как ритм в этом рэпе, \nкак нож в твоем сердце, просто нельзя____.", rhymes = ["устранить", "следовать", "опровергнуть"], answer = "устранить")
    $ tyrone3 = Rap(line = "Ты зажен во мне кровожадное намерение, \nМне нужно успокоиться, прежде чем я ____.", rhymes = ["истощусь", "согнусь", "запрусь"], answer = "истощусь")
    $ tyrone4 = Rap(line = "Дай мне немного кексов, парень, \nмне тоже нужно облегчение, так что не возвышайся ____.", rhymes = ["высоко", "сторону", "шагай"], answer = "высоко")
    $ tyrone5 = Rap(line = "Ты единственный раста, которого я когда-либо встречал, \nтоже самый гейский, если бы мне пришлось ____.", rhymes = ["ставить", "переживать", "потеть"], answer = "ставить")
    $ tyrone6 = Rap(line = "Ты не на улице, ты,отмечен как заноза в заднице, \nя был повсюду вокруг, ты не оставил этот ____.", rhymes = ["парк", "темноту", "искру"], answer = "парк")
    $ tyrone7 = Rap(line = "И да, я помню,как я оказался, я шлепнул двух сук, ты вскоре будешь ____.", rhymes = ["третим", "свободным", "собой"], answer = "третим")
    $ tyrone8 = Rap(line = "Мне не нужно заканчивать, я обезвредил твою бомбу, \nзаменил ее своим собственным сжиганием ____.", rhymes = ["напалма", "пальмы", "псалом"], answer = "напалма")
    $ tyrone_list = [tyrone1, tyrone2, tyrone3, tyrone4, tyrone5, tyrone6, tyrone7, tyrone8]
    $ tyrone9 = Rap(line = "Я говорил тебе один раз раньше, и я скажу тебе еще раз, \nоставь мою семью в покое, \nпрежде чем я передам гнев в прошлое ____.", rhymes = ["десяти", "шариковой ручкой", "лощина"], answer = "десяти")
    $ tyrone10 = Rap(line = "Я включу обогреватель до одиннадцати, когда я доберусь до тебя,\nя мистер T. в этом матче, и мне жаль тебя, ____.", rhymes = ["фуу", "r2d2", "тоже"], answer = "фуу")
    $ tyrone11 = Rap(line = "Ты представляешь себя драконом? \nСучка, это очень мило. \nУ тебя вес ящерицы в дешевой заднице ____.", rhymes = ["костюма", "дороги", "добычи"], answer = "костюма")
    $ tyrone12 = Rap(line = "Я настоящий истребитель драконов, \nи,истребительница кисок,в придачу \nу меня в логове гарем,а что есть у тебя?____?", rhymes = ["Фрукт", "привлекательность", "безмолвность"], answer = "Фрукт")
    $ tyrone13 = Rap(line = "Ты не смог бы поджарить меня, \nдаже если бы у тебя был мой огонь, ты проиграешь эту битву теперь, \nкогда спровоцировал мой ____.", rhymes = ["гнев", "дробилку", "оруженосца"], answer = "гнев")
    $ tyrone14 = Rap(line = "Ты думаешь, что избил меня, когда я истекал кровью? \nЭто история неудачника, в этом вся моя мотивация  ____.", rhymes = ["необходима", "бусина", "подвиг"], answer = "необходима")
    $ tyrone15 = Rap(line = "Я получил удар, как пуля в мозг, ты передо мной? \nТы должен быть ____.", rhymes = ["безумный", "крейн", "глупый"], answer = "безумный")
    $ tyrone16 = Rap(line = "Я видела тебя насквозь и знаю, кто ты такой. \nИди к себе домой мальчик, \nвозьми свою растовскую  ____ задницу.", rhymes = ["далекую", "бар", "машина"], answer = "далекую")
    $ tyrone_list2 = [tyrone9, tyrone10, tyrone11, tyrone12, tyrone13, tyrone14, tyrone15, tyrone16]
    $ tyrone17 = Rap(line = "Подожди, дай мне начать битву на этот раз. \nЭто упреждающий удар, надрать тебе задницу ____.", rhymes = ["стишком", "грязью", "центами"], answer = "стишком")
    $ tyrone18 = Rap(line = "Я бил твоих ребят, ты последний в списке, \nЧико командовал, а Чад был ____.", rhymes = ["уволен", "шипел", "бухой"], answer = "уволен")
    $ tyrone19 = Rap(line = "Я бы сказал, что уже убил тебя, \nно ты все еще дышишь, и это скоро будет исправлено, \nты, сырая ____задница.", rhymes = ["языческая", "фримэн", "спермой"], answer = "языческая")
    $ tyrone20 = Rap(line = "Я слышал твой рэп и слушал, как ты сорвался, \nпришло время уложить вас в постель с физраствором ____ физраствором.", rhymes = ["капельничным", "клип", "вырвано"], answer = "капельничным")
    $ tyrone21 = Rap(line = "Я бы посмотрел тебе в глаза, \nно я не вижу сквозь дым, ты думал, \nчто плюешься огнем, но твоя задница ____.", rhymes = ["посмешище", "чувак", "дубак"], answer = "посмешище")
    $ tyrone22 = Rap(line = "У меня лед в венах, я порочный и холодный. \nЯ прикончу тебя прямо здесь, \nу тебя не будет шанса получить ____.", rhymes = ["старье", "смелость", "холод"], answer = "старье")
    $ tyrone23 = Rap(line = "Запомни мои слова, когда я положил твою задницу на стул, \nты просил об этом в начале, \nкогда ты назвал меня ____.", rhymes = ["клоуном", "педиком", "хмурым"], answer = "клуном")
    $ tyrone24 = Rap(line = "Кто смеется сейчас, сучка? Ты не очень хорошо выглядишь, \nя здесь, я показал тебе, это мой ____.", rhymes = ["район", "дерево", "состояние"], answer = "район")
    $ tyrone_list3 = [tyrone17, tyrone18, tyrone19, tyrone20, tyrone21, tyrone22, tyrone23, tyrone24]
    $ tyrone25 = Rap(line = "Я остановлю тебя прямо здесь, ясно, что ты закончил. \nУ тебя закончился рэп, и я должен ____.", rhymes = ["тонну", "телефон", "ничего"], answer = "тонну")
    $ tyrone26 = Rap(line = "Так что я возьму твою лодку и поплыву по рэп-морю. \nНепобедимый и бесспорный, лучший ____.", rhymes = ["Мс", "Дс", "ПК"], answer = "Мс")
    $ tyrone27 = Rap(line = "Я победил твою команду и теперь ты кланяешься, \nпосмотри на меня, сука, я ____ капитан.", rhymes = ["сейчас", "корова", "голубок"], answer = "сейчас")
    $ tyrone_list4 = [tyrone25, tyrone26, tyrone27]

    $ player_point = 0

    if rap_opponent == "Chico":
        jump chico01

    elif rap_opponent == "Chad":
        jump chad01

    elif rap_opponent == "Tyrone":
        jump tyrone01

label chico01:
    $ time_count = 3.5
    $ timer_range = 3.5
    scene rapbattle01bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if player.stats.chr() > 3:
        $ chico_random = renpy.random.randint(1,4)
    if player.stats.chr() == 0 or chico_random == 1:
        show text " {size=17}Ты думаешь, что можешь противостоять мне белый хлебушек? \nеще до того, как ты начнешь, ты уже труп!{/size}" at Position(xpos = 320, ypos = 675)
        $ renpy.pause()
        hide text
        show text "{size=17}Ты такой пресный как простой тост; \n Дай мне показать тебе, как амигское западное жаркое!{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list4

    elif player.stats.chr() == 1 or chico_random == 2:
        show text " {size=17}Ты вернулся, но ты должен был бежать,\nвот вот тебя изобьет латино-американец.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Это наш парк, и твоя задница под запретом,\nТебе лучше уйти сейчас, и это приказ.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list2

    elif player.stats.chr() == 2 or chico_random == 3:
        show text " {size=17}Как ты себя чувствуешь, с парочкой побед?\nсовершенствуйся и будешь признан как родной.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Так что брось пару брусков и рок это бит,\nили тащи свою задницу домой и гоняй лысого.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list3

    elif player.stats.chr() == 3 or chico_random == 4:
        show text " {size=17}Посмотрите на этого дурака,он потрясен.\nЯ знаю, что этот дурак ошибся,{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Он всегда думал что может подойти ко мне\nДолжно быть он ударился головой об дерево.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chico_list
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label chad01:
    $ time_count = 5.0
    $ timer_range = 5.0
    scene rapbattle02bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if player.stats.chr() > 6:
        $ chad_random = renpy.random.randint(1,3)
    if player.stats.chr() == 4 or chad_random == 1:
        show text " {size=17}Я знаю, мы только познакомились и я ненавижу быть грубым,\nноЧико должен был покончить с тобой\nты не должен быть здесь, чувак.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Но добро пожаловать на мой урок,\nшкола вот-вот начнется,\nсадись мальчик, ты захочешь скопировать это искусство.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Ты мог бы научиться чему-то выступая против \nчеловека который овладел этим, поверь мне, тебе нежно\nулучшить свое чтение,потому что ты уродливый ублюдок.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Урок закончен и больше тебе здесь нечего делать\nя вдохнул свой рэп в тебя,\nи оно капает с твоих ушей.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list

    elif player.stats.chr() == 5 or chad_random == 2:
        show text " {size=17}Ты снова вернулся и звонок скоро зазвонит,\n Школа на сессии давайте сделаем это.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}В прошлый раз я был почти впечатлен, но ты все равно\nужасен. Ты сам сделал эту дрянь?\n твои щорты липкие, как гель для волос.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Но хватит о тебеu, давай поговорим обо мне,\nя самый спокойный в районе но\nсейчас я задам жару.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Как осечка,\nэта битва уже закончена\nЯ приготовил тебя, чувак, здавайся.Я выйграл.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list2

    elif player.stats.chr() == 6 or chad_random == 3:
        show text " {size=17}Моя кожа светлая, но мое сердце темное,\nТы в моем районе парень,Я управляю этим парком. {/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Ты подошел ко мне в шортах и сандалиях,\nУ меня огненный рэп, слишком жаркий для обращения.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}У меня было это злобное остроумие,сделать тебя тупым\nв вонючем говне, думал, ты пойдешь и ударишь,\nно я увидел сперму на твоем месте.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Ты думал, что ты прошел,но ты только промахнулся,\nшкола закрыта на лето\nи твоя задница свободна.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = chad_list3
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label tyrone01:
    $ time_count = 8.0
    $ timer_range = 8.0
    scene rapbattle03bg
    show rapbattle_npc at Position(xpos = 350, ypos = 750)
    if player.stats.chr() > 9:
        $ tyrone_random = renpy.random.randint(1,3)
    if player.stats.chr() == 7 or tyrone_random == 1:
        show text " {size=17}Не кричи, не волнуйся, я приду с применением силы \nпрыгну в окно и вышибу двери/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17} Был как полицейский тут служащий,\n орестую твою задницу которая этого заслуживает.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Я самая плохая Раста, которую ты когда-либо видел,\nэто была твоя ошибка, когда ты начал доставать меня.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Я разогреваю этот ритм и начал этого угля,\nприготовил этого маленького MC как запеканку. {/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text " {size=17}Пока я буду на кухне, я сделаю брауни,\nнужна помощь от этого дурака пытающимся порадировать меня.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Обратно на улицы и в мой квартал,\nЯ в своем районе от моей головы до кончика моего члена.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}И никогда не забудь, как ты добрался до меня,\n едва наскребывая каждую победу.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Теперь, когда я закончил и сбросил эту бомбу,\nя зайду к тебе и брошу твою кровать и трахну твою мать.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = tyrone_list

    elif player.stats.chr() == 8 or tyrone_random == 2:
        show text " {size=17}Вернись на место, время начать все сначала,\nповесить микрофон сука,ты знаешь что я победил.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Мой РЭП быстрее, а разум быстрее,\nты идешь ко мне,ты шагаешь к мастеру.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Я твой последний босс в твоем маленьком квесте,\nУ меня адский огненный дождь и сейчас пойдет ливень.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Я плюю жару изо рта, как китайский дракон,\nЯ зажарю тебя живьем, мальчик и глотну с бутыля.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text " {size=17}Зажгу затяжку от жары твоего пепла,\n дунул, дунул передал с рук в руки к массам.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Толпа соберется, когда мы засунем тебя в грязь,\nЯ утешу твою мамку, когда ей будет больно.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17} Я привезу ее к себе и засуну ей глубоко свой член, мистер,\nпосле брошу её задницу и приду за твоей сестрой.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        show text "{size=17}Мораль этой истории в том что я убью тебя дурень,\nлирически непревзойденный, когда твоя кровь станет бассейном.{/size}" at Position(xpos = 320, ypos = 670)
        $ renpy.pause()
        hide text
        $ temp_list = tyrone_list2

    elif player.stats.chr() == 9 or tyrone_random == 3:
        $ temp_list = tyrone_list3
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label tyrone02:
    show text " {size=17}Я думал, что ты здесь последний раз,\nна этот раз я прикончу тебя, как бомбу.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}Ты видишь, Я был в этом парке гораздо дольше, чем ты.,\nя поднялся из грязи в князи и получил эту банду.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}Ты думаешь, что можешь прийти сюда и зажигать на моей лодке?\nЯ вышвырну тебя за борт и посмотрим, поплывешь ли ты.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text "{size=17}Не могу поверить, что ты пришел сюда,и плюешься своим сыром,\nты не пройдешь мимо меня, Я брошу тебя с легкостью.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    show text " {size=17}Так что теперь пришло время поставить тебя на свое место,\nЯ устал от тебя, мальчик, терпеть не могу твое гребаное лицо.{/size}" at Position(xpos = 320, ypos = 670)
    $ renpy.pause()
    hide text
    $ temp_list = tyrone_list4
    $ player_point = 0
    $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label end_phase:
    if rap_opponent == "Chico":
        $ time_count = 7
        $ timer_range = 7

    elif rap_opponent == "Chad" or rap_opponent == "Tyrone":
        $ time_count = 9
        $ timer_range = 9
    $ player_point += 1
    if temp_list == tyrone_list3 and player_point == len(temp_list):
        jump tyrone02

    if player_point == len(temp_list):
        hide screen rapbattle
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")
        jump expression game.dialog_select("rapbattle_win")
    else:

        $ renpy.random.shuffle(temp_list[player_point].rhymes)
    call screen rapbattle

label rapbattle_win:
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    if rap_opponent == "Chico":
        call expression game.dialog_select("rapbattle_win_chico")

    elif rap_opponent == "Chad":
        call expression game.dialog_select("rapbattle_win_chad")

    elif rap_opponent == "Tyrone":
        $ A_eminem.unlock()
        call expression game.dialog_select("rapbattle_win_tyrone")

    hide player
    hide chico
    hide chad
    hide tyrone
    hide douche
    with dissolve

    $ game.timer.tick()
    if (rap_opponent == "Chico" and player.stats.chr() < 4) or (rap_opponent == "Chad" and player.stats.chr() < 7) or (rap_opponent == "Tyrone" and player.stats.chr() < 10):
        $ player.stats.increase("chr")
        show unlock23 at truecenter with dissolve
        pause
        hide unlock23 with dissolve
    $ rap_opponent = ""

    if M_eve.is_set("first rap battle"):
        call expression game.dialog_select("rapbattle_win_after_eve")
        $ M_eve.set("first rap battle", False)
    $ game.main()

label rapbattle_win_chico:
    show player 76 at left
    show chico 3
    show douche 2 at right
    with dissolve
    chi "Ты чекнутый, мужик!"
    show chico 2
    chi "...Это было хорошо..."
    show chico 1
    show player 77
    player_name "Спасибо!"
    show chico 2
    show player 76
    chi "Хорошо,мужик,Мир!!"
    return

label rapbattle_win_chad:
    show player 203 at left
    show chad 2 at right
    with dissolve
    chad "Неплохо пацан.Очень даже не плохо"
    chad "Возможно, я тебя немного недооценил."
    show chad 1
    show player 2
    player_name "Спасибо.Ты тоже был хорош!"
    return

label rapbattle_win_tyrone:
    show player 203 at left
    show tyrone 2 at right
    with dissolve
    tyrone "Не буду врать, что было не так уж плохо."
    tyrone "Я хочу снова тебя здесь увидеть, хорошо?"
    show player 2
    show tyrone 1
    player_name "Конечно,посмотрим."
    return

label rapbattle_win_after_eve:
    show player 76 at left
    show eve 4 at right
    with dissolve
    eve "Ух ты! Это было великолепно!"
    show player 77
    show eve 5
    player_name "Спасибо!"
    show eve 7
    show player 76 at left
    eve "Ты уверен, что это был твой первый раз??"
    show eve 5
    show player 71
    player_name "Да!"
    show eve 6
    show player 76
    eve "Ну, я рада, что ты попробовал.Ты должен вернуться снова в ближайшее время!"
    show eve 5
    show player 77
    player_name "Конечно! Я думаю, что смогу!"
    show eve 6
    show player 76
    player_name "Сейчас,мне нужно идти домой! Увидимся в следующий раз!"
    show eve 5
    show player 77
    eve "Окей. Спокойной ночи!"
    hide player
    hide eve
    with dissolve
    return

label rapbattle_lose:
    if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
        $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")
    $ renpy.suspend_rollback(False)
    $ renpy.checkpoint()
    scene park_bench
    if rap_opponent == "Chico":
        call expression game.dialog_select("rapbattle_win_chico")

    elif rap_opponent == "Chad":
        call expression game.dialog_select("rapbattle_win_chad")

    elif rap_opponent == "Tyrone":
        call expression game.dialog_select("rapbattle_win_tyrone")

    hide player
    hide chico
    hide chad
    hide tyrone
    hide douche
    with dissolve

    $ game.timer.tick()
    show unlock24 at truecenter with dissolve
    pause
    hide unlock24 with dissolve
    $ rap_opponent = ""

    if M_eve.is_set("first rap battle"):
        call expression game.dialog_select("rapbattle_lose_after_eve")
        $ M_eve.set("first rap battle", False)
    $ game.main()

label rapbattle_lose_chico:
    show player 74 at left
    show chico 3
    show douche 2 at right
    with dissolve
    chi "Йоу! Это были какие-то слабые тексты!"
    show chico 1
    show player 75
    player_name "..."
    show chico 4
    chi "Убирайся отсюда, фуууу!"
    return

label rapbattle_lose_chad:
    show player 3 at left
    show chad 4 at right
    with dissolve
    chad "Я чувствую себя оскорбленным."
    show chad 3
    chad "У тебя хватило яиц подойти ко мне, но затем ты пришел ко мне с этим мусором!"
    chad "Лучше бы мне больше никогда не видеть тебя здесь!"
    return

label rapbattle_lose_tyrone:
    show player 3 at left
    show tyrone 3 at right
    with dissolve
    tyrone "Зачем ты все равно пришел сюда?"
    tyrone "Пришел и потратил впустую мое время. Теперь я в бешенстве."
    tyrone "Тебе нужно личное сопровождение или типа того!? Уйди!"
    return

label rapbattle_lose_after_eve:
    show player 71 at left
    show eve 1 at right
    with dissolve
    player_name "Это было довольно плохо..."
    show eve 6
    show player 76
    eve "Хахаха, не то слово..."
    show eve 7
    eve "Но все в порядке, у тебя все получится."
    show eve 1
    show player 71
    player_name "Я не знаю, подхожу ли я для этого..."
    show eve 6
    show player 76
    eve "Не смей так говорить!"
    show eve 7
    eve "Ребята узнают тебя, так что все будет не так плохо."
    show eve 1
    show player 71
    player_name "Да. Возможно..."
    show eve 6
    show player 76
    eve "Я должна идти, но я думаю, что ты должен вернуться снова в следующий раз!"
    show eve 1
    show player 77
    player_name "Хорошо. Спокойной ночи!"
    show eve 6
    show player 76
    eve "Увидимся!"
    hide player
    hide eve
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
