label mia_triggers_init:
    python:

        T_mia_on_zero = Trigger("advance", "Задержка Мии")
        T_mia_kiss = Trigger("kiss", "Поцелуй Мии во время учебы")
        T_mia_kicked_out = Trigger("kicked out", "Выгнали из дома Мии ")
        T_mia_plan = Trigger("plan", "План с Мией")
        T_mia_results = Trigger("results", "Узнайте результаты с Мия")
        T_mia_delay = Trigger("delay", "Задержка запуска сюжета")
        T_mia_tattoo_start = Trigger("tattoo start", "Начните процесс, помогая Мия получить татуировку")
        T_mia_easel_found = Trigger("easel", "Нашел мольберт, чтобы сделать татуировку для Мии")
        T_mia_visit = Trigger("visit", "Посетите и поговорите с Мией")
        T_mia_wrong_tattoo = Trigger("wrong tattoo", "Мии не нравится татуировка, которую ты нарисовал")
        T_mia_right_tattoo = Trigger("right tattoo", "Мии понравилось тату, которые вы нарисовали")
        T_mia_visit_tattoo_parlor = Trigger("visit tattoo", "Идите с Миа в тату-салон")
        T_mia_tattoo_done = Trigger("tattoo done", "Мия восстала и имеет новую татуировку")
        T_mia_night_invite = Trigger("night invite", "Мия приглашает вас на ночь")
        T_mia_strip_tease = Trigger("strip tease", "Мия сделала вам хороший стриптиз-шоу")
        T_mia_afterthought = Trigger("afterthought", "Мысли о том, что вас выгнали из дома Мии")
        T_mia_grounded = Trigger("grounded", "Мия обосновала после того, как была поймана")
        T_mia_delay_progress = Trigger("delay progress", "Есть задержка в истории Мия")
        T_mia_message = Trigger("message", "Мия просит вас срочно ей помочь")
        T_mia_key_found = Trigger("key found", "Нашел ключ к запертой комнате Хелен")
        T_mia_rescue = Trigger("rescue", "Спасти Миа от связки")
        T_mia_concerned = Trigger("concerned", "Вы беспокоитесь о Миа не связавшись ней")
        T_mias_request = Trigger("request", "Миа спрашивает о том, что вы пытаетесь поговорить с Хелен")
        T_mia_helen_deny = Trigger("helen deny", "Хелен отказывается говорить с вами")
        T_mia_church_mention = Trigger("church mention", "Миа упоминает, что Хелен только слушает Бога или Церковь")
        T_mia_priest_outfit = Trigger("priest outfit", "Одолжите наряд священника, чтобы замаскировать себя")
        T_mia_thanks = Trigger("thanks", "Мия благодарит вас за помощь")
        T_mia_clues_summary = Trigger("clues summary", "Вы обобщили подсказки, которые вы собрали до сих пор.")
        T_mia_give_news = Trigger("give news", "Расскажи Мии новости, которые узнал")
        T_mia_gives_glasses = Trigger("gives glasses", "МИА дает тебе очки для своего отца")
        T_mia_dinner_plan = Trigger("dinner plan", "У Мии есть план, как уговорить Гарольда и Хелен поужинать.")
        T_mia_route = Trigger("route", "Это устанавливает вас постоянно на маршрут Мии")
        T_mia_family_reunion = Trigger("family reunion", "Мия воссоединяется с Гарольдом и Хелен для возвращения вместе")
        T_mia_sex = Trigger("sex", "Мия занимается с тобой сексом")
        T_mia_stay_alone = Trigger("stay alone", "Миа хочет остаться одна после того, как ее родители ушли навсегда")
    return

