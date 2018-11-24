init python:
    class Note():
        def __init__(self, y_pos, displayable, speed):
            self.y = y_pos 
            self.x = 1024 
            self._SPEED = speed 
            self._BAR_X = 206 
            self.displayable = displayable 
            self._WIDTH = 140 
            self._timer = clock() 
        def move(self): 
            if (clock() - self._timer)*100 >= 1:
                self._timer = clock()
                self.x -= self._SPEED
            return self.x > 0 
        def hitbox(self, event_y): 
            return (self.y == event_y) and (self.x+self._WIDTH >= self._BAR_X and self._BAR_X >= self.x)

    class GuitarHero(renpy.Displayable):
        def __init__(self, id_, win_label, fail_label, **properties):
            super(GuitarHero, self).__init__(**properties)
            
            self._win_label = win_label 
            self._fail_label = fail_label 
            
            
            self._background = (renpy.displayable("backgrounds/location_school_music_minigame01.jpg"),
                                renpy.displayable("backgrounds/location_school_music_minigame02.jpg")
                               ) 
            self._background = self._background[id_]
            self._bar = renpy.displayable("buttons/music_minigame_bar_highlight.png")
            _notes = ( renpy.displayable("buttons/music_minigame_note_01.png"),
                            renpy.displayable("buttons/music_minigame_note_02.png")
                          ) 
            
            self._start_time = clock() 
            self._blit_bar = False 
            self._blit_bar_start_timer = 0 
            number_of_notes = 25 
            self._counter_failed_notes = 0 
            self._NOTES_PIXEL_MAP = {"a":141, "s":283, "d":432, "f":576} 
            notes_y = [renpy.random.choice(self._NOTES_PIXEL_MAP.values()) for i in xrange(number_of_notes)]
            self._notes = iter([Note(y, renpy.random.choice(_notes), 11) for y in notes_y]) 
            self._notes_to_blit = [] 
            self._DELAY_TO_SPAWN = 110 
            self._NUMBER_OF_FAILS_ALLOWED = 5 
            self._LANE_WIDTH = 130 
            self._end_timer_start = 9999999999999
            self._end_timer_flag = True
        
        def render(self, width, height, st, at):
            render = renpy.render(self._background, width, height, st, at)
            bar_r = renpy.render(self._bar, width, height, st, at)
            if (clock() - self._blit_bar_start_timer)*100 >= 30:
                self._blit_bar = False
            self._note_spawner()
            if (clock() - self._end_timer_start) >= 1.5:
                if self._counter_failed_notes >= self._NUMBER_OF_FAILS_ALLOWED:
                    renpy.hide_screen("guitar_hero")
                    M_dewitt.increment("failcount", 1)
                    renpy.jump(self._fail_label)
                
                else:
                    renpy.hide_screen("guitar_hero")
                    renpy.jump(self._win_label)
            if self._blit_bar:
                render.blit(bar_r, (196, 104))
            for note in self._notes_to_blit:
                if not note.move(): 
                    self._counter_failed_notes += 1
                    renpy.music.play("audio/sfx_missed_chord{}.ogg".format(random.randint(1,2)), "sound")
                    self._notes_to_blit.remove(note)
                note_r = renpy.render(note.displayable, width, height, st, at)
                render.blit(note_r, (note.x, note.y))
            renpy.redraw(self, 0)
            return render
        
        def _note_spawner(self): 
            if (clock() - self._start_time)*100 >= self._DELAY_TO_SPAWN:
                self._start_time = clock()
                try:
                    self._notes_to_blit.append(next(self._notes))
                    self._DELAY_TO_SPAWN = random.randint(10, 12)*10
                except StopIteration:
                    if self._end_timer_flag:
                        self._end_timer_flag = False
                        self._end_timer_start = clock()
        
        def _hit_note(self, note_y): 
            self._blit_bar = True
            self._blit_bar_start_timer = clock()
            for note in self._notes_to_blit:
                if note.hitbox(note_y):
                    self._notes_to_blit.remove(note)
                else:
                    self._counter_failed_notes += 1
                    renpy.music.play("audio/sfx_missed_chord{}.ogg".format(random.randint(1,2)), "sound")
            pass
        
        def event(self, ev, x, y, st):
            if renpy.variant("mobile"):
                if ev.type == pygame.MOUSEBUTTONUP:
                    if x <= 196:
                        if self._NOTES_PIXEL_MAP["a"] < y <= (self._NOTES_PIXEL_MAP["a"] + self._LANE_WIDTH):
                            self._hit_note(self._NOTES_PIXEL_MAP["a"])
                        elif self._NOTES_PIXEL_MAP["s"] < y <= (self._NOTES_PIXEL_MAP["s"] + self._LANE_WIDTH):
                            self._hit_note(self._NOTES_PIXEL_MAP["s"])
                        elif self._NOTES_PIXEL_MAP["d"] < y <= (self._NOTES_PIXEL_MAP["d"] + self._LANE_WIDTH):
                            self._hit_note(self._NOTES_PIXEL_MAP["d"])
                        elif self._NOTES_PIXEL_MAP["f"] < y <= (self._NOTES_PIXEL_MAP["f"] + self._LANE_WIDTH):
                            self._hit_note(self._NOTES_PIXEL_MAP["f"])
            
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_a:
                    self._hit_note(self._NOTES_PIXEL_MAP["a"])
                elif ev.key == pygame.K_s:
                    self._hit_note(self._NOTES_PIXEL_MAP["s"])
                elif ev.key == pygame.K_d:
                    self._hit_note(self._NOTES_PIXEL_MAP["d"])
                elif ev.key == pygame.K_f:
                    self._hit_note(self._NOTES_PIXEL_MAP["f"])

screen guitar_hero(guitar_hero_bg, guitar_hero_win_label, guitar_hero_fail_label):
    add GuitarHero(guitar_hero_bg, guitar_hero_win_label, guitar_hero_fail_label)

screen guitar_hero_test:
    add GuitarHero(0, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
