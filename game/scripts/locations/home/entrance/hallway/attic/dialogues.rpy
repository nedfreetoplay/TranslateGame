label attic_first_visit:
    scene expression "backgrounds/location_home_attic_cutscene.jpg"
    show expression FilteredText("Using the key and stool, I was able to get into our attic.\nI had never been up there before.\nI was filled with excitement wondering what treasures {b}[deb_name]{/b} and dad had stashed away.") as cutscene at Position (xpos= 512, ypos= 700)
    with fade
    pause
    hide cutscene
    scene black
    with fade
    return

label painting:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}[deb_name]{/b} used to love painting farm animals..."
    hide expression "objects/closeup_painting01.png" with dissolve
    $ A_rooster.unlock()
    $ game.main()

label globe:
    scene location_home_attic_globe
    pause
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
