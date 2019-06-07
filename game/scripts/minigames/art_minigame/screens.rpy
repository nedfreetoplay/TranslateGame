init python:
    class ArtPaintResult():
        def __init__(self, position, id_, answer):
            self.x, self.y = position
            self.position = position
            self.width, self.height = 118, 119
            self.id_ = id_
            self.answer = set(answer)
            self.should_blit = False
            self.image = renpy.displayable("buttons/art_minigame_paint_0{}.png".format(id_))

    class ArtPaintTube():
        def __init__(self, position, id_):
            self.x = position[0]
            self.y = position[1]
            self.id = id_
            self.position = position
            self.selected = False
            self.should_blit_highlighted = False
            self.displayable = renpy.displayable("buttons/art_minigame_tube0{}.png".format(id_))
            self.highlighted = renpy.displayable("buttons/art_minigame_tube0{}b.png".format(id_))
            self.width, self.height = 235, 108
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class ArtMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(ArtMinigame, self).__init__(**properties)
            
            self._instructions = iter((renpy.displayable("buttons/art_minigame_instructions_0{}.png".format(i+1)) for i in xrange(4)))
            self._bg = renpy.displayable("backgrounds/location_school_art_minigame01.jpg")
            
            self._tubes = (ArtPaintTube((80,143), 1), 
                            ArtPaintTube((80,288), 2), 
                            ArtPaintTube((80, 423), 3), 
                            ArtPaintTube((80,564), 4)) 
            self._paints = iter((ArtPaintResult((460,389), 1, (1, 2)), 
                            ArtPaintResult((603,455), 2, (2, 3)), 
                            ArtPaintResult((754, 401), 3, (1, 3)), 
                            ArtPaintResult((726,251), 4, (3, 4)))) 
            self._position_instructions = (252, 21)
            self._selection = renpy.displayable("buttons/art_minigame_tube_selection.png")
            self._paints_to_blit = []
            self.player_answers = []
            self._timer = 99999999999999
            self._advance_page()
        
        def _return_screen(self, ret):
            self._timer = clock()
            self._should_advance_page = ret
            if ret:
                self.mark_to_blit = renpy.displayable("buttons/quiz_success.png")
                self._paints_to_blit.append(self._current_paint)
            else:
                self._mark_to_blit = renpy.displayable("buttons/quiz_fail.png")
                
                
                self.player_current_answers = []
                for item in self._tubes:
                    item.selected = False
                self._mark_to_blit = None
        def _advance_page(self):
            self.player_current_answers = []
            self._should_advance_page = False
            self._mark_to_blit = None
            for item in self._tubes:
                item.should_blit_highlighted = False
                item.selected = False
            try:
                self._instruction = next(self._instructions)
                self._current_paint = next(self._paints)
            except StopIteration:
                renpy.jump("art_minigame_done") 
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            instruction_r = renpy.render(self._instruction, width, height, st, at)
            render.blit(instruction_r, self._position_instructions)
            if (clock()-self._timer)*1000 >= 500:
                if self._should_advance_page:
                    self._advance_page()
            for item in self._tubes:
                item_r = renpy.render(item.displayable, width, height, st, at)
                render.blit(item_r, (item.x, item.y))
                if item.should_blit_highlighted:
                    item_r = renpy.render(item.highlighted, width, height, st ,at)
                    render.blit(item_r, item.position)
                if item.selected:
                    selection_r = renpy.render(self._selection, width, height, st, at)
                    render.blit(selection_r, item.position)
            for paint in self._paints_to_blit:
                paint_r = renpy.render(paint.image, width, height, st, at)
                render.blit(paint_r, paint.position)
            if self._mark_to_blit is not None:
                mark_r = renpy.render(self._mark_to_blit, width, height, st, at)
                render.blit(mark_r, (304,179))
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            for item in self._tubes:
                item.should_blit_highlighted = item.hitbox(x, y)
            if ev.type == pygame.MOUSEBUTTONUP:
                for item in self._tubes:
                    if item.should_blit_highlighted:
                        if not item.selected:
                            self.player_current_answers.append(item.id)
                        else:
                            self.player_current_answers.remove(item.id)
                        item.selected = not item.selected
                    if len(self.player_current_answers) == 2:
                        self.player_answers.append(self.player_current_answers)
                        self._return_screen(set(self.player_current_answers) == self._current_paint.answer)

screen art_minigame():
    add ArtMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
