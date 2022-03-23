class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2*(self.width + self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(int(self.height)):
        picture += "*" * int(self.width) + "\n"

      return picture

  def get_amount_inside(self, o_shape):
    return int(self.height/o_shape.height) * int(self.width/o_shape.width)

  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):
  def __init__(self,side_length):
    Rectangle.__init__(self, side_length, side_length)

  def set_side(self, side_length):
    self.set_width(side_length)
    self.set_height(side_length)

  def __str__(self):
    return "Square(side="+str(self.width)+")"


rect =  Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())


rect.set_height(8)
rect.set_width(16)

print(rect.get_amount_inside(sq))