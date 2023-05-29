class Car:
    color=None
def change_color(car,color):#here the object has been used as the arugment for this function
    car.color=color
car1=Car()
print(car1.color)
#now after the callig the function chnage_color
change_color(car1,"red")
print(car1.color)