label erik_bullying_2:
    $ player.go_to(L_hospital_room)
    call expression game.dialog_select("erik_bullying_2_dialogue")
    $ erik_bullying_2.finish()
    $ L_hospital.unlock()
    $ game.timer.tick(2)
    scene black with fade
    $ game.main()

label erik_bullying_2_dialogue:
    scene hospital_bed
    show player 392 at Position (xpos=805, ypos=665)
    show micoe 5 at left
    with fade
    "Привет, как-"
    "..."
    show micoe 4
    "Хм хм!!"
    player_name "Ух...."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "Ох хорошо! Ты начал просыпаться."
    show micoe 2
    "Как ты себя чувствуешь?"
    show micoe 1
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Я..."
    show player 397 at Position (xpos=772, ypos=660)
    player_name "Я чувствую себя прекрасно."
    show player 394 at Position (xpos=768, ypos=660)
    player_name "Немного кружится голова."
    pause
    show player 396 at Position (xpos=772, ypos=660)
    player_name "Где я?"
    show player 397
    show micoe 5
    "Ты в больнице."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Я?"
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "Правильно!"
    show micoe 2
    micoe "И я {b}Медсестра Micoe{/b}."
    show micoe 5
    micoe "У тебя было небольшое сотрясение, но ты будешь в порядке."
    micoe "Ты можешь пойти домой когда ты будешь готов."
    micoe "Только убедись что пьешь достаточно воды и тебе нужен отдых."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Ох, Я вижу... Спасибо."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 2
    micoe "Я забыла сказать что у тебя есть гость!"
    hide micoe with dissolve
    pause
    show player 393
    pause
    show erik 4f at left with dissolve
    eri "Хэй, {b}[firstname]{/b}!"
    eri "Как ты себя чувствуешь?"
    show erik 1f
    show player 395
    player_name "Хэй {b}Erik{/b}. Со мной все в порядке, Я думаю!"
    show player 393
    show erik 5f
    eri "{b}Dexter{/b} хорошо тебя избил, хм."
    show erik 1f
    show player 395
    player_name "Нет, {b}Dexter{/b} бьет как девченка!"
    show player 393
    show erik 4f
    eri "Хех хех."
    eri "Спасибо что заступился за меня сегодня."
    show erik 1f
    show player 395
    player_name "Всё нормально."
    show player 393
    show erik 5f
    eri "Никто и никогда раньше не выступал против {b}Dexter{/b} раньше."
    show erik 4f
    eri "Каждый в школе только об этом и говорит."
    show erik 1f
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Эх... Я не хотел что бы  этим все кончилось..."
    player_name "...И все же мне надрали задницу!"
    show player 393 at Position (xpos=772, ypos=660)
    show erik 4f
    eri "Что ж, {b}Dexter{/b} будет думать дважды прежде чем сделать что то подобное снова."
    show erik 1f
    show player 395
    player_name "Хех! еще посмотрим."
    show player 393
    pause
    show erik 4f
    eri "Хэй, Я слышал что медсестра сказала что ты уже можешь идти домой."
    eri "Готов"
    show erik 1f
    show player 395
    player_name "Ага."
    show player 393
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
