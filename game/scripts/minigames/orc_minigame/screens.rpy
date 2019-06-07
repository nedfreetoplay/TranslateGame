init python:
    class HealthBar:
        def __init__(self, id_):
            self.image = renpy.displayable("buttons/health_01.png")
            self.position = (396+77*id_,644)

    class OrcBattle(renpy.Displayable):
        def __init__(self, **properties):
            super(OrcBattle, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_erik_minigame07a.jpg")
            self._health = 3
            self._health_bars = [HealthBar(i) for i in range(3)]
            self._arrow = renpy.displayable("buttons/arrows_02.png")
            self._arrow_x = 239
            self._left_to_right = True
            self._start_timer = clock()
            self._reset_timer = 999999
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            instructions_r = renpy.render(FilteredText("Time your attacks by pressing {b}SPACEBAR{/b}!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            
            if (clock() - self._start_timer)*100 >= 1:
                self._start_timer = clock()
                if self._left_to_right:
                    self._arrow_x += 5
                    if self._arrow_x >= 763:
                        self._left_to_right = False
                else:
                    self._arrow_x -= 5
                    if self._arrow_x <= 239:
                        self._left_to_right = True
            if (clock() - self._reset_timer)*100 >= 30:
                if self._health == 0:
                    renpy.jump("orc_battle_finish")
                self._bg = renpy.displayable("backgrounds/location_erik_minigame07a.jpg")
            for i in range(self._health):
                health_r = renpy.render(self._health_bars[i].image, width, height, st, at)
                render.blit(health_r, self._health_bars[i].position)
            arrow_r = renpy.render(self._arrow, width, height, st, at)
            render.blit(arrow_r, (self._arrow_x, 697))
            renpy.not_infinite_loop(1)
            renpy.redraw(self, 0)
            return render
        
        def _on_event(self):
            if 476 <= self._arrow_x <=526:
                self._health -= 1
                self._bg = renpy.displayable("backgrounds/location_erik_minigame07b.jpg")
                self._reset_timer = clock()
            else:
                renpy.jump("orc_battle_fail")
        def event(self, ev, x, y, st):
            if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                self._on_event()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self._on_event()
                return
            return

screen orc_battle():
    add OrcBattle()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
