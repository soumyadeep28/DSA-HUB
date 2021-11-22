class Employee:
    __Compname = None
    __ID = 000
    __Salary = 100

    def set_name(self , name):
        self.__Compname = name

    def get_name(self):
        return self.__Compname

    #constructure
    def __init__(self , name , id , sal):
        self.__Compname = name
        self.__ID = id
        self.__Salary = sal

# harry = Employee()
# harry.set_name("Amaazon")
# print(harry.get_name())

harry = Employee("flipkart" , 10 , 18800)
print(harry.get_name())