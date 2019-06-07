init -900 python:
    if persistent.enable_save_locking is None:
        persistent.enable_save_locking = True

    if persistent.notify_label_name is None:
        persistent.notify_label_name = False

    if persistent.skip_intro is None:
        persistent.skip_intro = False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
