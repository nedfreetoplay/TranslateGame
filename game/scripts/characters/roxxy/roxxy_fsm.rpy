init python:
    T_roxxy_teachers_berating = Trigger("teachers berating")
    T_roxxy_locker_room = Trigger("locker room")
    T_roxxy_argument = Trigger("argument")
    T_roxxy_start_gymercise = Trigger("start gymercise")
    T_roxxy_in_shower = Trigger("in shower")
    T_roxxy_get_homework = Trigger("get homework")
    T_roxxy_lolipop_once = Trigger("lolipop once")
    T_roxxy_lolipop_lolipop = Trigger("lolipop lolipop")
    T_roxxy_confrontation = Trigger("confrontation")
    T_roxxy_do_assignment = Trigger("do assignment")
    T_roxxy_study_at_roxxy = Trigger("study at roxxy")
    T_roxxy_study_at_mcs = Trigger("study at mcs")
    T_roxxy_find_cheerleader_outfit= Trigger("find cheerleader outfit")
    T_roxxy_get_cheerleader = Trigger("get cheerleader")
    T_roxxy_confront_clyde = Trigger("confront clyde")
    T_roxxy_beaten_clyde = Trigger("beaten clyde")
    T_roxxy_wait_in_her_room = Trigger("wait in her room")
    T_roxxy_returned_to_school = Trigger("returned to school")
    T_roxxy_has_uniform = Trigger("has uniform")
    T_roxxy_go_to_basketball = Trigger("go to basketball")
    T_roxxy_get_beer = Trigger("get beer")
    T_roxxy_ask_terry = Trigger("ask terry")
    T_roxxy_take_picture = Trigger("take picture")
    T_roxxy_give_id = Trigger("give id")
    T_roxxy_home_foreclosed = Trigger("home foreclosed")
    T_roxxy_checked_trailer = Trigger("checked trailer")
    T_roxxy_confronted_clyde = Trigger("confronted clyde")
    T_roxxy_go_to_police = Trigger("go to police")
    T_roxxy_talk_to_crystal = Trigger("talk to crystal")
    T_roxxy_sell_meth = Trigger("sell meth")
    T_roxxy_meth_asked_roxxy = Trigger("meth asked roxxy")
    T_roxxy_meet_clyde = Trigger("meet clyde")
    T_roxxy_meet_buyer = Trigger("meet buyer")
    T_roxxy_drug_deal_over = Trigger("drug deal over")
    T_roxxy_chat_with_becca_missy = Trigger("chat with becca missy")
    T_roxxy_get_goldenschwagger = Trigger("get goldenschwagger")
    T_roxxy_spun_bottle = Trigger("spun bottle")
    T_roxxy_failing_exams = Trigger("failing exams")
    T_roxxy_find_evidence = Trigger("find evidence")
    T_roxxy_find_exams = Trigger("find exams")
    T_roxxy_escaped_smith = Trigger("escaped smith")
    T_roxxy_gave_exams = Trigger("gave exams")
    T_roxxy_help_dewitt = Trigger("help dewitt")

    T_roxxy_invitation_bikini = Trigger("invitation bikini")
    T_roxxy_check_on_roxxy = Trigger("check on roxxy")
    T_roxxy_go_see_contest = Trigger("go see contest")
    T_roxxy_go_to_cabin = Trigger("go to cabin")
    T_roxxy_bikini_failure = Trigger("bikini failure")
    T_roxxy_get_oil = Trigger("get oil")
    T_roxxy_contest_over = Trigger("contest over")
    T_roxxy_dexter_challenge_pushups = Trigger("dexter challenge pushups")
    T_roxxy_beaten_dexter_pushups = Trigger("beaten dexter pushups")
    T_roxxy_accepted_picnic = Trigger("accepted picnic")
    T_roxxy_picnic_done = Trigger("picnic done")
    T_roxxy_kissed = Trigger("kissed")
    T_roxxy_basket_challenged = Trigger("basket challenged")
    T_roxxy_humiliated_dexter = Trigger("humiliated dexter")
    T_roxxy_ninja_dexter = Trigger("ninja dexter")
    T_roxxy_trailer_sex = Trigger("roxxy trailer sex")
    T_roxxy_beach_sex = Trigger("roxxy beach sex")
    T_roxxy_locker_sex = Trigger("roxxy locker sex")
    T_roxxy_crystal_sex = Trigger("roxxy crystal sex")

