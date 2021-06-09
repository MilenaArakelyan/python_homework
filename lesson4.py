class People:
    def _init_(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age
    
    def add_age(self,age):
        self.age += age
        return self.age
    
    def __repr__(self):
        return self.name
        
class Worker(People):
    def _init_ (self,name,last_name,age,workplace):
        super()._init_(name, last_name, age)  
        
        
worker = Worker ("Victor","Hambardzumyan",110,"atronom")
print(worker.add_age(3))
print (worker.age)



