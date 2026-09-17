class Vehicle:
    def toll(self,per):
        return 0

class twowheeler(Vehicle):
    def toll(self,per):
        amount =20
        if(persons >2):
            amount= amount +(persons- 2) *10
        return amount

class threewheeler(Vehicle):
    def toll(self, per):
        amount = 30

        if(persons>3):
            amount= amount +(persons- 3) *20
        return amount

class fourwheeler(Vehicle):
    def toll(self, per):
        amount = 40
        if(persons>4):
            amount= amount + (persons- 4) *40
        return amount


class heavyvehicle(Vehicle):
    def toll(self, per):
        amount = 60

        if (per> 6):
            amount = amount + (persons - 6) *100
        return amount

while(True):

    print("\n1. two wheeler")
    print("2. three wheeler")
    print("3. four wheeler")
    print("4. heavy vehicle")
    print("5. exit")
    choice = int(input("enter choice: "))

    if(choice == 5):
        break

    persons = int(input("Enter number of persons: "))

    if(choice ==1):
        v = twowheeler()
    elif(choice ==2):
        v = threewheeler()
    elif(choice == 3):
        v = fourwheeler()
    elif(choice == 4):
        v = heavyvehicle()
    else:
        print("invalid choice")
        continue

    print("total toll =", v.toll(persons))
