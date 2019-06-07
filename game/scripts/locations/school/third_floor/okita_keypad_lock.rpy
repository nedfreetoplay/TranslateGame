init python:
    class KeypadButton:
        def __init__(self, index, position):
            self.x, self.y = position
            self.position = position
            if index == 10:
                k = "10"
                self.width, self.height = 168, 83
            else:
                k = "0{}".format(index)
                self.width, self.height = 86, 101
            self.displayable = renpy.displayable("buttons/okita_lock_{}.png".format(k))
            self.index = index
            self.should_blit = False
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class OkitaKeypad(renpy.Displayable):
        def __init__(self, **properties):
            super(OkitaKeypad, self).__init__(self, **properties)
            self._bg = renpy.displayable("backgrounds/location_school_office4_lock.jpg")
            positions = [(345, 252), (466,252), (586,252), (345,369),
                        (466,369), (586,369), (345,485), (466,485), (586,485), (425,606)]
            self._numbers = [KeypadButton(i+1, pos) for i, pos in enumerate(positions)]
            self.code = []
            self._code_spacing = 5
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            for button in self._numbers:
                if button.should_blit:
                    button_r = renpy.render(button.displayable, width, height, st, at)
                    render.blit(button_r, button.position)
            for i, c in enumerate(self.code):
                if c != 10 and i<6:
                    d = renpy.displayable("buttons/okita_input_0{}.png".format(c))
                    r = renpy.render(d, width, height, st, at)
                    render.blit(r, (350+i*50+self._code_spacing, 148))
            cursor = renpy.displayable("buttons/okita_bar.png")
            cursor_r = renpy.render(cursor, width, height, st, at)
            render.blit(cursor_r, (350+14+(len(self.code))*50+self._code_spacing, 194))
            if len(self.code)>0 and self.code[-1] == 10:
                if self.code == [6, 2, 1, 9, 10]:
                    renpy.jump("okita_office_unlock")
                else:
                    
                    renpy.jump("okita_office_locked")
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            for button in self._numbers:
                if button.hitbox(x, y):
                    button.should_blit = True
                else:
                    button.should_blit = False
                if ev.type == pygame.MOUSEBUTTONUP and button.should_blit:
                    self.code.append(button.index)

screen okita_keypad():
    add OkitaKeypad()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
