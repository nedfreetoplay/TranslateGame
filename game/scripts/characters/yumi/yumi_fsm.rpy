init python:

    T_yumi_backup_request = Trigger("backup request", "Юми просит срочного подкрепления")

label yumi_machine_init:
    python:
        M_yumi = Machine("yumi", default_loc=[[L_police_basement, L_police_basement, L_police_basement, L_NULL]],
                          vars = {"sex speed": 0.3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
