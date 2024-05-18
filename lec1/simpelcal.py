# Klass add

class Add:
    def __init__(self, tal1, tal2):
        self.tal1=tal1
        self.tal2=tal2

    #skapa en metod 
    def cal(self):
        return tal1 + tal2
    
#ta input från user
tal1=int(input("Ange tal1: "))
tal2=int(input("Ange tal2: "))

#Skapa ett objekt av klassen Add
add1=Add(tal1,tal2)

res=add1.cal()

print(res)