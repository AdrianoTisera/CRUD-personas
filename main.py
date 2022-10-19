class Persona:
    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre 
        self.apellido=apellido
        self.dni=dni 

class PersonaService:
    def __init__(self):
        self.personas=[]
    
    def add(self,a): 
        self.personas.append(a)
        
    def delete(self,a):
        self.personas.remove(a)
     
    def update(self,act,new):
        for i in range(len(self.personas)):
            if act.dni == self.personas[i].dni:
                self.personas[i] = new

    def findByDNI(self,a):
        for i in range(len(self.personas)):
            if self.personas[i].dni == a:
                return self.personas[i]
        
    def seeAll(self):
        return self.personas

    def loadFile(self):
        f = open("personas.txt","r")
        for line in f:
            self.personas.append(Persona(line.split(",")[0],line.split(",")[1],line.split(",")[2]))
        f.close()
    
    def saveFile(self):
        f = open("personas.txt","w")
        for i in range(len(self.personas)):
            f.write(self.personas[i].nombre+","+self.personas[i].apellido+","+self.personas[i].dni)
        f.close()