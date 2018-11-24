label button_ivy_start_intro:
    scene location_pink_closeup
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    show player 29
    show ivy 1
    player_name "It's my first time here. I... Umm..."
    show player 13
    show ivy 3
    ivy "It's okay! I understand! Everyone's a little shy when they first come here..."
    show ivy 2
    ivy "We have a large selection of {b}toys{/b} and {b}sexy apparel{/b} that you can view on our wall display."
    show player 11
    ivy "We can also offer a... {b}full body massage session{/b} in one of our... private rooms."
    ivy "Our masseuse uses a variety of natural body relaxation techniques... That will surely satisfy your needs..."
    show player 12
    show ivy 1
    player_name "Oh... I didn't know you offered massages here."
    show player 1
    show ivy 3
    ivy "It's one of our... less advertised... services."
    show ivy 2
    ivy "Would you like to see our massage selection {b}pamphlet{/b}?"
    return


label button_ivy_end_intro:
    scene pink
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    return

label button_ivy_diane_outfit_package:
    show ivy 1
    show player 2
    player_name "I'm here to pick up a {b}package{/b}."
    show player 1
    show ivy 3
    ivy "Sure!"
    show ivy 2
    ivy "What name is it under?"
    show ivy 1
    show player 12
    player_name "{b}Diane{/b}?"
    show player 1
    show ivy 11
    ivy "Let me check... Right! Here it is!"
    show ivy 1
    show player 170
    player_name "Thanks!"
    show ivy 3
    show player 169
    ivy "Is this for your {b}girlfriend{/b}?"
    show ivy 1
    show player 171
    player_name "!!!"
    show player 29
    player_name "Oh... No! It's for... Ummm... Someone asked me to get it for them!"
    show ivy 2
    show player 13
    ivy "Well, it's a really nice item from our collection..."
    show ivy 3
    ivy "I'm sure you'll like it!"
    show player 21
    show ivy 4
    player_name "Thanks..."
    hide player 21
    hide ivy 4
    show unlock29 at truecenter
    with dissolve
    pause
    hide unlock29 with dissolve
    return

label button_ivy_massage:
    show ivy 5
    show player 21
    player_name "Could I see... your massage pamphlet?"
    show player 13
    show ivy 4
    ivy "Sure! Suit yourself!"
    player_name "Thanks..."
    hide ivy
    hide player
    with dissolve
    return

label button_ivy_just_shopping:
    show player 10
    show ivy 1
    player_name "I'm fine, thank you."
    player_name "I'm just here to do some shopping..."
    show player 13
    show ivy 3
    ivy "Alright, then! Let me know if you need anything else."
    return

label button_ivy_massage_first:
    show ivy 5
    show player 21
    player_name "I guess I could have a look at it..."
    show player 13
    show ivy 4
    ivy "Sure! Suit yourself!"
    hide ivy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
