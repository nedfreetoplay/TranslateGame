init python:
    class SpinBottleMinigame(renpy.Displayable):
        def __init__(self, character="random", is_rox_11b=False, **properties):
            super(SpinBottleMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_beach_minigame01.jpg")
            self.center = (500, 414)
            self.bottle_base = renpy.displayable("buttons/beach_bottle.png")
            self.angle = random.randint(0, 359)
            self.bottle = Transform(self.bottle_base, rotate=self.angle)
            self.speed = 0
            self.spin_button = renpy.displayable("buttons/beach_button.png")
            self.is_spinning = False
            self.toggle_highlight_picture = False
            self.delay = 0
            self.count = 0
            self.is_rox_11b = is_rox_11b
            self.character = character
            if self.is_rox_11b and not self.is_spinning:
                self.spin()
        
        def spin(self):
            test = 0
            weights = {"roxxy":4, "mc":1, "missy":3, "becca":3}
            character = "mc"
            angles = {}
            if self.character == "random":
                character = random.choice(reduce(operator.concat, [[key]*value for key, value in weights.items()]))
                angles = {"missy":range(10,80), "mc":range(100,170), "roxxy":range(190,260), "becca":range(280,350)}
            else:
                character = self.character
                angles = {"missy":range(10,11), "mc":range(100,101), "roxxy":range(190,191), "becca":range(280,281)}
            results = []
            for angle in xrange(360):
                for speed in xrange(30,71):
                    results.append(((sum(range(speed))+angle)%360, speed, angle))
            choice_list = [(r[1], r[2]) for r in results if r[0] in angles[character]]
            self.speed, self.angle = random.choice(choice_list)
            self.is_spinning = True
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            self.angle = (self.angle+self.speed) % 360
            if self.speed > 0:
                self.speed -= 1
            if self.is_spinning and self.speed == 0:
                self.delay = 0.5
                self.count += 1
                self.toggle_highlight_picture = not self.toggle_highlight_picture
                if 0 <= self.angle < 90: 
                    position = (817, 97)
                    image = renpy.displayable("buttons/beach_icon02.png")
                    character = "missy"
                    pass
                elif 90 < self.angle <=180: 
                    position = (826, 555)
                    image = renpy.displayable("buttons/beach_icon04.png")
                    character = "mc"
                    pass
                elif 180 <= self.angle < 270: 
                    position = (57, 555)
                    image = renpy.displayable("buttons/beach_icon03.png")
                    character = "roxxy"
                    pass
                else: 
                    position = (57, 97)
                    image = renpy.displayable("buttons/beach_icon01.png")
                    character = "becca"
                    pass
                if self.toggle_highlight_picture:
                    image = im.MatrixColor(image, im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07))
                icon_r = renpy.render(image, width, height, st, at)
                render.blit(icon_r, position)
            if self.count >= 3:
                renpy.hide_screen("spin_bottle")
                renpy.hide_screen("spin_bottle_minigame")
                if not self.is_rox_11b:
                    M_player.set("beach bottle spins", M_player.get("beach bottle spins") + 1)
                    renpy.jump("spin_bottle_minigame_{}".format(character))
                else:
                    renpy.end_interaction(True)
            instructions_r = renpy.render(Text("Click the button to spin the bottle!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            self.bottle = Transform(self.bottle_base, rotate=self.angle)
            if not self.is_rox_11b and not self.is_spinning:
                spin_button_r = renpy.render(self.spin_button, width, height, st, at)
                render.blit(spin_button_r, (422, 666))
            bottle_r = renpy.render(self.bottle, width, height, st, at)
            width, height = bottle_r.get_size()
            render.blit(bottle_r, (self.center[0]-width/2, self.center[1]-height/2))
            renpy.redraw(self, self.delay)
            return render
        
        def event(self, ev, x, y, st):
            if not self.is_spinning:
                if 422<=x<=585 and 666<=y<=733 and not self.is_rox_11b:
                    self.spin_button = im.MatrixColor(renpy.displayable("buttons/beach_button.png"), im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07))
                    if ev.type == pygame.MOUSEBUTTONDOWN and not self.is_spinning:
                        self.spin()
                else:
                    self.spin_button = renpy.displayable("buttons/beach_button.png")
            pass

screen spin_bottle(character, is_rox_11b):
    add SpinBottleMinigame(character, is_rox_11b)

screen spin_bottle_minigame:
    add SpinBottleMinigame()

screen spin_bottle_minigame_solo_sex_options(character_machine):
    if character_machine == M_roxxy:
        $ character_label = "roxxy"

    elif character_machine == M_missy:
        $ character_label = "missy"

    elif character_machine == M_becca:
        $ character_label = "becca"

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("spin_bottle_minigame_solo_sex_options"), Jump("spin_bottle_minigame_" + str(character_label) + "_solo_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("spin_bottle_minigame_solo_sex_options"), Jump("spin_bottle_minigame_" + str(character_label) + "_solo_cum")

    if anim_toggle:
        if character_machine.get("sex speed") < .175:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("spin_bottle_minigame_solo_sex_options"), Function(character_machine.set, "sex speed", character_machine.get("sex speed") + 0.05), Jump("spin_bottle_minigame_" + str(character_label) + "_solo_loop")

        if character_machine.get("sex speed") > .076:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("spin_bottle_minigame_solo_sex_options"), Function(character_machine.set, "sex speed", character_machine.get("sex speed") - 0.05), Jump("spin_bottle_minigame_" + str(character_label) + "_solo_loop")

screen spin_bottle_minigame_mc_4some_options(character_machine):
    if M_player.get("left of 4some") == M_roxxy:
        $ next_character_button_left = "buttons/roxxy_04.png"
        $ next_character_machine_left = M_roxxy
        if character_machine == M_becca:
            $ next_character_button_right = "buttons/roxxy_02.png"
            $ next_character_machine_right = M_missy
        else:
            $ next_character_button_right = "buttons/roxxy_03.png"
            $ next_character_machine_right = M_becca

    elif M_player.get("left of 4some") == M_becca:
        $ next_character_button_left = "buttons/roxxy_03.png"
        $ next_character_machine_left = M_becca
        if character_machine == M_missy:
            $ next_character_button_right = "buttons/roxxy_04.png"
            $ next_character_machine_right = M_roxxy
        else:
            $ next_character_button_right = "buttons/roxxy_02.png"
            $ next_character_machine_right = M_missy

    elif M_player.get("left of 4some") == M_missy:
        $ next_character_button_left = "buttons/roxxy_02.png"
        $ next_character_machine_left = M_missy
        if character_machine == M_roxxy:
            $ next_character_button_right = "buttons/roxxy_03.png"
            $ next_character_machine_right = M_becca
        else:
            $ next_character_button_right = "buttons/roxxy_04.png"
            $ next_character_machine_right = M_roxxy

    if store._in_replay == None:
        imagebutton:
            focus_mask True
            pos (50,700)
            idle next_character_button_left
            hover HoverImage(next_character_button_left)
            action Hide("spin_bottle_minigame_mc_4some_options"), Function(M_player.set, "left of 4some", character_machine), Function(renpy.call, "spin_bottle_minigame_mc_4some_loop_pre", character_machine, next_character_machine_left)

    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("spin_bottle_minigame_mc_4some_options"), Function(renpy.call, "spin_bottle_minigame_mc_4some_loop", character_machine)

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("spin_bottle_minigame_mc_4some_options"), Function(renpy.call, "spin_bottle_minigame_mc_4some_cum", character_machine)

    if store._in_replay == None:
        imagebutton:
            focus_mask True
            pos (650,700)
            idle next_character_button_right
            hover HoverImage(next_character_button_right)
            action Hide("spin_bottle_minigame_mc_4some_options"), Function(renpy.call, "spin_bottle_minigame_mc_4some_loop_pre", character_machine, next_character_machine_right)

    if anim_toggle:
        if character_machine.get("sex speed") < .09:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("spin_bottle_minigame_mc_4some_options"), Function(character_machine.set, "sex speed", character_machine.get("sex speed") + 0.03), Function(renpy.call, "spin_bottle_minigame_mc_4some_loop", character_machine)

        if character_machine.get("sex speed") > .031:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("spin_bottle_minigame_mc_4some_options"), Function(character_machine.set, "sex speed", character_machine.get("sex speed") - 0.03), Function(renpy.call, "spin_bottle_minigame_mc_4some_loop", character_machine)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