label roxxy_fsm_init:
    python:

        S_roxxy_start = State("start", "Мне нужно пойти в школу...")
        S_roxxy_teachers_event_delay = State("teachers event delay", "Рокси такая стерва, Я должен проверить её завтра")
        S_roxxy_teachers_event = State("teachers event", "Рокси такая стерва, Я должен проверить её.")
        S_roxxy_lockerroom_event_delay = State("lockerroom event delay", "Ух ты, она в такой беде, интересно, смогу ли я ей помочь")
        S_roxxy_lockerroom_event = State("lockerroom event", "Я должен проверить школу...")
        S_roxxy_dexter_argument_delay = State("dexter argument delay", "Я подслушал, как Рокси говорил о проблемах с Декстером... Всё подходит ко мне!")
        S_roxxy_dexter_argument = State("dexter argument", "У Рокси проблемы с Декстером, я должен проверить школу...")
        S_roxxy_intense_gymercise = State("intense gymercise", "Тренер Бриджит хочет, чтобы я доказал, что могу отжиматься...")
        S_roxxy_shower_event = State("shower event", "После тренировки, мне нужен хороший душ.")
        S_roxxy_lolipop = State("lolipop", "Рокси хочет скопировать мою домашнюю работу.")
        S_roxxy_lolipop_delay = State("lolipop delay", "Мне нужно немного подождать...")
        S_roxxy_lolipop_just_once = State("lolipop just once", "Я согласился дать ей домашнее задание, только в этот раз.")
        S_roxxy_lolipop_for_lolipop = State("lolipop for lolipop", "Я согласился дать ей домашнее задание за вознаграждение.")
        S_roxxy_dexter_confront_delay = State("dexter confront delay", "У меня есть чупачупс, не думаю, что получу что-то большее прямо сейчас.")
        S_roxxy_dexter_confront = State("dexter confront", "Мне нужно пойти в школу.")
        S_roxxy_assignment_delay = State("assignment delay", "Декстер злится на меня за то, что я тусуюсь с Рокси. Когда она бросит его тупую задницу?")
        S_roxxy_assignment = State("assignment", "Рокси может понадобиться помощь в учебе для её задания.")
        S_roxxy_studying_at_roxxys = State("studying at roxxy's", "Мы направляемся к ней, чтобы позаниматься.")
        S_roxxy_studying_at_mcs = State("studying at mc's", "В конце концов, у меня дома спокойнее. Кто такая Кристал?")
        S_roxxy_missing_outfit_delay = State("missing outfit delay", "Я должен дать ей немного пространства.")
        S_roxxy_missing_outfit_delay2 = State("missing outfit delay 2", "Я должен дать ей немного пространства.")
        S_roxxy_missing_outfit = State("missing outfit", "Мне нужно поговорить с Рокси.")
        S_roxxy_get_cheerleader_outfit = State("get cheerleader outfit", "Рокси нуждается в её чирлидирской форме, чтобы практиковаться.")
        S_roxxy_beat_clyde = State("beat clyde", "Он у Клайда, может, я смогу убедить его вернуть это.")
        S_roxxy_get_uniform_on_doggo = State("get uniform on doggo", "Он положил его на свою собака свинью!")
        S_roxxy_wait_in_her_room = State("wait in her room", "Рокси собирается переодеться. Я должен пойти в её комнату")
        S_roxxy_return_to_school = State("return to school", "Скоро начнется второй период. Я должна вернуться в школу!")
        S_roxxy_dexter_alcohol_fight_delay = State("dexter alcohol fight", "Я не должен быть слишком настойчив с ней.")
        S_roxxy_dexter_alcohol_fight = State("dexter alcohol fight", "Надо отправится на баскетбольную площадку, Ева упомянула драку!")
        S_roxxy_need_booze = State("need booze", "Рокси подралась из-за алкоголя. Я мог бы помочь ей.")
        S_roxxy_get_fake_id = State("get fake id", "Рокси нужно поддельное удостоверение, чтобы купить алкоголь")
        S_roxxy_fake_id_ask_terry = State("fake id ask terry", "Я слышал, что Терри, на пирсе, делает поддельные документы")
        S_roxxy_fake_id_get_picture = State("fake id get picture", "Терри нужна фотография и 400$. Я должен рассказать Рокси.")
        S_roxxy_trailer_park_trouble_delay = State("trailer park trouble delay", "Я должен дать ей немного времени...")
        S_roxxy_trailer_park_trouble_delay2 = State("trailer park trouble delay 2", "Я должен дать ей немного времени...")
        S_roxxy_trailer_park_trouble = State("trailer park trouble", "Мне нужно с ней поговорить.")
        S_roxxy_check_trailer = State("check trailer", "Я должен сопроводить Рокси в её дом, в парке трейлеров")
        S_roxxy_confront_clyde = State("confront clyde", "Клайд как-то связан с закрытием трейлера.")
        S_roxxy_cookies_and_milk = State("cookies and milk", "Рокси нужно куда-то идти, я приведу её к себе домой для некоторого комфорта")
        S_roxxy_ask_earl_release = State("ask earl release", "Я должен проверить полицейский участок.")
        S_roxxy_talk_to_crystal = State("talk to crystal", "По словам Ярла, Кристал ничего не скажет. Может быть, я могу помочь?")
        S_roxxy_get_evidence = State("get evidence", "Кристал ничего не сделала, это все Клайд виноват. Я должен собрать доказательства.")
        S_roxxy_selling_meth_ask_roxxy = State("selling meth ask roxxy", "Я должен рассказать Рокси, что случилось...")
        S_roxxy_selling_meth = State("selling meth", "У Клайда есть план, как получить деньги под залог: продажа метамфетамина.")
        S_roxxy_meeting_clyde = State("meeting clyde", "Нужно встретиться с Клайдом для продажи наркотиков.")
        S_roxxy_meeting_buyer = State("meeting buyer", "Давай познакомимся с таинственным покупателем.")
        S_roxxy_shut_down_lab = State("shut down lab", "Кристал вышла, а Клайда нигде не видно...")
        S_roxxy_hows_it_going_delay = State("hows it going delay", "Я должен дать Рокси некоторое время после всех событий")
        S_roxxy_hows_it_going_delay2 = State("hows it going delay 2", "Я должен дать Рокси некоторое время после всех событий")
        S_roxxy_hows_it_going_delay3 = State("hows it going delay 3", "Я должен дать Рокси некоторое время после всех событий")
        S_roxxy_hows_it_going = State("hows it going", "Я должен спросить её, всё ли с ней в порядке...")
        S_roxxy_chat_with_becca_missy = State("chat with becca missy", "Мне нужно, чтобы Бекка и Мисси разогрелись.")
        S_roxxy_spin_bottle = State("spin bottle", "Девушки приглашали меня на пляж по выходным, но я не могу пойти с пустыми руками.")
        S_roxxy_ask_exam_copy_delay = State("ask exam copy delay", "Это было дико. и жарко.")
        S_roxxy_ask_exam_copy = State("ask exam copy", "Рокси ещё нужно сдать экзамены.")
        S_roxxy_sneak_into_smith = State("sneak into smith", "Директриса Смит, очевидно, хранит копию экзаменов у себя дома.")
        S_roxxy_give_exams_delay = State("give exams delay", "У меня есть экзамены!")
        S_roxxy_give_exams = State("give exams", "Я отдал Рокси экзамены. Надеюсь на лучшее!")
        S_roxxy_dexter_flirt_delay = State("dexter flirt delay", "Я очень надеюсь, что Рокси прошла тест.")
        S_roxxy_dexter_flirt = State("dexter flirt", "Мне нужно пойти в школу.")
        S_roxxy_go_in_auditorium = State("go in auditorium", "Я слышал кое-что, происходящее в зале.")
        S_roxxy_invite_to_bikini_contest = State("invite to bikini contest", "Декстер такая свинья! С другой стороны, я увижу Рокси в бикини в эти выходные.")
        S_roxxy_go_see_contest = State("go see contest", "Я должен пойти на конкурс, капитан Терри находится на сцене")
        S_roxxy_check_on_roxxy = State("check on roxxy", "Я должен проверить девочек в душе.")
        S_roxxy_in_cabin = State("in cabin", "У Рокси порвался топ! Я должен проверить, как она.")
        S_roxxy_get_new_bikini = State("get new bikini", "Рокси нужен новый купальник! Сара бросила её на подиум.")
        S_roxxy_get_oil = State("get oil", "Рокси нужно смазать маслом для конкурса. В башне спасателя есть немного масла.")
        S_roxxy_do_pushups_delay = State("do pushups delay", "Этот конкурс был диким, я рад, что Рокси выиграла!")
        S_roxxy_do_pushups_intro = State("do pushups intro", "Я нужен тренеру Бриджет в школе.")
        S_roxxy_do_pushups = State("do pushups", "Я должен доказать Декстеру, что он напал не на того парня.")
        S_roxxy_trailer_park_romance_delay = State("trailer park romance delay", "Получи это, Декстер!")
        S_roxxy_trailer_park_romance = State("trailer park romance", "Рокси определенно потеплела ко мне, я должен поговорить с ней.")
        S_roxxy_go_to_picnic = State("go to picnic", "Она пригласила меня на ужин сегодня днем!")
        S_roxxy_picnic_done = State("picnic done", "Декстер видел, как я целовался с Рокси. Это не хорошо...")
        S_roxxy_dexter_basketball = State("dexter basketball", "Декстер точно захочет меня побить... Но я ни могу не ходить в школу!")
        S_roxxy_dexter_basketball_delay = State("dexter basketball delay", "Декстер видел, как я целовался с Рокси. Это не хорошо...")
        S_roxxy_basketball_challenge = State("basketball challenge", "Если я обыграю Декстера в его же игре, он точно оставит меня в покое, верно?")
        S_roxxy_fight_dexter_delay = State("fight dexter delay", "Это добром не кончится. Но он это заслужил.")
        S_roxxy_fight_dexter = State("fight dexter", "Теперь, когда я унизил его в баскетболе, Декстер точно захочет меня убить!")
        S_roxxy_end = State("end")


        S_roxxy_start.add(T_roxxy_teachers_berating, S_roxxy_teachers_event_delay)
        S_roxxy_teachers_event_delay.add(T_all_sleep, S_roxxy_teachers_event,
                                         actions = ["location", {"tod": [0,1], "place": L_school_floor3},
                                                    "force", {"tod": [0,1]},
                                                    ]
                                         )
        S_roxxy_teachers_event.add(T_roxxy_locker_room, S_roxxy_lockerroom_event_delay,
                                   actions = ["unforce", None]
                                   )
        S_roxxy_lockerroom_event_delay.add(T_all_sleep, S_roxxy_lockerroom_event,
                                           actions = ["exec", L_school_girlsroom.unlock,
                                                      "location", {"tod": [0,1], "place": L_school_girlsroom},
                                                      "force", {"tod": [0,1]},
                                                      ]
                                           )
        S_roxxy_lockerroom_event.add(T_roxxy_argument, S_roxxy_dexter_argument_delay,
                                     actions = ["clear", "left hallway lock",
                                                "unforce", None,
                                                ]
                                     )
        S_roxxy_dexter_argument_delay.add(T_all_sleep, S_roxxy_dexter_argument)
        S_roxxy_dexter_argument.add(T_roxxy_start_gymercise, S_roxxy_intense_gymercise)
        S_roxxy_intense_gymercise.add(T_roxxy_in_shower, S_roxxy_shower_event,
                                      actions = ["location", {"tod": [0,1], "place": L_school_shower},
                                                 "force", {"tod": [0,1]},
                                                 ]
                                      )
        S_roxxy_shower_event.add(T_roxxy_get_homework, S_roxxy_lolipop_delay,
                                 actions = ["unforce", None]
                                 )
        S_roxxy_lolipop_delay.add(T_all_sleep, S_roxxy_lolipop)
        S_roxxy_lolipop.add(T_roxxy_lolipop_lolipop, S_roxxy_lolipop_for_lolipop)
        S_roxxy_lolipop.add(T_roxxy_lolipop_once, S_roxxy_lolipop_just_once)
        S_roxxy_lolipop_for_lolipop.add(T_roxxy_confrontation, S_roxxy_dexter_confront_delay)
        S_roxxy_lolipop_just_once.add(T_roxxy_confrontation, S_roxxy_dexter_confront_delay)
        S_roxxy_dexter_confront_delay.add(T_all_sleep, S_roxxy_dexter_confront)
        S_roxxy_dexter_confront.add(T_roxxy_do_assignment, S_roxxy_assignment_delay, actions=["inc", "roxxy relationship"])
        S_roxxy_assignment_delay.add(T_all_sleep, S_roxxy_assignment)
        S_roxxy_assignment.add(T_roxxy_study_at_roxxy, S_roxxy_studying_at_roxxys, actions=["exec", L_trailerpark.unlock,
                                                                                            "location", [M_clyde, {"tod":None, "place":L_trailer_interior}],
                                                                                            "force", [M_clyde, {"flag":[True]*4}]])
        S_roxxy_studying_at_roxxys.add(T_roxxy_study_at_mcs, S_roxxy_studying_at_mcs)
        S_roxxy_studying_at_mcs.add(T_roxxy_get_cheerleader, S_roxxy_missing_outfit_delay, actions=["unforce", M_clyde])
        S_roxxy_missing_outfit_delay.add(T_all_sleep, S_roxxy_missing_outfit_delay2)
        S_roxxy_missing_outfit_delay2.add(T_all_sleep, S_roxxy_missing_outfit)
        S_roxxy_missing_outfit.add(T_roxxy_find_cheerleader_outfit, S_roxxy_get_cheerleader_outfit)
        S_roxxy_get_cheerleader_outfit.add(T_roxxy_confront_clyde, S_roxxy_beat_clyde)
        S_roxxy_beat_clyde.add(T_roxxy_beaten_clyde, S_roxxy_get_uniform_on_doggo)
        S_roxxy_get_uniform_on_doggo.add(T_roxxy_wait_in_her_room, S_roxxy_wait_in_her_room)
        S_roxxy_wait_in_her_room.add(T_roxxy_has_uniform, S_roxxy_return_to_school)
        S_roxxy_return_to_school.add(T_roxxy_returned_to_school, S_roxxy_dexter_alcohol_fight_delay, actions=["inc", "roxxy relationship"])
        S_roxxy_dexter_alcohol_fight_delay.add(T_all_sleep, S_roxxy_dexter_alcohol_fight, actions=["location", {"tod":0, "place":L_basketball_court}, 
                                                                                                   "force", {"tod": 0},
                                                                                                   "location", [M_dexter, {"tod":0, "place":L_basketball_court}],
                                                                                                   "force", [M_dexter, {"tod":0}]])
        S_roxxy_dexter_alcohol_fight.add(T_roxxy_go_to_basketball, S_roxxy_need_booze, actions=["unforce", None, "unforce", M_dexter])
        S_roxxy_need_booze.add(T_roxxy_get_beer, S_roxxy_get_fake_id, actions=['exec', L_pier.unlock, "clear", "talked to roxxy booze"])
        S_roxxy_get_fake_id.add(T_roxxy_ask_terry, S_roxxy_fake_id_ask_terry)
        S_roxxy_fake_id_ask_terry.add(T_roxxy_take_picture, S_roxxy_fake_id_get_picture)
        S_roxxy_fake_id_get_picture.add(T_roxxy_give_id, S_roxxy_trailer_park_trouble_delay)

        S_roxxy_trailer_park_trouble_delay.add(T_all_sleep, S_roxxy_trailer_park_trouble_delay2)
        S_roxxy_trailer_park_trouble_delay2.add(T_all_sleep, S_roxxy_trailer_park_trouble, actions=["set", "trailer foreclosed",
                                                                                                    "location", [M_crystal, {"place":L_police_basement}],
                                                                                                    "force", [M_crystal, {"tod":[0,1,2,3]}],
                                                                                                    "location", {"tod":2},
                                                                                                    "location", {"tod":3},
                                                                                                    "force", {"tod":[2,3]}])
        S_roxxy_trailer_park_trouble.add(T_roxxy_home_foreclosed, S_roxxy_check_trailer)
        S_roxxy_check_trailer.add(T_roxxy_checked_trailer, S_roxxy_confront_clyde)
        S_roxxy_confront_clyde.add(T_roxxy_confronted_clyde, S_roxxy_cookies_and_milk)
        S_roxxy_cookies_and_milk.add(T_roxxy_go_to_police, S_roxxy_ask_earl_release, actions=["exec", L_police_lobby.unlock])
        S_roxxy_ask_earl_release.add(T_roxxy_talk_to_crystal, S_roxxy_talk_to_crystal)
        S_roxxy_talk_to_crystal.add(T_roxxy_find_evidence, S_roxxy_get_evidence, actions=["exec", L_trailer_shack_interior.unlock])
        S_roxxy_get_evidence.add(T_roxxy_sell_meth, S_roxxy_selling_meth_ask_roxxy)
        S_roxxy_selling_meth_ask_roxxy.add(T_roxxy_meth_asked_roxxy, S_roxxy_selling_meth)
        S_roxxy_selling_meth.add(T_roxxy_meet_clyde, S_roxxy_meeting_clyde)
        S_roxxy_meeting_clyde.add(T_roxxy_meet_buyer, S_roxxy_meeting_buyer)
        S_roxxy_meeting_buyer.add(T_roxxy_drug_deal_over, S_roxxy_shut_down_lab)
        S_roxxy_shut_down_lab.add(T_roxxy_failing_exams, S_roxxy_hows_it_going_delay, actions=["clear", "trailer foreclosed", 
                                                                                          "unforce", None,
                                                                                          "unforce", M_crystal,
                                                                                          "location", [M_clyde, {"place":L_NULL}],
                                                                                          "force", [M_clyde, {"flag":[True]*4}]])

        S_roxxy_hows_it_going_delay.add(T_all_sleep, S_roxxy_hows_it_going_delay2)
        S_roxxy_hows_it_going_delay2.add(T_all_sleep, S_roxxy_hows_it_going_delay3)
        S_roxxy_hows_it_going_delay3.add(T_all_sleep, S_roxxy_hows_it_going)
        S_roxxy_hows_it_going.add(T_roxxy_chat_with_becca_missy, S_roxxy_chat_with_becca_missy)
        S_roxxy_chat_with_becca_missy.add(T_roxxy_get_goldenschwagger, S_roxxy_spin_bottle)
        S_roxxy_spin_bottle.add(T_roxxy_spun_bottle, S_roxxy_ask_exam_copy_delay)

        S_roxxy_ask_exam_copy_delay.add(T_all_sleep, S_roxxy_ask_exam_copy)
        S_roxxy_ask_exam_copy.add(T_roxxy_find_exams, S_roxxy_sneak_into_smith, actions=["exec", L_smith_front.unlock])
        S_roxxy_sneak_into_smith.add(T_roxxy_escaped_smith, S_roxxy_give_exams_delay)
        S_roxxy_give_exams_delay.add(T_all_sleep, S_roxxy_give_exams)
        S_roxxy_give_exams.add(T_roxxy_gave_exams, S_roxxy_dexter_flirt_delay)
        S_roxxy_dexter_flirt_delay.add(T_all_sleep, S_roxxy_dexter_flirt)
        S_roxxy_dexter_flirt.add(T_roxxy_help_dewitt, S_roxxy_go_in_auditorium)
        S_roxxy_go_in_auditorium.add(T_roxxy_invitation_bikini, S_roxxy_invite_to_bikini_contest, actions=["location", {"place":L_beach_water, "dow":6},
                                                                                                           "location", {"place":L_beach_water, "dow":5},
                                                                                                           "force", {"tod":[0,1]}])

        S_roxxy_invite_to_bikini_contest.add(T_roxxy_go_see_contest, S_roxxy_go_see_contest)
        S_roxxy_go_see_contest.add(T_roxxy_check_on_roxxy, S_roxxy_check_on_roxxy)
        S_roxxy_check_on_roxxy.add(T_roxxy_go_to_cabin, S_roxxy_in_cabin)
        S_roxxy_in_cabin.add(T_roxxy_bikini_failure, S_roxxy_get_new_bikini)
        S_roxxy_get_new_bikini.add(T_roxxy_get_oil, S_roxxy_get_oil)
        S_roxxy_get_oil.add(T_roxxy_contest_over, S_roxxy_do_pushups_delay, actions = ["unforce", None])
        S_roxxy_do_pushups_delay.add(T_all_sleep, S_roxxy_do_pushups_intro)
        S_roxxy_do_pushups_intro.add(T_roxxy_dexter_challenge_pushups, S_roxxy_do_pushups)
        S_roxxy_do_pushups.add(T_roxxy_beaten_dexter_pushups, S_roxxy_trailer_park_romance_delay)
        S_roxxy_trailer_park_romance_delay.add(T_all_sleep, S_roxxy_trailer_park_romance)
        S_roxxy_trailer_park_romance.add(T_roxxy_accepted_picnic, S_roxxy_go_to_picnic)
        S_roxxy_go_to_picnic.add(T_roxxy_picnic_done, S_roxxy_picnic_done)
        S_roxxy_picnic_done.add(T_roxxy_kissed, S_roxxy_dexter_basketball_delay, actions=["unforce", M_clyde, "inc", "roxxy relationship"])
        S_roxxy_dexter_basketball_delay.add(T_all_sleep, S_roxxy_dexter_basketball)
        S_roxxy_dexter_basketball.add(T_roxxy_basket_challenged, S_roxxy_basketball_challenge)
        S_roxxy_basketball_challenge.add(T_roxxy_humiliated_dexter, S_roxxy_fight_dexter_delay)
        S_roxxy_fight_dexter_delay.add(T_all_sleep, S_roxxy_fight_dexter)
        S_roxxy_fight_dexter.add(T_roxxy_ninja_dexter, S_roxxy_end, actions=["inc", "roxxy relationship"])


        S_roxxy_end.add(T_roxxy_trailer_sex, S_roxxy_end,
                        actions = ["inc", "roxxy trailer sex",
                                   "exec", A_the_man.unlock,
                                   ]
                        )
        S_roxxy_end.add(T_roxxy_beach_sex, S_roxxy_end,
                        actions = ["inc", "roxxy beach sex"]
                        )
        S_roxxy_end.add(T_roxxy_locker_sex, S_roxxy_end,
                        actions = ["inc", "roxxy locker sex",
                                   "clear", "meet for locker sex",
                                   ]
                        )
        S_roxxy_end.add(T_roxxy_crystal_sex, S_roxxy_end,
                        actions = ["inc", "roxxy crystal sex"]
                        )

        M_roxxy.add(S_roxxy_start, S_roxxy_teachers_event_delay, S_roxxy_teachers_event, S_roxxy_lockerroom_event_delay, 
                    S_roxxy_lockerroom_event, S_roxxy_dexter_argument_delay, S_roxxy_dexter_argument, S_roxxy_shower_event,
                    S_roxxy_lolipop, S_roxxy_dexter_confront, S_roxxy_intense_gymercise, S_roxxy_lolipop_delay,
                    S_roxxy_lolipop_for_lolipop, S_roxxy_lolipop_just_once, S_roxxy_dexter_confront_delay,
                    S_roxxy_assignment_delay, S_roxxy_assignment, S_roxxy_studying_at_roxxys, S_roxxy_studying_at_mcs,
                    S_roxxy_missing_outfit, S_roxxy_missing_outfit_delay, S_roxxy_missing_outfit_delay2, 
                    S_roxxy_get_cheerleader_outfit, S_roxxy_beat_clyde, S_roxxy_get_uniform_on_doggo, S_roxxy_wait_in_her_room,
                    S_roxxy_get_fake_id, S_roxxy_fake_id_ask_terry, S_roxxy_return_to_school,
                    S_roxxy_dexter_alcohol_fight, S_roxxy_dexter_alcohol_fight_delay, S_roxxy_need_booze,
                    S_roxxy_fake_id_get_picture, S_roxxy_trailer_park_trouble, S_roxxy_get_evidence,
                    S_roxxy_trailer_park_trouble_delay, S_roxxy_trailer_park_trouble_delay2,
                    S_roxxy_check_trailer, S_roxxy_confront_clyde, S_roxxy_cookies_and_milk, S_roxxy_ask_earl_release,
                    S_roxxy_talk_to_crystal, S_roxxy_selling_meth, S_roxxy_selling_meth_ask_roxxy, S_roxxy_meeting_buyer,
                    S_roxxy_meeting_clyde, S_roxxy_shut_down_lab, S_roxxy_hows_it_going_delay, S_roxxy_hows_it_going_delay2,
                    S_roxxy_hows_it_going_delay3, S_roxxy_hows_it_going, S_roxxy_chat_with_becca_missy, S_roxxy_spin_bottle,
                    S_roxxy_ask_exam_copy_delay, S_roxxy_give_exams_delay, S_roxxy_dexter_flirt_delay, S_roxxy_go_in_auditorium,
                    S_roxxy_ask_exam_copy, S_roxxy_sneak_into_smith, S_roxxy_give_exams, S_roxxy_dexter_flirt,
                    S_roxxy_invite_to_bikini_contest, S_roxxy_get_new_bikini, S_roxxy_do_pushups, S_roxxy_picnic_done,
                    S_roxxy_do_pushups_delay, S_roxxy_do_pushups_intro, S_roxxy_trailer_park_romance_delay, S_roxxy_go_to_picnic,
                    S_roxxy_go_see_contest, S_roxxy_check_on_roxxy, S_roxxy_in_cabin, S_roxxy_get_oil,
                    S_roxxy_basketball_challenge, S_roxxy_dexter_basketball_delay, S_roxxy_fight_dexter_delay,
                    S_roxxy_trailer_park_romance, S_roxxy_fight_dexter, S_roxxy_dexter_basketball, S_roxxy_end)
        M_roxxy.add_action(T_all_sleep, ["clear", "massage",
                                         "clear", "meet for locker sex",
                                         ]
        )
    return

