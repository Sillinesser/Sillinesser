# class Polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class pramokutnyk(Polygon):
#     def __init__(self):
#         Polygon.__init__(self,4)

#     def findArea(self):
#         a,b,c,d = self.sides
#         print("The area of pramokutnyk", a*b)
# t = pramokutnyk()
# t.inputSides()
# t.findArea()





# class Auto:
#     def __init__(self, name, made, model):
#         self.name = name
#         self.made = made
#         self.model = model
    
#     def start(self):
#         print(f"You car {self.name} is made in {self.made} model {self.model} is started")
    
#     def stop(self):
#         print(f"You car {self.name} is made in {self.made} model {self.model} is stoped")

# car1 = Auto("Tesla", "USA", "X")
# car2 = Auto("VW", "Germany", "Passat b32")
# car1.stop()
# car2.start()





class Person:
    