import Rectangle

class Surface:
  def __init__(self, filename, x, y, h, w):
    '''
      initializes Surface object by utilizing Rectangle object

      filename (string): name of file
      x (int): x value of rectangle (positive)
      y (int): y value of rectangle (positive)
      height (int): height of rectangle (positive)
      width (int): width of rectangle (positive)

      return: None
    '''
    self.rect = Rectangle.Rectangle(x, y, h, w)
    self.image = filename

  def getRect(self):
    '''
      Returns Rectangle object of Surface object

      return: (Rectangle)
    '''
    return self.rect