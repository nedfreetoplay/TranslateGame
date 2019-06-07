init python:
    class Mob:
        def __init__(self, image, key):
            self.image = renpy.displayable(image+".png")
            self.kill_image = renpy.displayable(image+"b.png")
            self._key = key
        
        def kill(self, keyinput):
            ret = keyinput == self._key
            if keyinput in [pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN]:
                pass
            elif not ret:
                renpy.jump("computer_maze_fail")
            return ret

    class MazeAttackButton():
        def __init__(self, image, size, position, key):
            self.width, self.height = size
            self.x, self.y = position
            self.position = position
            self.image = renpy.displayable(image)
            self.key = key
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class MazeMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(MazeMinigame, self).__init__(**properties)
            
            self._bg = renpy.displayable("images/backgrounds/location_computer_minigame03.jpg")
            gelly = Mob("images/objects/minigame03_monster02", pygame.K_a)
            skeleton = Mob("images/objects/minigame03_monster01", pygame.K_s)
            firespirit = Mob("images/objects/minigame03_monster03", pygame.K_d)
            self._mob_list = [gelly, skeleton, firespirit]
            inputs_list = [pygame.K_UP, pygame.K_RIGHT, pygame.K_RIGHT, 
                                pygame.K_RIGHT, pygame.K_RIGHT, pygame.K_UP,
                                pygame.K_UP, pygame.K_LEFT, pygame.K_UP, pygame.K_UP, 
                                pygame.K_LEFT, pygame.K_LEFT, pygame.K_DOWN, 
                                pygame.K_DOWN, pygame.K_LEFT, pygame.K_LEFT,
                                pygame.K_UP, pygame.K_UP, pygame.K_LEFT,
                                pygame.K_LEFT, pygame.K_DOWN, pygame.K_DOWN,
                                pygame.K_DOWN, pygame.K_DOWN]
            self._path = iter(inputs_list)
            self._cell_width, self._cell_height = 90, 100
            positions = [(427, 615)]
            for ev in inputs_list:
                if ev == pygame.K_UP:
                    positions.append((positions[-1][0], positions[-1][1]-self._cell_height))
                elif ev == pygame.K_DOWN:
                    positions.append((positions[-1][0], positions[-1][1]+self._cell_height))
                elif ev == pygame.K_LEFT:
                    positions.append((positions[-1][0]-self._cell_width, positions[-1][1]))
                elif ev == pygame.K_RIGHT:
                    positions.append((positions[-1][0]+self._cell_width, positions[-1][1]))
            positions.append((0,0))
            self._player_positions = iter(positions)
            self._mob_positions = iter(positions)
            self._player_pos = next(self._player_positions)
            next(self._mob_positions)
            self._mob_pos = next(self._mob_positions)
            self._next_input = next(self._path)
            self._player = renpy.displayable("images/objects/minigame03_hero01.png")
            self.mob = None
            self._attack_buttons = [MazeAttackButton("images/buttons/maze_button_01.png", (106,88), (616,649), pygame.K_a),
                                    MazeAttackButton("images/buttons/maze_button_02.png", (83,88), (728,650), pygame.K_s),
                                    MazeAttackButton("images/buttons/maze_button_03.png", (86,94), (834,642), pygame.K_d)]
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            player_r = renpy.render(self._player, width, height, st, at)
            self.player_width, self.player_height = player_r.get_size()
            render.blit(player_r, self._player_pos)
            instructions_r = renpy.render(FilteredText("Use the {b}ARROW{/b} keys to move and {b}A,S,D{/b} to kill the matching monsters!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            if self.mob is not None:
                mob_r = renpy.render(self.mob.image, width, height, st, at)
                self.mob_width, self.mob_height = mob_r.get_size()
                self.x_pos, self.y_pos = self._mob_pos
                render.blit(mob_r, ((self.x_pos + (self.player_width - self.mob_width)),(self.y_pos + (self.player_height - self.mob_height))))
                for button in self._attack_buttons:
                    button_r = renpy.render(button.image, width, height, st, at)
                    render.blit(button_r, button.position)
            renpy.redraw(self, 0)
            return render
        
        def _on_event(self, key):
            if (key == self._next_input and self.mob is None) or (self.mob is not None and self.mob.kill(key)):
                self._mob_pos = next(self._mob_positions)
                self._player_pos = next(self._player_positions)
                try:
                    self._next_input = next(self._path)
                except StopIteration:
                    renpy.jump("computer_maze_success")
                if (random.randint(1,100)<=20):
                    self.mob = random.choice(self._mob_list)
                else:
                    self.mob = None
        
        def event(self, ev, x, y, st):
            if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                if self.mob is not None:
                    for button in self._attack_buttons:
                        if button.hitbox(x, y):
                            self._on_event(button.key)
                else:
                    self._on_event(self._next_input)
                pass
            if ev.type == pygame.KEYUP:
                self._on_event(ev.key)
            pass

screen maze_scr():
    add MazeMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
