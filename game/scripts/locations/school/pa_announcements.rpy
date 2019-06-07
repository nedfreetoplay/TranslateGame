label pa_announcement:
    if random.randint(1,100) < 5 and not game.timer.is_dark() and not game.timer.is_weekend() and M_smith.get("school intro done"):
        scene expression player.location.background_blur
        call expression "pa_announcement_{}".format(random.randint(1,23))
    return

label pa_announcement_1:
    show player 35b
    PA "Attention Seniors:"
    PA "The end of the term is quickly approaching and you know what that means..."
    PA "It's time to find yourself a date and hit the dance floor at our Annual Sorority Ball!"
    PA "We hope to see you all there!"
    player_name "..."
    return

label pa_announcement_2:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that PDA is strictly forbidden within the halls of Summerville College..."
    PA "So keep your hands and more importantly your genitals to yourselves!"
    PA "Thank you and have a great day!"
    player_name "..."
    return

label pa_announcement_3:
    show player 35b
    PA "Attention:"
    PA "{b}Principal Smith{/b}, you have a large package waiting for you in your office."
    show player 35
    PA "I repeat."
    PA "{b}Principal Smith{/b}, you have a large package waiting for you in your office."
    player_name "..."
    return

label pa_announcement_4:
    show player 35b
    PA "Attention Students:"
    PA "Taco Day in the cafeteria has been cancelled, do to a malfunctioning refrigeration unit."
    PA "Chili will be served as a substitute."
    show player 35
    PA "... On an unrelated note. Anyone showing signs of food poisoning should be brought to the main office immediately."
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_5:
    show player 35b
    PA "Attention Faculty:"
    PA "Whoever left the brownies in the teacher's lounge is asked to report to {b}Principal Smith's{/b} office asap."
    show player 35
    PA "I repeat."
    PA "Whoever left the brownies in the teacher's lounge is asked to report to {b}Principal Smith's{/b} office asap."
    PA "Thank you!"
    player_name "..."
    return

label pa_announcement_6:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that bullying is a strongly frowned upon here at Summerville College."
    PA "Anyone who feels they are being bullied is encouraged to report the situation to our student well-being representative, {b}Dexter{/b}."
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_7:
    show player 35b
    PA "Attention Faculty:"
    PA "This is a reminder that alchohalic beverages are strictly prohibited within Summerville College."
    PA "This includes personal offices."
    show player 43
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_8:
    show player 35b
    PA "Attention Students:"
    PA "We would like to invite you all to come out and support our school Basketball Team."
    PA "I mean, sure. They're 0-12 this season but that doesn't mean we can't show our school pride by attending!"
    show player 43
    PA "Come and cheer them on as they look to acquire their first win of the season!"
    player_name "..."
    return

label pa_announcement_9:
    show player 35b
    PA "Attention Students:"
    PA "We are still looking to fill a few spots on the Summerville Athletics Team."
    PA "Speak with Coach Bridget if you are interested in representing your school out on the track!"
    PA "... No Wussies allowed."
    show player 35
    player_name "..."
    return

label pa_announcement_10:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that defacing school property is a crime!"
    PA "... And any student caught doing this will be handed over to the proper authorities."
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_11:
    show player 35b
    PA "Attention Students:"
    PA "The Sexual Education DVD's stolen from Coach Bridget's office are still unaccounted for."
    show player 43
    PA "If anyone has any information regarding the DVD's whereabouts or the person who stole them."
    PA "Please report to Coach Bridget immediately!"
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_12:
    show player 35b
    PA "Attention Music Lovers:"
    PA "{b}Miss Dewitt{/b} is still looking for talented individuals to aid her in forming a school band."
    PA "If you have any interest, please report to her after class."
    PA "Thank you and have a pleasant day!"
    show player 35
    player_name "..."
    return

label pa_announcement_13:
    show player 35b
    PA "Attention Students:"
    PA "Miss Okita would like to remind students that lab coat and safety glasses must be worn inside the school lab at all times."
    PA "Anyone failing to abide this rule will be subject to strict disciplinary action."
    PA "Thank you and have a pleasant day!"
    show player 35
    player_name "..."
    return

label pa_announcement_14:
    show player 35b
    PA "Attention:"
    PA "To the owner of the red Conda Hivic, License number - 637 5chw1f7y."
    PA "Your car is illegally parked and will be towed if you don't move it immediately."
    show player 35
    PA "... Again."
    PA "To the owner of the red Conda Hivic, License number - 637 5chw1f7y."
    PA "Your car is illegally parked and will be towed if you don't move it immediately."
    PA "Thank you!"
    player_name "..."
    return

label pa_announcement_15:
    show player 35b
    PA "Attention Art Lovers:"
    PA "{b}Miss Ross{/b} will be offering a special, one time lecture, to students this Saturday."
    PA "... Entitled, 'Finding the Happiness in Everything!'"
    PA "Anyone attending is encouraged to bring snacks."
    PA "Thank you and have a pleasant day!"
    show player 43
    player_name "..."
    return

label pa_announcement_16:
    show player 35b
    PA "Attention:"
    PA "Miss Bissette, your presence is requested on the third floor immediately."
    PA "We have reports of a foul odor emanating from your office."
    show player 35
    PA "I repeat."
    PA "Miss Bissette to the third floor, immediately."
    PA "Thank you!"
    player_name "..."
    return

label pa_announcement_17:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that pornographic material is not allowed on school property."
    show player 43
    PA "... And yes, that does include nude drawings of green skinned fantasy characters."
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_18:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that striking school property is expressly forbidden."
    PA "... Unless it's that piece of shit printer in the computer lab."
    PA "In which case it's expressly encouraged!"
    show player 43
    PA "Thank you and have a pleasant day!"
    player_name "..."
    return

label pa_announcement_19:
    show player 35b
    PA "Attention Students:"
    PA "We've received several complaints involving the theft of used panties from the locker room."
    PA "We encourage anyone with information regarding these incidents to come forward immediately."
    PA "Thank you and have a pleasant day!"
    show player 35
    player_name "..."
    return

label pa_announcement_20:
    show player 35b
    PA "Attention Cheerleaders:"
    PA "Tonight's practice has been suspended in favor of what Coach Bridget referred to as - Real Sports."
    PA "Thank you and have a pleasant day!"
    show player 43
    player_name "..."
    return

label pa_announcement_21:
    show player 35b
    PA "Attention Basketball Players:"
    PA "An xtra xtra small jock-strap was found abandoned after practice lastnight."
    PA "If the owner of said jock-strap would like to reclaim it, please come to the main office at your earliest convenience."
    PA "Thank you and have a pleasant day!"
    show player 43
    player_name "..."
    return

label pa_announcement_22:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that your personal lockers are not meant for food storage."
    PA "Please be considerate of others and clean those disgusting things out once in awhile..."
    PA "Thank you and have a pleasant day!"
    show player 35
    player_name "..."
    return

label pa_announcement_23:
    show player 35b
    PA "Attention Students:"
    PA "This is a reminder that roof access is strictly forbidden."
    PA "When asked about the subject, {b}Principal Smith{/b} commented, 'This isn't Japan, you fucking weebs...'"
    PA "Thank you and have a pleasant day!"
    show player 43
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
