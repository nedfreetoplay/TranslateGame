init python:
    class FrenchQuizItem():
        def __init__(self, displayable, position, id_, size):
            self.x = position[0]
            self.y = position[1]
            self._id = id_
            self.position = position
            self.should_blit = False
            self.displayable = renpy.displayable(displayable)
            self.width, self.height = size
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class FrenchQuiz(renpy.Displayable):
        def __init__(self, **properties):
            super(FrenchQuiz, self).__init__(**properties)
            
            
            self._backgrounds = iter((renpy.displayable("backgrounds/location_school_french_minigame_quiz_01.jpg"),
                                renpy.displayable("backgrounds/location_school_french_minigame_quiz_02.jpg"),
                                renpy.displayable("backgrounds/location_school_french_minigame_quiz_03.jpg")
            ))
            
            self._items = iter( ((FrenchQuizItem("buttons/quiz_01.png", (107,479), 1, (203,201)), FrenchQuizItem("buttons/quiz_02.png", (353,317), 2, (262,138)), FrenchQuizItem("buttons/quiz_03.png", (558, 476), 3, (319,211))),
                                (FrenchQuizItem("buttons/quiz_04.png", (119,496), 1, (223,171)), FrenchQuizItem("buttons/quiz_05.png", (380,333), 2, (207,162)), FrenchQuizItem("buttons/quiz_06.png", (575, 498), 3, (291,171))), 
                                (FrenchQuizItem("buttons/quiz_07.png", (114,521), 1, (259,125)), FrenchQuizItem("buttons/quiz_08.png", (374,351), 2, (208,148)), FrenchQuizItem("buttons/quiz_09.png", (626, 460), 3, (229, 199)))
                            ))
            self._answers = iter((3, 1, 2))
            self._nb_pages = 3
            self.correct_answers_count = 0
            self._advance_page()
        
        def _advance_page(self):
            try:
                self._bg = next(self._backgrounds)
                self._items_on_page = next(self._items)
                self._answer = next(self._answers)
            except StopIteration:
                game.timer.tick()
                renpy.hide_screen("french_quiz")
                if self.correct_answers_count == self._nb_pages:
                    renpy.jump("french_classroom_bissette_quiz_pass")
                
                else:
                    renpy.jump("french_classroom_bissette_quiz_fail")
            for item in self._items_on_page:
                item.should_blit = False
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            instructions_r = renpy.render(FilteredText("Select the correct item that matches the word!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            for item in self._items_on_page:
                if item.should_blit:
                    item_r = renpy.render(item.displayable, width, height, st, at)
                    render.blit(item_r, item.position)
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            for item in self._items_on_page:
                if item.hitbox(x, y):
                    item.should_blit = True
                else:
                    item.should_blit = False
            if ev.type == pygame.MOUSEBUTTONUP:
                for item in self._items_on_page:
                    if item.should_blit:
                        if item._id == self._answer:
                            self.correct_answers_count += 1
                        self._advance_page()

screen french_quiz():
    add FrenchQuiz()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
