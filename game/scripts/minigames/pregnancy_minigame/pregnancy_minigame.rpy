label pregnancy_won(return_label):
    scene expression "backgrounds/pregnancy_minigame_02.jpg" with flash
    pause 1.0
    jump expression return_label

label pregnancy_lost(return_label):
    scene expression "backgrounds/pregnancy_minigame_03.jpg" with hpunch
    pause 1.0
    jump expression return_label

label call_pregnancy_minigame(return_label="bedroom_dialogue", machine=M_diane):
    if player.pregnancy_chance > 0 and not machine.pregnancy:
        if not persistent.seen_warning_pregnancy:
            show screen popup_warning_pregnancy
            $ persistent.seen_warning_pregnancy = True
        call screen pregnancy_minigame(return_label, machine)
    else:
        jump expression return_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
