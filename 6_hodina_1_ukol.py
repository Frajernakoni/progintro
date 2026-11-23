class Rectangle:
   def __init__(self,width,height):
      self.widht = width
      self.height = height
   def area(self):
      w= self.widht
      h= self.height
      area= w*h
      return(area)
   def perimeter(self):
      w= self.widht
      h= self.height
      perimeter=2*(w+h)
      return(perimeter)
   def is_square(self):
       w= self.widht
       h= self.height
       if w==h:
          is_square=True
          return(is_square)
       else: 
          is_square=False
          return(is_square)
   def scale(self,factor=2):
       self.factor=factor
       w= self.widht*factor
       h= self.height*factor
       print("x=",w)
       print("y=",h)
       return("")
   def describe(self):
       w= self.widht
       h= self.height      
       return("Obdelník",w,"x",h,"obsah",self.area())
rec= Rectangle(10,5)   
print(rec.area())
print(rec.perimeter())
print(rec.is_square())      
print(rec.scale())
print(rec.describe())