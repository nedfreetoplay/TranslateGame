init python:
    class ScienceItem():
        def __init__(self, position, id_):
            self.x = position[0]
            self.y = position[1]
            self.id = id_
            self.position = position
            self.should_blit_highlighted = False
            self.displayable = renpy.displayable("buttons/serum_ingredient_0{}.png".format(id_))
            self.highlighted = HoverImage("buttons/serum_ingredient_0{}.png".format(id_))
            self.width, self.height = 88, 87
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class ScienceMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(ScienceMinigame, self).__init__(**properties)
            
            self._backgrounds = iter((renpy.displayable("backgrounds/location_school_office4_minigame01.jpg"),
                                renpy.displayable("backgrounds/location_school_office4_minigame02.jpg")
            ))
            
            self._items = (ScienceItem((83,246), 1), 
                            ScienceItem((83,342), 2), 
                            ScienceItem((83, 440), 3), 
                            ScienceItem((855,246), 4), 
                            ScienceItem((855,342), 5), 
                            ScienceItem((855, 440), 6)) 
            self._answers = iter((set((1, 2, 4)), set((3, 5, 6))))
            self.player_answers = []
            self.middle_positions = ((474, 440), (474, 342), (474,246))
            self._timer = 99999999999999
            self._colors = iter(("blue", "pink"))
            self._advance_page()
        
        def _return_screen(self, ret):
            self._timer = clock()
            self._should_advance_page = ret
            if ret:
                self._mark_to_blit = renpy.displayable("buttons/quiz_success.png")
            else:
                self._failed_minigame = True
                self._mark_to_blit = renpy.displayable("buttons/quiz_fail.png")
        
        
        def _advance_page(self):
            self.player_current_answers = []
            self._should_advance_page = False
            self._failed_minigame = False
            self._mark_to_blit = None
            for item in self._items:
                item.should_blit_highlighted = False
                item.x, item.y = item.position
            try:
                self._bg = next(self._backgrounds)
                self._current_answer = next(self._answers)
                self._color = next(self._colors)
            except StopIteration:
                renpy.hide_screen("science_minigame")
                renpy.jump("science_minigame_success") 
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            instructions_r = renpy.render(FilteredText("Combine the right ingredients for the {b}"+self._color+"{/b} serum!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            if (clock() - self._timer) * 1000 >= 500:
                if self._should_advance_page:
                    self._advance_page()
                elif self._failed_minigame:
                    renpy.hide_screen("science_minigame")
                    renpy.jump("science_minigame_fail") 
            for item in self._items:
                item_r = renpy.render(item.displayable, width, height, st, at)
                render.blit(item_r, (item.x, item.y))
                if item.should_blit_highlighted:
                    render.blit(renpy.render(item.highlighted, width, height, st, at), (item.x, item.y))
            if self._mark_to_blit is not None:
                mark_r = renpy.render(self._mark_to_blit, width, height, st, at)
                self._mark_width, self._mark_height = mark_r.get_size()
                render.blit(mark_r, (((width / 2) - (self._mark_width / 2)),((height / 2) - (self._mark_height / 2))))
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            for item in self._items:
                if item.hitbox(x, y):
                    item.should_blit_highlighted = True
                else:
                    item.should_blit_highlighted = False
            if ev.type == pygame.MOUSEBUTTONUP:
                for item in self._items:
                    if item.should_blit_highlighted and len(self.player_current_answers) < 3:
                        self.player_current_answers.append(item.id)
                        item.x, item.y = self.middle_positions[len(self.player_current_answers)-1]
                    if len(self.player_current_answers) == 3:
                        self.player_answers.append(self.player_current_answers)
                        self._return_screen(set(self.player_current_answers) == self._current_answer)

screen science_minigame():
    add ScienceMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
