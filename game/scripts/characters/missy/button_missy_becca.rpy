label missy_becca_button_dialogue:
    scene expression player.location.background_blur
    if M_roxxy.is_state(S_roxxy_chat_with_becca_missy):
        call expression game.dialog_select("button_missy_becca_chat_with_becca_missy")
        $ M_roxxy.trigger(T_roxxy_get_goldenschwagger)
    elif M_roxxy.is_state(S_roxxy_spin_bottle):
        if player.has_item("goldschwagger"):
            show player 5f with dissolve
            player_name "( Я не должен больше беспокоить их. )"
            player_name "( Я их увижу в {b}Субботу вечером на пляже{/b}. )"
            hide player with dissolve
        else:
            show player 5f with dissolve
            player_name "( Я не должен больше беспокоить их . )"
            player_name "( Мне нужно поговорить с {b}Капитаном Терри{/b} об этом {b}Золотом Schwagger{/b} штуковине. )"
            hide player with dissolve
        $ game.main()
    else:
        if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
            call expression game.dialog_select("button_missy_becca_intro_rox11")
        elif not M_roxxy.finished_state(S_roxxy_ask_exam_copy_delay):
            call expression game.dialog_select("button_missy_becca_intro_0_1")
            $ game.main()
        else:
            call expression game.dialog_select("button_missy_becca_intro")
        menu:
            "Девочки, прекрасно выглядят." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_nice")
            "Я просто хотел сказать поздороваться." if M_roxxy.between_states(S_roxxy_ask_exam_copy_delay, S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave_rox11")
            "Вы обе сегодня выглядите прекрасно" if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_look_beautiful")
            "Еще увидимся." if M_roxxy.finished_state(S_roxxy_invite_to_bikini_contest):
                call expression game.dialog_select("button_missy_becca_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
