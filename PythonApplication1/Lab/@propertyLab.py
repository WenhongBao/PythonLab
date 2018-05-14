class Screen(object):
    def _init_(self,width,height,area):
        self.width = width
        self.height = height
        self.area = area

    @property
    def width(self):
        return self._birth

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('width must be an integer!')
        if value < 10:
            raise ValueError('width must be greater than 10')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('height must be an integer!')
        if value < 10:
            raise ValueError('height must be greater than 10')
        self._height = height

    @property
    def area(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.area)
assert s.area == 786432,'1024*768=%d ?' % s.area;