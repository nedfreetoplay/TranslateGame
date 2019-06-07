label cupid_daisy_get_new_flowers:
    scene expression player.location.background_blur
    show player 11 with dissolve
    player_name "( Whoa. )"
    player_name "( I wasn't expecting such a huge selection of flowers... )"
    pause
    show player 13
    player_name "( I should see if they have any {b}Sunflowers{/b} for {b}Daisy{/b}. )"
    hide player with dissolve
    return

label cupid_mom_cupid_store:
    scene location_mall_cupid_blur
    show player 5 at left
    show debbie 165f at Position(xpos=0.5, ypos=1.0)
    with dissolve
    deb "Oh, wow!"
    show debbie 166f
    deb "Look at all the pretty things!"
    show debbie 165 at Position(xpos=0.75, ypos=1.0) with dissolve
    deb "Isn't it wonderful, {b}[firstname]{/b}?!"
    show debbie 164
    player_name "..."
    show player 10
    player_name "I dunno {b}[deb_name]{/b}, it seems pretty girly in here..."
    show player 5
    show debbie 165
    deb "Well, yeah..."
    show debbie 166
    deb "But I AM a girl, Sweetheart."
    show debbie 164
    deb "..."
    show debbie 165
    deb "Besides, you're obviously starting to become more interested in girls."
    show debbie 167 at right with dissolve
    deb "... And if you want to keep one you'll have to start getting acquainted with places like this!"
    show debbie 164 at Position(xpos=0.9, ypos=1.0) with dissolve
    show player 10
    player_name "Really?"
    show player 5
    show debbie 166
    deb "Hehe, of course!"
    show debbie 165
    deb "Why don't you help me pick something out. It'll be good practice for you!"
    show player 10
    show debbie 164
    player_name "Practice?"
    show player 5
    show debbie 166
    deb "Yeah!"
    show debbie 165
    deb "{b}[firstname]{/b}, {b}gift giving{/b} is a very important part of {b}dating{/b}."
    show player 43
    show debbie 164
    player_name "Yeah, I know that, {b}[deb_name]{/b}!"
    show player 5
    show debbie 165
    deb "Okay, well... Pretend that you're dating me."
    show debbie 164
    player_name "..."
    show player 12
    player_name "You're Serious?"
    show player 11
    show debbie 166
    deb "Hehe, Yesss!"
    show debbie 165
    deb "If you were dating me... What kind of gift do you think I'd like?"
    show player 10
    show debbie 164
    player_name "Hmm, I'm not sure."
    show player 11
    show debbie 165
    deb "Well take a look around and see if you can find something!"
    deb "I'll be waiting over here."
    show player 10
    show debbie 164
    player_name "Alright."
    hide debbie with dissolve
    show player 4 at Position(xpos=0.375, ypos=1.0) with dissolve
    player_name "( What would {b}[deb_name]{/b} like? )"
    player_name "( ... )"
    player_name "( A {b}necklace{/b} maybe? )"
    hide player with dissolve
    return

label necklace_display_mom_choose_gift:
    scene location_mall_cupid_blur
    show player 4 zorder 0 at left
    player_name "Yeah, a necklace could definitely work."
    player_name "But which one?"
    show player 492
    show xtra 33 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    player_name "... No. Too gaudy."
    show xtra 32 with dissolve
    player_name "Hmm, no... This one is too childish for her, I think."
    show xtra 31 with dissolve
    player_name "Oh, this one looks like her!"
    show popup_item_necklace1 at truecenter with dissolve
    $ player.get_item("pearl_necklace")
    pause
    hide popup_item_necklace1 with dissolve
    player_name "It's perfect!"
    player_name "Now, let's see if she agrees!"
    hide xtra
    hide player
    with dissolve
    return

label necklace_display_repeat:
    scene location_mall_cupid_blur
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return

label cupid_dressroom:
    $ player.go_to(L_cupid_dressroom)
    if M_mom.is_state(S_mom_dressing_room):
        call expression game.dialog_select("cupid_dressroom_mom_dressing_room")
        $ M_player.set("jerk mom", True)
        $ M_mom.trigger(T_mom_dressing_room_check)
        $ player.go_to(L_cupid)

        $ game.timer.tick()
    $ game.main()