label mia_fsm_init:
    python:

        S_mia_start = State("start", "Приветствуя его")
        S_mia_do_homework = State("homework", "Ожидает Гг, чтобы сделать домашнюю работу")
        S_mia_wait_homework = State("show hw", "Ожидает Гг, который принесет готовую домашнюю работу")
        S_mia_parent_blocking = State("blocked", "Хелен запрещает вам видится с Мией")
        S_mia_consult = State("consult", "Проконсультируйтесь с Мией, чтобы снова иметь возможность проводить ночные учебные занятия")
        S_mia_impress_harold = State("impress", "Произведите впечатление на Гарольда, найдя его любимый пончик")
        S_mia_parent_unblock = State("unbanned", "Узнайте от Мии, разрешил ли её отец видется с Мией")
        S_mia_tattoo_help = State("tattoo", "Помогите Мии сделать татуировку")
        S_mia_find_easel = State("easel", "Find an easel to draw a tattoo for Mia")
        S_mia_draw_tattoo = State("draw tattoo", "Нарисуй татуировку для Мии")
        S_mia_show_tattoo = State("show tattoo", "Покажи Мии татуировку, которую вы нарисовали")
        S_mia_get_tattoo = State("get tattoo", "Иди с Мией, чтобы сделать татуировку")
        S_mia_buy_tattoo = State("buy tattoo", "Смотрии как Мии наносят её татуировку")
        S_mia_return_favor = State("return favor", "Мия хочет одолжения, чтобы вы помогли ей с её татуировкой")
        S_mia_night_visit = State("night visit", "Мия пригласила тебя на тайный ночной визит")
        S_mia_night_visit_afterthought = State("night visit afterthought", "Я должна пройтись по сегодняшним событиям в своей комнате") #Изменить перевод
        S_mia_strip_aftermath = State("strip aftermath", "Поговорите с Мией, чтобы узнать, что произошло после того, как её поймали")
        S_mia_midnight_call = State("midnight call", "Мия отправила тебе сообщение")
        S_mia_midnight_help = State("rescue", "Иди к Мии и узнай, зачем ей нужна помощь")
        S_mia_locked_room = State("locked room", "Войдите в секретную запертую комнату")
        S_mia_need_space = State("need space", "Лучше оставить Мию и её родителей в покое")
        S_mia_concerning_visit = State("concerning visit", "Вы решили навестить Мию, так как ничего от неё не слышали")
        S_mia_helen_fight = State("helen fight", "МИА подралась с Хелен")
        S_mia_helen_talk = State("helen talk", "Мия попросила тебя поговорить с Хелен")
        S_mia_helen_refusal = State("helen refusal", "Хелен отказалась говорить с тобой")
        S_mia_church_plan = State("church plan", "Сходи в церковь, посмотри, есть ли способ убедить Хелен")
        S_mia_convince_helen = State("convince helen", "Иди на исповедальню, поговори с Хелен")
        S_mia_priest_act = State("priest act", "Выступите в качестве священника, чтобы попытаться убедить Хелен")
        S_mia_return_priest_outfit = State("return priest outfit", "Верните костюм священника в покои монахини")
        S_mia_nun_thoughts = State("nun thoughts", "Вы идете по затруднительному положению монахиня поставила вас наместо")
        S_mia_helen_change_news = State("helen change news", "Скажи Мии хорошие новости, что Хелен готова измениться")
        S_mia_waiting_for_harold = State("waiting for harold", "Мия и Хелен ждут возвращения Гарольда")
        S_mia_urgent_message = State("urgent message", "Вы просыпаетесь со срочным сообщением от Мии")
        S_mia_urgent_help = State("urgent help", "Мии срочно нужна помощь в поисках Гарольда")
        S_mia_clues = State("clues", "Ищите подсказки, куда исчез Гарольд")
        S_mia_search_desk = State("search desk", "Найдите стол Гарольда для подсказок")
        S_mia_find_harold = State("find harold", "Ищите Гарольда на холме Воронов")
        S_mia_harold_found_news = State("harold found news", "Вернись и сообщи, что Гарольд в порядке")
        S_mia_angelicas_patience = State("angelicas patience", "Анжелика ждет вашего конца сделки")
        S_mia_angelicas_impatience = State("angelicas impatience", "Анжелика решила навестить вас, чтобы напомнить о вашей сделке")
        S_mia_church_night_visit = State("church night visit", "Вы посещаете церковь ночью, как Анжелика сказала вам")
        S_mia_find_sinners = State("find sinners", "Анжелика хочет, чтобы вы нашли грешников для её таинства")
        S_mia_church_sacrement = State("church sacrement", "Отправляйтесь с Хелен в церковь, чтобы совершить первое таинство")
        S_mia_glasses_favor = State("glasses favor", "Мия хочет вас попросить об одолжении, чтобы вы вернули её папины очки")
        S_mia_harold_gift = State("glasses gift", "Перейдите к Гарольду, чтобы отдать ему его очки")
        S_mia_inmate_status = State("inmate status", "Гарольду нужна обновленная информация о переводе заключенного")
        S_mia_harold_backup = State("harold backup", "Скажи Гарольду, что ему нужно прикрытие")
        S_mia_harold_to_the_rescue = State("harold to the rescue", "Гарольд приходит на помощь Юми")
        S_mia_harold_yumi_out = State("harold yumi out", "Гарольд и Юми взять остальную часть дня")
        S_mia_unexpected_visit = State("unexpected visit", "Вы платите Мии за неожиданный визит")
        S_mia_helen_outfit_request = State("helen outfit request", "Хелен попросила вас купить ей сексуальное белье")
        S_mia_angelicas_delay = State("angelicas delay", "Анжелика свяжется с вами утром")
        S_mia_angelicas_home_visit = State("angelicas home visit", "Анжелика посещает ваш дом, чтобы рассказать вам часть 2-го своего таинства")
        S_mia_angelicas_order = State("angelicas order", "Анжелика приказала вам приобрести хлыст для неё")
        S_mia_angelicas_whip = State("angelicas whip", "Анжелика требует хлыст")
        S_mia_helen_condition = State("helen condition", "Вы беспокоитесь о состоянии Хелен после порки")
        S_mia_favor = State("favor", "У Мии есть к вам просьба")
        S_mia_convince_harold = State("convince harold", "Вам нужно попытаться убедить Гарольда пойти поужинать с Мией и Хелен")
        S_mia_stolen_goods = State("stolen goods", "Гарольд должен найти украденные товары вора для продвижения по службе")
        S_mia_return_goods = State("return goods", "Вы должны вернуть украденное Гарольду")
        S_mia_angelicas_final_delay = State("angelicas final delay", "Анжелика свяжется с вами утром")
        S_mia_angelicas_final_home_visit = State("angelicas final home visit", "Анжелика приходит к вам домой, чтобы рассказать последнюю часть своего таинства")
        S_mia_harolds_thoughts = State("harolds thoughts", "Вы хотите спросить Гарольда о его связи с Хелен, прежде чем сделать последнее причастие")
        S_mia_angelicas_final_request = State("angelicas final request", "Вы решили прислушаться к последней просьбе Анжелики")
        S_mia_helens_final_sacrament = State("helens final sacrament", "Сейчас вы посещаете последнее причастие Хелен")
        S_mia_route_split = State("route split", "Разрыв, чтобы определить, если вы идете с Мией или с Хелен")
        S_mia_study_sex = State("study sex", "Мия предложила попробовать заниматься сексом")
        S_mia_end = State("end", "Конец маршрута Мии")

        S_mia_start.add(T_all_school_entrance, S_mia_do_homework,
                        actions = ["assign", ["homework", 1],
                                   "exec", L_miahouse.unlock,
                                   "location", {"place": L_miahouse},
                                   "force", {"tod": 1},
                                   ],
                        )
        S_mia_do_homework.add(T_mc_homework, S_mia_do_homework,
                              actions = ["triggerOnZero", ["homework", T_mia_on_zero],],
                              )
        S_mia_do_homework.add(T_mia_on_zero, S_mia_wait_homework,
                              actions = ["clear", "front door locked",
                                         "inc", "progress count",
                                         "unforce", None,
                                         ],
                              )
        S_mia_wait_homework.add(T_mia_kiss, S_mia_parent_blocking,
                                actions = ["set", "study",
                                           "inc", "progress count",],
                                )
        S_mia_parent_blocking.add(T_mia_kicked_out, S_mia_consult)
        S_mia_consult.add(T_mia_plan, S_mia_impress_harold,
                          actions = ["set", "buy donuts",
                                     "exec", L_donutshop.unlock,
                                     ],
                          )
        S_mia_impress_harold.add(T_harold_donuts, S_mia_parent_unblock)
        S_mia_parent_unblock.add(T_mia_results, S_mia_tattoo_help,
                                 actions = ["inc", "progress count"]
                                 )
        S_mia_tattoo_help.add(T_mia_delay, S_mia_tattoo_help,
                                 actions = ["set", "story delay"]
                                 )
        S_mia_tattoo_help.add(T_mia_tattoo_start, S_mia_find_easel,
                              actions = ["clear", "story delay"]
                              )
        S_mia_find_easel.add(T_mia_easel_found, S_mia_draw_tattoo)
        S_mia_draw_tattoo.add(T_mia_visit, S_mia_show_tattoo)
        S_mia_show_tattoo.add(T_mia_wrong_tattoo, S_mia_draw_tattoo)
        S_mia_show_tattoo.add(T_mia_right_tattoo, S_mia_get_tattoo,
                              actions = ["inc", "progress count",
                                         "exec", L_tattooparlor.unlock,
                                         "location", {"place": L_tattooparlor_interior,
                                                      "dow": 5,
                                                      },
                                         "force", {"tod": [0,1]},
                                         ],
                              )
        S_mia_get_tattoo.add(T_mia_visit_tattoo_parlor, S_mia_buy_tattoo)
        S_mia_buy_tattoo.add(T_mia_tattoo_done, S_mia_return_favor,
                             actions = ["unforce", None]
                             )
        S_mia_return_favor.add(T_mia_night_invite, S_mia_night_visit)
        S_mia_night_visit.add(T_mia_strip_tease, S_mia_strip_aftermath,
                              actions = ["inc", "progress count",]
                              )
        S_mia_strip_aftermath.add(T_mia_grounded, S_mia_midnight_call,
                                  actions = ["clear", "story delay",
                                             "exec", game.lock_sleep,
                                             ],
                                  )
        S_mia_midnight_call.add(T_mia_message, S_mia_midnight_help,
                                actions = ["location", {"place": L_miahouse_lockedroom},
                                           "force", {"tod": [2,3]},
                                           "location", [M_helen, {"place": L_NULL}],
                                           "force", [M_helen, {"tod": 3}],
                                           ],
                                )
        S_mia_midnight_help.add(T_mia_key_found, S_mia_locked_room,
                                actions = ["clear", "helens locked room locked"]
                                )
        S_mia_locked_room.add(T_mia_rescue, S_mia_need_space,
                              actions = ["assign", ["Trigger delay", 4],
                                         "inc", "progress count",
                                         "unforce", None,
                                         "unforce", M_helen,
                                         ],
                              )
        S_mia_need_space.add(T_all_sleep, S_mia_need_space,
                             actions = ["triggerOnZero", ["Trigger delay", T_mia_concerned]]
                             )
        S_mia_need_space.add(T_mia_concerned, S_mia_concerning_visit)
        S_mia_concerning_visit.add(T_harold_leaves, S_mia_helen_fight,
                                   actions = ["set", "harold left",
                                              "location", [M_helen, {"place": L_miahouse_helensbedroom}],
                                              "force", [M_helen, {"tod": [2,3]}],
                                              "location", [M_harold, {"place": [[L_police_office, L_police_office, L_NULL, L_NULL], [L_police_office, L_police_office, L_NULL, L_NULL]]}],
                                              "force", [M_harold, {"flag": True}],
                                              ],
                                   )
        S_mia_helen_fight.add(T_mias_request, S_mia_helen_talk)
        S_mia_helen_talk.add(T_mia_helen_deny, S_mia_helen_refusal,
                             actions = ["set", "helen button",
                                        "set", "helen button change",
                                        ],
                             )
        S_mia_helen_refusal.add(T_mia_church_mention, S_mia_church_plan,
                                actions = ["inc", "progress count"]
                                )
        S_mia_church_plan.add(T_mia_priest_outfit, S_mia_convince_helen)
        S_mia_convince_helen.add(T_helen_confessional, S_mia_priest_act,
                                 actions = ["location", [M_helen, {"place": L_NULL}],
                                            "force", [M_helen, {"flag": True}],
                                            ],
                                 )
        S_mia_priest_act.add(T_helen_convince_fail, S_mia_church_plan,
                             actions = ["location", [M_helen, {"place": L_miahouse_helensbedroom}],
                                        "force", [M_helen, {"tod": [2,3]}],
                                        ],
                             )
        S_mia_priest_act.add(T_helen_convince_change, S_mia_return_priest_outfit,
                             actions = ["set", "helen dialogue change",
                                        "location", [M_helen, {"place": L_miahouse_helensbedroom}],
                                        "force", [M_helen, {"tod": [2,3]}],
                                        ],
                             )
        S_mia_return_priest_outfit.add(T_mia_priest_outfit, S_mia_nun_thoughts,
                             actions = ["clear", "helen button change"]
                             )
        S_mia_nun_thoughts.add(T_mc_nun_thoughts, S_mia_helen_change_news,
                               actions = ["inc", "progress count"]
                               )
        S_mia_helen_change_news.add(T_mia_thanks, S_mia_waiting_for_harold,
                                    actions = ["assign", ["Trigger delay", 3]]
                                    )
        S_mia_waiting_for_harold.add(T_all_sleep, S_mia_waiting_for_harold,
                                     actions = ["triggerOnZero", ["Trigger delay", T_mia_on_zero]]
                                     )
        S_mia_waiting_for_harold.add(T_mia_on_zero, S_mia_urgent_message,
                                     actions = ["inc", "progress count", "exec", game.lock_sleep]
                                     )
        S_mia_urgent_message.add(T_mia_message, S_mia_urgent_help,
                                 actions = ["location", [M_harold, {"place": L_hill}],],
                                 )
        S_mia_urgent_help.add(T_harold_missing, S_mia_clues)
        S_mia_clues.add(T_mia_clues_summary, S_mia_search_desk,
                        actions = ["clear", "questioned yumi",
                                   "clear", "questioned earl",
                                   ],
                        )
        S_mia_search_desk.add(T_harold_photo_clue, S_mia_find_harold)
        S_mia_find_harold.add(T_harold_found, S_mia_harold_found_news)
        S_mia_harold_found_news.add(T_mia_give_news, S_mia_angelicas_patience,
                                    actions = ["assign", ["Trigger delay", 3],
                                               "inc", "progress count",
                                               "location", [M_harold, {"place": [[L_police_office, L_police_office, L_NULL, L_NULL], [L_police_office, L_police_office, L_NULL, L_NULL]]}],
                                               ],
                                    )
        S_mia_angelicas_patience.add(T_all_sleep, S_mia_angelicas_patience,
                                     actions = ["triggerOnZero", ["Trigger delay", T_mia_on_zero]]
                                     )
        S_mia_angelicas_patience.add(T_mia_on_zero, S_mia_angelicas_impatience)
        S_mia_angelicas_impatience.add(T_angelica_house_visit, S_mia_church_night_visit,
                                       actions = ["clear", "church night locked"]
                                       )
        S_mia_church_night_visit.add(T_angelica_ritual_deal, S_mia_find_sinners)
        S_mia_find_sinners.add(T_helen_secret_sacrement, S_mia_church_sacrement,
                               actions = ["inc", "progress count"]
                               )
        S_mia_church_sacrement.add(T_helen_angelica_ritual, S_mia_glasses_favor,
                                   actions = ["set", "helen angelica training",
                                              "set", "church night locked"]
                                   )
        S_mia_glasses_favor.add(T_mia_gives_glasses, S_mia_harold_gift)
        S_mia_harold_gift.add(T_harold_glasses, S_mia_inmate_status,
                              actions = ["set", "harold left",
                                         "location", [M_yumi, {"place":L_NULL}],
                                         "force", [M_yumi, {"flag": True}],
                                         "location", [M_earl, {"place":L_NULL}],
                                         "force", [M_earl, {"flag": True}],
                                         ],
                              )
        S_mia_inmate_status.add(T_yumi_backup_request, S_mia_harold_backup)
        S_mia_harold_backup.add(T_harold_grows_a_pair, S_mia_harold_to_the_rescue)
        S_mia_harold_to_the_rescue.add(T_harold_backup, S_mia_harold_yumi_out,
                                       actions = ["location", [M_harold, {"place": L_NULL}],
                                                  "unforce", M_earl,
                                                  ],
                                       )
        S_mia_harold_yumi_out.add(T_all_sleep, S_mia_unexpected_visit,
                                  actions = ["inc", "progress count",
                                             "location", {"place": L_NULL},
                                             "force", {"tod": [1,2,3]},
                                             "force", [M_helen, {"tod": [1,2,3]}],
                                             "location", [M_harold, {"place": [[L_police_office, L_police_office, L_NULL, L_NULL], [L_police_office, L_police_office, L_NULL, L_NULL]]}],
                                             "unforce", M_yumi,
                                             ],
                                  )
        S_mia_unexpected_visit.add(T_helen_caught_masturbating, S_mia_helen_outfit_request)
        S_mia_helen_outfit_request.add(T_helen_sexy_lingerie, S_mia_angelicas_delay,
                                       actions = ["unforce", None,
                                                  "force", [M_helen, {"tod": [2,3]}],
                                                  ],
                                       )
        S_mia_angelicas_delay.add(T_all_sleep, S_mia_angelicas_home_visit)
        S_mia_angelicas_home_visit.add(T_angelica_requires_whip, S_mia_angelicas_order,
                                       actions = ["clear", "church night locked",
                                                  "location", [M_helen, {"place": L_church_angelica}],
                                                  ],
                                       )
        S_mia_angelicas_order.add(T_angelica_sinful_thoughts, S_mia_angelicas_whip,
                                  actions = ["set", "helen angelica training 2",],
                                  )
        S_mia_angelicas_whip.add(T_helen_torture, S_mia_helen_condition,
                                 actions = ["inc", "progress count",
                                            "location", [M_helen, {"condition": "M_mia.is_set('helen angelica training 2')"}],
                                            ],
                                 )
        S_mia_helen_condition.add(T_helen_thanks, S_mia_favor)
        S_mia_favor.add(T_mia_dinner_plan, S_mia_convince_harold)
        S_mia_convince_harold.add(T_harold_find_goods, S_mia_stolen_goods,
                                  actions = ["condition", ["M_mia.is_set('stolen goods recovered')", ["trigger", T_harold_found_goods], []]]
                                  )
        S_mia_stolen_goods.add(T_harold_found_goods, S_mia_return_goods,
                               actions = ["set", "stolen goods recovered"]
                               )
        S_mia_return_goods.add(T_harold_promotion, S_mia_angelicas_final_delay,
                               actions = ["inc", "progress count"]
                               )
        S_mia_angelicas_final_delay.add(T_all_sleep, S_mia_angelicas_final_home_visit)
        S_mia_angelicas_final_home_visit.add(T_angelica_strapon_request, S_mia_harolds_thoughts)
        S_mia_harolds_thoughts.add(T_harold_indecisiveness, S_mia_angelicas_final_request)
        S_mia_angelicas_final_request.add(T_angelicas_final_ritual, S_mia_helens_final_sacrament,
                                          actions = ["inc", "progress count"]
                                          )
        S_mia_helens_final_sacrament.add(T_mia_route, S_mia_route_split,
                                         actions = ["set", "mia route",
                                                    "clear", "harold left",
                                                    "clear", "helen angelica training",
                                                    "clear", "helen angelica training 2",
                                                    "unforce", M_helen,
                                                    "unforce", M_harold,
                                                    ],
                                         )


        S_mia_route_split.add(T_mia_family_reunion, S_mia_study_sex)
        S_mia_study_sex.add(T_mia_sex, S_mia_end,
                            actions = ["inc", "progress count", "exec", A_not_a_prude.unlock]
                            )


        M_mia.add(S_mia_start, S_mia_do_homework, S_mia_wait_homework,
                  S_mia_parent_blocking, S_mia_consult, S_mia_impress_harold,
                  S_mia_parent_unblock, S_mia_tattoo_help,
                  S_mia_find_easel, S_mia_draw_tattoo, S_mia_show_tattoo,
                  S_mia_get_tattoo, S_mia_buy_tattoo, S_mia_return_favor,
                  S_mia_night_visit, S_mia_night_visit_afterthought, S_mia_strip_aftermath,
                  S_mia_midnight_call, S_mia_midnight_help, S_mia_locked_room,
                  S_mia_need_space, S_mia_concerning_visit, S_mia_helen_fight,
                  S_mia_helen_talk, S_mia_helen_refusal, S_mia_church_plan,
                  S_mia_convince_helen, S_mia_priest_act,
                  S_mia_return_priest_outfit, S_mia_nun_thoughts,
                  S_mia_helen_change_news, S_mia_waiting_for_harold,
                  S_mia_urgent_message, S_mia_urgent_help, S_mia_clues,
                  S_mia_search_desk, S_mia_find_harold,
                  S_mia_harold_found_news, S_mia_angelicas_patience,
                  S_mia_angelicas_impatience, S_mia_church_night_visit,
                  S_mia_find_sinners, S_mia_church_sacrement,
                  S_mia_glasses_favor, S_mia_harold_gift, S_mia_inmate_status,
                  S_mia_harold_backup, S_mia_harold_to_the_rescue,
                  S_mia_harold_yumi_out, S_mia_unexpected_visit,
                  S_mia_helen_outfit_request, S_mia_angelicas_delay,
                  S_mia_angelicas_home_visit, S_mia_angelicas_order,
                  S_mia_angelicas_whip, S_mia_helen_condition, S_mia_favor,
                  S_mia_convince_harold, S_mia_stolen_goods,
                  S_mia_return_goods, S_mia_angelicas_final_delay,
                  S_mia_angelicas_final_home_visit, S_mia_harolds_thoughts,
                  S_mia_angelicas_final_request, S_mia_helens_final_sacrament,
                  S_mia_route_split, S_mia_study_sex, S_mia_end
        )
    return

label mia_machine_init:
    python:
        M_mia = Machine("mia", default_loc=[[L_school_scienceclassroom, L_miahouse_entrance, L_miahouse_miaroom, L_miahouse_miaroom],
                            [L_church, L_miahouse_entrance, L_miahouse_miaroom, L_miahouse_miaroom]],
                        vars = {
                            'progress count': 0,
                            'progress mark': 2,
                            'progress max': 16,
                            'front door locked': True,
                            'telescope teddy seen': False,
                            'study': False,
                            'buy donuts': False,
                            'story delay': False,
                            'helens locked room locked': True,
                            'harold left': False,
                            'helen button': False,
                            'helen button change': False,
                            'helen dialogue change': False,
                            'questioned yumi': False,
                            'questioned earl': False,
                            'church night locked': True,
                            'helen angelica training': False,
                            'helen angelica training 2': False,
                            'stolen goods recovered': False,
                            'mia route': False,
                            'sex speed': .175,
                            'sex 1st choice': "",
                            'cum 1st choice': "",
                            'anal sex': False,
                            'vaginal sex': False,
                            'butt speed': 0,
                            'reminded study': False,
                            },
        )
        M_mia.set_priority(1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
