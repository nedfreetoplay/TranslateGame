label attic_first_visit:
    show expression Cutscene("home_attic_cs", "Используя ключ и табурет, я смог попасть на наш чердак.\nЯ никогда не был здесь раньше.\nЯ был полон волнения, задаваясь вопросом, какие сокровища {b}[deb_name]{/b} и папа спрятали.") as cutscene with fade
    with dissolve
    pause
    hide cutscene
    with dissolve
    return

label painting:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}[deb_name]{/b} любила рисовать домашних животных..."
    hide expression "objects/closeup_painting01.png" with dissolve
    $ A_rooster.unlock()
    $ game.main()

label globe:
    scene location_home_attic_globe
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
