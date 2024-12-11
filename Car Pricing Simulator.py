class car_show_room:
    def __init__(self):
        self.cgst=5555
        self.sgst=4444
        self.insurance=6666
        
    def company(self,name):
        while True:
            name=input("select the company : ") 
            if name=="audi":
                print("welcome to ",name,"company")
                self.f=name
                break
            elif name=="tata":
                self.f=name
                print("welcome to ",name,"company")
                break
            elif name=="mahendhra":
                self.f=name
                print("welcome to ",name,"company")
                break
            else:
                print(" try again , choose the above companies")
            
        
        
    def model(self,m):
       
            models=[["ax","bx"],["crysta","innova"],["thar","xuv"]]
        
            if m=="audi":
                print("select the model in ",m,"company")
                print(models[0])
                
            
            elif m=="tata":
                print("select the model in ",m,"company")
                print(models[1])
                
            
            elif m=="mahendhra" :
                print("select the model in ",m,"company")
                print(models[2])
                
            
            
                
    def price(self,p):
        while True:
            p = input("enter  model : ")
            
            if p=="ax":
                ax=250000
                print("ax price is ",ax)
                tprice=self.cgst+self.sgst+self.insurance+ax
                print("the onroad price of ax is : ",tprice)
                break
                
            elif p=="bx":
                bx=40000000
                print("bx price is ",bx)
                tprice=self.cgst+self.sgst+self.insurance+bx
                print("the onroad price of bx is : ",tprice)
                break
                
            elif p=="crysta":
                crysta=5666778
                print("crysta price is ",crysta)
                tprice=self.cgst+self.sgst+self.insurance+crysta
                print("the onroad price of crysta is : ",tprice)
                break
            
            elif p=="innova":
                innova=6000000
                print("innova price is ",innova)
                tprice=self.cgst+self.sgst+self.insurance+innova
                print("the onroad price of innova is : ",tprice)
                break
                
            elif p=="thar" :
                
                thar=999999
                print("thar price is ",thar)
                tprice=self.cgst+self.sgst+self.insurance+thar
                print("the onroad price of thar is : ",tprice)
                break
                
            elif p=="xuv":
                xuv=8899000
                print("xuv price is ",xuv)
                tprice=self.cgst+self.sgst+self.insurance+xuv
                print("the onroad price of xuv is : ",tprice)
                break
                
            else:
                print("enter the correct model")
            
companies=["audi","tata","mahendhra"]
print(companies)      
n=input("select the company : ") 
o=car_show_room()
o.company(n)
o.model(n)
p=input("select the model : ")
o.price(p)