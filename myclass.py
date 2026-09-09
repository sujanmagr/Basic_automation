# class intro:
#     name="sachin"
#     age=34

#     def display_name(self ,name):
#         print("my name is ", name)

# obj=intro()
# print(obj.age)
# print(obj.name)

# obj.display_name("sachin")


class car:
    def __init__(self, brand, color):
        self.brand=brand
        self.color=color


    def print_brand(self):
        print("the brand is", self.brand)

    def print_color(self):
        print("The color is ", self.color)
car1=car("toyota", "red")
car2=car("honda", "white")
car1.print_brand()
car1.print_color()
car2.print_brand()
car2.print_color()