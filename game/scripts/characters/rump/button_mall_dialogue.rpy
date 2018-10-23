label rump_mall_dialogue_pre:
    scene mall_closeup
    show xtra 18 zorder 2 at left
    with dissolve
    player_name "( Похоже на нового Мэра, который произносит свою речь сегодня. )"
    show rump 1 at Position(xpos = 330)
    show iwanka 1 at Position(xpos = 860)
    with dissolve
    pause
    show rump 2
    rump "Добрый День, граждане Саммервилл."
    rump "Именно благодаря вашей усердной работе и преданности делу Я горд возможностью находиться сегодня сдесь и говорить..."
    rump "Я удостоился великой чести быть выбранным Мэром вашего прекрасного города."
    show rump 4 at Position(xpos = 374)
    show iwanka 2
    rump "Вместе с моей дочерью, Иванкой."
    rump "Кто будет нести полную ответственность по всем вопросам связанными с иностранными делами."
    show rump 3 at Position(xpos = 266)
    show iwanka 1
    rump "И как было обещано сделать это во время моей компании..."
    rump "Мы возьмем этот жалкий Торговый центр, и превратим его в нечто великий {b}ТОРГОВЫЙ ЦЕНТР{/b}!"
    show rump 2 at Position(xpos = 330)
    rump "Это будет не легко!"
    rump "Это будет не быстро!"
    show rump 3 at Position(xpos = 266)
    rump "Но я прослежу за этим как мэр, это станет нашим прекрасным городом {b}БОЛЕЕ ВЕЛИКИМ!{/b}"
    hide rump
    hide iwanka
    with dissolve
    player_name "( Он несомненно умеет подбирать нужные слова... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
