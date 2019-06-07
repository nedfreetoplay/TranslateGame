label eve_classroom_dialogue_eve_intro:
    scene classroom
    show evedesk 1 at left
    with fade
    eve "Wow... I thought you were dead for sure!"
    show evedesk 2
    player_name "What?... What do you mean?"
    show evedesk 1
    eve "I dunno... You've been missing all month, and people started making up rumors about how your family had been murdered or something..."
    show evedesk 3
    player_name "Ugh... It's nothing like that!"
    show evedesk 4
    eve "I figured. People just like to talk, and this school is just a big joke."
    eve "I'm glad our last year is almost over..."
    show evedesk 5
    player_name "Yeah, I know what you mean."
    show evedesk 6
    eve "You should hang out with us at the {b}park{/b} sometime... Avoid all these idiots around school and chill, you know?"
    show evedesk 5
    eve "Make sure you come by at {b}night{/b}... it's usually when we go out there."
    player_name "Ehh... I guess I could come by one night."
    show evedesk 6
    eve "It's up to you. Do whatever you want!"
    show evedesk 4
    eve "Oh hey, did you hear {b}Miss Bissette's{/b} announcement about a special reward?"
    show evedesk 1
    eve "Or were you asleep for that part?"
    show evedesk 3
    player_name "Hey! I was awake... for that part."
    show evedesk 4
    eve "I wonder what the reward will be."
    eve "She didn't really say much about it. Probably something stupid anyway."
    eve "I'm already doing pretty well so it's not even worth trying."
    show evedesk 2
    player_name "Why not?"
    show evedesk 6
    eve "How is going from a B to an A much improvement?"
    eve "You'd be more likely to win..."
    show evedesk 5
    player_name "Me?"
    show evedesk 1
    eve "Well, yeah... you're failing right now aren't you?"
    eve "You've got lots of room for improvement."
    show evedesk 6
    eve "Plus, {b}Miss Bissette{/b} favors guys anyway."
    eve "You should seriously consider it."
    hide evedesk with dissolve
    return

label eve_classroom_dialogue_intro:
    show evedesk 4 at left with dissolve
    eve "Hey, {b}[firstname]{/b}."
    show evedesk 5
    player_name "Hey, {b}Eve{/b}."
    show evedesk 4
    eve "What's up?"
    return

label eve_classroom_dialogue_talent_show_help:
    show evedesk 5
    player_name "Do you play any instruments?"
    show evedesk 4
    eve "No, I don't play any instruments. I've always wanted to learn but I just haven't had the time, you know?"
    show evedesk 5
    player_name "Okay, well how about singing?"
    show evedesk 1
    eve "Oh, umm..."
    show evedesk 4
    eve "Yeah, I like to sing I guess. I dunno if I'm any good though."
    show evedesk 5
    player_name "I bet you are! You should sign up for the talent show with me!"
    show evedesk 3
    player_name "We're really hurting for more volunteers."
    show evedesk 1
    eve "... Yeah, I dunno."
    eve "You want me to sing in front of the entire school? That sounds pretty embarassing."
    eve "... And I haven't sang in awhile. Not since my karaoke machine broke."
    eve "I'm quite out of practice."
    show evedesk 5
    player_name "Hmm..."
    player_name "You know, I think my friend {b}Erik{/b} has a {b}karaoke machine{/b} in his basement."
    show evedesk 4
    eve "Oh, yeah?"
    show evedesk 5
    player_name "Totally! You should come over sometime and practice!"
    show evedesk 4
    eve "Heh, you want me to sing for you and your friend?"
    show evedesk 5
    player_name "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    eve "..."
    show evedesk 4
    eve "Alright, I guess I can stop by for a little while."
    show evedesk 5
    player_name "Awesome! {b}I'll meet you at Erik's house{/b} tonight."
    return

label eve_classroom_dialogue_adehsive:
    show evedesk 5
    player_name "What was the plan again?"
    show evedesk 4
    eve "You're supposed to meet {b}Kevin{/b} in the {b}science lab after class{/b}."
    eve "Remember?"
    show evedesk 5
    player_name "Oh, that's right. Thanks, {b}Eve{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show evedesk 5
    player_name "Are you going to sign up to be tutored by {b}Miss Bissette{/b}?"
    show evedesk 4
    eve "I'm already doing pretty well so it's not even worth trying."
    show evedesk 2
    player_name "Why not?"
    show evedesk 6
    eve "How is going from a B to an A much improvement?"
    eve "You'd be more likely to win..."
    show evedesk 5
    player_name "Me?"
    show evedesk 1
    eve "Well, yeah... you're failing right now aren't you?"
    eve "You've got lots of room for improvement."
    show evedesk 6
    eve "Plus, {b}Miss Bissette{/b} favors guys anyway."
    eve "You should seriously consider it."
    return

label eve_classroom_dialogue_hang_out:
    show evedesk 5
    player_name "Where did you say you hung out at?"
    show evedesk 4
    eve "My friends and {b}I hang out at the park{/b}."
    eve "Just make sure you {b}come by at night{/b}... it's usually when we go out there."
    show evedesk 5
    player_name "Alright. I might stop by one night."
    show evedesk 6
    eve "It's up to you. Do whatever you want!"
    return

label eve_classroom_dialogue_leave:
    show evedesk 5
    player_name "Nothing, just wanted to say hello."
    show evedesk 4
    eve "Oh. Talk to you later then."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
