init python:
    class Vector2(object):
        zero = lambda _=None:Vector2(0, 0)
        one = lambda _=None:Vector2(1, 1)
        left = lambda _=None:Vector2(-1, 0)
        up = lambda _=None:Vector2(0, 1)
        right = lambda _=None:Vector2(1, 0)
        down = lambda _=None:Vector2(0, -1)
        
        def __init__(self, *args):
            if isinstance(args[0], tuple):
                self.x = args[0][0]
                self.y = args[0][1]
            elif len(args) == 2:
                self.x = args[0]
                self.y = args[1]
            else:
                raise ValueError
        
        def __str__(self):
            return "Vector2 x: {}, y: {}".format(self.x, self.y)
        
        def __add__(self, other):
            if isinstance(other, Vector2):
                return Vector2(self.x+other.x, self.y+other.y)
            elif isinstance(other, tuple):
                return Vector2(self.x+other[0], self.y+other[1])
            else:
                raise ValueError
        
        def __iadd__(self, other):
            return self.__add__(other)
        
        def __sub__(self, other):
            if isinstance(other, Vector2):
                return Vector2(self.x-other.x, self.y-other.y)
            elif isinstance(other, tuple):
                return Vector2(self.x-other[0], self.y-other[1])
            else:
                raise ValueError
        
        def __isub__(self, other):
            return self.__sub__(other)
        
        def __mul__(self, other):
            if isinstance(other, int) or isinstance(other, float) or isinstance(other, long):
                return Vector2(self.x*other, self.y*other)
            else:
                raise ValueError
        
        def __imul__(self, other):
            return self.__mul__(other)
        
        def __nonzero__(self):
            return self.x and self.y
        
        def __bool__(self):
            return self.x and self.y
        
        def __neg__(self):
            return Vector2(-self.x, -self.y)
        
        def __eq__(self, other):
            if isinstance(other, Vector2):
                return self.x == other.x and self.y==other.y
            elif isinstance(other, tuple):
                return self.x==other[0] and self.y==other[1]
            else:
                raise ValueError
        
        def __abs__(self):
            return Vector2(abs(self.x), abs(self.y))
        
        def __hash__(self):
            return int("{}{}".format(self.x, self.y))
        
        @property
        def magnitude(self):
            return math.sqrt(self.x**2 + self.y**2)
        
        @property
        def magnitudesq(self):
            return self.x**2 + self.y**2
        
        def dot(self, other):
            if isinstance(other, Vector2):
                return self.x*other.x + self.y*other.y
            else:
                raise ValueError
        
        def angle_to(self, other):
            if isinstance(other, Vector2):
                return math.acos(self.dot(other)/(self.magnitude*other.magnitude))
            else:
                raise ValueError
        
        @property
        def square(self):
            return self.dot(self)
        
        @property
        def tuple(self):
            return (self.x, self.y)
        
        def distance(self, other):
            return math.sqrt(self.distancesq(other))
        
        def distancesq(self, other):
            if isinstance(other, tuple):
                other = Vector2(tuple)
            return (self.x-other.x)*(self.x-other.x)+(self.y-other.y)*(self.y-other.y)
        
        @classmethod
        def center(cls, width, height):
            w = width-1024
            h = height-768
            w /= 2
            h /= 2
            return Vector2(-w, -h)
        
        def clamp(self, minimum=(0,0), maximum=None):
            if maximum is None:
                raise ValueError
            if isinstance(minimum, tuple):
                minimum = Vector2(minimum)
            if isinstance(maximum, tuple):
                maximum = Vector2(maximum)
            rvx = self.x
            rvy = self.y
            if self.x >= maximum.x:
                rvx = maximum.x
            if self.x <= minimum.x:
                rvx = minimum.x
            if self.y >= maximum.y:
                rvy = maximum.y
            if self.y <= minimum.y:
                rvy = minimum.y
            self.x, self.y = rvx, rvy
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
