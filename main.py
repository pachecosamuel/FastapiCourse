import pydantic

class Person:
    nome: str
    
    def get_name(name: str):
        return name
    

print(Person.get_name("samuca"))