class Numero:
    VALID_NUMER = (int,float)
    ERROR_TEXT = "El valor debe ser un numero"
    def __init__(self,x , y):
        self.x = x
        self.y = y

    def validate(self, value):
      if not isinstance(value,self.VALID_NUMER):
          raise ValueError(self.ERROR_TEXT)
      return value
    
    @property
    def x(self):
      return self._x
    
    @x.setter
    def x(self,x):
      self._x = self.validate(x)

    @property
    def y(self):  
      return self._y
    
    @y.setter
    def y(self,y):
      self._y = self.validate(y)

    def suma(self):
      return self._x + self._y
    @classmethod
    def multiplica(cls,x,y):
        return x * y
    
    @staticmethod
    def restar(a,b):
      return a - b
    


try:
    num = Numero(3,4)
    print("Suma: ", num.suma())
    print("Resta: ", num.restar(20,2))
    print("Multi: ", Numero.multiplica(2,4))
except ValueError as error:
    print("Error: ", error)