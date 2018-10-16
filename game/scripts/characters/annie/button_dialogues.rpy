label annie_dialogue_music_classroom_intro:
    show player 2
    player_name "Привет, {b}Энни{/b}."
    show player 1
    show annie 3
    ann "Я пытаюсь сосредоточиться."
    show annie 1
    show player 3
    player_name "..."
    show player 29 with dissolve
    player_name "Извени-"
    show player 3 with dissolve
    show annie 7
    ann "Я КОНЦЕНТРИРУЮСЬ!"
    show annie 6
    show player 2f
    player_name "И я ухожу!"
    player_name "Боже..."
    hide player
    hide annie
    with dissolve
    return

label annie_dialogue_ross_ask_model:
    show player 2 at left
    show annie 1 at right
    player_name "Я работаю над проектом для {b}Miss Ross{/b} и для него нужна живая модель."
    player_name "Тебе это интересно?"
    show player 1
    show annie 3
    ann "Я не могу этого сделать. У меня раунды!"
    show player 10
    show annie 1
    player_name "А?"
    show player 11
    show annie 4
    ann "Я должена патрулировать негодяев!"
    ann "Убирайся с моего пути!"
    hide annie
    hide player
    show player 12f
    with dissolve

    player_name "Хорошо, блин!"
    player_name "Чудачка..."
    return

label annie_dialogue_leave:
    show player 14
    player_name "Привет {b}Энни{/b}!"
    show annie 5
    show player 1
    ann "Давай быстрее!"
    show annie 6
    show player 17
    player_name "О, ничего... я только хотел сказать привет!"
    show annie 4
    show player 18
    ann "Я на дежурстве по мониторингу зала... И ты зря тратишь мое время."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "Хорошо. Извини за беспокойство. Блин!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
