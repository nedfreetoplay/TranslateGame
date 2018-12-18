label check_pregnancies:
    python hide:
        preggos = pregnant_machines()
        if len(preggos) > 0:
            for preggo in preggos:
                if not game.new_message:
                    if preggo.pregnancy.stage == 1:
                        preggo.pregnancy.text_announcement_seen = True
                    if preggo.pregnancy.stage == 5:
                        preggo.pregnancy.text_labor_seen = True
                if preggo.pregnancy.text_announcement_seen and preggo.pregnancy.stage == 1 and not preggo.pregnancy.announced_pregnancy:
                    renpy.call("{}_pregnant_announcement_2".format(preggo._name))
                elif not preggo.pregnancy.text_announcement_seen and preggo.pregnancy.stage == 1 and not preggo.pregnancy.announced_pregnancy:
                    renpy.call("{}_pregnant_announcement_1".format(preggo._name))
                    preggo.pregnancy.text_announcement_seen = True
                elif preggo.pregnancy.text_labor_seen and preggo.pregnancy.stage == 5 and not preggo.pregnancy.seen_in_labor:
                    renpy.call("{}_pregnant_labor_2".format(preggo._name))
                elif not preggo.pregnancy.text_labor_seen and preggo.pregnancy.stage == 5 and not preggo.pregnancy.seen_in_labor:
                    renpy.call("{}_pregnant_labor_1".format(preggo._name))
                    preggo.pregnancy.text_labor_seen = True
    return

label diane_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "{b}I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label diane_pregnant_announcement_2:
    scene expression player.location.background_blur
    show player 12 with dissolve
    player_name "I wonder what's going on?"
    player_name "{b}I should swing by {b}Diane{/b}'s barn and see what's the matter{/b}."
    hide player with dissolve
    return

label diane_pregnant_labor_1:
    scene expression player.location.background_blur
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 9 with dissolve
    pause
    show player 14 with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label diane_pregnant_labor_2:
    scene expression player.location.background_blur
    show player 23 with dissolve
    player_name "The baby is coming!"
    player_name "Holy crap!"
    show player 22
    pause
    show player 23
    player_name "I'd better head to {b}the clinic{/b} to check on them!"
    hide player with dissolve
    return

label daisy_pregnant_announcement_1:
    scene expression player.location.background_blur
    show player 9 with dissolve
    player_name "Hmm?"
    player_name "{b}I've got a text from {b}Diane{/b}!"
    hide player with dissolve
    return

label daisy_pregnant_announcement_2:
    scene expression player.location.background_blur with None
    show player 10 with dissolve
    player_name "I wonder what's going on?"
    player_name "{b}I should swing by {b}Diane{/b}'s barn and see what's the matter?{/b}."
    hide player with dissolve
    return

label daisy_pregnant_labor_1:
    scene expression player.location.background_blur
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 9 with dissolve
    pause
    show player 14 with dissolve
    player_name "Looks like I got a text."
    hide player with dissolve
    return

label daisy_pregnant_labor_2:
    scene expression player.location.background_blur with None
    show player 14 with dissolve
    player_name "The baby is here!"
    show player 10
    player_name "Holy crap!"
    show player 5
    pause
    show player 14
    player_name "I'd better head to the {b}Barn{/b} to check on them."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
