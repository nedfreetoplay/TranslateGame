label pregnancy_won(return_label):
    scene expression "backgrounds/pregnancy_minigame_02.jpg" with flash
    pause 1.0
    jump expression return_label

label pregnancy_lost(return_label):
    scene expression "backgrounds/pregnancy_minigame_03.jpg" with hpunch
    pause 1.0
    jump expression return_label
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
