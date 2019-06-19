label sis_computer_locked:
    scene expression "backgrounds/location_computer_jenny_01.jpg"
    player_name "( Хмм... У неё стоит {b}пароль{/b}... )"
    return

label sis_computer_locked_diary_locked:
    player_name "( Нужно понять, что это за пароль. )"
    return

label sis_computer_locked_diary_unlocked:
    player_name "( Посмотрим, смогу ли я зайти к ней в учетную запись... )"
    return

label sis_computer_unlocked_unread_email:
    player_name "( Нужно посмотреть, какие ещё секреты она тут хранит... )"
    return

label sispc_desktop_response:
    scene jenny_computer_bg with None
    player_name "Сработало!"
    player_name "Интересно, что я смогу найти у {b}[jen_name]{/b} на компьютере..."
    return

label sispc_nude_response:
    if sispc_nude_seen == False:
        call expression game.dialog_select("sispc_nude_response_dialogue")
        $ sispc_nude_seen = True
    show screen sis_computer
    show screen sis_recycle
    call screen sis_picture(3)

label sispc_nude_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_nude
    with None
    player_name "!!!" with hpunch
    player_name "Это... {b}Её{/b}?!"
    return

label sispc_family_response:
    if sispc_family_seen == False:
        call expression game.dialog_select("sispc_family_response_dialogue")
        $ sispc_family_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(5)

label sispc_family_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_family
    with None
    player_name "( Не думал, что у неё есть эта фотка. )"
    player_name "( Я скучаю по {b}отцу{/b}... )"
    return

label sispc_swimsuit_response:
    if sispc_swimsuit_seen == False:
        call expression game.dialog_select("sispc_swimsuit_response_dialogue")
        $ sispc_swimsuit_seen = True
    show screen sis_computer
    show screen sis_newfolder
    call screen sis_picture(1)

label sispc_swimsuit_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_swimsuit
    with None
    player_name "( А она любит себя фоткать... )"
    return

label sispc_igor_response:
    if sispc_igor_seen == False:
        call expression game.dialog_select("sispc_igor_response_dialogue")
        $ sispc_igor_seen = True
    show screen sis_computer
    show screen sis_family
    call screen sis_picture(4)

label sispc_igor_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_igor
    with None
    player_name "..."
    player_name "( Думаю, что я уже видел этого парня. )"
    player_name "( Он, вроде, работал с {b}отцом{/b}... )"
    return

label sispc_summertime_response:
    if sispc_summertime_seen == False:
        call expression game.dialog_select("sispc_summertime_response_dialogue")
        $ sispc_summertime_seen = True
    show screen sis_computer
    call screen summertime_error

label sispc_summertime_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_summertime
    with None
    player_name "( Боже... Это игра {b}всегда{/b} забагована. )"
    return

label sispc_toylist_response:
    if sispc_toylist_seen == False:
        call expression game.dialog_select("sispc_toylist_response_dialogue")
        $ sispc_toylist_seen = True
    show screen sis_computer
    call screen sis_list

label sispc_toylist_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_toylist
    with None
    player_name "( Выглядет как список... {b}секс игрушек{/b}? )"
    return

label sispc_livecrush_response:
    if sispc_livecrush_seen == False:
        call expression game.dialog_select("sispc_livecrush_response_dialogue")
        $ sispc_livecrush_seen = True
    show screen sis_computer
    call screen sis_livecrush

label sispc_livecrush_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_livecrush
    with None
    player_name "( У {b}[jen_name]{/b} есть аккаунт на LiveCrush?! )"
    player_name "Вау..."
    player_name "( Неужели она проводит {b}прямые эфиры{/b} в своей комнате? )"
    player_name "( А она неплохо хранила этот секрет; Я и не подозревал... )"
    return

label sispc_email_response:
    if sispc_email_seen == False:
        call expression game.dialog_select("sispc_email_response_dialogue")
        $ sispc_email_seen = True
    show screen sis_computer
    call screen sis_email

label sispc_email_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_email
    with None
    player_name "( Не думаю, что нужно сюда заходить... )"
    return

label sispc_email04_response:
    if sis_email_04_read == False:
        call expression game.dialog_select("sispc_email04_response_dialogue")
        $ sis_email_04_read = True
    show screen sis_computer
    call screen sis_email

label sispc_email04_response_dialogue:
    player_name "( У {b}[jen_name]{/b} есть аккаунт на Pink канал?! Но она же может смотреть этот канал, лишь когда все спят. )"
    player_name "( Нужно будет проверить это как-нибудь ночью. )"
    return

label sispc_password_reminder:
    scene jennybedroom_night
    show player 35 at left
    player_name "( Если я всё правильно помню, пароль был в её дневнике... )"
    jump expression game.dialog_select("sis_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