label cupid_dressroom_mom_dressing_room:
    scene location_mall_cupid_blur
    show player 10
    player_name "{b}[deb_name]{/b}, you alright in there?"
    player_name "What's taking so long?"
    show player 11
    deb "Actually, sweetie, could you come in here for a second?"
    player_name "..."
    show player 10
    player_name "You want me to come in there?!"
    show player 11
    deb "Yes, please."
    show player 10
    player_name "... Okay."
    show player 11

    scene location_mall_cupid_closeup_stall

    show debbie 169 zorder 1 at Position(xpos=0.65, ypos=1.0)
    show player 10 at Position(xpos=0.35, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    with dissolve
    player_name "What's the matter?"
    show player 11
    show debbie 168
    deb "Oh, I got the necklace snagged on something and I can't get it to unclasp."
    deb "Could you give me a hand?"
    show player 10
    show debbie 169
    player_name "S-sure."
    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show debbie 178 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve

    deb "Oh!"
    show debbie 177b
    deb "..."
    show debbie 178b
    deb "Oh my..."
    show player 228c
    show debbie 177b
    player_name "What is it?"

    show debbie 178b
    show player 228d
    deb "{b}*Ahem*{/b} N-nothing Sweetheart."
    deb "Can you see where it's snagged?"
    show player 228c
    show debbie 177b
    player_name "Yup, I see it. Just hold still one second."
    show player 228d
    player_name "..."
    show player 228c
    player_name "Man, you really got it stuck."
    show player 228d
    deb "..."
    show player 228c
    player_name "Almoooost..."
    player_name "Got iiiit..."
    show player 228d
    player_name "..."
    show debbie 179
    deb "Hehehe."
    show player 228c
    player_name "What's so funny?"
    show player 228d
    show debbie 178
    deb "N-nothing. It's silly."
    show player 228c
    show debbie 177
    player_name "Oh c'mon, tell me."
    show player 228d
    show debbie 178
    deb "I'm just thinking about that movie we watched the other night."
    show player 228c
    show debbie 177
    player_name "That cheesy romance flick?"
    show player 228d
    show debbie 178
    deb "Y-yeah."
    show player 228c
    show debbie 177
    player_name "What about it?"
    show player 228d
    show debbie 178
    deb "There was a scene just like this... Remember?"
    show debbie 177
    player_name "..."
    show player 228c
    player_name "Oh yeah!"
    player_name "He helped the girl out with her necklace and then he-"
    show player 227d at Position(xpos=0.35, ypos=1.0) with dissolve
    player_name "{b}*Gulp*{/b}"
    show player 227c
    player_name "Kissed her."
    show player 227d
    show debbie 178
    deb "Uh huh."
    show player 228d at Position(xpos=0.475, ypos=1.0) with dissolve
    deb "Have you kissed a girl yet, {b}[firstname]{/b}?"
    show player 228c
    show debbie 177
    player_name "... No."
    show player 228d
    deb "..."
    show debbie 179
    deb "Well that's okay, Sweetheart! There's nothing wrong with that."
    show debbie 177
    player_name "..."
    show debbie 178
    deb "Would you like to to try?"
    show player 227c at Position(xpos=0.35, ypos=1.0) with dissolve
    show debbie 177
    player_name "You're serious?"
    show player 227d
    show debbie 178
    deb "Well, yeah... I suppo-"
    hide player
    hide debbie
    show debbie 180b
    with dissolve

    deb "( !!! )"

    show debbie 180
    pause
    show debbie 181
    deb "Mmm..."
    show debbie 182
    pause

    deb "... Wow."
    deb "Sweetie, we can't... I-I mean I shouldn't have..."
    hide debbie
    show player 5 at Position(xpos=0.35, ypos=1.0)
    show debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
    with dissolve
    player_name "..."
    deb "..."
    show player 10
    player_name "I'm sorry, {b}[deb_name]{/b}."
    show player 5
    show debbie 168
    deb "NO! No... It's me, I shouldn't have let myself..."
    show debbie 169b
    deb "..."
    show debbie 168
    deb "{b}*Ahem*{/b} W-why don't you just see about getting that necklace unstuck."
    show debbie 169b
    player_name "..."
    show player 10
    player_name "Y-yeah, sure thing, {b}[deb_name]{/b}."
    show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
    show debbie 177 zorder 1 at Position(xpos=0.60, ypos=1.0)
    hide mneck 1
    with dissolve
    pause
    player_name "..."
    pause

    show player 492 zorder 3 at Position(xpos=0.35, ypos=1.0)
    show xtra 31 zorder 4 at Position(xpos=0.4575, ypos=0.749)
    show debbie 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    player_name "There we go, all fixed."
    show player 493
    deb "..."
    show debbie 168
    deb "Thanks Sweetheart."
    deb "Why don't you go put the necklace back in its display case."
    deb "I'll be out in just a moment..."
    show player 492
    show debbie 169b
    player_name "Yeah, okay."
    hide player
    hide xtra
    with dissolve
    deb "..."
    show debbie 164b with dissolve
    deb "( Oh god... I can't believe I just did that! )"
    deb "( The poor thing is having a hard enough time as it is. )"
    deb "( What in the world was I thinking... )"
    hide debbie with dissolve
    return

label mom_cupid_outing_block:
    scene location_mall_cupid_blur
    if M_mom.is_state(S_mom_choose_gift):
        call expression game.dialog_select("mom_cupid_outing_block_choose_gift")

    elif M_mom.is_state(S_mom_show_necklace):
        call expression game.dialog_select("mom_cupid_outing_block_show_necklace")

    elif M_mom.is_state(S_mom_dressing_room):
        call expression game.dialog_select("mom_cupid_outing_block_dressing_room")
    $ game.main()

label mom_cupid_outing_block_choose_gift:
    show player 4 with dissolve
    player_name "Hmm, I should check out the necklace display for something {b}[deb_name]{/b} would like..."
    hide player with dissolve
    return

label mom_cupid_outing_block_show_necklace:
    show player 4 with dissolve
    player_name "I should take this necklace to {b}[deb_name]{/b} and see if she likes it."
    hide player with dissolve
    return

label mom_cupid_outing_block_dressing_room:
    show player 14 with dissolve
    player_name "I have to wait for {b}[deb_name]{/b}."
    show player 13
    player_name "..."
    show player 10
    player_name "I wonder what's taking her so long?"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
