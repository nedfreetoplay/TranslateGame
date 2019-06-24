init python:

    T_bissette_improvement_challenge = Trigger("improvement challenge", "Стандарт")
    T_bissette_challenge_thoughts = Trigger("challenge thoughts", "Стандарт")
    T_bissette_require_dictionary = Trigger("require dictionary", "Стандарт")
    T_bissette_check_library = Trigger("check library", "Стандарт")
    T_bissette_check_library_shelf = Trigger("check library shelf", "Стандарт")
    T_bissette_missing_pages = Trigger("missing pages", "Стандарт")
    T_bissette_judith_borrow_dictionary = Trigger("Judith borrow dictionary", "Стандарт")
    T_bissette_broken_printer = Trigger("broken printer", "Стандарт")
    T_bissette_june_scan_pages = Trigger("June scan pages", "Стандарт")
    T_bissette_june_printer_error = Trigger("June printer error", "Стандарт")
    T_bissette_private_study = Trigger("private study", "Стандарт")
    T_bissette_smith_threat = Trigger("Smith threat", "Стандарт")
    T_bissette_ask_dexter = Trigger("ask Dexter", "Стандарт")
    T_bissette_ask_erik = Trigger("ask Erik", "Стандарт")
    T_bissette_ask_martinez = Trigger("ask Martinez", "Стандарт")
    T_bissette_return_books = Trigger("return books", "Стандарт")
    T_bissette_do_assignment = Trigger("do assignment", "Стандарт")
    T_bissette_french_poem = Trigger("French poem", "Стандарт")
    T_bissette_mia_poem_advice = Trigger("Mia poem advice", "Стандарт")
    T_bissette_reference_book_found = Trigger("reference book found", "Стандарт")
    T_bissette_print_assignment = Trigger("print assignment", "Стандарт")
    T_bissette_roxxy_convince = Trigger("Roxxy convince", "Стандарт")
    T_bissette_roxxy_deal = Trigger("Roxxy deal", "Стандарт")
    T_bissette_bridget_pompoms_steal = Trigger("Bridget pompoms steal", "Стандарт")
    T_bissette_jenny_deal = Trigger("jenny deal", "Стандарт")
    T_bissette_jenny_paid = Trigger("jenny paid", "Стандарт")
    T_bissette_roxxy_meet_inform = Trigger("Roxxy meet inform", "Стандарт")
    T_bissette_roxxy_jenny_hangout = Trigger("Roxxy Jenny hangout", "Стандарт")
    T_bissette_roxxy_jenny_spied = Trigger("Roxxy Jenny spied", "Стандарт")
    T_bissette_quiz_warning = Trigger("quiz warning", "Стандарт")
    T_bissette_quiz_pass = Trigger("quiz pass", "Стандарт")
    T_bissette_sexy_time = Trigger("sexy time", "Стандарт")
    T_bissette_smith_pleased = Trigger("Smith pleased", "Стандарт")

