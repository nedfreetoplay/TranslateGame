init python:
    class Weightlifting(renpy.Displayable):
        
        def __init__(self, **kwargs):
            super(Weightlifting, self).__init__(**kwargs)
            
            bg_img = 'backgrounds/location_gym_minigame04{}.jpg'
            bar_img = 'buttons/meter_03.png'
            effort_img = 'buttons/meter_04.png'
            arrow_img = 'buttons/arrows.png'
            
            
            self.bar = renpy.displayable(bar_img)
            self.effort = renpy.displayable(effort_img)
            self.arrow = renpy.displayable(arrow_img)
            
            suffix = '_mobile' if renpy.variant('mobile') else ''
            if player.stats.str() >= 7:
                suffix += '_heavy'
            elif player.stats.str() >= 3:
                suffix += '_medium'
            self.bgs = (
                    renpy.displayable(bg_img.format('a' + suffix)),
                    renpy.displayable(bg_img.format('b' + suffix)))
            
            
            self.children = self.bgs + (self.bar, self.effort, self.arrow)
            
            
            self.bar_x, self.bar_y = 42, 54
            self.effort_width = 160
            self.effort_min_y, self.effort_max_y = 45, 610
            self.arrow_x = 74
            self.arrow_min_y, self.arrow_max_y = 155, 586
            
            
            self.effort_max_h = self.effort_max_y - self.effort_min_y
            self.arrow_max_h = self.arrow_max_y - self.arrow_min_y
            
            
            self.click_gain = 0.08 
            self.gravity = 0.0065 
            self.lift_after = 6 
            self.tick_duration = 1.0 / 60 
            self.time_limit = 8.0 
            
            
            self.clicks = 0 
            self.progress = 0
            self.started = None
            self.ticked = None
        
        def render(self, w, h, st, at):
            if self.started:
                
                if self.progress >= 1:
                    renpy.jump('weightlifting_done')
                
                
                time_left = 1 - min(1, (st - self.started) / self.time_limit)
                
                
                if time_left == 0:
                    renpy.jump('weightlifting_fail')
                
                
                ticks_elapsed = (st - self.ticked) / self.tick_duration
                if ticks_elapsed >= 1:
                    self.ticked = st
                    
                    downforce = self.gravity * ticks_elapsed
                    self.progress = max(0, self.progress - downforce)
            else:
                
                time_left = 1.0
            
            
            render = renpy.render(
                self.bgs[self.clicks / self.lift_after % 2], w, h, st, at)
            
            
            keyname = get_name("key_str").upper()
            text_instructions = "Press the {b}" + keyname + "{/b} key until you fill up the {b}bar{/b}!"
            instructions_r = renpy.render(FilteredText(text_instructions, style = "style_instructions"), w, h, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),22))
            
            bar = renpy.render(self.bar, w, h, st, at)
            render.blit(bar, (self.bar_x, self.bar_y))
            
            
            effort = renpy.render(self.effort, w, h, st, at)
            effort = effort.subsurface((
                -self.bar_x, -self.bar_y, self.effort_width,
                self.effort_min_y + self.effort_max_h * (1 - self.progress)))
            render.blit(effort, (0, 0))
            
            
            arrow = renpy.render(self.arrow, w, h, st, at)
            render.blit(arrow, (
                self.arrow_x, self.arrow_min_y + self.arrow_max_h * time_left))
            
            
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            click = renpy.variant('mobile') and ev.type == pygame.MOUSEBUTTONUP
            space = ev.type == pygame.KEYDOWN and ev.key == get_key("key_str")
            
            if not click and not space:
                return 
            
            if not self.started:
                self.started = self.ticked = st
            
            self.clicks += 1
            self.progress += self.click_gain
        
        def visit(self):
            return self.children

screen weightlifting():
    add Weightlifting()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
