import unittest
from main import Persona,PersonaService


class TestPersonas(unittest.TestCase):
    def test_add(self):
        persona1 = Persona("Elon","Musk","1")
        persona2 = Persona("Linus","Torvalds","2")
        persona3 = Persona("Tony","Stark","3")
        personaservice = PersonaService()
        personaservice.add(persona1)
        personaservice.add(persona2)
        personaservice.add(persona3)
        self.assertEqual(personaservice.personas[0].nombre,"Elon")
        self.assertEqual(personaservice.personas[1].nombre,"Linus")
        self.assertEqual(personaservice.personas[2].nombre,"Tony")

    
    def test_delete(self):
        persona = Persona("Linus","Torvalds","2")
        personaservice = PersonaService()
        personaservice.add(persona)
        personaservice.delete(persona)
        self.assertEqual(personaservice.personas,[])
    
    def test_update(self):
        persona = Persona("Elon","Musk","1")
        personaservice = PersonaService()
        personaservice.add(persona)
        self.assertEqual(personaservice.personas[0].nombre,"Elon")
        personaservice.update(persona,Persona("Tony","Stark","1"))
        self.assertEqual(personaservice.personas[0].nombre,"Tony")
    
    def test_findByDNI(self):
        persona1 = Persona("Elon","Musk","1")
        persona2 = Persona("Linus","Torvalds","2")
        persona3 = Persona("Tony","Stark","3")
        personaservice = PersonaService()
        personaservice.add(persona1)
        personaservice.add(persona2)
        personaservice.add(persona3)
        self.assertEqual(personaservice.findByDNI("1"), persona1)
        self.assertEqual(personaservice.findByDNI("2"), persona2)
        self.assertEqual(personaservice.findByDNI("3"), persona3)
        self.assertEqual(personaservice.findByDNI("4"), None)
    
    def test_seeAll(self):
        persona1 = Persona("Elon","Musk","1")
        persona2 = Persona("Linus","Torvalds","2")
        persona3 = Persona("Tony","Stark","3")
        personaservice = PersonaService()
        personaservice.add(persona1)
        personaservice.add(persona2)
        personaservice.add(persona3)
        self.assertEqual(personaservice.seeAll(), [persona1,persona2,persona3])

if __name__ == '__main__':
    unittest.main()