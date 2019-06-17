init python:
    class BasketArrowDirection:
        def __init__(self):
            self.clockwise = True
            self.base_image = renpy.displayable("buttons/basketball_ball_arrow.png")
            self.angle_increment = 0.5
            self.angle = 45-self.angle_increment
            self._start_arrow_rotation = clock()
            self.rot_origin = (878, 629)
            self.radius = 185
            self.rot_speed = 10
            self.move_arrow(force=True)
        
        def move_arrow(self, force=False):
            if (clock() - self._start_arrow_rotation)*self.rot_speed*100 >= 1 or force:
                self._start_arrow_rotation = clock()
                if self.angle <= 0:
                    self.clockwise = True
                elif self.angle >= 90:
                    self.clockwise = False
                if self.clockwise:
                    self.angle += self.angle_increment
                else:
                    self.angle -= self.angle_increment
                self.image = Transform(self.base_image, rotate=self.angle)
                alpha = self.angle * math.pi / 180
                self.position = (-self.radius*math.cos(alpha)+self.rot_origin[0], -self.radius*math.sin(alpha)+self.rot_origin[1])
            pass

    class BasketLife:
        def __init__(self, position, id_):
            self.displayable = None
            self.position = position
            self.x, self.y = position
            self.id_ = id_
            self.success = None
        def wrong(self):
            self.displayable = renpy.displayable("buttons/basketball_life_fail.png")
            self.success = False
        def good(self):
            self.displayable = renpy.displayable("buttons/basketball_life_win.png")
            self.success = True

    class BasketBall:
        def __init__(self):
            self.origin = (822,574)
            self.position = self.origin
            self.x, self.y = self.position
            self.image = renpy.displayable("buttons/basketball_ball.png")
            self.size = get_size("buttons/basketball_ball.png")
            self.width, self.height = self.size
            self.start_time = clock()
            self.in_air = False
            self.hit_net = False
            self.normal = 0
            self.V0 = 110 
            self.bounce_coefficient = 0.5
            self.point_of_contact_x = 0
            self.point_of_contact_y = 0
        
        def move(self, alpha):
            V0 = self.V0
            t = 6*(clock()-self.start_time) 
            g = 9.81 
            
            alpha = alpha * math.pi / 180
            if self.normal == 0: 
                
                
                
                
                
                
                
                
                
                x = -V0 * math.cos(alpha) * t + self.origin[0]
                y = (g*t*t)/2 - V0*math.sin(alpha)*t+self.origin[1]
            else:
                
                
                
                
                
                
                
                
                
                
                x = self.point_of_contact_x + self.normal*t
                y = g*t*t/2 + self.point_of_contact_y
            
            if y > 1024 or x < -116:
                self.in_air = False
                self.position = self.origin
                self.x, self.y = self.position
                self.normal, self.point_of_contact_x, self.point_of_contact_y = 0, 0, 0
                return True
            else:
                self.position = (x, y)
                self.x, self.y = self.position
                return None
        
        def hitbox(self, x1, y1, x2, y2):
            sx1 = self.x
            sx2 = self.x+self.width
            sy1 = self.y
            sy2 = self.y+self.height
            return (sx1<x2) and (sx2>x1) and (sy1<y2) and (sy2>y1)

    class BasketMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(BasketMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_basketball_minigame01.jpg")
            self.arrow = BasketArrowDirection()
            self.ball = BasketBall()
            self.net = renpy.displayable("buttons/basketball_net.png")
            self.net_position = (136, 399)
            self.lives_arrow = ((109,720), (215,720), (319,720))
            self.life = 2
            positions = [(88,641), (193,641), (297,641)]
            self.lives_images = [BasketLife(position, i) for i, position in enumerate(positions)]
            self.life_arrow_d = renpy.displayable("buttons/basketball_life_arrow.png")
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if renpy.variant("mobile"):
                instructions_r = renpy.render(Text("Нажмите на экран, чтобы кинуть мяч!", style = "style_instructions"), width, height, st, at)
            else:
                instructions_r = renpy.render(Text("Нажмите на экран, чтобы кинуть мяч!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)),20))
            if self.life < 0:
                count = sum([x.success for x in self.lives_images])
                if count == 3:
                    renpy.jump("basketball_success")
                else:
                    renpy.jump("basketball_fail")
            if not self.ball.in_air:
                self.arrow.move_arrow()
            else:
                is_success = self.ball.move(self.arrow.angle)
                if (138 <= self.ball.x+self.ball.width/2 <= 300) and (399 <= self.ball.y+self.ball.height/2 <= 419) and not self.ball.hit_net:
                    self.ball.hit_net = True
                if self.ball.hitbox(97, 132, 127, 403):
                    self.ball.point_of_contact_x = self.ball.x
                    self.ball.point_of_contact_y = self.ball.y + self.ball.height/2
                    self.ball.start_time = clock()
                    self.ball.normal = self.ball.V0 * self.ball.bounce_coefficient
                if is_success is not None: 
                    if not self.ball.hit_net:
                        self.lives_images[self.life].wrong()
                        self.life -= 1
                    else:
                        self.lives_images[self.life].good()
                        self.life -= 1
                    self.ball.hit_net = False
            arrow_r = renpy.render(self.arrow.image, width, height, st, at)
            render.blit(arrow_r, self.arrow.position)
            for l in self.lives_images:
                if l.displayable is not None:
                    l_r = renpy.render(l.displayable, width, height, st, at)
                    render.blit(l_r, l.position)
            life_arrow_r = renpy.render(self.life_arrow_d, width, height, st, at)
            render.blit(life_arrow_r, self.lives_arrow[self.life])
            ball_r = renpy.render(self.ball.image, width, height, st, at)
            render.blit(ball_r, self.ball.position)
            net_r = renpy.render(self.net, width, height, st, at)
            render.blit(net_r, self.net_position)
            renpy.redraw(self, 0)
            return render
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONUP and not self.ball.in_air:
                self.ball.in_air = True
                self.ball.start_time=clock()
            pass

screen basketball_minigame():
    add BasketMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