label bissette_fsm_init:
    python:

        S_bissette_start = State("start")
        S_bissette_intro = State("intro", "Я должен сообщить Мисс Биссетт о моем возвращении в школу.")
        S_bissette_challenge = State("challenge", "Частная опека, о которой говорила Мисс Биссетт, казалась очень интересной.")
        S_bissette_tutoring_delay = State("tutoring delay", "Вероятно, я должен поговорить с Мисс Биссетт о том частном обучении, завтра.")
        S_bissette_tutoring = State("tutoring", "Вероятно, я должен поговорить с Мисс Биссетт об этом частном репетиторстве.")
        S_bissette_find_dictionary = State("find dictionary", "Мне нужно найти французский словарь для урока по преподаванию, который Мисс Биссетт даст мне.")
        S_bissette_get_dictionary = State("get dictionary", "Мне нужно получить французский словарь с полки библиотеки.")
        S_bissette_check_dictionary = State("check dictionary", "Мне нужно проверить пропущенные страницы во французском словаре вместе с Мисс Биссетт.")
        S_bissette_find_full_dictionary = State("find full dictionary", "Мне нужно найти полный французский словарь. Мисс Биссетт думает, что у Джудит есть такая.")
        S_bissette_scan_missing_pages = State("scan missing pages", "Мне нужно сканировать недостающие страницы из полного французского словаря. Сканел должен быть в компьютерной лаборатории.")
        S_bissette_fix_printer = State("fix printer", "Мне нужно исправить принтер для недостающих страниц. Может быть, мне стоит попробовать ударить сильнее?")
        S_bissette_study = State("study", "Я должен вернуться к Мисс Биссетт, чтобы пройти эту главу.")
        S_bissette_smith_report = State("smith report", "Я должен поговорить с Мисс Биссетт о моём следующем задании.")
        S_bissette_find_food_book = State("find food book", "Мне нужна книга, чтобы помочь мне с моим направлением по еде.")
        S_bissette_jane_return_books = State("Jane return books", "Библиотекарю нужна моя помощь, чтобы вернуть просроченные книги от Декстера, Эрика и близнецов Мартинеса.")
        S_bissette_got_dexters_book = State("got Dexter's book", "У меня есть книга Декстера. Эрик и близнецы Мартинеса следующие.")
        S_bissette_got_dexters_martinez_books = State("got Dexter's & Martinez's book", "У меня есть книги Декстера и Мартинеса. Эрик остался последним.")
        S_bissette_got_dexters_eriks_books = State("got Dexter's & Erik's book", "У меня есть книги Декстера и Эрика. Осталось опросить близнецов Мартинеса.")
        S_bissette_got_eriks_book = State("got Erik's book", "У меня есть книга Эрика. Декстер и близнецы Мартинеса следующие.")
        S_bissette_got_eriks_dexters_books = State("got Erik's & Dexter's book", "У меня есть книги Эрика и Декстера. Остались близнецы Мартинеса.")
        S_bissette_got_eriks_martinez_books = State("got Erik's & Martinez's book", "У меня есть книги Эрика и Мартинеса. Декстер остался последним.")
        S_bissette_got_martinez_book = State("got Martinez's book", "У меня есть книга близнецов Мартинеса. Остались Декстер и Эрик.")
        S_bissette_got_martinez_dexters_books = State("got Martinez Dexter's book", "У меня есть книги близнецов Мартинеса и Декстера. Эрик остался последним.")
        S_bissette_got_martinez_eriks_books = State("got Martinez Erik's book", "У меня есть книги близнецов Мартинез и Эрика. Декстер последний.")
        S_bissette_return_overdue_books = State("return overdue books", "У меня есть все просроченные книги. Я должен вернуть их библиотекарю.")
        S_bissette_french_food_assignment = State("French food assignment", "Теперь, когда у меня есть справочник, я должен выполнить задание дома.")
        S_bissette_hand_in_assignment = State("hand in assignment", "Я должен передать свое завершенное задание Мисс Биссет.")
        S_bissette_poem_assignment = State("poem assignment", "Я должен поговорить с Мисс Биссет о моем следующем задании.")
        S_bissette_find_poem_reference_book = State("find poem reference book", "Мне нужно найти книгу о романтике для моего задания на стихотворение.")
        S_bissette_reference_book_search = State("reference book search", "Мия упомянула книгу, которую я мог бы использовать. Последний раз книгу видели у Джудит в библиотечной комнате.")
        S_bissette_do_poem_assignment = State("do poem assignment", "Теперь у меня есть книга, я должен выполнить задание дома.")
        S_bissette_print_poem_assignment = State("print poem assignment", "Мне нужно распечатать задание, чтобы сдать.")
        S_bissette_hand_in_poem_assignment = State("hand in poem assignment", "Я должен передать своё завершенное задание Мисс Биссет.")
        S_bissette_office_meetup = State("office meetup", "Мисс Биссет попросила меня встретиться с ней в её офисе вечером.")
        S_bissette_roxxy_exam_convince = State("Roxxy exam convince", "Мне нужно попытаться убедить Рокси пойти на экзамен по французскому.")
        S_bissette_roxxy_pom_poms = State("Roxxy pom poms", "Мне нужно забрать помпоны Рокси у тренера Бриджит, чтобы убедить Рокси пойти на экзамен по французскому.")
        S_bissette_roxxy_pom_poms_deal = State("Roxxy pom poms deal", "Мне нужно вернуть помпоны обратно Рокси для нашей сделки.")
        S_bissette_roxxy_cheerleader_deal = State("Roxxy cheerleader deal", "Мне нужно попросить [jen_name] помочь Рокси, чтобы она присутствовала на экзамене по французскому языку.")
        S_bissette_jenny_mentoring_payment = State("Jenny mentoring payment", "Мне нужно заплатить [jen_name] $500, чтобы помочь Рокси в черлидинге.")
        S_bissette_roxxy_deal_confirmation = State("Roxxy deal conformation", "Я должен пойти и сказать Рокси, что [jen_name] согласился наставлять её.")
        S_bissette_roxxy_jenny_mentoring = State("Roxxy Jenny mentoring", "Я должен отправиться домой и убедиться, что [jen_name] не {i}хлопнет{/i} на Рокси.")
        S_bissette_roxxy_jenny_spying = State("Roxxy Jenny spying", "Я должен пойти проверить Рокси и [jen_name] в спальне наверху.")
        S_bissette_roxxy_convinced = State("Roxxy Convinced", "Мне нужно сообщить Мисс Биссет, что Рокси будет присутствовать на экзамене.")
        S_bissette_quiz = State("quiz", "Мне нужно подготовиться к французской викторине во время урока.")
        S_bissette_wine_sampling = State("wine sampling", "Мисс Биссет предложила выпить с ней вина вечером в своём офисе.")
        S_bissette_smith_final_report = State("Smith final report", "Я должен поговорить с Мисс Биссет о том, что мы делали прошлой ночью.")
        S_bissette_end = State("end")



        S_bissette_start.add(T_bridget_workout, S_bissette_intro, actions=["exec", game.unlock_ui])
        S_bissette_intro.add(T_bissette_improvement_challenge, S_bissette_challenge, actions=["exec", L_library_front.unlock])
        S_bissette_challenge.add(T_bissette_challenge_thoughts, S_bissette_tutoring_delay)
        S_bissette_tutoring_delay.add(T_all_sleep, S_bissette_tutoring)
        S_bissette_tutoring.add(T_bissette_require_dictionary, S_bissette_find_dictionary)
        S_bissette_find_dictionary.add(T_bissette_check_library, S_bissette_get_dictionary)
        S_bissette_get_dictionary.add(T_bissette_check_library_shelf, S_bissette_check_dictionary)
        S_bissette_check_dictionary.add(T_bissette_missing_pages, S_bissette_find_full_dictionary)
        S_bissette_find_full_dictionary.add(T_bissette_judith_borrow_dictionary, S_bissette_scan_missing_pages)
        S_bissette_scan_missing_pages.add(T_bissette_broken_printer, S_bissette_fix_printer)
        S_bissette_fix_printer.add(T_bissette_june_scan_pages, S_bissette_study,
                                   actions = ["clear", "judith return dictionary"]
                                   )
        S_bissette_fix_printer.add(T_bissette_june_printer_error, S_bissette_fix_printer,
                                   actions = ["set", "printer fix fail"]
                                   )
        S_bissette_study.add(T_bissette_private_study, S_bissette_smith_report,
                             actions = ["exec", player.increase_grade_french]
                             )
        S_bissette_smith_report.add(T_bissette_smith_threat, S_bissette_find_food_book)
        S_bissette_find_food_book.add(T_bissette_check_library, S_bissette_jane_return_books)
        S_bissette_jane_return_books.add(T_bissette_ask_dexter, S_bissette_got_dexters_book,
                                         actions = ["clear", "dexters book search"]
                                         )
        S_bissette_got_dexters_book.add(T_bissette_ask_erik, S_bissette_got_dexters_eriks_books,
                                        actions = ["clear", "eriks book search"]
                                        )
        S_bissette_got_dexters_book.add(T_bissette_ask_martinez, S_bissette_got_dexters_martinez_books,
                                        actions = ["clear", "martinez book search"]
                                        )
        S_bissette_got_dexters_martinez_books.add(T_bissette_ask_erik, S_bissette_return_overdue_books,
                                                  actions = ["clear", "eriks book search"]
                                                  )
        S_bissette_got_dexters_eriks_books.add(T_bissette_ask_martinez, S_bissette_return_overdue_books,
                                               actions = ["clear", "martinez book search"]
                                               )
        S_bissette_jane_return_books.add(T_bissette_ask_erik, S_bissette_got_eriks_book,
                                         actions = ["clear", "eriks book search"]
                                         )
        S_bissette_got_eriks_book.add(T_bissette_ask_dexter, S_bissette_got_eriks_dexters_books,
                                      actions = ["clear", "dexters book search"]
                                      )
        S_bissette_got_eriks_book.add(T_bissette_ask_martinez, S_bissette_got_eriks_martinez_books,
                                      actions = ["clear", "martinez book search"]
                                      )
        S_bissette_got_eriks_dexters_books.add(T_bissette_ask_martinez, S_bissette_return_overdue_books,
                                               actions = ["clear", "martinez book search"]
                                               )
        S_bissette_got_eriks_martinez_books.add(T_bissette_ask_dexter, S_bissette_return_overdue_books,
                                                actions = ["clear", "dexters book search"]
                                                )
        S_bissette_jane_return_books.add(T_bissette_ask_martinez, S_bissette_got_martinez_book,
                                         actions = ["clear", "martinez book search"]
                                         )
        S_bissette_got_martinez_book.add(T_bissette_ask_dexter, S_bissette_got_martinez_dexters_books,
                                         actions = ["clear", "dexters book search"]
                                         )
        S_bissette_got_martinez_book.add(T_bissette_ask_erik, S_bissette_got_martinez_eriks_books,
                                         actions = ["clear", "eriks book search"]
                                         )
        S_bissette_got_martinez_dexters_books.add(T_bissette_ask_erik, S_bissette_return_overdue_books,
                                                  actions = ["clear", "eriks book search"]
                                                  )
        S_bissette_got_martinez_eriks_books.add(T_bissette_ask_dexter, S_bissette_return_overdue_books,
                                                actions = ["clear", "dexters book search"]
                                                )
        S_bissette_return_overdue_books.add(T_bissette_return_books, S_bissette_french_food_assignment,
                                            actions = ["clear", "martinez book search",
                                                       "clear", "eriks book search",
                                                       "clear", "dexters book search",
                                                       ]
                                            )
        S_bissette_french_food_assignment.add(T_bissette_do_assignment, S_bissette_hand_in_assignment)
        S_bissette_hand_in_assignment.add(T_bissette_private_study, S_bissette_poem_assignment,
                                          actions = ["exec", player.increase_grade_french]
                                          )
        S_bissette_poem_assignment.add(T_bissette_french_poem, S_bissette_find_poem_reference_book,
                                       actions = ["location", [M_mia ,{"place": L_library}],
                                                  "force", [M_mia, {"tod": 1}],
                                                  ],
                                       )
        S_bissette_find_poem_reference_book.add(T_bissette_mia_poem_advice, S_bissette_reference_book_search)
        S_bissette_reference_book_search.add(T_bissette_reference_book_found, S_bissette_do_poem_assignment,
                                             actions = ["set", "mia book feedback"]
                                             )
        S_bissette_do_poem_assignment.add(T_bissette_do_assignment, S_bissette_print_poem_assignment,
                                          actions = ["unforce", M_mia]
                                          )
        S_bissette_print_poem_assignment.add(T_bissette_print_assignment, S_bissette_hand_in_poem_assignment)
        S_bissette_hand_in_poem_assignment.add(T_bissette_private_study, S_bissette_office_meetup,
                                               actions = ["set", "meet in office",
                                                          "exec", player.increase_grade_french,
                                                         ]
                                               )
        S_bissette_office_meetup.add(T_bissette_roxxy_convince, S_bissette_roxxy_exam_convince)
        S_bissette_roxxy_exam_convince.add(T_bissette_roxxy_deal, S_bissette_roxxy_pom_poms)
        S_bissette_roxxy_pom_poms.add(T_bissette_bridget_pompoms_steal, S_bissette_roxxy_pom_poms_deal)
        S_bissette_roxxy_pom_poms_deal.add(T_bissette_roxxy_deal, S_bissette_roxxy_cheerleader_deal)
        S_bissette_roxxy_cheerleader_deal.add(T_bissette_jenny_deal, S_bissette_jenny_mentoring_payment)
        S_bissette_jenny_mentoring_payment.add(T_bissette_jenny_paid, S_bissette_roxxy_deal_confirmation)
        S_bissette_roxxy_deal_confirmation.add(T_bissette_roxxy_meet_inform, S_bissette_roxxy_jenny_mentoring)
        S_bissette_roxxy_jenny_mentoring.add(T_bissette_roxxy_jenny_hangout, S_bissette_roxxy_jenny_spying)
        S_bissette_roxxy_jenny_spying.add(T_bissette_roxxy_jenny_spied, S_bissette_roxxy_convinced)
        S_bissette_roxxy_convinced.add(T_bissette_quiz_warning, S_bissette_quiz)
        S_bissette_quiz.add(T_bissette_quiz_pass, S_bissette_wine_sampling,
                            actions = ["set", "night visit"],
                            )
        S_bissette_wine_sampling.add(T_bissette_sexy_time, S_bissette_smith_final_report,
                                     actions = ["clear", "meet in office"]
                                     )
        S_bissette_smith_final_report.add(T_bissette_smith_pleased, S_bissette_end,
                                          actions = ["exec", player.increase_grade_french, "exec", A_excellent_francais.unlock],
                                          )

        M_bissette = Machine("Bissette", default_loc = [[L_school_frenchclassroom, L_school_frenchclassroom, L_school_bissetteoffice, L_NULL], 
                                                        [L_NULL, L_NULL, L_NULL, L_NULL]
                                                        ],
                             vars = {"sex speed": .175,
                                     "office first visit": True,
                                     "printer fix fail": False,
                                     "judith return dictionary": True,
                                     "dexters book search": False,
                                     "eriks book search": False,
                                     "martinez book search": False,
                                     "mia book feedback": False,
                                     "meet in office": False,
                                     "night visit": False,
                                     "change angle": False,
                                    },
        )
        M_bissette.set_priority(1)
        M_bissette.add(S_bissette_start, S_bissette_intro, S_bissette_challenge,
                       S_bissette_tutoring_delay, S_bissette_tutoring,
                       S_bissette_find_dictionary, S_bissette_get_dictionary,
                       S_bissette_check_dictionary, S_bissette_find_full_dictionary,
                       S_bissette_scan_missing_pages, S_bissette_fix_printer,
                       S_bissette_study, S_bissette_smith_report,
                       S_bissette_find_food_book, S_bissette_jane_return_books,
                       S_bissette_got_dexters_book, S_bissette_got_dexters_martinez_books,
                       S_bissette_got_dexters_eriks_books, S_bissette_got_eriks_book,
                       S_bissette_got_eriks_dexters_books, S_bissette_got_eriks_martinez_books,
                       S_bissette_got_martinez_book, S_bissette_got_martinez_dexters_books,
                       S_bissette_got_martinez_eriks_books, S_bissette_return_overdue_books,
                       S_bissette_french_food_assignment, S_bissette_hand_in_assignment,
                       S_bissette_poem_assignment, S_bissette_find_poem_reference_book,
                       S_bissette_reference_book_search, S_bissette_do_poem_assignment,
                       S_bissette_print_poem_assignment,
                       S_bissette_hand_in_poem_assignment, S_bissette_office_meetup,
                       S_bissette_roxxy_exam_convince, S_bissette_roxxy_pom_poms,
                       S_bissette_roxxy_pom_poms_deal, S_bissette_roxxy_cheerleader_deal,
                       S_bissette_jenny_mentoring_payment, S_bissette_roxxy_deal_confirmation,
                       S_bissette_roxxy_jenny_mentoring, S_bissette_roxxy_jenny_spying,
                       S_bissette_roxxy_convinced, S_bissette_quiz, S_bissette_wine_sampling,
                       S_bissette_smith_final_report,
                       S_bissette_end
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
