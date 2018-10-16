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
    player_name "Я работаю над проектом для {b}Мисс Росс{/b}, и для него требуется живая модель."
    player_name "Вы были бы заинтересованы?"
    show player 1
    show annie 3
    ann "Не могу этого сделать. У меня раунды!"
    show player 10
    show annie 1
    player_name "Угу?"
    show player 11
    show annie 4
    ann "Я должен патрулировать для злодеев!"
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
    ann "Сделай это быстро!"
    show annie 6
    show player 17
    player_name "Да ничего... Я просто поздоровался!"
    show annie 4
    show player 18
    ann "Я на дежурстве по мониторингу зала... И ты тратишь мое время."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "Всё порядке. Извини за беспокойство. Шиш!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