label roxxy_machine_init:
    python:
        M_roxxy = Machine("roxxy", default_loc = [[L_school_frenchclassroom, L_school_frenchclassroom, L_trailer_bedroom, L_trailer_bedroom],
                                                  [L_trailer_interior, L_trailer_interior, L_beach_water, L_NULL]
                                                  ],
                          vars = {"sex speed": .3,
                                  "roxxy relationship": 0, 
                                  "left hallway lock": False,
                                  "dexter argument got information": False,
                                  "get erik clothes" : False,
                                  "heard clyde in trailer" : False,
                                  "lost shooting": False,
                                  "alcohol talked to eve": False,
                                  "talked to roxxy booze": False,
                                  "talked to roxxy id": False,
                                  "take roxxy mall": False,
                                  "talked to terry": False,
                                  "trailer foreclosed": False,
                                  "talked to harold": False,
                                  "caught by smith": False,
                                  "massage": False,
                                  "done basketball": False,
                                  "basketball unlocked": False,
                                  "shower event intro done" : False,
                                  "roxxy trailer sex": 0,
                                  "roxxy trailer sex first": True,
                                  "roxxy beach sex": 0,
                                  "roxxy locker sex": 0,
                                  "roxxy locker sex first": True,
                                  "meet for locker sex": False,
                                  "roxxy crystal sex": 0,
                                  },
        )
        M_roxxy.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
