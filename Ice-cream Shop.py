class Cost:
    price:float

    def __init__(self,price):
        self.price = price

    def setPrice(self,price:float):
        self.price = price

    def getPrice(self):
        return self.price

class Ice_Cream_Type(Cost):
    type_name:str

    def __init__(self,Name:str,price:float):
        self.type_name = Name
        self.setPrice(price)

    def getName(self):
        return self.type_name
        
class Ice_Cream_Flavour(Cost):
    flavour_name:str

    def __init__(self,Flav:str,price:float):
        self.flavour_name = Flav
        self.setPrice(price)

    def getFlav(self):
        return self.flavour_name

class Toppings(Cost):
    topping_name:str

    def __init__(self,Topping:str,price:float):
        self.topping_name = Topping
        self.setPrice(price)

    def getTopping(self):
        return self.topping_name

class Shop:
    flavors = []
    types = []
    toppings = []
    flav_choice :int
    type_choice:int
    topping_choice:int
    quantity :int
    bill_amount : Cost

    def prepareMenu(self):
        self.flavors.append(Ice_Cream_Flavour("VANILLA",10))
        self.flavors.append(Ice_Cream_Flavour("CHOCOLATE",25))
        self.flavors.append(Ice_Cream_Flavour("STRAWBERRY",20))

        self.types.append(Ice_Cream_Type("STICK",10))
        self.types.append(Ice_Cream_Type("CUP",15))
        self.types.append(Ice_Cream_Type("CONE",20))

        self.toppings.append(Toppings("OREO CRUMBIES",20))
        self.toppings.append(Toppings("CHERRIES",35))
        self.toppings.append(Toppings("CHOCOLATE CHIPS",60))
        self.toppings.append(Toppings("FRUITY-FRUITY",10))

    def displayTypeMenu(self):
        print("\nWELCOME TO ICE-CREAM SHOP")
        print("ICE-CREAM TYPES")

        type_count = 1
        if(len(self.types)>0):
            for ic_type in self.types:
                print(type_count,".",ic_type.getName(),"(Rs.",ic_type.getPrice(),")")
                type_count +=1
        else:
            print("There is no Ice-Cream Types!!")

    def askTypeChoice(self):
        return int(input("Choose the Ice-Cream Type you want: "))
    
    def checkTypeChoice(self,Type_choice:int):
        if (Type_choice > len(self.types) or Type_choice <= 0):
            print("Invalid choice entered.Choose again")
            self.checkTypeChoice(self.askTypeChoice())
        else:
            self.type_choice = Type_choice

    def displayFlaveMenu(self):
        print("ICE-CREAM FLAVOURS")

        flav_count = 1
        if(len(self.flavors)>0):
            for ic_flav in self.flavors:
                print(flav_count,".",ic_flav.getFlav(),"(Rs.",ic_flav.getPrice(),")")
                flav_count +=1
        else:
            print("There is no Ice-Cream Flavors!!")

    def askFlavChoice(self):
        return int(input("Choose the Ice-Cream Flavor you want: "))
    
    def checkFlavChoice(self,Flav_choice:int):
        if (Flav_choice > len(self.flavors) or Flav_choice <= 0):
            print("Invalid choice entered.Choose again")
            self.checkFlavChoice(self.askFlavChoice())
        else:
            self.flav_choice = Flav_choice


    def displayToppingMenu(self):
        if(self.flav_choice == 2):
            print("Toppings available for ", self.flavors[self.flav_choice -1].getFlav(),"ice-cream\n")

            topping_count = 1
            if(len(self.toppings)>0):
                for ic_top in self.toppings:
                    print(topping_count,".",ic_top.getTopping(),"(Rs.",ic_top.getPrice(),")")
                    topping_count +=1
            else:
                print("There are no toppings available for chocolate ice-cream!!")

    def askTopChoice(self):
        return int(input("Choose the Topping you want: "))
    
    def checkTopChoice(self,Top_choice:int):
        if (Top_choice > len(self.toppings) or Top_choice <= 0):
            print("Invalid choice entered.Choose again")
            self.checkTopChoice(self.askTopChoice())
        else:
            self.top_choice = Top_choice

    def displayQuantity(self):
        print("ICE-CREAM QUANTITY")

        if(self.flav_choice==2):
            print("You have chosen",self.types[self.type_choice-1].getName(),"type!")
            print("You have chosen",self.flavors[self.flav_choice-1].getFlav(),"flavor!")
            print("You have chosen",self.toppings[self.topping_choice-1].getTopping(),"topping!")
        else:
            print("You have chosen",self.types[self.type_choice-1].getName(),"type!")
            print("You have chosen",self.flavors[self.flav_choice-1].getFlav(),"flavor!")
    
    def askQuantity(self):
                return int(input("\nhow many ice-cream do you want: "))
    
    def checkQuantity(self,Quanchoice:int):
        if (Quanchoice <= 0):
            print("Invalid quantity entered.Choose again")
            self.checkQuantity(self.askQuantity())
        else:
            self.quantity = Quanchoice

    def calculateBillAmount(self):
        if(self.flav_choice==2):
            flav_amt = self.flavors[self.flav_choice-1].getPrice()
            type_amt = self.types[self.type_choice-1].getPrice()
            top_amt = self.toppings[self.topping_choice-1].getPrice()
            amt = (flav_amt+type_amt+top_amt) * self.quantity
            self.bill_amount = Cost(round(amt,2))
        else:
            flav_amt = self.flavors[self.flav_choice-1].getPrice()
            type_amt = self.types[self.type_choice-1].getPrice()
            amt = (flav_amt+type_amt) * self.quantity
            self.bill_amount = Cost(round(amt,2))

    def showBill(self):
        if(self.flav_choice == 2):
            print("BILL")
            
            print("Ice-cream Type           : ",self.types[self.type_choice-1].getName())
            print("Ice-cream Type Cost      : Rs.",self.types[self.type_choice-1].getPrice())

            print("Ice-cream Flavor         : ",self.flavors[self.flav_choice-1].getFlav())
            print("Ice-cream Flavor Cost    : Rs.",self.flavors[self.flav_choice-1].getPrice())

            print("Ice-cream Topping        : ",self.toppings[self.type_choice-1].getTopping())
            print("Ice-cream Topping Cost   : Rs.",self.toppings[self.type_choice-1].getPrice())

            print("Quantity                 : ",self.quantity)

            print("Amount To Pay =","(",self.types[self.type_choice-1].getPrice(),"+",self.flavors[self.flav_choice-1].getPrice(),"+",self.toppings[self.top_choice-1].getPrice(),") x ",self.quantity," = Rs.",self.bill_amount.getprice())

        else:
            print("BILL")
            
            print("Ice-cream Type           : ",self.types[self.type_choice-1].getName())
            print("Ice-cream Type Cost      : Rs.",self.types[self.type_choice-1].getPrice())

            print("Ice-cream Flavor         : ",self.flavors[self.flav_choice-1].getFlav())
            print("Ice-cream Flavor Cost    : Rs.",self.flavors[self.flav_choice-1].getPrice())

            print("Quantity                 : ",self.quantity)

            print("Amount To Pay =","(",self.types[self.type_choice-1].getPrice(),"+",self.flavors[self.flav_choice-1].getPrice(),") x ",self.quantity," = Rs.",self.bill_amount.getPrice())

shopobj = Shop()
shopobj.prepareMenu()

shopobj.displayTypeMenu()
shopobj.checkTypeChoice(shopobj.askTypeChoice())

shopobj.displayFlaveMenu()
shopobj.checkFlavChoice(shopobj.askFlavChoice())

if(shopobj.flav_choice==2):
    shopobj.displayToppingMenu()
    shopobj.checkTopChoice(shopobj.askTopChoice())

    shopobj.displayQuantity()
    shopobj.checkQuantity(shopobj.askQuantity())

    shopobj.calculateBillAmount()
    shopobj.showBill()

else:
    shopobj.displayQuantity()
    shopobj.checkQuantity(shopobj.askQuantity())

    shopobj.calculateBillAmount()
    shopobj.showBill()
            
