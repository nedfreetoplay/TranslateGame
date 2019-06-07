label sis_computer_locked:
    scene expression "backgrounds/location_computer_jenny_01.jpg"
    player_name "( Hmm... She has a {b}password{/b}... )"
    return

label sis_computer_locked_diary_locked:
    player_name "( I should try to find out what it is. )"
    return

label sis_computer_locked_diary_unlocked:
    player_name "( Let's see if I can log into her computer... )"
    return

label sis_computer_unlocked_unread_email:
    player_name "( I should look for other secrets she might have on here... )"
    return

label sispc_desktop_response:
    scene jenny_computer_bg with None
    player_name "It worked!"
    player_name "I wonder what {b}[jen_name]{/b} has on her computer..."
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
    player_name "Is that... {b}Her{/b}?!"
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
    player_name "( I never knew she had this picture. )"
    player_name "( I miss {b}Dad{/b}... )"
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
    player_name "( She loves taking pictures of herself... )"
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
    player_name "( I think I've seen this guy before. )"
    player_name "( He used to work with {b}Dad{/b}... )"
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
    player_name "( Man... This game {b}always{/b} has bugs. )"
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
    player_name "( Looks like a list of... {b}toys{/b}? )"
    return

label sispc_livecrush_response:
    if sispc_livecrush_seen == False:
        call expression game.dialog_select("sispc_livecrush_response_dialogue")
        $ sispc_livecrush_seen = True
    show screen sis_computer
    call screen jenny_camslut

label sispc_livecrush_response_dialogue:
    scene jenny_computer_bg
    show jenny_computer_livecrush
    with None
    player_name "( {b}[jen_name]{/b} has a profile on LiveCrush?! )"
    player_name "Woah..."
    player_name "( Does she do these {b}live shows{/b} in her room? )"
    player_name "( She must be pretty careful keeping this a secret; I had no idea... )"
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
    player_name "( I don't know If I should go through these... )"
    return

label sispc_email04_response:
    if sis_email_04_read == False:
        call expression game.dialog_select("sispc_email04_response_dialogue")
        $ sis_email_04_read = True
    show screen sis_computer
    call screen sis_email

label sispc_email04_response_dialogue:
    player_name "( {b}[jen_name]{/b} has a pink account?! The only time she'd have a chance to watch that adult cable TV channel would be when everybody's asleep. )"
    player_name "( I should check to see if she's downstairs at night. )"
    return

label sispc_password_reminder:
    scene jennybedroom_night
    show player 35 at left
    player_name "( If I remember right, the password was in her diary... )"
    jump expression game.dialog_select("sis_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
