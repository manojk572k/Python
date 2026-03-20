# drill
# class Car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def show_details(self):
#         print("Brand",self.brand," Price",self.price)
#
# p1 = Car("Tesla",50000)
# p2=Car("Tesla", 50000)
# p3=Car("BMW", 60000)
#
# p1.show_details()
# p2.show_details()
# p3.show_details()

# class variable vs instance variable
# class Student:
#     school="UNT"
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def show(self):
#         print("Name",self.name," Grade",self.grade,":",self.school)
#
# p1 = Student("Manoj","A")
# p1.show()

# Inheritance
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def show_brand(self):
        print("Brand",self.brand)
class Car(Vehicle):
    def __init__(self,brand,price):
        super().__init__(brand)
        self.price=price
    def show_details(self):
        print("Brand",self.brand," Price",self.price)

c= Car("Tesla",50000)

c.show_brand()
c.show_details()
