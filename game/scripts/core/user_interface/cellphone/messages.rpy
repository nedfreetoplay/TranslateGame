init python:
    class Message:
        def __init__(self, name, position):
            self.name = name
            self.sender = store.text_messages[name]["sender"].capitalize()
            self.content_prev = store.text_messages[name]["content_preview"]
            self.content = store.text_messages[name]["content"]
            self.image = store.text_messages[name]["image"]
            self.displayable = renpy.displayable(self.image)
            self.position = position
            self.width, self.height = (300,41)
        
        def move(self, yamount):
            self.position = (self.position[0], self.position[1]+yamount)
        
        def hitbox(self, x, y):
            xp, yp = self.position
            return (xp <= x <= xp+self.width) and (yp <= y <= yp+self.height)

    class CellPhoneMessage(renpy.Displayable):
        def __init__(self, message, **properties):
            super(CellPhoneMessage, self).__init__(**properties)
            self._bg = renpy.displayable("cellphone/cellphone.png")
            self.overlay = renpy.displayable("cellphone/cellphone_text_bg.png")
            self.message = message
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            overlay_r = renpy.render(self.overlay, width, height, st, at)
            render.blit(overlay_r, (43, 85))
            image_r = renpy.render(self.message.displayable, width, height, st, at)
            render.blit(image_r, (65,85))
            texting_r = renpy.render(Text("{} is texting you...".format(self.message.sender), style="style_cellphone_message_texting"), width, height, st, at)
            render.blit(texting_r, (145,115))
            content_r = renpy.render(Text(self.message.content, style="style_cellphone_message_content"), width, height, st, at)
            render.blit(content_r, (74,180))
            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            pass


    class CellPhoneMessageApp(renpy.Displayable):
        def __init__(self, **properties):
            super(CellPhoneMessageApp, self).__init__(**properties)
            self._bg = renpy.displayable("cellphone/cellphone.png")
            self.title = renpy.displayable("cellphone/cellphone_title_text.png")
            self.mouse_button_down = False
            self.start_mouse_coord_y = 0
            self.messages = [Message(m, (55, 110+50*i)) for i, m in enumerate(player.messages)]
            self.message_bg = renpy.displayable("cellphone/cellphone_text_tabs.png")
            self.current_message = None
            self.back_button_width, self.back_button_height = (19, 25)
            self.back_button_position = (44, 55)
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            global game
            if game.new_message:
                game.new_message = False
                game.read_message = True
            title_r = renpy.render(self.title, width, height, st, at)
            render.blit(title_r, (135,50))
            if self.current_message is None:
                message_bg_r = renpy.render(self.message_bg, width, height, st, at)
                for message in self.messages:
                    message_r = renpy.render(Text(message.sender + " - " + insert_newlines(message.content_prev, 30)[0], style = "style_cellphone_message"), width, height, st, at)
                    if 110 <= message.position[1] <= 490:
                        render.blit(message_bg_r, (message.position))
                        render.blit(message_r, (message.position[0]+20, message.position[1]))
            else:
                render = self.current_message.render(width, height, st, at)
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            if self.messages:
                if self.current_message is None:
                    sensitivity = 3
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_button_down = True
                        self.start_mouse_coord_y = y
                    elif ev.type == pygame.MOUSEBUTTONUP:
                        self.mouse_button_down = False
                    
                    if self.mouse_button_down:
                        try:
                            if ev.button == 4:
                                self.mouse_button_down = False
                                for message in self.messages:
                                    message.move(sensitivity)
                            elif ev.button == 5:
                                self.mouse_button_down = False
                                for message in self.messages:
                                    message.move(-sensitivity)
                        except AttributeError:
                            pass
                        if y - self.start_mouse_coord_y > 3:
                            for message in self.messages:
                                message.move(sensitivity)
                        elif y - self.start_mouse_coord_y < -3:
                            for message in self.messages:
                                message.move(-sensitivity)
                        else:
                            for message in self.messages:
                                if message.hitbox(x, y):
                                    self.current_message = CellPhoneMessage(message)
                    else:
                        if self.messages[0].position[1] > 110:
                            delta = self.messages[0].position[1] - 110
                            for message in self.messages:
                                message.move(-delta)
                        if self.messages[-1].position[1] < 440:
                            delta = 440-self.messages[-1].position[1]
                            for message in self.messages:
                                message.move(delta)
                else:
                    self.current_message.event(ev, x, y, st)
                    if (self.back_button_position[0]<=x<=self.back_button_position[0]+self.back_button_width) and (self.back_button_position[1]<=y<=self.back_button_position[1]+self.back_button_height):
                        if ev.type == pygame.MOUSEBUTTONUP:
                            self.current_message = None
            pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
