class CarFactory():
    def __init__(self,brand,model,year,hoursepower,piston,is_there_turbo) -> None:
        self.brand = brand
        self.model = model 
        self.year = year
        self.hoursepower = hoursepower
        self.piston = piston
        self.is_there_turbo = is_there_turbo
    def __str__(self) -> str:
        title = "Your model car here:"
        brand = "title: "+self.brand
        model =  "model: "+self.model
        year = "year: "+str(self.year)
        hoursepower = "hoursepower: "+str(self.hoursepower)+" watt"
        piston = "piston: "+str(self.piston)
        is_there_turbo = "Turbo: "+str(self.is_there_turbo)
        return f"{title}\n{brand}\n{model}\n{year}\n{hoursepower}\n{piston}\n{is_there_turbo}\n"
    
obj1 = CarFactory("Benz","E-3",2022,240,24,True)
print(obj1)